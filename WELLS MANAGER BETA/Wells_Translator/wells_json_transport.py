# -*- coding: utf-8 -*-
"""Clean line transport and map validation helpers for Ren'Py JSON strings."""
from __future__ import annotations

import hashlib
import re

MAP_FILENAME = "wells_json_translation_map.json"
MAP_SCHEMA = "wells-json-translation-map"
MAP_VERSION = 1


def split_protected(text: str):
    """Return Ren'Py [...] / {...} tokens without their contents being edited."""
    text = str(text)
    parts, buffer = [], []
    i = 0

    def flush():
        if buffer:
            parts.append((False, "".join(buffer)))
            buffer.clear()

    while i < len(text):
        opener = text[i]
        if opener not in "[{":
            buffer.append(opener)
            i += 1
            continue
        flush()
        closer = "]" if opener == "[" else "}"
        depth, j = 1, i + 1
        while j < len(text) and depth:
            if text[j] == opener:
                depth += 1
            elif text[j] == closer:
                depth -= 1
            j += 1
        if depth:
            parts.append((True, text[i:]))
            i = len(text)
        else:
            parts.append((True, text[i:j]))
            i = j
    flush()
    return parts


def mask_text(value: str):
    """Hide Ren'Py tokens and literal double quotes in a clean translation row."""
    out, protected, quote_count = [], [], 0
    for is_protected, part in split_protected(value):
        if is_protected:
            out.append(f"[[WELLS_P_{len(protected):06d}]]")
            protected.append(part)
            continue
        for char in part:
            if char == '"':
                out.append(f"[[WELLS_Q_{quote_count:06d}]]")
                quote_count += 1
            else:
                out.append(char)
    return "".join(out), protected, quote_count


def encode_transport(value: str):
    masked, protected, quote_count = mask_text(str(value))
    escaped = (masked.replace("\\", "\\\\")
               .replace("\r", "\\r")
               .replace("\n", "\\n")
               .replace("\t", "\\t"))
    return escaped, protected, quote_count


def decode_escapes(value: str):
    value = str(value)
    out, i = [], 0
    while i < len(value):
        if value[i] != "\\" or i + 1 >= len(value):
            out.append(value[i])
            i += 1
            continue
        nxt = value[i + 1]
        decoded = {"\\": "\\", "n": "\n", "r": "\r", "t": "\t"}.get(nxt)
        if decoded is None:
            out.extend(("\\", nxt))
        else:
            out.append(decoded)
        i += 2
    return "".join(out)


def restore_transport(value: str, protected, quote_count: int, record: int, label: str):
    value = decode_escapes(value)
    found_p = re.findall(r"\[\[WELLS_P_\d{6}\]\]", value)
    expected_p = [f"[[WELLS_P_{i:06d}]]" for i in range(len(protected))]
    found_q = re.findall(r"\[\[WELLS_Q_\d{6}\]\]", value)
    expected_q = [f"[[WELLS_Q_{i:06d}]]" for i in range(int(quote_count))]
    if found_p != expected_p:
        raise ValueError(f"Marcadores Ren'Py alterados em {label}, registro {record}.")
    if found_q != expected_q:
        raise ValueError(f"Aspas protegidas alteradas em {label}, registro {record}.")
    for marker, token in zip(expected_p, protected):
        value = value.replace(marker, token)
    for marker in expected_q:
        value = value.replace(marker, '"')
    return value


def sha256_text(value: str):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

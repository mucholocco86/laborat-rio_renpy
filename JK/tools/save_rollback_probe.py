#!/usr/bin/env python3
"""Read-only probe for Ren'Py save checkpoint identifiers vs compiled scripts."""
from __future__ import annotations
import json
import pickletools
import struct
import zlib
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
GAME = ROOT / "JOGOS PARA TESTES" / "GrandmasHouse-0.95-pc" / "game"
SAVE_NAMES = ("1-1-LT1.save", "1-2-LT1.save", "1-3-LT1.save", "10-1-LT1.save", "10-2-LT1.save", "10-3-LT1.save", "13-2-LT1.save", "13-4-LT1.save", "13-5-LT1.save")
RPYC_HEADER = b"RENPY RPC2"
MEMO_OPS = {"BINPUT", "LONG_BINPUT", "PUT", "MEMOIZE"}


def triplets(payload: bytes) -> set[tuple[str, int, int]]:
    """Extract direct tuple3 identifiers without executing pickle payloads."""
    result: set[tuple[str, int, int]] = set()
    try:
        ops = list(pickletools.genops(payload))
    except Exception:
        return result

    for i, (op, _arg, _pos) in enumerate(ops):
        if op.name != "TUPLE3":
            continue
        values = []
        j = i - 1
        while j >= 0 and len(values) < 3:
            prev_op, prev_arg, _ = ops[j]
            if prev_op.name in MEMO_OPS:
                j -= 1
                continue
            values.append((prev_op.name, prev_arg))
            j -= 1
        if len(values) != 3:
            continue
        values.reverse()
        first, second, third = values
        string_ops = {"STRING", "BINSTRING", "SHORT_BINSTRING", "UNICODE",
                      "BINUNICODE", "SHORT_BINUNICODE", "BINUNICODE8"}
        int_ops = {"INT", "BININT", "BININT1", "BININT2", "LONG", "LONG1", "LONG4"}
        if (first[0] in string_ops and second[0] in int_ops and third[0] in int_ops
                and isinstance(first[1], str) and isinstance(second[1], int)
                and isinstance(third[1], int)):
            filename = first[1].replace("\\", "/")
            if filename.endswith((".rpy", ".rpym")):
                result.add((filename, second[1], third[1]))
    return result


def save_identifiers(path: Path):
    with ZipFile(path) as archive:
        return triplets(archive.read("log"))


def rpyc_payloads(path: Path):
    data = path.read_bytes()
    if not data.startswith(RPYC_HEADER):
        return
    pos = len(RPYC_HEADER)
    while pos + 12 <= len(data):
        slot, start, length = struct.unpack_from("III", data, pos)
        if slot == 0:
            break
        if start + length <= len(data):
            try:
                yield slot, zlib.decompress(data[start:start + length])
            except zlib.error:
                pass
        pos += 12


def compiled_identifiers():
    result = {}
    for path in sorted(GAME.rglob("*.rpyc")):
        rel = path.relative_to(GAME).as_posix()
        source_name = "game/" + rel[:-1]
        found = set()
        for _slot, payload in rpyc_payloads(path) or ():
            found.update(triplets(payload))
        if found:
            result[source_name] = found
    return result


def main():
    compiled = compiled_identifiers()
    report = {
        "scope": "read-only pickle opcode and RPYC identifier comparison; not a runtime load test",
        "game_directory_present": GAME.is_dir(),
        "compiled_files_with_identifiers": len(compiled),
        "compiled_file_details": {name: {"identifier_count": len(ids), "versions": {str(version): sorted(serial for _filename, found_version, serial in ids if found_version == version) for version in sorted({found_version for _filename, found_version, _serial in ids})}} for name, ids in sorted(compiled.items())},
        "saves": [],
        "warnings": [],
    }
    for name in SAVE_NAMES:
        path = GAME / "saves" / name
        if not path.is_file():
            report["warnings"].append("Save not found: " + name)
            continue
        saved = save_identifiers(path)
        by_file = {}
        for filename, version, serial in sorted(saved):
            exact = (filename, version, serial) in compiled.get(filename, set())
            by_file.setdefault(filename, {"saved_identifiers": 0, "exact_matches": 0})
            by_file[filename]["saved_identifiers"] += 1
            by_file[filename]["exact_matches"] += int(exact)
        unmatched = [
            {"file": f, "compiled_version": v, "serial": s}
            for f, v, s in sorted(saved)
            if (f, v, s) not in compiled.get(f, set())
        ]
        report["saves"].append({
            "name": name,
            "identifier_count": len(saved),
            "matched_identifiers": len(saved) - len(unmatched),
            "unmatched_count": len(unmatched),
            "files": by_file,
            "unmatched_identifiers": unmatched,
            "saved_versions_by_file": {name: {str(version): {"saved_serials": sorted(serial for _filename, found_version, serial in saved if _filename == name and found_version == version), "compiled_serials": sorted(serial for _filename, found_version, serial in compiled.get(name, set()) if found_version == version)} for version in sorted({v for f, v, _s in saved if f == name})} for name in sorted({f for f, _v, _s in saved})},
        })
        print("{}: {} identifiers, {} exact matches, {} unmatched".format(
            name, len(saved), len(saved) - len(unmatched), len(unmatched)))

    out = ROOT / "save-rollback-probe"
    out.mkdir(exist_ok=True)
    (out / "save-rollback-probe.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    lines = [
        "# Grandma's House - rollback identifier probe",
        "",
        "Static analysis only: pickle data was not executed and game files were not modified.",
        "This is diagnostic evidence, not a runtime load test.",
        "",
        "- Compiled RPYC files with extracted identifiers: " + str(len(compiled)),
        "",
    ]
    for save in report["saves"]:
        lines += ["## " + save["name"], "",
                  "- Identifiers extracted: " + str(save["identifier_count"]), ""]
        if not save["files"]:
            lines.append("No direct identifiers could be associated with a source file.")
        else:
            lines += ["| File | IDs in save | Exact matches in RPYC |",
                      "|---|---:|---:|"]
            for filename, values in sorted(save["files"].items()):
                lines.append("| " + filename + " | " + str(values["saved_identifiers"])
                             + " | " + str(values["exact_matches"]) + " |")
        lines.append("")
    if report["warnings"]:
        lines += ["## Warnings", ""] + ["- " + w for w in report["warnings"]] + [""]
    lines += [
        "## Interpretation",
        "",
        "The JSON report includes the actual extracted RPYC identifiers and per-save compiled versions to diagnose parser or path mismatches.",
        "Missing matches may indicate that compiled scripts were regenerated or changed after the save was created.",
        "Ren'Py can preserve identifiers during recompilation when the previous RPYC is available.",
        "This report does not recommend automatic identifier remapping, which could resume at a different statement.",
        "",
    ]
    (out / "save-rollback-probe.md").write_text("\n".join(lines), encoding="utf-8")
    print("Save rollback identifier probe completed.")
    print("Report:", out / "save-rollback-probe.md")


if __name__ == "__main__":
    main()

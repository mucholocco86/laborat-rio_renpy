################################################################################
## Choice tracker — BlueFox.au v1.2.0
################################################################################
##
## Adds a small dot to menu options the player has previously picked at
## the same menu. The dot is optional and can be toggled in the Stats tab.
##
################################################################################

default persistent.cx_show_marker = False
default persistent.cx_seen_choices = None
default persistent.cx_choices_total = 0
default cx_choice_history = []

init -5 python:

    import hashlib as _cx_hashlib
    import importlib as _cx_importlib
    import time as _cx_time

    def _cx_script():
        return _cx_importlib.import_module("renpy.game").script

    def cx_marker_on():
        return bool(persistent.cx_show_marker)

    def _cx_seen_bank():
        bank = persistent.cx_seen_choices
        if not isinstance(bank, set):
            bank = set(bank) if bank else set()
        return bank

    def _cx_seen_bank_save(bank):
        persistent.cx_seen_choices = bank

    def _cx_hash12(raw):
        return _cx_hashlib.md5((raw or u"").encode("utf-8", "replace")).hexdigest()[:12]

    def _cx_here():
        try:
            fn, ln = renpy.get_filename_line()
            fn = (fn or u"").replace(u"\\", u"/")
            ln = int(ln or 0)
            return fn, ln
        except Exception:
            return u"", 0

    def _cx_menus_for_file(fn):
        base = (fn or u"").replace(u"\\", u"/").split(u"/")[-1]
        cache = getattr(_cx_menus_for_file, "_cache", None)
        if cache is None:
            cache = {}
            _cx_menus_for_file._cache = cache

        rows = cache.get(base)
        if rows is not None:
            return rows

        rows = []
        try:
            for node in _cx_script().all_stmts:
                if node.__class__.__name__ != "Menu":
                    continue
                nfn = (getattr(node, "filename", u"") or u"").replace(u"\\", u"/")
                if nfn.split(u"/")[-1] != base:
                    continue
                nln = int(getattr(node, "linenumber", 0) or 0)
                rows.append((nln, node))
            rows.sort(key=lambda it: it[0])
        except Exception:
            rows = []

        cache[base] = rows
        return rows

    def _cx_current_menu_node(fn, ln):
        rows = _cx_menus_for_file(fn)
        if not rows:
            return None

        for nln, node in rows:
            if nln == ln:
                return node

        prev = None
        for nln, node in rows:
            if nln <= ln:
                prev = (nln, node)
            else:
                break
        if prev is not None:
            return prev[1]

        return rows[0][1]

    def _cx_menu_fingerprint(node):
        if node is None:
            return u""
        caps = []
        try:
            for cap, _cond, _block in node.items:
                if cap:
                    caps.append(cap)
        except Exception:
            return u""
        return u"\x1f".join(caps)

    def cx_choice_key_legacy(caption, fn=None, ln=None):
        if fn is None or ln is None:
            fn, ln = _cx_here()
        raw = u"{}:{}:{}".format(fn or u"", int(ln or 0), caption or u"")
        return _cx_hash12(raw)

    def cx_choice_key_stable(caption, fn=None, ln=None):
        if fn is None or ln is None:
            fn, ln = _cx_here()
        base = (fn or u"").replace(u"\\", u"/").split(u"/")[-1]
        menu = _cx_current_menu_node(fn, int(ln or 0))
        if menu is None:
            return cx_choice_key_legacy(caption, fn=fn, ln=ln)

        menu_ln = int(getattr(menu, "linenumber", 0) or 0)
        label = _cx_nearest_label(fn, menu_ln) or u""
        menu_sig = _cx_menu_fingerprint(menu)
        raw = u"v2:{}:{}:{}:{}".format(base, label, menu_sig, caption or u"")
        return _cx_hash12(raw)

    def cx_choice_key(caption):
        return cx_choice_key_stable(caption)

    def _cx_choice_keys(caption):
        fn, ln = _cx_here()
        old_key = cx_choice_key_legacy(caption, fn=fn, ln=ln)
        new_key = cx_choice_key_stable(caption, fn=fn, ln=ln)
        if old_key == new_key:
            return [new_key]
        return [new_key, old_key]

    def cx_is_seen(caption):
        if not cx_marker_on():
            return False
        try:
            orig_caption = _cx_untranslate(caption)
            bank = _cx_seen_bank()
            keys = _cx_choice_keys(orig_caption)
            seen = [k for k in keys if k in bank]
            if not seen:
                return False

            if len(keys) >= 2 and keys[1] in bank and keys[0] not in bank:
                bank.add(keys[0])
                _cx_seen_bank_save(bank)
            return True
        except Exception:
            return False

    def _cx_untranslate(caption):
        try:
            lang = getattr(renpy.store._preferences, "language", None)
            if not lang:
                return caption

            strings_obj = renpy.game.script.translator.strings.get(lang)
            if not strings_obj:
                return caption

            for orig, trans in strings_obj.translations.items():
                if trans == caption:
                    return orig
        except Exception:
            pass

        return caption

    def _cx_label_index(fn):
        base = (fn or u"").replace(u"\\", u"/").split(u"/")[-1]
        cache = getattr(_cx_label_index, "_cache", None)
        if cache is None:
            cache = {}
            _cx_label_index._cache = cache
        idx = cache.get(base)
        if idx is None:
            items = None
            for _attempt in range(3):
                try:
                    items = list(_cx_script().namemap.items())
                    break
                except Exception as e:
                    _cx_label_index._last_error = repr(e)
                    items = None
            if items is None:
                return []
            try:
                idx = []
                for name, node in items:
                    if not isinstance(name, str) or name.startswith(u"_"):
                        continue
                    nfn = (getattr(node, "filename", u"") or u"").replace(u"\\", u"/")
                    if nfn.split(u"/")[-1] == base:
                        idx.append((int(getattr(node, "linenumber", 0) or 0), name))
                idx.sort()
                cache[base] = idx
            except Exception as e:
                _cx_label_index._last_error = repr(e)
                return []
        return idx

    def _cx_nearest_label(fn, ln):
        best = u""
        for line, name in _cx_label_index(fn):
            if line <= ln:
                best = name
            else:
                break
        return best

    def cx_record_choice(caption):
        orig_caption = _cx_untranslate(caption)
        try:
            bank = _cx_seen_bank()
            for key in _cx_choice_keys(orig_caption):
                bank.add(key)
            _cx_seen_bank_save(bank)
        except Exception:
            pass
        try:
            persistent.cx_choices_total = int(persistent.cx_choices_total or 0) + 1
        except Exception:
            pass
        try:
            fn, ln = renpy.get_filename_line()
            fn = (fn or u"").replace(u"\\", u"/")
            ln = int(ln or 0)
        except Exception:
            fn, ln = (u"", 0)
        try:
            hist = list(store.cx_choice_history or [])
            hist.append({
                "fn": fn,
                "ln": ln,
                "caption": orig_caption,
                "ts": _cx_time.time(),
            })
            store.cx_choice_history = hist
        except Exception:
            pass

    def cx_history_for_display():
        try:
            hist = list(store.cx_choice_history or [])
        except Exception:
            return []
        out = []
        for item in hist:
            if not item.get("label"):
                try:
                    item = dict(item)
                    item["label"] = _cx_nearest_label(item.get("fn", u""), int(item.get("ln") or 0))
                except Exception:
                    pass
            out.append(item)
        return list(reversed(out))

    def cx_format_relative_time(ts):
        try:
            ts = float(ts or 0)
        except Exception:
            return u""
        if ts <= 0:
            return u""
        delta = _cx_time.time() - ts
        if delta < 60:
            return _("just now")
        if delta < 3600:
            return __("{} min ago").format(int(delta // 60))
        if delta < 86400:
            return __("{} hr ago").format(int(delta // 3600))
        return __("{} d ago").format(int(delta // 86400))

################################################################################
## Debug: export choice history to JSON.
##
## From the console (Shift+O):
##     cx_export()            -> exports the current session's history
##     cx_export("main-3")    -> exports history stored inside save slot main-3
##                               (slot names as in the save browser: main-3,
##                               auto-1, quick-1, ...)
################################################################################

init python:

    import json as _cx_json
    import os as _cx_os
    import re as _cx_re
    import subprocess as _cx_subprocess

    def _cx_slot_history(slot):
        log_data, _sig = renpy.loadsave.location.load(slot)
        roots, _log = renpy.loadsave.loads(log_data)
        hist = roots.get("store.cx_choice_history")
        if not isinstance(hist, list):
            return []
        return hist

    def _cx_menu_locations():
        m = {}
        try:
            for node in _cx_script().all_stmts:
                if node.__class__.__name__ != "Menu":
                    continue
                nfn = (getattr(node, "filename", u"") or u"").replace(u"\\", u"/")
                nln = int(getattr(node, "linenumber", 0) or 0)
                for cap, _cond, _block in node.items:
                    if cap:
                        m.setdefault(cap, []).append((nfn, nln))
        except Exception:
            pass
        return m

    def _cx_episode_from_fn(fn):
        base = (fn or u"").split(u"/")[-1]
        m = _cx_re.match(r"episode_(\d+)", base)
        if m:
            return __("Episode {}").format(m.group(1))
        if base.endswith(u".rpy"):
            return base[:-4]
        return base

    def _cx_order_key(loc):
        fn, ln = loc
        base = (fn or u"").split(u"/")[-1]
        m = _cx_re.match(r"episode_(\d+)", base)
        ep = int(m.group(1)) if m else 9999
        return (ep, ln)

    def _cx_resolve_entries(hist):
        menu_map = None
        out = []
        cursor = None
        for item in hist:
            caption = item.get("caption", u"")
            fn = (item.get("fn") or u"").replace(u"\\", u"/")
            ln = int(item.get("ln") or 0)
            if not fn:
                if menu_map is None:
                    menu_map = _cx_menu_locations()
                cands = sorted(menu_map.get(caption) or [], key=_cx_order_key)
                if cands:
                    if cursor is not None:
                        fn, ln = next(
                            (c for c in cands if _cx_order_key(c) >= cursor),
                            cands[-1])
                    else:
                        fn, ln = cands[0]
            if fn:
                cursor = _cx_order_key((fn, ln))
            label = item.get("label") or (_cx_nearest_label(fn, ln) if fn else u"")
            episode = _cx_episode_from_fn(fn) if fn else u""
            out.append((episode, label, caption))
        return out

    def cx_export(slot=None, fmt="json"):
        try:
            if slot is None:
                hist = list(store.cx_choice_history or [])
                source = u"session"
            else:
                hist = _cx_slot_history(slot)
                source = slot
        except Exception as e:
            msg = _("Exported {} choices -> {}").format(len(entries), path)
            renpy.notify(msg)
            print(msg)
            return None

        entries = []
        for item, resolved in zip(hist, _cx_resolve_entries(hist)):
            episode, label, caption = resolved
            try:
                ts = float(item.get("ts") or 0)
            except Exception:
                ts = 0
            entries.append({
                "episode": episode,
                "label": label,
                "caption": caption,
                "ts": ts,
                "time": _cx_time.strftime("%Y-%m-%d %H:%M:%S", _cx_time.localtime(ts)) if ts > 0 else u"",
            })

        fn = u"choice_export_{}_{}.{}".format(
            source.replace(u"/", u"_"),
            _cx_time.strftime("%Y%m%d-%H%M%S"),
            u"txt" if fmt == "txt" else u"json")
        path = _cx_os.path.join(renpy.config.savedir, fn)

        with open(path, "w", encoding="utf-8") as f:
            if fmt == "txt":
                f.write(__(u"Choice history ({}) - {} choice(s)\n\n").format(source, len(entries)))
                header = None
                for e in entries:
                    h = u"{} {}".format(e["episode"] or u"", e["label"] or u"")
                    if h != header:
                        f.write(u"{}\n".format(h))
                        header = h
                    f.write(u" - {}\n".format(e["caption"]))
            else:
                _cx_json.dump({
                    "source": source,
                    "exported": _cx_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "count": len(entries),
                    "choices": entries,
                }, f, ensure_ascii=False, indent=2)

        msg = __(u"Exported {} choices -> {}").format(len(entries), path)
        renpy.notify(msg)
        print(msg)
        return path

    def _cx_open_file(path):
        try:
            if renpy.windows:
                _cx_os.startfile(path)
            elif renpy.macintosh:
                _cx_subprocess.Popen(["open", path])
            else:
                _cx_subprocess.Popen(["xdg-open", path])
            return True
        except Exception as e:
            renpy.notify(_("Could not open file: {!r}").format(e))
            return False

    def cx_export_and_open(slot=None):
        path = cx_export(slot, fmt="txt")
        if path:
            _cx_open_file(path)
        return path

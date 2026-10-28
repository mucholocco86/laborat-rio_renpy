################################################################################
## Dev debug overlay -- BlueFox.au v1.2.0
################################################################################
##
## In-game debugging overlay. Press F8 in-game to toggle it.
##
## Panels:
##   * Debug Overlay (top left): current position, watched flags (green True,
##     white False, blue numbers), and a live feed of recent flag changes
##     (any variable defaulted in game/scripts/flag_defaults.rpy).
##   * Tabs inside the overlay (vars / replays / jump / actions):
##       vars     type-to-filter variable browser; click a row to pin it.
##                Arbitrary names can be pinned via "pin as typed".
##       replays  every pathtests/*.json with its latest report verdict;
##                click to re-run it (confirms first, restarts the game).
##       jump     type-to-filter label browser; click to jump to a label.
##       actions  snapshot / fast skip / reload / open pathtests folder.
##   * Watched variables can be edited inline: [t] toggles bools, [-] and
##     [+] adjust numbers by 1.
##   * Choice Effects (left, only while a choice menu is on screen): for every
##     option in the current menu, the flag assignments inside that option's
##     block ("+True", "+6", "-6"), pulled from the compiled script AST.
##
## Console helpers (Shift+O):
##   dd_watch("Layla_LikeMC")     pin a flag to the overlay
##   dd_unwatch("Layla_LikeMC")   unpin
##   dd_watch_clear()             unpin all
##
## Clicking a line in "Recent changes" pins that flag. Clicking the small [x]
## next to a watched flag unpins it. F7 saves a path-test snapshot (see
## dev_pathtest.rpy).
##
################################################################################

init python:
    class DevDebugState(NoRollback):
        def __init__(self):
            self.dd_overlay = False
            self.dd_watches = []
            self.dd_panel = None
            self.dd_routes_min = False
            self.dd_routes_expand = False
            self.dd_help = True
            
    dd_state = DevDebugState()

default dd_var_filter = ""

init -2 python:

    import re as _dd_re
    import os as _dd_os
    import json as _dd_json
    import importlib as _dd_importlib
    import sys

    if not hasattr(sys, "_dd_cache"):
        sys._dd_cache = {}

    def _dd_mod(name):
        return _dd_importlib.import_module(name)

    _DD_DEFAULT_RE = _dd_re.compile(r'^default\s+([A-Za-z_]\w*)\s*=')
    _DD_ASSIGN_RE = _dd_re.compile(r'^\$?\s*([A-Za-z_]\w*)\s*(\+=|-=|=)\s*(.+?)\s*$')
    _DD_IDENT_RE = _dd_re.compile(r'^[A-Za-z_]\w*$')
    _DD_IDENT_ANY_RE = _dd_re.compile(r'[A-Za-z_]\w*')
    
    def _dd_q(s):
        return (s or u"").replace(u"{", u"{{").replace(u"[", u"[[")

    def _dd_perf_throttle(name, interval=0.08):
        try:
            import time
            now = time.time()
            prev = sys._dd_cache.get(name)
            if prev is not None and now - prev < interval:
                return False
            sys._dd_cache[name] = now
            return True
        except Exception:
            return True

    def _dd_flag_universe():
        if "flag_universe" in sys._dd_cache:
            return sys._dd_cache["flag_universe"]
        names = []
        for sub in (u"scripts", u""):
            path = _dd_os.path.join(config.gamedir, sub, "flag_defaults.rpy")
            if not _dd_os.path.isfile(path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        m = _DD_DEFAULT_RE.match(line.strip())
                        if m and not m.group(1).startswith(u"_"):
                            names.append(m.group(1))
            except Exception:
                continue
            if names:
                break
        if not names:
            return names
        sys._dd_cache["flag_universe"] = names
        return names

    def dd_watch(name):
        lst = list(dd_state.dd_watches or [])
        if name not in lst:
            lst.append(name)
            dd_state.dd_watches = lst
        renpy.restart_interaction()

    def dd_unwatch(name):
        lst = [n for n in (dd_state.dd_watches or []) if n != name]
        dd_state.dd_watches = lst
        renpy.restart_interaction()

    def dd_watch_clear():
        dd_state.dd_watches = []
        renpy.restart_interaction()

    def dd_value_markup(v):
        if v is True:
            return u"{color=#5be353}True{/color}"
        if v is False:
            return u"{color=#e8e8e8}False{/color}"
        if v is None:
            return u"{color=#888888}unset{/color}"
        if isinstance(v, (int, float)):
            return u"{{color=#6fd3ff}}{}{{/color}}".format(v)
        return u"{{color=#6fd3ff}}{}{{/color}}".format(_dd_q(str(v))[:24])

    def _dd_tick():
        import sys
        if not dd_state.dd_overlay:
            return
        if renpy.predicting() or renpy.config.skipping or renpy.in_rollback():
            return
        if not _dd_perf_throttle("dd_tick", 0.05):
            return

        try:
            snap = {}
            for n in _dd_flag_universe():
                v = getattr(store, n, None)
                if isinstance(v, (bool, int, float, str)) or v is None:
                    snap[n] = v
                    
            prev = sys._dd_cache.get("dd_snap")
            
            if prev is not None and prev != snap:
                changes = list(sys._dd_cache.get("dd_changes", []))
                for n, v in snap.items():
                    if n in prev and prev[n] != v:
                        changes.append((n, prev[n], v))
                sys._dd_cache["dd_changes"] = changes[-8:]
                
            sys._dd_cache["dd_snap"] = snap
        except Exception:
            pass

    def dd_recent_changes():
        import sys
        return list(reversed(sys._dd_cache.get("dd_changes", [])))


    def dd_clear_changes():
        import sys
        sys._dd_cache["dd_changes"] = []
        renpy.restart_interaction()

    def _dd_position():
        if renpy.predicting(): return u"?"
        try:
            game = _dd_mod("renpy.game")
            node = game.script.lookup(game.context().current)
            fn = (getattr(node, "filename", u"") or u"").replace(u"\\", u"/").split(u"/")[-1]
            ln = int(getattr(node, "linenumber", 0) or 0)
            nearest = getattr(store, "_cx_nearest_label", None)
            label = nearest(fn, ln) if nearest else u""
            if label:
                return u"{}:{}  ({})".format(fn, ln, label)
            return u"{}:{}".format(fn, ln)
        except Exception:
            return u"?"

    def _dd_cond_text(cond):
        if isinstance(cond, str):
            return cond
        return getattr(cond, "source", None) or u"?"

    def _dd_eval_cond(cond):
        txt = _dd_cond_text(cond)
        if txt == u"True":
            return True
        try:
            return bool(_dd_mod("renpy.python").py_eval(txt))
        except Exception:
            return None

    def _dd_effects_from_block(block, depth=0, out=None, note=None):
        if out is None:
            out = []
        if not block or depth > 3:
            return out
        ast = _dd_mod("renpy.ast")
        for node in block:
            try:
                if isinstance(node, ast.Python):
                    src = getattr(getattr(node, "code", None), "source", u"") or u""
                    for line in src.splitlines():
                        m = _DD_ASSIGN_RE.match(line.strip())
                        if m and not m.group(1).startswith(u"_"):
                            out.append((m.group(1), m.group(2), m.group(3), note))
                elif isinstance(node, ast.If):
                    entries = list(getattr(node, "entries", []))
                    taken = None
                    unknown = False
                    for i, (cond, sub) in enumerate(entries):
                        r = _dd_eval_cond(cond)
                        if r is None:
                            unknown = True
                            break
                        if r:
                            taken = (i, cond, sub)
                            break
                    if unknown:
                        for i, (cond, sub) in enumerate(entries):
                            txt = _dd_cond_text(cond)
                            branch = u"else?" if (txt == u"True" and i) else (u"if? " + txt)
                            sub_note = branch if note is None else note + u" & " + branch
                            _dd_effects_from_block(sub, depth + 1, out, sub_note)
                    elif taken is not None:
                        i, cond, sub = taken
                        txt = _dd_cond_text(cond)
                        branch = u"else" if (txt == u"True" and i) else (u"if " + txt)
                        sub_note = branch if note is None else note + u" & " + branch
                        _dd_effects_from_block(sub, depth + 1, out, sub_note)
                elif isinstance(node, ast.Menu):
                    break
            except Exception:
                pass
        return out

    _DD_EFF_GREEN = u"#5be353"  # gain: += positive, set True, set positive
    _DD_EFF_RED = u"#e8556b"    # loss: -= , += negative, set False, set negative
    _DD_EFF_GREY = u"#8a8a8a"   # no-op: assigns the value the flag already has

    def _dd_parse_literal(val):
        if val == u"True":
            return True
        if val == u"False":
            return False
        if val == u"None":
            return None
        try:
            if u"." in val:
                return float(val)
            return int(val)
        except Exception:
            pass
        if len(val) >= 2 and val[0] in u"\"'" and val[-1] == val[0]:
            return val[1:-1]
        return None

    def _dd_effect_color(name, op, val):
        try:
            cur = getattr(store, name)
            has_cur = True
        except Exception:
            cur = None
            has_cur = False

        if op == u"+=":
            n = _dd_parse_literal(val)
            if isinstance(n, (int, float)) and n < 0:
                return _DD_EFF_RED
            return _DD_EFF_GREEN
        if op == u"-=":
            return _DD_EFF_RED

        target = _dd_parse_literal(val)
        if has_cur and target is not None and cur == target and type(cur) == type(target):
            return _DD_EFF_GREY
        if target is True:
            return _DD_EFF_GREEN
        if target is False:
            return _DD_EFF_RED
        if isinstance(target, (int, float)):
            return _DD_EFF_RED if target < 0 else _DD_EFF_GREEN
        return _DD_EFF_GREEN

    def _dd_fmt_effect(name, op, val, note=None):
        val = val.strip()
        if op == u"+=":
            disp = u"+" + val
        elif op == u"-=":
            disp = u"-" + val
        elif val == u"True":
            disp = u"+True"
        else:
            disp = u"= " + val
        col = _dd_effect_color(name, op, val)
        line = _dd_q(name) + u": {color=" + col + u"}" + _dd_q(disp[:40]) + u"{/color}"
        if note:
            line += u" {color=#8a8a8a}[[" + _dd_q(note[:60]) + u"]{/color}"
        return line

    def _dd_current_menu_node():
        try:
            ast = _dd_mod("renpy.ast")
            game = _dd_mod("renpy.game")
            node = game.script.lookup(game.context().current)
            if isinstance(node, ast.Menu):
                return node
        except Exception:
            pass
        return None

    def _dd_menu_summary(menu_node):
        if menu_node is None:
            return []
        out = []
        for entry in getattr(menu_node, "items", []):
            try:
                label, condition, subblock = entry[0], entry[1], entry[2]
            except Exception:
                continue
            if subblock is None:
                continue
            effects = [_dd_fmt_effect(*e) for e in _dd_effects_from_block(subblock)]
            if effects:
                out.append((_dd_q(label), effects))
        return out

    def _dd_eval_cond(cond):
        try:
            if cond is None or cond is True:
                return True
            if cond is False:
                return False
            c = cond.strip() if isinstance(cond, str) else cond
            if c == u"" or c == u"True":
                return True
            return bool(_dd_mod("renpy.python").py_eval(c))
        except Exception:
            return False

    def _dd_followup_walk(block, seen):
        if not block:
            return []

        out = []
        ast = _dd_mod("renpy.ast")
        for node in block:
            try:
                if isinstance(node, ast.If):
                    for cond, sub in getattr(node, "entries", []):
                        if _dd_eval_cond(cond):
                            out.extend(_dd_followup_walk(sub, seen))
                            break
                elif isinstance(node, ast.Label):
                    name = getattr(node, "name", None)
                    if name and name not in seen:
                        seen.add(name)
                        out.extend(_dd_followup_walk(getattr(node, "block", []) or [], seen))
                elif isinstance(node, ast.Jump):
                    target = getattr(node, "target", None) or getattr(node, "label", None)
                    if target and target not in seen:
                        seen.add(target)
                        try:
                            nxt = _dd_mod("renpy.game").script.lookup(target)
                        except Exception:
                            nxt = None
                        if isinstance(nxt, ast.Menu):
                            out.extend(_dd_menu_summary(nxt))
                        elif nxt is not None and getattr(nxt, "block", None):
                            out.extend(_dd_followup_walk(getattr(nxt, "block", []) or [], seen))
                elif isinstance(node, ast.Call):
                    target = getattr(node, "label", None) or getattr(node, "target", None)
                    if target and target not in seen:
                        seen.add(target)
                        try:
                            nxt = _dd_mod("renpy.game").script.lookup(target)
                        except Exception:
                            nxt = None
                        if isinstance(nxt, ast.Menu):
                            out.extend(_dd_menu_summary(nxt))
                        elif nxt is not None and getattr(nxt, "block", None):
                            out.extend(_dd_followup_walk(getattr(nxt, "block", []) or [], seen))
                elif isinstance(node, ast.Menu):
                    out.extend(_dd_menu_summary(node))
            except Exception:
                pass
            if out:
                break
        return out

    def _dd_followup_option_lines(block, seen=None):
        """Look-ahead to the first meaningful menu reachable from a choice block.

        Returns a list of (sub_choice_label, [effect_str, ...]) tuples.
        """
        if seen is None:
            seen = set()
        return _dd_followup_walk(block, seen)

    def dd_choice_effects():
        import time
        import sys
        if renpy.predicting(): return None
        try:
            pos = _dd_mod("renpy.game").context().current
        except Exception:
            pos = None

        cache = sys._dd_cache.get("choice_effects")
        if cache and cache[0] == pos:
            return cache[1]

        node = _dd_current_menu_node()
        if node is None:
            sys._dd_cache["choice_effects"] = (pos, None)
            return None

        out = []
        for entry in getattr(node, "items", []):
            try:
                label, condition, block = entry[0], entry[1], entry[2]
            except Exception:
                continue
            if block is None:
                continue
            direct = [_dd_fmt_effect(*e) for e in _dd_effects_from_block(block)]
            cond = condition if isinstance(condition, str) else u"True"
            subs = _dd_followup_option_lines(block)
            out.append((_dd_q(label), direct, subs, cond))

        result = out or None
        sys._dd_cache["choice_effects"] = (pos, result)
        return result

    def dd_snapshot_shortcut():
        fn = getattr(store, "dp_save_path", None)
        if fn is not None:
            fn()
        else:
            renpy.notify("dev_pathtest.rpy is not installed")

    def dd_set_panel(p):
        dd_state.dd_panel = None if dd_state.dd_panel == p else p
        renpy.restart_interaction()

    def dd_drill(prefix):
        store.dd_var_filter = prefix + u"_"
        dd_state.dd_panel = u"vars"
        renpy.restart_interaction()

    def dd_toggle(name):
        try:
            v = getattr(store, name, None)
            if isinstance(v, bool) or v is None:
                setattr(store, name, not bool(v))
                renpy.restart_interaction()
        except Exception:
            pass

    def dd_adjust(name, delta):
        try:
            v = getattr(store, name, None)
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                setattr(store, name, v + delta)
                renpy.restart_interaction()
        except Exception:
            pass

    def dd_var_matches(filter_text, limit=16):
        if renpy.predicting(): return [], 0
        f = (filter_text or u"").strip().lower()
        names = list(_dd_flag_universe())
        if len(f) >= 2:
            seen = set(names)
            try:
                for k, v in list(store.__dict__.items()):
                    if k.startswith(u"_") or k in seen:
                        continue
                    if isinstance(v, (bool, int, float, str)) or v is None:
                        names.append(k)
                        seen.add(k)
            except Exception:
                pass
        if f:
            names = [n for n in names if f in n.lower()]
        watched = set(dd_state.dd_watches or [])
        names = [n for n in names if n not in watched]
        names.sort()
        return names[:limit], max(0, len(names) - limit)

    def _dd_latest_reports():
        rep_dir = _dd_os.path.join(config.basedir, "pathtests", "reports")
        try:
            key = _dd_os.path.getmtime(rep_dir)
        except Exception:
            return {}
        cache = sys._dd_cache.get("latest_reports")
        if cache is not None and cache[0] == key:
            return cache[1]
        latest = {}
        stamps = {}
        try:
            for fn in _dd_os.listdir(rep_dir):
                if not fn.endswith(u".json"):
                    continue
                path = _dd_os.path.join(rep_dir, fn)
                try:
                    mt = _dd_os.path.getmtime(path)
                    with open(path, "r", encoding="utf-8") as f:
                        data = _dd_json.load(f)
                except Exception:
                    continue
                nm = data.get("name")
                if nm and (nm not in stamps or mt > stamps[nm]):
                    stamps[nm] = mt
                    latest[nm] = bool(data.get("passed"))
        except Exception:
            return latest
        sys._dd_cache["latest_reports"] = (key, latest)
        return latest

    def dd_replay_entries():
        if renpy.predicting(): return []
        lister = getattr(store, "dp_list", None)
        if lister is None:
            return None
        try:
            names = lister()
        except Exception:
            names = []
        latest = _dd_latest_reports()
        return [(n, latest.get(n)) for n in names]

    def dd_replay_run(name):
        fn = getattr(store, "dp_replay", None)
        if fn is None:
            renpy.notify("dev_pathtest.rpy is not installed")
            return
        fn(name)

    def dd_open_pathtests():
        try:
            path = _dd_os.path.join(config.basedir, "pathtests")
            _dd_os.makedirs(path, exist_ok=True)
            _dd_os.startfile(path)
        except Exception as e:
            renpy.notify("Could not open folder: " + str(e)[:60])

    _DD_CONTEXT_BAKED = {
        u"episode_1.rpy": [u"Rachel_End"],
        u"episode_3.rpy": [u"Rachel_End"],
        u"episode_4.rpy": [
            u"Riverside_Friends", u"Riverside_FB_NikkiCaraChoice",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Nikki_Cheat", u"Cara_Cheat", u"Rachel_End", u"Lakeyn_End",
        ],
        u"episode_5.rpy": [u"Cara_Girlfriend", u"Gabi_End"],
        u"episode_6.rpy": [
            u"Riverside_End", u"Riverside_Friends",
            u"Nikki_Girlfriend", u"Cara_Girlfriend", u"Rachel_End",
        ],
        u"episode_7.rpy": [
            u"Riverside_Friends", u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Nikki_Cheat", u"Cara_Cheat",
            u"Alexis_End", u"Erynn_End", u"Gabi_End",
        ],
        u"episode_8.rpy": [
            u"Alexis_SecretPath", u"Alexis_Girlfriend", u"Alexis_Dating",
            u"Layla_Dating", u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Alexis_End", u"Tori_End",
        ],
        u"episode_9.rpy": [
            u"MC_Girlfriend_Riverside", u"Riverside_Friends",
            u"Alexis_Dating", u"Layla_Dating",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Layla_End", u"Elena_End",
        ],
        u"episode_10.rpy": [
            u"MC_NoFriends", u"Riverside_Friends",
            u"Alexis_Dating", u"Layla_Dating",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Layla_End", u"Melissa_End",
        ],
        u"episode_11.rpy": [
            u"Alexis_SecretPath", u"Alexis_Dating",
            u"Layla_Girlfriend", u"Layla_Dating",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Layla_End", u"Alexis_End",
        ],
        u"episode_12.rpy": [
            u"Alexis_SecretPath", u"Alexis_Dating", u"Layla_Dating",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Layla_End", u"Gabi_End",
        ],
        u"episode_13.rpy": [
            u"Alexis_SecretPath", u"Alexis_Dating", u"Layla_Dating",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Layla_End", u"Lakeyn_End", u"Mira_End",
        ],
        u"episode_14.rpy": [
            u"Riverside_End", u"Riverside_Friends", u"Riverside_MiraTruth",
            u"AlexisValeria", u"LayLena",
            u"Nikki_Cheat", u"Cara_Cheat",
            u"Nikki_Girlfriend", u"Cara_Girlfriend",
            u"Alexis_Dating", u"Layla_Dating",
        ],
        u"episode_15.rpy": [
            u"Riverside_End", u"MC_NoFriends", u"Riverside_Girlfriend",
            u"Riverside_FB_NikkiCaraChoice",
            u"AlexisValeria", u"LayLena",
            u"Alexis_SecretPath", u"Alexis_Girlfriend",
            u"Valeria_Dating", u"Layla_Dating",
            u"Nikki_Cheat", u"Cara_Cheat",
        ],
        u"episode_16.rpy": [
            u"MC_Week6_Wednesday_EthanCrash_Call",
            u"Erynn_Week6_Wednesday_TellEverything",
            u"Erynn_Week6_Wednesday_StayOver",
            u"MC_Week6_Wednesday_Cats", u"MC_Week6_Wednesday_Dogs",
        ],
    }

    def _dd_source_lines(fn):
        cache = sys._dd_cache.setdefault("source_lines", {})
        if fn in cache:
            return cache[fn]
        lines = None
        for p in (_dd_os.path.join(config.basedir, fn),
                _dd_os.path.join(config.gamedir, _dd_os.path.basename(fn))):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                break
            except Exception:
                continue
        cache[fn] = lines
        return lines

    def dd_context_vars(before=40, after=80, limit=20):
        if renpy.predicting() or renpy.config.skipping or renpy.in_rollback():
            return [], []
        fn = u""
        ln = 0
        try:
            game = _dd_mod("renpy.game")
            node = game.script.lookup(game.context().current)
            fn = (getattr(node, "filename", u"") or u"").replace(u"\\", u"/")
            ln = int(getattr(node, "linenumber", 0) or 0)
        except Exception:
            node = None
            
        cache = sys._dd_cache.get("context_vars")
        if cache and cache[0] == node:
            return cache[1]
        if not _dd_perf_throttle("context_vars_eval", 0.1):
            return cache[1] if cache else ([], [])

        baked_out = []
        seen = set()
        baked = list(_DD_CONTEXT_BAKED.get(u"*", []))
        if fn:
            baked += _DD_CONTEXT_BAKED.get(fn.split(u"/")[-1], [])
        for nm in baked:
            if nm not in seen:
                baked_out.append(nm)
                seen.add(nm)
        scanned = []
        lines = _dd_source_lines(fn) if (fn and ln) else None
        if lines:
            universe = set(_dd_flag_universe())
            lo = max(0, ln - 1 - before)
            hi = min(len(lines), ln - 1 + after)
            found = {}
            for i in range(lo, hi):
                off = i - (ln - 1)
                for m in _DD_IDENT_ANY_RE.finditer(lines[i]):
                    nm = m.group(0)
                    if nm in universe and (nm not in found or abs(off) < abs(found[nm])):
                        found[nm] = off
            for nm, off in sorted(found.items(), key=lambda kv: (abs(kv[1]), kv[0])):
                if nm not in seen:
                    scanned.append((nm, off))
                    seen.add(nm)
                    
        result = (baked_out[:limit], scanned[:limit])
        sys._dd_cache["context_vars"] = (node, result)
        return result

    _DD_GATE_RE = _dd_re.compile(r'^\s*(?:if|elif)\s+(.+?)\s*:\s*(?:#.*)?$')

    def dd_upcoming_gates(ahead=200, limit=5):
        if renpy.predicting() or renpy.config.skipping or renpy.in_rollback():
            return []
        try:
            game = _dd_mod("renpy.game")
            node = game.script.lookup(game.context().current)
            fn = (getattr(node, "filename", u"") or u"").replace(u"\\", u"/")
            ln = int(getattr(node, "linenumber", 0) or 0)
        except Exception:
            return []
        if not fn or not ln:
            return []

        def _normalize(parsed):
            out = []
            for item in parsed or []:
                if not isinstance(item, (tuple, list)):
                    continue
                if len(item) == 3:
                    offset, cond, result = item
                    out.append((offset, cond, result))
                elif len(item) == 2:
                    offset, cond = item
                    out.append((offset, cond, _dd_eval_cond(cond)))
            return out
            
        cache = sys._dd_cache.get("upcoming_gates")
        if cache and cache[0] == node:
            parsed_gates = _normalize(cache[1])
            if not parsed_gates and cache[1]:
                sys._dd_cache["upcoming_gates"] = (node, [])
        else:
            if not _dd_perf_throttle("upcoming_gates_eval", 0.1):
                return _normalize(cache[1]) if cache else []
            parsed_gates = []
            lines = _dd_source_lines(fn)
            if lines:
                universe = set(_dd_flag_universe())
                hi = min(len(lines), ln - 1 + ahead)
                for i in range(ln, hi):
                    m = _DD_GATE_RE.match(lines[i])
                    if not m:
                        continue
                    cond = m.group(1).strip()
                    if not any(x.group(0) in universe for x in _DD_IDENT_ANY_RE.finditer(cond)):
                        continue
                    if len(cond) > 52:
                        cond = cond[:49] + u"..."
                    parsed_gates.append((i + 1 - ln, cond))
                    if len(parsed_gates) >= limit:
                        break
            sys._dd_cache["upcoming_gates"] = (node, parsed_gates)
            parsed_gates = _normalize(parsed_gates)

        return parsed_gates

    _DD_TIERS = (
        (u"Girlfriend", u"GIRLFRIEND", u"#ff6fd8"),
        (u"Dating", u"dating", u"#ff9de2"),
        (u"LikeMC", u"likes MC", u"#5be353"),
        (u"Friends", u"friends", u"#6fd3ff"),
    )

    _DD_SPECIAL_RE = _dd_re.compile(
        r"(Path$|Route$|^Riverside_|^MC_NoFriends$|^MC_Girlfriend_"
        r"|^AlexisValeria$|^LayLena$)")

    _DD_SOFT_END = {
        u"Alexis": [
            (u"Alexis_Week6_Tuesday_Break", u"broke up"),
            (u"Alexis_Week5_Thursday_BreakUp", u"broke up"),
            (u"Alexis_Week3_Wednesday_TC_Breakup", u"broke up (chose Layla)"),
        ],
        u"Layla": [
            (u"Layla_Week5_Wednesday_BreakUp", u"broke up"),
        ],
        u"Elena": [
            (u"Layla_Week5_Wednesday_BreakUp", u"left w/ Layla"),
        ],
        u"Cara": [
            (u"Cara_Week6_Wednesday_Breakup or NikkiCara_Week6_Wednesday_Breakup",
            u"broke up"),
            (u"Cara_Week4_Wednesday_Visit_Breakup", u"broke up (visit)"),
        ],
        u"Nikki": [
            (u"Nikki_Week6_Wednesday_Breakup or NikkiCara_Week6_Wednesday_Breakup",
            u"broke up"),
            (u"Nikki_Week4_Wednesday_Visit_Breakup", u"broke up (visit)"),
        ],
        u"Valeria": [
            (u"Alexis_Week6_Tuesday_Break and not Valeria_Dating",
            u"likely broken"),
        ],
    }

    def _dd_route_chars():
        if "route_chars" in sys._dd_cache:
            return sys._dd_cache["route_chars"]
            
        universe = set(_dd_flag_universe())
        if not universe:
            return {}
        chars = set()
        for n in universe:
            if n.startswith(u"SexCounter_"):
                chars.add(n[len(u"SexCounter_"):])
            elif n.endswith(u"_Points") and n.count(u"_") == 1:
                chars.add(n[: -len(u"_Points")])
        chars.discard(u"MC")
        out = {}
        for c in sorted(chars):
            flags = set()
            for sfx in (u"Points", u"Girlfriend", u"Dating", u"Friends",
                        u"LikeMC", u"Sex", u"SecretPath", u"End", u"Cheat",
                        u"SP", u"SPoints", u"Solo", u"Visit", u"Visit_Points",
                        u"Weekend_Points", u"Jealousy", u"JealousyPoints",
                        u"Suspicion"):
                if c + u"_" + sfx in universe:
                    flags.add(sfx)
            if u"SexCounter_" + c in universe:
                flags.add(u"SexCounter")
            out[c] = flags
            
        sys._dd_cache["route_chars"] = out
        return out

    def dd_route_rows(limit=14):
        import time
        import sys
        now = time.time()
        key = ("route_rows", limit)
        
        cache = sys._dd_cache.get(key)
        if cache and (now - cache[0] < 0.2):
            return cache[1]
            
        rows = []
        for c, flags in _dd_route_chars().items():
            try:
                def gv(sfx, _c=c):
                    return getattr(store, _c + u"_" + sfx, None)
                tier_label = u""
                tier_color = u"#9ab0bb"
                rank = 0
                for i, (sfx, lbl, col) in enumerate(_DD_TIERS):
                    if sfx in flags and gv(sfx) is True:
                        tier_label, tier_color = lbl, col
                        rank = len(_DD_TIERS) - i
                        break
                pts = None
                if u"Points" in flags:
                    try:
                        pts = int(gv(u"Points") or 0)
                    except Exception:
                        pts = None
                sexn = 0
                if u"SexCounter" in flags:
                    try:
                        sexn = int(getattr(store, u"SexCounter_" + c, 0) or 0)
                    except Exception:
                        sexn = 0
                sex_flag = (u"Sex" in flags and gv(u"Sex") is True)
                if sexn:
                    sex_disp = u"sex x" + str(sexn)
                elif sex_flag:
                    sex_disp = u"sex"
                else:
                    sex_disp = u""
                secret = (u"SecretPath" in flags and gv(u"SecretPath") is True)
                ended = (u"End" in flags and gv(u"End") is True)
                cheat = (u"Cheat" in flags and gv(u"Cheat") is True)
                soft = u""
                if not ended:
                    for cond, lbl in _DD_SOFT_END.get(c, ()):
                        if _dd_eval_cond(cond) is True:
                            soft = lbl
                            break
                extras = []
                for sfx in (u"SP", u"SPoints"):
                    if sfx not in flags:
                        continue
                    v = gv(sfx)
                    if v is True:
                        extras.append((u"SP", u"#ffd35b"))
                    else:
                        try:
                            v = int(v or 0)
                        except Exception:
                            v = 0
                        if v:
                            extras.append((u"SP " + str(v), u"#ffd35b"))
                if u"Solo" in flags and gv(u"Solo") is True:
                    extras.append((u"solo", u"#b48aff"))
                meters = ((u"Visit_Points", u"visit"), (u"Weekend_Points", u"wknd"),
                        (u"JealousyPoints", u"jealousy"), (u"Jealousy", u"jealousy"),
                        (u"Suspicion", u"suspicion"))
                metered = set()
                for sfx, lbl in meters:
                    if sfx not in flags:
                        continue
                    try:
                        v = int(gv(sfx) or 0)
                    except Exception:
                        v = 0
                    if v:
                        extras.append((lbl + u" " + str(v), u"#c9a86a"))
                        metered.add(lbl)
                if u"Visit" in flags and gv(u"Visit") is True and u"visit" not in metered:
                    extras.append((u"visit", u"#b48aff"))
                if not rank and not secret and not sex_disp and not pts and not ended and not cheat and not extras and not soft:
                    continue
                pin = (c + u"_Points") if u"Points" in flags else None
                rows.append((c, pin, tier_label, tier_color, pts, sex_disp, secret, ended, cheat, extras, soft))
            except Exception:
                continue
        rows.sort(key=lambda r: (
            r[7] or bool(r[10]),
            -(4 if r[2] == u"GIRLFRIEND" else 3 if r[2] == u"dating"
                else 2 if r[2] == u"likes MC" else 1 if r[2] == u"friends" else 0),
            not r[6],
            -(r[4] or 0),
            r[0],
        ))
        more = max(0, len(rows) - limit)
        result = (rows[:limit], more)
        
        sys._dd_cache[key] = (now, result)
        return result

    def dd_route_specials():
        if renpy.predicting(): return []
        chars = _dd_route_chars()
        out = []
        for n in _dd_flag_universe():
            if not _DD_SPECIAL_RE.search(n):
                continue
            if n.endswith(u"_SecretPath") and n[: -len(u"_SecretPath")] in chars:
                continue
            try:
                if getattr(store, n, None) is True:
                    out.append(n)
            except Exception:
                pass
        return sorted(out)

    _DD_INTEL_RE = _dd_re.compile(
        r"(Know|Truth|Caught|Expose|See[A-Z]|Witness|Tell)")

    def dd_route_intel():
        if renpy.predicting(): return []
        out = []
        for n in _dd_flag_universe():
            if not _DD_INTEL_RE.search(n) or _DD_SPECIAL_RE.search(n):
                continue
            try:
                if getattr(store, n, None) is True:
                    out.append(n)
            except Exception:
                pass
        return sorted(out)

init python:
    if "dd_overlay" not in config.overlay_screens:
        config.overlay_screens.append("dd_overlay")
    if dd_state.dd_panel == u"jump":
        dd_state.dd_panel = u"context"

screen dd_overlay():
    predict False
    zorder 900
    key "K_F8" action ToggleField(dd_state, "dd_overlay")

    if dd_state.dd_overlay:
        
        $ _dd_tick()
        key "K_F7" action Function(dd_snapshot_shortcut)

        frame:
            xpos 12
            ypos 12
            background "#000000c8"
            padding (14, 10)

            vbox:
                spacing 2
                xminimum 330

                text "Debug" size 20 bold True
                text _dd_position() size 13 color "#9ab0bb"

                null height 4

                hbox:
                    spacing 14
                    for _dd_tab in ["context", "vars", "replays", "actions"]:
                        textbutton _dd_tab:
                            action Function(dd_set_panel, _dd_tab)
                            text_size 13
                            text_color ("#4ceefc" if dd_state.dd_panel == _dd_tab else "#777777")
                            text_hover_color "#ffffff"
                            padding (0, 0)
                    textbutton "?":
                        action ToggleField(dd_state, "dd_help")
                        text_size 13
                        text_color ("#4ceefc" if dd_state.dd_help else "#777777")
                        text_hover_color "#ffffff"
                        padding (0, 0)

                if dd_state.dd_panel == "context":
                    null height 4
                    if dd_state.dd_help:
                        text "What matters right now, in three groups. 'episode route flags': the big cross-episode flags this episode's story checks (hand-picked, always listed). 'referenced nearby': flags the script actually mentions around your current line; -N/+N = lines behind/ahead of you. 'upcoming gates': the next if-checks ahead, with PASS/FAIL for how each would resolve with your current flags. Click any flag to pin it." size 12 color "#9ab0bb" xmaximum 330
                        null height 4
                    $ _dd_baked, _dd_scan = dd_context_vars()
                    if not _dd_baked and not _dd_scan:
                        text "no known flags referenced nearby" size 13 color "#777777"
                    if _dd_baked:
                        text "episode route flags" size 12 color "#777777"
                        for _dd_n in _dd_baked:
                            textbutton (_dd_q(_dd_n) + u": " + dd_value_markup(getattr(store, _dd_n, None))):
                                action Function(dd_watch, _dd_n)
                                text_size 14
                                padding (0, 0)
                    if _dd_scan:
                        null height 6
                        text "referenced nearby" size 12 color "#777777"
                        for _dd_n, _dd_off in _dd_scan:
                            hbox:
                                spacing 6
                                text ((u"+" + str(_dd_off)) if _dd_off > 0 else str(_dd_off)) size 11 color "#555555" min_width 28 yalign 0.5
                                textbutton (_dd_q(_dd_n) + u": " + dd_value_markup(getattr(store, _dd_n, None))):
                                    action Function(dd_watch, _dd_n)
                                    text_size 14
                                    padding (0, 0)
                    $ _dd_gates = dd_upcoming_gates()
                    if _dd_gates:
                        null height 6
                        text "upcoming gates (this file, linear)" size 12 color "#777777"
                        for _dd_go, _dd_gc, _dd_gr in _dd_gates:
                            hbox:
                                spacing 6
                                text (u"+" + str(_dd_go)) size 12 color "#777777" yalign 0.5
                                if _dd_gr is True:
                                    text "PASS" size 12 color "#5be353" yalign 0.5
                                elif _dd_gr is False:
                                    text "FAIL" size 12 color "#ff5b5b" yalign 0.5
                                else:
                                    text "?" size 12 color "#777777" yalign 0.5
                                text _dd_q(_dd_gc) size 12 color "#bbbbbb" yalign 0.5

                if dd_state.dd_panel == "vars":
                    null height 4
                    if dd_state.dd_help:
                        text "Search every story flag by name (type 2+ letters). Click a result to pin it to the watch list below." size 12 color "#9ab0bb" xmaximum 330
                        null height 4
                    frame:
                        background "#ffffff20"
                        padding (6, 3)
                        input:
                            value VariableInputValue("dd_var_filter", returnable=False)
                            length 40
                            size 14
                            color "#ffffff"
                    $ _dd_vm, _dd_vmore = dd_var_matches(dd_var_filter)
                    for _dd_n in _dd_vm:
                        textbutton (_dd_q(_dd_n) + u": " + dd_value_markup(getattr(store, _dd_n, None))):
                            action Function(dd_watch, _dd_n)
                            text_size 14
                            padding (0, 0)
                    if _dd_vmore:
                        text (u"... " + str(_dd_vmore) + u" more, refine the filter") size 12 color "#777777"
                    if not _dd_vm and not _dd_vmore:
                        text "no matches" size 13 color "#777777"
                    $ _dd_typed = (dd_var_filter or u"").strip()
                    if _DD_IDENT_RE.match(_dd_typed) and _dd_typed not in _dd_vm and _dd_typed not in (dd_state.dd_watches or []):
                        textbutton (u"pin '" + _dd_q(_dd_typed) + u"' as typed"):
                            action Function(dd_watch, _dd_typed)
                            text_size 13
                            text_color "#c9a86a"
                            padding (0, 0)

                if dd_state.dd_panel == "replays":
                    null height 4
                    if dd_state.dd_help:
                        text "Recorded playthroughs (F7 saves your current one). Click a name to restart the game and auto-replay that route from the start. PASS/FAIL is the result of the last replay." size 12 color "#9ab0bb" xmaximum 330
                        null height 4
                    $ _dd_reps = dd_replay_entries()
                    if _dd_reps is None:
                        text "dev_pathtest.rpy is not installed" size 13 color "#777777"
                    elif not _dd_reps:
                        text "no path tests yet (F7 records one)" size 13 color "#777777"
                    else:
                        for _dd_rn, _dd_pass in _dd_reps:
                            hbox:
                                spacing 8
                                if _dd_pass is True:
                                    text "PASS" size 12 color "#5be353" yalign 0.5
                                elif _dd_pass is False:
                                    text "FAIL" size 12 color "#ff5b5b" yalign 0.5
                                else:
                                    text "----" size 12 color "#777777" yalign 0.5
                                textbutton _dd_q(_dd_rn):
                                    action Confirm(
                                        u"Replay '" + _dd_q(_dd_rn) + u"'?\nThe game restarts, fast-skips the route, writes a report and quits.",
                                        yes=Function(dd_replay_run, _dd_rn))
                                    text_size 14
                                    padding (0, 0)

                if dd_state.dd_panel == "actions":
                    null height 4
                    if dd_state.dd_help:
                        text "Utility shortcuts: save your playthrough as a replayable path test, toggle fast skip, reload changed scripts, open the pathtests folder, or clear the watch list." size 12 color "#9ab0bb" xmaximum 330
                        null height 4
                    textbutton "save path snapshot (F7)":
                        action Function(dd_snapshot_shortcut)
                        text_size 14
                        padding (0, 0)
                    textbutton "toggle fast skip":
                        action Skip(fast=True, confirm=False)
                        text_size 14
                        padding (0, 0)
                    textbutton "reload scripts (Shift+R)":
                        action Function(renpy.reload_script)
                        text_size 14
                        padding (0, 0)
                    textbutton "open pathtests folder":
                        action Function(dd_open_pathtests)
                        text_size 14
                        padding (0, 0)
                    textbutton "clear all watches":
                        action Function(dd_watch_clear)
                        text_size 14
                        padding (0, 0)

                null height 4

                if dd_state.dd_help and dd_state.dd_watches:
                    text "Watch list: pinned flags stay visible here. [[t] toggles true/false, [[-]/[[+] adjust numbers, [[x] unpins." size 12 color "#9ab0bb" xmaximum 330

                if dd_state.dd_watches:
                    for _dd_w in dd_state.dd_watches:
                        $ _dd_wv = getattr(store, _dd_w, None)
                        hbox:
                            spacing 8
                            text (_dd_q(_dd_w) + u": " + dd_value_markup(_dd_wv)) size 16
                            if isinstance(_dd_wv, bool) or _dd_wv is None:
                                textbutton "[[t]":
                                    action Function(dd_toggle, _dd_w)
                                    text_size 12
                                    text_color "#777777"
                                    text_hover_color "#5be353"
                                    padding (0, 0)
                            elif isinstance(_dd_wv, (int, float)):
                                textbutton "[[-]":
                                    action Function(dd_adjust, _dd_w, -1)
                                    text_size 12
                                    text_color "#777777"
                                    text_hover_color "#6fd3ff"
                                    padding (0, 0)
                                textbutton "[[+]":
                                    action Function(dd_adjust, _dd_w, 1)
                                    text_size 12
                                    text_color "#777777"
                                    text_hover_color "#6fd3ff"
                                    padding (0, 0)
                            textbutton "[[x]":
                                action Function(dd_unwatch, _dd_w)
                                text_size 12
                                text_color "#777777"
                                text_hover_color "#ff5b5b"
                                padding (0, 0)
                else:
                    text "no watches -- use the vars tab or click a recent change" size 13 color "#777777"

                if dd_recent_changes():
                    null height 6
                    hbox:
                        spacing 10
                        text "Recent changes" size 14 color "#c9a86a"
                        textbutton "clear":
                            action Function(dd_clear_changes)
                            text_size 12
                            text_color "#777777"
                            text_hover_color "#ffffff"
                            padding (0, 0)
                    if dd_state.dd_help:
                        text "Flags that just changed as you play: old value > new value. Click one to pin it." size 12 color "#9ab0bb" xmaximum 330
                    for _dd_n, _dd_old, _dd_new in dd_recent_changes():
                        textbutton (_dd_q(_dd_n) + u": " + dd_value_markup(_dd_old) + u" > " + dd_value_markup(_dd_new)):
                            action Function(dd_watch, _dd_n)
                            text_size 14
                            padding (0, 0)

        $ _dd_eff = dd_choice_effects()
        if _dd_eff:
            frame:
                xpos 15
                yalign 1.0
                yoffset - 15
                background "#000000c8"
                padding (14, 10)

                vbox:
                    spacing 6
                    xminimum 360

                    text "Choices" size 20 bold True

                    if dd_state.dd_help:
                        text "What each menu choice will change, shown before you pick. Blue are the choice's own variables; pink are the sub choices it leads to and their variables." size 12 color "#9ab0bb" xmaximum 420

                    for _dd_i, (_dd_cap, _dd_direct, _dd_subs, _dd_cond) in enumerate(_dd_eff):
                        vbox:
                            spacing 2
                            xsize 420

                            hbox:
                                spacing 6
                                text u"{color=#d10089}>{/color}" size 15 bold True
                                text _dd_cap size 16 bold True color "#dfe7eb"
                                if _dd_cond != u"True":
                                    text (u"if " + _dd_q(_dd_cond)) size 12 color "#c9a86a" yalign 0.5

                            if _dd_direct:
                                for _dd_line in _dd_direct:
                                    text (u"      " + _dd_line) size 15 color "#63c8e8"
                            elif not _dd_subs:
                                text u"      no variable changes" size 14 color "#777777"

                            if _dd_subs:
                                for _dd_slabel, _dd_slines in _dd_subs:
                                    text (u"      {color=#ff7bd8}> " + _dd_slabel + u"{/color}") size 14
                                    for _dd_sline in _dd_slines:
                                        text (u"            " + _dd_sline) size 14 color "#ff7bd8"

        if dd_state.dd_routes_min:
            textbutton "routes":
                xanchor 1.0
                xpos 1.0
                xoffset - 12
                ypos 12
                action ToggleField(dd_state, "dd_routes_min")
                text_size 13
                text_color "#777777"
                text_hover_color "#ffffff"
        else:
            $ _dd_route_limit = 100000 if dd_state.dd_routes_expand else 14
            $ _dd_routes, _dd_rmore = dd_route_rows(limit=_dd_route_limit)
            $ _dd_specials = dd_route_specials()
            frame:
                xanchor 1.0
                xpos 1.0
                xoffset - 12
                ypos 12
                background "#000000c8"
                padding (14, 10)

                vbox:
                    spacing 3
                    xminimum 250

                    hbox:
                        spacing 10
                        text "Routes" size 20 bold True
                        textbutton "[[hide]":
                            action ToggleField(dd_state, "dd_routes_min")
                            yalign 0.5
                            text_size 12
                            text_color "#777777"
                            text_hover_color "#ffffff"
                            padding (0, 0)

                    if dd_state.dd_help:
                        text "Where you stand with each character: relationship badge, points, and warnings. Grayed rows are routes that have ended (red ENDED) or broken off (orange). Gold bullets are major story paths, amber 'intel' bullets are things characters have found out. '>>' lists all of that character's flags. Click a name or bullet to pin it." size 12 color "#9ab0bb" xmaximum 340
                        null height 4

                    if _dd_specials:
                        for _dd_s in _dd_specials:
                            textbutton (u"{color=#ffd35b}\u2022{/color} " + _dd_q(_dd_s)):
                                action Function(dd_watch, _dd_s)
                                text_size 14
                                text_color "#ffd35b"
                                text_hover_color "#ffffff"
                                padding (0, 0)
                        null height 4

                    if not _dd_routes:
                        text "no route signals yet" size 13 color "#777777"

                    for _dd_rc, _dd_rpin, _dd_rt, _dd_rcol, _dd_rp, _dd_rs, _dd_rsec, _dd_rend, _dd_rcheat, _dd_rex, _dd_rsoft in _dd_routes:
                        hbox:
                            spacing 8
                            if _dd_rpin:
                                textbutton _dd_q(_dd_rc):
                                    action Function(dd_watch, _dd_rpin)
                                    text_size 15
                                    text_color ("#8a8a8a" if (_dd_rend or _dd_rsoft) else "#e8e8e8")
                                    text_hover_color "#ffffff"
                                    padding (0, 0)
                            else:
                                text _dd_q(_dd_rc) size 15 color ("#8a8a8a" if (_dd_rend or _dd_rsoft) else "#e8e8e8")
                            if _dd_rend:
                                text "ENDED" size 12 color "#ff5b5b" yalign 0.5
                            if _dd_rsoft:
                                text _dd_q(_dd_rsoft) size 12 color "#ff8f5b" yalign 0.5
                            if _dd_rcheat:
                                text "cheat" size 12 color "#ff9d5b" yalign 0.5
                            if _dd_rsec:
                                text "SECRET" size 12 color "#ffd35b" yalign 0.5
                            if _dd_rt:
                                text _dd_rt size 12 color _dd_rcol yalign 0.5
                            if _dd_rp:
                                text (str(_dd_rp) + u" pts") size 12 color "#6fd3ff" yalign 0.5
                            if _dd_rs:
                                text _dd_rs size 12 color "#d10089" yalign 0.5
                            for _dd_ext, _dd_exc in _dd_rex:
                                text _dd_ext size 12 color _dd_exc yalign 0.5
                            textbutton ">>":
                                action Function(dd_drill, _dd_rc)
                                yalign 0.5
                                text_size 12
                                text_color "#555555"
                                text_hover_color "#ffffff"
                                padding (0, 0)

                    if not dd_state.dd_routes_expand and _dd_rmore:
                        textbutton (u"... " + str(_dd_rmore) + u" more"):
                            action ToggleField(dd_state, "dd_routes_expand")
                            text_size 12
                            text_color "#777777"
                            text_hover_color "#ffffff"
                            padding (0, 0)
                    elif dd_state.dd_routes_expand:
                        textbutton "show fewer":
                            action ToggleField(dd_state, "dd_routes_expand")
                            text_size 12
                            text_color "#777777"
                            text_hover_color "#ffffff"
                            padding (0, 0)

                    $ _dd_intel = dd_route_intel()
                    if _dd_intel:
                        null height 4
                        text "intel" size 12 color "#777777"
                        for _dd_i in _dd_intel:
                            textbutton (u"{color=#c9a86a}\u2022{/color} " + _dd_q(_dd_i)):
                                action Function(dd_watch, _dd_i)
                                text_size 13
                                text_color "#c9a86a"
                                text_hover_color "#ffffff"
                                padding (0, 0)

################################################################################
## Path regression tests -- BlueFox.au v1.2.0
################################################################################
##
## Records a playthrough (the choices taken plus the final flag state) into a
## JSON file, and can later REPLAY that exact choice sequence on a new build,
## unattended, then diff the resulting flags against the recording. Use it to
## verify that a script update did not change the outcome of known paths.
##
## RECORDING:
##     Play normally. At any point, save a snapshot:
##       * console (Shift+O):  dp_save_path("valeria_route")
##       * or press F7 while the dev_debug overlay (F8) is visible
##     This writes <basedir>/pathtests/<name>.json containing every choice
##     made so far (from cx_choice_history) and all flag values.
##
## REPLAYING:
##     * console:  dp_replay("valeria_route")   (restarts into the test)
##     * or set an environment variable and launch the game:
##           $env:INTERTWINED_PATHTEST = "valeria_route"
##           & lib\py3-windows-x86_64\python.exe Intertwined.py
##     The game auto-starts, fast-skips everything, picks the recorded choice
##     at every menu, then stops at the first menu past the recording (or at
##     the end of the game), diffs flags, writes a report to
##     <basedir>/pathtests/reports/, and quits. PASS/FAIL is in the report
##     and on stdout (log.txt).
##
## LIMITATIONS:
##     * Menus are matched by caption text; reworded choices count as
##       divergences (which is usually what you want to know anyway).
##     * renpy.call_screen stalls automation; warning_screen and
##       player_name_screen are auto-answered, others get True returned and
##       are listed in the report. Add answers via _DP_SCREEN_ANSWERS.
##     * Randomness (renpy.random) is not replayed; flags driven by random
##       rolls can mismatch legitimately.
##
################################################################################

default persistent.dp_replay_pending = None

init -2 python:

    import os as _dp_os
    import re as _dp_re
    import json as _dp_json
    import time as _dp_time
    import importlib as _dp_importlib

    def _dp_mod(name):
        return _dp_importlib.import_module(name)

    _DP_SCREEN_ANSWERS = {
        "warning_screen": True,
        "player_name_screen": "__name__",
    }

    _DP_GAP_TIMEOUT = 300.0

    def _dp_dir():
        path = _dp_os.path.join(config.basedir, "pathtests")
        try:
            _dp_os.makedirs(path, exist_ok=True)
        except Exception:
            pass
        return path

    def _dp_flag_names():
        fn = getattr(store, "_dd_flag_universe", None)
        if fn is not None:
            try:
                names = fn()
                if names:
                    return names
            except Exception:
                pass
        names = []
        rx = _dp_re.compile(r'^default\s+([A-Za-z_]\w*)\s*=')
        for sub in (u"scripts", u""):
            path = _dp_os.path.join(config.gamedir, sub, "flag_defaults.rpy")
            if not _dp_os.path.isfile(path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line in f:
                        m = rx.match(line.strip())
                        if m and not m.group(1).startswith(u"_"):
                            names.append(m.group(1))
            except Exception:
                continue
            if names:
                break
        return names

    def _dp_snapshot_flags():
        out = {}
        for n in _dp_flag_names():
            try:
                v = getattr(store, n, None)
            except Exception:
                continue
            if isinstance(v, (bool, int, float, str)) or v is None:
                out[n] = v
        return out

    def dp_save_path(name=None):
        hist = list(getattr(store, "cx_choice_history", None) or [])
        if not hist:
            renpy.notify("No choices recorded yet, nothing to save")
            return None
        if name is None:
            name = u"path_" + _dp_time.strftime("%Y%m%d_%H%M%S")
        nearest = getattr(store, "_cx_nearest_label", None)
        choices = []
        for h in hist:
            entry = {
                "caption": h.get("caption"),
                "fn": h.get("fn"),
                "ln": h.get("ln"),
            }
            try:
                if nearest:
                    entry["label"] = nearest(h.get("fn", u""), int(h.get("ln") or 0))
            except Exception:
                pass
            choices.append(entry)
        try:
            cur_fn, cur_ln = renpy.get_filename_line()
        except Exception:
            cur_fn, cur_ln = (u"", 0)
        data = {
            "format": 1,
            "name": name,
            "created": _dp_time.strftime("%Y-%m-%d %H:%M:%S"),
            "game_version": getattr(config, "version", u""),
            "end_position": {"fn": cur_fn, "ln": cur_ln},
            "choices": choices,
            "expected_flags": _dp_snapshot_flags(),
        }
        path = _dp_os.path.join(_dp_dir(), name + u".json")
        try:
            with open(path, "w", encoding="utf-8") as f:
                _dp_json.dump(data, f, indent=2, sort_keys=True)
        except Exception as e:
            renpy.notify("Path test save FAILED: " + str(e)[:60])
            return None
        renpy.notify("Path test saved: " + name + " (" + str(len(choices)) + " choices)")
        return path

    def dp_list():
        try:
            return sorted(
                fn[:-5] for fn in _dp_os.listdir(_dp_dir()) if fn.endswith(u".json")
            )
        except Exception:
            return []

    def _dp_state_get():
        return getattr(_dp_state_get, "_st", None)

    def _dp_state_set(st):
        _dp_state_get._st = st

    def dp_active():
        st = _dp_state_get()
        return bool(st) and not st.get("done")

    def dp_replay(name):
        if name not in dp_list():
            renpy.notify("Unknown path test: " + str(name))
            return
        persistent.dp_replay_pending = name
        try:
            renpy.save_persistent()
        except Exception:
            pass
        _dp_restart_exc = getattr(_dp_mod("renpy.game"), "FullRestartException", None)
        try:
            renpy.full_restart()
        except Exception as e:
            if _dp_restart_exc is not None and isinstance(e, _dp_restart_exc):
                raise
            renpy.notify("Pending. Quit and relaunch to run: " + str(name))

    def _dp_recorded_name(st):
        flags = st["data"].get("expected_flags") or {}
        return flags.get("name") or u"Nico"

    ## ---- Engine hooks (tagged so reloads never re-wrap a wrapper) ------------

    def _dp_unwrap(fn):
        while getattr(fn, "_dp_hook", False):
            fn = fn._dp_original
        return fn

    def _dp_install_hooks():
        exports = _dp_mod("renpy.exports")

        orig_display_menu = _dp_unwrap(exports.display_menu)

        def _dp_display_menu(items, *args, **kwargs):
            st = _dp_state_get()
            if not st or st.get("done"):
                return orig_display_menu(items, *args, **kwargs)
            return _dp_pick(st, items, orig_display_menu, args, kwargs)

        _dp_display_menu._dp_hook = True
        _dp_display_menu._dp_original = orig_display_menu
        exports.display_menu = _dp_display_menu

        prev_store_menu = store.menu
        while getattr(prev_store_menu, "_dp_hook", False):
            prev_store_menu = prev_store_menu._dp_original

        def _dp_store_menu(items, *args, **kwargs):
            st = _dp_state_get()
            if not st or st.get("done"):
                return prev_store_menu(items, *args, **kwargs)
            return _dp_pick(st, items, prev_store_menu, args, kwargs)

        _dp_store_menu._dp_hook = True
        _dp_store_menu._dp_original = prev_store_menu
        store.menu = _dp_store_menu

        orig_call_screen = _dp_unwrap(exports.call_screen)

        def _dp_call_screen(_screen_name, *args, **kwargs):
            st = _dp_state_get()
            if not st or st.get("done"):
                return orig_call_screen(_screen_name, *args, **kwargs)
            answers = dict(_DP_SCREEN_ANSWERS)
            answers.update(st["data"].get("screen_answers") or {})
            if _screen_name in answers:
                rv = answers[_screen_name]
            else:
                st["unhandled_screens"].append(str(_screen_name))
                rv = True
            if rv == u"__name__":
                rv = _dp_recorded_name(st)
            try:
                renpy.checkpoint(rv)
            except Exception:
                pass
            _dp_capture_flags(st)
            return rv

        _dp_call_screen._dp_hook = True
        _dp_call_screen._dp_original = orig_call_screen
        exports.call_screen = _dp_call_screen

        orig_input = _dp_unwrap(exports.input)

        def _dp_input(prompt, default=u"", *args, **kwargs):
            st = _dp_state_get()
            if not st or st.get("done"):
                return orig_input(prompt, default, *args, **kwargs)
            return _dp_recorded_name(st)

        _dp_input._dp_hook = True
        _dp_input._dp_original = orig_input
        exports.input = _dp_input

    def _dp_in_menu_context():
        ## 00start sets `renpy.context()._main_menu = True`, and exports.context()
        ## returns game.context().INFO (a per-context info object), NOT the raw
        ## Context. Reading the attr off the raw Context always gave False.
        try:
            game = _dp_mod("renpy.game")
            return bool(getattr(game.context().info, "_main_menu", False))
        except Exception:
            return False

    def _dp_capture_flags(st):
        if _dp_in_menu_context():
            return
        try:
            st["last_flags"] = _dp_snapshot_flags()
            st["snap_ts"] = _dp_time.time()
        except Exception:
            pass

    def _dp_tick():
        st = _dp_state_get()
        if not st or st.get("done"):
            return
        try:
            config.skipping = "fast"
        except Exception:
            pass
        _dp_capture_flags(st)
        if (_dp_time.time() - st.get("progress_ts", 0)) > _DP_GAP_TIMEOUT:
            _dp_finish(st, u"stalled: no choice consumed for {}s".format(int(_DP_GAP_TIMEOUT)))

    config.interact_callbacks = [
        cb for cb in config.interact_callbacks
        if getattr(cb, "__name__", u"") != u"_dp_tick"
    ]
    config.interact_callbacks.append(_dp_tick)

    def _dp_begin(name):
        path = _dp_os.path.join(_dp_dir(), name + u".json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = _dp_json.load(f)
        except Exception as e:
            renpy.notify("Path test load FAILED: " + str(e)[:60])
            return False
        st = {
            "name": name,
            "data": data,
            "idx": 0,
            "divergences": [],
            "unhandled_screens": [],
            "started": _dp_time.time(),
            "progress_ts": _dp_time.time(),
            "done": False,
            "finish_reason": u"",
        }
        _dp_state_set(st)
        _dp_install_hooks()
        try:
            _preferences.skip_unseen = True
            _preferences.skip_after_choices = True
        except Exception:
            pass
        config.skipping = "fast"
        return True

    def _dp_pick(st, items, original, args, kwargs):
        config.skipping = "fast"
        choices = st["data"].get("choices") or []
        idx = st["idx"]

        if idx >= len(choices):
            _dp_finish(st, u"reached the first menu past the recorded path")
            return original(items, *args, **kwargs)

        expected = choices[idx].get("caption")
        for it in items:
            label, value = it[0], it[1]
            if value is None:
                continue
            if label == expected:
                st["idx"] = idx + 1
                st["progress_ts"] = _dp_time.time()
                _dp_capture_flags(st)

                try:
                    ui = _dp_mod("renpy.ui")
                    if isinstance(value, ui.ChoiceReturn):
                        value = value()
                except Exception:
                    pass
                try:
                    renpy.checkpoint(value)
                except Exception:
                    pass
                return value

        st["divergences"].append({
            "at_choice_index": idx,
            "expected": expected,
            "recorded_at": u"{}:{}".format(choices[idx].get("fn", u""), choices[idx].get("ln", 0)),
            "menu_offered": [it[0] for it in items if it[1] is not None],
        })
        _dp_finish(st, u"divergence: expected choice not present in menu")
        return original(items, *args, **kwargs)

    ## ---- Verdict --------------------------------------------------------------

    def _dp_finish(st, reason):
        if not st or st.get("done"):
            return
        st["done"] = True
        st["finish_reason"] = reason
        try:
            config.skipping = None
        except Exception:
            pass

        expected = st["data"].get("expected_flags") or {}

        if _dp_in_menu_context() and st.get("last_flags"):
            actual = st["last_flags"]
            flag_source = u"last in-game snapshot (store resets at the main menu)"
        else:
            actual = _dp_snapshot_flags()
            flag_source = u"live store"

        mismatches = []
        for k in sorted(expected):
            if k in actual and actual[k] != expected[k]:
                mismatches.append((k, expected[k], actual[k]))
        new_flags = sorted(k for k in actual if k not in expected)

        total = len(st["data"].get("choices") or [])
        consumed = st.get("idx", 0)
        divergences = st.get("divergences") or []
        passed = (not mismatches) and (not divergences) and consumed == total \
            and not reason.startswith(u"stalled")

        lines = []
        lines.append(u"Path test: " + st["name"])
        lines.append(u"Recorded on version: " + str(st["data"].get("game_version", u"?")))
        lines.append(u"Replayed on version: " + str(getattr(config, "version", u"?")))
        lines.append(u"Result: " + (u"PASS" if passed else u"FAIL"))
        lines.append(u"Finished because: " + reason)
        lines.append(u"Flags measured from: " + flag_source)
        lines.append(u"Choices consumed: {} / {}".format(consumed, total))
        lines.append(u"Duration: {}s".format(int(_dp_time.time() - st.get("started", 0))))
        if divergences:
            lines.append(u"")
            lines.append(u"Divergences:")
            for d in divergences:
                lines.append(u"  at choice #{} ({}):".format(d["at_choice_index"], d["recorded_at"]))
                lines.append(u"    expected: " + str(d["expected"]))
                lines.append(u"    menu offered: " + u" | ".join(d["menu_offered"]))
        if mismatches:
            lines.append(u"")
            lines.append(u"Flag mismatches (expected -> actual):")
            for k, e, a in mismatches:
                lines.append(u"  {}: {} -> {}".format(k, e, a))
        if st["unhandled_screens"]:
            lines.append(u"")
            lines.append(u"Unhandled call_screen (auto-answered True):")
            for s in sorted(set(st["unhandled_screens"])):
                lines.append(u"  " + s)
        if new_flags:
            lines.append(u"")
            lines.append(u"New flags not in recording (informational):")
            for k in new_flags:
                lines.append(u"  {} = {}".format(k, actual[k]))

        report = u"\n".join(lines) + u"\n"

        try:
            rep_dir = _dp_os.path.join(_dp_dir(), "reports")
            _dp_os.makedirs(rep_dir, exist_ok=True)
            stamp = _dp_time.strftime("%Y%m%d_%H%M%S")
            base = _dp_os.path.join(rep_dir, u"{}_{}".format(st["name"], stamp))
            with open(base + u".txt", "w", encoding="utf-8") as f:
                f.write(report)
            with open(base + u".json", "w", encoding="utf-8") as f:
                _dp_json.dump({
                    "name": st["name"],
                    "passed": passed,
                    "reason": reason,
                    "choices_consumed": consumed,
                    "choices_total": total,
                    "divergences": divergences,
                    "mismatches": [
                        {"flag": k, "expected": e, "actual": a} for k, e, a in mismatches
                    ],
                    "unhandled_screens": sorted(set(st["unhandled_screens"])),
                    "new_flags": {k: actual[k] for k in new_flags},
                }, f, indent=2, sort_keys=True)
        except Exception:
            pass

        print(u"[pathtest] " + (u"PASS" if passed else u"FAIL") + u" " + st["name"] + u": " + reason)

        ## Headless run (launched with the env var): report + stdout is all we
        ## need, so quit. Otherwise keep the game up and show the overlay.
        if _dp_os.environ.get("INTERTWINED_PATHTEST"):
            renpy.quit()

        _dp_finish._last = {
            "name": st["name"],
            "passed": passed,
            ## Double the braces so the text displayable does not eat flag
            ## values as text tags.
            "report": report.replace(u"{", u"{{"),
        }
        try:
            renpy.show_screen("dp_result_overlay")
            renpy.restart_interaction()
        except Exception:
            pass

    def dp_last_result():
        return getattr(_dp_finish, "_last", None)

    def dp_dismiss_result():
        _dp_finish._last = None
        try:
            renpy.hide_screen("dp_result_overlay")
        except Exception:
            pass

init 999 python:
    _dp_env_name = _dp_os.environ.get("INTERTWINED_PATHTEST")
    if _dp_env_name:
        persistent.dp_replay_pending = _dp_env_name.strip()

label before_main_menu:
    if persistent.dp_replay_pending:
        python:
            _dp_pending = persistent.dp_replay_pending
            persistent.dp_replay_pending = None
            renpy.save_persistent()
            if _dp_begin(_dp_pending):
                renpy.jump_out_of_context("start")
    elif dp_active():
        $ _dp_finish(_dp_state_get(), u"game ended and returned to the main menu")
    return

## Result overlay, shown after a replay finishes (at the main menu when the
## route ran to the end, or mid-game on a divergence / end of recording).
screen dp_result_overlay():
    zorder 210

    $ _dp_res = dp_last_result()

    if _dp_res:
        frame:
            align (0.5, 0.5)
            background "#0b0b14ee"
            padding (30, 24)
            xsize 920
            ymaximum 680

            vbox:
                spacing 14
                xfill True

                hbox:
                    spacing 16
                    text ("PASS" if _dp_res["passed"] else "FAIL"):
                        size 36
                        bold True
                        color ("#4ceefc" if _dp_res["passed"] else "#ff5470")
                    text _dp_res["name"]:
                        size 36
                        color "#c2c2ce"
                        yalign 1.0

                viewport:
                    xfill True
                    ymaximum 480
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    text _dp_res["report"]:
                        size 19
                        color "#e8e8f0"
                        substitute False
                        line_spacing 4

                hbox:
                    spacing 32
                    xalign 1.0
                    textbutton "Open reports folder":
                        action Function(dd_open_pathtests)
                        text_size 22
                    textbutton "Close":
                        action Function(dp_dismiss_result)
                        text_size 22

        key "game_menu" action Function(dp_dismiss_result)

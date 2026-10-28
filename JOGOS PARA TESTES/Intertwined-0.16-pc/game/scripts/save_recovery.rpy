################################################################################
## Save-load failure diagnostics & recovery — BlueFox.au v1.2.0
################################################################################
##
## Hooks into config.load_failed_label so that when a save fails to load:
##
################################################################################

init -100 python:
    import os as _sr_os
    import json as _sr_json
    import time as _sr_time
    import traceback as _sr_traceback

    _SR_SHIMS_FILE  = "save_shims.json"

    ## ------------------------------------------------------------------
    ## Path + shim helpers
    ## ------------------------------------------------------------------
    ##

    def _sr_savedir_path(name):
        try:
            return _sr_os.path.join(config.savedir, name)
        except Exception:
            return name

    def _sr_gamedir_path(name):
        try:
            return _sr_os.path.join(config.gamedir, name)
        except Exception:
            return name

    def _sr_read_shims_raw():
        loose = _sr_gamedir_path(_SR_SHIMS_FILE)
        if _sr_os.path.exists(loose):
            try:
                with open(loose, "r", encoding="utf-8") as fh:
                    data = _sr_json.load(fh) or {}
            except Exception:
                data = {}
        else:
            data = {}
            try:
                fh = renpy.file(_SR_SHIMS_FILE)
                try:
                    raw = fh.read()
                    if isinstance(raw, bytes):
                        raw = raw.decode("utf-8", errors="replace")
                    data = _sr_json.loads(raw) or {}
                finally:
                    fh.close()
            except Exception:
                data = {}
        data.setdefault("labels", {})
        return data

    def _sr_write_shims_raw(data):
        try:
            path = _sr_gamedir_path(_SR_SHIMS_FILE)
            dir_ = _sr_os.path.dirname(path) or "."
            ## Serialize FIRST — if it raises, the real file is untouched.
            payload = _sr_json.dumps(data, indent=2, sort_keys=True)
            tmp_path = path + ".tmp"
            with open(tmp_path, "w", encoding="utf-8") as fh:
                fh.write(payload)
            _sr_os.replace(tmp_path, path)
        except Exception:
            try:
                if _sr_os.path.exists(tmp_path):
                    _sr_os.unlink(tmp_path)
            except Exception:
                pass

    def _sr_shims_editable_path():
        return _sr_gamedir_path(_SR_SHIMS_FILE)

    def _sr_apply_label_shims():
        data = _sr_read_shims_raw()
        registered = 0
        for old, new in (data.get("labels") or {}).items():
            if not new:
                continue
            try:
                if renpy.has_label(new):
                    config.label_overrides[old] = new
                    registered += 1
            except Exception:
                pass
        return registered

    ## ------------------------------------------------------------------
    ## State inspection
    ## ------------------------------------------------------------------

    def _sr_current_labels():
        try:
            return set(renpy.game.script.namemap.keys())
        except Exception:
            return set()

    def _sr_missing_labels_from_log():
        current = _sr_current_labels()
        missing = []
        seen = set()
        try:
            entries = getattr(renpy.game.log, "log", None) or []
            for entry in entries:
                ctx = getattr(entry, "context", None)
                if ctx is None:
                    continue
                cur = getattr(ctx, "current", None)
                if not isinstance(cur, str):
                    continue
                if cur in current or cur in seen:
                    continue
                seen.add(cur)
                missing.append(cur)
        except Exception:
            pass
        return missing

    def _sr_position_resolves(cur):
        try:
            return renpy.game.script.has_label(cur)
        except Exception:
            return False

    def _sr_current_serials_by_file():
        serials = {}
        try:
            for name in renpy.game.script.namemap.keys():
                if isinstance(name, tuple) and len(name) >= 2 and isinstance(name[0], str):
                    key = name[0].replace("\\", "/").rsplit("/", 1)[-1]
                    serials.setdefault(key, set()).add(name[1])
        except Exception:
            pass
        return serials

    def _sr_anonymous_positions_from_log():
        buckets = {}
        try:
            entries = getattr(renpy.game.log, "log", None) or []
            for entry in entries:
                ctx = getattr(entry, "context", None)
                if ctx is None:
                    continue
                cur = getattr(ctx, "current", None)
                if isinstance(cur, str):
                    continue
                if not (isinstance(cur, tuple) and len(cur) >= 2):
                    continue
                if _sr_position_resolves(cur):
                    continue
                fname = cur[0]
                serial = cur[1] if len(cur) > 1 else None
                idx    = cur[2] if len(cur) > 2 else None
                key = (fname, serial)
                bucket = buckets.setdefault(key, {"count": 0, "indices": []})
                bucket["count"] += 1
                if len(bucket["indices"]) < 5 and idx is not None:
                    bucket["indices"].append(idx)
        except Exception:
            pass
        result = []
        for (fname, serial), b in buckets.items():
            result.append({
                "file": fname,
                "serial": serial,
                "count": b["count"],
                "example_indices": b["indices"],
            })
        result.sort(key=lambda r: (-r["count"], r["file"] or ""))
        return result

    def _sr_resume_point_info():
        try:
            entries = getattr(renpy.game.log, "log", None) or []
            for entry in reversed(entries):
                ctx = getattr(entry, "context", None)
                cur = getattr(ctx, "current", None) if ctx is not None else None
                if cur is None:
                    continue
                ## Skip entries created by the recovery flow itself — they
                ## resolve in the current script and sit at the end of the
                ## log, hiding the save's real resume point.
                if isinstance(cur, tuple) and _sr_os.path.basename(str(cur[0])) == "save_recovery.rpy":
                    continue
                return cur, _sr_position_resolves(cur)
        except Exception:
            pass
        return None, None

    def _sr_files_missing_summary():
        anons = _sr_anonymous_positions_from_log()
        current = _sr_current_serials_by_file()
        by_file = {}
        for a in anons:
            f = a["file"]
            entry = by_file.setdefault(f, {"file": f, "total": 0, "serials": []})
            entry["total"] += a["count"]
            if a["serial"] is not None and a["serial"] not in entry["serials"]:
                entry["serials"].append(a["serial"])
        result = list(by_file.values())
        for entry in result:
            base = (entry["file"] or "").replace("\\", "/").rsplit("/", 1)[-1]
            entry["current_serials"] = sorted(current.get(base, set()))
        result.sort(key=lambda r: (-r["total"], r["file"] or ""))
        return result

    def _sr_pending_load_slot():
        try:
            slot = renpy.session.get("_sr_last_load_slot")
            if slot:
                return slot
        except Exception:
            pass
        return getattr(renpy.store, "_sr_last_load_slot", None)

    ## ------------------------------------------------------------------
    ## Report writer
    ## ------------------------------------------------------------------

    def _sr_build_report_text():
        missing = _sr_missing_labels_from_log()
        files_summary = _sr_files_missing_summary()
        pending = _sr_pending_load_slot()
        resume_pos, resume_ok = _sr_resume_point_info()

        lines = []
        lines.append("=" * 72)
        lines.append(__("Save load failure at {}").format(
            _sr_time.strftime("%Y-%m-%d %H:%M:%S")))
        try:
            lines.append(__("Game version: {}").format(config.version))
        except Exception:
            pass
        try:
            lines.append(__("Ren'Py version: {}").format(renpy.version()))
        except Exception:
            pass
        if pending:
            lines.append(__("Loading slot: {}").format(pending))
        if resume_pos is not None:
            lines.append(__("Save's resume point: {}  [{}]").format(
                resume_pos,
                __("still exists") if resume_ok else __("MISSING from current script")))
        lines.append("")
        lines.append(__("WHY THE LOAD FAILED: a save can only resume at a statement that"))
        lines.append(__("still exists in the current script. Ren'Py walked the save's"))
        lines.append(__("entire rollback log looking for ANY usable checkpoint and found"))
        lines.append(__("none — every recorded position is listed below with the reason"))
        lines.append(__("it no longer resolves."))
        lines.append("")

        ## ----- Section 1: Named labels missing (shim-recoverable) -----
        if missing:
            lines.append(__("[1] Named labels referenced by the save but MISSING from current script:"))
            for lbl in missing:
                lines.append("      - {}".format(lbl))
            lines.append("")
            lines.append(__("    These are shim-recoverable. To fix future loads of this save:"))
            lines.append(__("      1) Open the shim file in the game folder:"))
            lines.append("           {}".format(_sr_shims_editable_path()))
            lines.append(__("      2) For each label above, set its value to the current label"))
            lines.append(__("         it should map to. Example:"))
            lines.append('           "old_label_name": "new_label_name"')
            lines.append(__("      3) Restart the game. The save will transparently jump to"))
            lines.append(__("         the mapped label on next load."))
            lines.append("")
        else:
            lines.append(__("[1] No named labels missing."))
            lines.append("")

        ## ----- Section 2: Anonymous positions (recompile drift) -----
        if files_summary:
            lines.append(__("[2] Anonymous rollback positions the save can't resolve."))
            lines.append(__("    (Positions that still resolve are not listed — they are not"))
            lines.append(__("    part of the failure.)"))
            lines.append("")
            for f in files_summary:
                serial_bits = ", ".join(str(s) for s in f["serials"])
                lines.append(__("      - {}").format(f["file"] or __("<unknown>")))
                lines.append(__("          {} unresolvable position(s), saved under serial(s): {}").format(
                    f["total"], serial_bits))
                if f["current_serials"]:
                    lines.append(__("          File still exists but was RECOMPILED — current serial(s): {}").format(
                        ", ".join(str(s) for s in f["current_serials"])))
                    lines.append(__("          (Statements were added/removed/edited since the save was made.)"))
                else:
                    lines.append(__("          File NO LONGER EXISTS in the current build."))
            lines.append("")
            lines.append(__("    These positions cannot be shimmed — only named labels can be"))
            lines.append(__("    redirected. Recovery: restore the OLD .rpyc for each file above"))
            lines.append(__("    (from the build the save was made with) into an 'old-game'"))
            lines.append(__("    folder next to the 'game' folder, touch the .rpy, and relaunch."))
            lines.append(__("    Ren'Py will merge the old statement names into the recompile,"))
            lines.append(__("    making the save's positions resolve again."))
            lines.append("")

        if not missing and not files_summary:
            lines.append(__("[3] Neither named labels nor anonymous positions were flagged."))
            lines.append(__("    The failure likely happened before rollback (e.g. while"))
            lines.append(__("    unpickling the save data) — check log.txt / traceback.txt."))
            lines.append("")

        text = "\n".join(lines)

        ## Seed the shim file with unresolved entries for missing labels.
        if missing:
            try:
                data = _sr_read_shims_raw()
                labels = data.setdefault("labels", {})
                changed = False
                for lbl in missing:
                    if lbl not in labels:
                        labels[lbl] = None
                        changed = True
                if changed:
                    data["notes"] = (
                        __("Fill each null value below with the current label a broken save should be redirected to.") + " " +
                        __("Set the value back to null or delete the entry to remove a mapping. Changes take effect on next game launch.")
                        )
                    _sr_write_shims_raw(data)
            except Exception:
                pass

        return text

    def _sr_copy_report_to_clipboard():
        try:
            text = _sr_build_report_text()
        except Exception as e:
            renpy.notify(_("Could not build report: {err}").format(err=str(e)))
            return
        ## Try Ren'Py's exposed clipboard first, then fall back to pygame_sdl2.
        ok = False
        try:
            if hasattr(renpy, "set_clipboard"):
                renpy.set_clipboard(text)
                ok = True
        except Exception:
            pass
        if not ok:
            try:
                import pygame_sdl2
                pygame_sdl2.scrap.put(pygame_sdl2.scrap.SCRAP_TEXT,
                                        text.encode("utf-8"))
                ok = True
            except Exception:
                pass
        if ok:
            renpy.notify(_("Report copied to clipboard."))
        else:
            renpy.notify(_("Could not access clipboard."))

    def _sr_load_failed_callback():
        return "_intertwined_load_failed"

    ## ------------------------------------------------------------------
    ## Track which slot was being loaded (so the recovery UI can name it
    ## and let the user retry / delete it). We wrap the underlying
    ## renpy.loadsave.load so we catch every load path, and mirror the
    ## patch onto renpy.load / renpy.exports.load for good measure.
    ##
    ## The marker is stored on renpy.session (a plain dict that survives
    ## the store-revert triggered by a failed load); we also mirror it
    ## onto the store so old code paths keep working.
    ##
    ## IMPORTANT: the original function must NOT be kept in a store
    ## variable. Init re-runs (Shift+R reload, utter_restart) reset the
    ## store but leave the module patch in place, so a store-based guard
    ## re-hooks the hook and recurses until RecursionError. Instead we tag
    ## the hook function itself (_sr_hook / _sr_original attributes) and
    ## unwrap any existing hooks before installing, and the new hook
    ## closes over the true original.
    ## ------------------------------------------------------------------

    def _sr_install_load_hook():
        try:
            import renpy.loadsave as _sr_loadsave_mod
            import renpy.exports as _sr_exports_mod
        except Exception:
            return

        def _sr_unwrap(fn):
            ## Follow the chain of previously-installed hooks (from
            ## earlier init runs) down to the real renpy function.
            seen = set()
            while getattr(fn, "_sr_hook", False) and id(fn) not in seen:
                seen.add(id(fn))
                fn = getattr(fn, "_sr_original", fn)
            return fn

        def _sr_rebuild_pristine_load():
            ## Last-resort recovery for a poisoned chain: an old-version
            ## hook (no _sr_hook marker, original lost with the store)
            ## sits at the bottom and would NameError when called. The
            ## pristine renpy.loadsave.load is a plain module-level
            ## function using only module globals, so we can rebuild an
            ## identical one by compiling the module source and binding
            ## the extracted code object to the LIVE module's __dict__.
            import types, inspect
            src = inspect.getsource(_sr_loadsave_mod)
            module_code = compile(src, _sr_loadsave_mod.__file__, "exec")
            for const in module_code.co_consts:
                if isinstance(const, types.CodeType) and const.co_name == "load":
                    return types.FunctionType(
                        const, _sr_loadsave_mod.__dict__, "load")
            return None

        try:
            original = _sr_unwrap(_sr_loadsave_mod.load)
        except Exception:
            return

        if getattr(original, "__name__", "") == "_sr_load_hook":
            ## Poisoned chain: a stale hook we can't unwrap. Rebuild the
            ## pristine function; if that fails, install nothing rather
            ## than stacking another broken layer.
            try:
                original = _sr_rebuild_pristine_load()
            except Exception:
                original = None
            if original is None:
                return

        def _sr_load_hook(filename, *args, **kwargs):
            import zipfile
            try:
                renpy.session["_sr_last_load_slot"] = filename
            except Exception:
                pass
            try:
                renpy.store._sr_last_load_slot = filename
            except Exception:
                pass
            try:
                return original(filename, *args, **kwargs)
            except FileNotFoundError:
                renpy.notify(__("Cannot load: The save file is physically missing from your computer."))
                return
            except zipfile.BadZipFile:
                renpy.notify(__("Cannot load: The save file is corrupted and cannot be read."))
                return

        _sr_load_hook._sr_hook = True
        _sr_load_hook._sr_original = original

        ## Patch every re-export of the load function so no caller escapes.
        try:
            _sr_loadsave_mod.load = _sr_load_hook
        except Exception:
            pass
        try:
            renpy.load = _sr_load_hook
        except Exception:
            pass
        try:
            _sr_exports_mod.load = _sr_load_hook
        except Exception:
            pass

    _sr_install_load_hook()

    ## ------------------------------------------------------------------
    ## Cross-platform "open the save folder" helper
    ## ------------------------------------------------------------------

    def _sr_open_savedir():
        import os, sys, subprocess
        path = config.savedir
        try:
            if not os.path.isdir(path):
                os.makedirs(path, exist_ok=True)
            if sys.platform == "win32":
                os.startfile(path)                         # noqa: S606
            elif sys.platform == "darwin":
                subprocess.Popen(["open", path])           # noqa: S603,S607
            else:
                subprocess.Popen(["xdg-open", path])       # noqa: S603,S607
        except Exception:
            pass

    ## ------------------------------------------------------------------
    ## Attempt further rollback from within the recovery label.
    ## ------------------------------------------------------------------

    def _sr_try_deeper_rollback():
        _sr_ctrl = getattr(renpy.game, "CONTROL_EXCEPTIONS", ())
        try:
            limit = getattr(renpy.game.log, "rollback_limit", 0) or 0
            if limit <= 0 and not renpy.game.log.can_rollback():
                renpy.notify(_("No rollback data available."))
                renpy.full_restart()
                return
            ## Ask for a very large number so Ren'Py rolls back as far as
            ## the log physically permits.
            renpy.rollback(force=True, greedy=True, checkpoints=max(limit, 1000))
        except Exception as e:
            if _sr_ctrl and isinstance(e, _sr_ctrl):
                raise
            renpy.notify(_("Rollback failed: {err}").format(err=str(e)))
            renpy.full_restart()

    def _sr_retry_greedy():
        slot = _sr_pending_load_slot()
        if not slot:
            renpy.notify(_("No slot recorded to retry."))
            return
        try:
            renpy.session["_greedy_rollback"] = True
        except Exception:
            pass
        try:
            renpy.load(slot)
        except Exception as e:
            ## renpy.load raises RestartTopContext on success and the recovery
            ## label on failure; if we get any OTHER exception, notify.
            renpy.notify(_("Greedy retry failed: {err}").format(err=str(e)))

    def _sr_delete_broken_slot():
        slot = _sr_pending_load_slot()
        if not slot:
            renpy.notify(_("No slot recorded — open the save browser and delete manually."))
            return
        try:
            renpy.unlink_save(slot)
            renpy.notify(_("Deleted broken save: {slot}").format(slot=slot))
        except Exception as e:
            renpy.notify(_("Delete failed: {err}").format(err=str(e)))

define config.load_failed_label = _sr_load_failed_callback

default _sr_last_load_slot = None

init 100 python:
    try:
        _sr_apply_label_shims()
    except Exception:
        pass

################################################################################
## Recovery UI
################################################################################

label _intertwined_load_failed:
    $ renpy.execute_default_statement(False)
    scene black with dissolve
    call screen sr_load_failed_screen
    return

screen sr_load_failed_screen():
    modal True
    zorder 400

    $ _sr_slot   = _sr_pending_load_slot()
    $ _sr_report = _sr_build_report_text()

    add Solid("#0a050fee")

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 12
            xsize 900

            text _("Save could not be loaded") style "sf_slot_menu_title"

            text _("This save was made against a version of the game that has since changed in a way Ren'Py can't safely resume.") style "sf_slot_menu_subtitle"

            if _sr_slot:
                text _("Slot: [_sr_slot!q]") style "sf_slot_menu_slot"

            null height 4

            ## Full diagnostic report, scrollable. Everything the .txt file
            ## used to hold is now here.
            frame:
                background Solid("#0a050fcc")
                padding (12, 10)
                xfill True

                side "c r":
                    ymaximum 460
                    xfill True

                    viewport:
                        id "sr_scroll_viewport"
                        mousewheel True
                        draggable True
                        pagekeys True
                        xfill True
                        ysize 460

                        text "[_sr_report!q]":
                            style "sf_slot_menu_slot"
                            size 14
                            color "#e8dcf0"

                    vbar value YScrollValue("sr_scroll_viewport"):
                        unscrollable "hide"
                        xsize 8

            null height 8

            ## Two-column action row for the more common actions.
            hbox:
                spacing 8
                xfill True

                textbutton _("Copy report to clipboard"):
                    action Function(_sr_copy_report_to_clipboard)
                    style "sf_slot_menu_item"
                    xsize 446

                textbutton _("Open save folder"):
                    action Function(_sr_open_savedir)
                    style "sf_slot_menu_item"
                    xsize 446

            hbox:
                spacing 8
                xfill True

                textbutton _("Retry with greedy rollback"):
                    action Function(_sr_retry_greedy)
                    style "sf_slot_menu_item"
                    sensitive bool(_sr_slot)
                    xsize 446

                textbutton _("Roll back as far as possible"):
                    action Function(_sr_try_deeper_rollback)
                    style "sf_slot_menu_item"
                    xsize 446

            textbutton _("Delete this broken save"):
                action Confirm(
                    _("Permanently delete this save?\n\nSlot: {slot}\n\nThis cannot be undone.").format(
                        slot=_sr_slot or _("<unknown — no slot recorded>")),
                    yes=Function(_sr_delete_broken_slot),
                )
                style "sf_slot_menu_item_danger"
                sensitive bool(_sr_slot)
                xfill True

            textbutton _("Return to main menu"):
                action [Return()]
                style "sf_slot_menu_item"
                xfill True

    key "K_ESCAPE" action Return()
    key "game_menu" action Return()

################################################################################
## Save / Load browser — folder-aware redesign — BlueFox.au v1.2.0
################################################################################
##
## Replaces the page-row layout in screens.rpy with a sidebar of named folders
## plus a scrollable grid of slots. Players can group saves by route, LI, run,
## or any custom name they like.
##
################################################################################

default persistent.sf_folders = None
default persistent.sf_active_folder = "main"
default persistent.sf_view_mode = "page"   ## "scroll" | "page"
default persistent.sf_sort_mode = "newest"     ## "slot" | "newest"

default sf_grid_page = 0   ## Current page in page view mode
default persistent.sfmigration = None
default persistent.sfmigrated_files = None   ## Filenames already migrated once; never offered again
default persistent.sfmigrated_persistent = None   ## Source dirs whose persistent was imported once
default persistent.sf_migration_reoffer = False   ## If True, previously migrated saves are offered again
default persistent.sf_profile_key_active = None   ## Which profile THIS persistent is (source of truth)
default sf_profile_confirm = None   ## Inline confirm state in the profiles overlay
default sf_profile_name_value = ""   ## Name input in the profiles overlay (snapshot / rename)

default sf_edit_target = None   ## None = idle, "__new__" = creating, "<folder_id>" = renaming
default sf_edit_value = ""

## Per-slot action state (Rename / Move save)
default sf_slot_menu_for = None    ## Full slot name whose action menu is open
default sf_move_source = None    ## Full slot name currently being moved
default sf_rename_target = None    ## Full slot name being renamed
default sf_rename_value = ""
default sf_bulk_mode = False    ## Selection mode for bulk save actions
default sf_bulk_selected = None ## set(full slot names) selected in bulk mode
default sf_bulk_move_modal = False ## Destination picker for bulk move

default _sf_last_label = None   ## Most recent story label, for default save names
default _sf_autoname_last = ""  ## Last auto-applied save name (saved with the game,
## so "did the player customize it?" survives loads)
default persistent.sf_auto_save_name = True   ## Prefill save name from the scene
default persistent.sf_view_tip_seen = False   ## Gear callout dismissed / view options opened once

transform sf_tip_bob:
    block:
        easein 0.5 yoffset -4
        easeout 0.5 yoffset 0
        repeat

init -10 python:
    import json as _sf_json
    import os as _sf_os
    import re as _sf_re
    import shutil as _sf_shutil
    import zlib as _sf_zlib
    import time as _sf_time
    import importlib as _sf_importlib

    SF_DEFAULT_FOLDERS = [
        {"id": "main", "name": "Main", "kind": "user"},
    ]

    SF_LEGACY_RE = r"^[0-9]+-[0-9]+$"

    SF_MIN_SLOTS   = 24
    SF_SLOT_BUFFER = 6

    ## ------------------------------------------------------------------
    ## Episode badge
    ## ------------------------------------------------------------------

    _SF_EP_RE = _sf_re.compile(r"episode_(\d+)\.rpy")

    def _sf_current_episode():
        """Episode number for the current gameplay position"""
        try:
            for ctx in reversed(renpy.game.contexts):
                cur = getattr(ctx, "current", None)
                if cur is None:
                    continue
                if isinstance(cur, tuple) and cur:
                    fname = cur[0]
                else:
                    node = renpy.game.script.lookup_or_none(cur)
                    fname = getattr(node, "filename", "") if node is not None else ""
                m = _SF_EP_RE.search(fname or "")
                if m:
                    return int(m.group(1))
        except Exception:
            pass
        return None

    def _sf_save_json_episode(d):
        ep = _sf_current_episode()
        if ep is not None:
            d["episode"] = ep

    config.save_json_callbacks.append(_sf_save_json_episode)

    ## ------------------------------------------------------------------
    ## Default save name from the current label/scene
    ## ------------------------------------------------------------------

    _SF_SKIP_LABELS = frozenset({
        "start", "quit", "after_load", "after_warp", "splashscreen",
        "before_main_menu", "main_menu", "hide_windows",
    })

    def _sf_track_label(name, abnormal):
        """Remember the last story label the player entered."""
        try:
            if not isinstance(name, str) or name.startswith("_"):
                return
            if name.lower() in _SF_SKIP_LABELS:
                return
            renpy.store._sf_last_label = name
        except Exception:
            pass

    config.label_callbacks.append(_sf_track_label)

    def _sf_prettify(name):
        txt = name.replace("_", " ")
        txt = _sf_re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)
        txt = _sf_re.sub(r"([A-Za-z])(\d)", r"\1 \2", txt)
        txt = _sf_re.sub(r"\s+", " ", txt).strip()
        words = []
        for w in txt.split(" "):
            if w.isupper() or w[:1].isupper():
                words.append(w)
            else:
                words.append(w.capitalize())
        return " ".join(words)[:80]

    def sf_pretty_save_name():
        name = getattr(renpy.store, "_sf_last_label", None)
        if not name or not isinstance(name, str):
            ep = _sf_current_episode()
            if ep is not None:
                return _("Episode {num}").format(num=ep)
            return ""
        return _sf_prettify(name)

    def _sf_all_autonames():
        cache = getattr(_sf_all_autonames, "_cache", None)
        if cache is not None:
            return cache
        items = None
        for _attempt in range(3):
            try:
                items = list(renpy.game.script.namemap.keys())
                break
            except Exception:
                items = None
        if items is None:
            return frozenset()
        try:
            names = set()
            for name in items:
                if isinstance(name, str) and not name.startswith("_") \
                        and name.lower() not in _SF_SKIP_LABELS:
                    names.add(_sf_prettify(name))
            cache = frozenset(names)
            _sf_all_autonames._cache = cache
            return cache
        except Exception:
            return frozenset()

    _SF_EPNAME_RE = _sf_re.compile(r"^Episode \d+$")

    def _sf_is_autoname(text):
        if not text:
            return True
        if text == (getattr(renpy.store, "_sf_autoname_last", "") or "").strip():
            return True
        if _SF_EPNAME_RE.match(text):
            return True
        return text in _sf_all_autonames()

    def sf_apply_default_save_name(mode):
        if mode != "save":
            return
        if persistent.sf_auto_save_name is False:
            return
        try:
            current = (renpy.store.save_name or "").strip()
        except Exception:
            current = ""
        if not _sf_is_autoname(current):
            return
        default = sf_pretty_save_name()
        if default and default != current:
            renpy.store.save_name = default
        if default:
            renpy.store._sf_autoname_last = default

    def sf_slot_episode(slot_name):
        try:
            ep = (renpy.slot_json(slot_name) or {}).get("episode", None)
            return int(ep) if ep is not None else None
        except Exception:
            return None

    def sf_folder_list():
        return persistent.sf_folders or []

    def sf_get_folder(folder_id):
        for f in sf_folder_list():
            if f["id"] == folder_id:
                return f
        return None

    ## System/virtual folders are NOT stored in persistent.sf_folders — they're
    ## rendered directly by the sidebar. Resolution for the header strip etc.
    ## needs to know about them, so callers should use sf_resolve_folder which
    ## falls back through:
    ##   1) the persistent list   (user folders, plus seeded "main")
    ##   2) the synthetic table   (auto / quick / __legacy__)
    ##   3) "main"                (last-ditch heal)
    SF_SYSTEM_FOLDERS = {
        "auto":       {"id": "auto", "name": _("Auto saves"), "kind": "system"},
        "quick":      {"id": "quick", "name": _("Quick saves"), "kind": "system"},
        "__legacy__": {"id": "__legacy__", "name": _("Old saves"), "kind": "legacy"},
    }

    def sf_resolve_folder(folder_id):
        f = sf_get_folder(folder_id)
        if f:
            return f
        sysf = SF_SYSTEM_FOLDERS.get(folder_id)
        if sysf:
            return sysf
        return sf_get_folder("main")

    def sf_user_folders():
        return [f for f in sf_folder_list() if f.get("kind") == "user"]

    def sf_normalize_folders(items=None):
        if items is None:
            source = persistent.sf_folders
            apply_to_persistent = True
        else:
            source = items
            apply_to_persistent = False

        if not isinstance(source, list):
            source = []

        out = []
        seen = set()
        for f in source:
            if not isinstance(f, dict):
                continue
            fid = str(f.get("id", "") or "").strip()
            if not fid or fid in seen:
                continue
            if fid in ("auto", "quick", "__legacy__"):
                continue
            name = (f.get("name", "") or "").strip() or _sf_prettify(fid)
            out.append({"id": fid, "name": name, "kind": "user"})
            seen.add(fid)

        if "main" not in seen:
            out.insert(0, {"id": "main", "name": "Main", "kind": "user"})
        else:
            for i, f in enumerate(out):
                if f["id"] == "main":
                    if i != 0:
                        main = out.pop(i)
                        out.insert(0, main)
                    break

        if apply_to_persistent:
            before = source if isinstance(source, list) else []
            changed = (out != before)
            persistent.sf_folders = out
            return changed

        return out

    def sf_init_folders():
        seeded = False
        if persistent.sf_folders is None:
            persistent.sf_folders = [dict(f) for f in SF_DEFAULT_FOLDERS]
            seeded = True
        return sf_normalize_folders() or seeded

    def sf_detect_missing_folders():
        try:
            names = renpy.list_saved_games(fast=True)
        except Exception:
            return False

        existing = {f.get("id") for f in sf_folder_list() if isinstance(f, dict)}
        created = False

        for slot_name in names:
            if not isinstance(slot_name, str) or "-" not in slot_name:
                continue
            if _sf_re.match(SF_LEGACY_RE, slot_name):
                continue

            folder_id, slot_num = slot_name.rsplit("-", 1)
            if not folder_id or not slot_num.isdigit():
                continue
            if folder_id.startswith("_"):
                continue
            if folder_id in SF_RESERVED_IDS or folder_id in SF_DETECT_IGNORE_IDS:
                continue
            if folder_id in existing:
                continue

            folder_name = _sf_prettify(folder_id)
            persistent.sf_folders.append({"id": folder_id, "name": folder_name, "kind": "user"})
            existing.add(folder_id)
            created = True

        return created

    def sf_refresh_folders_from_disk():
        changed = sf_init_folders()
        if sf_detect_missing_folders():
            changed = True
        if changed:
            sf_write_sidecar()

    def sf_has_legacy_saves():
        try:
            all_names = renpy.list_saved_games(fast=True)
        except Exception:
            return False
        for n in all_names:
            if _sf_re.match(SF_LEGACY_RE, n):
                return True
        return False

    def sf_legacy_saves_sorted():
        try:
            all_names = renpy.list_saved_games(fast=True)
        except Exception:
            return []
        names = [n for n in all_names if _sf_re.match(SF_LEGACY_RE, n)]
        def _mtime(name):
            try:
                return renpy.slot_mtime(name) or 0
            except Exception:
                return 0
        return sorted(names, key=_mtime, reverse=True)

    def sf_slot_count_for_folder(folder_id):
        if folder_id == "auto":
            return max(1, int(getattr(config, "autosave_slots", 24) or 24))
        if folder_id == "quick":
            return max(1, int(getattr(config, "quicksave_slots", 10) or 10))
        try:
            names = renpy.list_saved_games(fast=True)
        except Exception:
            return SF_MIN_SLOTS
        prefix = (folder_id or "") + "-"
        highest = 0
        for n in names:
            if n.startswith(prefix):
                tail = n[len(prefix):]
                if tail.isdigit():
                    slot = int(tail)
                    if slot > highest:
                        highest = slot
        return max(SF_MIN_SLOTS, highest + SF_SLOT_BUFFER)

    SF_PAGE_SIZE = 16   ## 4x4 grid per page in page view mode

    def sf_page_slot_count(folder_id):
        if folder_id in ("auto", "quick"):
            base = sf_slot_count_for_folder(folder_id)
            return ((base + SF_PAGE_SIZE - 1) // SF_PAGE_SIZE) * SF_PAGE_SIZE
        try:
            names = renpy.list_saved_games(fast=True)
        except Exception:
            names = []
        prefix = (folder_id or "") + "-"
        highest = 0
        for n in names:
            if n.startswith(prefix):
                tail = n[len(prefix):]
                if tail.isdigit() and int(tail) > highest:
                    highest = int(tail)
        pages = (SF_MIN_SLOTS + SF_PAGE_SIZE - 1) // SF_PAGE_SIZE
        if highest:
            ## 1-based page holding the highest save, plus one fresh page.
            pages = max(pages, (highest - 1) // SF_PAGE_SIZE + 2)
        return pages * SF_PAGE_SIZE

    def sf_sorted_slots(folder_id):
        if persistent.sf_sort_mode != "newest":
            if persistent.sf_view_mode == "page":
                return list(range(1, sf_page_slot_count(folder_id) + 1))
            return list(range(1, sf_slot_count_for_folder(folder_id) + 1))
        count = sf_slot_count_for_folder(folder_id)
        slots = list(range(1, count + 1))
        mtimes = {}
        for n in slots:
            try:
                mtimes[n] = renpy.slot_mtime("{}-{}".format(folder_id, n)) or 0
            except Exception:
                mtimes[n] = 0
        occupied = [n for n in slots if mtimes[n]]
        empty = [n for n in slots if not mtimes[n]]
        occupied.sort(key=lambda n: mtimes[n], reverse=True)
        return empty[:1] + occupied

    def sf_set_grid_page(page, total_pages):
        renpy.store.sf_grid_page = max(0, min(int(page), int(total_pages) - 1))
        renpy.restart_interaction()

    def sf_open_view_settings():
        persistent.sf_view_tip_seen = True
        renpy.show_screen("sf_view_settings_modal")
        renpy.restart_interaction()

    def sf_dismiss_view_tip():
        persistent.sf_view_tip_seen = True
        renpy.restart_interaction()

    def sf_close_view_settings(restart=True):
        try:
            if renpy.get_screen("sf_view_settings_modal"):
                renpy.hide_screen("sf_view_settings_modal")
        except Exception:
            pass
        if restart:
            renpy.restart_interaction()

    def sf_sanitize_id(name):
        base = _sf_re.sub(r"[^a-z0-9_]+", "_", name.lower()).strip("_")
        return base or "folder"

    def sf_folder_name_key(name):
        return _sf_re.sub(r"[^a-z0-9_]+", "_", (name or "").lower()).strip("_")

    SF_RESERVED_IDS = frozenset({
        "auto", "quick", "main", "legacy", "__legacy__",
        "persistent", "log", "cache", "tmp", "temp", "bak", "backup",
        "sync", "cloud", "steam", "steam_cloud", "renpy",
        "save", "saves", "load", "loads",
        "analytics", "achievements", "gallery",
        "preferences", "settings", "options", "config",
        "new", "none", "null", "default", "folder",
    })

    SF_DETECT_IGNORE_IDS = frozenset({
        "tracesave", "reload",
    })

    def sf_validate_folder_name(name, ignore_id=None):
        raw = (name or "").strip()
        if not raw:
            return (False, _("Folder name can't be empty."))
        if len(raw) > 40:
            return (False, _("Folder name is too long (max 40 characters)."))
        if raw[:1] in ("_", "."):
            return (False, _("Folder names can't start with '_' or '.'."))
        stripped = sf_folder_name_key(raw)
        if not stripped:
            return (False, _("Folder name must contain a letter or number."))
        if stripped.isdigit():
            return (False, _("Folder name can't be only numbers."))
        if stripped in SF_RESERVED_IDS:
            return (False, __("\"{name}\" is a reserved name. Pick another.").format(name=raw))
        existing = {
            sf_folder_name_key(f.get("name", ""))
            for f in sf_folder_list()
            if f.get("id") != ignore_id
        }
        if stripped in existing:
            return (False, __("A folder named \"{name}\" already exists.").format(name=raw))
        return (True, "")

    def sf_new_folder_id(name):
        base = sf_sanitize_id(name)
        existing = {f["id"] for f in sf_folder_list()} | set(SF_RESERVED_IDS)
        if base not in existing:
            return base
        i = 2
        while "{}_{}".format(base, i) in existing:
            i += 1
        return "{}_{}".format(base, i)

    def sf_write_sidecar():
        try:
            path = _sf_os.path.join(config.savedir, "save_folders.json")
            payload = {"version": 1, "active": persistent.sf_active_folder, "folders": list(sf_folder_list())}
            with open(path, "w", encoding="utf-8") as fh:
                _sf_json.dump(payload, fh, indent=2)
        except Exception:
            pass

    def sf_read_sidecar():
        try:
            path = _sf_os.path.join(config.savedir, "save_folders.json")
            if not _sf_os.path.exists(path):
                return
            with open(path, "r", encoding="utf-8") as fh:
                data = _sf_json.load(fh)
            sidecar_folders = data.get("folders") or []
            if not sidecar_folders:
                return
            current = sf_folder_list()
            if len(current) <= 1 and len(sidecar_folders) > 1:
                persistent.sf_folders = sf_normalize_folders(sidecar_folders)
                if data.get("active"):
                    persistent.sf_active_folder = data["active"]
        except Exception:
            pass

    def sf_create_finish(name):
        name = (name or "").strip()
        if not name:
            return
        ok, err = sf_validate_folder_name(name)
        if not ok:
            renpy.notify(err)
            return
        fid = sf_new_folder_id(name)
        persistent.sf_folders.append({"id": fid, "name": name, "kind": "user"})
        sf_write_sidecar()
        sf_select(fid)

    def sf_rename_finish(folder_id, new_name):
        f = sf_get_folder(folder_id)
        if not f:
            return
        new_name = (new_name or "").strip()
        if not new_name:
            return
        if new_name == f.get("name"):
            return
        ok, err = sf_validate_folder_name(new_name, ignore_id=folder_id)
        if not ok:
            renpy.notify(err)
            return
        f["name"] = new_name
        sf_write_sidecar()

    def sf_commit_edit(value):
        target = renpy.store.sf_edit_target
        if target == "__new__":
            sf_create_finish(value)
        elif target:
            sf_rename_finish(target, value)
        renpy.store.sf_edit_target = None
        renpy.store.sf_edit_value  = ""
        renpy.restart_interaction()

    def sf_cancel_edit():
        renpy.store.sf_edit_target = None
        renpy.store.sf_edit_value  = ""
        renpy.restart_interaction()

    def sf_delete_folder(folder_id):
        f = sf_get_folder(folder_id)
        if not f or f.get("kind") != "user" or folder_id == "main":
            return
        prefix = folder_id + "-"
        try:
            all_names = renpy.list_saved_games(fast=True)
        except Exception:
            all_names = []
        victims = [n for n in all_names
                    if n.startswith(prefix) and n[len(prefix):].isdigit()]
        for name in victims:
            try:
                renpy.unlink_save(name)
            except Exception:
                pass
        persistent.sf_folders = [x for x in persistent.sf_folders if x["id"] != folder_id]
        sf_write_sidecar()
        if persistent.sf_active_folder == folder_id:
            sf_select("main")
        try:
            renpy.scan_saved_game.cache_clear()
        except Exception:
            pass

    def sf_delete_legacy_saves():
        for name in sf_legacy_saves_sorted():
            try:
                renpy.unlink_save(name)
            except Exception:
                pass
        if persistent.sf_active_folder == "__legacy__":
            sf_select("main")
        try:
            renpy.scan_saved_game.cache_clear()
        except Exception:
            pass
        renpy.restart_interaction()

    ## --------------------------------------------------------------
    ## Focused-slot tracking for keyboard / controller delete (Y / H).
    ## Each sf_slot_tile sets these via its hovered / unhovered hooks;
    ## sf_save_browser binds K_h and pad_y_press to sf_delete_focused.
    ## --------------------------------------------------------------
    sf_focused_slot = None  # (target, full_slot) or None

    def sf_focus_slot(target, full_slot):
        global sf_focused_slot
        sf_focused_slot = (target, full_slot)

    def sf_unfocus_slot(target, full_slot):
        global sf_focused_slot
        if sf_focused_slot == (target, full_slot):
            sf_focused_slot = None

    def sf_delete_focused():
        if sf_focused_slot is None:
            return
        if renpy.store.sf_move_source is not None:
            return
        if renpy.store.sf_slot_menu_for is not None:
            return
        if renpy.store.sf_rename_target is not None:
            return
        target, slot = sf_focused_slot
        renpy.run(FileDelete(target, slot=slot))
        renpy.restart_interaction()

    ## --------------------------------------------------------------
    ## Bulk selection / actions
    ## --------------------------------------------------------------

    def sf_bulk_set():
        sel = renpy.store.sf_bulk_selected
        if not isinstance(sel, set):
            sel = set(sel) if sel else set()
            renpy.store.sf_bulk_selected = sel
        return sel

    def sf_bulk_clear():
        renpy.store.sf_bulk_selected = set()

    def sf_bulk_close_move_modal():
        renpy.store.sf_bulk_move_modal = False
        try:
            if renpy.get_screen("sf_bulk_move_modal"):
                renpy.hide_screen("sf_bulk_move_modal")
        except Exception:
            pass

    def sf_bulk_disable():
        renpy.store.sf_bulk_mode = False
        sf_bulk_clear()
        sf_bulk_close_move_modal()
        renpy.restart_interaction()

    def sf_bulk_enable():
        renpy.store.sf_bulk_mode = True
        sf_bulk_clear()
        sf_bulk_close_move_modal()
        sf_close_slot_menu()
        sf_cancel_move()
        renpy.restart_interaction()

    def sf_bulk_count():
        return len(sf_bulk_set())

    def sf_bulk_is_selected(slot_name):
        return slot_name in sf_bulk_set()

    def sf_bulk_toggle(slot_name):
        sel = sf_bulk_set()
        if slot_name in sel:
            sel.remove(slot_name)
        else:
            sel.add(slot_name)
        renpy.store.sf_bulk_selected = sel
        renpy.restart_interaction()

    def sf_bulk_candidate_slots_current_view():
        """Selectable (occupied) slot names in the current visible section."""
        fid = persistent.sf_active_folder
        if fid == "__legacy__":
            return [name for name in sf_legacy_saves_sorted() if sf_slot_is_occupied(name)]

        out = []
        for n in sf_sorted_slots(fid):
            full = "{}-{}".format(fid, n)
            if sf_slot_is_occupied(full):
                out.append(full)
        return out

    def sf_bulk_select_all_current_view():
        names = sf_bulk_candidate_slots_current_view()
        renpy.store.sf_bulk_selected = set(names)
        renpy.notify(__("Selected {count} save(s).").format(count=len(names)))
        renpy.restart_interaction()

    def sf_bulk_move_dest_folders():
        current = persistent.sf_active_folder
        return [f for f in sf_user_folders() if f.get("id") != current]

    def sf_bulk_open_move_modal():
        if not sf_bulk_count():
            renpy.notify(_("Select one or more saves first."))
            return
        if not sf_bulk_move_dest_folders():
            renpy.notify(_("No destination folder available."))
            return
        renpy.store.sf_bulk_move_modal = True
        renpy.show_screen("sf_bulk_move_modal")
        renpy.restart_interaction()

    def _sf_first_free_slot(folder_id, start_at=1):
        n = max(1, int(start_at or 1))
        while sf_slot_is_occupied("{}-{}".format(folder_id, n)):
            n += 1
        return n

    def sf_bulk_move_selected_to(folder_id):
        dest_folder = sf_get_folder(folder_id)
        if not dest_folder or dest_folder.get("kind") != "user":
            renpy.notify(_("Invalid destination folder."))
            return

        selected = list(sf_bulk_set())
        if not selected:
            renpy.notify(_("No saves selected."))
            return

        moved = 0
        failed = 0
        skipped = 0

        for source in selected:
            if not sf_slot_is_occupied(source):
                continue

            tail = ""
            if isinstance(source, str) and "-" in source:
                _prefix, tail = source.rsplit("-", 1)

            preferred = int(tail) if tail.isdigit() else 1
            if sf_slot_is_occupied("{}-{}".format(folder_id, preferred)):
                preferred = _sf_first_free_slot(folder_id, preferred)

            dest = "{}-{}".format(folder_id, preferred)
            if dest == source:
                skipped += 1
                continue

            try:
                renpy.rename_save(source, dest)
                moved += 1
            except Exception:
                try:
                    fallback_n = _sf_first_free_slot(folder_id, 1)
                    fallback = "{}-{}".format(folder_id, fallback_n)
                    if fallback != source:
                        renpy.rename_save(source, fallback)
                        moved += 1
                    else:
                        skipped += 1
                except Exception:
                    failed += 1

        renpy.store.sf_bulk_mode = False
        sf_bulk_clear()
        sf_bulk_close_move_modal()
        _sf_scan_cache_clear()
        renpy.restart_interaction()

        if failed:
            renpy.notify(__("Moved {ok} save(s), skipped {skip}, {bad} failed.").format(ok=moved, skip=skipped, bad=failed))
        else:
            renpy.notify(__("Moved {ok} save(s), skipped {skip}.").format(ok=moved, skip=skipped))

    def sf_bulk_delete_selected():
        sel = list(sf_bulk_set())
        if not sel:
            renpy.notify(_("No saves selected."))
            return

        deleted = 0
        failed = 0
        for slot_name in sel:
            if not sf_slot_is_occupied(slot_name):
                continue
            try:
                renpy.unlink_save(slot_name)
                deleted += 1
            except Exception:
                failed += 1

        renpy.store.sf_bulk_mode = False
        sf_bulk_clear()
        _sf_scan_cache_clear()
        renpy.restart_interaction()
        if failed:
            renpy.notify(__("Deleted {ok} save(s), {bad} failed.").format(ok=deleted, bad=failed))
        else:
            renpy.notify(__("Deleted {ok} save(s).").format(ok=deleted))

    ## --------------------------------------------------------------
    ## Per-slot actions: Rename / Move / Delete via floating menu.
    ## --------------------------------------------------------------

    def sf_full_slot_name(target, full_slot):
        if full_slot:
            return target
        return "{}-{}".format(persistent.sf_active_folder, target)

    def sf_slot_is_occupied(slot_name):
        try:
            return bool(renpy.slot_mtime(slot_name))
        except Exception:
            return False

    def sf_active_folder_accepts_drop():
        """User folders (including 'main') accept move destinations.
        Auto / quick / legacy do not."""
        fid = persistent.sf_active_folder
        f = sf_get_folder(fid)
        return bool(f and f.get("kind") == "user")

    def _sf_scan_cache_clear():
        try:
            renpy.scan_saved_game.cache_clear()
        except Exception:
            pass

    def sf_open_slot_menu(slot_name):
        renpy.store.sf_slot_menu_for = slot_name
        renpy.show_screen("sf_slot_menu_popup", slot_name)
        renpy.restart_interaction()

    def sf_close_slot_menu():
        renpy.store.sf_slot_menu_for = None
        try:
            if renpy.get_screen("sf_slot_menu_popup"):
                renpy.hide_screen("sf_slot_menu_popup")
        except Exception:
            pass
        renpy.restart_interaction()

    def sf_begin_move(slot_name):
        sf_close_slot_menu()
        renpy.store.sf_move_source = slot_name
        renpy.restart_interaction()

    def sf_cancel_move():
        renpy.store.sf_move_source = None
        renpy.restart_interaction()

    def sf_perform_move(dest_slot_name):
        source = renpy.store.sf_move_source
        if not source:
            return
        if source == dest_slot_name:
            sf_cancel_move()
            return
        dest_occupied = sf_slot_is_occupied(dest_slot_name)
        swap_tmp = None
        stage = 0
        try:
            if dest_occupied:
                base = "__sf_move_swap__"
                swap_tmp = base
                n = 2
                while sf_slot_is_occupied(swap_tmp):
                    swap_tmp = "{}_{}".format(base, n)
                    n += 1

                renpy.rename_save(source, swap_tmp)
                stage = 1
                renpy.rename_save(dest_slot_name, source)
                stage = 2
                renpy.rename_save(swap_tmp, dest_slot_name)
                stage = 3
            else:
                renpy.rename_save(source, dest_slot_name)
        except Exception as e:
            if dest_occupied and swap_tmp:
                try:
                    if stage == 1:
                        if sf_slot_is_occupied(swap_tmp) and not sf_slot_is_occupied(source):
                            renpy.rename_save(swap_tmp, source)
                    elif stage == 2:
                        if sf_slot_is_occupied(source) and not sf_slot_is_occupied(dest_slot_name):
                            renpy.rename_save(source, dest_slot_name)
                        if sf_slot_is_occupied(swap_tmp) and not sf_slot_is_occupied(source):
                            renpy.rename_save(swap_tmp, source)
                except Exception:
                    pass
            renpy.notify(__("Move failed: {err}").format(err=str(e)))
            renpy.store.sf_move_source = None
            _sf_scan_cache_clear()
            renpy.restart_interaction()
            return
        renpy.store.sf_move_source = None
        _sf_scan_cache_clear()
        if dest_occupied:
            renpy.notify(_("Swapped saves."))
        else:
            renpy.notify(_("Save moved."))
        renpy.restart_interaction()

    def sf_begin_rename(slot_name):
        try:
            data = renpy.slot_json(slot_name) or {}
        except Exception:
            data = {}
        sf_close_slot_menu()
        renpy.store.sf_rename_target = slot_name
        renpy.store.sf_rename_value = data.get("_save_name", "") or ""
        renpy.show_screen("sf_rename_modal")
        try:
            osk_force_show()
        except Exception:
            pass
        renpy.restart_interaction()

    def sf_cancel_rename():
        renpy.store.sf_rename_target = None
        renpy.store.sf_rename_value = ""
        try:
            if renpy.get_screen("sf_rename_modal"):
                renpy.hide_screen("sf_rename_modal")
        except Exception:
            pass
        try:
            osk_force_hide()
        except Exception:
            pass
        renpy.restart_interaction()

    def _sf_rewrite_save_name(slot_name, new_name):
        import zipfile, tempfile
        path = _sf_os.path.join(config.savedir, slot_name + renpy.savegame_suffix)
        if not _sf_os.path.exists(path):
            return False, _("Save file not found.")
        try:
            entries = []
            with zipfile.ZipFile(path, "r") as zin:
                for info in zin.infolist():
                    entries.append((info, zin.read(info.filename)))
        except Exception as e:
            return False, __("Could not open save: {err}").format(err=str(e))
        rewritten = []
        found_json = False
        for info, blob in entries:
            if info.filename == "json":
                try:
                    data = _sf_json.loads(blob) if blob else {}
                except Exception:
                    data = {}
                data["_save_name"] = new_name
                rewritten.append((info, _sf_json.dumps(data).encode("utf-8")))
                found_json = True
            else:
                rewritten.append((info, blob))
        if not found_json:
            info = zipfile.ZipInfo("json")
            rewritten.append((info, _sf_json.dumps({"_save_name": new_name}).encode("utf-8")))
        dir_ = _sf_os.path.dirname(path)
        tmp_fd, tmp_path = tempfile.mkstemp(prefix="._sf_rename_", suffix=".tmp", dir=dir_)
        _sf_os.close(tmp_fd)
        try:
            with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
                for info, blob in rewritten:
                    new_info = zipfile.ZipInfo(info.filename, date_time=info.date_time)
                    new_info.compress_type = zipfile.ZIP_DEFLATED
                    zout.writestr(new_info, blob)
            _sf_os.replace(tmp_path, path)
        except Exception as e:
            try:
                _sf_os.unlink(tmp_path)
            except Exception:
                pass
            return False, __("Rewrite failed: {err}").format(err=str(e))
        return True, ""

    def _sf_force_refresh(slot_name):
        try:
            renpy.loadsave.location.scan()
        except Exception:
            pass
        try:
            renpy.loadsave.clear_slot(slot_name)
        except Exception:
            pass
        _sf_scan_cache_clear()

    def sf_commit_rename():
        target = renpy.store.sf_rename_target
        value = (renpy.store.sf_rename_value or "").strip()
        if not target:
            return
        if len(value) > 80:
            renpy.notify(_("Save name is too long (max 80 characters)."))
            return
        ok, err = _sf_rewrite_save_name(target, value)
        if not ok:
            renpy.notify(err)
            return
        _sf_force_refresh(target)
        renpy.store.sf_rename_target = None
        renpy.store.sf_rename_value = ""
        try:
            if renpy.get_screen("sf_rename_modal"):
                renpy.hide_screen("sf_rename_modal")
        except Exception:
            pass
        try:
            osk_force_hide()
        except Exception:
            pass
        renpy.notify(_("Save renamed."))
        renpy.restart_interaction()

    def sf_select(folder_id):
        persistent.sf_active_folder = folder_id
        renpy.store.sf_grid_page = 0
        f = sf_get_folder(folder_id)
        if f and f.get("kind") == "user":
            renpy.run(FilePage(folder_id))
        elif folder_id == "auto":
            renpy.run(FilePage("auto"))
        elif folder_id == "quick":
            renpy.run(FilePage("quick"))
        renpy.restart_interaction()

    def sf_sync_filepage():
        fid = persistent.sf_active_folder
        if fid == "__legacy__":
            return
        target = None
        if fid in ("auto", "quick"):
            target = fid
        else:
            f = sf_get_folder(fid)
            if f and f.get("kind") == "user":
                target = fid
            else:
                target = "main"
                persistent.sf_active_folder = "main"
        if persistent._file_page != target:
            persistent._file_page = target

    def sf_current_save_dir_name():
        return str(getattr(config, "save_directory", "") or "")

    def sf_paired_migration_source_name():
        current = sf_current_save_dir_name().strip()
        if not current:
            return None

        if current.lower().endswith("_steam"):
            return current[:-6] or None

        return current + "_Steam"

    def sf_resolve_migration_source_names():
        current = sf_current_save_dir_name().strip()
        names = []

        paired = sf_paired_migration_source_name()
        if paired and paired != current:
            names.append(paired)

        dst_dir = getattr(config, "savedir", None) or ""
        root = _sf_os.path.dirname(dst_dir) if dst_dir else ""
        if root and _sf_os.path.isdir(root):
            try:
                entries = sorted(_sf_os.listdir(root))
            except Exception:
                entries = []
            for entry in entries:
                if not entry.startswith("Intertwined-"):
                    continue
                if entry == current or entry in names:
                    continue
                if _sf_os.path.isdir(_sf_os.path.join(root, entry)):
                    names.append(entry)

        return names

    def sf_get_migration_paths():
        dst_dir = getattr(config, "savedir", None) or ""
        if not dst_dir:
            return ([], None)
        root = _sf_os.path.dirname(dst_dir)
        sources = []
        for name in sf_resolve_migration_source_names():
            src_dir = _sf_os.path.join(root, name)
            if _sf_os.path.isdir(src_dir):
                sources.append((name, src_dir))
        return (sources, dst_dir)

    def sf_list_save_files_in_dir(path):
        if not path or not _sf_os.path.isdir(path):
            return []
        suffix = str(getattr(renpy, "savegame_suffix", ".save") or ".save")
        out = []
        try:
            for fn in _sf_os.listdir(path):
                if fn.startswith(("auto-", "quick-")):
                    continue
                full = _sf_os.path.join(path, fn)
                if _sf_os.path.isfile(full) and fn.endswith(suffix):
                    out.append(fn)
        except Exception:
            return []
        return sorted(out)

    def _sf_migrated_record():
        rec = persistent.sfmigrated_files
        if not isinstance(rec, dict):
            rec = {}
            persistent.sfmigrated_files = rec
        return rec

    def _sf_migration_seen_path():
        try:
            return _sf_os.path.join(config.savedir, "sf_migrated_seen.json")
        except Exception:
            return None

    def _sf_migration_seen_key(src_name, filename):
        src = (src_name or "").strip().lower()
        fn = (filename or "").strip().lower()
        return u"{}::{}".format(src, fn)

    def _sf_migrated_seen_disk():
        p = _sf_migration_seen_path()
        if not p or not _sf_os.path.isfile(p):
            return set()
        try:
            with open(p, "r", encoding="utf-8") as fh:
                data = _sf_json.load(fh)
            if not isinstance(data, dict):
                return set()
            keys = data.get("keys") or []
            if not isinstance(keys, list):
                return set()
            return set(str(k) for k in keys if k)
        except Exception:
            return set()

    def _sf_migrated_seen_disk_save(keys):
        p = _sf_migration_seen_path()
        if not p:
            return
        try:
            payload = {
                "version": 1,
                "keys": sorted(set(str(k) for k in (keys or []) if k)),
            }
            with open(p, "w", encoding="utf-8") as fh:
                _sf_json.dump(payload, fh, indent=2)
        except Exception:
            pass

    def _sf_mark_migrated_seen(src_name, filename):
        if not filename:
            return
        rec = _sf_migrated_record()
        rec[filename] = True
        rec[_sf_migration_seen_key(src_name, filename)] = True

        seen = _sf_migrated_seen_disk()
        seen.add(_sf_migration_seen_key(src_name, filename))
        _sf_migrated_seen_disk_save(seen)

    def _sf_is_migrated_seen(src_name, filename):
        if persistent.sf_migration_reoffer:
            return False

        rec = _sf_migrated_record()
        if rec.get(filename):
            return True
        key = _sf_migration_seen_key(src_name, filename)
        if rec.get(key):
            return True
        return key in _sf_migrated_seen_disk()

    ## ------------------------------------------------------------------
    ## Persistent (progress / unlocks) migration
    ## ------------------------------------------------------------------

    def _sf_migrated_persist_record():
        rec = persistent.sfmigrated_persistent
        if not isinstance(rec, dict):
            rec = {}
            persistent.sfmigrated_persistent = rec
        return rec

    def sf_find_persistent_file(src_dir):
        for fn in ("persistent.new", "persistent"):
            p = _sf_os.path.join(src_dir, fn)
            try:
                if _sf_os.path.isfile(p) and _sf_os.path.getsize(p) > 0:
                    return p
            except Exception:
                continue
        return None

    def sf_pending_persist_sources():
        sources, _dst = sf_get_migration_paths()
        rec = _sf_migrated_persist_record()
        out = []
        for name, src_dir in sources:
            if rec.get(name):
                continue
            p = sf_find_persistent_file(src_dir)
            if not p:
                continue
            prof = _sf_os.path.join(
                _sf_profiles_dir(), _SF_PROFILE_PREFIX + sf_profile_key(name))
            if _sf_os.path.isfile(prof):
                continue
            out.append((name, p))
        return out

    def _sf_load_old_persistent(path):
        pmod = _sf_importlib.import_module("renpy.persistent")
        try:
            other = pmod.load(path)
            if other is not None:
                return other
        except Exception:
            pass
        try:
            _loads = _sf_importlib.import_module("renpy.compat.pickle").loads
            with open(path, "rb") as f:
                do = _sf_zlib.decompressobj()
                data = do.decompress(f.read())
            other = _loads(data)
            other._update()
            return other
        except Exception:
            return None

    ## ------------------------------------------------------------------
    ## Persistent profiles: switchable progress files
    ## ------------------------------------------------------------------
    ##
    ## A profile is a full persistent file (unlocks, seen scenes, playtime,
    ## settings) stored next to the live one as persistent_profile_<key>.
    ## Migration imports the old install's persistent as a profile instead
    ## of touching the live data; the sf_profiles_modal overlay lets the
    ## player switch (restart required), merge unlocks in, or delete.
    ##
    ## Switching cannot happen in-place: the live Persistent object is
    ## referenced all over the running engine (renpy.game.preferences is
    ## persistent._preferences, the backup diff dict, the scan thread's
    ## auto-merge). So a switch stashes the live file, swaps the chosen
    ## file in, blocks the engine from saving over it, and relaunches.

    _SF_PROFILE_PREFIX = "persistent_profile_"
    _SF_PROFILE_SIDECAR = "persistent_profiles.json"

    def _sf_profiles_dir():
        return getattr(config, "savedir", None) or ""

    def _sf_profile_meta_load():
        path = _sf_os.path.join(_sf_profiles_dir(), _SF_PROFILE_SIDECAR)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = _sf_json.load(f)
            if isinstance(data, dict):
                data.setdefault("active", "main")
                data.setdefault("names", {})
                return data
        except Exception:
            pass
        return {"active": "main", "names": {}}

    def _sf_profile_meta_save(meta):
        try:
            path = _sf_os.path.join(_sf_profiles_dir(), _SF_PROFILE_SIDECAR)
            with open(path, "w", encoding="utf-8") as f:
                _sf_json.dump(meta, f, indent=2)
        except Exception:
            pass

    def sf_profile_key(name):
        base = _sf_re.sub(r"[^a-z0-9_]+", "_", (name or "").lower()).strip("_")
        return base or "profile"

    def _sf_active_profile_key():
        return sf_profile_key(getattr(persistent, "sf_profile_key_active", None) or "main")

    def _sf_profile_display(key, names):
        return names.get(key) or (_("This install") if key == "main" else key)

    def _sf_profile_path(key):
        return _sf_os.path.join(_sf_profiles_dir(), _SF_PROFILE_PREFIX + sf_profile_key(key))

    def _sf_write_persistent_file(path, obj):
        dumps = _sf_importlib.import_module("renpy.compat.pickle").dumps
        st = _sf_importlib.import_module("renpy.savetoken")
        data = dumps(obj)
        out = _sf_zlib.compress(data, 3) + (st.sign_data(data) or "").encode("utf-8")
        tmp = path + ".tmp"
        with open(tmp, "wb") as f:
            f.write(out)
        _sf_os.replace(tmp, path)

    def sf_profiles_exist():
        root = _sf_profiles_dir()
        try:
            return any(
                fn.startswith(_SF_PROFILE_PREFIX) and not fn.endswith(".tmp")
                for fn in _sf_os.listdir(root)
            )
        except Exception:
            return False

    def _sf_persist_summary_text(obj, live=False):
        try:
            seen = obj._seen_ever or {}
        except Exception:
            seen = {}
        scenes = 0
        labels_fn = getattr(store, "_ps_script_labels", None)
        if labels_fn is not None:
            try:
                scenes = sum(1 for l in (labels_fn() or ()) if l in seen)
            except Exception:
                scenes = 0
        if not scenes:
            try:
                scenes = sum(1 for k in seen if isinstance(k, str) and not k.startswith("_"))
            except Exception:
                scenes = 0
        try:
            ch = obj.cx_seen_choices
            choices = len(ch) if isinstance(ch, (set, frozenset, dict, list)) else 0
        except Exception:
            choices = 0
        secs = 0
        if live:
            live_fn = getattr(store, "ps_lifetime_seconds_live", None)
            if live_fn is not None:
                try:
                    secs = int(live_fn() or 0)
                except Exception:
                    secs = 0
        if not secs:
            try:
                secs = int(getattr(obj, "ps_lifetime_seconds", 0) or 0)
            except Exception:
                secs = 0
        fmt = getattr(store, "ps_format_duration", None)
        if fmt is not None:
            dur = fmt(secs)
        else:
            dur = "{}h {:02d}m".format(secs // 3600, (secs % 3600) // 60)
        return __("{dur} played  \u00b7  {scenes} scenes seen  \u00b7  {choices} choices").format(
            dur=dur, scenes=scenes, choices=choices)

    def sf_profile_live_summary():
        try:
            return _sf_persist_summary_text(persistent, live=True)
        except Exception:
            return ""

    def sf_profile_summary(path, mtime):
        cache = getattr(sf_profile_summary, "_cache", None)
        if cache is None:
            cache = {}
            sf_profile_summary._cache = cache
        ck = (path, mtime)
        if ck in cache:
            return cache[ck]
        obj = _sf_load_old_persistent(path)
        txt = _("(unreadable)") if obj is None else _sf_persist_summary_text(obj)
        if len(cache) > 32:
            cache.clear()
        cache[ck] = txt
        return txt

    def _sf_commit_playtime():
        commit = getattr(store, "_ps_commit_runtime", None)
        if commit is not None:
            try:
                commit()
            except Exception:
                pass

    def sf_profile_rows():
        root = _sf_profiles_dir()
        meta = _sf_profile_meta_load()
        names = meta.get("names") or {}
        active_key = _sf_active_profile_key()
        rows = []
        try:
            entries = _sf_os.listdir(root)
        except Exception:
            return rows
        for fn in sorted(entries):
            if not fn.startswith(_SF_PROFILE_PREFIX) or fn.endswith(".tmp"):
                continue
            key = fn[len(_SF_PROFILE_PREFIX):]
            if not key or key == active_key:
                continue
            path = _sf_os.path.join(root, fn)
            try:
                mtime = _sf_os.path.getmtime(path)
            except Exception:
                continue
            display = _sf_profile_display(key, names)
            rows.append({
                "key": key,
                "name": display,
                "mtime": mtime,
                "last_used": _sf_time.strftime("%d %b %Y, %H:%M", _sf_time.localtime(mtime)),
                "summary": sf_profile_summary(path, mtime),
            })
        rows.sort(key=lambda r: r["mtime"], reverse=True)
        return rows

    def sf_import_persist_as_profile(name, ppath):
        obj = _sf_load_old_persistent(ppath)
        if obj is None:
            return False
        try:
            rec = obj.sfmigrated_persistent
            if not isinstance(rec, dict):
                rec = {}
            for n in sf_resolve_migration_source_names():
                rec[n] = True
            obj.sfmigrated_persistent = rec
            try:
                obj._changed["sfmigrated_persistent"] = _sf_time.time()
            except Exception:
                pass
        except Exception:
            pass
        root = _sf_profiles_dir()
        if not root:
            return False
        key = sf_profile_key(name)
        path = _sf_profile_path(key)
        if _sf_os.path.exists(path):
            return True   ## already imported once, never overwrite
        _sf_write_persistent_file(path, obj)
        meta = _sf_profile_meta_load()
        meta["names"][key] = name
        _sf_profile_meta_save(meta)
        return True

    def _sf_profile_unique_key(name):
        base = sf_profile_key(name)
        key = base
        n = 2
        while _sf_os.path.exists(_sf_profile_path(key)):
            key = "{}_{}".format(base, n)
            n += 1
        return key

    def sf_profile_snapshot(name=None, notify=True):
        name = (name or "").strip()
        if not name:
            name = _sf_time.strftime("Restore point %d %b %Y, %H:%M")
        root = _sf_profiles_dir()
        live = _sf_os.path.join(root, "persistent")
        try:
            _sf_commit_playtime()
            renpy.save_persistent()
            key = _sf_profile_unique_key(name)
            _sf_shutil.copy2(live, _sf_profile_path(key))
        except Exception:
            if notify:
                renpy.notify(_("Could not create the profile."))
            return None
        meta = _sf_profile_meta_load()
        meta["names"][key] = name
        _sf_profile_meta_save(meta)
        if notify:
            renpy.notify(__("Current progress stored as '{name}'.").format(name=name))
        return key

    def sf_profile_cancel_input():
        store.sf_profile_name_value = ""
        store.sf_profile_confirm = None
        renpy.restart_interaction()

    def sf_profile_commit_snapshot():
        sf_profile_snapshot(store.sf_profile_name_value)
        store.sf_profile_name_value = ""
        store.sf_profile_confirm = None
        renpy.restart_interaction()

    def sf_profile_commit_rename(key):
        value = (store.sf_profile_name_value or "").strip()
        if value:
            meta = _sf_profile_meta_load()
            meta["names"][sf_profile_key(key)] = value
            _sf_profile_meta_save(meta)
        store.sf_profile_name_value = ""
        store.sf_profile_confirm = None
        renpy.restart_interaction()

    def sf_profile_new(name=None):
        pmod = _sf_importlib.import_module("renpy.persistent")
        obj = pmod.Persistent()
        now = _sf_time.time()
        keep = ("_preferences", "sf_folders", "sf_active_folder",
                "sfmigration", "sfmigrated_files", "sfmigrated_persistent")
        for f in keep:
            val = getattr(persistent, f, None)
            if val is not None:
                obj.__dict__[f] = val
                try:
                    obj._changed[f] = now
                except Exception:
                    pass
        rec = dict(obj.sfmigrated_persistent or {})
        for n in sf_resolve_migration_source_names():
            rec[n] = True
        obj.sfmigrated_persistent = rec
        name = (name or "").strip() or _("New profile")
        try:
            key = _sf_profile_unique_key(name)
            obj.sf_profile_key_active = key
            try:
                obj._changed["sf_profile_key_active"] = now
            except Exception:
                pass
            _sf_write_persistent_file(_sf_profile_path(key), obj)
        except Exception:
            renpy.notify(_("Could not create the profile."))
            return None
        meta = _sf_profile_meta_load()
        meta["names"][key] = name
        _sf_profile_meta_save(meta)
        renpy.notify(__("Blank profile '{name}' created. Switch to it to start fresh.").format(name=name))
        return key

    def sf_profile_commit_new():
        sf_profile_new(store.sf_profile_name_value)
        store.sf_profile_name_value = ""
        store.sf_profile_confirm = None
        renpy.restart_interaction()

    def sf_profile_delete(key):
        try:
            _sf_os.remove(_sf_profile_path(key))
        except Exception:
            pass
        meta = _sf_profile_meta_load()
        if meta["names"].pop(sf_profile_key(key), None) is not None:
            _sf_profile_meta_save(meta)
        store.sf_profile_confirm = None
        renpy.restart_interaction()

    def _sf_all_persistent_paths():
        paths = []
        try:
            loadsave = _sf_importlib.import_module("renpy.loadsave")
            loc = loadsave.location
            locs = loc.active_locations() if hasattr(loc, "active_locations") else [loc]
            for l in locs:
                p = getattr(l, "persistent", None)
                if p and p not in paths:
                    paths.append(p)
        except Exception:
            pass
        live = _sf_os.path.join(_sf_profiles_dir(), "persistent")
        if live not in paths:
            paths.append(live)
        return paths

    def sf_profile_switch(key):
        key = sf_profile_key(key)
        src = _sf_profile_path(key)
        root = _sf_profiles_dir()
        live = _sf_os.path.join(root, "persistent")
        if not _sf_os.path.isfile(src):
            renpy.notify(_("That profile could not be found."))
            return
        obj = _sf_load_old_persistent(src)
        if obj is None:
            renpy.notify(_("That profile file could not be read."))
            return
        obj.sf_profile_key_active = key
        try:
            obj._changed["sf_profile_key_active"] = _sf_time.time()
        except Exception:
            pass
        active_key = _sf_active_profile_key()

        try:
            _sf_commit_playtime()
            renpy.save_persistent()
            _sf_shutil.copy2(live, _sf_profile_path(active_key))
        except Exception:
            renpy.notify(_("Could not back up current progress; switch cancelled."))
            return

        try:
            for p in _sf_all_persistent_paths():
                for leftover in (p + ".new", p + ".tmp"):
                    if _sf_os.path.exists(leftover):
                        _sf_os.remove(leftover)
                _sf_write_persistent_file(p, obj)
        except Exception:
            renpy.notify(_("Switch failed."))
            return

        meta = _sf_profile_meta_load()
        meta["names"].setdefault(active_key, _sf_profile_display(active_key, meta["names"]))
        meta["active"] = key
        _sf_profile_meta_save(meta)

        pmod = _sf_importlib.import_module("renpy.persistent")
        pmod.should_save_persistent = False
        pmod.persistent_mtime = float("inf")

        ## Raises QuitException; nothing runs after this line.
        renpy.quit(relaunch=True)

    def sf_open_profiles_modal():
        store.sf_profile_confirm = None
        store.sf_profile_name_value = ""
        renpy.show_screen("sf_profiles_modal")
        renpy.restart_interaction()

    def sf_close_profiles_modal():
        store.sf_profile_confirm = None
        store.sf_profile_name_value = ""
        try:
            if renpy.get_screen("sf_profiles_modal"):
                renpy.hide_screen("sf_profiles_modal")
        except Exception:
            pass
        renpy.restart_interaction()

    def sf_get_migration_plan():
        sources, dst_dir = sf_get_migration_paths()
        result = {
            "source_names": [n for n, _d in sources],
            "source_name": ", ".join(n for n, _d in sources),
            "dest_dir": dst_dir,
            "total": 0,
            "transferable": 0,
            "skipped": 0,
            "candidates": [], ## list of (src_name, src_dir, filename)
            "has_source": bool(sources),
        }
        if not sources or not dst_dir:
            return result

        total = 0
        skipped = 0
        transferable = []
        claimed = set()   ## filenames already claimed by an earlier source
        for _name, src_dir in sources:
            for fn in sf_list_save_files_in_dir(src_dir):
                total += 1
                if fn in claimed or _sf_is_migrated_seen(_name, fn) or _sf_os.path.exists(_sf_os.path.join(dst_dir, fn)):
                    skipped += 1
                    continue
                claimed.add(fn)
                transferable.append((_name, src_dir, fn))

        result["total"] = total
        result["transferable"] = len(transferable)
        result["skipped"] = skipped
        result["candidates"] = transferable
        result["persist_pending"] = len(sf_pending_persist_sources())
        return result

    def sf_migration_prompt_key(plan=None):
        plan = plan or sf_get_migration_plan()
        current = sf_current_save_dir_name()
        sources = plan.get("source_names") or []
        key = "{}<-{}".format(current, "|".join(sources))
        ## Distinct key once progress import becomes available, so installs
        ## that dismissed the saves-only prompt get offered it once more.
        if plan.get("persist_pending"):
            key += "+persist"
        return key

    def sf_should_prompt_migration(mode):
        if mode != "load":
            return False
        plan = sf_get_migration_plan()
        ## Auto-popup only when there are actual save files to migrate.
        ## Profile-only imports remain available via the sidebar button.
        if plan.get("transferable", 0) <= 0:
            return False
        seen = persistent.sfmigration
        if not isinstance(seen, dict):
            seen = {}
            persistent.sfmigration = seen
        key = sf_migration_prompt_key(plan)
        return not bool(seen.get(key, False))

    def sf_mark_migration_prompt_seen():
        plan = sf_get_migration_plan()
        seen = persistent.sfmigration
        if not isinstance(seen, dict):
            seen = {}
            persistent.sfmigration = seen
        seen[sf_migration_prompt_key(plan)] = True

    def sf_open_migration_prompt():
        renpy.show_screen("sf_migrate_prompt_modal")
        renpy.restart_interaction()

    def sf_close_migration_prompt():
        try:
            if renpy.get_screen("sf_migrate_prompt_modal"):
                renpy.hide_screen("sf_migrate_prompt_modal")
        except Exception:
            pass
        renpy.restart_interaction()

    def sf_maybe_prompt_migration(mode):
        if not sf_should_prompt_migration(mode):
            return
        sf_mark_migration_prompt_seen()
        sf_open_migration_prompt()

    def sf_run_save_migration():
        plan = sf_get_migration_plan()
        dst_dir = plan.get("dest_dir")
        persist_pending = sf_pending_persist_sources()
        if (plan.get("total", 0) <= 0 and not persist_pending) \
                or not plan.get("has_source") or not dst_dir:
            sf_close_migration_prompt()
            renpy.notify(_("No old saves were found to migrate."))
            return

        copied = 0
        failed = 0
        skipped = 0
        for src_name, src_dir, fn in plan.get("candidates", []):
            src = _sf_os.path.join(src_dir, fn)
            dst = _sf_os.path.join(dst_dir, fn)
            if _sf_os.path.exists(dst):
                skipped += 1
                _sf_mark_migrated_seen(src_name, fn)
                continue
            try:
                _sf_shutil.copy2(src, dst)
                copied += 1
                _sf_mark_migrated_seen(src_name, fn)
            except Exception:
                failed += 1

        sources, _unused = sf_get_migration_paths()

        for _name, src_dir in sources:
            for fn in sf_list_save_files_in_dir(src_dir):
                if _sf_os.path.exists(_sf_os.path.join(dst_dir, fn)):
                    _sf_mark_migrated_seen(_name, fn)

        ## Bring old progress / unlocks over as switchable PROFILES: the
        ## old persistent is copied in alongside the live one, never
        ## merged into it or overwritten. Managed via the Profiles overlay.
        imported = 0
        prec = _sf_migrated_persist_record()
        for name, ppath in persist_pending:
            try:
                if sf_import_persist_as_profile(name, ppath):
                    prec[name] = True
                    imported += 1
            except Exception:
                pass

        renpy.save_persistent()

        sidecar = "save_folders.json"
        dst_sidecar = _sf_os.path.join(dst_dir, sidecar)
        if not _sf_os.path.exists(dst_sidecar):
            for _name, src_dir in sources:
                src_sidecar = _sf_os.path.join(src_dir, sidecar)
                if _sf_os.path.isfile(src_sidecar):
                    try:
                        _sf_shutil.copy2(src_sidecar, dst_sidecar)
                    except Exception:
                        pass
                    break

        try:
            renpy.loadsave.location.scan()
        except Exception:
            pass
        _sf_scan_cache_clear()

        sf_close_migration_prompt()

        skipped_total = int(plan.get("skipped", 0)) + skipped
        if failed:
            msg = __("Migrated {copied} saves, skipped {skipped}, {failed} failed.").format(
                copied=copied, skipped=skipped_total, failed=failed
            )
        else:
            msg = __("Migrated {copied} saves, skipped {skipped} existing.").format(
                copied=copied, skipped=skipped_total
            )
        if imported:
            msg += _(" Old progress imported to Profiles.")
        renpy.notify(msg)

        renpy.restart_interaction()

init 50 python:
    sf_read_sidecar()
    sf_refresh_folders_from_disk()
    sf_write_sidecar()

## ── Glass background for the folders sidebar ───────────────────────────────

init python:
    _SF_SIDEBAR_RECT = (395, 0, 280, 1080)

    ## Normally defined by screens.rpy at init -10. Fall back gracefully if
    ## this file is running against an older screens.rpy (partial update).
    _SF_GLASS_SOURCE = getattr(store, "_OUTER_GLASS_SOURCE", None) or "gui/gallery_menu.png"
    _SF_EDGE_GRADIENT = getattr(store, "INNER_SIDEBAR_EDGE_GRADIENT", None) or Solid("#4ceefc", xysize=(1, 1080))

    SF_SIDEBAR_BG = Composite(
        (_SF_SIDEBAR_RECT[2], _SF_SIDEBAR_RECT[3]),
        (0, 0), Crop(_SF_SIDEBAR_RECT, Transform(_SF_GLASS_SOURCE, blur=32)),
        (0, 0), Solid("#0a0514bb"),
        (0, 0), Solid("#66d1d910"),
        (_SF_SIDEBAR_RECT[2] - 1, 0), _SF_EDGE_GRADIENT,
    )

################################################################################
## Main screen
################################################################################

screen sf_save_browser(mode="load"):

    tag menu

    $ sf_sync_filepage()
    $ sf_maybe_prompt_migration(mode)

    $ _sf_active = sf_resolve_folder(persistent.sf_active_folder)
    $ _sf_legacy_visible = sf_has_legacy_saves()
    $ _sf_mig_plan = sf_get_migration_plan()

    # Y / H deletes the currently focused save slot
    key "K_h" action Function(sf_delete_focused)
    key "pad_y_press" action Function(sf_delete_focused)

    ## Cancel any per-slot action state if the browser is dismissed
    on "hide" action [
        Function(sf_cancel_move),
        Function(sf_bulk_disable),
        Function(sf_close_slot_menu),
        Function(sf_cancel_rename),
        Function(sf_close_view_settings, False),
    ]

    on "show" action [
        Function(sf_close_view_settings, False),
        Function(sf_refresh_folders_from_disk),
        Function(sf_apply_default_save_name, mode),
    ]
    on "replace" action [
        Function(sf_close_view_settings, False),
        Function(sf_apply_default_save_name, mode),
    ]

    use game_menu(_("Save") if mode == "save" else _("Load"), scroll=None):

        vbox:
            xfill True
            yfill True
            spacing 0

            if sf_move_source is not None:
                use sf_move_banner()

            hbox:
                xfill True
                yfill True
                spacing 0

                ## ─── Folder sidebar ───────────────────────────────────────────
                frame:
                    xsize 280
                    yfill True
                    padding (16, 18)
                    background SF_SIDEBAR_BG

                    viewport:
                        mousewheel True
                        scrollbars None
                        xfill True
                        yfill True

                        vbox:
                            spacing 6
                            xfill True

                            text _("FOLDERS") style "sf_section_label"
                            null height 6

                            use sf_folder_row("auto", _("Auto saves"), kind="system")
                            use sf_folder_row("quick", _("Quick saves"), kind="system")

                            null height 10
                            add Solid("#4ceefc26") xsize 240 ysize 1
                            null height 6

                            for f in sf_user_folders():
                                use sf_folder_row(f["id"], f["name"], kind="user")

                            null height 6
                            use sf_folder_creator()

                            if mode == "load":
                                null height 10
                                add Solid("#4ceefc26") xsize 240 ysize 1
                                null height 8
                                textbutton _("Migrate old saves"):
                                    action Function(sf_open_migration_prompt)
                                    sensitive bool(_sf_mig_plan.get("has_source"))
                                    style "sf_new_button"

                            null height 10
                            add Solid("#4ceefc26") xsize 240 ysize 1
                            null height 8
                            textbutton _("Progress profiles"):
                                action Function(sf_open_profiles_modal)
                                style "sf_new_button"

                            if _sf_legacy_visible:
                                null height 12
                                add Solid("#4ceefc26") xsize 240 ysize 1
                                null height 6
                                use sf_folder_row("__legacy__", _("Old saves"), kind="legacy")

                ## ─── Slot panel ──────────────────────────────────────────────
                frame:
                    background None
                    xfill True
                    yfill True
                    padding (30, 20, 24, 30)

                    vbox:
                        xfill True
                        yfill True
                        spacing 18
                        ## Draw the header last so the view tip overlays the slots below it.
                        order_reverse True

                        hbox:
                            spacing 18
                            yalign 0.0

                            text _sf_active["name"] style "sf_folder_title"

                            if _sf_active["id"] == "__legacy__":
                                text _("(read-only)") style "sf_folder_subtitle"
                                if not sf_bulk_mode:
                                    null width 16
                                    textbutton _("Delete folder"):
                                        action Confirm(
                                            _("Delete every old save?\n\nThis only removes saves in the Old saves folder and cannot be undone."),
                                            yes=Function(sf_delete_legacy_saves),
                                        )
                                        style "sf_header_chip_danger"
                                        yalign 0.5

                            if (not sf_bulk_mode
                                    and _sf_active.get("kind") == "user"
                                    and _sf_active["id"] != "main"):
                                null width 16
                                textbutton _("Rename"):
                                    action [
                                        SetVariable("sf_edit_target", _sf_active["id"]),
                                        SetVariable("sf_edit_value", _sf_active["name"]),
                                        Function(osk_force_show),
                                    ]
                                    style "sf_header_chip"
                                    yalign 0.5
                                textbutton _("Delete"):
                                    action Confirm(
                                        __("Delete folder \"{name}\" and every save inside it?\n\nThis cannot be undone.").format(name=_sf_active["name"]),
                                        yes=Function(sf_delete_folder, _sf_active["id"]),
                                    )
                                    style "sf_header_chip_danger"
                                    yalign 0.5

                            fixed:
                                xfill True
                                ysize 48

                                if sf_bulk_mode:
                                    hbox:
                                        spacing 10
                                        xalign 1.0
                                        yalign 0.5

                                        text _("Selected: [sf_bulk_count()]") style "sf_folder_subtitle"

                                        textbutton _("Select all"):
                                            action Function(sf_bulk_select_all_current_view)
                                            style "sf_header_chip"

                                        textbutton _("Clear"):
                                            action Function(sf_bulk_clear)
                                            style "sf_header_chip"

                                        textbutton _("Move"):
                                            action Function(sf_bulk_open_move_modal)
                                            sensitive sf_bulk_count() > 0
                                            style "sf_header_chip"

                                        textbutton _("Delete"):
                                            action Confirm(
                                                _("Delete [sf_bulk_count()] selected save(s)?\n\nThis cannot be undone."),
                                                yes=Function(sf_bulk_delete_selected),
                                            )
                                            sensitive sf_bulk_count() > 0
                                            style "sf_header_chip_danger"

                                        textbutton _("Done"):
                                            action Function(sf_bulk_disable)
                                            style "sf_header_chip"

                                if not sf_bulk_mode:
                                    ## Fixed box leaves room for the pulse to grow without leaving the panel.
                                    fixed:
                                        xysize (60, 48)
                                        xalign 1.0
                                        yalign 0.5
                                        textbutton "\u2699":
                                                action Function(sf_open_view_settings)
                                                style "sf_gear_button"
                                                align (0.5, 0.5)

                                    textbutton _("Select"):
                                        action Function(sf_bulk_enable)
                                        style "sf_header_chip"
                                        xalign 1.0
                                        yalign 0.5
                                        xoffset - 66

                                    if not persistent.sf_view_tip_seen:
                                        ## Hangs below the header row without taking layout space.
                                        vbox:
                                            xalign 0.98
                                            ypos 1.0
                                            yanchor 0.0
                                            spacing 0
                                            text "\u25b2" style "sf_tip_arrow" xalign 1.0 xoffset -11 at sf_tip_bob
                                            frame:
                                                style "sf_tip_frame"
                                                xalign 1.0
                                                modal True
                                                vbox:
                                                    spacing 12
                                                    text _("Tip: don't like this layout? Use the {font=DejaVuSans.ttf}\u2699{/font} button above to switch between pages and a scrolling grid, or change the sort order.") style "sf_tip_text"
                                                    hbox:
                                                        spacing 12
                                                        xalign 1.0
                                                        textbutton _("Show me"):
                                                            action Function(sf_open_view_settings)
                                                            style "sf_header_chip"
                                                        textbutton _("Got it"):
                                                            action Function(sf_dismiss_view_tip)
                                                            style "sf_header_chip"

                        if mode == "save" and _sf_active["id"] not in ("__legacy__", "auto", "quick") and sf_edit_target is None:
                            frame:
                                background Solid("#150a1f88")
                                padding (16, 12)
                                right_padding 78
                                xfill True
                                hbox:
                                    spacing 14
                                    yalign 0.5
                                    text _("SAVE NAME") style "sf_input_label"

                                    $ save_name_iv = VariableInputValue("save_name", default=False)
                                    button:
                                        style "sf_input_button"
                                        action Function(osk_activate_for, save_name_iv, "save_name")
                                        key_events True
                                        xfill True
                                        input value save_name_iv id "save_input" yalign 0.5

                                    textbutton _("Clear"):
                                        style "sf_input_clear"
                                        yalign 0.5
                                        sensitive bool((save_name or "").strip())
                                        action [SetVariable("save_name", ""), SetVariable("_sf_autoname_last", "")]

                        if _sf_active["id"] == "__legacy__":
                            if mode == "save":
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 12
                                    text _("Old saves are read-only.") style "sf_folder_title"
                                    text _("Pick or create a folder on the left to save into.") style "sf_hint"
                            else:
                                use sf_legacy_grid()
                        else:
                            use sf_normal_grid(mode)

################################################################################
## Sidebar pieces
################################################################################

screen sf_folder_row(folder_id, label, kind="user"):
    if sf_edit_target == folder_id:
        use sf_inline_edit()
    else:
        button:
            style "sf_folder_button"
            action SfSelect(folder_id)
            selected persistent.sf_active_folder == folder_id

            hbox:
                spacing 10
                yalign 0.5
                xfill True

                if persistent.sf_active_folder == folder_id:
                    add Solid("#4ceefc") xysize (3, 26)
                else:
                    null width 3 height 26

                if kind == "user":
                    text "[label]" style "sf_folder_button_text"
                else:
                    text "[label!t]" style "sf_folder_button_text"

screen sf_folder_creator():
    if sf_edit_target == "__new__":
        use sf_inline_edit()
    else:
        textbutton _("+ New folder"):
            action [
                SetVariable("sf_edit_target", "__new__"),
                SetVariable("sf_edit_value", ""),
                Function(osk_force_show),
            ]
            style "sf_new_button"

screen sf_inline_edit():
    vbox:
        spacing 6
        xfill True

        frame:
            style "sf_edit_frame"
            xfill True
            input:
                value SfEditInputValue()
                length 24
                yalign 0.5

        hbox:
            spacing 6
            xalign 1.0

            textbutton _("Save"):
                action [Function(sf_commit_edit, sf_edit_value), Function(osk_force_hide)]
                style "sf_edit_ok"
                sensitive sf_edit_value.strip() != ""

            textbutton _("Cancel"):
                action [Function(sf_cancel_edit), Function(osk_force_hide)]
                style "sf_edit_cancel"

    key "K_ESCAPE" action [Function(sf_cancel_edit), Function(osk_force_hide)]

################################################################################
## Slot grids
################################################################################

screen sf_page_bar(total_items):
    $ _pages = max(1, (total_items + SF_PAGE_SIZE - 1) // SF_PAGE_SIZE)
    $ _page = max(0, min(sf_grid_page, _pages - 1))

    hbox:
        spacing 14
        xalign 0.5

        textbutton _("< Prev"):
            action Function(sf_set_grid_page, _page - 1, _pages)
            sensitive _page > 0
            style "sf_page_btn"
            yalign 0.5

        $ _page_disp = "{} / {}".format(_page + 1, _pages)
        text "[_page_disp]" style "sf_page_label" yalign 0.5

        textbutton _("Next >"):
            action Function(sf_set_grid_page, _page + 1, _pages)
            sensitive _page < _pages - 1
            style "sf_page_btn"
            yalign 0.5

screen sf_normal_grid(mode):
    $ _slots = sf_sorted_slots(persistent.sf_active_folder)

    if persistent.sf_view_mode == "page":
        $ _pages = max(1, (len(_slots) + SF_PAGE_SIZE - 1) // SF_PAGE_SIZE)
        $ _page = max(0, min(sf_grid_page, _pages - 1))
        $ _page_slots = _slots[_page * SF_PAGE_SIZE : (_page + 1) * SF_PAGE_SIZE]
        $ _page_slots += [None] * max(0, SF_PAGE_SIZE - len(_page_slots))

        vbox:
            spacing 8
            xfill True
            yfill False
            yalign 0.0

            use sf_page_bar(len(_slots))

            grid 4 4:
                spacing 12
                xfill True
                yalign 0.0

                for slot in _page_slots:
                    if slot is None:
                        use sf_slot_blank_tile()
                    else:
                        use sf_slot_tile(target=slot)
    else:
        vpgrid:
            cols 4
            spacing 18
            mousewheel True
            draggable True
            pagekeys True
            scrollbars "vertical"
            side_yfill True
            side_spacing 18
            xfill True

            for slot in _slots:
                use sf_slot_tile(target=slot)

screen sf_legacy_grid():
    $ legacy_names = sf_legacy_saves_sorted()
    if not legacy_names:
        vbox:
            xalign 0.5
            yalign 0.5
            text _("No legacy saves detected.") style "sf_hint"
    elif persistent.sf_view_mode == "page":
        $ _pages = max(1, (len(legacy_names) + SF_PAGE_SIZE - 1) // SF_PAGE_SIZE)
        $ _page = max(0, min(sf_grid_page, _pages - 1))
        $ _page_names = legacy_names[_page * SF_PAGE_SIZE : (_page + 1) * SF_PAGE_SIZE]
        $ _page_names += [None] * max(0, SF_PAGE_SIZE - len(_page_names))

        vbox:
            spacing 8
            xfill True
            yfill False
            yalign 0.0

            use sf_page_bar(len(legacy_names))

            grid 4 4:
                spacing 12
                xfill True
                yalign 0.0

                for name in _page_names:
                    if name is None:
                        use sf_slot_blank_tile()
                    else:
                        use sf_slot_tile(target=name, full_slot=True)
    else:
        vpgrid:
            cols 4
            spacing 18
            mousewheel True
            draggable True
            pagekeys True
            scrollbars "vertical"
            side_yfill True
            side_spacing 18
            xfill True

            for name in legacy_names:
                use sf_slot_tile(target=name, full_slot=True)

screen sf_slot_tile(target, full_slot=False):
    $ _sf_full_name = sf_full_slot_name(target, full_slot)
    $ _sf_loadable = FileLoadable(target, slot=full_slot)
    $ _sf_moving = (sf_move_source is not None)
    $ _sf_bulk = bool(sf_bulk_mode)
    $ _sf_is_source = (_sf_moving and _sf_full_name == sf_move_source)
    $ _sf_can_drop = sf_active_folder_accepts_drop()
    $ _sf_episode = sf_slot_episode(_sf_full_name) if _sf_loadable else None
    $ _sf_selected = (_sf_bulk and sf_bulk_is_selected(_sf_full_name))

    button:
        style "slot_button"
        if _sf_moving:
            if _sf_is_source:
                action Function(sf_cancel_move)
            elif not _sf_can_drop:
                action Function(renpy.notify, _("Auto, quick, and old-saves folders can't be a move destination."))
            else:
                action Function(sf_perform_move, _sf_full_name)
        elif _sf_bulk:
            if _sf_loadable:
                action Function(sf_bulk_toggle, _sf_full_name)
            else:
                action Function(renpy.notify, _("Only occupied saves can be selected."))
        else:
            action FileAction(target, slot=full_slot)
        hovered Function(sf_focus_slot, target, full_slot)
        unhovered Function(sf_unfocus_slot, target, full_slot)

        has vbox

        fixed:
            xalign 0.5
            xysize (config.thumbnail_width, config.thumbnail_height)

            add FileScreenshot(target, slot=full_slot):
                fit "contain"
                xalign 0.5
                yalign 0.5

            if _sf_episode is not None:
                frame:
                    style "sf_slot_badge"
                    xalign 0.0
                    yalign 0.0
                    xoffset 6
                    yoffset 6
                    text _("Episode [_sf_episode]") style "sf_slot_badge_text"

            if _sf_loadable and not _sf_moving and not _sf_bulk:
                frame:
                    style "sf_slot_action_box"
                    xanchor 1.0
                    xpos config.thumbnail_width
                    ypos 0
                    has vbox
                    spacing 78

                    imagebutton:
                        idle "gui/button/button_edit_idle.png"
                        hover "gui/button/button_edit_hover.png"
                        action Function(sf_open_slot_menu, _sf_full_name)
                        keyboard_focus False

                    imagebutton:
                        idle "gui/button/button_delete_idle.png"
                        hover "gui/button/button_delete_hover.png"
                        action FileDelete(target, slot=full_slot)
                        keyboard_focus False

            if _sf_bulk and _sf_selected:
                frame:
                    style "sf_slot_selected_chip"
                    xalign 1.0
                    yalign 0.0
                    xoffset - 6
                    yoffset 6
                    text _("SELECTED") style "sf_slot_selected_chip_text"

        text FileTime(target, format=_("{#file_time}%a %b %d %Y  ·  %H:%M"), empty=_("empty slot"), slot=full_slot):
            style "slot_time_text"

        text FileSaveName(target, slot=full_slot):
            style "slot_name_text"

        if _sf_moving and _sf_is_source:
            text _("● moving this save") style "sf_slot_state_source" xalign 0.5
        elif _sf_moving and _sf_can_drop:
            text (_("swap here") if _sf_loadable else _("move here")) style "sf_slot_state_target" xalign 0.5
        elif _sf_bulk and _sf_loadable:
            text (_("selected") if _sf_selected else _("click to select")) style "sf_slot_state_target" xalign 0.5

screen sf_slot_blank_tile():
    button:
        style "slot_button"
        action NullAction()
        sensitive False

        has vbox

        fixed:
            xalign 0.5
            xysize (config.thumbnail_width, config.thumbnail_height)

            add Solid("#ffffff08") xysize (config.thumbnail_width, config.thumbnail_height)

        text " " style "slot_time_text"
        text " " style "slot_name_text"

################################################################################
## Custom actions
################################################################################

init python:
    class SfSelect(Action):
        """Switch to a folder. Also doubles as a `selected` predicate."""
        def __init__(self, folder_id):
            self.folder_id = folder_id
        def __call__(self):
            sf_select(self.folder_id)
        def get_selected(self):
            return persistent.sf_active_folder == self.folder_id

    class SfEditInputValue(InputValue):
        """InputValue bound to the screen variable `sf_edit_value`."""

        default = True

        def get_text(self):
            return renpy.store.sf_edit_value or ""

        def set_text(self, s):
            renpy.store.sf_edit_value = s
            renpy.restart_interaction()

        def enter(self):
            sf_commit_edit(renpy.store.sf_edit_value)
            raise renpy.IgnoreEvent()

    class SfRenameInputValue(InputValue):
        """InputValue bound to `sf_rename_value` for the Rename Save modal."""

        default = True

        def get_text(self):
            return renpy.store.sf_rename_value or ""

        def set_text(self, s):
            renpy.store.sf_rename_value = s
            renpy.restart_interaction()

        def enter(self):
            sf_commit_rename()
            raise renpy.IgnoreEvent()

    class SfProfileNameInputValue(InputValue):
        """InputValue bound to `sf_profile_name_value` for the Profiles overlay."""

        default = True

        def get_text(self):
            return renpy.store.sf_profile_name_value or ""

        def set_text(self, s):
            renpy.store.sf_profile_name_value = s
            renpy.restart_interaction()

        def enter(self):
            c = renpy.store.sf_profile_confirm
            if c == ("snapshot", None):
                sf_profile_commit_snapshot()
            elif c == ("new", None):
                sf_profile_commit_new()
            elif isinstance(c, tuple) and c and c[0] == "rename":
                sf_profile_commit_rename(c[1])
            raise renpy.IgnoreEvent()

################################################################################
## Styles
################################################################################

style sf_section_label is gui_text:
    color "#4ceefc"
    size 14
    kerning 6
    outlines []
    font gui.interface_text_font

style sf_slot_badge is empty:
    background Solid("#0a050fcc")
    padding (10, 4)

style sf_slot_badge_text is gui_text:
    color "#4ceefc"
    size 15
    bold True
    outlines []
    font gui.interface_text_font

style sf_slot_selected_chip is empty:
    background Solid("#4ceefccc")
    padding (8, 3)

style sf_slot_selected_chip_text is gui_text:
    color "#0a050f"
    size 12
    bold True
    kerning 2
    outlines []
    font gui.interface_text_font

style sf_folder_button is empty:
    background None
    hover_background Solid("#4ceefc14")
    selected_background Solid("#4ceefc22")
    selected_hover_background Solid("#4ceefc33")
    padding (10, 10)
    xfill True

style sf_folder_button_text is gui_text:
    color "#e8dcf0"
    hover_color "#ffffff"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    size 18
    outlines []
    font gui.interface_text_font

style sf_folder_icon is gui_text:
    color "#beadc6"
    size 16
    outlines []

style sf_folder_icon_warn is sf_folder_icon:
    color "#ffb84c"

style sf_folder_subtitle is gui_text:
    color "#8b7a99"
    size 18
    italic True
    outlines []
    font gui.interface_text_font
    yalign 0.6

style sf_folder_chip is empty:
    background None
    hover_background Solid("#0a050faa")
    padding (6, 4)

style sf_folder_chip_text is gui_text:
    color "#beadc6"
    hover_color "#ffffff"
    size 16
    outlines []
    font gui.interface_text_font

style sf_header_chip is empty:
    background Solid("#1d1230cc")
    hover_background Solid("#2a1640")
    padding (16, 10)

style sf_header_chip_text is gui_text:
    color "#4ceefc"
    hover_color "#ffffff"
    size 16
    kerning 4
    outlines []
    font gui.interface_text_font

style sf_header_chip_danger is sf_header_chip:
    hover_background Solid("#d10089")

style sf_header_chip_danger_text is sf_header_chip_text:
    color "#d10089"
    hover_color "#ffffff"

style sf_new_button is empty:
    background Solid("#4ceefc10")
    hover_background Solid("#4ceefc24")
    padding (14, 10)
    xfill True

style sf_new_button_text is gui_text:
    color "#4ceefc"
    hover_color "#ffffff"
    size 16
    outlines []
    font gui.interface_text_font
    xalign 0.5

style sf_edit_frame is empty:
    background Solid("#150a1fdd")
    padding (10, 4)
    foreground Solid("#4ceefc18")

style sf_edit_ok is empty:
    background Solid("#1d1230aa")
    hover_background Solid("#4ceefc99")
    padding (8, 6)

style sf_edit_ok_text is gui_text:
    color "#4ceefc"
    hover_color "#0a050f"
    insensitive_color "#5a4a68"
    size 16
    outlines []
    font gui.interface_text_font

style sf_edit_cancel is sf_edit_ok
style sf_edit_cancel_text is sf_edit_ok_text:
    color "#beadc6"

style sf_folder_title is gui_text:
    color "#f8eadb"
    size 36
    outlines []
    font gui.interface_text_font

style sf_input_label is gui_text:
    color "#4ceefc"
    size 16
    kerning 6
    outlines []
    font gui.interface_text_font
    yalign 0.5

style sf_input_button is empty:
    background Solid("#0a050f88")
    hover_background Solid("#4ceefc44")
    selected_background Solid("#4ceefc66")
    selected_hover_background Solid("#4ceefc99")
    padding (12, 4)

style sf_input_clear is empty:
    background Solid("#0a050f88")
    hover_background Solid("#4ceefc44")
    insensitive_background Solid("#0a050f44")
    padding (10, 6)

style sf_input_clear_text is gui_text:
    color "#beadc6"
    hover_color "#4ceefc"
    insensitive_color "#5a4a68"
    size 18
    outlines []
    font gui.interface_text_font

style sf_hint is gui_text:
    color "#8b7a99"
    size 18
    outlines []
    italic True
    font gui.interface_text_font

################################################################################
## Per-slot actions: menu popup, rename modal, move banner
################################################################################

screen sf_slot_menu_popup(slot_name):
    modal True
    zorder 200

    ## Dim / dismissal underlay
    button:
        style "empty"
        xfill True
        yfill True
        background Solid("#0a050faa")
        action Function(sf_close_slot_menu)
        key_events True

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 8
            xsize 380

            text _("Save actions") style "sf_slot_menu_title"

            $ _snm_json = renpy.slot_json(slot_name) or {}
            $ _snm = _snm_json.get("_save_name", "") or _("(untitled save)")
            text "[_snm!q]" style "sf_slot_menu_subtitle"
            text "[slot_name!q]" style "sf_slot_menu_slot"

            null height 6

            textbutton _("Rename save"):
                action Function(sf_begin_rename, slot_name)
                style "sf_slot_menu_item"
                xfill True

            textbutton _("Move to another slot or folder"):
                action Function(sf_begin_move, slot_name)
                style "sf_slot_menu_item"
                xfill True

            textbutton _("Export choice history"):
                action [Function(sf_close_slot_menu), Function(cx_export_and_open, slot_name)]
                style "sf_slot_menu_item"
                xfill True

            textbutton _("Delete save"):
                action [Function(sf_close_slot_menu), FileDelete(slot_name, slot=True)]
                style "sf_slot_menu_item_danger"
                xfill True

            null height 6

            textbutton _("Cancel"):
                action Function(sf_close_slot_menu)
                style "sf_slot_menu_item"
                xfill True

    key "K_ESCAPE" action Function(sf_close_slot_menu)
    key "game_menu" action Function(sf_close_slot_menu)

screen sf_rename_modal():
    modal True
    zorder 300

    button:
        style "empty"
        xfill True
        yfill True
        background Solid("#0a050fcc")
        action [Function(sf_cancel_rename), Function(osk_force_hide)]
        key_events True

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 12
            xsize 540

            text _("Rename save") style "sf_slot_menu_title"

            if sf_rename_target:
                text "[sf_rename_target!q]" style "sf_slot_menu_slot"

            null height 4

            frame:
                style "sf_edit_frame"
                xfill True

                $ _sf_rename_iv = SfRenameInputValue()
                button:
                    style "sf_input_button"
                    action Function(osk_activate_for, _sf_rename_iv, "sf_rename_input")
                    key_events True
                    xfill True

                    input:
                        value _sf_rename_iv
                        length 80
                        id "sf_rename_input"
                        yalign 0.5

            text _("Leave the name blank to clear it. Press Enter to save.") style "sf_hint"

            null height 6

            hbox:
                spacing 10
                xalign 1.0

                textbutton _("Save"):
                    action [Function(sf_commit_rename), Function(osk_force_hide)]
                    style "sf_edit_ok"

                textbutton _("Cancel"):
                    action [Function(sf_cancel_rename), Function(osk_force_hide)]
                    style "sf_edit_cancel"

    key "K_ESCAPE" action [Function(sf_cancel_rename), Function(osk_force_hide)]
    key "game_menu" action [Function(sf_cancel_rename), Function(osk_force_hide)]

screen sf_move_banner():
    $ _src = sf_move_source
    $ _src_json = (renpy.slot_json(_src) or {}) if _src else {}
    $ _src_name = _src_json.get("_save_name", "") or _("(untitled save)")

    frame:
        background Solid("#1d1230cc")
        padding (18, 12)
        xfill True

        hbox:
            spacing 14
            yalign 0.5
            xfill True

            text _("MOVING") style "sf_input_label" yalign 0.5

            text "[_src_name!q]" style "sf_move_banner_name" yalign 0.5

            text _("· Pick a destination slot in any user folder, or click the source again to cancel.") style "sf_hint":
                yalign 0.5

            null width 12

            textbutton _("Cancel move"):
                action Function(sf_cancel_move)
                style "sf_header_chip_danger"
                yalign 0.5
                xalign 1.0

screen sf_bulk_move_modal():
    modal True
    zorder 285

    $ _sf_dest_folders = sf_bulk_move_dest_folders()

    button:
        style "empty"
        xfill True
        yfill True
        background Solid("#0a050fcc")
        action Function(sf_bulk_close_move_modal)
        key_events True

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10
            xsize 520

            text _("Move selected saves") style "sf_slot_menu_title"
            text _("Selected: [sf_bulk_count()]") style "sf_slot_menu_subtitle"

            null height 4

            if _sf_dest_folders:
                for _sf_f in _sf_dest_folders:
                    textbutton _("To folder: [_sf_f['name']]"):
                        action [
                            Function(sf_bulk_close_move_modal),
                            Confirm(
                                __("Move {count} selected save(s) to folder \"{name}\"?\n\nIf a slot number is occupied there, the save is moved to the next free slot.").format(
                                    count=sf_bulk_count(),
                                    name=_sf_f["name"],
                                ),
                                yes=Function(sf_bulk_move_selected_to, _sf_f["id"]),
                            ),
                        ]
                        style "sf_slot_menu_item"
                        xfill True
            else:
                text _("No destination folders available.") style "sf_hint"

            null height 8

            textbutton _("Cancel"):
                action Function(sf_bulk_close_move_modal)
                style "sf_slot_menu_item"
                xfill True

    key "K_ESCAPE" action Function(sf_bulk_close_move_modal)
    key "game_menu" action Function(sf_bulk_close_move_modal)

screen sf_migrate_prompt_modal():
    modal True
    zorder 290

    $ _sf_mig = sf_get_migration_plan()
    $ _sf_mig_source = _sf_mig["source_name"] or ""
    $ _sf_mig_multi = len(_sf_mig["source_names"]) > 1
    $ _sf_mig_total = _sf_mig["total"]
    $ _sf_mig_transfer = _sf_mig["transferable"]
    $ _sf_mig_skipped = _sf_mig["skipped"]
    $ _sf_mig_persist = _sf_mig.get("persist_pending", 0) > 0

    button:
        style "empty"
        xfill True
        yfill True
        background Solid("#0a050fcc")
        action Function(sf_close_migration_prompt)
        key_events True

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 0
            xsize 680

            text _("OLD SAVES DETECTED") style "sf_mig_title"

            null height 10

            if _sf_mig_source:
                hbox:
                    spacing 8
                    text (_("From:") if not _sf_mig_multi else _("From folders:")) style "sf_mig_source_label"
                    text "[_sf_mig_source]" style "sf_mig_source_value"

            null height 18

            hbox:
                spacing 14
                xfill True

                frame:
                    style "sf_mig_stat_box"
                    xsize 217
                    vbox:
                        spacing 2
                        xalign 0.5
                        text "[_sf_mig_total]" style "sf_mig_stat_num"
                        text _("FOUND") style "sf_mig_stat_label"

                frame:
                    style "sf_mig_stat_box_accent"
                    xsize 217
                    vbox:
                        spacing 2
                        xalign 0.5
                        text "[_sf_mig_transfer]" style "sf_mig_stat_num_accent"
                        text _("WILL MIGRATE") style "sf_mig_stat_label"

                frame:
                    style "sf_mig_stat_box"
                    xsize 217
                    vbox:
                        spacing 2
                        xalign 0.5
                        text "[_sf_mig_skipped]" style "sf_mig_stat_num_dim"
                        text _("ALREADY HERE") style "sf_mig_stat_label"

            null height 16

            add Solid("#4ceefc26") xsize 680 ysize 1

            null height 12

            text _("Your existing saves are never overwritten. Saves that already exist here are skipped.") style "sf_hint"

            if _sf_mig_persist:
                null height 6
                text _("The old version's progress (gallery unlocks, seen scenes, playtime) is brought over as a separate profile. Nothing here is changed; you can switch to it from the Profiles panel.") style "sf_hint"

            null height 18

            hbox:
                spacing 12
                xalign 1.0

                if _sf_mig_transfer > 0 or _sf_mig_persist:
                    textbutton _("Migrate now"):
                        action Function(sf_run_save_migration)
                        style "sf_mig_primary"

                textbutton _("Later"):
                    action Function(sf_close_migration_prompt)
                    style "sf_edit_cancel"

    key "K_ESCAPE" action Function(sf_close_migration_prompt)
    key "game_menu" action Function(sf_close_migration_prompt)

style sf_mig_title is gui_text:
    color "#4ceefc"
    size 26
    kerning 6
    outlines []
    font gui.interface_text_font

style sf_mig_source_label is gui_text:
    color "#8b7a99"
    size 16
    outlines []
    font gui.interface_text_font

style sf_mig_source_value is gui_text:
    color "#e8dcf0"
    size 16
    outlines []
    font gui.interface_text_font

style sf_mig_stat_box is empty:
    background Solid("#1d123088")
    foreground Solid("#4ceefc11")
    padding (18, 14)

style sf_mig_stat_box_accent is sf_mig_stat_box:
    background Solid("#4ceefc14")
    foreground Solid("#4ceefc33")

style sf_mig_stat_num is gui_text:
    color "#f8eadb"
    size 34
    bold True
    outlines []
    font gui.interface_text_font
    xalign 0.5

style sf_mig_stat_num_accent is sf_mig_stat_num:
    color "#4ceefc"

style sf_mig_stat_num_dim is sf_mig_stat_num:
    color "#8b7a99"

style sf_mig_stat_label is gui_text:
    color "#8b7a99"
    size 13
    kerning 4
    outlines []
    font gui.interface_text_font
    xalign 0.5

style sf_mig_primary is empty:
    background Solid("#4ceefc22")
    hover_background Solid("#4ceefc")
    padding (22, 10)

style sf_mig_primary_text is gui_text:
    color "#4ceefc"
    hover_color "#0a050f"
    size 18
    outlines []
    font gui.interface_text_font

################################################################################
## Progress profiles (switchable persistent files)
################################################################################

screen sf_profiles_modal():
    modal True
    zorder 290

    $ _sf_prof_rows = sf_profile_rows()
    $ _sf_prof_names = _sf_profile_meta_load().get("names", {})
    $ _sf_prof_active = _sf_profile_display(_sf_active_profile_key(), _sf_prof_names)

    button:
        style "empty"
        xfill True
        yfill True
        background Solid("#0a050fcc")
        action Function(sf_close_profiles_modal)
        key_events True

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 0
            xsize 760

            text _("PROGRESS PROFILES") style "sf_mig_title"

            null height 8

            text _("Each profile is a full set of progress: gallery unlocks, seen scenes, choices, and playtime. Saves are shared; only progress switches.") style "sf_hint"

            null height 14

            ## Current (live) profile
            frame:
                style "sf_mig_stat_box_accent"
                xfill True
                vbox:
                    spacing 4
                    xfill True
                    hbox:
                        spacing 10
                        text _sf_prof_active style "sf_prof_name"
                        text _("CURRENT") style "sf_prof_badge"
                    text sf_profile_live_summary() style "sf_prof_summary"
                    text _("Last used: now") style "sf_prof_meta"

                    null height 6

                    if sf_profile_confirm == ("snapshot", None):
                        text _("Name this restore point:") style "sf_prof_meta"
                        frame:
                            style "sf_edit_frame"
                            xfill True
                            $ _sf_prof_iv = SfProfileNameInputValue()
                            button:
                                style "sf_input_button"
                                action Function(osk_activate_for, _sf_prof_iv, "sf_prof_snapshot_input")
                                key_events True
                                xfill True
                                input:
                                    value _sf_prof_iv
                                    length 60
                                    id "sf_prof_snapshot_input"
                                    yalign 0.5
                        null height 4
                        hbox:
                            spacing 12
                            textbutton _("Save profile"):
                                action [Function(sf_profile_commit_snapshot), Function(osk_force_hide)]
                                style "sf_prof_btn_primary"
                            textbutton _("Cancel"):
                                action [Function(sf_profile_cancel_input), Function(osk_force_hide)]
                                style "sf_prof_btn"
                    elif sf_profile_confirm == ("new", None):
                        text _("Name the new profile:") style "sf_prof_meta"
                        frame:
                            style "sf_edit_frame"
                            xfill True
                            $ _sf_prof_niv = SfProfileNameInputValue()
                            button:
                                style "sf_input_button"
                                action Function(osk_activate_for, _sf_prof_niv, "sf_prof_new_input")
                                key_events True
                                xfill True
                                input:
                                    value _sf_prof_niv
                                    length 60
                                    id "sf_prof_new_input"
                                    yalign 0.5
                        text _("Starts with no unlocks or playtime, like a fresh install. Settings and save folders carry over.") style "sf_prof_meta"
                        null height 4
                        hbox:
                            spacing 12
                            textbutton _("Create profile"):
                                action [Function(sf_profile_commit_new), Function(osk_force_hide)]
                                style "sf_prof_btn_primary"
                            textbutton _("Cancel"):
                                action [Function(sf_profile_cancel_input), Function(osk_force_hide)]
                                style "sf_prof_btn"
                    else:
                        hbox:
                            spacing 12
                            textbutton _("Save a copy as a restore point"):
                                action [SetVariable("sf_profile_name_value", ""), SetVariable("sf_profile_confirm", ("snapshot", None))]
                                style "sf_prof_btn"
                            textbutton _("New blank profile"):
                                action [SetVariable("sf_profile_name_value", ""), SetVariable("sf_profile_confirm", ("new", None))]
                                style "sf_prof_btn"

            null height 10

            viewport:
                mousewheel True
                scrollbars ("vertical" if len(_sf_prof_rows) > 3 else None)
                xfill True
                ymaximum 420

                vbox:
                    spacing 10
                    xfill True

                    for _sf_p in _sf_prof_rows:
                        frame:
                            style "sf_mig_stat_box"
                            xfill True
                            vbox:
                                spacing 4
                                xfill True

                                text _sf_p["name"] style "sf_prof_name"
                                text _sf_p["summary"] style "sf_prof_summary"
                                text __("Last used: {when}").format(when=_sf_p["last_used"]) style "sf_prof_meta"

                                null height 6

                                if sf_profile_confirm == ("switch", _sf_p["key"]):
                                    text _("Switching restarts the game. Your current progress is stored as a profile first, so nothing is lost.") style "sf_prof_warn"
                                    null height 4
                                    hbox:
                                        spacing 12
                                        textbutton _("Switch and restart"):
                                            action Function(sf_profile_switch, _sf_p["key"])
                                            style "sf_prof_btn_primary"
                                        textbutton _("Cancel"):
                                            action SetVariable("sf_profile_confirm", None)
                                            style "sf_prof_btn"
                                elif sf_profile_confirm == ("rename", _sf_p["key"]):
                                    frame:
                                        style "sf_edit_frame"
                                        xfill True
                                        $ _sf_prof_riv = SfProfileNameInputValue()
                                        button:
                                            style "sf_input_button"
                                            action Function(osk_activate_for, _sf_prof_riv, "sf_prof_rename_" + _sf_p["key"])
                                            key_events True
                                            xfill True
                                            input:
                                                value _sf_prof_riv
                                                length 60
                                                id ("sf_prof_rename_" + _sf_p["key"])
                                                yalign 0.5
                                    null height 4
                                    hbox:
                                        spacing 12
                                        textbutton _("Rename"):
                                            action [Function(sf_profile_commit_rename, _sf_p["key"]), Function(osk_force_hide)]
                                            style "sf_prof_btn_primary"
                                        textbutton _("Cancel"):
                                            action [Function(sf_profile_cancel_input), Function(osk_force_hide)]
                                            style "sf_prof_btn"
                                elif sf_profile_confirm == ("delete", _sf_p["key"]):
                                    text _("Delete this profile permanently? Its unlocks and playtime cannot be recovered.") style "sf_prof_warn"
                                    null height 4
                                    hbox:
                                        spacing 12
                                        textbutton _("Delete profile"):
                                            action Function(sf_profile_delete, _sf_p["key"])
                                            style "sf_prof_btn_danger"
                                        textbutton _("Cancel"):
                                            action SetVariable("sf_profile_confirm", None)
                                            style "sf_prof_btn"
                                else:
                                    hbox:
                                        spacing 12
                                        textbutton _("Switch to this"):
                                            action SetVariable("sf_profile_confirm", ("switch", _sf_p["key"]))
                                            style "sf_prof_btn_primary"
                                        textbutton _("Rename"):
                                            action [SetVariable("sf_profile_name_value", _sf_p["name"]), SetVariable("sf_profile_confirm", ("rename", _sf_p["key"]))]
                                            style "sf_prof_btn"
                                        textbutton _("Delete"):
                                            action SetVariable("sf_profile_confirm", ("delete", _sf_p["key"]))
                                            style "sf_prof_btn_danger"

            null height 14

            hbox:
                xalign 1.0
                textbutton _("Close"):
                    action Function(sf_close_profiles_modal)
                    style "sf_prof_btn"

    key "K_ESCAPE" action Function(sf_close_profiles_modal)
    key "game_menu" action Function(sf_close_profiles_modal)

style sf_prof_name is gui_text:
    color "#e8dcf0"
    size 20
    bold True
    outlines []
    font gui.interface_text_font

style sf_prof_badge is gui_text:
    color "#4ceefc"
    size 13
    kerning 4
    outlines []
    font gui.interface_text_font
    yalign 0.5

style sf_prof_summary is gui_text:
    color "#b8a8c8"
    size 16
    outlines []
    font gui.interface_text_font

style sf_prof_meta is gui_text:
    color "#8b7a99"
    size 14
    outlines []
    font gui.interface_text_font

style sf_prof_warn is gui_text:
    color "#f0c674"
    size 15
    outlines []
    font gui.interface_text_font

## Uniform action buttons for the Profiles overlay (same padding and
## text size everywhere, so every button in a row is the same height).
style sf_prof_btn is empty:
    background Solid("#1d1230aa")
    hover_background Solid("#4ceefc99")
    padding (16, 8)

style sf_prof_btn_text is gui_text:
    color "#beadc6"
    hover_color "#0a050f"
    size 16
    outlines []
    font gui.interface_text_font

style sf_prof_btn_primary is sf_prof_btn:
    background Solid("#4ceefc22")
    hover_background Solid("#4ceefc")

style sf_prof_btn_primary_text is sf_prof_btn_text:
    color "#4ceefc"

style sf_prof_btn_danger is sf_prof_btn:
    hover_background Solid("#d10089")

style sf_prof_btn_danger_text is sf_prof_btn_text:
    color "#d10089"
    hover_color "#ffffff"

################################################################################
## View options (layout / sorting)
################################################################################

screen sf_view_settings_modal():
    modal True
    zorder 280

    button:
        style "empty"
        xfill True
        yfill True
        background Solid("#0a050fcc")
        action Function(sf_close_view_settings)
        key_events True

    frame:
        style "sf_slot_menu_frame"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 0
            xsize 520

            text _("VIEW OPTIONS") style "sf_mig_title"

            null height 18

            text _("LAYOUT") style "sf_section_label"
            null height 8

            hbox:
                spacing 10
                textbutton _("Scrolling grid"):
                    action SetField(persistent, "sf_view_mode", "scroll")
                    style "sf_view_choice"
                textbutton _("Pages (4x4)"):
                    action [SelectedIf(SetField(persistent, "sf_view_mode", "page")), SetVariable("sf_grid_page", 0)]
                    style "sf_view_choice"

            null height 6
            text _("Scrolling grid: one long list of slots that you can scroll through.") style "sf_view_help"
            text _("Pages (4x4): fixed 4x4 pages with page buttons, easier for controller and keyboard navigation.") style "sf_view_help"

            null height 16

            text _("SORT ORDER") style "sf_section_label"
            null height 8

            hbox:
                spacing 10
                textbutton _("Slot order"):
                    action SetField(persistent, "sf_sort_mode", "slot")
                    style "sf_view_choice"
                textbutton _("Newest first"):
                    action SetField(persistent, "sf_sort_mode", "newest")
                    style "sf_view_choice"

            null height 6
            text _("Slot order: shows slots in numeric order (1, 2, 3...) so locations stay predictable.") style "sf_view_help"
            text _("Newest first: puts the most recently updated saves first and keeps one empty slot ready at the top.") style "sf_view_help"

            null height 16

            text _("SUGGESTED SAVE NAMES") style "sf_section_label"
            null height 8

            hbox:
                spacing 10
                textbutton _("On"):
                    action SetField(persistent, "sf_auto_save_name", True)
                    selected (persistent.sf_auto_save_name is not False)
                    style "sf_view_choice"
                textbutton _("Off"):
                    action SetField(persistent, "sf_auto_save_name", False)
                    selected (persistent.sf_auto_save_name is False)
                    style "sf_view_choice"

            null height 6
            text _("On: pre-fills the save name from the current scene/label when opening Save.") style "sf_view_help"
            text _("Off: keeps whatever name is already in the field, unless you change it manually.") style "sf_view_help"

            null height 16

            text _("OLD SAVE DETECTION") style "sf_section_label"
            null height 8

            hbox:
                spacing 10
                textbutton _("Keep migrated saves hidden"):
                    action SetField(persistent, "sf_migration_reoffer", False)
                    selected (persistent.sf_migration_reoffer is not True)
                    style "sf_view_choice"
                textbutton _("Re-offer migrated saves"):
                    action SetField(persistent, "sf_migration_reoffer", True)
                    selected (persistent.sf_migration_reoffer is True)
                    style "sf_view_choice"

            null height 6
            text _("Keep migrated saves hidden: once a source save was migrated, it stays exempt even if you later move/rename/delete it here.") style "sf_view_help"
            text _("Re-offer migrated saves: show previously migrated source saves again in the migration prompt.") style "sf_view_help"

            null height 20

            textbutton _("Close"):
                action Function(sf_close_view_settings)
                style "sf_edit_cancel"
                xalign 1.0

    key "K_ESCAPE" action Function(sf_close_view_settings)
    key "game_menu" action Function(sf_close_view_settings)

style sf_gear_button is empty:
    background None
    hover_background Solid("#4ceefc22")
    padding (10, 4)

style sf_gear_button_text is gui_text:
    color "#8b7a99"
    hover_color "#4ceefc"
    size 30
    outlines []
    font "DejaVuSans.ttf"

style sf_tip_frame is empty:
    background Solid("#150a1fee")
    padding (18, 12)

style sf_tip_text is gui_text:
    color "#e6dcef"
    size 16
    outlines []
    font gui.interface_text_font
    xmaximum 460

style sf_tip_arrow is gui_text:
    color "#4ceefc"
    size 18
    outlines []
    font "DejaVuSans.ttf"

style sf_view_choice is empty:
    background Solid("#1d1230aa")
    hover_background Solid("#4ceefc33")
    selected_background Solid("#4ceefc22")
    selected_hover_background Solid("#4ceefc44")
    padding (16, 10)

style sf_view_choice_text is gui_text:
    color "#beadc6"
    hover_color "#ffffff"
    selected_color "#4ceefc"
    selected_hover_color "#4ceefc"
    size 17
    outlines []
    font gui.interface_text_font

style sf_view_help is gui_text:
    color "#a99ab8"
    size 15
    outlines []
    font gui.interface_text_font
    xmaximum 900

style sf_page_btn is sf_header_chip

style sf_page_btn_text is sf_header_chip_text:
    insensitive_color "#5a4a68"

style sf_page_label is gui_text:
    color "#8b7a99"
    size 16
    outlines []
    font gui.interface_text_font

################################################################################
## Styles for per-slot actions
################################################################################

style sf_slot_menu_button is empty:
    background Solid("#0a050fcc")
    hover_background Solid("#4ceefcbb")
    padding (12, 2)

style sf_slot_menu_button_text is gui_text:
    color "#4ceefc"
    hover_color "#0a050f"
    size 24
    outlines []
    font gui.interface_text_font
    xalign 0.5

style sf_slot_action_box is empty:
    background Solid("#0a050f88")
    foreground Solid("#4ceefc22")
    padding (2, 2)

style sf_slot_menu_frame is empty:
    background Solid("#150a1fee")
    foreground Solid("#4ceefc22")
    padding (28, 24)

style sf_slot_menu_title is gui_text:
    color "#4ceefc"
    size 22
    kerning 4
    outlines []
    font gui.interface_text_font

style sf_slot_menu_subtitle is gui_text:
    color "#f8eadb"
    size 18
    outlines []
    font gui.interface_text_font

style sf_slot_menu_slot is gui_text:
    color "#8b7a99"
    size 14
    outlines []
    font gui.interface_text_font

style sf_slot_menu_item is empty:
    background Solid("#1d1230aa")
    hover_background Solid("#4ceefc55")
    padding (14, 10)
    xfill True

style sf_slot_menu_item_text is gui_text:
    color "#e8dcf0"
    hover_color "#ffffff"
    size 18
    outlines []
    font gui.interface_text_font

style sf_slot_menu_item_danger is sf_slot_menu_item:
    hover_background Solid("#d10089")

style sf_slot_menu_item_danger_text is sf_slot_menu_item_text:
    color "#d10089"
    hover_color "#ffffff"

style sf_slot_state_source is gui_text:
    color "#4ceefc"
    size 13
    kerning 3
    outlines []
    font gui.interface_text_font

style sf_slot_state_target is sf_slot_state_source:
    color "#8b7a99"

style sf_move_banner_name is gui_text:
    color "#ffffff"
    size 18
    italic True
    outlines []
    font gui.interface_text_font

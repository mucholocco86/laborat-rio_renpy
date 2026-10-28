################################################################################
## Ending / Credits — BlueFox.au v1.2.0
################################################################################
##
## Drop-in end-of-episode / end-of-season screen. Handles the fade-to-black
## transition, per-save chronological memory slideshow, credits panel, and
## the standalone credits viewer reached from the game menu.
##
################################################################################

default ending_memories = []
default ending_seen_images = set()
default ending_seen_scene_log = {}
default ending_current_label = ""
default ending_recommended_save_done = set()
default persistent.ending_recommended_save_done = None

init -1 python:

    import random as _ending_random
    import re as _ending_re

    ## ---------- Episode key derivation -------------------------------------
    def _ending_episode_for_tag(tag):
        if not tag:
            return u""
        prefix = str(tag).split("_", 1)[0]
        if prefix.isdigit():
            try:
                return __("Episode {}").format(int(prefix))
            except Exception:
                return u""
        return u""

    def _ending_episode_num(episode):
        try:
            return int(str(episode).split()[-1])
        except Exception:
            return 0

    def _ending_resolve_item(item):
        try:
            parts = tuple(str(item).split())
            while parts:
                joined = u" ".join(parts)
                if renpy.has_image(joined, exact=True):
                    return joined
                parts = parts[:-1]
        except Exception:
            pass
        return None

    def _ending_resolve_list(items):
        out = []
        for item in items or []:
            resolved = _ending_resolve_item(item)
            if resolved and resolved not in out:
                out.append(resolved)
        return out

    def _ending_persistent_seen_by_episode():
        out = {}
        try:
            seen = renpy.game.persistent._seen_images or {}
        except Exception:
            return out
        for parts in seen.keys():
            try:
                episode = _ending_episode_for_tag(parts[0])
            except Exception:
                continue
            if not episode:
                continue
            item = _ending_resolve_item(u" ".join(str(p) for p in parts))
            if not item:
                continue
            bucket = out.setdefault(episode, [])
            if item not in bucket:
                bucket.append(item)
        return out

    ## ---------- Label tracking ---------------------------------------------
    def _ending_label_entered(name, abnormal):
        try:
            if name:
                store.ending_current_label = str(name)
        except Exception:
            pass

    config.label_callbacks.append(_ending_label_entered)

    ## ---------- Per-save "what did this player see" tracker ----------------
    def _ending_record_current_scene():
        try:
            seen = store.ending_seen_images
            if seen is None:
                seen = set()
                store.ending_seen_images = seen

            log = store.ending_seen_scene_log
            if log is None:
                log = {}
                store.ending_seen_scene_log = log

            label = store.ending_current_label or u""

            for tag in renpy.get_showing_tags("master"):
                episode = _ending_episode_for_tag(tag)
                if not episode:
                    continue
                try:
                    attrs = renpy.get_attributes(tag, layer="master") or ()
                except Exception:
                    attrs = ()
                parts = (tag,) + tuple(attrs)
                item = u" ".join(str(p) for p in parts)
                seen.add(item)

                key = (episode, label)
                bucket = log.get(key)
                if bucket is None:
                    bucket = []
                    log[key] = bucket
                if item not in bucket:
                    bucket.append(item)
        except Exception:
            pass

    config.start_interact_callbacks.append(_ending_record_current_scene)

    ## ---------- Credits file parsing ----------------------------------------
    def load_credits(path="credits.txt"):
        try:
            with renpy.file(path) as f:
                raw = f.read()
        except Exception:
            return []

        try:
            raw = raw.decode("utf-8", "replace")
        except Exception:
            pass

        sections = []
        current = None
        for line in raw.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if stripped.startswith("==") and stripped.endswith("==") and len(stripped) >= 4:
                title = stripped.strip("= ").strip()
                current = {"title": title, "lines": []}
                sections.append(current)
                continue
            if current is None:
                current = {"title": "", "lines": []}
                sections.append(current)
            current["lines"].append(stripped)
        return sections

    def ending_pick_memories(count=20):
        log = store.ending_seen_scene_log or {}

        save_eps = {}
        for key, images in log.items():
            episode = key[0] if isinstance(key, tuple) and key else u""
            if not episode or not images:
                continue
            pool = _ending_resolve_list(images)
            if not pool:
                continue
            save_eps.setdefault(episode, []).append(_ending_random.choice(pool))

        persist_eps = _ending_persistent_seen_by_episode()

        ordered = []
        for episode in sorted(set(save_eps) | set(persist_eps), key=_ending_episode_num):
            picks = list(save_eps.get(episode, []))
            if len(picks) < 5 and episode in persist_eps:
                items = [i for i in persist_eps[episode] if i not in picks]
                take = min(5 - len(picks), len(items))
                if take > 0:
                    step = len(items) / float(take)
                    idxs = sorted({int(i * step) for i in range(take)})
                    picks.extend(items[i] for i in idxs)
            ordered.extend(picks)

        if ordered:
            if len(ordered) > count and count > 0:
                n = len(ordered)
                step = n / float(count)
                indices = []
                for i in range(count):
                    idx = int(i * step)
                    if idx >= n:
                        idx = n - 1
                    if not indices or indices[-1] != idx:
                        indices.append(idx)
                ordered = [ordered[i] for i in indices]
            return ordered

        seen = store.ending_seen_images or set()
        pool = _ending_resolve_list(sorted(n for n in seen if n))
        if not pool:
            pool = [p for p in (store.ending_memories or []) if p]
        if not pool:
            pool = ending_scan_images()
        if not pool:
            return []
        count = min(count, len(pool))
        return _ending_random.sample(pool, count)

    def ending_scan_images(prefix="images/", exts=(".jpg", ".jpeg", ".png", ".webp")):
        try:
            files = renpy.list_files()
        except Exception:
            return []
        out = []
        for f in files:
            lf = f.lower()
            if not lf.startswith(prefix):
                continue
            if lf.endswith(exts):
                out.append(f)
        return out

    ## ---------- Restore globals locked down by ending_sequence ------------
    def _ending_restore_state():
        try:
            if hasattr(store, "_ending_prev_allow_skipping"):
                config.allow_skipping = store._ending_prev_allow_skipping
                del store._ending_prev_allow_skipping
            else:
                config.allow_skipping = True
            if hasattr(store, "_ending_prev_quick_menu"):
                store.quick_menu = store._ending_prev_quick_menu
                del store._ending_prev_quick_menu
            if hasattr(store, "_ending_prev_game_menu"):
                store._game_menu_screen = store._ending_prev_game_menu
                del store._ending_prev_game_menu
        except Exception:
            pass

    config.start_callbacks.append(_ending_restore_state)
    if _ending_restore_state not in config.after_load_callbacks:
        config.after_load_callbacks.append(_ending_restore_state)

    def ending_caption_for(item):
        if not item:
            return u""
        path = item
        try:
            img = renpy.get_registered_image(item)
            fn = getattr(img, "filename", None) if img is not None else None
            if fn:
                path = fn
        except Exception:
            pass
        try:
            parts = path.replace("\\", "/").split("/")
            if len(parts) >= 2:
                folder = parts[-2]
                if folder.lower() == "images" and len(parts) >= 3:
                    folder = parts[-3]
                return folder
        except Exception:
            pass
        return u""

    def recommend_save_point_create(save_title, folder_id="main"):
        try:
            if "sf_init_folders" in globals():
                sf_init_folders()
        except Exception:
            pass

        try:
            fid = folder_id or "main"
            if "sf_get_folder" in globals():
                f = sf_get_folder(fid)
                if not f or f.get("kind") != "user":
                    fid = "main"

            if "_sf_first_free_slot" in globals():
                slot_n = _sf_first_free_slot(fid, 1)
            else:
                slot_n = 1
                while True:
                    slot_name = "{}-{}".format(fid, slot_n)
                    try:
                        if not renpy.slot_mtime(slot_name):
                            break
                    except Exception:
                        break
                    slot_n += 1

            slot_name = "{}-{}".format(fid, slot_n)
            renpy.store.save_name = save_title or ""
            renpy.save(slot_name, extra_info=(save_title or ""))
            return True, slot_name, None, "created"
        except Exception as e:
            return False, None, str(e), "error"

    def recommend_save_point_key(save_title):
        try:
            label = (getattr(store, "ending_current_label", "") or "").strip()
        except Exception:
            label = ""
        return "{}::{}".format(label, save_title or "")

    def recommend_save_point_done_keys():
        try:
            keys = getattr(persistent, "ending_recommended_save_done", None)
            if keys is None:
                keys = set()
        except Exception:
            keys = set()

        try:
            legacy = renpy.store.ending_recommended_save_done
            if legacy:
                keys = set(keys) | set(legacy)
        except Exception:
            pass

        return set(keys)

    def recommend_save_point_set_done(key, value=True):
        keys = recommend_save_point_done_keys()
        if value:
            keys.add(key)
        else:
            keys.discard(key)
        setattr(persistent, "ending_recommended_save_done", set(keys))
        try:
            renpy.save_persistent()
        except Exception:
            pass

    def recommend_save_point_create_once(save_title, folder_id="main", key=None):
        k = key or recommend_save_point_key(save_title)

        if k in recommend_save_point_done_keys():
            return True, None, None, "already"

        recommend_save_point_set_done(k, True)

        ok, slot_name, err, state = recommend_save_point_create(save_title, folder_id)
        if ok:
            return True, slot_name, None, state

        ## Save failed, allow retry later.
        recommend_save_point_set_done(k, False)
        return False, None, err, "error"

################################################################################
## Label: ending_sequence
################################################################################

label ending_sequence(title=_("End of Episode"), credits_file="credits.txt", music="Music/Alessio Acierno - To Light Our Youth.mp3"):

    ## Halt any in-progress skip and prevent it from being re-enabled.
    $ _skipping = False
    $ store._ending_prev_allow_skipping = config.allow_skipping
    $ config.allow_skipping = False

    ## Hide the quick menu (Save / Skip / Auto / Q.Save / Q.Load all gone).
    $ store._ending_prev_quick_menu = quick_menu
    $ quick_menu = False

    ## Disable the game menu (Esc and right-click open nothing).
    $ store._ending_prev_game_menu = _game_menu_screen
    $ _game_menu_screen = None

    python:
        try:
            analytics.track_ending(title)
        except Exception:
            pass

    window hide
    stop music fadeout 2.0
    scene black with Fade(2.0, 1.0, 0.0)

    if music:
        play music music fadein 3.0

    $ _ending_credits_data = load_credits(credits_file)
    $ _ending_pics = ending_pick_memories(20)

    call screen ending_screen(title=title, credits=_ending_credits_data, memories=_ending_pics)

    $ _ending_restore_state()
    return

label recommend_save_point(save_title="Recommended Save"):
    if _in_replay:
        return

    $ _rsp_key = recommend_save_point_key(save_title)
    if _rsp_key in recommend_save_point_done_keys():
        return

    $ _rsp_pick = renpy.call_screen("recommend_save_point_screen", save_title=save_title)
    if _rsp_pick == "save":
        $ _rsp_ok, _rsp_slot, _rsp_err, _rsp_state = recommend_save_point_create_once(save_title, "main", _rsp_key)
        if _rsp_ok:
            if _rsp_state == "created":
                $ renpy.notify(_("Save created in Main."))
        else:
            $ renpy.notify(_("Save failed: {err}").format(err=_rsp_err or _("Unknown error")))

    return

screen recommend_save_point_screen(save_title="Recommended Save"):
    modal True
    zorder 260

    key "K_ESCAPE" action Return("continue")
    key "game_menu" action NullAction()

    add Solid("#06040add")

    frame:
        style "rsp_panel"
        xalign 0.5
        yalign 0.72

        hbox:
            spacing 56

            vbox:
                xsize 760
                spacing 10

                text _("Save Here") style "rsp_title"
                text _("If you choose to save it will save in Main folder as {title}").format(title=save_title) style "rsp_body"

            vbox:
                spacing 12
                xalign 1.0

                textbutton _("Save"):
                    style "rsp_primary"
                    action Return("save")

                textbutton _("Continue"):
                    style "rsp_secondary"
                    action Return("continue")
################################################################################
## Screen: ending_screen
################################################################################

screen ending_screen(title="End of Episode", credits=[], memories=[], standalone=False):
    tag menu
    modal True
    zorder 200

    key "skip"        action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip"   action NullAction()
    key "game_menu"   action NullAction()

    key "K_s"         action NullAction()
    key "K_F5"        action NullAction()
    key "K_F9"        action NullAction()
    key "K_TAB"       action NullAction()
    key "K_LCTRL"     action NullAction()
    key "K_RCTRL"     action NullAction()
    if standalone:
        key "K_ESCAPE" action Return()
    else:
        key "K_ESCAPE" action NullAction()

    default _bg_idx = 0
    default _bg_prev_idx = 0

    if memories and len(memories) > 1:
        timer ENDING_SLIDE_SECONDS repeat True action [
            SetScreenVariable("_bg_prev_idx", _bg_idx),
            SetScreenVariable("_bg_idx", (_bg_idx + 1) % len(memories)),
        ]

    fixed:
        at ending_screen_fade_in

        ## ---------- Slideshow background -----------------------------------
        add Solid("#000000")

        if memories:
            add memories[_bg_prev_idx]:
                xysize (1920, 1080)
                fit "cover"

            add memories[_bg_idx]:
                xysize (1920, 1080)
                fit "cover"
                at ending_slideshow_fade(_bg_idx)

        add Solid("#0a050f99")

        ## ---------- Optional per-slide caption -----------------------------
        if memories:
            $ _slide_caption = ending_caption_for(memories[_bg_idx])
            if _slide_caption:
                frame:
                    background Solid("#0a050fcc")
                    xpos 60
                    ypos 990
                    padding (24, 10)
                    text "[_slide_caption!t]" style "ending_slide_caption_text"

        ## ---------- Right side panel: title / credits ----------------------
        frame:
            background Solid("#0a050fcc")
            xpos 1280
            ypos 0
            xysize (640, 1080)
            padding (40, 50)

            vbox:
                spacing 16
                xfill True

                ## --- Title header -------------------------------------------
                text "[title!t]" style "ending_title_text"

                add Solid("#4ceefc"):
                    xsize 120
                    ysize 2

                ## --- Scrollable credits -------------------------------------
                viewport id "credits_vp":
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    xfill True
                    ysize 880
                    vbox:
                        spacing 8
                        for sec in credits:
                            if sec.get("title"):
                                null height 14
                                text sec["title"] style "ending_section_text"
                                null height 4
                            for ln in sec.get("lines", []):
                                if ln:
                                    text ln style "ending_line_text"
                                else:
                                    null height 14
                        null height 40

        ## ---------- Action button row --------------------------------------
        hbox:
            xalign 0.5
            ypos 1020
            spacing 40

            if standalone:
                textbutton _("< BACK"):
                    action Return()
                    style "ending_button"
            else:
                textbutton _("< BACK"):
                    action [
                        Function(_ending_restore_state),
                        Function(renpy.rollback, force="menu", checkpoints=1),
                    ]
                    style "ending_button"

                textbutton _("MAIN MENU"):
                    action Confirm(
                        _("Are you sure you want to return to the main menu?\nThis will end the current game."),
                        yes=[Function(_ending_restore_state), MainMenu(confirm=False)],
                    )
                    style "ending_button"

## Seconds between slideshow crossfades. Tweak to taste.
define ENDING_SLIDE_SECONDS = 6.0

transform ending_slideshow_fade(idx):
    alpha 0.0
    linear 1.5 alpha 1.0

transform ending_screen_fade_in:
    alpha 0.0
    linear 2.5 alpha 1.0

################################################################################
## Styles
################################################################################

style ending_title_text is default:
    font gui.name_text_font
    size 42
    color "#ffffff"
    kerning 3
    outlines []

style ending_slide_caption_text is default:
    font gui.interface_text_font
    size 22
    color "#4ceefc"
    kerning 6
    outlines []

style ending_section_text is default:
    font gui.interface_text_font
    size 28
    color "#4ceefc"
    kerning 3
    outlines []

style ending_line_text is default:
    font gui.text_font
    size 22
    color "#f0e8f5"
    kerning 1
    line_spacing 6
    outlines []

style ending_button is default:
    background None
    hover_background Solid("#d1008922")
    selected_background Solid("#d1008938")
    selected_hover_background Solid("#d1008955")
    padding (16, 6)

style ending_button_text is default:
    font gui.interface_text_font
    size 18
    color "#f0e8f5"
    hover_color "#ffffff"
    selected_color "#ffffff"
    insensitive_color "#8b7a99"
    kerning 5
    outlines []

style rsp_panel is empty:
    background Solid("#120b1dd9")
    xmaximum 1600
    yminimum 190
    padding (42, 28)

style rsp_title is default:
    font gui.name_text_font
    size 50
    color "#ffffff"
    outlines []

style rsp_body is default:
    font gui.interface_text_font
    size 32
    color "#f0e8f5"
    outlines []

style rsp_primary is default:
    background Solid("#1a364acc")
    hover_background Solid("#24557acc")
    selected_background Solid("#24557acc")
    selected_hover_background Solid("#2a6a97cc")
    padding (28, 12)
    xminimum 660

style rsp_primary_text is default:
    font gui.interface_text_font
    size 42
    color "#eaf8ff"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines []

style rsp_secondary is default:
    background Solid("#ffffff1f")
    hover_background Solid("#ffffff33")
    selected_background Solid("#ffffff2a")
    selected_hover_background Solid("#ffffff44")
    padding (28, 12)
    xminimum 660

style rsp_secondary_text is default:
    font gui.interface_text_font
    size 42
    color "#f0e8f5"
    hover_color "#ffffff"
    selected_color "#ffffff"
    outlines []

################################################################################
## Screen: credits
################################################################################

screen credits():
    tag menu

    default _credits_data = load_credits("credits.txt")
    default _credits_pics = ending_pick_memories(20)

    use ending_screen(title=_("Credits"), credits=_credits_data, memories=_credits_pics, standalone=True)

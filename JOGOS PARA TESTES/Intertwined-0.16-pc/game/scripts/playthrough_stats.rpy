################################################################################
## Playthrough Stats tab — BlueFox.au v1.2.0
################################################################################
##
## Lifetime metrics and per-save recent choices.
##
################################################################################

default persistent.ps_lifetime_seconds = 0

init -5 python:

    import time as _ps_time

    def ps_unique_scenes_seen():
        try:
            labels = getattr(store, "GALLERY_LABELS", None) or []
        except Exception:
            labels = []
        n = 0
        for lbl in labels:
            try:
                if renpy.seen_label(lbl):
                    n += 1
            except Exception:
                pass
        return n

    def ps_gallery_total():
        try:
            return len(getattr(store, "GALLERY_LABELS", None) or [])
        except Exception:
            return 0

    import re as _ps_re
    _PS_EPISODE_FILE_RE = _ps_re.compile(r"(?:^|[\\/])episode_\d+\.rpyc?$", _ps_re.IGNORECASE)

    def _ps_label_from_episode_file(name):
        try:
            node = renpy.game.script.namemap.get(name)
        except Exception:
            return False
        if node is None:
            return False
        fn = getattr(node, "filename", None) or u""
        return bool(_PS_EPISODE_FILE_RE.search(fn))

    def _ps_script_labels():
        cached = getattr(store, "_ps_script_labels_cache", None)
        if cached is not None:
            return cached
        try:
            raw = renpy.get_all_labels()
        except Exception:
            raw = ()
        filtered = tuple(
            l for l in raw
            if l
            and not l.startswith("_")
            and not l[:1].isdigit()
            and _ps_label_from_episode_file(l)
        )
        store._ps_script_labels_cache = filtered
        return filtered

    def ps_story_labels_seen():
        n = 0
        for lbl in _ps_script_labels():
            try:
                if renpy.seen_label(lbl):
                    n += 1
            except Exception:
                pass
        return n

    def ps_story_labels_total():
        return len(_ps_script_labels())

    def ps_choices_lifetime():
        try:
            return int(persistent.cx_choices_total or 0)
        except Exception:
            return 0

    def _ps_session_anchor_ensure():
        if getattr(_ps_commit_runtime, "_anchor", None) is None:
            _ps_commit_runtime._anchor = _ps_time.time()

    def _ps_commit_runtime():
        try:
            _ps_session_anchor_ensure()
            now = _ps_time.time()
            anchor = float(_ps_commit_runtime._anchor or now)
            delta = max(0, int(now - anchor))
            if delta:
                persistent.ps_lifetime_seconds = int(persistent.ps_lifetime_seconds or 0) + delta
            _ps_commit_runtime._anchor = now
        except Exception:
            pass

    def ps_lifetime_seconds_live():
        try:
            _ps_session_anchor_ensure()
            now = _ps_time.time()
            anchor = float(_ps_commit_runtime._anchor or now)
            return int(persistent.ps_lifetime_seconds or 0) + max(0, int(now - anchor))
        except Exception:
            return int(persistent.ps_lifetime_seconds or 0)

    _ps_session_anchor_ensure()

    def ps_format_duration(seconds):
        try:
            total = max(0, int(seconds or 0))
        except Exception:
            total = 0
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        if h:
            return __("{h}h {m:02d}m {s:02d}s").format(h=h, m=m, s=s)
        return __("{m}m {s:02d}s").format(m=m, s=s)

    _PS_EP_RE = _ps_re.compile(r"episode_(\d+)\.rpy", _ps_re.IGNORECASE)

    def ps_current_scene_label_raw():
        try:
            sf = getattr(store, "_sf_last_label", None)
            if isinstance(sf, str) and sf:
                return sf
        except Exception:
            pass
        try:
            cur = getattr(renpy.game.context(), "current", None)
            if isinstance(cur, str) and cur and not cur.startswith("_"):
                return cur
        except Exception:
            pass
        return ""

    def ps_pretty_scene_label(name):
        txt = (name or "").replace("_", " ")
        txt = _ps_re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)
        txt = _ps_re.sub(r"([A-Za-z])(\d)", r"\1 \2", txt)
        txt = _ps_re.sub(r"\s+", " ", txt).strip()
        if not txt:
            return _("(unknown)")
        parts = []
        for w in txt.split(" "):
            if w.isupper() or w[:1].isupper():
                parts.append(w)
            else:
                parts.append(w.capitalize())
        return " ".join(parts)

    def ps_current_episode_label():
        raw = ps_current_scene_label_raw()
        if raw:
            try:
                node = renpy.game.script.lookup_or_none(raw)
            except Exception:
                node = None
            fn = getattr(node, "filename", "") if node is not None else ""
            m = _PS_EP_RE.search(fn or "")
            if m:
                return __("Episode {n}").format(n=int(m.group(1)))
        return _("Unknown")

    def ps_points_snapshot():
        out = []
        try:
            items = list(vars(store).items())
        except Exception:
            items = []
        for name, value in items:
            if not isinstance(name, str):
                continue
            if name.startswith("_"):
                continue
            if not (name.endswith("_Points") or name.endswith("Points")):
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                continue
            label = name.replace("_", " ")
            out.append((label, float(value), str(value)))
        out.sort(key=lambda x: (-x[1], x[0].lower()))
        if out and out[0][1] <= 0:
            return []
        return [(label, value_text) for label, _num, value_text in out]

    _ps_session_anchor_ensure()
    config.quit_callbacks.append(_ps_commit_runtime)
    config.after_load_callbacks.append(_ps_session_anchor_ensure)

screen px_pref_stats():
    vbox:
        spacing 36

        use px_tab_header(_("Stats"))

        ## ── Choice indicator toggle ───────────────────────────────
        use px_field(_("PREVIOUSLY PICKED")):
            vbox:
                style_prefix "px_check"
                spacing 2
                $ _cx_on = bool(persistent.cx_show_marker)
                textbutton (_("Hide marker on previously-picked options") if _cx_on else _("Show marker on previously-picked options")):
                    action ToggleField(persistent, "cx_show_marker")
                    selected _cx_on
                    xminimum 560

        text _("When on, a small dot appears next to choices you've previously selected at the same menu."):
            style "px_hint"

        ## ── Lifetime metrics ──────────────────────────────────────
        use px_field(_("LIFETIME")):
            vbox:
                spacing 10
                $ _ps_gallery_total = ps_gallery_total()
                $ _ps_gallery_seen = ps_unique_scenes_seen()
                $ _ps_scenes = (u"{} / {}".format(_ps_gallery_seen, _ps_gallery_total) if _ps_gallery_total else str(_ps_gallery_seen))
                $ _ps_label_total = ps_story_labels_total()
                $ _ps_label_seen = ps_story_labels_seen()
                $ _ps_labels = (u"{} / {}".format(_ps_label_seen, _ps_label_total) if _ps_label_total else str(_ps_label_seen))
                use ps_stat_row(_("Gallery scenes unlocked"), _ps_scenes)
                use ps_stat_row(_("Story scenes seen"), _ps_labels)
                use ps_stat_row(_("Choices made"), str(ps_choices_lifetime()))

        ## ── Current save / run snapshot ───────────────────────────
        $ _ps_episode = ps_current_episode_label()
        if _ps_episode != _("Unknown"):
            use px_field(_("CURRENT SAVE")):
                vbox:
                    spacing 10
                    $ _ps_scene = ps_pretty_scene_label(ps_current_scene_label_raw())
                    $ _ps_points = ps_points_snapshot()
                    use ps_stat_row(_("Current scene"), _ps_scene)
                    use ps_stat_row(_("Current episode"), _ps_episode)

                    null height 10

                    text _("POINT VARIABLES") style "px_field_label"
                    if not _ps_points:
                        text _("No *Points variables found in current save state."):
                            style "px_hint"
                    else:
                        frame:
                            background Solid("#150a1f80")
                            xfill True
                            padding (16, 14, 16, 14)

                            viewport:
                                ymaximum 320
                                scrollbars "vertical"
                                mousewheel True
                                draggable True
                                pagekeys True
                                xfill True

                                vbox:
                                    spacing 10
                                    for _name, _value in _ps_points:
                                        use ps_stat_row(_name, _value)

        ## ── Recent choices on this save ───────────────────────────
        use px_field(_("RECENT CHOICES")):
            $ _ps_hist = cx_history_for_display()
            if not _ps_hist:
                text _("No choices recorded on this save yet."):
                    style "px_hint"
            else:
                frame:
                    background Solid("#150a1f80")
                    xfill True
                    padding (16, 14, 16, 14)

                    viewport:
                        ymaximum 420
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        xfill True

                        vbox:
                            spacing 10
                            for _entry in _ps_hist:
                                use ps_history_row(_entry)

screen ps_stat_row(label, value):
    hbox:
        spacing 24

        text "[label!t]":
            style "ps_stat_label"
            min_width 360
            text_align 0.0
            yalign 0.5

        text "[value!t]":
            style "ps_stat_value"
            yalign 0.5

screen ps_history_row(entry):
    $ _ps_caption = entry.get(u"caption", u"") or u""
    $ _ps_label = entry.get(u"label", u"") or u""

    hbox:
        spacing 14
        xfill True

        vbox:
            spacing 2
            text "[_ps_caption!tq]" style "ps_hist_caption"
            if _ps_label:
                text "[_ps_label!q]" style "ps_hist_label"

style ps_stat_label is gui_text:
    color "#beadc6"
    size 24
    outlines []
    font gui.interface_text_font

style ps_stat_value is gui_text:
    color "#4ceefc"
    size 28
    kerning 2
    outlines []
    font gui.interface_text_font

style ps_hist_caption is gui_text:
    color "#f8eadb"
    size 22
    outlines []
    font gui.interface_text_font

style ps_hist_label is gui_text:
    color "#8b7a99"
    size 18
    italic True
    outlines []
    font gui.interface_text_font

style ps_hist_time is gui_text:
    color "#8b7a99"
    size 18
    outlines []
    font gui.interface_text_font

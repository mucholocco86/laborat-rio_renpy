################################################################################
## Preferences screen — BlueFox v1.2.0
################################################################################
##
## Sidebar-tabbed settings.
##
################################################################################

## ── State ────────────────────────────────────────────────────────────────
default preferences.text_cps = 0
default preferences.afm_time = 15
default preferences.fullscreen = False
default preferences.skip_unseen = False
default preferences.skip_after_choices = False
default preferences.desktop_rollback_side = "disable"
default preferences.transitions = 2
define gui.default_music_volume = 0.5
define gui.default_sound_volume = 0.5
define gui.default_voice_volume = 0.5
default persistent.text_box_opacity = 0.0
default persistent.alt_menu_bg = True

default pref_active_tab = "display"

default persistent.autosave_enabled = True

## Skip-speed presets.
default persistent.skip_speed = "fast"

define PX_SKIP_SPEEDS = {
    "normal":  75,   ## ~13 lines/s
    "fast":    25,   ## ~40 lines/s
    "instant":  0,   ## engine cap (~60 lines/s @ 60 FPS)
}

init 100 python:
    if persistent.autosave_enabled is False:
        renpy.store._autosave = False

    config.fast_skipping = True

    config.skip_delay = PX_SKIP_SPEEDS.get(persistent.skip_speed, 0)

    def px_set_skip_speed(name):
        persistent.skip_speed = name
        config.skip_delay = PX_SKIP_SPEEDS.get(name, 0)

init python:
    def px_open_saves_folder():
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

    def px_now_playing_label():
        import os as _os
        try:
            track = renpy.music.get_playing("music")
        except Exception:
            track = None
        if not track:
            return _("(silence)")
        name = _os.path.basename(track)
        stem, _ext = _os.path.splitext(name)
        return stem.replace("_", " ").strip() or _("(silence)")

################################################################################
## Outer shell
################################################################################

screen preferences():

    tag menu

    on "show" action Function(intertwined_set_pause_screen, "preferences")

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"
                xfill True
                yfill True

                viewport:
                    xfill True
                    yfill True
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    frame:
                        background None
                        xfill True
                        padding (72, 60, 72, 60)

                        vbox:
                            xfill True

                            if pref_active_tab == "display":
                                use px_pref_display
                            elif pref_active_tab == "reading":
                                use px_pref_reading
                            elif pref_active_tab == "audio":
                                use px_pref_audio
                            elif pref_active_tab == "controls":
                                use px_pref_controls
                            elif pref_active_tab == "accessibility":
                                use px_pref_accessibility
                            elif pref_active_tab == "stats":
                                use px_pref_stats
                            elif pref_active_tab == "privacy":
                                use px_pref_privacy
                            elif pref_active_tab == "system":
                                use px_pref_system

                            null height 60

    use prefs_nav

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

################################################################################
## Helpers
################################################################################

screen px_tab(tab_id, label):
    button:
        style "px_tab_button"
        action SetVariable("pref_active_tab", tab_id)
        selected pref_active_tab == tab_id

        hbox:
            spacing 14
            yalign 0.5

            if pref_active_tab == tab_id:
                add Solid("#00d1d1") xysize (3, 28)
            else:
                null width 3 height 22

            text "[label!t]" style "px_tab_button_text"

screen px_tab_header(title):
    vbox:
        spacing 10
        text "[title!t]" style "px_tab_header_text"
        add Solid("#d10089") xysize (54, 2)
        null height 28

screen px_field(label):
    vbox:
        spacing 12
        text "[label!t]" style "px_field_label"
        transclude

################################################################################
## Tab: Display
################################################################################

screen px_pref_display():
    vbox:
        spacing 36

        use px_tab_header(_("Display"))

        if renpy.variant("pc"):
            use px_field(_("WINDOW MODE")):
                hbox:
                    style_prefix "px_pill"
                    spacing 8
                    textbutton _("Windowed") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

        use px_field(_("LANGUAGE")):
            $ available_languages = sorted(l for l in renpy.known_languages() if l)
            if available_languages:
                hbox:
                    style_prefix "px_pill"
                    box_wrap True
                    spacing 8
                    textbutton _("English"):
                        action Language(None)
                        selected _preferences.language is None
                    for lang in available_languages:
                        textbutton "[lang!c]":
                            action Language(lang)
                            selected _preferences.language == lang
            else:
                text _("Only English is shipped with this build. Additional languages will appear here when added."):
                    style "px_hint"

################################################################################
## Tab: Reading
################################################################################

screen px_pref_reading():
    vbox:
        spacing 36

        use px_tab_header(_("Reading"))

        use px_field(_("TEXT SPEED")):
            bar value Preference("text speed") xsize 940

        use px_field(_("AUTO-FORWARD TIME")):
            bar value Preference("auto-forward time") xsize 940

        use px_field(_("TEXTBOX OPACITY")):
            bar:
                value FieldValue(persistent, "text_box_opacity", range=1.0)
                style "slider"
                xsize 940

        use px_field(_("SKIP")):
            hbox:
                style_prefix "px_check"
                spacing 32
                textbutton _("Skip unseen text") action Preference("skip", "toggle")
                textbutton _("Skip after choices") action Preference("after choices", "toggle")
                textbutton _("Play transitions while skipping"):
                    action InvertSelected(Preference("transitions", "toggle"))

        use px_field(_("SKIP SPEED")):
            hbox:
                style_prefix "px_pill"
                spacing 8
                textbutton _("Normal"):
                    action Function(px_set_skip_speed, "normal")
                    selected persistent.skip_speed == "normal"
                textbutton _("Fast"):
                    action Function(px_set_skip_speed, "fast")
                    selected persistent.skip_speed == "fast"
                textbutton _("Instant"):
                    action Function(px_set_skip_speed, "instant")
                    selected persistent.skip_speed == "instant"
            text _("Speed of the hold-Ctrl skip loop. \"Instant\" runs at the engine's render-rate cap (~60 lines/sec). Press {b}>{/b} during play to race to the next choice."):
                style "px_hint"

################################################################################
## Tab: Audio
################################################################################

screen px_pref_audio():
    vbox:
        spacing 36

        use px_tab_header(_("Audio"))

        if config.has_music:
            use px_field(_("NOW PLAYING")):
                text px_now_playing_label() style "px_now_playing"

            use px_field(_("MUSIC")):
                bar value Preference("music volume") xsize 940

        if config.has_sound:
            use px_field(_("SOUND EFFECTS")):
                hbox:
                    spacing 18
                    bar:
                        value Preference("sound volume")
                        xsize (820 if config.sample_sound else 940)
                        yalign 0.5
                    if config.sample_sound:
                        textbutton _("Test"):
                            action Play("sound", config.sample_sound)
                            style "px_test_button"

        if config.has_voice:
            use px_field(_("VOICE")):
                hbox:
                    spacing 18
                    bar:
                        value Preference("voice volume")
                        xsize (820 if config.sample_voice else 940)
                        yalign 0.5
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "px_test_button"

        null height 4
        textbutton _("Mute everything"):
            action Preference("all mute", "toggle")
            style "px_mute_button"

################################################################################
## Tab: Controls
################################################################################

screen px_pref_controls():
    vbox:
        spacing 36

        use px_tab_header(_("Controls"))

        use px_field(_("ROLLBACK ON MOUSE EDGE")):
            hbox:
                style_prefix "px_pill"
                spacing 8
                textbutton _("Off") action Preference("rollback side", "disable")
                textbutton _("Left edge") action Preference("rollback side", "left")
                textbutton _("Right edge") action Preference("rollback side", "right")

        text _("Drag the chosen edge of the screen to roll dialogue backwards. Useful on touch screens or trackpads where the mouse wheel is awkward."):
            style "px_hint"

        null height 12

        use px_keymap_section(_("DIALOGUE"), [
            (_("Advance"),                 _("Space · Enter · Left-click")),
            (_("Rollback"),                _("Page Up · Scroll wheel up · Mouse Back")),
            (_("Rollforward"),             _("Page Down · Scroll wheel down · Mouse Forward")),
            (_("Hide interface"),          _("H · Middle-click")),
        ])

        use px_keymap_section(_("SKIP & AUTO"), [
            (_("Skip (hold)"),             _("Ctrl")),
            (_("Toggle skip"),             _("Tab")),
            (_("Race to next choice"),     _("Shift + . (>)")),
            (_("Toggle auto-forward"),     _("A")),
        ])

        use px_keymap_section(_("SAVE & LOAD"), [
            (_("Save menu"),               _("P")),
            (_("Load menu"),               _("L")),
            (_("Quick save"),              _("F5")),
            (_("Quick load"),              _("F9")),
        ])

        use px_keymap_section(_("MENUS & WINDOW"), [
            (_("Game menu / Preferences"),  _("Escape · Right-click")),
            (_("Debug Overlay"),            _("F8")),
            (_("Toggle fullscreen"),        _("Alt + Enter · F")),
            (_("Screenshot"),               _("Print Screen · S")),
            (_("Quit"),                     _("Alt + F4")),
        ])

        use px_keymap_section(_("ACCESSIBILITY"), [
            (_("Toggle self-voicing"),     _("V")),
            (_("Clipboard voicing"),       _("Shift + C")),
        ])

## ── Helpers (Controls tab) ──────────────────────────────────────────────

screen px_keymap_section(title, rows):
    vbox:
        spacing 8
        text "[title!t]" style "px_field_label"
        for label, keys in rows:
            hbox:
                xfill True
                spacing 24
                text "[label!t]" style "px_keymap_action"
                text "[keys!t]" style "px_keymap_keys" xalign 1.0

################################################################################
## Tab: Accessibility
################################################################################

screen px_pref_accessibility():
    vbox:
        spacing 36

        use px_tab_header(_("Accessibility"))

        use px_field(_("SELF-VOICING")):
            hbox:
                style_prefix "px_pill"
                spacing 8
                textbutton _("Off"):
                    action SetField(_preferences, "self_voicing", False)
                    selected _preferences.self_voicing is False
                textbutton _("Text-to-speech"):
                    action SetField(_preferences, "self_voicing", True)
                    selected _preferences.self_voicing is True
                textbutton _("Copy to clipboard"):
                    action SetField(_preferences, "self_voicing", "clipboard")
                    selected _preferences.self_voicing == "clipboard"

        use px_field(_("HIGH CONTRAST TEXT")):
            hbox:
                style_prefix "px_pill"
                spacing 8
                textbutton _("Off") action Preference("high contrast text", "disable")
                textbutton _("On") action Preference("high contrast text", "enable")

        use px_field(_("FONT OVERRIDE")):
            hbox:
                style_prefix "px_pill"
                spacing 8
                textbutton _("Default") action Preference("font transform", None)
                textbutton _("OpenDyslexic") action Preference("font transform", "opendyslexic")
                textbutton _("DejaVu Sans") action Preference("font transform", "dejavusans")

################################################################################
## Tab: Privacy
################################################################################

screen px_pref_privacy():
    vbox:
        spacing 36

        use px_tab_header(_("Privacy"))

        use px_field(_("ANALYTICS")):
            vbox:
                style_prefix "px_check"
                spacing 2
                $ _analytics_on = not persistent.analytics_opt_out
                textbutton (_("Disable Analytics") if _analytics_on else _("Enable Analytics")):
                    action SetField(persistent, "analytics_opt_out", _analytics_on)
                    selected _analytics_on

        text _("Anonymous analytics help track playtime and choice patterns across the player base."):
            style "px_hint"

        use px_field(_("DISCORD")):
            vbox:
                style_prefix "px_check"
                spacing 2
                $ _rpc_on = (persistent.discord_rpc_enabled is not False)
                textbutton (_("Disable Discord RPC") if _rpc_on else _("Enable Discord RPC")):
                    action ToggleDiscordRPC()
                    selected _rpc_on

        text _("Rich Presence shows the current episode and scene on your Discord profile while you play."):
            style "px_hint"

        null height 8
        textbutton _("Read the privacy policy  →"):
            action OpenURL("https://valerianyx.com/privacy")
            style "px_link_button"

################################################################################
## Tab: System
################################################################################

screen px_pref_system():
    vbox:
        spacing 36

        use px_tab_header(_("System"))

        use px_field(_("FILES")):
            vbox:
                spacing 10
                textbutton _("Open saves folder in file explorer"):
                    action Function(px_open_saves_folder)
                    style "px_files_button"
                text _("Opens the folder where your saves and settings are stored."):
                    style "px_hint"

        use px_field(_("AUTOSAVE")):
            vbox:
                spacing 10
                hbox:
                    style_prefix "px_pill"
                    spacing 8
                    textbutton _("Off"):
                        action [SetField(persistent, "autosave_enabled", False), SetVariable("_autosave", False)]
                        selected (persistent.autosave_enabled is False)
                    textbutton _("On"):
                        action [SetField(persistent, "autosave_enabled", True), SetVariable("_autosave", True)]
                        selected (persistent.autosave_enabled is not False)

        null height 8

        text _("DANGER ZONE") style "px_danger_label"
        null height 8

        textbutton _("Reset all preferences to defaults"):
            style "px_reset_button"
            action Confirm(
                _("Reset every preference to its default value?\n\nYour save files will not be touched."),
                yes=[
                    Preference("display", "window"),
                    Preference("transitions", "all"),
                    Preference("text speed", 150),
                    Preference("auto-forward time", 15),
                    SetField(persistent, "text_box_opacity", 0.0),
                    Function(px_set_skip_speed, "normal"),
                    SetField(_preferences, "skip_unseen", False),
                    SetField(_preferences, "skip_after_choices", False),
                    Preference("music volume", 0.5),
                    Preference("sound volume", 0.5),
                    Preference("voice volume", 0.5),
                    Preference("rollback side", "disable"),
                    SetField(_preferences, "self_voicing", False),
                    Preference("high contrast text", "disable"),
                    Preference("font transform", None),
                    SetVariable("_autosave", True),
                    SetField(persistent, "autosave_enabled", True),
                    SetField(persistent, "sf_auto_save_name", True),
                    If(persistent.discord_rpc_enabled is False, true=ToggleDiscordRPC()),
                ],
            )

################################################################################
## Styles (px_*)
################################################################################

## ── Sidebar tab buttons ─────────────────────────────────────────────────

style px_tab_button is empty:
    background None
    hover_background Solid("#4ceefc4d")
    selected_background Solid("#4ceefc59")
    selected_hover_background Solid("#4ceefc73")
    padding (14, 14)
    xfill True

style px_tab_button_text is gui_text:
    color "#e8dcf0"
    hover_color "#4ceefc"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    size 20
    kerning 4
    outlines []
    font gui.interface_text_font
    yalign 0.5

## ── Section headers ─────────────────────────────────────────────────────

style px_tab_header_text is gui_text:
    color "#f8eadb"
    size 50
    outlines []
    font gui.interface_text_font

style px_field_label is gui_text:
    color "#4ceefc"
    size 22
    kerning 6
    outlines []
    font gui.interface_text_font

style px_hint is gui_text:
    color "#8b7a99"
    size 22
    outlines []
    italic True
    font gui.interface_text_font

style px_now_playing is gui_text:
    color "#4ceefc"
    size 26
    outlines []
    font gui.interface_text_font

## ── Controls-tab keymap rows ────────────────────────────────────────────

style px_keymap_action is gui_text:
    color "#e8dcf0"
    size 22
    outlines []
    font gui.interface_text_font

style px_keymap_keys is gui_text:
    color "#4ceefc"
    size 22
    outlines []
    font gui.interface_text_font

style px_danger_label is gui_text:
    color "#d10089"
    size 22
    kerning 6
    outlines []
    font gui.interface_text_font

## ── Pill-style segmented selector (radio) ───────────────────────────────

style px_pill_button is empty:
    background Solid("#1d1230cc")
    hover_background Solid("#2a1640dd")
    selected_background Solid("#d10089")
    selected_hover_background Solid("#e6189c")
    insensitive_background Solid("#150a1f80")
    padding (22, 12)
    xminimum 120

style px_pill_button_text is gui_text:
    color "#beadc6"
    hover_color "#4ceefc"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    insensitive_color "#5a4a68"
    size 26
    outlines []
    xalign 0.5
    font gui.interface_text_font

## ── Inline check rows ───────────────────────────────────────────────────

style px_check_button is empty:
    background Solid("#150a1fcc")
    hover_background Solid("#1d1230dd")
    selected_background Solid("#1d12309c")
    selected_hover_background Solid("#261540dd")
    padding (16, 12)
    xfill False

style px_check_button_text is gui_text:
    color "#8b7a99"
    hover_color "#4ceefc"
    selected_color "#d10089"
    selected_hover_color "#e6189c"
    size 26
    outlines []
    font gui.interface_text_font

## ── Audio test trigger ──────────────────────────────────────────────────

style px_test_button is empty:
    background None
    padding (8, 6)
    yalign 0.5

style px_test_button_text is gui_text:
    color "#4ceefc"
    hover_color "#ffffff"
    size 22
    kerning 4
    underline True
    outlines []
    font gui.interface_text_font

## ── Mute everything ─────────────────────────────────────────────────────

style px_mute_button is empty:
    background Solid("#1d1230cc")
    hover_background Solid("#2a1640dd")
    selected_background Solid("#d10089")
    selected_hover_background Solid("#e6189c")
    padding (24, 14)
    xminimum 340

style px_mute_button_text is gui_text:
    color "#beadc6"
    hover_color "#4ceefc"
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
    size 26
    kerning 4
    outlines []
    xalign 0.5
    font gui.interface_text_font

## ── Reset button (System tab) ───────────────────────────────────────────

style px_reset_button is empty:
    background Solid("#1d1230cc")
    hover_background Solid("#d10089")
    padding (22, 14)
    xminimum 360

style px_reset_button_text is gui_text:
    color "#d10089"
    hover_color "#ffffff"
    size 24
    kerning 4
    outlines []
    xalign 0.0
    font gui.interface_text_font

## ── Open-files button (System tab) ──────────────────────────────────────

style px_files_button is empty:
    background Solid("#1d1230cc")
    hover_background Solid("#4ceefc44")
    padding (22, 14)
    xminimum 360

style px_files_button_text is gui_text:
    color "#4ceefc"
    hover_color "#ffffff"
    size 24
    kerning 4
    outlines []
    xalign 0.0
    font gui.interface_text_font

## ── Privacy policy link ─────────────────────────────────────────────────

style px_link_button is empty:
    background None
    padding (4, 6)

style px_link_button_text is gui_text:
    color "#4ceefc"
    hover_color "#ffffff"
    size 24
    underline True
    outlines []
    font gui.interface_text_font

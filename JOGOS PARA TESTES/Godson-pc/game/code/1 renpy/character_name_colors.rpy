init offset = 180




define -180 GODSON_DEFAULT_NAME_COLOR = "#FFD85A"

default -180 persistent.godson_character_name_colors = { }

default -180 godson_name_color_selected = "marnie"
default -180 godson_name_color_dropdown = False
default -180 godson_name_color_dropdown_hovered = False
default -180 godson_color_picker_character = "marnie"
default -180 godson_color_picker_red = 255
default -180 godson_color_picker_green = 216
default -180 godson_color_picker_blue = 90
default -180 godson_color_picker_hex = "#FFD85A"
default -180 godson_color_picker_error = ""


init -10 python:

    GODSON_NAME_COLOR_CHARACTERS = (
    ("player", "MAIN CHARACTER"),
    ("marnie", "MARNIE"),
    ("henry", "HENRY"),
    ("jennifer", "JENNIFER"),
    ("yuni", "YUNI"),
    ("lorraine", "LORRAINE"),
    ("myles", "MYLES"),
    ("martha", "MARTHA"),
    ("gianna", "GIANNA"),
    ("narrator", "NARRATOR"),
    ("father", "FATHER"),
    ("bianca", "BIANCA"),
    ("nina", "NINA"),
    ("tania", "TANIA"),
    ("kyle", "KYLE"),
    ("janice", "JANICE"),
    ("dan", "DAN"),
    ("brian", "BRIAN"),
    ("sun", "SUN"),
    ("george", "GEORGE"),
    ("robert", "ROBERT"),
    ("therapist", "THERAPIST"),
    ("ceo", "CEO"),
    ("pizza_guy", "PIZZA GUY"),
    ("cheesecake", "CHEESECAKE"),
    ("jay", "JAY"),
    ("unknown", "???"),
    ("unknown_man", "UNKNOWN MAN"),
    ("him", "HIM"),
    ("bianca_children", "BIANCA'S CHILDREN"),
    ("first_child", "FIRST CHILD"),
    ("second_child", "SECOND CHILD"),
)

    GODSON_NAME_COLOR_STATIC_NAMES = {
    "marnie": "Marnie",
    "henry": "Henry",
    "jennifer": "Jennifer",
    "yuni": "Yuni",
    "lorraine": "Lorraine",
    "myles": "Myles",
    "martha": "Martha",
    "gianna": "Gianna",
    "narrator": "Narrator",
    "bianca": "Bianca",
    "nina": "Nina",
    "tania": "Tania",
    "kyle": "Kyle",
    "janice": "Janice",
    "dan": "Dan",
    "brian": "Brian",
    "sun": "Sun",
    "george": "George",
    "robert": "Robert",
    "therapist": "Therapist",
    "ceo": "CEO",
    "pizza_guy": "Pizza Guy",
    "cheesecake": "Cheesecake",
    "jay": "JAY",
    "unknown": "???",
    "unknown_man": "Unknown Man",
    "him": "Him",
    "bianca_children": "Bianca's Children",
    "first_child": "First Child",
    "second_child": "Second Child",
}

    GODSON_NAME_COLOR_PRESETS = (
    "#FFD85A", "#FF5A67", "#FF8A4C", "#F46BFF", "#A66CFF", "#5B7CFF",
    "#39A9FF", "#31E4F3", "#48E0A4", "#9BE34B", "#F5F1E8", "#AEB8C4",
)

    def godson_normalize_name_color(value):
        if value is None:
            return None
        
        value = str(value).strip()
        if not value:
            return None
        
        if not value.startswith("#"):
            value = "#" + value
        
        if len(value) == 4:
            value = "#" + "".join(ch * 2 for ch in value[1:])
        
        if len(value) != 7:
            return None
        
        try:
            int(value[1:], 16)
        except ValueError:
            return None
        
        return value.upper()

    def godson_character_editor_label(character_id):
        if character_id == "player":
            return str(getattr(store, "playerName", None) or "MAIN CHARACTER").upper()
        if character_id == "father":
            return str(getattr(store, "fatherName", None) or "FATHER").upper()
        
        for candidate_id, label in GODSON_NAME_COLOR_CHARACTERS:
            if candidate_id == character_id:
                return label
        
        return str(character_id).replace("_", " ").upper()

    def godson_character_spoken_name(character_id):
        if character_id == "player":
            return str(getattr(store, "playerName", None) or "Braden")
        if character_id == "father":
            return str(getattr(store, "fatherName", None) or "Father")
        return GODSON_NAME_COLOR_STATIC_NAMES.get(character_id, character_id)

    def godson_name_color_settings():
        value = getattr(persistent, "godson_character_name_colors", None)
        if not isinstance(value, dict):
            persistent.godson_character_name_colors = { }
        return persistent.godson_character_name_colors

    def godson_character_name_color(character_id):
        value = godson_name_color_settings().get(character_id)
        return godson_normalize_name_color(value) or GODSON_DEFAULT_NAME_COLOR

    def godson_character_id_from_who(who):
        if who is None:
            return None
        
        try:
            clean_name = renpy.filter_text_tags(str(who), allow=set())
        except Exception:
            clean_name = str(who)
        
        clean_name = clean_name.strip().casefold()
        if not clean_name:
            return None
        
        player_aliases = (
        getattr(store, "playerName", None),
        getattr(store, "MC_Name", None),
    )
        if any(str(alias).strip().casefold() == clean_name for alias in player_aliases if alias):
            return "player"
        
        for character_id, _label in GODSON_NAME_COLOR_CHARACTERS:
            if godson_character_spoken_name(character_id).strip().casefold() == clean_name:
                return character_id
        
        return None

    def godson_name_color_for(who):
        character_id = godson_character_id_from_who(who)
        if character_id is None:
            return GODSON_DEFAULT_NAME_COLOR
        return godson_character_name_color(character_id)

    def godson_select_name_color_character(character_id):
        store.godson_name_color_selected = character_id
        store.godson_name_color_dropdown = False
        store.godson_name_color_dropdown_hovered = False
        renpy.restart_interaction()

    def godson_toggle_name_color_dropdown():
        store.godson_name_color_dropdown = not store.godson_name_color_dropdown
        store.godson_name_color_dropdown_hovered = False
        renpy.restart_interaction()

    def godson_color_picker_rgb_from_hex(color):
        color = godson_normalize_name_color(color) or GODSON_DEFAULT_NAME_COLOR
        return (
        int(color[1:3], 16),
        int(color[3:5], 16),
        int(color[5:7], 16),
    )

    def godson_color_picker_preview():
        return "#{:02X}{:02X}{:02X}".format(
        max(0, min(255, int(store.godson_color_picker_red))),
        max(0, min(255, int(store.godson_color_picker_green))),
        max(0, min(255, int(store.godson_color_picker_blue))),
    )

    def godson_color_picker_update_from_rgb():
        store.godson_color_picker_hex = godson_color_picker_preview()
        store.godson_color_picker_error = ""

    def godson_color_picker_set_hex(color):
        color = godson_normalize_name_color(color)
        if color is None:
            store.godson_color_picker_error = _("Enter a valid six-digit hex color, such as #FF5A67.")
            renpy.restart_interaction()
            
            
            
            
            return
        
        red, green, blue = godson_color_picker_rgb_from_hex(color)
        store.godson_color_picker_red = red
        store.godson_color_picker_green = green
        store.godson_color_picker_blue = blue
        store.godson_color_picker_hex = color
        store.godson_color_picker_error = ""
        renpy.restart_interaction()
        return

    def godson_open_name_color_picker(character_id):
        store.godson_color_picker_character = character_id
        godson_color_picker_set_hex(godson_character_name_color(character_id))
        renpy.show_screen("godson_name_color_picker")
        renpy.restart_interaction()

    def godson_apply_name_color_picker():
        color = godson_normalize_name_color(store.godson_color_picker_hex)
        if color is None:
            store.godson_color_picker_error = _("Enter a valid six-digit hex color, such as #FF5A67.")
            renpy.restart_interaction()
            return
        
        updated = dict(godson_name_color_settings())
        updated[store.godson_color_picker_character] = color
        persistent.godson_character_name_colors = updated
        renpy.save_persistent()
        renpy.hide_screen("godson_name_color_picker")
        renpy.restart_interaction()

    def godson_reset_character_name_color(character_id):
        updated = dict(godson_name_color_settings())
        updated.pop(character_id, None)
        persistent.godson_character_name_colors = updated
        renpy.save_persistent()
        
        if renpy.get_screen("godson_name_color_picker") is not None:
            godson_color_picker_set_hex(GODSON_DEFAULT_NAME_COLOR)
        else:
            renpy.restart_interaction()

    def godson_cancel_name_color_picker():
        renpy.hide_screen("godson_name_color_picker")
        renpy.restart_interaction()


init -5 screen godson_name_color_editor():
    $ selected_id = godson_name_color_selected
    $ selected_label = godson_character_editor_label(selected_id)
    $ selected_color = godson_character_name_color(selected_id)

    frame:
        style "ui_preferences_panel"
        xfill True

        has vbox
        spacing 22
        xfill True

        text _("CHARACTER NAME COLORS") style "ui_preferences_label"
        text _("Keep Godson's signature gold, or give individual speakers their own colors. Changes apply to dialogue and History across every save.") style "ui_preferences_description"

        hbox:
            spacing 24
            xfill True
            yalign 0.5

            vbox:
                spacing 10
                xsize 830

                text _("CHARACTER") style "godson_name_color_caption"

                textbutton _("[selected_label]  ▼"):
                    style "godson_name_color_selector"
                    action Function(godson_toggle_name_color_dropdown)
                    at ui_button_motion

            frame:
                style "godson_name_color_preview"
                xsize 830

                has vbox
                spacing 5
                xalign 0.5
                yalign 0.5

                text selected_label:
                    style "godson_name_color_preview_name"
                    color selected_color
                    xalign 0.5

                text selected_color:
                    style "godson_name_color_hex_readout"
                    xalign 0.5

            vbox:
                spacing 10
                xsize 250

                text _("COLOR") style "godson_name_color_caption" xalign 0.5

                button:
                    style "godson_name_color_swatch_shell"
                    action Function(godson_open_name_color_picker, selected_id)
                    at ui_button_motion

                    add Solid(selected_color):
                        xalign 0.5
                        yalign 0.5
                        xysize (178, 52)

            textbutton _("↻  RESET"):
                style "godson_name_color_reset"
                action Function(godson_reset_character_name_color, selected_id)
                at ui_button_motion

        if godson_name_color_dropdown:
            frame:
                style "godson_name_color_dropdown"
                xsize 830

                has viewport
                xfill True
                ysize 390
                mousewheel True
                draggable True
                scrollbars "vertical"

                vbox:
                    spacing 8
                    xfill True

                    for character_id, _editor_label in GODSON_NAME_COLOR_CHARACTERS:
                        $ option_label = godson_character_editor_label(character_id)
                        $ option_color = godson_character_name_color(character_id)

                        button:
                            style "godson_name_color_dropdown_item"
                            selected character_id == selected_id
                            action Function(godson_select_name_color_character, character_id)
                            at ui_button_motion

                            has hbox
                            spacing 18
                            yalign 0.5

                            add Solid(option_color):
                                xysize (34, 34)
                                yalign 0.5

                            text option_label:
                                style "godson_name_color_dropdown_text"
                                color option_color
                                yalign 0.5


init -5 screen godson_name_color_picker():
    modal True
    zorder 400

    $ picker_label = godson_character_editor_label(godson_color_picker_character)
    $ picker_preview = godson_color_picker_preview()

    key "game_menu" action Function(godson_cancel_name_color_picker)

    add Solid("#020101D8")

    button:
        xfill True
        yfill True
        background None
        action Function(godson_cancel_name_color_picker)

    frame:
        style "godson_color_picker_frame"
        xalign 0.5
        yalign 0.5

        has vbox
        spacing 30
        xfill True

        hbox:
            xfill True

            vbox:
                spacing 6

                text _("SPEAKER COLOR") style "godson_color_picker_eyebrow"
                text picker_label style "godson_color_picker_title"

            null width 1 xfill True

            textbutton _("CLOSE"):
                style "godson_color_picker_close"
                action Function(godson_cancel_name_color_picker)
                at ui_button_motion

        frame:
            style "godson_color_picker_preview_panel"
            xfill True

            has vbox
            spacing 6
            xalign 0.5

            text picker_label:
                style "godson_color_picker_preview_name"
                color picker_preview
                xalign 0.5

            text _("This is how the speaker's name will appear."):
                style "godson_color_picker_copy"
                xalign 0.5

        vbox:
            spacing 20
            xfill True

            hbox:
                spacing 24
                yalign 0.5

                text _("RED") style "godson_color_channel_label" xsize 190
                bar:
                    style "godson_color_slider_red"
                    value VariableValue("godson_color_picker_red", 255, step=1, action=Function(godson_color_picker_update_from_rgb))
                text "[godson_color_picker_red:03.0f]" style "godson_color_channel_value"

            hbox:
                spacing 24
                yalign 0.5

                text _("GREEN") style "godson_color_channel_label" xsize 190
                bar:
                    style "godson_color_slider_green"
                    value VariableValue("godson_color_picker_green", 255, step=1, action=Function(godson_color_picker_update_from_rgb))
                text "[godson_color_picker_green:03.0f]" style "godson_color_channel_value"

            hbox:
                spacing 24
                yalign 0.5

                text _("BLUE") style "godson_color_channel_label" xsize 190
                bar:
                    style "godson_color_slider_blue"
                    value VariableValue("godson_color_picker_blue", 255, step=1, action=Function(godson_color_picker_update_from_rgb))
                text "[godson_color_picker_blue:03.0f]" style "godson_color_channel_value"

        hbox:
            spacing 22
            xalign 0.5
            yalign 0.5

            text _("HEX") style "godson_color_channel_label" yalign 0.5

            frame:
                style "godson_color_hex_shell"

                input:
                    value VariableInputValue("godson_color_picker_hex", returnable=False)
                    length 7
                    allow "#0123456789abcdefABCDEF"
                    style "godson_color_hex_input"

            textbutton _("LOAD HEX"):
                style "godson_color_picker_action_small"
                action Function(godson_color_picker_set_hex, godson_color_picker_hex)
                at ui_button_motion

        if godson_color_picker_error:
            text godson_color_picker_error:
                style "godson_color_picker_error"
                xalign 0.5

        vbox:
            spacing 12
            xalign 0.5

            text _("QUICK COLORS") style "godson_color_picker_eyebrow" xalign 0.5

            grid 6 2:
                spacing 16

                for preset_color in GODSON_NAME_COLOR_PRESETS:
                    button:
                        style "godson_color_preset"
                        action Function(godson_color_picker_set_hex, preset_color)
                        at ui_button_motion

                        add Solid(preset_color):
                            xalign 0.5
                            yalign 0.5
                            xysize (128, 54)

        hbox:
            spacing 24
            xalign 0.5

            textbutton _("↻  DEFAULT GOLD"):
                style "godson_color_picker_action"
                action Function(godson_color_picker_set_hex, GODSON_DEFAULT_NAME_COLOR)
                at ui_button_motion

            textbutton _("CANCEL"):
                style "godson_color_picker_action"
                action Function(godson_cancel_name_color_picker)
                at ui_button_motion

            textbutton _("APPLY COLOR"):
                style "godson_color_picker_apply"
                action Function(godson_apply_name_color_picker)
                at ui_button_motion


init -5 style godson_name_color_caption is text:
    font "fonts/jenriv-titling-bold.otf"
    size 20
    color "#A99B86"
    kerning 2.0
    outlines [(1, "#080604", 0, 1)]

init -5 style godson_name_color_selector is ui_preferences_button:
    xsize 830
    xminimum 830

init -5 style godson_name_color_selector_text is ui_preferences_button_text:
    xalign 0.0
    color "#F1E2C2"
    hover_color "#FFE497"

init -5 style godson_name_color_preview is frame:
    ysize 106
    padding (24, 13)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)

init -5 style godson_name_color_preview_name is text:
    font gui.name_text_font
    size 40
    outlines [(3, "#000000D0", 0, 2)]

init -5 style godson_name_color_hex_readout is text:
    font "fonts/jenriv-titling-bold.otf"
    size 19
    color "#AFA18A"
    kerning 2.0

init -5 style godson_name_color_swatch_shell is button:
    xsize 224
    ysize 78
    padding (18, 12)
    background Frame("gui/christmas_noir/button_idle.png", 36, 36)
    hover_background Frame("gui/christmas_noir/button_hover.png", 36, 36)

init -5 style godson_name_color_reset is ui_preferences_small_button:
    xminimum 300
    yalign 1.0

init -5 style godson_name_color_dropdown is frame:
    padding (18, 18)
    background Frame("gui/christmas_noir/panel_strong.png", 52, 52)

init -5 style godson_name_color_dropdown_item is button:
    xfill True
    ysize 62
    padding (18, 8)
    background Frame("gui/christmas_noir/button_idle.png", 32, 26)
    hover_background Frame("gui/christmas_noir/button_hover.png", 32, 26)
    selected_background Frame("gui/christmas_noir/button_selected.png", 32, 26)

init -5 style godson_name_color_dropdown_text is text:
    font "fonts/jenriv-titling-bold.otf"
    size 24
    outlines [(2, "#050302", 0, 1)]

init -5 style godson_color_picker_frame is frame:
    xsize 2240
    ysize 1780
    padding (70, 58)
    background Frame("gui/christmas_noir/panel_strong.png", 70, 70)

init -5 style godson_color_picker_eyebrow is text:
    font "fonts/jenriv-titling-bold.otf"
    size 22
    color "#D3AE54"
    kerning 4.0
    outlines [(2, "#080503", 0, 1)]

init -5 style godson_color_picker_title is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 62
    color "#F6EBDD"
    outlines [(3, "#080503", 0, 2)]

init -5 style godson_color_picker_close is ui_preferences_small_button:
    xminimum 250

init -5 style godson_color_picker_preview_panel is frame:
    ysize 220
    padding (35, 28)
    background Frame("gui/christmas_noir/tab_idle.png", 34, 34)

init -5 style godson_color_picker_preview_name is text:
    font gui.name_text_font
    size 72
    outlines [(5, "#000000DD", 0, 3), (2, "#000000", 0, 0)]

init -5 style godson_color_picker_copy is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 27
    color "#BEB19D"

init -5 style godson_color_channel_label is text:
    font "fonts/jenriv-titling-bold.otf"
    size 27
    color "#EFE2C8"
    kerning 2.0
    outlines [(2, "#090603", 0, 1)]

init -5 style godson_color_channel_value is text:
    font "fonts/jenriv-titling-bold.otf"
    size 27
    color "#F4D77B"
    min_width 95
    text_align 1.0
    outlines [(2, "#090603", 0, 1)]

init -5 style godson_color_slider_base is bar:
    xsize 1550
    ysize 62
    right_bar Solid("#170E0FB8")
    thumb "gui/christmas_noir/slider_thumb_idle.png"
    hover_thumb "gui/christmas_noir/slider_thumb_hover.png"
    thumb_offset 31

init -5 style godson_color_slider_red is godson_color_slider_base:
    left_bar Solid("#D74452")

init -5 style godson_color_slider_green is godson_color_slider_base:
    left_bar Solid("#49B976")

init -5 style godson_color_slider_blue is godson_color_slider_base:
    left_bar Solid("#438FD5")

init -5 style godson_color_hex_shell is frame:
    xsize 620
    ysize 80
    padding (24, 10)
    background Frame("gui/christmas_noir/button_idle.png", 36, 36)

init -5 style godson_color_hex_input is input:
    font "fonts/jenriv-titling-bold.otf"
    size 38
    color "#F8E9C7"
    caret Transform(Solid("#F5D36B"), xsize=3)
    xalign 0.5
    yalign 0.5
    text_align 0.5
    outlines [(2, "#080503", 0, 1)]

init -5 style godson_color_picker_error is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 27
    color "#FF6976"
    outlines [(2, "#080503", 0, 1)]

init -5 style godson_color_preset is button:
    xsize 164
    ysize 82
    padding (18, 14)
    background Frame("gui/christmas_noir/button_idle.png", 34, 34)
    hover_background Frame("gui/christmas_noir/button_hover.png", 34, 34)

init -5 style godson_color_picker_action is ui_preferences_button:
    xminimum 480

init -5 style godson_color_picker_action_small is ui_preferences_small_button:
    xminimum 300

init -5 style godson_color_picker_apply is ui_preferences_button:
    xminimum 540
    background Frame("gui/christmas_noir/button_selected.png", 42, 42)
    hover_background Frame("gui/christmas_noir/button_hover.png", 42, 42)

init -5 style godson_color_picker_apply_text is ui_preferences_button_text:
    color "#FFE39A"
    hover_color "#FFFFFF"




init screen godson_name_color_editor():
    $ selected_id = godson_name_color_selected
    $ selected_label = godson_character_editor_label(selected_id)
    $ selected_color = godson_character_name_color(selected_id)

    frame:
        style "ui_preferences_panel"
        xfill True

        has vbox
        spacing 20
        xfill True

        text _("CHARACTER NAME COLORS") style "ui_preferences_label"
        text _("Keep Godson's signature gold, or give individual speakers their own colors. Changes apply to dialogue and History across every save.") style "ui_preferences_description"

        hbox:
            spacing 22
            xfill True
            yalign 0.5

            vbox:
                spacing 9
                xsize 740

                text _("CHARACTER") style "godson_name_color_caption"

                button:
                    style "godson_name_color_selector_clean"
                    action Function(godson_toggle_name_color_dropdown)
                    at ui_button_motion

                    has hbox
                    xfill True
                    yalign 0.5

                    text selected_label:
                        style "godson_name_color_selector_label"
                        yalign 0.5

                    null width 1 xfill True

                    text _("SELECT"):
                        style "godson_name_color_selector_hint"
                        yalign 0.5

            vbox:
                spacing 9
                xsize 700

                text _("PREVIEW") style "godson_name_color_caption" xalign 0.5

                frame:
                    style "godson_name_color_preview_clean"

                    has vbox
                    spacing 2
                    xalign 0.5
                    yalign 0.5

                    text selected_label:
                        style "godson_name_color_preview_name_clean"
                        color selected_color
                        xalign 0.5

                    text selected_color:
                        style "godson_name_color_hex_readout_clean"
                        xalign 0.5

            vbox:
                spacing 9
                xsize 190

                text _("COLOR") style "godson_name_color_caption" xalign 0.5

                button:
                    style "godson_name_color_swatch_shell_clean"
                    action Function(godson_open_name_color_picker, selected_id)
                    at ui_button_motion

                    add Solid(selected_color):
                        xalign 0.5
                        yalign 0.5
                        xysize (142, 44)

            vbox:
                spacing 9
                xsize 230

                text _("ACTION") style "godson_name_color_caption" xalign 0.5

                button:
                    style "godson_name_color_reset_clean"
                    action Function(godson_reset_character_name_color, selected_id)
                    at ui_button_motion

                    text _("RESET"):
                        style "godson_name_color_reset_label"
                        xalign 0.5
                        yalign 0.5

        if godson_name_color_dropdown:
            fixed:
                xysize (790, 392)




                mousearea:
                    xysize (790, 392)
                    hovered SetVariable("godson_name_color_dropdown_hovered", True)
                    unhovered SetVariable("godson_name_color_dropdown_hovered", False)

                frame:
                    style "godson_name_color_dropdown_clean"
                    xsize 790

                    has hbox
                    spacing 14

                    viewport:
                        id "godson_name_color_list_clean"
                        xsize 660
                        ysize 360
                        mousewheel True
                        draggable True

                        has vbox
                        spacing 8
                        xfill True

                        for character_id, _editor_label in GODSON_NAME_COLOR_CHARACTERS:
                            $ option_label = godson_character_editor_label(character_id)
                            $ option_color = godson_character_name_color(character_id)

                            button:
                                style "godson_name_color_dropdown_item_clean"
                                selected character_id == selected_id
                                action Function(godson_select_name_color_character, character_id)
                                at ui_button_motion

                                has hbox
                                spacing 16
                                xfill True
                                yalign 0.5

                                add Solid(option_color):
                                    xysize (30, 30)
                                    yalign 0.5

                                text option_label:
                                    style "godson_name_color_dropdown_text_clean"
                                    color option_color
                                    yalign 0.5

                                null width 1 xfill True

                                if character_id == selected_id:
                                    text _("ACTIVE"):
                                        style "godson_name_color_dropdown_status"
                                        yalign 0.5

                    vbar:
                        value YScrollValue("godson_name_color_list_clean")
                        style "godson_name_color_vscrollbar"
                        yalign 0.5


init screen godson_name_color_picker():
    modal True
    zorder 400

    $ picker_label = godson_character_editor_label(godson_color_picker_character)
    $ picker_preview = godson_color_picker_preview()

    key "game_menu" action Function(godson_cancel_name_color_picker)

    add Solid("#020101D8")

    button:
        xfill True
        yfill True
        background None
        action Function(godson_cancel_name_color_picker)

    frame:
        style "godson_color_picker_frame_clean"
        xalign 0.5
        yalign 0.5

        has vbox
        spacing 22
        xfill True

        hbox:
            xfill True
            yalign 0.5

            vbox:
                spacing 4

                text _("SPEAKER COLOR") style "godson_color_picker_eyebrow"
                text picker_label style "godson_color_picker_title_clean"

            null width 1 xfill True

            button:
                style "godson_color_picker_close_clean"
                action Function(godson_cancel_name_color_picker)
                at ui_button_motion

                text _("CLOSE"):
                    style "godson_color_picker_button_text"
                    xalign 0.5
                    yalign 0.5

        frame:
            style "godson_color_picker_preview_panel_clean"
            xfill True

            has vbox
            spacing 3
            xalign 0.5
            yalign 0.5

            text picker_label:
                style "godson_color_picker_preview_name_clean"
                color picker_preview
                xalign 0.5

            text _("This is how the speaker's name will appear."):
                style "godson_color_picker_copy_clean"
                xalign 0.5

        vbox:
            spacing 12
            xfill True

            hbox:
                spacing 22
                yalign 0.5

                text _("RED") style "godson_color_channel_label_clean" xsize 150
                bar:
                    style "godson_color_slider_red_clean"
                    value VariableValue("godson_color_picker_red", 255, step=1, action=Function(godson_color_picker_update_from_rgb))
                text "[godson_color_picker_red:03.0f]" style "godson_color_channel_value_clean"

            hbox:
                spacing 22
                yalign 0.5

                text _("GREEN") style "godson_color_channel_label_clean" xsize 150
                bar:
                    style "godson_color_slider_green_clean"
                    value VariableValue("godson_color_picker_green", 255, step=1, action=Function(godson_color_picker_update_from_rgb))
                text "[godson_color_picker_green:03.0f]" style "godson_color_channel_value_clean"

            hbox:
                spacing 22
                yalign 0.5

                text _("BLUE") style "godson_color_channel_label_clean" xsize 150
                bar:
                    style "godson_color_slider_blue_clean"
                    value VariableValue("godson_color_picker_blue", 255, step=1, action=Function(godson_color_picker_update_from_rgb))
                text "[godson_color_picker_blue:03.0f]" style "godson_color_channel_value_clean"

        hbox:
            spacing 20
            xalign 0.5
            yalign 0.5

            text _("HEX") style "godson_color_channel_label_clean" yalign 0.5

            frame:
                style "godson_color_hex_shell_clean"

                input:
                    value VariableInputValue("godson_color_picker_hex", returnable=False)
                    length 7
                    allow "#0123456789abcdefABCDEF"
                    style "godson_color_hex_input_clean"

            button:
                style "godson_color_picker_action_small_clean"
                action Function(godson_color_picker_set_hex, godson_color_picker_hex)
                at ui_button_motion

                text _("LOAD HEX"):
                    style "godson_color_picker_button_text"
                    xalign 0.5
                    yalign 0.5

        if godson_color_picker_error:
            text godson_color_picker_error:
                style "godson_color_picker_error"
                xalign 0.5

        vbox:
            spacing 10
            xalign 0.5

            text _("QUICK COLORS") style "godson_color_picker_eyebrow" xalign 0.5

            grid 6 2:
                spacing 14

                for preset_color in GODSON_NAME_COLOR_PRESETS:
                    button:
                        style "godson_color_preset_clean"
                        action Function(godson_color_picker_set_hex, preset_color)
                        at ui_button_motion

                        add Solid(preset_color):
                            xalign 0.5
                            yalign 0.5
                            xysize (122, 42)

        hbox:
            spacing 20
            xalign 0.5

            button:
                style "godson_color_picker_action_clean"
                action Function(godson_color_picker_set_hex, GODSON_DEFAULT_NAME_COLOR)
                at ui_button_motion

                text _("DEFAULT GOLD"):
                    style "godson_color_picker_button_text"
                    xalign 0.5
                    yalign 0.5

            button:
                style "godson_color_picker_action_clean"
                action Function(godson_cancel_name_color_picker)
                at ui_button_motion

                text _("CANCEL"):
                    style "godson_color_picker_button_text"
                    xalign 0.5
                    yalign 0.5

            button:
                style "godson_color_picker_apply_clean"
                action Function(godson_apply_name_color_picker)
                at ui_button_motion

                text _("APPLY COLOR"):
                    style "godson_color_picker_apply_text_clean"
                    xalign 0.5
                    yalign 0.5


style godson_name_color_selector_clean is button:
    xsize 740
    ysize 72
    padding (22, 10)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_name_color_selector_label is text:
    font "fonts/jenriv-titling-bold.otf"
    size 24
    color "#F1E2C2"
    outlines [(2, "#080503", 0, 1)]

style godson_name_color_selector_hint is text:
    font "fonts/jenriv-titling-bold.otf"
    size 16
    color "#D3AE54"
    kerning 2.0
    outlines [(1, "#080503", 0, 1)]

style godson_name_color_preview_clean is frame:
    xfill True
    ysize 72
    padding (22, 6)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)

style godson_name_color_preview_name_clean is text:
    font gui.name_text_font
    size 29
    outlines [(3, "#000000D0", 0, 2)]

style godson_name_color_hex_readout_clean is text:
    font "fonts/jenriv-titling-bold.otf"
    size 15
    color "#AFA18A"
    kerning 2.0

style godson_name_color_swatch_shell_clean is button:
    xsize 190
    ysize 72
    padding (16, 10)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_name_color_reset_clean is button:
    xsize 230
    ysize 72
    padding (18, 10)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_name_color_reset_label is text:
    font "fonts/jenriv-titling-bold.otf"
    size 21
    color "#E7DAC3"
    hover_color "#FFE497"
    kerning 1.0
    outlines [(2, "#080503", 0, 1)]

style godson_name_color_dropdown_clean is frame:
    padding (18, 16)
    background Frame("gui/christmas_noir/panel_strong.png", 52, 52)

style godson_name_color_dropdown_item_clean is button:
    xfill True
    ysize 58
    padding (16, 8)
    background Frame("gui/christmas_noir/tab_idle.png", 26, 26)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 26, 26)
    selected_background Frame("gui/christmas_noir/tab_selected.png", 26, 26)

style godson_name_color_dropdown_text_clean is text:
    font "fonts/jenriv-titling-bold.otf"
    size 20
    outlines [(2, "#050302", 0, 1)]

style godson_name_color_dropdown_status is text:
    font "fonts/jenriv-titling-bold.otf"
    size 13
    color "#FFE497"
    kerning 2.0
    outlines [(1, "#050302", 0, 1)]

style godson_name_color_vscrollbar is vbar:
    xsize 62
    ysize 360
    bar_invert True
    top_bar Frame("gui/christmas_noir/slider_track_fill_vertical.png", 24, 30)
    bottom_bar Frame("gui/christmas_noir/slider_track_empty_vertical.png", 24, 30)
    thumb Transform("gui/christmas_noir/slider_thumb_idle.png", zoom=0.72)
    hover_thumb Transform("gui/christmas_noir/slider_thumb_hover.png", zoom=0.72)
    thumb_offset 30
    unscrollable "hide"

style godson_color_picker_frame_clean is frame:
    xsize 2200
    ysize 1120
    padding (58, 46)
    background Frame("gui/christmas_noir/panel_strong.png", 70, 70)

style godson_color_picker_title_clean is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 52
    color "#F6EBDD"
    outlines [(3, "#080503", 0, 2)]

style godson_color_picker_close_clean is button:
    xsize 250
    ysize 66
    padding (20, 9)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_color_picker_preview_panel_clean is frame:
    ysize 170
    padding (32, 18)
    background Frame("gui/christmas_noir/tab_idle.png", 30, 30)

style godson_color_picker_preview_name_clean is text:
    font gui.name_text_font
    size 56
    outlines [(5, "#000000DD", 0, 3), (2, "#000000", 0, 0)]

style godson_color_picker_copy_clean is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 23
    color "#BEB19D"

style godson_color_channel_label_clean is text:
    font "fonts/jenriv-titling-bold.otf"
    size 24
    color "#EFE2C8"
    kerning 2.0
    outlines [(2, "#090603", 0, 1)]

style godson_color_channel_value_clean is text:
    font "fonts/jenriv-titling-bold.otf"
    size 24
    color "#F4D77B"
    min_width 90
    text_align 1.0
    outlines [(2, "#090603", 0, 1)]

style godson_color_slider_base_clean is bar:
    xsize 1490
    ysize 52
    right_bar Solid("#170E0FB8")
    thumb "gui/christmas_noir/slider_thumb_idle.png"
    hover_thumb "gui/christmas_noir/slider_thumb_hover.png"
    thumb_offset 26

style godson_color_slider_red_clean is godson_color_slider_base_clean:
    left_bar Solid("#D74452")

style godson_color_slider_green_clean is godson_color_slider_base_clean:
    left_bar Solid("#49B976")

style godson_color_slider_blue_clean is godson_color_slider_base_clean:
    left_bar Solid("#438FD5")

style godson_color_hex_shell_clean is frame:
    xsize 560
    ysize 66
    padding (22, 8)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)

style godson_color_hex_input_clean is input:
    font "fonts/jenriv-titling-bold.otf"
    size 29
    color "#F8E9C7"
    caret Transform(Solid("#F5D36B"), xsize=3)
    xalign 0.5
    yalign 0.5
    text_align 0.5
    outlines [(2, "#080503", 0, 1)]

style godson_color_preset_clean is button:
    xsize 156
    ysize 64
    padding (14, 9)
    background Frame("gui/christmas_noir/tab_idle.png", 26, 26)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 26, 26)

style godson_color_picker_action_clean is button:
    xsize 520
    ysize 68
    padding (20, 9)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_color_picker_action_small_clean is button:
    xsize 300
    ysize 66
    padding (18, 9)
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_color_picker_button_text is text:
    font "fonts/jenriv-titling-bold.otf"
    size 21
    color "#E7DAC3"
    hover_color "#FFE497"
    kerning 1.0
    outlines [(2, "#080503", 0, 1)]

style godson_color_picker_apply_clean is button:
    xsize 560
    ysize 68
    padding (20, 9)
    background Frame("gui/christmas_noir/tab_selected.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)

style godson_color_picker_apply_text_clean is text:
    font "fonts/jenriv-titling-bold.otf"
    size 21
    color "#FFE39A"
    hover_color "#FFFFFF"
    kerning 1.0
    outlines [(2, "#080503", 0, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

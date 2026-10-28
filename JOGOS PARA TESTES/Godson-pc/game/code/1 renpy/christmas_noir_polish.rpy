init offset = 160



transform -160 godson_noir_confirm_arrive:
    alpha 0.0
    zoom 0.975
    easeout 0.22 alpha 1.0 zoom 1.0



init screen say(who, what):
    style_prefix "say"
    $ ui_dialogue_ypos = 1852 if who is not None else 1810
    $ ui_has_dialogue = bool(what and str(what).strip())

    if persistent.narrator_autoplay and _narrator_autoplay_active:
        timer 0.05 repeat True action NarratorVoiceAutoAdvance(
            _narrator_autoplay_generation
        )

    fixed:
        id "window"
        xpos 0
        ypos 0
        xanchor 0.0
        yanchor 0.0
        xsize config.screen_width
        ysize config.screen_height
        at ui_dialogue_arrive

        if who is not None and ui_has_dialogue:
            text who id "who":
                xalign 0.5
                ypos 1782
                xsize 2800
                font gui.name_text_font
                size gui.name_text_size
                color godson_name_color_for(who)
                text_align 0.5
                outlines [(absolute(3), "#000000D0", 0, absolute(2))]

        if ui_has_dialogue:
            text what id "what":
                xalign 0.5
                ypos ui_dialogue_ypos
                xsize 2800
                font gui.text_font
                size gui.text_size
                color "#FFFFFF"
                text_align 0.5
                line_spacing 6
                outlines [(absolute(5), "#000000E6", absolute(1), absolute(2)), (absolute(2), "#000000", 0, 0)]

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init screen gallery_card(entry):
    $ is_unlocked = gallery_scene_unlocked(entry["id"], entry["legacy_flag"])
    $ replay_label = entry.get("replay_label", None)
    $ replay_action = [PauseAudio("music", True), Function(renpy.call_in_new_context, replay_label), PauseAudio("music", False)] if replay_label else Show("gallery_player", entry=entry)

    button:
        style "ui_gallery_card"
        sensitive is_unlocked
        action replay_action
        at ui_button_motion

        has fixed
        xfill True
        yfill True

        add entry["thumbnail"]:
            xpos 22
            ypos 22
            xysize (740, 340)
            fit "cover"

        if not is_unlocked:
            add Solid("#090506E8"):
                xpos 22
                ypos 22
                xysize (740, 340)

            add "gui/christmas_noir/gallery_lock_gold.png":
                xalign 0.5
                ypos 102
                xysize (150, 150)

            text _("LOCKED"):
                style "ui_gallery_locked_text"
                xalign 0.5
                ypos 270

        else:
            add "gui/christmas_noir/gallery_play_gold.png":
                xalign 0.5
                ypos 104
                xysize (146, 146)

        text entry["title"]:
            style "ui_gallery_title"
            xpos 28
            ypos 384

        text entry["subtitle"]:
            style "ui_gallery_subtitle"
            xpos 28
            ypos 445

        if is_unlocked:
            text _("REPLAY"):
                style "ui_gallery_replay_text"
                xalign 1.0
                xpos 750
                ypos 398



init screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add Solid("#020101E8")

    add "gui/christmas_noir/snowflake_gold.png":
        xpos 510
        ypos 360
        xysize (130, 130)
        alpha 0.34
        at godson_noir_ornament_turn

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 3200
        ypos 1580
        xysize (105, 105)
        alpha 0.22
        at godson_noir_ornament_turn

    frame:
        style "godson_noir_confirm_frame"
        at godson_noir_confirm_arrive

        has vbox
        xalign 0.5
        yalign 0.5
        spacing 44

        text _("CONFIRMATION"):
            style "godson_noir_confirm_kicker"
            xalign 0.5

        add Solid("#B99248"):
            xalign 0.5
            xsize 420
            ysize 3

        text _(message):
            style "godson_noir_confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 54

            textbutton _("YES"):
                style "godson_noir_confirm_button"
                action yes_action

            textbutton _("NO"):
                style "godson_noir_confirm_button"
                action no_action

    key "game_menu" action no_action


style ui_section_eyebrow:
    color "#D6AE5D"





style about_label_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 66
    color "#FFD85A"
    outlines [(3, "#000000D0", 0, 2)]


style about_text:
    font gui.interface_text_font2
    size 46
    color "#D8CCBA"


style hyperlink_text:
    color "#FFD85A"
    hover_color "#FFF0A6"
    selected_color "#FFF0A6"
    hover_underline True


style page_label_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    color "#FFD85A"
    hover_color "#FFF0A6"
    selected_color "#FFF0A6"
    outlines [(3, "#000000D0", 0, 2)]





init 10 style ui_choice_player_name:
    color "#718A96"
    outlines [(3, "#000000D0", 0, 2)]


init 10 style ui_choice_player_name_neutral is ui_choice_player_name:
    color "#718A96"


init 10 style ui_choice_player_name_good is ui_choice_player_name:
    color "#479EF5"


init 10 style ui_choice_player_name_supergood is ui_choice_player_name:
    color "#E6EDF3"


init 10 style ui_choice_player_name_evil is ui_choice_player_name:
    color "#C94B58"


init 10 style ui_choice_player_name_sexaddict is ui_choice_player_name:
    color "#7D429F"


init 10 style ui_choice_player_name_superevil is ui_choice_player_name:
    color "#2EDFE4"





init 10 style ui_quick_button is button:
    xsize 190
    ysize 58
    background Frame("gui/christmas_noir/nav_idle.png", 42, 24)
    hover_background Frame("gui/christmas_noir/nav_hover.png", 42, 24)
    selected_background Frame("gui/christmas_noir/nav_hover.png", 42, 24)
    selected_hover_background Frame("gui/christmas_noir/nav_hover.png", 42, 24)
    insensitive_background Frame("gui/christmas_noir/nav_idle.png", 42, 24)
    padding (14, 7)


init 10 style ui_quick_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 24
    color "#CBBEAA"
    hover_color "#FFF0A6"
    selected_color "#FFD85A"
    selected_hover_color "#FFF0A6"
    insensitive_color "#756A5D"
    outlines [(2, "#000000D0", 0, 1)]
    xalign 0.5
    yalign 0.5


style slot_time_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 34
    color "#F4E9D7"
    hover_color "#FFDF7A"
    selected_color "#FFDF7A"
    insensitive_color "#6E665C"
    outlines [(4, "#000000E8", 0, 2), (2, "#000000", 0, 0)]
    text_align 0.5


style slot_name_text:
    font "fonts/Louis George Cafe Bold.ttf"
    size 20
    color "#9A8E7D"
    hover_color "#FFEC7A"
    selected_color "#FFEC7A"
    outlines [(3, "#000000E0", 0, 1), (1, "#000000", 0, 0)]
    text_align 0.5


style ui_gallery_intro:
    font gui.interface_text_font2
    size 46
    color "#D7CCBD"


style ui_gallery_count_frame:
    background Frame("gui/christmas_noir/tab_selected.png", 28, 28)
    padding (34, 18)
    yalign 0.5


style ui_gallery_count_text:
    font gui.interface_text_font
    size 38
    color "#FFE9B0"


style ui_gallery_card is button:
    xsize 784
    ysize 505
    background Frame("gui/christmas_noir/gallery_idle_noir.png", 38, 38)
    hover_background Frame("gui/christmas_noir/gallery_hover_noir.png", 38, 38)
    insensitive_background Frame("gui/christmas_noir/gallery_locked_noir.png", 38, 38)
    padding (0, 0)


style ui_gallery_title:
    font gui.interface_text_font
    size 48
    color "#FFF3D2"
    outlines [(2, "#00000099", 0, 2)]


style ui_gallery_subtitle:
    font gui.interface_text_font2
    size 34
    color "#B7A995"


style ui_gallery_locked_text:
    font gui.interface_text_font
    size 38
    color "#D7B86D"
    outlines [(3, "#000000CC", 0, 2)]


style ui_gallery_replay_text:
    font gui.interface_text_font
    size 31
    color "#E9C56F"


style ui_gallery_close_button is button:
    xsize 220
    ysize 70
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)
    padding (18, 8)


style ui_gallery_close_button_text is button_text:
    font gui.interface_text_font
    size 27
    color "#E8DAC0"
    hover_color "#FFE9B0"
    xalign 0.5
    yalign 0.5


style godson_noir_confirm_frame is frame:
    xsize 1660
    ysize 770
    xalign 0.5
    yalign 0.5
    background Frame("gui/christmas_noir/panel_strong.png", 58, 58)
    padding (120, 92)


style godson_noir_confirm_kicker is text:
    font "fonts/jenriv-titling-bold.otf"
    size 30
    color "#D8B768"
    kerning 4.0
    outlines [(2, "#000000C8", 0, 1)]


style godson_noir_confirm_prompt is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 60
    color "#F4EBDD"
    xsize 1360
    text_align 0.5
    layout "subtitle"
    outlines [(3, "#000000D0", 0, 2)]


style godson_noir_confirm_button is button:
    xsize 420
    ysize 94
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)


style godson_noir_confirm_button_text is button_text:
    font "fonts/jenriv-titling-bold.otf"
    size 31
    color "#D8CDBD"
    hover_color "#FFE7A4"
    selected_color "#FFE7A4"
    xalign 0.5
    yalign 0.5
    text_align 0.5
    kerning 2.0
    outlines [(2, "#000000C8", 0, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init offset = 90





transform -90 ui_button_motion:
    on idle:
        linear 0.12 zoom 1.0
    on hover:
        linear 0.12 zoom 1.018

transform -90 ui_panel_arrive:
    alpha 0.0
    yoffset 30
    easeout 0.28 alpha 1.0 yoffset 0


transform -90 ui_route_hover_good:
    subpixel True
    alpha 0.0
    zoom 0.68
    yoffset 10
    easeout 0.18 alpha 1.0 zoom 1.0 yoffset 0
    parallel:
        ease 0.85 yoffset -6
        ease 0.85 yoffset 4
        repeat
    parallel:
        ease 0.90 alpha 0.82
        ease 0.90 alpha 1.0
        repeat


transform -90 ui_route_hover_supergood:
    subpixel True
    alpha 0.0
    zoom 0.66
    yoffset 12
    easeout 0.22 alpha 1.0 zoom 1.0 yoffset 0
    parallel:
        ease 1.05 yoffset -7
        ease 1.05 yoffset 4
        repeat
    parallel:
        ease 0.75 alpha 0.82
        ease 0.75 alpha 1.0
        repeat


transform -90 ui_route_hover_evil:
    subpixel True
    alpha 0.0
    zoom 0.68
    yoffset 10
    easeout 0.18 alpha 1.0 zoom 1.0 yoffset 0
    parallel:
        ease 0.18 xoffset -3
        ease 0.18 xoffset 3
        ease 0.18 xoffset 0
        pause 0.42
        repeat
    parallel:
        ease 0.42 zoom 1.055
        ease 0.42 zoom 1.0
        repeat


transform -90 ui_route_hover_sexaddict:
    subpixel True
    alpha 0.0
    zoom 0.68
    yoffset 10
    easeout 0.18 alpha 1.0 zoom 1.0 yoffset 0
    easeout 0.12 zoom 1.08
    easein 0.12 zoom 1.0
    pause 0.08
    easeout 0.10 zoom 1.05
    easein 0.16 zoom 1.0
    pause 0.62
    repeat


transform -90 ui_route_hover_superevil:
    subpixel True
    alpha 0.0
    zoom 0.68
    yoffset 10
    easeout 0.18 alpha 1.0 zoom 1.0 yoffset 0
    parallel:
        linear 0.08 alpha 0.72
        linear 0.08 alpha 1.0
        pause 0.34
        linear 0.05 alpha 0.82
        linear 0.05 alpha 1.0
        pause 0.48
        repeat
    parallel:
        ease 0.30 yoffset -5
        ease 0.30 yoffset 3
        repeat


transform -90 ui_route_hover_neutral:
    subpixel True
    alpha 0.0
    zoom 0.68
    yoffset 10
    easeout 0.18 alpha 0.92 zoom 1.0 yoffset 0
    ease 0.80 yoffset -4 alpha 0.72
    ease 0.80 yoffset 3 alpha 0.92
    repeat


transform -90 ui_dialogue_arrive:
    alpha 0.0
    yoffset 14
    easeout 0.18 alpha 1.0 yoffset 0


transform -90 ui_memory_arrive:
    alpha 0.0
    xoffset -1250
    on show:
        parallel:
            easeout 0.42 xoffset 20
            easeout 0.12 xoffset 0
        parallel:
            linear 0.16 alpha 1.0
    on hide:
        easein 0.30 xoffset -1250 alpha 0.0


transform -90 ui_memory_icon_arrive:
    alpha 0.0
    zoom 0.55
    pause 0.18
    easeout 0.24 alpha 1.0 zoom 1.12
    easein 0.12 zoom 1.0


transform -90 ui_memory_signal:
    alpha 0.42
    linear 0.18 alpha 1.0
    linear 0.22 alpha 0.58
    linear 0.18 alpha 1.0


transform -90 ui_memory_progress(duration=7.0):
    xanchor 0.0
    xzoom 1.0
    linear duration xzoom 0.0


transform -90 ui_memory_sweep:
    alpha 0.0
    xoffset -130
    pause 0.22
    linear 0.12 alpha 0.10
    linear 0.55 xoffset 1020
    linear 0.12 alpha 0.0


init 10 screen say(who, what):
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
                color gui.accent_color
                text_align 0.5
                outlines [(absolute(5), "#000000D9", absolute(1), absolute(2)), (absolute(2), "#000000", 0, 0)]

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


init 10 screen input(prompt):
    style_prefix "input"



    fixed:
        xpos 0
        ypos 0
        xanchor 0.0
        yanchor 0.0
        xsize config.screen_width
        ysize config.screen_height
        at ui_dialogue_arrive

        text prompt:
            xalign 0.5
            ypos 1782
            xsize 2800
            font gui.text_font
            size gui.name_text_size
            color "#FFD85A"
            text_align 0.5
            outlines [(absolute(3), "#000000D0", 0, absolute(2))]

        input id "input":
            xalign 0.5
            ypos 1852
            xsize 2800
            font gui.text_font
            size gui.text_size
            color "#FFFFFF"
            text_align 0.5
            outlines [(absolute(5), "#000000E6", absolute(1), absolute(2)), (absolute(2), "#000000", 0, 0)]


init 10 screen tooltip(n=1, time=7.0):
    zorder 250

    $ ui_memory_text = {
        1: "A kinder path has opened before you. GOOD!",
        2: "Something darker has taken root within you. EVIL!",
        3: "Desire now guides your path. SEX ADDICT!",
        4: "Marnie has been added to your contacts.",
        5: "Marnie noticed the way you looked at her.",
        6: "Marnie will remember your compassion.",
        7: "Marnie will remember your cruelty.",
        8: "Marnie will remember that you backed away.",
        9: "Marnie will remember your kiss.",
        10: "Jennifer noticed that you followed her.",
        11: "Jennifer will remember that you resisted her.",
        12: "Jennifer will remember what you chose to call her.",
        13: "Lorraine will remember your respectful approach.",
        14: "Lorraine will remember that you intruded.",
        15: "Lorraine will remember your praise.",
        16: "You uncovered part of Lorraine's secret.",
        17: "Lorraine will remember what happened between you.",
        18: "Yuni will remember your first impression.",
        19: "Yuni will remember that you resisted her.",
        20: "Yuni will remember that you accepted her title.",
        21: "Yuni will remember that you helped with her video.",
        22: "Yuni will remember that you refused to help.",
        23: "Yuni will remember your failed music choice.",
        24: "Martha will remember how you treated her.",
        25: "Henry will remember that you agreed to help.",
        26: "Henry will remember that you stood by and watched.",
        27: "Marnie will remember that you intervened.",
        28: "Henry will remember that you attacked his boss.",
        29: "Marnie will remember your explanation.",
        30: "Marnie will remember what happened afterward.",
        31: "Nina will remember your patience.",
        32: "Nina will remember how you pressured her.",
        33: "Nina will remember that you crossed the line.",
        34: "Henry will remember your help.",
        35: "Lorraine will remember your honesty.",
        36: "Nina has been added to your contacts.",
        37: "Nina is now your girlfriend.",
        38: "Nina now hates you.",
        39: "Gianna will remember that you paid her.",
        40: "Gianna will remember your indecent proposition.",
        41: "Gianna will remember that you demanded a preview.",
        42: "Myles and Gianna learned what you truly are.",
        43: "Myles will remember that you claimed Martha.",
        44: "Myles will remember that.",
        45: "Martha will remember your invitation to dance.",
        46: "Mommy will remember that you love to make out.",
        47: "Mommy thinks you love her."
    }.get(n, "")

    $ ui_memory_title = "CONSEQUENCE RECORDED"
    if n in (1, 2, 3):
        $ ui_memory_title = "PATH UPDATED"
    elif n in (4, 36):
        $ ui_memory_title = "CONTACT ADDED"
    elif n == 16:
        $ ui_memory_title = "SECRET UNCOVERED"
    elif n in (37, 38):
        $ ui_memory_title = "RELATIONSHIP CHANGED"

    $ ui_memory_icon = "gui/neturalicon.png"
    if n == 1:
        $ ui_memory_icon = "gui/goodicon.png"
    elif n == 2:
        $ ui_memory_icon = "gui/evilicon.png"
    elif n == 3:
        $ ui_memory_icon = "gui/sexaddicticon.png"
    elif supergood:
        $ ui_memory_icon = "gui/supergoodicon.png"
    elif superevil:
        $ ui_memory_icon = "gui/superevilicon.png"
    elif good:
        $ ui_memory_icon = "gui/goodicon.png"
    elif evil:
        $ ui_memory_icon = "gui/evilicon.png"
    elif sexaddict:
        $ ui_memory_icon = "gui/sexaddicticon.png"

    fixed:
        xpos 60
        ypos 86
        xsize 1000
        ysize 158
        at ui_memory_arrive



        add Frame("gui/christmas_noir/panel_strong.png", 58, 58):
            xysize (1000, 158)


        fixed:
            xsize 1000
            ysize 158
            clipping True

            add Solid("#FFE6A8"):
                xpos 0
                ypos 0
                xsize 82
                ysize 158
                at ui_memory_sweep

        hbox:
            xpos 30
            ypos 35
            spacing 22

            frame:
                style "ui_memory_icon_frame"
                at ui_memory_icon_arrive

                add ui_memory_icon:
                    xalign 0.5
                    yalign 0.5
                    xysize (58, 58)
                    fit "contain"

            vbox:
                yalign 0.5
                spacing 8

                text ui_memory_title:
                    style "ui_memory_header"

                text ui_memory_text:
                    style "ui_memory_body"
                    xmaximum 830

        add Solid("#651522"):
            xpos 18
            ypos 149
            xsize 964
            ysize 3

        add Solid("#FFD85A"):
            xpos 18
            ypos 149
            xsize 964
            ysize 3
            at ui_memory_progress(time)

    timer time action Hide("tooltip")


init screen choice(items):
    style_prefix "choice"
    default hovered_choice = -1

    $ route_icon = "gui/neturalicon.png"

    if supergood:
        $ route_icon = "gui/supergoodicon.png"
    elif superevil:
        $ route_icon = "gui/superevilicon.png"
    elif evil:
        $ route_icon = "gui/evilicon.png"
    elif sexaddict:
        $ route_icon = "gui/sexaddicticon.png"
    elif good:
        $ route_icon = "gui/goodicon.png"

    hbox:
        style "ui_choice_cluster"
        at ui_panel_arrive

        if supergood:
            text "[playerName]" style "ui_choice_player_name_supergood" yalign 0.5
        elif superevil:
            text "[playerName]" style "ui_choice_player_name_superevil" yalign 0.5
        elif evil:
            text "[playerName]" style "ui_choice_player_name_evil" yalign 0.5
        elif sexaddict:
            text "[playerName]" style "ui_choice_player_name_sexaddict" yalign 0.5
        elif good:
            text "[playerName]" style "ui_choice_player_name_good" yalign 0.5
        else:
            text "[playerName]" style "ui_choice_player_name_neutral" yalign 0.5

        vbox:
            style "ui_choice_list"

            for choice_index, item in enumerate(items):
                $ choice_enabled = (item.action is not None) and item.action.get_sensitive()

                fixed:
                    xsize 1845
                    fit_first "height"

                    hbox:
                        spacing 22
                        xalign 0.5

                        if not choice_enabled:
                            frame:
                                style "ui_route_badge_disabled"
                                add route_icon:
                                    xalign 0.5
                                    yalign 0.5
                                    xysize (64, 64)
                                    fit "contain"
                                    alpha 0.28
                                    matrixcolor SaturationMatrix(0.0)
                            textbutton item.caption:
                                style "ui_choice_button_disabled"
                                action item.action
                                sensitive False
                        elif supergood:
                            frame:
                                style "ui_route_badge_supergood"
                                add route_icon xalign 0.5 yalign 0.5 xysize (64, 64) fit "contain"
                            textbutton item.caption:
                                style "ui_choice_button_supergood"
                                action item.action
                                hovered SetScreenVariable("hovered_choice", choice_index)
                                unhovered SetScreenVariable("hovered_choice", -1)
                                at ui_button_motion
                        elif superevil:
                            frame:
                                style "ui_route_badge_superevil"
                                add route_icon xalign 0.5 yalign 0.5 xysize (64, 64) fit "contain"
                            textbutton item.caption:
                                style "ui_choice_button_superevil"
                                action item.action
                                hovered SetScreenVariable("hovered_choice", choice_index)
                                unhovered SetScreenVariable("hovered_choice", -1)
                                at ui_button_motion
                        elif evil:
                            frame:
                                style "ui_route_badge_evil"
                                add route_icon xalign 0.5 yalign 0.5 xysize (64, 64) fit "contain"
                            textbutton item.caption:
                                style "ui_choice_button_evil"
                                action item.action
                                hovered SetScreenVariable("hovered_choice", choice_index)
                                unhovered SetScreenVariable("hovered_choice", -1)
                                at ui_button_motion
                        elif sexaddict:
                            frame:
                                style "ui_route_badge_sexaddict"
                                add route_icon xalign 0.5 yalign 0.5 xysize (64, 64) fit "contain"
                            textbutton item.caption:
                                style "ui_choice_button_sexaddict"
                                action item.action
                                hovered SetScreenVariable("hovered_choice", choice_index)
                                unhovered SetScreenVariable("hovered_choice", -1)
                                at ui_button_motion
                        elif good:
                            frame:
                                style "ui_route_badge_good"
                                add route_icon xalign 0.5 yalign 0.5 xysize (64, 64) fit "contain"
                            textbutton item.caption:
                                style "ui_choice_button_good"
                                action item.action
                                hovered SetScreenVariable("hovered_choice", choice_index)
                                unhovered SetScreenVariable("hovered_choice", -1)
                                at ui_button_motion
                        else:
                            frame:
                                style "ui_route_badge_neutral"
                                add route_icon xalign 0.5 yalign 0.5 xysize (64, 64) fit "contain"
                            textbutton item.caption:
                                style "ui_choice_button_neutral"
                                action item.action
                                hovered SetScreenVariable("hovered_choice", choice_index)
                                unhovered SetScreenVariable("hovered_choice", -1)
                                at ui_button_motion

                    if choice_enabled and hovered_choice == choice_index:
                        if supergood:
                            add "gui/ui_refresh/route_hover_supergood.png":
                                xpos 1715
                                yalign 0.5
                                xysize (116, 116)
                                fit "contain"
                                at ui_route_hover_supergood
                        elif superevil:
                            add "gui/ui_refresh/route_hover_superevil.png":
                                xpos 1715
                                yalign 0.5
                                xysize (116, 116)
                                fit "contain"
                                at ui_route_hover_superevil
                        elif evil:
                            add "gui/ui_refresh/route_hover_evil.png":
                                xpos 1715
                                yalign 0.5
                                xysize (116, 116)
                                fit "contain"
                                at ui_route_hover_evil
                        elif sexaddict:
                            add "gui/ui_refresh/route_hover_sexaddict.png":
                                xpos 1715
                                yalign 0.5
                                xysize (116, 116)
                                fit "contain"
                                at ui_route_hover_sexaddict
                        elif good:
                            add "gui/ui_refresh/route_hover_good.png":
                                xpos 1715
                                yalign 0.5
                                xysize (116, 116)
                                fit "contain"
                                at ui_route_hover_good
                        else:
                            add route_icon:
                                xpos 1730
                                yalign 0.5
                                xysize (76, 76)
                                fit "contain"
                                at ui_route_hover_neutral


init screen quick_menu():
    zorder 100

    if quick_menu:
        vbox:
            style "ui_quick_rail"

            textbutton _("AUTO") action Preference("auto-forward", "toggle") style "ui_quick_button" at ui_button_motion
            textbutton _("BACK") action Rollback() style "ui_quick_button" at ui_button_motion
            textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True) style "ui_quick_button" at ui_button_motion
            textbutton _("Q.SAVE") action QuickSave() style "ui_quick_button" at ui_button_motion
            textbutton _("Q.LOAD") action QuickLoad() style "ui_quick_button" at ui_button_motion
            textbutton _("CONFIG") action ShowMenu("preferences") style "ui_quick_button" at ui_button_motion


init screen navigation():
    vbox:
        style "ui_navigation_list"

        text _("GODSON") style "ui_navigation_brand"
        text _("SYSTEM MENU") style "ui_navigation_kicker"

        null height 45

        if main_menu:
            textbutton _("NEW GAME") action Start() style "ui_navigation_button" at ui_button_motion
        else:
            textbutton _("HISTORY") action ShowMenu("history") style "ui_navigation_button" at ui_button_motion
            textbutton _("SAVE") action ShowMenu("save") style "ui_navigation_button" at ui_button_motion

        textbutton _("LOAD") action ShowMenu("load") style "ui_navigation_button" at ui_button_motion
        textbutton _("GALLERY") action ShowMenu("gallery") style "ui_navigation_button" at ui_button_motion
        textbutton _("OPTIONS") action ShowMenu("preferences") style "ui_navigation_button" at ui_button_motion

        if _in_replay:
            textbutton _("END REPLAY") action EndReplay(confirm=True) style "ui_navigation_button" at ui_button_motion
        elif not main_menu:
            textbutton _("MAIN MENU") action MainMenu() style "ui_navigation_button" at ui_button_motion

        textbutton _("ABOUT") action ShowMenu("about") style "ui_navigation_button" at ui_button_motion

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("HELP") action ShowMenu("help") style "ui_navigation_button" at ui_button_motion

        if renpy.variant("pc"):
            textbutton _("QUIT") action Quit(confirm=not main_menu) style "ui_navigation_button" at ui_button_motion

        null height 25

        textbutton _("RETURN"):
            style "ui_return_button"
            action Return()
            at ui_button_motion


init screen main_menu():
    tag menu

    if day_mode:
        add gui.main_menu_background
    else:
        add gui.main_menu_background2

    add Solid("#03070A42")

    if show_buttons:
        frame:
            style "ui_main_dock"
            at ui_panel_arrive

            has vbox
            spacing 28
            xfill True

            hbox:
                spacing 24
                xalign 0.5

                textbutton _("NEW GAME") action Start() style "ui_main_primary_button" at ui_button_motion
                textbutton _("LOAD") action ShowMenu("load") style "ui_main_primary_button" at ui_button_motion
                textbutton _("GALLERY") action ShowMenu("gallery") style "ui_main_primary_button" at ui_button_motion
                textbutton _("OPTIONS") action ShowMenu("preferences") style "ui_main_primary_button" at ui_button_motion
                textbutton _("QUIT") action Quit(confirm=False) style "ui_main_primary_button" at ui_button_motion

            hbox:
                spacing 18
                xalign 0.5

                textbutton _("ABOUT") action ShowMenu("about") style "ui_main_secondary_button" at ui_button_motion
                textbutton _("HELP") action ShowMenu("help") style "ui_main_secondary_button" at ui_button_motion
                textbutton _("PATREON") action OpenURL("https://patreon.com/cheesecake3d") style "ui_main_secondary_button" at ui_button_motion
                textbutton _("DISCORD") action OpenURL("https://discord.gg/cheesecake") style "ui_main_secondary_button" at ui_button_motion

    text _("GODSON  //  BUILD [config.version]"):
        style "ui_main_version"
        xpos 120
        ypos 2070
        yanchor 1.0


init screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background

    add Solid("#05090DEB")

    frame:
        style "ui_game_menu_shell"
        at ui_panel_arrive

        has hbox
        spacing 0
        xfill True
        yfill True

        frame:
            style "ui_game_menu_sidebar"

            use navigation

        frame:
            style "ui_game_menu_content"

            has vbox
            spacing 28
            xfill True
            yfill True

            hbox:
                xfill True
                ysize 120

                vbox:
                    spacing 0

                    text _("MENU") style "ui_section_eyebrow"
                    label title style "ui_game_menu_title"

                null

                text _("ESC  /  RIGHT CLICK TO RETURN") style "ui_game_menu_hint" yalign 0.5

            add Solid("#3CDFFF"):
                xsize 160
                ysize 5

            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    has vbox
                    spacing 20
                    transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    transclude

            else:
                transclude

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action Return()





init -1 python:
    def godson_apply_renderer(renderer):
        _preferences.renderer = renderer
        renpy.save_persistent()
        renpy.restart_interaction()

    def godson_renderer_label():
        return {
        "auto": _("AUTOMATIC"),
        "gl2": _("GL2"),
        "angle2": _("ANGLE2"),
    }.get(_preferences.renderer, str(_preferences.renderer).upper())


init screen preferences():
    tag menu

    default ui_preferences_tab = "visuals"

    use game_menu(_("OPTIONS"), scroll="viewport"):
        vbox:
            spacing 34
            xfill True

            hbox:
                spacing 18

                textbutton _("GRAPHICS"):
                    style "ui_preferences_tab"
                    selected ui_preferences_tab == "visuals"
                    action SetScreenVariable("ui_preferences_tab", "visuals")
                    at ui_button_motion

                textbutton _("TEXT & AUTO"):
                    style "ui_preferences_tab"
                    selected ui_preferences_tab == "text"
                    action SetScreenVariable("ui_preferences_tab", "text")
                    at ui_button_motion

                textbutton _("AUDIO"):
                    style "ui_preferences_tab"
                    selected ui_preferences_tab == "audio"
                    action SetScreenVariable("ui_preferences_tab", "audio")
                    at ui_button_motion

            if ui_preferences_tab == "visuals":
                vbox:
                    spacing 24
                    xfill True

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 20

                        text _("DISPLAY MODE") style "ui_preferences_label"
                        text _("Choose how Godson uses your screen.") style "ui_preferences_description"

                        hbox:
                            spacing 18

                            textbutton _("WINDOWED"):
                                style "ui_preferences_button"
                                action Preference("display", "window")
                                at ui_button_motion

                            textbutton _("FULLSCREEN"):
                                style "ui_preferences_button"
                                action Preference("display", "fullscreen")
                                at ui_button_motion

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 20

                        text _("FRAME SKIPPING") style "ui_preferences_label"
                        text _("Reduce tearing or favour smoother playback on your system.") style "ui_preferences_description"

                        hbox:
                            spacing 18

                            textbutton _("ON"):
                                style "ui_preferences_small_button"
                                action Preference("gl tearing", False)
                                at ui_button_motion

                            textbutton _("OFF"):
                                style "ui_preferences_small_button"
                                action Preference("gl tearing", True)
                                at ui_button_motion

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 20

                        text _("POWER SAVE MODE") style "ui_preferences_label"
                        text _("Balance power use and animation performance.") style "ui_preferences_description"

                        hbox:
                            spacing 18

                            textbutton _("ON"):
                                style "ui_preferences_small_button"
                                action Preference("gl powersave", True)
                                at ui_button_motion

                            textbutton _("OFF"):
                                style "ui_preferences_small_button"
                                action Preference("gl powersave", False)
                                at ui_button_motion

                            textbutton _("AUTO"):
                                style "ui_preferences_small_button"
                                action Preference("gl powersave", "auto")
                                at ui_button_motion

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 20

                        text _("GRAPHICS RENDERER") style "ui_preferences_label"
                        text _("If you experience flickering, screen tearing, black screens, or visual corruption, use a different renderer. It fixes it.") style "ui_preferences_description"

                        $ current_renderer = godson_renderer_label()
                        text _("CURRENT: [current_renderer]"):
                            style "ui_preferences_description"
                            color "#D6AE5D"

                        hbox:
                            spacing 18

                            textbutton _("AUTOMATIC"):
                                style "ui_preferences_button"
                                selected _preferences.renderer == "auto"
                                action Confirm(_("Apply the Automatic renderer? Godson must be restarted before this change takes effect."), Function(godson_apply_renderer, "auto"))
                                at ui_button_motion

                            textbutton _("FORCE GL2"):
                                style "ui_preferences_button"
                                selected _preferences.renderer == "gl2"
                                action Confirm(_("Force the GL2 renderer? Godson must be restarted before this change takes effect."), Function(godson_apply_renderer, "gl2"))
                                at ui_button_motion

                            if renpy.windows:
                                textbutton _("FORCE ANGLE2"):
                                    style "ui_preferences_button"
                                    selected _preferences.renderer == "angle2"
                                    action Confirm(_("Force the ANGLE2 renderer? Godson must be restarted before this change takes effect."), Function(godson_apply_renderer, "angle2"))
                                    at ui_button_motion

            elif ui_preferences_tab == "text":
                vbox:
                    spacing 24
                    xfill True

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 20

                        text _("ROLLBACK SIDE") style "ui_preferences_label"
                        text _("Choose which screen edge triggers rollback.") style "ui_preferences_description"

                        hbox:
                            spacing 18

                            textbutton _("DISABLED"):
                                style "ui_preferences_button"
                                action Preference("rollback side", "disable")
                                at ui_button_motion

                            textbutton _("LEFT"):
                                style "ui_preferences_small_button"
                                action Preference("rollback side", "left")
                                at ui_button_motion

                            textbutton _("RIGHT"):
                                style "ui_preferences_small_button"
                                action Preference("rollback side", "right")
                                at ui_button_motion

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 20

                        text _("SKIP & AUTO") style "ui_preferences_label"
                        text _("Fine-tune what Skip passes and how Auto follows voiced dialogue.") style "ui_preferences_description"

                        hbox:
                            spacing 18

                            textbutton _("UNSEEN TEXT"):
                                style "ui_preferences_button"
                                action Preference("skip", "toggle")
                                at ui_button_motion

                            textbutton _("AFTER CHOICES"):
                                style "ui_preferences_button"
                                action Preference("after choices", "toggle")
                                at ui_button_motion

                            textbutton _("TRANSITIONS"):
                                style "ui_preferences_button"
                                action InvertSelected(Preference("transitions", "toggle"))
                                at ui_button_motion

                            textbutton _("WAIT FOR VOICE"):
                                style "ui_preferences_button"
                                action Preference("wait for voice", "toggle")
                                at ui_button_motion

                    frame:
                        style "ui_preferences_panel"

                        has vbox
                        spacing 24

                        text _("TEXT SPEED") style "ui_preferences_label"
                        bar:
                            style "ui_preferences_bar"
                            value Preference("text speed")

                        text _("AUTO-FORWARD TIME") style "ui_preferences_label"
                        bar:
                            style "ui_preferences_bar"
                            value Preference("auto-forward time")

                    use godson_name_color_editor

            else:
                vbox:
                    spacing 20
                    xfill True

                    if config.has_music:
                        frame:
                            style "ui_preferences_panel"

                            has hbox
                            spacing 28
                            yalign 0.5

                            vbox:
                                xsize 620
                                spacing 8

                                text _("MUSIC") style "ui_preferences_label"
                                text _("Background music and menu themes.") style "ui_preferences_description"

                            bar:
                                style "ui_preferences_bar"
                                value Preference("music volume")
                                yalign 0.5

                            textbutton _("MUTE"):
                                style "ui_preferences_small_button"
                                action Preference("music mute", "toggle")
                                at ui_button_motion

                        frame:
                            style "ui_preferences_panel"

                            has hbox
                            spacing 28
                            yalign 0.5

                            vbox:
                                xsize 620
                                spacing 8

                                text _("ANIMATION SOUND") style "ui_preferences_label"
                                text _("Audio embedded in cinematic animation scenes.") style "ui_preferences_description"

                            bar:
                                style "ui_preferences_bar"
                                value Preference("mixer animation volume")
                                yalign 0.5

                            textbutton _("MUTE"):
                                style "ui_preferences_small_button"
                                action Preference("mixer animation mute", "toggle")
                                at ui_button_motion

                    if config.has_sound:
                        frame:
                            style "ui_preferences_panel"

                            has hbox
                            spacing 28
                            yalign 0.5

                            vbox:
                                xsize 620
                                spacing 8

                                text _("SOUND EFFECTS") style "ui_preferences_label"
                                text _("Environmental and story sound effects.") style "ui_preferences_description"

                            bar:
                                style "ui_preferences_bar"
                                value Preference("sound volume")
                                yalign 0.5

                            textbutton _("MUTE"):
                                style "ui_preferences_small_button"
                                action Preference("sound mute", "toggle")
                                at ui_button_motion

                    frame:
                        style "ui_preferences_panel"

                        has hbox
                        spacing 28
                        yalign 0.5

                        vbox:
                            xsize 2140
                            spacing 8

                            text _("UI FEEDBACK") style "ui_preferences_label"
                            text _("Hover and click sounds. One switch controls both.") style "ui_preferences_description"

                        textbutton _("MUTE BOTH"):
                            style "ui_preferences_button"
                            action Preference("mixer ui_sfx mute", "toggle")
                            at ui_button_motion

                    if config.has_voice:
                        frame:
                            style "ui_preferences_panel"

                            has hbox
                            spacing 28
                            yalign 0.5

                            vbox:
                                xsize 620
                                spacing 8

                                text _("VOICE") style "ui_preferences_label"
                                text _("Narration and spoken character dialogue.") style "ui_preferences_description"

                            bar:
                                style "ui_preferences_bar"
                                value Preference("voice volume")
                                yalign 0.5

                            textbutton _("MUTE"):
                                style "ui_preferences_small_button"
                                action Preference("voice mute", "toggle")
                                at ui_button_motion

                        frame:
                            style "ui_preferences_panel"

                            has hbox
                            spacing 28
                            yalign 0.5

                            vbox:
                                xsize 2140
                                spacing 8

                                text _("NARRATOR AUTOPLAY") style "ui_preferences_label"
                                text _("Automatically continue when the narrator's voice finishes. Normal dialogue still waits for you.") style "ui_preferences_description"

                            if persistent.narrator_autoplay:
                                textbutton _("ENABLED"):
                                    style "ui_preferences_button"
                                    selected True
                                    action ToggleField(persistent, "narrator_autoplay")
                                    at ui_button_motion
                            else:
                                textbutton _("DISABLED"):
                                    style "ui_preferences_button"
                                    action ToggleField(persistent, "narrator_autoplay")
                                    at ui_button_motion


style ui_choice_cluster is hbox:
    xpos 1000
    xanchor 0.0
    yanchor 1.0
    ypos 2142
    spacing 45

style ui_memory_icon_frame is frame:
    xsize 86
    ysize 86
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    padding (10, 10)
    yalign 0.5

style ui_memory_header:
    font gui.interface_text_font
    size 25
    color "#FFD85A"
    outlines [(3, "#000000E0", 0, 2)]
    kerning 2.0

style ui_memory_body:
    font "fonts/Louis George Cafe Bold.ttf"
    size 34
    color "#F4EBDD"
    outlines [(3, "#000000D9", 0, 2)]
    line_spacing 3

style ui_say_speaker:
    properties gui.text_properties("name", accent=True)
    font gui.name_text_font
    color gui.accent_color
    text_align 0.5
    outlines [(absolute(5), "#000000D9", absolute(1), absolute(2)), (absolute(2), "#000000", 0, 0)]

style ui_say_dialogue:
    properties gui.text_properties("dialogue")
    font gui.text_font
    color "#FFFFFF"
    text_align 0.5
    line_spacing 6
    outlines [(absolute(5), "#000000E6", absolute(1), absolute(2)), (absolute(2), "#000000", 0, 0)]

style ui_choice_list is vbox:
    spacing 10

style ui_choice_player_name:
    font gui.name_text_font
    size 42
    color gui.accent_color
    outlines [(3, "#000000", 1, 1)]

style ui_route_badge is frame:
    xsize 88
    yminimum 88
    background Frame("gui/ui_refresh/choice_badge.png", 28, 28)
    padding (10, 10)
    yalign 0.5

style ui_choice_button is button:
    xsize 1600
    yminimum 88
    background Frame("gui/ui_refresh/choice_idle.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected.png", 34, 34)
    insensitive_background Frame("gui/ui_refresh/choice_insensitive.png", 34, 34)
    padding (30, 14, 26, 14)

style ui_choice_button_text is button_text:
    font "fonts/Louis George Cafe Bold.ttf"
    size 49
    color "#F3F3F0"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    insensitive_color "#69757B"
    outlines [(3, "#050709D9", 0, 2), (1, "#000000", 0, 0)]
    line_spacing 4
    text_align 0.0
    xalign 0.0
    yalign 0.5

style ui_choice_player_name_neutral is ui_choice_player_name:
    color "#718A96"

style ui_choice_player_name_good is ui_choice_player_name:
    color "#479EF5"

style ui_choice_player_name_supergood is ui_choice_player_name:
    color "#E6EDF3"

style ui_choice_player_name_evil is ui_choice_player_name:
    color "#C94B58"

style ui_choice_player_name_sexaddict is ui_choice_player_name:
    color "#7D429F"

style ui_choice_player_name_superevil is ui_choice_player_name:
    color "#2EDFE4"

style ui_route_badge_neutral is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge_neutral.png", 28, 28)

style ui_route_badge_good is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge_good.png", 28, 28)

style ui_route_badge_supergood is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge_supergood.png", 28, 28)

style ui_route_badge_evil is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge_evil.png", 28, 28)

style ui_route_badge_sexaddict is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge_sexaddict.png", 28, 28)

style ui_route_badge_superevil is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge_superevil.png", 28, 28)

style ui_route_badge_disabled is ui_route_badge:
    background Frame("gui/ui_refresh/choice_badge.png", 28, 28)

style ui_choice_button_neutral is ui_choice_button:
    background Frame("gui/ui_refresh/choice_idle_neutral.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover_neutral.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected_neutral.png", 34, 34)

style ui_choice_button_good is ui_choice_button:
    background Frame("gui/ui_refresh/choice_idle_good.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover_good.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected_good.png", 34, 34)

style ui_choice_button_supergood is ui_choice_button:
    background Frame("gui/ui_refresh/choice_idle_supergood.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover_supergood.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected_supergood.png", 34, 34)

style ui_choice_button_evil is ui_choice_button:
    background Frame("gui/ui_refresh/choice_idle_evil.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover_evil.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected_evil.png", 34, 34)

style ui_choice_button_sexaddict is ui_choice_button:
    background Frame("gui/ui_refresh/choice_idle_sexaddict.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover_sexaddict.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected_sexaddict.png", 34, 34)

style ui_choice_button_superevil is ui_choice_button:
    background Frame("gui/ui_refresh/choice_idle_superevil.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_hover_superevil.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_selected_superevil.png", 34, 34)

style ui_choice_button_disabled is ui_choice_button:
    background Frame("gui/ui_refresh/choice_insensitive.png", 34, 34)
    hover_background Frame("gui/ui_refresh/choice_insensitive.png", 34, 34)
    selected_background Frame("gui/ui_refresh/choice_insensitive.png", 34, 34)
    insensitive_background Frame("gui/ui_refresh/choice_insensitive.png", 34, 34)

style ui_choice_button_disabled_text is ui_choice_button_text:
    color "#7D878C"
    hover_color "#7D878C"
    selected_color "#7D878C"
    insensitive_color "#7D878C"
    outlines [(2, "#030506B8", 0, 1)]

style ui_choice_button_neutral_text is ui_choice_button_text:
    color "#F3F3F0"
    insensitive_color "#7D878C"

style ui_choice_button_good_text is ui_choice_button_text:
    color "#F3F3F0"
    insensitive_color "#7D878C"

style ui_choice_button_supergood_text is ui_choice_button_text:
    color "#F3F3F0"
    insensitive_color "#7D878C"

style ui_choice_button_evil_text is ui_choice_button_text:
    color "#F3F3F0"
    insensitive_color "#7D878C"

style ui_choice_button_sexaddict_text is ui_choice_button_text:
    color "#F3F3F0"
    insensitive_color "#7D878C"

style ui_choice_button_superevil_text is ui_choice_button_text:
    color "#F3F3F0"
    insensitive_color "#7D878C"

style ui_auto_button is button:
    xsize 270
    ysize 86
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)
    padding (22, 12)

style ui_auto_button_text is button_text:
    font gui.interface_text_font
    size 35
    color "#EAF0F3"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_quick_rail is vbox:
    xpos 3808
    xanchor 1.0
    ypos 1720
    spacing 8

style ui_quick_button is button:
    xsize 190
    ysize 58
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)
    padding (14, 7)

style ui_quick_button_text is button_text:
    font gui.interface_text_font
    size 24
    color "#CAD4D9"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_main_dock is frame:
    background Frame("gui/ui_refresh/panel.png", 44, 44)
    xalign 0.5
    yalign 0.92
    xsize 3420
    ysize 330
    padding (55, 42)

style ui_main_primary_button is button:
    xsize 600
    ysize 112
    background Frame("gui/ui_refresh/button_idle.png", 34, 34)
    hover_background Frame("gui/ui_refresh/button_hover.png", 34, 34)
    padding (25, 18)

style ui_main_primary_button_text is button_text:
    font gui.interface_text_font
    size 45
    color "#F4F8FA"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_main_secondary_button is button:
    xsize 430
    ysize 76
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    padding (20, 10)

style ui_main_secondary_button_text is button_text:
    font gui.interface_text_font2
    size 32
    color "#B7C4CA"
    hover_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_main_version:
    font gui.interface_text_font2
    size 26
    color "#7C8A91"

style ui_game_menu_shell is frame:
    background Frame("gui/ui_refresh/panel.png", 48, 48)
    xalign 0.5
    yalign 0.5
    xsize 3540
    ysize 1920
    padding (0, 0)

style ui_game_menu_sidebar is frame:
    background Solid("#080D11E8")
    xsize 690
    yfill True
    padding (60, 70)

style ui_game_menu_content is frame:
    background Solid("#101820D9")
    xfill True
    yfill True
    padding (70, 62, 75, 70)

style ui_navigation_list is vbox:
    spacing 13
    xfill True
    yfill True

style ui_navigation_brand:
    font gui.interface_text_font
    size 72
    color "#FFFFFF"

style ui_navigation_kicker:
    font gui.interface_text_font2
    size 27
    color "#3CDFFF"
    kerning 4

style ui_navigation_button is button:
    xfill True
    ysize 79
    background Frame("gui/ui_refresh/button_idle.png", 32, 32)
    hover_background Frame("gui/ui_refresh/button_hover.png", 32, 32)
    selected_background Frame("gui/ui_refresh/button_selected.png", 32, 32)
    padding (30, 12)

style ui_navigation_button_text is button_text:
    font gui.interface_text_font
    size 34
    color "#C8D2D7"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.0
    yalign 0.5

style ui_return_button is button:
    xfill True
    ysize 82
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    padding (30, 12)

style ui_return_button_text is button_text:
    font gui.interface_text_font
    size 34
    color "#3CDFFF"
    hover_color "#FFFFFF"
    xalign 0.0
    yalign 0.5

style ui_section_eyebrow:
    font gui.interface_text_font2
    size 27
    color "#3CDFFF"
    kerning 5

style ui_game_menu_title is label:
    padding (0, 0)

style ui_game_menu_title_text is label_text:
    font gui.interface_text_font
    size 82
    color "#FFFFFF"

style ui_game_menu_hint:
    font gui.interface_text_font2
    size 26
    color "#77878F"

style ui_preferences_tab is button:
    xsize 470
    ysize 88
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)
    padding (20, 12)

style ui_preferences_tab_text is button_text:
    font gui.interface_text_font
    size 34
    color "#AEBBC1"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_preferences_panel is frame:
    xfill True
    background Frame("gui/ui_refresh/panel_soft.png", 38, 38)
    padding (38, 30)

style ui_preferences_label:
    font gui.interface_text_font
    size 36
    color "#F3F7F9"

style ui_preferences_description:
    font gui.interface_text_font2
    size 27
    color "#87969D"

style ui_preferences_button is button:
    xminimum 330
    ysize 78
    background Frame("gui/ui_refresh/button_idle.png", 30, 30)
    hover_background Frame("gui/ui_refresh/button_hover.png", 30, 30)
    selected_background Frame("gui/ui_refresh/button_selected.png", 30, 30)
    padding (28, 12)

style ui_preferences_button_text is button_text:
    font gui.interface_text_font
    size 29
    color "#C8D3D8"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_preferences_small_button is button:
    xminimum 210
    ysize 78
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)
    padding (24, 12)

style ui_preferences_small_button_text is button_text:
    font gui.interface_text_font
    size 29
    color "#C8D3D8"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    xalign 0.5
    yalign 0.5

style ui_preferences_bar is bar:
    xsize 1420
    ysize 48


style slot_button:
    background Frame("gui/ui_refresh/panel_soft.png", 38, 38)
    hover_background Frame("gui/ui_refresh/panel_strong.png", 38, 38)

style page_button:
    background Frame("gui/ui_refresh/quick_idle.png", 28, 28)
    hover_background Frame("gui/ui_refresh/quick_hover.png", 28, 28)
    selected_background Frame("gui/ui_refresh/quick_selected.png", 28, 28)

style confirm_frame:
    background Frame("gui/ui_refresh/panel_strong.png", 44, 44)

style confirm_button:
    background Frame("gui/ui_refresh/button_idle.png", 34, 34)
    hover_background Frame("gui/ui_refresh/button_hover.png", 34, 34)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

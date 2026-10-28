init offset = 140








define -140 config.game_menu_music = "music/menu theme.wav"


transform -140 godson_noir_system_arrive:
    subpixel True
    alpha 0.0
    zoom 0.99
    easeout 0.28 alpha 1.0 zoom 1.0


transform -140 godson_noir_sidebar_arrive:
    subpixel True
    alpha 0.0
    xoffset -78
    pause 0.03
    easeout 0.32 alpha 1.0 xoffset 0


transform -140 godson_noir_content_arrive:
    subpixel True
    alpha 0.0
    xoffset 72
    pause 0.07
    easeout 0.34 alpha 1.0 xoffset 0


transform -140 godson_noir_nav_motion:
    subpixel True
    on idle:
        easeout 0.14 xoffset 0 zoom 1.0
    on hover:
        easeout 0.14 xoffset 14 zoom 1.014
    on selected_idle:
        xoffset 7
        zoom 1.006
    on selected_hover:
        easeout 0.14 xoffset 14 zoom 1.014


transform -140 godson_noir_logo_breathe:
    alpha 0.94
    ease 2.8 alpha 1.0
    ease 2.8 alpha 0.94
    repeat


transform -140 godson_noir_status_pulse:
    alpha 0.48
    ease 1.25 alpha 1.0
    ease 1.25 alpha 0.48
    repeat


transform -140 godson_noir_ornament_turn:
    subpixel True
    alpha 0.66
    rotate 0
    linear 70.0 rotate 360
    repeat


transform -140 godson_noir_gold_scan:
    alpha 0.0
    xoffset -180
    pause 0.8
    linear 0.4 alpha 0.55
    linear 3.4 xoffset 2600 alpha 0.0
    pause 1.8
    repeat


init screen godson_system_nav_item(nav_index, label_text, button_action, danger=False):
    $ nav_style = "godson_noir_nav_danger" if danger else "godson_noir_nav_button"

    textbutton label_text:
        style nav_style
        action button_action
        at godson_noir_nav_motion


init screen godson_system_tips_nav_item():
    fixed:
        xsize 630
        ysize 102

        textbutton _("TIPS"):
            style "godson_noir_tips_nav_button"
            action ShowMenu("tips")
            at godson_noir_nav_motion

        add Transform(Solid("#D7B75F"), rotate=45):
            xpos 9
            yalign 0.5
            xysize (17, 17)

        add Transform(Solid("#7A1C29"), rotate=45):
            xpos 25
            yalign 0.5
            xysize (11, 11)

        add "gui/christmas_noir/snowflake_gold.png":
            xpos 548
            yalign 0.5
            xysize (50, 50)
            at godson_noir_status_pulse


init screen navigation():
    $ active_alignment = godson_current_alignment()
    $ alignment_label, alignment_color, alignment_tint, alignment_edge, alignment_icon = godson_alignment_visuals(active_alignment)
    $ current_player = getattr(renpy.store, "playerName", "PLAYER") or "PLAYER"

    fixed:
        xfill True
        yfill True

        add Solid("#050302F4")
        add Solid("#21050A70") xpos 0 ypos 0 xsize 720 ysize 2000

        add Solid("#B78F42") xpos 718 ypos 0 xsize 2 ysize 2000 alpha 0.65
        add Solid("#5D1620") xpos 710 ypos 0 xsize 7 ysize 2000 alpha 0.90

        add "gui/christmas_noir/snowflake_gold.png":
            xpos 536
            ypos 60
            xysize (112, 112)
            at godson_noir_ornament_turn

        vbox:
            xpos 42
            ypos 30
            xsize 630
            spacing 0

            fixed:
                xsize 630
                ysize 450

                add Crop((330, 35, 1025, 855), "gui/godson_system_logo.png"):
                    xalign 0.5
                    yalign 0.5
                    xysize (555, 420)
                    fit "contain"
                    at godson_noir_logo_breathe

            text _("MENU"):
                font "fonts/jenriv-titling-bold.otf"
                size 20
                color "#D0AD62"
                kerning 4.0
                xalign 0.5

            null height 16

            fixed:
                xsize 630
                ysize 4

                add Solid("#6A151E") xsize 196 ysize 3
                add Solid("#B99347") xpos 196 xsize 238 ysize 3
                add Solid("#6A151E") xpos 434 xsize 196 ysize 3

            null height 28

            vbox:
                xfill True
                spacing 9

                if main_menu:
                    use godson_system_nav_item("01", _("NEW GAME"), Start())
                    use godson_system_nav_item("02", _("LOAD GAME"), ShowMenu("load"))
                    use godson_system_nav_item("03", _("GALLERY"), ShowMenu("gallery"))
                    use godson_system_nav_item("04", _("OPTIONS"), ShowMenu("preferences"))
                    use godson_system_nav_item("05", _("ABOUT"), ShowMenu("about"))

                    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                        use godson_system_nav_item("06", _("CONTROLS"), ShowMenu("help"))

                    if renpy.variant("pc"):
                        use godson_system_nav_item("07", _("QUIT GAME"), Quit(confirm=False), danger=True)

                    null height 18


                    use godson_system_nav_item("00", _("RETURN"), Return())

                else:
                    use godson_system_nav_item("01", _("RESUME"), Return())
                    use godson_system_nav_item("02", _("SAVE GAME"), ShowMenu("save"))
                    use godson_system_nav_item("03", _("LOAD GAME"), ShowMenu("load"))
                    use godson_system_nav_item("04", _("HISTORY"), ShowMenu("history"))
                    use godson_system_nav_item("05", _("GALLERY"), ShowMenu("gallery"))
                    use godson_system_nav_item("06", _("OPTIONS"), ShowMenu("preferences"))
                    use godson_system_nav_item("07", _("ABOUT"), ShowMenu("about"))

                    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                        use godson_system_nav_item("08", _("CONTROLS"), ShowMenu("help"))

                    if _in_replay:
                        use godson_system_nav_item("09", _("END REPLAY"), EndReplay(confirm=True), danger=True)
                    else:
                        use godson_system_nav_item("09", _("MAIN MENU"), MainMenu(), danger=True)

                    if renpy.variant("pc"):
                        use godson_system_nav_item("10", _("QUIT GAME"), Quit(confirm=True), danger=True)

                    null height 46
                    use godson_system_tips_nav_item

        frame:
            style "godson_noir_identity_card"
            xpos 45
            ypos 1684

            has fixed
            xfill True
            yfill True

            add alignment_icon:
                xpos 42
                yalign 0.5
                xysize (88, 88)
                fit "contain"

            vbox:
                xpos 152
                yalign 0.5
                spacing 3

                if main_menu:
                    text _("FRONTEND STATUS") style "godson_noir_card_kicker"
                    text _("AWAITING DESTINY") style "godson_noir_card_title"
                else:
                    text _("[current_player] // CURRENT PATH") style "godson_noir_card_kicker"
                    text _("[alignment_label] ALIGNMENT"):
                        style "godson_noir_card_title"
                        color alignment_color

            add "gui/christmas_noir/duality_medallion.png":
                xpos 510
                yalign 0.5
                xysize (82, 82)
                at godson_noir_ornament_turn


init screen game_menu(title, scroll=None, yinitial=0.0):
    tag menu
    style_prefix "game_menu"

    $ active_alignment = godson_current_alignment()
    $ alignment_label, alignment_color, alignment_tint, alignment_edge, alignment_icon = godson_alignment_visuals(active_alignment)

    add "gui/christmas_noir/system_background_neutral_4k.png"
    add Solid("#03020266")

    frame:
        style "godson_noir_system_shell"
        at godson_noir_system_arrive

        has hbox
        spacing 0
        xfill True
        yfill True

        frame:
            style "godson_noir_system_sidebar"
            at godson_noir_sidebar_arrive

            use navigation

        frame:
            style "godson_noir_system_content"
            at godson_noir_content_arrive

            has vbox
            spacing 0
            xfill True
            yfill True

            fixed:
                xfill True
                ysize 178

                vbox:
                    xpos 0
                    ypos 5
                    spacing 0

                    text _("GODSON") style "godson_noir_system_section"
                    label title style "godson_noir_page_title"

                vbox:
                    xalign 1.0
                    ypos 18
                    spacing 8

                    hbox:
                        xalign 1.0
                        spacing 13

                        add alignment_icon:
                            xysize (38, 38)
                            fit "contain"
                            yalign 0.5

                        text _("[alignment_label] PATH"):
                            style "godson_noir_session"
                            color alignment_color

                    text _("ESC / RIGHT CLICK TO RETURN") style "godson_noir_hint" xalign 1.0

            fixed:
                xfill True
                ysize 7

                add Solid("#3C3027") xsize 2730 ysize 2 yalign 0.5
                add Solid("#B99248") xsize 380 ysize 4 yalign 0.5
                add Solid("#651822") xpos 380 xsize 160 ysize 4 yalign 0.5
                add Solid("#F2D991") xsize 180 ysize 2 yalign 0.5 at godson_noir_gold_scan

            null height 34

            if scroll == "viewport":
                viewport:
                    xsize 2730
                    ysize 1544




                    mousewheel (not (godson_name_color_dropdown and godson_name_color_dropdown_hovered))
                    draggable (not (godson_name_color_dropdown and godson_name_color_dropdown_hovered))
                    pagekeys True
                    yinitial yinitial

                    has vbox
                    xsize 2670
                    spacing 20
                    transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    xsize 2730
                    ysize 1544
                    mousewheel True
                    draggable True
                    pagekeys True
                    yinitial yinitial
                    transclude

            else:
                fixed:
                    xsize 2730
                    ysize 1544
                    transclude

            null height 18

            hbox:
                xfill True
                ysize 34

                text _("GODSON") style "godson_noir_footer"
                null
                text _("BUILD [config.version]") style "godson_noir_footer"

    if main_menu:

        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action Return()


init screen godson_tip_card(tip_number, tip_title, tip_body, accent_side="left"):
    frame:
        style "godson_noir_tip_card"

        has fixed
        xfill True
        yfill True

        add Solid("#C8A24F"):
            xpos (0 if accent_side == "left" else 1244)
            ypos 26
            xsize 5
            ysize 470

        add Transform(Solid("#7A1B28"), rotate=45):
            xpos (21 if accent_side == "left" else 1218)
            ypos 32
            xysize (18, 18)

        text tip_number:
            style "godson_noir_tip_number"
            xpos 48
            ypos 35

        text tip_title:
            style "godson_noir_tip_title"
            xpos 152
            ypos 32
            xmaximum 1015

        add Solid("#6F1721"):
            xpos 48
            ypos 116
            xsize 1120
            ysize 2

        add Solid("#D1AE5B"):
            xpos 48
            ypos 116
            xsize 210
            ysize 3

        text tip_body:
            style "godson_noir_tip_body"
            xpos 50
            ypos 156
            xmaximum 1115

        text _("THE NIGHT REMEMBERS"):
            style "godson_noir_tip_footer"
            xpos 50
            ypos 463

        add "gui/christmas_noir/snowflake_gold.png":
            xpos 1132
            ypos 438
            xysize (54, 54)
            alpha 0.46


init screen tips():
    tag menu

    use game_menu(_("Tips")):
        fixed:
            xsize 2730
            ysize 1544

            vbox:
                xpos 36
                ypos 8
                spacing 7

                text _("GODSON FIELD NOTES") style "godson_noir_tips_heading"
                text _("Four things worth knowing before the night decides what it remembers.") style "godson_noir_tips_intro"

            add Solid("#C9A655") xpos 36 ypos 132 xsize 260 ysize 4
            add Solid("#651822") xpos 296 ypos 133 xsize 1015 ysize 2

            grid 2 2:
                xpos 34
                ypos 180
                xspacing 70
                yspacing 56

                use godson_tip_card("01", _("EXPLORE EVERY PATH"), _("Every route tells a meaningfully different version of Godson. Characters, discoveries, and entire scenes change with your alignment, so one playthrough never shows the full story."), "left"
                )





                use godson_tip_card("02", _("SAVE SUPER EVIL FOR LATER"), _("The Super Evil route is designed for players who have already completed at least one other path. Its shortcuts, reveals, and altered perspective land best when you know what it is twisting."), "right"
                )





                use godson_tip_card("03", _("CHARACTERS REMEMBER"), _("Important words and actions can stay with people long after a conversation ends. A response that seems small now may shape how someone treats you later."), "left"
                )





                use godson_tip_card("04", _("HOW YOU SAY IT MATTERS"), _("Two choices can reach the same immediate result without meaning the same thing. Tone matters, and characters may remember whether you were kind, cold, blunt, or cruel."), "right"
                )






style godson_noir_system_shell is frame:
    background Frame("gui/christmas_noir/panel_strong.png", 58, 58)
    xalign 0.5
    yalign 0.5
    xsize 3680
    ysize 2020
    padding (0, 0)


style godson_noir_system_sidebar is frame:
    background Solid("#050302EE")
    xsize 720
    yfill True
    padding (0, 0)


style godson_noir_system_content is frame:
    background Solid("#0B0807D8")
    xfill True
    yfill True
    padding (78, 56, 80, 46)


style godson_noir_nav_button is button:
    xfill True
    ysize 74
    background "gui/christmas_noir/nav_idle.png"
    hover_background "gui/christmas_noir/nav_hover.png"
    selected_background "gui/christmas_noir/nav_hover.png"
    insensitive_background "gui/christmas_noir/nav_idle.png"
    padding (32, 10)


style godson_noir_nav_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 31
    color "#AFA79A"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    insensitive_color "#514B44"
    xalign 0.0
    yalign 0.5
    kerning 1.2
    outlines [(2, "#000000C8", 0, 1)]


style godson_noir_nav_danger is godson_noir_nav_button:
    hover_background "gui/christmas_noir/nav_danger.png"
    selected_background "gui/christmas_noir/nav_danger.png"


style godson_noir_nav_danger_text is godson_noir_nav_button_text:
    hover_color "#FFC4C8"
    selected_color "#FFC4C8"


style godson_noir_tips_nav_button is button:
    xfill True
    ysize 102
    background Frame("gui/christmas_noir/panel_velvet.png", 52, 52)
    hover_background Frame("gui/christmas_noir/button_selected.png", 42, 42)
    selected_background Frame("gui/christmas_noir/button_selected.png", 42, 42)
    padding (50, 14)


style godson_noir_tips_nav_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 34
    color "#E7CC86"
    hover_color "#FFF0A6"
    selected_color "#FFF0A6"
    xalign 0.0
    yalign 0.5
    kerning 2.1
    outlines [(3, "#000000D0", 0, 1)]


style godson_noir_identity_card is frame:
    xsize 630
    ysize 146
    background Frame("gui/christmas_noir/panel_velvet.png", 52, 52)
    padding (0, 0)


style godson_noir_card_kicker:
    font "fonts/jenriv-titling-bold.otf"
    size 18
    color "#8E806E"
    kerning 1.8


style godson_noir_card_title:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 31
    color "#F5EBDD"
    outlines [(2, "#000000C8", 0, 1)]


style godson_noir_system_section:
    font "fonts/jenriv-titling-bold.otf"
    size 22
    color "#C8A354"
    kerning 4.0


style godson_noir_page_title is label:
    padding (0, 0)


style godson_noir_page_title_text is label_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 78
    color "#F7EFE3"
    outlines [(3, "#000000B8", 0, 2)]


style godson_noir_session:
    font "fonts/jenriv-titling-bold.otf"
    size 22
    color "#D8C9B5"
    kerning 2.0


style godson_noir_hint:
    font "fonts/jenriv-titling-bold.otf"
    size 18
    color "#766B5F"
    kerning 1.4


style godson_noir_footer:
    font "fonts/jenriv-titling-bold.otf"
    size 17
    color "#655A50"
    kerning 2.0


style godson_noir_tip_card is frame:
    xsize 1275
    ysize 520
    background Frame("gui/christmas_noir/panel_soft.png", 52, 52)
    padding (0, 0)


style godson_noir_tips_heading is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 58
    color "#FFD85A"
    kerning 1.2
    outlines [(3, "#000000D0", 0, 2)]


style godson_noir_tips_intro is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 28
    color "#AFA291"
    outlines [(2, "#000000B8", 0, 1)]


style godson_noir_tip_number is text:
    font "fonts/jenriv-titling-bold.otf"
    size 38
    color "#C34A57"
    kerning 2.0
    outlines [(2, "#000000C8", 0, 1)]


style godson_noir_tip_title is text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 38
    color "#F4DFC0"
    kerning 0.8
    outlines [(2, "#000000C8", 0, 1)]


style godson_noir_tip_body is text:
    font gui.interface_text_font2
    size 30
    color "#D8CCBA"
    line_spacing 8
    outlines [(2, "#000000A8", 0, 1)]


style godson_noir_tip_footer is text:
    font "fonts/jenriv-titling-bold.otf"
    size 16
    color "#776A59"
    kerning 2.4



style ui_preferences_tab is button:
    xsize 470
    ysize 88
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)
    selected_background Frame("gui/christmas_noir/tab_selected.png", 28, 28)
    padding (20, 12)


style ui_preferences_tab_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 31
    color "#AFA598"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    xalign 0.5
    yalign 0.5
    outlines [(2, "#000000B8", 0, 1)]


style ui_preferences_panel is frame:
    xfill True
    background Frame("gui/christmas_noir/panel_soft.png", 52, 52)
    padding (42, 34)


style ui_preferences_label:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 36
    color "#F4EBDD"
    outlines [(2, "#000000B8", 0, 1)]


style ui_preferences_description:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 26
    color "#9B8E7D"


style ui_preferences_button is button:
    xminimum 330
    ysize 78
    background Frame("gui/christmas_noir/button_idle.png", 42, 42)
    hover_background Frame("gui/christmas_noir/button_hover.png", 42, 42)
    selected_background Frame("gui/christmas_noir/button_selected.png", 42, 42)
    padding (28, 12)


style ui_preferences_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 28
    color "#C7BCAE"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    xalign 0.5
    yalign 0.5
    outlines [(2, "#000000B0", 0, 1)]


style ui_preferences_small_button is button:
    xminimum 210
    ysize 78
    background Frame("gui/christmas_noir/button_idle.png", 42, 42)
    hover_background Frame("gui/christmas_noir/button_hover.png", 42, 42)
    selected_background Frame("gui/christmas_noir/button_selected.png", 42, 42)
    padding (24, 12)


style ui_preferences_small_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 28
    color "#C7BCAE"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    xalign 0.5
    yalign 0.5
    outlines [(2, "#000000B0", 0, 1)]




style ui_preferences_bar is bar:
    xsize 1420
    ysize 82
    left_bar Frame("gui/christmas_noir/slider_track_fill.png", 30, 30)
    right_bar Frame("gui/christmas_noir/slider_track_empty.png", 30, 30)
    thumb "gui/christmas_noir/slider_thumb_idle.png"
    hover_thumb "gui/christmas_noir/slider_thumb_hover.png"
    thumb_offset 41




style slot_button is button:
    background "gui/christmas_noir/save_slot_idle_clean.png"
    hover_background "gui/christmas_noir/save_slot_hover_clean.png"
    selected_background "gui/christmas_noir/save_slot_hover_clean.png"
    padding (14, 14)





init 50 screen help():
    tag menu

    default device = "keyboard"

    use game_menu(_("Controls"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 45

            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help




init 50 screen controls():
    tag menu

    default device = "keyboard"

    use game_menu(_("Controls"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 45

            hbox:
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help





init 20 style help_button is button:
    xmargin 24
    background Frame("gui/christmas_noir/tab_idle.png", 28, 28)
    hover_background Frame("gui/christmas_noir/tab_hover.png", 28, 28)
    selected_background Frame("gui/christmas_noir/tab_selected.png", 28, 28)
    padding (28, 14)


init 20 style help_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size 34
    color "#D8CCBA"
    hover_color "#FFD85A"
    selected_color "#FFD85A"
    insensitive_color "#6E665C"
    xalign 0.5
    yalign 0.5
    outlines [(2, "#000000D0", 0, 1)]


init 20 style help_label:
    xsize 750
    right_padding 60


init 20 style help_label_text is label_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    size gui.text_size
    color "#FFD85A"
    xalign 1.0
    text_align 1.0
    outlines [(2, "#000000D0", 0, 1)]


init 20 style help_text is text:
    font gui.interface_text_font2
    size gui.text_size
    color "#E9E0D3"


style page_button is button:



    background Frame("gui/christmas_noir/button_idle.png", 20, 20)
    hover_background Frame("gui/christmas_noir/button_hover.png", 20, 20)
    selected_background Frame("gui/christmas_noir/button_selected.png", 20, 20)
    insensitive_background Frame("gui/christmas_noir/button_idle.png", 20, 20)


style page_button_text is button_text:
    font "fonts/CrimsonText-SemiBold.ttf"
    color "#9F9588"
    hover_color "#FFE6A8"
    selected_color "#FFE6A8"
    insensitive_color "#4B453F"
    outlines [(2, "#000000B0", 0, 1)]


style godson_pager_page_button is page_button:
    background None
    hover_background None
    selected_background None
    selected_hover_background None
    insensitive_background None
    xminimum 94
    yminimum 60
    xpadding 16
    ypadding 6


style godson_pager_page_button_text is page_button_text:
    size 40
    text_align 0.5


style godson_pager_arrow_button is godson_pager_page_button:
    xminimum 78


style godson_pager_arrow_button_text is godson_pager_page_button_text:
    size 34


style godson_pager_utility_button is page_button:
    background None
    hover_background None
    selected_background None
    selected_hover_background None
    insensitive_background None
    xminimum 210
    yminimum 50
    xpadding 22
    ypadding 5


style godson_pager_utility_button_text is page_button_text:
    size 28
    kerning 1.5
    text_align 0.5


style godson_pager_jump_button is page_button:
    background None
    hover_background None
    selected_background None
    selected_hover_background None
    insensitive_background None
    xminimum 98
    yminimum 50
    xpadding 14
    ypadding 5


style godson_pager_jump_button_text is page_button_text:
    size 29
    text_align 0.5


style godson_pager_jump_label is text:
    font "fonts/jenriv-titling-bold.otf"
    size 22
    color "#C4A153"
    kerning 2.5
    outlines [(1, "#000000B8", 0, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc







transform godson_noir_logo_arrive:
    subpixel True
    alpha 0.0
    xoffset -54
    zoom 0.975
    easeout 0.62 alpha 1.0 xoffset 0 zoom 1.0
    parallel:
        ease 3.4 zoom 1.008
        ease 3.4 zoom 1.0
        repeat


transform godson_noir_menu_arrive:
    subpixel True
    alpha 0.0
    xoffset -90
    pause 0.14
    easeout 0.52 alpha 1.0 xoffset 0


transform godson_noir_command_motion:
    subpixel True
    on idle:
        easeout 0.16 xoffset 0 zoom 1.0
    on hover:
        easeout 0.16 xoffset 28 zoom 1.012


transform godson_noir_secondary_motion:
    subpixel True
    on idle:
        easeout 0.14 yoffset 0 zoom 1.0
    on hover:
        easeout 0.14 yoffset -5 zoom 1.025


transform godson_noir_gold_pulse:
    alpha 0.34
    ease 1.35 alpha 0.92
    ease 1.35 alpha 0.34
    repeat


transform godson_noir_candle_breathe:
    alpha 0.80
    ease 1.1 alpha 1.0
    ease 1.45 alpha 0.76
    repeat


transform godson_noir_snowflake_turn:
    subpixel True
    alpha 0.34
    rotate 0
    linear 42.0 rotate 360
    repeat


transform godson_noir_snowflake_turn_reverse:
    subpixel True
    alpha 0.26
    rotate 360
    linear 56.0 rotate 0
    repeat


transform godson_noir_snowflake_turn_slow:
    subpixel True
    alpha 0.20
    rotate 0
    linear 74.0 rotate 360
    repeat


transform godson_noir_snowflake_turn_medium:
    subpixel True
    alpha 0.24
    rotate 0
    linear 51.0 rotate 360
    repeat


transform godson_noir_snowflake_turn_reverse_slow:
    subpixel True
    alpha 0.18
    rotate 360
    linear 82.0 rotate 0
    repeat


transform godson_noir_medallion_turn:
    subpixel True
    alpha 0.88
    rotate 0
    linear 72.0 rotate 360
    repeat


transform godson_noir_particle_one:
    alpha 0.0
    yoffset -70
    pause 0.25
    linear 0.8 alpha 0.76
    linear 10.5 yoffset 860 alpha 0.18
    linear 0.7 alpha 0.0
    repeat


transform godson_noir_particle_two:
    alpha 0.0
    yoffset -60
    pause 1.75
    linear 0.9 alpha 0.60
    linear 12.0 yoffset 720 alpha 0.14
    linear 0.7 alpha 0.0
    repeat


transform godson_noir_particle_three:
    alpha 0.0
    yoffset -80
    pause 3.4
    linear 0.75 alpha 0.70
    linear 9.25 yoffset 1040 alpha 0.12
    linear 0.65 alpha 0.0
    repeat


transform godson_noir_particle_four:
    alpha 0.0
    yoffset -55
    pause 5.1
    linear 1.0 alpha 0.52
    linear 13.0 yoffset 900 alpha 0.10
    linear 0.8 alpha 0.0
    repeat


transform godson_noir_particle_five:
    alpha 0.0
    yoffset -65
    pause 6.65
    linear 0.85 alpha 0.66
    linear 11.0 yoffset 680 alpha 0.12
    linear 0.7 alpha 0.0
    repeat


transform godson_noir_particle_six:
    alpha 0.0
    yoffset -75
    pause 0.95
    linear 0.7 alpha 0.62
    linear 8.6 yoffset 780 alpha 0.10
    linear 0.65 alpha 0.0
    repeat


transform godson_noir_particle_seven:
    alpha 0.0
    yoffset -60
    pause 2.55
    linear 1.0 alpha 0.48
    linear 14.2 yoffset 980 alpha 0.08
    linear 0.8 alpha 0.0
    repeat


transform godson_noir_particle_eight:
    alpha 0.0
    yoffset -85
    pause 4.25
    linear 0.75 alpha 0.68
    linear 10.8 yoffset 760 alpha 0.12
    linear 0.7 alpha 0.0
    repeat


transform godson_noir_particle_nine:
    alpha 0.0
    yoffset -70
    pause 5.85
    linear 0.9 alpha 0.50
    linear 12.6 yoffset 1120 alpha 0.08
    linear 0.75 alpha 0.0
    repeat


transform godson_noir_particle_ten:
    alpha 0.0
    yoffset -50
    pause 7.45
    linear 0.8 alpha 0.60
    linear 9.8 yoffset 820 alpha 0.10
    linear 0.65 alpha 0.0
    repeat


init 140 screen main_menu():
    tag menu

    default menu_focus = "new"



    $ load_menu_action = ShowMenu("load")
    $ gallery_menu_action = ShowMenu("gallery")
    $ options_menu_action = ShowMenu("preferences")
    $ about_menu_action = ShowMenu("about")
    $ help_menu_action = ShowMenu("help")

    $ main_commands = [
        (_("NEW GAME"), _("BEGIN THE STORY"), Start(), "new"),
        (_("LOAD GAME"), _("RETURN TO A SAVED MOMENT"), load_menu_action, "load"),
        (_("GALLERY"), _("VIEW UNLOCKED MEMORIES"), gallery_menu_action, "gallery"),
        (_("OPTIONS"), _("CUSTOMIZE YOUR EXPERIENCE"), options_menu_action, "options"),
        (_("ABOUT"), _("CREDITS AND PROJECT INFORMATION"), about_menu_action, "about"),
        (_("HELP"), _("CONTROLS AND GAMEPLAY GUIDE"), help_menu_action, "help"),
        (_("PATREON"), _("SUPPORT CHEESECAKE STUDIO FOR FASTER UPDATES, EARLY CONTENT, AND EXTRA CONTENT"), OpenURL("https://patreon.com/cheesecake3d"), "patreon"),
        (_("DISCORD"), _("JOIN THE COMMUNITY"), OpenURL("https://discord.gg/cheesecake"), "discord"),
        (_("QUIT GAME"), _("RETURN TO DESKTOP"), Quit(confirm=False), "quit")
    ]

    add "gui/christmas_noir/main_background_neutral_4k.png"


    add Solid("#02020278") xpos 0 ypos 0 xsize 1780 ysize 2160
    add Solid("#1703072C") xpos 0 ypos 0 xsize 1950 ysize 2160




    add "gui/christmas_noir/snowflake_gold.png":
        xpos 1428
        ypos 178
        xysize (118, 118)
        at godson_noir_snowflake_turn

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 452
        ypos 1390
        xysize (72, 72)
        at godson_noir_snowflake_turn_reverse

    add "gui/christmas_noir/snowflake_gold.png":
        xpos 2040
        ypos 246
        xysize (88, 88)
        at godson_noir_snowflake_turn_slow

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 2790
        ypos 1190
        xysize (66, 66)
        at godson_noir_snowflake_turn_reverse

    add "gui/christmas_noir/snowflake_gold.png":
        xpos 3480
        ypos 390
        xysize (96, 96)
        at godson_noir_snowflake_turn

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 3190
        ypos 1770
        xysize (54, 54)
        at godson_noir_snowflake_turn_slow

    add "gui/christmas_noir/snowflake_gold.png":
        xpos 220
        ypos 520
        xysize (58, 58)
        at godson_noir_snowflake_turn_medium

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 980
        ypos 1760
        xysize (48, 48)
        at godson_noir_snowflake_turn_reverse_slow

    add "gui/christmas_noir/snowflake_gold.png":
        xpos 1760
        ypos 1120
        xysize (76, 76)
        at godson_noir_snowflake_turn_reverse

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 2390
        ypos 690
        xysize (56, 56)
        at godson_noir_snowflake_turn_slow

    add "gui/christmas_noir/snowflake_gold.png":
        xpos 3010
        ypos 120
        xysize (68, 68)
        at godson_noir_snowflake_turn_medium

    add "gui/christmas_noir/snowflake_frost.png":
        xpos 3710
        ypos 1440
        xysize (62, 62)
        at godson_noir_snowflake_turn_reverse_slow

    add "gui/christmas_noir/duality_medallion.png":
        xpos 3440
        ypos 1588
        xysize (250, 250)
        at godson_noir_medallion_turn

    add "gui/christmas_noir/gold_particle.png":
        xpos 92
        ypos 40
        xysize (12, 12)
        at godson_noir_particle_one

    add "gui/christmas_noir/gold_particle.png":
        xpos 286
        ypos 810
        xysize (9, 9)
        at godson_noir_particle_two

    add "gui/christmas_noir/gold_particle.png":
        xpos 486
        ypos 210
        xysize (16, 16)
        at godson_noir_particle_three

    add "gui/christmas_noir/gold_particle.png":
        xpos 690
        ypos 1110
        xysize (8, 8)
        at godson_noir_particle_four

    add "gui/christmas_noir/gold_particle.png":
        xpos 884
        ypos 70
        xysize (11, 11)
        at godson_noir_particle_five

    add "gui/christmas_noir/gold_particle.png":
        xpos 1080
        ypos 620
        xysize (14, 14)
        at godson_noir_particle_two

    add "gui/christmas_noir/gold_particle.png":
        xpos 1286
        ypos 1320
        xysize (8, 8)
        at godson_noir_particle_one

    add "gui/christmas_noir/gold_particle.png":
        xpos 1480
        ypos 310
        xysize (13, 13)
        at godson_noir_particle_four

    add "gui/christmas_noir/gold_particle.png":
        xpos 1682
        ypos 930
        xysize (10, 10)
        at godson_noir_particle_three

    add "gui/christmas_noir/gold_particle.png":
        xpos 1880
        ypos 90
        xysize (17, 17)
        at godson_noir_particle_two

    add "gui/christmas_noir/gold_particle.png":
        xpos 2084
        ypos 1190
        xysize (8, 8)
        at godson_noir_particle_five

    add "gui/christmas_noir/gold_particle.png":
        xpos 2280
        ypos 470
        xysize (12, 12)
        at godson_noir_particle_one

    add "gui/christmas_noir/gold_particle.png":
        xpos 2488
        ypos 1440
        xysize (9, 9)
        at godson_noir_particle_three

    add "gui/christmas_noir/gold_particle.png":
        xpos 2680
        ypos 180
        xysize (15, 15)
        at godson_noir_particle_four

    add "gui/christmas_noir/gold_particle.png":
        xpos 2884
        ypos 790
        xysize (10, 10)
        at godson_noir_particle_two

    add "gui/christmas_noir/gold_particle.png":
        xpos 3080
        ypos 1280
        xysize (7, 7)
        at godson_noir_particle_five

    add "gui/christmas_noir/gold_particle.png":
        xpos 3284
        ypos 330
        xysize (14, 14)
        at godson_noir_particle_one

    add "gui/christmas_noir/gold_particle.png":
        xpos 3482
        ypos 1040
        xysize (9, 9)
        at godson_noir_particle_four

    add "gui/christmas_noir/gold_particle.png":
        xpos 3690
        ypos 120
        xysize (12, 12)
        at godson_noir_particle_three

    add "gui/christmas_noir/gold_particle.png":
        xpos 170
        ypos 1240
        xysize (10, 10)
        at godson_noir_particle_six

    add "gui/christmas_noir/gold_particle.png":
        xpos 380
        ypos 360
        xysize (13, 13)
        at godson_noir_particle_seven

    add "gui/christmas_noir/gold_particle.png":
        xpos 590
        ypos 1540
        xysize (8, 8)
        at godson_noir_particle_eight

    add "gui/christmas_noir/gold_particle.png":
        xpos 790
        ypos 540
        xysize (15, 15)
        at godson_noir_particle_nine

    add "gui/christmas_noir/gold_particle.png":
        xpos 990
        ypos 1450
        xysize (9, 9)
        at godson_noir_particle_ten

    add "gui/christmas_noir/gold_particle.png":
        xpos 1190
        ypos 180
        xysize (12, 12)
        at godson_noir_particle_six

    add "gui/christmas_noir/gold_particle.png":
        xpos 1390
        ypos 790
        xysize (7, 7)
        at godson_noir_particle_seven

    add "gui/christmas_noir/gold_particle.png":
        xpos 1585
        ypos 1510
        xysize (14, 14)
        at godson_noir_particle_eight

    add "gui/christmas_noir/gold_particle.png":
        xpos 1785
        ypos 520
        xysize (10, 10)
        at godson_noir_particle_nine

    add "gui/christmas_noir/gold_particle.png":
        xpos 1980
        ypos 1370
        xysize (16, 16)
        at godson_noir_particle_ten

    add "gui/christmas_noir/gold_particle.png":
        xpos 2185
        ypos 230
        xysize (8, 8)
        at godson_noir_particle_six

    add "gui/christmas_noir/gold_particle.png":
        xpos 2380
        ypos 930
        xysize (13, 13)
        at godson_noir_particle_seven

    add "gui/christmas_noir/gold_particle.png":
        xpos 2580
        ypos 1550
        xysize (9, 9)
        at godson_noir_particle_eight

    add "gui/christmas_noir/gold_particle.png":
        xpos 2785
        ypos 520
        xysize (15, 15)
        at godson_noir_particle_nine

    add "gui/christmas_noir/gold_particle.png":
        xpos 2980
        ypos 80
        xysize (10, 10)
        at godson_noir_particle_ten

    add "gui/christmas_noir/gold_particle.png":
        xpos 3180
        ypos 760
        xysize (12, 12)
        at godson_noir_particle_six

    add "gui/christmas_noir/gold_particle.png":
        xpos 3380
        ypos 1480
        xysize (7, 7)
        at godson_noir_particle_seven

    add "gui/christmas_noir/gold_particle.png":
        xpos 3580
        ypos 600
        xysize (14, 14)
        at godson_noir_particle_eight

    add "gui/christmas_noir/gold_particle.png":
        xpos 3780
        ypos 1180
        xysize (9, 9)
        at godson_noir_particle_nine

    add "gui/christmas_noir/gold_particle.png":
        xpos 1120
        ypos 1060
        xysize (11, 11)
        at godson_noir_particle_ten

    add "gui/christmas_noir/gold_particle.png":
        xpos 1520
        ypos 70
        xysize (8, 8)
        at godson_noir_particle_six

    add "gui/christmas_noir/gold_particle.png":
        xpos 1920
        ypos 770
        xysize (13, 13)
        at godson_noir_particle_seven

    add "gui/christmas_noir/gold_particle.png":
        xpos 2320
        ypos 1320
        xysize (10, 10)
        at godson_noir_particle_eight

    add "gui/christmas_noir/gold_particle.png":
        xpos 2720
        ypos 1040
        xysize (15, 15)
        at godson_noir_particle_nine

    add "gui/christmas_noir/gold_particle.png":
        xpos 3320
        ypos 820
        xysize (9, 9)
        at godson_noir_particle_ten

    fixed:
        xpos 148
        ypos 82
        xsize 1570
        ysize 1960
        at godson_noir_menu_arrive

        text _("CHEESECAKE STUDIO"):
            font "fonts/jenriv-titling-bold.otf"
            size 22
            color "#CBA85B"
            kerning 4.0
            xpos 48
            ypos 22

        add Solid("#C9A454"):
            xpos 48
            ypos 72
            xsize 210
            ysize 3

        add Solid("#5D1620"):
            xpos 274
            ypos 72
            xsize 900
            ysize 2

        text _("GODSON"):
            font "fonts/CrimsonText-SemiBold.ttf"
            size 70
            color "#E7C760"
            kerning 1.6
            xpos 54
            ypos 118
            outlines [(3, "#000000D0", 0, 2)]

        text _("SEX, CHOICES, AND ADVENTURE"):
            font "fonts/CrimsonText-SemiBold.ttf"
            size 30
            color "#D9CFBC"
            kerning 1.2
            xpos 58
            ypos 214
            outlines [(2, "#000000C8", 0, 1)]

        add Solid("#B99042"):
            xpos 58
            ypos 274
            xsize 1040
            ysize 2

        vbox:
            xpos 34
            ypos 318
            spacing 7

            for command_label, command_detail, command_action, command_key in main_commands:
                $ command_active = menu_focus == command_key
                $ command_is_quit = command_key == "quit"
                $ command_idle = "gui/christmas_noir/command_danger_flat.png" if command_is_quit else "gui/christmas_noir/command_idle_flat.png"
                $ command_hover = "gui/christmas_noir/command_danger_flat.png" if command_is_quit else "gui/christmas_noir/command_hover_flat.png"
                $ command_accent = "#D26A72" if command_is_quit else "#E2C374"

                button:
                    xsize 1260
                    ysize 104



                    background Transform(command_idle, xysize=(1260, 104))
                    hover_background Transform(command_hover, xysize=(1260, 104))
                    padding (0, 0)
                    action command_action
                    hovered SetScreenVariable("menu_focus", command_key)
                    at godson_noir_command_motion

                    has fixed
                    xfill True
                    yfill True





                    vbox:
                        xpos 52
                        yalign 0.5
                        spacing -5

                        text command_label:
                            font "fonts/CrimsonText-SemiBold.ttf"
                            size 39
                            color ("#FFF7E6" if command_active else "#D3CCBE")
                            kerning 1.0
                            outlines [(2, "#000000D0", 0, 1)]

                        text command_detail:
                            font "fonts/jenriv-titling-bold.otf"
                            size 15
                            color (command_accent if command_active else "#7E7468")
                            kerning 1.8

                    if command_active:
                        text ">":
                            font "fonts/CrimsonText-SemiBold.ttf"
                            size 35
                            color command_accent
                            xpos 1160
                            yalign 0.5
                            at godson_noir_gold_pulse

        fixed:
            xpos 48
            ypos 1378
            xsize 1260
            ysize 70

            text _("GODSON"):
                font "fonts/jenriv-titling-bold.otf"
                size 21
                color "#C7A153"
                kerning 3.0

            text _("BUILD [config.version]"):
                font "fonts/jenriv-titling-bold.otf"
                size 18
                color "#766C61"
                kerning 1.5
                xpos 198
                ypos 2

            text _("MULTIPLE PATHS - ALL CHOICES"):
                font "fonts/jenriv-titling-bold.otf"
                size 18
                color "#766C61"
                kerning 1.8
                xalign 1.0
                ypos 2



    fixed:
        xpos 2300
        ypos 430
        xsize 1240
        ysize 1010

        add Crop((330, 35, 1025, 855), "gui/godson_system_logo.png"):
            xalign 0.5
            yalign 0.5
            xysize (1110, 925)
            fit "contain"
            at godson_noir_logo_arrive

    fixed:
        xpos 2370
        ypos 122
        xsize 1210
        ysize 92

        text _("THE NIGHT REMEMBERS"):
            font "fonts/jenriv-titling-bold.otf"
            size 22
            color "#D9BE7A"
            kerning 4.2
            xalign 0.5
            outlines [(2, "#000000D8", 0, 1)]

        add Solid("#D0AE62") xpos 250 ypos 55 xsize 710 ysize 2 alpha 0.62


init 140 style godson_noir_secondary_button is button:
    xsize 284
    ysize 68
    background "gui/christmas_noir/secondary_idle.png"
    hover_background "gui/christmas_noir/secondary_hover.png"
    padding (14, 8)


init 140 style godson_noir_secondary_button_text is button_text:
    font "fonts/jenriv-titling-bold.otf"
    size 20
    color "#9C9182"
    hover_color "#F0D58F"
    xalign 0.5
    yalign 0.5
    kerning 1.5
    outlines [(2, "#000000B8", 0, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

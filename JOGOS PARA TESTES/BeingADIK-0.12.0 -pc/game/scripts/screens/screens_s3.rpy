screen freeroam_intro_screen(arg):
    tag freeroam_intro_screen
    modal False
    timer 5 action Hide("freeroam_intro_screen")

    add "fr_ol_box" at fr_text_show_transform
    add "fr_ol_line" yalign 0.08 yoffset -5 at fr_ol_line_transform
    add "fr_ol_line" yalign 0.13 yoffset -5 at fr_ol_line_transform2
    add "fr_ol_line" yalign 0.18 yoffset -5 at fr_ol_line_transform3
    add "fr_ol_line" yalign 0.43 yoffset -5 at fr_ol_line_transform3
    add "fr_ol_line" yalign 0.48 yoffset -5 at fr_ol_line_transform2
    add "fr_ol_line" yalign 0.53 yoffset -5 at fr_ol_line_transform

    vbox at fr_text_show_transform2:
        xalign 0.93
        yalign 0.25
        spacing 5 * persistent.scale_factor
        if arg == " ":
            text "Free roam" style "fr_new_style"
            text "Complete the tasks in the Tasks app" style "fr_new_style2"
        else:
            text "Free roam" style "fr_new_style"
            text "[arg]" style "fr_new_style2"


style fr_new_style:
    font "fonts/centurygothicregular.ttf"
    size 80 * persistent.scale_factor
    color "#fe9416"
    outlines [(4, "#2d2d2d", 0, 0)]
style fr_new_style2:
    font "fonts/centurygothicregular.ttf"
    size 50 * persistent.scale_factor
    color "#ffffff"
    outlines [(4, "#2d2d2d", 0, 0)]
style score_new_style:
    font "fonts/centurygothicregular.ttf"
    size 30 * persistent.scale_factor
    color "#ffffff"
    outlines [(4, "#2d2d2d", 0, 0)]

transform fr_text_show_transform:
    on show:
        xoffset 1000 * persistent.scale_factor
        easein 0.5 xoffset 0
    on hide:
        alpha 1.0
        easein 1.0 alpha 0.0
transform fr_text_show_transform2:
    on show:
        xoffset 2000 * persistent.scale_factor
        easein 1.0 xoffset 0
    on hide:
        alpha 1.0
        easein 1.0 alpha 0.0

transform fr_ol_line_transform:
    xpos 1900 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1850 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1840 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1860 * persistent.scale_factor
    easein 0.5 xpos 1900 * persistent.scale_factor
    repeat
    on hide:
        alpha 1.0
        easein 1.0 alpha 0.0
transform fr_ol_line_transform2:
    xpos 1820 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1780 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1760 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1770 * persistent.scale_factor
    easein 0.5 xpos 1820 * persistent.scale_factor
    repeat
    on hide:
        alpha 1.0
        easein 1.0 alpha 0.0
transform fr_ol_line_transform3:
    xpos 1740 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1700 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1690 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1680 * persistent.scale_factor
    easein 0.5 xpos 1740 * persistent.scale_factor
    repeat
    on hide:
        alpha 1.0
        easein 1.0 alpha 0.0

screen yearbook_quote_screen:
    tag yearbook_quote_screen
    modal False

    text "[ep10_quote]" xalign 0.48 yalign 0.35 style "yb_style2" xminimum 500 * persistent.scale_factor xmaximum 500 * persistent.scale_factor yminimum 140 * persistent.scale_factor ymaximum 140 * persistent.scale_factor

    text "[name] [lname]" xalign 0.48 yalign 0.54 style "yb_style"

screen yearbook_quote_input_screen:
    tag yearbook_quote_input_screen
    modal False
    zorder 1

    hbox:
        yoffset 1000 * persistent.scale_factor
        xoffset 20 * persistent.scale_factor
        xalign 0.50
        yalign 0.35
        spacing 10 * persistent.scale_factor
        frame:

            style "yb_input_style"
            ymaximum 26 * persistent.scale_factor
            xmaximum 385 * persistent.scale_factor
            input:

                size 25 * persistent.scale_factor
                default "[save_name]"
                font "fonts/bradhitc.ttf"
                color "#1844c2"
                value VariableInputValue('ep10_quote')
                length 100
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _1234567890.!,;:?'´`"
                yoffset 4 * persistent.scale_factor

style yb_style:
    font "fonts/bradhitc.ttf"
    size 25 * persistent.scale_factor
    color "#1844c2"
style yb_style2:
    font "fonts/bradhitc.ttf"
    size 25 * persistent.scale_factor
    color "#1844c2"
    text_align 0.0

style yb_input_style:
    background "#cdd0d6"

style yb_input_style2:
    color "#1844c2"
    font "fonts/bradhitc.ttf"
    size 25 * persistent.scale_factor

image particle_bf1 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_bf1.png", count=5, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_bf2 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_bf2.png", count=5, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_bf3 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_bf3.png", count=5, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_bf4 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_bf4.png", count=5, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_mf1 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_mf1.png", count=10, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_mf2 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_mf2.png", count=10, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_mf3 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_mf3.png", count=10, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_sf1 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_sf1.png", count=20, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_sf2 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_sf2.png", count=20, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_sf3 = SnowBlossom("[persistent.img_dir]/ep10/snow_screen2/snow_sf3.png", count=20, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)

screen ep10_snow_screen:
    tag ep10_snow_screen
    modal False
    add "particle_bf1"
    add "particle_bf2"
    add "particle_bf3"
    add "particle_bf4"
    add "particle_sf1"
    add "particle_sf2"
    add "particle_sf3"
    add "particle_mf1"
    add "particle_mf2"
    add "particle_mf3"

screen ep10_snow_queue_screen:
    tag ep10_snow_queue_screen
    modal False
    timer 6 action Hide("ep10_snow_queue_screen")
    add "particle_bf1"
    add "particle_bf2"
    add "particle_bf3"
    add "particle_bf4"
    add "particle_sf1"
    add "particle_sf2"
    add "particle_sf3"
    add "particle_mf1"
    add "particle_mf2"
    add "particle_mf3"

init python:
    def checkYbSpace(quote):
        q_list = quote.split(" ")
        for x in q_list:
            if len(x) > 20:
                return True
        return False
    def g_play_plop():
        renpy.play("sound_effects/plop.mp3","sfx1")

screen giftMsgScreen:
    tag giftMsgScreen
    modal True
    add "christmas_list_ol"

    key "mouseup_2" action (Function(ft_play_menu),Return())

    imagebutton:
        idle "ft_x_button_idle"
        hover "ft_x_button_hover"
        action (Function(ft_play_menu),Return())
        xalign 0.99
        yalign 0.02

    text "{color=e10d00}{size=%d}c{/size}{/color}hristmas gift list" % (120 * persistent.scale_factor) style "gift_header_style" xalign .886 yalign 0.00 yoffset -17 * persistent.scale_factor
    hbox:
        yalign 0.1
        xalign 0.97
        spacing 40 * persistent.scale_factor
        text "{color=e10d00}{size=%d}{size=%d}n{/size}aughty{/size}{/color}" % ((40 * persistent.scale_factor),(60 * persistent.scale_factor)) style "gift_header_style"
        text "{color=ffc27b}{size=%d}{size=%d}n{/size}ice{/size}{/color}" % ((40 * persistent.scale_factor),(60 * persistent.scale_factor)) style "gift_header_style"
        text "{color=fe9416}{size=%d}{size=%d}v{/size}ery nice{/size}{/color}" % ((40 * persistent.scale_factor),(60 * persistent.scale_factor)) style "gift_header_style"

    for i in range(0,len(ep11_gift_list)):
        hbox:
            yalign 0.218
            xalign 0.955
            spacing 35 * persistent.scale_factor
            if i > 3:
                yoffset (-2 + i * 113) * persistent.scale_factor
            else:
                yoffset (-1 + i * 113) * persistent.scale_factor
            for j in range(0,3):
                imagebutton:
                    if j == ep11_gift_list[i]:
                        idle "gift_btn_selected"
                        hover "gift_btn_selected"
                        action NullAction()
                    elif j == 0 or j < ep11_gift_list[i] or (j == 1 and ep11_gift_money > 0) or (j == 2 and ep11_gift_money + ep11_gift_list[i] > 2):
                        idle "gift_btn_idle"
                        hover "gift_btn_hover"
                        if ep11_gift_list[i] == 0 and j == 1:
                            action (Function(ft_play_coin),SetVariable("ep11_gift_money",ep11_gift_money-1),SetDict(ep11_gift_list, i, j))
                        elif ep11_gift_list[i] == 1 and j == 2:
                            action (Function(ft_play_coin),SetVariable("ep11_gift_money",ep11_gift_money-2),SetDict(ep11_gift_list, i, j))
                        elif ep11_gift_list[i] == 0 and j == 2:
                            action (Function(ft_play_coin),SetVariable("ep11_gift_money",ep11_gift_money-3),SetDict(ep11_gift_list, i, j))
                        elif ep11_gift_list[i] == 1 and j == 0:
                            action (Function(g_play_plop),SetVariable("ep11_gift_money",ep11_gift_money+1),SetDict(ep11_gift_list, i, j))
                        elif ep11_gift_list[i] == 2 and j == 1:
                            action (Function(ft_play_coin),SetVariable("ep11_gift_money",ep11_gift_money+2),SetDict(ep11_gift_list, i, j))
                        elif ep11_gift_list[i] == 2 and j == 0:
                            action (Function(g_play_plop),SetVariable("ep11_gift_money",ep11_gift_money+3),SetDict(ep11_gift_list, i, j))
                    else:
                        idle "gift_btn_idle"
                        hover "gift_btn_idle"
                        action NullAction()

    for i in range(0,len(ep11_gift_list)):
        hbox:
            yalign 0.218
            xalign 0.92
            spacing 85 * persistent.scale_factor
            yoffset i * 113 * persistent.scale_factor
            text "{color=bb433b}None{/color}" style "gift_text_style" xoffset -2 * persistent.scale_factor
            if ep11_gift_money > 0 or ep11_gift_list[i] > 0:
                text "{color=36ca2b}${/color}" style "gift_text_style"
            else:
                text "{color=dcdcdc}${/color}" style "gift_text_style"
            if ep11_gift_money + ep11_gift_list[i] > 2 or ep11_gift_list[i] == 2:
                text "{color=36ca2b}$$${/color}" style "gift_text_style" xoffset 30 * persistent.scale_factor
            else:
                text "{color=dcdcdc}$$${/color}" style "gift_text_style" xoffset 30 * persistent.scale_factor

    hbox:
        xalign 0.87
        yalign 0.89
        spacing 200 * persistent.scale_factor
        text "Pocket money:" style "gift_text2_style"
        text "Budget:" style "gift_text2_style"
    hbox:
        xalign 0.77
        yalign 0.89
        spacing 200 * persistent.scale_factor
        text "{color=36ca2b}$%d{/color}" % money style "gift_text2_style"

    hbox:
        xalign 0.93
        yalign 0.89
        spacing 200 * persistent.scale_factor
        text "{color=36ca2b}$%d{/color}" % ep11_gift_money style "gift_text2_style"
    hbox:
        xalign 0.95
        yalign 0.974
        spacing 150 * persistent.scale_factor
        if ep11_gift_opp > 0:
            text "{color=fdf0bc}Remaining opportunities to update the list: %d{/color}" % ep11_gift_opp style "gift_text2_style"
        else:
            text "{color=fdf0bc}Final opportunity to update the list{/color}" xoffset -60 yoffset -10 style "gift_text2_style"

    imagebutton:
        xalign 0.815
        yalign 0.91
        if ep11_gift_money > 0 and ((money < 10 and wallet_lvl == 3) or (money < 8 and wallet_lvl == 2) or (money < 6 and wallet_lvl == 1) or (money < 5 and wallet_lvl == 0)):
            auto "ft_cash_plus_%s"
            action (Function(ft_play_click),SetVariable("ep11_gift_money_tracker", ep11_gift_money_tracker-1),SetVariable("ep11_gift_money", ep11_gift_money-1),SetVariable("money",money+1))
        else:
            idle "ft_cash_plus_disabled"
            hover "ft_cash_plus_disabled"
            action NullAction()

    imagebutton:
        xalign 0.98
        yalign 0.91
        if money > 0 and ep11_gift_money_tracker < 18:
            auto "ft_cash_plus_%s"
            action (Function(ft_play_click),SetVariable("ep11_gift_money_tracker", ep11_gift_money_tracker+1),SetVariable("money", money-1),SetVariable("ep11_gift_money",ep11_gift_money+1))
        else:
            idle "ft_cash_plus_disabled"
            hover "ft_cash_plus_disabled"
            action NullAction()

style gift_header_style:
    color "#ffffff"
    font "fonts/Precious.ttf"
    size 50 * persistent.scale_factor
    outlines [(4, "#000000", 0, 0)]

style gift_text_style:
    color "#ffffff"
    font "fonts/candara.ttf"
    size 45 * persistent.scale_factor
    outlines [(2, "#000000", 0, 0)]

style gift_text2_style:
    color "#ffffff"
    font "fonts/candara.ttf"
    size 30 * persistent.scale_factor
    outlines [(2, "#000000", 0, 0)]

screen sauna_screen:
    tag sauna_screen
    modal False
    add "ep11_sauna_smoke_fx"

image ep11_sauna_smoke_fx:
    "ep11_sauna_smoke"
    zoom 1.0
    xalign 0.0 yalign 0.0
    linear 15.0 zoom 1.5
    linear 15.0 zoom 1.0
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

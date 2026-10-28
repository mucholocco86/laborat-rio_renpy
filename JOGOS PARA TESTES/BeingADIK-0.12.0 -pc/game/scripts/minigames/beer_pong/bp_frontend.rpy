screen bp_screen:
    tag bp_screen
    modal True

    if bp_player_turn:
        add "bp_%s_def_%d_%s" % (bp_cpu_name.lower(),max(1,bp_cpu_cups),bp_ep_suffix)
    else:
        add "bp_%s_off_%d_%s" % (bp_cpu_name.lower(),max(1,bp_cpu_cups),bp_ep_suffix)

    if bp_showing_img:
        if not bp_game_over:
            timer bp_delay repeat True action Function(bp_hide_image)
        add bp_img_name at bp_dissolve

    add "bp_bg_ap_boxes"
    add "bp_bg_cpu_box"
    vbox:
        xalign 0.025
        yalign 0.175
        spacing 5 * persistent.scale_factor
        xminimum 255 * persistent.scale_factor
        xmaximum 255 * persistent.scale_factor
        if bp_cpu_chance[0] > 60:
            text "Arc shot {color=fe9416}6 AP{/color} {color=1df400}%d%%{/color}" % bp_cpu_chance[0] style "bp_cpu_box_style"
        elif bp_cpu_chance[0] > 30:
            text "Arc shot {color=fe9416}6 AP{/color} {color=ffe059}%d%%{/color}" % bp_cpu_chance[0] style "bp_cpu_box_style"
        else:
            text "Arc shot {color=fe9416}6 AP{/color} {color=bb433b}%d%%{/color}" % bp_cpu_chance[0] style "bp_cpu_box_style"

        if bp_cpu_chance[1] > 60:
            text "Fastball {color=fe9416}0 AP{/color} {color=1df400}%d%%{/color}" % bp_cpu_chance[1] style "bp_cpu_box_style"
        elif bp_cpu_chance[1] > 30:
            text "Fastball {color=fe9416}0 AP{/color} {color=ffe059}%d%%{/color}" % bp_cpu_chance[1] style "bp_cpu_box_style"
        else:
            text "Fastball {color=fe9416}0 AP{/color} {color=bb433b}%d%%{/color}" % bp_cpu_chance[1] style "bp_cpu_box_style"

        if bp_cpu_chance[2] > 60:
            text "Bounce shot {color=fe9416}3 AP{/color} {color=1df400}%d%%{/color}" % bp_cpu_chance[2] style "bp_cpu_box_style"
        elif bp_cpu_chance[2] > 30:
            text "Bounce shot {color=fe9416}3 AP{/color} {color=ffe059}%d%%{/color}" % bp_cpu_chance[2] style "bp_cpu_box_style"
        else:
            text "Bounce shot {color=fe9416}3 AP{/color} {color=bb433b}%d%%{/color}" % bp_cpu_chance[2] style "bp_cpu_box_style"

    vbox:
        xalign 0.974
        yalign 0.175
        spacing 5 * persistent.scale_factor
        xminimum 255 * persistent.scale_factor
        xmaximum 255 * persistent.scale_factor
        if bp_player_chance[0] > 60:
            text "Arc shot {color=fe9416}6 AP{/color} {color=1df400}%d%%{/color}" % bp_player_chance[0] style "bp_cpu_box_style"
        elif bp_player_chance[0] > 30:
            text "Arc shot {color=fe9416}6 AP{/color} {color=ffe059}%d%%{/color}" % bp_player_chance[0] style "bp_cpu_box_style"
        else:
            text "Arc shot {color=fe9416}6 AP{/color} {color=bb433b}%d%%{/color}" % bp_player_chance[0] style "bp_cpu_box_style"

        if bp_player_chance[1] > 60:
            text "Fastball {color=fe9416}0 AP{/color} {color=1df400}%d%%{/color}" % bp_player_chance[1] style "bp_cpu_box_style"
        elif bp_player_chance[1] > 30:
            text "Fastball {color=fe9416}0 AP{/color} {color=ffe059}%d%%{/color}" % bp_player_chance[1] style "bp_cpu_box_style"
        else:
            text "Fastball {color=fe9416}0 AP{/color} {color=bb433b}%d%%{/color}" % bp_player_chance[1] style "bp_cpu_box_style"

        if bp_player_chance[2] > 60:
            text "Bounce shot {color=fe9416}3 AP{/color} {color=1df400}%d%%{/color}" % bp_player_chance[2] style "bp_cpu_box_style"
        elif bp_player_chance[2] > 30:
            text "Bounce shot {color=fe9416}3 AP{/color} {color=ffe059}%d%%{/color}" % bp_player_chance[2] style "bp_cpu_box_style"
        else:
            text "Bounce shot {color=fe9416}3 AP{/color} {color=bb433b}%d%%{/color}" % bp_player_chance[2] style "bp_cpu_box_style"



    text "%d" % bp_cpu_ap style "bp_ap_style" xalign 0.046 yalign 0.026
    text "{size=+%d}{color=ffffff}/{/color}{/size}" % (20 * persistent.scale_factor) style "bp_ap_style" xalign 0.06 yalign 0.02
    text "10" style "bp_ap_style" xalign 0.072 yalign 0.043
    text "{size=+%d}AP{/size}" % (25 * persistent.scale_factor) style "bp_ap_style" xalign 0.1 yalign 0.02
    text "{color=ffe059}%s{/color}" % bp_cpu_name style "bp_ap_style" xalign 0.027 yalign 0.08
    text "{color=ffffff}%d cups{/color}" % bp_cpu_cups style "bp_ap_style" xalign 0.092 yalign 0.08

    text "%d" % bp_player_ap style "bp_ap_style" xalign 0.877 yalign 0.026
    text "{size=+%d}{color=ffffff}/{/color}{/size}" % (20 * persistent.scale_factor) style "bp_ap_style" xalign 0.892 yalign 0.02
    text "10" style "bp_ap_style" xalign 0.909 yalign 0.043
    text "{size=+%d}AP{/size}" % (25 * persistent.scale_factor) style "bp_ap_style" xalign 0.95 yalign 0.02
    text "{color=ffe059}You{/color}" style "bp_ap_style" xalign 0.88 yalign 0.08
    text "{color=ffffff}%d cups{/color}" % bp_player_cups style "bp_ap_style" xalign 0.947 yalign 0.08


    if bp_showing_img:
        vbox:
            xalign .98
            yalign 0.95
            xminimum 500 * persistent.scale_factor
            xmaximum 500 * persistent.scale_factor
            text "%s" % bp_action_msg style "bp_action_msg_style"


    if not bp_showing_img:
        if bp_player_turn:
            vbox:
                xalign 1.0
                yalign 0.75
                spacing 40 * persistent.scale_factor
                imagebutton:
                    idle "bp_choice_box_idle"
                    if bp_player_ap >= 6:
                        hover "bp_choice_box_hover"
                        action Function(bp_shot,bp_player_turn,0)
                    else:
                        hover "bp_choice_box_idle"
                        action NullAction()
                imagebutton:
                    idle "bp_choice_box_idle"
                    hover "bp_choice_box_hover"
                    action Function(bp_shot,bp_player_turn,1)
                imagebutton:
                    idle "bp_choice_box_idle"
                    if bp_player_ap >= 3:
                        hover "bp_choice_box_hover"
                        action Function(bp_shot,bp_player_turn,2)
                    else:
                        hover "bp_choice_box_idle"
                        action NullAction()

            vbox:
                xalign 0.99
                yalign 0.74
                spacing 60 * persistent.scale_factor
                if bp_player_ap >= 6:
                    if bp_player_chance[0] > 60:
                        text "Arc shot {color=#fe9416}6 AP{/color}\n{color=1df400}%d%%{/color}" % bp_player_chance[0] style "bp_choice_style"
                    elif bp_player_chance[0] > 30:
                        text "Arc shot {color=#fe9416}6 AP{/color}\n{color=ffe059}%d%%{/color}" % bp_player_chance[0] style "bp_choice_style"
                    else:
                        text "Arc shot {color=#fe9416}6 AP{/color}\n{color=bb433b}%d%%{/color}" % bp_player_chance[0] style "bp_choice_style"
                else:
                    text "{color=c4c4c4}Arc shot 6 AP\n%d%%{/color}" % bp_player_chance[0] style "bp_choice_style"

                if bp_player_chance[1] > 60:
                    text "Fastball {color=#fe9416}0 AP{/color}\n{color=1df400}%d%%{/color}" % bp_player_chance[1] style "bp_choice_style"
                elif bp_player_chance[1] > 30:
                    text "Fastball {color=#fe9416}0 AP{/color}\n{color=ffe059}%d%%{/color}" % bp_player_chance[1] style "bp_choice_style"
                else:
                    text "Fastball {color=#fe9416}0 AP{/color}\n{color=bb433b}%d%%{/color}" % bp_player_chance[1] style "bp_choice_style"

                if bp_player_ap >= 3:
                    if bp_player_chance[2] > 60:
                        text "Bounce shot {color=#fe9416}3 AP{/color}\n{color=1df400}%d%%{/color}" % bp_player_chance[2] style "bp_choice_style"
                    elif bp_player_chance[2] > 30:
                        text "Bounce shot {color=#fe9416}3 AP{/color}\n{color=ffe059}%d%%{/color}" % bp_player_chance[2] style "bp_choice_style"
                    else:
                        text "Bounce shot {color=#fe9416}3 AP{/color}\n{color=bb433b}%d%%{/color}" % bp_player_chance[2] style "bp_choice_style"
                else:
                    text "{color=c4c4c4}Bounce shot 3 AP\n%d%%{/color}" % bp_player_chance[2] style "bp_choice_style"

        else:
            vbox:
                xalign 1.0
                yalign 0.75
                spacing 40 * persistent.scale_factor
                imagebutton:
                    idle "bp_choice_box_idle"
                    hover "bp_choice_box_hover"
                    action Function(bp_def,True,1)
                imagebutton:
                    idle "bp_choice_box_idle"
                    hover "bp_choice_box_hover"
                    action Function(bp_def,True,2)
                imagebutton:
                    idle "bp_choice_box_idle"
                    hover "bp_choice_box_hover"
                    action Function(bp_def,True,3)
            vbox:
                xalign 0.97
                yalign 0.735
                spacing 76 * persistent.scale_factor
                text "Tease ({color=#bb433b}5-10%%{/color})\n{size=-%d}{color=bb433b}Lower their hit chance{/color}{/size}" % (15 * persistent.scale_factor) style "bp_choice_style"
                text "Focus ({color=#1df400}5-10%%{/color})\n{size=-%d}{color=ffe059}Increase your hit chance{/color}{/size}" % (15 * persistent.scale_factor) style "bp_choice_style"
                text "Rest\n{size=-%d}{color=fe9416}Recover +3 AP{/color}{/size}" % (15 * persistent.scale_factor) style "bp_choice_style"

screen bp_say_screen():
    tag bp_say_screen
    modal True

    if bp_force_delay:
        timer 1 repeat False action SetVariable("bp_force_delay", False)
    else:
        text "%s" % bp_who_list[bp_dlg] style "say_label_bp_style" xalign 0.202 yalign 0.87
        hbox:
            yalign 0.945 xminimum 950 * persistent.scale_factor xmaximum 950 * persistent.scale_factor yminimum 150 * persistent.scale_factor ymaximum 150 * persistent.scale_factor
            text "%s" % bp_dlg_list[bp_dlg] style "say_dialogue_bp_style"

        imagebutton:
            idle "bp_big_invis"
            hover "bp_big_invis"
            if len(bp_who_list) > bp_dlg + 1:
                action SetVariable("bp_dlg", bp_dlg + 1)
            else:
                action Hide("bp_say_screen")

screen bp_tut_screen():
    tag bp_tut_screen
    modal True

    add "bp_mc_hit_6"
    add "bp_tut_box"

    vbox:
        xalign 0.5
        xminimum 983 * persistent.scale_factor
        xmaximum 983 * persistent.scale_factor
        yminimum 245 * persistent.scale_factor
        ymaximum 245 * persistent.scale_factor
        if bp_dlg == 0:
            yalign 0.95
            text "{size=+%d}{color=ffe059}Beer Pong{/color}{/size}\nIn the Beer Pong mini-game, your goal is to hit your opponent's cups with a ping pong ball. If you hit, they will be forced to drink and even strip.\nBut beware: the same applies to you if they manage to hit your cups." % (20 * persistent.scale_factor) style "bp_tut_style"
        elif bp_dlg == 1:
            yalign 0.95
            text "{size=+%d}{color=ffe059}Shooting{/color}{/size}\nWhen it's your turn to throw the ball, choose between three types of shots.\nThe percentage shows the chance the shot has of hitting.\nSome shots cost {color=fe9416}action points{/color} ({color=fe9416}AP{/color})." % (20 * persistent.scale_factor) style "bp_tut_style"
        elif bp_dlg == 2:
            yalign 0.95
            text "{color=ffe059}Arc shots{/color} have a {color=1df400}high chance{/color} of hitting, but they cost a lot of {color=fe9416}AP{/color}.\n{color=ffe059}Fastballs{/color} don't cost {color=fe9416}AP{/color}, but they have a {color=bb433b}low chance{/color} of hitting.\n{color=ffe059}Bounce shots{/color} cost a medium amount of {color=fe9416}AP{/color} to use. If you hit a cup with a bounce shot, it counts as two cups. But your opponent has a chance to swat away your ball when you try the bounce shot." style "bp_tut_style"
        elif bp_dlg == 3:
            yalign 0.97
            text "You can view your and your opponent's hit chances, current {color=fe9416}AP{/color}, and {color=fe9416}AP{/color} costs at any time in the upper left and upper right corners.\nYou can also check how many cups you and your opponent have left.\nEvery two cups that you hit will cause your opponent to strip." style "bp_tut_style"
        elif bp_dlg == 4:
            yalign 0.93
            text "{size=+%d}{color=ffe059}Defending{/color}{/size}\nWhen it's your opponent's turn - and before they shoot their shot - you get to choose an action to affect the game or prepare yourself for your future shots.\nThese are strategic actions that will have a big impact on winning or losing." % (20 * persistent.scale_factor) style "bp_tut_style"
        elif bp_dlg == 5:
            yalign 0.97
            text "You can {color=ffe059}tease{/color} your opponent and lower their {color=bb433b}hit chances{/color} by {color=bb433b}5-10%{/color}.\nYou can {color=ffe059}focus{/color} and increase your own {color=1df400}hit chances{/color} by {color=1df400}5-10%{/color}.\nOr you can {color=ffe059}rest{/color} and recover up to {color=fe9416}3 AP{/color}.\nChoose wisely." style "bp_tut_style"
        elif bp_dlg == 6:
            yalign 0.97
            text "After you have chosen your {color=ffe059}defensive action{/color}, your opponent will {color=ffe059}shoot{/color} and proceed to choose their {color=ffe059}defensive action{/color}.\nAfter that, the cycle repeats until the game ends.\nThe game ends when you or your opponent have {color=bb433b}no cups left{/color}." style "bp_tut_style"

    if bp_dlg == 3:
        add "bp_bg_ap_boxes"
        add "bp_bg_cpu_box"
        vbox:
            xalign 0.025
            yalign 0.175
            spacing 5 * persistent.scale_factor
            xminimum 246 * persistent.scale_factor
            xmaximum 246 * persistent.scale_factor
            text "Arc shot {color=fe9416}6 AP{/color} {color=1df400}62%{/color}" style "bp_cpu_box_style"
            text "Fastball {color=fe9416}0 AP{/color} {color=bb433b}15%{/color}" style "bp_cpu_box_style"
            text "Bounce shot {color=fe9416}3 AP{/color} {color=ffe059}33%{/color}" style "bp_cpu_box_style"


        vbox:
            xalign 0.970
            yalign 0.175
            spacing 5 * persistent.scale_factor
            xminimum 246 * persistent.scale_factor
            xmaximum 246 * persistent.scale_factor
            text "Arc shot {color=fe9416}6 AP{/color} {color=1df400}66%{/color}" style "bp_cpu_box_style"
            text "Fastball {color=fe9416}0 AP{/color} {color=bb433b}20%{/color}" style "bp_cpu_box_style"
            text "Bounce shot {color=fe9416}3 AP{/color} {color=ffe059}45%{/color}" style "bp_cpu_box_style"




        text "7" style "bp_ap_style" xalign 0.046 yalign 0.026
        text "{size=+%d}{color=ffffff}/{/color}{/size}" % (20 * persistent.scale_factor) style "bp_ap_style" xalign 0.06 yalign 0.02
        text "10" style "bp_ap_style" xalign 0.072 yalign 0.043
        text "{size=+%d}AP{/size}" % (25 * persistent.scale_factor) style "bp_ap_style" xalign 0.1 yalign 0.02
        text "{color=ffe059}CPU{/color}" style "bp_ap_style" xalign 0.027 yalign 0.08
        text "{color=ffffff}5 cups{/color}" style "bp_ap_style" xalign 0.092 yalign 0.08

        text "9" style "bp_ap_style" xalign 0.877 yalign 0.026
        text "{size=+%d}{color=ffffff}/{/color}{/size}" % (20 * persistent.scale_factor) style "bp_ap_style" xalign 0.892 yalign 0.02
        text "10" style "bp_ap_style" xalign 0.909 yalign 0.043
        text "{size=+%d}AP{/size}" % (25 * persistent.scale_factor) style "bp_ap_style" xalign 0.95 yalign 0.02
        text "{color=ffe059}You{/color}" style "bp_ap_style" xalign 0.88 yalign 0.08
        text "{color=ffffff}6 cups{/color}" style "bp_ap_style" xalign 0.947 yalign 0.08
    elif bp_dlg == 1 or bp_dlg == 2:
        vbox:
            xalign 1.0
            yalign 0.75
            spacing 40 * persistent.scale_factor
            imagebutton:
                idle "bp_choice_box_idle"
                hover "bp_choice_box_idle"
                action NullAction()
            imagebutton:
                idle "bp_choice_box_idle"
                hover "bp_choice_box_idle"
                action NullAction()
            imagebutton:
                idle "bp_choice_box_idle"
                hover "bp_choice_box_idle"
                action NullAction()

        vbox:
            xalign 0.99
            yalign 0.74
            spacing 60 * persistent.scale_factor
            text "Arc shot {color=#fe9416}6 AP{/color}\n{color=1df400}66%{/color}" style "bp_choice_style"
            text "Fastball {color=#fe9416}0 AP{/color}\n{color=bb433b}20%{/color}" style "bp_choice_style"
            text "Bounce shot {color=#fe9416}3 AP{/color}\n{color=ffe059}45%{/color}" style "bp_choice_style"
    elif bp_dlg == 4 or bp_dlg == 5:
        vbox:
            xalign 1.0
            yalign 0.75
            spacing 40 * persistent.scale_factor
            imagebutton:
                idle "bp_choice_box_idle"
                hover "bp_choice_box_idle"
                action NullAction()
            imagebutton:
                idle "bp_choice_box_idle"
                hover "bp_choice_box_idle"
                action NullAction()
            imagebutton:
                idle "bp_choice_box_idle"
                hover "bp_choice_box_idle"
                action NullAction()

        vbox:
            xalign 0.97
            yalign 0.735
            spacing 76 * persistent.scale_factor
            text "Tease ({color=#bb433b}5-10%%{/color})\n{size=%d}{color=bb433b}Lower their hit chance{/color}{/size}" % (-15 * persistent.scale_factor) style "bp_choice_style"
            text "Focus ({color=#1df400}5-10%%{/color})\n{size=%d}{color=ffe059}Increase your hit chance{/color}{/size}" % (-15 * persistent.scale_factor) style "bp_choice_style"
            text "Rest\n{size=-%d}{color=fe9416}Recover +3 AP{/color}{/size}" % (15 * persistent.scale_factor) style "bp_choice_style"


    imagebutton:
        idle "bp_big_invis"
        hover "bp_big_invis"
        if bp_dlg + 1 < 7:
            action SetVariable("bp_dlg", bp_dlg + 1)
        else:
            action (Hide("bp_tut_screen"), Jump(bp_jump_label))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen brawler_skill_screen:
    tag brawler_skill_screen
    modal True

    add "bn_skill_bg"
    add "bn_scroll_lines" at bn_line_transform
    add "bn_skill_ol"

    text "Stats" style "brawler_skill_header_style" xalign 0.122 yalign 0.158
    text "Special attack" style "brawler_skill_header_style" xalign 0.722 yalign 0.158

    text "{size=-%d}Available Skill Points:{/size}" % (40 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.27 yalign 0.205
    text "{color=ffffff}{size=-%d}%d{/size}{/color}" % ((40 * persistent.scale_factor),bn_skill_points) style "brawler_skill_header_style" xalign 0.40 yalign 0.205

    vbox:
        xalign 0.16
        yalign 0.415
        spacing 20 * persistent.scale_factor
        xminimum 583 * persistent.scale_factor
        xmaximum 583 * persistent.scale_factor
        hbox:
            text "Power" style "brawler_skill_text_style"
        hbox:
            text "Stamina" style "brawler_skill_text_style"
        hbox:
            text "Speed" style "brawler_skill_text_style"
        hbox:
            text "Block" style "brawler_skill_text_style"
        hbox:
            text "Counter" style "brawler_skill_text_style"
        hbox:
            text "Rage" style "brawler_skill_text_style"

    vbox:
        xalign 0.313
        yalign 0.422
        spacing 47 * persistent.scale_factor
        xminimum 583 * persistent.scale_factor
        xmaximum 583 * persistent.scale_factor
        hbox:
            yalign 0.5
            spacing -10 * persistent.scale_factor
            if bonusPointsSports == 12 or bn_reward_available_list[3] == 0:
                imagebutton:
                    idle "bn_skill_bar_default"
                    hover "bn_skill_bar_default"
                    hovered SetScreenVariable("bn_tt",0)
                    action Function(bn_play_failed_click,0,0,0)
                for i in range(1,bn_skill_alloc[0]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",0)
                        action Function(bn_set_skill,0,i+1)
            else:
                for i in range(0,bn_skill_alloc[0]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",0)
                        action Function(bn_set_skill,0,i+1)
            for i in range(bn_skill_alloc[0],min(bn_skill_max_level,5)):
                imagebutton:
                    idle "bn_skill_bar_empty"
                    hover "bn_skill_bar_empty"
                    hovered SetScreenVariable("bn_tt",0)
                    action Function(bn_set_skill,0,i+1)
            for i in range(bn_skill_max_level,5):
                add "bn_skill_bar_locked"
        hbox:
            yalign 0.5
            spacing -10 * persistent.scale_factor
            imagebutton:
                idle "bn_skill_bar_default"
                hover "bn_skill_bar_default"
                hovered SetScreenVariable("bn_tt",1)
                action Function(bn_play_failed_click,0,0,0)
            imagebutton:
                idle "bn_skill_bar_default"
                hover "bn_skill_bar_default"
                hovered SetScreenVariable("bn_tt",1)
                action Function(bn_play_failed_click,0,0,0)
            for i in range(2,bn_skill_alloc[1]):
                imagebutton:
                    idle "bn_skill_bar_full"
                    hover "bn_skill_bar_full"
                    hovered SetScreenVariable("bn_tt",1)
                    action Function(bn_set_skill,1,i+1)
            for i in range(bn_skill_alloc[1],min(bn_skill_max_level,5)):
                imagebutton:
                    idle "bn_skill_bar_empty"
                    hover "bn_skill_bar_empty"
                    hovered SetScreenVariable("bn_tt",1)
                    action Function(bn_set_skill,1,i+1)
            for i in range(bn_skill_max_level,5):
                add "bn_skill_bar_locked"
        hbox:
            yalign 0.5
            spacing -10 * persistent.scale_factor
            if bonusPointsSports > 8 or bn_reward_available_list[3] < 2:
                imagebutton:
                    idle "bn_skill_bar_default"
                    hover "bn_skill_bar_default"
                    hovered SetScreenVariable("bn_tt",2)
                    action Function(bn_play_failed_click,0,0,0)
                for i in range(1,bn_skill_alloc[2]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",2)
                        action Function(bn_set_skill,2,i+1)
            else:
                for i in range(0,bn_skill_alloc[2]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",2)
                        action Function(bn_set_skill,2,i+1)
            for i in range(bn_skill_alloc[2],min(bn_skill_max_level,5)):
                imagebutton:
                    idle "bn_skill_bar_empty"
                    hover "bn_skill_bar_empty"
                    hovered SetScreenVariable("bn_tt",2)
                    action Function(bn_set_skill,2,i+1)
            for i in range(bn_skill_max_level,5):
                add "bn_skill_bar_locked"
        hbox:
            yalign 0.5
            spacing -10 * persistent.scale_factor
            if bonusPointsSports > 5 or bn_reward_available_list[3] < 3:
                imagebutton:
                    idle "bn_skill_bar_default"
                    hover "bn_skill_bar_default"
                    hovered SetScreenVariable("bn_tt",3)
                    action Function(bn_play_failed_click,0,0,0)
                for i in range(1,bn_skill_alloc[3]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",3)
                        action Function(bn_set_skill,3,i+1)
            else:
                for i in range(0,bn_skill_alloc[3]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",3)
                        action Function(bn_set_skill,3,i+1)
            for i in range(bn_skill_alloc[3],min(bn_skill_max_level,5)):
                imagebutton:
                    idle "bn_skill_bar_empty"
                    hover "bn_skill_bar_empty"
                    hovered SetScreenVariable("bn_tt",3)
                    action Function(bn_set_skill,3,i+1)
            for i in range(bn_skill_max_level,5):
                add "bn_skill_bar_locked"
        hbox:
            yalign 0.5
            spacing -10 * persistent.scale_factor
            if bonusPointsSports > 2 or bn_reward_available_list[3] < 4:
                imagebutton:
                    idle "bn_skill_bar_default"
                    hover "bn_skill_bar_default"
                    hovered SetScreenVariable("bn_tt",4)
                    action Function(bn_play_failed_click,0,0,0)
                for i in range(1,bn_skill_alloc[4]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",4)
                        action Function(bn_set_skill,4,i+1)
            else:
                for i in range(0,bn_skill_alloc[4]):
                    imagebutton:
                        idle "bn_skill_bar_full"
                        hover "bn_skill_bar_full"
                        hovered SetScreenVariable("bn_tt",4)
                        action Function(bn_set_skill,4,i+1)
            for i in range(bn_skill_alloc[4],min(bn_skill_max_level,5)):
                imagebutton:
                    idle "bn_skill_bar_empty"
                    hover "bn_skill_bar_empty"
                    hovered SetScreenVariable("bn_tt",4)
                    action Function(bn_set_skill,4,i+1)
            for i in range(bn_skill_max_level,5):
                add "bn_skill_bar_locked"
        hbox:
            yalign 0.5
            spacing -10 * persistent.scale_factor
            for i in range(0,bn_skill_alloc[5]):
                imagebutton:
                    idle "bn_skill_bar_full"
                    hover "bn_skill_bar_full"
                    hovered SetScreenVariable("bn_tt",5)
                    action Function(bn_set_skill,5,i+1)
            for i in range(bn_skill_alloc[5],min(bn_skill_max_level,5)):
                imagebutton:
                    idle "bn_skill_bar_empty"
                    hover "bn_skill_bar_empty"
                    hovered SetScreenVariable("bn_tt",5)
                    action Function(bn_set_skill,5,i+1)
            for i in range(bn_skill_max_level,5):
                add "bn_skill_bar_locked"


    key "mouseup_2" action (Function(bn_play_click,0,0,0),Jump("brawler_skill_state_set_label"))
    textbutton "X" action (Function(bn_play_click,0,0,0),Jump("brawler_skill_state_set_label")) text_style "brawler_skill_x_style" xalign 0.98 yalign 0.02

    textbutton "Reset Skill Points" action Function(bn_play_reset,0,0,0),Function(bn_reset_skill_points) text_style "brawler_skill_reset_style" xalign 0.1245 yalign 0.7

    default bn_tt = -1
    default bn_tooltips = ["{color=ffe059}Power{/color} - Determines how much damage you deal.","{color=ffe059}Stamina{/color} - Increases the number of stamina bars by one per skill point.","{color=ffe059}Speed{/color} - Increases the time for attacking and defending.","{color=ffe059}Block{/color} - Reduces the damage taken when blocking an attack.","{color=ffe059}Counter{/color} - Increases your chance to counter-attack when dodging.","{color=ffe059}Rage{/color} - Increases the Rage start value by x5 per skill point."]
    if bn_tt > -1:
        vbox:
            xalign 0.19
            yalign 0.75
            xmaximum 800 * persistent.scale_factor
            xminimum 800 * persistent.scale_factor
            text "%s" % bn_tooltips[bn_tt] style "brawler_skill_tt_style"

    if bn_special == 0 and bn_specials_unlocked[0]:
        add "brawler_sel_arr" xalign 0.5 yalign 0.315
    elif bn_special == 1 and bn_specials_unlocked[1]:
        add "brawler_sel_arr" xalign 0.5 yalign 0.5
    elif bn_special == 2 and bn_specials_unlocked[2]:
        add "brawler_sel_arr" xalign 0.5 yalign 0.685

    vbox:
        xalign 0.95
        yalign 0.5
        spacing 50 * persistent.scale_factor
        xoffset 6 * persistent.scale_factor
        hbox:
            spacing 20 * persistent.scale_factor
            if bn_specials_unlocked[0]:
                imagebutton:
                    if bn_special == 0:
                        idle "bn_flurry_hover"
                        hover "bn_flurry_hover"
                    else:
                        idle "bn_flurry_idle"
                        hover "bn_flurry_hover"
                    action Function(bn_play_click,0,0,0),SetVariable("bn_special",0)
                vbox:
                    xminimum 690 * persistent.scale_factor
                    yalign 0.5
                    text "{size=-%d}Flurry{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style"
                    text "{size=-%d}Deals moderate damage. Completely drains opponent's Stamina.{/size}" % (20 * persistent.scale_factor) style "brawler_skill_text_style"
            else:
                imagebutton:
                    idle "bn_unknown"
                    hover "bn_unknown"
                    action Function(bn_play_failed_click,0,0,0)
                vbox:
                    xminimum 690 * persistent.scale_factor
                    yalign 0.5
                    text "{size=-%d}Unknown{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style"
                    text "{size=-%d}Progress further in Brawler to unlock.{/size}" % (20 * persistent.scale_factor) style "brawler_skill_text_style"
        hbox:
            spacing 20 * persistent.scale_factor
            if bn_specials_unlocked[1]:
                imagebutton:
                    if bn_special == 1:
                        idle "bn_cripple_hover"
                        hover "bn_cripple_hover"
                    else:
                        idle "bn_cripple_idle"
                        hover "bn_cripple_hover"
                    action Function(bn_play_click,0,0,0),SetVariable("bn_special",1)
                vbox:
                    xminimum 690 * persistent.scale_factor
                    yalign 0.5
                    text "{size=-%d}Crippling leg kick{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style"
                    text "{size=-%d}Deals moderate damage. Stuns opponent for one turn.{/size}" % (20 * persistent.scale_factor) style "brawler_skill_text_style"
            else:
                imagebutton:
                    idle "bn_unknown"
                    hover "bn_unknown"
                    action Function(bn_play_failed_click,0,0,0)
                vbox:
                    xminimum 690 * persistent.scale_factor
                    yalign 0.5
                    text "{size=-%d}Unknown{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style"
                    text "{size=-%d}Progress further in Brawler to unlock.{/size}" % (20 * persistent.scale_factor) style "brawler_skill_text_style"
        hbox:
            spacing 20 * persistent.scale_factor
            if bn_specials_unlocked[2]:
                imagebutton:
                    if bn_special == 2:
                        idle "bn_highkick_hover"
                        hover "bn_highkick_hover"
                    else:
                        idle "bn_highkick_idle"
                        hover "bn_highkick_hover"
                    action Function(bn_play_click,0,0,0),SetVariable("bn_special",2)
                vbox:
                    xminimum 690 * persistent.scale_factor
                    yalign 0.5
                    text "{size=-%d}High kick combo{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style"
                    text "{size=-%d}Deals great damage. The opponent's next counter-attack will fail.{/size}" % (20 * persistent.scale_factor) style "brawler_skill_text_style"
            else:
                imagebutton:
                    idle "bn_unknown"
                    hover "bn_unknown"
                    action Function(bn_play_failed_click,0,0,0)
                vbox:
                    yalign 0.5
                    xminimum 690 * persistent.scale_factor
                    text "{size=-%d}Unknown{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style"
                    text "{size=-%d}Progress further in Brawler to unlock.{/size}" % (20 * persistent.scale_factor) style "brawler_skill_text_style"

label brawler_skill_state_set_label:
show screen brawler_menu_screen
hide screen brawler_skill_screen
pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

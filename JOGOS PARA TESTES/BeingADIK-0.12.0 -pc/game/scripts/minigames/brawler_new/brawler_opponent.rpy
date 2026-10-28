screen brawler_opponent_screen:
    tag brawler_opponent_screen
    modal True

    add "bn_skill_bg"
    add "bn_scroll_lines" at bn_line_transform
    add "bn_opponent_ol"

    key "mouseup_2" action (Function(bn_play_click,0,0,0),Show("brawler_menu_screen"),Hide("brawler_opponent_screen"))
    textbutton "X" action (Function(bn_play_click,0,0,0),Show("brawler_menu_screen"),Hide("brawler_opponent_screen")) text_style "brawler_skill_x_style" xalign 0.98 yalign 0.02

    text "Choose your opponent" style "brawler_skill_header_style" xalign 0.13 yalign 0.04

    default bn_hover = -1
    hbox:
        spacing 15 * persistent.scale_factor
        xalign 0.5
        yalign 0.83
        yoffset -1 * persistent.scale_factor
        if bn_hover == 0:
            add "bn_opponent_selector" xoffset -668 * persistent.scale_factor
        elif bn_hover == 1:
            add "bn_opponent_selector" xoffset -334 * persistent.scale_factor
        elif bn_hover == 2:
            add "bn_opponent_selector"
        elif bn_hover == 3:
            add "bn_opponent_selector" xoffset 334 * persistent.scale_factor
        elif bn_hover == 4:
            add "bn_opponent_selector" xoffset 668 * persistent.scale_factor

    hbox:
        spacing 15 * persistent.scale_factor
        xalign 0.5
        yalign 0.65
        yoffset -1 * persistent.scale_factor

        for i in range(0,len(bn_opponent_list)):
            vbox:
                xminimum 319 * persistent.scale_factor
                xmaximum 319 * persistent.scale_factor
                imagebutton:
                    idle "bn_opponent_" + bn_opponent_list[i][0].lower() + "_idle"
                    hover "bn_opponent_" + bn_opponent_list[i][0].lower() + "_hover"
                    hovered SetScreenVariable("bn_hover", i), Function(bn_play_hover,0,0,0)
                    action (Function(bn_play_click,0,0,0),Hide("brawler_opponent_screen"),Jump("brawler_story_"+bn_opponent_list[i][0].lower()+"_label"))
                spacing 10 * persistent.scale_factor
                vpgrid:
                    xminimum 319 * persistent.scale_factor
                    xmaximum 319 * persistent.scale_factor
                    xoffset 12 * persistent.scale_factor
                    yoffset 10 * persistent.scale_factor
                    cols 2
                    text "Difficulty" style "brawler_opp_style"
                    if bn_opponent_list[i][1] > 8:
                        text "{color=bb433b}%d{/color}" % bn_opponent_list[i][1] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    elif bn_opponent_list[i][1] > 4:
                        text "{color=ffe059}%d{/color}" % bn_opponent_list[i][1] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    else:
                        text "{color=1df400}%d{/color}" % bn_opponent_list[i][1] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    text "Power" style "brawler_opp_style"
                    if bn_opponent_list[i][2] > 8:
                        text "{color=bb433b}%d{/color}" % bn_opponent_list[i][2] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    elif bn_opponent_list[i][2] > 4:
                        text "{color=ffe059}%d{/color}" % bn_opponent_list[i][2] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    else:
                        text "{color=1df400}%d{/color}" % bn_opponent_list[i][2] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    text "Health" style "brawler_opp_style"
                    if bn_opponent_list[i][3] > 150:
                        text "{color=bb433b}%d{/color}" % bn_opponent_list[i][3] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    elif bn_opponent_list[i][3] > 100:
                        text "{color=ffe059}%d{/color}" % bn_opponent_list[i][3] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    else:
                        text "{color=1df400}%d{/color}" % bn_opponent_list[i][3] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                    text "Stamina" style "brawler_opp_style"
                    hbox:
                        yalign 0.6
                        spacing -8 * persistent.scale_factor
                        for j in range(0,bn_opponent_list[i][4]):
                            add "bn_stamina_cpu"
                vbox:
                    xalign 0.5
                    yoffset 30 * persistent.scale_factor
                    text "%s" % bn_opponent_list[i][5] style "brawler_opp_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

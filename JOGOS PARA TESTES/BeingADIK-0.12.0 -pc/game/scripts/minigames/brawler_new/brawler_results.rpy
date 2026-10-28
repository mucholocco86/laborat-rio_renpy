screen brawler_result_screen:
    tag brawler_result_screen
    modal True
    add "brawler_results_bg"
    add "bn_scroll_lines" at bn_line_transform
    add "brawler_menu_ol"

    default bn_item_hovered = -1
    default bn_show_quit_message = False

    text "Results" style "brawler_skill_header_style" xalign 0.395 yalign 0.04
    if bn_quit_message != "":
        key "mouseup_2" action (Function(bn_play_failed_click,0,0,0),SetScreenVariable("bn_show_quit_message",True))
    else:
        key "mouseup_2" action (Function(bn_play_click,0,0,0),Jump("app_new_brawler_quit_label"))

    if bn_item_hovered == 0:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.26
    elif bn_item_hovered == 1:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.385
    elif bn_item_hovered == 2:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.52
    elif bn_item_hovered == 3:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.653
    elif bn_item_hovered == 4:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.78
    vbox:
        xalign 0.065
        yalign 0.55
        spacing 0 * persistent.scale_factor
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 0), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action (Function(bn_play_click,0,0,0),Function(bn_init_opponents),Show("brawler_opponent_screen"),Hide("brawler_result_screen"))
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 1), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action (Function(bn_play_click,0,0,0),Show("brawler_skill_screen"),Hide("brawler_result_screen"))
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 2), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action (Function(bn_play_click,0,0,0),Show("brawler_tutorial_screen"),Hide("brawler_result_screen"))
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 3), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action ShowMenu('save')
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 4), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            if bn_quit_message != "":
                action (Function(bn_play_failed_click,0,0,0),SetScreenVariable("bn_show_quit_message",True))
            else:
                action (Function(bn_play_click,0,0,0),Jump("app_new_brawler_quit_label"))

    if bn_show_quit_message:
        timer 3 repeat False action SetScreenVariable("bn_show_quit_message",False)
        imagebutton at show_hide_dissolve:
            idle "bg_toprightmsg"
            xalign 0.9825
            yalign -0.01
            action NullAction()
        text "[bn_quit_message]" style "score_new_style" at show_hide_dissolve:
            xalign 0.97
            yalign 0.01

    vbox:
        xalign 0.118
        yalign 0.54
        spacing 65 * persistent.scale_factor + (persistent.scale_factor-1)*10
        if bn_item_hovered == 0:
            text "Fight" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Fight" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 1:
            text "Skills" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Skills" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 2:
            text "Tutorial" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Tutorial" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 3:
            text "Save" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Save" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 4:
            text "Quit" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Quit" style "brawler_menu_text_style" xalign 0.5

    if bn_playlist:
        textbutton "{color=ffe059}Music Playlist:{/color} Brawler Playlist" action (Function(bn_play_click,0,0,0),SetVariable("bn_playlist",False), Function(bn_play_song,False)) xminimum 500 * persistent.scale_factor xmaximum 500 * persistent.scale_factor xalign 0.049 text_align 0.5 yalign 0.89 text_style "brawler_menu_diff_style"
    else:
        textbutton "{color=ffe059}Music Playlist:{/color} Favorites Playlist" action (Function(bn_play_click,0,0,0),SetVariable("bn_playlist",True),Function(bn_play_song,True)) xminimum 500 * persistent.scale_factor xmaximum 500 * persistent.scale_factor text_align 0.5 xalign 0.049 yalign 0.89 text_style "brawler_menu_diff_style"

    default bn_change_diff = False
    if bn_hard_difficulty and not bn_change_diff:
        textbutton "{color=870600}Hard Difficulty{/color} {color=#ffffff}|{/color} Lower Difficulty" action (Function(bn_play_reset,0,0,0),SetScreenVariable("bn_change_diff",True)) xalign 0.047 yalign 0.96 text_style "brawler_menu_diff_style"
    elif bn_hard_difficulty and bn_change_diff:
        timer 3 repeat False action SetScreenVariable("bn_change_diff",False)
        textbutton "{size=-%d}Click to permanently lower the difficulty{/size}" % (3 * persistent.scale_factor) action (Function(bn_play_reset,0,0,0),Function(bn_lower_difficulty)) xalign 0.017 yalign 0.96 text_style "brawler_menu_diff_style"
    else:
        textbutton "{color=b7b7b7}Normal Difficulty{/color}" action Function(bn_play_failed_click,0,0,0) xalign 0.11 yalign 0.96 text_style "brawler_menu_diff_style"

    hbox:
        spacing 15 * persistent.scale_factor
        xalign 0.52
        yalign 0.72
        yoffset -1 * persistent.scale_factor

        vbox:
            xminimum 565 * persistent.scale_factor
            add "bn_avatar_mc"
            spacing 10 * persistent.scale_factor
            vpgrid:
                xminimum 565 * persistent.scale_factor
                xoffset 12 * persistent.scale_factor
                yoffset 10 * persistent.scale_factor
                cols 2
                spacing 10 * persistent.scale_factor
                text "{color=fe9416}Fights                              {/color}" style "brawler_opp_style" xminimum 500 * persistent.scale_factor
                text "{color=fe9416}%d{/color}" % bn_fight_count style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                text "{color=1df400}Win{/color} / {color=bb433b}Lose{/color}" style "brawler_opp_style" xminimum 500 * persistent.scale_factor
                text "{color=1df400}%d{/color} / {color=bb433b}%d{/color}" % (bn_fight_wins, bn_fight_losses) style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                text "{color=e10d00}Highest {font=fonts/ApeMount.ttf}Rage{/font}{/color}" style "brawler_opp_style" xminimum 500 * persistent.scale_factor
                text "{color=e10d00}%d{/color}" % bn_rage_record style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                text "{color=00b0ff}Highest Damage{/color}" style "brawler_opp_style" xminimum 500 * persistent.scale_factor
                text "{color=00b0ff}%d{/color}" % bn_dmg_record style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                text "{color=ffe059}Available Skill Points{/color}" style "brawler_opp_style" xminimum 500 * persistent.scale_factor
                text "{color=ffe059}%d{/color}" % bn_skill_points style "brawler_opp_style" xoffset 15 * persistent.scale_factor

    if bn_rage_new_record:
        text "{i}New Record!{/i}" style "brawler_record_style" xalign 0.63 yalign 0.842
    if bn_dmg_new_record:
        text "{i}New Record!{/i}" style "brawler_record_style" xalign 0.63 yalign 0.889

    hbox:
        spacing 15 * persistent.scale_factor
        xalign 0.94
        yalign 0.72
        yoffset -1 * persistent.scale_factor

        vbox:
            xminimum 319 * persistent.scale_factor
            xmaximum 319 * persistent.scale_factor
            add "bn_opponent_" + bn_opponent_list[bn_which_fighter][0].lower() + "_hover"
            spacing 10 * persistent.scale_factor
            vpgrid:
                xminimum 319 * persistent.scale_factor
                xmaximum 319 * persistent.scale_factor
                xoffset 12 * persistent.scale_factor
                yoffset 10 * persistent.scale_factor
                cols 2
                spacing 10 * persistent.scale_factor
                text "Difficulty" style "brawler_opp_style"
                if bn_opponent_list[bn_which_fighter][1] > 8:
                    text "{color=bb433b}%d{/color}" % bn_opponent_list[bn_which_fighter][1] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                elif bn_opponent_list[bn_which_fighter][1] > 4:
                    text "{color=ffe059}%d{/color}" % bn_opponent_list[bn_which_fighter][1] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                else:
                    text "{color=1df400}%d{/color}" % bn_opponent_list[bn_which_fighter][1] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                text "Power" style "brawler_opp_style"
                if bn_opponent_list[bn_which_fighter][2] > 8:
                    text "{color=bb433b}%d{/color}" % bn_opponent_list[bn_which_fighter][2] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                elif bn_opponent_list[bn_which_fighter][2] > 4:
                    text "{color=ffe059}%d{/color}" % bn_opponent_list[bn_which_fighter][2] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                else:
                    text "{color=1df400}%d{/color}" % bn_opponent_list[bn_which_fighter][2] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                text "Health" style "brawler_opp_style"
                if bn_opponent_list[bn_which_fighter][3] > 150:
                    text "{color=bb433b}%d{/color}" % bn_opponent_list[bn_which_fighter][3] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                elif bn_opponent_list[bn_which_fighter][3] > 100:
                    text "{color=ffe059}%d{/color}" % bn_opponent_list[bn_which_fighter][3] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                else:
                    text "{color=1df400}%d{/color}" % bn_opponent_list[bn_which_fighter][3] style "brawler_opp_style" xoffset 15 * persistent.scale_factor
                text "Stamina" style "brawler_opp_style"
                hbox:
                    yalign 0.6
                    spacing -8 * persistent.scale_factor
                    for j in range(0,bn_opponent_list[bn_which_fighter][4]):
                        add "bn_stamina_cpu"
            vbox:
                xalign 0.5
                yoffset 30 * persistent.scale_factor
                text "" style "brawler_opp_style"

    vbox:
        xalign 0.69 yalign 0.32
        spacing 30 * persistent.scale_factor
        if bn_mc_won:
            text "You win!" style "brawler_result_text_style" xalign 0.5
            text "%s" % bn_reward style "brawler_skill_text_style" xalign 0.5
        else:
            text "You lose!" style "brawler_result_text_style" xalign 0.5
            text "{color=ededed}No reward{/color}" style "brawler_skill_text_style" xalign 0.5
        textbutton "Fight again" action (Function(bn_play_click,0,0,0),Function(bn_init_opponents),Hide("brawler_result_screen"),Jump("brawler_story_"+bn_opponent_list[bn_which_fighter][0].lower()+"_label")) text_style "brawler_skill_text_btn_style" xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

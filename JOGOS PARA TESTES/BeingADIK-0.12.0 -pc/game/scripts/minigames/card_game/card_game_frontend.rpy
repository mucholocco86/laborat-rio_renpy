screen cg_ol_screen():
    tag cg_ol_screen
    modal False
    zorder 100
    add "cg_overlay"

    vbox:
        xalign 0.99
        yalign 0.035
        xminimum 340 * persistent.scale_factor
        xmaximum 340 * persistent.scale_factor
        text "{u}Score                    Discards          {/u}" style "cg_info_style"
        hbox:
            vbox:
                if "Derek" in cg_leader:
                    text "{color=ffed00}Derek: {/color}" style "cg_info_style"
                else:
                    text "Derek: " style "cg_info_style"
                if "Maya" in cg_leader:
                    text "{color=ffed00}Maya: {/color}" style "cg_info_style"
                else:
                    text "Maya: " style "cg_info_style"
                if "Sage" in cg_leader:
                    text "{color=ffed00}Sage: {/color}" style "cg_info_style"
                else:
                    text "Sage: " style "cg_info_style"
                if "You" in cg_leader:
                    text "{color=ffed00}You: {/color}" style "cg_info_style"
                else:
                    text "You: " style "cg_info_style"
            vbox:
                for i in range(0,4):
                    if "Derek" in cg_leader and i == 0:
                        text "{color=ffed00}%d{/color}" % cg_scores[i] style "cg_info_style"
                    elif "Maya" in cg_leader and i == 1:
                        text "{color=ffed00}%d{/color}" % cg_scores[i] style "cg_info_style"
                    elif "Sage" in cg_leader and i == 2:
                        text "{color=ffed00}%d{/color}" % cg_scores[i] style "cg_info_style"
                    elif "You" in cg_leader and i == 3:
                        text "{color=ffed00}%d{/color}" % cg_scores[i] style "cg_info_style"
                    else:
                        text "%d" % cg_scores[i] style "cg_info_style"
    hbox:
        xalign 0.975
        yalign 0.08
        spacing 8
        for i in range(0,3):
            imagebutton:
                focus_mask True
                if cg_discard_count > i:
                    idle "cg_discard_card"
                    hover "cg_discard_card"
                else:
                    idle "cg_discard_card_used"
                    hover "cg_discard_card_used"

screen cg_mc_cards_screen():
    tag cg_mc_cards_screen
    modal True
    zorder 99
    add "ep12_cg_mc_look_at_cards"
    hbox:
        xalign 0.495
        yalign 0.15
        text "%s" % cg_get_current_question_string() style "cg_question_style" xalign 0.5 xmaximum 200 * persistent.scale_factor

    for i in range(0,5):
        imagebutton:
            focus_mask True
            idle "cg_card%d_idle" % i
            hover "cg_card%d_hover" % i
            action (Function(cg_mc_select_card,i), Return())
    for i in range(0,5):
        vbox:
            xminimum 200 * persistent.scale_factor
            xmaximum 200 * persistent.scale_factor
            yminimum 200 * persistent.scale_factor
            ymaximum 200 * persistent.scale_factor
            yalign 0.62
            if i == 0:
                xalign 0.168
            elif i == 1:
                xalign 0.332
            elif i == 2:
                xalign 0.495
            elif i == 3:
                xalign 0.658
            else:
                xalign 0.823
            text "%s" % cg_get_mc_card_string(i) style "cg_text_btn_style" xalign 0.25 yalign 0.35
    if cg_discard_count > 0:
        for i in range(0,5):
            textbutton "Discard" action (Function(cg_discard_card,i), SetVariable("cg_discard_count", cg_discard_count - 1)) text_style "cg_text_discard_style":
                yalign 0.80
                if i == 0:
                    xalign 0.185
                elif i == 1:
                    xalign 0.34
                elif i == 2:
                    xalign 0.497
                elif i == 3:
                    xalign 0.650
                else:
                    xalign 0.805

screen cg_mc_pick_winner_screen():
    tag cg_mc_pick_winner_screen
    modal True
    for i in range(0,3):
        imagebutton:
            focus_mask True
            idle "cg_win_card%d_idle" % i
            hover "cg_win_card%d_hover" % i
            action (SetVariable("cg_winning_string",cg_answers_and_reactions[i][0]),SetVariable("cg_current_winner",cg_answers_and_reactions[i][1]), Return())

screen cg_read_answers_screen():
    tag cg_read_answers_screen
    modal False
    hbox:
        xalign 0.15
        yalign 0.25
        text "%s" % cg_get_current_question_string() style "cg_question_big_style" xalign 0.5 xmaximum 200 * persistent.scale_factor

screen cg_read_answers_screen1():
    tag cg_read_answers_screen1
    modal False
    vbox:
        xminimum 200 * persistent.scale_factor
        xmaximum 200 * persistent.scale_factor
        yminimum 200 * persistent.scale_factor
        ymaximum 200 * persistent.scale_factor
        yalign 0.2
        xalign 0.39
        text "%s" % cg_answers_and_reactions[0][0] style "cg_text_big_btn_style" xalign 0.25 yalign 0.35

screen cg_read_answers_screen2():
    tag cg_read_answers_screen2
    modal False
    vbox:
        xminimum 200 * persistent.scale_factor
        xmaximum 200 * persistent.scale_factor
        yminimum 200 * persistent.scale_factor
        ymaximum 200 * persistent.scale_factor
        yalign 0.2
        xalign 0.605
        text "%s" % cg_answers_and_reactions[1][0] style "cg_text_big_btn_style" xalign 0.25 yalign 0.35

screen cg_read_answers_screen3():
    tag cg_read_answers_screen3
    modal False
    vbox:
        xminimum 200 * persistent.scale_factor
        xmaximum 200 * persistent.scale_factor
        yminimum 200 * persistent.scale_factor
        ymaximum 200 * persistent.scale_factor
        yalign 0.2
        xalign 0.798
        text "%s" % cg_answers_and_reactions[2][0] style "cg_text_big_btn_style" xalign 0.25 yalign 0.35
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

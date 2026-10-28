label party_planner_setup_evaluation_label:
$ renpy.block_rollback()
$ pp_round_score = 0.0
$ pp_50_satisfied_diks = 0.0
$ pp_round_item_score = 0.0
$ pp_round_item_only_score = 0.0
$ pp_round_activity_score = 0.0
$ pp_round_needs_score = 0.0
$ pp_round_happiness_change = [0,0,0,0,0,0,0,0]
$ pp_round_diks_score = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
$ pp_happiness_icon = [2,2,2,2,2,2,2,2]
$ tmp_list = [-1,-1]

python:
    for x in range(0,len(pp_needs_met)):
        tmpInt = 0.0
        for y in pp_needs_met[x]:
            if y:
                tmpInt += 1.0
        pp_round_happiness_change[x] = tmpInt * 6.0 * pp_extra_happiness - (4.0-tmpInt)*8.0 * pp_happiness_penalty
        pp_happiness_level[x] = round(pp_happiness_level[x] + pp_round_happiness_change[x])
        pp_round_happiness_change[x] = round(pp_round_happiness_change[x])
        if pp_happiness_level[x] > 100:
            pp_happiness_level[x] = 100
        elif pp_happiness_level[x] < 0:
            pp_happiness_level[x] = 0

python:
    for x in range(0,len(pp_happiness_level)):
        if pp_happiness_level[x] >= 50.0:
            pp_50_satisfied_diks += 1.0
        if pp_happiness_level[x] < 25.0:
            pp_happiness_icon[x] = 0
        elif pp_happiness_level[x] < 50.0:
            pp_happiness_icon[x] = 1
        elif pp_happiness_level[x] < 75.0:
            pp_happiness_icon[x] = 2
        else:
            pp_happiness_icon[x] = 3

python:
    for x in range(0,6):
        for y in range(0,6):
            if pp_grid[x][y]>0 and pp_grid[x][y]<9 and pp_active_grid[x][y]:
                if pp_grid[x][y] == 2 or pp_grid[x][y] == 3 or (pp_grid[x][y] == 1 and pp_perk_list[0]) or (pp_grid[x][y] == 4 and pp_perk_list[1]) or (pp_grid[x][y] == 6 and pp_perk_list[2]):
                    pp_round_item_score += pp_item_base_score * len(pp_connector_grid_active[x][y])
                else:
                    pp_round_item_score += pp_item_base_score * (len(pp_connector_grid_active[x][y]) - 1)
                pp_round_item_only_score += pp_item_base_score
python:
    for x in range(0,len(pp_needs_met)):
        for y in pp_needs_met[x]:
            if y:
                pp_round_diks_score[x] += round(pp_needs_met_base_score*((-0.008*pp_happiness_level[x]*pp_happiness_level[x]) + 1.8*pp_happiness_level[x]))
                pp_round_needs_score += round(pp_needs_met_base_score*((-0.008*pp_happiness_level[x]*pp_happiness_level[x]) + 1.8*pp_happiness_level[x]))

$ pp_activity_number = 0
python:
    for x in range(0, len(pp_activity_list)):
        if currentEpisode  == 9:
            if pp_activity_list[x][pp_activity_choices[x]][0] != "Nothing":
                pp_activity_number += 1
                pp_round_activity_score += round(pp_activity_base_score * pp_bonus_multiplier)
        elif currentEpisode  == 10:
            if pp_activity_list[x][pp_activity_choices[x]][0] != "B.Y.O.B." and pp_activity_list[x][pp_activity_choices[x]][0] != "Hot dogs" and pp_activity_list[x][pp_activity_choices[x]][0] != "Nothing":
                pp_activity_number += 1
                pp_round_activity_score += round(pp_activity_base_score * pp_bonus_multiplier)
        elif currentEpisode  == 11:
            if pp_activity_list[x][pp_activity_choices[x]][0] != "B.Y.O.B." and pp_activity_list[x][pp_activity_choices[x]][0] != "Nothing":
                pp_activity_number += 1
                pp_round_activity_score += round(pp_activity_base_score * pp_bonus_multiplier)
        elif currentEpisode  == 12:
            if pp_activity_list[x][pp_activity_choices[x]][0] != "Cheap buffet" and pp_activity_list[x][pp_activity_choices[x]][0] != "No fireworks" and pp_activity_list[x][pp_activity_choices[x]][0] != "Nothing":
                pp_activity_number += 1
                pp_round_activity_score += round(pp_activity_base_score * pp_bonus_multiplier)


$ pp_multiplier = pp_multiplier + pp_multiplier_madness*pp_50_satisfied_diks
$ pp_round_score = int((pp_round_item_score + pp_round_activity_score + pp_round_item_only_score + pp_round_needs_score)*pp_multiplier)
$ pp_score += int(pp_round_score)


$ mansion_animated_score = [0,0,0,0,0,0]
if pp_multiplier > 0:
    $ animated_score_step = max(50, (int)(pp_round_score/(50 * pp_multiplier)))
else:
    $ animated_score_step = 50
$ animated_score_step2 = max(50,(int)(pp_round_score/50))
$ animated_score_step3 = max(50,(int)(pp_score/50))

$ party_planner_get_rank(pp_round_score,pp_activity_number)
$ pp_tut_state = -1
show screen party_planner_happiness_screen
pause


screen party_planner_score_screen:
    tag party_planner_score_screen
    modal True
    add "party_planner_score_screen_bg"

    imagebutton:
        focus_mask True
        idle "pp_next_button"
        hover "pp_next_button_hover"
        action (Play("sfx1", "sound_effects/menu.mp3", loop = False),Hide("party_planner_score_screen"),Show("party_planner_item_perk_screen"))

    vpgrid:
        rows 4
        cols 2
        spacing 30 * persistent.scale_factor
        xalign 0.1
        yalign 0.55

        for x in range(0,len(pp_dik_list)):
            hbox:
                spacing 30 * persistent.scale_factor

                imagebutton:
                    idle "pp_"+pp_dik_list[x]+"_%d_%d_idle" % (pp_happiness_icon[x],pp_needs_met[x].count(True))
                    hover "pp_"+pp_dik_list[x]+"_%d_%d_idle" % (pp_happiness_icon[x],pp_needs_met[x].count(True))
                vbox:
                    yalign 0.5
                    xminimum 300 * persistent.scale_factor
                    text "{color=ffed00}%d{/color} points" % pp_round_diks_score[x] style "pp_eval_style"
                    text "{color=ffed00}%d{/color} points" % pp_round_diks_score[x] style "pp_eval_style"

    timer 0.02 repeat True action If(mansion_animated_score[0] < pp_round_needs_score, true=SetDict(mansion_animated_score, 0, mansion_animated_score[0] + animated_score_step), false=SetDict(mansion_animated_score, 0, pp_round_needs_score))
    if mansion_animated_score[0] == pp_round_needs_score:
        timer 0.02 repeat True action If(mansion_animated_score[1] < pp_round_item_only_score, true=SetDict(mansion_animated_score, 1, mansion_animated_score[1] + animated_score_step), false=SetDict(mansion_animated_score, 1, pp_round_item_only_score))
        if mansion_animated_score[1] == pp_round_item_only_score:
            timer 0.02 repeat True action If(mansion_animated_score[2] < pp_round_item_score, true=SetDict(mansion_animated_score, 2, mansion_animated_score[2] + animated_score_step), false=SetDict(mansion_animated_score, 2, pp_round_item_score))
            if mansion_animated_score[2] == pp_round_item_score:
                timer 0.02 repeat True action If(mansion_animated_score[3] < pp_round_activity_score, true=SetDict(mansion_animated_score, 3, mansion_animated_score[3] + animated_score_step), false=SetDict(mansion_animated_score, 3, pp_round_activity_score))
                if mansion_animated_score[3] == pp_round_activity_score:
                    timer 0.02 repeat True action If(mansion_animated_score[4] < pp_round_score, true=SetDict(mansion_animated_score, 4, mansion_animated_score[4] + animated_score_step2), false=SetDict(mansion_animated_score, 4, pp_round_score))
                    if mansion_animated_score[4] == pp_round_score:
                        timer 0.02 repeat True action If(mansion_animated_score[5] < pp_score, true=SetDict(mansion_animated_score, 5, mansion_animated_score[5] + animated_score_step3), false=SetDict(mansion_animated_score, 5, pp_score))
                        if mansion_animated_score[5] == pp_score:
                            timer 0.02 repeat True action SetDict(mansion_animated_score, 5, pp_score)

    vbox:
        xalign 1.0
        yalign 0.5
        xminimum 800 * persistent.scale_factor
        hbox:
            text "{color=1df400}Fulfilled Needs Score:{/color} " style "pp_eval_style"
            text "{color=ffed00}%d{/color} points" % mansion_animated_score[0] style "pp_eval_style"
        hbox:
            text "{color=1df400}Active Items Score:{/color} " style "pp_eval_style"
            text "{color=ffed00}%d{/color} points" % mansion_animated_score[1] style "pp_eval_style"
        hbox:
            text "{color=1df400}Efficiency Bonus:{/color} " style "pp_eval_style"
            text "{color=ffed00}%d{/color} points" % mansion_animated_score[2] style "pp_eval_style"
        hbox:
            text "{color=1df400}Activities Score:{/color} " style "pp_eval_style"
            text "{color=ffed00}%d{/color} points" % mansion_animated_score[3] style "pp_eval_style"
        text ""
        hbox:
            text "{color=e51475}Multiplier: [pp_multiplier]x" style "pp_eval_style"
        hbox:
            if pp_perk_list[11]:
                text "{color=fe9416}Money Saved: $%d{/color}" % min(pp_money,5) style "pp_eval_style"
            else:
                text ""
        text ""
        hbox:
            text "Total Party Score:" style "pp_eval_style"
            text "{color=ffed00}%d{/color} points" % mansion_animated_score[4] style "pp_eval_style"
        hbox:
            text "Total Score: " style "pp_eval_style"
            if mansion_animated_score[4] == pp_round_score:
                text "{color=ffed00}%d{/color} ({color=ffed00}+%d{/color}) points" % (mansion_animated_score[5],mansion_animated_score[4]) style "pp_eval_style"
            else:
                text "{color=ffed00}%d{/color} ({color=ffed00}+%d{/color}) points" % (mansion_animated_score[5],0) style "pp_eval_style"
        text ""
        hbox:
            text "{color=ffed00}Party Rank:{/color}" style "pp_eval_style"
    if mansion_animated_score[5] == pp_score:
        imagebutton at pp_s_rank_transform:
            idle "drw_rank_%s" % pp_party_rank[-1][1].lower()
            hover "drw_rank_%s" % pp_party_rank[-1][1].lower()
            action NullAction()
            xpos 850 * persistent.scale_factor
            ypos 650 * persistent.scale_factor
        imagebutton at pp_rank_transform:
            idle "drw_rank_%s" % pp_party_rank[-1][1].lower()
            hover "drw_rank_%s" % pp_party_rank[-1][1].lower()
            action NullAction()
            xpos 850 * persistent.scale_factor
            ypos 650 * persistent.scale_factor

    if persistent.pp_tutorial != 2 and currentEpisode == 9:
        if pp_tut_state == 0:
            imagebutton:
                idle "pp_invis_tutorial_button"
                hover "pp_invis_tutorial_button"
                action SetVariable("pp_tut_state",pp_tut_state+1)
        elif pp_tut_state == 1:
            imagebutton:
                idle "party_planner_tutorial_focus_score1"
                hover "party_planner_tutorial_focus_score1"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=00ff00}Fulfilled Needs Score{/color} is the sum of each individual DIK's score." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
        elif pp_tut_state == 2:
            imagebutton:
                idle "party_planner_tutorial_focus_score2"
                hover "party_planner_tutorial_focus_score2"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=00ff00}Active Items Score{/color} is calculated based on the number of active items on the party grid. More items on the grid mean a higher score." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
        elif pp_tut_state == 3:
            imagebutton:
                idle "party_planner_tutorial_focus_score3"
                hover "party_planner_tutorial_focus_score3"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=00ff00}Efficiency Bonus{/color} is calculated based on the number of shared items on the grid. You get a higher efficiency score if you make the DIKs share items." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
        elif pp_tut_state == 4:
            imagebutton:
                idle "party_planner_tutorial_focus_score4"
                hover "party_planner_tutorial_focus_score4"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=00ff00}Activities Score{/color} is based on the number of activities you had at the party. Having activities is an easy way to boost your score." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
        elif pp_tut_state == 5:
            imagebutton:
                idle "party_planner_tutorial_focus_score5"
                hover "party_planner_tutorial_focus_score5"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=ffed00}Total Party Score{/color} is the sum of all scores multiplied by the {color=e51475}Multiplier{/color}." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
        elif pp_tut_state == 6:
            imagebutton:
                idle "party_planner_tutorial_focus_score6"
                hover "party_planner_tutorial_focus_score6"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=ffed00}Party Rank{/color} is based on your {color=ffed00}total party score{/color} and the number of activities you had. The ranking system goes through F, E, D, C, B, A, and S (Best rank)." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
        elif pp_tut_state == 7:
            imagebutton:
                idle "party_planner_tutorial_focus_score6"
                hover "party_planner_tutorial_focus_score6"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "You can get the S rank based on your score alone, but having multiple activities boosts the rank by a lot." xalign 0.15 yalign 0.89 style "pp_tut_text_style"

screen party_planner_happiness_screen:
    tag party_planner_happiness_screen
    modal True
    add "party_planner_happiness_bg"

    imagebutton:
        focus_mask True
        idle "pp_next_button"
        hover "pp_next_button_hover"
        if pp_score > 10000:
            action (Play("sfx1", "sound_effects/season2/score_long.mp3", loop = False),Play("sfx2", "sound_effects/menu.mp3", loop = False),Hide("party_planner_happiness_screen"), Show("party_planner_score_screen"))
        elif pp_score > 5000:
            action (Play("sfx1", "sound_effects/season2/score_short.mp3", loop = False),Play("sfx2", "sound_effects/menu.mp3", loop = False),Hide("party_planner_happiness_screen"), Show("party_planner_score_screen"))
        else:
            action (Play("sfx1", "sound_effects/season2/score_none.mp3", loop = False),Play("sfx2", "sound_effects/menu.mp3", loop = False),Hide("party_planner_happiness_screen"), Show("party_planner_score_screen"))

    vpgrid:
        rows 4
        cols 2
        spacing 30 * persistent.scale_factor
        xalign 0.5
        yalign 0.55

        for x in range(0,len(pp_dik_list)):
            hbox:
                spacing 30 * persistent.scale_factor
                imagebutton:
                    idle "pp_happiness%d" % pp_happiness_icon[x]
                    hover "pp_happiness%d" % pp_happiness_icon[x]
                    xoffset 30 * persistent.scale_factor

                imagebutton:
                    idle "pp_"+pp_dik_list[x]+"_%d_%d_idle" % (pp_happiness_icon[x],pp_needs_met[x].count(True))
                    hover "pp_"+pp_dik_list[x]+"_%d_%d_idle" % (pp_happiness_icon[x],pp_needs_met[x].count(True))
                vbox:
                    yalign 0.5
                    xminimum 400 * persistent.scale_factor
                    if pp_needs_met[x].count(True) == 1:
                        text "{color=00ff00}%d need{/color} fulfilled" % pp_needs_met[x].count(True) style "pp_eval_style"
                    else:
                        text "{color=00ff00}%d needs{/color} fulfilled" % pp_needs_met[x].count(True) style "pp_eval_style"
                    if pp_round_happiness_change[x] < 0.0:
                        text "{color=fe9416}Happiness{/color}: {color=#fe9416}%d%%{/color} ({color=#e10d00}%d%%{/color})" % (pp_happiness_level[x],pp_round_happiness_change[x]) style "pp_eval_style"
                    else:
                        text "{color=fe9416}Happiness{/color}: {color=#fe9416}%d%%{/color} ({color=#1df400}+%d%%{/color})" % (pp_happiness_level[x],pp_round_happiness_change[x]) style "pp_eval_style"

    if persistent.pp_tutorial != 2 and currentEpisode == 9:
        if pp_tut_state == -1:
            imagebutton:
                idle "party_planner_tutorial_happiness_focus"
                hover "party_planner_tutorial_happiness_focus"
                action SetVariable("pp_tut_state",pp_tut_state+1)
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "After each party, you get a party report. This screen shows the DIKs' changes in {color=fe9416}Happiness{/color}. The {color=fe9416}Happiness{/color} percentage affects each DIK's individual {color=ffed00}score{/color}." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

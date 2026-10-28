screen math_quit_screen:
    modal True
    add "math_quit_screen_bg"
    imagebutton:
        xalign 0.33
        yalign 0.57
        idle "pp_yes_idle"
        hover "pp_yes_hover"
        action (Hide("math_quit_screen"),Function(math_quit_func))
    imagebutton:
        xalign 0.67
        yalign 0.57
        idle "pp_no_idle"
        hover "pp_no_hover"
        action Hide("math_quit_screen")
screen math_screen:
    tag math_screen
    modal True
    add "math_bg"

    imagebutton:
        idle "ft_x_button_idle"
        hover "ft_x_button_hover"
        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),Show("math_quit_screen"))
        xalign 0.99
        yalign 0.01

    text "Task %d/%d" % (math_task, math_task_total) style "math_main_style" xalign 0.875 yalign 0.01

    if not (math_own_query and math_own_b and math_own_q):
        text "{size=-%d}Money: {color=00ff00}$%d{/color}{/size}" % ((10 * persistent.scale_factor),money) style "math_task_style" xalign 0.73 yalign 0.984

    if math_d_count == math_d_count_total:
        textbutton "Next" text_style "math_button_style" xalign 0.98 yalign 0.998 action (Function(math_next_task),Function(ft_play_click)):
            hovered (SetVariable("math_tool_tip",5), Show("math_tool_tip_screen"))
            unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))
    else:
        textbutton "Next" text_style "math_button_disabled_style" xalign 0.98 yalign 0.998 action Function(math_play_failed_click):
            hovered (SetVariable("math_tool_tip",5), Show("math_tool_tip_screen"))
            unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))

    if math_tooltips:
        textbutton "{size=-%d}Tooltips: {color=00ff00}On{/color}{/size}" % (20 * persistent.scale_factor) text_style "math_button_style" xalign 0.86 yalign 0.99 action SetVariable("math_tooltips", not math_tooltips)
    else:
        textbutton "{size=-%d}Tooltips: {color=ff0000}Off{/color}{/size}" % (20 * persistent.scale_factor) text_style "math_button_style" xalign 0.86 yalign 0.99 action SetVariable("math_tooltips", not math_tooltips)


    for x in range(0,len(math_grid)):
        $ tmpBool = False
        if len(math_query_info) > 0 and math_grid[x][2] == "d":
            for y in math_query_info:
                if x == y[0]:
                    $ tmpBool = True
                    imagebutton:
                        xpos math_grid[x][0] * persistent.scale_factor
                        ypos math_grid[x][1] * persistent.scale_factor
                        if y[1]:
                            if persistent.colorblind:
                                idle "math_tile_d_correct_idle_alt"
                            else:
                                idle "math_tile_d_correct_idle"
                        else:
                            if persistent.colorblind:
                                idle "math_tile_d_incorrect_idle_alt"
                            else:
                                idle "math_tile_d_incorrect_idle"
                        hover "math_tile_d_hover"
                        if math_active_tool == 1:
                            action (SetVariable("math_d_count", math_d_count - 1),SetDict(math_grid[x],2,"x"),Function(ft_play_menu))
                        elif math_active_tool == 2:
                            action (SetVariable("math_d_count", math_d_count - 1),SetDict(math_grid[x],2,"q"),Function(ft_play_menu))
                        elif math_active_tool == 3:
                            action NullAction()
                        elif math_active_tool == 4:
                            action ((SetVariable("math_d_count", math_d_count - 1),SetDict(math_grid[x],2,"base")),Function(ft_play_menu))
                        else:
                            action NullAction()
        if not tmpBool:
            imagebutton:
                xpos math_grid[x][0] * persistent.scale_factor
                ypos math_grid[x][1] * persistent.scale_factor
                if math_grid[x][2] == "base" or math_grid[x][2] == "q" or math_grid[x][2] == "x":
                    idle "math_tile_%s_idle" % math_grid[x][2]
                    hover "math_tile_%s_hover" % math_grid[x][2]
                elif math_grid[x][2] == "d":
                    idle "math_tile_%s_idle" % math_grid[x][2]
                    hover "math_tile_%s_hover" % math_grid[x][2]
                elif math_grid[x][2] == "crack":
                    idle "math_bomb_img"
                    hover "math_bomb_img"
                else:
                    if persistent.colorblind:
                        if math_grid[x][2] == "pink" or math_grid[x][2] == "orange" or math_grid[x][2] == "blue" or math_grid[x][2] == "gray":
                            idle "math_tile_%s_alt" % math_grid[x][2]
                            hover "math_tile_%s_alt" % math_grid[x][2]
                        else:
                            idle "math_tile_%s" % math_grid[x][2]
                            hover "math_tile_%s" % math_grid[x][2]
                    else:
                        idle "math_tile_%s" % math_grid[x][2]
                        hover "math_tile_%s" % math_grid[x][2]

                if math_grid[x][2] == "pink" or math_grid[x][2] == "orange" or math_grid[x][2] == "blue" or math_grid[x][2] == "gray" or math_grid[x][2] == "crack":
                    action NullAction()
                else:
                    if math_active_tool == 1:
                        if math_grid[x][2] != "x":
                            if math_grid[x][2] == "d":
                                action (SetVariable("math_d_count", math_d_count - 1),SetDict(math_grid[x],2,"x"),Function(ft_play_menu))
                            else:
                                action (SetDict(math_grid[x],2,"x"),Function(ft_play_menu))
                        else:
                            action (SetDict(math_grid[x],2,"base"),Function(ft_play_menu))
                    elif math_active_tool == 2:
                        if math_grid[x][2] != "q":
                            if math_grid[x][2] == "d":
                                action (SetVariable("math_d_count", math_d_count - 1),SetDict(math_grid[x],2,"q"),Function(ft_play_menu))
                            else:
                                action (SetDict(math_grid[x],2,"q"),Function(ft_play_menu))
                        else:
                            action (SetDict(math_grid[x],2,"base"),Function(ft_play_menu))
                    elif math_active_tool == 3:
                        action NullAction()
                    elif math_active_tool == 4:
                        if math_grid[x][2] != "d":
                            if math_d_count != math_d_count_total:
                                action (SetVariable("math_d_count", math_d_count + 1),SetDict(math_grid[x],2,"d"),Function(math_play_beep))
                            else:
                                action NullAction()
                        else:
                            action ((SetVariable("math_d_count", math_d_count - 1),SetDict(math_grid[x],2,"base")),Function(ft_play_menu))
                    else:
                        action NullAction()


    vbox:
        spacing 20 * persistent.scale_factor
        xalign 0.99
        ypos 150 * persistent.scale_factor
        xminimum 600 * persistent.scale_factor
        xmaximum 600 * persistent.scale_factor
        ymaximum 620 * persistent.scale_factor

        hbox:
            spacing 10 * persistent.scale_factor
            text "%s" % math_task_desc[0] style "math_task_style"
            if math_task_desc[1] != "":
                imagebutton:
                    idle "math_%s_icon" % math_task_desc[1]
                    hover "math_%s_icon" % math_task_desc[1]
                    action NullAction()


        for x in math_task_list:
            hbox:
                spacing 10 * persistent.scale_factor
                if x[0] != "":
                    text "{size=-%d}• {/size}" % (6 * persistent.scale_factor) style "math_task_style"
                text "{size=-%d}%s{/size}" % ((6 * persistent.scale_factor),x[0]) style "math_task_style"
                if x[1] != "":
                    imagebutton:
                        if persistent.colorblind:
                            idle "math_%s_icon_alt" % x[1]
                            hover "math_%s_icon_alt" % x[1]
                        else:
                            idle "math_%s_icon" % x[1]
                            hover "math_%s_icon" % x[1]
                        action NullAction()



    text "Tools" style "math_task_style" xalign 0.85 yalign 0.75
    hbox:
        xalign 0.97
        yalign 0.9
        spacing 20 * persistent.scale_factor
        vbox:
            imagebutton:
                hovered (SetVariable("math_tool_tip",1), Show("math_tool_tip_screen"))
                unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))

                if math_active_tool == 1:
                    idle "math_tile_x_hover"
                    hover "math_tile_x_hover"
                    action (Function(math_tool_selected,1),Function(ft_play_menu))
                else:
                    idle "math_tile_x_idle"
                    hover "math_tile_x_hover"
                    action (SetVariable("math_active_tool", 1),Function(math_tool_selected,1),Function(ft_play_menu))
            text "" style "math_task_style" xalign 0.5
        vbox:
            imagebutton:
                hovered (SetVariable("math_tool_tip",2), Show("math_tool_tip_screen"))
                unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))
                if math_own_q:
                    if math_active_tool == 2:
                        idle "math_tile_q_hover"
                        hover "math_tile_q_hover"
                        action (Function(math_tool_selected,2),Function(ft_play_menu))
                    else:
                        idle "math_tile_q_idle"
                        hover "math_tile_q_hover"
                        action (SetVariable("math_active_tool", 2),Function(math_tool_selected,2),Function(ft_play_menu))
                else:
                    idle "math_tile_q_disabled_idle"
                    hover "math_tile_q_disabled_hover"
                    if math_buy_tool == 2:
                        action (Function(math_buy_tool_func,2,1),SetVariable("math_active_tool", 0))
                    elif money >= 1:
                        action (Function(math_tool_selected,2),SetVariable("math_active_tool", 0),Function(ft_play_menu))
                    else:
                        action (SetVariable("math_active_tool", 0),Function(ft_play_menu))
            if math_own_q:
                text "" style "math_task_style" xalign 0.5
            else:
                if math_buy_tool == 2:
                    text "Buy?" style "math_task_style" xalign 0.5
                else:
                    if money >= 1:
                        text "{color=00ff00}$1{/color}" style "math_task_style" xalign 0.5
                    else:
                        text "{color=7b7b7b}$1{/color}" style "math_task_style" xalign 0.5
        vbox:
            imagebutton:
                hovered (SetVariable("math_tool_tip",3), Show("math_tool_tip_screen"))
                unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))
                if math_own_b:
                    if math_active_tool == 3:
                        idle "math_tile_b_hover"
                        hover "math_tile_b_hover"
                        if math_active_tool == 3 and not math_bomb_used and math_b_count > 0:
                            action (Function(math_use_bomb),Function(math_tool_selected,3))
                        else:
                            action (Function(math_tool_selected,3),Function(ft_play_menu))
                    else:
                        idle "math_tile_b_idle"
                        hover "math_tile_b_hover"
                        action (SetVariable("math_active_tool", 3),Function(math_tool_selected,3),Function(ft_play_menu))
                else:
                    idle "math_tile_b_disabled_idle"
                    hover "math_tile_b_disabled_hover"
                    if math_buy_tool == 3:
                        action (Function(math_buy_tool_func,3,1),SetVariable("math_active_tool", 0))
                    elif money >= 1:
                        action (Function(math_tool_selected,3),SetVariable("math_active_tool", 0),Function(ft_play_menu))
                    else:
                        action (SetVariable("math_active_tool", 0),Function(ft_play_menu))
            if math_own_b:
                if math_active_tool == 3 and not math_bomb_used and math_b_count > 0:
                    text "Use?" style "math_task_style" xalign 0.5
                elif math_active_tool == 3 and math_bomb_used:
                    text "{color=ff0000}Used{/color}" style "math_task_style" xalign 0.5
                else:
                    if math_bomb_used:
                        text "{color=ff0000}Used{/color}" style "math_task_style" xalign 0.5
                    else:
                        text "%d/%d" % (math_b_count,math_b_count_total) style "math_task_style" xalign 0.5
            else:
                if math_buy_tool == 3:
                    text "Buy?" style "math_task_style" xalign 0.5
                else:
                    if money >= 1:
                        text "{color=00ff00}$1{/color}" style "math_task_style" xalign 0.5
                    else:
                        text "{color=7b7b7b}$1{/color}" style "math_task_style" xalign 0.5
        vbox:
            imagebutton:
                hovered (SetVariable("math_tool_tip",6), Show("math_tool_tip_screen"))
                unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))
                if math_own_query and math_d_count == math_d_count_total:
                    if math_active_tool == 5:
                        idle "math_tile_query_hover"
                        hover "math_tile_query_hover"
                        if math_active_tool == 5 and math_query_count > 0:
                            action (Function(math_use_query),Function(math_tool_selected,0), SetVariable("math_active_tool", 0))
                        else:
                            action (Function(math_tool_selected,5),Function(ft_play_menu))
                    else:
                        idle "math_tile_query_idle"
                        hover "math_tile_query_hover"
                        action (SetVariable("math_active_tool", 5),Function(math_tool_selected,5),Function(ft_play_menu))
                else:
                    idle "math_tile_query_disabled_idle"
                    hover "math_tile_query_disabled_hover"
                    if math_own_query:
                        action NullAction()
                    else:
                        if math_buy_tool == 5:
                            action (Function(math_buy_tool_func,5,1),SetVariable("math_active_tool", 0))
                        elif money >= 1:
                            action (Function(math_tool_selected,5),SetVariable("math_active_tool", 0),Function(ft_play_menu))
                        else:
                            action (SetVariable("math_active_tool", 0),Function(ft_play_menu))
            if math_own_query:
                if math_active_tool == 5 and math_query_count > 0:
                    text "Use?" style "math_task_style" xalign 0.5
                else:
                    text "%d/%d" % (math_query_count,math_query_count_total) style "math_task_style" xalign 0.5
            else:
                if math_buy_tool == 5:
                    text "Buy?" style "math_task_style" xalign 0.5
                else:
                    if money >= 1:
                        text "{color=00ff00}$1{/color}" style "math_task_style" xalign 0.5
                    else:
                        text "{color=7b7b7b}$1{/color}" style "math_task_style" xalign 0.5
        vbox:
            imagebutton:
                hovered (SetVariable("math_tool_tip",4), Show("math_tool_tip_screen"))
                unhovered (SetVariable("math_tool_tip",0), Hide("math_tool_tip_screen"))
                if math_active_tool == 4:
                    idle "math_tile_d_hover"
                    hover "math_tile_d_hover"
                    action (Function(math_tool_selected,4),Function(ft_play_menu))
                else:
                    idle "math_tile_d_idle"
                    hover "math_tile_d_hover"
                    action (SetVariable("math_active_tool", 4),Function(math_tool_selected,4),Function(ft_play_menu))
            if math_d_count == math_d_count_total:
                text "{color=00ff00}%d/%d{/color}" % (math_d_count,math_d_count_total) style "math_task_style" xalign 0.5
            else:
                text "%d/%d" % (math_d_count,math_d_count_total) style "math_task_style" xalign 0.5

screen math_result_screen:
    tag math_result_screen
    modal True

    add "math_bg"

    text "You had %d correct answers!" % math_task_correct_answers.count(True) style "math_task_style":
        size 40 * persistent.scale_factor + 7* persistent.scale_factor
        xalign 0.96
        yalign 0.18
    vbox:
        xminimum 614 * persistent.scale_factor
        xmaximum 614 * persistent.scale_factor
        xpos 1280 * persistent.scale_factor
        yalign 0.35
        text "[mathResult]% {color=00ff00}+[bonusPercentageMath]%{/color}" style "math_task_res_style":
            size 190 * persistent.scale_factor - 50 * persistent.scale_factor

    if mathResult + bonusPercentageMath < 70 - (mathBoost*5):
        text "{color=ff0000}You failed the test.{/color}" style "math_task2_style":
            size 40 * persistent.scale_factor + 7* persistent.scale_factor
            xalign 0.915
            yalign 0.6
    else:
        if math_rew:
            text "You passed the test.\n{color=fe9416}You unlocked a special render!{/color}" style "math_task2_style":
                size 40 * persistent.scale_factor + 5 * persistent.scale_factor
                xalign 0.975
                yalign 0.6
        else:
            text "You passed the test." style "math_task2_style":
                size 40 * persistent.scale_factor + 7* persistent.scale_factor
                xalign 0.915
                yalign 0.6


    text "{u}Result{/u}" style "math_task_res_style" xalign 0.25 yalign 0.08
    hbox:
        xalign 0.2
        yalign 0.5
        spacing 10 * persistent.scale_factor
        vbox:
            spacing 10 * persistent.scale_factor
            for i in range(0,len(math_task_correct_answers)):
                hbox:
                    spacing 10 * persistent.scale_factor
                    text "{color=ffed00}Task %d{/color}  - " % (i+1) style "math_task_style" xminimum 600 * persistent.scale_factor:
                        size 40 * persistent.scale_factor + 20 * persistent.scale_factor

                    if currentEpisode == 10:
                        if i == 0 or i == 2:
                            text "Find 1" style "math_task_style":
                                size 40 * persistent.scale_factor + 20 * persistent.scale_factor
                        elif i == 1 or i == 3:
                            text "Find 2" style "math_task_style":
                                size 40 * persistent.scale_factor + 20 * persistent.scale_factor
                        else:
                            text "Find 3" style "math_task_style":
                                size 40 * persistent.scale_factor + 20 * persistent.scale_factor
        vbox:
            xoffset 10 * persistent.scale_factor
            yoffset 10 * persistent.scale_factor
            spacing 30 * persistent.scale_factor
            for i in range(0,len(math_task_correct_answers)):
                imagebutton:
                    idle "math_d_icon"
                    hover "math_d_icon"
                    action NullAction()
                    xalign 0.5
                    yalign 0.5

        vbox:
            spacing 10 * persistent.scale_factor
            for i in range(0,len(math_task_correct_answers)):
                hbox:
                    spacing 10 * persistent.scale_factor
                    if math_task_correct_answers[i]:
                        text "{color=00ff00}    Correct!{/color}" style "math_task_style" xminimum 600 * persistent.scale_factor:
                            size 40 * persistent.scale_factor + 20 * persistent.scale_factor
                    else:
                        text "{color=ff0000}    Incorrect!{/color}" style "math_task_style" xminimum 600 * persistent.scale_factor:
                            size 40 * persistent.scale_factor + 20 * persistent.scale_factor


    imagebutton:
        idle "big_invis"
        hover "big_invis"
        action (SetVariable("bonusPercentageMath",0),Jump(math_jump_label))


screen math_tool_tip_screen:
    tag math_tool_tip_screen
    modal False
    if math_tooltips:
        add "math_tool_tip" at math_tt_transform
        text "%s" % math_tt[math_tool_tip-1] style "math_tt_style" xalign 0.21 yalign 0.018 at math_tt_transform
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

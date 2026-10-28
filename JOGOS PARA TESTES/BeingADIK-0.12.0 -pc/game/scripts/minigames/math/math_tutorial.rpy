screen math_tut_screen:
    tag math_tut_screen
    modal True

    add "math_bg"

    text "Tutorial" style "math_main_style" xalign 0.875 yalign 0.01

    if math_tut_step > 10:
        textbutton "Next" text_style "math_button_style" xalign 0.98 yalign 0.998 action NullAction()
    else:
        textbutton "Next" text_style "math_button_disabled_style" xalign 0.98 yalign 0.998 action NullAction()


    for x in math_grid:
        imagebutton:
            xpos x[0] * persistent.scale_factor
            ypos x[1] * persistent.scale_factor
            if x[2] == "base" or x[2] == "q" or x[2] == "x" or x[2] == "d":
                idle "math_tile_%s_idle" % x[2]
                hover "math_tile_%s_hover" % x[2]
            elif x[2] == "crack":
                idle "math_bomb_img"
                hover "math_bomb_img"
            else:
                if persistent.colorblind:
                    if x[2] == "pink" or x[2] == "orange" or x[2] == "blue" or x[2] == "gray":
                        idle "math_tile_%s_alt" % x[2]
                        hover "math_tile_%s_alt" % x[2]
                    else:
                        idle "math_tile_%s" % x[2]
                        hover "math_tile_%s" % x[2]
                else:
                    idle "math_tile_%s" % x[2]
                    hover "math_tile_%s" % x[2]

            if x[2] == "pink" or x[2] == "orange" or x[2] == "blue" or x[2] == "gray" or x[2] == "crack":
                action NullAction()
            else:
                if math_active_tool == 1:
                    if x[2] != "x":
                        if x[2] == "d":
                            action (SetVariable("math_d_count", math_d_count - 1),SetDict(x,2,"x"),Function(ft_play_menu))
                        else:
                            action (SetDict(x,2,"x"),Function(ft_play_menu))
                    else:
                        action (SetDict(x,2,"base"),Function(ft_play_menu))
                elif math_active_tool == 2:
                    if x[2] != "q":
                        if x[2] == "d":
                            action (SetVariable("math_d_count", math_d_count - 1),SetDict(x,2,"q"),Function(ft_play_menu))
                        else:
                            action (SetDict(x,2,"q"),Function(ft_play_menu))
                    else:
                        action (SetDict(x,2,"base"),Function(ft_play_menu))
                elif math_active_tool == 3:
                    action NullAction()
                elif math_active_tool == 4:
                    if x[2] != "d":
                        if math_d_count != math_d_count_total:
                            action (SetVariable("math_d_count", math_d_count + 1),SetDict(x,2,"d"),Function(math_play_beep))
                        else:
                            action NullAction()
                    else:
                        action ((SetVariable("math_d_count", math_d_count - 1),SetDict(x,2,"base")),Function(ft_play_menu))
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
                    text "{size=-%d}• {/size}" % (5 * persistent.scale_factor) style "math_task_style"
                text "{size=-%d}%s{/size}" % ((5 * persistent.scale_factor), x[0]) style "math_task_style"
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
                if math_active_tool == 2:
                    idle "math_tile_q_hover"
                    hover "math_tile_q_hover"
                    action (Function(math_tool_selected,2),Function(ft_play_menu))
                else:
                    idle "math_tile_q_idle"
                    hover "math_tile_q_hover"
                    action (SetVariable("math_active_tool", 2),Function(math_tool_selected,2),Function(ft_play_menu))

            text "" style "math_task_style" xalign 0.5

        vbox:
            imagebutton:
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


            if math_tut_step > 11:
                text "{color=ff0000}Used{/color}" style "math_task_style" xalign 0.5
            else:
                text "%d/%d" % (math_b_count,math_b_count_total) style "math_task_style" xalign 0.5
        vbox:
            imagebutton:
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
            if math_tut_step > 13:
                text "1/2" style "math_task_style" xalign 0.5
            else:
                text "2/2" style "math_task_style" xalign 0.5
        vbox:
            imagebutton:
                if math_active_tool == 4:
                    idle "math_tile_d_hover"
                    hover "math_tile_d_hover"
                    action (Function(math_tool_selected,4),Function(ft_play_menu))
                else:
                    idle "math_tile_d_idle"
                    hover "math_tile_d_hover"
                    action (SetVariable("math_active_tool", 4),Function(math_tool_selected,4),Function(ft_play_menu))
            if math_tut_step > 10:
                text "{color=00ff00}1/1{/color}" style "math_task_style" xalign 0.5
            else:
                text "%d/%d" % (math_d_count,math_d_count_total) style "math_task_style" xalign 0.5


    if math_tut_step == 1:
        add "math_tut1"
    elif math_tut_step == 2:
        add "math_tut2"
    elif math_tut_step == 3:
        add "math_tut3"
    elif math_tut_step == 4:
        imagebutton:
            idle "math_tile_no_diamond"
            hover "math_tile_no_diamond"
            xpos 700 * persistent.scale_factor
            ypos 500 * persistent.scale_factor
        imagebutton:
            idle "math_tile_no_diamond"
            hover "math_tile_no_diamond"
            xpos 600 * persistent.scale_factor
            ypos 600 * persistent.scale_factor
        imagebutton:
            idle "math_tile_no_diamond"
            hover "math_tile_no_diamond"
            xpos 700 * persistent.scale_factor
            ypos 600 * persistent.scale_factor
        imagebutton:
            idle "math_tile_no_diamond"
            hover "math_tile_no_diamond"
            xpos 600 * persistent.scale_factor
            ypos 700 * persistent.scale_factor
    elif math_tut_step == 5:
        add "math_tut4"
    if math_tut_step > 4:
        imagebutton:
            idle "math_tile_x_idle"
            hover "math_tile_x_idle"
            xpos 700 * persistent.scale_factor
            ypos 500 * persistent.scale_factor
        imagebutton:
            idle "math_tile_x_idle"
            hover "math_tile_x_idle"
            xpos 600 * persistent.scale_factor
            ypos 600 * persistent.scale_factor
        imagebutton:
            idle "math_tile_x_idle"
            hover "math_tile_x_idle"
            xpos 700 * persistent.scale_factor
            ypos 600 * persistent.scale_factor
        imagebutton:
            idle "math_tile_x_idle"
            hover "math_tile_x_idle"
            xpos 600 * persistent.scale_factor
            ypos 700 * persistent.scale_factor
        if math_tut_step > 7:
            imagebutton:
                idle "math_tile_q_idle"
                hover "math_tile_q_idle"
                xpos 600 * persistent.scale_factor
                ypos 300 * persistent.scale_factor
            imagebutton:
                idle "math_tile_q_idle"
                hover "math_tile_q_idle"
                xpos 600 * persistent.scale_factor
                ypos 400 * persistent.scale_factor
        if math_tut_step > 11:
            imagebutton:
                idle "math_bomb_img"
                hover "math_bomb_img"
                xpos 600 * persistent.scale_factor
                ypos 400 * persistent.scale_factor
            imagebutton:
                idle "math_bomb_img"
                hover "math_bomb_img"
                xpos 600 * persistent.scale_factor
                ypos 500 * persistent.scale_factor
            imagebutton:
                idle "math_bomb_img"
                hover "math_bomb_img"
                xpos 700 * persistent.scale_factor
                ypos 500 * persistent.scale_factor
            imagebutton:
                idle "math_bomb_img"
                hover "math_bomb_img"
                xpos 600 * persistent.scale_factor
                ypos 700 * persistent.scale_factor
            imagebutton:
                idle "math_bomb_img"
                hover "math_bomb_img"
                xpos 700 * persistent.scale_factor
                ypos 600 * persistent.scale_factor
    if math_tut_step == 6:
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 300 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 400 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 600 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 700 * persistent.scale_factor
    elif math_tut_step == 7:
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 300 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 400 * persistent.scale_factor
    elif math_tut_step == 8:
        add "math_tut5"
    elif math_tut_step == 9:
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 300 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 400 * persistent.scale_factor
            ypos 500 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 500 * persistent.scale_factor
            ypos 600 * persistent.scale_factor
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 700 * persistent.scale_factor
    elif math_tut_step == 10:
        imagebutton at math_tut_flash:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 300 * persistent.scale_factor
        add "math_tut7"
    elif math_tut_step == 11 or math_tut_step == 12 or math_tut_step == 13:
        imagebutton:
            idle "math_tile_d_idle"
            hover "math_tile_d_idle"
            xpos 600 * persistent.scale_factor
            ypos 300 * persistent.scale_factor
        if math_tut_step == 11:
            add "math_tut8"
        elif math_tut_step == 13:
            add "math_tut6"
    elif math_tut_step > 13:
        imagebutton:
            idle "math_tile_d_correct_idle"
            hover "math_tile_d_correct_idle"
            xpos 600 * persistent.scale_factor
            ypos 300 * persistent.scale_factor
    add "math_tut_box"

    if math_tut_step == 0:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "In the math mini-game, your goal is to find the diamonds that are hidden behind the empty tiles. You accomplish this by deducing their locations.\n" style "math_tut_style" xalign 0.13 yalign 0.97
    elif math_tut_step == 1:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "In this area, you can see how many diamonds you must find.\nYou can also read the criteria that apply to the diamonds.\nBy understanding the criteria, you will be able to find the diamonds." style "math_tut_style" xalign 0.14 yalign 0.95
    elif math_tut_step == 2:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "The diamond is hidden behind one of the empty tiles.\nThe tiles with colored spheres exist to aid you with the task criteria." style "math_tut_style" xalign 0.15 yalign 0.933
    elif math_tut_step == 3:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "The first criterion says that the diamond has to be 2 steps or fewer away from the blue sphere. A step is counted horizontally and vertically but never diagonally. Tiles with spheres cannot contain diamonds but count as steps." style "math_tut_style" xalign 0.12 yalign 0.95
    elif math_tut_step == 4:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (SetVariable("math_tut_step",math_tut_step+1),SetVariable("math_active_tool",1))
        text "This means that the diamond cannot be hidden behind these tiles.\nUse the X tool to make it easier to keep track of your deductions." style "math_tut_style" xalign 0.17 yalign 0.933
    elif math_tut_step == 5:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "Marking empty tiles with an \'X\' is an easy way to remember that they cannot contain diamonds. The X tool is free to use." style "math_tut_style" xalign 0.094 yalign 0.94
    elif math_tut_step == 6:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "The second criterion says the diamond is in the same column as the pink sphere. There are 4 empty tiles that fulfill this criterion, but only 2 empty\ntiles fulfill the first criterion as well." style "math_tut_style" xalign 0.125 yalign 0.95
    elif math_tut_step == 7:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (SetVariable("math_tut_step",math_tut_step+1),SetVariable("math_active_tool",2))
        text "The diamond must be hiding behind one of these two empty tiles.\nUse the ? tool to highlight empty tiles that may have a diamond." style "math_tut_style" xalign 0.15 yalign 0.933
    elif math_tut_step == 8:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "Marking empty tiles with a \'?\' is an easy way to remember where diamonds can be located. The ? tool costs {color=00ff00}$1{/color} to unlock permanently." style "math_tut_style" xalign 0.10 yalign 0.94
    elif math_tut_step == 9:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action SetVariable("math_tut_step",math_tut_step+1)
        text "The final criterion says that the diamond cannot be within 3 steps of the orange sphere. The highlighted squares show which ones fulfill this criterion." style "math_tut_style" xalign 0.10 yalign 0.933
    elif math_tut_step == 10:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (SetVariable("math_tut_step",math_tut_step+1),SetVariable("math_active_tool",4))
        text "Only one empty tile fulfills all three criteria at once. This must be where the diamond is. Select and use the diamond tool to mark the tile you believe has the diamond." style "math_tut_style" xalign 0.11 yalign 0.95
    elif math_tut_step == 11:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (SetVariable("math_tut_step",math_tut_step+1),Function(math_play_bomb))
        text "The difficulty of the tasks varies, and if a task becomes too hard, you can use the bomb tool. The bomb tool removes a set of empty tiles that don't hide the diamond. This simplifies your deduction." style "math_tut_style" xalign 0.11 yalign 0.95
    elif math_tut_step == 12:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (SetVariable("math_tut_step",math_tut_step+1),SetVariable("math_active_tool",3))
        text "The removed tiles will appear cracked and cannot be clicked anymore. You can only use the bomb tool once per task and twice per math class. The bomb tool costs {color=00ff00}$1{/color} to unlock." style "math_tut_style" xalign 0.12 yalign 0.95
    elif math_tut_step == 13:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (Function(math_play_query_correct),SetVariable("math_tut_step",math_tut_step+1),SetVariable("math_active_tool",5))
        text "If you are unsure if your answer is correct and want to check it in advance, you can use the query tool. Place the diamond(s) and click the query tool." style "math_tut_style" xalign 0.12 yalign 0.933
    elif math_tut_step == 14:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (SetVariable("math_tut_step",math_tut_step+1),SetVariable("math_active_tool",5))
        text "The border of your diamond(s) will either highlight green if your answer is correct or red if your answer is wrong. You can only use the query tool\ntwice per math class. The query tool costs {color=00ff00}$1{/color} to unlock." style "math_tut_style" xalign 0.12 yalign 0.95
    elif math_tut_step == 15:
        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (Hide("math_tut_screen"),Jump("after_math_tut_ep10_label"))
        text "When you are done with the task, you can click the Next button to continue. This concludes the tutorial." style "math_tut_style" xalign 0.11 yalign 0.93
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

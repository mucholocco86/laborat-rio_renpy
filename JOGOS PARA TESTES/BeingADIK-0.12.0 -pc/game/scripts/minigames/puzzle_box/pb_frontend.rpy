screen puzzle_box_screen_ep10:
    tag puzzle_box_screen_ep10
    modal True

    add "pb_translucent"
    if puzzle_box_side_unlocked[puzzle_box_side]:
        add "pb_unlocked_base"
    else:
        add "pb_locked_base"
    if persistent.mod_wtenabled:
                textbutton "{b}HELP{/b}" action [Show("puzzle_box_wt_help"),Hide("puzzle_box_help")] text_size 25 text_color "#FFFFFF" yalign 0.2 xalign 0.9
    imagebutton:
        idle "pp_x_button_idle"
        hover "pp_x_button_hover"
        action Return()
        xalign 0.98
        yalign 0.02


    for i in range (1,7):
        imagebutton:
            focus_mask True
            if puzzle_box_side + 1 != i:
                idle "pb_%d_idle" % i
                hover "pb_%d_hover" % i
                action SetVariable("puzzle_box_side",i-1)
            else:
                idle "pb_%d_selected" % i
                hover "pb_%d_selected" % i
                action NullAction()

    if puzzle_box_side_unlocked[puzzle_box_side]:
        add "pb_side_art_%d" % (puzzle_box_side+1)
        if puzzle_box_side == 0:

            for i in range (1,5):
                imagebutton:
                    focus_mask True
                    if pb_side1_dials[i-1] == 0:
                        idle "pb1_dial%d_up_idle" % i
                        hover "pb1_dial%d_up_hover" % i
                    elif pb_side1_dials[i-1] == 1:
                        idle "pb1_dial%d_right_idle" % i
                        hover "pb1_dial%d_right_hover" % i
                    elif pb_side1_dials[i-1] == 2:
                        idle "pb1_dial%d_down_idle" % i
                        hover "pb1_dial%d_down_hover" % i
                    else:
                        idle "pb1_dial%d_left_idle" % i
                        hover "pb1_dial%d_left_hover" % i
                    action (Function(play_pb_dial),Function(pb_rotate_dials,i-1))
            imagebutton:
                focus_mask True
                idle "pb_button_1_idle"
                hover "pb_button_1_hover"
                if "button1" in pb_button_unlockable and not puzzle_box_side_unlocked[1]:
                    action (Function(play_pb_open),SetDict(puzzle_box_side_unlocked,1,True),SetDict(puzzle_box_side_unlocked,2,True))
                elif "button2" in pb_button_unlockable and puzzle_box_side_unlocked[1] and puzzle_box_side_unlocked[2] and not pb_3_lid_open[0]:
                    action (Function(play_pb_open),SetDict(pb_3_lid_open,0, True),Return())
                else:
                    action Function(play_pb_failed_click)
        elif puzzle_box_side == 1:

            for i in range (1,13):
                imagebutton:
                    focus_mask True
                    if pb_2nd_count == i:
                        idle "pb_hole%d_close" % i
                        hover "pb_hole%d_close" % i
                        action NullAction()
                    else:
                        idle "pb_hole%d_open" % i
                        hover "pb_hole%d_open_hover" % i
                        action (Function(play_pb_switch),Function(pb_6_symbol_pressed,i-1))
            imagebutton:
                focus_mask True
                idle "pb_button_1_idle"
                hover "pb_button_1_hover"
                action (Function(pb_play_flip), Function(pb_push_2nd))
        elif puzzle_box_side == 2:

            imagebutton:
                focus_mask True
                idle "pb3_lid1_close"
                hover "pb3_lid1_close"
                action NullAction()
            imagebutton:
                focus_mask True
                idle "pb3_lid2_close"
                hover "pb3_lid2_close"
                action NullAction()
            imagebutton:
                focus_mask True
                idle "pb3_lid3_close"
                hover "pb3_lid3_close"
                action NullAction()
            imagebutton:
                focus_mask True
                idle "pb3_lid4_close"
                hover "pb3_lid4_close"
                action NullAction()
            imagebutton:
                focus_mask True
                idle "pb3_lid5_close"
                hover "pb3_lid5_close"
                action NullAction()
screen puzzle_box_screen_ep10_fake:
    tag puzzle_box_screen_ep10_fake
    modal False

    add "pb_translucent"
    add "pb_unlocked_base"

    add "pb_side_art_1"
    for i in range (1,5):
        imagebutton:
            focus_mask True
            if pb_side1_dials[i-1] == 0:
                idle "pb1_dial%d_up_idle" % i
                hover "pb1_dial%d_up_idle" % i
            elif pb_side1_dials[i-1] == 1:
                idle "pb1_dial%d_right_idle" % i
                hover "pb1_dial%d_right_idle" % i
            elif pb_side1_dials[i-1] == 2:
                idle "pb1_dial%d_down_idle" % i
                hover "pb1_dial%d_down_idle" % i
            else:
                idle "pb1_dial%d_left_idle" % i
                hover "pb1_dial%d_left_idle" % i
            action NullAction()
    imagebutton:
        focus_mask True
        idle "pb_button_1_idle"
        hover "pb_button_1_idle"
        action NullAction()
screen puzzle_box_screen:
    tag puzzle_box_screen
    modal True

    add "pb_translucent"
    if puzzle_box_side_unlocked[puzzle_box_side]:
        add "pb_unlocked_base"
    else:
        add "pb_locked_base"
    if persistent.mod_wtenabled:
                textbutton "{b}HELP{/b}" action [Show("puzzle_box_wt_help"),Hide("puzzle_box_help")] text_size 25 text_color "#FFFFFF" yalign 0.2 xalign 0.9
    imagebutton:
        idle "pp_x_button_idle"
        hover "pp_x_button_hover"
        action Return()
        xalign 0.98
        yalign 0.02


    for i in range (1,7):
        imagebutton:
            focus_mask True
            if puzzle_box_side + 1 != i:
                idle "pb_%d_idle" % i
                hover "pb_%d_hover" % i
                action SetVariable("puzzle_box_side",i-1)
            else:
                idle "pb_%d_selected" % i
                hover "pb_%d_selected" % i
                action NullAction()

    if puzzle_box_side_unlocked[puzzle_box_side]:
        if final_button_unlocked and puzzle_box_side==3:
            add "pb_side_art_4_open"
            imagebutton:
                focus_mask True
                idle "pb4_idle"
                hover "pb4_hover"
                action (SetVariable("pb_completed",True),SetVariable("persistent.pb_completed",True),Return())
        else:
            add "pb_side_art_%d" % (puzzle_box_side+1)
        if puzzle_box_side == 0:

            for i in range (1,5):
                imagebutton:
                    focus_mask True
                    if pb_side1_dials[i-1] == 0:
                        idle "pb1_dial%d_up_idle" % i
                        hover "pb1_dial%d_up_hover" % i
                    elif pb_side1_dials[i-1] == 1:
                        idle "pb1_dial%d_right_idle" % i
                        hover "pb1_dial%d_right_hover" % i
                    elif pb_side1_dials[i-1] == 2:
                        idle "pb1_dial%d_down_idle" % i
                        hover "pb1_dial%d_down_hover" % i
                    else:
                        idle "pb1_dial%d_left_idle" % i
                        hover "pb1_dial%d_left_hover" % i
                    action (Function(play_pb_dial),Function(pb_rotate_dials,i-1))
            imagebutton:
                focus_mask True
                idle "pb_button_1_idle"
                hover "pb_button_1_hover"
                if "button1" in pb_button_unlockable and not puzzle_box_side_unlocked[1]:
                    action (Function(play_pb_open),SetDict(puzzle_box_side_unlocked,1,True),SetDict(puzzle_box_side_unlocked,2,True))
                elif "button2" in pb_button_unlockable and puzzle_box_side_unlocked[1] and puzzle_box_side_unlocked[2] and not pb_3_lid_open[0]:
                    if currentEpisode > 10:
                        action (Function(play_pb_open),SetDict(pb_3_lid_open,0, True))
                    else:
                        action (Function(play_pb_open),SetDict(pb_3_lid_open,0, True),Return())
                elif "button3" in pb_button_unlockable and pb_3_lid_open[0] and not puzzle_box_side_unlocked[4]:
                    action (Function(play_pb_open),SetDict(puzzle_box_side_unlocked,4,True))
                elif "button4" in pb_button_unlockable and pb_3_lid_open[0] and not puzzle_box_side_unlocked[5]:
                    action (Function(play_pb_open), SetDict(puzzle_box_side_unlocked,5,True))
                else:
                    action Function(play_pb_failed_click)
        elif puzzle_box_side == 1:

            for i in range (1,13):
                imagebutton:
                    focus_mask True
                    if pb_2nd_count == i:
                        idle "pb_hole%d_close" % i
                        hover "pb_hole%d_close" % i
                        action NullAction()
                    else:
                        idle "pb_hole%d_open" % i
                        hover "pb_hole%d_open_hover" % i
                        action (Function(play_pb_switch),Function(pb_6_symbol_pressed,i-1))
            imagebutton:
                focus_mask True
                idle "pb_button_1_idle"
                hover "pb_button_1_hover"
                action (Function(pb_play_flip), Function(pb_push_2nd))
        elif puzzle_box_side == 2:

            imagebutton:
                focus_mask True
                if pb_3_lid_open[0]:
                    idle "pb3_lid1_open"
                    hover "pb3_lid1_open"
                else:
                    idle "pb3_lid1_close"
                    hover "pb3_lid1_close"
                action NullAction()
            imagebutton:
                focus_mask True
                if pb_3_lid_open[1]:
                    idle "pb3_lid2_open"
                    hover "pb3_lid2_open"
                else:
                    idle "pb3_lid2_close"
                    hover "pb3_lid2_close"
                action NullAction()
            imagebutton:
                focus_mask True
                if pb_3_lid_open[2]:
                    idle "pb3_lid3_open"
                    hover "pb3_lid3_open"
                else:
                    idle "pb3_lid3_close"
                    hover "pb3_lid3_close"
                action NullAction()
            imagebutton:
                focus_mask True
                if pb_3_lid_open[3]:
                    idle "pb3_lid4_open"
                    hover "pb3_lid4_open"
                else:
                    idle "pb3_lid4_close"
                    hover "pb3_lid4_close"
                action NullAction()
            imagebutton:
                focus_mask True
                if pb_3_lid_open[4]:
                    idle "pb3_lid5_open"
                    hover "pb3_lid5_open"
                else:
                    idle "pb3_lid5_close"
                    hover "pb3_lid5_close"
                action NullAction()

            if pb_3_lid_open[1]:
                hbox:
                    xalign 0.36
                    yalign 0.215
                    spacing 20 * persistent.scale_factor
                    for i in range(0,3):
                        imagebutton:
                            focus_mask True
                            if pb_3_buttons[0][i]:
                                idle "pb3_button_open_idle"
                                hover "pb3_button_open_hover"
                            else:
                                idle "pb3_button_close_idle"
                                hover "pb3_button_close_hover"
                            action (Function(play_pb_switch),SetDict(pb_3_buttons[0],i,not pb_3_buttons[0][i]),Function(pb_3_check))
            if pb_3_lid_open[2]:
                hbox:
                    xalign 0.642
                    yalign 0.215
                    spacing 20 * persistent.scale_factor
                    for i in range(0,3):
                        imagebutton:
                            focus_mask True
                            if pb_3_buttons[1][i]:
                                idle "pb3_button_open_idle"
                                hover "pb3_button_open_hover"
                            else:
                                idle "pb3_button_close_idle"
                                hover "pb3_button_close_hover"
                            action (Function(play_pb_switch),SetDict(pb_3_buttons[1],i,not pb_3_buttons[1][i]),Function(pb_3_check))
            if pb_3_lid_open[3]:
                hbox:
                    xalign 0.36
                    yalign 0.78
                    spacing 20 * persistent.scale_factor
                    for i in range(0,3):
                        imagebutton:
                            focus_mask True
                            if pb_3_buttons[2][i]:
                                idle "pb3_button_open_idle"
                                hover "pb3_button_open_hover"
                            else:
                                idle "pb3_button_close_idle"
                                hover "pb3_button_close_hover"
                            action (Function(play_pb_switch),SetDict(pb_3_buttons[2],i,not pb_3_buttons[2][i]),Function(pb_3_check))
            if pb_3_lid_open[4]:
                hbox:
                    xalign 0.642
                    yalign 0.78
                    spacing 20 * persistent.scale_factor
                    for i in range(0,3):
                        imagebutton:
                            focus_mask True
                            if pb_3_buttons[3][i]:
                                idle "pb3_button_open_idle"
                                hover "pb3_button_open_hover"
                            else:
                                idle "pb3_button_close_idle"
                                hover "pb3_button_close_hover"
                            action (Function(play_pb_switch),SetDict(pb_3_buttons[3],i,not pb_3_buttons[3][i]),Function(pb_3_check))

        elif puzzle_box_side == 3:

            imagebutton:
                focus_mask True
                if pb_button_pressed[puzzle_box_side]:
                    idle "pb_button_4_pressed"
                    hover "pb_button_4_pressed"
                    action Function(play_pb_failed_click)
                else:
                    idle "pb_button_4_idle"
                    hover "pb_button_4_hover"
                    if "final_button" in pb_button_unlockable and not final_button_unlocked:
                        action (Function(play_pb_open),SetDict(pb_button_pressed,puzzle_box_side,True),SetVariable("final_button_unlocked",True))
                    else:
                        action Function(play_pb_failed_click)
        elif puzzle_box_side == 4:

            vpgrid:
                xalign 0.515
                yalign 0.53
                spacing 158 * persistent.scale_factor
                cols 3
                for i in range(0,3):
                    for j in range(0,3):
                        imagebutton:
                            focus_mask True
                            idle "pb5_%d_idle" % pb_5_buttons[(i*3)+j]
                            if not pb_3_lid_open[1] and not pb_3_lid_open[3]:
                                hover "pb5_%d_hover" % pb_5_buttons[(i*3)+j]
                                action (Function(play_pb_switch),Function(pb5_pressed,(i*3)+j))
                            else:
                                hover "pb5_%d_idle" % pb_5_buttons[(i*3)+j]
                                action Function(play_pb_switch)
        else:

            hbox:
                xalign 0.501
                yalign 0.465
                spacing 1 * persistent.scale_factor
                yoffset 1 * persistent.scale_factor
                xoffset -1 * persistent.scale_factor
                for i in range(0,3):
                    imagebutton:
                        focus_mask True
                        idle "pb6_%s" % pb_6_3letters[i][pb_6_3count[i]]
                        hover "pb6_%s" % pb_6_3letters[i][pb_6_3count[i]]
                        action NullAction()
            hbox:
                xalign 0.50
                yalign 0.55
                spacing 1 * persistent.scale_factor
                xoffset 1 * persistent.scale_factor
                yoffset 1 * persistent.scale_factor
                for i in range(0,4):
                    imagebutton:
                        focus_mask True
                        idle "pb6_%s" % pb_6_4letters[i][pb_6_4count[i]]
                        hover "pb6_%s" % pb_6_4letters[i][pb_6_4count[i]]
                        action NullAction()
            hbox:
                xalign 0.5
                yalign 0.637
                spacing 1 * persistent.scale_factor
                xoffset 1 * persistent.scale_factor
                yoffset -1 * persistent.scale_factor
                for i in range(0,5):
                    imagebutton:
                        focus_mask True
                        idle "pb6_%s" % pb_6_5letters[i][pb_6_5count[i]]
                        hover "pb6_%s" % pb_6_5letters[i][pb_6_5count[i]]
                        action NullAction()
            imagebutton:
                focus_mask True
                if pb_button_pressed[puzzle_box_side]:
                    idle "pb_button_5_pressed"
                    hover "pb_button_5_pressed"
                    action Function(play_pb_failed_click)
                else:
                    idle "pb_button_5_idle"
                    hover "pb_button_5_hover"
                if "button5" in pb_button_unlockable and not pb_3_lid_open[2] and not pb_3_lid_open[4]:
                    action (Function(play_pb_open),SetDict(pb_button_pressed,puzzle_box_side,True),SetDict(pb_3_lid_open,2,True),SetDict(pb_3_lid_open,4,True))
                else:
                    action (Function(play_pb_failed_click),NullAction())
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

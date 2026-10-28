init python:

    def play_pb_failed_click():
        renpy.play("sound_effects/failed_click.mp3","sfx1")
    def play_pb_dial():
        renpy.play("sound_effects/season3/dial.mp3","sfx1")
    def play_pb_open():
        renpy.play("sound_effects/season3/pb_open.mp3","sfx1")
    def play_pb_switch():
        renpy.play("sound_effects/switch.mp3","sfx2")
    def pb_play_flip():
        renpy.play("sound_effects/season3/flick.mp3","sfx2")

    def pb_rotate_dials(_side):
        global pb_side1_dials
        global pb_button_unlockable
        global puzzle_box_side_unlocked
        
        if pb_side1_dials[_side] == 3:
            pb_side1_dials[_side] = 0
        else:
            pb_side1_dials[_side] +=1
        
        if _side == 0:
            affected_side = 3
        elif _side == 2:
            affected_side = 0
        else:
            pb_check_unlocked()
            return
        
        if pb_side1_dials[affected_side] == 3:
            pb_side1_dials[affected_side] = 0
        else:
            pb_side1_dials[affected_side] +=1
        
        pb_check_unlocked()
        return

    def pb_check_unlocked():
        global pb_side1_dials
        global pb_button_unlockable
        global puzzle_box_side_unlocked
        global pb_3_lid_open
        global final_button_unlocked
        
        if not puzzle_box_side_unlocked[1]:
            if pb_side1_dials[0] == 2 and pb_side1_dials[1] == 1 and pb_side1_dials[2] == 3 and pb_side1_dials[3] == 1:
                if "button1" not in pb_button_unlockable:
                    pb_button_unlockable.append("button1")
        else:
            while "button1" in pb_button_unlockable:
                pb_button_unlockable.remove("button1")
        
        if not pb_3_lid_open[0]:
            if pb_side1_dials[0] == 1 and pb_side1_dials[1] == 1 and pb_side1_dials[2] == 0 and pb_side1_dials[3] == 1:
                if "button2" not in pb_button_unlockable:
                    pb_button_unlockable.append("button2")
        else:
            while "button2" in pb_button_unlockable:
                pb_button_unlockable.remove("button2")
        
        if not puzzle_box_side_unlocked[4]:
            if pb_side1_dials[0] == 2 and pb_side1_dials[1] == 0 and pb_side1_dials[2] == 1 and pb_side1_dials[3] == 3:
                if "button3" not in pb_button_unlockable:
                    pb_button_unlockable.append("button3")
        else:
            while "button3" in pb_button_unlockable:
                pb_button_unlockable.remove("button3")
        
        if not puzzle_box_side_unlocked[5]:
            if pb_side1_dials[0] == 3 and pb_side1_dials[1] == 2 and pb_side1_dials[2] == 0 and pb_side1_dials[3] == 3:
                if "button4" not in pb_button_unlockable:
                    pb_button_unlockable.append("button4")
        else:
            while "button4" in pb_button_unlockable:
                pb_button_unlockable.remove("button4")
        
        if not final_button_unlocked and puzzle_box_side_unlocked[3]:
            if pb_side1_dials[0] == 1 and pb_side1_dials[1] == 1 and pb_side1_dials[2] == 2 and pb_side1_dials[3] == 2:
                if "final_button" not in pb_button_unlockable:
                    pb_button_unlockable.append("final_button")
        else:
            while "final_button" in pb_button_unlockable:
                pb_button_unlockable.remove("final_button")
        
        return

    def pb_push_2nd():
        global pb_2nd_count
        
        if pb_2nd_count < 10:
            pb_2nd_count += 1
        elif pb_2nd_count == 10:
            pb_2nd_count += 2
        else:
            pb_2nd_count = 0
        
        if pb_2nd_count == 4:
            pb_2nd_count = 7
        return

    def pb_3_check():
        global pb_3_buttons
        global puzzle_box_side_unlocked
        
        if pb_3_buttons == [[False,False,False],[True,True,False],[True,True,False],[False,False,False]] and not puzzle_box_side_unlocked[3]:
            play_pb_open()
            puzzle_box_side_unlocked[3] = True
        return

    def pb5_pressed(idx):
        global pb_5_buttons
        global pb_3_lid_open
        
        if pb_5_buttons[idx] < 8:
            pb_5_buttons[idx] += 2
        else:
            if pb_5_buttons[idx] == 8:
                pb_5_buttons[idx] = 1
            else:
                pb_5_buttons[idx] = 2
        
        if (pb_5_buttons[2] + pb_5_buttons[4] + pb_5_buttons[6] == 15) and (pb_5_buttons[0] + pb_5_buttons[3] + pb_5_buttons[6] == 15) and (pb_5_buttons[1] + pb_5_buttons[4] + pb_5_buttons[7] == 15) and (pb_5_buttons[2] + pb_5_buttons[5] + pb_5_buttons[8] == 15) and (pb_5_buttons[0] + pb_5_buttons[1] + pb_5_buttons[2] == 15) and (pb_5_buttons[3] + pb_5_buttons[4] + pb_5_buttons[5] == 15) and (pb_5_buttons[6] + pb_5_buttons[7] + pb_5_buttons[8] == 15) and (pb_5_buttons[0] + pb_5_buttons[4] + pb_5_buttons[8] == 15) and 1 in pb_5_buttons and 2 in pb_5_buttons and 3 in pb_5_buttons and 4 in pb_5_buttons and 5 in pb_5_buttons and 6 in pb_5_buttons and 7 in pb_5_buttons and 8 in pb_5_buttons and 9 in pb_5_buttons:        
            play_pb_open()
            pb_3_lid_open[1] = True
            pb_3_lid_open[3] = True
        return

    def pb_6_symbol_pressed(idx):
        global pb_6_3count
        global pb_6_4count
        global pb_6_5count
        if idx == 0:
            if pb_6_3count[0] < 3:
                pb_6_3count[0] += 1
            else:
                pb_6_3count[0] = 0
        elif idx == 4:
            if pb_6_3count[1] < 3:
                pb_6_3count[1] += 1
            else:
                pb_6_3count[1] = 0
        elif idx == 7:
            if pb_6_3count[2] < 3:
                pb_6_3count[2] += 1
            else:
                pb_6_3count[2] = 0
        elif idx == 8:
            if pb_6_4count[0] < 3:
                pb_6_4count[0] += 1
            else:
                pb_6_4count[0] = 0
        elif idx == 11:
            if pb_6_4count[1] < 3:
                pb_6_4count[1] += 1
            else:
                pb_6_4count[1] = 0
        elif idx == 2:
            if pb_6_4count[2] < 3:
                pb_6_4count[2] += 1
            else:
                pb_6_4count[2] = 0
        elif idx == 1:
            if pb_6_4count[3] < 3:
                pb_6_4count[3] += 1
            else:
                pb_6_4count[3] = 0
        elif idx == 6:
            if pb_6_5count[0] < 3:
                pb_6_5count[0] += 1
            else:
                pb_6_5count[0] = 0
        elif idx == 10:
            if pb_6_5count[1] < 3:
                pb_6_5count[1] += 1
            else:
                pb_6_5count[1] = 0
        elif idx == 9:
            if pb_6_5count[2] < 3:
                pb_6_5count[2] += 1
            else:
                pb_6_5count[2] = 0
        elif idx == 5:
            if pb_6_5count[3] < 3:
                pb_6_5count[3] += 1
            else:
                pb_6_5count[3] = 0
        else:
            if pb_6_5count[4] < 3:
                pb_6_5count[4] += 1
            else:
                pb_6_5count[4] = 0
        pb_6_check()
        return

    def pb_6_check():
        global pb_6_3letters
        global pb_6_4letters
        global pb_6_5letters
        global pb_6_3count
        global pb_6_4count
        global pb_6_5count
        global pb_3_lid_open
        
        if pb_3_lid_open[2] and pb_3_lid_open[4]:
            return
        while "button5" in pb_button_unlockable:
            pb_button_unlockable.remove("button5")
        
        if pb_6_3letters[0][pb_6_3count[0]] == "s" and pb_6_3letters[1][pb_6_3count[1]] == "u" and pb_6_3letters[2][pb_6_3count[2]] == "n":
            if pb_6_4letters[0][pb_6_4count[0]] == "m" and pb_6_4letters[1][pb_6_4count[1]] == "o" and pb_6_4letters[2][pb_6_4count[2]] == "o" and pb_6_4letters[3][pb_6_4count[3]] == "n":
                if pb_6_5letters[0][pb_6_5count[0]] == "s" and pb_6_5letters[1][pb_6_5count[1]] == "t" and pb_6_5letters[2][pb_6_5count[2]] == "a" and pb_6_5letters[3][pb_6_5count[3]] == "r" and pb_6_5letters[4][pb_6_5count[4]] == "s":
                    if "button5" not in pb_button_unlockable:
                        pb_button_unlockable.append("button5")
                    else:
                        while "button5" in pb_button_unlockable:
                            pb_button_unlockable.remove("button5")
                    return
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

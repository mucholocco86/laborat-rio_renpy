init python:

    def bp_shot_nm(player,shot):
        global bp_cpu_chance
        global bp_cpu_ap
        global bp_player_chance_nm
        
        bp_player_chance_list = [min(80,renpy.random.randint(40,65)+bp_player_chance_nm),min(80,renpy.random.randint(45,50)+bp_player_chance_nm),min(80,renpy.random.randint(30,50)+bp_player_chance_nm)]
        
        if player:
            if renpy.random.randint(0,1) <= bp_player_chance_list[shot]:
                if shot == 2 and renpy.random.randint(0,100) <= 5:
                    bp_swat(False)
                else:
                    bp_player_chance_nm = 0
                    bp_hit(True,shot)
            else:
                bp_miss(True,shot)
        return

    def bp_def_nm(player,act):
        global bp_cpu_chance
        global bp_player_ap
        global bp_cpu_ap
        global bp_player_chance_nm
        if player:
            if act == 1:
                bp_cpu_chance[0] = max(bp_cpu_chance[0]-renpy.random.randint(5,10),0)
                bp_cpu_chance[1] = max(bp_cpu_chance[1]-renpy.random.randint(5,10),0)
                bp_cpu_chance[2] = max(bp_cpu_chance[2]-renpy.random.randint(5,10),0)
                bp_show_image("pc_tease")
            else:
                bp_player_chance_nm += 5
                bp_show_image("pc_focus")
        else:
            if act == 1:
                bp_player_chance_nm = max(0,bp_player_chance_nm-3)
                bp_show_image("cpu_tease")
            elif act == 2:
                bp_cpu_chance[0] = min(bp_cpu_chance[0]+renpy.random.randint(5,10),100)
                bp_cpu_chance[1] = min(bp_cpu_chance[1]+renpy.random.randint(5,10),100)
                bp_cpu_chance[2] = min(bp_cpu_chance[2]+renpy.random.randint(5,10),100)
                bp_show_image("cpu_focus")
            else:
                bp_cpu_ap = min(10,bp_cpu_ap+3)
                bp_show_image("cpu_rest")
        return

    def bp_hide_image_nm():
        global bp_showing_img
        global bp_state
        global bp_cpu_cue_strip
        global bp_mc_cue_strip
        global bp_cpu_cups_tmp
        global bp_cpu_cups
        
        bp_showing_img = False
        
        if bp_mc_cue_strip:
            bp_mc_cue_strip = False
            bp_show_image("pc_strip")
            return
        elif bp_cpu_cue_strip:
            bp_cpu_cue_strip = False
            bp_show_image("cpu_strip")
            return
        bp_cpu_cups = bp_cpu_cups_tmp
        if bp_state == 0:
            if bp_check_game_over():
                return
            bp_next_turn()
            bp_state = 1
        elif bp_state == 1:
            bp_state = 2
            bp_cpu_shot()
        elif bp_state == 2:
            bp_state = 3
            if bp_check_game_over():
                return
            bp_cpu_def_nm()
        else:
            bp_next_turn()
            bp_state = 0
        return

    def bp_cpu_def_nm():
        global bp_player_chance_nm
        global bp_cpu_ap
        global bp_cpu_chance
        
        if bp_player_chance_nm >= 10 and renpy.random.randint(0,100) < 50:
            bp_def_nm(False,1)
        elif (bp_cpu_chance[0] < 10 or bp_cpu_chance[1] < 10 or bp_cpu_chance[2] < 10) and renpy.random.randint(0,100) < 50:
            bp_def_nm(False,2)
        elif bp_cpu_ap < 6 and renpy.random.randint(0,100) < 50:
            bp_def_nm(False,3)
        else:
            if bp_cpu_ap < 8 and renpy.random.randint(0,100) < 50:
                bp_def_nm(False,3)
            elif renpy.random.randint(0,100) < 50:
                bp_def_nm(False,2)
            else:
                bp_def_nm(False,1)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:

    def bp_init_game(who,episode,lbl):
        global bp_cpu_name
        global bp_ep_suffix
        global bp_cpu_cups
        global bp_player_turn
        global bp_game_over
        global bp_player_won
        global bp_state
        global bp_img_list
        global bp_mc_strip_state
        global bp_cpu_strip_state
        global bp_player_chance
        global bp_cpu_chance
        global bp_player_cups
        global bp_player_ap
        global bp_cpu_ap
        global bp_action_msg
        global bp_jump_label
        global tmpInt
        global bp_player_chance_nm
        global bp_cpu_cups_tmp
        
        tmpInt = 0
        bp_jump_label = lbl
        bp_mc_strip_state = 0
        bp_cpu_strip_state = 0
        bp_game_over = False
        bp_player_won = False
        bp_action_msg = ""
        bp_ep_suffix = episode
        bp_cpu_name = who
        
        bp_player_ap = 10
        bp_cpu_ap = 10
        
        bp_state = 0
        bp_cpu_cups = 6
        bp_cpu_cups_tmp = 6
        bp_player_cups = 6
        bp_player_turn = True
        
        bp_img_list = []
        
        bp_img_list.append(["pc_tease"])
        bp_img_list.append(["cpu_tease"])
        bp_img_list.append(["pc_arc"])
        bp_img_list.append(["pc_fast"])
        bp_img_list.append(["pc_bounce"])
        bp_img_list.append(["cpu_arc"])
        bp_img_list.append(["cpu_fast"])
        bp_img_list.append(["cpu_bounce"])
        bp_img_list.append(["pc_miss"])
        bp_img_list.append(["cpu_miss"])
        bp_img_list.append(["pc_swat"])
        bp_img_list.append(["cpu_swat"])
        bp_img_list.append(["pc_focus"])
        bp_img_list.append(["pc_rest"])
        bp_img_list.append(["cpu_focus"])
        bp_img_list.append(["cpu_rest"])
        bp_img_list.append(["pc_strip"])
        bp_img_list.append(["cpu_strip"])
        
        bp_player_chance = [100,100,100]
        bp_player_chance_nm = 0
        
        if who == "Camila" and bp_ep_suffix == "ep10":
            bp_cpu_chance = [75,33,50]
            bp_img_list[0].append("mc_tease")
            
            bp_img_list[1].append("camila_tease")
            
            bp_img_list[2].append("mc_hit")
            bp_img_list[3].append("mc_hit")
            bp_img_list[4].append("player_bounce")
            
            bp_img_list[5].append("cpu_hit")
            bp_img_list[6].append("cpu_hit")
            bp_img_list[7].append("cpu_bounce")
            
            bp_img_list[8].append("mc_miss")
            bp_img_list[9].append("cpu_miss")
            bp_img_list[10].append("player_swat_ep10")
            bp_img_list[11].append("camila_swat_ep10")
            bp_img_list[12].append("mc_focus")
            bp_img_list[13].append("mc_rest")
            bp_img_list[14].append("camila_focus")
            bp_img_list[15].append("camila_rest")
            bp_img_list[16].append("mc_strip")
            bp_img_list[17].append("camila_strip")
        elif who == "Sage" and bp_ep_suffix == "ep10":
            bp_cpu_chance = [75,33,50]
            bp_img_list[0].append("mc_tease")
            
            bp_img_list[1].append("sage_tease")
            
            bp_img_list[2].append("mc_hit")
            bp_img_list[3].append("mc_hit")
            bp_img_list[4].append("player_bounce")
            
            bp_img_list[5].append("cpu_hit")
            bp_img_list[6].append("cpu_hit")
            bp_img_list[7].append("cpu_bounce")
            
            bp_img_list[8].append("mc_miss")
            bp_img_list[9].append("cpu_miss")
            bp_img_list[10].append("player_swat_ep10")
            bp_img_list[11].append("sage_swat_ep10")
            bp_img_list[12].append("mc_focus")
            bp_img_list[13].append("mc_rest")
            bp_img_list[14].append("sage_focus")
            bp_img_list[15].append("sage_rest")
            bp_img_list[16].append("mc_strip")
            bp_img_list[17].append("sage_strip")
        elif who == "Josy" and bp_ep_suffix == "ep10":
            bp_cpu_chance = [75,33,50]
            bp_img_list[0].append("mc_tease")
            
            bp_img_list[1].append("josy_tease")
            
            bp_img_list[2].append("mc_hit")
            bp_img_list[3].append("mc_hit")
            bp_img_list[4].append("player_bounce")
            
            bp_img_list[5].append("cpu_hit")
            bp_img_list[6].append("cpu_hit")
            bp_img_list[7].append("cpu_bounce")
            
            bp_img_list[8].append("mc_miss")
            bp_img_list[9].append("cpu_miss")
            bp_img_list[10].append("player_swat_ep10")
            bp_img_list[11].append("josy_swat_ep10")
            bp_img_list[12].append("mc_focus")
            bp_img_list[13].append("mc_rest")
            bp_img_list[14].append("josy_focus")
            bp_img_list[15].append("josy_rest")
            bp_img_list[16].append("mc_strip")
            bp_img_list[17].append("josy_strip")
        elif who == "Jill" and bp_ep_suffix == "ep10":
            bp_cpu_chance = [75,33,50]
            bp_img_list[0].append("mc_tease")
            
            bp_img_list[1].append("jill_tease")
            
            bp_img_list[2].append("mc_hit")
            bp_img_list[3].append("mc_hit")
            bp_img_list[4].append("player_bounce")
            
            bp_img_list[5].append("cpu_hit")
            bp_img_list[6].append("cpu_hit")
            bp_img_list[7].append("cpu_bounce")
            
            bp_img_list[8].append("mc_miss")
            bp_img_list[9].append("cpu_miss")
            bp_img_list[10].append("player_swat_ep10")
            bp_img_list[11].append("jill_swat_ep10")
            bp_img_list[12].append("mc_focus")
            bp_img_list[13].append("mc_rest")
            bp_img_list[14].append("jill_focus")
            bp_img_list[15].append("jill_rest")
            bp_img_list[16].append("mc_strip")
            bp_img_list[17].append("jill_strip")
        elif who == "Isabella" and bp_ep_suffix == "ep10":
            bp_cpu_chance = [90,45,75]
            bp_img_list[0].append("mc_tease_bella")
            
            bp_img_list[1].append("isabella_tease")
            
            bp_img_list[2].append("mc_hit_bella")
            bp_img_list[3].append("mc_hit_bella")
            bp_img_list[4].append("player_bounce_bella")
            
            bp_img_list[5].append("cpu_hit_bella")
            bp_img_list[6].append("cpu_hit_bella")
            bp_img_list[7].append("cpu_bounce_bella")
            
            bp_img_list[8].append("mc_miss_bella")
            bp_img_list[9].append("cpu_miss_bella")
            bp_img_list[10].append("player_swat_bella_ep10")
            bp_img_list[11].append("isabella_swat_ep10")
            bp_img_list[12].append("mc_focus_bella")
            bp_img_list[13].append("mc_rest_bella")
            bp_img_list[14].append("isabella_focus")
            bp_img_list[15].append("isabella_rest")
            bp_img_list[16].append("mc_strip_bella")
            bp_img_list[17].append("isabella_strip")
        elif who == "Isabella" and bp_ep_suffix == "ep11":
            bp_cpu_chance = [90,45,75]
            bp_img_list[0].append("mc_tease_bella_ep11")
            
            bp_img_list[1].append("isabella_tease_ep11")
            
            bp_img_list[2].append("mc_hit_bella_ep11")
            bp_img_list[3].append("mc_hit_bella_ep11")
            bp_img_list[4].append("player_bounce_bella_ep11")
            
            bp_img_list[5].append("cpu_hit_bella_ep11")
            bp_img_list[6].append("cpu_hit_bella_ep11")
            bp_img_list[7].append("cpu_bounce_bella_ep11")
            
            bp_img_list[8].append("mc_miss_bella_ep11")
            bp_img_list[9].append("cpu_miss_bella_ep11")
            bp_img_list[10].append("player_swat_bella_ep11")
            bp_img_list[11].append("isabella_swat_ep11")
            bp_img_list[12].append("mc_focus_bella_ep11")
            bp_img_list[13].append("mc_rest_bella_ep11")
            bp_img_list[14].append("isabella_focus_ep11")
            bp_img_list[15].append("isabella_rest_ep11")
            bp_img_list[16].append("mc_strip_bella_ep11")
            bp_img_list[17].append("isabella_strip_ep11")
        
        return


    def bp_shot(player,shot):
        global bp_player_chance
        global bp_cpu_chance
        global bp_player_ap
        global bp_cpu_ap
        
        if player:
            if shot == 0:
                bp_player_ap -= 6
            elif shot == 2:
                bp_player_ap -= 3
            if renpy.random.randint(0,100) <= bp_player_chance[shot]:
                if shot == 2 and renpy.random.randint(0,100) <= 50:
                    bp_swat(False)
                else:
                    bp_hit(True,shot)
            else:
                bp_miss(True,shot)
        else:
            if shot == 0:
                bp_cpu_ap -= 6
            elif shot == 2:
                bp_cpu_ap -= 3
            if renpy.random.randint(0,100) <= bp_cpu_chance[shot]:
                if shot == 2 and renpy.random.randint(0,100) <= 50:
                    bp_swat(True)
                else:
                    bp_hit(False,shot)
            else:
                bp_miss(False,shot)
        return

    def bp_hit(player,shot):
        global bp_cpu_cups
        global bp_player_cups
        global bp_cpu_strip_state
        global bp_mc_strip_state
        global bp_cpu_cue_strip
        global bp_mc_cue_strip
        global bp_cpu_cups_tmp
        bp_cpu_cups_tmp = bp_cpu_cups
        if player:
            if shot == 2:
                bp_cpu_cups_tmp = max(bp_cpu_cups-2,0)
            else:
                bp_cpu_cups_tmp = bp_cpu_cups - 1
            
            if bp_cpu_cups_tmp < 5 and bp_cpu_strip_state == 0:
                bp_cpu_cue_strip = True
                bp_cpu_strip_state += 1
            elif bp_cpu_cups_tmp < 3 and bp_cpu_strip_state == 1:
                bp_cpu_cue_strip = True
                bp_cpu_strip_state += 1
            
            if shot == 0:
                bp_show_image("pc_arc")
            elif shot == 1:
                bp_show_image("pc_fast")
            else:
                bp_show_image("pc_bounce")
        else:
            if shot == 2:
                bp_player_cups = max(bp_player_cups-2,0)
            else:
                bp_player_cups -= 1
            
            if bp_player_cups < 5 and bp_mc_strip_state == 0:
                bp_mc_cue_strip = True
                bp_mc_strip_state += 1
            elif bp_player_cups < 3 and bp_mc_strip_state == 1:
                bp_mc_cue_strip = True
                bp_mc_strip_state += 1
            
            if shot == 0:
                bp_show_image("cpu_arc")
            elif shot == 1:
                bp_show_image("cpu_fast")
            else:
                bp_show_image("cpu_bounce")
        return

    def bp_miss(player,shot):
        if player:
            bp_show_image("pc_miss")
        else:
            bp_show_image("cpu_miss")
        return

    def bp_swat(player_swatted):
        if player_swatted:
            bp_show_image("pc_swat")
        else:
            bp_show_image("cpu_swat")
        return

    def bp_check_game_over():
        global bp_game_over
        global bp_cpu_cups
        global bp_player_cups
        global bp_player_won
        global bp_jump_label
        if bp_cpu_cups == 0:
            bp_game_over = True
            bp_player_won = True
            renpy.jump(bp_jump_label)
        elif bp_player_cups == 0:
            bp_game_over = True
            bp_player_won = False
            renpy.jump(bp_jump_label)
        
        return False

    def bp_next_turn():
        global bp_player_turn
        bp_player_turn = not bp_player_turn
        return

    def bp_def(player,act):
        global bp_cpu_chance
        global bp_player_chance
        global bp_player_ap
        global bp_cpu_ap
        if player:
            if act == 1:
                bp_cpu_chance[0] = max(bp_cpu_chance[0]-renpy.random.randint(5,10),0)
                bp_cpu_chance[1] = max(bp_cpu_chance[1]-renpy.random.randint(5,10),0)
                bp_cpu_chance[2] = max(bp_cpu_chance[2]-renpy.random.randint(5,10),0)
                bp_show_image("pc_tease")
            elif act == 2:
                bp_player_chance[0] = min(bp_player_chance[0]+renpy.random.randint(5,10),100)
                bp_player_chance[1] = min(bp_player_chance[1]+renpy.random.randint(5,10),100)
                bp_player_chance[2] = min(bp_player_chance[2]+renpy.random.randint(5,10),100)
                bp_show_image("pc_focus")
            else:
                bp_player_ap = min(10,bp_player_ap+3)
                bp_show_image("pc_rest")
        else:
            if act == 1:
                bp_player_chance[0] = max(bp_player_chance[0]-renpy.random.randint(5,10),0)
                bp_player_chance[1] = max(bp_player_chance[1]-renpy.random.randint(5,10),0)
                bp_player_chance[2] = max(bp_player_chance[2]-renpy.random.randint(5,10),0)
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

    def bp_cpu_shot():
        global bp_cpu_chance
        global bp_player_chance
        global bp_cpu_ap
        global bp_player_ap
        global bp_player_cups
        global bp_cpu_cups
        
        if bp_cpu_ap >=6:
            if bp_cpu_chance[0] >= bp_cpu_chance[2] + 15 and bp_cpu_chance[0] > bp_cpu_chance[1] and renpy.random.randint(0,100) < 60:
                bp_shot(False,0)
            elif bp_player_cups > 1 and bp_cpu_chance[2] >= bp_cpu_chance[1] + 15 and renpy.random.randint(0,100) < 60:
                bp_shot(False,2)
            else:
                if renpy.random.randint(0,100) < 60:
                    bp_shot(False,0)
                elif renpy.random.randint(0,100) < 60:
                    bp_shot(False,2)
                else:
                    bp_shot(False,1)
        elif bp_cpu_ap >=3:
            if bp_cpu_chance[1] >= bp_cpu_chance[2]:
                bp_shot(False,1)
            elif bp_player_cups == 1 and bp_cpu_chance[1] > 10:
                bp_shot(False,1)
            elif renpy.random.randint(0,100) < 50:
                bp_shot(False,2)
            else:
                bp_shot(False,1)
        else:
            bp_shot(False,1)


    def bp_cpu_def():
        global bp_player_chance
        global bp_cpu_chance
        global bp_player_ap
        global bp_cpu_ap
        
        if (bp_player_chance[0] > 30 and bp_player_chance[1] > 30 and bp_player_chance[2] > 30) and bp_player_ap > 3 and renpy.random.randint(0,100) < 50:
            bp_def(False,1)
        elif (bp_cpu_chance[0] < 10 or bp_cpu_chance[1] < 10 or bp_cpu_chance[2] < 10) and renpy.random.randint(0,100) < 50:
            bp_def(False,2)
        elif bp_cpu_ap < 6 and renpy.random.randint(0,100) < 50:
            bp_def(False,3)
        else:
            if bp_cpu_ap < 8 and renpy.random.randint(0,100) < 50:
                bp_def(False,3)
            elif renpy.random.randint(0,100) < 50:
                bp_def(False,2)
            else:
                bp_def(False,1)
        return


    def bp_show_image(img):
        global bp_showing_img
        global bp_img_list
        global bp_img_name
        global bp_ep_suffix
        global bp_player_cups
        global bp_cpu_cups
        global tmpInt2
        global bp_dlg_list
        global bp_who_list
        global bp_delay
        global bp_dlg
        global bp_force_delay
        global bp_action_msg
        global bp_cpu_name
        global bp_cpu_cups_tmp
        
        if img == "pc_rest" or img == "cpu_rest" or img == "pc_focus" or img == "cpu_focus" or img == "pc_tease" or img == "cpu_tease":
            idx = list(map(itemgetter(0), bp_img_list)).index(img)
            
            tmpInt = renpy.random.randint(1,len(bp_img_list[idx])-1)
            
            bp_dlg_list = []
            bp_who_list = []
            
            if img == "pc_tease":
                
                if bp_player_cups < 3:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_3"
                elif bp_player_cups < 5:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_2"
                else:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_1"
                
                bp_get_tease(True)
                bp_delay = 0.5
                bp_action_msg = "You teased [bp_cpu_name]."
            elif img == "cpu_tease":
                if bp_cpu_cups < 3:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_3"
                    if bp_cpu_name == "Sage" and bp_ep_suffix == "ep10":
                        if renpy.random.randint(0,100) <= 50:
                            bp_img_name += "a"
                        else:
                            bp_img_name += "b"
                    elif bp_cpu_name == "Josy" and bp_ep_suffix == "ep10":
                        if renpy.random.randint(0,100) <= 50:
                            bp_img_name += "a"
                        else:
                            bp_img_name += "b"
                elif bp_cpu_cups < 5:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_2"
                else:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_1"
                bp_get_tease(False)
                bp_delay = 0.5
                bp_action_msg = "[bp_cpu_name] teased you."
            elif img == "cpu_focus":
                if bp_cpu_name == "Jill" and bp_ep_suffix == "ep10":
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt]
                else:
                    if bp_cpu_cups < 3:
                        bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_3"
                    elif bp_cpu_cups < 5:
                        bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_2"
                    else:
                        bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_1"
                bp_get_focus(False)
                bp_delay = 0.5
                bp_action_msg = "[bp_cpu_name] focused."
            elif img == "pc_focus":
                if bp_player_cups < 3:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_3"
                elif bp_player_cups < 5:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_2"
                else:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_1"
                bp_get_focus(True)
                bp_delay = 0.5
                bp_action_msg = "You focused."
            elif img == "pc_rest":
                if bp_player_cups < 3:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_3"
                elif bp_player_cups < 5:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_2"
                else:
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_1"
                bp_get_rest(True)
                bp_delay = 0.5
                bp_action_msg = "You rested."
            elif img == "cpu_rest":
                if bp_cpu_name == "Jill" and bp_ep_suffix == "ep10":
                    bp_img_name = "bp_" + bp_img_list[idx][tmpInt]
                else:
                    if bp_cpu_cups < 3:
                        bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_3"
                    elif bp_cpu_cups < 5:
                        bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_2"
                    else:
                        bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_1"
                bp_get_rest(False)
                bp_delay = 0.5
                bp_action_msg = "[bp_cpu_name] rested."
        else:
            idx = list(map(itemgetter(0), bp_img_list)).index(img)
            
            tmpInt = renpy.random.randint(1,len(bp_img_list[idx])-1)
            
            if img == "cpu_arc" or img == "cpu_fast":
                tmpInt2 = bp_player_cups + 1
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_[tmpInt2]"
                bp_delay = 0.5
                bp_get_hit(False, 0)
                if img == "cpu_fast":
                    bp_action_msg = "[bp_cpu_name] threw a fastball."
                else:
                    bp_action_msg = "[bp_cpu_name] threw an arc shot."
                bp_play_splash(0,0,0)
            elif img == "cpu_bounce":
                bp_force_delay = True
                tmpInt2 = bp_player_cups + 2
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_[tmpInt2]"
                bp_delay = 0.5
                bp_get_hit(False, 2)
                bp_action_msg = "[bp_cpu_name] threw a bounce shot."
                bp_play_bounce_shot(0,0,0)
            elif img == "pc_arc" or img == "pc_fast":
                tmpInt2 = bp_cpu_cups
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_[tmpInt2]"
                bp_delay = 0.5
                bp_get_hit(True, 0)
                if img == "pc_arc":
                    bp_action_msg = "You threw an arc shot."
                else:
                    bp_action_msg = "You threw a fastball."
                bp_play_splash(0,0,0)
            elif img == "pc_bounce":
                bp_force_delay = True
                tmpInt2 = bp_cpu_cups
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_[tmpInt2]"
                bp_delay = 0.5
                bp_get_hit(True, 2)
                bp_action_msg = "You threw a bounce shot."
                bp_play_bounce_shot(0,0,0)
            elif img == "pc_strip":
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_[bp_mc_strip_state]"
                bp_delay = 0.5
                bp_get_strip(True)
                if bp_cpu_name == "Isabella" and bp_ep_suffix == "ep11":
                    bp_action_msg = "She's getting closer!"
                else:
                    bp_action_msg = "You have to strip!"
            elif img == "cpu_strip":
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt] + "_[bp_cpu_strip_state]"
                bp_delay = 0.5
                bp_get_strip(False)
                if bp_cpu_name == "Isabella" and bp_ep_suffix == "ep11":
                    bp_action_msg = "One step closer to victory!"
                elif bp_cpu_name == "Jill" and bp_ep_suffix == "ep10":
                    bp_action_msg = "[bp_cpu_name] doesn't strip."
                else:
                    bp_action_msg = "[bp_cpu_name] has to strip!"
            elif img == "cpu_miss":
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt]
                bp_delay = 0.5
                bp_get_miss(False)
                bp_action_msg = "[bp_cpu_name] missed!"
                bp_play_bounce(0,0,0)
            elif img == "pc_miss":
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt]
                bp_delay = 0.5
                bp_get_miss(True)
                bp_action_msg = "You missed!"
                bp_play_bounce(0,0,0)
            elif img == "pc_swat":
                bp_force_delay = True
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt]
                bp_delay = 0.5
                bp_get_swat(True)
                bp_action_msg = "[bp_cpu_name] threw a bounce shot."
                bp_play_swat(0,0,0)
            elif img == "cpu_swat":
                bp_force_delay = True
                bp_img_name = "bp_" + bp_img_list[idx][tmpInt]
                bp_delay = 0.5
                bp_get_swat(False)
                bp_action_msg = "You threw a bounce shot."
                bp_play_swat(0,0,0)
        
        bp_showing_img = True
        bp_dlg = 0
        renpy.show_screen("bp_say_screen")
        return

    def bp_hide_image():
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
            bp_cpu_def()
        else:
            bp_next_turn()
            bp_state = 0
        return


    def bp_get_tease(player):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            bp_who_list.append("{color=#ffaf05}[name]{/color}")
            
            ind =  renpy.random.randint(0,9)
            if bp_ep_suffix == "ep11":
                if ind == 0:
                    bp_dlg_list.append("I'm looking forward to the change in dress code. Aren't you?")
                elif ind == 1:
                    bp_dlg_list.append("I can't wait for the moment we all remove our bras together.")
                elif ind == 2:
                    bp_dlg_list.append("No pressure. However, that shot could seal the fate of ten breasts.")
                elif ind == 3:
                    bp_dlg_list.append("Your aim is way off. You don't even have to throw for me to see that.")
                elif ind == 4:
                    bp_dlg_list.append("Why did you make this bet, Bella? It was reckless of you.")
                elif ind == 5:
                    bp_dlg_list.append("This bra is chafing. It's gonna feel good to remove it.")
                elif ind == 6:
                    bp_dlg_list.append("Bra-boy has the power to make everyone braless. What a fitting superpower.")
                elif ind == 7:
                    bp_dlg_list.append("Wanna back out of the bet yet?")
                elif ind == 8:
                    bp_dlg_list.append("Bella! Over here! Bella!")
                else:
                    bp_dlg_list.append("All of you look very nervous. Haha!")
            else:
                if ind == 0:
                    bp_dlg_list.append("Is the table leaning, or is it just me? You should aim a bit to the right.")
                elif ind == 1:
                    bp_dlg_list.append("You're so not gonna hit this next shot.")
                elif ind == 2:
                    bp_dlg_list.append("You're not gonna do a bounce shot, are you? I'm ready to swat it. Just saying.")
                elif ind == 3:
                    bp_dlg_list.append("You look a bit nervous. I wonder why that is.")
                elif ind == 4:
                    bp_dlg_list.append("That ball is pretty big for these cups, don't you think? It makes it hard to hit them.")
                elif ind == 5:
                    bp_dlg_list.append("No pressure... Don't miss, though.")
                elif ind == 6:
                    bp_dlg_list.append("If you miss now, I will probably win.")
                elif ind == 7:
                    bp_dlg_list.append("Try a fast shot. They're pretty easy to make.")
                elif ind == 8:
                    bp_dlg_list.append("If you focus too much, you'll end up missing.")
                else:
                    bp_dlg_list.append("How about throwing with your other hand? It might be more accurate.")
        
        else:
            if bp_cpu_name == "Camila":
                bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,9)
                if ind == 0:
                    bp_dlg_list.append("Get ready to strip, cutie.")
                elif ind == 1:
                    bp_dlg_list.append("It's cold outside, don't you think?")
                elif ind == 2:
                    bp_dlg_list.append("It's hard hitting the cup when you're imagining me naked, isn't it?")
                elif ind == 3:
                    bp_dlg_list.append("I've never seen anyone more desperate to hit a ball in a cup. My tits make you excited, don't they?")
                elif ind == 4:
                    bp_dlg_list.append("No pressure, [name], but everyone's watching you undress.")
                elif ind == 5:
                    bp_dlg_list.append("It's time to strip. Show me some skin, [name].")
                elif ind == 6:
                    bp_dlg_list.append("Your clothes look better off than on, I think.")
                elif ind == 7:
                    bp_dlg_list.append("Don't let my body distract you. Hit the cup, [name].")
                elif ind == 8:
                    bp_dlg_list.append("Show me your ding dong, [name]. Haha!")
                else:
                    bp_dlg_list.append("You're gonna miss that shot.")
            elif bp_cpu_name == "Sage":
                bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,9)
                if ind == 0:
                    bp_dlg_list.append("I'll make you regret that you challenged me.")
                elif ind == 1:
                    bp_dlg_list.append("Keep it in your pants, [name]. At least until I win.")
                elif ind == 2:
                    bp_dlg_list.append("You're so kinky, [name]. I didn't know you wanted to strip in front of everyone.")
                elif ind == 3:
                    bp_dlg_list.append("Get ready to get naked.")
                elif ind == 4:
                    bp_dlg_list.append("Look at you focusing hard. It doesn't matter, though. You're still going to miss.")
                elif ind == 5:
                    bp_dlg_list.append("I don't think you will hit the cup. That shot will fly over it.")
                elif ind == 6:
                    bp_dlg_list.append("Look at my body for good luck, [name]. I hope it's not distracting you.")
                elif ind == 7:
                    bp_dlg_list.append("Do you want me to strip for you? That won't happen when you keep missing your shots.")
                elif ind == 8:
                    bp_dlg_list.append("[name]. Look over here. [name]!")
                else:
                    bp_dlg_list.append("Everyone's watching you miss that shot, and soon, they'll also see you strip.")
            elif bp_cpu_name == "Josy":
                bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,9)
                if ind == 0:
                    bp_dlg_list.append("[name]! La-la-la-la! Miss the shot! La-la-la-la!")
                elif ind == 1:
                    bp_dlg_list.append("Come on, [name]... You're not hitting that shot, are you? Please?")
                elif ind == 2:
                    bp_dlg_list.append("I don't know why I agreed to this... But I know you won't make me remove my clothes out here... Right?")
                elif ind == 3:
                    bp_dlg_list.append("[name]... Miss on purpose. Pretty please?")
                elif ind == 4:
                    bp_dlg_list.append("How much do you want for missing the next shot?")
                elif ind == 5:
                    bp_dlg_list.append("Ok, I have decided that you won't make this next shot. So, you better not.")
                elif ind == 6:
                    bp_dlg_list.append("Be nice to me, [name]. Think about what you're doing before you hit a cup, ok?")
                elif ind == 7:
                    bp_dlg_list.append("It's cold outside... Should we stop playing?")
                elif ind == 8:
                    bp_dlg_list.append("Miss it! Miiiiiiss it!!!")
                else:
                    bp_dlg_list.append("Can we cut a deal or something? If I flash you real quick, can you miss your shots on purpose?")
            elif bp_cpu_name == "Jill":
                bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,9)
                if ind == 0:
                    bp_dlg_list.append("Are you going to show me how it's done or not?")
                elif ind == 1:
                    bp_dlg_list.append("I'm confused. I thought you said you were good at this game.")
                    bp_who_list.append("{color=#BCB88A}Sage{/color}")
                    bp_dlg_list.append("Oh! That sounded like trash talk to me, [name]. Haha!")
                elif ind == 2:
                    bp_dlg_list.append("Are these the cups you're trying to hit? Because it doesn't seem so.")
                elif ind == 3:
                    bp_dlg_list.append("It doesn't matter if you miss. I still like you.")
                elif ind == 4:
                    bp_dlg_list.append("The goal is to throw the ball into the cup, right? When will you show me how to do that?")
                elif ind == 5:
                    bp_dlg_list.append("You've got this, [name]. I believe in you.")
                    bp_who_list.append("{color=#BCB88A}Sage{/color}")
                    bp_dlg_list.append("You call that teasing? Jill, you gotta say he sucks and stuff.")
                elif ind == 6:
                    bp_dlg_list.append("If you miss this one, and I hit my next one... Does that mean I'm better than you at this game?")
                elif ind == 7:
                    bp_dlg_list.append("It's ok, [name]. I think this game is hard, too.")
                elif ind == 8:
                    bp_dlg_list.append("It's pretty easy to miss the cups, isn't it?")
                else:
                    bp_dlg_list.append("Maybe we should move the cups closer to each other? That way, we won't keep missing.")
            elif bp_cpu_name == "Isabella":
                bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,9)
                if bp_ep_suffix == "ep11":
                    if ind == 0:
                        bp_dlg_list.append("Why did you agree to be humiliated further, [name]?")
                    elif ind == 1:
                        bp_dlg_list.append("Hey, Thong-boy! How are you doing over there?")
                    elif ind == 2:
                        bp_dlg_list.append("Do you want a thong with lace or without?")
                    elif ind == 3:
                        bp_dlg_list.append("Oh, [name]... I've got you beat, but you don't know it yet.")
                    elif ind == 4:
                        bp_dlg_list.append("Does he look nervous, or is it just me?")
                        bp_who_list.append("{color=#BCB88A}Sage{/color}")
                        bp_dlg_list.append("He knows he's about to lose.")
                    elif ind == 5:
                        bp_dlg_list.append("That bra suits you. You'll be wearing it all night.")
                        bp_who_list.append("{color=#ffe9b9}Jill{/color}")
                        bp_dlg_list.append("I wonder if the thong will fit him as well as the bra. Haha!")
                    elif ind == 6:
                        bp_dlg_list.append("Are you going to throw or just sit there?")
                        bp_who_list.append("{color=#ff1c63}Josy{/color}")
                        bp_dlg_list.append("He's feeling the pressure now.")
                    elif ind == 7:
                        bp_dlg_list.append("You look distracted, [name]. Why is that?")
                    elif ind == 8:
                        bp_dlg_list.append("Nope. You're not going to make this shot.")
                        bp_who_list.append("{color=#a7f442}Maya{/color}")
                        bp_dlg_list.append("If you ask me, it looks like he lacks confidence in his shots.")
                    else:
                        bp_dlg_list.append("Wanna forfeit? You're not getting out of the bet, but maybe it will save you some humiliation to throw in the towel.")
                else:
                    if ind == 0:
                        bp_dlg_list.append("They called me Beer Pong Queen back in college. I think your nickname will be loser.")
                    elif ind == 1:
                        bp_dlg_list.append("Beer Pong is one of my hidden talents, [name]. And from the looks of it, it isn't one of yours.")
                    elif ind == 2:
                        bp_dlg_list.append("You definitely need training. I could help you suck less if you want.")
                    elif ind == 3:
                        bp_dlg_list.append("I can play with my left hand if you want. Although it won't make much of a difference. I'll still whoop your ass.")
                    elif ind == 4:
                        bp_dlg_list.append("Why would you want to play this game outside? Everyone would see your penis, you know.")
                    elif ind == 5:
                        bp_dlg_list.append("I suppose this is where I should talk some smack, but I pity you. You suck, [name].")
                    elif ind == 6:
                        bp_dlg_list.append("Do you regret challenging me to this game yet? No? Just wait.")
                    elif ind == 7:
                        bp_dlg_list.append("Maybe you should stick to games that don't involve balls? How about dominoes?")
                    elif ind == 8:
                        bp_dlg_list.append("You mock me for my glasses? It seems like you're the one in need of a pair.")
                    else:
                        bp_dlg_list.append("Your throws are pathetic. Try harder.")
        
        return

    def bp_get_focus(player):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            bp_who_list.append("{color=#ffaf05}[name]{/color}")
            
            ind =  renpy.random.randint(0,5)
            if ind == 0:
                bp_dlg_list.append("Get a grip... Don't lose this one.")
            elif ind == 1:
                bp_dlg_list.append("Come on, [name]... You got this.")
            elif ind == 2:
                bp_dlg_list.append("It's just a ball getting thrown into a cup... You can do this.")
            elif ind == 3:
                bp_dlg_list.append("Ok... The next throw is gonna be a direct hit... I can feel it.")
            elif ind == 4:
                bp_dlg_list.append("Focus...")
            else:
                bp_dlg_list.append("Don't overthink it. Aim and throw. Aim and throw...")
        
        else:
            if bp_cpu_name == "Camila":
                bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("Ugh... I'm feeling distracted. Come on, Cammy!")
                elif ind == 1:
                    bp_dlg_list.append("Breathe... The next throw will hit.")
                elif ind == 2:
                    bp_dlg_list.append("You can do this. [name]'s gonna strip butt naked for everyone...")
                elif ind == 3:
                    bp_dlg_list.append("*{i}Deep breath{/i}*")
                elif ind == 4:
                    bp_dlg_list.append("Be one with the ping pong ball, Cammy...")
                else:
                    bp_dlg_list.append("The ball goes into the cup... It's that simple.")
            elif bp_cpu_name == "Sage":
                bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("I will win. Failure is not an option.")
                elif ind == 1:
                    bp_dlg_list.append("It sucks that I can't cheat at this game... I will have to rely on my skills.")
                elif ind == 2:
                    bp_dlg_list.append("Oh, [name]... You don't know what you're in for. I'm not letting you win.")
                elif ind == 3:
                    bp_dlg_list.append("You know how to do this. Don't get nervous because there's stripping involved.")
                elif ind == 4:
                    bp_dlg_list.append("Don't look at [name]. Look at the cups. [name] will only try to make you lose focus.")
                else:
                    bp_dlg_list.append("Focus... Focus...")
            elif bp_cpu_name == "Josy":
                bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("Ok... I will hit this next shot. I can feel it.")
                elif ind == 1:
                    bp_dlg_list.append("Don't stress... You still have a chance to beat him.")
                elif ind == 2:
                    bp_dlg_list.append("You can do this... Come on. It's just a ping-pong ball in a cup. How hard can it be?")
                elif ind == 3:
                    bp_dlg_list.append("The ball is light, and that's what my throw should be, too. Not too hard, but also not too soft.")
                elif ind == 4:
                    bp_dlg_list.append("Look and aim. Don't just throw.")
                else:
                    bp_dlg_list.append("If [name] won't show me mercy, it's up to me to win.")
            elif bp_cpu_name == "Jill":
                bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("I can do this. I think if I stay relaxed when I throw it, it will be easier.")
                elif ind == 1:
                    bp_dlg_list.append("I think I can win. Would it be mean to win?")
                elif ind == 2:
                    bp_dlg_list.append("I think I'm starting to get the hang of this.")
                elif ind == 3:
                    bp_dlg_list.append("This isn't too hard. I thought it would be.")
                elif ind == 4:
                    bp_dlg_list.append("This is kind of fun. I didn't think I could do it, but I can.")
                else:
                    bp_dlg_list.append("Concentrate...")
            elif bp_cpu_name == "Isabella":
                bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if bp_ep_suffix == "ep11":
                    if ind == 0:
                        bp_dlg_list.append("I've got this...")
                    elif ind == 1:
                        bp_dlg_list.append("There's no way I'll lose.")
                    elif ind == 2:
                        bp_dlg_list.append("Don't celebrate too early... Finish the job first.")
                    elif ind == 3:
                        bp_dlg_list.append("He doesn't stand a chance. We both know it.")
                    elif ind == 4:
                        bp_dlg_list.append("Focus... You've got the upper hand. This is his first game of the night.")
                    else:
                        bp_dlg_list.append("Trust your muscle memory.")
                else:
                    if ind == 0:
                        bp_dlg_list.append("*{i}Mumbles{/i}* Does he really think he can beat the champ?")
                    elif ind == 1:
                        bp_dlg_list.append("I need to channel my college self. It's been too long since I played this. I've gotten sloppier.")
                    elif ind == 2:
                        bp_dlg_list.append("Remember how you did it in the past. You were famous for your accuracy.")
                    elif ind == 3:
                        bp_dlg_list.append("Go, Beer Pong Bella. Go.")
                    elif ind == 4:
                        bp_dlg_list.append("I'll make his clothes fly off faster than when we're having sex.")
                    else:
                        bp_dlg_list.append("I'll show him that there's truth to my words. I am the best at this game.")
        
        return
    def bp_get_rest(player):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            bp_who_list.append("{color=#ffaf05}[name]{/color}")
            
            ind =  renpy.random.randint(0,5)
            if ind == 0:
                bp_dlg_list.append("(Think about your own game. That's the only thing you can affect.)")
            elif ind == 1:
                bp_dlg_list.append("(Arc shots are better, but they require so much focus...)")
            elif ind == 2:
                bp_dlg_list.append("(If I hit a bounce shot, I can get rid of two cups with one shot.)")
            elif ind == 3:
                bp_dlg_list.append("(The fast shots aren't my friend... Maybe I should do fewer of them?)")
            elif ind == 4:
                bp_dlg_list.append("(I'm still in the game. If I concentrate, I can hit some great shots.)")
            else:
                bp_dlg_list.append("(The bounce shots are risky... They get swatted away if I'm unlucky.)")
        
        else:
            if bp_cpu_name == "Camila":
                bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("(Visualize him naked in front of you. You can do this, but you may have to play a bit dirty.)")
                elif ind == 1:
                    bp_dlg_list.append("(Hm... If I throw a bounce shot, I can make him lose two cups. Is it worth it?)")
                elif ind == 2:
                    bp_dlg_list.append("(Throwing it in an arc feels like it's the best way to do it.)")
                elif ind == 3:
                    bp_dlg_list.append("(Get some energy back, Cammy. This game isn't over yet.)")
                elif ind == 4:
                    bp_dlg_list.append("(I so wanna see him nude, and I'm sure others want me to win, too.)")
                else:
                    bp_dlg_list.append("(I'm not removing my panties in this game. No, sir. Not tonight.)")
            elif bp_cpu_name == "Sage":
                bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("(There's gotta be a way I can cheat... I guess I could tease him into oblivion.)")
                elif ind == 1:
                    bp_dlg_list.append("(As soon as he lowers his guard, I'll go for the bounce shot.)")
                elif ind == 2:
                    bp_dlg_list.append("(Don't let it get to you. It's just a simple game.)")
                elif ind == 3:
                    bp_dlg_list.append("(Those fucking fastballs are too hard for me. I need to shoot with an arc.)")
                elif ind == 4:
                    bp_dlg_list.append("(He's trying to rile you up. Don't let him. Turn the game around on him instead.)")
                else:
                    bp_dlg_list.append("(He expects me to lose, but I'll prove him wrong.)")
            elif bp_cpu_name == "Josy":
                bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("(I blame Maya for this... That stupid Dare Game is getting out of hand.)")
                elif ind == 1:
                    bp_dlg_list.append("(I don't want to strip naked out here... Everyone's gonna watch me do it.)")
                elif ind == 2:
                    bp_dlg_list.append("(How can I win this? Can I make him lose focus somehow?)")
                elif ind == 3:
                    bp_dlg_list.append("(What's the best way to throw the ball? Should I try bouncing it?)")
                elif ind == 4:
                    bp_dlg_list.append("(Next time, I'll make Maya do this.)")
                else:
                    bp_dlg_list.append("(Haha! I can't believe him. He's smiling at me. I didn't think he'd enjoy this, but apparently he does.)")
            elif bp_cpu_name == "Jill":
                bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("(I hope I'm not embarrassing him in front of his friends. But he wanted to play this...)")
                elif ind == 1:
                    bp_dlg_list.append("(He looks so cute when playing. I can't stop looking at him.)")
                elif ind == 2:
                    bp_dlg_list.append("(I should probably let him win. He's not going to remove all of his clothes if he loses...right?)")
                elif ind == 3:
                    bp_dlg_list.append("(Haha! Bianca would love this game. I can feel it. I bet she wouldn't have any issues with removing her clothes.)")
                elif ind == 4:
                    bp_dlg_list.append("(It's very exciting when people are watching us play. I'm having so much fun.)")
                else:
                    bp_dlg_list.append("(Oh, [name]. Please, win. You can do this!)")
            elif bp_cpu_name == "Isabella":
                bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                
                ind =  renpy.random.randint(0,5)
                if bp_ep_suffix == "ep11":
                    if ind == 0:
                        bp_dlg_list.append("(Take a deep breath. Relax your body and mind.)")
                    elif ind == 1:
                        bp_dlg_list.append("(He thought he would see everyone's breasts... Typical. I'll teach him a lesson.)")
                    elif ind == 2:
                        bp_dlg_list.append("(Losing is not an option.)")
                    elif ind == 3:
                        bp_dlg_list.append("(Don't get worked up. You've got this.)")
                    elif ind == 4:
                        bp_dlg_list.append("(I'll finish this quickly.)")
                    else:
                        bp_dlg_list.append("(Everyone is counting on me. I will not let them down.)")
                else:
                    if ind == 0:
                        bp_dlg_list.append("(Would he slap my bounce shot or not? His stance is telling me that he might.)")
                    elif ind == 1:
                        bp_dlg_list.append("(Ignore his attempts at getting inside your head. Focus on the task at hand.)")
                    elif ind == 2:
                        bp_dlg_list.append("(He's not winning this game. I know it. He knows it.)")
                    elif ind == 3:
                        bp_dlg_list.append("(He thought this was an easy way to see me naked. I'm about to prove him wrong.)")
                    elif ind == 4:
                        bp_dlg_list.append("(He is starting to crumble. And as he does, he'll miss even more shots.)")
                    else:
                        bp_dlg_list.append("(I've got this. There's no way I will lose.)")
        
        return
    def bp_get_miss(player):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            ind =  renpy.random.randint(0,10)
            if ind == 0:
                bp_who_list.append("{color=#ffaf05}[name]{/color}")
                bp_dlg_list.append("Dammit!")
            elif ind == 1:
                bp_who_list.append("{color=#ffaf05}[name]{/color}")
                bp_dlg_list.append("That was way off...")
            elif ind == 2:
                bp_who_list.append("{color=#ffaf05}[name]{/color}")
                bp_dlg_list.append("I need to get a grip... That wasn't even close.")
            elif ind == 3:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! Totally missed it!")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("FAIL!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Yes! Haha! You missed it!")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Oh! That was very close.")
                    bp_who_list.append("{color=#BCB88A}Sage{/color}")
                    bp_dlg_list.append("Haha! No, it wasn't.")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("WEAK!")
            elif ind == 4:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're not gonna win with those kinds of shots.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Boo! You suck!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("*{i}Phew{/i}* I thought that one would go in for a while.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Maybe next time you'll hit it.")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("A pathetic attempt from a pathetic player.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You know, words hurt...")
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Suck it up, bitch. All is fair during Beer Pong.")
            elif ind == 5:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! Yes!")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I think you need glasses, Grandpa.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I'm so lucky it missed.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Oh, no! I thought that one wouldn't miss.")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're so nervous you can't even come close to the cups now.")
            elif ind == 6:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Missed it!")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Are you trying to hit cups that aren't on the table or something? Sheesh!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Yes! Keep missing, [name]. Haha!")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Better luck next time!")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Is that the best you got? It's going to be a quick game if it is.")
            elif ind == 7:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I almost feel bad for you. Almost.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You throw like a girl!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Maya! Look! He missed it!")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That one seems to have missed.")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Loser.")
            elif ind == 8:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're not that good at this game, are you?")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That one was way off! What are you even aiming at?")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("La-la-la-la! Missed it!")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You missed it. Is it my turn?")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That's just sad.")
            elif ind == 9:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That's a miss! And now it's my turn.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Location: Grass. Population: All your ping pong balls.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Did you really miss it on purpose?")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Missed it.")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("It's rare for guys to suck this much at ball sports.")
            else:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Don't cry, [name], but that was way off target.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're playing like you want to lose. Not that I mind.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That shot was horrible. Haha!")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You almost got that one. I believe in you.")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("*{i}Yawn{/i}* I wish you'd at least put up a fight.")
        
        else:
            if bp_cpu_name == "Camila":
                ind =  renpy.random.randint(0,10)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Not even close, Cammy!")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("That's a miss.")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("What a fail!")
                elif ind == 3:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Did you aim or just chuck it?")
                elif ind == 4:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You must be drunk because that shot was nowhere near the cup.")
                elif ind == 5:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("What's wrong, Cammy? Did you give up already?")
                elif ind == 6:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Gah! What a bad shot.")
                elif ind == 7:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("How could I miss that one?")
                elif ind == 8:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I suck!")
                elif ind == 9:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No!!!")
                else:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That was just...bleh.")
            elif bp_cpu_name == "Sage":
                ind =  renpy.random.randint(0,10)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Oh, Sage. You call that a throw?")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Shouldn't you yell fore, or something after throwing that bad?")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Haha!")
                elif ind == 3:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("And it's out of here! Woho!")
                elif ind == 4:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You're supposed to hit the cups, Sage, not avoid them.")
                elif ind == 5:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You can throw again if you want because that doesn't really count as a shot to me.")
                elif ind == 6:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Gah! Fuck!")
                elif ind == 7:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No! That one is your fault! You distracted me.")
                elif ind == 8:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I can't believe that one didn't go in.")
                elif ind == 9:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("My fingers slipped! That damned ball is too slippery.")
                else:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Ugh... I can do better than that.")
            elif bp_cpu_name == "Josy":
                ind =  renpy.random.randint(0,10)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Should I feel bad that you missed?")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yikes! At least warn me before you throw that kinda shot.")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Josy, Josy, Josy... Are you getting nervous?")
                elif ind == 3:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("*{i}Sings{/i}* Get that ball out of here! Throw it like you just don't care!")
                elif ind == 4:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Almost. But really not.")
                elif ind == 5:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You're not good at this. Haha!")
                elif ind == 6:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Stop distracting me! Haha!")
                elif ind == 7:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No! Can't we say that it counted as a hit? Please?")
                elif ind == 8:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I don't know how to throw this stupid ball...")
                elif ind == 9:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Maya? Can you throw the next one instead of me?")
                    bp_who_list.append("{color=#a7f442}Maya{/color}")
                    bp_dlg_list.append("Haha! Nope. You're on your own.")
                else:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I hate this game.")
            elif bp_cpu_name == "Jill":
                ind =  renpy.random.randint(0,10)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("That was really close!")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Good throw, but your aim could be better.")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Try throwing it in an arc next time.")
                elif ind == 3:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Sorry, but that's a miss.")
                elif ind == 4:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Not that bad. Keep it up.")
                elif ind == 5:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("That was kinda close.")
                elif ind == 6:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Shoot!")
                elif ind == 7:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Aw... I'm trying here, but I just can't hit them.")
                elif ind == 8:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Am I throwing it right? Is there a better way to do it?")
                elif ind == 9:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No! Haha!")
                else:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Maybe next time I'll hit it.")
            elif bp_cpu_name == "Isabella":
                ind =  renpy.random.randint(0,10)
                if bp_ep_suffix == "ep11":
                    if ind == 0:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Look at that... You missed it.")
                    elif ind == 1:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Did you stop trying?")
                    elif ind == 2:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Way off!")
                    elif ind == 3:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("What are you aiming at? There's no cup over there.")
                    elif ind == 4:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You're not gonna win with those kinds of shots.")
                    elif ind == 5:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Do you want someone else to throw for you?")
                    elif ind == 6:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Dammit!")
                    elif ind == 7:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("You can't hit all of them.")
                    elif ind == 8:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Ok, that was a bad throw.")
                    elif ind == 9:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("*{i}Groans{/i}*")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Gah!")
                else:
                    if ind == 0:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Look at that... You missed it.")
                    elif ind == 1:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("The master missed it.")
                    elif ind == 2:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Way off!")
                    elif ind == 3:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Since you can't blame this one on wind, whose fault was it?")
                    elif ind == 4:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You're not gonna win with those kinds of shots.")
                    elif ind == 5:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("That one almost hit me.")
                    elif ind == 6:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Dammit!")
                    elif ind == 7:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("You can't hit all of them.")
                    elif ind == 8:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Shit...")
                    elif ind == 9:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("We're better than this...")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Gah!")
        
        return

    def bp_get_swat(player):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            ind =  renpy.random.randint(0,5)
            if ind == 0:
                bp_who_list.append("{color=#ffaf05}[name]{/color}")
                bp_dlg_list.append("Denied!")
            elif ind == 1:
                bp_who_list.append("{color=#ffaf05}[name]{/color}")
                bp_dlg_list.append("You got too greedy with that one.")
            elif ind == 2:
                bp_who_list.append("{color=#ffaf05}[name]{/color}")
                bp_dlg_list.append("Slapped that ball.")
            elif ind == 3:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No! Don't slap my ball! Haha!")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You slapped it? What the hell!?")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Don't do that!")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("What are you doing?")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I underestimated you. It's easy to do.")
            elif ind == 4:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No! I'm gonna get you for that one.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Oh! Fuck you! That's not cool.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Huh! You can do that? Isn't that cheating?")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Huh? That one was about to go in!")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Damn you!")
            else:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("That's so unfair!")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("No!!! You bastard!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I feel like you shouldn't be allowed to slap my balls.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're so good at that!")
                elif bp_cpu_name == "Isabella":
                    bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Ok. Now you got me mad.")
        
        else:
            if bp_cpu_name == "Camila":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Hey! Don't slap my ball.")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Come on... Dammit!")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("No! That one was going to hit!")
                elif ind == 3:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("And that's how I will slap your naked butt after I win! Haha!")
                elif ind == 4:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("What do the five fingers say to your ball? SLAP!")
                else:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Nice try! But I could see that bounce shot coming from a mile away.")
            elif bp_cpu_name == "Sage":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Hey! Don't slap my ball.")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Come on... Dammit!")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("No! That one was going to hit!")
                elif ind == 3:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Get that shit out of here! Haha!")
                elif ind == 4:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Nuh-uh! This is my house!")
                else:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You must be crazy if you think a bounce shot will work on me!")
            elif bp_cpu_name == "Josy":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Hey! Don't slap my ball.")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Come on... Dammit!")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("No! That one was going to hit!")
                elif ind == 3:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! That was legal, right? It bounced before I slapped it.")
                elif ind == 4:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Slappy-slappy!")
                else:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're so mean! Going for two cups like that. But not if I can help it.")
            elif bp_cpu_name == "Jill":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You did it! Nice slap!")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Haha! Nice job.")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("So close!")
                elif ind == 3:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! Did I do it right?")
                elif ind == 4:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Nice try!")
                else:
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Yes! I got it!")
            elif bp_cpu_name == "Isabella":
                ind =  renpy.random.randint(0,5)
                if bp_ep_suffix == "ep11":
                    if ind == 0:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You don't have to slap it that hard!")
                    elif ind == 1:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("No way...")
                    elif ind == 2:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("I didn't think you had those kinds of reflexes tonight.")
                    elif ind == 3:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("That's how I'll slap your cheeks when you put those thongs on.")
                    elif ind == 4:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("A bounce shot? Oh, please.")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Was that an intentional attempt at a bounce shot or just a miss?")
                else:
                    if ind == 0:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You don't have to slap it that hard!")
                    elif ind == 1:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Wow! That was so fast.")
                    elif ind == 2:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("The ball might break if you slap it that hard.")
                    elif ind == 3:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Pff! I saw right through that one.")
                    elif ind == 4:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Your bounce shots are weak!")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Did you think you could slip a bounce shot past me?")
        return

    def bp_get_strip(player):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            ind =  renpy.random.randint(0,5)
            if ind == 0:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Work it, [name]! Show me some skin!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Pff... This is nothing.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Everyone! Look! [name] is stripping! WOOOO!!!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You don't need to call everyone's attention, you know.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I can't believe I got you to strip!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yeah, yeah. You got me with that one.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You don't have to remove your clothes, [name].")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("No, no. It's part of the game. At least for me.")
                elif bp_cpu_name == "Isabella":
                    if bp_ep_suffix == "ep11":
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Don't worry, [name]. I'll find some matching thongs for you.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("It's not over yet.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("It's only a matter of time.")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("How about you save us both some time and remove everything?")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("I'm not throwing in the towel. I can still win.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Keep lying to yourself.")
            elif ind == 1:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Undress for me! Haha!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("It's pretty chilly outside.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("*{i}Whistles{/i}* Sexy!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Funny because I don't feel that way at the moment.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Look, Maya! I got him to strip! Haha!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Enjoy it while it lasts.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Oh! Did my shot make you remove your clothes?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yeah. Those are the rules.")
                elif bp_cpu_name == "Isabella":
                    if bp_ep_suffix == "ep11":
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("That splash means that you're losing.")
                        bp_who_list.append("{color=#BCB88A}Sage{/color}")
                        bp_dlg_list.append("Haha! Finish him!!!")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Come on...")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Strip, loser.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You're making me feel bad.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("I'm not done with you yet.")
            elif ind == 2:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Wooo!!! If I had some dollar bills on me, I'd throw them at you.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I accept credit cards, too.")
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Great! I'll swipe it between your buttcheeks after you're fully nude.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Girls? Who ordered the stripper? WOOO!!!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I'll make you eat those words.")
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I'll make you eat me. Haha!")
                    bp_who_list.append("{color=#a333a5}Elena{/color}")
                    bp_dlg_list.append("Haha! Chill, you two.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Aw... Better you than me, though.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("For now...")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Oh, my...")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Are you blushing?")
                elif bp_cpu_name == "Isabella":
                    if bp_ep_suffix == "ep11":
                        bp_who_list.append("{color=#ffe9b9}Jill{/color}")
                        bp_dlg_list.append("Yes! Haha! We're winning!")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("No, you're not...")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Your clothes. Remove them.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Give me a second...")
            elif ind == 3:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Bow-chicka-wow-wow!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You won that one, but not the next.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Everybody! Step right up! Watch the naked guy remove his clothes for you.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I'm not naked yet. But you will be!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! Maya! Look!")
                    bp_who_list.append("{color=#a7f442}Maya{/color}")
                    bp_dlg_list.append("Trust me, Josy, we're all looking.")
                    bp_who_list.append("{color=#ff99cc}Melanie{/color}")
                    bp_dlg_list.append("Haha! I'll drink to that.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yeah, yeah...")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Is this really how you play Beer Pong?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I think so.")
                elif bp_cpu_name == "Isabella":
                    if bp_ep_suffix == "ep11":
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Maya, can you do those chicken noises again?")
                        bp_who_list.append("{color=#a7f442}Maya{/color}")
                        bp_dlg_list.append("*{i}Chicken noises{/i}* Haha!")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You girls are mean...")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Don't say I didn't warn you.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You haven't won yet.")
            elif ind == 4:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You should consider doing that for a living, [name]. WOOO!!!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I don't think anyone would pay for that.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I hope you're wearing hot underwear, or it will be embarrassing for you.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I always do.")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I can get used to this. Haha!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("No, you won't.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("And the game ends when all your clothes are off?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yep.")
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I think you better win, then.")
                elif bp_cpu_name == "Isabella":
                    if bp_ep_suffix == "ep11":
                        bp_who_list.append("{color=#ff1c63}Josy{/color}")
                        bp_dlg_list.append("I was worried, but I feel confident you'll win now.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("This victory will feel extra sweet.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("It's not over until it's over.")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("I like the view.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("That's kind of sexist.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("No, it's not.")
            else:
                if bp_cpu_name == "Camila":
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Strip! Strip! Strip!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yeah, I'm gonna. Relax, Cammy.")
                elif bp_cpu_name == "Sage":
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Girls, you may look, but don't touch. [name] is all mine. Haha!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("What's wrong with you? Why would you want everyone to see me naked?")
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Says you!")
                elif bp_cpu_name == "Josy":
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I think I have a chance of winning!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Good that you think that because it's not true.")
                elif bp_cpu_name == "Jill":
                    bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Right... The clothes. I forgot about that part for a second.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You're pretty good at this game, Jill.")
                elif bp_cpu_name == "Isabella":
                    if bp_ep_suffix == "ep11":
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Thong Pong, was it?")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("I'm not putting on a thong!")
                        bp_who_list.append("{color=#BCB88A}Sage{/color}")
                        bp_dlg_list.append("You have to honor the bet when you lose!")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Did you expect anything else?")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("You'll see what I expected when I win.")
        else:
            if bp_cpu_name == "Camila":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("That looks cold, Cammy. I'll give you an out if you wanna stop playing.")
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Not needed, [name]. And I won't give you the same offer when it's your turn to strip.")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Where's the dance, Cammy? I thought you'd be dancing too.")
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! You wish!")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("There we go! Whoop whoop!")
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Enjoy it while it lasts. I'll get the last laugh.")
                elif ind == 3:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You're so enjoying this, aren't you?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I think everyone here is enjoying it.")
                elif ind == 4:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Oh, well... I didn't expect all my clothes to stay on during the game.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You should have thought twice before challenging me.")
                else:
                    bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Wipe that smug look off your face. This isn't over yet, cutie.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("This smile isn't going anywhere, but the rest of your clothes are.")
            elif bp_cpu_name == "Sage":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Here we go. And I'm here for the show.")
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("If I see a phone taking pictures, I'll punch you.")
                elif ind == 1:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You got undressed fast. It was almost like you were prepared to strip.")
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("The only thing I'm prepared for is to kick your ass. You'll be stripping next.")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Wow... That's hot.")
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I hope you enjoy stripping with a boner, [name]. Because you're gonna.")
                elif ind == 3:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("You thought I wouldn't strip, didn't you?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I'm always happy to be proven wrong.")
                elif ind == 4:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I'll get you for this. Mark my words.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("It's not my fault you suck at hitting the cups, Sage.")
                else:
                    bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Fine! I'll strip!")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Hey, don't blame me. Blame yourself.")
            elif bp_cpu_name == "Josy":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Am I supposed to feel bad?")
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Actually, yes. Yes, you are.")
                elif ind == 1:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("I can't believe you got me to do this...")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You wanted to play, remember?")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("At least you don't have to feel ashamed of your body. Rawr!")
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Haha! That's not helping.")
                elif ind == 3:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Ugh... I blame Maya for this.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("And I'll thank her for it.")
                elif ind == 4:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Fine! Fine! I'll remove some clothes.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I wouldn't have it any other way.")
                else:
                    bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                    bp_dlg_list.append("Can we stop playing now? I feel it's about to get worse.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Yep, you're right about that. But sorry, we're finishing this game.")
            elif bp_cpu_name == "Jill":
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_who_list.append("{color=#BCB88A}Sage{/color}")
                    bp_dlg_list.append("This is where you normally strip, Jill.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Don't worry about it. You're not forced to do anything.")
                elif ind == 1:
                    bp_who_list.append("{color=#BCB88A}Sage{/color}")
                    bp_dlg_list.append("Poor [name]. He's missing out on nudity.")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("I saw Derek naked before. I'm good.")
                elif ind == 2:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Are you gonna get drunk from this?")
                elif ind == 3:
                    bp_who_list.append("{color=#d749ff}Lily{/color}")
                    bp_dlg_list.append("Why isn't she stripping?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("Because she doesn't have to.")
                elif ind == 4:
                    bp_who_list.append("{color=#d749ff}Lily{/color}")
                    bp_dlg_list.append("You're not gonna show any skin?")
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("We already said she wouldn't. We just wanted to play Beer Pong.")
                    bp_who_list.append("{color=#d749ff}Lily{/color}")
                    bp_dlg_list.append("You're still getting naked, right?")
                else:
                    bp_who_list.append("{color=#ffaf05}[name]{/color}")
                    bp_dlg_list.append("You don't have to drink all of it unless you want to.")
            elif bp_cpu_name == "Isabella":
                ind =  renpy.random.randint(0,5)
                if bp_ep_suffix == "ep11":
                    if ind == 0:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Would you look at that? How many cups do you have left?")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Perfect games are rare. Don't get too excited.")
                    elif ind == 1:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Wipe that smirk off your face.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("It will be even wider when we lose these bras together.")
                    elif ind == 2:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("The look on your faces is priceless.")
                        bp_who_list.append("{color=#ffe9b9}Jill{/color}")
                        bp_dlg_list.append("Bella, don't lose...")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("It's not game over yet.")
                    elif ind == 3:
                        bp_who_list.append("{color=#a7f442}Maya{/color}")
                        bp_dlg_list.append("No...")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Yep... I know you know what this means.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("This means nothing yet.")
                    elif ind == 4:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Dammit... Get a grip, Bella.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("I'd rather you don't.")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("I can't lose...")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Actually, I think you can.")
                        bp_who_list.append("{color=#ff1c63}Josy{/color}")
                        bp_dlg_list.append("Bella, don't give up!")
                else:
                    if ind == 0:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Did the amateur get the master to strip?")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Perfect games are rare. Don't get too excited.")
                    elif ind == 1:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("You don't suck as much as I thought you would.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("And you suck more than you think. Show me that skin.")
                    elif ind == 2:
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Aw, yeah. That's the stuff...")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("If you get a boner, it's game over.")
                    elif ind == 3:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Ugh...")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Don't frown. Part of you wants this.")
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("No, it's only you who wants this.")
                    elif ind == 4:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Dammit... Get a grip, Bella.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("I'd rather you don't.")
                    else:
                        bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                        bp_dlg_list.append("Maybe this will work in my favor. You look distracted.")
                        bp_who_list.append("{color=#ffaf05}[name]{/color}")
                        bp_dlg_list.append("Huh? What did you say?")
        return

    def bp_get_hit(player, shot):
        global bp_dlg_list
        global bp_who_list
        global bp_cpu_name
        global name
        global bp_ep_suffix
        
        bp_dlg_list = []
        bp_who_list = []
        ind = 0
        
        if player:
            bp_who_list.append("{color=#ffaf05}[name]{/color}")
            
            if shot == 2:
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("Yes! That's worth two cups!")
                elif ind == 1:
                    bp_dlg_list.append("The bounce shot went in! Yes!")
                elif ind == 2:
                    bp_dlg_list.append("I knew I would hit that bounce shot.")
                elif ind == 3:
                    bp_dlg_list.append("It was a gamble, but it paid off.")
                elif ind == 4:
                    bp_dlg_list.append("Sank the bounce shot! Whoop whoop!")
                else:
                    bp_dlg_list.append("Hell yes! That's a perfect bounce.")
            else:
                ind =  renpy.random.randint(0,5)
                if ind == 0:
                    bp_dlg_list.append("Into the cup it goes!")
                elif ind == 1:
                    bp_dlg_list.append("Yes!")
                elif ind == 2:
                    bp_dlg_list.append("There we go!")
                elif ind == 3:
                    bp_dlg_list.append("Look at that. It went right in!")
                elif ind == 4:
                    bp_dlg_list.append("Sunk it!")
                else:
                    bp_dlg_list.append("What a shot!")
        
        else:
            if bp_cpu_name == "Camila":
                bp_who_list.append("{color=#c55ffc}[bp_cpu_name]{/color}")
                
                if shot == 2:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Strip for me, [name]! That shot is worth two cups, you know.")
                    elif ind == 1:
                        bp_dlg_list.append("Bounce, baby, bounce!")
                    elif ind == 2:
                        bp_dlg_list.append("That shot bounced. Now I wanna see you bounce around as you strip.")
                    elif ind == 3:
                        bp_dlg_list.append("Wooooo!!! Did you guys see that? That was a bounce shot!")
                    elif ind == 4:
                        bp_dlg_list.append("Haha! You didn't swat it, and now you have to drink and strip!")
                    else:
                        bp_dlg_list.append("Yes!!! Bounced it!")
                else:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Yay! I hit it!")
                    elif ind == 1:
                        bp_dlg_list.append("Oh! I didn't think it would go in, but it did! Wooo!!!")
                    elif ind == 2:
                        bp_dlg_list.append("I knew I would hit that shot! I could feel it.")
                    elif ind == 3:
                        bp_dlg_list.append("You won't see me naked tonight, [name]. I'm on fire!")
                    elif ind == 4:
                        bp_dlg_list.append("It went in! Haha!")
                    else:
                        bp_dlg_list.append("Yes!!! I'm so gonna win.")
            elif bp_cpu_name == "Sage":
                bp_who_list.append("{color=#BCB88A}[bp_cpu_name]{/color}")
                
                if shot == 2:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Look at that! Do you know what that means? It's time for you to lose some clothes.")
                    elif ind == 1:
                        bp_dlg_list.append("Strip, baby, strip!")
                    elif ind == 2:
                        bp_dlg_list.append("And that's how you do a perfect bounce shot!")
                    elif ind == 3:
                        bp_dlg_list.append("Haha! You could have swatted that one, but now you have to strip.")
                    elif ind == 4:
                        bp_dlg_list.append("Yes! It went in! That's two cups, [name]!")
                    else:
                        bp_dlg_list.append("And she scores! The audience screams in jubilation as [name] strips!")
                else:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Yes! Get in there!")
                    elif ind == 1:
                        bp_dlg_list.append("I'm the Beer Pong Master, bitch!")
                    elif ind == 2:
                        bp_dlg_list.append("That's all skill, baby!")
                    elif ind == 3:
                        bp_dlg_list.append("Haha! You're gonna lose.")
                    elif ind == 4:
                        bp_dlg_list.append("Hit it!")
                    else:
                        bp_dlg_list.append("Aw, yeah! That's how you do it!")
            elif bp_cpu_name == "Josy":
                bp_who_list.append("{color=#ff1c63}[bp_cpu_name]{/color}")
                
                if shot == 2:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Huh? It bounced into the cup. That's good, right?")
                    elif ind == 1:
                        bp_dlg_list.append("Haha! That was so not on purpose.")
                    elif ind == 2:
                        bp_dlg_list.append("I did it! That's a bounce shot, right!?")
                    elif ind == 3:
                        bp_dlg_list.append("Isn't that shot worth two cups? That means [name] will have to strip!")
                    elif ind == 4:
                        bp_dlg_list.append("Haha! That's a bounce shot!!!")
                    else:
                        bp_dlg_list.append("I can't believe I hit a bounce shot!")
                else:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Oh! I hit one!")
                    elif ind == 1:
                        bp_dlg_list.append("Hahaha! Yes!")
                    elif ind == 2:
                        bp_dlg_list.append("That wasn't so hard! I should just throw it like that every time.")
                    elif ind == 3:
                        bp_dlg_list.append("Yes! I have a chance of winning.")
                    elif ind == 4:
                        bp_dlg_list.append("Oh! I didn't expect that to happen.")
                    else:
                        bp_dlg_list.append("It went right in!")
            elif bp_cpu_name == "Jill":
                bp_who_list.append("{color=#ffe9b9}[bp_cpu_name]{/color}")
                
                if shot == 2:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("Does that bounce mean I hit two cups?")
                    elif ind == 1:
                        bp_dlg_list.append("Haha! What a happy accident.")
                    elif ind == 2:
                        bp_dlg_list.append("Oh! Wow!")
                    elif ind == 3:
                        bp_dlg_list.append("I wasn't going for a bounce shot, but it became one.")
                    elif ind == 4:
                        bp_dlg_list.append("Yes! Haha!")
                    else:
                        bp_dlg_list.append("That was so lucky!")
                else:
                    ind =  renpy.random.randint(0,5)
                    if ind == 0:
                        bp_dlg_list.append("It hit!")
                    elif ind == 1:
                        bp_dlg_list.append("That was a good shot, right?")
                    elif ind == 2:
                        bp_dlg_list.append("I think I know how to throw now.")
                    elif ind == 3:
                        bp_dlg_list.append("This will get harder and harder the more cups I hit.")
                    elif ind == 4:
                        bp_dlg_list.append("Yes! It went in.")
                    else:
                        bp_dlg_list.append("I thought that one would miss, but it didn't. Haha!")
            elif bp_cpu_name == "Isabella":
                bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                
                if shot == 2:
                    ind =  renpy.random.randint(0,5)
                    if bp_ep_suffix == "ep11":
                        if ind == 0:
                            bp_dlg_list.append("You could have swatted that one away.")
                        elif ind == 1:
                            bp_dlg_list.append("Bounce shot! That's two cups!")
                        elif ind == 2:
                            bp_dlg_list.append("I've always been good at bounce shots, [name].")
                        elif ind == 3:
                            bp_dlg_list.append("If you focused, you could have swatted that one. But now you'll have to pay the price.")
                        elif ind == 4:
                            bp_dlg_list.append("Mhm. That's what I warned you about.")
                        else:
                            bp_dlg_list.append("Easy.")
                    else:
                        if ind == 0:
                            bp_dlg_list.append("Don't look surprised. Look naked because your clothes should be coming off right now.")
                        elif ind == 1:
                            bp_dlg_list.append("Did you expect anything less?")
                        elif ind == 2:
                            bp_dlg_list.append("I've always been good at bounce shots, [name].")
                        elif ind == 3:
                            bp_dlg_list.append("If you focused, you could have swatted that one. But now you'll have to pay the price.")
                        elif ind == 4:
                            bp_dlg_list.append("That just happened. Drink and strip.")
                        else:
                            bp_dlg_list.append("Easy.")
                else:
                    ind =  renpy.random.randint(0,5)
                    if bp_ep_suffix == "ep11":
                        if ind == 0:
                            bp_dlg_list.append("There we go.")
                            bp_who_list.append("{color=#ffe9b9}Jill{/color}")
                            bp_dlg_list.append("Yes!!! Haha!")
                        elif ind == 1:
                            bp_dlg_list.append("If you're looking for where the ball went, check your cup.")
                        elif ind == 2:
                            bp_dlg_list.append("Easy!")
                            bp_who_list.append("{color=#a7f442}Maya{/color}")
                            bp_dlg_list.append("Yep, I could tell it was. It went right in.")
                        elif ind == 3:
                            bp_dlg_list.append("Check your cup, not ours.")
                            bp_who_list.append("{color=#ff1c63}Josy{/color}")
                            bp_dlg_list.append("Haha!")
                        elif ind == 4:
                            bp_dlg_list.append("Yes!")
                            bp_who_list.append("{color=#ff1c63}Josy{/color}")
                            bp_dlg_list.append("That was such a good throw!")
                            bp_who_list.append("{color=#BCB88A}Sage{/color}")
                            bp_dlg_list.append("You've got this, Bella!")
                        else:
                            bp_dlg_list.append("Hit it!")
                            bp_who_list.append("{color=#BCB88A}Sage{/color}")
                            bp_dlg_list.append("I never doubted you for a second.")
                    else:
                        if ind == 0:
                            bp_dlg_list.append("Tick-tock goes the penis clock.")
                            bp_who_list.append("{color=#ffaf05}[name]{/color}")
                            bp_dlg_list.append("What does that even mean?")
                            bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                            bp_dlg_list.append("That you're about to be naked.")
                        elif ind == 1:
                            bp_dlg_list.append("If you're looking for where the ball went, check your cup.")
                        elif ind == 2:
                            bp_dlg_list.append("Boom! I've still got it.")
                        elif ind == 3:
                            bp_dlg_list.append("That's right, you will lose.")
                        elif ind == 4:
                            bp_dlg_list.append("Didn't I warn you? I'm the best.")
                            bp_who_list.append("{color=#ffaf05}[name]{/color}")
                            bp_dlg_list.append("And kinda obnoxious.")
                            bp_who_list.append("{color=#d8f2ff}[bp_cpu_name]{/color}")
                            bp_dlg_list.append("Such a sore loser.")
                        else:
                            bp_dlg_list.append("Hit it!")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

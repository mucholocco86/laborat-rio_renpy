init python:
    def sm_play_burner():
        renpy.play("sound_effects/season3/lighter.mp3", channel="sfx3")
        renpy.play("sound_effects/season2/bubbles.mp3", channel="sfx2")
        return
    def sm_play_pour():
        renpy.play("sound_effects/season2/pour.mp3", channel="sfx2")
        return
    def sm_play_burner_off():
        renpy.play("sound_effects/season3/burner_off.mp3", channel="sfx3")
        renpy.music.stop(channel="sfx2", fadeout=1)
        return
    def sm_play_stirrer():
        renpy.sound.play("sound_effects/season3/magnetic_stirrer.mp3", channel="sfx1", loop=True)
        return
    def sm_play_stirrer_stop():
        renpy.music.stop(channel="sfx1", fadeout=1)
        return
    def sm_mute_sfx():
        renpy.music.stop(channel="sfx1", fadeout=1)
        renpy.music.stop(channel="sfx2", fadeout=1)
        renpy.music.stop(channel="sfx3", fadeout=1)
        return
    def sm_init_mg(exp):
        global sm_weigh_result
        global sm_bunsen_on
        global sm_stirrer_on
        global sm_stirrer_str
        global sm_scale_str
        global sm_vol_str
        global sm_round_str
        global sm_measure_color
        global sm_measure_vol
        global sm_measure_phase
        global sm_measure_result_vol
        global sm_time_penalty
        global sm_button_set
        global sm_pour_mode
        global sm_weigh_color
        global sm_weight
        global sm_weigh_phase
        global sm_stirrer_vol
        global sm_stirrer_mode
        global sm_stir_list
        global sm_round_list
        global sm_purity
        global sm_stirrer_criteria
        global sm_round_criteria
        global sm_cue_color_change
        global sm_experiment_list
        global sm_notes
        
        sm_experiment = exp
        
        sm_weigh_result = 0
        sm_stirrer_on = False
        sm_bunsen_on = False
        
        sm_stirrer_str = "empty"
        sm_scale_str = "empty"
        sm_vol_str = "empty"
        sm_round_str = "empty"
        sm_measure_color = "red"
        
        
        sm_measure_vol = 0
        sm_measure_phase = 0
        sm_measure_result_vol = 0
        sm_time_penalty = 0
        sm_button_set = 0
        sm_pour_mode = 0
        sm_weigh_color = ""
        sm_weight = 0
        sm_weigh_phase = 0
        sm_stirrer_vol = 0
        sm_stirrer_mode = 0
        sm_stir_list = []
        sm_round_list = []
        sm_purity = 0
        sm_stirrer_criteria = 0
        sm_round_criteria = 0
        sm_cue_color_change = []
        sm_experiment_list = []
        sm_notes = []
        
        return

    def sm_clear_selection():
        global sm_button_set
        sm_button_set = 0
        return

    def sm_init_measure(clr):
        global sm_measure_phase
        global sm_measure_vol
        global sm_measure_color
        
        sm_measure_color = clr
        sm_measure_vol = 0
        sm_measure_phase = 0
        return

    def sm_init_weigh(clr):
        global sm_weight
        global sm_weigh_color
        global sm_weigh_phase
        
        sm_weigh_color = clr
        sm_weight = 0
        sm_weigh_phase = 0
        return

    def sm_bunsen(x):
        global sm_bunsen_on
        sm_bunsen_on = x
        sm_check_round()
        return


    def sm_discard_measure():
        global sm_measure_color
        global sm_measure_result_vol
        global sm_vol_str
        
        sm_measure_color = "empty"
        sm_measure_result_vol = 0
        sm_vol_str = "empty"
        
        return

    def sm_discard_weigh(x):
        global sm_weigh_color
        global sm_scale_str
        global sm_weigh_result
        
        if x:
            sm_weigh_color = ""
        sm_scale_str = "empty"
        sm_weigh_result = 0
        
        return

    def sm_discard_stirrer():
        global sm_stirrer_str
        global sm_stirrer_on
        global sm_stirrer_vol
        global sm_stir_list
        global sm_stirrer_criteria
        
        sm_stirrer_criteria = 0
        sm_stirrer_vol = 0
        sm_stirrer_on = False
        sm_stirrer_str = "empty"
        sm_stir_list = []
        
        return

    def sm_discard_round():
        global sm_round_str
        global sm_round_list
        global sm_round_criteria
        
        sm_round_criteria = 0
        sm_round_list = []
        sm_round_str = "empty"
        
        return

    def sm_add_to_beaker():
        global sm_pour_mode
        global sm_vol_str
        global sm_measure_color
        global sm_measure_result_vol
        global sm_weigh_color
        global sm_scale_str
        global sm_weigh_result
        
        if sm_pour_mode == 1:
            sm_vol_to_beaker()
            sm_vol_str = "empty"
            sm_measure_color = "empty"
            sm_measure_result_vol = 0
        elif sm_pour_mode == 2:
            sm_weigh_to_beaker()
            sm_weigh_color = ""
            sm_scale_str = "empty"
            sm_weigh_result = 0
        
        sm_pour_mode = 0
        return

    def sm_add_to_flask():
        global sm_pour_mode
        global sm_vol_str
        global sm_measure_color
        global sm_measure_result_vol
        global sm_weigh_color
        global sm_scale_str
        global sm_weigh_result
        global sm_stirrer_on
        global sm_stirrer_str
        global sm_stirrer_vol
        global sm_stir_list
        
        if sm_pour_mode == 1:
            sm_vol_to_round()
            sm_vol_str = "empty"
            sm_measure_color = "empty"
            sm_measure_result_vol = 0
        elif sm_pour_mode == 2:
            sm_weigh_to_round()
            sm_weigh_color = ""
            sm_scale_str = "empty"
            sm_weigh_result = 0
        elif sm_pour_mode == 3:
            sm_stir_to_round()
            sm_stirrer_on = False
            sm_stirrer_str = "empty"
            sm_stirrer_vol = 0
            sm_stir_list = []
        sm_pour_mode = 0
        return

    def sm_weigh_subtract():
        global sm_weigh_result
        sm_weigh_result -= renpy.random.randint(1, 9)
        sm_weigh_result = max(sm_weigh_result,0)
        return

    def sm_weigh_add():
        global sm_weigh_result
        sm_weigh_result += renpy.random.randint(1, 9)
        sm_weigh_result = min(sm_weigh_result,100)
        return

    def sm_vol_to_beaker():
        global sm_stirrer_vol
        global sm_stirrer_str
        global sm_vol_str
        global sm_stir_list
        global sm_measure_result_vol
        
        if sm_stirrer_vol == 0:
            sm_stirrer_str = sm_vol_str
        sm_stirrer_vol = 1
        
        sm_stir_list.append(["vol",sm_vol_str,sm_measure_result_vol])
        
        sm_check_beaker()
        return

    def sm_weigh_to_beaker():
        global sm_stir_list
        global sm_weigh_color
        global sm_weigh_result
        
        sm_stir_list.append(["weight",sm_weigh_color,sm_weigh_result])
        sm_check_beaker()
        
        return

    def sm_vol_to_round():
        global sm_round_list
        global sm_vol_str
        global sm_measure_result_vol
        global sm_round_str
        
        if sm_round_str == "empty":
            sm_round_str = sm_vol_str
        
        sm_round_list.append(["vol",sm_vol_str,sm_measure_result_vol])
        sm_check_round()
        
        return

    def sm_weigh_to_round():
        global sm_round_list
        global sm_weigh_color
        global sm_weigh_result
        
        sm_round_list.append(["weight",sm_weigh_color,sm_weigh_result])
        sm_check_round()
        return

    def sm_stir_to_round():
        global sm_stir_list
        global sm_round_list
        global sm_stirrer_str
        global sm_round_str
        global sm_stirrer_criteria
        
        if sm_round_str == "empty":
            sm_round_str = sm_stirrer_str
        sm_round_list.append(["stir",sm_stir_list])
        sm_stirrer_criteria = 0
        sm_check_round()
        return

    def sm_check_beaker():
        global sm_stir_list
        global sm_stirrer_str
        global sm_stirrer_criteria
        global sm_experiment
        global sm_experiment_list
        
        if sm_experiment == 1:
            if len(sm_stir_list) == 2 and ((sm_stir_list[0][0]=="vol" and sm_stir_list[0][1]==sm_experiment_list[0][0] and sm_stir_list[0][2]>=sm_experiment_list[0][1]-4 and sm_stir_list[0][2]<=sm_experiment_list[0][1]+4 and sm_stir_list[1][0]=="weight" and sm_stir_list[1][1]==sm_experiment_list[1][0] and sm_stir_list[1][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[1][2]<=sm_experiment_list[1][1]+5) or (sm_stir_list[1][0]=="vol" and sm_stir_list[1][1]==sm_experiment_list[0][0] and sm_stir_list[1][2]>=sm_experiment_list[0][1]-4 and sm_stir_list[1][2]<=sm_experiment_list[0][1]+4 and sm_stir_list[0][0]=="weight" and sm_stir_list[0][1]==sm_experiment_list[1][0] and sm_stir_list[0][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[0][2]<=sm_experiment_list[1][1]+5)):
                sm_stirrer_str = "green"
                sm_stirrer_criteria = 1
                sm_check_stirrer()
            elif len(sm_stir_list) == 4 and ((sm_stir_list[0][0]=="vol" and sm_stir_list[0][1]==sm_experiment_list[0][0] and sm_stir_list[0][2]>=sm_experiment_list[0][1]-4 and sm_stir_list[0][2]<=sm_experiment_list[0][1]+4 and sm_stir_list[1][0]=="weight" and sm_stir_list[1][1]==sm_experiment_list[1][0] and sm_stir_list[1][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[1][2]<=sm_experiment_list[1][1]+5) or (sm_stir_list[1][0]=="vol" and sm_stir_list[1][1]==sm_experiment_list[0][0] and sm_stir_list[1][2]>=sm_experiment_list[0][1]-4 and sm_stir_list[1][2]<=sm_experiment_list[0][1]+4 and sm_stir_list[0][0]=="weight" and sm_stir_list[0][1]==sm_experiment_list[1][0] and sm_stir_list[0][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[0][2]<=sm_experiment_list[1][1]+5)):
                if sm_stir_list[2][0]=="stir" and sm_stir_list[2][1]==sm_experiment_list[4][0]:
                    if sm_stir_list[3][0]=="weight" and sm_stir_list[3][1]==sm_experiment_list[4][1] and sm_stir_list[3][2] >= sm_experiment_list[4][2]-5 and sm_stir_list[3][2] <= sm_experiment_list[4][2]+5:
                        sm_stirrer_criteria = 2
                        sm_check_stirrer()
                elif sm_stir_list[2][0]=="stir" and sm_stir_list[2][1]=="clear":
                    if sm_stir_list[3][0]=="vol" and sm_stir_list[3][1]=="green" and sm_stir_list[3][2] >= sm_experiment_list[3][2]-4 and sm_stir_list[3][2] <= sm_experiment_list[3][2]+4:
                        sm_stirrer_criteria = 2
                        sm_check_stirrer()
        elif sm_experiment == 2:
            if len(sm_stir_list) == 3 and sm_stir_list[0][0]=="weight" and sm_stir_list[0][1]==sm_experiment_list[0][0] and sm_stir_list[0][2]>=sm_experiment_list[0][1]-5 and sm_stir_list[0][2]<=sm_experiment_list[0][1]+5 and sm_stir_list[1][0]=="weight" and sm_stir_list[1][1]==sm_experiment_list[1][0] and sm_stir_list[1][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[1][2]<=sm_experiment_list[1][1]+5 and sm_stir_list[2][0]=="vol" and sm_stir_list[2][1]==sm_experiment_list[2][0] and sm_stir_list[2][2]>=sm_experiment_list[2][1]-4 and sm_stir_list[2][2]<=sm_experiment_list[2][1]+4:
                sm_stirrer_str = sm_experiment_list[2][0]
                sm_stirrer_criteria = 1
                sm_check_stirrer()
            elif len(sm_stir_list) == 5 and sm_stir_list[0][0]=="weight" and sm_stir_list[0][1]==sm_experiment_list[0][0] and sm_stir_list[0][2]>=sm_experiment_list[0][1]-5 and sm_stir_list[0][2]<=sm_experiment_list[0][1]+5 and sm_stir_list[1][0]=="weight" and sm_stir_list[1][1]==sm_experiment_list[1][0] and sm_stir_list[1][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[1][2]<=sm_experiment_list[1][1]+5 and sm_stir_list[2][0]=="vol" and sm_stir_list[2][1]==sm_experiment_list[2][0] and sm_stir_list[2][2]>=sm_experiment_list[2][1]-4 and sm_stir_list[2][2]<=sm_experiment_list[2][1]+4:
                
                if sm_stir_list[3][0]=="stir" and sm_stir_list[3][1]=="clear":
                    if sm_stir_list[4][0]=="weight" and sm_stir_list[4][1]==sm_experiment_list[5][0] and sm_stir_list[4][2] >= sm_experiment_list[5][1]-5 and sm_stir_list[4][2] <= sm_experiment_list[5][1]+5:
                        sm_stirrer_criteria = 2
                        sm_check_stirrer()
                elif sm_stir_list[3][0]=="stir" and sm_stir_list[3][1]=="blue":
                    if sm_stir_list[4][0]=="vol" and sm_stir_list[4][1]=="red" and sm_stir_list[4][2] >= sm_experiment_list[4][1]-4 and sm_stir_list[4][2] <= sm_experiment_list[4][1]+4:
                        sm_stirrer_criteria = 2
                        sm_check_stirrer()
        elif sm_experiment == 3:
            if len(sm_stir_list) == 3 and sm_stir_list[0][0]=="weight" and sm_stir_list[0][1]==sm_experiment_list[0][0] and sm_stir_list[0][2]>=sm_experiment_list[0][1]-5 and sm_stir_list[0][2]<=sm_experiment_list[0][1]+5 and sm_stir_list[1][0]=="weight" and sm_stir_list[1][1]==sm_experiment_list[1][0] and sm_stir_list[1][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[1][2]<=sm_experiment_list[1][1]+5 and sm_stir_list[2][0]=="vol" and sm_stir_list[2][1]==sm_experiment_list[2][0] and sm_stir_list[2][2]>=sm_experiment_list[2][1]-4 and sm_stir_list[2][2]<=sm_experiment_list[2][1]+4:
                sm_stirrer_str = sm_experiment_list[2][0]
                sm_stirrer_criteria = 1
                sm_check_stirrer()
            elif len(sm_stir_list) == 5 and sm_stir_list[0][0]=="weight" and sm_stir_list[0][1]==sm_experiment_list[0][0] and sm_stir_list[0][2]>=sm_experiment_list[0][1]-5 and sm_stir_list[0][2]<=sm_experiment_list[0][1]+5 and sm_stir_list[1][0]=="weight" and sm_stir_list[1][1]==sm_experiment_list[1][0] and sm_stir_list[1][2]>=sm_experiment_list[1][1]-5 and sm_stir_list[1][2]<=sm_experiment_list[1][1]+5 and sm_stir_list[2][0]=="vol" and sm_stir_list[2][1]==sm_experiment_list[2][0] and sm_stir_list[2][2]>=sm_experiment_list[2][1]-4 and sm_stir_list[2][2]<=sm_experiment_list[2][1]+4:
                
                if sm_stir_list[3][0]=="stir" and (sm_stir_list[3][1]=="clear" or sm_stir_list[3][1]=="red"):
                    if sm_stir_list[4][0]=="weight" and sm_stir_list[4][1]=="red" and sm_stir_list[4][2] >= sm_experiment_list[4][1]-5 and sm_stir_list[4][2] <= sm_experiment_list[4][1]+5:
                        sm_stirrer_criteria = 2
                        sm_check_stirrer()
        return

    def sm_check_round():
        global sm_round_list
        global sm_bunsen_on
        global sm_round_criteria
        global sm_cue_color_change
        global sm_experiment
        global sm_experiment_list
        
        if sm_experiment == 1:
            if sm_bunsen_on:
                if len(sm_round_list) == 1 and len(sm_round_list[0]) == 2 and sm_round_list[0][0] == "stir" and len(sm_round_list[0][1]) == 5:
                    if sm_round_list[0][1][4][1] == "blue" and sm_round_list[0][1][4][0] == "stir" and sm_round_criteria == 0:
                        sm_round_criteria = 1
                        if renpy.random.randint(1, 2) == 2:
                            sm_cue_color_change = [5,"clear","round"]
                        else:
                            sm_cue_color_change = [5,"red","round"]
                elif len(sm_round_list) == 3 and sm_round_criteria == 1 and len(sm_round_list[1])==3 and len(sm_round_list[2])==3:
                    if sm_round_list[1][1] == "clear" and sm_round_list[1][0] == "round":
                        if sm_round_list[2][0] == "vol" and sm_round_list[2][1] == "green" and sm_round_list[2][2] >= sm_experiment_list[6][1]-4 and sm_round_list[2][2] <= sm_experiment_list[6][1]+4:
                            sm_round_criteria = 2
                            sm_cue_color_change = [5,"blue","round"]
                    elif sm_round_list[1][1] == "red" and sm_round_list[1][0] == "round":
                        if sm_round_list[2][0] == "weight" and sm_round_list[2][1] == "blue" and sm_round_list[2][2] >= sm_experiment_list[7][1]-5 and sm_round_list[2][2] <= sm_experiment_list[7][1]+5:
                            sm_round_criteria = 2
                            sm_cue_color_change = [5,"blue","round"]
        elif sm_experiment == 2:
            if sm_bunsen_on:
                if len(sm_round_list) == 1 and len(sm_round_list[0]) == 2 and sm_round_list[0][0] == "stir" and len(sm_round_list[0][1]) == 6:
                    if sm_round_list[0][1][5][1] == "red" and sm_round_list[0][1][5][0] == "stir" and sm_round_criteria == 0:
                        sm_round_criteria = 1
                        if renpy.random.randint(1, 2) == 2:
                            sm_cue_color_change = [10,"green","round"]
                        else:
                            sm_cue_color_change = [10,"clear","round"]
                elif len(sm_round_list) == 3 and sm_round_criteria == 1 and len(sm_round_list[1])==3 and len(sm_round_list[2])==3:
                    if sm_round_list[1][1] == "green" and sm_round_list[1][0] == "round":
                        if sm_round_list[2][0] == "vol" and sm_round_list[2][1] == "red" and sm_round_list[2][2] >= sm_experiment_list[7][1]-4 and sm_round_list[2][2] <= sm_experiment_list[7][1]+4:
                            sm_round_criteria = 2
                            sm_cue_color_change = [10,"blue","round"]
                    elif sm_round_list[1][1] == "clear" and sm_round_list[1][0] == "round":
                        if sm_round_list[2][0] == "weight" and sm_round_list[2][1] == "red" and sm_round_list[2][2] >= sm_experiment_list[8][1]-5 and sm_round_list[2][2] <= sm_experiment_list[8][1]+5:
                            sm_round_criteria = 2
                            sm_cue_color_change = [10,"blue","round"]
            elif len(sm_round_list) == 4 and sm_round_criteria == 2 and len(sm_round_list[1])==3 and len(sm_round_list[2])==3:
                sm_round_criteria = 3
                sm_cue_color_change = [10,"green","round"]
        elif sm_experiment == 3:
            if sm_bunsen_on:
                if len(sm_round_list) == 1 and len(sm_round_list[0]) == 2 and sm_round_list[0][0] == "stir" and len(sm_round_list[0][1]) == 6:
                    if sm_round_list[0][1][5][1] == "green" and sm_round_list[0][1][5][0] == "stir" and sm_round_criteria == 0:
                        sm_round_criteria = 1
                        if renpy.random.randint(1, 2) == 2:
                            sm_cue_color_change = [10,"clear","round"]
                        else:
                            sm_cue_color_change = [10,"blue","round"]
                elif len(sm_round_list) == 3 and sm_round_criteria == 1 and len(sm_round_list[1])==3 and len(sm_round_list[2])==3:
                    if sm_round_list[1][1] == "clear" and sm_round_list[1][0] == "round":
                        if sm_round_list[2][0] == "weight" and sm_round_list[2][1] == "blue" and sm_round_list[2][2] >= sm_experiment_list[7][1]-5 and sm_round_list[2][2] <= sm_experiment_list[7][1]+5:
                            sm_round_criteria = 2
                            sm_cue_color_change = [10,"red","round"]
                    elif sm_round_list[1][1] == "blue" and sm_round_list[1][0] == "round":
                        if sm_round_list[2][0] == "weight" and sm_round_list[2][1] == "red" and sm_round_list[2][2] >= sm_experiment_list[8][1]-5 and sm_round_list[2][2] <= sm_experiment_list[8][1]+5:
                            sm_round_criteria = 2
                            sm_cue_color_change = [10,"red","round"]
            elif len(sm_round_list) == 4 and sm_round_criteria == 2 and len(sm_round_list[1])==3 and len(sm_round_list[2])==3:
                sm_round_criteria = 3
                sm_cue_color_change = [15,"green","round"]
        return

    def sm_check_stirrer():
        global sm_stirrer_on
        global sm_stirrer_mode
        global sm_stirrer_criteria
        global sm_cue_color_change
        global sm_stir_list
        global sm_experiment
        global sm_experiment_list
        
        if sm_experiment == 1:
            if sm_stirrer_criteria == 1 and sm_stirrer_on and sm_stirrer_mode == sm_experiment_list[2][1]:
                if renpy.random.randint(1, 2) == 2:
                    sm_cue_color_change = [5,"clear","stir"]
                    sm_stirrer_criteria = 0
                else:
                    sm_cue_color_change = [5,sm_experiment_list[4][0],"stir"]
                    sm_stirrer_criteria = 0
            elif sm_stirrer_criteria == 2 and sm_stirrer_on and sm_stirrer_mode == sm_experiment_list[5][1]:
                sm_cue_color_change = [5,"blue","stir"]
                sm_stirrer_criteria = 0
        elif sm_experiment == 2:
            if sm_stirrer_criteria == 1 and sm_stirrer_on and sm_stirrer_mode == sm_experiment_list[3][1]:
                if renpy.random.randint(1, 2) == 2:
                    sm_cue_color_change = [10,"clear","stir"]
                    sm_stirrer_criteria = 0
                else:
                    sm_cue_color_change = [10,"blue","stir"]
                    sm_stirrer_criteria = 0
            elif sm_stirrer_criteria == 2 and sm_stirrer_on and sm_stirrer_mode == sm_experiment_list[6][1]:
                if renpy.random.randint(1, 2) == 2:
                    sm_cue_color_change = [5,"red","stir"]
                    sm_stirrer_criteria = 0
                else:
                    sm_cue_color_change = [5,"red","stir"]
                    sm_stirrer_criteria = 0
        elif sm_experiment == 3:
            if sm_stirrer_criteria == 1 and sm_stirrer_on and sm_stirrer_mode == sm_experiment_list[3][1]:
                if renpy.random.randint(1, 2) == 2:
                    sm_cue_color_change = [15,"red","stir"]
                    sm_stirrer_criteria = 0
                else:
                    sm_cue_color_change = [15,"clear","stir"]
                    sm_stirrer_criteria = 0
            elif sm_stirrer_criteria == 2 and sm_stirrer_on and sm_stirrer_mode == sm_experiment_list[6][1]:
                if renpy.random.randint(1, 2) == 2:
                    sm_cue_color_change = [10,"green","stir"]
                    sm_stirrer_criteria = 0
                else:
                    sm_cue_color_change = [10,"green","stir"]
                    sm_stirrer_criteria = 0
        
        return

    def sm_change_color():
        global sm_cue_color_change
        global sm_stirrer_str
        global sm_round_str
        global sm_stir_list
        global sm_round_list
        
        if len(sm_cue_color_change)>0:
            if sm_cue_color_change[2] == "stir":
                sm_stirrer_str = sm_cue_color_change[1]
                sm_stir_list.append([sm_cue_color_change[2],sm_cue_color_change[1],0])
                sm_cue_color_change = []
            elif sm_cue_color_change[2] == "round":
                sm_round_str = sm_cue_color_change[1]
                sm_round_list.append([sm_cue_color_change[2],sm_cue_color_change[1],0])
                sm_cue_color_change = []
        return

    def sm_calc_purity():
        global sm_experiment
        global sm_experiment_list
        global sm_purity
        global sm_round_list
        global sm_perk_purity
        global failedScienceS3
        global maxedScienceS3
        global passedScienceS3
        
        sm_purity = 0
        
        if sm_experiment == 1:
            if len(sm_round_list)==4 and len(sm_round_list[3]) == 3:
                if sm_round_list[3][0] == "round" and sm_round_list[3][1] == "blue":
                    if len(sm_round_list[0])==2 and len(sm_round_list[0][1])==5:
                        if sm_round_list[0][1][0][0] == "vol" and sm_round_list[0][1][0][1] == sm_experiment_list[0][0]:
                            sm_purity += 25 - abs(sm_experiment_list[0][1]-sm_round_list[0][1][0][2])
                        elif sm_round_list[0][1][1][0] == "vol" and sm_round_list[0][1][1][1] == sm_experiment_list[0][0]:
                            sm_purity += 25 - abs(sm_experiment_list[0][1]-sm_round_list[0][1][1][2])
                        if sm_round_list[0][1][0][0] == "weight" and sm_round_list[0][1][0][1] == sm_experiment_list[1][0]:
                            sm_purity += 25 - abs(sm_experiment_list[1][1]-sm_round_list[0][1][0][2])
                        elif sm_round_list[0][1][1][0] == "weight" and sm_round_list[0][1][1][1] == sm_experiment_list[1][0]:
                            sm_purity += 25 - abs(sm_experiment_list[1][1]-sm_round_list[0][1][1][2])
                        
                        if sm_round_list[0][1][2][1] == "red" and sm_round_list[0][1][3][1] == "blue":
                            sm_purity += 25 - abs(sm_experiment_list[4][2]-sm_round_list[0][1][3][2])
                        elif sm_round_list[0][1][2][1] == "green" and sm_round_list[0][1][3][1] == "red":
                            sm_purity += 25 - abs(sm_experiment_list[4][2]-sm_round_list[0][1][3][2])
                        elif sm_round_list[0][1][2][1] == "clear" and sm_round_list[0][1][3][0] == "vol" and sm_round_list[0][1][3][1] == "green":
                            sm_purity += 25 - abs(sm_experiment_list[3][2]-sm_round_list[0][1][3][2])
                    if len(sm_round_list[1])==3 and sm_round_list[1][0] == "round" and sm_round_list[1][1] != "clear":
                        if len(sm_round_list[2])==3 and sm_round_list[2][0] == "weight" and sm_round_list[2][1] == "blue":
                            sm_purity += 25 - abs(sm_experiment_list[7][1]-sm_round_list[2][2])
                    elif len(sm_round_list[1])==3 and sm_round_list[1][0] == "round" and sm_round_list[1][1] == "clear":
                        if len(sm_round_list[2])==3 and sm_round_list[2][0] == "vol" and sm_round_list[2][1] == "green":
                            sm_purity += 25 - abs(sm_experiment_list[6][1]-sm_round_list[2][2])
        elif sm_experiment == 2:
            if len(sm_round_list)==5 and len(sm_round_list[3]) == 3 and len(sm_round_list[4]) == 3:
                if sm_round_list[3][0] == "round" and sm_round_list[3][1] == "blue" and sm_round_list[4][0] == "round" and sm_round_list[4][1] == "green":
                    if len(sm_round_list[0]) == 2 and sm_round_list[0][0] == "stir" and len(sm_round_list[0][1]) == 6:
                        if sm_round_list[0][1][0][0] == "weight" and sm_round_list[0][1][0][1] == sm_experiment_list[0][0]:
                            sm_purity += 20 - abs(sm_experiment_list[0][1]-sm_round_list[0][1][0][2])
                        if sm_round_list[0][1][1][0] == "weight" and sm_round_list[0][1][1][1] == sm_experiment_list[1][0]:
                            sm_purity += 20 - abs(sm_experiment_list[1][1]-sm_round_list[0][1][1][2])
                        if sm_round_list[0][1][2][0] == "vol" and sm_round_list[0][1][2][1] == sm_experiment_list[2][0]:
                            sm_purity += 20 - abs(sm_experiment_list[2][1]-sm_round_list[0][1][2][2])
                        if sm_round_list[0][1][3][1] == "blue" and sm_round_list[0][1][4][0] == "vol" and sm_round_list[0][1][4][1] == sm_experiment_list[4][0]:
                            sm_purity += 20 - abs(sm_experiment_list[4][1]-sm_round_list[0][1][4][2])
                        elif sm_round_list[0][1][3][1] == "clear" and sm_round_list[0][1][4][0] == "weight" and sm_round_list[0][1][4][1] == sm_experiment_list[5][0]:
                            sm_purity += 20 - abs(sm_experiment_list[5][1]-sm_round_list[0][1][4][2])
                    
                    if len(sm_round_list[2])==3 and sm_round_list[2][0] == "vol" and sm_round_list[2][1] == "red":
                        sm_purity += 20 - abs(sm_experiment_list[7][1]-sm_round_list[2][2])
                    elif len(sm_round_list[2])==3 and sm_round_list[2][0] == "weight" and sm_round_list[2][1] == "red":
                        sm_purity += 20 - abs(sm_experiment_list[8][1]-sm_round_list[2][2])
        elif sm_experiment == 3:
            if len(sm_round_list)==5 and len(sm_round_list[3]) == 3 and len(sm_round_list[4]) == 3:
                if sm_round_list[3][0] == "round" and sm_round_list[3][1] == "red" and sm_round_list[4][0] == "round" and sm_round_list[4][1] == "green":
                    if len(sm_round_list[0]) == 2 and sm_round_list[0][0] == "stir" and len(sm_round_list[0][1]) == 6:
                        if sm_round_list[0][1][0][0] == "weight" and sm_round_list[0][1][0][1] == sm_experiment_list[0][0]:
                            sm_purity += 20 - abs(sm_experiment_list[0][1]-sm_round_list[0][1][0][2])
                        if sm_round_list[0][1][1][0] == "weight" and sm_round_list[0][1][1][1] == sm_experiment_list[1][0]:
                            sm_purity += 20 - abs(sm_experiment_list[1][1]-sm_round_list[0][1][1][2])
                        if sm_round_list[0][1][2][0] == "vol" and sm_round_list[0][1][2][1] == sm_experiment_list[2][0]:
                            sm_purity += 20 - abs(sm_experiment_list[2][1]-sm_round_list[0][1][2][2])
                        if (sm_round_list[0][1][3][1] == "clear" or sm_round_list[0][1][3][1] == "red") and sm_round_list[0][1][4][0] == "weight" and sm_round_list[0][1][4][1] == sm_experiment_list[4][0]:
                            sm_purity += 20 - abs(sm_experiment_list[4][1]-sm_round_list[0][1][4][2])
                    
                    if len(sm_round_list[2])==3 and sm_round_list[2][0] == "weight" and sm_round_list[1][1] == "clear" and sm_round_list[2][1] == "blue":
                        sm_purity += 20 - abs(sm_experiment_list[7][1]-sm_round_list[2][2])
                    elif len(sm_round_list[2])==3 and sm_round_list[2][0] == "weight" and sm_round_list[1][1] == "blue" and sm_round_list[2][1] == "red":
                        sm_purity += 20 - abs(sm_experiment_list[8][1]-sm_round_list[2][2])
        
        sm_purity = min(sm_purity+(sm_perk_purity*5),100)
        
        if sm_purity == 100:
            maxedScienceS3 += 1
        if sm_purity > 50:
            passedScienceS3 += 1
        else:
            failedScienceS3 += 1
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

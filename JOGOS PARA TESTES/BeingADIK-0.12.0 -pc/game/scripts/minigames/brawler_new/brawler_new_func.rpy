init python:
    def bn_play_counter(trans,st,at):
        renpy.play("sound_effects/season3/counter.mp3","sfx2")
    def bn_play_bell(trans,st,at):
        renpy.play("sound_effects/bell.mp3","sfx1")
    def bn_play_dodge(trans,st,at):
        renpy.play("sound_effects/whoosh.mp3","sfx1")
    def bn_play_punch(trans,st,at):
        renpy.play("sound_effects/season2/punching_bag_punch.mp3","sfx2")
    def bn_play_kick(trans,st,at):
        renpy.play("sound_effects/season2/punching_bag_kick.mp3","sfx2")
    def bn_play_kick_body(trans,st,at):
        renpy.play("sound_effects/season3/kick_body.mp3","sfx2")
    def bn_play_kick_slap(trans,st,at):
        renpy.play("sound_effects/season3/kick_slap.mp3","sfx2")
    def bn_play_kick_slap2(trans,st,at):
        renpy.play("sound_effects/season3/kick_slap2.mp3","sfx2")
    def bn_play_block(trans,st,at):
        renpy.play("sound_effects/shove.mp3","sfx1")
    def bn_play_rage(trans,st,at):
        renpy.play("sound_effects/season2/thunder3.mp3","sfx1")
        renpy.play("sound_effects/heartbeat.mp3","sfx2")
    def bn_play_silence(trans,st,at):
        return
    def play_bn_main(trans,st,at):
        renpy.play("sound_effects/season3/bn_main.mp3","sfx1")
    def play_bn_flurry(trans,st,at):
        renpy.play("sound_effects/season3/bn_flurry.mp3","sfx1")
    def play_bn_highkick(trans,st,at):
        renpy.play("sound_effects/season3/bn_highkick.mp3","sfx1")
        return
    def bn_play_click(trans,st,at):
        renpy.play("sound_effects/season3/bn_click.mp3","sfx1")
    def bn_play_reset(trans,st,at):
        renpy.play("sound_effects/season3/bn_reset.mp3","sfx1")
    def bn_play_failed_click(trans,st,at):
        renpy.play("sound_effects/season3/bn_failed_click.mp3","sfx1")
    def bn_play_hover(trans,st,at):
        renpy.play("sound_effects/season3/bn_hover.mp3","sfx2")

init python:
    def init_brawler_mg(update):
        global bonusPointsSports
        global bn_skill_alloc
        global bn_reward_available_list
        global bn_skill_points_total
        if update:
            if bonusPointsSports == 12:
                bn_skill_points_total = 6
                bn_reward_available_list = [10,1,3,0]
            elif bonusPointsSports > 8:
                bn_skill_points_total = 5
                bn_reward_available_list = [10,1,3,1]
            elif bonusPointsSports > 5:
                bn_skill_points_total = 4
                bn_reward_available_list = [10,1,3,2]
            elif bonusPointsSports > 2:
                bn_skill_points_total = 3
                bn_reward_available_list = [10,1,3,3]
            else:
                bn_skill_points_total = 2
                bn_reward_available_list = [10,1,3,4]
        bn_skill_alloc = [0,2,0,0,0,0]
        if bonusPointsSports == 12 or bn_reward_available_list[3] == 0:
            bn_skill_alloc[0] = 1
        if bonusPointsSports > 8 or bn_reward_available_list[3] < 2:
            bn_skill_alloc[2] = 1
        if bonusPointsSports > 5 or bn_reward_available_list[3] < 3:
            bn_skill_alloc[3] = 1
        if bonusPointsSports > 2 or bn_reward_available_list[3] < 4:
            bn_skill_alloc[4] = 1
        if update:
            for i in range(0,6):
                bn_update_player_skills(i)
        return

    def bn_populate_rage_arrow():
        global bn_arrow_combination
        bn_arrow_combination = []
        tmpInt =  renpy.random.randint(0,3)
        if tmpInt == 0:
            bn_arrow_combination.append("up")
        elif tmpInt == 1:
            bn_arrow_combination.append("right")
        elif tmpInt == 2:
            bn_arrow_combination.append("down")
        else:
            bn_arrow_combination.append("left")
        return

    def bn_populate_arrow_combo(number):
        global bn_arrow_combination
        global bn_combo_idx
        bn_combo_idx = 0
        bn_arrow_combination = []
        for i in range(0,number):
            tmpInt =  renpy.random.randint(0,3)
            if tmpInt == 0:
                bn_arrow_combination.append("up")
            elif tmpInt == 1:
                bn_arrow_combination.append("right")
            elif tmpInt == 2:
                bn_arrow_combination.append("down")
            else:
                bn_arrow_combination.append("left")
        return

    def bn_populate_arrows():
        global bn_miss_list
        global bn_normal_list
        global bn_power_list
        global bn_special_list
        global bn_arrow_selection
        global bn_mc_stamina
        global bn_player_special_cd
        
        bn_arrow_selection = ["","","",""]
        idx = 0
        misses = 0
        powers = 0
        specials = 0
        while "" in bn_arrow_selection:
            i = renpy.random.randint(0,3)
            if i == 0 and misses < 2:
                j = renpy.random.randint(0,len(bn_miss_list)-1)
                if bn_miss_list[j] not in bn_arrow_selection:
                    bn_arrow_selection[idx] = bn_miss_list[j]
                    idx += 1
                    misses += 1
            elif i == 1:
                j = renpy.random.randint(0,len(bn_normal_list)-1)
                if bn_normal_list[j] not in bn_arrow_selection:
                    bn_arrow_selection[idx] = bn_normal_list[j]
                    idx += 1
            elif i == 2 and powers < 1 and bn_mc_stamina > 1:
                j = renpy.random.randint(0,len(bn_power_list)-1)
                if bn_power_list[j] not in bn_arrow_selection:
                    bn_arrow_selection[idx] = bn_power_list[j]
                    powers += 1
                    idx += 1
            elif i == 3 and specials < 1  and bn_mc_stamina > 3 and bn_player_special_cd == 0:
                j = renpy.random.randint(0,len(bn_special_list)-1)
                if bn_special_list[j] not in bn_arrow_selection:
                    bn_arrow_selection[idx] = bn_special_list[j]
                    specials += 1
                    idx += 1
        return

    def bn_populate_def_arrows():
        global bn_miss_list
        global bn_arrow_selection
        global bn_mc_stamina
        
        bn_arrow_selection = ["","","",""]
        idx = 0
        misses = 0
        dodges = 0
        blocks = 0
        while "" in bn_arrow_selection:
            i = renpy.random.randint(0,2)
            if i == 0 and misses < 2:
                j = renpy.random.randint(0,len(bn_miss_list)-1)
                if bn_miss_list[j] not in bn_arrow_selection:
                    bn_arrow_selection[idx] = bn_miss_list[j]
                    idx += 1
                    misses += 1
            elif i == 1 and bn_mc_stamina > 0 and dodges + blocks < 2:
                bn_arrow_selection[idx] = "DODGE"
                dodges += 1
                idx += 1
            elif i == 2 and dodges + blocks < 2:
                bn_arrow_selection[idx] = "BLOCK"
                blocks += 1
                idx += 1
        return

    def bn_next_round():
        global bn_turn
        bn_recover_stamina()
        bn_reduce_cd()
        if bn_turn:
            bn_populate_arrows()
            renpy.show_screen("brawler_arrow_choice_screen")
        else:
            bn_populate_def_arrows()
            renpy.show_screen("brawler_arrow_choice_screen")
        return

    def bn_evaluate_rage():
        global bn_turn
        global bn_arrow_combination
        global bn_combo_idx
        global bn_combo_input
        global bn_rage_flash
        global bn_player_rage
        
        if bn_combo_input == bn_arrow_combination[0]:
            bn_rage_flash = True
            bn_combo_idx += 1
            if renpy.random.randint(0,1) == 0:
                return
            else:
                bn_populate_rage_arrow()
        else:
            bn_combo_idx = max(bn_player_rage,bn_combo_idx-1)
        return

    def bn_end_rage():
        global bn_rage_flash
        global bn_rage_ending
        bn_rage_ending = False
        bn_rage_flash = False
        renpy.hide_screen("brawler_rage_screen")
        bn_cpu_got_hit("rage")
        return

    def bn_evaluate_combo():
        global bn_combo_input
        global bn_turn
        global bn_arrow_combination
        global bn_combo_idx
        global bn_arrow_selection
        global bn_arrow_input
        
        if bn_combo_input == "" or bn_arrow_combination[bn_combo_idx] != bn_combo_input:
            renpy.hide_screen("brawler_arrow_combo_screen")
            if bn_turn:
                bn_player_missed()
            else:
                bn_player_got_hit()
        else:
            if bn_combo_idx + 1 < len(bn_arrow_combination):
                bn_combo_idx += 1
            else:
                renpy.hide_screen("brawler_arrow_combo_screen")
                if bn_turn:
                    if bn_arrow_selection[bn_arrow_input] in bn_normal_list:
                        bn_cpu_got_hit("normal")
                    elif bn_arrow_selection[bn_arrow_input] in bn_power_list:
                        bn_cpu_got_hit("power")
                    else:
                        bn_cpu_got_hit("special")
                else:
                    if bn_arrow_selection[bn_arrow_input] == "BLOCK":
                        bn_player_blocked()
                    else:
                        bn_player_dodged()
        return

    def bn_evaluate_input():
        global bn_arrow_input
        global bn_turn
        global bn_arrow_selection
        
        renpy.hide_screen("brawler_arrow_choice_screen")
        
        if not bn_turn:
            bn_cpu_prepare_attack()
        if bn_arrow_input == 4 or bn_arrow_selection[bn_arrow_input] in bn_miss_list:
            if bn_turn:
                bn_player_missed()
            else:
                bn_player_got_hit()
        elif bn_arrow_selection[bn_arrow_input] in bn_normal_list:
            bn_player_normal_attack()
        elif bn_arrow_selection[bn_arrow_input] in bn_power_list:
            bn_player_power_attack()
        elif bn_arrow_selection[bn_arrow_input] in bn_special_list:
            bn_player_special_attack()
        elif bn_arrow_selection[bn_arrow_input] == "BLOCK":
            bn_player_block_attack()
        elif bn_arrow_selection[bn_arrow_input] == "DODGE":
            bn_player_dodge_attack()
        return

    def bn_player_missed():
        global bn_cpu_counter_chance
        global bn_counter
        global bn_cpu_counter_stun
        if bn_cpu_counter_stun:
            bn_cpu_counter_stun = False
        elif renpy.random.randint(1,10) < bn_cpu_counter_chance:
            bn_counter = True
        bn_show_image("cpu_block")
        return

    def bn_player_dodged():
        global bn_cpu_attack
        global bn_cpu_special_cd
        global bn_cpu_stamina
        global bn_cpu_power
        global bn_pc_counter_chance
        global bn_show_counter
        dmg = 0
        if bn_cpu_attack == "normal":
            dmg = 0
        elif bn_cpu_attack == "power":
            bn_cpu_stamina -= 2
        else:
            bn_cpu_stamina -= 4
            bn_cpu_special_cd = 3
        
        if renpy.random.randint(1,10) < bn_pc_counter_chance:
            bn_show_counter = True
            bn_play_counter(0,0,0)
        
        bn_show_image("dodge")
        return

    def bn_player_blocked():
        global bn_cpu_attack
        global bn_mc_hp
        global bn_cpu_special_cd
        global bn_cpu_stamina
        global bn_cpu_power
        global bn_player_block
        dmg = 0
        if bn_cpu_attack == "normal":
            limit = (int)(10*bn_cpu_power)
            limit1 = (int)(5*bn_cpu_power)
            dmg = renpy.random.randint(limit1,limit)
        elif bn_cpu_attack == "power":
            bn_cpu_stamina -= 2
            limit = (int)(15*bn_cpu_power)
            limit1 = (int)(10*bn_cpu_power)
            dmg = renpy.random.randint(limit1,limit)
        else:
            bn_cpu_stamina -= 4
            bn_cpu_special_cd = 3
            limit = (int)(20*bn_cpu_power)
            limit1 = (int)(15*bn_cpu_power)
            dmg = renpy.random.randint(limit1,limit)
        dmg = dmg - (int) (dmg * bn_player_block)
        bn_mc_hp = max(0,bn_mc_hp-dmg)
        bn_show_image("block")
        return

    def bn_player_got_hit():
        global bn_cpu_attack
        global bn_mc_hp
        global bn_cpu_special_cd
        global bn_cpu_stamina
        global bn_cpu_power
        dmg = 0
        if bn_cpu_attack == "normal":
            limit = (int)(10*bn_cpu_power)
            limit1 = (int)(5*bn_cpu_power)
            dmg = renpy.random.randint(limit1,limit)
        elif bn_cpu_attack == "power":
            bn_cpu_stamina -= 2
            limit = (int)(15*bn_cpu_power)
            limit1 = (int)(10*bn_cpu_power)
            dmg = renpy.random.randint(limit1,limit)
        else:
            bn_cpu_stamina -= 4
            bn_cpu_special_cd = 3
            limit = (int)(20*bn_cpu_power)
            limit1 = (int)(15*bn_cpu_power)
            dmg = renpy.random.randint(limit1,limit)
        bn_mc_hp = max(0,bn_mc_hp-dmg)
        bn_show_image("cpu_"+bn_cpu_attack)
        return

    def bn_cpu_got_hit(attack_type):
        global bn_player_power
        global bn_cpu_hp
        global bn_cpu_stamina
        global bn_combo_idx
        global bn_special
        global bn_cpu_stunned
        global bn_cpu_counter_stun
        global bn_rage_record
        global bn_rage_new_record
        global bn_dmg_new_record
        global bn_dmg_record
        
        if attack_type == "normal":
            limit = (int)(10*bn_player_power)
            limit1 = (int)(5*bn_player_power)
            dmg = renpy.random.randint(limit1,limit)
            bn_cpu_hp = max(0,(bn_cpu_hp-dmg))
        elif attack_type == "power":
            limit = (int)(15*bn_player_power)
            limit1 = (int)(10*bn_player_power)
            dmg = renpy.random.randint(limit1,limit)
            bn_cpu_hp = max(0,(bn_cpu_hp-dmg))
            if bn_arrow_selection[bn_arrow_input] == "BREAK":
                bn_cpu_stamina = max(0,bn_cpu_stamina-4)
        elif attack_type == "special":
            if bn_special == 0:
                limit = (int)(20*bn_player_power)
                limit1 = (int)(15*bn_player_power)
                dmg = renpy.random.randint(limit1,limit)
                bn_cpu_hp = max(0,(bn_cpu_hp-dmg))
                bn_cpu_stamina = 0
            elif bn_special == 1:
                limit = (int)(20*bn_player_power)
                limit1 = (int)(15*bn_player_power)
                dmg = renpy.random.randint(limit1,limit)
                bn_cpu_hp = max(0,(bn_cpu_hp-dmg))
                bn_cpu_stunned = True
            elif bn_special == 2:
                limit = (int)(25*bn_player_power)
                limit1 = (int)(20*bn_player_power)
                dmg = renpy.random.randint(limit1,limit)
                bn_cpu_hp = max(0,(bn_cpu_hp-dmg))
                bn_cpu_counter_stun = True
        elif attack_type == "rage":
            if bn_combo_idx > bn_rage_record:
                bn_rage_record = bn_combo_idx
                bn_rage_new_record = True
            dmg = (int) (bn_combo_idx*1.25*bn_player_power)
            bn_cpu_hp = max(0,(bn_cpu_hp-dmg))
        
        if dmg > bn_dmg_record:
            bn_dmg_record = dmg
            bn_dmg_new_record = True
        bn_show_image(attack_type)
        return

    def bn_player_normal_attack():
        
        bn_populate_arrow_combo(renpy.random.randint(3,4))
        renpy.show_screen("brawler_arrow_combo_screen")
        return

    def bn_player_power_attack():
        global bn_mc_stamina
        global bn_cpu_stamina
        global bn_arrow_selection
        global bn_arrow_input
        bn_mc_stamina -= 2
        
        bn_populate_arrow_combo(renpy.random.randint(4,5))
        renpy.show_screen("brawler_arrow_combo_screen")
        return

    def bn_player_special_attack():
        global bn_mc_stamina
        global bn_player_special_cd
        global bn_rage_time
        global e_time
        global timer_range
        global bn_player_rage
        global bn_combo_idx
        global bn_hard_difficulty
        bn_player_special_cd = 3
        if bn_arrow_selection[bn_arrow_input] == "RAGE":
            bn_rage_time = bn_mc_stamina
            bn_combo_idx = bn_player_rage
            e_time = bn_rage_time
            timer_range = bn_rage_time
            
            bn_mc_stamina = 0
            bn_populate_rage_arrow()
            bn_play_rage(0,0,0)
            renpy.show_screen("brawler_rage_screen")
        else:
            bn_mc_stamina -= 4
            if bn_hard_difficulty:
                bn_populate_arrow_combo(renpy.random.randint(6,7))
            else:
                bn_populate_arrow_combo(renpy.random.randint(5,6))
            renpy.show_screen("brawler_arrow_combo_screen")
        return

    def bn_player_block_attack():
        global bn_hard_difficulty
        global bn_which_fighter
        global bn_opponent_list
        if bn_hard_difficulty and bn_opponent_list[bn_which_fighter][1]>8:
            bn_populate_arrow_combo(renpy.random.randint(4,5))
        else:
            bn_populate_arrow_combo(renpy.random.randint(3,4))
        renpy.show_screen("brawler_arrow_combo_screen")
        return

    def bn_player_dodge_attack():
        global bn_mc_stamina
        global bn_hard_difficulty
        global bn_which_fighter
        global bn_opponent_list
        bn_mc_stamina -= 1
        if bn_hard_difficulty and bn_opponent_list[bn_which_fighter][1]>8:
            bn_populate_arrow_combo(renpy.random.randint(5,6))
        else:
            bn_populate_arrow_combo(renpy.random.randint(4,5))
        renpy.show_screen("brawler_arrow_combo_screen")
        return

    def bn_decide_turn():
        global bn_turn
        global bn_cpu_stunned
        if bn_cpu_stunned:
            bn_cpu_stunned = False
            return
        bn_turn = not bn_turn
        return

    def bn_reduce_cd():
        global bn_player_special_cd
        global bn_cpu_special_cd
        global bn_turn
        if bn_turn:
            bn_player_special_cd = max(0,bn_player_special_cd-1)
        else:
            bn_cpu_special_cd = max(0,bn_cpu_special_cd-1)
        return

    def bn_recover_stamina():
        global bn_mc_stamina
        global bn_cpu_stamina
        global bn_mc_stamina_max
        global bn_cpu_stamina_max
        
        if bn_mc_stamina < bn_mc_stamina_max:
            bn_mc_stamina += 1
        if bn_cpu_stamina < bn_cpu_stamina_max:
            bn_cpu_stamina += 1
        return

    def bn_cpu_prepare_attack():
        global bn_cpu_stamina
        global bn_cpu_attack
        global bn_cpu_special_cd
        bn_cpu_attack = ""
        while bn_cpu_attack == "":
            tmpInt = renpy.random.randint(0,2)
            if tmpInt == 0 and bn_cpu_stamina > 1:
                bn_cpu_attack = "power"
            elif tmpInt == 1 and bn_cpu_stamina > 3 and bn_cpu_special_cd == 0:
                bn_cpu_attack = "special"
            elif tmpInt == 2:
                bn_cpu_attack = "normal"
        return

    def bn_init_fight(fighter):
        global bn_img_list
        global bn_cpu_name
        global bn_delay_list
        global bn_sound_list
        global bn_game_over
        global bn_mc_won
        global bn_mc_hp
        global bn_cpu_hp
        global bn_opponent_list
        global bn_cpu_stamina_lvl
        global bn_cpu_stamina_max
        global bn_cpu_stamina
        global bn_cpu_power
        global bn_mc_stamina_max
        global bn_mc_stamina
        global bn_special_list
        global bn_special
        global bn_cpu_stunned
        global bn_cpu_counter_stun
        global bn_showing_img
        global bn_turn
        global bn_which_fighter
        global bn_rage_new_record
        global bn_dmg_new_record
        global bn_cpu_counter_chance
        global bn_hard_difficulty
        global ep10_troy_mad
        global bn_specials_unlocked
        
        if bn_hard_difficulty:
            bn_cpu_counter_chance = 8
        else:
            bn_cpu_counter_chance = 5
        
        bn_rage_new_record = False
        bn_dmg_new_record = False
        bn_which_fighter = fighter
        bn_game_over = False
        bn_turn = True
        bn_mc_won = False
        bn_showing_img = False
        bn_cpu_stunned = False
        bn_cpu_counter_stun = False
        bn_mc_stamina = bn_mc_stamina_max
        bn_mc_hp = 100
        bn_cpu_name = bn_opponent_list[fighter][0]
        if bn_special >= 0 and bn_specials_unlocked[bn_special]:
            bn_special_list = ["SPECIAL","RAGE"]
        else:
            bn_special_list = ["RAGE"]
        bn_img_list = []
        bn_delay_list = []
        bn_sound_list = []
        
        bn_opponent_list
        bn_cpu_hp = bn_opponent_list[fighter][3]
        bn_cpu_stamina_lvl = bn_opponent_list[fighter][4]
        bn_cpu_stamina_max = 2*bn_cpu_stamina_lvl
        bn_cpu_stamina = bn_cpu_stamina_max
        bn_cpu_power = 0.5 + 0.5 * bn_opponent_list[fighter][2]
        
        bn_img_list.append(["block"])
        bn_img_list.append(["dodge"])
        bn_img_list.append(["normal"])
        bn_img_list.append(["power"])
        bn_img_list.append(["special"])
        bn_img_list.append(["rage"])
        bn_img_list.append(["cpu_normal"])
        bn_img_list.append(["cpu_power"])
        bn_img_list.append(["cpu_special"])
        bn_img_list.append(["cpu_block"])
        bn_img_list.append(["cpu_dodge"])
        bn_img_list.append(["win"])
        bn_img_list.append(["lose"])
        if bn_opponent_list[fighter][0] == "Troy":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            bn_img_list[3].append("mc_power4")
            bn_img_list[3].append("mc_power5")
            bn_delay_list.append([1,1,2.5,1,1])
            bn_sound_list.append([bn_play_kick_slap,bn_play_kick,bn_play_silence,bn_play_silence,bn_play_kick])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([4])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([4])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_kick1")
            bn_img_list[6].append("cpu_kick2")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick,bn_play_punch,bn_play_punch])
            
            bn_img_list[8].append("cpu_special")
            bn_delay_list.append([1.4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_img_list[9].append("cpu_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            if ep10_troy_mad:
                bn_img_list[11].append("mc_win1")
            else:
                bn_img_list[11].append("mc_win2")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            if ep10_troy_mad:
                bn_img_list[12].append("mc_lose1")
            else:
                bn_img_list[12].append("mc_lose2")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        elif bn_opponent_list[fighter][0] == "Alex":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap2])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            bn_img_list[3].append("mc_power4")
            bn_img_list[3].append("mc_power5")
            bn_delay_list.append([1,1.5,2.5,2.0,1])
            bn_sound_list.append([bn_play_kick_slap,bn_play_silence,bn_play_silence,bn_play_silence,bn_play_kick_body])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([4])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([4])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_punch3")
            bn_img_list[6].append("cpu_kick1")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick_body])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick,bn_play_punch,bn_play_punch])
            
            bn_img_list[8].append("cpu_special")
            bn_delay_list.append([1])
            bn_sound_list.append([bn_play_kick_slap2])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_img_list[9].append("cpu_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[11].append("mc_win")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[12].append("mc_lose")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        elif bn_opponent_list[fighter][0] == "Chao":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_img_list[1].append("mc_dodge4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            bn_img_list[3].append("mc_power4")
            bn_img_list[3].append("mc_power5")
            bn_delay_list.append([1,1,1.5,2.0,1])
            bn_sound_list.append([bn_play_kick,bn_play_kick_slap,bn_play_silence,bn_play_silence,bn_play_kick])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([4])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([4])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_punch3")
            bn_img_list[6].append("cpu_kick1")
            bn_img_list[6].append("cpu_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap2])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick_slap2,bn_play_kick,bn_play_kick_slap])
            
            bn_img_list[8].append("cpu_special1")
            bn_delay_list.append([2])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_img_list[9].append("cpu_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[11].append("mc_win")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[12].append("mc_lose")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        elif bn_opponent_list[fighter][0] == "Dwyane":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick_body,bn_play_kick_slap2])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            bn_img_list[3].append("mc_power4")
            bn_img_list[3].append("mc_power5")
            bn_delay_list.append([1,1,1.5,1.5,1])
            bn_sound_list.append([bn_play_kick,bn_play_kick_slap,bn_play_silence,bn_play_silence,bn_play_kick_slap2])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([2])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([2])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_punch3")
            bn_img_list[6].append("cpu_kick1")
            bn_img_list[6].append("cpu_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick_body,bn_play_kick_slap])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick,bn_play_kick,bn_play_punch])
            
            bn_img_list[8].append("cpu_special")
            bn_delay_list.append([1.5])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_img_list[9].append("cpu_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[11].append("mc_win")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[12].append("mc_lose")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        elif bn_opponent_list[fighter][0] == "Tate":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_img_list[1].append("mc_dodge4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick_body,bn_play_kick_body])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            bn_img_list[3].append("mc_power4")
            bn_img_list[3].append("mc_power5")
            bn_delay_list.append([1,1,1.5,1.5,1])
            bn_sound_list.append([bn_play_kick_slap2,bn_play_kick_slap2,bn_play_silence,bn_play_silence,bn_play_punch])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([4])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([4])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_kick1")
            bn_img_list[6].append("cpu_kick2")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_kick_slap2,bn_play_kick_slap2])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick_slap,bn_play_kick_slap2,bn_play_punch])
            
            bn_img_list[8].append("cpu_special1")
            bn_delay_list.append([1.5])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[11].append("mc_win")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[12].append("mc_lose")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        elif bn_opponent_list[fighter][0] == "Dawe":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap2])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            bn_img_list[3].append("mc_power4")
            bn_img_list[3].append("mc_power5")
            bn_delay_list.append([1,1.5,2.5,2.0,1])
            bn_sound_list.append([bn_play_kick_slap,bn_play_silence,bn_play_silence,bn_play_silence,bn_play_kick_body])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([2])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([2])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4.5])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_punch3")
            bn_img_list[6].append("cpu_kick1")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick_body])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick,bn_play_punch,bn_play_punch])
            
            bn_img_list[8].append("cpu_special")
            bn_delay_list.append([1])
            bn_sound_list.append([bn_play_kick_slap2])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_img_list[9].append("cpu_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[11].append("mc_win")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[12].append("mc_lose")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        elif bn_opponent_list[fighter][0] == "Johnny":
            
            bn_img_list[0].append("mc_block1")
            bn_img_list[0].append("mc_block2")
            bn_img_list[0].append("mc_block3")
            bn_img_list[0].append("mc_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[1].append("mc_dodge1")
            bn_img_list[1].append("mc_dodge2")
            bn_img_list[1].append("mc_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[2].append("mc_punch1")
            bn_img_list[2].append("mc_punch2")
            bn_img_list[2].append("mc_punch3")
            bn_img_list[2].append("mc_kick1")
            bn_img_list[2].append("mc_kick2")
            bn_delay_list.append([1,1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick,bn_play_kick_slap2])
            
            bn_img_list[3].append("mc_power1")
            bn_img_list[3].append("mc_power2")
            bn_img_list[3].append("mc_power3")
            if not breakup and (branchMayaJosy or branchSage):
                bn_img_list[3].append("mc_power4jms")
                bn_delay_list.append([1,1.5,3,3.0,1])
            elif branchZoey:
                bn_img_list[3].append("mc_power4z")
                bn_delay_list.append([1,1.5,3,3.0,1])
            elif not ep12_nicole_breakup and ep12_nicole_path and not ep12_nicole_ditch:
                bn_img_list[3].append("mc_power4n")
                bn_delay_list.append([1,1.5,3,3.0,1])
            else:
                bn_img_list[3].append("mc_power4")
                bn_delay_list.append([1,1.5,3,2.0,1])
            bn_img_list[3].append("mc_power5")
            bn_sound_list.append([bn_play_kick_slap,bn_play_silence,bn_play_silence,bn_play_silence,bn_play_kick_slap])
            
            if bn_special == 0:
                bn_img_list[4].append("flurry")
                bn_delay_list.append([4])
                bn_sound_list.append([play_bn_flurry])
            elif bn_special == 1:
                bn_img_list[4].append("crippling")
                bn_delay_list.append([4])
                bn_sound_list.append([bn_play_silence])
            elif bn_special == 2:
                bn_img_list[4].append("highkick")
                bn_delay_list.append([5])
                bn_sound_list.append([play_bn_highkick])
            else:
                bn_img_list[4].append("")
                bn_delay_list.append([1])
                bn_sound_list.append([bn_play_silence])
            
            bn_img_list[5].append("mc_rage")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[6].append("cpu_punch1")
            bn_img_list[6].append("cpu_punch2")
            bn_img_list[6].append("cpu_punch3")
            bn_img_list[6].append("cpu_kick1")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_punch,bn_play_punch,bn_play_punch,bn_play_kick_body])
            
            bn_img_list[7].append("cpu_power1")
            bn_img_list[7].append("cpu_power2")
            bn_img_list[7].append("cpu_power3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_kick,bn_play_punch,bn_play_punch])
            
            bn_img_list[8].append("cpu_special")
            bn_delay_list.append([1])
            bn_sound_list.append([bn_play_punch])
            
            bn_img_list[9].append("cpu_block")
            bn_img_list[9].append("cpu_block2")
            bn_img_list[9].append("cpu_block3")
            bn_img_list[9].append("cpu_block4")
            bn_delay_list.append([1,1,1,1])
            bn_sound_list.append([bn_play_block,bn_play_block,bn_play_block,bn_play_block])
            
            bn_img_list[10].append("cpu_dodge")
            bn_img_list[10].append("cpu_dodge2")
            bn_img_list[10].append("cpu_dodge3")
            bn_delay_list.append([1,1,1])
            bn_sound_list.append([bn_play_dodge,bn_play_dodge,bn_play_dodge])
            
            bn_img_list[11].append("mc_win")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
            
            bn_img_list[12].append("mc_lose")
            bn_delay_list.append([4])
            bn_sound_list.append([bn_play_silence])
        
        renpy.show_screen("brawler_screen")
        return

    def bn_hide_image():
        global bn_showing_img
        global bn_counter
        global bn_turn
        global bn_cpu_attack
        global bn_show_counter
        global bn_story_fight
        
        bn_showing_img = False
        bn_show_counter = False
        
        if bn_check_game_over():
            if bn_story_fight:
                bn_showing_img = True
            return
        if bn_counter:
            bn_counter = False
            if bn_turn:
                bn_cpu_attack = "normal"
                bn_player_got_hit()
            else:
                bn_cpu_got_hit("normal")
            return
        bn_decide_turn()
        bn_next_round()
        return

    def bn_show_image(img):
        global bn_img_list
        global bn_delay_list
        global bn_showing_img
        global bn_img_name
        global bn_img_delay
        global bn_sound_list
        
        idx = list(map(itemgetter(0), bn_img_list)).index(img)
        
        tmpInt = renpy.random.randint(1,len(bn_img_list[idx])-1)
        bn_showing_img = True
        bn_img_name = bn_img_list[idx][tmpInt]
        bn_img_delay = bn_delay_list[idx][tmpInt-1]
        
        bn_sound_list[idx][tmpInt-1](0,0,0)
        
        return

    def bn_check_game_over():
        global bn_mc_hp
        global bn_cpu_hp
        global bn_mc_won
        global bn_game_over
        global bn_fight_count
        global bn_fight_losses
        global bn_fight_wins
        global bn_story_fight
        
        if not bn_game_over:
            if bn_mc_hp == 0:
                bn_fight_count = bn_fight_count + 1
                bn_fight_losses = bn_fight_losses + 1
                bn_game_over = True
                bn_mc_won = False
                if not bn_story_fight:
                    bn_show_image("lose")
                    bn_play_bell(0,0,0)
                return True
            elif bn_cpu_hp == 0:
                bn_fight_count = bn_fight_count + 1
                bn_fight_wins = bn_fight_wins + 1
                bn_game_over = True
                bn_mc_won = True
                if not bn_story_fight:
                    bn_show_image("win")
                    bn_handle_rewards()
                    bn_play_bell(0,0,0)
                return True
        else:
            return True
        return False

    def bn_handle_rewards():
        global bn_opponent_list
        global bn_which_fighter
        global bn_skill_points
        global bn_skill_points_total
        global bn_skill_max_level
        global bn_specials_unlocked
        global bn_reward
        global bn_sr_reward
        global bn_money_reward
        global bn_money_reward2
        global bn_money_reward3
        global bn_skill_alloc
        global bn_reward_available_list
        
        bn_reward = bn_opponent_list[bn_which_fighter][5]
        if bn_opponent_list[bn_which_fighter][6] == "sa":
            bn_specials_unlocked[bn_opponent_list[bn_which_fighter][7]] = True
        elif bn_opponent_list[bn_which_fighter][6] == "sr":
            if bn_opponent_list[bn_which_fighter][7] == "sr1":
                if currentEpisode == 10 and not persistent.ep10_cardsa19:
                    bn_sr_reward = False
                    persistent.ep10_cardsa19 = True
                    persistent.rew_sage_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                elif currentEpisode == 11 and not persistent.ep11_cardmy15:
                    bn_sr_reward = False
                    persistent.ep11_cardmy15 = True
                    persistent.rew_maya_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                elif currentEpisode == 12 and not persistent.ep12_cardisa14:
                    bn_sr_reward = False
                    persistent.ep12_cardisa14 = True
                    persistent.rew_isa_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
        elif bn_opponent_list[bn_which_fighter][6] == "sml":
            bn_skill_max_level = min(bn_skill_max_level+bn_opponent_list[bn_which_fighter][7],5)
        elif bn_opponent_list[bn_which_fighter][6] == "money":
            if bn_which_fighter == 1:
                bn_money_reward = False
            elif bn_which_fighter == 2:
                bn_money_reward2 = False
            else:
                bn_money_reward3 = False
            mny(bn_opponent_list[bn_which_fighter][7])
        elif bn_opponent_list[bn_which_fighter][6] == "skill point":
            if bn_skill_alloc[4] == 0:
                bn_skill_alloc[4] = 1
                bn_skill_points_total += 1
                bn_reward_available_list[3] = 3
                bn_update_player_skills(4)
            elif bn_skill_alloc[3] == 0:
                bn_skill_alloc[3] = 1
                bn_skill_points_total += 1
                bn_reward_available_list[3] = 2
                bn_update_player_skills(3)
            elif bn_skill_alloc[2] == 0:
                bn_skill_alloc[2] = 1
                bn_skill_points_total += 1
                bn_reward_available_list[3] = 1
                bn_update_player_skills(2)
            elif bn_skill_alloc[0] == 0:
                bn_skill_alloc[0] = 1
                bn_skill_points_total += 1
                bn_reward_available_list[3] = 0
                bn_update_player_skills(0)
        elif bn_opponent_list[bn_which_fighter][6] == "skill points":
            bn_skill_points_total += bn_opponent_list[bn_which_fighter][7]
            if bn_skill_points_total > 30:
                bn_skill_points += bn_skill_points_total - 30
                bn_skill_points_total = 30
            else:
                bn_skill_points += bn_opponent_list[bn_which_fighter][7]
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

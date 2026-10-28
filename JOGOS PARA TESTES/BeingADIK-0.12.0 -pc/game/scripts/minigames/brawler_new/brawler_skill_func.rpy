init python:
    def bn_reset_skill_points():
        global bn_skill_points
        global bn_skill_alloc
        global bonusPointsSports
        global bn_reward_available_list
        tmpList = [0,2,0,0,0,0]
        if bonusPointsSports == 12 or bn_reward_available_list[3] == 0:
            tmpList[0] = 1
        if bonusPointsSports > 8 or bn_reward_available_list[3] < 2:
            tmpList[2] = 1
        if bonusPointsSports > 5 or bn_reward_available_list[3] < 3:
            tmpList[3] = 1
        if bonusPointsSports > 2 or bn_reward_available_list[3] < 4:
            tmpList[4] = 1
        
        for i in range(0,6):
            bn_skill_points += bn_skill_alloc[i]-tmpList[i]
        init_brawler_mg(False)
        
        for i in range(0,6):
            bn_update_player_skills(i)
        return

    def bn_set_skill(which, lvl):
        global bn_skill_points
        global bn_skill_alloc
        
        if bn_skill_alloc[which] == lvl:
            bn_play_click(0,0,0)
            bn_skill_points += 1
            bn_skill_alloc[which] -= 1
        elif bn_skill_alloc[which] > lvl:
            bn_play_click(0,0,0)
            bn_skill_points += bn_skill_alloc[which] - lvl
            bn_skill_alloc[which] = lvl
        elif bn_skill_alloc[which] < lvl:
            if bn_skill_points >= lvl - bn_skill_alloc[which]:
                bn_play_click(0,0,0)
                bn_skill_points -= lvl - bn_skill_alloc[which]
                bn_skill_alloc[which] = lvl
            else:
                if bn_skill_points == 0:
                    bn_play_failed_click(0,0,0)
                else:
                    bn_play_click(0,0,0)
                bn_skill_alloc[which] += bn_skill_points
                bn_skill_points = 0
        bn_update_player_skills(which)
        return

    def bn_update_player_skills(which):
        global bn_skill_alloc
        global bn_player_power
        global bn_mc_stamina_lvl
        global bn_mc_stamina_max
        global bn_timer
        global bn_player_block
        global bn_pc_counter_chance
        global bn_player_rage
        global bn_hard_difficulty
        
        if which == 0:
            bn_player_power = 0.75 + bn_skill_alloc[which] * 0.25
        elif which == 1:
            bn_mc_stamina_lvl = bn_skill_alloc[which]
            bn_mc_stamina_max = bn_skill_alloc[which] * 2
        elif which == 2:
            if bn_hard_difficulty:
                bn_timer = 2.5 + bn_skill_alloc[which] * 0.25
            else:
                bn_timer = 4.0 + bn_skill_alloc[which] * 0.4
        elif which == 3:
            bn_player_block = 0.55 + 0.05 * bn_skill_alloc[which]
        elif which == 4:
            bn_pc_counter_chance = 2 + bn_skill_alloc[which]
        elif which == 5:
            bn_player_rage = 5 * bn_skill_alloc[which]
        
        return

    def bn_lower_difficulty():
        global bn_timer
        global bn_hard_difficulty
        bn_hard_difficulty = False
        bn_timer = 4.0 + bn_skill_alloc[2] * 0.4
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

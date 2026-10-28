init python:
    def bn_init_opponents():
        global bn_reward_available_list
        global bn_opponent_list
        global bn_money_reward
        global bn_sr_reward
        global bn_hard_difficulty
        global bn_history_list
        global bn_skill_points_total
        global bn_story_fight
        global bn_story_fight_round
        
        bn_check_sr_reward()
        bn_opponent_list = []
        
        bn_scaling = 0
        if bn_skill_points_total < 9:
            bn_scaling = 0
        elif bn_skill_points_total < 12 or bn_skill_max_level == 2:
            bn_scaling = 1
        elif bn_skill_points_total < 15 or bn_skill_max_level == 3:
            bn_scaling = 2
        elif bn_skill_points_total < 20 or bn_skill_max_level == 4:
            bn_scaling = 3
        else:
            bn_scaling = 4
        
        bn_scaling_list = []
        if bn_hard_difficulty:
            bn_scaling_list.append([[2,2,2],[4,4,3],[7,6,3],[8,7,4],[8,8,4]])
            bn_scaling_list.append([[3,3,2],[5,5,3],[8,7,4],[9,8,4],[9,9,4]])
            bn_scaling_list.append([[5,4,3],[8,7,4],[9,9,4],[10,10,4],[11,11,4]])
            bn_scaling_list.append([[7,7,3],[8,8,4],[10,10,4],[11,11,4],[12,12,4]])
            bn_scaling_list.append([[4,3,4],[7,7,4],[8,8,4],[9,8,4],[10,10,4]])
        else:
            bn_scaling_list.append([[1,1,1],[2,2,2],[3,3,3],[4,4,3],[5,5,3]])
            bn_scaling_list.append([[2,2,2],[3,3,2],[4,3,4],[5,5,3],[6,6,4]])
            bn_scaling_list.append([[3,3,2],[5,4,3],[7,6,4],[8,7,4],[9,9,4]])
            bn_scaling_list.append([[6,6,3],[7,7,3],[8,8,4],[9,9,4],[10,10,4]])
            bn_scaling_list.append([[3,2,3],[4,3,4],[6,5,4],[7,7,4],[8,8,4]])
        if bn_story_fight:
            if currentEpisode == 12:
                if bn_story_fight_round == 1:
                    bn_scaling_list.append([[9,9,4],[9,9,4],[9,9,4],[9,9,4],[9,9,4]])
                elif bn_story_fight_round == 2:
                    bn_scaling_list.append([[11,11,4],[11,11,4],[11,11,4],[11,11,4],[11,11,4]])
                else:
                    bn_scaling_list.append([[10,10,4],[10,10,4],[10,10,4],[10,10,4],[10,10,4]])
        
        
        if bn_reward_available_list[3] > 0:
            bn_opponent_list.append(["Troy", bn_scaling_list[0][bn_scaling][0], bn_scaling_list[0][bn_scaling][1], 100, bn_scaling_list[0][bn_scaling][2], "{color=#00b0ff}Skill point +1{/color}", "skill point", 1,bn_history_list[0]])
        else:
            if bn_skill_points_total + 2 <= bn_reward_available_list[0]:
                bn_opponent_list.append(["Troy", bn_scaling_list[0][bn_scaling][0], bn_scaling_list[0][bn_scaling][1], 100, bn_scaling_list[0][bn_scaling][2], "{color=#ffe059}Skill points +2{/color}", "skill points", 2,bn_history_list[0]])
            else:
                bn_opponent_list.append(["Troy", bn_scaling_list[0][bn_scaling][0], bn_scaling_list[0][bn_scaling][1], 100, bn_scaling_list[0][bn_scaling][2], "{color=ededed}No reward{/color}", "", 0,bn_history_list[0]])
        
        if bn_history_list[1] < 2 or currentEpisode == 10:
            if bn_money_reward:
                bn_opponent_list.append(["Alex", bn_scaling_list[1][bn_scaling][0], bn_scaling_list[1][bn_scaling][1], 100, bn_scaling_list[1][bn_scaling][2],"{color=#1df400}Money $2{/color}", "money", 2,bn_history_list[1]])
            else:
                bn_opponent_list.append(["Alex", bn_scaling_list[1][bn_scaling][0], bn_scaling_list[1][bn_scaling][1], 100, bn_scaling_list[1][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[1]])
        else:
            if bn_money_reward:
                bn_opponent_list.append(["Dawe", bn_scaling_list[1][bn_scaling][0], bn_scaling_list[1][bn_scaling][1], 100, bn_scaling_list[1][bn_scaling][2],"{color=#1df400}Money $2{/color}", "money", 2,bn_history_list[1]])
            else:
                bn_opponent_list.append(["Dawe", bn_scaling_list[1][bn_scaling][0], bn_scaling_list[1][bn_scaling][1], 100, bn_scaling_list[1][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[1]])
        
        if bn_skill_max_level < bn_reward_available_list[2]:
            bn_opponent_list.append(["Chao", bn_scaling_list[2][bn_scaling][0], bn_scaling_list[2][bn_scaling][1], 150, bn_scaling_list[2][bn_scaling][2],"{color=00b0ff}Skill Max Level +1{/color}", "sml", 1,bn_history_list[2]])
        elif bn_money_reward2 and bn_skill_max_level == 5:
            bn_opponent_list.append(["Chao", bn_scaling_list[2][bn_scaling][0], bn_scaling_list[2][bn_scaling][1], 150, bn_scaling_list[2][bn_scaling][2],"{color=#1df400}Money $2{/color}", "money", 2,bn_history_list[2]])
        else:
            bn_opponent_list.append(["Chao", bn_scaling_list[2][bn_scaling][0], bn_scaling_list[2][bn_scaling][1], 150, bn_scaling_list[2][bn_scaling][2], "{color=ededed}No reward{/color}", "", 0,bn_history_list[2]])
        
        if bn_specials_unlocked.count(True) < bn_reward_available_list[1]:
            bn_opponent_list.append(["Dwyane", bn_scaling_list[3][bn_scaling][0], bn_scaling_list[3][bn_scaling][1], 200, bn_scaling_list[3][bn_scaling][2],"{color=#fe9416}Special Attack{/color}","sa",bn_specials_unlocked.count(True),bn_history_list[3]])
        elif bn_money_reward3 and bn_specials_unlocked.count(True) == 3:
            bn_opponent_list.append(["Dwyane", bn_scaling_list[3][bn_scaling][0], bn_scaling_list[3][bn_scaling][1], 200, bn_scaling_list[3][bn_scaling][2],"{color=#1df400}Money $2{/color}", "money", 2,bn_history_list[3]])
        else:
            bn_opponent_list.append(["Dwyane", bn_scaling_list[3][bn_scaling][0], bn_scaling_list[3][bn_scaling][1], 200, bn_scaling_list[3][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[3]])
        
        if bn_sr_reward:
            bn_opponent_list.append(["Tate", bn_scaling_list[4][bn_scaling][0], bn_scaling_list[4][bn_scaling][1], 100, bn_scaling_list[4][bn_scaling][2],"{color=#fe67b2}Special Render{/color}","sr","sr1",bn_history_list[4]])
        else:
            bn_opponent_list.append(["Tate", bn_scaling_list[4][bn_scaling][0], bn_scaling_list[4][bn_scaling][1], 100, bn_scaling_list[4][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[4]])
        
        if bn_story_fight:
            if currentEpisode == 12:
                if bn_story_fight_round == 1:
                    bn_opponent_list.append(["Johnny", bn_scaling_list[5][bn_scaling][0], bn_scaling_list[5][bn_scaling][1], 100, bn_scaling_list[5][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[5]])
                elif bn_story_fight_round == 2:
                    bn_opponent_list.append(["Johnny", bn_scaling_list[5][bn_scaling][0], bn_scaling_list[5][bn_scaling][1], 150, bn_scaling_list[5][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[5]])
                else:
                    bn_opponent_list.append(["Johnny", bn_scaling_list[5][bn_scaling][0], bn_scaling_list[5][bn_scaling][1], 200, bn_scaling_list[5][bn_scaling][2],"{color=ededed}No reward{/color}", "", 0,bn_history_list[5]])
        
        return

    def bn_check_sr_reward():
        global bn_sr_reward
        global currentEpisode
        if currentEpisode == 10 and not persistent.ep10_cardsa19:
            bn_sr_reward = True
        elif currentEpisode == 11 and not persistent.ep11_cardmy15:
            bn_sr_reward = True
        elif currentEpisode == 12 and not persistent.ep12_cardisa14:
            bn_sr_reward = True
        else:
            bn_sr_reward = False
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

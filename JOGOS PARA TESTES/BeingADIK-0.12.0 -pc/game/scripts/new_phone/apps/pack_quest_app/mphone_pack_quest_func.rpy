init python:
    def unlock_pq_renders():
        global pq_open_animation
        pq_open_animation = False
        
        if currentEpisode == 9:
            if not persistent.ep9_card9:
                persistent.ep9_card9 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card10:
                persistent.ep9_card10 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card11:
                persistent.ep9_card11 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card12:
                persistent.ep9_card12 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card13:
                persistent.ep9_card13 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card14:
                persistent.ep9_card14 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card15:
                persistent.ep9_card15 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep9_card16:
                persistent.ep9_card16 = True
                persistent.rew_mixed_unlocked += 1
            persistent.chat_new_rewards = True
            calcRenders()
            persistent.pack_quest4_completed = True
        elif currentEpisode == 10:
            if not persistent.ep10_card1:
                persistent.ep10_card1 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card2:
                persistent.ep10_card2 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card3:
                persistent.ep10_card3 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card4:
                persistent.ep10_card4 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card5:
                persistent.ep10_card5 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card6:
                persistent.ep10_card6 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card7:
                persistent.ep10_card7 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep10_card8:
                persistent.ep10_card8 = True
                persistent.rew_mixed_unlocked += 1
            persistent.chat_new_rewards = True
            calcRenders()
            persistent.pack_quest5_completed = True
        elif currentEpisode == 11:
            if not persistent.ep11_card1:
                persistent.ep11_card1 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card2:
                persistent.ep11_card2 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card3:
                persistent.ep11_card3 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card4:
                persistent.ep11_card4 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card5:
                persistent.ep11_card5 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card6:
                persistent.ep11_card6 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card7:
                persistent.ep11_card7 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep11_card8:
                persistent.ep11_card8 = True
                persistent.rew_mixed_unlocked += 1
            persistent.chat_new_rewards = True
            calcRenders()
            persistent.pack_quest6_completed = True
        elif currentEpisode == 12:
            if not persistent.ep12_card1:
                persistent.ep12_card1 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card2:
                persistent.ep12_card2 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card3:
                persistent.ep12_card3 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card4:
                persistent.ep12_card4 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card5:
                persistent.ep12_card5 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card6:
                persistent.ep12_card6 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card7:
                persistent.ep12_card7 = True
                persistent.rew_mixed_unlocked += 1
            if not persistent.ep12_card8:
                persistent.ep12_card8 = True
                persistent.rew_mixed_unlocked += 1
            persistent.chat_new_rewards = True
            calcRenders()
            persistent.pack_quest7_completed = True
        
        return

    def pq_check_tasks():
        global pq_found_buttons
        global pack_quest_list
        i = 0
        pq_found_buttons = 0
        for x in range(0,len(pack_quest_list)):
            if pack_quest_list[x][1]:
                pq_found_buttons += 1
                if pack_quest_list[x][0][0] != "{color=#00a400}%s{/color}" % pack_quest_list[x][0]:
                    pack_quest_list[x][0] = "{color=#00a400}%s{/color}" % pack_quest_list[x][0]
            i += 1
        return

    def mphone_pack_quest_clear():
        global pq_found_buttons
        global pack_quest_list
        global pack_quest_active
        pack_quest_active = False
        pack_quest_list = []
        pack_quest_available = False
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

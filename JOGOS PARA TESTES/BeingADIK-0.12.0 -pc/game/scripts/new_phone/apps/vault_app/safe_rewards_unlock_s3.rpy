init:
    if persistent.vaulti == None:
        $ persistent.vaulti = False
    if persistent.vaultep9 == None:
        $ persistent.vaultep9 = False

init python:
    def safe_rewards_unlock_epi():
        global minigames
        persistent.vaulti = True
        if not persistent.ep7_wpi1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpi1 = True
        if not persistent.ep7_wpi2:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpi2 = True
        if not persistent.ep7_wpj1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpj1 = True
        if not persistent.ep7_wpj2:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpj2 = True
        if not persistent.ep7_wpjo1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpjo1 = True
        if not persistent.ep7_wpjo2:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpjo2 = True
        if not persistent.ep7_wpm1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpm1 = True
        if not persistent.ep7_wpm2:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wpm2 = True
        if not persistent.ep7_wps1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wps1 = True
        if not persistent.ep7_wps2:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep7_wps2 = True
        if not persistent.ep8_wpi1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpi1 = True
        if not persistent.ep8_wpj1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpj1 = True
        if not persistent.ep8_wpjo1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpjo1 = True
        if not persistent.ep8_wpm1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpm1 = True
        if not persistent.ep8_wpq1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpq1 = True
        if not persistent.ep8_wps1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wps1 = True
        if not persistent.ep8_wpe1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpe1 = True
        if not persistent.ep8_wpjade1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpjade1 = True
        if not persistent.ep8_wpmad1:
            persistent.chat_new_rewards = True
            persistent.rew_2d_unlocked += 1
            persistent.ep8_wpmad1 = True
        
        if not minigames:
            if not persistent.epi_card5:
                persistent.chat_new_rewards = True
                persistent.rew_mixed_unlocked += 1
                persistent.epi_card5 = True
            if not persistent.epi_card6:
                persistent.chat_new_rewards = True
                persistent.rew_mixed_unlocked += 1
                persistent.epi_card6 = True
            if not persistent.epi_card7:
                persistent.chat_new_rewards = True
                persistent.rew_mixed_unlocked += 1
                persistent.epi_card7 = True
        
        if not persistent.epi_card8:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.epi_card8 = True
        
        if not persistent.epi_card9:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.epi_card9 = True
        if not persistent.epi_card10:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.epi_card10 = True
        if not persistent.epi_card11:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.epi_card11 = True
        if not persistent.epi_card12:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.epi_card12 = True
        return

    def safe_rewards_unlock_ep9():
        global minigames
        persistent.vaultep9 = True
        if not persistent.ep9_cardjo18:
            persistent.chat_new_rewards = True
            persistent.rew_josy_unlocked += 1
            persistent.ep9_cardjo18 = True
        if not persistent.ep9_cardjo19:
            persistent.chat_new_rewards = True
            persistent.rew_josy_unlocked += 1
            persistent.ep9_cardjo19 = True
        if not persistent.ep9_cardjo20:
            persistent.chat_new_rewards = True
            persistent.rew_josy_unlocked += 1
            persistent.ep9_cardjo20 = True
        if not persistent.ep9_cardji18:
            persistent.chat_new_rewards = True
            persistent.rew_jill_unlocked += 1
            persistent.ep9_cardji18 = True
        if not persistent.ep9_cardji19:
            persistent.chat_new_rewards = True
            persistent.rew_jill_unlocked += 1
            persistent.ep9_cardji19 = True
        if not persistent.ep9_cardji20:
            persistent.chat_new_rewards = True
            persistent.rew_jill_unlocked += 1
            persistent.ep9_cardji20 = True
        return

    def safe_rewards_unlock_ep10():
        global minigames
        persistent.vaultep10 = True
        if not minigames:
            if not persistent.ep10_cardsa17:
                persistent.chat_new_rewards = True
                persistent.rew_sage_unlocked += 1
                persistent.ep10_cardsa17 = True
            if not persistent.ep10_cardsa18:
                persistent.chat_new_rewards = True
                persistent.rew_sage_unlocked += 1
                persistent.ep10_cardsa18 = True
            if not persistent.ep10_cardsa19:
                persistent.chat_new_rewards = True
                persistent.rew_sage_unlocked += 1
                persistent.ep10_cardsa19 = True
            if not persistent.ep10_cardsa20:
                persistent.chat_new_rewards = True
                persistent.rew_sage_unlocked += 1
                persistent.ep10_cardsa20 = True
        if not persistent.ep10_cardsa16:
            persistent.chat_new_rewards = True
            persistent.rew_sage_unlocked += 1
            persistent.ep10_cardsa16 = True
        if not persistent.ep10_cardsa15:
            persistent.chat_new_rewards = True
            persistent.rew_sage_unlocked += 1
            persistent.ep10_cardsa15 = True
        if not persistent.ep10_cardsa14:
            persistent.chat_new_rewards = True
            persistent.rew_sage_unlocked += 1
            persistent.ep10_cardsa14 = True
        if not persistent.ep10_cardsa13:
            persistent.chat_new_rewards = True
            persistent.rew_sage_unlocked += 1
            persistent.ep10_cardsa13 = True
        if not persistent.ep10_cardzo20:
            persistent.chat_new_rewards = True
            persistent.rew_zoey_unlocked += 1
            persistent.ep10_cardzo20 = True
        if not persistent.ep10_cardzo19:
            persistent.chat_new_rewards = True
            persistent.rew_zoey_unlocked += 1
            persistent.ep10_cardzo19 = True
        if not persistent.ep10_cardzo16:
            persistent.chat_new_rewards = True
            persistent.rew_zoey_unlocked += 1
            persistent.ep10_cardzo16 = True
        if not persistent.ep10_cardzo15:
            persistent.chat_new_rewards = True
            persistent.rew_zoey_unlocked += 1
            persistent.ep10_cardzo15 = True
        if not persistent.ep10_cardzo14:
            persistent.chat_new_rewards = True
            persistent.rew_zoey_unlocked += 1
            persistent.ep10_cardzo14 = True
        return

    def safe_rewards_unlock_ep11():
        global minigames
        persistent.vaultep11 = True
        if not minigames:
            if not persistent.ep11_cardmy10:
                persistent.chat_new_rewards = True
                persistent.rew_maya_unlocked += 1
                persistent.ep11_cardmy10 = True
            if not persistent.ep11_cardmy11:
                persistent.chat_new_rewards = True
                persistent.rew_maya_unlocked += 1
                persistent.ep11_cardmy11 = True
            if not persistent.ep11_cardmy12:
                persistent.chat_new_rewards = True
                persistent.rew_maya_unlocked += 1
                persistent.ep11_cardmy12 = True
            if not persistent.ep11_cardmy15:
                persistent.chat_new_rewards = True
                persistent.rew_maya_unlocked += 1
                persistent.ep11_cardmy15 = True
        if not persistent.ep11_cardmy6:
            persistent.chat_new_rewards = True
            persistent.rew_maya_unlocked += 1
            persistent.ep11_cardmy6 = True
        if not persistent.ep11_cardmy7:
            persistent.chat_new_rewards = True
            persistent.rew_maya_unlocked += 1
            persistent.ep11_cardmy7 = True
        if not persistent.ep11_cardmy8:
            persistent.chat_new_rewards = True
            persistent.rew_maya_unlocked += 1
            persistent.ep11_cardmy8 = True
        if not persistent.ep11_card9b:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep11_card9b = True
        if not persistent.ep11_card10b:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep11_card10b = True
        if not persistent.ep11_card11b:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep11_card11b = True
        if not persistent.ep11_card12b:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep11_card12b = True
        return

    def safe_rewards_unlock_ep12():
        global minigames
        persistent.vaultep12 = True
        if not minigames:
            if not persistent.ep12_cardisa9:
                persistent.chat_new_rewards = True
                persistent.rew_isa_unlocked += 1
                persistent.ep12_cardisa9 = True
            if not persistent.ep12_cardisa10:
                persistent.chat_new_rewards = True
                persistent.rew_isa_unlocked += 1
                persistent.ep12_cardisa10 = True
            if not persistent.ep12_cardisa11:
                persistent.chat_new_rewards = True
                persistent.rew_isa_unlocked += 1
                persistent.ep12_cardisa11 = True
            if not persistent.ep12_cardisa14:
                persistent.chat_new_rewards = True
                persistent.rew_isa_unlocked += 1
                persistent.ep12_cardisa14 = True
        
        if not persistent.ep12_card9:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep12_card9 = True
        if not persistent.ep12_card10:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep12_card10 = True
        if not persistent.ep12_card11:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep12_card11 = True
        if not persistent.ep12_card12:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep12_card12 = True
        if not persistent.ep12_card13:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep12_card13 = True
        if not persistent.ep12_card14:
            persistent.chat_new_rewards = True
            persistent.rew_mixed_unlocked += 1
            persistent.ep12_card14 = True
        if not persistent.ep12_cardcam20:
            persistent.chat_new_rewards = True
            persistent.rew_cam_unlocked += 1
            persistent.ep12_cardcam20 = True
        
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

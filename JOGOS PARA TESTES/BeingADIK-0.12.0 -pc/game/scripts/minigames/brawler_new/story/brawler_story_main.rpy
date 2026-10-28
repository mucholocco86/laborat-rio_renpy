label brawler_after_fight_label:
scene black
hide screen brawler_screen
if bn_opponent_list[bn_which_fighter][0] == "Alex":
    jump brawler_story_alex_after_label
elif bn_opponent_list[bn_which_fighter][0] == "Chao":
    jump brawler_story_chao_after_label
elif bn_opponent_list[bn_which_fighter][0] == "Dwyane":
    jump brawler_story_dwyane_after_label
elif bn_opponent_list[bn_which_fighter][0] == "Tate":
    jump brawler_story_tate_after_label
elif bn_opponent_list[bn_which_fighter][0] == "Troy":
    jump brawler_story_troy_after_label
elif bn_opponent_list[bn_which_fighter][0] == "Dawe":
    jump brawler_story_dawe_after_label
elif bn_opponent_list[bn_which_fighter][0] == "Johnny":
    jump brawler_story_johnny_after_label

label brawler_story_alex_label:
if bn_history_list[1] == 0:
    jump brawler_story_alex0_label
else:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Alex":
                bn_init_fight(i)
    pause

label brawler_story_alex_after_label:
if bn_history_list[1] == 1:
    if not bn_mc_won:
        jump brawler_story_alex_after0b_label
    else:
        jump brawler_story_alex_after0_label
else:
    show screen brawler_result_screen
pause

label brawler_story_chao_label:
if bn_history_list[2] == 0:
    jump brawler_story_chao0_label
elif bn_history_list[2] == 2 and currentEpisode > 10:
    jump brawler_story_chao1_label
else:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Chao":
                bn_init_fight(i)
    pause

label brawler_story_chao_after_label:
if bn_history_list[2] == 1:
    jump brawler_story_chao_after0_label
elif bn_history_list[2] == 3:
    jump brawler_story_chao_after1_label
else:
    show screen brawler_result_screen
pause

label brawler_story_dwyane_label:
if bn_history_list[3] == 0:
    jump brawler_story_dwyane0_label
elif bn_history_list[3] == 2 and currentEpisode > 10:
    jump brawler_story_dwyane1_label
else:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Dwyane":
                bn_init_fight(i)
    pause

label brawler_story_dwyane_after_label:
if bn_history_list[3] == 1:
    jump brawler_story_dwyane_after0_label
elif bn_history_list[3] == 3:
    jump brawler_story_dwyane_after1_label
else:
    show screen brawler_result_screen
pause

label brawler_story_tate_label:
if bn_history_list[4] == 0:
    jump brawler_story_tate0_label
elif bn_history_list[4] == 2 and currentEpisode > 10:
    jump brawler_story_tate1_label
else:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Tate":
                bn_init_fight(i)
    pause

label brawler_story_tate_after_label:
if bn_history_list[4] == 1:
    jump brawler_story_tate_after0_label
elif bn_history_list[4] == 3:
    jump brawler_story_tate_after1_label
else:
    show screen brawler_result_screen
pause

label brawler_story_troy_label:
if bn_history_list[0] == 0:
    jump brawler_story_troy0_label
elif bn_history_list[0] == 2 and currentEpisode > 10:
    jump brawler_story_troy1_label
else:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Troy":
                bn_init_fight(i)
    pause

label brawler_story_troy_after_label:
if bn_history_list[0] == 1:
    jump brawler_story_troy_after0_label
elif bn_history_list[0] == 3:
    jump brawler_story_troy_after1_label
else:
    show screen brawler_result_screen
pause

label brawler_story_dawe_label:
if bn_history_list[1] == 2:
    jump brawler_story_dawe0_label
else:
    python:
        for i in range(0,len(bn_opponent_list)):
            if bn_opponent_list[i][0] == "Dawe":
                bn_init_fight(i)
    pause

label brawler_story_dawe_after_label:
if bn_history_list[1] == 3:
    if not bn_mc_won:
        jump brawler_story_dawe_after0b_label
    else:
        jump brawler_story_dawe_after0_label
else:
    show screen brawler_result_screen
pause

label brawler_story_johnny_after_label:
if bn_history_list[5] == 1:
    jump ep12_fcomp_round1_end_label
elif bn_history_list[5] == 2:
    jump ep12_fcomp_round2_end_label
elif bn_history_list[5] == 3:
    jump ep12_fcomp_round3_end_label
else:
    show screen brawler_result_screen
pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

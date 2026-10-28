label init_eng_test_ep10_label:
$ renpy.block_rollback()
$ tmpMenu = quick_menu
$ quick_menu = 0
hide screen new_phone_screen
$ e_time = 200
$ timer_range = 200
$ eng_jump_label = "after_eng_test_ep10_label"
$ eng_rew = False
$ eng_cheated = False
$ eng_perc3 = 0
$ eng_perc4 = 0
$ eng_perc5 = 0
$ eng_perc6 = 0
$ eng_total3 = 0
$ eng_total4 = 0
$ eng_total5 = 0
$ eng_total6 = 0
$ eng_yalign = [0.34,0.34,0.60,0.8,0.225,0.225,0.52,0.708]

$ eng_chars = ["a","r","g","n","d","e"]
$ eng_chars_word = ""
$ eng_word = ""
$ eng_max_length = 6
$ eng_completed_list6 = []
$ eng_completed_list5 = []
$ eng_completed_list4 = []
$ eng_completed_list3 = []
$ eng_list6 = []
$ eng_list5 = []
$ eng_list4 = []
$ eng_list3 = []
$ eng_lists_used = [False,True,True,True]

$ eng_list6.append("danger")
$ eng_list6.append("gander")
$ eng_list6.append("grande")
$ eng_list6.append("ranged")
$ eng_list6.append("garden")
$ eng_total6 = len(eng_list6)

$ eng_list5.append("grand")
$ eng_list5.append("anger")
$ eng_list5.append("grade")
$ eng_list5.append("raged")
$ eng_list5.append("range")
$ eng_total5 = len(eng_list5)

$ eng_list4.append("aged")
$ eng_list4.append("dare")
$ eng_list4.append("darn")
$ eng_list4.append("dean")
$ eng_list4.append("dear")
$ eng_list4.append("drag")
$ eng_list4.append("dreg")
$ eng_list4.append("earn")
$ eng_list4.append("gear")
$ eng_list4.append("gnar")
$ eng_list4.append("gran")
$ eng_list4.append("nard")
$ eng_list4.append("near")
$ eng_list4.append("nerd")
$ eng_list4.append("rage")
$ eng_list4.append("rang")
$ eng_list4.append("read")
$ eng_list4.append("rend")
$ eng_list4.append("grad")
$ eng_total4 = len(eng_list4)
$ eng_shuffle_func()


$ wt_eng_class_help = "{color=#000000}4 letter:AGED,DARE,DARN,DEAN,DEAR,DRAG,DREG,EARN,GEAR,GNAR,GRAN,\nNARD,NEAR,NERD,RAGE,RANG,READ,REND,GRAD\n5 letter:GRAND,ANGER,GRADE,RAGED,RANGE \n6 letter:DANGER,GANDER,RANGED,GARDEN,GRANDE {/color}"
show screen english_screen
show screen word_cheat


pause
hide screen word_cheat
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

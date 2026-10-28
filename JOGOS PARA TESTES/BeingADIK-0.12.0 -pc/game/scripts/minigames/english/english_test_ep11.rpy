label init_eng_test_ep11_label:
$ renpy.block_rollback()
$ tmpMenu = quick_menu
$ quick_menu = 0
hide screen new_phone_screen
$ e_time = 200
$ timer_range = 200
$ eng_jump_label = "after_eng_test_ep11_label"
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
$ eng_yalign = [0.34,0.34,0.63,0.75,0.225,0.225,0.52,0.708]

$ eng_chars = ["a","e","e","l","p","s"]
$ eng_word = ""
$ eng_chars_word = ""
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

$ eng_list6.append("asleep")
$ eng_list6.append("elapse")
$ eng_list6.append("please")
$ eng_total6 = len(eng_list6)

$ eng_list5.append("easel")
$ eng_list5.append("lapse")
$ eng_list5.append("leaps")
$ eng_list5.append("lease")
$ eng_list5.append("pales")
$ eng_list5.append("peals")
$ eng_list5.append("peels")
$ eng_list5.append("pleas")
$ eng_list5.append("sleep")
$ eng_total5 = len(eng_list5)

$ eng_list4.append("ales")
$ eng_list4.append("alps")
$ eng_list4.append("apes")
$ eng_list4.append("ease")
$ eng_list4.append("eels")
$ eng_list4.append("else")
$ eng_list4.append("laps")
$ eng_list4.append("leap")
$ eng_list4.append("pale")
$ eng_list4.append("pals")
$ eng_list4.append("peal")
$ eng_list4.append("peas")
$ eng_list4.append("peel")
$ eng_list4.append("pees")
$ eng_list4.append("plea")
$ eng_list4.append("seal")
$ eng_list4.append("seep")
$ eng_list4.append("slap")
$ eng_list4.append("sale")
$ eng_total4 = len(eng_list4)
$ eng_shuffle_func()

$ wt_eng_class_help = "{color=#000000}4 letter:ALES,ALPS,APES,EASE,EELS,ELSE,LAPS,LEAP,PALE,PALS\nPEAL,PEAS,PEEL,PEES,PLEA,SEAL,SEEP,SLAP,SALE\n5 letter:EASEL,LAPSE,LEAPS,LEASE,PALES,PEALS,PEELS,PLEAS,SLEEP \n6 letter:ASLEEP,ELAPSE,PLEASE {/color}"
show screen english_screen
show screen word_cheat

pause
hide screen word_cheat
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

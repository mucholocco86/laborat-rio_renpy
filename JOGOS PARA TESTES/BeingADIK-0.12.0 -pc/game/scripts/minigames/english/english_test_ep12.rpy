label init_eng_test_ep12_label:
$ renpy.block_rollback()
$ tmpMenu = quick_menu
$ quick_menu = 0
hide screen new_phone_screen
$ e_time = 200
$ timer_range = 200
$ eng_jump_label = "after_eng_test_ep12_label"
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
$ eng_yalign = [0.34,0.34,0.63,0.8,0.225,0.225,0.52,0.708]

$ eng_chars = ["p","l","a","y","r","e"]
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

$ eng_list6.append("parley")
$ eng_list6.append("pearly")
$ eng_list6.append("player")
$ eng_list6.append("replay")
$ eng_total6 = len(eng_list6)

$ eng_list5.append("plyer")
$ eng_list5.append("reply")
$ eng_list5.append("apery")
$ eng_list5.append("payer")
$ eng_list5.append("repay")
$ eng_list5.append("paler")
$ eng_list5.append("pearl")
$ eng_list5.append("early")
$ eng_list5.append("layer")
$ eng_list5.append("relay")
$ eng_total5 = len(eng_list5)

$ eng_list4.append("play")
$ eng_list4.append("yelp")
$ eng_list4.append("pray")
$ eng_list4.append("prey")
$ eng_list4.append("pyre")
$ eng_list4.append("leap")
$ eng_list4.append("pale")
$ eng_list4.append("peal")
$ eng_list4.append("plea")
$ eng_list4.append("lyre")
$ eng_list4.append("pare")
$ eng_list4.append("pear")
$ eng_list4.append("rape")
$ eng_list4.append("reap")
$ eng_list4.append("rely")
$ eng_list4.append("year")
$ eng_list4.append("earl")
$ eng_list4.append("real")
$ eng_total4 = len(eng_list4)
$ eng_shuffle_func()

$ wt_eng_class_help = "{color=#000000}4 letter:EARL,LEAP,LYRE,PALE,PARE,PEAL,PEAR,PLAY,PLEA,PRAY,PREY,PYRE,RAPE,REAL,REAP,RELY,YEAR,YELP\n5 letter:APERY,EARLY,LAYER,PALER,PAYER,PEARL,PLYER,RELAY,REPAY,REPLY\n6 letter:PARLEY,PEARLY,PLAYER,REPLAY {/color}"
show screen english_screen
show screen word_cheat

pause
hide screen word_cheat
return

# Decompiled by unrpyc {v1.3.2}: https://github.com/CensoredUsername/unrpyc dev-branch



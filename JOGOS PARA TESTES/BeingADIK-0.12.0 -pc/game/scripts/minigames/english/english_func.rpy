init python:
    def eng_input_func(char):
        global eng_word
        global eng_max_length
        if len(eng_word) <  eng_max_length:
            eng_word += char
        return
    def eng_del_func():
        global eng_word
        if len(eng_word) > 0:
            eng_word = eng_word[:-1]
        return

    def eng_shuffle_func():
        global eng_chars_word
        global eng_chars
        global eng_list6
        global eng_list5
        global eng_list4
        global eng_list3
        
        renpy.random.shuffle(eng_list6)
        renpy.random.shuffle(eng_list5)
        renpy.random.shuffle(eng_list4)
        renpy.random.shuffle(eng_list3)
        renpy.random.shuffle(eng_chars)
        eng_chars_word = ""
        for char in eng_chars:
            eng_chars_word += char + " "
        
        return

    def eng_enter_word():
        global eng_word
        global eng_list6
        global eng_list5
        global eng_list4
        global eng_list3
        global eng_completed_list6
        global eng_completed_list5
        global eng_completed_list4
        global eng_completed_list3
        global eng_total6
        global eng_total5
        global eng_total4
        global eng_total3
        global eng_perc6
        global eng_perc5
        global eng_perc4
        global eng_perc3
        global eng_cheated
        global wt_eng_class_help
        
        if eng_word in eng_list6:
            eng_completed_list6.append(eng_word)
            eng_list6.remove(eng_word)
            eng_perc6 = (int) (100.0*len(eng_completed_list6)/eng_total6)
            
            eng_word=eng_word.upper()
            wt_eng_class_help = wt_eng_class_help.replace(eng_word, "",1)
            wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
            wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
            
        elif eng_word in eng_list5:
            eng_completed_list5.append(eng_word)
            eng_list5.remove(eng_word)
            eng_perc5 = (int) (100.0*len(eng_completed_list5)/eng_total5)
            
            eng_word=eng_word.upper()
            wt_eng_class_help = wt_eng_class_help.replace(eng_word, "",1)
            wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
            wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
        elif eng_word in eng_list4:
            eng_completed_list4.append(eng_word)
            eng_list4.remove(eng_word)
            eng_perc4 = (int) (100.0*len(eng_completed_list4)/eng_total4)
            
            eng_word=eng_word.upper()
            wt_eng_class_help = wt_eng_class_help.replace(eng_word, "",1)
            wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
            wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
        elif eng_word in eng_list3:
            eng_completed_list3.append(eng_word)
            eng_list3.remove(eng_word)
            eng_perc3 = (int) (100.0*len(eng_completed_list3)/eng_total3)
            
            eng_word=eng_word.upper()
            wt_eng_class_help = wt_eng_class_help.replace(eng_word, "",1)
            wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
            wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
        elif eng_word == "cheat" and not eng_cheated:
            eng_cheat()
        elif eng_word == "quit":
            eng_test_done()
        eng_word = ""
        if (len(eng_list3)+len(eng_list4)+len(eng_list5)+len(eng_list6)) == 0:
            eng_test_done()
        return

    def eng_cheat():
        global eng_cheated
        global eng_list6
        global eng_list5
        global eng_list4
        global eng_list3
        global eng_total6
        global eng_total5
        global eng_total4
        global eng_total3
        global englishCheatBoost
        global eng_completed_list6
        global eng_completed_list5
        global eng_completed_list4
        global eng_completed_list3
        global eng_perc6
        global eng_perc5
        global eng_perc4
        global eng_perc3
        global tmp_eng_class_word
        global wt_eng_class_help
        
        eng_cheated = True
        
        total = eng_total6+eng_total5+eng_total4+eng_total3
        times = 0
        if englishCheatBoost == 0:
            times = (int)(total*0.25)
        elif englishCheatBoost == 1:
            times = (int)(total*0.33)
        elif englishCheatBoost == 2:
            times = (int)(total*0.4)
        else:
            times = (int)(total*0.5)
        
        while times > 0 and (len(eng_list3)+len(eng_list4)+len(eng_list5)+len(eng_list6)) > 0:
            i = renpy.random.randint(0,3)
            if i == 0 and len(eng_list3) > 0:
                eng_completed_list3.append(eng_list3[0])
                
                tmp_eng_class_word=eng_list3[0].upper()
                wt_eng_class_help = wt_eng_class_help.replace(tmp_eng_class_word, "",1)
                wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
                wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
                
                eng_list3.pop(0)
                eng_perc3 = (int) (100.0*len(eng_completed_list3)/eng_total3)
                times = times - 1
            elif i == 1 and len(eng_list4) > 0:
                eng_completed_list4.append(eng_list4[0])
                
                tmp_eng_class_word=eng_list4[0].upper()
                wt_eng_class_help = wt_eng_class_help.replace(tmp_eng_class_word, "",1)
                wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
                wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
                
                eng_list4.pop(0)
                eng_perc4 = (int) (100.0*len(eng_completed_list4)/eng_total4)
                times = times - 1
            elif i == 2 and len(eng_list5) > 0:
                eng_completed_list5.append(eng_list5[0])
                
                tmp_eng_class_word=eng_list5[0].upper()
                wt_eng_class_help = wt_eng_class_help.replace(tmp_eng_class_word, "",1)
                wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
                wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
                
                eng_list5.pop(0)
                eng_perc5 = (int) (100.0*len(eng_completed_list5)/eng_total5)
                times = times - 1
            elif i == 3 and len(eng_list6) > 0:
                eng_completed_list6.append(eng_list6[0])
                
                tmp_eng_class_word=eng_list6[0].upper()
                wt_eng_class_help = wt_eng_class_help.replace(tmp_eng_class_word, "",1)
                wt_eng_class_help = wt_eng_class_help.replace(",,", ",")
                wt_eng_class_help = wt_eng_class_help.replace(":,", ":")
                
                eng_list6.pop(0)
                eng_perc6 = (int) (100.0*len(eng_completed_list6)/eng_total6)
                times = times - 1
        
        if (len(eng_list3)+len(eng_list4)+len(eng_list5)+len(eng_list6)) == 0:
            eng_test_done()
        return

    def eng_test_done():
        global englishResult
        global eng_completed_list6
        global eng_completed_list5
        global eng_completed_list4
        global eng_completed_list3
        global eng_total6
        global eng_total5
        global eng_total4
        global eng_total3
        global maxedEnglishS3
        global bonusPercentageEnglish
        global englishBoost
        global failedEnglishS3
        global passedEnglishS3
        global currentEpisode
        global eng_rew
        global eng_word
        
        englishResult = int(100 * (len(eng_completed_list6)+len(eng_completed_list5)+len(eng_completed_list4)+len(eng_completed_list3)) / (eng_total6+eng_total5+eng_total4+eng_total3))
        eng_word = ""
        if englishResult == 100:
            maxedEnglishS3 += 1
        
        if englishResult + bonusPercentageEnglish >= 70 - (englishBoost*5):
            passedEnglishS3 += 1
            if englishResult + bonusPercentageEnglish >= 90- (englishBoost*5):
                if currentEpisode == 10 and not persistent.ep10_cardsa17:
                    persistent.ep10_cardsa17 = True
                    persistent.rew_sage_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                    eng_rew = True
                elif currentEpisode == 11 and not persistent.ep11_cardmy10:
                    persistent.ep11_cardmy10 = True
                    persistent.rew_maya_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                    eng_rew = True
                elif currentEpisode == 12 and not persistent.ep12_cardisa11:
                    persistent.ep12_cardisa11 = True
                    persistent.rew_isa_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                    eng_rew = True
            if eng_cheated:
                dk(1)
            else:
                dk(-1)
        else:
            failedEnglishS3 += 1
        
        renpy.jump("eng_results_label")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

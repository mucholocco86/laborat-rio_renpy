init python:
    def math_play_failed_click():
        renpy.play("sound_effects/failed_click.mp3","sfx1")
    def math_play_beep():
        renpy.play("sound_effects/interlude/paint_bling.mp3","sfx1")
    def math_play_bomb():
        renpy.play("sound_effects/season3/bomb.mp3","sfx1")
    def math_play_query_correct():
        renpy.play("sound_effects/win.mp3","sfx1")
    def math_play_query_incorrect():
        renpy.play("sound_effects/fail.mp3","sfx1")

init python:

    def math_quit_func():
        global currentEpisode
        global math_task
        
        if math_task > 0:
            math_task_correct_answers.append(False)
        math_task += 1
        if currentEpisode == 10:
            if math_task <= 5:
                math_task1_ep10(math_task)
                math_quit_func()
            else:
                math_calc_result()
        elif currentEpisode == 11:
            if math_task <= 5:
                math_task1_ep11(math_task)
                math_quit_func()
            else:
                math_calc_result()
        elif currentEpisode == 12:
            if math_task <= 5:
                math_task1_ep12(math_task)
                math_quit_func()
            else:
                math_calc_result()
        return

    def math_buy_tool_func(tool,price):
        global math_buy_tool
        global money
        global math_own_b
        global math_own_q
        global math_own_query
        
        mny(-price)
        if math_buy_tool == 2:
            math_own_q = True
        elif math_buy_tool == 3:
            math_own_b = True
        elif math_buy_tool == 5:
            math_own_query = True
        
        math_buy_tool = 0
        ft_play_coin()
        
        return

    def math_tool_selected(tool):
        global math_buy_tool
        math_buy_tool = tool
        return

    def math_use_query():
        global math_query_count
        math_query_count = math_query_count - 1
        math_check_answer()
        return

    def math_use_bomb():
        global math_bomb_used
        global math_bomb_grid
        global math_grid
        global math_b_count
        global math_d_count
        
        math_b_count = math_b_count - 1
        
        math_bomb_used = True
        
        for x in math_bomb_grid:
            if math_grid[x][2] == "d":
                math_d_count -= 1
            math_grid[x][2] = "crack"
        math_play_bomb()
        return

    def math_next_task():
        global currentEpisode
        global math_task
        
        if math_task > 0:
            math_check_answers()
        math_task += 1
        if currentEpisode == 10:
            math_task1_ep10(math_task)
        elif currentEpisode == 11:
            math_task1_ep11(math_task)
        elif currentEpisode == 12:
            math_task1_ep12(math_task)
        return

    def math_check_answer():
        global math_diamond_position
        global math_grid
        global math_query_info
        
        tmpList = []
        math_query_info = []
        if len(math_diamond_position) == 0:
            return
        
        for x in range(0,len(math_grid)):
            if math_grid[x][2] == "d":
                tmpList.append(x)
        
        emitWrongSound = False
        for x in tmpList:
            if x in math_diamond_position:
                math_query_info.append([x,True])
            else:
                emitWrongSound = True
                math_query_info.append([x,False])
        
        if emitWrongSound:
            math_play_query_incorrect()
        else:
            math_play_query_correct()
        return

    def math_check_answers():
        global math_diamond_position
        global math_task_correct_answers
        global math_grid
        
        if len(math_diamond_position) == 0:
            return
        
        tmpList = []
        for x in range(0,len(math_grid)):
            if math_grid[x][2] == "d":
                tmpList.append(x)
        
        for x in tmpList:
            if x not in math_diamond_position:
                math_task_correct_answers.append(False)
                return
        math_task_correct_answers.append(True)
        return

    def math_calc_result():
        global mathResult
        global passedMathS3
        global maxedMathS3
        global failedMathS3
        global math_task_correct_answers
        global math_task_total
        global math_jump_label
        global math_rew
        
        mathResult = int(100 * math_task_correct_answers.count(True) / math_task_total)
        if mathResult == 100:
            maxedMathS3 += 1
        
        if mathResult + bonusPercentageMath >= 80 - (mathBoost*10):
            passedMathS3 += 1
            if mathResult + bonusPercentageMath >= 90- (mathBoost*10):
                if currentEpisode == 10 and not persistent.ep10_cardsa18:
                    persistent.ep10_cardsa18 = True
                    persistent.rew_sage_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                    math_rew = True
                elif currentEpisode == 11 and not persistent.ep11_cardmy11:
                    persistent.ep11_cardmy11 = True
                    persistent.rew_maya_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                    math_rew = True
                elif currentEpisode == 12 and not persistent.ep12_cardisa10:
                    persistent.ep12_cardisa10 = True
                    persistent.rew_isa_unlocked += 1
                    persistent.chat_new_rewards = True
                    calcRenders()
                    math_rew = True
        else:
            failedMathS3 += 1
        
        renpy.jump(math_jump_label)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

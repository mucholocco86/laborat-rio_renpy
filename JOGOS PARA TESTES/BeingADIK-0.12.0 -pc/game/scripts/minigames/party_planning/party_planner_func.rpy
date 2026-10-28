init python:
    def play_pp_need_met_sound():
        renpy.play("sound_effects/season2/beep.mp3", "sfx1")

    def party_planner_get_rank(score, activities):
        global pp_party_rank
        global currentEpisode
        
        pp_tmp_rank = 0
        pp_given_rank = ["F","E","D","C","B","A","S"]
        
        if currentEpisode == 9:
            if score > 90000:
                pp_tmp_rank = 6
            elif score > 80000:
                pp_tmp_rank = 5
            elif score > 70000:
                pp_tmp_rank = 4
            elif score > 65000:
                pp_tmp_rank = 3
            elif score > 50000:
                pp_tmp_rank = 2
            elif score > 40000:
                pp_tmp_rank = 1
        elif currentEpisode == 10:
            if score > 90000:
                pp_tmp_rank = 6
            elif score > 80000:
                pp_tmp_rank = 5
            elif score > 70000:
                pp_tmp_rank = 4
            elif score > 65000:
                pp_tmp_rank = 3
            elif score > 50000:
                pp_tmp_rank = 2
            elif score > 40000:
                pp_tmp_rank = 1
        elif currentEpisode == 11:
            if score > 100000:
                pp_tmp_rank = 6
            elif score > 90000:
                pp_tmp_rank = 5
            elif score > 80000:
                pp_tmp_rank = 4
            elif score > 70000:
                pp_tmp_rank = 3
            elif score > 60000:
                pp_tmp_rank = 2
            elif score > 50000:
                pp_tmp_rank = 1
        elif currentEpisode == 12:
            if score > 110000:
                pp_tmp_rank = 6
            elif score > 100000:
                pp_tmp_rank = 5
            elif score > 90000:
                pp_tmp_rank = 4
            elif score > 80000:
                pp_tmp_rank = 3
            elif score > 70000:
                pp_tmp_rank = 2
            elif score > 60000:
                pp_tmp_rank = 1
        
        pp_party_rank.append([currentEpisode,pp_given_rank[min(pp_tmp_rank+max(0,activities-2),6)]])
        return

    def party_planner_get_nm_score(happiness):
        global pp_score_nm
        
        for i in happiness:
            pp_score_nm += i
        return


    def party_planner_get_nm_rank(happiness):
        global pp_party_rank
        global currentEpisode
        
        pp_tmp_rank = 0
        pp_given_rank = ["F","E","D","C","B","A","S"]
        
        score = 0
        for i in happiness:
            score += i
        
        if currentEpisode == 9:
            if score > 5:
                pp_tmp_rank = 6
            elif score > 4:
                pp_tmp_rank = 5
            elif score > 3:
                pp_tmp_rank = 4
            elif score > 2:
                pp_tmp_rank = 3
            elif score > 1:
                pp_tmp_rank = 2
            else:
                pp_tmp_rank = 1
        elif currentEpisode == 10:
            if score > 5:
                pp_tmp_rank = 6
            elif score > 4:
                pp_tmp_rank = 5
            elif score > 3:
                pp_tmp_rank = 4
            elif score > 2:
                pp_tmp_rank = 3
            elif score > 1:
                pp_tmp_rank = 2
            else:
                pp_tmp_rank = 1
        elif currentEpisode == 11:
            if score > 5:
                pp_tmp_rank = 6
            elif score > 4:
                pp_tmp_rank = 5
            elif score > 3:
                pp_tmp_rank = 4
            elif score > 2:
                pp_tmp_rank = 3
            elif score > 1:
                pp_tmp_rank = 2
            else:
                pp_tmp_rank = 1
        elif currentEpisode == 12:
            if score > 5:
                pp_tmp_rank = 6
            elif score > 4:
                pp_tmp_rank = 5
            elif score > 3:
                pp_tmp_rank = 4
            elif score > 2:
                pp_tmp_rank = 3
            elif score > 1:
                pp_tmp_rank = 2
            else:
                pp_tmp_rank = 1
        
        pp_party_rank.append([currentEpisode,pp_given_rank[pp_tmp_rank]])
        return

    def pp_check_criteria_met(firstTime):
        global pp_grid
        global pp_needs_met
        global pp_needs
        global pp_active_grid
        global pp_special_needs
        global pp_connector_grid_active
        global pp_connector_grid_inactive
        global pp_multiplier
        
        pp_needs_met_tmp = [[False, False, False, False],[False, False, False, False],[False, False, False, False],[False, False, False, False],[False, False, False, False],[False, False, False, False],[False, False, False, False],[False, False, False, False]]
        tmp_pp_multiplier = pp_multiplier
        pp_multiplier = 1.00
        for i in range(0,8):
            for x in range(0,6):
                for y in range(0,6):
                    if pp_grid[x][y] == 100+i:
                        for need in range(0,3):
                            
                            
                            if pp_needs[i][need][0] in pp_icons_limited_list:
                                pp_icons_limited_list.index(pp_needs[i][need][0])
                                tmpInt = 0
                                if y != 0 and pp_grid[x][y-1]<100 and pp_grid[x][y-1]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x][y-1] and pp_active_grid[x][y-1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x][y-1].append("mr")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x][y-1]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x][y-1].append("mr")
                                if y != 5 and pp_grid[x][y+1]<100 and pp_grid[x][y+1]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x][y+1] and pp_active_grid[x][y+1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x][y+1].append("ml")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x][y+1]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x][y+1].append("ml")
                                if x != 0 and pp_grid[x-1][y]<100 and pp_grid[x-1][y]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x-1][y] and pp_active_grid[x-1][y]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x-1][y].append("lc")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x-1][y]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x-1][y].append("lc")
                                if x != 5 and pp_grid[x+1][y]<100 and pp_grid[x+1][y]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x+1][y] and pp_active_grid[x+1][y]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x+1][y].append("uc")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x+1][y]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x+1][y].append("uc")
                                
                                if y != 0 and x != 0 and pp_grid[x-1][y-1]<100 and pp_grid[x-1][y-1]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x-1][y-1] and pp_active_grid[x-1][y-1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x-1][y-1].append("lr")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x-1][y-1]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x-1][y-1].append("lr")
                                if y != 5 and x != 5 and pp_grid[x+1][y+1]<100 and pp_grid[x+1][y+1]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x+1][y+1] and pp_active_grid[x+1][y+1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x+1][y+1].append("ul")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x+1][y+1]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x+1][y+1].append("ul")
                                if y != 5 and x != 0 and pp_grid[x-1][y+1]<100 and pp_grid[x-1][y+1]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x-1][y+1] and pp_active_grid[x-1][y+1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x-1][y+1].append("ll")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x-1][y+1]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x-1][y+1].append("ll")
                                if y != 0 and x != 5 and pp_grid[x+1][y-1]<100 and pp_grid[x+1][y-1]<len(pp_icons_limited_list)+1:
                                    if pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x+1][y-1] and pp_active_grid[x+1][y-1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x+1][y-1].append("ur")
                                    elif pp_icons_limited_list.index(pp_needs[i][need][0]) + 1 == pp_grid[x+1][y-1]:
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_inactive[x+1][y-1].append("ur")
                                
                                if tmpInt >= pp_needs[i][need][1]:
                                    pp_needs_met_tmp[i][need] = True
                            elif pp_needs[i][need][0] in pp_icons_unlimited_list:
                                pp_icons_unlimited_list.index(pp_needs[i][need][0])
                                tmpInt = 0
                                if y != 0 and pp_grid[x][y-1]<100 and pp_grid[x][y-1]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x][y-1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x][y-1].append("mr")
                                if y != 5 and pp_grid[x][y+1]<100 and pp_grid[x][y+1]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x][y+1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x][y+1].append("ml")
                                if x != 0 and pp_grid[x-1][y]<100 and pp_grid[x-1][y]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x-1][y]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x-1][y].append("lc")
                                if x != 5 and pp_grid[x+1][y]<100 and pp_grid[x+1][y]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x+1][y]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x+1][y].append("uc")
                                
                                if y != 0 and x != 0 and pp_grid[x-1][y-1]<100 and pp_grid[x-1][y-1]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x-1][y-1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x-1][y-1].append("lr")
                                if y != 5 and x != 5 and pp_grid[x+1][y+1]<100 and pp_grid[x+1][y+1]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x+1][y+1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x+1][y+1].append("ul")
                                if y != 5 and x != 0 and pp_grid[x-1][y+1]<100 and pp_grid[x-1][y+1]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x-1][y+1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x-1][y+1].append("ll")
                                if y != 0 and x != 5 and pp_grid[x+1][y-1]<100 and pp_grid[x+1][y-1]>len(pp_icons_limited_list):
                                    if pp_icons_unlimited_list.index(pp_needs[i][need][0]) + 1 + len(pp_icons_limited_list) == pp_grid[x+1][y-1]:
                                        tmpInt += 1
                                        if tmpInt <= pp_needs[i][need][1]:
                                            pp_connector_grid_active[x+1][y-1].append("ur")
                                
                                if tmpInt >= pp_needs[i][need][1]:
                                    pp_needs_met_tmp[i][need] = True
                    
                    tmpInt = 0
                    for k in range(0,6):
                        for l in range(0,6):
                            if pp_special_needs[pp_needs[i][3][1]][0] in pp_icons_limited_list:
                                if pp_icons_limited_list.index(pp_special_needs[pp_needs[i][3][1]][0]) + 1 == pp_grid[k][l] and pp_active_grid[k][l]:
                                    tmpInt += 1
                            elif pp_special_needs[pp_needs[i][3][1]][0] in pp_icons_unlimited_list:
                                if pp_icons_unlimited_list.index(pp_special_needs[pp_needs[i][3][1]][0]) + 1 + len(pp_icons_limited_list) == pp_grid[k][l]:
                                    tmpInt += 1
                    if pp_special_needs[pp_needs[i][3][1]][1] == 0 and tmpInt == 0:
                        pp_needs_met_tmp[i][3] = True
                    elif tmpInt >= pp_special_needs[pp_needs[i][3][1]][1] and pp_special_needs[pp_needs[i][3][1]][1] > 0:
                        pp_needs_met_tmp[i][3] = True
        
        pp_needs_met = pp_needs_met_tmp
        for i in pp_needs_met:
            for j in i:
                if j:
                    pp_multiplier += 0.25
        if pp_multiplier > tmp_pp_multiplier and not firstTime:
            play_pp_need_met_sound()
        return

    def pp_handle_active_cells():
        global pp_grid
        global pp_active_grid
        global pp_connector_grid_active
        global pp_connector_grid_inactive
        
        pp_tmp_active_grid = [[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False]]
        pp_connector_grid_active = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
        pp_connector_grid_inactive = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
        
        for x in range(0,6):
            for y in range(0,6):
                if pp_grid[x][y]>0 and pp_grid[x][y]<len(pp_icons_limited_list)+1 and pp_icons_limited_dependency_list[pp_grid[x][y]-1] != "":
                    if y != 0 and pp_grid[x][y-1]<100 and pp_grid[x][y-1]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x][y-1]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x][y-1].append("mr")
                                pp_connector_grid_active[x][y].append("ml")
                    if y != 5 and pp_grid[x][y+1]<100 and pp_grid[x][y+1]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x][y+1]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x][y+1].append("ml")
                                pp_connector_grid_active[x][y].append("mr")
                    if x != 0 and pp_grid[x-1][y]<100 and pp_grid[x-1][y]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x-1][y]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x-1][y].append("lc")
                                pp_connector_grid_active[x][y].append("uc")
                    if x != 5 and pp_grid[x+1][y]<100 and pp_grid[x+1][y]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x+1][y]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x+1][y].append("uc")
                                pp_connector_grid_active[x][y].append("lc")
                    
                    if y != 0 and x != 0 and pp_grid[x-1][y-1]<100 and pp_grid[x-1][y-1]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x-1][y-1]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x-1][y-1].append("lr")
                                pp_connector_grid_active[x][y].append("ul")
                    if y != 5 and x != 5 and pp_grid[x+1][y+1]<100 and pp_grid[x+1][y+1]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x+1][y+1]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x+1][y+1].append("ul")
                                pp_connector_grid_active[x][y].append("lr")
                    if y != 5 and x != 0 and pp_grid[x-1][y+1]<100 and pp_grid[x-1][y+1]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x-1][y+1]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x-1][y+1].append("ll")
                                pp_connector_grid_active[x][y].append("ur")
                    if y != 0 and x != 5 and pp_grid[x+1][y-1]<100 and pp_grid[x+1][y-1]>len(pp_icons_limited_list):
                        if pp_icons_limited_dependency_list[pp_grid[x][y]-1] == pp_icons_unlimited_list[pp_grid[x+1][y-1]-len(pp_icons_limited_list)-1]:
                            pp_tmp_active_grid[x][y] = True
                            if len(pp_connector_grid_active[x][y]) == 0:
                                pp_connector_grid_active[x+1][y-1].append("ur")
                                pp_connector_grid_active[x][y].append("ll")
                elif pp_grid[x][y]>0 and pp_grid[x][y]<len(pp_icons_limited_list)+1 and pp_icons_limited_dependency_list[pp_grid[x][y]-1] == "":
                    pp_tmp_active_grid[x][y] = True
        
        pp_active_grid = pp_tmp_active_grid
        
        pp_check_criteria_met(False)
        return

    def pp_update_happiness_icons():
        global pp_happiness_level
        for x in range(0,len(pp_happiness_level)):
            if pp_happiness_level[x] < 25.0:
                pp_happiness_icon[x] = 0
            elif pp_happiness_level[x] < 50.0:
                pp_happiness_icon[x] = 1
            elif pp_happiness_level[x] < 75.0:
                pp_happiness_icon[x] = 2
            else:
                pp_happiness_icon[x] = 3
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

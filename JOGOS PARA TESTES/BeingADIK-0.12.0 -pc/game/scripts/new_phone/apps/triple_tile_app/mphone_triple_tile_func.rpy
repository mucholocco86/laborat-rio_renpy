init python:
    def mphone_triple_tile_new_game_func():
        global mphone_triple_tile_is_playing
        global triple_tile_new_highscore
        global triple_tile_turn
        global triple_tile_score
        global triple_tile_sets
        global triple_tile_chosen_tile
        global triple_tile_grid
        global triple_tile_game_over
        global triple_tile_new_high_score
        global triple_tile_spr
        global triple_tile_hovered_tile
        global triple_tile_grid_spr
        global triple_tile_hs_checked
        
        triple_tile_hs_checked = False
        triple_tile_hovered_tile = [-1,-1]
        triple_tile_new_high_score = 0
        triple_tile_game_over = False
        triple_tile_chosen_tile = -1
        triple_tile_turn = 0
        triple_tile_score = 0
        triple_tile_new_highscore = 0
        mphone_triple_tile_is_playing = True
        triple_tile_sets = [[0,0,0],[0,0,0],[0,0,0]]
        triple_tile_grid = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
        triple_tile_grid_spr = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
        triple_tile_spr = [[False,False,False],[False,False,False],[False,False,False]]
        triple_tile_get_tile_set()
        return

    def triple_tile_get_tile_set():
        global triple_tile_sets
        global triple_card_number_of_cards
        global triple_tile_chosen_tile
        global triple_tile_turn
        global triple_tile_easy_mode
        
        triple_tile_turn += 1
        if not triple_tile_easy_mode and steamAchievements and not config.console and not config.developer:
            if triple_tile_turn == 15:
                achievement.grant("ID_16")
                achievement.Sync()
            if triple_tile_turn == 100:
                achievement.grant("ID_17")
                achievement.Sync()
        triple_tile_chosen_tile = -1
        for i in range(0,3):
            if triple_tile_easy_mode:
                x = 1
            else:
                x = renpy.random.randint(0,10)
                if x < 8:
                    x = 1
                else:
                    x = 2
            for j in range(0,x):
                y = -1
                while y == -1:
                    y = renpy.random.randint(0,2)
                    if triple_tile_sets[i][y] != 0:
                        y = -1
                triple_tile_sets[i][y] = renpy.random.randint(1,triple_card_number_of_cards)
        triple_tile_check_game_over()
        return

    def triple_tile_add_is_possible(i,j,a):
        global triple_tile_grid
        global triple_tile_sets
        
        for k in range(0,3):
            if triple_tile_grid[i][j][k] != 0 and triple_tile_sets[a][k] != 0:
                return False
        return True

    def triple_tile_add_tile(i,j):
        global triple_tile_grid
        global triple_tile_sets
        global triple_tile_chosen_tile
        global triple_tile_hovered_tile
        
        triple_tile_hovered_tile = [-1,-1]
        if triple_tile_add_is_possible(i,j,triple_tile_chosen_tile):
            for k in range(0,3):
                if triple_tile_sets[triple_tile_chosen_tile][k] != 0:
                    triple_tile_grid[i][j][k] = triple_tile_sets[triple_tile_chosen_tile][k]
            
            triple_tile_sets[triple_tile_chosen_tile] = [0,0,0]
            triple_tile_chosen_tile = -1
        
        triple_tile_check_score(i,j)
        return

    def triple_tile_check_score(j,k):
        global triple_tile_grid
        global triple_tile_score
        global triple_tile_spr
        global triple_tile_grid_spr
        
        triple_tile_spr = [[False,False,False],[False,False,False],[False,False,False]]
        triple_tile_grid_spr = [[[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]], [[0,0,0],[0,0,0],[0,0,0]]]
        triple_tile_cell_to_delete = [-1,-1]
        if triple_tile_grid[j][k][0] == triple_tile_grid[j][k][1] == triple_tile_grid[j][k][2]:
            triple_tile_cell_to_delete = [j,k]
        triple_tile_tmp_score = 0
        for x in triple_tile_grid[j][k]:
            triple_tile_row_to_delete = -1
            triple_tile_col_to_delete = -1
            triple_tile_dia_to_delete = -1
            if x > 0:
                if j == 0:
                    if k == 0:
                        if x in triple_tile_grid[j][1] and x in triple_tile_grid[j][2]:
                            triple_tile_row_to_delete = 0
                        if x in triple_tile_grid[1][k] and x in triple_tile_grid[2][k]:
                            triple_tile_col_to_delete = 0
                        if x in triple_tile_grid[1][1] and x in triple_tile_grid[2][2]:
                            triple_tile_dia_to_delete = 0
                    elif k == 1:
                        if x in triple_tile_grid[j][0] and x in triple_tile_grid[j][2]:
                            triple_tile_row_to_delete = 0
                        if x in triple_tile_grid[1][k] and x in triple_tile_grid[2][k]:
                            triple_tile_col_to_delete = 1
                    elif k == 2:
                        if x in triple_tile_grid[j][1] and x in triple_tile_grid[j][0]:
                            triple_tile_row_to_delete = 0
                        if x in triple_tile_grid[1][k] and x in triple_tile_grid[2][k]:
                            triple_tile_col_to_delete = 2
                        if x in triple_tile_grid[1][1] and x in triple_tile_grid[2][0]:
                            triple_tile_dia_to_delete = 1
                elif j == 1:
                    if k == 0:
                        if x in triple_tile_grid[j][1] and x in triple_tile_grid[j][2]:
                            triple_tile_row_to_delete = 1
                        if x in triple_tile_grid[0][k] and x in triple_tile_grid[2][k]:
                            triple_tile_col_to_delete = 0
                    elif k == 1:
                        if x in triple_tile_grid[j][0] and x in triple_tile_grid[j][2]:
                            triple_tile_row_to_delete = 1
                        if x in triple_tile_grid[0][k] and x in triple_tile_grid[2][k]:
                            triple_tile_col_to_delete = 1
                        if x in triple_tile_grid[0][0] and x in triple_tile_grid[2][2]:
                            triple_tile_dia_to_delete = 0
                        if x in triple_tile_grid[0][2] and x in triple_tile_grid[2][0]:
                            if triple_tile_dia_to_delete == 0:
                                triple_tile_dia_to_delete = 2
                            else:
                                triple_tile_dia_to_delete = 1
                    elif k == 2:
                        if x in triple_tile_grid[j][1] and x in triple_tile_grid[j][0]:
                            triple_tile_row_to_delete = 1
                        if x in triple_tile_grid[0][k] and x in triple_tile_grid[2][k]:
                            triple_tile_col_to_delete = 2
                elif j == 2:
                    if k == 0:
                        if x in triple_tile_grid[j][1] and x in triple_tile_grid[j][2]:
                            triple_tile_row_to_delete = 2
                        if x in triple_tile_grid[1][k] and x in triple_tile_grid[0][k]:
                            triple_tile_col_to_delete = 0
                        if x in triple_tile_grid[1][1] and x in triple_tile_grid[0][2]:
                            triple_tile_dia_to_delete = 1
                    elif k == 1:
                        if x in triple_tile_grid[j][0] and x in triple_tile_grid[j][2]:
                            triple_tile_row_to_delete = 2
                        if x in triple_tile_grid[1][k] and x in triple_tile_grid[0][k]:
                            triple_tile_col_to_delete = 1
                    elif k == 2:
                        if x in triple_tile_grid[j][1] and x in triple_tile_grid[j][0]:
                            triple_tile_row_to_delete = 2
                        if x in triple_tile_grid[1][k] and x in triple_tile_grid[0][k]:
                            triple_tile_col_to_delete = 2
                        if x in triple_tile_grid[1][1] and x in triple_tile_grid[0][0]:
                            triple_tile_dia_to_delete = 0
                
                if triple_tile_cell_to_delete != [-1,-1]:
                    for a in range(0,3):
                        triple_tile_grid_spr[triple_tile_cell_to_delete[0]][triple_tile_cell_to_delete[1]][a] = triple_tile_grid[triple_tile_cell_to_delete[0]][triple_tile_cell_to_delete[1]][a]
                        triple_tile_grid[triple_tile_cell_to_delete[0]][triple_tile_cell_to_delete[1]][a] = 0
                        triple_tile_tmp_score += 1
                        triple_tile_spr[triple_tile_cell_to_delete[0]][triple_tile_cell_to_delete[1]] = True
                if triple_tile_row_to_delete != -1:
                    for a in range(0,3):
                        for b in range(0,3):
                            if triple_tile_grid[triple_tile_row_to_delete][a][b] == x:
                                triple_tile_grid_spr[triple_tile_row_to_delete][a][b] = triple_tile_grid[triple_tile_row_to_delete][a][b]
                                triple_tile_grid[triple_tile_row_to_delete][a][b] = 0
                                triple_tile_tmp_score += 1
                                triple_tile_spr[triple_tile_row_to_delete][a] = True
                if triple_tile_col_to_delete != -1:
                    for a in range(0,3):
                        for b in range(0,3):
                            if triple_tile_grid[a][triple_tile_col_to_delete][b] == x:
                                triple_tile_grid_spr[a][triple_tile_col_to_delete][b] = triple_tile_grid[a][triple_tile_col_to_delete][b]
                                triple_tile_grid[a][triple_tile_col_to_delete][b] = 0
                                triple_tile_tmp_score += 1
                                triple_tile_spr[a][triple_tile_col_to_delete] = True
                if triple_tile_dia_to_delete != -1:
                    if triple_tile_dia_to_delete == 0 or triple_tile_dia_to_delete == 2:
                        for a in range(0,3):
                            for b in range(0,3):
                                if triple_tile_grid[a][a][b] == x:
                                    triple_tile_grid_spr[a][a][b] = triple_tile_grid[a][a][b]
                                    triple_tile_grid[a][a][b] = 0
                                    triple_tile_tmp_score += 1
                                    triple_tile_spr[a][a] = True
                    if triple_tile_dia_to_delete == 1 or triple_tile_dia_to_delete == 2:
                        for a in range(0,3):
                            for b in range(0,3):
                                if triple_tile_grid[a][2-a][b] == x:
                                    triple_tile_grid_spr[a][2-a][b] = triple_tile_grid[a][2-a][b]
                                    triple_tile_grid[a][2-a][b] = 0
                                    triple_tile_tmp_score += 1
                                    triple_tile_spr[a][2-a] = True
        if triple_tile_tmp_score > 0:
            triple_tile_score += (triple_tile_tmp_score * 100 + (triple_tile_tmp_score - 1) * 100)
            if triple_tile_sets == [[0,0,0],[0,0,0],[0,0,0]]:
                triple_tile_get_tile_set()
            renpy.show_screen("triple_tile_spr_screen")
            return
        if triple_tile_sets == [[0,0,0],[0,0,0],[0,0,0]]:
            triple_tile_get_tile_set()
            triple_tile_check_game_over()
        else:
            triple_tile_check_game_over()
        return

    def triple_tile_check_game_over():
        global triple_tile_game_over
        global triple_tile_hovered_tile
        
        for a in range(0,3):
            if triple_tile_sets[a] != [0,0,0]:
                for i in range(0,3):
                    for j in range(0,3):
                        if triple_tile_add_is_possible(i,j,a):
                            return
        renpy.show_screen("triple_tile_game_over_screen")
        return

    def triple_tile_force_game_over():
        global triple_tile_game_over
        global triple_tile_hovered_tile
        
        triple_tile_game_over = True
        triple_tile_hovered_tile = [-1,-1]
        renpy.hide_screen("triple_tile_spr_screen")
        triple_tile_check_high_score()
        return

    def triple_tile_check_high_score():
        global triple_tile_new_high_score
        global triple_tile_easy_mode
        global triple_tile_money_available
        global triple_tile_turn
        global triple_turn_to_beat
        global triple_tile_score
        global triple_tile_hs_checked
        
        if triple_tile_hs_checked:
            return
        triple_tile_hs_checked = True
        
        if triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
            mny(1)
        if triple_tile_easy_mode:
            for i in range(0,len(persistent.triple_tile_highscores_easy)):
                if triple_tile_score > persistent.triple_tile_highscores_easy[i][0] or (triple_tile_score == persistent.triple_tile_highscores_easy[i][0] and triple_tile_turn > persistent.triple_tile_highscores_easy[i][1]):
                    if i == 0:
                        persistent.triple_tile_highscores_easy[i+2] = persistent.triple_tile_highscores_easy[i+1]
                    if i < 2:
                        persistent.triple_tile_highscores_easy[i+1] = persistent.triple_tile_highscores_easy[i]
                    persistent.triple_tile_highscores_easy[i] = [triple_tile_score,triple_tile_turn]
                    triple_tile_new_high_score = i+1
                    return
        else:
            for i in range(0,len(persistent.triple_tile_highscores)):
                if triple_tile_score > persistent.triple_tile_highscores[i][0] or (triple_tile_score == persistent.triple_tile_highscores[i][0] and triple_tile_turn > persistent.triple_tile_highscores[i][1]):
                    if i == 0:
                        persistent.triple_tile_highscores[i+2] = persistent.triple_tile_highscores[i+1]
                    if i < 2:
                        persistent.triple_tile_highscores[i+1] = persistent.triple_tile_highscores[i]
                    persistent.triple_tile_highscores[i] = [triple_tile_score,triple_tile_turn]
                    triple_tile_new_high_score = i+1
                    return
        triple_tile_new_high_score = 0
        return


    def triple_tile_add_is_possible(i,j,a):
        global triple_tile_grid
        global triple_tile_sets
        
        for k in range(0,3):
            if triple_tile_grid[i][j][k] != 0 and triple_tile_sets[a][k] != 0:
                return False
        return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

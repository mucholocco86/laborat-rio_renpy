init python:

    def mphone_shuffle_solvable():
        global eco_shf
        eco_shf = [0,1,2,3,4,5,6,7,8]
        renpy.random.shuffle(eco_shf)
        inversions = 0
        i = 0
        j = 0
        while i < 8:
            j = i + 1
            while j < 9:
                if eco_shf[j] > eco_shf[i] and eco_shf[j] != 8 and eco_shf[i] != 8:
                    inversions += 1
                j += 1
            i += 1
        
        if inversions%2 != 0:
            mphone_shuffle_solvable()
        return

    def mphone_shuffle_new_game():
        global game_brick_set
        global eco_bricks
        global eco_moveable
        global eco_wrongs
        global e_time
        global timer_range
        global eco_current_hole
        
        e_time = 50
        timer_range = 50
        eco_current_hole = 0
        
        mphone_shuffle_solvable()
        game_brick_set = renpy.random.randint(0, 9)
        eco_bricks = []
        for x in range(0,8):
            eco_bricks.append("shuffle_brick_%i_tile%i" % (game_brick_set,x))
        eco_bricks.append("[persistent.img_dir]/new_phone/apps/shuffle_app/tiles/shuffle_brick_empty.png")
        eco_moveable = [False, False, False, False, False, False, False, False, False]
        
        return

    def mphone_shuffle_update_board():
        global eco_wrongs
        global eco_shf
        global eco_moveable
        global eco_current_hole
        
        
        count = 0
        tmp_wrongs = 0
        for x in range(0,8):
            if x != eco_shf[x]:
                tmp_wrongs += 1
        eco_wrongs = tmp_wrongs
        
        if eco_shf[0] == 8:
            eco_moveable = [False, True, False, True, False, False, False, False, False]
            eco_current_hole = 0
        elif eco_shf[1] == 8:
            eco_moveable = [True, False, True, False, True, False, False, False, False]
            eco_current_hole = 1
        elif eco_shf[2] == 8:
            eco_moveable = [False, True, False, False, False, True, False, False, False]
            eco_current_hole = 2
        elif eco_shf[3] == 8:
            eco_moveable = [True, False, False, False, True, False, True, False, False]
            eco_current_hole = 3
        elif eco_shf[4] == 8:
            eco_moveable = [False, True, False, True, False, True, False, True, False]
            eco_current_hole = 4
        elif eco_shf[5] == 8:
            eco_moveable = [False, False, True, False, True, False, False, False, True]
            eco_current_hole = 5
        elif eco_shf[6] == 8:
            eco_moveable = [False, False, False, True, False, False, False, True, False]
            eco_current_hole = 6
        elif eco_shf[7] == 8:
            eco_moveable = [False, False, False, False, True, False, True, False, True]
            eco_current_hole = 7
        else:
            eco_moveable = [False, False, False, False, False, True, False, True, False]
            eco_current_hole = 8
        return

    def mphone_shuffle_swap_vars(x):
        global eco_shf
        global mphone_playing_shuffle
        global eco_current_hole
        global shuffle_wins
        global game_money_available
        
        eco_swap_var = eco_shf[x]
        eco_shf[x] = eco_shf[eco_current_hole]
        eco_shf[eco_current_hole] = eco_swap_var
        
        if eco_shf == [0,1,2,3,4,5,6,7,8]:
            renpy.hide_screen("scr_shuffle_game")
            if game_money_available:
                mny(1)
            shuffle_wins += 1
            mphone_playing_shuffle = 4
        return

    def mphone_shuffle_win():
        global mphone_playing_shuffle
        global shuffle_wins
        global steamAchievements
        renpy.hide_screen("scr_shuffle_game")
        if game_money_available:
            mny(1)
        shuffle_wins += 1
        mphone_playing_shuffle = 4
        if steamAchievements and not config.console and not config.developer:
            achievement.grant("PUZZLEPRO")
            achievement.Sync()
        return

init:
    $ achievement.register("PUZZLEPRO")

style mphone_shuffle_style:
    font "fonts/centurygothicbold.ttf"
    size 25 * persistent.scale_factor
    color "#ffffff"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:
    def ft_clean_tank():
        global ft_filth_rate
        global ft_inv_clean
        global ft_tank_state
        global ft_tool_tip
        
        ft_inv_clean = ft_inv_clean-1
        ft_tank_state = min(100,ft_tank_state+renpy.random.randint(25,50))
        ft_filth_rate = max(20, ft_filth_rate - 5)
        
        if ft_inv_clean == 0:
            ft_tool_tip = 22
        elif ft_tank_state == 100:
            ft_tool_tip = 33
        
        return

    def ft_sell_fish():
        global ft_fish_list
        global ft_money
        global ft_tool_tip
        
        count = 0
        for fish in ft_fish_list[:]:
            if count < 5 and fish.gender == "Young":
                count += 1
                ft_fish_list.remove(fish)
        
        if sum(1 for f in ft_fish_list if f.gender == "Young") < 5:
            ft_tool_tip = 16
        ft_money += 2
        return

    def ft_remove_dead_fish():
        global ft_fish_list
        global ft_filth_rate
        
        for fish in ft_fish_list[:]:
            if fish.health == 0:
                ft_fish_list.remove(fish)
        
        ft_filth_rate = max(20, ft_filth_rate - 10)
        return

    def ft_cure_sick_fish():
        global ft_fish_list
        global ft_inv_med
        global ft_sick_rate
        global ft_tool_tip
        
        for fish in ft_fish_list[:]:
            if fish.sick:
                fish.sick = False
        
        ft_sick_rate = max(10,ft_sick_rate-10)
        ft_inv_med -= 1
        if ft_inv_med == 0:
            ft_tool_tip = 21
        return

    def ft_feed_fish():
        global ft_fish_list
        global ft_inv_food
        global ft_tool_tip
        global ft_food_state
        
        if ft_inv_food > 4 and ft_food_state <= 95:
            ft_inv_food -= 5
            ft_food_state += 5
        elif ft_inv_food > 4 and ft_food_state < 100:
            ft_inv_food = ft_inv_food-(100-ft_food_state)
            ft_food_state = ft_food_state+100-ft_food_state
        elif ft_inv_food > 0 and ft_food_state <= 100-ft_inv_food:
            ft_inv_food = 0
            ft_food_state = ft_food_state+ft_inv_food
        
        if ft_inv_food == 0:
            ft_tool_tip = 10
        elif ft_food_state == 100:
            ft_tool_tip = 32
        return

    def ft_get_mature_fish():
        global ft_fish_list
        for fish in ft_fish_list:
            if fish.gender == "Young":
                if renpy.random.randint(0,10) < 5:
                    fish.gender = "Male"
                else:
                    fish.gender = "Female"
        for fish in ft_fish_list:
            if fish.gender == "New":
                fish.gender = "Young"
        return

    def ft_get_deaths():
        global ft_fish_list
        global ft_death_rate
        
        if ft_tank_state > 50:
            ft_death_rate -= renpy.random.randint(1,5)
            if ft_death_rate < 10:
                ft_death_rate = 10
        elif ft_tank_state > 25:
            ft_death_rate = min(25,ft_death_rate+3)
        else:
            ft_death_rate = min(25,ft_death_rate+5)
        
        for fish in ft_fish_list:
            fish.health = max(0,fish.health-ft_death_rate)
        
        return

    def ft_get_food_state():
        global ft_food_left
        global ft_food_state
        global ft_death_rate
        global ft_repro_rate
        global ft_sick_rate
        global ft_filth_rate
        global ft_fish_list
        
        ft_food_left = ft_food_state - (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)) + sum(1 for f in ft_fish_list if f.gender == "New")
        ft_food_state = max(0,ft_food_left)
        
        if ft_food_left < -5:
            ft_death_rate -= max(-10,ft_food_left)
            ft_repro_rate += max(-10,ft_food_left)
            ft_sick_rate -= max(-10,ft_food_left)
            ft_filth_rate += max(-10,ft_food_left)
        elif ft_food_left < 6:
            ft_repro_rate += max(5,10 - abs(ft_food_left))
            ft_sick_rate -= max(5,10 - abs(ft_food_left))
        else:
            ft_repro_rate -= min(10,ft_food_left)
            ft_sick_rate += min(10, ft_food_left-5)
        
        ft_filth_rate += max(0, ft_food_left)
        
        if ft_death_rate > 25:
            ft_death_rate = 25
        elif ft_death_rate < 10:
            ft_death_rate = 10
        if ft_repro_rate > 30:
            ft_repro_rate = 30
        elif ft_repro_rate < 0:
            ft_repro_rate = 0
        if ft_sick_rate > 200:
            ft_sick_rate = 200
        elif ft_sick_rate < 10:
            ft_sick_rate = 10
        if ft_filth_rate > 50:
            ft_filth_rate = 50
        elif ft_filth_rate < 20:
            ft_filth_rate = 20
        
        return

    def ft_get_sickness():
        global ft_sick_rate
        global ft_fish_list
        global ft_inv_props
        
        ft_sick_rate = min(200,ft_sick_rate + sum(1 for f in ft_fish_list if f.sick))
        
        if ft_tank_state > 50:
            if ft_inv_props:
                ft_sick_rate -= renpy.random.randint(5,10)
            else:
                ft_sick_rate -= renpy.random.randint(1,5)
            if ft_sick_rate < 10:
                ft_sick_rate = 10
        elif ft_tank_state > 25:
            ft_sick_rate = min(200,ft_sick_rate + 5)
        else:
            ft_sick_rate = min(200,ft_sick_rate + 10)
        
        
        for fish in ft_fish_list:
            if not fish.sick and renpy.random.randint(0,1000) <= ft_sick_rate:
                fish.sick = True
        return

    def ft_get_new_fish():
        global ft_fish_list
        global ft_tank_state
        global ft_repro_rate
        
        if ft_tank_state > 50:
            for times in range(0,sum(1 for f in ft_fish_list if f.gender == "Female" and not f.sick)):
                if ft_repro_rate >= renpy.random.randint(0,100):
                    ft_spawn_new_fish()
        return

    def ft_spawn_new_fish():
        global ft_fish_list
        times = renpy.random.randint(1,2)
        for i in range(0,times):
            ft_fish_list.append(ft_fish("New",renpy.random.randint(40,100), renpy.random.randint(0,1000) <= ft_sick_rate))
        return

    def ft_get_repro_rate():
        global ft_repro_rate
        global ft_tank_state
        global ft_inv_ph
        
        if ft_tank_state > 50:
            ft_repro_rate = min(30,ft_repro_rate + 3)
        elif ft_tank_state > 25:
            ft_repro_rate = max(0,ft_repro_rate - 3)
        else:
            ft_repro_rate = max(0,ft_repro_rate - 7)
        
        if ft_inv_ph:
            ft_repro_rate = min(30,ft_repro_rate + 3)
        
        return

    def ft_get_filth_rate():
        global ft_tank_state
        global ft_filth_rate
        global ft_inv_filter
        
        ft_filth_rate = min(50, ft_filth_rate + sum(1 for f in ft_fish_list if f.health == 0))
        ft_tank_state = max(0,ft_tank_state - ft_filth_rate)
        
        if ft_inv_filter:
            ft_tank_state = min(100,ft_tank_state + 15)
        
        return

    def get_fish_list():
        lst = []
        for fish in ft_fish_list:
            lst.append([fish.gender, fish.health, fish.sick])
        return lst
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

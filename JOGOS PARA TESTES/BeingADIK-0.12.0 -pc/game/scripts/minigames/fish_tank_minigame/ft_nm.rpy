init python:
    def ft_init_nm():
        global ft_money
        global ft_tank_state
        global ft_food_state
        global ft_food_left
        global ft_fish_nm
        global ft_round
        
        ft_money = 2
        ft_round = 1
        ft_tank_state = 50
        ft_food_state = 50
        ft_food_left = 50
        ft_fish_nm = 50
        return

    def ft_nm_new_round():
        global ft_tank_state
        global ft_food_state
        global ft_fish_nm
        
        if ft_fish_nm <= 0:
            return
        
        tmpInt = 0
        if ft_food_state < 50:
            tmpInt +=1
        if ft_tank_state < 50:
            tmpInt +=1
        
        for x in range(0,tmpInt):
            ft_fish_nm -= renpy.random.randint(1,10)
            ft_fish_nm = max(0,ft_fish_nm)
        
        ft_tank_state = max(0,ft_tank_state - renpy.random.randint(25,65))
        ft_food_state = max(0,ft_food_state - renpy.random.randint(25,65))
        return

label ep10_ft_nm_label:
hide screen new_phone_screen
show screen ft_nm_screen
if ft_tank_state < 50 and ft_food_state < 50:
    mc "(I should clean the tank and feed the fish.)"
elif ft_tank_state < 50:
    mc "(I should clean the tank.)"
elif ft_food_state < 50:
    mc "(I should feed the fish.)"
else:
    mc "(The fish should be fine. I don't think I have to do something unless I wanna go the extra mile with it.)"
if ft_round == 1:
    "{i}Keep the food and clean levels above 50, or the fish will gradually die.{/i}"
label ep10_ft_nm_loop_label:
menu:
    "Clean tank ({color=fe9416}${/color})" if ft_money > 0 and ft_tank_state < 100:
        $ ft_tank_state = 100
        $ ft_money -= 1
        jump ep10_ft_nm_loop_label
    "Feed fish (Food left: [ft_food_left])" if ft_food_left > 0:
        $ tmpInt = min(ft_food_left,(100 - ft_food_state))
        if tmpInt == 0:
            mc "(I don't need to feed them more than this.)"
        else:
            $ ft_food_state += tmpInt
            $ ft_food_left -= tmpInt
        jump ep10_ft_nm_loop_label
    "Buy 50 Food ({color=fe9416}${/color})" if ft_money > 0:
        $ ft_money -= 1
        $ ft_food_left = min(ft_food_left + 50,500)
        jump ep10_ft_nm_loop_label
    "Add money to budget ({color=1df400}${/color})" if money > 0:
        $ mny(-1)
        $ ft_money += 1
        jump ep10_ft_nm_loop_label
    "Take money from budget ({color=fe9416}${/color})" if ft_money > 0 and ((money < 10 and wallet_lvl == 3) or (money < 8 and wallet_lvl == 2) or (money < 6 and wallet_lvl == 1) or (money < 5 and wallet_lvl == 0)):
        $ mny(1)
        $ ft_money -= 1
        jump ep10_ft_nm_loop_label
    "Done":
        hide screen ft_nm_screen
        show screen new_phone_screen

$ renpy.jump(jumpLabel)

screen ft_nm_screen:
    tag ft_nm_screen
    modal False
    add "ft_nm_ol"
    vbox:
        xalign 0.99
        yalign 0.18
        hbox:
            xminimum 350 * persistent.scale_factor
            textbutton "Pocket money: {color=1df400}$%d{/color}" % money text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                action NullAction()
        hbox:
            xminimum 350 * persistent.scale_factor
            textbutton "Budget: {color=fe9416}$%d{/color}" % ft_money text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                action NullAction()
        hbox:
            xminimum 350 * persistent.scale_factor
            if ft_fish_nm > 35:
                textbutton "Fish ({color=1df400}%d{/color})" % ft_fish_nm text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    action NullAction()
            elif ft_fish_nm > 15:
                textbutton "Fish ({color=ffed00}%d{/color})" % ft_fish_nm text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    action NullAction()
            else:
                textbutton "Fish ({color=1df400}%d{/color})" % ft_fish_nm text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    action NullAction()
        hbox:
            xminimum 350 * persistent.scale_factor
            if ft_tank_state > 50:
                textbutton "Tank: {color=1df400}Clean (%d%%){/color}" % ft_tank_state text_style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor:
                    action NullAction()
            elif ft_tank_state > 25:
                textbutton "Tank: {color=ffed00}Dirty (%d%%){/color}" % ft_tank_state text_style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor:
                    action NullAction()
            else:
                textbutton "Tank: {color=f72400}Toxic (%d%%){/color}" % ft_tank_state text_style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor:
                    action NullAction()
        hbox:
            xminimum 350 * persistent.scale_factor
            if ft_food_state > 65:
                textbutton "Food: {color=1df400}%d{/color}/100" % ft_food_state text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    action NullAction()
            elif ft_food_state > 15:
                textbutton "Food: {color=ffed00}%d{/color}/100" % ft_food_state text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    action NullAction()
            else:
                textbutton "Food: {color=f72400}%d{/color}/100" % ft_food_state text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    action NullAction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

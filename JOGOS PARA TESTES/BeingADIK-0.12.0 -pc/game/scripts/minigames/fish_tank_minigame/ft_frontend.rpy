screen ft_tool_tip_screen:
    tag ft_tool_tip_screen
    modal False
    if ft_tooltips:
        add "ft_tool_tip" at ft_tt_transform
        text "%s" % ft_tt[ft_tool_tip-1] style "ft_tt_style" xalign 0.535 yalign 0.034 at ft_tt_transform

screen fish_tank_screen:
    tag fish_tank_screen
    modal True

    if not ft_failed:
        add "ft_bg_main" at ft_bg_transform
        if ft_tank_state <= 50:
            add "ft_bg_main_dirty" at ft_bg_transform
        if ft_tank_state <= 25:
            add "ft_bg_main_toxic" at ft_bg_transform
    else:
        add "ft_bg_main_dead" at ft_bg_transform
    if not ft_failed:
        imagebutton:
            idle "ft_crazy_fish_anim"
            hover "ft_crazy_fish_anim"
            xalign 0.55
            yalign 0.5
        imagebutton:
            idle "ft_fish_anim"
            hover "ft_fish_anim"
            xalign 0.55
            yalign 0.5
    else:
        imagebutton:
            idle "dead_fish_anim"
            hover "dead_fish_anim"
            xalign 0.55
            yalign 0.0
            yoffset -300 * persistent.scale_factor
        add "ft_fail_ol"
        text "{size=+%d}{color=ffed00}Mini-game failed!{/color}\nYour fish are {color=f72400}dead{/color}.{/size}" % (40 * persistent.scale_factor) style "ft_main_style" xalign 0.53 yalign 0.5 text_align 0.5

    add "ft_overlay"
    imagebutton:
        idle "ft_x_button_idle"
        hover "ft_x_button_hover"
        hovered (SetVariable("ft_tool_tip",1), Show("ft_tool_tip_screen"))
        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
        action (Function(ft_play_menu),Hide("ft_tool_tip_screen"),Return())
        xalign 0.99
        yalign 0.01

    key "mouseup_2" action (Function(ft_play_menu),Hide("ft_tool_tip_screen"),Return())

    if ft_debug:
        vbox:
            xalign 0.5
            yalign 0.1
            spacing 50 * persistent.scale_factor
            vbox:
                text "Round %d" % ft_round
                text "ft_death_rate: %d" % ft_death_rate
                text "ft_sick_rate: %d" % ft_sick_rate
                text "ft_repro_rate: %d" % ft_repro_rate
                text "ft_filth_rate: %d" % ft_filth_rate
                text "ft_food_left: %d" % ft_food_left

    vbox:
        xalign 0.015
        yalign 0.2
        spacing 100 * persistent.scale_factor
        vbox:
            spacing 20 * persistent.scale_factor
            hbox:
                hbox:
                    xminimum 350 * persistent.scale_factor
                    if ft_tank_state > 50:
                        textbutton "Tank: {color=1df400}Clean (%d%%){/color}" % ft_tank_state text_style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor:
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",3), Show("ft_tool_tip_screen"))
                            unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    elif ft_tank_state > 25:
                        textbutton "Tank: {color=ffed00}Dirty (%d%%){/color}" % ft_tank_state text_style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor:
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",4), Show("ft_tool_tip_screen"))
                            unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    else:
                        textbutton "Tank: {color=f72400}Toxic (%d%%){/color}" % ft_tank_state text_style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor:
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",5), Show("ft_tool_tip_screen"))
                            unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                hbox:
                    imagebutton:
                        xalign 0.0
                        yalign 0.5
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        if ft_inv_clean > 0 and ft_tank_state < 100:
                            auto "ft_clean_%s"
                            action (Function(ft_play_bubbles),Function(ft_clean_tank))
                            hovered (SetVariable("ft_tool_tip",2), Show("ft_tool_tip_screen"))
                        else:
                            idle "ft_clean_disabled"
                            hover "ft_clean_disabled"
                            action NullAction()
                            if ft_inv_clean == 0:
                                hovered (SetVariable("ft_tool_tip",22), Show("ft_tool_tip_screen"))
                            else:
                                hovered (SetVariable("ft_tool_tip",33), Show("ft_tool_tip_screen"))
            hbox:
                hbox:
                    xminimum 350 * persistent.scale_factor
                    if ft_food_state + 5 < (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)):
                        textbutton "Food: {color=ffed00}%d{/color}/100" % ft_food_state text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",6), Show("ft_tool_tip_screen"))
                            unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    elif ft_food_state < (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)) + 6:
                        textbutton "Food: {color=1df400}%d{/color}/100" % ft_food_state text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",7), Show("ft_tool_tip_screen"))
                            unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    else:
                        textbutton "Food: {color=ffed00}%d{/color}/100" % ft_food_state text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",8), Show("ft_tool_tip_screen"))
                            unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                hbox:
                    imagebutton:
                        yalign 0.5
                        xalign 0.0
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        if (ft_inv_food > 4 and ft_food_state <= 95) or (ft_inv_food > 4 and ft_food_state < 100) or (ft_inv_food > 0 and ft_food_state <= 100-ft_inv_food):
                            auto "ft_food_%s"
                            action (Function(ft_play_click),Function(ft_feed_fish))
                            hovered (SetVariable("ft_tool_tip",9), Show("ft_tool_tip_screen"))
                        else:
                            idle "ft_food_disabled"
                            hover "ft_food_disabled"
                            if ft_inv_food == 0:
                                hovered (SetVariable("ft_tool_tip",10), Show("ft_tool_tip_screen"))
                            else:
                                hovered (SetVariable("ft_tool_tip",32), Show("ft_tool_tip_screen"))
                            action NullAction()
        vbox:
            xalign 0.8
            xoffset 50 * persistent.scale_factor
            spacing 20 * persistent.scale_factor
            vbox:
                spacing 20 * persistent.scale_factor
                textbutton "{u}Fish (%d){/u}" % (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)) text_style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor:
                    hovered (SetVariable("ft_tool_tip",11), Show("ft_tool_tip_screen"))
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    action NullAction()

                hbox:
                    xminimum 400 * persistent.scale_factor
                    textbutton "{color=fe67b2}Female{/color}: %d" % sum(1 for f in ft_fish_list if f.gender == "Female" and f.health > 0) text_style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor:
                        hovered (SetVariable("ft_tool_tip",12), Show("ft_tool_tip_screen"))
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        action NullAction()
                    imagebutton:
                        idle "ft_empty"
                        hover "ft_empty"
                        action NullAction()
                hbox:
                    xminimum 400 * persistent.scale_factor
                    textbutton "{color=39e4db}Male{/color}: %d" % sum(1 for f in ft_fish_list if f.gender == "Male" and f.health > 0) text_style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor:
                        hovered (SetVariable("ft_tool_tip",13), Show("ft_tool_tip_screen"))
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        action NullAction()
                    imagebutton:
                        idle "ft_empty"
                        hover "ft_empty"
                        action NullAction()
                hbox:
                    xminimum 400 * persistent.scale_factor
                    textbutton "{color=1df400}Young{/color}: %d" % sum(1 for f in ft_fish_list if f.gender == "Young" and f.health > 0) text_style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor:
                        hovered (SetVariable("ft_tool_tip",14), Show("ft_tool_tip_screen"))
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        action NullAction()
                    imagebutton:
                        xalign 0.0
                        yalign 0.5
                        xoffset -100 * persistent.scale_factor
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        if sum(1 for f in ft_fish_list if f.gender == "Young") > 4:
                            auto "ft_young_%s"
                            action (Function(ft_play_coin),Function(ft_sell_fish))
                            hovered (SetVariable("ft_tool_tip",15), Show("ft_tool_tip_screen"))
                        else:
                            idle "ft_young_disabled"
                            hover "ft_young_disabled"
                            action NullAction()
                            hovered (SetVariable("ft_tool_tip",16), Show("ft_tool_tip_screen"))
                hbox:
                    xminimum 400 * persistent.scale_factor
                    textbutton "{color=f72400}Dead{/color}: %d" % sum(1 for f in ft_fish_list if f.health == 0) text_style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor:
                        hovered (SetVariable("ft_tool_tip",17), Show("ft_tool_tip_screen"))
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        action NullAction()
                    imagebutton:
                        xalign 0.0
                        yalign 0.5
                        xoffset -100 * persistent.scale_factor
                        hovered (SetVariable("ft_tool_tip",18), Show("ft_tool_tip_screen"))
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        if sum(1 for f in ft_fish_list if f.health == 0) > 0:
                            auto "ft_dead_%s"
                            action (Function(ft_play_dead),Function(ft_remove_dead_fish))
                        else:
                            idle "ft_dead_disabled"
                            hover "ft_dead_disabled"
                            action NullAction()
                hbox:
                    xminimum 400 * persistent.scale_factor
                    textbutton "{color=ffc27b}Sick{/color}: %d" % sum(1 for f in ft_fish_list if f.sick and not f.health == 0) text_style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor:
                        hovered (SetVariable("ft_tool_tip",19), Show("ft_tool_tip_screen"))
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        action NullAction()
                    imagebutton:
                        xalign 0.0
                        yalign 0.5
                        xoffset -100 * persistent.scale_factor
                        unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                        if sum(1 for f in ft_fish_list if f.sick) > 0 and ft_inv_med > 0:
                            auto "ft_med_%s"
                            action (Function(ft_play_heal),Function(ft_cure_sick_fish))
                            hovered (SetVariable("ft_tool_tip",20), Show("ft_tool_tip_screen"))
                        else:
                            idle "ft_med_disabled"
                            hover "ft_med_disabled"
                            action NullAction()
                            if ft_inv_med == 0:
                                hovered (SetVariable("ft_tool_tip",20), Show("ft_tool_tip_screen"))
                            else:
                                hovered (SetVariable("ft_tool_tip",21), Show("ft_tool_tip_screen"))


    vbox:
        xalign 1.0
        yalign 0.3
        xminimum 380 * persistent.scale_factor
        yminimum 450 * persistent.scale_factor
        xoffset 10 * persistent.scale_factor
        text "{u}Supplies{/u}" style "ft_main_style" xminimum 350 * persistent.scale_factor xalign 0.5
        vpgrid:
            cols 3
            spacing 5 * persistent.scale_factor
            xminimum 380 * persistent.scale_factor
            yminimum 225 * persistent.scale_factor
            vbox:
                xminimum 120 * persistent.scale_factor
                xalign 0.5
                text "{color=ffed00}Food{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    hovered (SetVariable("ft_tool_tip",23), Show("ft_tool_tip_screen"))
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 0:
                        idle "ft_food_idle"
                        hover "ft_food_buy_hover"
                        action (Function(ft_play_coin),SetVariable("ft_money", ft_money-1),SetVariable("ft_inv_food",ft_inv_food+100))
                    else:
                        if ft_inv_food > 0:
                            idle "ft_food_idle"
                            hover "ft_food_idle"
                        else:
                            idle "ft_food_disabled"
                            hover "ft_food_disabled"
                        action NullAction()
                text "%d" % ft_inv_food style "ft_main_style2" xalign 0.5
            vbox:
                xminimum 120 * persistent.scale_factor
                xalign 0.5
                text "{color=ffed00}Cleaning{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    hovered (SetVariable("ft_tool_tip",24), Show("ft_tool_tip_screen"))
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 0:
                        idle "ft_clean_idle"
                        hover "ft_clean_buy_hover"
                        action (Function(ft_play_coin),SetVariable("ft_money", ft_money-1),SetVariable("ft_inv_clean",ft_inv_clean+1))
                    else:
                        if ft_inv_clean > 0:
                            idle "ft_clean_idle"
                            hover "ft_clean_idle"
                        else:
                            idle "ft_clean_disabled"
                            hover "ft_clean_disabled"
                        action NullAction()
                text "%d" % ft_inv_clean style "ft_main_style2" xalign 0.5
            vbox:
                xalign 0.5
                xminimum 120 * persistent.scale_factor
                text "{color=ffed00}Meds{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    hovered (SetVariable("ft_tool_tip",25), Show("ft_tool_tip_screen"))
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 0:
                        idle "ft_med_idle"
                        hover "ft_med_buy_hover"
                        action (Function(ft_play_coin),SetVariable("ft_money", ft_money-1),SetVariable("ft_inv_med",ft_inv_med+1))
                    else:
                        if ft_inv_med > 0:
                            idle "ft_med_idle"
                            hover "ft_med_idle"
                        else:
                            idle "ft_med_disabled"
                            hover "ft_med_disabled"
                        action NullAction()
                text "%d" % ft_inv_med style "ft_main_style2" xalign 0.5
        text "{u}Upgrades{/u}" style "ft_main_style" xminimum 350 * persistent.scale_factor xalign 0.5
        vpgrid:
            cols 3
            spacing 5 * persistent.scale_factor
            xminimum 380 * persistent.scale_factor
            yminimum 225 * persistent.scale_factor
            vbox:
                xalign 0.5
                xminimum 120 * persistent.scale_factor
                text "{color=ffc015}Air Pump{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 9 and not ft_inv_filter:
                        hovered (SetVariable("ft_tool_tip",26), Show("ft_tool_tip_screen"))
                        idle "ft_pump_idle"
                        hover "ft_pump_buy_hover"
                        action (Function(ft_play_coin),SetVariable("ft_money", ft_money-10),SetVariable("ft_inv_filter",True),SetVariable("ft_tool_tip",27))
                    else:
                        if ft_inv_filter:
                            hovered (SetVariable("ft_tool_tip",27), Show("ft_tool_tip_screen"))
                            idle "ft_pump_idle"
                            hover "ft_pump_idle"
                        else:
                            hovered (SetVariable("ft_tool_tip",26), Show("ft_tool_tip_screen"))
                            idle "ft_pump_disabled"
                            hover "ft_pump_disabled"
                        action NullAction()
                if ft_inv_filter:
                    text " " style "ft_main_style2" xalign 0.5
                else:
                    text "{color=1df400}$10{/color}" style "ft_main_style2" xalign 0.5
            vbox:
                xalign 0.5
                xminimum 120 * persistent.scale_factor
                text "{color=ffc015}Chemicals{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 9 and not ft_inv_ph:
                        idle "ft_chem_idle"
                        hover "ft_chem_buy_hover"
                        hovered (SetVariable("ft_tool_tip",28), Show("ft_tool_tip_screen"))
                        action (Function(ft_play_coin),SetVariable("ft_money", ft_money-10),SetVariable("ft_inv_ph",True),SetVariable("ft_tool_tip",29))
                    else:
                        if ft_inv_ph:
                            idle "ft_chem_idle"
                            hover "ft_chem_idle"
                            hovered (SetVariable("ft_tool_tip",29), Show("ft_tool_tip_screen"))
                        else:
                            idle "ft_chem_disabled"
                            hover "ft_chem_disabled"
                            hovered (SetVariable("ft_tool_tip",28), Show("ft_tool_tip_screen"))
                        action NullAction()
                if ft_inv_ph:
                    text " " style "ft_main_style2" xalign 0.5
                else:
                    text "{color=1df400}$10{/color}" style "ft_main_style2" xalign 0.5
            vbox:
                xalign 0.5
                xminimum 120 * persistent.scale_factor
                text "{color=ffc015}Props{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 9 and not ft_inv_props:
                        hovered (SetVariable("ft_tool_tip",30), Show("ft_tool_tip_screen"))
                        idle "ft_props_idle"
                        hover "ft_props_buy_hover"
                        action (Function(ft_play_coin),SetVariable("ft_money", ft_money-10),SetVariable("ft_inv_props",True),SetVariable("ft_tool_tip",31))
                    else:
                        if ft_inv_props:
                            idle "ft_props_idle"
                            hover "ft_props_idle"
                            hovered (SetVariable("ft_tool_tip",31), Show("ft_tool_tip_screen"))
                        else:
                            idle "ft_props_disabled"
                            hover "ft_props_disabled"
                            hovered (SetVariable("ft_tool_tip",30), Show("ft_tool_tip_screen"))
                        action NullAction()
                if ft_inv_props:
                    text " " style "ft_main_style2" xalign 0.5
                else:
                    text "{color=1df400}$10{/color}" style "ft_main_style2" xalign 0.5
    vbox:
        xalign 1.0
        yalign 0.8
        xminimum 320 * persistent.scale_factor
        xoffset -15 * persistent.scale_factor
        spacing 15 * persistent.scale_factor
        hbox:
            spacing 10 * persistent.scale_factor
            hbox:
                yalign 0.5
                xminimum 250 * persistent.scale_factor
                text "Pocket Money: {color=1df400}$%d{/color}" % money style "ft_main_style2" yalign 0.5 xmaximum 250 * persistent.scale_factor
            hbox:
                yalign 0.5
                imagebutton:
                    yalign 0.5
                    xalign 1.0
                    hovered (SetVariable("ft_tool_tip",34), Show("ft_tool_tip_screen"))
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if ft_money > 0 and ((money < 10 and wallet_lvl == 3) or (money < 8 and wallet_lvl == 2) or (money < 6 and wallet_lvl == 1) or (money < 5 and wallet_lvl == 0)):
                        auto "ft_cash_plus_%s"
                        action (Function(ft_play_click),SetVariable("ft_money", ft_money-1),SetVariable("money",money+1))
                    else:
                        idle "ft_cash_plus_disabled"
                        hover "ft_cash_plus_disabled"
                        action NullAction()
        hbox:
            spacing 10 * persistent.scale_factor
            hbox:
                yalign 0.5
                xminimum 250 * persistent.scale_factor
                text "Budget: {color=1df400}$%d{/color}" % ft_money style "ft_main_style2" yalign 0.5 xmaximum 250 * persistent.scale_factor
            hbox:
                yalign 0.5
                imagebutton:
                    yalign 0.5
                    xalign 1.0
                    hovered (SetVariable("ft_tool_tip",35), Show("ft_tool_tip_screen"))
                    unhovered (SetVariable("ft_tool_tip",0), Hide("ft_tool_tip_screen"))
                    if money > 0 and not ft_failed:
                        auto "ft_cash_plus_%s"
                        action (Function(ft_play_click),SetVariable("money", money-1),SetVariable("ft_money",ft_money+1))
                    else:
                        idle "ft_cash_plus_disabled"
                        hover "ft_cash_plus_disabled"
                        action NullAction()

    if ft_tooltips:
        textbutton "Tooltips: {color=1df400}On{/color} " text_style "ft_main_btn_style" yalign 0.99 xalign 0.967 xminimum 300 * persistent.scale_factor action (Function(ft_play_menu),SetVariable("ft_tooltips", False))
    else:
        textbutton "Tooltips: {color=909090}Off{/color}" text_style "ft_main_btn_style" yalign 0.99 xalign 0.967 xminimum 300 * persistent.scale_factor action (Function(ft_play_menu),SetVariable("ft_tooltips", True))

    if ft_first_time:
        imagebutton:
            idle "ft_big_button_idle"
            hover "ft_big_button_idle"
            action SetVariable("ft_first_time", False)
        add "ft_fail_ol"
        text "{color=ffed00}Fish tank mini-game{/color}\nKeep the fish alive by {color=ffed00}feeding{/color} them and {color=ffed00}cleaning{/color} the tank. Cure {color=ffc27b}sick{/color} fish and remove {color=f72400}dead{/color} fish to keep the tank {color=1df400}clean{/color} and the fish healthy.\nHealthy fish will reproduce. Sell the offspring ({color=1df400}young{/color} fish) for a profit or keep them to increase your fish population.\nYou {color=f72400}lose{/color} the mini-game if all your fish {color=f72400}die{/color}. Hover over any button for more information. Good luck!" style "ft_main_style3" xalign 0.53 yalign 0.5 text_align 0.5 xmaximum 800 * persistent.scale_factor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

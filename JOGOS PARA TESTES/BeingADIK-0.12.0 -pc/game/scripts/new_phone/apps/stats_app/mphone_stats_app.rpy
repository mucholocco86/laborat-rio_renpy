screen mphone_stats_app_screen():
    tag mphone_stats_app_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    default mphone_stats_page = 0

    if mphone_stats_page == 1:
        $ pp_update_happiness_icons()
        fixed:
            at mphone_app_big_transform2
            add "mphone_stats_app_pp_big"
            fixed:
                at mphone_app_stat_zoom1
                vpgrid:
                    rows 2
                    cols 4
                    xalign 0.46
                    yalign 0.39

                    for x in range(0,len(pp_dik_list)):
                        hbox:
                            spacing 25 * persistent.scale_factor
                            vbox:
                                xalign 0.5
                                imagebutton:
                                    idle "pp_happiness%d" % pp_happiness_icon[x]
                                    hover "pp_happiness%d" % pp_happiness_icon[x]
                                    xalign 0.5
                                    yoffset 10 * persistent.scale_factor
                                if pp_happiness_icon[x] == 0:
                                    text "{color=#f72400}%d%%{/color}" % pp_happiness_level[x] style "pp_eval_style" xalign 0.5
                                elif pp_happiness_icon[x] == 1:
                                    text "{color=#ffed00}%d%%{/color}" % pp_happiness_level[x] style "pp_eval_style" xalign 0.5
                                elif pp_happiness_icon[x] == 2:
                                    text "{color=#1df400}%d%%{/color}" % pp_happiness_level[x] style "pp_eval_style" xalign 0.5
                                else:
                                    text "{color=#fe9416}%d%%{/color}" % pp_happiness_level[x] style "pp_eval_style" xalign 0.5

                            imagebutton:
                                yoffset 30 * persistent.scale_factor
                                xoffset -40 * persistent.scale_factor
                                idle "pp_"+pp_dik_list[x]+"_%d_idle" % (pp_happiness_icon[x])
                                hover "pp_"+pp_dik_list[x]+"_%d_idle" % (pp_happiness_icon[x])
        fixed:
            at mphone_app_big_transform2
            fixed:
                at mphone_app_stat_zoom2
                vpgrid:
                    rows 2
                    cols 4
                    xalign 0.185
                    yalign 0.75
                    spacing 0
                    for x in range(0,len(pp_icons_limited_list)):
                        vbox:
                            xminimum 100 * persistent.scale_factor
                            text pp_icons_limited_list[x] style "pp_perk_item_style" yalign 0.5 xalign 0.5
                            imagebutton:
                                idle "pp_"+pp_icons_limited_list[x].lower()+"_idle"
                                hover "pp_"+pp_icons_limited_list[x].lower()+"_hover"
                                yalign 0.5
                                xalign 0.5
                            if pp_inventory_limited_start_list[x] > 0:
                                text "{size=+%d}%d{/size}" % ((10 * persistent.scale_factor),pp_inventory_limited_start_list[x]) style "pp_perk_item_style" yalign 0.5 xalign 0.5
                            else:
                                text "{color=ff0000}{size=+%d}%d{/size}{/color}" % ((10 * persistent.scale_factor),pp_inventory_limited_start_list[x]) style "pp_perk_item_style" yalign 0.5 xalign 0.5
        fixed:
            at mphone_app_big_transform2

            vbox:
                xalign 0.44
                yalign 0.58
                text "{u}{color=ffffff}Active Perks{/color}{/u}" style "pp_perk_item_stat_style" yalign 0.5
                vpgrid:
                    rows 6
                    cols 2
                    spacing 0
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[0]:
                            text "Pink Weiß" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Pink Weiß" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[1]:
                            text "Finger Food" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Finger Food" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[2]:
                            text "Jello Shots" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Jello Shots" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[3]:
                            text "Connections" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Connections" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[4]:
                            text "Wholesale" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Wholesale" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[5]:
                            text "Black Friday" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Black Friday" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[6]:
                            text "Crowdfunding" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Crowdfunding" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[7]:
                            text "DIK Party" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "DIK Party" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[8]:
                            text "Easy to Please" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Easy to Please" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[9]:
                            text "Hard to Let Down" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Hard to Let Down" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[10]:
                            text "Multiplier Madness" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Multiplier Madness" style "pp_perk_item_stat_style" yalign 0.5
                    vbox:
                        xminimum 220 * persistent.scale_factor
                        if pp_perk_list[11]:
                            text "Below Budget" style "pp_perk_item_stat2_style" yalign 0.5
                        else:
                            text "Below Budget" style "pp_perk_item_stat_style" yalign 0.5

        fixed:
            at mphone_app_big_transform2

            hbox:
                xpos 1108 * persistent.scale_factor
                ypos 183 * persistent.scale_factor
                xminimum 575 * persistent.scale_factor
                xmaximum 575 * persistent.scale_factor
                vpgrid:
                    draggable True
                    mousewheel True
                    cols 1
                    xminimum 575 * persistent.scale_factor
                    xmaximum 575 * persistent.scale_factor
                    yminimum 594 * persistent.scale_factor
                    ymaximum 594 * persistent.scale_factor
                    scrollbars "vertical"
                    if len(mphone_pp_history_list) < 15:
                        yinitial 0.0
                    else:
                        yinitial 1.0
                    vbox:
                        xmaximum 560 * persistent.scale_factor
                        xminimum 560 * persistent.scale_factor
                        yminimum 50 * persistent.scale_factor
                        text ""
                    for x in range(0,len(mphone_pp_history_list)):
                        vbox:
                            xmaximum 560 * persistent.scale_factor
                            xminimum 560 * persistent.scale_factor
                            yminimum 50 * persistent.scale_factor
                            text "{size=-%d}%s{/size}" % ((7 * persistent.scale_factor),mphone_pp_history_list[x]) style "mphone_bios_char_text_style"
                    text "\n\n"



                    if len(mphone_pp_history_list) < 15:
                        for x in range(0,15-len(mphone_pp_history_list)):
                            vbox:
                                xmaximum 560 * persistent.scale_factor
                                xminimum 560 * persistent.scale_factor
                                yminimum 50 * persistent.scale_factor
                                text ""
    elif mphone_stats_page == 2:
        fixed:
            at mphone_app_big_transform2
            if not ft_failed:
                if ft_tank_state > 50:
                    add "mphone_stats_app_bg_ft1"
                elif ft_tank_state > 25:
                    add "mphone_stats_app_bg_ft2"
                else:
                    add "mphone_stats_app_bg_ft3"
            else:
                add "mphone_stats_app_bg_ft_dead"

            if not ft_failed:
                imagebutton at ft_fish_transform_stat:
                    idle "ft_fish_anim"
                    hover "ft_fish_anim"
                    xalign 0.47
                    yalign 0.3
            else:
                imagebutton at ft_fish_transform_stat2:
                    idle "dead_fish_anim"
                    hover "dead_fish_anim"
                    xalign 0.47
                    yalign 0.5
                    yoffset -100 * persistent.scale_factor

            vbox:
                xalign 0.148
                yalign 0.22
                spacing 100 * persistent.scale_factor
                vbox:
                    spacing 20 * persistent.scale_factor
                    hbox:
                        xminimum 350 * persistent.scale_factor
                        if ft_tank_state > 50:
                            text "Tank: {color=1df400}Clean (%d%%){/color}" % ft_tank_state style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor
                        elif ft_tank_state > 25:
                            text "Tank: {color=ffed00}Dirty (%d%%){/color}" % ft_tank_state style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor
                        else:
                            text "Tank: {color=f72400}Toxic (%d%%){/color}" % ft_tank_state style "ft_main_style" yalign 0.5 xminimum 350 * persistent.scale_factor
                    hbox:
                        xminimum 350 * persistent.scale_factor
                        if ft_food_state + 5 < (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)):
                            text "Food: {color=ffed00}%d{/color}/100" % ft_food_state style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor
                        elif ft_food_state < (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)) + 6:
                            text "Food: {color=1df400}%d{/color}/100" % ft_food_state style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor
                        else:
                            text "Food: {color=ffed00}%d{/color}/100" % ft_food_state style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor
            vbox:
                xalign 0.120
                yalign 0.5
                xoffset 50 * persistent.scale_factor
                spacing 20 * persistent.scale_factor
                vbox:
                    spacing 20 * persistent.scale_factor
                    text "{u}Fish (%d){/u}" % (len(ft_fish_list) - sum(1 for f in ft_fish_list if f.health == 0)) style "ft_main_style" yalign 0.5 xminimum 300 * persistent.scale_factor
                    hbox:
                        xminimum 400 * persistent.scale_factor
                        text "{color=fe67b2}Female{/color}: %d" % sum(1 for f in ft_fish_list if f.gender == "Female" and f.health > 0) style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor
                    hbox:
                        xminimum 400 * persistent.scale_factor
                        text "{color=39e4db}Male{/color}: %d" % sum(1 for f in ft_fish_list if f.gender == "Male" and f.health > 0) style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor
                    hbox:
                        xminimum 400 * persistent.scale_factor
                        text "{color=1df400}Young{/color}: %d" % sum(1 for f in ft_fish_list if f.gender == "Young" and f.health > 0) style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor
                    hbox:
                        xminimum 400 * persistent.scale_factor
                        text "{color=f72400}Dead{/color}: %d" % sum(1 for f in ft_fish_list if f.health == 0) style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor
                    hbox:
                        xminimum 400 * persistent.scale_factor
                        text "{color=ffc27b}Sick{/color}: %d" % sum(1 for f in ft_fish_list if f.sick and not f.health == 0) style "ft_main_style2" yalign 0.5 xminimum 300 * persistent.scale_factor
            vbox:
                xalign 0.83
                yalign 0.35
                xminimum 380 * persistent.scale_factor
                yminimum 350 * persistent.scale_factor
                xoffset 10 * persistent.scale_factor
                spacing 5 * persistent.scale_factor
                text "{u}Supplies{/u}" style "ft_main_style" xminimum 350 * persistent.scale_factor xalign 0.5
                vpgrid:
                    cols 3
                    spacing 5 * persistent.scale_factor
                    xminimum 380 * persistent.scale_factor
                    yminimum 150 * persistent.scale_factor
                    vbox:
                        xminimum 120 * persistent.scale_factor
                        xalign 0.5
                        text "{color=ffed00}Food{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            idle "ft_food_idle"
                            hover "ft_food_idle"
                            action NullAction()
                        text "%d" % ft_inv_food style "ft_main_style2" xalign 0.5
                    vbox:
                        xminimum 120 * persistent.scale_factor
                        xalign 0.5
                        text "{color=ffed00}Cleaning{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            idle "ft_clean_idle"
                            hover "ft_clean_idle"
                            action NullAction()
                        text "%d" % ft_inv_clean style "ft_main_style2" xalign 0.5
                    vbox:
                        xalign 0.5
                        xminimum 120 * persistent.scale_factor
                        text "{color=ffed00}Meds{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            idle "ft_med_idle"
                            hover "ft_med_idle"
                            action NullAction()
                        text "%d" % ft_inv_med style "ft_main_style2" xalign 0.5
                text "{u}Upgrades{/u}" style "ft_main_style" xminimum 350 * persistent.scale_factor xalign 0.5
                vpgrid:
                    cols 3
                    spacing 5 * persistent.scale_factor
                    xminimum 380 * persistent.scale_factor
                    yminimum 150 * persistent.scale_factor
                    vbox:
                        xalign 0.5
                        xminimum 120 * persistent.scale_factor
                        text "{color=ffc015}Air Pump{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            if ft_inv_filter:
                                idle "ft_pump_idle"
                                hover "ft_pump_idle"
                            else:
                                idle "ft_pump_disabled"
                                hover "ft_pump_disabled"
                            action NullAction()
                    vbox:
                        xalign 0.5
                        xminimum 120 * persistent.scale_factor
                        text "{color=ffc015}Chemicals{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            if ft_inv_ph:
                                idle "ft_chem_idle"
                                hover "ft_chem_idle"
                            else:
                                idle "ft_chem_disabled"
                                hover "ft_chem_disabled"
                            action NullAction()
                    vbox:
                        xalign 0.5
                        xminimum 120 * persistent.scale_factor
                        text "{color=ffc015}Props{/color}" style "ft_main_style3" xalign 0.5 xminimum 200 * persistent.scale_factor
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            if ft_inv_props:
                                idle "ft_props_idle"
                                hover "ft_props_idle"
                            else:
                                idle "ft_props_disabled"
                                hover "ft_props_disabled"
                            action NullAction()
            vbox:
                xalign 0.81
                yalign 0.65
                xminimum 320 * persistent.scale_factor
                spacing 15 * persistent.scale_factor
                text "Budget: {color=1df400}$%d{/color}" % ft_money style "ft_main_style2" xmaximum 250 * persistent.scale_factor
    elif mphone_stats_page == 3:
        fixed:
            at mphone_app_big_transform2
            add "mphone_stats_app_brawler_big"

            text "Stats" style "brawler_skill_header_style" xalign 0.132 yalign 0.188
            text "Special Attack" style "brawler_skill_header_style" xalign 0.61 yalign 0.188

            vbox:
                xalign 0.17
                yalign 0.445
                spacing 20 * persistent.scale_factor
                xminimum 583 * persistent.scale_factor
                xmaximum 583 * persistent.scale_factor
                hbox:
                    text "Power" style "brawler_skill_text_style"
                hbox:
                    text "Stamina" style "brawler_skill_text_style"
                hbox:
                    text "Speed" style "brawler_skill_text_style"
                hbox:
                    text "Block" style "brawler_skill_text_style"
                hbox:
                    text "Counter" style "brawler_skill_text_style"
                hbox:
                    text "Rage" style "brawler_skill_text_style"

            vbox:
                xalign 0.323
                yalign 0.442
                spacing 47 * persistent.scale_factor
                xminimum 583 * persistent.scale_factor
                xmaximum 583 * persistent.scale_factor
                hbox:
                    yalign 0.5
                    spacing -10 * persistent.scale_factor
                    if bonusPointsSports == 12 or bn_reward_available_list[3] == 0:
                        imagebutton:
                            idle "bn_skill_bar_default"
                            hover "bn_skill_bar_default"
                        for i in range(1,bn_skill_alloc[0]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    else:
                        for i in range(0,bn_skill_alloc[0]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    for i in range(bn_skill_alloc[0],min(bn_skill_max_level,5)):
                        imagebutton:
                            idle "bn_skill_bar_empty"
                            hover "bn_skill_bar_empty"
                    for i in range(bn_skill_max_level,5):
                        add "bn_skill_bar_locked"
                hbox:
                    yalign 0.5
                    spacing -10 * persistent.scale_factor
                    imagebutton:
                        idle "bn_skill_bar_default"
                        hover "bn_skill_bar_default"
                    imagebutton:
                        idle "bn_skill_bar_default"
                        hover "bn_skill_bar_default"
                    for i in range(2,bn_skill_alloc[1]):
                        imagebutton:
                            idle "bn_skill_bar_full"
                            hover "bn_skill_bar_full"
                    for i in range(bn_skill_alloc[1],min(bn_skill_max_level,5)):
                        imagebutton:
                            idle "bn_skill_bar_empty"
                            hover "bn_skill_bar_empty"
                    for i in range(bn_skill_max_level,5):
                        add "bn_skill_bar_locked"
                hbox:
                    yalign 0.5
                    spacing -10 * persistent.scale_factor
                    if bonusPointsSports > 8 or bn_reward_available_list[3] < 2:
                        imagebutton:
                            idle "bn_skill_bar_default"
                            hover "bn_skill_bar_default"
                        for i in range(1,bn_skill_alloc[2]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    else:
                        for i in range(0,bn_skill_alloc[2]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    for i in range(bn_skill_alloc[2],min(bn_skill_max_level,5)):
                        imagebutton:
                            idle "bn_skill_bar_empty"
                            hover "bn_skill_bar_empty"
                    for i in range(bn_skill_max_level,5):
                        add "bn_skill_bar_locked"
                hbox:
                    yalign 0.5
                    spacing -10 * persistent.scale_factor
                    if bonusPointsSports > 5 or bn_reward_available_list[3] < 3:
                        imagebutton:
                            idle "bn_skill_bar_default"
                            hover "bn_skill_bar_default"
                        for i in range(1,bn_skill_alloc[3]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    else:
                        for i in range(0,bn_skill_alloc[3]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    for i in range(bn_skill_alloc[3],min(bn_skill_max_level,5)):
                        imagebutton:
                            idle "bn_skill_bar_empty"
                            hover "bn_skill_bar_empty"
                    for i in range(bn_skill_max_level,5):
                        add "bn_skill_bar_locked"
                hbox:
                    yalign 0.5
                    spacing -10 * persistent.scale_factor
                    if bonusPointsSports > 2 or bn_reward_available_list[3] < 4:
                        imagebutton:
                            idle "bn_skill_bar_default"
                            hover "bn_skill_bar_default"
                        for i in range(1,bn_skill_alloc[4]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    else:
                        for i in range(0,bn_skill_alloc[4]):
                            imagebutton:
                                idle "bn_skill_bar_full"
                                hover "bn_skill_bar_full"
                    for i in range(bn_skill_alloc[4],min(bn_skill_max_level,5)):
                        imagebutton:
                            idle "bn_skill_bar_empty"
                            hover "bn_skill_bar_empty"
                    for i in range(bn_skill_max_level,5):
                        add "bn_skill_bar_locked"
                hbox:
                    yalign 0.5
                    spacing -10 * persistent.scale_factor
                    for i in range(0,bn_skill_alloc[5]):
                        imagebutton:
                            idle "bn_skill_bar_full"
                            hover "bn_skill_bar_full"
                    for i in range(bn_skill_alloc[5],min(bn_skill_max_level,5)):
                        imagebutton:
                            idle "bn_skill_bar_empty"
                            hover "bn_skill_bar_empty"
                    for i in range(bn_skill_max_level,5):
                        add "bn_skill_bar_locked"

            imagebutton:
                xalign 0.49
                yalign 0.33
                if bn_specials_unlocked[0]:
                    if bn_special == 0:
                        idle "bn_flurry_idle"
                        hover "bn_flurry_idle"
                    elif bn_special == 1:
                        idle "bn_cripple_idle"
                        hover "bn_cripple_idle"
                    else:
                        idle "bn_highkick_idle"
                        hover "bn_highkick_idle"
                else:
                    idle "bn_unknown"
                    hover "bn_unknown"

            if bn_specials_unlocked[0]:
                if bn_special == 0:
                    text "{size=-%d}Flurry{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" yalign 0.34 xalign 0.575 xminimum 650 * persistent.scale_factor
                elif bn_special == 1:
                    text "{size=-%d}Crippling leg kick{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" yalign 0.34 xalign 0.65 xminimum 650 * persistent.scale_factor
                else:
                    text "{size=-%d}High kick combo{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" yalign 0.34 xalign 0.65 xminimum 650 * persistent.scale_factor
            else:
                text "{size=-%d}None{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" yalign 0.34 xalign 0.575 xminimum 650 * persistent.scale_factor

            vbox:
                add "bn_avatar_mc"
                xalign 0.85
                yalign 0.41
                yoffset 3 * persistent.scale_factor
            vbox:
                xalign 0.635
                yalign 0.575

                xminimum 565 * persistent.scale_factor
                vpgrid:
                    xminimum 500 * persistent.scale_factor
                    xoffset 12 * persistent.scale_factor
                    yoffset 10 * persistent.scale_factor
                    cols 2
                    spacing 14 * persistent.scale_factor
                    text "{color=fe9416}Fights                        {/color}" style "brawler_opp_style" xminimum 400 * persistent.scale_factor
                    text "{color=fe9416}%d{/color}" % bn_fight_count style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                    text "{color=1df400}Win{/color} / {color=bb433b}Lose{/color}" style "brawler_opp_style" xminimum 400 * persistent.scale_factor
                    text "{color=1df400}%d{/color} / {color=bb433b}%d{/color}" % (bn_fight_wins, bn_fight_losses) style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                    text "{color=e10d00}Highest {font=fonts/ApeMount.ttf}Rage{/font}{/color}" style "brawler_opp_style" xminimum 400 * persistent.scale_factor
                    text "{color=e10d00}%d{/color}" % bn_rage_record style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                    text "{color=00b0ff}Highest Damage{/color}" style "brawler_opp_style" xminimum 400 * persistent.scale_factor
                    text "{color=00b0ff}%d{/color}" % bn_dmg_record style "brawler_opp_style" xoffset 15 * persistent.scale_factor

                    if bn_hard_difficulty:
                        text "{color=870600}Hard Difficulty{/color}" style "brawler_opp_style" xminimum 400 * persistent.scale_factor
                    else:
                        text "{color=b7b7b7}Normal Difficulty{/color}" style "brawler_opp_style" xminimum 400 * persistent.scale_factor
    elif mphone_stats_page == 4:
        $ mphone_stats_generate_girls()
        default stats_app_girl_filter = ""
        fixed:
            at mphone_app_big_transform2
            add "mphone_stats_app_girls_big"
        fixed:
            at mphone_app_big_transform
            text "{size=-%d}Sexual History{/size}" % (5 * persistent.scale_factor) style "mphone_stats_header_style" xalign 0.14 yalign 0.185

            text "Status: {size=-%d}%s{/size}" % ((10 * persistent.scale_factor), mphone_stats_girl_get_rank()) style "ft_main_style" xalign 0.32 yalign 0.187
        fixed:
            at mphone_app_big_transform

            vpgrid:
                at stats_zoom_girls
                xpos 220 * persistent.scale_factor
                ypos 285 * persistent.scale_factor
                draggable False
                mousewheel False
                cols 7
                xminimum 1049 * persistent.scale_factor
                xmaximum 1049 * persistent.scale_factor
                yminimum 515 * persistent.scale_factor
                ymaximum 515 * persistent.scale_factor

                for x in mphone_stats_girl_list:
                    imagebutton:
                        idle "mmbios_" + x
                        hover "mmbios_" + x + "_hover"
                        if stats_app_girl_filter == x:
                            action SetScreenVariable("stats_app_girl_filter","")
                        else:
                            action SetScreenVariable("stats_app_girl_filter",x)
        fixed:
            at mphone_app_big_transform2

            hbox:
                xpos 863 * persistent.scale_factor
                ypos 183 * persistent.scale_factor
                xminimum 820 * persistent.scale_factor
                xmaximum 820 * persistent.scale_factor
                vpgrid:
                    draggable True
                    mousewheel True
                    cols 1
                    xminimum 820 * persistent.scale_factor
                    xmaximum 820 * persistent.scale_factor
                    yminimum 594 * persistent.scale_factor
                    ymaximum 594 * persistent.scale_factor
                    scrollbars "vertical"
                    if stats_girl_count(stats_app_girl_filter) < 10:
                        yinitial 0.0
                    else:
                        yinitial 1.0
                    vbox:
                        xmaximum 800 * persistent.scale_factor
                        xminimum 800 * persistent.scale_factor
                        yminimum 73 * persistent.scale_factor
                        if stats_app_girl_filter == "":
                            text "{color=ffed00}Showing:{/color} All Girls" yoffset 20 * persistent.scale_factor style "mphone_stats_text_style"
                        else:
                            if stats_app_girl_filter ==  "madamerose":
                                text "{color=ffed00}Showing:{/color} Madame Rose" yoffset 20 * persistent.scale_factor style "mphone_stats_text_style"
                            else:
                                text "{color=ffed00}Showing:{/color} %s" % stats_app_girl_filter.title() yoffset 20 * persistent.scale_factor style "mphone_stats_text_style"
                    for x in range(0,len(mphone_stats_girl_log)):
                        if stats_app_girl_filter == "" or stats_app_girl_filter == mphone_stats_girl_log[x][0]:
                            hbox:
                                yminimum 73 * persistent.scale_factor
                                spacing 30 * persistent.scale_factor
                                imagebutton:
                                    at stats_zoom_avatar
                                    idle "mmbios_" + mphone_stats_girl_log[x][0]
                                    hover "mmbios_" + mphone_stats_girl_log[x][0]
                                text "{size=-%d}%s{/size}" % ((7 * persistent.scale_factor),mphone_stats_girl_log[x][1]) style "mphone_bios_char_text_style" yalign 0.4 xmaximum 680 * persistent.scale_factor
                    for x in range(0,len(mphone_stats_girl_log_s3)):
                        if stats_app_girl_filter == "" or stats_app_girl_filter == mphone_stats_girl_log_s3[x][0]:
                            hbox:
                                yminimum 73 * persistent.scale_factor
                                spacing 30 * persistent.scale_factor
                                imagebutton:
                                    at stats_zoom_avatar
                                    idle "mmbios_" + mphone_stats_girl_log_s3[x][0]
                                    hover "mmbios_" + mphone_stats_girl_log_s3[x][0]
                                text "{size=-%d}%s{/size}" % ((7 * persistent.scale_factor),mphone_stats_girl_log_s3[x][1]) style "mphone_bios_char_text_style" yalign 0.4 xmaximum 680 * persistent.scale_factor

                    if stats_girl_count(stats_app_girl_filter) < 7:
                        for x in range(0,7-stats_girl_count(stats_app_girl_filter)):
                            vbox:
                                xmaximum 800 * persistent.scale_factor
                                xminimum 800 * persistent.scale_factor
                                yminimum 73 * persistent.scale_factor
                                text ""
    else:
        if minigames:
            $ stats_xalign = [0.11,0.425,0.817,0.13,0.488,0.98,0.11]
            $ xcomp = 0.293
        else:
            $ stats_xalign = [0.25,0.575,0.817,0.302,0.66,0.78,0.11]
            $ xcomp = 0.160
        $ dtype_list =["Neutral","{font=fonts/collegiate.ttf}{color=fe9416}DIK{/color}{/font}","Huge {font=fonts/collegiate.ttf}{color=fe9416}DIK{/color}{/font}","Massive {font=fonts/collegiate.ttf}{color=fe9416}DIK{/color}{/font}","{size=-%d}Massive {font=fonts/collegiate.ttf}{color=00a0e6}CHICK{/color}{/font}{/size}" % (5 * persistent.scale_factor),"Huge {font=fonts/collegiate.ttf}{color=00a0e6}CHICK{/color}{/font}","{font=fonts/collegiate.ttf}{color=00a0e6}CHICK{/color}{/font}"]
        $ calcRenders()
        $ calcScenes()
        $ calcWallpapers()
        $ calcArt()
        $ foundCardsSum = foundCards
        $ unlockedScenesSum = unlockedScenes

        $ totalCardsSum = persistent.totalCards
        $ totalScenesSum = persistent.totalScenes
        $ totalPassedClasses = passedEnglish + passedMath + passedGender + passedEnglishS3 + passedMathS3 + passedScienceS3
        $ totalPerfectClasses = maxedEnglish + maxedMath + maxedGender + maxedGender_s2 + maxedEnglish_s2 + maxedMath_s2 + maxedEnglishS3 + maxedMathS3 + maxedScienceS3
        $ totalFailedClasses = failedEnglish + failedMath + failedGender + failedEnglishS3 + failedMathS3 + failedScienceS3

        $ foundArtSum = foundArt
        $ totalArtSum = persistent.totalArt
        $ foundWallpaperSum = foundWallpapers
        $ totalWallpaperSum = persistent.totalWallpapers

        fixed:
            at mphone_app_big_transform2
            if minigames:
                add "mphone_stats_app_bg"
            else:
                add "mphone_stats_app_bg2"

        fixed:
            at mphone_app_big_transform
            text "Stats" style "mphone_stats_header_style" xalign stats_xalign[0] yalign 0.25
            text "Collectibles" style "mphone_stats_header_style" xalign stats_xalign[1] yalign 0.25
            if minigames:
                text "Classes & Mini-games" style "mphone_stats_header_style" xalign stats_xalign[2] yalign 0.25

            vbox:
                xalign stats_xalign[3]
                yalign 0.45
                if money > 0:
                    if wallet_lvl == 3:
                        text "Money: {color=#068109}$[money]{/color} {size=-%d}(Max $10){/size}" % (5 * persistent.scale_factor) style "mphone_stats_text_style"
                    elif wallet_lvl == 2:
                        text "Money: {color=#068109}$[money]{/color} {size=-%d}(Max $8){/size}" % (5 * persistent.scale_factor) style "mphone_stats_text_style"
                    elif wallet_lvl == 1:
                        text "Money: {color=#068109}$[money]{/color} {size=-%d}(Max $6){/size}" % (5 * persistent.scale_factor) style "mphone_stats_text_style"
                    else:
                        text "Money: {color=#068109}$[money]{/color} {size=-%d}(Max $5){/size}" % (5 * persistent.scale_factor) style "mphone_stats_text_style"
                else:
                    if wallet_lvl == 3:
                        text "Money: {color=#068109}{size=-%d}No money{/size}{/color} {size=-%d}(Max $10){/size}" % ((4 * persistent.scale_factor),(5 * persistent.scale_factor)) style "mphone_stats_text_style"
                    elif wallet_lvl == 2:
                        text "Money: {color=#068109}{size=-%d}No money{/size}{/color} {size=-%d}(Max $8){/size}" % ((4 * persistent.scale_factor),(5 * persistent.scale_factor)) style "mphone_stats_text_style"
                    elif wallet_lvl == 1:
                        text "Money: {color=#068109}{size=-%d}No money{/size}{/color} {size=-%d}(Max $6){/size}" % ((4 * persistent.scale_factor),(5 * persistent.scale_factor)) style "mphone_stats_text_style"
                    else:
                        text "Money: {color=#068109}{size=-%d}No money{/size}{/color} {size=-%d}(Max $5){/size}" % ((4 * persistent.scale_factor),(5 * persistent.scale_factor)) style "mphone_stats_text_style"

                if dik > 0:
                    text "{color=#fe9416}{font=fonts/collegiate.ttf}DIK{/font}{/color} Score: +[dik]" style "mphone_stats_text_style"
                else:
                    text "{color=#fe9416}{font=fonts/collegiate.ttf}DIK{/font}{/color} Score: [dik]" style "mphone_stats_text_style"
                text "{color=#fe9416}{font=fonts/collegiate.ttf}DIK{/font}{/color} Status: %s" % dtype_list[dtype] style "mphone_stats_text_style"

                text " " style "mphone_stats_text_style"

                if affinity == "DIK":
                    text "Affinity: {font=fonts/collegiate.ttf}{color=fe9416}%s{/color}{/font}" % affinity style "mphone_stats_text_style"
                elif affinity == "CHICK":
                    text "Affinity: {font=fonts/collegiate.ttf}{color=00a0e6}%s{/color}{/font}" % affinity style "mphone_stats_text_style"
                else:
                    text "Affinity: {font=fonts/collegiate.ttf}%s{/font}" % affinity style "mphone_stats_text_style"
                if permanent_affinity:
                    text "Permanent Affinity: Yes" style "mphone_stats_text_style"
                else:
                    text "Permanent Affinity: No" style "mphone_stats_text_style"

                if branchMayaJosy:
                    text "Chosen Road: Josy & Maya" style "mphone_stats_text_style"
                elif branchSage:
                    text "Chosen Road: Sage" style "mphone_stats_text_style"
                elif branchJill:
                    text "Chosen Road: Jill" style "mphone_stats_text_style"
                elif branchIsabella:
                    text "Chosen Road: Isabella" style "mphone_stats_text_style"
                else:
                    text "Chosen Road: Others" style "mphone_stats_text_style"

            vbox:
                xalign stats_xalign[4]

                yalign 0.485
                xminimum 455 * persistent.scale_factor
                xmaximum 455 * persistent.scale_factor

                if unlockedScenesSum == totalScenesSum:
                    text "Scenes: {color=1df400}%d/%d{/color}" % (unlockedScenesSum,totalScenesSum) style "mphone_stats_text_style"
                else:
                    text "Scenes: %d/%d" % (unlockedScenesSum,totalScenesSum) style "mphone_stats_text_style"
                if foundCardsSum == totalCardsSum:
                    text "Rewards: {color=1df400}%d/%d{/color}" % (foundCardsSum,totalCardsSum) style "mphone_stats_text_style"
                else:
                    text "Rewards: %d/%d" % (foundCardsSum,totalCardsSum) style "mphone_stats_text_style"
                if foundWallpaperSum == totalWallpaperSum:
                    text "Wallpapers: {color=1df400}%d/%d{/color}" % (foundWallpaperSum,totalWallpaperSum) style "mphone_stats_text_style"
                else:
                    text "Wallpapers: %d/%d" % (foundWallpaperSum,totalWallpaperSum) style "mphone_stats_text_style"
                if foundArtSum == totalArtSum:
                    text "2D Art: {color=1df400}%d/%d{/color}" % (foundArtSum,totalArtSum) style "mphone_stats_text_style"
                else:
                    text "2D Art: %d/%d" % (foundArtSum,totalArtSum) style "mphone_stats_text_style"
                text " " style "mphone_stats_text_style"
                if renpy.count_seen_dialogue_blocks() >= renpy.count_dialogue_blocks():
                    text "{color=ffed00}Seen Dialogue:{/color} {color=1df400}100 %{/color}" style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 95.0:
                    text "{color=ffed00}Seen Dialogue:{/color} {color=1df400}%s %%{/color}" % (str(calc_seen_dialogue())) style "mphone_stats_text_style"
                else:
                    text "{color=ffed00}Seen Dialogue:{/color} %s %%" % (str(calc_seen_dialogue())) style "mphone_stats_text_style"
                if calc_seen_dialogue() > 99.8:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}You won! But at what cost?{/color}{/size}" % (12 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 99.6:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}Not even I saw this much.{/color}{/size}" % (8 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 99.4:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}This is supposed to be an enjoyable game, you know?{/color}{/size}" % (12 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 99.2:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}The final reward is shit. You're just wasting your time.{/color}{/size}" % (12 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 99.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}Dude... Stop.{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 97.5:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}Obsessive{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 95.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=1df400}Completionist{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 90.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=fe9416}Master explorer{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 85.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=ffc27b}Adept explorer{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 80.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=ffe2c1}Novice explorer{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 70.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=ffe2c1}Initiate explorer{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 60.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=ffe2c1}Apprentice explorer{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 50.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=f7ffff}Over the hump{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 40.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=beebff}Closing in{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 30.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=76d5ff}You'll get there{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 20.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=76d5ff}Keep going{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                elif calc_seen_dialogue() > 10.0:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=dfe6fd}Getting somewhere{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"
                else:
                    text "{color=ffed00}Status:{/color} {size=-%d}{color=dfe6fd}Getting started{/color}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style"

                text " " style "mphone_stats_text_style"
            if minigames:
                vbox:
                    xminimum 700 * persistent.scale_factor
                    xmaximum 700 * persistent.scale_factor
                    xalign stats_xalign[5]
                    yalign 0.5
                    text "{size=-%d}{color=ffed00}Perfect{/color} Classes: %d{/size}" % ((3 * persistent.scale_factor),totalPerfectClasses) style "mphone_stats_text_style"
                    text "{size=-%d}{color=1df400}Passed{/color} Classes: %d{/size}" % ((3 * persistent.scale_factor),totalPassedClasses) style "mphone_stats_text_style"
                    text "{size=-%d}{color=f72400}Failed{/color} Classes: %d{/size}" % ((3 * persistent.scale_factor),totalFailedClasses) style "mphone_stats_text_style"
                    $ tmpInt = str(round((float)(shuffle_wins)/max(1.0,shuffle_losses), 2))
                    text " " style "mphone_stats_text_style"
                    text "{size=-%d}{u}Shuffle{/u}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style" yoffset -40 * persistent.scale_factor
                    text "{size=-%d}{color=1df400}Win{/color} / {color=f72400}Lose{/color}    {color=1df400}%i{/color} / {color=f72400}%i{/color}{/size}" % ((3 * persistent.scale_factor),shuffle_wins, shuffle_losses) style "mphone_stats_text_style" yoffset -40 * persistent.scale_factor

                    text "{size=-%d}{u}Triple Tile{/u}{/size}" % (3 * persistent.scale_factor) style "mphone_stats_text_style" yoffset -30 * persistent.scale_factor
                    if not triple_tile_easy_mode:
                        for i in persistent.triple_tile_highscores:
                            if i[0]!=0:
                                text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Normal{/color}{/size}" % ((8 * persistent.scale_factor),i[0],i[1]) style "mphone_triple_tile_text_style" yoffset -30 * persistent.scale_factor
                            else:
                                text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} - {color=fe9416}Normal{/color}{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" yoffset -30 * persistent.scale_factor
                    else:
                        for i in persistent.triple_tile_highscores_easy:
                            if i[0]!=0:
                                text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Easy{/color}{/size}" % ((8 * persistent.scale_factor),i[0],i[1]) style "mphone_triple_tile_text_style" yoffset -30 * persistent.scale_factor
                            else:
                                text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} - {color=fe9416}Easy{/color}{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" yoffset -30 * persistent.scale_factor

    fixed:
        at mphone_app_big_transform
        hbox:
            xalign 0.5
            yalign 0.8
            textbutton "General" action SetScreenVariable("mphone_stats_page", 0) text_style "mphone_stats_btn_text_style"
            if minigames and mphone_stats_unlocked_state > 0:
                text " | " style "mphone_stats_text_style"
                textbutton "Party Planner" action SetScreenVariable("mphone_stats_page", 1) text_style "mphone_stats_btn_text_style"
                if ep8_help_nick and mphone_stats_unlocked_state > 1:
                    text " | " style "mphone_stats_text_style"
                    textbutton "Fish Tank" action SetScreenVariable("mphone_stats_page", 2) text_style "mphone_stats_btn_text_style"
                if mphone_stats_unlocked_state > 2:
                    text " | " style "mphone_stats_text_style"
                    textbutton "Brawler" action SetScreenVariable("mphone_stats_page", 3) text_style "mphone_stats_btn_text_style"
            text " | " style "mphone_stats_text_style"
            textbutton "Girls" action SetScreenVariable("mphone_stats_page", 4) text_style "mphone_stats_btn_text_style"




    fixed:
        at mphone_app_big_transform2
        if persistent.golden_phone and persistent.golden_phone_skin_enabled:
            add "mphone_big_shell_gold"
        else:
            add "mphone_big_shell"
        add "mphone_bios_app_fg"
        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action (Show("mphone_screen"),Hide("mphone_stats_app_screen"))
            xalign 0.95
            yalign 0.5
        key "mouseup_2" action (Show("mphone_screen"),Hide("mphone_stats_app_screen"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

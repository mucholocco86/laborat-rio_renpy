screen party_planner_main_screen:
    tag party_planner_main_screen
    modal True

    if currentEpisode == 9:
        timer 37 action Function(play_lightning_ep9)
        add "pp_lightning" at pp_intro_lightning_transform2_ep9

    add "party_planner_overlay"
    imagebutton:
        idle "pp_x_button_idle"
        hover "pp_x_button_hover"
        xalign 0.985
        yalign 0.025
        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),Jump("pp_warn_label"))


    for x in range(0,6):
        for y in range(0,6):
            if len(pp_connector_grid_active[y][x])==0 and len(pp_connector_grid_inactive[y][x])==0:
                imagebutton:
                    xpos (122 + 143*x + 4*x) * persistent.scale_factor
                    ypos (29 + 143*y + 4*y) * persistent.scale_factor
                    idle "pp_connector_empty"
                    hover "pp_connector_empty"
                    action NullAction()
            else:
                for z in pp_connector_list:
                    if z in pp_connector_grid_active[y][x]:
                        imagebutton:
                            xpos (122 + 143*x + 4*x) * persistent.scale_factor
                            ypos (29 + 143*y + 4*y) * persistent.scale_factor
                            idle "pp_"+z+"_active"
                            hover "pp_"+z+"_active"
                            action NullAction()
                    elif z in pp_connector_grid_inactive[y][x]:
                        imagebutton:
                            xpos (122 + 143*x + 4*x) * persistent.scale_factor
                            ypos (29 + 143*y + 4*y) * persistent.scale_factor
                            idle "pp_"+z+"_inactive"
                            hover "pp_"+z+"_inactive"
                            action NullAction()

    vpgrid:
        xalign 0.153
        yalign 0.31
        xoffset -37 * persistent.scale_factor
        yoffset -33 * persistent.scale_factor
        rows 6
        cols 6
        spacing 4 * persistent.scale_factor
        yminimum 878 * persistent.scale_factor
        ymaximum 878 * persistent.scale_factor
        xminimum 878 * persistent.scale_factor
        xmaximum 878 * persistent.scale_factor
        draggable True
        mousewheel True
        if pp_grid_hovered[0]>-1 and pp_grid_hovered[1]>-1:
            for x in range(0,6):
                for y in range(0,6):
                    if pp_grid_hovered[0]==x and pp_grid_hovered[1]==y:
                        imagebutton:
                            yminimum 143 * persistent.scale_factor
                            ymaximum 143 * persistent.scale_factor
                            xminimum 143 * persistent.scale_factor
                            xmaximum 143 * persistent.scale_factor
                            idle "pp_grid_frame"
                            hover "pp_grid_frame"
                            action NullAction()
                    else:
                        imagebutton:
                            yminimum 143 * persistent.scale_factor
                            ymaximum 143 * persistent.scale_factor
                            xminimum 143 * persistent.scale_factor
                            xmaximum 143 * persistent.scale_factor
                            idle "pp_empty"
                            hover "pp_empty"
                            action NullAction()

    vpgrid:
        xalign 0.153
        yalign 0.31
        rows 6
        cols 6
        spacing 4 * persistent.scale_factor
        yminimum 878 * persistent.scale_factor
        ymaximum 878 * persistent.scale_factor
        xminimum 878 * persistent.scale_factor
        xmaximum 878 * persistent.scale_factor
        xoffset -37 * persistent.scale_factor
        yoffset -33 * persistent.scale_factor
        draggable True
        mousewheel True
        for x in range(0,6):
            for y in range(0,6):
                if pp_grid[x][y] == 0:
                    imagebutton:
                        yminimum 143 * persistent.scale_factor
                        ymaximum 143 * persistent.scale_factor
                        xminimum 143 * persistent.scale_factor
                        xmaximum 143 * persistent.scale_factor
                        xoffset 37 * persistent.scale_factor
                        yoffset 33 * persistent.scale_factor
                        idle "pp_empty"
                        hover "pp_empty"
                        hovered SetVariable("pp_grid_hovered",[x,y])
                        unhovered SetVariable("pp_grid_hovered",[-1,-1])
                        if pp_active_icon > -1:
                            if pp_active_icon < len(pp_icons_limited_list) and pp_inventory_limited_list[pp_active_icon] > 0:
                                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(pp_inventory_limited_list,pp_active_icon,pp_inventory_limited_list[pp_active_icon]-1), SetDict(pp_grid[x],y,pp_active_icon+1), Function(pp_handle_active_cells))
                            elif pp_active_icon < len(pp_icons_limited_list):
                                action NullAction()
                            else:
                                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(pp_grid[x],y,pp_active_icon+1), Function(pp_handle_active_cells))
                        else:
                            action NullAction()
                elif pp_grid[x][y] < len(pp_icons_limited_list) + 1:
                    imagebutton:
                        yminimum 143 * persistent.scale_factor
                        ymaximum 143 * persistent.scale_factor
                        xminimum 143 * persistent.scale_factor
                        xmaximum 143 * persistent.scale_factor
                        xoffset 37 * persistent.scale_factor
                        yoffset 33 * persistent.scale_factor
                        if pp_active_grid[x][y]:
                            if len(pp_connector_grid_active[x][y]) > 0:
                                idle "pp_"+pp_icons_limited_list[pp_grid[x][y]-1].lower()+"_active"
                            else:
                                idle "pp_"+pp_icons_limited_list[pp_grid[x][y]-1].lower()+"_idle"
                        else:
                            idle "pp_"+pp_icons_limited_list[pp_grid[x][y]-1].lower()+"_disabled"
                        hover "pp_"+pp_icons_limited_list[pp_grid[x][y]-1].lower()+"_remove"
                        hovered SetVariable("pp_grid_hovered",[x,y])
                        unhovered SetVariable("pp_grid_hovered",[-1,-1])
                        action (Play("sfx1", "sound_effects/season2/app_click.mp3", loop = False),SetDict(pp_inventory_limited_list,pp_grid[x][y]-1,pp_inventory_limited_list[pp_grid[x][y]-1]+1), SetDict(pp_grid[x],y,0), Function(pp_handle_active_cells))

                elif pp_grid[x][y] < len(pp_icons_limited_list) + len(pp_icons_unlimited_list) + 1:
                    imagebutton:
                        yminimum 143 * persistent.scale_factor
                        ymaximum 143 * persistent.scale_factor
                        xminimum 143 * persistent.scale_factor
                        xmaximum 143 * persistent.scale_factor
                        xoffset 37 * persistent.scale_factor
                        yoffset 33 * persistent.scale_factor
                        if len(pp_connector_grid_active[x][y]) > 0:
                            idle "pp_"+pp_icons_unlimited_list[pp_grid[x][y]-1-len(pp_icons_limited_list)].lower()+"_active"
                        else:
                            idle "pp_"+pp_icons_unlimited_list[pp_grid[x][y]-1-len(pp_icons_limited_list)].lower()+"_idle"
                        hover "pp_"+pp_icons_unlimited_list[pp_grid[x][y]-1-len(pp_icons_limited_list)].lower()+"_remove"
                        hovered SetVariable("pp_grid_hovered",[x,y])
                        unhovered SetVariable("pp_grid_hovered",[-1,-1])
                        action (Play("sfx1", "sound_effects/season2/app_click.mp3", loop = False),SetDict(pp_grid[x],y,0), Function(pp_handle_active_cells))
                elif pp_grid[x][y] > 99:
                    imagebutton:
                        yminimum 143 * persistent.scale_factor
                        ymaximum 143 * persistent.scale_factor
                        xminimum 143 * persistent.scale_factor
                        xmaximum 143 * persistent.scale_factor
                        idle "pp_"+pp_dik_list[pp_grid[x][y]-100]+"_%d_%d_idle" % (pp_happiness_icon[pp_grid[x][y]-100],pp_needs_met[pp_grid[x][y]-100].count(True))
                        hover "pp_"+pp_dik_list[pp_grid[x][y]-100]+"_%d_%d_idle" % (pp_happiness_icon[pp_grid[x][y]-100],pp_needs_met[pp_grid[x][y]-100].count(True))
                        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_dik_info",pp_grid[x][y]-100))

    vpgrid:
        xalign 0.153
        yalign 0.31
        rows 6
        cols 6
        spacing 4 * persistent.scale_factor
        yminimum 878 * persistent.scale_factor
        ymaximum 878 * persistent.scale_factor
        xminimum 878 * persistent.scale_factor
        xmaximum 878 * persistent.scale_factor
        xoffset -37 * persistent.scale_factor
        yoffset -33 * persistent.scale_factor
        draggable False
        mousewheel False
        for x in range(0,6):
            for y in range(0,6):
                $ tmpInt = 0
                if pp_grid[x][y] >= 100:
                    for i in range(0,8):
                        if pp_grid[x][y] == 100+i:
                            for need in range(0,3):
                                if pp_active_icon < len(pp_icons_limited_list):
                                    if pp_needs[i][need][0] == pp_icons_limited_list[pp_active_icon]:
                                        $ tmpInt = 1
                                    if pp_special_needs[i][0] == pp_icons_limited_list[pp_active_icon]:
                                        if pp_special_needs[i][1] > 0:
                                            $ tmpInt = 1
                                        else:
                                            $ tmpInt = 2
                                else:
                                    if pp_needs[i][need][0] == pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)]:
                                        $ tmpInt = 1
                                    if pp_special_needs[i][0] == pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)]:
                                        if pp_special_needs[i][1] > 0:
                                            $ tmpInt = 1
                                        else:
                                            $ tmpInt = 2
                if tmpInt == 1:
                    imagebutton:
                        idle "pp_want"
                        hover "pp_want"
                elif tmpInt == 2:
                    imagebutton:
                        idle "pp_not_want"
                        hover "pp_not_want"
                else:
                    imagebutton:
                        idle "pp_demand_empty"
                        hover "pp_demand_empty"

    imagebutton:
        yminimum 143 * persistent.scale_factor
        ymaximum 143 * persistent.scale_factor
        xminimum 143 * persistent.scale_factor
        xmaximum 143 * persistent.scale_factor
        xalign 0.068
        yalign 0.986
        idle "pp_"+pp_dik_list[pp_dik_info]+"_%d_idle" % pp_happiness_icon[pp_dik_info]
        hover "pp_"+pp_dik_list[pp_dik_info]+"_%d_idle" % pp_happiness_icon[pp_dik_info]
        action NullAction()

    text "%d%%" % (int) (pp_happiness_level[pp_dik_info]) style "pp_info_happiness_style" xpos 922 * persistent.scale_factor ypos 930 * persistent.scale_factor

    imagebutton at pp_happiness_zoom:
        idle "pp_happiness%d" % pp_happiness_icon[pp_dik_info]
        hover "pp_happiness%d" % pp_happiness_icon[pp_dik_info]
        xalign 0.49
        yalign 0.99

    vbox:
        xalign 0.28
        yalign 0.97
        xminimum 800 * persistent.scale_factor
        xmaximum 800 * persistent.scale_factor
        spacing 10 * persistent.scale_factor
        if pp_needs_met[pp_dik_info][3]:
            text "{size=-%d}%s{/size}" % ((25 * persistent.scale_factor), pp_needs[pp_dik_info][3][0]) style "pp_criteria_met_style"
        else:
            text "{size=-%d}%s{/size}" % ((25 * persistent.scale_factor), pp_needs[pp_dik_info][3][0]) style "pp_criteria_not_met_style"
        hbox:
            spacing 50 * persistent.scale_factor
            for x in range(0,3):
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        if pp_needs_met[pp_dik_info][x]:
                            idle "pp_"+pp_needs[pp_dik_info][x][0].lower()+"_active"
                            hover "pp_"+pp_needs[pp_dik_info][x][0].lower()+"_active"
                        else:
                            idle "pp_"+pp_needs[pp_dik_info][x][0].lower()+"_idle"
                            hover "pp_"+pp_needs[pp_dik_info][x][0].lower()+"_idle"
                        action NullAction()
                        yalign 0.5
                    if pp_needs_met[pp_dik_info][x]:
                        text "%d" % pp_needs[pp_dik_info][x][1] style "pp_criteria_met_style"
                    else:
                        text "%d" % pp_needs[pp_dik_info][x][1] style "pp_criteria_not_met_style"


    textbutton "Watch Tutorial" text_style "pp_header_tut_style" xalign 0.66 yalign 0.02 action Show("warning_pp_tut_screen")
    text "Items" style "pp_header_style" xalign 0.82 yalign 0.02
    text "Guests" style "pp_header_style" xalign 0.697 yalign 0.28
    text "Supplies" style "pp_header_style" xalign 0.935 yalign 0.28
    text "Activities" style "pp_header_style" xalign 0.82 yalign 0.54

    hbox:
        xalign 0.97
        yalign 0.125
        spacing 20 * persistent.scale_factor
        for x in range(0,len(pp_icons_limited_list)):
            vbox:
                if pp_active_icon == x:
                    text pp_icons_limited_list[x] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
                else:
                    text pp_icons_limited_list[x] style "pp_icon_style" yalign 0.5 xalign 0.5
                imagebutton:
                    if pp_active_icon == x:
                        idle "pp_"+pp_icons_limited_list[x].lower()+"_hover"
                    else:
                        idle "pp_"+pp_icons_limited_list[x].lower()+"_idle"
                    hover "pp_"+pp_icons_limited_list[x].lower()+"_hover"
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", x))
                    yalign 0.5
                    xalign 0.5
                if pp_inventory_limited_list[x] > 0:
                    if pp_bought_this_round[x] > 0:
                        text "{color=00ff00}{size=+%d}%d{/size}{/color}" % ((10 * persistent.scale_factor), pp_inventory_limited_list[x]) style "pp_icon_style" yalign 0.5 xalign 0.5
                    else:
                        text "{size=+%d}%d{/size}" % ((10 * persistent.scale_factor), pp_inventory_limited_list[x]) style "pp_icon_style" yalign 0.5 xalign 0.5
                else:
                    text "{color=ff0000}{size=+%d}%d{/size}{/color}" % ((10 * persistent.scale_factor), pp_inventory_limited_list[x]) style "pp_icon_style" yalign 0.5 xalign 0.5
    hbox:
        xalign 0.7
        yalign 0.41
        spacing 20 * persistent.scale_factor
        vbox:
            if pp_active_icon == 1+len(pp_icons_limited_list):
                text pp_icons_unlimited_list[1] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[1] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 1+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[1].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[1].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[1].lower()+"_hover"
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 1+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
        vbox:
            if pp_active_icon == 2+len(pp_icons_limited_list):
                text pp_icons_unlimited_list[2] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[2] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 2+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[2].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[2].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[2].lower()+"_hover"
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 2+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
    hbox:
        xalign 0.956
        yalign 0.41
        spacing 20 * persistent.scale_factor
        vbox:
            if pp_active_icon == len(pp_icons_limited_list):
                text pp_icons_unlimited_list[0] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[0] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[0].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[0].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[0].lower()+"_hover"
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
        vbox:
            if pp_active_icon == 3+len(pp_icons_limited_list):
                text pp_icons_unlimited_list[3] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[3] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 3+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[3].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[3].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[3].lower()+"_hover"
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 3+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
        vbox:
            if pp_active_icon == 4+len(pp_icons_limited_list):
                text "Trash Cans" style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text "Trash Cans" style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 4+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[4].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[4].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[4].lower()+"_hover"
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 4+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5


    vpgrid:
        xalign 1.0
        yalign 0.76
        rows len(pp_activity_list)
        cols 3
        xminimum 750 * persistent.scale_factor

        yspacing 45 * persistent.scale_factor
        xoffset 20 * persistent.scale_factor
        for x in range (0,len(pp_activity_list)):
            for y in range (0,len(pp_activity_list[x])):
                if len(pp_activity_list[x]) < 3 and y == 0:
                    textbutton " " text_style "pp_icon_style" xminimum 230 * persistent.scale_factor action NullAction()
                if pp_activity_list[x][y][1] > 0:
                    if pp_activity_choices[x]==y:
                        if len(pp_activity_list[x][y][0]) < 18:
                            textbutton "{u}%s{/u} ({color=fe9416}$%d{/color})" % (pp_activity_list[x][y][0],pp_activity_list[x][y][1]) text_style "pp_activity_selected_style" xminimum 250 * persistent.scale_factor action NullAction()
                        else:
                            textbutton "{size=-4}{u}%s{/u} ({color=fe9416}$%d{/color}){/size}" % (pp_activity_list[x][y][0],pp_activity_list[x][y][1]) text_style "pp_activity_selected_style" xminimum 250 * persistent.scale_factor action NullAction()
                    else:
                        if pp_activity_list[x][y][1] <= pp_money + pp_activity_list[x][pp_activity_choices[x]][1]:
                            if len(pp_activity_list[x][y][0]) < 18:
                                textbutton "%s ({color=fe9416}$%d{/color})" % (pp_activity_list[x][y][0],pp_activity_list[x][y][1]) text_style "pp_activity_style" xminimum 250 * persistent.scale_factor action (Play("sfx1", "sound_effects/coin.mp3", loop = False),SetVariable("pp_money",pp_money-pp_activity_list[x][y][1]+pp_activity_list[x][pp_activity_choices[x]][1]),SetDict(pp_activity_choices,x,y))
                            else:
                                textbutton "{size=-4}%s ({color=fe9416}$%d{/color}){/size}" % (pp_activity_list[x][y][0],pp_activity_list[x][y][1]) text_style "pp_activity_style" xminimum 250 * persistent.scale_factor action (Play("sfx1", "sound_effects/coin.mp3", loop = False),SetVariable("pp_money",pp_money-pp_activity_list[x][y][1]+pp_activity_list[x][pp_activity_choices[x]][1]),SetDict(pp_activity_choices,x,y))
                        else:
                            if len(pp_activity_list[x][y][0]) < 18:
                                textbutton "%s ({color=fe9416}$%d{/color})" % (pp_activity_list[x][y][0],pp_activity_list[x][y][1]) text_style "pp_activity_style_disabled" xminimum 250 * persistent.scale_factor action Play("sfx1", "sound_effects/failed_click.mp3", loop = False)
                            else:
                                textbutton "{size=-4}%s ({color=fe9416}$%d{/color}){/size}" % (pp_activity_list[x][y][0],pp_activity_list[x][y][1]) text_style "pp_activity_style_disabled" xminimum 250 * persistent.scale_factor action Play("sfx1", "sound_effects/failed_click.mp3", loop = False)
                else:
                    if pp_activity_choices[x]==y:
                        if len(pp_activity_list[x][y][0]) < 18:
                            textbutton "{u}%s{/u}" % pp_activity_list[x][y][0] text_style "pp_activity_selected_style" xminimum 250 * persistent.scale_factor action NullAction()
                        else:
                            textbutton "{size=-4}{u}%s{/u}{/size}" % pp_activity_list[x][y][0] text_style "pp_activity_selected_style" xminimum 250 * persistent.scale_factor action NullAction()
                    else:
                        if len(pp_activity_list[x][y][0]) < 18:
                            textbutton "%s" % pp_activity_list[x][y][0] text_style "pp_activity_style" xminimum 250 * persistent.scale_factor action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_money",pp_money+pp_activity_list[x][pp_activity_choices[x]][1]), SetDict(pp_activity_choices,x,y))
                        else:
                            textbutton "{size=-4}%s{/size}" % pp_activity_list[x][y][0] text_style "pp_activity_style" xminimum 250 * persistent.scale_factor action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_money",pp_money+pp_activity_list[x][pp_activity_choices[x]][1]), SetDict(pp_activity_choices,x,y))
    vbox:
        xalign 0.615
        yalign 0.77
        spacing 40 * persistent.scale_factor
        text "I" style "pp_activity_number_style"
        text "II" style "pp_activity_number_style"
        text "III" style "pp_activity_number_style"

    vbox:
        xalign 0.76
        yalign 0.975
        xminimum 400 * persistent.scale_factor
        text "{color=ffed00}Money:{/color} {color=fe9416}$[pp_money]{/color}" style "pp_stat_style" xminimum 400 * persistent.scale_factor:
            size 35 * persistent.scale_factor - 5 * persistent.scale_factor
        text "{color=ffed00}Multiplier:{/color} {color=e51475}[pp_multiplier]x{/color}" style "pp_stat_style" xminimum 400 * persistent.scale_factor:
            size 35 * persistent.scale_factor - 5 * persistent.scale_factor
        text "{color=ffed00}Score:{/color} [pp_score]" style "pp_stat_style" xminimum 400 * persistent.scale_factor:
            size 35 * persistent.scale_factor - 5 * persistent.scale_factor


    if pp_active_icon >= 0:
        if pp_active_icon < len(pp_icons_limited_list):
            hbox:
                xalign 0.89 yalign 0.92 xminimum 300 * persistent.scale_factor
                text pp_icons_limited_list[pp_active_icon] style "pp_stat_text_style" xalign 0.5
            hbox:
                xalign 0.905 yalign 0.93
                imagebutton:
                    idle "pp_"+pp_icons_limited_list[pp_active_icon].lower()+"_idle"
                    hover "pp_"+pp_icons_limited_list[pp_active_icon].lower()+"_idle"
                    action NullAction()
            hbox:
                xalign 0.998 yalign 0.95 xminimum 170 * persistent.scale_factor xoffset 15 * persistent.scale_factor
                vbox:
                    if pp_money >= pp_price_limited_list[pp_active_icon]:
                        textbutton "{size=-%d}Buy {color=fe9416}$%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_buy_style" action (Play("sfx1", "sound_effects/coin.mp3", loop = False),SetVariable("pp_money", pp_money - pp_price_limited_list[pp_active_icon]),SetDict(pp_inventory_limited_list,pp_active_icon,pp_inventory_limited_list[pp_active_icon]+1),SetDict(pp_bought_this_round,pp_active_icon,pp_bought_this_round[pp_active_icon]+1))
                    else:
                        textbutton "{size=-%d}{color=ff0000}Buy $%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_stat_style" action Play("sfx1", "sound_effects/failed_click.mp3", loop = False)
                    if pp_bought_this_round[pp_active_icon] and pp_inventory_limited_list[pp_active_icon] > 0:
                        textbutton "{size=-%d}Sell {color=fe9416}$%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_buy_style" action (Play("sfx1", "sound_effects/coin.mp3", loop = False),SetVariable("pp_money", pp_money + pp_price_limited_list[pp_active_icon]),SetDict(pp_inventory_limited_list,pp_active_icon,pp_inventory_limited_list[pp_active_icon]-1),SetDict(pp_bought_this_round,pp_active_icon,pp_bought_this_round[pp_active_icon]-1)) yoffset -10 * persistent.scale_factor
                    else:
                        textbutton "{size=-%d}{color=ff0000}Sell $%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_stat_style" action Play("sfx1", "sound_effects/failed_click.mp3", loop = False) yoffset -10 * persistent.scale_factor
        else:
            hbox:
                xalign 0.89 yalign 0.92 xminimum 300 * persistent.scale_factor
                text pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)] style "pp_stat_text_style" xalign 0.5
            hbox:
                xalign 0.905 yalign 0.93
                imagebutton:
                    idle "pp_"+pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)].lower()+"_idle"
                    hover "pp_"+pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)].lower()+"_idle"
                    action NullAction()
            hbox:
                xalign 0.998 yalign 0.925 xminimum 170 * persistent.scale_factor xoffset 20 * persistent.scale_factor
                text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (20 * persistent.scale_factor) style "pp_stat_text_style"
    hbox:
        xalign 0.96
        yalign 0.976
        xminimum 300 * persistent.scale_factor
        xmaximum 300 * persistent.scale_factor
        if pp_active_icon >= 0:
            if pp_active_icon < len(pp_icons_limited_list):
                if pp_icons_limited_dependency_list[pp_active_icon] != "":
                    text "{size=-%d}Activated by %s{/size}" % ((10 * persistent.scale_factor), pp_icons_limited_dependency_list[pp_active_icon]) style "pp_stat_style" xalign 0.5
                else:
                    text " " style "pp_stat_style"
            else:
                $ tmp_str = ""
                for i in range(0,len(pp_icons_limited_dependency_list)):
                    if pp_icons_limited_dependency_list[i] == pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)]:
                        $ tmp_str += pp_icons_limited_list[i] + " "
                if tmp_str != "":
                    text "{size=-%d}Activates [tmp_str]{/size}" % (10 * persistent.scale_factor) style "pp_stat_style" xalign 0.5
                else:
                    text " " style "pp_stat_style"
        else:
            text " " style "pp_stat_style"

screen warning_pp_screen:
    modal True
    add "warning_pp_screen"
    imagebutton:
        xalign 0.3
        yalign 0.5
        idle "pp_yes_idle"
        hover "pp_yes_hover"
        action (Hide("warning_pp_screen"),Hide("party_planner_main_screen"),Jump(pp_continue_label))
    imagebutton:
        xalign 0.7
        yalign 0.5
        idle "pp_no_idle"
        hover "pp_no_hover"
        action Jump("pp_cancel_label")

screen warning_pp_tut_screen:
    modal True
    add "warning_pp_tut_screen"
    imagebutton:
        xalign 0.3
        yalign 0.5
        idle "pp_yes_idle"
        hover "pp_yes_hover"
        action (Hide("warning_pp_tut_screen"),Hide("party_planner_main_screen"),Jump("pp_tutorial_label"))
    imagebutton:
        xalign 0.7
        yalign 0.5
        idle "pp_no_idle"
        hover "pp_no_hover"
        action Hide("warning_pp_tut_screen")

label pp_tutorial_label:
$ from_game_tut = True
$ pp_tut_inventory_limited_list = [1,1,1,1,0,1,0,0]
$ pp_bought_tut_this_round = [0,0,0,0,0,0,0,0]
$ pp_tut_state = 0
$ pp_tut_multiplier = 1.25
$ pp_tut_money = 20
call screen pp_tutorial_screen
jump currentPPRoundLabel

label pp_warn_label:
show screen warning_pp_screen
pause

label pp_cancel_label:
hide screen warning_pp_screen
pause

label party_planner_setup_round_label:
$ renpy.block_rollback()
$ pp_multiplier = 1.00
$ pp_money += pp_extra_budget + pp_below_budget
$ pp_inventory_limited_list = []
$ pp_bought_this_round = [0,0,0,0,0,0,0,0]
$ pp_inventory_limited_list.extend(pp_inventory_limited_start_list)
$ pp_needs_met = []
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs_met.append([False, False, False, False])
$ pp_needs = []
$ pp_dik_info = 0

$ pp_active_grid = [[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False]]
$ pp_connector_grid_active = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
$ pp_connector_grid_inactive = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]



if pp_round == 1:
    if pp_seed == 0:
        $ pp_grid = [[101,0,0,0,102,0],[0,0,0,0,0,0],[0,0,100,107,0,106],[0,0,0,0,0,0],[0,0,0,104,105,0],[0,103,0,0,0,0]]
    elif pp_seed == 1:
        $ pp_grid = [[101,0,0,0,102,0],[0,0,0,0,0,0],[0,0,104,105,0,106],[0,0,0,0,0,0],[0,0,0,100,107,0],[0,103,0,0,0,0]]
    elif pp_seed == 2:
        $ pp_grid = [[101,0,0,0,102,0],[0,0,0,0,0,0],[0,0,100,107,0,103],[0,0,0,0,0,0],[0,0,0,104,105,0],[0,106,0,0,0,0]]
    elif pp_seed == 3:
        $ pp_grid = [[101,0,0,0,103,0],[0,0,0,0,0,0],[0,0,100,107,0,106],[0,0,0,0,0,0],[0,0,0,104,105,0],[0,102,0,0,0,0]]
    else:
        $ pp_grid = [[101,0,0,0,106,0],[0,0,0,0,0,0],[0,0,105,107,0,102],[0,0,0,0,0,0],[0,0,0,104,100,0],[0,103,0,0,0,0]]
    $ pp_activity_list = [[["Body Shots",2],["Beer Battle",1],["Nothing",0]],[["Scary Stories",0],["Haunted Mansion",2],["Nothing",0]],[["CUM-petition",5],["Nothing",0]]]
    $ pp_needs.append([["Liquor",1],["Girls",2],["Snacks",1],["This party needs at least 2 Speakers!",0]])
    $ pp_needs.append([["Speakers",1],["Beers",1],["Girls",1],["Would be cool if the party had a Keg!",1]])
    $ pp_needs.append([["Beers",2],["Food",1],["Girls",2],["Can we have a party without Drugs for once?",2]])
    $ pp_needs.append([["Snacks",2],["Food",1],["Beers",2],["Make sure we have at least 3 Trash Cans.",3]])
    $ pp_needs.append([["Beers",3],["Liquor",1],["Girls",2],["This party gotta have at least 2 Guys!",4]])
    $ pp_needs.append([["Beers",2],["Food",1],["Speakers",1],["Let's not skimp on the Decor! At least 2!",5]])
    $ pp_needs.append([["Beers",2],["Liquor",1],["Food",1],["We need Liquor for drinks! 3 will do!",6]])
    $ pp_needs.append([["Beers",2],["Girls",3],["Drugs",1],["No sausage party! More than 5 Girls, ok?",7]])
    $ pp_special_needs = [["Speakers",2],["Kegs",1],["Drugs",0],["Trashcans",3],["Guys",2],["Decor",2],["Liquor",3],["Girls",6]]
elif pp_round == 2:
    if pp_seed == 0:
        $ pp_grid = [[0,0,0,0,0,0],[0,103,0,105,0,0],[100,0,0,0,0,106],[0,0,104,0,102,0],[0,0,0,0,0,0],[0,107,0,0,101,0]]
    elif pp_seed == 1:
        $ pp_grid = [[0,0,0,0,0,0],[0,103,0,105,0,0],[100,0,0,0,0,106],[0,0,102,0,104,0],[0,0,0,0,0,0],[0,107,0,0,101,0]]
    elif pp_seed == 2:
        $ pp_grid = [[0,0,0,0,0,0],[0,103,0,105,0,0],[100,0,0,0,0,101],[0,0,104,0,102,0],[0,0,0,0,0,0],[0,107,0,0,106,0]]
    elif pp_seed == 3:
        $ pp_grid = [[0,0,0,0,0,0],[0,103,0,105,0,0],[100,0,0,0,0,106],[0,0,104,0,102,0],[0,0,0,0,0,0],[0,101,0,0,107,0]]
    else:
        $ pp_grid = [[0,0,0,0,0,0],[0,103,0,104,0,0],[100,0,0,0,0,106],[0,0,105,0,102,0],[0,0,0,0,0,0],[0,107,0,0,101,0]]
    $ pp_activity_list = [[["New Alcohol",3],["Leftover Alcohol",1],["B.Y.O.B.",0]],[["BBQ Quality Meat",4],["BBQ Pork",2],["Hot Dogs",0]],[["Beer Pong",5],["Nothing",0]]]
    $ pp_needs.append([["Beers",2],["Speakers",1],["Food",1],["We gotta invite a lot of chicks! 6?",0]])
    $ pp_needs.append([["Snacks",1],["Beers",1],["Girls",2],["I feel like smoking some tonight.",1]])
    $ pp_needs.append([["Liquor",2],["Food",1],["Guys",2],["Music will cheer me up. 2 Speakers!",2]])
    $ pp_needs.append([["Snacks",1],["Food",1],["Beers",2],["Let's have a beer night! No hard Liquor, ok?",3]])
    $ pp_needs.append([["Kegs",1],["Liquor",2],["Decor",2],["3 Food will make sure no one is hungry.",4]])
    $ pp_needs.append([["Beers",4],["Girls",1],["Guys",1],["I wanna get drunk! At least 2 Liquor would be cool.",5]])
    $ pp_needs.append([["Snacks",2],["Beers",1],["Decor",1],["Beer should be flowing! 6 Beers!",6]])
    $ pp_needs.append([["Beers",1],["Girls",1],["Drugs",2],["Music should be blasting! 3 or so.",7]])
    $ pp_special_needs = [["Girls",6],["Drugs",1],["Speakers",2],["Liquor",0],["Food",3],["Liquor",2],["Beers",6],["Music",3]]
elif pp_round == 3:
    if pp_seed == 0:
        $ pp_grid = [[0,0,105,0,107,0],[0,0,0,0,0,0],[0,106,0,102,0,104],[0,0,0,0,0,0],[0,100,0,101,0,103],[0,0,0,0,0,0]]
    elif pp_seed == 1:
        $ pp_grid = [[0,0,105,0,103,0],[0,0,0,0,0,0],[0,106,0,102,0,104],[0,0,0,0,0,0],[0,100,0,101,0,107],[0,0,0,0,0,0]]
    elif pp_seed == 2:
        $ pp_grid = [[0,0,105,0,107,0],[0,0,0,0,0,0],[0,106,0,100,0,104],[0,0,0,0,0,0],[0,102,0,101,0,103],[0,0,0,0,0,0]]
    elif pp_seed == 3:
        $ pp_grid = [[0,0,105,0,103,0],[0,0,0,0,0,0],[0,106,0,100,0,104],[0,0,0,0,0,0],[0,102,0,101,0,107],[0,0,0,0,0,0]]
    else:
        $ pp_grid = [[0,0,105,0,103,0],[0,0,0,0,0,0],[0,102,0,106,0,104],[0,0,0,0,0,0],[0,100,0,101,0,107],[0,0,0,0,0,0]]
    $ pp_activity_list = [[["Alcohol and Food",4],["Alcohol",2],["B.Y.O.B.",0]],[["Wet T-shirt",4],["{size=-%d}Cucumber Competition{/size}" %  (2 * persistent.scale_factor),2],["Nothing",0]],[["{size=-%d}Guess Who? Game{/size}" %  (2 * persistent.scale_factor),2],["Nothing",0]]]
    $ pp_needs.append([["Liquor",2],["Girls",4],["Snacks",1],["We need Cups for all kegs! 4 Cups!",0]])
    $ pp_needs.append([["Drugs",1],["Liquor",2],["Beers",2],["People will be hungry. Make sure we have 3 Food!",1]])
    $ pp_needs.append([["Speakers",1],["Kegs",2],["Girls",3],["3 Music will have everyone in this place dancing!",2]])
    $ pp_needs.append([["Food",2],["Drugs",1],["Girls",1],["I wanna be able to snack. 3 Snacks should do.",3]])
    $ pp_needs.append([["Kegs",1],["Liquor",1],["Girls",2],["2 Decor will make this place look good!",4]])
    $ pp_needs.append([["Kegs",1],["Speakers",1],["Girls",3],["We need 5 Beers for a small competition!",5]])
    $ pp_needs.append([["Food",2],["Liquor",2],["Kegs",2],["3 Trash Cans will keep the party clean.",6]])
    $ pp_needs.append([["Beers",2],["Drugs",1],["Snacks",1],["Did you invite the 7 Girls I asked you about?",7]])
    $ pp_special_needs = [["Cups",4],["Food",3],["Music",3],["Snacks",3],["Decor",2],["Beers",5],["Trashcans",3],["Girls",7]]
elif pp_round == 4:
    if pp_seed == 0:
        $ pp_grid = [[0,0,0,103,0,0],[0,0,0,0,0,100],[0,102,105,0,0,0],[0,107,101,0,0,0],[0,0,0,0,106,0],[0,0,0,104,0,0]]
    elif pp_seed == 1:
        $ pp_grid = [[0,0,0,103,0,0],[0,0,0,0,0,100],[0,102,105,0,0,0],[0,101,107,0,0,0],[0,0,0,0,106,0],[0,0,0,104,0,0]]
    elif pp_seed == 2:
        $ pp_grid = [[0,0,0,103,0,0],[0,0,0,0,0,100],[0,105,102,0,0,0],[0,107,101,0,0,0],[0,0,0,0,106,0],[0,0,0,104,0,0]]
    elif pp_seed == 3:
        $ pp_grid = [[0,0,0,100,0,0],[0,0,0,0,0,103],[0,102,105,0,0,0],[0,107,101,0,0,0],[0,0,0,0,106,0],[0,0,0,104,0,0]]
    else:
        $ pp_grid = [[0,0,0,103,0,0],[0,0,0,0,0,100],[0,102,106,0,0,0],[0,101,107,0,0,0],[0,0,0,0,105,0],[0,0,0,104,0,0]]
    $ pp_activity_list = [[["Fancy Buffet",4],["Decent Buffet",2],["Cheap Buffet",0]],[["Card Game",4],["Nothing",0]],[["Fireworks",4],["Some Fireworks",2],["No Fireworks",0]]]
    $ pp_needs.append([["Kegs",1],["Decor",1],["Food",2],["We need 3 Speakers for this party!",0]])
    $ pp_needs.append([["Guys",2],["Food",1],["Drugs",2],["I'm tired of cleaning. Let's put out 3 Trash Cans!",1]])
    $ pp_needs.append([["Liquor",1],["Beers",2],["Guys",2],["3 Kegs would be more than enough for tonight!",2]])
    $ pp_needs.append([["Snacks",2],["Kegs",2],["Girls",1],["No Beer, unless it comes as a keg!",3]])
    $ pp_needs.append([["Drugs",2],["Speakers",1],["Decor",1],["Did you invite the 5 girls?",4]])
    $ pp_needs.append([["Liquor",2],["Beers",1],["Speakers",2],["3 Food makes for a great party!",5]])
    $ pp_needs.append([["Speakers",2],["Girls",2],["Snacks",1],["We ran out of Cups last time. Get 4 Cups!",6]])
    $ pp_needs.append([["Drugs",2],["Beers",2],["Liquor",1],["If I see any faggy Decor I'm gonna flip!",7]])
    $ pp_special_needs = [["Speakers",3],["Trashcans",3],["Kegs",3],["Beers",0],["Girls",5],["Food",3],["Cups",4],["Decor",0]]
$ pp_check_criteria_met(True)

label currentPPRoundLabel:
show screen party_planner_main_screen
pause
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

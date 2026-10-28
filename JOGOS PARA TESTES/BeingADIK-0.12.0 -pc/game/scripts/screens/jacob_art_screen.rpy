init:
    if persistent.art_unlocked_lvl1 == None:
        $ persistent.art_unlocked_lvl1 = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    if persistent.art_unlocked_lvl2 == None:
        $ persistent.art_unlocked_lvl2 = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    if persistent.art_unlocked_lvl3 == None:
        $ persistent.art_unlocked_lvl3 = [False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    if len(persistent.art_unlocked_lvl1) != 16:
        $ persistent.art_unlocked_lvl1.insert(10,False)
        $ persistent.art_unlocked_lvl1.append(False)
    if len(persistent.art_unlocked_lvl2) != 16:
        $ persistent.art_unlocked_lvl2.insert(10,False)
        $ persistent.art_unlocked_lvl2.append(False)
    if len(persistent.art_unlocked_lvl3) != 16:
        $ persistent.art_unlocked_lvl3.insert(10,False)
        $ persistent.art_unlocked_lvl3.append(False)

label art_setup_shop_label:
python:
    for x in range(0,len(persistent.art_unlocked_lvl1)):
        if persistent.art_unlocked_lvl1[x]:
            art_order_lvl1_list[x] = 2
            art_girl_level_list[x] = 1
    for x in range(0,len(persistent.art_unlocked_lvl2)):
        if persistent.art_unlocked_lvl2[x]:
            art_order_lvl2_list[x] = 2
            art_girl_level_list[x] = 2
    for x in range(0,len(persistent.art_unlocked_lvl3)):
        if persistent.art_unlocked_lvl3[x]:
            art_order_lvl3_list[x] = 2
            art_girl_level_list[x] = 3

$ tmpMenu = quick_menu
$ quick_menu = 0
hide screen new_phone_screen
show screen jacob_art_screen_main
$ renpy.pause()

label art_exit_shop_label:
hide screen jacob_art_screen_main
show screen new_phone_screen
$ quick_menu = tmpMenu
$ renpy.jump(currentFreeRoamLabel)

image spr_art1 = SnowBlossom("[persistent.img_dir]/gui/jacob_art/sprites/spr_art_star_big.png", count=4, xspeed=(5 * persistent.scale_factor, -5 * persistent.scale_factor), yspeed=(5 * persistent.scale_factor, 12 * persistent.scale_factor), fast=True)
image spr_art2 = SnowBlossom("[persistent.img_dir]/gui/jacob_art/sprites/spr_art_star2_big.png", count=4, xspeed=(5 * persistent.scale_factor, -5 * persistent.scale_factor),  yspeed=(5 * persistent.scale_factor, 12 * persistent.scale_factor), fast=True)
image spr_art3 = SnowBlossom("[persistent.img_dir]/gui/jacob_art/sprites/spr_art_star_medium.png", count=8, xspeed=(5 * persistent.scale_factor, -5 * persistent.scale_factor), yspeed=(9 * persistent.scale_factor, 13 * persistent.scale_factor), fast=True)
image spr_art4 = SnowBlossom("[persistent.img_dir]/gui/jacob_art/sprites/spr_art_star2_medium.png", count=8, xspeed=(5 * persistent.scale_factor, -5 * persistent.scale_factor),  yspeed=(9 * persistent.scale_factor, 13 * persistent.scale_factor), fast=True)
image spr_art5 = SnowBlossom("[persistent.img_dir]/gui/jacob_art/sprites/spr_art_star_small.png", count=15, xspeed=(5 * persistent.scale_factor, -5 * persistent.scale_factor), yspeed=(7 * persistent.scale_factor, 15 * persistent.scale_factor), fast=True)
image spr_art6 = SnowBlossom("[persistent.img_dir]/gui/jacob_art/sprites/spr_art_star2_small.png", count=15, xspeed=(5 * persistent.scale_factor, -5 * persistent.scale_factor),  yspeed= (7 * persistent.scale_factor, 15 * persistent.scale_factor), fast=True)
image 2d_jacob_screen_fg0:
    "2d_jacob_screen_fg" with Dissolve(0.5, alpha=True)
    pause 1
    "2d_jacob_screen_fg1" with Dissolve(0.5, alpha=True)
    pause 1
    repeat

image 2d_jacob_screen_main:
    "2d_jacob_screen_main_fr0" with Dissolve(0.5, alpha=True)
    pause 1
    "2d_jacob_screen_main_fr1" with Dissolve(0.5, alpha=True)
    pause 1
    repeat

transform jacob_screen_main_scroller:
    yalign 1.0
    linear 4 yalign 0.0
    repeat

style art2d_header_style:
    font "fonts/cabin-regular.ttf"
    size 120 * persistent.scale_factor
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

style art2d_level_style:
    font "fonts/cabin-regular.ttf"
    size 80 * persistent.scale_factor
    color "#00a0e6"
    outlines [(2, "#000000", 0, 0)]

style art2d_level2_style:
    font "fonts/cabin-regular.ttf"
    size 40 * persistent.scale_factor
    color "#fe9416"
    outlines [(2, "#000000", 0, 0)]

style art2d_price_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#ffed00"
    outlines [(2, "#000000", 0, 0)]

style art2d_criteria_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#1df400"
    outlines [(2, "#000000", 0, 0)]

style art2d_criteria_null_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

style art2d_criteria_null2_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#ff0000"
    outlines [(2, "#000000", 0, 0)]


style art2d_jacob_style:
    font "fonts/cabin-regular.ttf"
    size 130 * persistent.scale_factor
    color "#2b3b46"
    outlines [(2, "#000000", 0, 0)]

style art2d_money_style:
    font "fonts/cabin-regular.ttf"
    outlines [(2, "#000000", 0, 0)]
    size 40 * persistent.scale_factor
    color "#ffffff"
    xalign 0.7
    yalign .8
    yoffset -30 * persistent.scale_factor
    xminimum 350 * persistent.scale_factor
    xmaximum 350 * persistent.scale_factor
    text_align 0.0

transform art_rotate_title:
    rotate -90
    alpha 0.5

screen jacob_art_screen_char:
    tag jacob_art_screen_char
    modal True
    add "2d_jacob_screen_bg"
    add "spr_art1"
    add "spr_art2"
    add "spr_art3"
    add "spr_art4"
    add "spr_art5"
    add "spr_art6"
    add art_girl_list[current_girl_2d]
    add "2d_jacob_screen_fg0"
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()

    hbox:
        xalign 0.95
        yalign 0.975
        spacing 0
        imagebutton:
            idle Transform ("[persistent.img_dir]/rewards/general/rew_button_prev_idle.png")
            hover Transform ("[persistent.img_dir]/rewards/general/rew_button_prev_hover.png")
            if current_girl_2d == 0:
                action (SetDict(art_girl_new_icon,len(new_art_girl_name_list)-1,False),SetVariable("current_girl_2d",len(new_art_girl_name_list)-1))
            else:
                action (SetDict(art_girl_new_icon,max(current_girl_2d-1,0),False),SetVariable("current_girl_2d",current_girl_2d-1))
            xoffset 5 * persistent.scale_factor
        imagebutton:
            idle Transform ("[persistent.img_dir]/rewards/general/rew_button_next_idle.png")
            hover Transform ("[persistent.img_dir]/rewards/general/rew_button_next_hover.png")
            if current_girl_2d == len(new_art_girl_name_list)-1:
                action (SetDict(art_girl_new_icon,0,False),SetVariable("current_girl_2d",0))
            else:
                action (SetDict(art_girl_new_icon,current_girl_2d+1,False),SetVariable("current_girl_2d",current_girl_2d+1))
    vbox:
        xalign 0.22
        yalign 0.55
        text "%s\n{size=-%d}{color=#fe9416}Level %d/3{/color}{/size}" % (new_art_girl_name_list[current_girl_2d],(40 * persistent.scale_factor),art_girl_level_list[current_girl_2d]) style "art2d_header_style" text_align 0.5 xminimum 300

    vbox:
        xpos 1000 * persistent.scale_factor
        yalign 0.5
        xminimum 990 * persistent.scale_factor
        xmaximum 990 * persistent.scale_factor
        yminimum 990 * persistent.scale_factor
        ymaximum 990 * persistent.scale_factor
        hbox:
            spacing 25 * persistent.scale_factor
            text "{u}Level 1{/u}" style "art2d_level_style"
            imagebutton:
                if art_order_lvl1_list[current_girl_2d]>0:
                    idle "art_sold_idle"
                    hover "art_sold_idle"
                    action NullAction()
                elif money > 0 and art_girl_lvl1_list[current_girl_2d] and art_order_lvl1_list[current_girl_2d]==0:
                    idle "art_buy_idle"
                    hover "art_buy_hover"
                    action (Play("sfx1", "sound_effects/coin.mp3", loop = False), Function(mny,-1),SetDict(art_order_lvl1_list,current_girl_2d,1), SetDict(art_girl_level_list,current_girl_2d,1))
                else:
                    idle "art_buy_disabled"
                    hover "art_buy_disabled"
                    action NullAction()
                yalign 0.8
            text "Price {color=1df400}${/color}" style "art2d_price_style" yalign 0.8
        if art_girl_lvl1_list[current_girl_2d]:
            text "%s" % art_girl_crit1_list[current_girl_2d] style "art2d_criteria_style"
        else:
            if art_girl_crit1_list[current_girl_2d] == "- ???":
                text "%s" % art_girl_crit1_list[current_girl_2d] style "art2d_criteria_null_style"
            else:
                text "%s" % art_girl_crit1_list[current_girl_2d] style "art2d_criteria_null2_style"

        hbox:
            spacing 25 * persistent.scale_factor
            text "{u}Level 2{/u}" style "art2d_level_style"
            imagebutton:
                if art_order_lvl2_list[current_girl_2d]>0 or art_girl_level_list[current_girl_2d] == 2:
                    idle "art_sold_idle"
                    hover "art_sold_idle"
                    action NullAction()
                elif money > 1 and art_girl_lvl2_list[current_girl_2d] and art_order_lvl2_list[current_girl_2d]==0 and art_girl_level_list[current_girl_2d] == 1:
                    idle "art_buy_idle"
                    hover "art_buy_hover"
                    action (Play("sfx1", "sound_effects/coin.mp3", loop = False), Function(mny,-2),SetDict(art_order_lvl2_list,current_girl_2d,1), SetDict(art_girl_level_list,current_girl_2d,2))
                else:
                    idle "art_buy_disabled"
                    hover "art_buy_disabled"
                    action NullAction()
                yalign 0.8
            text "Price {color=1df400}$${/color}" style "art2d_price_style" yalign 0.8
        if art_girl_lvl2_list[current_girl_2d]:
            text "%s" % art_girl_crit2_list[current_girl_2d] style "art2d_criteria_style"
        else:
            if art_girl_crit2_list[current_girl_2d] == "- ???":
                text "%s" % art_girl_crit2_list[current_girl_2d] style "art2d_criteria_null_style"
            else:
                text "%s" % art_girl_crit2_list[current_girl_2d] style "art2d_criteria_null2_style"

        hbox:
            spacing 25 * persistent.scale_factor
            text "{u}Level 3{/u}" style "art2d_level_style" text_align 0.5
            imagebutton:
                if art_order_lvl3_list[current_girl_2d]>0 or art_girl_level_list[current_girl_2d] == 3:
                    idle "art_sold_idle"
                    hover "art_sold_idle"
                    action NullAction()
                elif money > 2 and art_girl_lvl3_list[current_girl_2d] and art_order_lvl3_list[current_girl_2d]==0 and art_girl_level_list[current_girl_2d] == 2:
                    idle "art_buy_idle"
                    hover "art_buy_hover"
                    action (Play("sfx1", "sound_effects/coin.mp3", loop = False), Function(mny,-3),SetDict(art_order_lvl3_list,current_girl_2d,1), SetDict(art_girl_level_list,current_girl_2d,3))
                else:
                    idle "art_buy_disabled"
                    hover "art_buy_disabled"
                    action NullAction()
                yalign 0.8
            text "Price {color=1df400}$$${/color}" style "art2d_price_style" yalign 0.8
        if art_girl_lvl3_list[current_girl_2d]:
            text "%s" % art_girl_crit3_list[current_girl_2d] style "art2d_criteria_style"
        else:
            if art_girl_crit3_list[current_girl_2d] == "- ???":
                text "%s" % art_girl_crit3_list[current_girl_2d] style "art2d_criteria_null_style"
            else:
                text "%s" % art_girl_crit3_list[current_girl_2d] style "art2d_criteria_null2_style"

        if money > 0:
            text "Money: {color=#36ca2b}$[money]{/color}" style "art2d_money_style"
        else:
            text "Money: {color=#36ca2b}No money{/color}" style "art2d_money_style"
    imagebutton:
        focus_mask True
        xpos 1765 * persistent.scale_factor
        ypos 20 * persistent.scale_factor
        idle "laptop_x2_button_idle"
        hover "laptop_x2_button_hover"
        action Hide("jacob_art_screen_char")
    key "mouseup_2" action Hide("jacob_art_screen_char")

screen jacob_art_screen_main:
    tag jacob_art_screen_main
    modal True
    add "2d_jacob_screen_main"
    add "2d_jacob_screen_main_scroll" at jacob_screen_main_scroller
    text "Jacob's Art Shop" at art_rotate_title style "art2d_jacob_style" xoffset -330 * persistent.scale_factor yoffset 90 * persistent.scale_factor
    vpgrid:
        ypos 0.0
        ysize 1.0
        yoffset 2 * persistent.scale_factor
        cols 5
        spacing 15 * persistent.scale_factor
        draggable True
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.5

        for x in range(0,len(new_art_girl_name_list)):
            vbox:
                xalign 0.5
                imagebutton:
                    idle "art_"+new_art_girl_name_list[x].lower()+"_idle"
                    hover "art_"+new_art_girl_name_list[x].lower()+"_hover"
                    action (SetVariable("current_girl_2d",x),Show("jacob_art_screen_char"))
                text "Level %d/3" % art_girl_level_list[x] style "art2d_level2_style" text_align 0.5 xalign 0.5

    imagebutton:
        focus_mask True
        xpos 1765 * persistent.scale_factor
        ypos 20 * persistent.scale_factor
        idle "laptop_x2_button_idle"
        hover "laptop_x2_button_hover"
        action Jump("art_exit_shop_label")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

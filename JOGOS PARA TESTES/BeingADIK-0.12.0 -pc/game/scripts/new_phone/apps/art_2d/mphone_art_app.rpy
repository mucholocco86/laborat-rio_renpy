init python:

    def setup_art_shop():
        global art_order_lvl1_list
        global art_order_lvl2_list
        global art_order_lvl3_list
        global art_girl_level_list
        
        for x in range(0,len(persistent.art_unlocked_lvl1)):
            if persistent.art_unlocked_lvl1[x]:
                art_order_lvl1_list[x] = 2
                art_girl_level_list[x] = 1
        for x in range(0,len(persistent.art_unlocked_lvl2)):
            if persistent.art_unlocked_lvl2[x]:
                art_order_lvl2_list[x] = 2
                art_girl_level_list[x] = 2
            elif art_order_lvl2_list[x] == 1:
                art_girl_level_list[x] = 2
        for x in range(0,len(persistent.art_unlocked_lvl3)):
            if persistent.art_unlocked_lvl3[x]:
                art_order_lvl3_list[x] = 2
                art_girl_level_list[x] = 3
            elif art_order_lvl3_list[x] == 1:
                art_girl_level_list[x] = 3
        return

    def art_unlock_orders():
        global art_order_lvl1_list
        global art_order_lvl2_list
        global art_order_lvl3_list
        global art_girl_level_list
        
        setup_art_shop()
        
        order_unlocked = False
        for x in range(0,len(art_order_lvl1_list)):
            if art_order_lvl1_list[x] == 1:
                art_order_lvl1_list[x] = 2
                art_girl_level_list[x] = 1
                persistent.art_unlocked_lvl1[x] = True
                order_unlocked = True
        for x in range(0,len(art_order_lvl2_list)):
            if art_order_lvl2_list[x] == 1:
                art_order_lvl2_list[x] = 2
                art_girl_level_list[x] = 2
                persistent.art_unlocked_lvl2[x] = True
                order_unlocked = True
        for x in range(0,len(art_order_lvl3_list)):
            if art_order_lvl3_list[x] == 1:
                art_order_lvl3_list[x] = 2
                art_girl_level_list[x] = 3
                persistent.art_unlocked_lvl3[x] = True
                order_unlocked = True
        
        if order_unlocked:
            persistent.chat_new_rewards = True
            unlock_wallpapers_s2()
            calcRenders()
        return order_unlocked

screen mphone_jacob_art_screen_main:
    tag mphone_jacob_art_screen_main
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
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
                    if art_girl_new_icon[x]:
                        idle "art_"+new_art_girl_name_list[x].lower()+"_new_idle"
                        hover "art_"+new_art_girl_name_list[x].lower()+"_new_hover"
                    else:
                        idle "art_"+new_art_girl_name_list[x].lower()+"_idle"
                        hover "art_"+new_art_girl_name_list[x].lower()+"_hover"
                    action (SetVariable("current_girl_2d",x),SetDict(art_girl_new_icon,x,False),Show("jacob_art_screen_char"))
                text "Level %d/3" % art_girl_level_list[x] style "art2d_level2_style" text_align 0.5 xalign 0.5

    imagebutton:
        focus_mask True
        xpos 1765 * persistent.scale_factor
        ypos 20 * persistent.scale_factor
        idle "laptop_x2_button_idle"
        hover "laptop_x2_button_hover"
        action Hide("mphone_jacob_art_screen_main")
    key "mouseup_2" action Hide("mphone_jacob_art_screen_main")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

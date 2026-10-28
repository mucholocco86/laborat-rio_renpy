screen notebook_button_screen:
    tag notebook_button_screen
    modal False
    if not _in_replay and currentEpisode == 0:
        key "mouseup_2" action (SetVariable("phone_opened",True),SetVariable("_game_menu_screen",None),Function(play_page_turn_func),Show("notebook_screen"))
        imagebutton at show_hide_dissolve:
            idle "notebook_proximity_btn"
            hover "notebook_proximity_btn_hover"
            xalign 0.021
            yalign 0.022
            action NullAction()
        imagebutton at show_hide_dissolve:
            idle "notebook_btn"
            hover "notebook_btn_hover"
            xalign 0.0205
            yalign 0.021
            action (SetVariable("phone_opened",True),SetVariable("_game_menu_screen",None),Function(play_page_turn_func),Show("notebook_screen"))

screen notebook_tutorial_screen:
    tag notebook_tutorial_screen
    modal True
    imagebutton:
        idle "notebook_tutorial_screen_button"
        hover "notebook_tutorial_screen_button"
        action (Hide("notebook_tutorial_screen"), SetVariable("phone_opened",True),SetVariable("_game_menu_screen",None),Function(play_page_turn_func),Show("notebook_screen"), Return())

screen notebook_screen:
    tag notebook_screen
    modal True
    key "mouseup_2" action (Function(play_book_close_func),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("notebook_screen"))
    imagebutton:
        idle "zoey_notebook_bg_black"
        hover "zoey_notebook_bg_black"
        focus_mask True
        action (Function(play_book_close_func),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("notebook_screen"))

    add "zoey_notebook_bg"
    if nb_state == 0:
        add "zn_page_%d" % currentNotebookPage
    else:
        if nb_state == 1 and currentNotebookPage == max_notebook_pages and vault_unlocked:
            add "zn2_page_%db" % currentNotebookPage
        else:
            add "zn2_page_%d" % currentNotebookPage


    if currentNotebookPage > 0:
        imagebutton:
            xalign 0.16
            yalign 0.92
            idle "notebook_arrow_left_idle"
            hover "notebook_arrow_left_hover"
            action (Function(play_page_turn_func),SetVariable("currentNotebookPage",currentNotebookPage-1))
    if currentNotebookPage < max_notebook_pages:
        imagebutton:
            xalign 0.84
            yalign 0.92
            idle "notebook_arrow_right_idle"
            hover "notebook_arrow_right_hover"
            action (Function(play_page_turn_func),SetVariable("currentNotebookPage",currentNotebookPage+1))

    if nb_state == 1 and currentNotebookPage == max_notebook_pages:
        hbox:
            xalign 0.29
            yalign 0.85
            spacing 20 * persistent.scale_factor
            for x in range(0,4):
                vbox:
                    xalign 0.5
                    imagebutton at mphone_vault_arrow_zoom:
                        xalign 0.5
                        idle "zoey_arrow_up_idle"
                        hover "zoey_arrow_up_hover"
                        if safe_digits[x] < 9:
                            action SetDict(safe_digits,x, safe_digits[x]+1)
                        else:
                            action SetDict(safe_digits,x, 0)
                    textbutton "%s" % safe_digits[x] text_style "zoey_vault_digit_style" xalign 0.5 yoffset -30 * persistent.scale_factor
                    imagebutton at mphone_vault_arrow_zoom:
                        xalign 0.5
                        yoffset -60 * persistent.scale_factor
                        idle "zoey_arrow_down_idle"
                        hover "zoey_arrow_down_hover"
                        if safe_digits[x] > 0:
                            action SetDict(safe_digits,x, safe_digits[x]-1)
                        else:
                            action SetDict(safe_digits,x, 9)
        fixed:
            imagebutton:
                if vault_unlocked:
                    idle "zoey_vault_unlock"
                    hover "zoey_vault_unlock"
                else:
                    idle "zoey_vault_lock_idle"
                    hover "zoey_vault_lock_hover"
                xalign 0.31
                yalign 0.96
                if safe_digits[0] == 2 and safe_digits[1] == 5 and safe_digits[2] == 7 and safe_digits[3] == 5 and not vault_unlocked:
                    action (SetVariable("vault_unlocked", True),Function(safe_rewards_unlock_epi), calcRenders(),Function(vault_ach_func))
                else:
                    action NullAction()

style zoey_vault_digit_style:
    font "fonts/daisy.ttf"
    size 80 * persistent.scale_factor
    color "#2b2b2b"

style zoey_choice_style:
    font "fonts/daisy.ttf"
    size 65 * persistent.scale_factor
    color "#000000"
    hover_color "#fe9416"
    text_align 0.5

style camera_text_style:
    font "fonts/daisy.ttf"
    size 90 * persistent.scale_factor
    color "#ffffff"
    hover_color "#ffffff"
    outlines [(4, "#000000", 0, 0)]
    text_align 0.5

transform z_choice_button_transform:
    zoom 0.8
    ease 1 zoom 0.81
    ease 1 zoom .80
    repeat

screen zoey_choice_screen(choice1, x1, y1, choice2, x2, y2):
    tag zoey_choice_screen
    modal True

    hbox:
        xpos (x1 - 50) * persistent.scale_factor
        ypos (y1 - 60) * persistent.scale_factor
        imagebutton at z_choice_button_transform:
            xalign 0.5 yalign 0.5
            idle "z_choice_button1_idle"
            hover "z_choice_button1_hover"
            hovered Function(play_bubble_func)
            action (Function(play_select_choice_func),Call("choice_1_label"))
    hbox:
        xpos x1 * persistent.scale_factor
        ypos y1 * persistent.scale_factor
        xoffset 10 * persistent.scale_factor
        yoffset 55 * persistent.scale_factor
        xminimum 350 * persistent.scale_factor
        xmaximum 350 * persistent.scale_factor
        text "%s" % choice1 style "zoey_choice_style" xalign 0.5 yalign 0.5

    hbox:
        xpos (x2 - 50) * persistent.scale_factor
        ypos (y2 - 60) * persistent.scale_factor
        imagebutton at z_choice_button_transform:
            xalign 0.5 yalign 0.5
            idle "z_choice_button2_idle"
            hover "z_choice_button2_hover"
            hovered Function(play_bubble_func)
            action (Function(play_select_choice_func),Call("choice_2_label"))

    hbox:
        xpos x2 * persistent.scale_factor
        ypos y2 * persistent.scale_factor
        xoffset 10 * persistent.scale_factor
        yoffset 55 * persistent.scale_factor
        xminimum 350 * persistent.scale_factor
        xmaximum 350 * persistent.scale_factor
        text "%s" % choice2 style "zoey_choice_style" xalign 0.5 yalign 0.5

label choice_1_label:
$ tmp_choice = 1
return

label choice_2_label:
$ tmp_choice = 2
return

screen epi_render_screen(x):
    tag epi_render_screen
    modal False
    imagebutton:
        focus_mask True
        idle "epi_card_"+ x +"_idle"
        hover "epi_card_"+ x +"_hover"
        action (Function(unlock_epi_render,x),Hide("epi_render_screen"))

screen epi_camera_screen(x):
    tag epi_camera_screen
    modal True
    for i in range(0,len(x)):
        imagebutton:
            idle "camera_icon_idle"
            hover "camera_icon_hover"
            hovered SetVariable("tmpInt",i+1)
            unhovered SetVariable("tmpInt",0)
            action (SetVariable("tmpInt",i+1), Return())
            xpos x[i][1] * persistent.scale_factor
            ypos x[i][2] * persistent.scale_factor
        if tmpInt == i+1:
            text x[i][0] style "camera_text_style" xpos x[i][3] * persistent.scale_factor ypos x[i][4] * persistent.scale_factor


init python:
    def unlock_epi_render(x):
        if x == "1" and not persistent.epi_card1:
            persistent.epi_card1 = True
            persistent.rew_2d_unlocked += 1
        elif x == "2" and not persistent.epi_card2:
            persistent.epi_card2 = True
            persistent.rew_2d_unlocked += 1
        elif x == "3" and not persistent.epi_card3:
            persistent.epi_card3 = True
            persistent.rew_2d_unlocked += 1
        elif x == "4" and not persistent.epi_card4:
            persistent.epi_card4 = True
            persistent.rew_2d_unlocked += 1
        elif x == 5 and not persistent.epi_card5:
            persistent.epi_card5 = True
            persistent.rew_mixed_unlocked += 1
        elif x == 6 and not persistent.epi_card6:
            persistent.epi_card6 = True
            persistent.rew_mixed_unlocked += 1
        elif x == 7 and not persistent.epi_card7:
            persistent.epi_card7 = True
            persistent.rew_mixed_unlocked += 1
        
        persistent.chat_new_rewards = True
        calcRenders()
        renpy.show_screen("srmsg")
        return

screen rooster_texts_screen:
    tag rooster_texts_screen
    modal False
    vbox:
        xalign 0.05
        yoffset 100 * persistent.scale_factor
        spacing 50 * persistent.scale_factor
        xminimum 600 * persistent.scale_factor
        xmaximum 600 * persistent.scale_factor

        for x in range(0,tmpInt+1):
            if x % 2 == 0:
                hbox at text_message_pop_up_random_transform:
                    spacing 20 * persistent.scale_factor
                    imagebutton:
                        idle "screen_text_avatar_%d" % (x+1)
                        hover "screen_text_avatar_%d" % (x+1)
                        action NullAction()
                        yalign 0.0
                    frame:
                        xmaximum 500 * persistent.scale_factor
                        xpadding 20 * persistent.scale_factor
                        ypadding 20 * persistent.scale_factor
                        yoffset -5 * persistent.scale_factor
                        background Frame("screen_text_message_them",10 * persistent.scale_factor,10 * persistent.scale_factor)

                        has vbox
                        text "{color=2b2b2b}%s{/color}" % text_message_screen_list[x] style "text_message_screen_style" text_align 0.0
            else:
                hbox at text_message_pop_up_random_transform2:
                    spacing 20 * persistent.scale_factor
                    imagebutton:
                        idle "screen_text_avatar_%d" % (x+1)
                        hover "screen_text_avatar_%d" % (x+1)
                        action NullAction()
                        yalign 0.0
                    frame:
                        xmaximum 500 * persistent.scale_factor
                        xpadding 20 * persistent.scale_factor
                        ypadding 20 * persistent.scale_factor
                        yoffset -5 * persistent.scale_factor
                        background Frame("screen_text_message_them",10 * persistent.scale_factor,10 * persistent.scale_factor)

                        has vbox
                        text "{color=2b2b2b}%s{/color}" % text_message_screen_list[x] style "text_message_screen_style" text_align 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

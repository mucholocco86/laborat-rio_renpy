label app_new_brawler_label:
$ renpy.block_rollback()
$ bn_jump_label = currentFreeRoamLabel
$ bn_freeroam = True
if "Visit the gym (Brawler)" in optional_task_list:
    $ optional_task_list[optional_task_list.index("Visit the gym (Brawler)")] = ""
    $ updateTaskList()
label app_new_brawler_story_label:
$ renpy.block_rollback()
$ _game_menu_screen = None
$ map_fast_travel_enabled = False
hide screen new_phone_screen
$ phone_opened = True
$ bn_play_song(bn_playlist)
show screen brawler_menu_screen
$ renpy.pause()

label app_new_brawler_quit_label:
stop music fadeout 2
$ phone_opened = False
hide screen brawler_menu_screen
hide screen brawler_result_screen
show screen new_phone_screen
$ _game_menu_screen = "save"
if bn_freeroam:
    $ mphone_next_song()
$ map_fast_travel_enabled = True
$ renpy.jump(bn_jump_label)

screen brawler_menu_screen:
    tag brawler_menu_screen
    modal True
    add "bg anim_brawler_movie movie"

    add "brawler_menu_ol"

    default bn_item_hovered = -1
    default bn_show_quit_message = False
    if bn_quit_message != "":
        key "mouseup_2" action (Function(bn_play_failed_click,0,0,0),SetScreenVariable("bn_show_quit_message",True))
    else:
        key "mouseup_2" action (Function(bn_play_click,0,0,0),Jump("app_new_brawler_quit_label"))

    if bn_item_hovered == 0:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.26
    elif bn_item_hovered == 1:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.385
    elif bn_item_hovered == 2:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.52
    elif bn_item_hovered == 3:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.653
    elif bn_item_hovered == 4:
        add "brawler_double_sel_arr" xalign 0.032 yalign 0.78
    vbox:
        xalign 0.065
        yalign 0.55
        spacing 0
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 0), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action (Function(bn_play_click,0,0,0),Function(bn_init_opponents),Show("brawler_opponent_screen"),Hide("brawler_menu_screen"))
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 1), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action (Function(bn_play_click,0,0,0),Show("brawler_skill_screen"),Hide("brawler_menu_screen"))
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 2), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action (Function(bn_play_click,0,0,0),Show("brawler_tutorial_screen"),Hide("brawler_menu_screen"))
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 3), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            action ShowMenu('save')
        imagebutton:
            idle "brawler_menu_box_idle"
            hover "brawler_menu_box_hover"
            hovered SetScreenVariable("bn_item_hovered", 4), Function(bn_play_hover,0,0,0)
            unhovered SetScreenVariable("bn_item_hovered", -1)
            if bn_quit_message != "":
                action (Function(bn_play_failed_click,0,0,0),SetScreenVariable("bn_show_quit_message",True))
            else:
                action (Function(bn_play_click,0,0,0),Jump("app_new_brawler_quit_label"))

    if bn_show_quit_message:
        timer 3 repeat False action SetScreenVariable("bn_show_quit_message",False)
        imagebutton at show_hide_dissolve:
            idle "bg_toprightmsg"
            xalign 0.9825
            yalign -0.01
            action NullAction()
        text "[bn_quit_message]" style "score_new_style" at show_hide_dissolve:
            xalign 0.97
            yalign 0.01

    vbox:
        xalign 0.118
        yalign 0.54
        spacing 65 * persistent.scale_factor + (persistent.scale_factor-1)*10
        if bn_item_hovered == 0:
            text "Fight" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Fight" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 1:
            text "Skills" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Skills" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 2:
            text "Tutorial" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Tutorial" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 3:
            text "Save" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Save" style "brawler_menu_text_style" xalign 0.5
        if bn_item_hovered == 4:
            text "Quit" style "brawler_menu_text_selected_style" xalign 0.5
        else:
            text "Quit" style "brawler_menu_text_style" xalign 0.5

    if bn_playlist:
        textbutton "{color=ffe059}Music Playlist:{/color} Brawler Playlist" action (Function(bn_play_click,0,0,0),SetVariable("bn_playlist",False), Function(bn_play_song,False)) xminimum 500 * persistent.scale_factor xmaximum 500 * persistent.scale_factor xalign 0.049 text_align 0.5 yalign 0.89 text_style "brawler_menu_diff_style"
    else:
        textbutton "{color=ffe059}Music Playlist:{/color} Favorites Playlist" action (Function(bn_play_click,0,0,0),SetVariable("bn_playlist",True),Function(bn_play_song,True)) xminimum 500 * persistent.scale_factor xmaximum 500 * persistent.scale_factor text_align 0.5 xalign 0.049 yalign 0.89 text_style "brawler_menu_diff_style"

    default bn_change_diff = False
    if bn_hard_difficulty and not bn_change_diff:
        textbutton "{color=870600}Hard Difficulty{/color} {color=#ffffff}|{/color} Lower Difficulty" action (Function(bn_play_reset,0,0,0),SetScreenVariable("bn_change_diff",True)) xalign 0.047 yalign 0.96 text_style "brawler_menu_diff_style"
    elif bn_hard_difficulty and bn_change_diff:
        timer 3 repeat False action SetScreenVariable("bn_change_diff",False)
        textbutton "{size=-%d}Click to permanently lower the difficulty{/size}" % (3 * persistent.scale_factor) action (Function(bn_play_reset,0,0,0),Function(bn_lower_difficulty)) xalign 0.017 yalign 0.96 text_style "brawler_menu_diff_style"
    else:
        textbutton "{color=b7b7b7}Normal Difficulty{/color}" action Function(bn_play_failed_click,0,0,0) xalign 0.11 yalign 0.96 text_style "brawler_menu_diff_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

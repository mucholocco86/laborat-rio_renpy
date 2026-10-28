init python:
    def sm_play_notepad():
        renpy.play("sound_effects/interlude/page_turn.mp3","sfx1")
        return
    def sm_play_sketch():
        renpy.play("sound_effects/interlude/sketch.mp3","sfx1")
        return
screen sm_timer_screen:
    tag sm_timer_screen
    modal False
    zorder 100

    default start_time = time.time()
    default current_time = time.time()
    timer 0.05 repeat True action If(ms_time -  (current_time-start_time) - sm_time_penalty > 0.0, true=SetScreenVariable('current_time', time.time()), false=[Function(sm_calc_purity),Hide("sm_timer_screen"),Hide("sm_measure_screen"),Hide("sm_weigh_screen"),Hide("sm_notes_screen"),Hide("sm_stir_screen"),Hide("sm_turn_in_screen"),Hide("science_screen"),Jump(science_jump_label)])
    $ tmp_time = max(ms_time -  (current_time-start_time) - sm_time_penalty,0)
    hbox:
        xalign 0.98
        yalign 0.02
        xminimum 100 * persistent.scale_factor
        if tmp_time > 70:
            text "%d" % tmp_time style "sm_time1_style"
        elif tmp_time > 30:
            text "%d" % tmp_time style "sm_time2_style"
        else:
            text "%d" % tmp_time style "sm_time3_style"


init -5 python:

    style.sm_bar_style = Style(style.default)
    style.sm_bar_style.left_bar = Frame("gui/bar/left.png", 0, 0)
    style.sm_bar_style.right_bar = Frame("gui/bar/right.png", 0, 0)
    style.sm_bar_style.ymaximum = 20 * persistent.scale_factor 

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen science_screen:
    tag science_screen
    modal True

    if len(sm_cue_color_change) > 0:
        timer sm_cue_color_change[0] repeat False action Function(sm_change_color)

    if sm_button_set > 0:
        if sm_button_set == 1:
            vbox:
                xalign 0.105
                yalign 0.7
                textbutton "Pour" text_style "sm_button_menu_style":
                    xalign 0.5
                    if sm_measure_result_vol > 0:
                        action (Function(sm_clear_selection), SetVariable("sm_pour_mode",1), Show("sm_pour_screen"))
                textbutton "Discard" text_style "sm_button_menu_style" action (Function(sm_clear_selection),Function(sm_discard_measure)) xalign 0.5
        elif sm_button_set == 2:
            vbox:
                xalign 0.256
                yalign 0.76
                textbutton "Add to" text_style "sm_button_menu_style":
                    xalign 0.5
                    if sm_weigh_result > 0:
                        action (Function(sm_clear_selection), SetVariable("sm_pour_mode",2), Show("sm_pour_screen"))
                textbutton "Discard" text_style "sm_button_menu_style" action (Function(sm_clear_selection),Function(sm_discard_weigh,True)) xalign 0.5
        elif sm_button_set == 3:
            vbox:
                xalign 0.50
                yalign 0.76
                textbutton "Stir settings" text_style "sm_button_menu_style":
                    xalign 0.5
                    action (Function(sm_clear_selection),Show("sm_stir_screen"))
                textbutton "Pour" text_style "sm_button_menu_style":
                    xalign 0.5
                    if sm_stirrer_vol > 0:
                        action (Function(sm_clear_selection), SetVariable("sm_pour_mode",3), Show("sm_pour_screen"))
                textbutton "Discard" text_style "sm_button_menu_style" action (Function(sm_clear_selection),Function(sm_discard_stirrer)) xalign 0.5
        elif sm_button_set == 4:
            vbox:
                xalign 0.65
                yalign 0.2
                textbutton "Turn in" text_style "sm_button_menu_style":
                    xalign 0.5
                    action Function(sm_clear_selection), Show("sm_turn_in_screen")
                textbutton "Discard" text_style "sm_button_menu_style" action (Function(sm_clear_selection),Function(sm_discard_round)) xalign 0.5


    imagebutton:
        idle "sm_notepad_idle"
        hover "sm_notepad_hover"
        focus_mask True
        action (Function(sm_clear_selection),Function(sm_play_notepad),Show("sm_notes_screen"))


    imagebutton:
        idle "sm_vol_%s_idle" % sm_vol_str
        hover "sm_vol_%s_hover" % sm_vol_str
        focus_mask True
        action SetVariable("sm_button_set",1)


    imagebutton:
        idle "sm_scale_%s_idle" % sm_scale_str
        hover "sm_scale_%s_hover" % sm_scale_str
        focus_mask True
        action SetVariable("sm_button_set",2)


    imagebutton:
        idle "sm_red_liquid_idle"
        hover "sm_red_liquid_hover"
        focus_mask True
        action (Function(sm_clear_selection),Function(sm_init_measure,"red"),Show("sm_measure_screen"))
    imagebutton:
        idle "sm_green_liquid_idle"
        hover "sm_green_liquid_hover"
        focus_mask True
        action (Function(sm_clear_selection),Function(sm_init_measure,"green"),Show("sm_measure_screen"))
    imagebutton:
        idle "sm_blue_liquid_idle"
        hover "sm_blue_liquid_hover"
        focus_mask True
        action (Function(sm_clear_selection),Function(sm_init_measure,"blue"),Show("sm_measure_screen"))


    imagebutton:
        idle "sm_red_solids_idle"
        hover "sm_red_solids_hover"
        focus_mask True
        action (Function(sm_clear_selection),Function(sm_init_weigh,"red"),Show("sm_weigh_screen"))
    imagebutton:
        idle "sm_blue_solids_idle"
        hover "sm_blue_solids_hover"
        focus_mask True
        action (Function(sm_clear_selection),Function(sm_init_weigh,"blue"),Show("sm_weigh_screen"))


    imagebutton:
        if sm_stirrer_on:
            idle "sm_stirrer_%s_bubbles_idle" % sm_stirrer_str
            hover "sm_stirrer_%s_bubbles_hover" % sm_stirrer_str
        else:
            idle "sm_stirrer_%s_idle" % sm_stirrer_str
            hover "sm_stirrer_%s_hover" % sm_stirrer_str
        focus_mask True
        action SetVariable("sm_button_set",3)


    imagebutton:
        if sm_bunsen_on:
            idle "sm_bunsen_on_idle"
            hover "sm_bunsen_on_hover"
            focus_mask True
            action (Function(sm_play_burner_off),Function(sm_clear_selection),Function(sm_bunsen,False))
        else:
            idle "sm_bunsen_off_idle"
            hover "sm_bunsen_off_hover"
            focus_mask True
            action (Function(sm_play_burner),Function(sm_clear_selection),Function(sm_bunsen,True))


    imagebutton:
        if sm_bunsen_on:
            idle "sm_round_%s_bubbles_idle" % sm_round_str
            hover "sm_round_%s_bubbles_hover" % sm_round_str
        else:
            idle "sm_round_%s_idle" % sm_round_str
            hover "sm_round_%s_hover" % sm_round_str
        focus_mask True
        action SetVariable("sm_button_set",4)

    if persistent.colorblind:
        text "Liquids\n{color=#ffffff}Red  Green  Blue{/color}" style "sm_help_style" xalign 0.14 yalign 0.24 text_align 0.5
        text "Salts\n{color=#ffffff}Red   Blue{/color}" style "sm_help_style" xalign 0.3 yalign 0.18 text_align 0.5
        text "Volumetric flask\n{color=#ffffff}%s{/color}" % sm_vol_str.capitalize() style "sm_help_style" xalign 0.07 yalign 0.42 text_align 0.5
        text "Scale" style "sm_help_style" xalign 0.27 yalign 0.47
        text "Stirrer\n{color=#ffffff}%s{/color}" % sm_stirrer_str.capitalize() style "sm_help_style" xalign 0.498 yalign 0.415 text_align 0.5
        text "Round flask\n{color=#ffffff}%s{/color}" % sm_round_str.capitalize() style "sm_help_style" xalign 0.714 yalign 0.32 text_align 0.5
        text "Burner" style "sm_help_style" xalign 0.705 yalign 0.668
        text "Notepad" style "sm_help_style" xalign 0.89 yalign 0.34
    else:
        text "Liquids" style "sm_help_style" xalign 0.16 yalign 0.26
        text "Salts" style "sm_help_style" xalign 0.3 yalign 0.2
        text "Volumetric flask" style "sm_help_style" xalign 0.07 yalign 0.42
        text "Scale" style "sm_help_style" xalign 0.27 yalign 0.47
        text "Stirrer" style "sm_help_style" xalign 0.498 yalign 0.415
        text "Round flask" style "sm_help_style" xalign 0.714 yalign 0.35
        text "Burner" style "sm_help_style" xalign 0.705 yalign 0.668
        text "Notepad" style "sm_help_style" xalign 0.89 yalign 0.34


style sm_button_menu_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    hover_color "#fe9416"
    insensitive_color "#808080"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 30 * persistent.scale_factor

style sm_help_style:
    font "fonts/cabin-regular.ttf"
    color "#ffe059"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 30 * persistent.scale_factor

style sm_time1_style:
    font "fonts/cabin-regular.ttf"
    color "#6dff59"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 50 * persistent.scale_factor
style sm_time2_style:
    font "fonts/cabin-regular.ttf"
    color "#ffe059"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 50 * persistent.scale_factor
style sm_time3_style:
    font "fonts/cabin-regular.ttf"
    color "#bb433b"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 50 * persistent.scale_factor


screen sm_turn_in_screen:
    tag sm_turn_in_screen
    modal True

    if sm_round_str == "blue":
        add "science_minigame_results_blue"
    elif sm_round_str == "red":
        add "science_minigame_results_red"
    elif sm_round_str == "clear":
        add "science_minigame_results_clear"
    elif sm_round_str == "green":
        add "science_minigame_results_green"
    else:
        add "science_minigame_results_empty"

    vbox:
        xalign 0.98
        yalign 0.4
        xminimum 800 * persistent.scale_factor
        xmaximum 800 * persistent.scale_factor
        spacing 20 * persistent.scale_factor
        text "{size=-%d}Do you want to turn in your solution and end the experiment?{/size}" % (150 * persistent.scale_factor) style "sm_measure_style_yellow" xalign 0.5 text_align 0.5
        hbox:
            xalign 0.5
            spacing 100 * persistent.scale_factor
            textbutton "Yes" text_style "sm_measure_button_style" action (Function(sm_mute_sfx),Function(sm_calc_purity),Hide("sm_timer_screen"),Hide("sm_turn_in_screen"),Hide("science_screen"),Jump(science_jump_label))
            textbutton "Cancel" text_style "sm_measure_button_style" action Hide("sm_turn_in_screen")

screen sm_pour_screen:
    tag sm_pour_screen
    modal True
    if sm_pour_mode == 1:
        vbox:
            xalign 0.105
            yalign 0.67
            textbutton "Cancel" text_style "sm_button_menu_style" action Hide("sm_pour_screen") xalign 0.5
        vbox:
            xalign 0.50
            yalign 0.68
            textbutton "Add to beaker" text_style "sm_button_menu_style" action (Function(sm_play_pour),Function(sm_add_to_beaker),Hide("sm_pour_screen")) xalign 0.5
        vbox:
            xalign 0.725
            yalign 0.39
            textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_play_pour),Function(sm_add_to_flask),Hide("sm_pour_screen")) xalign 0.5
    elif sm_pour_mode == 2:
        vbox:
            xalign 0.256
            yalign 0.72
            textbutton "Cancel" text_style "sm_button_menu_style" action Hide("sm_pour_screen") xalign 0.5
        vbox:
            xalign 0.50
            yalign 0.68
            textbutton "Add to beaker" text_style "sm_button_menu_style" action (Function(sm_add_to_beaker),Hide("sm_pour_screen")) xalign 0.5
        vbox:
            xalign 0.725
            yalign 0.39
            textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_add_to_flask),Hide("sm_pour_screen")) xalign 0.5
    elif sm_pour_mode == 3:
        vbox:
            xalign 0.50
            yalign 0.68
            textbutton "Cancel" text_style "sm_button_menu_style" action Hide("sm_pour_screen") xalign 0.5
        vbox:
            xalign 0.725
            yalign 0.39
            textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_play_pour),Function(sm_add_to_flask),Hide("sm_pour_screen")) xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

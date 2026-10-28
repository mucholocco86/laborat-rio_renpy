style sm_stir_button_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    selected_idle_color "#ffe059"
    insensitive_color "#808080"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 40 * persistent.scale_factor

style sm_stir_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 40 * persistent.scale_factor

screen sm_stir_screen:
    tag sm_stir_screen

    modal False

    if sm_stirrer_on:
        add "science_minigame_stir_%s_bubbles" % sm_stirrer_str
    else:
        add "science_minigame_stir_%s" % sm_stirrer_str

    vbox:
        spacing 50 * persistent.scale_factor
        xalign 0.95 yalign 0.2
        hbox:
            spacing 100 * persistent.scale_factor
            textbutton "Stirrer:" text_style "sm_stir_style" xalign 0.5

            textbutton "On" text_style "sm_stir_button_style" action (Function(sm_play_stirrer),SetVariable("sm_stirrer_on", True),Function(sm_check_stirrer))
            textbutton "Off" text_style "sm_stir_button_style" action (Function(sm_play_stirrer_stop),SetVariable("sm_stirrer_on", False),Function(sm_check_stirrer))

        hbox:
            spacing 100 * persistent.scale_factor
            textbutton "Speed:" text_style "sm_stir_style" xalign 0.5
            textbutton "Slow" text_style "sm_stir_button_style" action SetVariable("sm_stirrer_mode", 0),Function(sm_check_stirrer)
            textbutton "Medium" text_style "sm_stir_button_style" action SetVariable("sm_stirrer_mode", 1),Function(sm_check_stirrer)
            textbutton "Fast" text_style "sm_stir_button_style" action SetVariable("sm_stirrer_mode", 2),Function(sm_check_stirrer)


        textbutton "Ok" text_style "sm_measure_button_style" action (Function(sm_play_stirrer_stop),Function(sm_check_stirrer),Hide("sm_stir_screen")) xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

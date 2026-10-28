style sm_measure_style:
    font "fonts/cabin-regular.ttf"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 50 * persistent.scale_factor

style sm_measure_button_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    insensitive_color "#808080"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 60 * persistent.scale_factor

style sm_measure_style_yellow:
    font "fonts/cabin-regular.ttf"
    color "#ffe059"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 200 * persistent.scale_factor

screen sm_measure_screen:
    tag sm_measure_screen
    modal True
    add "science_minigame_measure_empty"

    if sm_measure_phase == 0:
        text "How much do you want to measure?" style "sm_measure_style" xalign 0.9 yalign 0.3
        vbox:
            xalign 0.60
            yalign 0.48
            textbutton "{size=+%d}+{/size}" % (90 * persistent.scale_factor) text_style "sm_measure_button_style" action SetVariable("sm_measure_vol",min(100,sm_measure_vol+10))
            textbutton "{size=+%d}-{/size}" % (90 * persistent.scale_factor) text_style "sm_measure_button_style" action SetVariable("sm_measure_vol",max(0,sm_measure_vol-10)) yoffset -50 * persistent.scale_factor
        vbox:
            text "%s" % sm_measure_vol style "sm_measure_style_yellow" xalign 1.0
            xalign 0.75 yalign 0.45
            xminimum 500 * persistent.scale_factor
        vbox:
            xalign 0.92
            yalign 0.46
            spacing 40 * persistent.scale_factor
            textbutton "Ok" text_style "sm_measure_button_style" action If (sm_measure_vol > 0, (SetVariable("e_time", 1.95), SetVariable("sm_measure_phase", 1),Show("sm_measure_bar_screen")))
            textbutton "Cancel" text_style "sm_measure_button_style" action Hide("sm_measure_screen")
    elif sm_measure_phase == 2:
        if sm_measure_result_vol - sm_measure_vol == 0:
            add "sm_measure_%s" % sm_measure_color at sm_measure_perfect_transform
        elif sm_measure_result_vol - sm_measure_vol > 3:
            add "sm_measure_%s" % sm_measure_color at sm_measure_way_over_transform
        elif sm_measure_result_vol - sm_measure_vol > 0:
            add "sm_measure_%s" % sm_measure_color at sm_measure_over_transform
        elif sm_measure_result_vol - sm_measure_vol > -4:
            add "sm_measure_%s" % sm_measure_color at sm_measure_under_transform
        else:
            add "sm_measure_%s" % sm_measure_color at sm_measure_way_under_transform
        vbox:
            xalign 0.8
            yalign 0.2
            text "{size=+%d}You measured{/size}" % (50 * persistent.scale_factor) style "sm_measure_style" xalign 0.5
            text "%s" % sm_measure_result_vol style "sm_measure_style_yellow" xalign 0.5
        hbox:
            xalign 0.9
            yalign 0.6
            spacing 80 * persistent.scale_factor
            textbutton "Ok" text_style "sm_measure_button_style" action (SetVariable("sm_vol_str",sm_measure_color), SetVariable("sm_measure_phase", 3),Hide("sm_measure_screen"))
            textbutton "Retry ({color=bb433b}-5 seconds{/color})" text_style "sm_measure_button_style" action (SetVariable("sm_time_penalty", sm_time_penalty+5.0), SetVariable("sm_measure_phase", 3),Show("sm_measure_bar_screen"))

    add "sm_measure_line"
transform sm_measure_under_transform:
    ypos 1080 * persistent.scale_factor
    ease 1.0 ypos 640 * persistent.scale_factor

transform sm_measure_over_transform:
    ypos 1080 * persistent.scale_factor
    ease 1.0 ypos 440 * persistent.scale_factor

transform sm_measure_way_under_transform:
    ypos 1080 * persistent.scale_factor
    ease 1.0 ypos 740 * persistent.scale_factor

transform sm_measure_way_over_transform:
    ypos 1080 * persistent.scale_factor
    ease 1.0 ypos 300 * persistent.scale_factor

transform sm_measure_perfect_transform:
    ypos 1080 * persistent.scale_factor
    ease 1.0 ypos 540 * persistent.scale_factor

transform sm_bar_movement:
    xpos 1801 * persistent.scale_factor
    ypos 940 * persistent.scale_factor
    linear 1 xpos 1801 * persistent.scale_factor ypos 55 * persistent.scale_factor
    linear 1 xpos 1801 * persistent.scale_factor ypos 940 * persistent.scale_factor

image sm_arrow_moving:
    "sm_power_bar"
    sm_bar_movement

screen sm_measure_bar_screen:
    tag sm_measure_bar_screen
    modal True
    imagebutton:
        idle "sm_bar"
        hover "sm_bar"
        action NullAction()
        xalign 0.98
        yalign 0.5

    add "sm_arrow_moving"

    default end_time2 = time.time() + 2
    default current_time2 = time.time()
    timer 0.05 repeat True action If(current_time2 < end_time2, true=SetScreenVariable('current_time2', time.time()), false=[Hide('sm_measure_bar_screen'),Function(sm_eval_measure,0),SetVariable("sm_measure_phase",2)])
    imagebutton:
        idle "sm_stop_idle"
        hover "sm_stop_hover"
        action (Hide('sm_measure_bar_screen'), Function(sm_eval_measure,max(end_time2-current_time2,0)),SetVariable("sm_measure_phase",2))
        xpos 1510 * persistent.scale_factor
        ypos 840 * persistent.scale_factor


init python:
    def sm_eval_measure(x):
        global sm_measure_result_vol
        global sm_measure_vol
        error = 0
        if x < 0.05:
            x = 0
        
        if x >= 1.9:
            error = -4
        elif x >= 1.77:
            error = -3
        elif x >= 1.60:
            error = -2
        elif x >= 1.46:
            error = 0
        elif x >= 1.25:
            error = 2
        elif x >= 1.19:
            error = 3
        elif x >= 0.92:
            error = 4
        elif x >= 0.80:
            error = 3
        elif x >= 0.61:
            error = 2
        elif x >= 0.48:
            error = 0
        elif x >= 0.29:
            error = -2
        elif x >= 0.16:
            error = -3
        else:
            error = -4
        sm_measure_result_vol = sm_measure_vol + error
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

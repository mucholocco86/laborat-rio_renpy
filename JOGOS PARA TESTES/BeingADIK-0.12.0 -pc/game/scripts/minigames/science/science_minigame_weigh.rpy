style sm_weigh_style:
    font "fonts/cabin-regular.ttf"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 37 * persistent.scale_factor
    text_align 0.5

style sm_weigh_digit_style:
    font "fonts/cabin-regular.ttf"
    color "#2d2d2d"
    size 70 * persistent.scale_factor

style sm_weigh_button_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    insensitive_color "#808080"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 200 * persistent.scale_factor

screen sm_weigh_screen:
    tag sm_weigh_screen
    modal True
    add "science_minigame_weigh"

    if sm_weigh_phase == 0:
        vbox:
            spacing 100 * persistent.scale_factor
            xalign 0.98 yalign 0.2
            text "Do you want to weigh a new chemical?\nAny chemical in this beaker will be discarded." style "sm_weigh_style" xalign 0.5
            hbox:
                xalign 0.5
                spacing 100 * persistent.scale_factor
                textbutton "Yes" text_style "sm_measure_button_style" action (Function(sm_discard_weigh,False),SetVariable("sm_weigh_phase", 1), SetVariable("sm_scale_str","full"))
                textbutton "Cancel" text_style "sm_measure_button_style" action Hide("sm_weigh_screen")
    elif sm_weigh_phase == 1:
        text "%s" % sm_weigh_result style "sm_weigh_digit_style" xalign 0.45 yalign 0.88
        vbox:
            xalign 0.85
            yalign 0.40
            text "{size=-%d}%s{/size}" % ((50 * persistent.scale_factor), sm_weigh_result) style "sm_measure_style_yellow" xalign 0.5 yoffset 220 * persistent.scale_factor
            hbox:
                spacing 300 * persistent.scale_factor
                textbutton "-" text_style "sm_weigh_button_style" action Function(sm_weigh_subtract)
                textbutton "+" text_style "sm_weigh_button_style" action Function(sm_weigh_add)
            textbutton "Ok" text_style "sm_measure_button_style" action If (sm_weigh_result > 0, Hide("sm_weigh_screen")) xalign 0.5 yoffset 20 * persistent.scale_factor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

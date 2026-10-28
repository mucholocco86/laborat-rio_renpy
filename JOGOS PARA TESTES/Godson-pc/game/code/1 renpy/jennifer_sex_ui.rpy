




default sex_ui_previous_quick_menu = True
default sex_ui_last_doggy_ready_slap = 0
default sex_ui_last_doggy_sex_slap = 0
default sex_ui_last_doggy_front_slap = 0
default sex_ui_last_neck_grab_slap = 0
default sex_ui_gallery_replay = False
default sex_ui_gallery_saved_makeout_count = 0

define sex_ui_hover_sound = "music/uihoversound2.wav"
define sex_ui_click_sound = "music/uiclicksound3.wav"
define sex_scene_dissolve = Dissolve(0.40)



define sex_ui_jennifer_intro_transition_time = 8.50
define sex_ui_jennifer_makeout_times = (14.041666, 14.041666, 14.041666, 13.666666)
define sex_ui_jennifer_position_time = 4.041666
define sex_ui_jennifer_reverse_position_time = 4.041666
define sex_ui_jennifer_upright_question_times = (6.541666, 9.333333, 8.25, 9.541666)
define sex_ui_jennifer_doggy_front_question_times = (6.583333,)



define sex_ui_question_return_lead = 1.0


define sex_ui_jennifer_doggy_ready_slap_return_times = (1.62, 1.78, 2.20, 2.00, 1.37, 1.53, 2.03, 1.91, 1.78, 2.25)
define sex_ui_jennifer_doggy_sex_slap_times = (8.208333, 6.583333, 9.333333, 8.958333)
define sex_ui_jennifer_doggy_front_slap_times = (5.083333, 9.666666)
define sex_ui_jennifer_neck_grab_slap_times = (4.916666, 4.041666)
define sex_ui_jennifer_ass_rub_time = 84.791664
define sex_ui_jennifer_cum_time = 29.75



define sex_ui_ready_slap_return_advance = 0.20


define sex_ui_slap_return_lead = 0.45


transform sex_ui_icon_motion:
    subpixel True
    on idle:
        xoffset 0
        alpha 0.96
        linear 0.14 alpha 1.0
    on hover:
        easeout 0.12 xoffset 12 alpha 1.0
    on insensitive:
        xoffset 0
        alpha 0.82
    on selected_idle:
        xoffset 7
        alpha 1.0
    on selected_hover:
        easeout 0.12 xoffset 12 alpha 1.0


transform sex_ui_primary_pulse:
    alpha 0.94
    zoom 1.0
    linear 0.75 alpha 1.0 zoom 1.035
    linear 0.75 alpha 0.94 zoom 1.0
    repeat


transform sex_ui_tooltip_reveal:
    on show:
        alpha 0.0
        xoffset -14
        easeout 0.12 alpha 1.0 xoffset 0
    on hide:
        easein 0.09 alpha 0.0 xoffset -8


style sex_ui_tooltip_frame is empty:
    background None
    xpadding 20
    ypadding 10

style sex_ui_tooltip_text is text:
    font gui.interface_text_font
    size 34
    color "#FFF0B2"
    outlines [(2, "#080405", 0, 0)]
    kerning 2

style sex_ui_tooltip_locked is text:
    font gui.interface_text_font
    size 18
    color "#A18D70"
    outlines [(1, "#080405", 0, 0)]
    kerning 2


screen sex_ui_icon_button(icon, label, action_value=None, enabled=True, selected=False, primary=False):
    $ icon_idle = "gui/sex_ui/%s.png" % icon
    $ icon_hover = "gui/sex_ui/%s_hover.png" % icon
    $ icon_locked = "gui/sex_ui/%s_locked.png" % icon

    fixed:
        xsize 620
        ysize 198

        if primary:
            fixed:
                xsize 212
                ysize 198
                at sex_ui_primary_pulse

                imagebutton:
                    idle Transform(icon_idle, xysize=(180, 180))
                    hover Transform(icon_hover, xysize=(198, 198))
                    insensitive Transform(icon_locked, xysize=(180, 180))
                    selected_idle Transform(icon_hover, xysize=(188, 188))
                    selected_hover Transform(icon_hover, xysize=(198, 198))
                    action action_value
                    sensitive enabled
                    selected selected
                    tooltip label
                    hover_sound sex_ui_hover_sound
                    activate_sound sex_ui_click_sound
                    focus_mask True
                    xalign 0.0
                    yalign 0.5
                    at sex_ui_icon_motion
        else:
            imagebutton:
                idle Transform(icon_idle, xysize=(180, 180))
                hover Transform(icon_hover, xysize=(198, 198))
                insensitive Transform(icon_locked, xysize=(180, 180))
                selected_idle Transform(icon_hover, xysize=(188, 188))
                selected_hover Transform(icon_hover, xysize=(198, 198))
                action action_value
                sensitive enabled
                selected selected
                tooltip label
                hover_sound sex_ui_hover_sound
                activate_sound sex_ui_click_sound
                focus_mask True
                xalign 0.0
                yalign 0.5
                at sex_ui_icon_motion

        if GetTooltip() == label:
            frame:
                style "sex_ui_tooltip_frame"
                xpos 216
                yalign 0.5
                at sex_ui_tooltip_reveal

                has hbox
                spacing 12

                text label:
                    style "sex_ui_tooltip_text"
                    yalign 0.5

                if not enabled:
                    text "LOCKED":
                        style "sex_ui_tooltip_locked"
                        yalign 0.56


screen sex_scene_controls(stage="intro", busy=False, auto_return=None):
    zorder 210

    $ upright_ready = stage == "upright_ready"
    $ upright_active = stage == "upright_active"
    $ upright_neck_grab = stage == "upright_neck_grab"
    $ doggy_ready = stage == "doggy_ready"
    $ doggy_rub = stage == "doggy_rub"
    $ doggy_active = stage == "doggy_active"
    $ doggy_front_active = stage == "doggy_front_active"
    $ sex_active = upright_active or upright_neck_grab or doggy_active or doggy_front_active
    $ doggy_stage = doggy_ready or doggy_active or doggy_front_active
    $ doggy_angle_one = doggy_ready or doggy_rub or doggy_active

    if auto_return is not None:
        timer auto_return action Return("clip_complete")



    frame:
        background None
        xpos 52
        yalign 0.5
        xsize 1500
        xpadding 0
        ypadding 0

        has vbox
        spacing 8

        if stage == "intro":
            use sex_ui_icon_button("start", "START", Return("start"), not busy, False, True)
        elif upright_ready or doggy_ready:
            use sex_ui_icon_button("penetrate", "PENETRATE", Return("penetrate"), not busy, False, True)
        elif sex_active and not upright_neck_grab:
            use sex_ui_icon_button("withdraw", "STOP PENETRATION", Return("withdraw"), not busy, False, True)
        else:
            use sex_ui_icon_button("penetrate", "PENETRATE", None, False, False, True)

        if doggy_stage or upright_neck_grab:
            use sex_ui_icon_button("slap", "SLAP", Return("butt_slap"), not busy)
        else:
            use sex_ui_icon_button("slap", "SLAP", None, False)

        if upright_active or upright_neck_grab:
            use sex_ui_icon_button("grab_neck", "GRAB NECK", Return("grab_neck"), not busy, upright_neck_grab)
        else:
            use sex_ui_icon_button("grab_neck", "GRAB NECK", None, False)

        if upright_ready and jennifer_makeout_count < 4:
            use sex_ui_icon_button("makeout", "MAKE OUT", Return("makeout"), not busy)
        else:
            use sex_ui_icon_button("makeout", "MAKE OUT", None, False)

        if upright_ready or upright_active or upright_neck_grab or doggy_angle_one:
            use sex_ui_icon_button("position", "CHANGE POSITION", Return("position"), not busy)
        else:
            use sex_ui_icon_button("position", "CHANGE POSITION", None, False)

        if upright_active:
            use sex_ui_icon_button("talk", "TALK", Return("talk"), not busy)
        elif doggy_front_active:
            use sex_ui_icon_button("talk", "TALK", Return("talk"), not busy)
        else:
            use sex_ui_icon_button("talk", "TALK", None, False)

        if doggy_ready or doggy_rub:
            use sex_ui_icon_button("rub", "RUB / MASSAGE", Return("rub"), not busy, doggy_rub)
        else:
            use sex_ui_icon_button("rub", "RUB / MASSAGE", None, False)

        use sex_ui_icon_button("spit", "SPIT", None, False)

        if doggy_active or doggy_front_active:
            use sex_ui_icon_button("camera", "CAMERA ANGLE", Return("camera"), not busy, doggy_front_active)
        else:
            use sex_ui_icon_button("camera", "CAMERA ANGLE", None, False)

        if doggy_active or doggy_front_active:
            use sex_ui_icon_button("finish", "FINISH", Return("finish"), not busy)
        else:
            use sex_ui_icon_button("finish", "FINISH", None, False)




screen jennifer_sex_controls(stage="intro"):
    use sex_scene_controls(stage=stage)


label jennifer_sex_scene:
    window hide
    $ sex_ui_previous_quick_menu = quick_menu
    $ quick_menu = False



    scene jenloop
    with slowfade
    jump sex_ui_jennifer_intro_controls


label jennifer_sex_gallery_replay:


    $ sex_ui_gallery_replay = True
    $ sex_ui_gallery_saved_makeout_count = jennifer_makeout_count
    $ jennifer_makeout_count = 0
    jump jennifer_sex_scene


label sex_ui_jennifer_intro_loop:
    scene jenloop
    with sex_scene_dissolve

label sex_ui_jennifer_intro_controls:
    call screen sex_scene_controls(stage="intro")

    if _return == "start":
        scene jentransition1
        with sex_scene_dissolve
        call screen sex_scene_controls(stage="intro", busy=True, auto_return=sex_ui_jennifer_intro_transition_time)
        scene jenloopbeforesex


        $ renpy.with_statement(sex_scene_dissolve, always=True)
        jump jennifer_sex_upright_ready

    jump sex_ui_jennifer_intro_loop


label jennifer_sex_upright_ready:
    call screen sex_scene_controls(stage="upright_ready")

    if _return == "makeout":
        jump jennifer_sex_makeout

    if _return == "penetrate":
        scene jenuprightsex
        with sex_scene_dissolve
        jump jennifer_sex_upright_active

    if _return == "position":
        jump jennifer_sex_change_position_ready

    jump jennifer_sex_upright_ready



label jennifer_sex_ready:
    jump jennifer_sex_upright_ready


label jennifer_sex_makeout:
    if jennifer_makeout_count == 0:
        $ jennifer_makeout_count = 1
        $ makeout_play_time = sex_ui_jennifer_makeout_times[0]
        scene jenmakeout1
        with sex_scene_dissolve

    elif jennifer_makeout_count == 1:
        $ jennifer_makeout_count = 2
        $ makeout_play_time = sex_ui_jennifer_makeout_times[1]
        scene jenmakeout2
        with sex_scene_dissolve

    elif jennifer_makeout_count == 2:
        $ jennifer_makeout_count = 3
        $ makeout_play_time = sex_ui_jennifer_makeout_times[2]
        scene jenmakeout3
        with sex_scene_dissolve
        if not sex_ui_gallery_replay:
            $ memory_jennifer_loves_makeout = True
            $ show_tooltip(n=46)

    elif jennifer_makeout_count == 3:
        $ jennifer_makeout_count = 4
        $ makeout_play_time = sex_ui_jennifer_makeout_times[3]
        scene jenmakeout4
        with sex_scene_dissolve
        if not sex_ui_gallery_replay:
            $ memory_jennifer_thinks_you_love_her = True
            $ show_tooltip(n=47)


    call screen sex_scene_controls(stage="upright_ready", busy=True, auto_return=makeout_play_time)

    scene jenloopbeforesex
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_upright_ready


label jennifer_sex_upright_active:
    call screen sex_scene_controls(stage="upright_active")

    if _return == "withdraw":
        scene jenloopbeforesex
        $ renpy.with_statement(sex_scene_dissolve, always=True)
        jump jennifer_sex_upright_ready

    if _return == "talk":
        jump jennifer_sex_upright_talk

    if _return == "grab_neck":
        scene jensexgrabneck
        with sex_scene_dissolve
        jump jennifer_sex_upright_neck_grab

    if _return == "position":
        jump jennifer_sex_change_position_active

    jump jennifer_sex_upright_active


label jennifer_sex_upright_neck_grab:
    call screen sex_scene_controls(stage="upright_neck_grab")

    if _return == "grab_neck":
        scene jenuprightsex
        $ renpy.with_statement(sex_scene_dissolve, always=True)
        jump jennifer_sex_upright_active

    if _return == "butt_slap":
        jump jennifer_sex_upright_neck_grab_slap

    if _return == "position":
        jump jennifer_sex_change_position_neck_grab

    jump jennifer_sex_upright_neck_grab


label jennifer_sex_upright_neck_grab_slap:
    $ sex_ui_last_neck_grab_slap = 2 if sex_ui_last_neck_grab_slap == 1 else 1
    $ neck_grab_slap_image = "jensexgrabneckslap%d" % sex_ui_last_neck_grab_slap
    $ neck_grab_slap_time = max(0.05, sex_ui_jennifer_neck_grab_slap_times[sex_ui_last_neck_grab_slap - 1] - sex_ui_slap_return_lead)

    scene expression neck_grab_slap_image
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="upright_neck_grab", busy=True, auto_return=neck_grab_slap_time)

    scene jensexgrabneck
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    hide screen sex_scene_controls
    jump jennifer_sex_upright_neck_grab



label jennifer_sex_active:
    jump jennifer_sex_upright_active


label jennifer_sex_upright_talk:

    show screen sex_scene_controls(stage="upright_active", busy=True)

    menu:
        "You're just a dumb college slut!":
            $ upright_question_image = "jenquestion1collegeslut"
            $ upright_question_time = max(0.05, sex_ui_jennifer_upright_question_times[0] - sex_ui_question_return_lead)
        "Stupid two-dollar bitch!!":

            $ upright_question_image = "jenquestion2twodollars"
            $ upright_question_time = max(0.05, sex_ui_jennifer_upright_question_times[1] - sex_ui_question_return_lead)
        "God Mommy, you're such a fucking whore!":

            $ upright_question_image = "jenquestion3fuckingwhore"
            $ upright_question_time = max(0.05, sex_ui_jennifer_upright_question_times[2] - sex_ui_question_return_lead)
        "You know, you're just like your mother.":

            $ upright_question_image = "jenquestion4justlikeyourmother"
            $ upright_question_time = max(0.05, sex_ui_jennifer_upright_question_times[3] - sex_ui_question_return_lead)
        "Return":

            hide screen sex_scene_controls
            jump jennifer_sex_upright_active

    scene expression upright_question_image
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="upright_active", busy=True, auto_return=upright_question_time)

    scene jenuprightsex
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    hide screen sex_scene_controls
    jump jennifer_sex_upright_active


label jennifer_sex_change_position_ready:
    scene jenuprighttranz
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="upright_ready", busy=True, auto_return=sex_ui_jennifer_position_time)
    scene jendoggyloop
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_doggy_ready


label jennifer_sex_change_position_active:
    scene jenuprighttranz
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="upright_active", busy=True, auto_return=sex_ui_jennifer_position_time)
    scene jendoggyloop
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_doggy_ready


label jennifer_sex_change_position_neck_grab:
    scene jenuprighttranz
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="upright_neck_grab", busy=True, auto_return=sex_ui_jennifer_position_time)
    scene jendoggyloop
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_doggy_ready


label jennifer_sex_doggy_ready:
    call screen sex_scene_controls(stage="doggy_ready")

    if _return == "penetrate":
        scene jenniferdoggysex
        with sex_scene_dissolve
        jump jennifer_sex_doggy_active

    if _return == "butt_slap":
        jump jennifer_sex_doggy_ready_butt_slap

    if _return == "rub":
        jump jennifer_sex_doggy_ass_rub

    if _return == "position":
        $ doggy_reverse_stage = "doggy_ready"
        jump jennifer_sex_change_position_to_upright

    jump jennifer_sex_doggy_ready


label jennifer_sex_doggy_ready_butt_slap:
    $ ready_slap_choices = [i for i in range(1, 11) if i != sex_ui_last_doggy_ready_slap]
    $ sex_ui_last_doggy_ready_slap = renpy.random.choice(ready_slap_choices)
    $ ready_slap_image = "slap%d" % sex_ui_last_doggy_ready_slap
    $ ready_slap_time = max(0.05, sex_ui_jennifer_doggy_ready_slap_return_times[sex_ui_last_doggy_ready_slap - 1] - sex_ui_ready_slap_return_advance)

    scene expression ready_slap_image
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="doggy_ready", busy=True, auto_return=ready_slap_time)

    scene jendoggyloop
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_doggy_ready


label jennifer_sex_doggy_active:
    call screen sex_scene_controls(stage="doggy_active")

    if _return == "withdraw":
        scene jendoggyloop
        $ renpy.with_statement(sex_scene_dissolve, always=True)
        jump jennifer_sex_doggy_ready

    if _return == "butt_slap":
        jump jennifer_sex_doggy_sex_butt_slap

    if _return == "camera":
        scene jenfrontviewsex
        with sex_scene_dissolve
        jump jennifer_sex_doggy_front_active

    if _return == "position":
        $ doggy_reverse_stage = "doggy_active"
        jump jennifer_sex_change_position_to_upright

    if _return == "finish":
        jump jennifer_sex_end

    jump jennifer_sex_doggy_active


label jennifer_sex_doggy_sex_butt_slap:
    $ sex_slap_choices = [i for i in range(1, 5) if i != sex_ui_last_doggy_sex_slap]
    $ sex_ui_last_doggy_sex_slap = renpy.random.choice(sex_slap_choices)
    $ sex_slap_image = "jensexslap%d" % sex_ui_last_doggy_sex_slap
    $ sex_slap_time = max(0.05, sex_ui_jennifer_doggy_sex_slap_times[sex_ui_last_doggy_sex_slap - 1] - sex_ui_slap_return_lead)

    scene expression sex_slap_image
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="doggy_active", busy=True, auto_return=sex_slap_time)

    scene jenniferdoggysex
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    hide screen sex_scene_controls
    jump jennifer_sex_doggy_active


label jennifer_sex_doggy_ass_rub:
    scene jenassrub
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="doggy_rub")

    if _return == "position":
        $ doggy_reverse_stage = "doggy_rub"
        jump jennifer_sex_change_position_to_upright

    scene jendoggyloop
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_doggy_ready


label jennifer_sex_change_position_to_upright:
    scene jendoggytranz
    with sex_scene_dissolve
    call screen sex_scene_controls(stage=doggy_reverse_stage, busy=True, auto_return=sex_ui_jennifer_reverse_position_time)

    scene jenloopbeforesex
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    jump jennifer_sex_upright_ready


label jennifer_sex_doggy_front_active:
    call screen sex_scene_controls(stage="doggy_front_active")

    if _return == "withdraw":
        scene jendoggyloop
        $ renpy.with_statement(sex_scene_dissolve, always=True)
        jump jennifer_sex_doggy_ready

    if _return == "butt_slap":
        jump jennifer_sex_doggy_front_butt_slap

    if _return == "camera":
        scene jenniferdoggysex
        $ renpy.with_statement(sex_scene_dissolve, always=True)
        jump jennifer_sex_doggy_active

    if _return == "talk":
        jump jennifer_sex_doggy_front_talk

    if _return == "finish":
        jump jennifer_sex_end

    jump jennifer_sex_doggy_front_active


label jennifer_sex_doggy_front_butt_slap:
    $ front_slap_choices = [i for i in range(1, 3) if i != sex_ui_last_doggy_front_slap]
    $ sex_ui_last_doggy_front_slap = renpy.random.choice(front_slap_choices)

    if sex_ui_last_doggy_front_slap == 1:
        $ front_slap_image = "jensexslapangle2"
    else:
        $ front_slap_image = "jensexslapangle2_alt"

    $ front_slap_time = max(0.05, sex_ui_jennifer_doggy_front_slap_times[sex_ui_last_doggy_front_slap - 1] - sex_ui_slap_return_lead)

    scene expression front_slap_image
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="doggy_front_active", busy=True, auto_return=front_slap_time)

    scene jenfrontviewsex
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    hide screen sex_scene_controls
    jump jennifer_sex_doggy_front_active


label jennifer_sex_doggy_front_talk:

    show screen sex_scene_controls(stage="doggy_front_active", busy=True)

    menu:
        "This is my pussy now!":
            $ doggy_question_image = "jendoggyquestion2"
            $ doggy_question_time = max(0.05, sex_ui_jennifer_doggy_front_question_times[0] - sex_ui_question_return_lead)
        "Return":

            hide screen sex_scene_controls
            jump jennifer_sex_doggy_front_active

    scene expression doggy_question_image
    with sex_scene_dissolve
    call screen sex_scene_controls(stage="doggy_front_active", busy=True, auto_return=doggy_question_time)

    scene jenfrontviewsex
    $ renpy.with_statement(sex_scene_dissolve, always=True)
    hide screen sex_scene_controls
    jump jennifer_sex_doggy_front_active


label jennifer_sex_end:
    scene jennifercum
    with sex_scene_dissolve
    pause sex_ui_jennifer_cum_time

    scene black
    with slowfade

    $ quick_menu = sex_ui_previous_quick_menu
    window auto

    if sex_ui_gallery_replay:
        $ jennifer_makeout_count = sex_ui_gallery_saved_makeout_count
        $ sex_ui_gallery_replay = False
        return

    jump marnie2nd
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

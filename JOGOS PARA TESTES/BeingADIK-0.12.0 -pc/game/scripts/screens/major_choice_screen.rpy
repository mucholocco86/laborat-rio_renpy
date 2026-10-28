screen major_choice_screen:
    tag major_choice_screen
    modal True
    add "major_choices_blur"
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg_short"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "Affinity: {font=fonts/collegiate.ttf}[affinity]{/font}" style "score_new_style" at show_hide_dissolve:
        xalign 0.97
        yalign 0.01

    hbox:
        xalign 0.5
        yalign 0.868
        spacing 50 * persistent.scale_factor
        imagebutton at show_hide_dissolve:
            if affinity == "DIK" or (affinity == "NEUTRAL" and mc_info[6]):
                idle "mc_dik_idle"
                hover "mc_dik_hover"
                action (Function(addCPenalty),Hide("major_choice_screen"),Jump(mc_info[1]))
            else:
                idle "mc_dik_disabled"
                hover "mc_dik_disabled"
                action NullAction()
        imagebutton at show_hide_dissolve:
            idle "mc_neutral_idle"
            hover "mc_neutral_hover"
            action (Function(addNPenalty),Hide("major_choice_screen"),Jump(mc_info[3]))
        imagebutton at show_hide_dissolve:
            if affinity == "CHICK" or (affinity == "NEUTRAL" and not mc_info[6]):
                idle "mc_chick_idle"
                hover "mc_chick_hover"
                action (Function(addDPenalty),Hide("major_choice_screen"),Jump(mc_info[5]))
            else:
                idle "mc_chick_disabled"
                hover "mc_chick_disabled"
                action NullAction()

    hbox:
        xalign 0.5
        yalign 0.868
        spacing 50 * persistent.scale_factor
        xoffset 110 * persistent.scale_factor
        yoffset 35 * persistent.scale_factor
        hbox:
            xminimum 598 * persistent.scale_factor
            xmaximum 598 * persistent.scale_factor
            yminimum 127 * persistent.scale_factor
            ymaximum 127 * persistent.scale_factor
            if affinity == "DIK" or (affinity == "NEUTRAL" and mc_info[6]):
                text mc_info[0] style "mc_choice_dik_style" at show_hide_dissolve
            else:
                text mc_info[0] style "mc_choice_disabled_style" at show_hide_dissolve
        hbox:
            xminimum 598 * persistent.scale_factor
            xmaximum 598 * persistent.scale_factor
            yminimum 127 * persistent.scale_factor
            ymaximum 127 * persistent.scale_factor
            text mc_info[2] style "mc_choice_neutral_style" at show_hide_dissolve
        hbox:
            xminimum 598 * persistent.scale_factor
            xmaximum 598 * persistent.scale_factor
            yminimum 127 * persistent.scale_factor
            ymaximum 127 * persistent.scale_factor
            if affinity == "CHICK" or (affinity == "NEUTRAL" and not mc_info[6]):
                text mc_info[4] style "mc_choice_chick_style" at show_hide_dissolve
            else:
                text mc_info[4] style "mc_choice_disabled_style" at show_hide_dissolve

style mc_choice_dik_style:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#ffc27b"
    outlines [(2, "#000000", 0, 0)]

style mc_choice_neutral_style:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#22d431"
    outlines [(2, "#000000", 0, 0)]

style mc_choice_chick_style:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#0f99bf"
    outlines [(2, "#000000", 0, 0)]

style mc_choice_disabled_style:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#494949"
    outlines [(2, "#ffffff", 0, 0)]

image major_choices_blur:
    "major_choices_blur_fr0" with Dissolve(1, alpha=True)
    pause 1
    "major_choices_blur_fr1" with Dissolve(1, alpha=True)
    pause 1
    "major_choices_blur_fr2" with Dissolve(1, alpha=True)
    pause 1
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

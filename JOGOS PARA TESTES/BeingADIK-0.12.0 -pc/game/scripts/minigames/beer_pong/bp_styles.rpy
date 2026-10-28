style bp_ap_style:
    font "fonts/cabin-regular.ttf"
    size 30 * persistent.scale_factor
    color "#fe9416"
    outlines [(2, "#000000", 0, 0)]
style bp_tut_style:
    font "fonts/cabin-regular.ttf"
    size 30 * persistent.scale_factor
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]
    xalign 0.5
    text_align 0.5

style bp_choice_style:
    font "fonts/cabin-regular.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

style bp_cpu_box_style:
    font "fonts/cabin-regular.ttf"
    size 24 * persistent.scale_factor
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]
style bp_action_msg_style:
    font "fonts/cabin-regular.ttf"
    size 30 * persistent.scale_factor
    color "#ffe059"
    outlines [(2, "#000000", 0, 0)]
    xalign 1.0

transform bp_go_transform:
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    repeat

transform bp_dissolve:
    alpha 0.0
    easein 0.2 alpha 1.0

style bp_go_style:
    font "fonts/ApeMount.ttf"
    color "#ff0000"
    size 200 * persistent.scale_factor
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style say_label_bp_style:
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    font "fonts/Redressed.ttf"
    size 56 * persistent.scale_factor
    xpos 360 * persistent.scale_factor
    ypos 70 * persistent.scale_factor

style say_dialogue_bp_style:
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    color "#FFFFFF"
    font "fonts/Audrey-Bold.otf"
    size 33 * persistent.scale_factor
    xpos 402 * persistent.scale_factor
    ypos 70 * persistent.scale_factor

style bp_nm_idle_style:
    font "fonts/Audrey-Bold.otf"
    size 30 * persistent.scale_factor
    color "#ffcc66"

    yoffset 5 * persistent.scale_factor
    xoffset 55 * persistent.scale_factor
    outlines [(1, "#330000", 0, 0)]

    drop_shadow [(2, 2)]
    drop_shadow_color "#663300"

style bp_nm_hover_style:
    font "fonts/Audrey-Bold.otf"
    size 30 * persistent.scale_factor
    color "#ffffff"

    yoffset 5 * persistent.scale_factor
    xoffset 55 * persistent.scale_factor
    outlines [(1, "#660066", 0, 0)]

    drop_shadow [(2, 2)]
    drop_shadow_color "#663300"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

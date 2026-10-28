style math_main_style:
    font "fonts/candara.ttf"
    size 50 * persistent.scale_factor
    color "#ffffff"
    outlines [(4, "#101119", 0, 0)]

style math_task_style:
    font "fonts/candara.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"
    outlines [(4, "#101119", 0, 0)]

style math_task2_style:
    font "fonts/candara.ttf"
    xalign 0.5
    text_align 0.5
    size 40 * persistent.scale_factor
    color "#ffffff"
    outlines [(4, "#101119", 0, 0)]

style math_task_res_style:
    font "fonts/candara.ttf"
    xalign 0.5
    size 190 * persistent.scale_factor
    color "#ffffff"
    outlines [(4, "#101119", 0, 0)]

style math_button_style:
    font "fonts/candara.ttf"
    size 50 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"
    outlines [(4, "#101119", 0, 0)]

style math_button_disabled_style:
    font "fonts/candara.ttf"
    size 50 * persistent.scale_factor
    color "#9d9d9d"
    outlines [(4, "#101119", 0, 0)]

image math_bomb_img:
    "math_tile_bomb"
    pause 0.7
    "math_tile_crack" with Dissolve(0.4, alpha=True)

transform math_tt_transform:
    on show:
        alpha 0.0
        easein 0.5 alpha 1.0
    on hide:
        alpha 1.0
        easein 0.5 alpha 0.0

transform math_tut_flash:
    alpha 0.0
    easein 1.0 alpha 1.0
    easein 1.0 alpha 0.0
    repeat

style math_tt_style:
    font "fonts/cabin-regular.ttf"
    size 25 * persistent.scale_factor
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]
    text_align 0.5
    xminimum 780 * persistent.scale_factor
    xmaximum 780 * persistent.scale_factor
    yminimum 100 * persistent.scale_factor
    ymaximum 100 * persistent.scale_factor

style math_tut_style:
    font "fonts/cabin-regular.ttf"
    size 35 * persistent.scale_factor
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    text_align 0.5
    xminimum 1130 * persistent.scale_factor
    xmaximum 1130 * persistent.scale_factor
    yminimum 120 * persistent.scale_factor
    ymaximum 120 * persistent.scale_factor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

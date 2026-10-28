style app_pack_quest_task_text_style2:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(1), "#000", absolute(1), absolute(1)) ]

style app_pack_quest_task_text_style3:
    font "fonts/candara.ttf"
    size 17 * persistent.scale_factor
    color "#ffffff"
    text_align 0.5
    xalign 0.5

transform app_pack_quest_resize:
    zoom 0.6
    alpha 0.0
    easein 2.0 alpha 1.0

transform app_pack_quest_text_fade_anim:
    zoom 0.7
    alpha 0.0
    easein 2.0 alpha 1.0

transform app_pack_quest_text_anim2:
    easein 1.0 xpos 960

style app_pack_quest_opening_text_style:
    font "fonts/candara.ttf"
    size 30 * persistent.scale_factor
    color "#fe9416"
    outlines [(2, "#000000", 0, 0)]

style pack_quest_big_text_style:
    font "fonts/cabin-regular.ttf"
    size 125 * persistent.scale_factor
    color "#fe9416"

style pack_quest_task_text_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#ffffff"

style pack_quest_task_text_style2:
    font "fonts/cabin-regular.ttf"
    size 35 * persistent.scale_factor
    color "#ffffff"

style pack_quest_found_button_style:
    font "fonts/cabin-regular.ttf"
    size 100 * persistent.scale_factor
    color "#fe9416"
    outlines [(2, "#ffffff", 0, 0)]

style pack_quest_opening_text_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#fe9416"
    outlines [(2, "#000000", 0, 0)]

transform pack_quest_text_anim:
    choice:
        easein 1.0 xpos -2000 * persistent.scale_factor
    choice:
        easein 0.9 xpos -2000 * persistent.scale_factor
    choice:
        easein 0.8 xpos -2000 * persistent.scale_factor
    choice:
        easein 0.7 xpos -2000 * persistent.scale_factor
    choice:
        easein 0.6 xpos -2000 * persistent.scale_factor
    choice:
        easein 0.5 xpos -2000 * persistent.scale_factor
    choice:
        easein 0.4 xpos -2000 * persistent.scale_factor

transform pack_quest_text_anim2:
    easein 1.0 xpos -1000 * persistent.scale_factor

transform pack_quest_text_fade_anim:
    alpha 0.0
    easein 2.0 alpha 1.0

transform pack_quest_text_anim_found_button:
    easein 0.5 xpos -1000 * persistent.scale_factor
    easein 2.0 xpos -1100 * persistent.scale_factor
    easein 0.5 xpos -3000 * persistent.scale_factor

transform pack_quest_line_anim_found_button:
    easein 1.0 xpos -3200 * persistent.scale_factor
    easein 0.5 xpos -3300 * persistent.scale_factor
    easein 0.5 xpos -3200 * persistent.scale_factor
    easein 1.0 xpos -6000 * persistent.scale_factor

transform pack_quest_line_anim_found_button2:
    easein 1.0 xpos 2700 * persistent.scale_factor
    easein 0.5 xpos 2800 * persistent.scale_factor
    easein 0.5 xpos 2700 * persistent.scale_factor
    easein 1.0 xpos 6000 * persistent.scale_factor


transform pack_quest_resize:
    zoom 0.7
    alpha 0.0
    easein 2.0 alpha 1.0

transform pack_quest_open_anim:
    zoom 0.7
    alpha 0.0
    easein 1.0 alpha 1.0
    linear 0.1 xpos 295 * persistent.scale_factor
    linear 0.1 xpos 281 * persistent.scale_factor
    linear 0.1 xpos 293 * persistent.scale_factor
    linear 0.1 xpos 283 * persistent.scale_factor
    linear 0.1 xpos 290 * persistent.scale_factor
    linear 0.1 xpos 286 * persistent.scale_factor
    linear 0.1 xpos 291 * persistent.scale_factor
    linear 0.1 xpos 287 * persistent.scale_factor
    linear 0.1 xpos 288 * persistent.scale_factor
    pause 0.5
    linear 0.1 xpos 303 * persistent.scale_factor
    linear 0.1 xpos 273 * persistent.scale_factor
    linear 0.1 xpos 298 * persistent.scale_factor
    linear 0.1 xpos 278 * persistent.scale_factor
    linear 0.1 xpos 294 * persistent.scale_factor
    linear 0.1 xpos 282 * persistent.scale_factor
    linear 0.1 xpos 291 * persistent.scale_factor
    linear 0.1 xpos 287 * persistent.scale_factor
    linear 0.1 xpos 288 * persistent.scale_factor
    pause 0.5
    linear 0.1 xpos 291 * persistent.scale_factor
    linear 0.1 xpos 287 * persistent.scale_factor
    linear 0.1 xpos 294 * persistent.scale_factor
    linear 0.1 xpos 282 * persistent.scale_factor
    linear 0.1 xpos 298 * persistent.scale_factor
    linear 0.1 xpos 278 * persistent.scale_factor
    linear 0.1 xpos 304 * persistent.scale_factor
    linear 0.1 xpos 272 * persistent.scale_factor
    linear 0.1 xpos 312 * persistent.scale_factor
    linear 0.1 xpos 264 * persistent.scale_factor
    linear 0.1 xpos 322 * persistent.scale_factor
    linear 0.1 xpos 254 * persistent.scale_factor
    linear 0.1 xpos 336 * persistent.scale_factor
    linear 0.1 xpos 240 * persistent.scale_factor
    linear 0.1 xpos 288 * persistent.scale_factor
    linear 0.5 alpha 0.0

transform pack_quest_open_sparkle_anim:
    alpha 0.0
    pause 5.0
    linear 0.5 alpha 1.0
    linear 1.0 alpha 0.5
    linear 2.5 alpha 0.0

transform pack_quest_open_sparkle_anim2:
    alpha 0.0
    pause 5.1
    linear 0.5 alpha 0.7
    linear 0.5 alpha 0.5
    linear 2.5 alpha 0.0

transform pack_quest_open_img1_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 171 * persistent.scale_factor ypos 300 * persistent.scale_factor

transform pack_quest_open_img2_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 608 * persistent.scale_factor ypos 300 * persistent.scale_factor

transform pack_quest_open_img3_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 1045 * persistent.scale_factor ypos 300 * persistent.scale_factor

transform pack_quest_open_img4_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 1482 * persistent.scale_factor ypos 300 * persistent.scale_factor

transform pack_quest_open_img5_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 171 * persistent.scale_factor ypos 600 * persistent.scale_factor

transform pack_quest_open_img6_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 608 * persistent.scale_factor ypos 600 * persistent.scale_factor

transform pack_quest_open_img7_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 1045 * persistent.scale_factor ypos 600 * persistent.scale_factor

transform pack_quest_open_img8_anim:
    alpha 0.0
    pause 5.2
    alpha 1.0
    easeout 0.5 xpos 960 * persistent.scale_factor ypos 400 * persistent.scale_factor
    easeout 0.5 xpos 1482 * persistent.scale_factor ypos 600 * persistent.scale_factor

transform pack_quest_open_x_anim:
    alpha 0.0
    xpos 2500 * persistent.scale_factor
    pause 7
    linear 1.0 xpos 1800 * persistent.scale_factor
    alpha 1.0

transform pack_quest_opening_text_anim:
    pause 3
    linear 1 alpha 0.0

transform pack_quest_opening_text_anim2:
    alpha 0.0
    pause 5.2
    linear 1 alpha 1.0

transform pack_quest_open_img_twinkle_anim:
    alpha 0.0
    pause 7.2
    choice:
        pause 0.0
    choice:
        pause 0.5
    choice:
        pause 1.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 4.0
    choice:
        pause 5.0
    choice:
        pause 5.5
    choice:
        pause 6.0
    choice:
        pause 6.5
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat


image pack_quest_pack_no_crp_idle:
    "pack_quest_crp_no" with Dissolve(1.5, alpha=True)
    pause 1.5
    "pack_quest_crp_nob" with Dissolve(1.5, alpha=True)
    pause 1.5
    repeat

image pack_quest_turn_in_button_idle:
    "pack_quest_turn_in_button_idle_fr0" with Dissolve(1.5, alpha=True)
    pause 1.5
    "pack_quest_turn_in_button_idle_fr1" with Dissolve(1.5, alpha=True)
    pause 1.5
    repeat

image pack_quest_turn_in_button_hover:
    "pack_quest_turn_in_button_hover_fr0" with Dissolve(1.5, alpha=True)
    pause 1.5
    "pack_quest_turn_in_button_hover_fr1" with Dissolve(1.5, alpha=True)
    pause 1.5
    repeat

image pack_quest_start_quest_idle:
    "pack_quest_start_quest_idle_fr0" with Dissolve(1.5, alpha=True)
    pause 1.5
    "pack_quest_start_quest_idle_fr1" with Dissolve(1.5, alpha=True)
    pause 1.5
    repeat

image pack_quest_start_quest_hover:
    "pack_quest_start_quest_hover_fr0" with Dissolve(1.5, alpha=True)
    pause 1.5
    "pack_quest_start_quest_hover_fr1" with Dissolve(1.5, alpha=True)
    pause 1.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

style brawler_record_style:
    font "fonts/centurygothicregular.ttf"
    size 25 * persistent.scale_factor
    color "#ffe059"

style brawler_menu_diff_style:
    font "fonts/centurygothicbold.ttf"
    size 30 * persistent.scale_factor
    hover_color "#fe9416"
    outlines [ (absolute(1), "#2d2d2d", absolute(1), absolute(1)) ]

style brawler_tut_text_style:
    font "fonts/centurygothicbold.ttf"
    size 25 * persistent.scale_factor
    outlines [ (absolute(1), "#090909", absolute(1), absolute(1)) ]

style brawler_tut_text3_style:
    font "fonts/centurygothicbold.ttf"
    text_align 0.5
    size 25 * persistent.scale_factor
    outlines [ (absolute(1), "#090909", absolute(1), absolute(1)) ]

style brawler_tut_text2_style:
    font "fonts/centurygothicbold.ttf"
    text_align 0.5
    size 20 * persistent.scale_factor
    outlines [ (absolute(1), "#090909", absolute(1), absolute(1)) ]

style brawler_opp_style:
    font "fonts/centurygothicbold.ttf"
    size 30 * persistent.scale_factor

style brawler_menu_text_selected_style:
    font "fonts/centurygothicbold.ttf"
    size 50 * persistent.scale_factor
    color "#262626"
    outlines [ (absolute(2), "#ffc27b", absolute(1), absolute(1)) ]

style brawler_skill_tt_style:
    font "fonts/centurygothicbold.ttf"
    size 20 * persistent.scale_factor
    outlines [ (absolute(2), "#090909", absolute(1), absolute(1)) ]

style brawler_skill_header_style:
    font "fonts/centurygothicbold.ttf"
    size 70 * persistent.scale_factor
    color "#ffe059"

style brawler_skill_reset_style:
    font "fonts/centurygothicbold.ttf"
    size 30 * persistent.scale_factor
    color "#ff5959"
    hover_color "#e10d00"

style brawler_skill_text_style:
    font "fonts/centurygothicbold.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"
style brawler_skill_text_btn_style:
    font "fonts/centurygothicbold.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"

style brawler_menu_text_style:
    font "fonts/centurygothicbold.ttf"
    size 50 * persistent.scale_factor
    color "#f3f3f3"
    outlines [ (absolute(2), "#1b1c21", absolute(1), absolute(1)) ]

style brawler_arrow_text_style:
    font "fonts/cabin-regular.ttf"
    size 30 * persistent.scale_factor
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style brawler_rage_text_style:
    font "fonts/cabin-regular.ttf"
    color "#2d2d2d"
    size 30 * persistent.scale_factor
    outlines [ (absolute(2), "#ffffff", absolute(1), absolute(1)) ]

style brawler_skill_x_style:
    font "fonts/ApeMount.ttf"
    color "#e2e2e2"
    hover_color "#ffe059"
    size 150 * persistent.scale_factor

style brawler_rage_text2_style:
    font "fonts/ApeMount.ttf"
    color "#ffffff"
    size 200 * persistent.scale_factor
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style brawler_go_style:
    font "fonts/ApeMount.ttf"
    color "#ff0000"
    size 200 * persistent.scale_factor
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style brawler_counter_text_style:
    font "fonts/ApeMount.ttf"
    color "#fe9416"
    size 80 * persistent.scale_factor
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style brawler_result_text_style:
    font "fonts/ApeMount.ttf"
    color "#bb433b"
    size 100 * persistent.scale_factor

style bn_name_style:
    font "fonts/cabin-regular.ttf"
    size 25 * persistent.scale_factor
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style brawler_dwy_tut_style:
    font "fonts/centurygothicbold.ttf"
    size 25 * persistent.scale_factor
    color "#ffe059"
    outlines [ (absolute(3), "#090909", absolute(1), absolute(1)) ]


image brawler_rage_text:
    "rage_fr0" with Dissolve(0.5, alpha=True)
    pause 0.5
    "rage_fr1" with Dissolve(0.5, alpha=True)
    repeat

transform brawler_rage_zoom:
    zoom 1.0
    easein 1.0 zoom 1.07
    easein 1.0 zoom 1.0
    repeat
transform brawler_ready_zoom:
    zoom 0.0
    easein 0.2 zoom 1.0

transform brawler_rage_zoom2:
    zoom 1.0
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    repeat

transform bn_go_transform:
    easein 0.2 zoom 1.07
    easein 0.2 zoom 1.05
    repeat

init -5 python:
    style.rage_bar_style = Style(style.default)
    style.rage_bar_style.left_bar = Frame("[persistent.img_dir]/minigames/brawler/displayables/brawler_bar1.png", 0, 0)
    style.rage_bar_style.right_bar = Frame("[persistent.img_dir]/minigames/brawler/displayables/brawler_bar2.png", 0, 0)
    style.rage_bar_style.ymaximum = 20 * persistent.scale_factor 

transform bn_line_transform:
    xpos 0
    linear 10 xpos -1920 * persistent.scale_factor
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

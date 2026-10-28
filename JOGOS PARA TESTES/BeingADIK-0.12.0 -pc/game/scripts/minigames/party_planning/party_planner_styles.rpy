init -1 python:
    def play_pp_s_rank(trans, st, at):
        renpy.play("sound_effects/interlude/paint_bling.mp3","sfx2")

style pp_eval_style:
    font "fonts/cabin-regular.ttf"
    color "#ffffff"
    size 35 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

transform pp_s_rank_transform:
    function play_pp_s_rank
    alpha 0.0
    ease 0.1 alpha 1.0

transform pp_rank_transform:
    alpha 0.0
    ease 0.1 alpha 1.0

style pp_activity_number_style:
    font "fonts/collegiate.ttf"
    size 60 * persistent.scale_factor
    color "#fe9416"
    xalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_tut_text_style:
    font "fonts/candara.ttf"
    xmaximum 800 * persistent.scale_factor
    xminimum 800 * persistent.scale_factor
    size 34 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
    text_align 0.5

style pp_header_style:
    font "fonts/candara.ttf"
    size 50 * persistent.scale_factor
    color "#ffc27b"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_header_tut_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_icon_style:
    font "fonts/candara.ttf"
    size 20 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_stat_style:
    font "fonts/candara.ttf"
    size 35 * persistent.scale_factor
    xalign 0.0
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_stat_text_style:
    font "fonts/candara.ttf"
    size 35 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_activity_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    xalign 0.5
    hover_color "#fe9416"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_activity_style_disabled:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    xalign 0.5
    color "#8f8f8f"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_activity_selected_style:
    font "fonts/candara.ttf"
    color "#ffed00"
    size 25 * persistent.scale_factor
    xalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_buy_style:
    font "fonts/candara.ttf"
    color "#ffffff"
    hover_color "#00ff00"
    size 35 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_icon_selected_style:
    font "fonts/candara.ttf"
    color "#fe9416"
    size 20 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_criteria_not_met_style:
    font "fonts/candara.ttf"
    color "#ff0000"
    size 50 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_criteria_met_style:
    font "fonts/candara.ttf"
    color "#00ff00"
    size 50 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_info_happiness_style:
    font "fonts/candara.ttf"
    color "#ffffff"
    size 30 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

transform pp_happiness_zoom:
    zoom 0.8

style pp_perk_continue_style:
    font "fonts/candara.ttf"
    idle_color "#ffffff"
    hover_color "#fe9416"
    insensitive_color "#4e4d4d"
    size 80 * persistent.scale_factor
    xalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_perk_style_big:
    font "fonts/candara.ttf"
    color "#ffed00"
    size 80 * persistent.scale_factor
    xalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_perk_style:
    font "fonts/candara.ttf"
    color "#ffffff"
    size 50 * persistent.scale_factor
    xalign 0.5
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_perk_item_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_perk_item_selected_style:
    font "fonts/candara.ttf"
    size 25 * persistent.scale_factor
    color "1df400"
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]

style pp_perks_header_style:
    font "fonts/candara.ttf"
    size 30 * persistent.scale_factor
    outlines [ (absolute(2), "#000", absolute(1), absolute(1)) ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

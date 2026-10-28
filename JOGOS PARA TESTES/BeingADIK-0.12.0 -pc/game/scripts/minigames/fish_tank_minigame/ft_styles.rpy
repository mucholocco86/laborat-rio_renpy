transform ft_bg_transform:
    zoom 1.0
    easein 10 zoom 1.05
    easein 10 zoom 1.0
    repeat

transform ft_fish_transform_stat:
    zoom 0.6
transform ft_fish_transform_stat2:
    zoom 0.6

transform ft_tt_transform:
    on show:
        alpha 0.0
        easein 0.5 alpha 1.0
    on hide:
        alpha 1.0
        easein 0.5 alpha 0.0

style ft_main_style:
    font "fonts/cabin-regular.ttf"
    size 40 * persistent.scale_factor
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]

style ft_main_style2:
    font "fonts/cabin-regular.ttf"
    size 30 * persistent.scale_factor
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]

style ft_main_style3:
    font "fonts/cabin-regular.ttf"
    size 25 * persistent.scale_factor
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]

style ft_main_btn_style:
    font "fonts/cabin-regular.ttf"
    size 30 * persistent.scale_factor
    color "#ffffff"
    hover_color "#fe9416"
    outlines [(1, "#000000", 0, 0)]
    hover_outlines [(1, "#000000", 0, 0)]

style ft_tt_style:
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

image ft_crazy_fish_anim:
    choice:
        pause 80
    choice:
        pause 60
    choice:
        pause 105
    "ft_crazy_fish05"
    pause 0.04
    "ft_crazy_fish06"
    pause 0.04
    "ft_crazy_fish07"
    pause 0.04
    "ft_crazy_fish08"
    pause 0.04
    "ft_crazy_fish09"
    pause 0.04
    "ft_crazy_fish10"
    pause 0.04
    "ft_crazy_fish11"
    pause 0.04
    "ft_crazy_fish12"
    pause 0.04
    "ft_crazy_fish13"
    pause 0.04
    "ft_crazy_fish14"
    pause 0.04
    "ft_crazy_fish15"
    pause 0.04
    "ft_crazy_fish16"
    pause 0.04
    "ft_crazy_fish17"
    pause 0.04
    "ft_crazy_fish18"
    pause 0.04
    "ft_crazy_fish19"
    pause 0.04
    "ft_crazy_fish20"
    pause 0.04
    "ft_crazy_fish21"
    pause 0.04
    "ft_crazy_fish22"
    pause 0.04
    "ft_crazy_fish23"
    pause 0.04
    "ft_crazy_fish24"
    pause 0.04
    "ft_crazy_fish25"
    pause 0.04
    "ft_crazy_fish26"
    pause 0.04
    "ft_crazy_fish27"
    pause 0.04
    "ft_crazy_fish28"
    pause 0.04
    "ft_crazy_fish29"
    pause 0.04
    "ft_crazy_fish30"
    pause 0.04
    "ft_crazy_fish31"
    pause 0.04
    "ft_crazy_fish32"
    pause 0.04
    "ft_crazy_fish33"
    pause 0.04
    "ft_crazy_fish34"
    pause 0.04
    "ft_crazy_fish35"
    pause 0.04
    "ft_crazy_fish36"
    pause 0.04
    "ft_crazy_fish37"
    pause 0.04
    "ft_crazy_fish38"
    pause 0.04
    "ft_crazy_fish39"
    pause 0.04
    "ft_crazy_fish40"
    pause 0.04
    "ft_crazy_fish41"
    pause 0.04
    "ft_crazy_fish42"
    pause 0.04
    "ft_crazy_fish43"
    pause 0.04
    "ft_crazy_fish44"
    pause 0.04
    "ft_crazy_fish45"
    pause 0.04
    "ft_crazy_fish46"
    pause 0.04
    "ft_crazy_fish47"
    pause 0.04
    "ft_crazy_fish48"
    pause 0.04
    "ft_crazy_fish49"
    pause 0.04
    "ft_crazy_fish50"
    pause 0.04
    "ft_crazy_fish51"
    pause 0.04
    repeat

image ft_fish_anim:
    "ft_fish_00"
    pause 0.04
    "ft_fish_01"
    pause 0.04
    "ft_fish_02"
    pause 0.04
    "ft_fish_03"
    pause 0.04
    "ft_fish_04"
    pause 0.04
    "ft_fish_05"
    pause 0.04
    "ft_fish_06"
    pause 0.04
    "ft_fish_07"
    pause 0.04
    "ft_fish_08"
    pause 0.04
    "ft_fish_09"
    pause 0.04
    "ft_fish_10"
    pause 0.04
    "ft_fish_11"
    pause 0.04
    "ft_fish_12"
    pause 0.04
    "ft_fish_13"
    pause 0.04
    "ft_fish_14"
    pause 0.04
    "ft_fish_15"
    pause 0.04
    "ft_fish_16"
    pause 0.04
    "ft_fish_17"
    pause 0.04
    "ft_fish_18"
    pause 0.04
    "ft_fish_19"
    pause 0.04
    "ft_fish_20"
    pause 0.04
    "ft_fish_21"
    pause 0.04
    "ft_fish_22"
    pause 0.04
    "ft_fish_23"
    pause 0.04
    "ft_fish_24"
    pause 0.04
    "ft_fish_25"
    pause 0.04
    "ft_fish_26"
    pause 0.04
    "ft_fish_27"
    pause 0.04
    "ft_fish_28"
    pause 0.04
    "ft_fish_29"
    pause 0.04
    "ft_fish_30"
    pause 0.04
    repeat

image dead_fish_anim:
    "dead_fish_00"
    pause 0.04
    "dead_fish_01"
    pause 0.04
    "dead_fish_02"
    pause 0.04
    "dead_fish_03"
    pause 0.04
    "dead_fish_04"
    pause 0.04
    "dead_fish_05"
    pause 0.04
    "dead_fish_06"
    pause 0.04
    "dead_fish_07"
    pause 0.04
    "dead_fish_08"
    pause 0.04
    "dead_fish_09"
    pause 0.04
    "dead_fish_10"
    pause 0.04
    "dead_fish_11"
    pause 0.04
    "dead_fish_12"
    pause 0.04
    "dead_fish_13"
    pause 0.04
    "dead_fish_14"
    pause 0.04
    "dead_fish_15"
    pause 0.04
    "dead_fish_14"
    pause 0.04
    "dead_fish_13"
    pause 0.04
    "dead_fish_12"
    pause 0.04
    "dead_fish_11"
    pause 0.04
    "dead_fish_10"
    pause 0.04
    "dead_fish_09"
    pause 0.04
    "dead_fish_08"
    pause 0.04
    "dead_fish_07"
    pause 0.04
    "dead_fish_06"
    pause 0.04
    "dead_fish_05"
    pause 0.04
    "dead_fish_04"
    pause 0.04
    "dead_fish_03"
    pause 0.04
    "dead_fish_02"
    pause 0.04
    "dead_fish_01"
    pause 0.04
    "dead_fish_00"
    pause 0.04
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

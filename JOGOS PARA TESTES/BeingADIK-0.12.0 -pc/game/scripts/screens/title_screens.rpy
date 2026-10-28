init:
    default episode_title_name = ""

style episode_number_title_style:
    font "fonts/cabin-regular.ttf"
    size 50 * persistent.scale_factor
    color "#ffffff"

style episode_title_style:
    font "fonts/cabin-regular.ttf"
    size 150 * persistent.scale_factor
    color "#ffffff"
style episode_title_style2:
    font "fonts/cabin-regular.ttf"
    size 100 * persistent.scale_factor
    color "#ffffff"

screen episode_title_screen:
    tag episode_title_screen
    modal True
    timer 5 action Hide("episode_title_screen")

    if currentEpisode == 0:
        $ episode_title_name = "Riding the Waves"
    elif currentEpisode == 9:
        $ episode_title_name = "Vixens"
    elif currentEpisode == 10:
        $ episode_title_name = "Calm Before the Snow"
    elif currentEpisode == 11:
        $ episode_title_name = "Paradigm Shift"
    elif currentEpisode == 12:
        $ episode_title_name = "Smoke and Fire"

    imagebutton at title_white_line_anim4:
        xoffset -2200 * persistent.scale_factor
        idle "title_ol_white_line"
        hover "title_ol_white_line"
        yalign 0.28
    imagebutton at title_white_line_anim3:
        xoffset 2920 * persistent.scale_factor
        idle "title_ol_white_line"
        hover "title_ol_white_line"
        yalign 0.32
    imagebutton at title_orange_line_anim:
        xoffset -5030 * persistent.scale_factor
        idle "title_ol_orange_line"
        hover "title_ol_orange_line"
        yalign 0.36
    imagebutton at title_orange_line_anim:
        xoffset -1750 * persistent.scale_factor
        idle "title_ol_orange_line"
        hover "title_ol_orange_line"
        yalign 0.36
    if currentEpisode >= 9:
        text "Episode %d" % currentEpisode style "episode_number_title_style" at episode_number_anim:
            xoffset -2000 * persistent.scale_factor
            yalign 0.35
    else:
        text "Interlude" style "episode_number_title_style" at episode_number_anim:
            xoffset -2000 * persistent.scale_factor
            yalign 0.35
    if currentEpisode == 10:
        text "[episode_title_name]" style "episode_title_style2" at episode_title_anim:
            xoffset 2000 * persistent.scale_factor
            yalign 0.45
    else:
        text "[episode_title_name]" style "episode_title_style" at episode_title_anim:
            xoffset 2000 * persistent.scale_factor
            yalign 0.45
    imagebutton at title_orange_line_anim2:
        xoffset 2000 * persistent.scale_factor
        idle "title_ol_orange_line"
        hover "title_ol_orange_line"
        yalign 0.57
    imagebutton at title_white_line_anim2:
        xoffset -4000 * persistent.scale_factor
        idle "title_ol_white_line"
        hover "title_ol_white_line"
        yalign 0.61
    imagebutton at title_white_line_anim:
        xoffset 1700 * persistent.scale_factor
        idle "title_ol_white_line"
        hover "title_ol_white_line"
        yalign 0.65


transform title_orange_line_anim:
    easein 1.0 xpos 2500 * persistent.scale_factor
    easein 3.0 xpos 2600 * persistent.scale_factor
    easein 1.0 xpos 8000 * persistent.scale_factor
transform title_orange_line_anim2:
    easein 0.5 xpos -2000 * persistent.scale_factor
    easein 3.5 xpos -2100 * persistent.scale_factor
    easein 1.0 xpos -8000 * persistent.scale_factor

transform title_white_line_anim:
    easein 1.0 xpos -4400 * persistent.scale_factor
    easein 0.5 xpos -4450 * persistent.scale_factor
    easein 0.5 xpos -4350 * persistent.scale_factor
    easein 0.5 xpos -4400 * persistent.scale_factor
    easein 0.5 xpos -4420 * persistent.scale_factor
    easein 0.5 xpos -4450 * persistent.scale_factor
    easein 0.5 xpos -4400 * persistent.scale_factor
    easein 0.5 xpos -6000 * persistent.scale_factor

transform title_white_line_anim2:
    easein 1.0 xpos 1400 * persistent.scale_factor
    easein 0.5 xpos 1450 * persistent.scale_factor
    easein 0.75 xpos 1350 * persistent.scale_factor
    easein 0.25 xpos 1400 * persistent.scale_factor
    easein 0.5 xpos 1455 * persistent.scale_factor
    easein 0.5 xpos 1350 * persistent.scale_factor
    easein 0.5 xpos 1400 * persistent.scale_factor
    easein 1.0 xpos 6000 * persistent.scale_factor

transform title_white_line_anim3:
    easein 1.0 xpos -1400 * persistent.scale_factor
    easein 0.5 xpos -1450 * persistent.scale_factor
    easein 0.5 xpos -1350 * persistent.scale_factor
    easein 0.5 xpos -1400 * persistent.scale_factor
    easein 0.5 xpos -1420 * persistent.scale_factor
    easein 0.5 xpos -1450 * persistent.scale_factor
    easein 0.5 xpos -1400 * persistent.scale_factor
    easein 0.5 xpos -7000 * persistent.scale_factor

transform title_white_line_anim4:
    easein 1.0 xpos 3600 * persistent.scale_factor
    easein 0.5 xpos 3650 * persistent.scale_factor
    easein 0.75 xpos 3550 * persistent.scale_factor
    easein 0.25 xpos 3600 * persistent.scale_factor
    easein 0.5 xpos 3655 * persistent.scale_factor
    easein 0.5 xpos 3550 * persistent.scale_factor
    easein 0.5 xpos 3600 * persistent.scale_factor
    easein 1.0 xpos 6000 * persistent.scale_factor

transform episode_number_anim:
    easein 1.0 xpos 2500 * persistent.scale_factor
    easein 3.0 xpos 2600 * persistent.scale_factor
    easein 1.0 xpos 8000 * persistent.scale_factor

transform episode_title_anim:
    easein 1.0 xpos -1300 * persistent.scale_factor
    easein 3.0 xpos -1400 * persistent.scale_factor
    easein 1.0 xpos -7000 * persistent.scale_factor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen pp_intro_screen:
    tag pp_intro_screen
    modal True

    if currentEpisode == 9:
        add "pp_sky" at pp_intro_sky_transformb_ep9
        vbox at pp_intro_sky_transform2_ep9:
            add "pp_sky" at pp_intro_sky_transform_ep9
        add "particle_rain1" at pp_intro_rain_transform_ep9
        add "particle_rain2" at pp_intro_rain_transform_ep9
        add "particle_rain3" at pp_intro_rain_transform_ep9
        add "particle_rain4" at pp_intro_rain_transform_ep9
        add "particle_rain5" at pp_intro_rain_transform_ep9
        add "particle_rain6" at pp_intro_rain_transform_ep9
        add "pp_blood" xoffset -50 * persistent.scale_factor yoffset 130 * persistent.scale_factor at pp_intro_blood_transform_ep9
        add "pp_pumpkin" xalign .5 yoffset -170 * persistent.scale_factor at pp_intro_pumpkin_transform_ep9
        add "pp_lightning" at pp_intro_lightning_transform_ep9

        text "Party Planning" style "pp_intro_header_style" xalign .5 yalign 0.75 at pp_intro_text_transform_ep9
        text "{color=007db5}Party{/color} #1 - {color=fe9416}Halloween{/color}" style "pp_intro_header_style2" xalign .5 yalign 0.92 at pp_intro_text_transform2_ep9
        add "pp_axe" xalign 0.7 yalign 1.0 at pp_axe_transform_ep9

        if persistent.pp_tutorial != 0:
            textbutton "Skip Tutorial" text_style "pp_intro_btn_style_ep9" xalign 0.98 yalign 0.5 action (Play("sfx1", "sound_effects/slash.mp3", loop = False),Hide("pp_intro_screen"), Jump("ep9_skip_tut_label")) at pp_intro_text_transform3_ep9
        else:
            textbutton "Skip Tutorial" text_style "pp_intro_btn_style2_ep9" xalign 0.98 yalign 0.5 action NullAction() at pp_intro_text_transform3_ep9

        textbutton "Play Tutorial" text_style "pp_intro_btn_style_ep9" xalign 0.04 yalign 0.5 action (Play("sfx1", "sound_effects/slash.mp3", loop = False),Hide("pp_intro_screen"), Jump("ep9_play_tut_label")) at pp_intro_text_transform3_ep9

        add "pp_blood_choice" at pp_blood_choice_transform
    elif currentEpisode == 10:
        add "pp_bbq_bg" at pp_intro_bg_transform_ep10
        add AlphaBlend("%s/ep10/diks/pp_bbq_bg_rev_mask.png" % persistent.img_dir,Frame(Null(), 10 * persistent.scale_factor,10 * persistent.scale_factor),"particle_ember", alpha=True) at pp_intro_prt_transform_ep9
        add AlphaBlend("%s/ep10/diks/pp_bbq_bg_rev_mask.png" % persistent.img_dir,Frame(Null(), 10 * persistent.scale_factor,10 * persistent.scale_factor),"particle_ember2", alpha=True) at pp_intro_prt_transform_ep9
        add AlphaBlend("%s/ep10/diks/pp_bbq_bg_rev_mask.png" % persistent.img_dir,Frame(Null(), 10 * persistent.scale_factor,10 * persistent.scale_factor),"particle_ember3", alpha=True) at pp_intro_prt_transform_ep9
        add AlphaBlend("%s/ep10/diks/pp_bbq_bg_rev_mask.png" % persistent.img_dir,Frame(Null(), 10 * persistent.scale_factor,10 * persistent.scale_factor),"particle_ember4", alpha=True) at pp_intro_prt_transform_ep9

        add "particle_firefly1" at pp_intro_prt_transform_ep9
        add "particle_firefly2" at pp_intro_prt_transform_ep9

        add "pp_bbq_flame_right" at pp_intro_fire_transform_ep10
        add "pp_bbq_flame_left" at pp_intro_fire_transform2_ep10

        add "pp_bbq_title" at pp_intro_title_transform_ep10
        add "pp_bbq_title2" at pp_intro_title_transform2_ep10
        add "pp_bbq_guitar" at pp_intro_item_transform_ep10
        add "pp_bbq_bp" at pp_intro_item_transform2_ep10
        add "pp_bbq_beer" at pp_intro_item_transform3_ep10

        text "PARTY PLANNING" style "pp_intro_header_ep10_style" xalign .5 yalign 0.2 at pp_intro_text_transform_ep10
        text "{color=007db5}Party{/color} #2" style "pp_intro_header_ep10_style2" xalign .5 yalign 0.8 at pp_intro_text_transform2_ep10

        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (Hide("pp_intro_screen"), Jump("ep10_play_label"))
    elif currentEpisode == 11:
        add "pp_cpp_bgg"
        add "pp_cpp_bg2" at pp_intro_bg_transform_ep11
        add "pp_cpp_fg" at pp_intro_bg_transform_ep10
        add "particle_bf1"
        add "particle_bf2"
        add "particle_bf3"
        add "particle_bf4"
        add "particle_sf1"
        add "particle_sf2"
        add "particle_sf3"
        add "particle_mf1"
        add "particle_mf2"
        add "particle_mf3"

        add "pp_cpp_xx" at pp_intro_title_transform_ep11
        add "pp_cpp_title2" at pp_intro_title_transform_ep11
        add "pp_cpp_title3" at pp_intro_title_transform_ep10
        add "pp_cpp_title4" at pp_intro_title_transform2_ep10

        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (Hide("pp_intro_screen"), Jump("ep11_play_label"))
    elif currentEpisode == 12:
        add "pp_ny_bgg"
        add "pp_ny_title" at pp_my_title2_transform_ep12

        add "particle_conf3"
        add "particle_conf6"
        add "particle_conf7"
        add "particle_conf9"
        add "particle_conf10"
        add "particle_conf5"

        add "pp_ny_new" at pp_my_title_transform_ep12
        add "pp_ny_years" at pp_my_title_transform_ep12
        add "pp_ny_eve" at pp_my_title_transform_ep12
        add "pp_ny_party" at pp_my_title_transform_ep12
        add "pp_ny_balloon" at pp_intro_balloon_transform_ep12
        add "pp_ny_bottle" at pp_intro_bottle_transform_ep12
        add "pp_ny_glasses" at pp_intro_glasses_transform_ep12

        add "particle_conf8"
        add "particle_conf1"
        add "particle_conf2"
        add "particle_conf4"


        imagebutton:
            idle "big_invis"
            hover "big_invis"
            action (Hide("pp_intro_screen"), Jump("ep12_play_label"))

image pp_cpp_bgg:
    "pp_cpp_bg" with Dissolve(1.0, alpha=True)
    pause 1
    "pp_cpp_bgb" with Dissolve(1.0, alpha=True)
    pause 1
    repeat
image pp_cpp_xx:
    function play_neon_ep11
    "pp_cpp_title1" with Dissolve(0.1, alpha=True)
    pause 0.1
    "pp_cpp_empty" with Dissolve(0.1, alpha=True)
    pause 0.1
    choice:
        function play_neon2_ep11
        "pp_cpp_title1" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_cpp_empty" with Dissolve(0.1, alpha=True)
        pause 0.1
    choice:
        function play_neon3_ep11
        "pp_cpp_title1" with Dissolve(0.1, alpha=True)
        pause 5.0
        "pp_cpp_empty" with Dissolve(0.1, alpha=True)
        pause 0.1
    choice:
        function play_neon2_ep11
        "pp_cpp_title1" with Dissolve(0.1, alpha=True)
        pause 4.0
        "pp_cpp_empty" with Dissolve(0.1, alpha=True)
        pause 0.1
    repeat

image particle_conf1 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti1.png", count=3, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf2 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti2.png", count=3, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf3 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti3.png", count=3, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf4 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti4.png", count=3, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf5 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti5.png", count=5, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf6 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti6.png", count=5, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf7 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti7.png", count=7, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf8 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti8.png", count=7, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf9 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti9.png", count=7, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)
image particle_conf10 = SnowBlossom("[persistent.img_dir]/ep12/pp_minigame/pp_ny_confetti10.png", count=8, xspeed=(5 * persistent.scale_factor, -20 * persistent.scale_factor), yspeed=(50 * persistent.scale_factor, 100 * persistent.scale_factor), fast=True)


image pp_ny_new:
    "pp_ny_new_fr0" with Dissolve(1.5, alpha=True)
    pause 1.5
    "pp_ny_new_fr1" with Dissolve(1.5, alpha=True)
    pause 1.5
    repeat
image pp_ny_years:
    "pp_ny_years_fr0" with Dissolve(1, alpha=True)
    pause 1
    "pp_ny_years_fr1" with Dissolve(1, alpha=True)
    pause 1
    repeat
image pp_ny_eve:
    "pp_ny_eve_fr0" with Dissolve(2, alpha=True)
    pause 2
    "pp_ny_eve_fr1" with Dissolve(2, alpha=True)
    pause 2
    choice:
        function play_neon2_ep11
        "pp_ny_eve_fr2" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_ny_eve_fr1" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_ny_eve_fr2" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_ny_eve_fr1" with Dissolve(0.1, alpha=True)
        pause 0.1
    choice:
        function play_neon3_ep11
        "pp_ny_eve_fr2" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_ny_eve_fr1" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_ny_eve_fr2" with Dissolve(0.1, alpha=True)
        pause 0.1
        "pp_ny_eve_fr1" with Dissolve(0.1, alpha=True)
        pause 0.1
    choice:
        "pp_ny_eve_fr0" with Dissolve(2, alpha=True)
        pause 2
        "pp_ny_eve_fr1" with Dissolve(2, alpha=True)
        pause 2
    repeat
image pp_ny_party:
    "pp_ny_party_fr0" with Dissolve(2, alpha=True)
    pause 2
    "pp_ny_party_fr1" with Dissolve(2, alpha=True)
    pause 2
    repeat

image particle_ember = SnowBlossom("%s/ep10/diks/pp_ember1.png" % persistent.img_dir, count=10, xspeed=(-10, 10), yspeed=(-300, -100), fast=True)
image particle_ember2 = SnowBlossom("%s/ep10/diks/pp_ember2.png" % persistent.img_dir, count=10, xspeed=(-10, 10), yspeed=(-300, -100), fast=True)
image particle_ember3 = SnowBlossom("%s/ep10/diks/pp_ember3.png" % persistent.img_dir, count=10, xspeed=(-10, 10), yspeed=(-200, -100), fast=True)
image particle_ember4 = SnowBlossom("%s/ep10/diks/pp_ember4.png" % persistent.img_dir, count=10, xspeed=(-10, 10), yspeed=(-200, -100), fast=True)

image particle_firefly1 = SnowBlossom("%s/ep10/diks/pp_firefly1.png" % persistent.img_dir, count=10, xspeed=(-100, 100), yspeed=(-40, 50), fast=True)
image particle_firefly2 = SnowBlossom("%s/ep10/diks/pp_firefly2.png" % persistent.img_dir, count=10, xspeed=(-100, 100), yspeed=(-40, 50), fast=True)

transform pp_my_title_transform_ep12:
    yoffset 100 * persistent.scale_factor
transform pp_my_title2_transform_ep12:
    yoffset 75 * persistent.scale_factor
transform pp_intro_balloon_transform_ep12:
    zoom 1.00
    yoffset -450 * persistent.scale_factor
    around (.1, .1) alignaround (.1, .1) xalign .1 yalign .1
    rotate 0
    linear 5 rotate 2
    linear 5 rotate 0
    repeat
    repeat
transform pp_intro_bottle_transform_ep12:
    zoom 1.00
    choice:
        easein 4 zoom 1.02
        easein 4 zoom 1.00
    choice:
        easein 5 zoom 1.03
        easein 5 zoom 1.00
    repeat
transform pp_intro_glasses_transform_ep12:
    zoom 1.00
    choice:
        easein 7 zoom 1.04
        easein 7 zoom 1.00
    choice:
        easein 6 zoom 1.03
        easein 6 zoom 1.00
    repeat
transform pp_intro_sky_transform_ep9:
    on show:
        alpha 0.0
        easein 3 alpha 1.0
    on hide:
        pause 1.0
        alpha 1.0
        easein 1 alpha 0.0
transform pp_intro_sky_transformb_ep9:
    on show:
        alpha 0.0
        easein 6 alpha 1.0
    on hide:
        pause 1.0
        alpha 1.0
        easein 1 alpha 0.0
transform pp_intro_sky_transform2_ep9:
    zoom 1.0
    easein 10 zoom 1.07
    easein 10 zoom 1.00
    repeat
transform pp_intro_bg_transform_ep10:
    zoom 1.0
    easein 10 zoom 1.02
    easein 10 zoom 1.00
    repeat
transform pp_intro_bg_transform_ep11:
    zoom 1.0
    easein 10 zoom 1.04
    easein 10 zoom 1.00
    repeat
transform pp_intro_title_transform_ep10:
    zoom 1.00
    easein 3 zoom 1.01
    easein 3 zoom 1.00
    repeat
transform pp_intro_title_transform_ep11:
    zoom 1.00
    easein 3 zoom 1.01
    easein 3 zoom 1.00
    repeat
transform pp_intro_title_transform2_ep10:
    zoom 1.00
    choice:
        easein 3 zoom 1.01
        easein 3 zoom 1.00
    choice:
        easein 3 zoom 1.02
        easein 3 zoom 1.00
    repeat
transform pp_intro_fire_transform_ep10:
    zoom 1.01
    choice:
        easein 2 zoom 1.00
        easein 2 zoom 1.01
    choice:
        easein 1 zoom 1.00
        easein 1 zoom 1.01
    repeat
transform pp_intro_fire_transform2_ep10:
    zoom 1.0
    choice:
        easein 2 zoom 1.02
        easein 2 zoom 1.00
    choice:
        easein 1 zoom 1.01
        easein 1 zoom 1.00
    repeat
transform pp_intro_item_transform_ep10:
    yoffset 450 * persistent.scale_factor
    around (.1, .9) alignaround (.1, .9) xalign .1 yalign .9
    rotate 0
    linear 5 rotate 2
    linear 5 rotate 0
    repeat
transform pp_intro_item_transform3_ep10:
    yoffset 450 * persistent.scale_factor
    around (.1, .9) alignaround (.1, .9) xalign .1 yalign .9
    rotate 0
    linear 5 rotate 2
    linear 5 rotate 0
    repeat
transform pp_intro_item_transform2_ep10:
    zoom 1.00
    easein 7 zoom 1.03
    easein 7 zoom 1.00
    repeat

transform pp_blood_choice_transform:
    on show:
        alpha 0.0
    on hide:
        alpha 1.0
        pause 1.0

transform pp_intro_rain_transform_ep9:
    on show:
        alpha 0.0
        easein 3 alpha 1.0
    on hide:
        pause 1.0
        alpha 1.0
        easein 1 alpha 0.0
transform pp_intro_prt_transform_ep9:
    on show:
        alpha 0.0
        easein 3 alpha 1.0

transform pp_sky_transform_ep9:
    zoom 1.0
    easein 10 zoom 1.07
    easein 10 zoom 1.0
    repeat
transform pp_intro_lightning_transform_ep9:
    alpha 0.0
    pause 2.0
    easein 0.3 alpha 1.0
    easein 0.3 alpha 0.0

transform pp_intro_lightning_transform2_ep9:
    alpha 0.0
    pause 36
    easein 0.3 alpha 1.0
    easein 0.3 alpha 0.0
transform pp_intro_blood_transform_ep9:
    alpha 0.0
    pause 1.5
    easein 0.1 alpha 1.0
transform pp_axe_transform_ep9:
    xpos 1150 * persistent.scale_factor
    choice:
        easein 1 xpos 1170 * persistent.scale_factor
        easein 1.5 xpos 1150 * persistent.scale_factor
    choice:
        easein 1 xpos 1160 * persistent.scale_factor
        easein 1 xpos 1150 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1165 * persistent.scale_factor
        easein 1 xpos 1150 * persistent.scale_factor
    repeat

transform pp_intro_transform_ep9:
    xpos 1350 * persistent.scale_factor
    choice:
        easein 1 xpos 1320 * persistent.scale_factor
        easein 1.5 xpos 1350 * persistent.scale_factor
    choice:
        easein 1 xpos 1310 * persistent.scale_factor
        easein 1 xpos 1350 * persistent.scale_factor
    choice:
        easein 0.5 xpos 1330 * persistent.scale_factor
        easein 1 xpos 1350 * persistent.scale_factor
    repeat

transform pp_intro_pumpkin_transform_ep9:
    on show:
        alpha 0.0
        easein 1 alpha 1.0
    on hide:
        pause 1.0
        alpha 1.0
        easein 1 alpha 0.0

transform pp_intro_text_transform_ep9:
    on show:
        alpha 0.0
        pause 2.0
        easein 1 alpha 1.0
    on hide:
        alpha 0.0
transform pp_intro_text_transform2_ep9:
    on show:
        alpha 0.0
        pause 3.5
        easein 1 alpha 1.0
    on hide:
        pause 1.0
        alpha 1.0
        easein 1 alpha 0.0
transform pp_intro_text_transform_ep10:
    on show:
        alpha 0.0
        easein 1 alpha 1.0
    on hide:
        alpha 0.0
transform pp_intro_text_transform2_ep10:
    on show:
        alpha 0.0
        pause 1.0
        easein 1 alpha 1.0
transform pp_intro_text_transform3_ep9:
    on show:
        alpha 0.0
        pause 5.0
        easein 1 alpha 1.0
    on hide:
        alpha 0.0

style pp_intro_btn_style_ep9:
    font "fonts/Creepster-Regular.ttf"
    size 80 * persistent.scale_factor
    color "#191919"
    hover_color "#147917"
    outlines [ (absolute(3), "#fe9416", absolute(2), absolute(2)) ]

style pp_intro_btn_style2_ep9:
    font "fonts/Creepster-Regular.ttf"
    size 80 * persistent.scale_factor
    color "#676767"
    outlines [ (absolute(3), "#fe9416", absolute(2), absolute(2)) ]

style pp_intro_header_ep10_style:
    font "fonts/briarwood_heavy_font.ttf"
    size 80 * persistent.scale_factor
    color "#ffe059"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
style pp_intro_header_ep10_style2:
    font "fonts/briarwood_heavy_font.ttf"
    size 80 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]

style pp_intro_header_style:
    font "fonts/Creepster-Regular.ttf"
    size 80 * persistent.scale_factor
    color "#f72400"
    outlines [ (absolute(3), "#fe9416", absolute(2), absolute(2)) ]

style pp_intro_header_style2:
    font "fonts/Creepster-Regular.ttf"
    size 80 * persistent.scale_factor
    color "#ffffff"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

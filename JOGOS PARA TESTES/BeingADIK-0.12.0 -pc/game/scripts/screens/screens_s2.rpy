image particle_rain1 = SnowBlossom("[persistent.img_dir]/gui/rain/raindrop1.png", count=30, xspeed=(-200 * persistent.scale_factor, -500 * persistent.scale_factor), yspeed=(1000 * persistent.scale_factor, 2000 * persistent.scale_factor), fast=True)
image particle_rain2 = SnowBlossom("[persistent.img_dir]/gui/rain/raindrop2.png", count=30, xspeed=(-200 * persistent.scale_factor, -500 * persistent.scale_factor),  yspeed=(1000 * persistent.scale_factor, 2000 * persistent.scale_factor), fast=True)
image particle_rain3 = SnowBlossom("[persistent.img_dir]/gui/rain/raindrop3.png", count=40, xspeed=(-200 * persistent.scale_factor, -500 * persistent.scale_factor), yspeed=(1000 * persistent.scale_factor, 2000 * persistent.scale_factor), fast=True)
image particle_rain4 = SnowBlossom("[persistent.img_dir]/gui/rain/raindrop4.png", count=40, xspeed=(-200 * persistent.scale_factor, -500 * persistent.scale_factor),  yspeed=(1000 * persistent.scale_factor, 2000 * persistent.scale_factor), fast=True)
image particle_rain5 = SnowBlossom("[persistent.img_dir]/gui/rain/raindrop5.png", count=30, xspeed=(-200 * persistent.scale_factor, -500 * persistent.scale_factor), yspeed=(1000 * persistent.scale_factor, 2000 * persistent.scale_factor), fast=True)
image particle_rain6 = SnowBlossom("[persistent.img_dir]/gui/rain/raindrop6.png", count=30, xspeed=(-200 * persistent.scale_factor, -500 * persistent.scale_factor),  yspeed= (1000 * persistent.scale_factor, 2000 * persistent.scale_factor), fast=True)

screen rain_screen:
    tag rain_screen
    modal False
    add "particle_rain1"
    add "particle_rain2"
    add "particle_rain3"
    add "particle_rain4"
    add "particle_rain5"
    add "particle_rain6"

screen rain_screen_minor:
    tag rain_screen_minor
    modal False
    add "particle_rain1"

style click_to_continue_style:
    color "#ffffff"
    outlines [(4, "#000000", 0, 0)]
    text_align 0.5
    size 45 * persistent.scale_factor

screen click_to_continue_screen:
    tag click_to_continue_screen
    modal False
    text "Click to continue" style "click_to_continue_style" xalign 0.5 yalign 0.9

screen new_phone_screen:
    tag new_phone_screen
    modal False
    if not _in_replay:
        key "mouseup_2" action (Function(mphone_init_phone_screen),SetVariable("phone_opened",True),SetVariable("_game_menu_screen",None),Hide("map_screen_notification"), Hide("specialmsglong"), Hide("srmsg"), Hide("newmoneymsg"),Show("mphone_screen"))
        imagebutton at show_hide_dissolve:
            if persistent.golden_phone and persistent.golden_phone_skin_enabled:
                idle "phone_proximity_btn"
                hover "mphone_proximity_btn_golden_hover"
            else:
                idle "phone_proximity_btn"
                hover "mphone_proximity_btn_hover"
            xalign 0.021
            yalign 0.022
            action NullAction()
        imagebutton at show_hide_dissolve:
            if persistent.golden_phone and persistent.golden_phone_skin_enabled:
                idle "mphone_btn"
                hover "mphone_btn_golden_hover"
            else:
                idle "mphone_btn"
                hover "mphone_btn_hover"
            xalign 0.02
            yalign 0.0198
            action (Function(mphone_init_phone_screen),SetVariable("phone_opened",True),Hide("map_screen_notification"), Hide("specialmsglong"), Hide("srmsg"),Hide("newmoneymsg"),Show("mphone_screen"),SetVariable("_game_menu_screen",None))
        if not "music" in disabled_apps:
            imagebutton at show_hide_dissolve:
                idle "skip_song_proximity_button"
                hover "skip_song_proximity_button_hover"
                xalign 0.99
                yalign 0.01
                action NullAction()
            imagebutton at show_hide_dissolve:
                idle "skip_song_button"
                hover "skip_song_button_hover"
                xalign 0.99
                yalign 0.01
                action Function(mphone_next_song)

screen dance_filter_screen:
    tag dance_filter_screen
    modal False
    add "dance_filter_image"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

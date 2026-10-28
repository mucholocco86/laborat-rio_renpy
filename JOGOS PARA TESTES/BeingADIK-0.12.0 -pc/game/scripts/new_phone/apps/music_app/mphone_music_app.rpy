screen mphone_music_app_screen:
    tag mphone_music_app_screen
    modal True
    timer 2 repeat True action SetVariable("tmpMusicInt",0)
    fixed:
        at mphone_app_transform
        add "mphone_music_app_bg"
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action Hide("mphone_music_app_screen")
    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_music_app_screen")
            xalign 0.5
            yalign mphone_off_yalign

    fixed:
        at mphone_app_transform
        hbox:
            spacing 8 * persistent.scale_factor
            xalign 0.53
            yalign 0.376
            vbox:
                xminimum 220 * persistent.scale_factor
                xmaximum 220 * persistent.scale_factor
                yalign 0.5
                xoffset 16 * persistent.scale_factor
                text "Music - Now Playing" style "mphone_music_bar_style"
                $ tmpBool = False
                for x in range(0,len(persistent.mphone_music_list)):
                    if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                        $ tmpList = persistent.mphone_music_list[x][0].split(" - ", 1)
                        text "%s" % tmpList[1] style "mphone_music_bar_style"
                        text "%s" % tmpList[0] style "mphone_music_bar_style"
                        $ tmpBool = True
                if not tmpBool:
                    text "-" style "mphone_music_bar_style"
                    text "-" style "mphone_music_bar_style"

            vbox:
                yalign 0.5
                spacing -16 * persistent.scale_factor
                xminimum 220 * persistent.scale_factor
                xmaximum 220 * persistent.scale_factor
                hbox:
                    imagebutton:
                        yalign 0.5
                        idle "mphone_music_bar_next_button_idle"
                        hover "mphone_music_bar_next_button_hover"
                        action Function(mphone_next_song)
                    imagebutton:
                        yalign 0.5
                        if _preferences.get_volume('music') > 0:
                            idle "mphone_music_bar_sound"
                            hover "mphone_music_bar_sound"
                        else:
                            idle "mphone_music_bar_mute"
                            hover "mphone_music_bar_mute"
                        action NullAction()

                    bar value Preference("music volume") style 'mphone_music_hbar_style' yalign 0.5
                if mphone_music_genre == 4:
                    textbutton "Play: Favorites" text_style "mphone_music_text_button_style" action (SetVariable("mphone_music_genre",0),Function(mphone_next_song))
                elif mphone_music_genre == 3:
                    textbutton "Play: Relaxing songs" text_style "mphone_music_text_button_style" action (SetVariable("mphone_music_genre",4),Function(mphone_next_song))
                elif mphone_music_genre == 2:
                    textbutton "Play: Party songs" text_style "mphone_music_text_button_style" action (SetVariable("mphone_music_genre",3),Function(mphone_next_song))
                elif mphone_music_genre == 1:
                    textbutton "Play: Rock songs" text_style "mphone_music_text_button_style" action (SetVariable("mphone_music_genre",2),Function(mphone_next_song))
                else:
                    textbutton "Play: Shuffle all" text_style "mphone_music_text_button_style" action (SetVariable("mphone_music_genre",1),Function(mphone_next_song))
                if mphone_music_bar_show:
                    textbutton "Home Screen Bar: Show" text_style "mphone_music_text_button_style" action SetVariable("mphone_music_bar_show",False)
                else:
                    textbutton "Home Screen Bar: Hide" text_style "mphone_music_text_button_style" action SetVariable("mphone_music_bar_show",True)

    fixed:
        at mphone_app_transform
        textbutton "Filter by genre: %s" % mphone_genre_list[mphone_genre_count] text_style "mphone_music_text_button_style" action Function(mphone_next_genre) xalign 0.51 yalign 0.44 xminimum 470 * persistent.scale_factor xmaximum 470 * persistent.scale_factor

    fixed:
        at mphone_app_transform
        vpgrid:
            xminimum 470 * persistent.scale_factor
            xmaximum 470 * persistent.scale_factor
            yminimum 490 * persistent.scale_factor
            ymaximum 490 * persistent.scale_factor
            xalign 0.515
            yalign 0.834
            cols 1
            draggable True
            mousewheel True

            for x in range(0,len(persistent.mphone_music_list)):
                if mphone_genre_count == 0 or (persistent.mphone_music_list[x][3] == mphone_genre_count) or (persistent.mphone_music_list[x][2] and mphone_genre_count == 4):
                    hbox:
                        yalign 0.5
                        xminimum 470 * persistent.scale_factor xmaximum 470 * persistent.scale_factor
                        hbox:
                            yalign 0.5
                            xminimum 320 * persistent.scale_factor xmaximum 320 * persistent.scale_factor
                            if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                                text "{color=#fe9416}%s{/color}" % persistent.mphone_music_list[x][0] style "mphone_music_bar_style" yalign 0.5
                            else:
                                text "%s" % persistent.mphone_music_list[x][0] style "mphone_music_bar_style" yalign 0.5
                        hbox:
                            yalign 0.5
                            imagebutton:
                                yalign 0.5
                                if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                                    idle "mphone_music_play_active_idle"
                                    hover "mphone_music_play_active_hover"
                                else:
                                    idle "mphone_music_play_inactive_idle"
                                    hover "mphone_music_play_inactive_hover"
                                action Function(mphone_play_song, persistent.mphone_music_list[x][1])
                            if persistent.mphone_music_list[x][2]:
                                imagebutton:
                                    yalign 0.5
                                    idle "mphone_fav_active_idle"
                                    hover "mphone_fav_active_hover"
                                    action SetDict(persistent.mphone_music_list[x],2,False)
                            else:
                                imagebutton:
                                    yalign 0.5
                                    idle "mphone_fav_inactive_idle"
                                    hover "mphone_fav_inactive_hover"
                                    action SetDict(persistent.mphone_music_list[x],2,True)
        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

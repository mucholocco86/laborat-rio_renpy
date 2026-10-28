screen mphone_screen:
    tag mphone_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    if (freeRoamID == "" or disabled_apps != []) and freeRoamID != "texting":
        key "mouseup_2" action (SetVariable("mphone_bios_app_exception",False),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("mphone_screen"))
    else:
        key "mouseup_2" action (SetVariable("mphone_bios_app_exception",False),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("mphone_screen"),Jump(currentFreeRoamLabel))

    fixed:
        at mphone_bg_transform
        add "mphone_bg"
    fixed:
        if not mphone_bios_app_exception:
            at mphone_show_transform
        else:
            at mphone_show_transform_alt

        if mphone_custom_wallpaper != "":
            fixed:
                at CustomWallpaperMask
                add mphone_custom_wallpaper:
                    ypos (55 - min(mphone_custom_wallpaper_ypos,(int) (1.29636 * (mphone_custom_wallpaper_zoom*1.00)))) * persistent.scale_factor
                    xpos (min((int)(-960.0*((mphone_custom_wallpaper_zoom * 0.0012) + 0.9167) + 960.0) + (mphone_custom_wallpaper_xpos - (int)(((mphone_custom_wallpaper_max_width * ((mphone_custom_wallpaper_zoom * 0.0012) + 0.9167)) - 470.0)/2.0)),(int)(-960.0*((mphone_custom_wallpaper_zoom * 0.0012) + 0.9167) + 960.0) + (((int)(mphone_custom_wallpaper_max_width * ((mphone_custom_wallpaper_zoom * 0.0012) + 0.9167) - 470)) - (int)(((mphone_custom_wallpaper_max_width * ((mphone_custom_wallpaper_zoom * 0.0012) + 0.9167)) - 470.0)/2.0)))) * persistent.scale_factor
                    zoom (mphone_custom_wallpaper_zoom * 0.0012) + 0.9167

        else:
            add mphone_wallpaper_list[mphone_current_wallpaper][0]

        if persistent.golden_phone and persistent.golden_phone_skin_enabled:
            add "mphone_shell_gold"
        else:
            add "mphone_shell"
        add "mphone_fg"

        imagebutton at mphone_off_transform:
            idle "mphone_off_idle"
            hover "mphone_off_hover"
            if freeRoamID == "" or disabled_apps != []:
                action (SetVariable("mphone_bios_app_exception",False),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("mphone_screen"))
            else:
                action (SetVariable("mphone_bios_app_exception",False),SetVariable("phone_opened",False),SetVariable("_game_menu_screen","save"),Hide("mphone_screen"),Jump(currentFreeRoamLabel))
            xalign 0.5
            yalign mphone_off_yalign

        imagebutton:
            focus_mask True
            idle "mphone_invis_border_button"
            hover "mphone_invis_border_button"
            if freeRoamID == "" or disabled_apps != []:
                action (SetVariable("mphone_bios_app_exception",False),SetVariable("_game_menu_screen","save"),SetVariable("phone_opened",False),Hide("mphone_screen"))
            else:
                action (SetVariable("mphone_bios_app_exception",False),SetVariable("_game_menu_screen","save"),SetVariable("phone_opened",False),Hide("mphone_screen"),Jump(currentFreeRoamLabel))

        hbox:
            xalign 0.5
            yalign 0.06
            spacing 300 * persistent.scale_factor
            add "mphone_top_cakenet"
            if phone_bars_zero:
                add "mphone_top_icons_zero"
            else:
                add "mphone_top_icons"

        if mphone_app_gallery_enabled:
            imagebutton at mphone_gallery_transform:
                focus_mask True
                if mphone_app_gallery_new:
                    idle "mphone_app_gallery_new"
                    hover "mphone_app_gallery_new_hover"
                else:
                    idle "mphone_app_gallery"
                    hover "mphone_app_gallery_hover"
                xalign 0.43
                yalign 0.058
                action (SetVariable("mphone_app_gallery_new", False),Show("mphone_gallery_app_screen"))

    if mphone_music_bar_show:
        timer 2 repeat True action SetVariable("tmpMusicInt",0)
        fixed:
            if not mphone_bios_app_exception:
                at mphone_show_transform
            else:
                at mphone_show_transform_alt
            add "mphone_music_bar" xalign 0.5 yalign mphone_music_bar_position
            hbox:
                spacing 2 * persistent.scale_factor
                xoffset 8 * persistent.scale_factor
                xalign 0.52
                yalign mphone_music_bar_position
                vbox:
                    xminimum 220 * persistent.scale_factor
                    xmaximum 220 * persistent.scale_factor
                    yalign 0.5
                    xoffset 10 * persistent.scale_factor
                    text "Music - Now Playing" style "mphone_music_bar_style"
                    $ tmpBool = False
                    for x in range(0,len(persistent.mphone_music_list)):
                        if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                            $ tmpList = persistent.mphone_music_list[x][0].split(" - ", 1)
                            text "%s" % tmpList[1] style "mphone_music_bar_style"
                            text "%s" % tmpList[0] style "mphone_music_bar_style"
                            $ tmpBool = True
                    if not tmpBool:
                        for x in range(0,len(persistent.mphone_unlisted_music_list)):
                            if renpy.music.get_playing() == persistent.mphone_unlisted_music_list[x][1]:
                                $ tmpList = persistent.mphone_unlisted_music_list[x][0].split(" - ", 1)
                                text "%s" % tmpList[1] style "mphone_music_bar_style"
                                text "%s" % tmpList[0] style "mphone_music_bar_style"
                                $ tmpBool = True
                    if not tmpBool:
                        text "-" style "mphone_music_bar_style"
                        text "-" style "mphone_music_bar_style"
                vbox:
                    xoffset -18 * persistent.scale_factor
                    yalign 0.5
                    spacing -25 * persistent.scale_factor
                    hbox:
                        $ tmpBool = False
                        for x in range(0,len(persistent.mphone_music_list)):
                            if renpy.music.get_playing() == persistent.mphone_music_list[x][1]:
                                $ tmpBool = True
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
                        if not tmpBool:
                            imagebutton:
                                yalign 0.5
                                idle "mphone_fav_disabled"
                                hover "mphone_fav_disabled"
                                action NullAction()
                        imagebutton:
                            yalign 0.5
                            if not "music" in disabled_apps:
                                idle "mphone_music_bar_next_button_idle"
                                hover "mphone_music_bar_next_button_hover"
                                action Function(mphone_next_song)
                            else:
                                idle "mphone_music_bar_next_button_disabled"
                                hover "mphone_music_bar_next_button_disabled"
                                action NullAction()
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

    fixed:
        if not mphone_bios_app_exception:
            at mphone_show_transform
        else:
            at mphone_show_transform_alt
        vpgrid:
            xalign 0.5
            yalign mphone_app_grid_yalign
            cols 5
            rows 3
            xspacing 5 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if chat_new_tasks:
                        idle "mphone_app_tasks_new"
                        hover "mphone_app_tasks_new_hover"
                    else:
                        idle "mphone_app_tasks"
                        hover "mphone_app_tasks_hover"
                    action (SetVariable("chat_new_tasks",False),Show("mphone_tasks_app_screen"))
                    xalign 0.5
                text "Tasks" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if not "contacts" in disabled_apps:
                        if mphone_new_contact_event:
                            idle "mphone_app_contacts_new"
                            hover "mphone_app_contacts_new_hover"
                        else:
                            idle "mphone_app_contacts"
                            hover "mphone_app_contacts_hover"
                        action Show("mphone_contacts_app_screen")
                    else:
                        idle "mphone_app_contacts_disabled"
                        hover "mphone_app_contacts_disabled"
                        action NullAction()
                    xalign 0.5
                text "Contacts" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if not "rooster" in disabled_apps:
                        if new_cluck:
                            idle "mphone_app_rooster_new"
                            hover "mphone_app_rooster_new_hover"
                        else:
                            idle "mphone_app_rooster"
                            hover "mphone_app_rooster_hover"
                        action (SetVariable("new_cluck",False),Show("mphone_rooster_app_screen"))
                    else:
                        idle "mphone_app_rooster_disabled"
                        hover "mphone_app_rooster_disabled"
                        action NullAction()
                    xalign 0.5
                text "Rooster" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    idle "mphone_app_stats"
                    hover "mphone_app_stats_hover"
                    action (SetVariable("mphone_bios_app_exception",True),Hide("mphone_screen"),Show("mphone_stats_app_screen"))
                    xalign 0.5
                text "Stats" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if chat_new_bios:
                        idle "mphone_app_bios_new"
                        hover "mphone_app_bios_new_hover"
                    else:
                        idle "mphone_app_bios"
                        hover "mphone_app_bios_hover"
                    if mphone_bios_chars_list == []:
                        action (Function(update_bios_list), SetVariable("mphone_bios_app_exception",True),Hide("mphone_screen"),Show("mphone_bios_app_screen"))
                    else:
                        action (SetVariable("mphone_bios_app_exception",True),Hide("mphone_screen"),Show("mphone_bios_app_screen"))
                    xalign 0.5
                text "Bios" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if not "music" in disabled_apps:
                        idle "mphone_app_music"
                        hover "mphone_app_music_hover"
                        action Show("mphone_music_app_screen")
                    else:
                        idle "mphone_app_music_disabled"
                        hover "mphone_app_music_disabled"
                        action NullAction()
                    xalign 0.5
                text "Music" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if not "settings" in disabled_apps:
                        idle "mphone_app_settings"
                        hover "mphone_app_settings_hover"
                        action (SetVariable("mphone_current_input",""),SetVariable("settings_name",name),SetVariable("settings_rooster_nickname",roosterNickMCCustom),Show("mphone_settings_app_screen"))
                    else:
                        idle "mphone_app_settings_disabled"
                        hover "mphone_app_settings_disabled"
                        action NullAction()
                    xalign 0.5
                text "Settings" style "mphone_app_text_style" xalign 0.5
            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if not "vault" in disabled_apps:
                        if safe_new_renders:
                            idle "mphone_app_safe_new"
                            hover "mphone_app_safe_new_hover"
                        else:
                            idle "mphone_app_safe"
                            hover "mphone_app_safe_hover"
                        action (SetVariable("safe_new_renders",False),Show("mphone_vault_app_screen"))
                    else:
                        idle "mphone_app_safe_disabled"
                        hover "mphone_app_safe_disabled"
                        action NullAction()
                    xalign 0.5
                text "Vault" style "mphone_app_text_style" xalign 0.5

            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if persistent.chat_new_rewards:
                        idle "mphone_app_rewards_new"
                        hover "mphone_app_rewards_new_hover"
                    else:
                        idle "mphone_app_rewards"
                        hover "mphone_app_rewards_hover"
                    action (SetVariable("persistent.chat_new_rewards",False),SetVariable("chat_new_rewards",False),ShowMenu("rewards"))
                    xalign 0.5
                text "Rewards" style "mphone_app_text_style" xalign 0.5

            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    idle "mphone_app_scenes"
                    hover "mphone_app_scenes_hover"
                    action ShowMenu("scenes")
                    xalign 0.5
                text "Scenes" style "mphone_app_text_style" xalign 0.5

            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if not "2dart" in disabled_apps and currentEpisode >= 9:
                        if mphone_new_art_available:
                            idle "mphone_app_2d_art_new"
                            hover "mphone_app_2d_art_new_hover"
                        else:
                            idle "mphone_app_2d_art"
                            hover "mphone_app_2d_art_hover"
                        action (SetVariable("mphone_new_art_available",False), Function(setup_art_shop), Show("mphone_jacob_art_screen_main"))
                    else:
                        idle "mphone_app_2d_art_disabled"
                        hover "mphone_app_2d_art_disabled"
                        action NullAction()
                    xalign 0.5
                text "2D Art" style "mphone_app_text_style" xalign 0.5

            vbox:
                xminimum 80 * persistent.scale_factor
                imagebutton at mphone_app_zoom:
                    if pack_quest_available:
                        idle "mphone_app_pack_quest_new"
                        hover "mphone_app_pack_quest_new_hover"
                    else:
                        idle "mphone_app_pack_quest"
                        hover "mphone_app_pack_quest_hover"
                    if pack_quest_active:
                        action (Function(pq_check_tasks), Show("mphone_pack_quest_app_screen"))
                    else:
                        action Show("mphone_pack_quest_app_screen")
                    xalign 0.5
                text "Pack Quest" style "mphone_app_text_style" xalign 0.5

            if minigames:
                vbox:
                    xminimum 80 * persistent.scale_factor
                    imagebutton at mphone_app_zoom:
                        if not "brawler" in disabled_apps:
                            if bn_money_reward or bn_money_reward2 or bn_money_reward3 or bn_sr_reward:
                                idle "mphone_app_brawler_new"
                                hover "mphone_app_brawler_new_hover"
                            else:
                                idle "mphone_app_brawler"
                                hover "mphone_app_brawler_hover"
                            if currentEpisode < 10:
                                action Show("brawler_unavailable_screen")
                            else:
                                action (Hide("mphone_screen"),Jump("app_new_brawler_label"))
                        else:
                            idle "mphone_app_brawler_disabled"
                            hover "mphone_app_brawler_disabled"
                            action NullAction()
                        xalign 0.5
                    text "Brawler" style "mphone_app_text_style" xalign 0.5

                vbox:
                    xminimum 80 * persistent.scale_factor
                    imagebutton at mphone_app_zoom:
                        if not "shuffle" in disabled_apps:
                            if game_money_available:
                                idle "mphone_app_shuffle_new"
                                hover "mphone_app_shuffle_new_hover"
                            else:
                                idle "mphone_app_shuffle"
                                hover "mphone_app_shuffle_hover"
                            action (SetVariable("mphone_playing_shuffle", 0),Show("mphone_shuffle_screen"))
                        else:
                            idle "mphone_app_shuffle_disabled"
                            hover "mphone_app_shuffle_disabled"
                            action NullAction()
                        xalign 0.5
                    text "Shuffle" style "mphone_app_text_style" xalign 0.5

                vbox:
                    xminimum 80 * persistent.scale_factor
                    imagebutton at mphone_app_zoom:
                        if not "tripletile" in disabled_apps:
                            if triple_tile_money_available:
                                idle "mphone_app_tripletile_new"
                                hover "mphone_app_tripletile_new_hover"
                            else:
                                idle "mphone_app_tripletile"
                                hover "mphone_app_tripletile_hover"
                            action Show("mphone_triple_tile_screen")
                        else:
                            idle "mphone_app_tripletile_disabled"
                            hover "mphone_app_tripletile_disabled"
                            action NullAction()
                        xalign 0.5
                    text "Triple Tile" style "mphone_app_text_style" xalign 0.5

    if mphone_app_gallery_first_time and mphone_app_gallery_enabled:
        imagebutton:
            idle "mphone_app_gallery_tut"
            hover "mphone_app_gallery_tut"
            action SetVariable("mphone_app_gallery_first_time", False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

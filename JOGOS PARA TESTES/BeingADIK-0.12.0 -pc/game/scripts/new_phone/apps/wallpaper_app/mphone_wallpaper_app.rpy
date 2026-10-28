screen mphone_wallpaper_app_screen:
    tag mphone_wallpaper_app_screen
    modal True
    fixed:
        at mphone_app_transform
        if mphone_wallpaper_list[mphone_wallpaper_int][2]:
            add mphone_wallpaper_list[mphone_wallpaper_int][0]
        else:
            add "mphone_wallpaper_disabled"
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action Hide("mphone_wallpaper_app_screen")
    fixed:
        at mphone_app_transform
        add "mphone_fg"

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_wallpaper_app_screen")
            xalign 0.5
            yalign mphone_off_yalign

        hbox:
            xalign 0.5
            yalign 0.75
            spacing 330 * persistent.scale_factor
            imagebutton at mphone_rotate_90cw_zoom:
                idle "mphone_arrow_down_idle"
                hover "mphone_arrow_down_hover"
                if mphone_wallpaper_int == 0:
                    action SetVariable("mphone_wallpaper_int",len(mphone_wallpaper_list)-1)
                else:
                    action SetVariable("mphone_wallpaper_int",mphone_wallpaper_int-1)

            imagebutton at mphone_rotate_90cw_zoom:
                idle "mphone_arrow_up_idle"
                hover "mphone_arrow_up_hover"
                action NullAction()
                if mphone_wallpaper_int == len(mphone_wallpaper_list)-1:
                    action SetVariable("mphone_wallpaper_int",0)
                else:
                    action SetVariable("mphone_wallpaper_int",mphone_wallpaper_int+1)

        if mphone_wallpaper_list[mphone_wallpaper_int][2]:
            imagebutton:
                if mphone_wallpaper_list[mphone_wallpaper_int][1]:
                    idle "mphone_fav_active_idle"
                    hover "mphone_fav_active_hover"
                else:
                    idle "mphone_fav_inactive_idle"
                    hover "mphone_fav_inactive_hover"
                action SetDict(mphone_wallpaper_list[mphone_wallpaper_int],1,not mphone_wallpaper_list[mphone_wallpaper_int][1])
                xalign 0.6
                yalign 0.9

        vbox:
            xalign 0.489
            yalign 0.9
            xminimum 400 * persistent.scale_factor
            if mphone_wallpaper_list[mphone_wallpaper_int][2]:
                if mphone_wallpaper_int == mphone_current_wallpaper:
                    textbutton "Set as current wallpaper" text_style "mphone_wallpaper_text2_button_style" action (SetVariable("mphone_custom_wallpaper",""), SetVariable("mphone_current_wallpaper",mphone_wallpaper_int))
                else:
                    textbutton "Set as current wallpaper" text_style "mphone_wallpaper_text_button_style" action (SetVariable("mphone_custom_wallpaper",""), SetVariable("mphone_current_wallpaper",mphone_wallpaper_int))
            else:
                textbutton "Set as current wallpaper" text_style "mphone_wallpaper_text_button_style2" action NullAction()
            if mphone_use_favs:
                textbutton "Rotate favorite wallpapers: {color=#fe9416}Yes{/color}" text_style "mphone_wallpaper_text_button_style" action (SetVariable("mphone_custom_wallpaper",""),SetVariable("mphone_use_favs",not mphone_use_favs))
            else:
                textbutton "Rotate favorite wallpapers: No" text_style "mphone_wallpaper_text_button_style" action (SetVariable("mphone_custom_wallpaper",""),SetVariable("mphone_use_favs",not mphone_use_favs))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

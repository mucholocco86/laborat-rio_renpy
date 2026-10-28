screen mphone_gallery_app_screen:
    tag mphone_gallery_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_gallery_app_bg"
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    hbox:
        xalign 0.5
        yalign 0.06
        spacing 300 * persistent.scale_factor
        add "mphone_top_cakenet"
        add "mphone_top_icons"
    key "mouseup_2" action Hide("mphone_gallery_app_screen")
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_gallery_app_screen")
            xalign 0.5
            yalign mphone_off_yalign

        text "Gallery" style "mphone_gallery_header_style" xalign 0.5 yalign 0.10
    fixed:
        at mphone_app_transform
        vpgrid:
            draggable True
            mousewheel True
            cols 4
            xminimum 470 * persistent.scale_factor
            xmaximum 470 * persistent.scale_factor
            yminimum 820 * persistent.scale_factor
            ymaximum 820 * persistent.scale_factor
            xalign 0.515
            yalign 0.63
            spacing 10 * persistent.scale_factor

            for idx in range(0,len(mphone_app_gallery_photos_list)):
                imagebutton:
                    idle mphone_app_gallery_photos_list[idx] + "_mini"
                    hover mphone_app_gallery_photos_list[idx] + "_mini"
                    action Show("mphone_gallery_viewer_screen", idx=idx)
                    yoffset 10 * persistent.scale_factor
            for idx in range(0,4):
                imagebutton:
                    idle "gallery_empty"
                    hover "gallery_empty"
                    action NullAction()
                    yoffset 10 * persistent.scale_factor

    fixed:
        at mphone_app_transform
        add "mphone_fg"

    if mphone_app_wp_first_time:
        imagebutton:
            idle "custom_wallpaper_tutorial"
            hover "custom_wallpaper_tutorial"
            action SetVariable("mphone_app_wp_first_time", False)


screen mphone_gallery_viewer_screen:
    tag mphone_gallery_viewer_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action Hide("mphone_gallery_viewer_screen")
    add mphone_app_gallery_photos_list[idx]
    imagebutton:
        idle "credits_invis_button"
        hover "credits_invis_button"
        action Hide ("mphone_gallery_viewer_screen")

    hbox:
        xalign 0.99
        yalign 0.01
        if persistent.rewards_screen_on_hover:
            if "stupid_reward_pic" == mphone_app_gallery_photos_list[idx]:
                textbutton "Set as wallpaper" text_style "mphone_custom_wallpaper_style" action (SetVariable("mphone_custom_wallpaper_tmp_xpos", mphone_custom_wallpaper_get_start_xpos(mphone_app_gallery_photos_list[idx])),SetVariable("mphone_custom_wallpaper_tmp_ypos", 0), SetVariable("mphone_custom_wallpaper_tmp_zoom",0),Hide("mphone_gallery_viewer_screen"),Show("mphone_custom_wallpaper_screen", img="stupid_reward_picb", max_width=mphone_custom_wallpaper_get_width(mphone_app_gallery_photos_list[idx]))) at mphone_gallery_button_hide_transform
            else:
                textbutton "Set as wallpaper" text_style "mphone_custom_wallpaper_style" action (SetVariable("mphone_custom_wallpaper_tmp_xpos", mphone_custom_wallpaper_get_start_xpos(mphone_app_gallery_photos_list[idx])),SetVariable("mphone_custom_wallpaper_tmp_ypos", 0), SetVariable("mphone_custom_wallpaper_tmp_zoom",0),Hide("mphone_gallery_viewer_screen"),Show("mphone_custom_wallpaper_screen", img=mphone_app_gallery_photos_list[idx], max_width=mphone_custom_wallpaper_get_width(mphone_app_gallery_photos_list[idx]))) at mphone_gallery_button_hide_transform
        else:
            if "stupid_reward_pic" == mphone_app_gallery_photos_list[idx]:
                textbutton "Set as wallpaper" text_style "mphone_custom_wallpaper_style" action (SetVariable("mphone_custom_wallpaper_tmp_xpos", mphone_custom_wallpaper_get_start_xpos(mphone_app_gallery_photos_list[idx])),SetVariable("mphone_custom_wallpaper_tmp_ypos", 0), SetVariable("mphone_custom_wallpaper_tmp_zoom",0),Hide("mphone_gallery_viewer_screen"),Show("mphone_custom_wallpaper_screen", img="stupid_reward_picb", max_width=mphone_custom_wallpaper_get_width(mphone_app_gallery_photos_list[idx])))
            else:
                textbutton "Set as wallpaper" text_style "mphone_custom_wallpaper_style" action (SetVariable("mphone_custom_wallpaper_tmp_xpos", mphone_custom_wallpaper_get_start_xpos(mphone_app_gallery_photos_list[idx])),SetVariable("mphone_custom_wallpaper_tmp_ypos", 0), SetVariable("mphone_custom_wallpaper_tmp_zoom",0),Hide("mphone_gallery_viewer_screen"),Show("mphone_custom_wallpaper_screen", img=mphone_app_gallery_photos_list[idx], max_width=mphone_custom_wallpaper_get_width(mphone_app_gallery_photos_list[idx])))

    hbox:
        xalign 0.99
        yalign 0.99
        spacing 0
        imagebutton:
            if persistent.rewards_screen_on_hover:
                at mphone_gallery_button_hide_transform
            if idx == 0:
                idle Transform ("[persistent.img_dir]/rewards/general/rew_button_prev_disabled.png")
                hover Transform ("[persistent.img_dir]/rewards/general/rew_button_prev_disabled.png")
            else:
                idle Transform ("[persistent.img_dir]/rewards/general/rew_button_prev_idle.png")
                hover Transform ("[persistent.img_dir]/rewards/general/rew_button_prev_hover.png")
            xoffset 5 * persistent.scale_factor
            action SetScreenVariable("idx",max(idx-1,0))
        imagebutton:
            if persistent.rewards_screen_on_hover:
                at mphone_gallery_button_hide_transform
            if idx == len(mphone_app_gallery_photos_list)-1:
                idle Transform ("[persistent.img_dir]/rewards/general/rew_button_next_disabled.png")
                hover Transform ("[persistent.img_dir]/rewards/general/rew_button_next_disabled.png")
                action NullAction()
            else:
                idle Transform ("[persistent.img_dir]/rewards/general/rew_button_next_idle.png")
                hover Transform ("[persistent.img_dir]/rewards/general/rew_button_next_hover.png")
                action SetScreenVariable("idx",idx+1)

screen mphone_custom_wallpaper_screen(img, max_width):
    tag mphone_custom_wallpaper_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action Hide("mphone_custom_wallpaper_screen")
    fixed:
        at mphone_bg_transform

    fixed:
        at CustomWallpaperMask
        add img:
            ypos (55 - min(mphone_custom_wallpaper_tmp_ypos,(int) (1.29636 * (mphone_custom_wallpaper_tmp_zoom*1.00)))) * persistent.scale_factor
            xpos (min((int)(-960.0*((mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167) + 960.0) + (mphone_custom_wallpaper_tmp_xpos - (int)(((max_width * ((mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167)) - 470.0)/2.0)),(int)(-960.0*((mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167) + 960.0) + (((int)(max_width * ((mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167) - 470)) - (int)(((max_width * ((mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167)) - 470.0)/2.0)))) * persistent.scale_factor
            zoom (mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167

    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    add "mphone_fg"

    vbox:
        xalign 0.61
        yalign 0.125
        spacing 15 * persistent.scale_factor
        xoffset -2 * persistent.scale_factor
        imagebutton:
            idle "mphone_wp_ok_idle"
            hover "mphone_wp_ok_hover"
            action (SetVariable("mphone_custom_wallpaper",img),SetVariable("mphone_custom_wallpaper_max_width",max_width),SetVariable("mphone_custom_wallpaper_xpos",mphone_custom_wallpaper_tmp_xpos),SetVariable("mphone_custom_wallpaper_ypos",mphone_custom_wallpaper_tmp_ypos),SetVariable("mphone_custom_wallpaper_zoom",mphone_custom_wallpaper_tmp_zoom),Hide("mphone_custom_wallpaper_screen"))
        imagebutton:
            idle "mphone_wp_x_idle"
            hover "mphone_wp_x_hover"
            action Hide("mphone_custom_wallpaper_screen")

    hbox:
        xalign 0.5
        yalign 0.95
        spacing 5 * persistent.scale_factor
        imagebutton:
            yalign 0.5
            yoffset -2 * persistent.scale_factor
            idle "mphone_arrows_icon"
            hover "mphone_arrows_icon"
            action NullAction()
        if max_width == 1920:
            bar value VariableValue("mphone_custom_wallpaper_tmp_xpos", 1289 * persistent.scale_factor):
                yalign 0.5
                xalign 0.0
                xmaximum 360 * persistent.scale_factor
                ymaximum 15 * persistent.scale_factor
                style "my_bar"
        else:
            bar value VariableValue("mphone_custom_wallpaper_tmp_xpos", ((int)(max_width * ((mphone_custom_wallpaper_tmp_zoom * 0.0012) + 0.9167) - 470)) * persistent.scale_factor):
                yalign 0.5
                xalign 0.0
                xmaximum 360 * persistent.scale_factor
                ymaximum 15 * persistent.scale_factor
                style "my_bar"
    if (int) (1.29636 * (mphone_custom_wallpaper_tmp_zoom*1.00)) > 5.0:
        vbox:
            xalign 0.61
            yalign 0.67
            spacing 5 * persistent.scale_factor

            bar value VariableValue("mphone_custom_wallpaper_tmp_ypos", ((int) (1.29636 * (mphone_custom_wallpaper_tmp_zoom*1.00))) * persistent.scale_factor):
                xalign 0.5 yalign 0.0
                xmaximum 15 * persistent.scale_factor
                ymaximum 600 * persistent.scale_factor
                style "my_vbar"
            imagebutton:
                xalign 0.5
                xoffset -2 * persistent.scale_factor
                idle "mphone_arrows2_icon"
                hover "mphone_arrows2_icon"
                action NullAction()

    hbox:
        xalign 0.5
        yalign 0.07
        spacing 5 * persistent.scale_factor
        imagebutton:
            idle "mphone_magnify_icon"
            hover "mphone_magnify_icon"
            action NullAction()
        bar value VariableValue("mphone_custom_wallpaper_tmp_zoom", 100):
            xalign 0.0 yalign 0.0
            xmaximum 360 * persistent.scale_factor
            ymaximum 15 * persistent.scale_factor
            style "my_bar"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

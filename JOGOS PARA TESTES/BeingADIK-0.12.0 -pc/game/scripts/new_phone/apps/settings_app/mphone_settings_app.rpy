screen mphone_settings_app_screen:
    tag mphone_settings_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_settings_bg"
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
    fixed:
        at mphone_app_transform

        text "{size=+%d}Settings{/size}" % (5 * persistent.scale_factor) style "mphone_contacts_header_style" xalign 0.5 yalign 0.1

        imagebutton:
            idle "mphone_settings_profile"
            hover "mphone_settings_profile"
            action NullAction()
            xpos 740 * persistent.scale_factor
            ypos 150 * persistent.scale_factor

        text "Edit Profile Settings" style "mphone_settings_text_style" xpos 802 * persistent.scale_factor ypos 165 * persistent.scale_factor

        hbox:
            xpos 752 * persistent.scale_factor
            ypos 225 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Name" style "mphone_settings_text_style"

            if mphone_current_input == "name":
                input:
                    style "mphone_settings_textbutton2_style"
                    default "[settings_name]"
                    value VariableInputValue('settings_name')
                    length 12
                    allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _1234567890"
            else:
                textbutton "[settings_name]" text_style "mphone_settings_textbutton_style" action SetVariable("mphone_current_input","name") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor

        hbox:
            xpos 752 * persistent.scale_factor
            ypos 270 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Rooster Nickname" style "mphone_settings_text_style"

            if mphone_current_input == "rooster":
                input:
                    style "mphone_settings_textbutton2_style" default "[settings_rooster_nickname]" value VariableInputValue('settings_rooster_nickname') length 12
            else:
                textbutton "[settings_rooster_nickname]" text_style "mphone_settings_textbutton_style" action SetVariable("mphone_current_input","rooster") xoffset -6 * persistent.scale_factor yoffset -6 * persistent.scale_factor


        hbox:
            xpos 752 * persistent.scale_factor
            ypos 315 * persistent.scale_factor
            text "Avatar" style "mphone_settings_text_style"
        hbox:
            xalign 0.5
            ypos 360 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            for x in range(1,4):
                imagebutton:
                    if x != mphone_mc_avatar:
                        idle "mphone_avatar_mc%d" % x + "_idle"
                    else:
                        idle "mphone_avatar_mc%d" % x + "_hover"
                    hover "mphone_avatar_mc%d" % x + "_hover"
                    action (SetVariable("mphone_current_input",""),SetVariable("mphone_mc_avatar", x),SetVariable("mc_avatar","rooster_mini_mc%d" % x))

        imagebutton:
            idle "mphone_settings_dialtone"
            hover "mphone_settings_dialtone"
            action NullAction()
            xpos 740 * persistent.scale_factor
            ypos 470 * persistent.scale_factor

        text "Edit Notification Signal" style "mphone_settings_text_style" xpos 802 * persistent.scale_factor ypos 483 * persistent.scale_factor

        hbox:
            xpos 752 * persistent.scale_factor
            ypos 543 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Notifications" style "mphone_settings_text_style"
            if notifications:
                textbutton "On" text_style "mphone_settings_textbutton_style" action (SetVariable("mphone_current_input",""),SetVariable("notifications",not notifications)) yoffset -6 * persistent.scale_factor
            else:
                textbutton "Off" text_style "mphone_settings_textbutton_style" action (SetVariable("mphone_current_input",""),SetVariable("notifications",not notifications)) yoffset -6 * persistent.scale_factor

        hbox:
            xpos 752 * persistent.scale_factor
            ypos 588 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Signal" style "mphone_settings_text_style"
            textbutton "%s" % mphone_notifications[current_notification_sound][0] text_style "mphone_settings_textbutton_style" action (SetVariable("mphone_current_input",""),Function(mphone_change_notification)) yoffset -6 * persistent.scale_factor

        imagebutton:
            idle "mphone_settings_wallpaper"
            hover "mphone_settings_wallpaper"
            action NullAction()
            xpos 740 * persistent.scale_factor
            ypos 714 * persistent.scale_factor

        textbutton "Edit Wallpaper Settings" text_style "mphone_settings_textbutton_style2" xpos 802 * persistent.scale_factor ypos 725 * persistent.scale_factor action (Function(unlock_wallpapers_s2),SetVariable("mphone_current_input",""),Show("mphone_wallpaper_app_screen"))

        if persistent.golden_phone:
            hbox:
                xpos 752 * persistent.scale_factor
                ypos 790 * persistent.scale_factor
                spacing 10 * persistent.scale_factor
                text "Golden Phone Skin" style "mphone_settings_text_style"
                if persistent.golden_phone_skin_enabled:
                    textbutton "On" text_style "mphone_settings_textbutton_style" action (SetVariable("mphone_current_input",""),SetVariable("persistent.golden_phone_skin_enabled",not persistent.golden_phone_skin_enabled)) yoffset -6 * persistent.scale_factor
                else:
                    textbutton "Off" text_style "mphone_settings_textbutton_style" action (SetVariable("mphone_current_input",""),SetVariable("persistent.golden_phone_skin_enabled",not persistent.golden_phone_skin_enabled)) yoffset -6 * persistent.scale_factor


        imagebutton:
            idle "mphone_settings_petnames"
            hover "mphone_settings_petnames"
            action NullAction()
            xpos 740 * persistent.scale_factor
            ypos 645 * persistent.scale_factor

        textbutton "Edit Pet Names" text_style "mphone_settings_textbutton_style2" xpos 802 * persistent.scale_factor ypos 658 * persistent.scale_factor action (SetVariable("mphone_current_input",""),Show("mphone_pet_names_app_screen"))

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action (Function(mphone_settings_set_new_names), SetVariable("mphone_current_input",""),Hide("mphone_settings_app_screen"))
            xalign 0.5
            yalign mphone_off_yalign
    key "mouseup_2" action (Function(mphone_settings_set_new_names), SetVariable("mphone_current_input",""),Hide("mphone_settings_app_screen"))
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform
        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

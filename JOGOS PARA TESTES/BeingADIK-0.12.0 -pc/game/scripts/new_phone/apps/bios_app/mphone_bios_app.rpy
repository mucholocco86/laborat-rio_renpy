screen mphone_bios_app_screen():
    tag mphone_bios_app_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_big_transform2
        add "mphone_bios_app_bg"
    fixed:
        at mphone_app_big_transform


        if mphone_bios_chars_list[mphone_current_bios_char][0] == "You":
            add "mphone_bios_big_mc%d" % mphone_mc_avatar
        else:
            add "mphone_bios_big_" + mphone_bios_chars_list[mphone_current_bios_char][0].lower().replace(" ","")

        imagebutton:
            idle "phone_app_bios"
            hover "phone_app_bios"
            action NullAction()
            xalign 0.115
            yalign 0.214

        text "Bios" style "mphone_bios_header2_style" xalign 0.172 yalign 0.216

        hbox:
            xalign 0.45 yalign 0.216
            text "Profile:" style "mphone_bios_header2_style" xalign 0.0
        hbox:
            xalign 0.0
            xpos 1000 * persistent.scale_factor
            yalign 0.216
            text "%s" % mphone_bios_chars_list[mphone_current_bios_char][0] style "mphone_bios_header_style"

        hbox:
            textbutton "{color=fe9416}Filter by:{/color} %s" % mphone_bios_sort_by[mphone_bios_sort_by_idx]:
                text_style "mphone_bios_small_style"
                xalign 0.0
                ypos 870 * persistent.scale_factor
                xpos 210 * persistent.scale_factor
                xminimum 500 * persistent.scale_factor
                action Function(mphone_bios_change_sort_filter)

        add "mphone_bios_transparent"
        vpgrid:
            xpos 253 * persistent.scale_factor
            ypos 320 * persistent.scale_factor
            draggable True
            mousewheel True
            cols 10
            xminimum 1049 * persistent.scale_factor
            xmaximum 1049 * persistent.scale_factor
            yminimum 535 * persistent.scale_factor
            ymaximum 535 * persistent.scale_factor
            scrollbars "vertical"


            for x in range(0,len(mphone_bios_chars_list)):
                $ tmpBool = False
                if mphone_bios_sort_by_idx == 0:
                    $ tmpBool = True
                else:
                    for y in mphone_bios_chars_list[x][1]:
                        if y == mphone_bios_sort_by_idx:
                            $ tmpBool = True
                if tmpBool:
                    imagebutton:
                        if mphone_bios_chars_list[x][0] == "You":
                            if mphone_bios_chars_list[x][4]:
                                idle "mmbios_mc%d_new" % mphone_mc_avatar
                                hover "mmbios_mc%d_new_hover" % mphone_mc_avatar
                            else:
                                idle "mmbios_mc%d" % mphone_mc_avatar
                                hover "mmbios_mc%d_hover" % mphone_mc_avatar
                        else:
                            if mphone_bios_chars_list[x][4]:
                                idle "mmbios_" + mphone_bios_chars_list[x][0].lower().replace(" ","") + "_new"
                                hover "mmbios_" + mphone_bios_chars_list[x][0].lower().replace(" ","") + "_new_hover"
                            else:
                                idle "mmbios_" + mphone_bios_chars_list[x][0].lower().replace(" ","")
                                hover "mmbios_" + mphone_bios_chars_list[x][0].lower().replace(" ","") + "_hover"
                        hovered SetVariable("mphone_current_bios_char", x)
                        action Show("mphone_bios_char_screen")


    fixed:
        at mphone_app_big_transform2
        if persistent.golden_phone and persistent.golden_phone_skin_enabled:
            add "mphone_big_shell_gold"
        else:
            add "mphone_big_shell"
        add "mphone_bios_app_fg"
        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action (Function(check_if_new_bio),Show("mphone_screen"),Hide("mphone_bios_app_screen"))
            xalign 0.95
            yalign 0.5
    key "mouseup_2" action (Function(check_if_new_bio),Show("mphone_screen"),Hide("mphone_bios_app_screen"))

screen mphone_bios_char_screen:
    tag mphone_bios_char_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_bios_bg_transform
        add "mphone_bios_app_bg"

        if mphone_bios_chars_list[mphone_current_bios_char][0] == "You":
            add "mphone_bios_big_mc%s" % mphone_mc_avatar
        else:
            add "mphone_bios_big_" + mphone_bios_chars_list[mphone_current_bios_char][0].lower().replace(" ","")
    fixed:
        at mphone_bios_text_transform
        hbox:
            xalign 0.45 yalign 0.216
            text "Profile:" style "mphone_bios_header2_style" xalign 0.0
        hbox:
            xalign 0.0
            xpos 1000 * persistent.scale_factor
            yalign 0.216
            text "%s" % mphone_bios_chars_list[mphone_current_bios_char][0] style "mphone_bios_header_style"
    fixed:
        at mphone_bios_box_transform
        add "mphone_bios_char_bg"
        hbox:
            xalign 0.28
            yalign 0.315
            xmaximum 1130 * persistent.scale_factor
            xminimum 1130 * persistent.scale_factor
            text "%s" % mphone_bios_chars_list[mphone_current_bios_char][2] style "mphone_bios_char_text_style"
        hbox:
            xalign 0.28
            xmaximum 1180 * persistent.scale_factor
            xminimum 1180 * persistent.scale_factor

            vpgrid:
                ypos 393 * persistent.scale_factor
                xpos 25 * persistent.scale_factor
                draggable True
                mousewheel True
                cols 1
                xminimum 1180 * persistent.scale_factor
                xmaximum 1180 * persistent.scale_factor
                yminimum 538 * persistent.scale_factor
                ymaximum 538 * persistent.scale_factor
                scrollbars "vertical"
                if len(mphone_bios_chars_list[mphone_current_bios_char][3]) < 8:
                    yinitial 0.0
                else:
                    yinitial 1.0

                vbox:
                    xmaximum 1100 * persistent.scale_factor
                    xminimum 1100 * persistent.scale_factor
                    yminimum 50 * persistent.scale_factor
                    text getBioText() style "mphone_bios_char_text_style"

    fixed:
        at mphone_bios_bg_transform
        if persistent.golden_phone and persistent.golden_phone_skin_enabled:
            add "mphone_big_shell_gold"
        else:
            add "mphone_big_shell"
        add "mphone_bios_app_fg"
        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action (SetDict(mphone_bios_chars_list[mphone_current_bios_char],4,0),Hide("mphone_bios_char_screen"))
            xalign 0.95
            yalign 0.5
    key "mouseup_2" action (SetDict(mphone_bios_chars_list[mphone_current_bios_char],4,0),Hide("mphone_bios_char_screen"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen mphone_contacts_app_screen:
    tag mphone_contacts_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_contacts_app_bg"
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
    key "mouseup_2" action Hide("mphone_contacts_app_screen")
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_contacts_app_screen")
            xalign 0.5
            yalign mphone_off_yalign

        hbox:
            xalign 0.5
            yalign 0.08
            spacing 100 * persistent.scale_factor
            imagebutton:
                yoffset 20 * persistent.scale_factor
                if mphone_notification_count == 0:
                    idle "mphone_contacts_no_notifications"
                    hover "mphone_contacts_no_notifications"
                else:
                    idle "mphone_contacts_new_notifications"
                    hover "mphone_contacts_new_notifications"
                action NullAction()
            imagebutton:
                idle "mphone_avatar_mc%d" % mphone_mc_avatar + "_idle"
                hover "mphone_avatar_mc%d" % mphone_mc_avatar + "_idle"
                action NullAction()
                yoffset -5 * persistent.scale_factor
            imagebutton:
                yoffset 20 * persistent.scale_factor
                idle "mphone_contacts_edit_button_idle"
                hover "mphone_contacts_edit_button_idle"
                action NullAction()
        imagebutton:
            idle "mphone_contacts_online"
            hover "mphone_contacts_online"
            action NullAction()
            xalign 0.518
            yalign 0.135
            yoffset -5 * persistent.scale_factor
        if mphone_notification_count > 0:
            text "%d" % mphone_notification_count style "mphone_contacts_notification_style" xalign 0.413 yalign 0.078 yoffset 20 * persistent.scale_factor

        text "Contacts" style "mphone_contacts_header_style" xalign 0.5 yalign 0.17
    fixed:
        at mphone_app_transform
        vpgrid:
            draggable True
            mousewheel True
            cols 1
            xminimum 470 * persistent.scale_factor
            xmaximum 470 * persistent.scale_factor
            yminimum 773 * persistent.scale_factor
            ymaximum 773 * persistent.scale_factor
            xalign 0.50
            yalign 0.685
            xoffset 1 * persistent.scale_factor

            if mphone_notification_count > 0:
                vbox:
                    yminimum 65 * persistent.scale_factor
                    ymaximum 65 * persistent.scale_factor
                    yalign 0.5
                    text "Online now" style "mphone_contacts_header2_style" xalign 0.08 yalign 0.5
                    imagebutton:
                        idle "mphone_contacts_orange_separator"
                        hover "mphone_contacts_orange_separator"
                        action NullAction()
                        yalign 0.5
                $ i = 0
                for x in mphone_contact_list:
                    if (x[1] != "NONE" or x[2]) and x[1].find("_shop") == -1:
                        vbox:
                            yminimum 65 * persistent.scale_factor
                            ymaximum 65 * persistent.scale_factor
                            yalign 0.5
                            hbox:
                                xoffset 20 * persistent.scale_factor
                                xalign 0.0
                                spacing 15 * persistent.scale_factor
                                imagebutton at mphone_contacts_avatar_zoom:
                                    idle "mphone_avatar_"+ x[0].lower().replace(" ","") + "_idle"
                                    hover "mphone_avatar_"+ x[0].lower().replace(" ","") + "_idle"
                                    action NullAction()
                                    yalign 0.4
                                hbox:
                                    xminimum 200 * persistent.scale_factor
                                    xmaximum 200 * persistent.scale_factor
                                    yalign 0.5
                                    text "%s" % x[0] style "mphone_contacts_text_style" xalign 0.0 yalign 0.5
                                hbox:
                                    yalign 0.5
                                    spacing 10 * persistent.scale_factor
                                    xoffset 7 * persistent.scale_factor
                                    imagebutton at mphone_contacts_button_zoom:
                                        yalign 0.5
                                        xalign 1.0
                                        if x[1] != "NONE":
                                            idle "contacts_call_idle"
                                            hover "contacts_call_hover"
                                            if x[1].find("_loop") == -1:
                                                action (SetVariable("phone_opened",False),SetDict(x,1,"NONE"),Hide("mphone_contacts_app_screen"),Hide("mphone_screen"),Hide("new_phone_screen"),SetVariable("currentEvent",x[1]),SetVariable("_game_menu_screen","save"),Jump("startEvent"))
                                            else:
                                                action (SetVariable("phone_opened",False),Hide("mphone_contacts_app_screen"),Hide("mphone_screen"),Hide("new_phone_screen"),SetVariable("currentEvent",x[1]),SetVariable("_game_menu_screen","save"),Jump("startEvent"))
                                        else:
                                            idle "contacts_call_disabled"
                                            hover "contacts_call_disabled"
                                            action NullAction()
                                    imagebutton at mphone_contacts_button_zoom:
                                        yalign 0.5
                                        xalign 1.0
                                        if x[2]:
                                            idle "contacts_chat_new_idle"
                                            hover "contacts_chat_new_hover"
                                        else:
                                            idle "contacts_chat_idle"
                                            hover "contacts_chat_hover"
                                        action (Show("mphone_chat_screen",arg=x,idx=i),Function(mphone_chat_handle_replies,i))
                            imagebutton:
                                yalign 0.5
                                idle "mphone_contacts_gray_separator"
                                hover "mphone_contacts_gray_separator"
                                action NullAction()
                    $ i += 1

            if mphone_shop_active:
                vbox:
                    yminimum 65 * persistent.scale_factor
                    ymaximum 65 * persistent.scale_factor
                    yalign 0.5
                    text "Shops" style "mphone_contacts_header2_style" xalign 0.08 yalign 0.5
                    imagebutton:
                        idle "mphone_contacts_orange_separator"
                        hover "mphone_contacts_orange_separator"
                        action NullAction()
                        yalign 0.5
                $ i = 0
                for x in mphone_contact_list:
                    if x[1].find("_shop") != -1:
                        if x[1] != "NONE":
                            vbox:
                                yminimum 65 * persistent.scale_factor
                                ymaximum 65 * persistent.scale_factor
                                yalign 0.5
                                hbox:
                                    xoffset 20 * persistent.scale_factor
                                    xalign 0.0
                                    spacing 15 * persistent.scale_factor
                                    imagebutton at mphone_contacts_avatar_zoom:
                                        idle "mphone_avatar_"+ x[0].lower().replace(" ","") + "_idle"
                                        hover "mphone_avatar_"+ x[0].lower().replace(" ","") + "_idle"
                                        action NullAction()
                                        yalign 0.4
                                    hbox:
                                        xminimum 200 * persistent.scale_factor
                                        xmaximum 200 * persistent.scale_factor
                                        yalign 0.5
                                        text "%s" % x[0] style "mphone_contacts_text_style" xalign 0.0 yalign 0.5
                                    hbox:
                                        yalign 0.5
                                        spacing 10 * persistent.scale_factor
                                        xoffset 7 * persistent.scale_factor
                                        imagebutton at mphone_contacts_button_zoom:
                                            yalign 0.5
                                            xalign 1.0
                                            idle "contacts_call_idle"
                                            hover "contacts_call_hover"
                                            action (SetVariable("phone_opened",False),Hide("mphone_contacts_app_screen"),Hide("mphone_screen"),Hide("new_phone_screen"),SetVariable("currentEvent",x[1]),SetVariable("_game_menu_screen","save"),Jump("startEvent"))
                                        imagebutton at mphone_contacts_button_zoom:
                                            yalign 0.5
                                            xalign 1.0
                                            if x[2]:
                                                idle "contacts_chat_new_idle"
                                                hover "contacts_chat_new_hover"
                                            else:
                                                idle "contacts_chat_idle"
                                                hover "contacts_chat_hover"
                                            action (Show("mphone_chat_screen",arg=x,idx=i),Function(mphone_chat_handle_replies,i))
                                imagebutton:
                                    yalign 0.5
                                    idle "mphone_contacts_gray_separator"
                                    hover "mphone_contacts_gray_separator"
                                    action NullAction()
                    $ i += 1

            vbox:
                yminimum 65 * persistent.scale_factor
                ymaximum 65 * persistent.scale_factor
                yalign 0.5
                text "People" style "mphone_contacts_header2_style" xalign 0.08 yalign 0.5
                imagebutton:
                    yalign 0.5
                    idle "mphone_contacts_orange_separator"
                    hover "mphone_contacts_orange_separator"
                    action NullAction()
            $ i = 0
            for x in mphone_contact_list:
                vbox:
                    yminimum 65 * persistent.scale_factor
                    ymaximum 65 * persistent.scale_factor
                    yalign 0.5
                    hbox:
                        xoffset 20 * persistent.scale_factor
                        xalign 0.0
                        spacing 15 * persistent.scale_factor
                        imagebutton at mphone_contacts_avatar_zoom:
                            yalign 0.4
                            idle "mphone_avatar_"+ x[0].lower().replace(" ","") + "_idle"
                            hover "mphone_avatar_"+ x[0].lower().replace(" ","") + "_idle"
                            action NullAction()
                        hbox:
                            xminimum 200 * persistent.scale_factor
                            xmaximum 200 * persistent.scale_factor
                            yalign 0.5
                            text "%s" % x[0] style "mphone_contacts_text_style" xalign 0.0 yalign 0.5

                        hbox:
                            yalign 0.5
                            spacing 10 * persistent.scale_factor
                            xoffset 7 * persistent.scale_factor
                            imagebutton at mphone_contacts_button_zoom:
                                yalign 0.5
                                if x[1] != "NONE":
                                    idle "contacts_call_idle"
                                    hover "contacts_call_hover"
                                    if x[1].find("_shop") == -1 and x[1].find("_loop") == -1:
                                        action (SetVariable("phone_opened",False),SetDict(x,1,"NONE"),Hide("mphone_contacts_app_screen"),Hide("mphone_screen"),SetVariable("currentEvent",x[1]),SetVariable("_game_menu_screen","save"),Jump("startEvent"))
                                    else:
                                        action (SetVariable("phone_opened",False),Hide("mphone_contacts_app_screen"),Hide("mphone_screen"),SetVariable("currentEvent",x[1]),SetVariable("_game_menu_screen","save"),Jump("startEvent"))
                                else:
                                    idle "contacts_call_disabled"
                                    hover "contacts_call_disabled"
                                    action NullAction()
                            imagebutton at mphone_contacts_button_zoom:
                                yalign 0.5
                                if x[2]:
                                    idle "contacts_chat_new_idle"
                                    hover "contacts_chat_new_hover"
                                else:
                                    idle "contacts_chat_idle"
                                    hover "contacts_chat_hover"
                                if x[0].lower().replace(" ","") in disabled_contacts_list:
                                    action NullAction()
                                else:
                                    action (Show("mphone_chat_screen",arg=x,idx=i),Function(mphone_chat_handle_replies,i))
                    imagebutton:
                        yalign 0.5
                        idle "mphone_contacts_gray_separator"
                        hover "mphone_contacts_gray_separator"
                        action NullAction()
                $ i += 1
    fixed:
        at mphone_app_transform
        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc








init -1 python:
    phone_position_x = 0.215
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")

    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")

    def print_bonjour():
        print("bonjour")

    def phone_contact_name(dialogue):
        """Returns the latest person in the thread who is not the player."""
        player_name = getattr(renpy.store, "MC_Name", "")
        
        for entry in reversed(dialogue):
            if entry.who and entry.who != player_name:
                return entry.who
        
        open_thread = getattr(renpy.store, "open_text", "")
        if open_thread:
            return open_thread
        
        return "Messages"

    def phone_contact_icon(dialogue):
        contact_name = phone_contact_name(dialogue)
        icons = getattr(renpy.store, "character_icons", {})
        return icons.get(contact_name, "gui/phone_received_icon.png")

    def phone_route_accent():
        if getattr(renpy.store, "supergood", False):
            return "#E6EDF3"
        if getattr(renpy.store, "superevil", False):
            return "#62F2F4"
        if getattr(renpy.store, "evil", False):
            return "#D94A52"
        if getattr(renpy.store, "sexaddict", False):
            return "#B767E3"
        if getattr(renpy.store, "good", False):
            return "#3CDFFF"
        return "#7CCBD9"


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign


transform phone_appear(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign
    on show:
        alpha 0.0
        xoffset -110
        easeout 0.34 alpha 1.0 xoffset 0


transform message_appear(pDirection):
    alpha 0.0
    xoffset 54 * pDirection
    yoffset 12
    parallel:
        easeout 0.28 alpha 1.0
    parallel:
        easeout_back 0.34 xoffset 0 yoffset 0


transform message_appear_icon:
    alpha 0.0
    zoom 0.76
    easeout_back 0.34 alpha 1.0 zoom 1.0


transform message_narrator:
    alpha 0.0
    yoffset -22
    easeout 0.28 alpha 1.0 yoffset 0


transform messenger_online_pulse:
    alpha 1.0
    zoom 1.0
    ease 0.75 alpha 0.55 zoom 0.86
    ease 0.75 alpha 1.0 zoom 1.0
    repeat


transform messenger_reply_motion:
    subpixel True
    on idle:
        easeout 0.12 xoffset 0
    on hover:
        easeout 0.12 xoffset 12


transform messenger_proxy_hidden:
    alpha 0.0


screen PhoneDialogue(dialogue, items=None):
    style_prefix "phoneFrame"

    $ phone_items = items or []
    $ contact_name = phone_contact_name(dialogue)
    $ contact_icon = phone_contact_icon(dialogue)
    $ route_accent = phone_route_accent()
    $ money_amount = getattr(renpy.store, "player_money", 0)
    $ reply_content_height = max(0, len(phone_items) * 122 - 10)
    $ reply_panel_height = min(930, 72 + reply_content_height) if phone_items else 0
    $ reply_panel_bottom = 1918
    $ reply_panel_top = reply_panel_bottom - reply_panel_height
    $ message_view_height = max(700, reply_panel_top - 250) if phone_items else 1650

    frame:
        at phone_transform(phone_position_x, phone_position_y)
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)

        background None
        xysize (1280, 1940)





        fixed:
            xpos -4
            ypos -4
            xysize (1, 1)
            clipping True

            for proxy_entry in dialogue:
                if proxy_entry.who is not None:
                    text proxy_entry.who:
                        id proxy_entry.who_id
                        at messenger_proxy_hidden

                text proxy_entry.what:
                    id proxy_entry.what_id
                    at messenger_proxy_hidden



        add Solid(route_accent):
            xpos 0
            ypos 198
            xsize 3
            ysize 1718
            alpha 0.34

        add Solid(route_accent):
            xpos 0
            ypos 198
            xsize 110
            ysize 3
            alpha 0.34


        add "gui/ui_refresh/messenger/header.png":
            xpos 50
            ypos 18

        frame:
            style "messenger_header_avatar"
            xpos 78
            ypos 42

            add contact_icon:
                xalign 0.5
                yalign 0.5
                xysize (96, 96)
                fit "cover"

        vbox:
            xpos 232
            ypos 54
            spacing 2

            text contact_name:
                style "messenger_contact_name"

            hbox:
                spacing 13

                text "●":
                    size 23
                    color route_accent
                    yoffset -2
                    at messenger_online_pulse

                text _("ACTIVE NOW"):
                    style "messenger_contact_status"

        text _("MESSAGES  //  PRIVATE THREAD"):
            xpos 232
            ypos 146
            style "messenger_thread_label"

        frame:
            style "messenger_money_chip"
            xpos 824
            ypos 66

            text "$ {:,}".format(money_amount):
                style "messenger_money_text"



        viewport:
            id "phone_message_view"
            xpos 64
            ypos 226
            xsize 1160
            ysize message_view_height
            draggable True
            mousewheel True
            pagekeys True
            yinitial 1.0

            has vbox
            xsize 1120
            spacing 18

            null height 12
            use nvl_phonetext(dialogue)
            null height 34



        vbar:
            value YScrollValue("phone_message_view")
            xpos 1235
            ypos 250
            ysize message_view_height - 44
            style "messenger_vscrollbar"



        if phone_items:
            frame:
                xpos 58
                ypos reply_panel_top
                xsize 1168
                ysize reply_panel_height
                background None

                text _("QUICK REPLIES"):
                    xpos 18
                    ypos 0
                    style "messenger_reply_label"

                add Solid(route_accent):
                    xpos 235
                    ypos 20
                    xsize 840
                    ysize 2
                    alpha 0.52

                viewport:
                    xpos 16
                    ypos 54
                    xsize 1140
                    ysize reply_panel_height - 62
                    draggable True
                    mousewheel True
                    pagekeys True
                    yinitial 0.0

                    has vbox
                    id "menu"
                    spacing 10

                    for reply_index, item in enumerate(phone_items):
                        $ reply_enabled = (item.action is not None) and item.action.get_sensitive()

                        button:
                            action item.action
                            sensitive reply_enabled
                            style "messenger_reply_button"
                            at messenger_reply_motion

                            has fixed
                            xysize (1120, 112)

                            add Solid(route_accent):
                                xpos 8
                                ypos 16
                                xsize 5
                                ysize 80
                                alpha 0.82

                            text "{:02d}".format(reply_index + 1):
                                xpos 38
                                yalign 0.5
                                style "messenger_reply_number"

                            text item.caption:
                                xpos 120
                                xsize 900
                                yalign 0.5
                                style "messenger_reply_text"

                            text "›":
                                xpos 1052
                                yalign 0.46
                                style "messenger_reply_arrow"


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None

    for id_d, d in enumerate(dialogue):
        if d.who is None:
            frame:
                xalign 0.5
                xmaximum 780
                padding (34, 20)
                background Frame(
                    "gui/ui_refresh/messenger/narrator_note.png",
                    28, 28, 28, 28
                )

                if d.current:
                    at message_narrator

                text d.what:
                    xmaximum 710
                    text_align 0.5
                    slow_cps False
                    style "messenger_narrator_text"

        else:
            $ is_player_message = d.who == MC_Name
            $ is_group_start = previous_d_who != d.who
            $ message_alignment = 1.0 if is_player_message else 0.0
            $ message_direction = 1 if is_player_message else -1

            if is_player_message:
                $ message_frame = "gui/ui_refresh/messenger/bubble_outgoing.png"



                $ message_icon = "phone_send_icon.png"
            elif d.who == "Love Match":
                $ message_frame = "gui/ui_refresh/messenger/bubble_love.png"
                $ message_icon = character_icons.get(d.who, "gui/phone_received_icon.png")
            else:
                $ message_frame = "gui/ui_refresh/messenger/bubble_incoming.png"
                $ message_icon = character_icons.get(d.who, "gui/phone_received_icon.png")

            hbox:
                xalign message_alignment
                spacing 18
                box_reverse is_player_message

                if is_group_start:
                    frame:
                        style "messenger_message_avatar"
                        yoffset 36

                        if d.current:
                            at message_appear_icon

                        add message_icon:
                            xalign 0.5
                            yalign 0.5
                            xysize (82, 82)
                            fit "cover"
                else:
                    null width 108

                vbox:
                    xmaximum 900
                    spacing 6

                    if is_group_start:
                        text d.who:
                            xalign message_alignment
                            style "messenger_sender_name"
                            color godson_name_color_for(d.who)

                    frame:
                        xminimum 440
                        xmaximum 870
                        padding (38, 25)
                        background Frame(message_frame, 38, 38, 38, 38)

                        if d.current:
                            at message_appear(message_direction)

                        text d.what:
                            xmaximum 794
                            xalign 0.0
                            text_align 0.0
                            slow_cps False
                            style "messenger_message_text"

                    if d.current:
                        text (_("DELIVERED  •  NOW") if is_player_message else _("NOW")):
                            xalign message_alignment
                            style "messenger_delivery_text"

        $ previous_d_who = d.who


style phoneFrame_frame:
    xsize 1280
    ysize 1940
    background None


style messenger_header_avatar is empty:
    xysize (132, 132)
    padding (18, 18)
    background None


style messenger_contact_name is text:
    font "fonts/nexa-bold.otf"
    size 52
    color "#FFFFFF"
    outlines [(3, "#000000C8", 0, 2)]


style messenger_contact_status is text:
    font "fonts/nexa-bold.otf"
    size 24
    color "#8DEAFF"
    kerning 2


style messenger_thread_label is text:
    font "fonts/nexa-bold.otf"
    size 20
    color "#9FB0B7"
    kerning 2


style messenger_money_chip is empty:
    xysize (300, 86)
    padding (28, 10)
    background "gui/ui_refresh/messenger/money_chip.png"


style messenger_money_text is text:
    xalign 0.5
    yalign 0.5
    font "fonts/nexa-bold.otf"
    size 34
    color "#FFFFFF"
    outlines [(2, "#000000B0", 0, 1)]


style messenger_message_avatar is empty:
    xysize (108, 108)
    padding (13, 13)
    background None


style messenger_sender_name is text:
    font "fonts/nexa-bold.otf"
    size 31
    color "#F2F7F9"
    outlines [(3, "#000000D0", 0, 2)]


style messenger_message_text is text:
    font "fonts/VioletSans-Regular.otf"
    size 43
    color "#FFFFFF"
    line_spacing 4
    outlines [(2, "#00000080", 0, 1)]


style messenger_delivery_text is text:
    font "fonts/nexa-bold.otf"
    size 18
    color "#8CC9D5"
    kerning 2
    outlines [(2, "#000000A0", 0, 1)]


style messenger_narrator_text is text:
    font "fonts/VioletSans-Regular.otf"
    size 29
    color "#D5E2E6"
    italic True
    line_spacing 3
    outlines [(2, "#000000A0", 0, 1)]


style messenger_reply_label is text:
    font "fonts/nexa-bold.otf"
    size 24
    color "#A9DCE5"
    kerning 3
    outlines [(2, "#000000A0", 0, 1)]


style messenger_reply_button is button:
    xysize (1120, 112)
    background "gui/ui_refresh/messenger/reply_idle.png"
    hover_background "gui/ui_refresh/messenger/reply_hover.png"
    selected_background "gui/ui_refresh/messenger/reply_selected.png"
    insensitive_background "gui/ui_refresh/messenger/reply_insensitive.png"
    padding (0, 0)


style messenger_reply_text is text:
    font "fonts/Louis George Cafe Bold.ttf"
    size 36
    color "#EDF5F7"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    insensitive_color "#777F83"
    line_spacing 2
    outlines [(2, "#000000A8", 0, 1)]


style messenger_reply_number is text:
    font "fonts/nexa-bold.otf"
    size 26
    color "#72DDEF"
    hover_color "#B1F4FF"
    selected_color "#FFFFFF"
    insensitive_color "#626B6F"
    outlines [(2, "#000000A8", 0, 1)]


style messenger_reply_arrow is text:
    font "fonts/nexa-bold.otf"
    size 54
    color "#69D8EC"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    insensitive_color "#626B6F"
    outlines [(2, "#000000A8", 0, 1)]


style messenger_vscrollbar is vscrollbar:
    xsize 7
    base_bar Solid("#4B687040")
    thumb Solid("#64DFF0B8")
    unscrollable "hide"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

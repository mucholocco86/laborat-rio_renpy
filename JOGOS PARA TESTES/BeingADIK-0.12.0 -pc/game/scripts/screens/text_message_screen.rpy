screen text_message_screen:
    tag text_message_screen
    modal False
    vbox:
        if currentEpisode > 8:
            xalign 0.02
        else:
            xalign 0.05
        yoffset 100 * persistent.scale_factor
        spacing 50 * persistent.scale_factor
        xminimum 600 * persistent.scale_factor
        xmaximum 600 * persistent.scale_factor

        if currentEpisode > 8:
            for x in range(tmpInt2,tmpInt+1):
                hbox at text_message_pop_up_transform:
                    spacing 20 * persistent.scale_factor
                    imagebutton:
                        if text_message_screen_list[x][0] == name:
                            idle "screen_text_avatar_mc2"
                            hover "screen_text_avatar_mc2"
                        else:
                            idle "screen_text_avatar_" + text_message_screen_list[x][0].lower()
                            hover "screen_text_avatar_" + text_message_screen_list[x][0].lower()
                        action NullAction()
                        yalign 0.0
                    frame:
                        if text_message_screen_list[x][2]:
                            xmaximum 400 * persistent.scale_factor
                            xpadding 20 * persistent.scale_factor
                            ypadding 20 * persistent.scale_factor
                            yoffset -5 * persistent.scale_factor
                            background Frame("screen_text_message_them",10 * persistent.scale_factor,10 * persistent.scale_factor)
                        else:
                            xmaximum 400 * persistent.scale_factor
                            xpadding 20 * persistent.scale_factor
                            ypadding 20 * persistent.scale_factor
                            yoffset -5 * persistent.scale_factor
                            background Frame("screen_text_message_you",10 * persistent.scale_factor,10 * persistent.scale_factor)
                        if text_message_screen_list[x][1][0:5] != "chat_":
                            vbox:
                                if mphone_get_chat_str(text_message_screen_list[x][1]) != "":
                                    if text_message_screen_list[x][2]:
                                        text "{color=2b2b2b}{b}%s{/b}\n%s{/color}" % (text_message_screen_list[x][0],mphone_get_chat_str(text_message_screen_list[x][1])) style "text_message_screen_style" text_align 0.0
                                    else:
                                        text "{b}%s{/b}\n%s" % (text_message_screen_list[x][0],mphone_get_chat_str(text_message_screen_list[x][1])) style "text_message_screen_style" text_align 0.0
                                else:
                                    if text_message_screen_list[x][2]:
                                        text "{color=2b2b2b}{b}%s{/b}{/color}" % text_message_screen_list[x][0] style "text_message_screen_style" text_align 0.0
                                    else:
                                        text "{b}%s{/b}" % text_message_screen_list[x][0] style "text_message_screen_style" text_align 0.0
                                hbox:
                                    for i in mphones_emotes:
                                        if i[1]:
                                            imagebutton:
                                                idle i[0]
                                                hover i[0]
                                                yminimum 24 * persistent.scale_factor
                                                ymaximum 24 * persistent.scale_factor
                                                action NullAction()
                        else:
                            imagebutton:
                                idle text_message_screen_list[x][1]
                                hover text_message_screen_list[x][1]+"_hover"
                                action (Show(text_message_screen_list[x][1].split("_thumb")[0]+"_screen"))
        else:
            for x in range(0,tmpInt+1):
                hbox at text_message_pop_up_transform:
                    spacing 20 * persistent.scale_factor
                    imagebutton:
                        if text_message_screen_list[x][0] == name:
                            idle "screen_text_avatar_mc"
                            hover "screen_text_avatar_mc"
                        else:
                            idle "screen_text_avatar_" + text_message_screen_list[x][0].lower()
                            hover "screen_text_avatar_" + text_message_screen_list[x][0].lower()
                        action NullAction()
                        yalign 0.0
                    frame:
                        if text_message_screen_list[x][2]:
                            xmaximum 500 * persistent.scale_factor
                            xpadding 20 * persistent.scale_factor
                            ypadding 20 * persistent.scale_factor
                            yoffset -5 * persistent.scale_factor
                            background Frame("screen_text_message_them",10 * persistent.scale_factor,10 * persistent.scale_factor)
                        else:
                            xmaximum 500 * persistent.scale_factor
                            xpadding 20 * persistent.scale_factor
                            ypadding 20 * persistent.scale_factor
                            yoffset -5 * persistent.scale_factor
                            background Frame("screen_text_message_you",10 * persistent.scale_factor,10 * persistent.scale_factor)

                        vbox:
                            if mphone_get_chat_str(text_message_screen_list[x][1]) != "":
                                if text_message_screen_list[x][2]:
                                    text "{color=2b2b2b}{b}%s{/b}\n%s{/color}" % (text_message_screen_list[x][0],mphone_get_chat_str(text_message_screen_list[x][1])) style "text_message_screen_style" text_align 0.0
                                else:
                                    text "{b}%s{/b}\n%s" % (text_message_screen_list[x][0],mphone_get_chat_str(text_message_screen_list[x][1])) style "text_message_screen_style" text_align 0.0
                            else:
                                if text_message_screen_list[x][2]:
                                    text "{color=2b2b2b}{b}%s{/b}{/color}" % text_message_screen_list[x][0] style "text_message_screen_style" text_align 0.0
                                else:
                                    text "{b}%s{/b}" % text_message_screen_list[x][0] style "text_message_screen_style" text_align 0.0
                            hbox:
                                for i in mphones_emotes:
                                    if i[1]:
                                        imagebutton:
                                            idle i[0]
                                            hover i[0]
                                            yminimum 24 * persistent.scale_factor
                                            ymaximum 24 * persistent.scale_factor
                                            action NullAction()

style text_message_screen_style:
    font "fonts/Roboto-Regular.ttf"
    size 24 * persistent.scale_factor
    color "#ffffff"

transform text_message_pop_up_transform:
    alpha 0.0 yoffset 800 * persistent.scale_factor
    ease 0.8 yoffset 0 alpha 1.0

transform text_message_pop_up_random_transform:
    alpha 0.0 yoffset 800 * persistent.scale_factor
    ease 0.8 yoffset 0 alpha 1.0
transform text_message_pop_up_random_transform2:
    alpha 0.0 yoffset 800 * persistent.scale_factor xoffset 1250 * persistent.scale_factor
    ease 0.8 yoffset 0 alpha 1.0 xoffset 1250 * persistent.scale_factor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

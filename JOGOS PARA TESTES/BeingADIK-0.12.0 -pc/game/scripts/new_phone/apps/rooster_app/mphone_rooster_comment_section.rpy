screen rooster_comment_section_screen:
    tag rooster_comment_section_screen
    modal True
    add "mphone_rooster_bg"
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    key "mouseup_2" action Hide("rooster_comment_section_screen")

    vpgrid:
        yfill True
        xminimum 468 * persistent.scale_factor
        xmaximum 468 * persistent.scale_factor
        yminimum 834 * persistent.scale_factor
        ymaximum 834 * persistent.scale_factor
        ypos 149 * persistent.scale_factor
        cols 1
        draggable False
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.502
        xoffset -2 * persistent.scale_factor

        vbox xalign 0.5 yalign 0:
            xminimum 468 * persistent.scale_factor
            xmaximum 468 * persistent.scale_factor
            spacing 5 * persistent.scale_factor
            yoffset 5 * persistent.scale_factor
            yminimum 680 * persistent.scale_factor
            ymaximum 680 * persistent.scale_factor
            hbox xalign 0.05 yalign 0:
                xoffset 30 * persistent.scale_factor
                spacing 5 * persistent.scale_factor
                imagebutton:
                    if "rooster_mini_mc" in mroosterAvatarArray[roosterCurrentIdx]:
                        idle Transform(mc_avatar)
                        hover Transform(mc_avatar)
                    else:
                        idle Transform(mroosterAvatarArray[roosterCurrentIdx])
                        hover Transform(mroosterAvatarArray[roosterCurrentIdx])
                    action NullAction()
                text mroosterNickArray[roosterCurrentIdx] style "rooster_avatar_style":
                    yalign 0.5
            hbox xalign 0.05 yalign 0:
                xoffset 30 * persistent.scale_factor
                xmaximum 380 * persistent.scale_factor
                xminimum 380 * persistent.scale_factor
                text mroosterTextArray[roosterCurrentIdx] style "rooster_text_style":
                    yalign 0.5
            hbox xalign 0.05 yalign 0:
                xoffset 30 * persistent.scale_factor
                imagebutton:
                    idle Transform(mroosterPhotoArray[roosterCurrentIdx]+"_idle")
                    hover Transform(mroosterPhotoArray[roosterCurrentIdx]+"_hover")
                    action Show(mroosterPhotoArray[roosterCurrentIdx])
            hbox xalign 0.45 yalign 0:
                spacing 50 * persistent.scale_factor
                xminimum 210 * persistent.scale_factor
                hbox xalign 0.5 yalign 0:
                    xminimum 70 * persistent.scale_factor
                    spacing 5 * persistent.scale_factor
                    imagebutton:
                        idle Transform("rooster_cluck_icon_idle")
                        hover Transform("rooster_cluck_icon_idle")
                        action NullAction()
                    text "%s" % mroosterPostsArray[roosterCurrentIdx] style "rooster_text_style":
                        yalign 0.5
                hbox xalign 0.5 yalign 0:
                    xminimum 70 * persistent.scale_factor
                    spacing 5 * persistent.scale_factor
                    if not mroosterLikedArray[roosterCurrentIdx]:
                        imagebutton:
                            idle Transform("rooster_like_icon_idle")
                            hover Transform("rooster_like_icon_hover")
                            action (SetDict(mroosterLikedArray, roosterCurrentIdx, True), SetDict(mroosterLikesArray,roosterCurrentIdx, mroosterLikesArray[roosterCurrentIdx] + 1))
                    else:
                        imagebutton:
                            idle Transform("rooster_like_icon_active")
                            hover Transform("rooster_like_icon_hover")
                            action (SetDict(mroosterLikedArray, roosterCurrentIdx, False), SetDict(mroosterLikesArray,roosterCurrentIdx, mroosterLikesArray[roosterCurrentIdx] - 1))
                    text "%s" % mroosterLikesArray[roosterCurrentIdx] style "rooster_text_style":
                        yalign 0.5
                hbox xalign 0.5 yalign 0:
                    xminimum 70 * persistent.scale_factor
                    imagebutton:
                        idle Transform("rooster_share_icon")
                        hover Transform("rooster_share_icon")
                        action NullAction()
            hbox xalign 0.0 yalign 0.5:
                imagebutton:
                    idle Transform("mphone_rooster_divider")
                    hover Transform("mphone_rooster_divider")
                    action NullAction()


            $ count = 0
            for x in mroosterHistory_text[roosterCurrentIdx]:
                vbox xalign 0.0 yalign 0.5:
                    xoffset 30 * persistent.scale_factor
                    spacing 5 * persistent.scale_factor
                    hbox xalign 0.0 yalign 0.5:
                        spacing 8 * persistent.scale_factor
                        imagebutton:
                            if "rooster_mini_mc" in mroosterHistory_avatars[roosterCurrentIdx][count]:
                                idle mc_avatar
                                hover mc_avatar
                            else:
                                idle mroosterHistory_avatars[roosterCurrentIdx][count]
                                hover mroosterHistory_avatars[roosterCurrentIdx][count]
                            action NullAction()
                            yoffset 10 * persistent.scale_factor
                        vbox xalign 0.0 yalign 0.5:
                            xmaximum 320 * persistent.scale_factor
                            xminimum 320 * persistent.scale_factor
                            text mroosterHistory_nicknames[roosterCurrentIdx][count] style "rooster_avatar2_style"
                            if "Download here" in x:
                                textbutton "%s" % x text_style "rooster_comment_style" action (SetVariable("ep11_virus",True))
                            elif "people in Uganda have access" in x:
                                textbutton "%s" % x text_style "rooster_comment_style" action (Function(ft_play_click),Function(mgallery_add_photo,"ep12_bikini_minny"))
                            elif "Sure can do! One bikini image is coming right up." in x:
                                textbutton "%s" % x text_style "rooster_comment_style" action (Function(ft_play_click),Function(mgallery_add_photo,"ep12_bikini_dawe"))
                            else:
                                text "%s" % x style "rooster_comment_style"
                    hbox xalign 0.45 yalign 0.5:
                        spacing 50 * persistent.scale_factor
                        hbox xalign 0.5 yalign 0:
                            spacing 5 * persistent.scale_factor
                            imagebutton:
                                idle "rooster_cluck_icon_mini_idle"
                                hover "rooster_cluck_icon_mini_idle"
                                action NullAction()
                        hbox xalign 0.5 yalign 0:
                            spacing 5 * persistent.scale_factor
                            if not mroosterHistory_liked[roosterCurrentIdx][count]:
                                imagebutton:
                                    idle Transform("rooster_like_icon_mini_idle")
                                    hover Transform("rooster_like_icon_mini_hover")
                                    action (SetDict(mroosterHistory_liked[roosterCurrentIdx], count, True), SetDict(mroosterHistory_likes[roosterCurrentIdx],count, mroosterHistory_likes[roosterCurrentIdx][count] + 1))
                            else:
                                imagebutton:
                                    idle Transform("rooster_like_icon_mini_active")
                                    hover Transform("rooster_like_icon_mini_hover")
                                    action (SetDict(mroosterHistory_liked[roosterCurrentIdx], count, False), SetDict(mroosterHistory_likes[roosterCurrentIdx],count, mroosterHistory_likes[roosterCurrentIdx][count] - 1))
                            if mroosterHistory_likes[roosterCurrentIdx][count] != 0:
                                text "%s" % mroosterHistory_likes[roosterCurrentIdx][count] style "rooster_comment_style":
                                    yalign 0.5
                        hbox xalign 0.5 yalign 0:
                            spacing 5 * persistent.scale_factor
                            imagebutton:
                                idle "rooster_share_mini_icon"
                                hover "rooster_share_mini_icon"
                                action NullAction()
                hbox xalign 0.0 yalign 0.5:
                    imagebutton:
                        idle Transform("mphone_rooster_divider")
                        hover Transform("mphone_rooster_divider")
                        action NullAction()
                $ count += 1

    if mroosterChoices[roosterCurrentIdx][0] == 0 and len(mroosterChoices[roosterCurrentIdx])>1:
        vbox xalign 0.79 yalign 0.75:
            spacing 5 * persistent.scale_factor
            xoffset 5 * persistent.scale_factor
            yoffset 5 * persistent.scale_factor
            for x in range(1,len(mroosterChoices[roosterCurrentIdx])):
                hbox:
                    imagebutton:
                        idle mc_avatar
                        hover mc_avatar
                        action NullAction()
                        yalign 0.5
                    textbutton "%s" % mroosterChoices[roosterCurrentIdx][x]:
                        action (SetDict(mphone_text_frame,x-1,"chat_mc_box"),SetDict(mroosterPostsArray,roosterCurrentIdx,mroosterPostsArray[roosterCurrentIdx]+1),SetDict(mroosterChoices[roosterCurrentIdx],0,x), Function(rooster_reply_func,roosterCurrentIdx))
                        text_style "mphone_chat_text_style"
                        yalign 0.5
                        background Frame(mphone_text_frame[x-1],10 * persistent.scale_factor,10 * persistent.scale_factor)
                        hovered SetDict(mphone_text_frame,x-1,"mphone_chat_selection_box")
                        unhovered SetDict(mphone_text_frame,x-1,"chat_mc_box")
                        xmaximum 320 * persistent.scale_factor
                        xminimum 320 * persistent.scale_factor


    add "mphone_rooster_fg"
    imagebutton at mphone_off_transform:
        idle "mphone_off_circle_idle"
        hover "mphone_off_circle_hover"
        action (SetVariable("mphone_text_frame",["chat_mc_box","chat_mc_box","chat_mc_box","chat_mc_box"]),Hide("rooster_comment_section_screen"))
        xalign 0.5
        yalign mphone_off_yalign
    hbox:
        xalign 0.5
        yalign 0.06
        spacing 300 * persistent.scale_factor
        add "mphone_top_cakenet"
        add "mphone_top_icons"
    add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

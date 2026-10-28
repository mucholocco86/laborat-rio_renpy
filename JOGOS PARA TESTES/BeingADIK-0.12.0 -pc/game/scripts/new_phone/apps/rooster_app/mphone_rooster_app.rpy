screen mphone_rooster_app_screen:
    tag mphone_rooster_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add "mphone_rooster_bg"
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_2" action Hide("mphone_rooster_app_screen")
    fixed:
        at mphone_app_transform

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
            $ count = 0
            for x in mroosterAvatarArray:
                vbox xalign 0.5 yalign 0:
                    xminimum 468 * persistent.scale_factor
                    xmaximum 468 * persistent.scale_factor
                    spacing 5 * persistent.scale_factor
                    yoffset 5 * persistent.scale_factor
                    yminimum 680 * persistent.scale_factor
                    ymaximum 680 * persistent.scale_factor
                    if count < new_rooster_int:
                        hbox xalign 0.05 yalign 0:
                            xoffset 30 * persistent.scale_factor
                            spacing 5 * persistent.scale_factor
                            imagebutton:
                                if "rooster_mini_mc" in mroosterAvatarArray[count]:
                                    idle Transform(mc_avatar)
                                    hover Transform(mc_avatar)
                                else:
                                    idle Transform(mroosterAvatarArray[count])
                                    hover Transform(mroosterAvatarArray[count])
                                action NullAction()
                            text mroosterNickArray[count] style "rooster_avatar_style":
                                yalign 0.5
                            imagebutton:
                                yalign 0.25
                                idle Transform("rooster_new_icon0")
                                action NullAction()
                    else:
                        hbox xalign 0.05 yalign 0:
                            xoffset 30 * persistent.scale_factor
                            spacing 5 * persistent.scale_factor
                            imagebutton:
                                if "rooster_mini_mc" in mroosterAvatarArray[count]:
                                    idle Transform(mc_avatar)
                                    hover Transform(mc_avatar)
                                else:
                                    idle Transform(mroosterAvatarArray[count])
                                    hover Transform(mroosterAvatarArray[count])
                                action NullAction()
                            text mroosterNickArray[count] style "rooster_avatar_style":
                                yalign 0.5
                    hbox xalign 0.05 yalign 0:
                        xoffset 30 * persistent.scale_factor
                        xmaximum 380 * persistent.scale_factor
                        xminimum 380 * persistent.scale_factor
                        text mroosterTextArray[count] style "rooster_text_style":
                            yalign 0.5
                    hbox xalign 0.05 yalign 0:
                        xoffset 30 * persistent.scale_factor
                        imagebutton:
                            idle Transform(mroosterPhotoArray[count]+"_idle")
                            hover Transform(mroosterPhotoArray[count]+"_hover")
                            action Show(mroosterPhotoArray[count])
                    hbox xalign 0.45 yalign 0:
                        spacing 50 * persistent.scale_factor
                        xminimum 210 * persistent.scale_factor
                        hbox xalign 0.5 yalign 0:
                            xminimum 70 * persistent.scale_factor
                            spacing 5 * persistent.scale_factor
                            imagebutton:
                                idle Transform("rooster_cluck_icon_idle_pulse")
                                hover Transform("rooster_cluck_icon_hover")
                                action (SetVariable("roosterCurrentIdx", count), Function(checkedCluck), Show("rooster_comment_section_screen"))
                            text "%s" % mroosterPostsArray[count] style "rooster_text_style":
                                yalign 0.5
                        hbox xalign 0.5 yalign 0:
                            xminimum 70 * persistent.scale_factor
                            spacing 5 * persistent.scale_factor
                            if not mroosterLikedArray[count]:
                                imagebutton:
                                    idle Transform("rooster_like_icon_idle")
                                    hover Transform("rooster_like_icon_hover")
                                    action (SetDict(mroosterLikedArray, count, True), SetDict(mroosterLikesArray,count, mroosterLikesArray[count] + 1))
                            else:
                                imagebutton:
                                    idle Transform("rooster_like_icon_active")
                                    hover Transform("rooster_like_icon_hover")
                                    action (SetDict(mroosterLikedArray, count, False), SetDict(mroosterLikesArray,count, mroosterLikesArray[count] - 1))
                            text "%s" % mroosterLikesArray[count] style "rooster_text_style":
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
                $ count += 1

    fixed:
        at mphone_app_transform


        add "mphone_rooster_fg"
        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            action Hide("mphone_rooster_app_screen")
            xalign 0.5
            yalign mphone_off_yalign
        hbox:
            xalign 0.5
            yalign 0.06
            spacing 300 * persistent.scale_factor
            add "mphone_top_cakenet"
            add "mphone_top_icons"
        add "mphone_fg"

image rooster_cluck_icon_idle_pulse:
    "rooster_cluck_icon_idle" with Dissolve(0.8, alpha=True)
    pause 1.5
    "rooster_cluck_icon_idle2" with Dissolve(0.8, alpha=True)
    pause 1.5
    repeat

style rooster_avatar_style:
    font "fonts/candara.ttf"
    size 20 * persistent.scale_factor
    color "#fe9416"
    xmaximum 320 * persistent.scale_factor

style rooster_avatar2_style:
    font "fonts/candara.ttf"
    size 18 * persistent.scale_factor
    color "#fe9416"
    xmaximum 320 * persistent.scale_factor

style rooster_text_style:
    font "fonts/candara.ttf"
    size 20 * persistent.scale_factor
    color "#000000"
    xmaximum 432 * persistent.scale_factor

style rooster_text_style2:
    font "fonts/candara.ttf"
    size 5 * persistent.scale_factor
    color "#000000"
    xmaximum 432 * persistent.scale_factor

style rooster_comment_style:
    font "fonts/candara.ttf"
    size 18 * persistent.scale_factor
    color "#000000"
    xmaximum 432 * persistent.scale_factor

style rooster_choice_text:
    font "fonts/candara.ttf"
    size 20 * persistent.scale_factor
    color "#2b2b2b"
    hover_color "#fe9416"
    xmaximum 320 * persistent.scale_factor

image rooster_new_icon0:
    "rooster_new_icon" with Dissolve(0.2, alpha=True)
    pause 0.2
    "rooster_new_icon2" with Dissolve(0.2, alpha=True)
    pause 0.2
    "rooster_new_icon" with Dissolve(0.2, alpha=True)
    pause 0.2
    "rooster_new_icon3" with Dissolve(0.2, alpha=True)
    pause 0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen mphone_pack_quest_app_screen:
    tag mphone_pack_quest_app_screen
    modal True
    fixed:
        at mphone_app_transform
        add AlphaBlend("mphone_screen_alpha2", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "mphone_pack_quest_app_moving_scroll", alpha=True)
        add "mphone_pack_quest_app_bg"

    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    if not pq_open_animation:
        key "mouseup_2" action Hide("mphone_pack_quest_app_screen")
    else:
        key "mouseup_2" action (Function(unlock_pq_renders), Function(pq_ach_func),Hide("mphone_pack_quest_app_screen"))
    fixed:
        at mphone_app_transform

        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            if not pq_open_animation:
                action Hide("mphone_pack_quest_app_screen")
            else:
                action (Function(unlock_pq_renders), Function(pq_ach_func),Hide("mphone_pack_quest_app_screen"))

            xalign 0.5
            yalign mphone_off_yalign

        if pq_open_animation:
            text "Opening Custom Render Pack..." at app_pack_quest_opening_text_anim style "app_pack_quest_opening_text_style":
                xalign 0.5
                yalign 0.2

            text "Custom renders unlocked!" at app_pack_quest_opening_text_anim2 style "app_pack_quest_opening_text_style":
                xalign 0.5
                yalign 0.2

            imagebutton at app_pack_quest_open_anim:
                xpos 960 * persistent.scale_factor
                yalign 0.50
                xoffset -180 * persistent.scale_factor
                idle mphone_pq_img
                action NullAction()


            add AlphaBlend("mphone_screen_alpha2", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "pq_smoke_stack1", alpha=True)
            add AlphaBlend("mphone_screen_alpha2", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "pq_smoke_stack2", alpha=True)

            imagebutton at app_pack_quest_open_img1_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr1.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr1_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_1" % currentEpisode)
            imagebutton at app_pack_quest_open_img2_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr2.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr2_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_2" % currentEpisode)
            imagebutton at app_pack_quest_open_img3_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr3.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr3_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_3" % currentEpisode)
            imagebutton at app_pack_quest_open_img4_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr4.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr4_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_4" % currentEpisode)
            imagebutton at app_pack_quest_open_img5_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr5.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr5_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_5" % currentEpisode)
            imagebutton at app_pack_quest_open_img6_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr6.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr6_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_6" % currentEpisode)
            imagebutton at app_pack_quest_open_img7_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr7.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr7_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_7" % currentEpisode)
            imagebutton at app_pack_quest_open_img8_anim:
                xpos 850 * persistent.scale_factor
                ypos 540 * persistent.scale_factor
                focus_mask True
                idle Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr8.png" % (currentEpisode,currentEpisode))
                hover Transform ("[persistent.img_dir]/rewards/ep%d/rew_ep%d_cr8_hover.png" % (currentEpisode,currentEpisode))
                action Show("packquest_image_preview",None,"ep%d_reward_cr_8" % currentEpisode)

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 725 * persistent.scale_factor
                ypos 251 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 950 * persistent.scale_factor
                ypos 251 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 725 * persistent.scale_factor
                ypos 380 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 950 * persistent.scale_factor
                ypos 380 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 725 * persistent.scale_factor
                ypos 509 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 950 * persistent.scale_factor
                ypos 509 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 725 * persistent.scale_factor
                ypos 638 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

            imagebutton at pack_quest_open_img_twinkle_anim:
                xpos 950 * persistent.scale_factor
                ypos 638 * persistent.scale_factor
                focus_mask True
                idle Transform ("twinkle_medium")
                hover Transform ("twinkle_medium")
                action NullAction()

        elif not pack_quest_active:
            if pack_quest_available:
                text "{color=fe9416}New Quest Available!{/color}" style "app_pack_quest_task_text_style2" at pack_quest_text_fade_anim:
                    xalign 0.50
                    yalign 0.18
                    text_align 0.5
                imagebutton at app_pack_quest_resize:
                    xalign 0.50
                    yalign 0.4
                    idle mphone_pq_img
                    action NullAction()
                imagebutton at app_pack_quest_text_fade_anim:
                    idle "pack_quest_start_quest_idle"
                    hover "pack_quest_start_quest_hover"
                    xalign 0.50
                    yalign 0.755
                    action (SetVariable("pack_quest_active", True), SetVariable("pack_quest_available", False))
            else:
                text "{color=c9c9c9}No Quest Available{/color}" style "app_pack_quest_task_text_style2" at pack_quest_text_fade_anim:
                    xalign 0.50
                    yalign 0.18
                    text_align 0.5
                imagebutton at app_pack_quest_resize:
                    xalign 0.50
                    yalign 0.4
                    idle "pack_quest_pack_no_crp_idle"
                    action NullAction()

            vbox:
                xalign 0.5
                if pack_quest_available:
                    yalign 0.87
                else:
                    yalign 0.8
                text "{color=#00a0e6}Find hidden buttons - Unlock Custom Renders{/color}" style "app_pack_quest_task_text_style3"
                text "Hidden buttons are scattered in the current free roam event." style "app_pack_quest_task_text_style3"
                text "Find all the buttons to unlock a set of custom renders." style "app_pack_quest_task_text_style3"
                text "The names of each button are hints to their location." style "app_pack_quest_task_text_style3"
                text "The unlocked renders are added to your Rewards app." style "app_pack_quest_task_text_style3"
        else:
            vbox:
                add AlphaBlend("mphone_screen_alpha2", Frame(Null(), 10 * persistent.scale_factor, 10 * persistent.scale_factor), "app_pq_img", alpha=True)
            if pq_found_buttons == 10:
                imagebutton at app_pack_quest_resize:
                    xalign 0.5
                    yalign 0.78
                    yoffset 20 * persistent.scale_factor
                    idle "pack_quest_turn_in_button_idle"
                    hover "pack_quest_turn_in_button_hover"
                    action (SetVariable("pack_quest_active", False), SetVariable("pq_open_animation", True), Show("app_packquest_glass_screen"), Function(pq_ach_func))
            text "{size=%d}{color=ffffff}{font=fonts/candara.ttf}Found {color=#00ff00}%d out of %d{/color} secret buttons{/font}{/color}{/size}" % ((25 * persistent.scale_factor),pq_found_buttons,len(pack_quest_list)) xalign 0.5 yalign 0.88

    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"
    fixed:
        at mphone_app_transform
        add "mphone_fg"

screen packquest_image_preview(arg1):
    tag packquest_image_preview
    modal True
    imagebutton:
        idle "%s" % arg1
        hover "%s" % arg1
        action Hide("packquest_image_preview")

screen packquest_button_found:
    tag packquest_button_found
    modal True
    timer 3 action Hide('packquest_button_found')
    imagebutton at pack_quest_line_anim_found_button2:
        xoffset -4200 * persistent.scale_factor
        idle "packquest_line"
        hover "packquest_line"
        yalign 0.40
    imagebutton at pack_quest_line_anim_found_button:
        xoffset 1920 * persistent.scale_factor
        idle "packquest_line"
        hover "packquest_line"
        yalign 0.44
    text "Hidden button found!" style "pack_quest_found_button_style" at pack_quest_text_anim_found_button:
        xoffset 2000 * persistent.scale_factor
        yalign 0.5
    imagebutton at pack_quest_line_anim_found_button2:
        xoffset -4000 * persistent.scale_factor
        idle "packquest_line"
        hover "packquest_line"
        yalign 0.56
    imagebutton at pack_quest_line_anim_found_button:
        xoffset 1700 * persistent.scale_factor
        idle "packquest_line"
        hover "packquest_line"
        yalign 0.60
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

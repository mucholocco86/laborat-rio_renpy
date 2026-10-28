screen rewards_camila:
    tag menu
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rew_camila2" xalign 0.0 yalign 0.9
    add "rewards_new_fg2"

    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Rewards - {color=#fe9416}Camila{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

    vpgrid:
        xalign 0.85
        ypos 0.14
        ysize 0.8
        cols 4
        spacing 10 * persistent.scale_factor
        draggable True
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.5

        if persistent.ep12_cardcam1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila1")
                    hover Transform ("rew_ep12_camila1_hover")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila2")
                    hover Transform ("rew_ep12_camila2_hover")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila3")
                    hover Transform ("rew_ep12_camila3_hover")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila4")
                    hover Transform ("rew_ep12_camila4_hover")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila5")
                    hover Transform ("rew_ep12_camila5_hover")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila6")
                    hover Transform ("rew_ep12_camila6_hover")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila7")
                    hover Transform ("rew_ep12_camila7_hover")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila8")
                    hover Transform ("rew_ep12_camila8_hover")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila9")
                    hover Transform ("rew_ep12_camila9_hover")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila10")
                    hover Transform ("rew_ep12_camila10_hover")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila11")
                    hover Transform ("rew_ep12_camila11_hover")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila12")
                    hover Transform ("rew_ep12_camila12_hover")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila13")
                    hover Transform ("rew_ep12_camila13_hover")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila14")
                    hover Transform ("rew_ep12_camila14_hover")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila15")
                    hover Transform ("rew_ep12_camila15_hover")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila16")
                    hover Transform ("rew_ep12_camila16_hover")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila17")
                    hover Transform ("rew_ep12_camila17_hover")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila18")
                    hover Transform ("rew_ep12_camila18_hover")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila19")
                    hover Transform ("rew_ep12_camila19_hover")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Story" style "reward_locked_style"
        if persistent.ep12_cardcam20:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_camila20")
                    hover Transform ("rew_ep12_camila20_hover")
                    action (SetVariable("tmpInt2",19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][19]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

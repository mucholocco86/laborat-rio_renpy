screen rewards_jill:
    tag menu
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rew_jill2" xalign 0.0 yalign 0.9
    add "rewards_new_fg2"

    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Rewards - {color=#fe9416}Jill{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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





        if persistent.ep9_cardji1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill1")
                    hover Transform ("rew_ep9_jill1_hover")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill2")
                    hover Transform ("rew_ep9_jill2_hover")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill3")
                    hover Transform ("rew_ep9_jill3_hover")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill4")
                    hover Transform ("rew_ep9_jill4_hover")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill5")
                    hover Transform ("rew_ep9_jill5_hover")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill6")
                    hover Transform ("rew_ep9_jill6_hover")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill7")
                    hover Transform ("rew_ep9_jill7_hover")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill8")
                    hover Transform ("rew_ep9_jill8_hover")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill9")
                    hover Transform ("rew_ep9_jill9_hover")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill10")
                    hover Transform ("rew_ep9_jill10_hover")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill11")
                    hover Transform ("rew_ep9_jill11_hover")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill12")
                    hover Transform ("rew_ep9_jill12_hover")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill13")
                    hover Transform ("rew_ep9_jill13_hover")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill14")
                    hover Transform ("rew_ep9_jill14_hover")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill15")
                    hover Transform ("rew_ep9_jill15_hover")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Free roam" style "reward_locked_style"
        if persistent.ep9_cardji16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill16")
                    hover Transform ("rew_ep9_jill16_hover")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill17")
                    hover Transform ("rew_ep9_jill17_hover")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Story" style "reward_locked_style"
        if persistent.ep9_cardji18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill18")
                    hover Transform ("rew_ep9_jill18_hover")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Vault" style "reward_locked_style"
        if persistent.ep9_cardji19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill19")
                    hover Transform ("rew_ep9_jill19_hover")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Vault" style "reward_locked_style"
        if persistent.ep9_cardji20:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_jill20")
                    hover Transform ("rew_ep9_jill20_hover")
                    action (SetVariable("tmpInt2",19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][19]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Vault" style "reward_locked_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

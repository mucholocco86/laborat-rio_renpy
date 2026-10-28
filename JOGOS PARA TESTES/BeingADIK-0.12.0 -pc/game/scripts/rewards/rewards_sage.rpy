screen rewards_sage:
    tag menu
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rew_sage2" xalign 0.0 yalign 0.9
    add "rewards_new_fg2"

    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Rewards - {color=#fe9416}Sage{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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

        if persistent.ep10_cardsa1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage1")
                    hover Transform ("rew_ep10_sage1_hover")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage2")
                    hover Transform ("rew_ep10_sage2_hover")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage3")
                    hover Transform ("rew_ep10_sage3_hover")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage4")
                    hover Transform ("rew_ep10_sage4_hover")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage5")
                    hover Transform ("rew_ep10_sage5_hover")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage6")
                    hover Transform ("rew_ep10_sage6_hover")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage7")
                    hover Transform ("rew_ep10_sage7_hover")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage8")
                    hover Transform ("rew_ep10_sage8_hover")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage9")
                    hover Transform ("rew_ep10_sage9_hover")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage10")
                    hover Transform ("rew_ep10_sage10_hover")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage11")
                    hover Transform ("rew_ep10_sage11_hover")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage12")
                    hover Transform ("rew_ep10_sage12_hover")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Free roam" style "reward_locked_style"
        if persistent.ep10_cardsa13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage13")
                    hover Transform ("rew_ep10_sage13_hover")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage14")
                    hover Transform ("rew_ep10_sage14_hover")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage15")
                    hover Transform ("rew_ep10_sage15_hover")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage16")
                    hover Transform ("rew_ep10_sage16_hover")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage17")
                    hover Transform ("rew_ep10_sage17_hover")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "English Class" style "reward_locked_style"
                else:
                    text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage18")
                    hover Transform ("rew_ep10_sage18_hover")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "Math Class" style "reward_locked_style"
                else:
                    text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage19")
                    hover Transform ("rew_ep10_sage19_hover")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "Ep 10 - Brawler" style "reward_locked_style"
                else:
                    text "Ep 10 - Vault" style "reward_locked_style"
        if persistent.ep10_cardsa20:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_sage20")
                    hover Transform ("rew_ep10_sage20_hover")
                    action (SetVariable("tmpInt2",19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][19]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "Science Class" style "reward_locked_style"
                else:
                    text "Ep 10 - Vault" style "reward_locked_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

screen rewards_isa:
    tag menu
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rew_isa2" xalign 0.0 yalign 0.9
    add "rewards_new_fg2"

    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Rewards - {color=#fe9416}Isabella{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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

        if persistent.ep12_cardisa1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella1")
                    hover Transform ("rew_ep12_isabella1_hover")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella2")
                    hover Transform ("rew_ep12_isabella2_hover")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella3")
                    hover Transform ("rew_ep12_isabella3_hover")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella4")
                    hover Transform ("rew_ep12_isabella4_hover")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella5")
                    hover Transform ("rew_ep12_isabella5_hover")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella6")
                    hover Transform ("rew_ep12_isabella6_hover")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella7")
                    hover Transform ("rew_ep12_isabella7_hover")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella8")
                    hover Transform ("rew_ep12_isabella8_hover")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella9")
                    hover Transform ("rew_ep12_isabella9_hover")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "Science Class" style "reward_locked_style"
                else:
                    text "Ep 12 - Vault" style "reward_locked_style"
        if persistent.ep12_cardisa10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella10")
                    hover Transform ("rew_ep12_isabella10_hover")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "Math Finals" style "reward_locked_style"
                else:
                    text "Ep 12 - Vault" style "reward_locked_style"
        if persistent.ep12_cardisa11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella11")
                    hover Transform ("rew_ep12_isabella11_hover")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "English Finals" style "reward_locked_style"
                else:
                    text "Ep 12 - Vault" style "reward_locked_style"
        if persistent.ep12_cardisa12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella12")
                    hover Transform ("rew_ep12_isabella12_hover")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella13")
                    hover Transform ("rew_ep12_isabella13_hover")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Card game" style "reward_locked_style"
        if persistent.ep12_cardisa14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella14")
                    hover Transform ("rew_ep12_isabella14_hover")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if minigames:
                    text "Brawler" style "reward_locked_style"
                else:
                    text "Ep 12 - Vault" style "reward_locked_style"
        if persistent.ep12_cardisa15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella15")
                    hover Transform ("rew_ep12_isabella15_hover")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "{size=-5}Fighting competition{/size}" style "reward_locked_style"
        if persistent.ep12_cardisa16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella16")
                    hover Transform ("rew_ep12_isabella16_hover")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Faculty party" style "reward_locked_style"
        if persistent.ep12_cardisa17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella17")
                    hover Transform ("rew_ep12_isabella17_hover")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella18")
                    hover Transform ("rew_ep12_isabella18_hover")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella19")
                    hover Transform ("rew_ep12_isabella19_hover")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
        if persistent.ep12_cardisa20:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_isabella20")
                    hover Transform ("rew_ep12_isabella20_hover")
                    action (SetVariable("tmpInt2",19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][19]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Free roam" style "reward_locked_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

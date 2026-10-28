screen rewards_mixed:
    tag menu
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rew_mixed2" xalign 0.0 yalign 0.9
    add "rewards_new_fg2"

    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")
    text "Rewards - {color=#fe9416}Mixed{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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

        if persistent.epi_card5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr1")
                    hover Transform ("rew_epi_cr1_hover")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if not minigames:
                    text "Interlude - Vault" style "reward_locked_style"
                else:
                    text "Drawing" style "reward_locked_style"
        if persistent.epi_card6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr2")
                    hover Transform ("rew_epi_cr2_hover")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if not minigames:
                    text "Interlude - Vault" style "reward_locked_style"
                else:
                    text "Drawing" style "reward_locked_style"
        if persistent.epi_card7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr3")
                    hover Transform ("rew_epi_cr3_hover")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                if not minigames:
                    text "Interlude - Vault" style "reward_locked_style"
                else:
                    text "Drawing" style "reward_locked_style"
        if persistent.epi_card8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr4")
                    hover Transform ("rew_epi_cr4_hover")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"
        if persistent.epi_card9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr5")
                    hover Transform ("rew_epi_cr5_hover")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"
        if persistent.epi_card10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr6")
                    hover Transform ("rew_epi_cr6_hover")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"
        if persistent.epi_card11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr7")
                    hover Transform ("rew_epi_cr7_hover")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"
        if persistent.epi_card12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_epi_cr8")
                    hover Transform ("rew_epi_cr8_hover")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep9_card9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr1")
                    hover Transform ("rew_ep9_cr1_hover")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr2")
                    hover Transform ("rew_ep9_cr2_hover")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr3")
                    hover Transform ("rew_ep9_cr3_hover")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr4")
                    hover Transform ("rew_ep9_cr4_hover")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr5")
                    hover Transform ("rew_ep9_cr5_hover")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr6")
                    hover Transform ("rew_ep9_cr6_hover")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr7")
                    hover Transform ("rew_ep9_cr7_hover")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep9_card16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_cr8")
                    hover Transform ("rew_ep9_cr8_hover")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr1")
                    hover Transform ("rew_ep10_cr1_hover")
                    action (SetVariable("tmpInt2",16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][16]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr2")
                    hover Transform ("rew_ep10_cr2_hover")
                    action (SetVariable("tmpInt2",17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][17]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr3")
                    hover Transform ("rew_ep10_cr3_hover")
                    action (SetVariable("tmpInt2",18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][18]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr4")
                    hover Transform ("rew_ep10_cr4_hover")
                    action (SetVariable("tmpInt2",19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][19]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr5")
                    hover Transform ("rew_ep10_cr5_hover")
                    action (SetVariable("tmpInt2",20),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][20]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr6")
                    hover Transform ("rew_ep10_cr6_hover")
                    action (SetVariable("tmpInt2",21),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][21]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr7")
                    hover Transform ("rew_ep10_cr7_hover")
                    action (SetVariable("tmpInt2",22),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][22]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep10_card8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep10_cr8")
                    hover Transform ("rew_ep10_cr8_hover")
                    action (SetVariable("tmpInt2",23),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][23]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr1")
                    hover Transform ("rew_ep11_cr1_hover")
                    action (SetVariable("tmpInt2",24),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][24]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr2")
                    hover Transform ("rew_ep11_cr2_hover")
                    action (SetVariable("tmpInt2",25),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][25]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr3")
                    hover Transform ("rew_ep11_cr3_hover")
                    action (SetVariable("tmpInt2",26),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][26]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr4")
                    hover Transform ("rew_ep11_cr4_hover")
                    action (SetVariable("tmpInt2",27),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][27]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr5")
                    hover Transform ("rew_ep11_cr5_hover")
                    action (SetVariable("tmpInt2",28),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][28]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr6")
                    hover Transform ("rew_ep11_cr6_hover")
                    action (SetVariable("tmpInt2",29),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][29]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr7")
                    hover Transform ("rew_ep11_cr7_hover")
                    action (SetVariable("tmpInt2",30),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][30]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr8")
                    hover Transform ("rew_ep11_cr8_hover")
                    action (SetVariable("tmpInt2",31),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][31]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Pack Quest" style "reward_locked_style"

        if persistent.ep11_card9b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr9")
                    hover Transform ("rew_ep11_cr9_hover")
                    action (SetVariable("tmpInt2",32),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][32]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Vault" style "reward_locked_style"

        if persistent.ep11_card10b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr10")
                    hover Transform ("rew_ep11_cr10_hover")
                    action (SetVariable("tmpInt2",33),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][33]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Vault" style "reward_locked_style"

        if persistent.ep11_card11b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr11")
                    hover Transform ("rew_ep11_cr11_hover")
                    action (SetVariable("tmpInt2",34),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][34]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Vault" style "reward_locked_style"

        if persistent.ep11_card12b:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep11_cr12")
                    hover Transform ("rew_ep11_cr12_hover")
                    action (SetVariable("tmpInt2",35),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][35]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Vault" style "reward_locked_style"

        if persistent.ep12_card1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr1")
                    hover Transform ("rew_ep12_cr1_hover")
                    action (SetVariable("tmpInt2",36),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][36]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr2")
                    hover Transform ("rew_ep12_cr2_hover")
                    action (SetVariable("tmpInt2",37),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][37]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr3")
                    hover Transform ("rew_ep12_cr3_hover")
                    action (SetVariable("tmpInt2",38),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][38]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr4")
                    hover Transform ("rew_ep12_cr4_hover")
                    action (SetVariable("tmpInt2",39),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][39]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr5")
                    hover Transform ("rew_ep12_cr5_hover")
                    action (SetVariable("tmpInt2",40),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][40]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr6")
                    hover Transform ("rew_ep12_cr6_hover")
                    action (SetVariable("tmpInt2",41),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][41]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr7")
                    hover Transform ("rew_ep12_cr7_hover")
                    action (SetVariable("tmpInt2",42),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][42]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr8")
                    hover Transform ("rew_ep12_cr8_hover")
                    action (SetVariable("tmpInt2",43),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][43]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Pack Quest" style "reward_locked_style"

        if persistent.ep12_card9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr9")
                    hover Transform ("rew_ep12_cr9_hover")
                    action (SetVariable("tmpInt2",44),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][44]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"

        if persistent.ep12_card10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr10")
                    hover Transform ("rew_ep12_cr10_hover")
                    action (SetVariable("tmpInt2",45),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][45]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"

        if persistent.ep12_card11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr11")
                    hover Transform ("rew_ep12_cr11_hover")
                    action (SetVariable("tmpInt2",46),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][46]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"

        if persistent.ep12_card12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr12")
                    hover Transform ("rew_ep12_cr12_hover")
                    action (SetVariable("tmpInt2",47),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][47]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"

        if persistent.ep12_card13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr13")
                    hover Transform ("rew_ep12_cr13_hover")
                    action (SetVariable("tmpInt2",48),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][48]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"

        if persistent.ep12_card14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep12_cr14")
                    hover Transform ("rew_ep12_cr14_hover")
                    action (SetVariable("tmpInt2",49),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][49]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Vault" style "reward_locked_style"

        vbox xalign 0.5 yalign 0.5:
            add "disabled_btn"
            text "" style "reward_locked_style"
        vbox xalign 0.5 yalign 0.5:
            add "disabled_btn"
            text "" style "reward_locked_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

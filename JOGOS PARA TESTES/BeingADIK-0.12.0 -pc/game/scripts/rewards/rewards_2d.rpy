screen rewards_2d:
    tag menu
    add "rewards_new_bg"
    add "spr_crp1"
    add "spr_crp2"
    add "spr_crp3"
    add "spr_crp4"
    add "spr_crp5"
    add "spr_crp6"
    add "rew_2d_art2" xalign 0.0 yalign 0.9
    add "rewards_new_fg2"

    imagebutton:
        idle "rew_x_idle"
        hover "rew_x_hover"
        action ShowMenu("rewards")
        xalign 0.99
        yalign 0.00
    key "mouseup_2" action ShowMenu("rewards")

    text "Rewards - {color=#67ed55}2D Art{/color}" style "reward_header_style" xalign 0.02 yalign 0.004

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

        if persistent.art_unlocked_lvl1[0]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[0].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[0].lower()+"_hover")
                    action (SetVariable("tmpInt2",0),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][0][0] or (persistent.rewards_seen_list[tmpInt][0][1] and persistent.art_unlocked_lvl2[0]) or (persistent.rewards_seen_list[tmpInt][0][2] and persistent.art_unlocked_lvl3[0]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[1]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[1].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[1].lower()+"_hover")
                    action (SetVariable("tmpInt2",1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][1][0] or (persistent.rewards_seen_list[tmpInt][1][1] and persistent.art_unlocked_lvl2[1]) or (persistent.rewards_seen_list[tmpInt][1][2] and persistent.art_unlocked_lvl3[1]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[2]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[2].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[2].lower()+"_hover")
                    action (SetVariable("tmpInt2",2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][2][0] or (persistent.rewards_seen_list[tmpInt][2][1] and persistent.art_unlocked_lvl2[2]) or (persistent.rewards_seen_list[tmpInt][2][2] and persistent.art_unlocked_lvl3[2]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[3]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[3].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[3].lower()+"_hover")
                    action (SetVariable("tmpInt2",3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][3][0] or (persistent.rewards_seen_list[tmpInt][3][1] and persistent.art_unlocked_lvl2[3]) or (persistent.rewards_seen_list[tmpInt][3][2] and persistent.art_unlocked_lvl3[3]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[4]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[4].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[4].lower()+"_hover")
                    action (SetVariable("tmpInt2",4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][4][0] or (persistent.rewards_seen_list[tmpInt][4][1] and persistent.art_unlocked_lvl2[4]) or (persistent.rewards_seen_list[tmpInt][4][2] and persistent.art_unlocked_lvl3[4]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[5]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[5].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[5].lower()+"_hover")
                    action (SetVariable("tmpInt2",5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][5][0] or (persistent.rewards_seen_list[tmpInt][5][1] and persistent.art_unlocked_lvl2[5]) or (persistent.rewards_seen_list[tmpInt][5][2] and persistent.art_unlocked_lvl3[5]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"

        if persistent.art_unlocked_lvl1[6]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[6].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[6].lower()+"_hover")
                    action (SetVariable("tmpInt2",6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][6][0] or (persistent.rewards_seen_list[tmpInt][6][1] and persistent.art_unlocked_lvl2[6]) or (persistent.rewards_seen_list[tmpInt][6][2] and persistent.art_unlocked_lvl3[6]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[7]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[7].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[7].lower()+"_hover")
                    action (SetVariable("tmpInt2",7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][7][0] or (persistent.rewards_seen_list[tmpInt][7][1] and persistent.art_unlocked_lvl2[7]) or (persistent.rewards_seen_list[tmpInt][7][2] and persistent.art_unlocked_lvl3[7]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[8]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[8].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[8].lower()+"_hover")
                    action (SetVariable("tmpInt2",8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][8][0] or (persistent.rewards_seen_list[tmpInt][8][1] and persistent.art_unlocked_lvl2[8]) or (persistent.rewards_seen_list[tmpInt][8][2] and persistent.art_unlocked_lvl3[8]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[9]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[9].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[9].lower()+"_hover")
                    action (SetVariable("tmpInt2",9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][9][0] or (persistent.rewards_seen_list[tmpInt][9][1] and persistent.art_unlocked_lvl2[9]) or (persistent.rewards_seen_list[tmpInt][9][2] and persistent.art_unlocked_lvl3[9]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[10]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_2d_"+new_art_girl_name_list[10].lower())
                    hover Transform ("rew_ep9_2d_"+new_art_girl_name_list[10].lower()+"_hover")
                    action (SetVariable("tmpInt2",10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][10][0] or (persistent.rewards_seen_list[tmpInt][10][1] and persistent.art_unlocked_lvl2[10]) or (persistent.rewards_seen_list[tmpInt][10][2] and persistent.art_unlocked_lvl3[10]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[11]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[11].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[11].lower()+"_hover")
                    action (SetVariable("tmpInt2",11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][11][0] or (persistent.rewards_seen_list[tmpInt][11][1] and persistent.art_unlocked_lvl2[11]) or (persistent.rewards_seen_list[tmpInt][11][2] and persistent.art_unlocked_lvl3[11]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[12]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[12].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[12].lower()+"_hover")
                    action (SetVariable("tmpInt2",12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][12][0] or (persistent.rewards_seen_list[tmpInt][12][1] and persistent.art_unlocked_lvl2[12]) or (persistent.rewards_seen_list[tmpInt][12][2] and persistent.art_unlocked_lvl3[12]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[13]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[13].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[13].lower()+"_hover")
                    action (SetVariable("tmpInt2",13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][13][0] or (persistent.rewards_seen_list[tmpInt][13][1] and persistent.art_unlocked_lvl2[13]) or (persistent.rewards_seen_list[tmpInt][13][2] and persistent.art_unlocked_lvl3[13]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[14]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep7_2d_"+new_art_girl_name_list[14].lower())
                    hover Transform ("rew_ep7_2d_"+new_art_girl_name_list[14].lower()+"_hover")
                    action (SetVariable("tmpInt2",14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][14][0] or (persistent.rewards_seen_list[tmpInt][14][1] and persistent.art_unlocked_lvl2[14]) or (persistent.rewards_seen_list[tmpInt][14][2] and persistent.art_unlocked_lvl3[14]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"
        if persistent.art_unlocked_lvl1[15]:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("rew_ep9_2d_"+new_art_girl_name_list[15].lower())
                    hover Transform ("rew_ep9_2d_"+new_art_girl_name_list[15].lower()+"_hover")
                    action (SetVariable("tmpInt2",15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][15][0] or (persistent.rewards_seen_list[tmpInt][15][1] and persistent.art_unlocked_lvl2[15]) or (persistent.rewards_seen_list[tmpInt][15][2] and persistent.art_unlocked_lvl3[15]):
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "2D Art shop" style "reward_locked_style"


        if persistent.ep7_wpi1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_isabella_1a_idle")
                    hover Transform ("ep7_wallpaper_isabella_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpi2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_isabella_2a_idle")
                    hover Transform ("ep7_wallpaper_isabella_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+1),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+1]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpj1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_jill_1a_idle")
                    hover Transform ("ep7_wallpaper_jill_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+2),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+2]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpj2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_jill_2a_idle")
                    hover Transform ("ep7_wallpaper_jill_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+3),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+3]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpjo1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_josy_1a_idle")
                    hover Transform ("ep7_wallpaper_josy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+4),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+4]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpjo2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_josy_2a_idle")
                    hover Transform ("ep7_wallpaper_josy_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+5),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+5]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpm1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_maya_1a_idle")
                    hover Transform ("ep7_wallpaper_maya_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+6),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+6]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wpm2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_maya_2a_idle")
                    hover Transform ("ep7_wallpaper_maya_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+7),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+7]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wps1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_sage_1a_idle")
                    hover Transform ("ep7_wallpaper_sage_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+8),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+8]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep7_wps2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep7_wallpaper_sage_2a_idle")
                    hover Transform ("ep7_wallpaper_sage_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+9),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+9]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpi1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_isabella_1a_idle")
                    hover Transform ("ep8_wallpaper_isabella_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+10),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+10]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpj1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_jill_1a_idle")
                    hover Transform ("ep8_wallpaper_jill_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+11),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+11]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpjo1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_josy_1a_idle")
                    hover Transform ("ep8_wallpaper_josy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+12),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+12]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpm1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_maya_1a_idle")
                    hover Transform ("ep8_wallpaper_maya_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+13),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+13]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpq1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_quinn_1a_idle")
                    hover Transform ("ep8_wallpaper_quinn_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+14),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+14]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wps1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_sage_1a_idle")
                    hover Transform ("ep8_wallpaper_sage_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+15),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+15]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpe1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_envy_1a_idle")
                    hover Transform ("ep8_wallpaper_envy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+16),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+16]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpjade1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_jade_1a_idle")
                    hover Transform ("ep8_wallpaper_jade_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+17),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+17]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.ep8_wpmad1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep8_wallpaper_madame_1a_idle")
                    hover Transform ("ep8_wallpaper_madame_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+18),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+18]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude - Vault" style "reward_locked_style"

        if persistent.epi_card1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("epi_wallpaper_zoey_1a_idle")
                    hover Transform ("epi_wallpaper_zoey_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+19),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+19]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude" style "reward_locked_style"

        if persistent.epi_card2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("epi_wallpaper_zoey_2a_idle")
                    hover Transform ("epi_wallpaper_zoey_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+20),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+20]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude" style "reward_locked_style"

        if persistent.epi_card3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("epi_wallpaper_zoey_3a_idle")
                    hover Transform ("epi_wallpaper_zoey_3a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+21),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+21]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude" style "reward_locked_style"

        if persistent.epi_card4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("epi_wallpaper_zoey_4a_idle")
                    hover Transform ("epi_wallpaper_zoey_4a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+22),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+22]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Interlude" style "reward_locked_style"

        if persistent.ep9_card1:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_camila_1a_idle")
                    hover Transform ("ep9_wallpaper_camila_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+23),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+23]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Others" style "reward_locked_style"

        if persistent.ep9_card2:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_jill_1a_idle")
                    hover Transform ("ep9_wallpaper_jill_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+24),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+24]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Jill" style "reward_locked_style"

        if persistent.ep9_card3:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_jill_2a_idle")
                    hover Transform ("ep9_wallpaper_jill_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+25),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+25]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Jill" style "reward_locked_style"

        if persistent.ep9_card4:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_josy_1a_idle")
                    hover Transform ("ep9_wallpaper_josy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+26),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+26]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Josy & Maya" style "reward_locked_style"

        if persistent.ep9_card5:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_josy_2a_idle")
                    hover Transform ("ep9_wallpaper_josy_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+27),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+27]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Josy & Maya" style "reward_locked_style"

        if persistent.ep9_card6:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_maya_1a_idle")
                    hover Transform ("ep9_wallpaper_maya_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+28),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+28]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Josy & Maya" style "reward_locked_style"

        if persistent.ep9_card7:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_maya_2a_idle")
                    hover Transform ("ep9_wallpaper_maya_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+29),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+29]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Josy & Maya" style "reward_locked_style"

        if persistent.ep9_card8:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_riona_1a_idle")
                    hover Transform ("ep9_wallpaper_riona_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+30),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+30]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Others" style "reward_locked_style"

        if persistent.ep9_card17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_riona_2a_idle")
                    hover Transform ("ep9_wallpaper_riona_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+31),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+31]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Others" style "reward_locked_style"

        if persistent.ep9_card18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_riona_3a_idle")
                    hover Transform ("ep9_wallpaper_riona_3a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+32),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+32]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Others" style "reward_locked_style"

        if persistent.ep9_card19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_lily_1a_idle")
                    hover Transform ("ep9_wallpaper_lily_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+33),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+33]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Others" style "reward_locked_style"

        if persistent.ep9_card20:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep9_wallpaper_lily_2a_idle")
                    hover Transform ("ep9_wallpaper_lily_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+34),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+34]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 9 - Others" style "reward_locked_style"

        if persistent.ep10_card13:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_cathy_1a_idle")
                    hover Transform ("ep10_wallpaper_cathy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+35),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+35]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card14:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_cathy_2a_idle")
                    hover Transform ("ep10_wallpaper_cathy_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+36),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+36]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_envy_1a_idle")
                    hover Transform ("ep10_wallpaper_envy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+37),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+37]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_envy_2a_idle")
                    hover Transform ("ep10_wallpaper_envy_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+38),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+38]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_quinn_1a_idle")
                    hover Transform ("ep10_wallpaper_quinn_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+39),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+39]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_quinn_2a_idle")
                    hover Transform ("ep10_wallpaper_quinn_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+40),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+40]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_nora_1a_idle")
                    hover Transform ("ep10_wallpaper_nora_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+41),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+41]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep10_card10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep10_wallpaper_nora_2a_idle")
                    hover Transform ("ep10_wallpaper_nora_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+42),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+42]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 10 - Others" style "reward_locked_style"

        if persistent.ep11_card9:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep11_wallpaper_isabella_2a_idle")
                    hover Transform ("ep11_wallpaper_isabella_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+43),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+43]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Isabella" style "reward_locked_style"

        if persistent.ep11_card10:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep11_wallpaper_isabella_1a_idle")
                    hover Transform ("ep11_wallpaper_isabella_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+44),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+44]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Isabella" style "reward_locked_style"

        if persistent.ep11_card11:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep11_wallpaper_sage_2a_idle")
                    hover Transform ("ep11_wallpaper_sage_2a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+45),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+45]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Sage" style "reward_locked_style"

        if persistent.ep11_card12:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep11_wallpaper_sage_1a_idle")
                    hover Transform ("ep11_wallpaper_sage_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+46),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+46]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 11 - Sage" style "reward_locked_style"

        if persistent.ep12_card15:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep12_wallpaper_josy_2_idle")
                    hover Transform ("ep12_wallpaper_josy_2_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+47),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+47]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Josy & Maya" style "reward_locked_style"

        if persistent.ep12_card16:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep12_wallpaper_josy_1a_idle")
                    hover Transform ("ep12_wallpaper_josy_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+48),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+48]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Josy & Maya" style "reward_locked_style"

        if persistent.ep12_card17:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep12_wallpaper_maya_2_idle")
                    hover Transform ("ep12_wallpaper_maya_2_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+49),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+49]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Josy & Maya" style "reward_locked_style"

        if persistent.ep12_card18:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("ep12_wallpaper_maya_1a_idle")
                    hover Transform ("ep12_wallpaper_maya_1a_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+50),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+50]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - Josy & Maya" style "reward_locked_style"

        if persistent.ep12_card19:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    idle Transform ("2d_jb_elena_idle")
                    hover Transform ("2d_jb_elena_hover")
                    action (SetVariable("tmpInt2",len(new_art_girl_name_list)+51),Show("rewards_renders_screen"))
                if persistent.rewards_seen_list[tmpInt][len(new_art_girl_name_list)+51]:
                    text "{font=fonts/Redressed.ttf}!{/font}" style "reward_new_style"
                else:
                    text "" style "reward_new_style"
        else:
            vbox xalign 0.5 yalign 0.5:
                add "locked"
                text "Ep 12 - DIKmas" style "reward_locked_style"






image epi_wallpaper_zoey_3 = Transform(Movie(play="%s/rewards/epi/epi_wallpaper_zoey_3a.webm" % persistent.img_dir, start_image="epi_wallpaper_zoey_3a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image epi_wallpaper_zoey_4 = Transform(Movie(play="%s/rewards/epi/epi_wallpaper_zoey_4a.webm" % persistent.img_dir, start_image="epi_wallpaper_zoey_4a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep9_wallpaper_jill_2 = Transform(Movie(play="%s/rewards/ep9/ep9_wallpaper_jill_2a.webm" % persistent.img_dir, start_image="ep9_wallpaper_jill_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep9_wallpaper_josy_2 = Transform(Movie(play="%s/rewards/ep9/ep9_wallpaper_josy_2a.webm" % persistent.img_dir, start_image="ep9_wallpaper_josy_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep9_wallpaper_maya_2 = Transform(Movie(play="%s/rewards/ep9/ep9_wallpaper_maya_2a.webm" % persistent.img_dir, start_image="ep9_wallpaper_maya_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep9_wallpaper_lily_1 = Transform(Movie(play="%s/rewards/ep9/ep9_wallpaper_lily_1a.webm" % persistent.img_dir, start_image="ep9_wallpaper_lily_1a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep9_wallpaper_riona_2 = Transform(Movie(play="%s/rewards/ep9/ep9_wallpaper_riona_2a.webm" % persistent.img_dir, start_image="ep9_wallpaper_riona_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))

image ep10_wallpaper_cathy_2 = Transform(Movie(play="%s/rewards/ep10/ep10_wallpaper_cathy_2a.webm" % persistent.img_dir, start_image="ep10_wallpaper_cathy_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep10_wallpaper_envy_2 = Transform(Movie(play="%s/rewards/ep10/ep10_wallpaper_envy_2a.webm" % persistent.img_dir, start_image="ep10_wallpaper_envy_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep10_wallpaper_quinn_2 = Transform(Movie(play="%s/rewards/ep10/ep10_wallpaper_quinn_2a.webm" % persistent.img_dir, start_image="ep10_wallpaper_quinn_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep10_wallpaper_nora_2 = Transform(Movie(play="%s/rewards/ep10/ep10_wallpaper_nora_2a.webm" % persistent.img_dir, start_image="ep10_wallpaper_nora_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))

image ep11_wallpaper_isabella_2 = Transform(Movie(play="%s/rewards/ep11/ep11_wallpaper_isabella_2a.webm" % persistent.img_dir, start_image="ep11_wallpaper_isabella_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep11_wallpaper_sage_2 = Transform(Movie(play="%s/rewards/ep11/ep11_wallpaper_sage_2a.webm" % persistent.img_dir, start_image="ep11_wallpaper_sage_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))

image ep12_wallpaper_josy_2 = Transform(Movie(play="%s/rewards/ep12/ep12_wallpaper_josy_2a.webm" % persistent.img_dir, start_image="ep12_wallpaper_josy_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
image ep12_wallpaper_maya_2 = Transform(Movie(play="%s/rewards/ep12/ep12_wallpaper_maya_2a.webm" % persistent.img_dir, start_image="ep12_wallpaper_maya_2a_start"), size=(1920 * persistent.scale_factor, 1080 * persistent.scale_factor))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

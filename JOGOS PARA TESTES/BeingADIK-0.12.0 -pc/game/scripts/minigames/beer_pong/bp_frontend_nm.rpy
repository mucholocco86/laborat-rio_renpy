screen bp_screen_nm:
    tag bp_screen_nm
    modal True

    if bp_player_turn:
        add "bp_%s_def_%d_%s" % (bp_cpu_name.lower(),max(1,bp_cpu_cups),bp_ep_suffix)
    else:
        add "bp_%s_off_%d_%s" % (bp_cpu_name.lower(),max(1,bp_cpu_cups),bp_ep_suffix)

    if bp_showing_img:
        if not bp_game_over:
            timer bp_delay repeat True action Function(bp_hide_image_nm)
        add bp_img_name at bp_dissolve


    if bp_showing_img:
        vbox:
            xalign .98
            yalign 0.95
            xminimum 500 * persistent.scale_factor
            xmaximum 500 * persistent.scale_factor
            text "%s" % bp_action_msg style "bp_action_msg_style"


    if not bp_showing_img:
        if bp_player_turn:
            vbox:
                xalign 1.0
                xoffset 160 + (persistent.scale_factor-1)*1300
                yoffset (persistent.scale_factor-1)*(8)
                yalign 0.75
                spacing 15 * persistent.scale_factor - (persistent.scale_factor-1)*2
                imagebutton:
                    xminimum int(config.screen_width * 0.3) * persistent.scale_factor
                    xmaximum int(config.screen_width * 0.3) * persistent.scale_factor
                    yminimum 70 * persistent.scale_factor
                    ymaximum 70 * persistent.scale_factor
                    ypadding 10 * persistent.scale_factor
                    xpadding 15 * persistent.scale_factor
                    idle "sex_choices_idle"
                    hover "sex_choices_hover"
                    action Function(bp_shot_nm,bp_player_turn,0),SetVariable("tmpInt",0)
                    hovered SetVariable("tmpInt",1)
                    unhovered SetVariable("tmpInt",0)
                imagebutton:
                    xminimum int(config.screen_width * 0.3) * persistent.scale_factor
                    xmaximum int(config.screen_width * 0.3) * persistent.scale_factor
                    yminimum 70 * persistent.scale_factor
                    ymaximum 70 * persistent.scale_factor
                    ypadding 10 * persistent.scale_factor
                    xpadding 15 * persistent.scale_factor
                    idle "sex_choices_idle"
                    hover "sex_choices_hover"
                    action Function(bp_shot_nm,bp_player_turn,1),SetVariable("tmpInt",0)
                    hovered SetVariable("tmpInt",2)
                    unhovered SetVariable("tmpInt",0)
                imagebutton:
                    xminimum int(config.screen_width * 0.3) * persistent.scale_factor
                    xmaximum int(config.screen_width * 0.3) * persistent.scale_factor
                    yminimum 70 * persistent.scale_factor
                    ymaximum 70 * persistent.scale_factor
                    ypadding 10 * persistent.scale_factor
                    xpadding 15 * persistent.scale_factor
                    idle "sex_choices_idle"
                    hover "sex_choices_hover"
                    action Function(bp_shot_nm,bp_player_turn,2),SetVariable("tmpInt",0)
                    hovered SetVariable("tmpInt",3)
                    unhovered SetVariable("tmpInt",0)

            vbox:
                xalign 0.865
                yalign 0.755
                spacing 45 * persistent.scale_factor
                if tmpInt == 1:
                    text "Arc shot" style "bp_nm_hover_style"
                else:
                    text "Arc shot" style "bp_nm_idle_style"
                if tmpInt == 2:
                    text "Fastball " style "bp_nm_hover_style"
                else:
                    text "Fastball " style "bp_nm_idle_style"
                if tmpInt == 3:
                    text "Bounce shot" style "bp_nm_hover_style"
                else:
                    text "Bounce shot" style "bp_nm_idle_style"
        else:
            vbox:
                yalign 0.75
                xalign 1.0
                xoffset 160 + (persistent.scale_factor-1)*1300
                yoffset (persistent.scale_factor-1)*(6)
                spacing 15 * persistent.scale_factor - (persistent.scale_factor-1)*2

                imagebutton:
                    xminimum int(config.screen_width * 0.3) * persistent.scale_factor
                    xmaximum int(config.screen_width * 0.3) * persistent.scale_factor
                    yminimum 70 * persistent.scale_factor
                    ymaximum 70 * persistent.scale_factor
                    ypadding 10 * persistent.scale_factor
                    xpadding 15 * persistent.scale_factor
                    idle "sex_choices_idle"
                    hover "sex_choices_hover"
                    action Function(bp_def_nm,True,1),SetVariable("tmpInt",0)
                    hovered SetVariable("tmpInt",1)
                    unhovered SetVariable("tmpInt",0)
                imagebutton:
                    xminimum int(config.screen_width * 0.3) * persistent.scale_factor
                    xmaximum int(config.screen_width * 0.3) * persistent.scale_factor
                    yminimum 70 * persistent.scale_factor
                    ymaximum 70 * persistent.scale_factor
                    ypadding 10 * persistent.scale_factor
                    xpadding 15 * persistent.scale_factor
                    idle "sex_choices_idle"
                    hover "sex_choices_hover"
                    action Function(bp_def_nm,True,2),SetVariable("tmpInt",0)
                    hovered SetVariable("tmpInt",1)
                    unhovered SetVariable("tmpInt",0)
            vbox:
                xalign 0.825
                yalign 0.753
                spacing 45 * persistent.scale_factor
                if tmpInt == 1:
                    text "Tease" style "bp_nm_hover_style"
                else:
                    text "Tease" style "bp_nm_idle_style"
                if tmpInt == 2:
                    text "Focus" style "bp_nm_hover_style"
                else:
                    text "Focus" style "bp_nm_idle_style"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

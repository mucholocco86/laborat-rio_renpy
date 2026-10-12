init:
    $ v_sp_cum_enabled = True
    $ v_sp_sexspeed = 1
    $ v_sp_sexcamera = 1
    $ v_sex_activity =""

################# MC - TASHA ##########################

screen scr_ep01_sex_player_1:
    vpgrid:
        xalign 0.99
        yalign 0.3
        cols 1
        spacing 2
        if v_sex_activity == "rev_cow":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep01_01_mc_tasha_revcow")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_sp_ep01_01_mc_tasha_revcow")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep01_01_mc_tasha_revcow")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep01_01_mc_tasha_revcow")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep01_01_mc_tasha_revcow")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep01_01_mc_tasha_revcow")]


        if v_sex_activity == "sidefuck":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]


        if v_sex_activity == "missionary":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep01_01_mc_tasha_missionary")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep01_01_mc_tasha_missionary")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep01_01_mc_tasha_missionary")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep01_01_mc_tasha_missionary")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep01_01_mc_tasha_missionary")]


        imagebutton:
            auto "sp_cum_%s"
            sensitive v_sp_cum_enabled
            action [Hide("scr_ep01_sex_player_1"),Jump ("lb_sp_ep01_01_mc_tasha_cum")]



    vpgrid:
        xalign 0.99
        yalign 0.65
        cols 1
        spacing 2

        imagebutton:
            auto "sp_cowgirl_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","rev_cow"),Jump("lb_sp_ep01_01_mc_tasha_revcow")]

        imagebutton:
            auto "sp_missionary_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","missionary"),Jump("lb_sp_ep01_01_mc_tasha_missionary")]


        imagebutton:
            auto "sp_spoon_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","sidefuck"),Jump("lb_sp_ep01_01_mc_tasha_sidefuck")]






label lb_sp_ep01_01_mc_tasha_revcow:
    show scr_ep01_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow_front1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h126b

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow_front2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h126b

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow_front3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h126b



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h122

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h122

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h122



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h124

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h124

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_revcow_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h124

    hide screen scr_ep01_sex_player_1
    call screen scr_ep01_sex_player_1


label lb_sp_ep01_01_mc_tasha_sidefuck:
    show scr_ep01_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259a

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259a

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259a



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck_top1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259b

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck_top2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259b

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_sidefuck_top3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h259b

    hide screen scr_ep01_sex_player_1
    call screen scr_ep01_sex_player_1





label lb_sp_ep01_01_mc_tasha_missionary:
    show scr_ep01_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_missionary1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h107a

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_missionary2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h107a

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_missionary3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h107a



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_missionary_side1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h107b

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_missionary_side2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h107b

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_tasha_missionary_side3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h107b


    hide screen scr_ep01_sex_player_1
    call screen scr_ep01_sex_player_1



################# MC - MIK ##########################


screen scr_ep01_sex_player_2:
    vpgrid:
        xalign 0.99
        yalign 0.3
        cols 1
        spacing 2


        if v_sex_activity == "rev_cow":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep01_01_mc_mik_revcow")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep01_01_mc_mik_revcow")]


            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep01_01_mc_mik_revcow")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep01_01_mc_mik_revcow")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep01_01_mc_mik_revcow")]

        if v_sex_activity == "doggy":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep01_01_mc_mik_doggy")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep01_01_mc_mik_doggy")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep01_01_mc_mik_doggy")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep01_01_mc_mik_doggy")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep01_01_mc_mik_doggy")]

        if v_sex_activity == "standing":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep01_01_mc_mik_standing")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep01_01_mc_mik_standing")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep01_01_mc_mik_standing")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep01_01_mc_mik_standing")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep01_01_mc_mik_standing")]
        imagebutton:
            auto "sp_cum_%s"
            sensitive v_sp_cum_enabled
            action [Hide("scr_ep01_sex_player_2"),Jump ("lb_sp_ep01_01_mc_mik_cum")]



    vpgrid:
        xalign 0.99
        yalign 0.7
        cols 1
        spacing 2

        imagebutton:
            auto "sp_cowgirl_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","rev_cow"),Jump("lb_sp_ep01_01_mc_mik_revcow")]

        imagebutton:
            auto "sp_doggy_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","doggy"),Jump("lb_sp_ep01_01_mc_mik_doggy")]

        imagebutton:
            auto "sp_wallback_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","standing"),Jump("lb_sp_ep01_01_mc_mik_standing")]



label lb_sp_ep01_01_mc_mik_revcow:
    show scr_ep01_sex_player_2
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_revcow_far1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h209

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_revcow_far2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h209

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_revcow_far3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h209



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_revcow_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h206

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_revcow_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h206

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_revcow_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h206


    hide screen scr_ep01_sex_player_2
    call screen scr_ep01_sex_player_2



label lb_sp_ep01_01_mc_mik_doggy:
    show scr_ep01_sex_player_2
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_doggy1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h220

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_doggy2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h220

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_doggy3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h220



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_doggy_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h222

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_doggy_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h222

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_doggy_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h222


    hide screen scr_ep01_sex_player_2
    call screen scr_ep01_sex_player_2





label lb_sp_ep01_01_mc_mik_standing:
    show scr_ep01_sex_player_2
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_behind1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h230

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_behind2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h230

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_behind3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h230



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_behind_floor1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h239

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_behind_floor2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h239

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_mik_behind_floor3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel h239


    hide screen scr_ep01_sex_player_2
    call screen scr_ep01_sex_player_2




################# MC - MIK - TASHA ##########################



screen scr_ep01_sex_player_3:
    vpgrid:
        xalign 0.99
        yalign 0.3
        cols 1
        spacing 2


        if v_sex_activity == "rev_cow":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_ep01_The_MC_3some_revcow")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_ep01_The_MC_3some_revcow")]


            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_ep01_The_MC_3some_revcow")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_ep01_The_MC_3some_revcow")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_ep01_The_MC_3some_revcow")]

        if v_sex_activity == "doggy":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_ep01_The_MC_3some_doggy")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_ep01_The_MC_3some_doggy")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_ep01_The_MC_3some_doggy")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_ep01_The_MC_3some_doggy")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_ep01_The_MC_3some_doggy")]

        if v_sex_activity == "sidefuck":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_ep01_The_MC_3some_sidefuck")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_ep01_The_MC_3some_sidefuck")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_ep01_The_MC_3some_sidefuck")]




            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_ep01_The_MC_3some_sidefuck")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_ep01_The_MC_3some_sidefuck")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_ep01_The_MC_3some_sidefuck")]

        if v_sex_activity == "missionary":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_ep01_The_MC_3some_missionary")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_ep01_The_MC_3some_missionary")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_ep01_The_MC_3some_missionary")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_ep01_The_MC_3some_missionary")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_ep01_The_MC_3some_missionary")]


        imagebutton:
            auto "sp_cum_%s"
            sensitive v_sp_cum_enabled
            action [Hide("scr_ep01_sex_player_3"),Jump ("lb_ep01_The_MC_3some_sex_scene_cum")]



    vpgrid:
        xalign 0.99
        yalign 0.7
        cols 1
        spacing 2

        imagebutton:
            auto "sp_cowgirl_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","rev_cow"),Jump("lb_ep01_The_MC_3some_revcow")]

        imagebutton:
            auto "sp_doggy_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","doggy"),Jump("lb_ep01_The_MC_3some_doggy")]

        imagebutton:
            auto "sp_spoon_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","sidefuck"),Jump("lb_ep01_The_MC_3some_sidefuck")]

        imagebutton:
            auto "sp_missionary_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","missionary"),Jump("lb_ep01_The_MC_3some_missionary")]





label lb_ep01_The_MC_3some_revcow:
    show scr_ep01_sex_player_3
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_reverse_cow_far1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h136

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_reverse_cow_far2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h136

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_reverse_cow_far3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h136



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_reverse_cow_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h139

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_reverse_cow_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h139

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_reverse_cow_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h139


    hide screen scr_ep01_sex_player_3
    call screen scr_ep01_sex_player_3





label lb_ep01_The_MC_3some_doggy:
    show scr_ep01_sex_player_3
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_doggy1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h143

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_doggy2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h143

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_doggy3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h143



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_doggy_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h145

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_doggy_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h145

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_doggy_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h145


    hide screen scr_ep01_sex_player_3
    call screen scr_ep01_sex_player_3




label lb_ep01_The_MC_3some_sidefuck:
    show scr_ep01_sex_player_3
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h112

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h112

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h112



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h113

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h113

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h113



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck_back1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h114b

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck_back2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h114b

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_sidefuck_back3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h114b

    hide screen scr_ep01_sex_player_3
    call screen scr_ep01_sex_player_3



label lb_ep01_The_MC_3some_missionary:
    show scr_ep01_sex_player_3
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_missionary1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h121

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_missionary2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h121

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_missionary3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h121



    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_missionary_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h128

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_missionary_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h128

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep01_mc_3some_missionary_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc hotel3some h128


    hide screen scr_ep01_sex_player_3
    call screen scr_ep01_sex_player_3

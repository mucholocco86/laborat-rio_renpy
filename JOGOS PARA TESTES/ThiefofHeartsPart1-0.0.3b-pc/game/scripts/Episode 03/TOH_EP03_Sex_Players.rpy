################# MC - ZORA ##########################

screen scr_ep03_sex_player_1:
    vpgrid:
        xalign 0.99
        yalign 0.3
        cols 1
        spacing 2
        if v_sex_activity == "missionary":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep03_01_mc_zora_missionary")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_sp_ep03_01_mc_zora_missionary")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep03_01_mc_zora_missionary")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep03_01_mc_zora_missionary")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep03_01_mc_zora_missionary")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep03_01_mc_zora_missionary")]

        if v_sex_activity == "cowgirl":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep03_01_mc_zora_cowgirl")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_sp_ep03_01_mc_zora_cowgirl")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep03_01_mc_zora_cowgirl")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep03_01_mc_zora_cowgirl")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep03_01_mc_zora_cowgirl")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep03_01_mc_zora_cowgirl")]

        if v_sex_activity == "spoon":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep03_01_mc_zora_spoon")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_sp_ep03_01_mc_zora_spoon")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep03_01_mc_zora_spoon")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep03_01_mc_zora_spoon")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep03_01_mc_zora_spoon")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep03_01_mc_zora_spoon")]

        if v_sex_activity == "doggy":
            imagebutton:
                auto "sp_camera_%s"
                if v_sp_sexcamera == 1:
                    action [SetVariable("v_sp_sexcamera",2), Jump("lb_sp_ep03_01_mc_zora_doggy")]
                if v_sp_sexcamera == 2:
                    action [SetVariable("v_sp_sexcamera",3), Jump("lb_sp_ep03_01_mc_zora_doggy")]
                if v_sp_sexcamera == 3:
                    action [SetVariable("v_sp_sexcamera",1), Jump("lb_sp_ep03_01_mc_zora_doggy")]

            imagebutton:
                auto "sp_speed_{}_%s".format(v_sp_sexspeed)
                sensitive not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled
                if v_sp_sexspeed == 1:
                    action [SetVariable("v_sp_sexspeed",2), Jump("lb_sp_ep03_01_mc_zora_doggy")]
                if v_sp_sexspeed == 2:
                    action [SetVariable("v_sp_sexspeed",3), Jump("lb_sp_ep03_01_mc_zora_doggy")]
                if v_sp_sexspeed == 3:
                    action [SetVariable("v_sp_sexspeed",1), Jump("lb_sp_ep03_01_mc_zora_doggy")]

        imagebutton:
            auto "sp_cum_%s"
            sensitive v_sp_cum_enabled
            action [Hide("scr_ep03_sex_player_1"),Jump ("lb_ep03_02_05_The_MC_goes_over_to_Zoras_place_Climax")]



    vpgrid:
        xalign 0.99
        if v_ep03_02_05_zora_counter >= 3:
            yalign 0.74
        else:
            yalign 0.65
        cols 1
        spacing 2
        imagebutton:
            auto "sp_missionary_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","missionary"),Jump("lb_sp_ep03_01_mc_zora_missionary")]

        imagebutton:
            auto "sp_cowgirl_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","cowgirl"),Jump("lb_sp_ep03_01_mc_zora_cowgirl")]

        imagebutton:
            auto "sp_spoon_%s"
            action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","spoon"),Jump("lb_sp_ep03_01_mc_zora_spoon")]

        if v_ep03_02_05_zora_counter >= 3:
            imagebutton:
                auto "sp_doggy_%s"
                action [SetVariable("v_sp_sexcamera",1),SetVariable("v_sp_sexspeed",1),SetVariable("v_sp_cum_enabled",True),SetVariable("v_sex_activity","doggy"),Jump("lb_sp_ep03_01_mc_zora_doggy")]



label lb_sp_ep03_01_mc_zora_missionary:
    show scr_ep03_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_far1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s066

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_far2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s066

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_far3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s066
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s067

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s067

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s067
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_face1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s068

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_face2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s068

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_missionary_face3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s068

    hide screen scr_ep03_sex_player_1
    call screen scr_ep03_sex_player_1

label lb_sp_ep03_01_mc_zora_cowgirl:
    show scr_ep03_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_far1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s069

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_far2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s069

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_far3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s069
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s070

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s070

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s070
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_front1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s071

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_front2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s071

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_cowgirl_front3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s071

    hide screen scr_ep03_sex_player_1
    call screen scr_ep03_sex_player_1

label lb_sp_ep03_01_mc_zora_spoon:
    show scr_ep03_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_far1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s072

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_far2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s072

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_far3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s072
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s073

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s073

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s073
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_side1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s074

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_side2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s074

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_spoon_side3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s074

    hide screen scr_ep03_sex_player_1
    call screen scr_ep03_sex_player_1


label lb_sp_ep03_01_mc_zora_doggy:
    show scr_ep03_sex_player_1
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_far1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s075

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_far2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s075

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 1:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_far3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s075
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_front1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s077

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_front2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s077

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 2:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_front3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s077
    #---
    if v_sp_sexspeed == 1 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_close1:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s076

    if v_sp_sexspeed == 2 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_close2:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s076

    if v_sp_sexspeed == 3 and v_sp_sexcamera == 3:
        if not persistent.v_sex_anim_enabled_locked and persistent.v_sex_anim_enabled:
            scene anim_ep03_zoras_house_doggy_close3:
                size (config.screen_width, config.screen_height)
        elif True:
            show sc ep3 zorasplace sex s076

    hide screen scr_ep03_sex_player_1
    call screen scr_ep03_sex_player_1

init:
    $ v_mm_replay_tab = 0

    $ replay_menu = False



    if persistent.replay_ep01_tasha_night == None:
        $ persistent.replay_ep01_tasha_night = True

    if persistent.replay_ep01_mik_night == None:
        $ persistent.replay_ep01_mik_night = True

    if persistent.replay_ep01_3some == None:
        $ persistent.replay_ep01_3some = True



    if persistent.replay_ep02_tattoogirl_sex == None:
        $ persistent.replay_ep02_tattoogirl_sex = True

    if persistent.replay_ep02_mc_dreams == None:
        $ persistent.replay_ep02_mc_dreams = True


    if persistent.replay_ep03_mc_zoras_place == None:
        $ persistent.replay_ep03_mc_zoras_place = True




    if persistent.replay_bella_fantasy == None:
        $ persistent.replay_bella_fantasy = True

    if persistent.replay_vivian_fantasy == None:
        $ persistent.replay_vivian_fantasy = True

    if persistent.replay_vivian_fantasy_bathroom == None:
        $ persistent.replay_vivian_fantasy_bathroom = True

    if persistent.replay_ariel_fantasy == None:
        $ persistent.replay_ariel_fantasy = True

    if persistent.replay_Megan_fantasy_drive == None:
        $ persistent.replay_Megan_fantasy_drive = True



    if persistent.replay_ep02_mysterygirl_fantasy == None:
        $ persistent.replay_ep02_mysterygirl_fantasy = True

    if persistent.replay_ep02_bella_solo_fantasy == None:
        $ persistent.replay_ep02_bella_solo_fantasy = True

    if persistent.replay_ep02_zora_shower_fantasy == None:
        $ persistent.replay_ep02_zora_shower_fantasy = True

    if persistent.replay_ep02_juliet_changing_room_fantasy == None:
        $ persistent.replay_ep02_juliet_changing_room_fantasy = True

    if persistent.replay_ep02_ariel_moviedate_fantasy == None:
        $ persistent.replay_ep02_ariel_moviedate_fantasy = True




    if persistent.replay_ep03_ariel_bed_fantasy == None:
        $ persistent.replay_ep03_ariel_bed_fantasy = True

    if persistent.replay_ep03_bella_maze_fantasy == None:
        $ persistent.replay_ep03_bella_maze_fantasy = True

    if persistent.replay_ep03_lucy_bathroom_fantasy == None:
        $ persistent.replay_ep03_lucy_bathroom_fantasy = True

    if persistent.replay_ep03_officer_alley_fantasy == None:
        $ persistent.replay_ep03_officer_alley_fantasy = True



screen scr_end_replay:
    textbutton _("END REPLAY") xalign 0.01 yalign 0.01 action EndReplay():
        text_outlines [ (3, "#000000", 0, 0) ]




screen scr_mm_replay_menu:
    key "game_menu" action [Hide("scr_mm_replay_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]



    add "background_replay"
    imagebutton:
        idle "img_gradient_[persistent.v_mm_gradient[persistent.v_mm_gradient_order]]" action NullAction()

    add "img_replay_frame"

    hbox:
        xalign 0.6
        yalign 0.9
        style_prefix "radio"
        textbutton _("REPLAY SCENES") action SetVariable("v_mm_replay_tab",0) text_outlines [ (3, "#000000", 0, 0) ]
        textbutton _("SECRET SCENES") action SetVariable("v_mm_replay_tab",1) text_outlines [ (3, "#000000", 0, 0) ]


    if replay_menu:
        imagebutton:
            xalign 0.01
            yalign 0.98
            auto "btn_mm_back_%s" action Return()
    else:
        imagebutton:
            xalign 0.01
            yalign 0.98
            auto "btn_mm_back_%s" action [Hide("scr_mm_replay_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

        imagebutton:
            xalign 0.98
            yalign 0.98
            auto "btn_mm_exit_%s" action [Hide("scr_mm_replay_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]






    if v_mm_replay_tab == 0:
        use scr_mm_replay_sex_scenes
    else:
        use scr_mm_replay_fantasy_scenes



screen scr_mm_replay_sex_scenes:
    vpgrid:
        align (0.879, 0.4)
        ysize 0.675
        cols 4
        spacing 5
        draggable True
        mousewheel True


        side_xalign 0.5



        if persistent.replay_ep01_tasha_night == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/sex_scenes/btnreplay_ep01_tasha_night_%s.jpg"
                    action Replay("lb_ep01_The_MC_and_Tasha_sex_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5

        if persistent.replay_ep01_mik_night == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/sex_scenes/btnreplay_ep01_mik_night_%s.jpg"
                    action Replay("lb_ep01_The_MC_and_mik_sex_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep01_3some == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/sex_scenes/btnreplay_ep01_3some_%s.jpg"
                    action Replay("lb_ep01_The_MC_3some_sex_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5



        if persistent.replay_ep02_mc_dreams == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/sex_scenes/btnreplay_ep02_mc_dreams_%s.jpg"
                    action Replay("lb_ep02_03_01_The_MC_has_sex_dreams")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep02_tattoogirl_sex == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/sex_scenes/btnreplay_ep02_tattoogirl_sex_%s.jpg"
                    action Replay("lb_ep02_03_09_The_MC_sees_the_tattoo_girl_from_the_parlour")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5



        if persistent.replay_ep03_mc_zoras_place == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep03/sex_scenes/btnreplay_ep03_mc_zoras_place_%s.jpg"
                    action Replay("lb_ep03_02_05_The_MC_goes_over_to_Zoras_place_sex")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5



screen scr_mm_replay_fantasy_scenes:
    frame:
        yalign 0.98
        xalign 0.5
        xsize 0.73
        has vbox
        if renpy.variant("small"):
            text "{size=30}DISCLAIMER: All secret scenes are considered \"non-canon\" and thus are fantasy scenes that have no bearing on the story or how it unfolds.{/size}" style "char_info_description"
        else:
            text "{size=20}DISCLAIMER: All secret scenes are considered \"non-canon\" and thus are fantasy scenes that have no bearing on the story or how it unfolds.{/size}" style "char_info_description"
    vpgrid:
        align (0.879, 0.4)
        ysize 0.675
        cols 4
        spacing 5
        draggable True
        mousewheel True


        side_xalign 0.5

        if persistent.replay_bella_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/fantasy_scenes/btnreplay_ep01_bella_fantasy_%s.jpg"
                    action Replay("lb_ep01_03_02_Bella_Room_1_fantasy_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_vivian_fantasy_bathroom == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/fantasy_scenes/btnreplay_ep01_vivian_fantasy_bathroom_%s.jpg"
                    action Replay("lb_ep01_vivians_room_fantasy_shower")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ariel_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/fantasy_scenes/btnreplay_ep01_ariel_fantasy_%s.jpg"
                    action Replay("lb_ep01_13_03_Ariel_Room_1_fantasy_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_vivian_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/fantasy_scenes/btnreplay_ep01_vivian_fantasy_%s.jpg"
                    action Replay("lb_ep01_06_01_Vivian_Work_1_fantasy_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5

        if persistent.replay_Megan_fantasy_drive == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep01/fantasy_scenes/btnreplay_ep01_megan_fantasy_%s.jpg"
                    action Replay("lb_ep01_Megan_fantasy_drive")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5







        if persistent.replay_ep02_mysterygirl_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/fantasy_scenes/btnreplay_ep02_mysterygirl_fantasy_%s.jpg"
                    action Replay("lb_ep02_01_04_The_MC_catches_up_with_Punk_Girl_NC")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep02_bella_solo_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/fantasy_scenes/btnreplay_ep02_bella_solo_fantasy_%s.jpg"
                    action Replay("lb_ep02_02_03_The_late_chat_with_Bella_NC")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep02_zora_shower_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/fantasy_scenes/btnreplay_ep02_zora_shower_fantasy_%s.jpg"
                    action Replay("lb_ep02_03_07_zora_fantasy_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep02_juliet_changing_room_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/fantasy_scenes/btnreplay_ep02_juliet_changing_room_fantasy_%s.jpg"
                    action Replay("lb_ep02_03_08_The_MCs_private_session_with_Juliet_fantasy")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep02_ariel_moviedate_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep02/fantasy_scenes/btnreplay_ep02_ariel_moviedate_fantasy_%s.jpg"
                    action Replay("lb_ep02_03_11_The_MC_watches_a_movie_with_Ariel_fantasy")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5






        if persistent.replay_ep03_officer_alley_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep03/fantasy_scenes/btnreplay_ep03_officer_alley_fantasy_%s.jpg"
                    action Replay("lb_ep03_01_03_officer_justice_nc")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep03_ariel_bed_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep03/fantasy_scenes/btnreplay_ep03_ariel_bed_fantasy_%s.jpg"
                    action Replay("lb_ep03_01_06_ariel_masturbating")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep03_lucy_bathroom_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep03/fantasy_scenes/btnreplay_ep03_lucy_bathroom_fantasy_%s.jpg"
                    action Replay("lb_ep03_03_04_Lucy_NC")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5


        if persistent.replay_ep03_bella_maze_fantasy == False:
            vbox xalign 0.5 yalign 0.5:
                imagebutton:
                    focus_mask True
                    auto "images/replay/ep03/fantasy_scenes/btnreplay_ep03_bella_maze_fantasy_%s.jpg"
                    action Replay("lb_04_03_bella_nc_scene")

                text "" xalign 0.5 yalign 0.5
        else:
            vbox xalign 0.5 yalign 0.5:
                add "screens/locked.png"
                text "" xalign 0.5 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

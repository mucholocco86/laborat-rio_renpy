default persistent.mm_video = "default"

init python:
    tohpart1 = MultiPersistent("tohpart1.mrdotsgames.com")

    if not tohpart1.part1_part2_transfer:
        tohpart1.part1_part2_transfer = {}


init:
    $ v_part1_part2_transfer_failed = False


label splashscreen:
    $ default_mouse = "new"

    show bg adult warning with dissolve
    pause 2.0

    show bg support with dissolve
    pause 2.0

    show adult_gaming_disclaimer with dissolve
    pause 2.0

    scene black with dissolve
    with Pause(2)

    show ani_mrdotsgames:
        size (config.screen_width, config.screen_height)
    with faster_dissolve
    pause(12.0)
    scene black with dissolve
    with Pause(2)
    return

label start:
    stop music fadeout 1.0
    show black
    with Dissolve(1.0)
    pause 1.0
    jump lb_ep01_intro_01_fantasy_intro
    label start_pick_menu:
        hide redefine
        show text "How to start the game?":
            yalign 0.25
        menu:
            "Start game normally":
                scene black
                with dissolve
                jump lb_ep01_intro_01_fantasy_intro
            "Pick a Scene to Play":
                jump Scene_Select_Menu

label Scene_Select_Menu:
    scene black
    window hide
    $ v_choice_type = "main"
    menu:
        "GO BACK":
            jump start_pick_menu
        "Episode 01":
            menu:
                "GO BACK":
                    jump Scene_Select_Menu
                "Scene 01-00 - MC Introduction":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    jump lb_ep01_intro_01_fantasy_intro
                "Scene 01-01 - Intro Heist1 - Breaking In":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    jump lb_ep01_intro_02_heist_scene
                "Scene 01-02 - Intro Heist2 - Security Room":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    jump lb_ep01_intro_03_heist_scene
                "Scene 01-03 - Intro Heist3 - Dance and Escape":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    jump lb_ep01_intro_04_heist_scene
                "Scene 01-04 - Intro Heist4 - In the Van":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    jump lb_ep01_intro_05_heist_scene
                "Scene 02-01 - group Meeting at Home":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_group_meeting_home
                "Scene 03-01 - The Girls Rooms":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_girls_rooms
                "Scene 03-02 - MC Sneaks into Bella's Room":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    $ v_ep01_01_bella_room = True
                    jump lb_ep01_03_02_Bella_Room_1
                "Scene 03-03 - MC spies on Ariel":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    $ v_ep01_01_ariel_room = True
                    jump lb_ep01_Ariel_Room_1
                "Scene 03-04 - MC Sneaks into Vivian's Room":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    $ v_ep01_01_vivian_room = True
                    jump lb_ep01_vivians_room_3
                "Scene 04-00 - The MC wakes up on Day 2":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MCs_Room_1
                "Scene 04-01 - MC visits Bella at work":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    $ v_ep01_work_visit_options_1 = "[b_name]"
                    jump lb_ep01_04_01_Bella_Work_1
                "Scene 05-01 - MC visits Ariel at work":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    $ v_ep01_work_visit_options_1 = "[a_name]"
                    jump lb_ep01_05_01_Ariel_Work_1
                "Scene 06-01 - MC visits Vivian at work":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    $ v_ep01_work_visit_options_1 = "[v_name]"
                    jump lb_ep01_06_01_Vivian_Work_1
                "Scene 06-02 - MC & Bella Go to Tattoo Parlour":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_06_02_Tattoo_Parlour_1
                "Scene 07-01 - MC rides his bike to work":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_MC_rides_to_work
                "Scene 08-01 - MC arrives at the gym":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_arrives_at_work1
                "Scene 08-02 - MC meets Juliet":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_meets_Juliet1
                "Scene 09-01 - The MC and Harry at the club":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_and_Harry_at_the_club
                "Scene 09-02 - The MC and Harry with the girls at the hotel":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_and_Tasha_or_Mikayla_sex_path
                "Scene 10-01 - The MC wakes up the next morning":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_the_morning_after1
                "Scene 10-02 - The group Meeting":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_the_group_meeting1
                "Scene 11-01 - The MC talks with Vivian1":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_talks_with_Vivian1
                "Scene 11-02 - The MC talks with Bella1":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_talks_with_Bella1
                "Scene 11-03 - The MC talks with Ariel1":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_talks_with_Ariel1
                "Scene 12-01 - The MC talks with Victor":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_talks_with_Victor1
                "Scene 12-02 - The MC and Vivian infiltrate acting school":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_and_Vivian_acting_school1
                "Scene 12-03 - The MC meets Zora":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_meets_Zora
                "Scene 12-04 - The MC helps Ariel steal security cards":
                    menu:
                        "To test differend endings, did MC visit Ariel Last?\n(Dialog and the endings will depend on choices):"
                        "Yes":
                            $ v_ep01_mc_task_visit_options_3 = "Ariel"
                        "No":
                            $ v_ep01_mc_task_visit_options_1 = "Ariel"
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_12_04_card_theft1
                "Scene 12-05 - The MC gets a call from Megan":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_MC_gets_a_call_from_Megan1
                "Scene 12-06 - The MC and Bella at the Art School":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_and_Bella_at_the_art_school
                "Scene 13-01 - The MC sees Vivian in the bathroom":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_sees_Vivian_in_the_bathroom
                "Scene 13-02 - The MC gets his bike back":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_gets_his_bike_back
                "Scene 13-03 - The MC watches Ariel dress up/Bella's Yoga":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_13_03_MC_Evening_Visit1
                "Scene 14-01 - The MC goes to the art gallery with Vivian":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_goes_to_the_art_gallery
                "Scene 14-02 - Bonus Scene Date with Vivian":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_Bonus_Scene_Date_with_Vivian1
                "Scene 14-03 - Bonus Scene Date with Bella":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_Bonus_Scene_Date_with_Bella1
                "Scene 14-04 - Bonus Scene Date with Ariel":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_Bonus_Scene_Date_with_Ariel1
                "Scene 14-05 - The MC investigates the gang":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep01_The_MC_Investigates_the_gang
        "Episode 02":
            menu:
                "GO BACK":
                    jump Scene_Select_Menu
                "Scene 03-01 - The MC has sex dreams":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep02_03_01_The_MC_has_sex_dreams
                "Scene 03-07 - Session with Zora":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep02_03_07_Zora_arrives_at_the_gym
                "Scene 03-08 - Session with Juliet":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep02_03_08_The_MCs_private_session_with_Juliet
                "Scene 03-09 - The MC sees Tattoo Girl":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep02_03_09_The_MC_sees_the_tattoo_girl_from_the_parlour
                "Scene 03-10 - The MC returns home in the evening":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep02_03_10_The_MC_returns_home_in_the_evening
                "Scene 04-01 - The MC receives a call from Megan":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep02_04_01_The_MC_Receives_A_Call_From_Megan
        "Episode 03":
            menu:
                "GO BACK":
                    jump Scene_Select_Menu
                "Scene 01-01 - Megan Scene Continues":
                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_01_01_Megan_scene_continues
                "Scene 02-02 - At Bella's clothing store with Ariel":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_02_02_Trying_clothes_on_with_Ariel
                "Scene 02-04 - The MC speaks with Victor":


                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_02_04_The_MC_talks_with_Victor_at_the_house
                "Scene 02-05 - The MC goes over to Zoras place":


                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True

                    jump lb_ep03_02_05_The_MC_goes_over_to_Zoras_place
                "Scene 03-01 - TIME SKIP - Montage Scene over the next week":



                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True

                    jump lb_ep03_03_01_Time_Skip_Montage_MC_other_characters
                "Scene 03-02 - Intercepting the German Artist at the Airport":


                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_03_02_Intercepting_the_German_artist
                "Scene 03-03 - Ariel speaks with the MC":


                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_03_03_Ariel_speaks_with_the_MC
                "Scene 03-04 - The MC follows Victor":


                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_03_04_The_MC_follows_Victor
                "Scene 04-01 - The Final meeting before the Art Gallery Heist":


                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_04_01_Final_meeting_before_the_heist
                "Scene 04-02 - THE ART GALLERY HEIST - PART 1 - The Art Gallery Function":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_04_02_The_Art_Gallery_Heist_Part_1
                "Scene 04-03 - THE ART GALLERY HEIST - PART 2 - Bella and the MC":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_04_03_The_Art_Gallery_Heist_Part_2
                "Scene 04-04 - THE ART GALLERY HEIST - PART 3 - Evening Heist":

                    scene black
                    with dissolve
                    $ v_choice_type = ""
                    show screen toh_main_game_screen
                    $ v_mm_available = True
                    $ v_allow_redefine = True
                    jump lb_ep03_04_04_The_Art_Gallery_Heist_Part_3

label before_main_menu:
    if persistent.mm_music == "default":
        $ renpy.music.play("gui/main_menu_music.ogg", channel='music', loop=True)
    else:
        $ renpy.music.play("gui/main_menu_music_alt.ogg", channel='music', loop=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

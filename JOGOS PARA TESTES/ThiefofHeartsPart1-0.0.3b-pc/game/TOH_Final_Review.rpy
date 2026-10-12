init:
    $ v_review_stats_tab = 0
    $ v_review_count_ariel_result = ""
    $ v_review_count_bella_result = ""
    $ v_review_count_vivian_result = ""
    $ v_review_count_juliet_result = ""
    $ v_review_count_zora_result = ""
    $ v_review_count_justice_result = ""
    $ v_review_count_othergirls_result = ""
    $ justice_known = True
    $ othergirls_known = True


    $ v_ep03_zora_fantasy_counter = 0

    $ justice_love_level = 0

default v_review_episode = 1


init python:

    def count_points(who):
        
        
        v_list = [getattr(store, "v_ep01_"+who+"_respect_counter"),getattr(store, "v_ep01_"+who+"_cocky_counter"),getattr(store, "v_ep01_"+who+"_arrogant_counter")]
        
        
        
        v_index = v_list.index (max(v_list))
        
        if v_index == 0:
            setattr (store,"v_review_count_"+who+"_result","respect")
        elif v_index == 1:
            setattr (store,"v_review_count_"+who+"_result","cocky")
        else:
            setattr (store,"v_review_count_"+who+"_result","arrogant")
        
        v_count = v_list.count (max(v_list))
        if v_count > 1:
            setattr (store,"v_review_count_"+who+"_result","both")

screen toh_final_review_screen:

    modal True tag menu
    imagebutton idle "bg_characters_mm" action NullAction()
    add "black" alpha 0.7
    hbox:
        xalign 0.4
        spacing 10
        if v_mm_stats_who == "ariel":
            imagebutton:
                idle "heart_panel_ariel_hover"
                if ariel_love_level == 1:
                    foreground Text(_("[ariel_love_level]"),style="stats_button_style_idle",xpos=5)
                else:
                    foreground Text(_("[ariel_love_level]"),style="stats_button_style_idle")
        else:
            imagebutton:
                auto "heart_panel_ariel_%s"
                action SetVariable ("v_mm_stats_who","ariel")
                if ariel_love_level == 1:
                    foreground Text(_("[ariel_love_level]"),style="stats_button_style_idle",xpos=5)
                else:
                    foreground Text(_("[ariel_love_level]"),style="stats_button_style_idle")

        if v_mm_stats_who == "bella":
            imagebutton:
                idle "heart_panel_bella_hover"
                if bella_love_level == 1:
                    foreground Text(_("[bella_love_level]"),style="stats_button_style_idle",xpos=5)
                else:
                    foreground Text(_("[bella_love_level]"),style="stats_button_style_idle")
        else:
            imagebutton:
                auto "heart_panel_bella_%s"
                action SetVariable ("v_mm_stats_who","bella")
                if bella_love_level == 1:
                    foreground Text(_("[bella_love_level]"),style="stats_button_style_idle",xpos=5)
                else:
                    foreground Text(_("[bella_love_level]"),style="stats_button_style_idle")


        if v_mm_stats_who == "vivian":
            imagebutton:
                idle "heart_panel_vivian_hover"
                if vivian_love_level == 1:
                    foreground Text(_("[vivian_love_level]"),style="stats_button_style_idle",xpos=5)
                else:
                    foreground Text(_("[vivian_love_level]"),style="stats_button_style_idle")

        else:
            imagebutton:
                auto "heart_panel_vivian_%s"
                action SetVariable ("v_mm_stats_who","vivian")
                if vivian_love_level == 1:
                    foreground Text(_("[vivian_love_level]"),style="stats_button_style_idle",xpos=5)
                else:
                    foreground Text(_("[vivian_love_level]"),style="stats_button_style_idle")
        if megan_known:

            if v_mm_stats_who == "megan":
                imagebutton:
                    idle "heart_panel_megan_hover"
                    if megan_love_level == 1:
                        foreground Text(_("[megan_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[megan_love_level]"),style="stats_button_style_idle")

            else:
                imagebutton:
                    auto "heart_panel_megan_%s"
                    action SetVariable ("v_mm_stats_who","megan")
                    if megan_love_level == 1:
                        foreground Text(_("[megan_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[megan_love_level]"),style="stats_button_style_idle")



        else:
            imagebutton:
                idle "heart_panel_unknown_idle"

        if juliet_known:

            if v_mm_stats_who == "juliet":
                imagebutton:
                    idle "heart_panel_juliet_hover"
                    if juliet_love_level == 1:
                        foreground Text(_("[juliet_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[juliet_love_level]"),style="stats_button_style_idle")

            else:
                imagebutton:
                    auto "heart_panel_juliet_%s"
                    action SetVariable ("v_mm_stats_who","juliet")
                    if juliet_love_level == 1:
                        foreground Text(_("[juliet_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[juliet_love_level]"),style="stats_button_style_idle")



        else:
            imagebutton:
                idle "heart_panel_unknown_idle"



        if zora_known:

            if v_mm_stats_who == "zora":
                imagebutton:
                    idle "heart_panel_zora_hover"
                    if zora_love_level == 1:
                        foreground Text(_("[zora_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[zora_love_level]"),style="stats_button_style_idle")

            else:
                imagebutton:
                    auto "heart_panel_zora_%s"
                    action SetVariable ("v_mm_stats_who","zora")
                    if zora_love_level == 1:
                        foreground Text(_("[zora_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[zora_love_level]"),style="stats_button_style_idle")



        else:
            imagebutton:
                idle "heart_panel_unknown_idle"


        if justice_known:

            if v_mm_stats_who == "justice":
                imagebutton:
                    idle "heart_panel_justice_hover"
                    if justice_love_level == 1:
                        foreground Text(_("[justice_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[justice_love_level]"),style="stats_button_style_idle")

            else:
                imagebutton:
                    auto "heart_panel_justice_%s"
                    action SetVariable ("v_mm_stats_who","justice")
                    if justice_love_level == 1:
                        foreground Text(_("[justice_love_level]"),style="stats_button_style_idle",xpos=5)
                    else:
                        foreground Text(_("[justice_love_level]"),style="stats_button_style_idle")



        else:
            imagebutton:
                idle "heart_panel_unknown_idle"


        if othergirls_known:

            if v_mm_stats_who == "othergirls":
                imagebutton:
                    idle "heart_panel_othergirls_hover"





            else:
                imagebutton:
                    auto "heart_panel_othergirls_%s"
                    action SetVariable ("v_mm_stats_who","othergirls")





        else:
            imagebutton:
                idle "heart_panel_unknown_idle"



    hbox:
        xalign 0.5
        yalign 0.35
        if v_mm_stats_who == "ariel":
            text "{size=50}[a_name!u]{/size}" style "char_info_description"
        if v_mm_stats_who == "vivian":
            text "{size=50}[v_name!u]{/size}" style "char_info_description"
        if v_mm_stats_who == "bella":
            text "{size=50}[b_name!u]{/size}" style "char_info_description"
        if v_mm_stats_who == "megan":
            text "{size=50}MEGAN{/size}" style "char_info_description"
        if v_mm_stats_who == "juliet":
            text "{size=50}JULIET{/size}" style "char_info_description"
        if v_mm_stats_who == "zora":
            text "{size=50}ZORA{/size}" style "char_info_description"

        if v_mm_stats_who == "justice":
            text "{size=50}OFFICER JUSTICE{/size}" style "char_info_description"

        if v_mm_stats_who == "othergirls":
            text "{size=50}OTHER GIRLS & TASKS{/size}" style "char_info_description"


    vbox:
        xpos 100
        ypos 400
        if v_mm_stats_who == "ariel":
            use scr_review_stats_menu_ariel


        if v_mm_stats_who == "vivian":
            use scr_review_stats_menu_vivian

        if v_mm_stats_who == "bella":
            use scr_review_stats_menu_bella

        if v_mm_stats_who == "megan":
            use scr_review_stats_menu_megan


        if v_mm_stats_who == "juliet":
            use scr_review_stats_menu_juliet

        if v_mm_stats_who == "zora":
            use scr_review_stats_menu_zora

        if v_mm_stats_who == "justice":
            use scr_review_stats_menu_justice

        if v_mm_stats_who == "othergirls":
            use scr_review_stats_menu_othergirls



    if v_review_episode == 1:
        textbutton _("{size=40}CONTINUE TO EPISODE 2{/size}") xpos 1350 ypos 980 text_outlines [ (2, "#000000", 0, 0) ] action [Hide("toh_final_review_screen",dissolve),Jump("lb_ep02_01_01_Team_Meeting_Without_The_MC")] text_style "char_info_button"
    if v_review_episode == 2:
        textbutton _("{size=40}CONTINUE TO EPISODE 3{/size}") xpos 1400 ypos 980 text_outlines [ (2, "#000000", 0, 0) ] action [Hide("toh_final_review_screen",dissolve),Jump("lb_ep03_01_01_Megan_scene_continues")] text_style "char_info_button"
    if v_review_episode == 3:
        textbutton _("{size=50}FINISH EPISODE 3{/size}") xpos 1400 ypos 980 text_outlines [ (2, "#000000", 0, 0) ] action [Hide("toh_final_review_screen",dissolve),Jump("lb_end_of_version")] text_style "char_info_button"



style text_final_review:
    color "#ffffff"

screen scr_review_stats_menu_ariel:
    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("-You visited [a_name] at the Computer Store and also helped her steal special cards from the Security Headquarters.")
                    if v_ep01_ariel_dates_counter > 0:
                        text _("-You went on a Special Date with [a_name] to the Local Cafe.")
                    else:
                        text _("-You missed out on a Special (Date) scene with [a_name].")

                    if v_ep01_ariel_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [a_name].")
                    else:
                        text _("-You did not find the Secret Scene with [a_name].")
                    if v_ep01_ariel_aa_tasks_counter > 1:
                        text _("-You managed to get an A+ rating for both of your set tasks with [a_name].")
                        text _("For this, you gain {color=#d84e96}2 Hearts.{/color}")
                    elif v_ep01_ariel_aa_tasks_counter == 1:
                        text _("-You managed to get an A+ rating for one of your set tasks with [a_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You did not get an A+ rating for any of your set tasks with [a_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""



                if v_review_episode == 2:
                    text _("-[a_name] helped out by supplying you with a replica flash drive to help you steal the original.")
                    text _("-You and [a_name] were able to see what was on the flash drive.")
                    if ariel_heart_ep02_flash_drive_chat:
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    if v_ep02_ariel_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [a_name].")
                    else:
                        text _("-You did not find the Secret Scene with [a_name].")
                    if v_ep02_ariel_dates_counter > 0:
                        if v_ep02_03_11_movie_date_with_ariel_counter >= 4:
                            text _("-Your movie date with [a_name] went very well.")
                            text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                        else:
                            text _("-Your movie date with [a_name] went okay.")
                            text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    else:
                        text _("-When you returned home from the gym, and after you had dinner, you chose to Go to bed rather than Knock on [a_name]'s door.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""


                if v_review_episode == 3:
                    if v_ep03_01_06_ariel_kiss:
                        text _("-You kissed [a_name] before you went to bed on the first night.")
                    text _("-You visited [b_name]’s clothing store with [a_name] and tried on some clothes for when the two of you were to meet the German Artist at the Airport.")
                    if v_ep03_ariel_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [a_name].")
                    else:
                        text _("-You did not find the Secret Scene with [a_name].")

                    if v_ep03_01_05_shopping_with_Ariel >= 5:
                        text _("You had fun with [a_name] at [b_name]'s clothing store while she was changing clothes and you also made out with her.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("You had some fun with [a_name] at [b_name]'s clothing store but there's more you could have done with her.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")



                if v_review_count_ariel_result == "respect":

                    text _("[a_name] appreciates how much you respect her. Be sure not to speak to her in a cocky or arrogant manner, and your relationship with her will continue to strengthen. Treat her with respect and you’ll become even closer to her.")
                elif v_review_count_ariel_result == "cocky":

                    text _("[a_name] doesn’t mind you being cocky when speaking to her, but she prefers you to show her respect more often than not. Do not have an arrogant attitude around her. She doesn’t like that.")
                elif v_review_count_ariel_result == "arrogant":

                    text _("[a_name] does not appreciate your arrogant tone or attitude whenever you are around her or in a public place. She sees this as a huge turn-off. If you want to have any chance of progressing your relationship with her. You better start making better choices in the future. Show her more respect, dude!")
                else:

                    text _("[a_name] appreciates it when you respect her and she doesn’t mind if you are cocky every once in a while. But she does not appreciate your arrogant tone or attitude whenever you are around her or in a public place. Be sure not to speak to her in a cocky or arrogant manner. Treat her respectfully and you’ll become even closer with her.")

            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('ariel',1,6))
                    text _("Secret Scenes: "+str(v_ep01_ariel_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep01_ariel_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep01_ariel_aa_tasks_counter)+"/2")
                    text ""
                    if v_ep01_ariel_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_ariel_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('ariel',7,10))
                    text _("Secret Scenes: "+str(v_ep02_ariel_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep02_ariel_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep02_ariel_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep02_ariel_hearts_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep02_ariel_hearts_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]


                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('ariel',11,15))
                    text _("Secret Scenes: "+str(v_ep03_ariel_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+"0/0")
                    text _("A+ Tasks Completed: "+"0/0")
                    text ""
                    if v_ep03_ariel_hearts_counter > 0:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]






    else:

        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("-You visited [a_name] at the Computer Store and also helped her steal special cards from the Security Headquarters.")
                    if v_ep01_ariel_dates_counter > 0:
                        text _("-You went on a Special Date with [a_name] to the Local Cafe.")
                    else:
                        text _("-You missed out on a Special (Date) scene with [a_name].")

                    if v_ep01_ariel_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [a_name].")
                    else:
                        text _("-You did not find the Secret Scene with [a_name].")
                    if v_ep01_ariel_aa_tasks_counter > 1:
                        text _("-You managed to get an A+ rating for both of your set tasks with [a_name].")
                        text _("For this, you gain {color=#d84e96}2 Hearts.{/color}")
                    elif v_ep01_ariel_aa_tasks_counter == 1:
                        text _("-You managed to get an A+ rating for one of your set tasks with [a_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You did not get an A+ rating for any of your set tasks with [a_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""



                if v_review_episode == 2:
                    text _("-[a_name] helped out by supplying you with a replica flash drive to help you steal the original.")
                    text _("-You and [a_name] were able to see what was on the flash drive.")
                    if ariel_heart_ep02_flash_drive_chat:
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    if v_ep02_ariel_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [a_name].")
                    else:
                        text _("-You did not find the Secret Scene with [a_name].")
                    if v_ep02_ariel_dates_counter > 0:
                        if v_ep02_03_11_movie_date_with_ariel_counter >= 4:
                            text _("-Your movie date with [a_name] went very well.")
                            text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                        else:
                            text _("-Your movie date with [a_name] went okay.")
                            text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    else:
                        text _("-When you returned home from the gym, and after you had dinner, you chose to Go to bed rather than Knock on [a_name]'s door.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""



                if v_review_episode == 3:
                    if v_ep03_01_06_ariel_kiss:
                        text _("-You kissed [a_name] before you went to bed on the first night.")
                    text _("-You visited [b_name]’s clothing store with [a_name] and tried on some clothes for when the two of you were to meet the German Artist at the Airport.")
                    if v_ep03_ariel_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [a_name].")
                    else:
                        text _("-You did not find the Secret Scene with [a_name].")

                    if v_ep03_01_05_shopping_with_Ariel >= 5:
                        text _("You had fun with [a_name] at [b_name]'s clothing store while she was changing clothes and you also made out with her.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("You had some fun with [a_name] at [b_name]'s clothing store but there's more you could have done with her.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")



                if v_review_count_ariel_result == "respect":

                    text _("[a_name] appreciates how much you respect her. Be sure not to speak to her in a cocky or arrogant manner, and your relationship with her will continue to strengthen. Treat her with respect and you’ll become even closer to her.")
                elif v_review_count_ariel_result == "cocky":

                    text _("[a_name] doesn’t mind you being cocky when speaking to her, but she prefers you to show her respect more often than not. Do not have an arrogant attitude around her. She doesn’t like that.")
                elif v_review_count_ariel_result == "arrogant":

                    text _("[a_name] does not appreciate your arrogant tone or attitude whenever you are around her or in a public place. She sees this as a huge turn-off. If you want to have any chance of progressing your relationship with her. You better start making better choices in the future. Show her more respect, dude!")
                else:

                    text _("[a_name] appreciates it when you respect her and she doesn’t mind if you are cocky every once in a while. But she does not appreciate your arrogant tone or attitude whenever you are around her or in a public place. Be sure not to speak to her in a cocky or arrogant manner. Treat her respectfully and you’ll become even closer with her.")

            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('ariel',1,6))
                    text _("Secret Scenes: "+str(v_ep01_ariel_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep01_ariel_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep01_ariel_aa_tasks_counter)+"/2")
                    text ""
                    if v_ep01_ariel_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_ariel_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('ariel',7,10))
                    text _("Secret Scenes: "+str(v_ep02_ariel_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep02_ariel_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep02_ariel_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep02_ariel_hearts_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep02_ariel_hearts_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('ariel',11,15))
                    text _("Secret Scenes: "+str(v_ep03_ariel_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+"0/0")
                    text _("A+ Tasks Completed: "+"0/0")
                    text ""
                    if v_ep03_ariel_hearts_counter > 0:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]



screen scr_review_stats_menu_vivian:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("-You helped [v_name] steal items from the local Acting Theatre and also helped her to investigate the Art Gallery.")
                    if v_ep01_vivian_dates_counter > 0:
                        text _("-You had a Special Date with [v_name] at home in the Living Room.")
                    else:
                        text _("-You missed out on a Special (Date) scene with [v_name].")

                    if v_ep01_vivian_fantasy_counter > 1:
                        text _("-You found the Secret Scenes with [v_name].")
                    elif v_ep01_vivian_fantasy_counter == 1:
                        text _("-You found one of the two Secret Scenes with [v_name].")
                    else:
                        text _("-You did not find the Secret Scene with [v_name].")
                    if v_ep01_vivian_aa_tasks_counter > 1:
                        text _("-You managed to get an A+ rating for both of your set tasks with [v_name].")
                        text _("For this, you gain {color=#d84e96}2 Hearts.{/color}")
                    elif v_ep01_vivian_aa_tasks_counter == 1:
                        text _("-You managed to get an A+ rating for one of your set tasks with [v_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You did not get an A+ rating for any of your set tasks with [v_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""


                if v_review_episode == 2:
                    text _("-[v_name] helped to buy you some more time to get the flash drive back to [vic_name].")
                    text _("-[v_name] greeted you when you returned home later that night.")
                    text _("-You were able to kiss [v_name] during this scene.")
                    text ""


                if v_review_episode == 3:
                    if v_ep03_01_06_vivian_knock_door:
                        text _("-You chose to check on [v_name] before you went to bed.")
                        if v_ep03_01_06_continue_talking_with_Vivian:
                            if v_ep03_01_05_checking_on_Vivian_counter >= 4:
                                text _("-You comforted [v_name] by going to her room after dinner. You also made out with her while she was in her underwear.")
                                text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                            else:
                                text _("-You comforted [v_name] by going to her room after dinner, but there was more than you could have done with her that you missed.")
                                text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                        else:
                            text _("-You didn't stay long enough to comfort [v_name]")
                            text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                    else:
                        text _("-You went to bed without checking on [v_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")




                if v_review_count_vivian_result == "respect":

                    text _("[v_name] loves that you respect her and are willing to put her first. She also loves that cocky side of you, but also worries that it could one day get you into big trouble. You need to know when to show her respect, and also be a risk-taker, which is a classic trait for someone who is cocky like you are. After being with [vic_name] for so long, she’s sick and tired of being with an arrogant man. So don’t be that guy!")
                elif v_review_count_vivian_result == "cocky":

                    text _("[v_name] finds it amusing that you are cocky every so often. But she also worries that it could one day get you into big trouble. A fine balance between being cocky and respectful is the best way to make her happy, and you may soon reap the rewards by doing this. After being with [vic_name] for so long, she’s sick and tired of being with an arrogant man. So don’t be that guy!")
                elif v_review_count_vivian_result == "arrogant":

                    text _("After being with [vic_name] for so long, she’s sick and tired of being with an arrogant man. Are you really trying to follow in his footsteps? Come on, don’t be that guy! A fine balance between being cocky and respectful is the best way to make [v_name] happy, and you may soon reap the rewards by doing this.")
                else:

                    text _("A fine balance between being cocky and respectful is the best way to make her happy, and you may soon reap the rewards by doing this. She’s sick and tired of being with an arrogant man, especially after being with [vic_name] for so long. So don’t be that guy!")

            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""

                if v_review_episode == 1:
                    text _("Secret Images: "+count_unlocked_rewards('vivian'))
                    text _("Secret Scenes: "+str(v_ep01_vivian_fantasy_counter)+"/2")
                    text _("Special Date Scenes: "+str(v_ep01_vivian_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep01_vivian_aa_tasks_counter)+"/2")
                    text ""
                    if v_ep01_vivian_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_vivian_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('vivian',11,14))
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('vivian',15,20))
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep03_vivian_hearts_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]


    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("-You helped [v_name] steal items from the local Acting Theatre and also helped her to investigate the Art Gallery.")
                    if v_ep01_vivian_dates_counter > 0:
                        text _("-You had a Special Date with [v_name] at home in the Living Room.")
                    else:
                        text _("-You missed out on a Special (Date) scene with [v_name].")

                    if v_ep01_vivian_fantasy_counter > 1:
                        text _("-You found the Secret Scenes with [v_name].")
                    elif v_ep01_vivian_fantasy_counter == 1:
                        text _("-You found one of the two Secret Scenes with [v_name].")
                    else:
                        text _("-You did not find the Secret Scene with [v_name].")
                    if v_ep01_vivian_aa_tasks_counter > 1:
                        text _("-You managed to get an A+ rating for both of your set tasks with [v_name].")
                        text _("For this, you gain {color=#d84e96}2 Hearts.{/color}")
                    elif v_ep01_vivian_aa_tasks_counter == 1:
                        text _("-You managed to get an A+ rating for one of your set tasks with [v_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You did not get an A+ rating for any of your set tasks with [v_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""

                if v_review_episode == 2:
                    text _("-[v_name] helped to buy you some more time to get the flash drive back to [vic_name].")
                    text _("-[v_name] greeted you when you returned home later that night.")
                    text _("-You were able to kiss [v_name] during this scene.")
                    text ""

                if v_review_episode == 3:
                    if v_ep03_01_06_vivian_knock_door:
                        text _("-You chose to check on [v_name] before you went to bed.")
                        if v_ep03_01_06_continue_talking_with_Vivian:
                            if v_ep03_01_05_checking_on_Vivian_counter >= 4:
                                text _("-You comforted [v_name] by going to her room after dinner. You also made out with her while she was in her underwear.")
                                text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                            else:
                                text _("-You comforted [v_name] by going to her room after dinner, but there was more than you could have done with her that you missed.")
                                text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                        else:
                            text _("-You didn't stay long enough to comfort [v_name]")
                            text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                    else:
                        text _("-You went to bed without checking on [v_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")



                if v_review_count_vivian_result == "respect":

                    text _("[v_name] loves that you respect her and are willing to put her first. She also loves that cocky side of you, but also worries that it could one day get you into big trouble. You need to know when to show her respect, and also be a risk-taker, which is a classic trait for someone who is cocky like you are. After being with [vic_name] for so long, she’s sick and tired of being with an arrogant man. So don’t be that guy!")
                elif v_review_count_vivian_result == "cocky":

                    text _("[v_name] finds it amusing that you are cocky every so often. But she also worries that it could one day get you into big trouble. A fine balance between being cocky and respectful is the best way to make her happy, and you may soon reap the rewards by doing this. After being with [vic_name] for so long, she’s sick and tired of being with an arrogant man. So don’t be that guy!")
                elif v_review_count_vivian_result == "arrogant":

                    text _("After being with [vic_name] for so long, she’s sick and tired of being with an arrogant man. Are you really trying to follow in his footsteps? Come on, don’t be that guy! A fine balance between being cocky and respectful is the best way to make [v_name] happy, and you may soon reap the rewards by doing this.")
                else:

                    text _("A fine balance between being cocky and respectful is the best way to make her happy, and you may soon reap the rewards by doing this. She’s sick and tired of being with an arrogant man, especially after being with [vic_name] for so long. So don’t be that guy!")

            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('vivian',1,10))
                    text _("Secret Scenes: "+str(v_ep01_vivian_fantasy_counter)+"/2")
                    text _("Special Date Scenes: "+str(v_ep01_vivian_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep01_vivian_aa_tasks_counter)+"/2")
                    text ""
                    if v_ep01_vivian_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_vivian_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('vivian',11,14))
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('vivian',15,20))
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep03_vivian_hearts_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]


screen scr_review_stats_menu_bella:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("- [b_name] helped by attending to the slight bruise on your face.")
                    if v_ep02_02_03_chat_with_bella_counter > 0:
                        text _("-You were able to smooth things over with [b_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You were able to kiss [b_name] when she was in your room. ")

                    if v_ep01_bella_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [b_name].")
                    else:
                        text _("-You did not find the Secret Scene with [b_name].")
                    text ""

                if v_review_episode == 1:
                    text _("-You went with [b_name] to the local Tattoo Parlour and also helped her steal supplies from the Art School.")
                    if v_ep01_bella_dates_counter > 0:
                        text _("-You went on a Special Date with [b_name] to the Local Park.")
                    else:
                        text _("-You missed out on a Special (Date) scene with [b_name].")

                    if v_ep01_bella_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [b_name].")
                    else:
                        text _("-You did not find the Secret Scene with [b_name].")
                    if v_ep01_bella_aa_tasks_counter > 1:
                        text _("-You managed to get an A+ rating for both of your set tasks with [b_name].")
                        text _("For this, you gain {color=#d84e96}2 Hearts.{/color}")
                    elif v_ep01_bella_aa_tasks_counter == 1:
                        text _("-You managed to get an A+ rating for one of your set tasks with [b_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You did not get an A+ rating for any of your set tasks with [b_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""


                if v_review_episode == 3:
                    text _("-You tried on some clothes at [b_name]’s store for the Art Gallery function.")

                    if v_ep03_02_03_trying_on_clothes_with_Bella >= 4:
                        text _("-You decided to watch [b_name] while she was changing and saw her topless.")
                        text _("-You told [b_name] she looked incredible in her black gown.")
                        text _("-You put your arm around [b_name] while posing for a photo with her.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:

                        text _("-Even though you spent time with [b_name], you missed out on some extra content with her during this scene.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")


                    if bella_love_level >= 2:
                        text _("-You kissed [b_name] while you were at her clothing store.")

                    if v_ep03_bella_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [b_name].")
                    else:
                        text _("-You did not find the Secret Scene with [b_name].")



                if v_review_count_bella_result == "respect":

                    text _("[b_name] doesn’t always care if you show her respect, but it certainly helps to keep the peace between you too. Showing her too much respect will further drive a wedge in your already tetchy relationship. Don’t be afraid to be a bit cocky sometimes, but definitely don’t be too arrogant.")
                elif v_review_count_bella_result == "cocky":

                    text _("[b_name] doesn’t mind you being cocky every so often. She might even find it somewhat charming. Just don’t overdo it. A cross between being cocky and respectful is the best way to simmer things down between the two of you.")
                elif v_review_count_bella_result == "arrogant":

                    text _("If it’s one thing [b_name] detests in a guy, it’s one who is incredibly arrogant. Given your already tetchy relationship, you really don’t want to push her buttons too much, especially if you want to get something more out of your relationship with her. A cross between being cocky and respectful is the best way to simmer things down between the two of you.")
                else:

                    text _("[b_name] doesn’t mind if you’re a little cocky, she’s grown to expect that from you. But she also wants to be respected for what she does and who she is. Continued playful banter between the two of you is what could bring you closer to her. A cross between being cocky and respectful is the best way to simmer things down between the two of you. Just don’t piss her off by being ignorant and a complete asshole to her.")

            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('bella',1,11))
                    text _("Secret Scenes: "+str(v_ep01_bella_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep01_bella_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep01_bella_aa_tasks_counter)+"/2")
                    text ""
                    if v_ep01_bella_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_bella_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('bella',12,15))
                    text _("Secret Scenes: "+str(v_ep02_bella_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep02_02_03_chat_with_bella_counter > 0:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('bella',16,20))
                    text _("Secret Scenes: "+str(v_ep03_bella_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep03_02_03_trying_on_clothes_with_Bella >= 4:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]


    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("- [b_name] helped by attending to the slight bruise on your face.")
                    if v_ep02_02_03_chat_with_bella_counter > 0:
                        text _("-You were able to smooth things over with [b_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You were able to kiss [b_name] when she was in your room.")

                    if v_ep02_bella_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [b_name].")
                    else:
                        text _("-You did not find the Secret Scene with [b_name].")
                    text ""

                if v_review_episode == 1:
                    text _("-You went with [b_name] to the local Tattoo Parlour and also helped her steal supplies from the Art School.")
                    if v_ep01_bella_dates_counter > 0:
                        text _("-You went on a Special Date with [b_name] to the Local Park.")
                    else:
                        text _("-You missed out on a Special (Date) scene with [b_name].")

                    if v_ep01_bella_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [b_name].")
                    else:
                        text _("-You did not find the Secret Scene with [b_name].")
                    if v_ep01_bella_aa_tasks_counter > 1:
                        text _("-You managed to get an A+ rating for both of your set tasks with [b_name].")
                        text _("For this, you gain {color=#d84e96}2 Hearts.{/color}")
                    elif v_ep01_bella_aa_tasks_counter == 1:
                        text _("-You managed to get an A+ rating for one of your set tasks with [b_name].")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You did not get an A+ rating for any of your set tasks with [b_name].")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")
                    text ""




                if v_review_episode == 3:
                    text _("-You tried on some clothes at [b_name]’s store for the Art Gallery function.")

                    if v_ep03_02_03_trying_on_clothes_with_Bella >= 4:
                        text _("-You decided to watch [b_name] while she was changing and saw her topless.")
                        text _("-You told [b_name] she looked incredible in her black gown.")
                        text _("-You put your arm around [b_name] while posing for a photo with her.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:

                        text _("-Even though you spent time with [b_name], you missed out on some extra content with her during this scene.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")


                    if bella_love_level >= 2:
                        text _("-You kissed [b_name] while you were at her clothing store.")

                    if v_ep03_bella_fantasy_counter > 0:
                        text _("-You found the Secret Scene with [b_name].")
                    else:
                        text _("-You did not find the Secret Scene with [b_name].")




                if v_review_count_bella_result == "respect":

                    text _("[b_name] doesn’t always care if you show her respect, but it certainly helps to keep the peace between you too. Showing her too much respect will further drive a wedge in your already tetchy relationship. Don’t be afraid to be a bit cocky sometimes, but definitely don’t be too arrogant.")
                elif v_review_count_bella_result == "cocky":

                    text _("[b_name] doesn’t mind you being cocky every so often. She might even find it somewhat charming. Just don’t overdo it. A cross between being cocky and respectful is the best way to simmer things down between the two of you.")
                elif v_review_count_bella_result == "arrogant":

                    text _("If it’s one thing [b_name] detests in a guy, it’s one who is incredibly arrogant. Given your already tetchy relationship, you really don’t want to push her buttons too much, especially if you want to get something more out of your relationship with her. A cross between being cocky and respectful is the best way to simmer things down between the two of you.")
                else:

                    text _("[b_name] doesn’t mind if you’re a little cocky, she’s grown to expect that from you. But she also wants to be respected for what she does and who she is. Continued playful banter between the two of you is what could bring you closer to her. A cross between being cocky and respectful is the best way to simmer things down between the two of you. Just don’t piss her off by being ignorant and a complete asshole to her.")

            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('bella',1,11))
                    text _("Secret Scenes: "+str(v_ep01_bella_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep01_bella_dates_counter)+"/1")
                    text _("A+ Tasks Completed: "+str(v_ep01_bella_aa_tasks_counter)+"/2")
                    text ""
                    if v_ep01_bella_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_bella_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('bella',12,15))
                    text _("Secret Scenes: "+str(v_ep02_bella_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep02_02_03_chat_with_bella_counter > 0:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('bella',16,20))
                    text _("Secret Scenes: "+str(v_ep03_bella_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep03_02_03_trying_on_clothes_with_Bella >= 4:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]



screen scr_review_stats_menu_megan:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""



                if v_review_episode == 2:
                    text _("-Megan apologises for what happened.")
                    text _("-Megan asks for you to work with her.")

                    text _("-There were no Special Dates with Megan in this Episode.")

                    if v_ep02_04_01_megan_work_with_her:
                        text _("-You decided to 'Agree' to work with her.")
                    else:
                        text _("-You decided to 'Refuse' to work with her.")

                    text _("There are no Hearts available for Megan in this Episode.")
                    text ""

                if v_review_episode == 1:
                    text _("-You met Megan at a local clothing store in town, she helped you retrieve your stolen bike and also invited you to her house, which you have visited.")
                    text _("-She also asked you to check out a location in town that could lead to the mysterious cat tattoo girl.")
                    text _("-There were no Special Dates with Megan in this Episode.")

                    if v_ep01_megan_fantasy_counter > 0:
                        text _("-You found the Secret Scene with Megan.")
                    else:
                        text _("-You did not find the Secret Scene with Megan.")

                    text _("There are no Hearts available for Megan in this Episode.")
                    text ""


                if v_review_episode == 3:
                    text _("-You met with Megan at her house.")

                    if v_ep02_04_01_megan_work_with_her:
                        text _("-You chose to work with Megan and be her ally.")

                    else:
                        text _("-You chose not to work with Megan or be her ally.")

                    if v_ep03_megan_oral_sex:
                        text _("-You received oral pleasures from Megan.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You didn't gain any hearts from Megan.")

                    text ""




                if v_review_count_megan_result == "respect":

                    text _("Megan likes a man who respects her. But don’t overdo it, she doesn’t like an ass-kisser either. She’s known to like men who are cocky, and sometimes even a little arrogant. An even balance between these three characteristics is your best bet.")
                elif v_review_count_megan_result == "cocky":

                    text _("Megan likes a man who is a little cocky and sure of himself. Maybe even a little arrogant. However, she has no time for those who act like complete narcissists. Deep down she demands respect. An even balance between these three characteristics is your best bet.")
                elif v_review_count_megan_result == "arrogant":

                    text _("Megan became successful by being a little arrogant, every so often. So you won’t completely rub her the wrong way by acting similarly. Just don't overdo it. She’s known to also like men who are cocky, but deep down she demands respect. An even balance between these three characteristics is your best bet.")
                else:

                    text _("You’re on the right track! Megan likes a man who respects her. But don’t overdo it, she doesn’t like an ass-kisser either. She’s also known to like men who are cocky, and sometimes even a little arrogant. Continue to have an even balance of these three characteristics and Megan will greatly reward you.")

            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('megan',1,6))
                    text _("Secret Scenes: "+str(v_ep01_megan_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep01_megan_dates_counter)+"/0")
                    text _("A+ Tasks Completed: "+str(v_ep01_megan_aa_tasks_counter)+"/0")
                    text ""
                    if v_ep01_megan_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_megan_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('megan',7,10))
                    text _("Secret Scenes: "+str(v_ep03_megan_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep03_megan_oral_sex:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]



    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("-Megan apologises for what happened.")
                    text _("-Megan asks for you to work with her.")

                    text _("-There were no Special Dates with Megan in this Episode.")

                    if v_ep02_04_01_megan_work_with_her:
                        text _("-You decided to 'Agree' to work with her.")
                    else:
                        text _("-You decided to 'Refuse' to work with her.")

                    text _("There are no Hearts available for Megan in this Episode.")
                    text ""

                if v_review_episode == 1:
                    text _("-You met Megan at a local clothing store in town, she helped you retrieve your stolen bike and also invited you to her house, which you have visited.")
                    text _("-She also asked you to check out a location in town that could lead to the mysterious cat tattoo girl.")
                    text _("-There were no Special Dates with Megan in this Episode.")

                    if v_ep01_megan_fantasy_counter > 0:
                        text _("-You found the Secret Scene with Megan.")
                    else:
                        text _("-You did not find the Secret Scene with Megan.")

                    text _("There are no Hearts available for Megan in this Episode.")
                    text ""

                if v_review_episode == 3:
                    text _("-You met with Megan at her house.")

                    if v_ep02_04_01_megan_work_with_her:
                        text _("-You chose to work with Megan and be her ally.")

                    else:
                        text _("-You chose not to work with Megan or be her ally.")

                    if v_ep03_megan_oral_sex:
                        text _("-You received oral pleasures from Megan.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You didn't gain any hearts from Megan.")

                    text ""

                if v_review_count_megan_result == "respect":

                    text _("Megan likes a man who respects her. But don’t overdo it, she doesn’t like an ass-kisser either. She’s known to like men who are cocky, and sometimes even a little arrogant. An even balance between these three characteristics is your best bet.")
                elif v_review_count_megan_result == "cocky":

                    text _("Megan likes a man who is a little cocky and sure of himself. Maybe even a little arrogant. However, she has no time for those who act like complete narcissists. Deep down she demands respect. An even balance between these three characteristics is your best bet.")
                elif v_review_count_megan_result == "arrogant":

                    text _("Megan became successful by being a little arrogant, every so often. So you won’t completely rub her the wrong way by acting similarly. Just don't overdo it. She’s known to also like men who are cocky, but deep down she demands respect. An even balance between these three characteristics is your best bet.")
                else:

                    text _("You’re on the right track! Megan likes a man who respects her. But don’t overdo it, she doesn’t like an ass-kisser either. She’s also known to like men who are cocky, and sometimes even a little arrogant. Continue to have an even balance of these three characteristics and Megan will greatly reward you.")

            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 1:
                    text _("Secret Images: "+rewards_count_range('megan',1,6))
                    text _("Secret Scenes: "+str(v_ep01_megan_fantasy_counter)+"/1")
                    text _("Special Date Scenes: "+str(v_ep01_megan_dates_counter)+"/0")
                    text _("A+ Tasks Completed: "+str(v_ep01_megan_aa_tasks_counter)+"/0")
                    text ""
                    if v_ep01_megan_aa_tasks_counter > 1:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep01_megan_aa_tasks_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 2:
                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('megan',7,10))
                    text _("Secret Scenes: "+str(v_ep03_megan_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
                    if v_ep03_megan_oral_sex:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]





screen scr_review_stats_menu_juliet:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""



                if v_review_episode == 2:
                    if v_ep02_03_08_fitness_session_with_juliet_fight:
                        text _("-You had a personal fitness session with Juliet at the gym.")
                        if v_ep02_03_08_fitness_session_with_juliet_fight_win:
                            text _("-You won the fight with Juliet.")
                        else:
                            text _("-You lost the fight with Juliet.")
                    else:
                        text _("-You refused to challenge her to a fight.")

                    if v_ep02_03_08_fitness_session_with_juliet_counter >= 4:
                        text _("-Juliet was pretty impressed after her session with you.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-Juliet was somewhat happy after her session with you.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")


                    if v_ep02_juliet_fantasy_counter > 0:
                        text _("-You found the Secret Scene with Juliet.")
                    else:
                        text _("-You did not find the Secret Scene with Juliet.")

                    text ""


                if v_review_episode == 3:
                    text _("-Juliet did not feature in this episode.")




                if v_review_count_juliet_result == "respect":

                    text _("Juliet wants respect, but not as often as you think. If you try and suck up to her, she’s going to know. She much prefers a guy who is cock-sure of himself, and sometimes a little arrogant. An even balance between these two traits will get you somewhere with her.")
                elif v_review_count_juliet_result == "cocky":

                    text _("Juliet prefers a guy who is cock-sure of himself. And sometimes even a little arrogant. An even balance between these two traits will get you somewhere with her.")
                elif v_review_count_juliet_result == "arrogant":

                    text _("Juliet doesn’t mind a guy who’s a little arrogant. But she sometimes prefers a guy who is cock-sure of himself. An even balance between these two traits will get you somewhere with her.")
                else:

                    text _("Believe it or not, you’re the kind of guy Juliet is interested in, even if she’s not showing it yet. Juliet prefers a guy who is cock-sure of himself. And sometimes even a little arrogant. Continue to keep and even balance between these two traits and it will start to get you somewhere with her.")

            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('juliet',1,4))
                    text _("Secret Scenes: "+str(v_ep02_juliet_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: "+str(v_ep02_juliet_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep02_03_08_fitness_session_with_juliet_counter >= 4:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:

                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""


    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    if v_ep02_03_08_fitness_session_with_juliet_fight:
                        text _("-You had a personal fitness session with Juliet at the gym.")
                        if v_ep02_03_08_fitness_session_with_juliet_fight_win:
                            text _("-You won the fight with Juliet.")
                        else:
                            text _("-You lost the fight with Juliet.")
                    else:
                        text _("-You refused to challenge her to a fight.")

                    if v_ep02_03_08_fitness_session_with_juliet_counter >= 4:
                        text _("-Juliet was pretty impressed after her session with you.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")

                    else:
                        text _("-Juliet was somewhat happy after her session with you.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")


                    if v_ep02_juliet_fantasy_counter > 0:
                        text _("-You found the Secret Scene with Juliet.")
                    else:
                        text _("-You did not find the Secret Scene with Juliet.")

                    text ""



                if v_review_episode == 3:
                    text _("-Juliet did not feature in this episode.")




                if v_review_count_juliet_result == "respect":

                    text _("Juliet wants respect, but not as often as you think. If you try and suck up to her, she’s going to know. She much prefers a guy who is cock-sure of himself, and sometimes a little arrogant. An even balance between these two traits will get you somewhere with her.")
                elif v_review_count_juliet_result == "cocky":

                    text _("Juliet prefers a guy who is cock-sure of himself. And sometimes even a little arrogant. An even balance between these two traits will get you somewhere with her.")
                elif v_review_count_juliet_result == "arrogant":

                    text _("Juliet doesn’t mind a guy who’s a little arrogant. But she sometimes prefers a guy who is cock-sure of himself. An even balance between these two traits will get you somewhere with her.")
                else:

                    text _("Believe it or not, you’re the kind of guy Juliet is interested in, even if she’s not showing it yet. Juliet prefers a guy who is cock-sure of himself. And sometimes even a little arrogant. Continue to keep and even balance between these two traits and it will start to get you somewhere with her.")

            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('juliet',1,4))
                    text _("Secret Scenes: "+str(v_ep02_juliet_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: "+str(v_ep02_juliet_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep02_03_08_fitness_session_with_juliet_counter >= 4:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:

                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: 0/0")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""


screen scr_review_stats_menu_zora:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""



                if v_review_episode == 2:
                    text _("-You had a beginners fitness session with Zora at the gym.")

                    if v_ep02_03_07_fitness_session_with_zora_counter >= 5:
                        text _("-Zora was pretty impressed after her session with you.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-Zora was somewhat happy after her session with you.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                    if v_ep02_zora_fantasy_counter > 0:
                        text _("-You found the Secret Scene with Zora.")
                    else:
                        text _("-You did not find the Secret Scene with Zora.")

                    text ""



                if v_review_episode == 3:
                    text _("-You called Zora to see if she would join you for a morning fitness session at the local park. She agreed to meet with you.")

                    if v_ep03_02_01_standing_up_for_Zora >= 4:
                        text _("-When Zora felt some pain in her back, you offered to check it for her.")
                        text _("-You stood up for Zora when you ran into “Guy” at the park and was able to get rid of him.")
                        text _("-Once he was gone, you made sure Zora was okay and then you kissed her.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-You encountered “Guy” at the park.")
                        text _("-Even though you managed to get rid of him, there are some better decisions that you could have made to make Zora feel less concerned about him.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                    if v_ep03_02_01_standing_up_for_Zora >= 4:
                        text _("-Zora invited you over to her place and showed you around her home.")
                        text _("-You found out some important details for Victor while you were at Zora’s place.")
                        text _("-After kissing Zora, she invited you into her bedroom and you had sex with her.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-Zora invited you over to her place and showed you around her home.")
                        text _("-You found out some important details for Victor while you were at Zora’s place.")
                        text _("-You ended up leaving Zora’s place earlier than she expected.")
                        text _("-There was more content with Zora that you did not find.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                    text ""

                if v_review_count_zora_result == "respect":

                    text _("Zora believes that if you treat her with respect, then she will give it back in return. She really doesn’t like it when a guy acts cocky or arrogant with her. Zora sees it as a huge turn-off. Keep showing her respect and she may respond to you in 'other' ways.")
                elif v_review_count_zora_result == "cocky":

                    text _("Zora really doesn’t like it when a guy acts cocky with her. She sees it as a huge turn-off. Zora doesn’t like arrogant guys either. Zora believes that if you treat her with respect, then she will give it back in return. Try and get your Respect points up! Show her more respect and she may respond to you in 'other' ways.")
                elif v_review_count_zora_result == "arrogant":

                    text _("Zora really doesn’t like it when a guy acts arrogantly around her. She sees it as a huge turn-off. Zora doesn’t like cocky guys either. Zora believes that if you treat her with respect, then she will give it back in return. Try and get your Respect points up!")
                else:

                    text _("Zora really doesn’t like it when a guy acts or arrogant with her. She sees it as a huge turn-off. Zora believes that if you treat her with respect, then she will give it back in return. Show her more respect and she may respond to you in 'other' ways.")

            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('zora',1,4))
                    text _("Secret Scenes: "+str(v_ep02_zora_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: "+str(v_ep02_zora_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep02_03_07_fitness_session_with_zora_counter >= 5:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]

                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('zora',5,10))
                    text _("Secret Scenes: "+str(v_ep03_zora_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: "+str(v_ep03_zora_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep03_zora_fantasy_counter >= 2:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep03_zora_fantasy_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]









    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("-You had a beginners fitness session with Zora at the gym.")

                    if v_ep02_03_07_fitness_session_with_zora_counter >= 5:
                        text _("-Zora was pretty impressed after her session with you.")
                        text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                    else:
                        text _("-Zora was somewhat happy after her session with you.")
                        text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                    if v_ep02_zora_fantasy_counter > 0:
                        text _("-You found the Secret Scene with Zora.")
                    else:
                        text _("-You did not find the Secret Scene with Zora.")

                    text ""

                    if v_review_episode == 3:
                        text _("-You called Zora to see if she would join you for a morning fitness session at the local park. She agreed to meet with you.")

                        if v_ep03_02_01_standing_up_for_Zora >= 4:
                            text _("-When Zora felt some pain in her back, you offered to check it for her.")
                            text _("-You stood up for Zora when you ran into “Guy” at the park and was able to get rid of him.")
                            text _("-Once he was gone, you made sure Zora was okay and then you kissed her.")
                            text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                        else:
                            text _("-You encountered “Guy” at the park.")
                            text _("-Even though you managed to get rid of him, there are some better decisions that you could have made to make Zora feel less concerned about him.")
                            text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                        if v_ep03_02_01_standing_up_for_Zora >= 4:
                            text _("-Zora invited you over to her place and showed you around her home.")
                            text _("-You found out some important details for Victor while you were at Zora’s place.")
                            text _("-After kissing Zora, she invited you into her bedroom and you had sex with her.")
                            text _("For this, you gain {color=#d84e96}1 Heart.{/color}")
                        else:
                            text _("-Zora invited you over to her place and showed you around her home.")
                            text _("-You found out some important details for Victor while you were at Zora’s place.")
                            text _("-You ended up leaving Zora’s place earlier than she expected.")
                            text _("-There was more content with Zora that you did not find.")
                            text _("For this, you gain {color=#d84e96}0 Heart.{/color}")

                        text ""

                if v_review_count_zora_result == "respect":

                    text _("Zora believes that if you treat her with respect, then she will give it back in return. She really doesn’t like it when a guy acts cocky or arrogant with her. Zora sees it as a huge turn-off. Keep showing her respect and she may respond to you in 'other' ways.")
                elif v_review_count_zora_result == "cocky":

                    text _("Zora really doesn’t like it when a guy acts cocky with her. She sees it as a huge turn-off. Zora doesn’t like arrogant guys either. Zora believes that if you treat her with respect, then she will give it back in return. Try and get your Respect points up! Show her more respect and she may respond to you in 'other' ways.")
                elif v_review_count_zora_result == "arrogant":

                    text _("Zora really doesn’t like it when a guy acts arrogantly around her. She sees it as a huge turn-off. Zora doesn’t like cocky guys either. Zora believes that if you treat her with respect, then she will give it back in return. Try and get your Respect points up!")
                else:

                    text _("Zora really doesn’t like it when a guy acts or arrogant with her. She sees it as a huge turn-off. Zora believes that if you treat her with respect, then she will give it back in return. Show her more respect and she may respond to you in 'other' ways.")

            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 2:
                    text _("Secret Images: "+rewards_count_range('zora',1,4))
                    text _("Secret Scenes: "+str(v_ep02_zora_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: "+str(v_ep02_zora_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep02_03_07_fitness_session_with_zora_counter >= 5:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]


                if v_review_episode == 3:
                    text _("Secret Images: "+rewards_count_range('zora',5,10))
                    text _("Secret Scenes: "+str(v_ep03_zora_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: "+str(v_ep03_zora_aa_tasks_counter)+"/1")
                    text ""
                    if v_ep03_zora_fantasy_counter >= 2:
                        text _("{color=#d84e96}Hearts Gained: 2{/color}") outlines [ (2, "#000000", 0, 0) ]
                    elif v_ep03_zora_fantasy_counter == 1:
                        text _("{color=#d84e96}Hearts Gained: 1{/color}") outlines [ (2, "#000000", 0, 0) ]
                    else:
                        text _("{color=#d84e96}Hearts Gained: 0{/color}") outlines [ (2, "#000000", 0, 0) ]





screen scr_review_stats_menu_justice:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""



                if v_review_episode == 3:
                    if v_ep01_04_01_Bella_Stay_Or_Leave == "Leave":
                        text _("-You spoke with Officer Justice at the gym that you work at.")
                    else:
                        text _("-You did not speak with Officer Justice at the gym that you work at.")


                    text _("-You followed Officer Justice out of the gym and filmed her destroying evidence.")

                    if v_ep03_justice_fantasy_counter == 1:
                        text _("-You found the Secret Scene with Officer Justice.")
                    else:
                        text _("-You did not find the Secret Scene with Officer Justice.")


                    text _("-No hearts were given for Officer Justice in this episode.")


                if v_review_count_justice_result == "respect":

                    text _("No more info available as yet.")
                elif v_review_count_justice_result == "cocky":

                    text _("No more info available as yet.")
                elif v_review_count_justice_result == "arrogant":

                    text _("No more info available as yet.")
                else:

                    text _("No more info available as yet.")
            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""

                if v_review_episode == 3:

                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: "+str(v_ep03_justice_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""


    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""


                if v_review_episode == 3:
                    if v_ep01_04_01_Bella_Stay_Or_Leave == "Leave":
                        text _("-You spoke with Officer Justice at the gym that you work at.")
                    else:
                        text _("-You did not speak with Officer Justice at the gym that you work at.")


                    text _("-You followed Officer Justice out of the gym and filmed her destroying evidence.")

                    if v_ep03_justice_fantasy_counter == 1:
                        text _("-You found the Secret Scene with Officer Justice.")
                    else:
                        text _("-You did not find the Secret Scene with Officer Justice.")


                    text _("-No hearts were given for Officer Justice in this episode.")


                if v_review_count_justice_result == "respect":

                    text _("No more info available as yet.")
                elif v_review_count_justice_result == "cocky":

                    text _("No more info available as yet.")
                elif v_review_count_justice_result == "arrogant":

                    text _("No more info available as yet.")
                else:

                    text _("No more info available as yet.")
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 3:

                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: "+str(v_ep03_justice_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""



screen scr_review_stats_menu_othergirls:

    if renpy.variant("small"):
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            has hbox:
                spacing 150
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                ymaximum 1500
                has vbox
                text _("{size=50}Final Review{/size}") style "char_info_description"
                text ""



                if v_review_episode == 3:
                    if v_ep01_04_01_Bella_Stay_Or_Leave == "Leave":
                        text _("-You spoke with Officer Justice at the gym that you work at.")
                    else:
                        text _("-You did not speak with Officer Justice at the gym that you work at.")


                    text _("-You followed Officer Justice out of the gym and filmed her destroying evidence.")

                    if v_ep03_justice_fantasy_counter == 1:
                        text _("-You found the Secret Scene with Officer Justice.")
                    else:
                        text _("-You did not find the Secret Scene with Officer Justice.")


                    text _("-No hearts were given for Officer Justice in this episode.")


                if v_review_count_justice_result == "respect":

                    text _("No more info available as yet.")
                elif v_review_count_justice_result == "cocky":

                    text _("No more info available as yet.")
                elif v_review_count_justice_result == "arrogant":

                    text _("No more info available as yet.")
                else:

                    text _("No more info available as yet.")
            vbox:
                xpos -80
                xmaximum 1500
                text _("{size=50}Stats{/size}") style "char_info_description"
                text ""

                if v_review_episode == 3:

                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: "+str(v_ep03_othergirls_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""


    else:
        hbox:
            spacing 150
            vbox:
                spacing 5
                xalign 0.4
                yalign 0.6
                xmaximum 1200
                text _("{size=40}Final Review{/size}") style "char_info_description"
                text ""


                if v_review_episode == 3:
                    if v_ep03_task_13_german_woman_counter == 5:
                        text _("-You helped the team intercept the German Artist at the airport and you found enough task points for an A+ rating.")
                    else:
                        text _("-You helped the team intercept the German Artist at the airport but you did not find enough task points for an A+ rating.")


                    if v_ep03_task_14_helping_the_team == 5:
                        text _("-You helped the team on the next major heist at the art gallery and you found enough task points for an A+ rating.")
                    else:
                        text _("-You helped the team on the next major heist at the art gallery but you did not find enough task points for an A+ rating.")


                    if v_ep03_03_04_lucy_kiss:
                        text _("-You kissed Lucy while you were at the local nightclub.")
                        text _("-You will be able to see Lucy again as a possible love interest in a future episode.")
                    else:
                        text _("-You did not kiss Lucy while you were at the local nightclub.")
                        text _("-You won’t see Lucy again as a possible love interest in a future episode.")



                    if v_ep02_01_04_Switch_The_Drives == True:
                        text _("-You found the Secret Scene with Lucy.")
                    else:
                        text _("-You did not find the Secret Scene with Lucy.")





            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text _("{size=40}Stats{/size}") style "char_info_description"
                text ""
                if v_review_episode == 3:

                    text _("Secret Images: 0/0")
                    text _("Secret Scenes: "+str(v_ep03_othergirls_fantasy_counter)+"/1")
                    text _("Special Date Scenes: 0/0")
                    text _("A+ Tasks Completed: 0/0")
                    text ""
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

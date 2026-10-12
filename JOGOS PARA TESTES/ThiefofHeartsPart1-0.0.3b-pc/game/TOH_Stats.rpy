init:
    $ ariel_love_level = 0
    $ bella_love_level = 0
    $ vivian_love_level = 0
    $ megan_love_level = 0
    $ juliet_love_level = 0
    $ zora_love_level = 0
    $ megan_known = False
    $ juliet_known = False
    $ zora_known = False
    $ v_mm_stats_tab = 0
    $ v_mm_stats_who = "ariel"







style stats_button_style_selected:
    yoffset 225
    xoffset 95
    size 40
    color "#ffb2b6"


style stats_button_style_idle:
    yoffset 225
    xoffset 95
    size 40
    color "#ffffff"

screen scr_mm_stats_menu:
    key "game_menu" action [Hide("scr_mm_stats_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton idle "bg_stats_screen" action NullAction()
    add "black" alpha 0.7


    hbox:
        xalign 0.4
        spacing 10
        if v_mm_stats_who == "ariel":
            imagebutton:
                idle "heart_panel_ariel_hover"
                foreground Text(_("[ariel_love_level]"),style="stats_button_style_selected")
        else:
            imagebutton:
                auto "heart_panel_ariel_%s"
                action SetVariable ("v_mm_stats_who","ariel")
                foreground Text(_("[ariel_love_level]"),style="stats_button_style_idle")

        if v_mm_stats_who == "bella":
            imagebutton:
                idle "heart_panel_bella_hover"
                foreground Text(_("[bella_love_level]"),style="stats_button_style_selected")
        else:
            imagebutton:
                auto "heart_panel_bella_%s"
                action SetVariable ("v_mm_stats_who","bella")
                foreground Text(_("[bella_love_level]"),style="stats_button_style_idle")


        if v_mm_stats_who == "vivian":
            imagebutton:
                idle "heart_panel_vivian_hover"
                foreground Text(_("[vivian_love_level]"),style="stats_button_style_selected")

        else:
            imagebutton:
                auto "heart_panel_vivian_%s"
                action SetVariable ("v_mm_stats_who","vivian")
                foreground Text(_("[vivian_love_level]"),style="stats_button_style_idle")

        if megan_known:
            if v_mm_stats_who == "megan":
                imagebutton:
                    idle "heart_panel_megan_hover"
                    foreground Text(_("[megan_love_level]"),style="stats_button_style_selected")

            else:
                imagebutton:
                    auto "heart_panel_megan_%s"
                    action SetVariable ("v_mm_stats_who","megan")
                    foreground Text(_("[megan_love_level]"),style="stats_button_style_idle")

        else:
            imagebutton:
                idle "heart_panel_unknown_idle"

        if juliet_known:
            if v_mm_stats_who == "juliet":
                imagebutton:
                    idle "heart_panel_juliet_hover"
                    foreground Text(_("[juliet_love_level]"),style="stats_button_style_selected")

            else:
                imagebutton:
                    auto "heart_panel_juliet_%s"
                    action SetVariable ("v_mm_stats_who","juliet")
                    foreground Text(_("[juliet_love_level]"),style="stats_button_style_idle")

        else:
            imagebutton:
                idle "heart_panel_unknown_idle"

        if zora_known:
            if v_mm_stats_who == "zora":
                imagebutton:
                    idle "heart_panel_zora_hover"
                    foreground Text(_("[zora_love_level]"),style="stats_button_style_selected")

            else:
                imagebutton:
                    auto "heart_panel_zora_%s"
                    action SetVariable ("v_mm_stats_who","zora")
                    foreground Text(_("[zora_love_level]"),style="stats_button_style_idle")


        else:
            imagebutton:
                idle "heart_panel_unknown_idle"

        imagebutton:
            idle "heart_panel_unknown_idle"


    hbox:
        xalign 0.4
        yalign 0.4
        style_prefix "radio"
        textbutton _("RELATIONSHIP LEVEL") action SetVariable("v_mm_stats_tab",0)
        textbutton _("SEXUAL PROGRESS") action SetVariable("v_mm_stats_tab",1)

        if v_review_episode >= 2:
            textbutton _("HAREM") action SetVariable("v_mm_stats_tab",3)


    vbox:
        xpos 100
        ypos 500
        if v_mm_stats_who == "ariel":
            use scr_mm_stats_menu_ariel
        if v_mm_stats_who == "vivian":
            use scr_mm_stats_menu_vivian

        if v_mm_stats_who == "bella":
            use scr_mm_stats_menu_bella

        if v_mm_stats_who == "megan":
            use scr_mm_stats_menu_megan

        if v_mm_stats_who == "juliet":
            use scr_mm_stats_menu_juliet

        if v_mm_stats_who == "zora":
            use scr_mm_stats_menu_zora


    imagebutton:
        xalign 0.01
        yalign 0.98
        auto "btn_mm_back_%s" action [Hide("scr_mm_stats_menu",dissolve),renpy.restart_interaction, SetVariable('quick_menu', False)]

    imagebutton:
        xalign 0.98
        yalign 0.98
        auto "btn_mm_exit_%s" action [Hide("scr_mm_stats_menu",dissolve),Hide("scr_mm_main",dissolve),renpy.restart_interaction, SetVariable('quick_menu', True), SetVariable('v_mm_open', False)]



screen scr_mm_stats_menu_ariel:

    if v_mm_stats_tab == 0:
        if ariel_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "[a_name] sees you as her inspiration, her rock to cling to when things get tough."
                text "But nothing more than that."
                text "Play up your romantic and understanding side and you just might get somewhere with [a_name]."


        if ariel_love_level <= 7:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 4-7" style "char_info_description"
                text ""
                text "[a_name] is starting to fall hard for you. So it’s up to you to not let her down, and to continue to be her inspiration."
                text "Spend time with her when you can, show her your romantic and sensual side and you will be rewarded in kind."





    if v_mm_stats_tab == 1:
        if ariel_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "Keep spending time with [a_name] and taking an interest in what she likes and things will change here!"


        if ariel_love_level <= 7:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 4-7" style "char_info_description"
                text ""
                text "Slow and steady wins the race with [a_name]."
                text "Rushing things with her will only hurt your chances of progressing things with the shy redhead."



    if v_mm_stats_tab == 2:
        vbox:
            xalign 0.4
            yalign 0.6
            xmaximum 1500
            text "This is the Selfies section for [a_name]."
            text "Each time you gain a full heart with her, some new selfie images will appear here for you to view."
            text "The more hearts that you gain, the hotter the selfie images in this section will be of [a_name]!"

    if v_mm_stats_tab == 3:
        vbox:
            xalign 0.4
            yalign 0.6
            xmaximum 1500
            text "To gain Harem points for the girls, look out for choices and situations in the story, where she might take an interest in you being with another female character, or even just the idea of sharing you with someone else."
            text "The more of these points you gain, the better your chances of viewing one of the harem scenes, featuring the girls, later in the game."
            text "If you have the Game or In-Game Walkthrough, it will tell you where to find all the Harem points in each Episode."
            text ""
            text ""
            if ariel_harem_points_counter == 0:
                text "Ariel Status: Currently unknown."
            if ariel_harem_points_counter == 1:
                text "Ariel status: Slightly interested."






screen scr_mm_stats_menu_vivian:
    if v_mm_stats_tab == 0:
        if vivian_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "No progression yet as she still sees you as her 'special little guy'."
                text "[v_name] wants to be romanced, told that she is beautiful and doesn’t believe that her best days are behind her."
                text "Make her feel loved and appreciated, and you could be greatly rewarded."




    if v_mm_stats_tab == 1:
        if vivian_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "The opportunities are there to see more of [v_name], you’re just not taking them."
                text "Seeing her sexy, naughty side is easier than you think."

    if v_mm_stats_tab == 2:
        if vivian_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "This is the Selfies section for [v_name]."
                text "Each time you gain a full heart with her, some new selfie images will appear here for you to view."
                text "The more hearts that you gain, the hotter the selfie images in this section will be of [v_name]!"

    if v_mm_stats_tab == 3:
        if vivian_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "To gain Harem points for the girls, look out for choices and situations in the story, where she might take an interest in you being with another female character, or even just the idea of sharing you with someone else."
                text "The more of these points you gain, the better your chances of viewing one of the harem scenes, featuring the girls, later in the game."
                text "If you have the Game or In-Game Walkthrough, it will tell you where to find all the Harem points in each Episode."
                text ""
                text ""
                if vivian_harem_points_counter == 0:
                    text "Vivian Status: Currently unknown."
                if vivian_harem_points_counter == 1:
                    text "Vivian status: Slightly interested."




screen scr_mm_stats_menu_bella:
    if v_mm_stats_tab == 0:
        if bella_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "You and [b_name] rarely get along, even at the best of times."
                text "At best, she respects what you do, but she won’t ever tell you that."
                text "Expect her to be a tough nut to crack."



    if v_mm_stats_tab == 1:
        if bella_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "Don’t piss her off, know when to side with her or defend her honour, and you’ll soon see a different side of [b_name]."

    if v_mm_stats_tab == 2:
        if bella_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "This is the Selfies section for [b_name]."
                text "Each time you gain a full heart with her, some new selfie images will appear here for you to view."
                text "The more hearts that you gain, the hotter the selfie images in this section will be of [b_name]!"

    if v_mm_stats_tab == 3:
        if bella_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "To gain Harem points for the girls, look out for choices and situations in the story, where she might take an interest in you being with another female character, or even just the idea of sharing you with someone else."
                text "The more of these points you gain, the better your chances of viewing one of the harem scenes, featuring the girls, later in the game."
                text "If you have the Game or In-Game Walkthrough, it will tell you where to find all the Harem points in each Episode."
                text ""
                text ""
                if bella_harem_points_counter == 0:
                    text "Bella Status: Currently unknown."
                if bella_harem_points_counter == 1:
                    text "Bella status: Slightly interested."


screen scr_mm_stats_menu_megan:
    if v_mm_stats_tab == 0:
        if megan_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "Can you trust Megan? That’s the million-dollar question right now."
                text "She seems nice enough, but is she genuinely interested in you, or does she have an ulterior motive for befriending you?"
                text "Learn more about her character, trust your instincts..."
                text "And then you might find out the truth about this highly alluring, attractive older woman."
                text "And much, much more..."




    if v_mm_stats_tab == 1:
        if megan_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "Megan isn’t shy about showing you a lot more than most men have had the fortune of seeing."
                text "Further meetings and discussions with this tasty temptress will help you to progress things with her sexually."

    if v_mm_stats_tab == 2:
        if megan_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "This is the Selfies section for Megan."
                text "Each time you gain a full heart with her, some new selfie images will appear here for you to view."
                text "The more hearts that you gain, the hotter the selfie images in this section will be of Megan!"

    if v_mm_stats_tab == 3:
        if megan_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "To gain Harem points for the girls, look out for choices and situations in the story, where she might take an interest in you being with another female character, or even just the idea of sharing you with someone else."
                text "The more of these points you gain, the better your chances of viewing one of the harem scenes, featuring the girls, later in the game."
                text "If you have the Game or In-Game Walkthrough, it will tell you where to find all the Harem points in each Episode."
                text ""
                text ""
                text "Megan Status: Not Available For Harem."


screen scr_mm_stats_menu_juliet:
    if v_mm_stats_tab == 0:
        if juliet_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "You’ve only just met Juliet, and there’s an obvious tension in the air between you two."
                text "This tension could be one a competitive nature, or it could be purely a sexual thing."
                text "Pursuing Juliet could be dangerous, but also ultimately rewarding."


    if v_mm_stats_tab == 1:
        if juliet_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "She’s a drop-dead hottie for sure, but that doesn’t mean it will be easy to get into her pants."
                text "Juliet is a feisty character, but also tiger waiting to get of her cage."
                text "Tread carefully with what you say to her and when you try to get close to her."
                text "Patience is the key here."


    if v_mm_stats_tab == 2:
        if juliet_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "This is the Selfies section for Juliet."
                text "Each time you gain a full heart with her, some new selfie images will appear here for you to view."
                text "The more hearts that you gain, the hotter the selfie images in this section will be of Juliet!"

    if v_mm_stats_tab == 3:
        if juliet_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "To gain Harem points for the girls, look out for choices and situations in the story, where she might take an interest in you being with another female character, or even just the idea of sharing you with someone else."
                text "The more of these points you gain, the better your chances of viewing one of the harem scenes, featuring the girls, later in the game."
                text "If you have the Game or In-Game Walkthrough, it will tell you where to find all the Harem points in each Episode."
                text ""
                text ""
                text "Juliet Status: Currently unknown."


screen scr_mm_stats_menu_zora:
    if v_mm_stats_tab == 0:
        if zora_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "You and Zora have hit it off since your first meeting..."
                text "But now that you have agreed to be her personal trainer, she’s going to rely on you a lot for advice and to help her gain confidence."
                text "Be prepared to help Zora whenever you get to spend time with her."


    if v_mm_stats_tab == 1:
        if zora_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "Level 0-3" style "char_info_description"
                text ""
                text "You’ve only just met, and she already sees you as her hero."
                text "When you have your private session with her, make sure not to be too much of a pervert or to be too touchy-feely with."
                text "Follow these simple instructions and you’ll progress things with Zora."



    if v_mm_stats_tab == 2:
        if zora_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "This is the Selfies section for Zora."
                text "Each time you gain a full heart with her, some new selfie images will appear here for you to view."
                text "The more hearts that you gain, the hotter the selfie images in this section will be of Zora!"

    if v_mm_stats_tab == 3:
        if zora_love_level <= 3:
            vbox:
                xalign 0.4
                yalign 0.6
                xmaximum 1500
                text "To gain Harem points for the girls, look out for choices and situations in the story, where she might take an interest in you being with another female character, or even just the idea of sharing you with someone else."
                text "The more of these points you gain, the better your chances of viewing one of the harem scenes, featuring the girls, later in the game."
                text "If you have the Game or In-Game Walkthrough, it will tell you where to find all the Harem points in each Episode."
                text ""
                text ""
                text "Zora Status: Currently unknown."
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

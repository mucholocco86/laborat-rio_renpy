screen pp_tutorial_screen:
    tag pp_tutorial_screen
    modal True
    add "ep9_party_planning25"
    add "party_planner_tutorial_bg"

    imagebutton:
        xpos 122 * persistent.scale_factor
        ypos 28 * persistent.scale_factor
        if pp_tut_state > 31 and pp_tut_state < 34:
            idle "pp_jacob_0_4_idle"
            hover "pp_jacob_0_4_idle"
        elif pp_tut_state > 22:
            idle "pp_jacob_0_3_idle"
            hover "pp_jacob_0_3_idle"
        elif pp_tut_state > 18:
            idle "pp_jacob_0_2_idle"
            hover "pp_jacob_0_2_idle"
        elif pp_tut_state > 13:
            idle "pp_jacob_0_1_idle"
            hover "pp_jacob_0_1_idle"
        else:
            idle "pp_jacob_0_0_idle"
            hover "pp_jacob_0_0_idle"
        if pp_tut_state == 1 or pp_tut_state == 10 or pp_tut_state == 24:
            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_tut_state",pp_tut_state+1))
        else:
            action NullAction()

    imagebutton:
        xpos 269 * persistent.scale_factor
        ypos 322 * persistent.scale_factor
        if pp_tut_state > 22:
            idle "pp_jamie_1_1_idle"
            hover "pp_jamie_1_1_idle"
        else:
            idle "pp_jamie_1_0_idle"
            hover "pp_jamie_1_0_idle"
        if pp_tut_state == 4 or pp_tut_state == 20:
            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_tut_state",pp_tut_state+1))
        else:
            action NullAction()

    imagebutton:
        xpos 563 * persistent.scale_factor
        ypos 175 * persistent.scale_factor
        if pp_tut_state > 31 and pp_tut_state < 34:
            idle "pp_nick_2_0_idle"
            hover "pp_nick_2_0_idle"
        else:
            idle "pp_nick_2_1_idle"
            hover "pp_nick_2_1_idle"
        if pp_tut_state == 29:
            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_tut_state",pp_tut_state+1))
        else:
            action NullAction()

    imagebutton:
        xpos 857 * persistent.scale_factor
        ypos 470 * persistent.scale_factor
        idle "pp_johnboy_3_0_idle"
        hover "pp_johnboy_3_0_idle"
        action NullAction()



    if pp_tut_state > 11:
        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_ml_inactive"
            hover "pp_ml_inactive"
            action NullAction()

    if pp_tut_state > 13:
        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_ml_active"
            hover "pp_ml_active"
            action NullAction()
        imagebutton:
            xpos 268 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_mr_active"
            hover "pp_mr_active"
            action NullAction()
        imagebutton:
            xpos 417 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_ml_active"
            hover "pp_ml_active"
            action NullAction()

    if pp_tut_state > 17:
        imagebutton:
            xpos 124 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            if pp_tut_state > 18:
                idle "pp_uc_active"
                hover "pp_uc_active"
            else:
                idle "pp_uc_inactive"
                hover "pp_uc_inactive"
            action NullAction()
    if pp_tut_state > 18:
        imagebutton:
            xpos 124 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_lc_active"
            hover "pp_lc_active"
            action NullAction()
        imagebutton:
            xpos 124 * persistent.scale_factor
            ypos 323 * persistent.scale_factor
            idle "pp_uc_active"
            hover "pp_uc_active"
            action NullAction()

    if pp_tut_state > 21:
        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            if pp_tut_state > 22:
                idle "pp_ul_active"
                hover "pp_ul_active"
            else:
                idle "pp_ul_inactive"
                hover "pp_ul_inactive"
            action NullAction()
        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            if pp_tut_state > 22:
                idle "pp_lc_active"
                hover "pp_lc_active"
            else:
                idle "pp_lc_inactive"
                hover "pp_lc_inactive"
            action NullAction()

    if pp_tut_state > 22:
        imagebutton:
            xpos 417 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_ml_active"
            hover "pp_ml_active"
            action NullAction()
        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_mr_active"
            hover "pp_mr_active"
            action NullAction()


    if pp_tut_state > 11:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 307 * persistent.scale_factor
            ypos 65 * persistent.scale_factor
            if pp_tut_state > 13:
                idle "pp_beers_active"
            else:
                idle "pp_beers_disabled"
            hover "pp_beers_remove"
            action NullAction()
    if pp_tut_state > 13:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 453 * persistent.scale_factor
            ypos 65 * persistent.scale_factor
            idle "pp_cups_active"
            hover "pp_cups_remove"
            action NullAction()
    if pp_tut_state > 17:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 160 * persistent.scale_factor
            ypos 210 * persistent.scale_factor
            if pp_tut_state > 18:
                idle "pp_speakers_active"
            else:
                idle "pp_speakers_disabled"
            hover "pp_speakers_remove"
            action NullAction()
    if pp_tut_state > 18:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 160 * persistent.scale_factor
            ypos 355 * persistent.scale_factor
            idle "pp_music_active"
            hover "pp_music_remove"
            action NullAction()
    if pp_tut_state > 21:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 307 * persistent.scale_factor
            ypos 210 * persistent.scale_factor
            if pp_tut_state > 22:
                idle "pp_food_active"
            else:
                idle "pp_food_disabled"
            hover "pp_food_remove"
            action NullAction()
    if pp_tut_state > 22:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 453 * persistent.scale_factor
            ypos 210 * persistent.scale_factor
            idle "pp_trashcans_active"
            hover "pp_trashcans_remove"
            action NullAction()
    if pp_tut_state > 31 and pp_tut_state < 34:
        imagebutton:
            yminimum 143 * persistent.scale_factor
            ymaximum 143 * persistent.scale_factor
            xminimum 143 * persistent.scale_factor
            xmaximum 143 * persistent.scale_factor
            xpos 891 * persistent.scale_factor
            ypos 210 * persistent.scale_factor
            idle "pp_drugs_active"
            hover "pp_drugs_remove"
            if pp_tut_state == 33:
                action (Play("sfx1", "sound_effects/season2/app_click.mp3", loop = False),SetDict(pp_tut_inventory_limited_list,2,1),SetVariable("pp_tut_state",pp_tut_state+1))
            else:
                action NullAction()



    if pp_active_icon == 0:


        imagebutton:
            xpos 122 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 1:

        imagebutton:
            xpos 563 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"

        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 326 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 2:

        imagebutton:
            xpos 122 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"


        imagebutton:
            xpos 563 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_not_want"
            hover "pp_not_want"
    elif pp_active_icon == 3:

        imagebutton:
            xpos 122 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"

        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 326 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 4:


        imagebutton:
            xpos 563 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 5:

        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 326 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 6:

        imagebutton:
            xpos 270 * persistent.scale_factor
            ypos 326 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"

        imagebutton:
            xpos 858 * persistent.scale_factor
            ypos 475 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 7:

        imagebutton:
            xpos 122 * persistent.scale_factor
            ypos 30 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"

        imagebutton:
            xpos 858 * persistent.scale_factor
            ypos 475 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 9:

        imagebutton:
            xpos 563 * persistent.scale_factor
            ypos 176 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"

        imagebutton:
            xpos 858 * persistent.scale_factor
            ypos 475 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"
    elif pp_active_icon == 10:

        imagebutton:
            xpos 858 * persistent.scale_factor
            ypos 475 * persistent.scale_factor
            idle "pp_want"
            hover "pp_want"


    if pp_tut_state == 0:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "In the party planner mini-game, you plan parties, trying to keep the DIKs {color=fe9416}happy{/color}. This tutorial will teach you the basics of the mini-game." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 1:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Click Jacob to highlight him." xalign 0.25 yalign 0.87 style "pp_tut_text_style"
    elif pp_tut_state >= 2 and pp_tut_state < 4:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        if pp_tut_state == 2:
            imagebutton:
                idle "party_planner_tutorial_text_box"
                hover "party_planner_tutorial_text_box"
            text "The {color=fe9416}Happiness{/color} of each DIK can be seen from their avatar and the smiley in the info box." xmaximum 700 * persistent.scale_factor xalign 0.19 yalign 0.89 style "pp_tut_text_style"
        elif pp_tut_state == 3:
            text "There are four levels of {color=fe9416}Happiness{/color}." xmaximum 700 * persistent.scale_factor xalign 0.25 yalign 0.775 style "pp_tut_text_style"
            hbox:
                xalign 0.17
                yalign 0.92
                vbox:
                    xminimum 200 * persistent.scale_factor
                    imagebutton at pp_happiness_zoom:
                        idle "pp_happiness0"
                        hover "pp_happiness0"
                        xalign 0.5
                    text "{color=ff0000}Disappointed{/color}" style "pp_tut_text_style" xalign 0.5
                vbox:
                    xminimum 200 * persistent.scale_factor
                    imagebutton at pp_happiness_zoom:
                        idle "pp_happiness1"
                        hover "pp_happiness1"
                        xalign 0.5
                    text "{color=ffed00}Neutral{/color}" style "pp_tut_text_style" xalign 0.5
                vbox:
                    xminimum 200 * persistent.scale_factor
                    imagebutton at pp_happiness_zoom:
                        idle "pp_happiness2"
                        hover "pp_happiness2"
                        xalign 0.5
                    text "{color=00ff00}Happy{/color}" style "pp_tut_text_style" xalign 0.5
                vbox:
                    xminimum 200 * persistent.scale_factor
                    imagebutton at pp_happiness_zoom:
                        idle "pp_happiness3"
                        hover "pp_happiness3"
                        xalign 0.5
                    text "{color=fe9416}Very happy{/color}" style "pp_tut_text_style" xalign 0.5
    elif pp_tut_state == 4:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Click Jamie to see his {color=fe9416}Happiness{/color}." xalign 0.24 yalign 0.87 style "pp_tut_text_style"
    elif pp_tut_state == 5:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Jamie has a higher level of {color=fe9416}Happiness{/color} than Jacob.\nThe {color=fe9416}happier{/color} a DIK is, the higher your {color=ffed00}score{/color} will be for fulfilling their {color=00ff00}needs{/color}." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 6:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Every DIK has {color=00ff00}4 needs{/color} you can fulfill.\nThe more {color=00ff00}needs{/color} you fulfill, the {color=fe9416}happier{/color} they will be." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 7:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "The three bottom icons show which {color=ffc27b}items{/color} they want to be surrounded by and how many. The text at the top is a special {color=00ff00}need{/color} that we will talk about later." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 8:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "If you fail to fulfill their {color=00ff00}needs{/color}, they will lose {color=fe9416}Happiness{/color}, and you will get a lower {color=ffed00}score{/color}." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 9:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Their {color=fe9416}Happiness{/color} will increase or decrease, depending on your playstyle, and the mini-game choices will affect the story." xalign 0.15 yalign 0.91 style "pp_tut_text_style"

    elif pp_tut_state == 10:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Let's fulfill Jacob's {color=00ff00}needs{/color}. Click on Jacob." xalign 0.20 yalign 0.88 style "pp_tut_text_style"
    elif pp_tut_state == 11:
        imagebutton:
            idle "party_planner_tutorial_focus1"
            hover "party_planner_tutorial_focus1"
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        imagebutton:
            idle "party_planner_tutorial_focus1b"
            hover "party_planner_tutorial_focus1b"
            focus_mask True
            if pp_active_icon == 0:
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(pp_tut_inventory_limited_list,0,0),SetVariable("pp_tut_state",pp_tut_state+1))
        text "Jacob wants 1 {color=ffc27b}Beer{/color}.\nClick the {color=ffc27b}Beers item{/color} to the right to select it and place it in the highlighted box on the grid." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 12:
        imagebutton:
            idle "party_planner_tutorial_focus2"
            hover "party_planner_tutorial_focus2"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "The {color=ffc27b}Beer{/color} is disabled because it needs {color=ffc27b}Cups{/color} to activate. The information at the bottom right shows any requirements for using the {color=ffc27b}items{/color}." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 13:
        imagebutton:
            idle "party_planner_tutorial_focus3"
            hover "party_planner_tutorial_focus3"
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        imagebutton:
            idle "party_planner_tutorial_focus3b"
            hover "party_planner_tutorial_focus3b"
            if pp_active_icon == 8:
                action (Play("sfx1", "sound_effects/season2/beep.mp3", loop = False),SetVariable("pp_tut_multiplier",1.5),SetVariable("pp_tut_state",pp_tut_state+1))
        text "Click the {color=ffc27b}Cups supply{/color} and place it in the highlighted box next to the {color=ffc27b}Beers item{/color} on the grid." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 14:
        imagebutton:
            idle "party_planner_tutorial_focus4"
            hover "party_planner_tutorial_focus4"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "The {color=ffc27b}Beer{/color} is now active, and Jacob's first {color=00ff00}need{/color} is fulfilled. The green dots at the top left of his avatar show how many {color=00ff00}needs{/color} you have fulfilled." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 15:
        imagebutton:
            idle "party_planner_tutorial_focus5"
            hover "party_planner_tutorial_focus5"
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Jacob wants 1 {color=ffc27b}Speaker{/color}. Since you don't have any {color=ffc27b}Speakers{/color}, you will need to purchase one. Click the {color=ffc27b}Speakers item{/color} and then the {color=00ff00}Buy{/color} button." xalign 0.16 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 16:
        imagebutton:
            idle "party_planner_tutorial_focus6"
            hover "party_planner_tutorial_focus6"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "You just bought 1 {color=ffc27b}Speaker{/color} and spent {color=fe9416}money{/color} from the party budget. Keep track of your {color=fe9416}money{/color}. You can sell back {color=00ff00}unused{/color} {color=ffc27b}items{/color} you buy if needed." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 17:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        imagebutton:
            focus_mask True
            idle "party_planner_tutorial_focus7b"
            hover "party_planner_tutorial_focus7b"
            if pp_active_icon == 7:
                action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(pp_tut_inventory_limited_list,7,0),SetVariable("pp_tut_state",pp_tut_state+1))
        text "Place the {color=ffc27b}Speaker{/color} in the box below Jacob on the grid." xalign 0.15 yalign 0.87 style "pp_tut_text_style"
    elif pp_tut_state == 18:
        imagebutton:
            idle "party_planner_tutorial_focus8"
            hover "party_planner_tutorial_focus8"
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        imagebutton:
            focus_mask True
            idle "party_planner_tutorial_focus8b"
            hover "party_planner_tutorial_focus8b"
            if pp_active_icon == 11:
                action (Play("sfx1", "sound_effects/season2/beep.mp3", loop = False),SetVariable("pp_tut_multiplier",1.75),SetVariable("pp_tut_state",pp_tut_state+1))
        text "Activate the {color=ffc27b}Speaker{/color} by putting a {color=ffc27b}Music supply{/color} next to it. Click the {color=ffc27b}Music supply{/color} and put it below the {color=ffc27b}Speaker item{/color}." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 19:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Great! You satisfied another one of Jacob's {color=00ff00}needs{/color}.\nJacob also wants {color=ffc27b}Food{/color} placed next to him.\nClick the {color=ffc27b}Food item{/color}." xalign 0.17 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 20:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "As you can see from the check mark at the top right of Jamie's avatar, he's also interested in {color=ffc27b}Food{/color}.\nClick Jamie." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 21:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        imagebutton:
            focus_mask True
            idle "party_planner_tutorial_focus9b"
            hover "party_planner_tutorial_focus9b"
            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(pp_tut_inventory_limited_list,3,0),SetVariable("pp_tut_state",pp_tut_state+1))
        text "Jamie also wants 1 {color=ffc27b}Food{/color}. Let's have Jacob and Jamie share the {color=ffc27b}Food item{/color} by putting it in the grid above Jamie's avatar." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 22:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        imagebutton:
            focus_mask True
            idle "party_planner_tutorial_focus10b"
            hover "party_planner_tutorial_focus10b"
            if pp_active_icon == 12:
                action (Play("sfx1", "sound_effects/season2/beep.mp3", loop = False),SetVariable("pp_tut_multiplier",2.25),SetVariable("pp_tut_state",pp_tut_state+1))
        text "The {color=ffc27b}Food item{/color} will be used by both Jacob and Jamie, but it needs to be activated first. Activate it by putting a {color=ffc27b}Trashcan supply{/color} in a grid next to it." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 23:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Great job! By being smart with the {color=ffc27b}item{/color} placement, you can fulfill the {color=00ff00}needs{/color} of more DIKs at the same time." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 24:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Any empty grid next to a DIK, in any direction, can be used to satisfy their {color=00ff00}needs{/color}.\nClick Jacob again." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 25:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Every DIK has a special {color=00ff00}need{/color} at the top of their info box. Read it carefully to understand how to fulfill it." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 26:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Jacob wants {color=ffc27b}Drugs{/color} at the party.\nBut where on the grid you put the special {color=00ff00}needs{/color} {color=ffc27b}items{/color} doesn't matter." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 27:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action (SetVariable("pp_active_icon",12),SetVariable("pp_tut_state",pp_tut_state+1))
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "To summarize, the special {color=00ff00}needs{/color} {color=ffc27b}items{/color} can be placed anywhere on the grid, but the {color=ffc27b}items{/color} indicated by the icons must be placed on a grid next to the DIK." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 28:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Click the {color=ffc27b}Drugs item{/color}." xalign 0.24 yalign 0.87 style "pp_tut_text_style"
    elif pp_tut_state == 29:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "You can see how Jacob wants the {color=ffc27b}Drugs{/color} as indicated by the check mark. However, Nick doesn't want {color=ffc27b}Drugs{/color}. Click Nick to see what his {color=00ff00}need{/color} says." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 30:
        imagebutton:
            idle "party_planner_tutorial_info_box_focus"
            hover "party_planner_tutorial_info_box_focus"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Nick's special {color=00ff00}need{/color} says he doesn't want any {color=ffc27b}Drugs{/color} at the party. If you add the {color=ffc27b}Drugs{/color} for Jacob, you will lose the already fulfilled {color=00ff00}need{/color} for Nick." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 31:
        imagebutton:
            focus_mask True
            idle "party_planner_tutorial_focus11b"
            hover "party_planner_tutorial_focus11b"
            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetDict(pp_tut_inventory_limited_list,2,0),SetVariable("pp_tut_state",pp_tut_state+1))
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Put the {color=ffc27b}Drugs{/color} in the highlighted box on the grid and watch what happens." xalign 0.16 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 32:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Jacob's {color=00ff00}needs{/color} are all fulfilled, while Nick lost one of his already fulfilled {color=00ff00}needs{/color}." xalign 0.15 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 33:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Click any {color=ffc27b}item{/color} on the grid to remove it and return it to your inventory. Click the {color=ffc27b}Drugs{/color} you just placed on the grid to remove it." xalign 0.15 yalign 0.91 style "pp_tut_text_style"

    elif pp_tut_state == 34:
        imagebutton:
            idle "party_planner_tutorial_focus12"
            hover "party_planner_tutorial_focus12"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"

        text "When you plan parties, there will be {color=ffc27b}activities{/color} listed here. Most of them cost {color=fe9416}money{/color}. They all improve your party greatly. Prioritize them for a higher score." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 35:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Your goals with the mini-game are to fulfill as many {color=00ff00}needs{/color} as possible for the DIKs and to keep them {color=fe9416}happy{/color}." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 36:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "{color=ffc27b}Items{/color} and {color=ffc27b}Activities{/color} cost money, while {color=ffc27b}Guests{/color} and {color=ffc27b}Supplies{/color} are free. Keep track of your budget when planning your party." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 37:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "You can permanently upgrade your free {color=ffc27b}item{/color} inventory between party planning rounds." xalign 0.16 yalign 0.89 style "pp_tut_text_style"
    elif pp_tut_state == 38:
        imagebutton:
            idle "party_planner_tutorial_focus13"
            hover "party_planner_tutorial_focus13"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "Each party you plan will get a {color=ffed00}score{/color} that's affected by how many {color=00ff00}needs{/color} you fulfilled and the {color=e51475}score multiplier{/color}, which you increase by fulfilling {color=00ff00}needs{/color}." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 39:
        imagebutton:
            idle "pp_invis_tutorial_button"
            hover "pp_invis_tutorial_button"
            action SetVariable("pp_tut_state",pp_tut_state+1)
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "After each party, you will get a report showing your {color=ffed00}score{/color}, and then you can select more perks for the future." xalign 0.15 yalign 0.91 style "pp_tut_text_style"
    elif pp_tut_state == 40:
        imagebutton:
            idle "party_planner_tutorial_text_box"
            hover "party_planner_tutorial_text_box"
        text "You can watch this tutorial again within the mini-game. Click the {color=ff0000}X{/color} at the top right to finish the tutorial and select starting perks." xalign 0.15 yalign 0.91 style "pp_tut_text_style"



    if (pp_tut_state >= 2 and pp_tut_state < 5) or (pp_tut_state > 10 and pp_tut_state < 21) or (pp_tut_state > 24 and pp_tut_state < 30):

        imagebutton:
            xpos 123 * persistent.scale_factor
            ypos 630 * persistent.scale_factor
            if pp_tut_state > 24:
                idle "pp_jacob_0_3_idle"
                hover "pp_jacob_0_3_idle"
            elif pp_tut_state > 18:
                idle "pp_jacob_0_2_idle"
                hover "pp_jacob_0_2_idle"
            elif pp_tut_state >= 14:
                idle "pp_jacob_0_1_idle"
                hover "pp_jacob_0_1_idle"
            else:
                idle "pp_jacob_0_0_idle"
                hover "pp_jacob_0_0_idle"
            action NullAction()

        imagebutton at pp_happiness_zoom:
            idle "pp_happiness0"
            hover "pp_happiness0"
            xalign 0.49
            yalign 0.69
        text "12%" style "pp_info_happiness_style" xpos 922 * persistent.scale_factor ypos 640 * persistent.scale_factor

        vbox:
            xalign 0.28
            yalign 0.665
            xminimum 800 * persistent.scale_factor
            xmaximum 800 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "{size=-%d}Can we have something to smoke at the party? 1 Drugs?{/size}" % (25 * persistent.scale_factor) style "pp_criteria_not_met_style"
            hbox:
                spacing 50 * persistent.scale_factor
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        if pp_tut_state >= 14:
                            idle "pp_beers_active"
                            hover "pp_beers_active"
                        else:
                            idle "pp_beers_idle"
                            hover "pp_beers_idle"
                        action NullAction()
                        yalign 0.5
                    if pp_tut_state >= 14:
                        text "1" style "pp_criteria_met_style"
                    else:
                        text "1" style "pp_criteria_not_met_style"
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        if pp_tut_state > 24:
                            idle "pp_food_active"
                            hover "pp_food_active"
                        else:
                            idle "pp_food_idle"
                            hover "pp_food_idle"
                        action NullAction()
                        yalign 0.5
                    if pp_tut_state > 24:
                        text "1" style "pp_criteria_met_style"
                    else:
                        text "1" style "pp_criteria_not_met_style"
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        if pp_tut_state > 18:
                            idle "pp_speakers_active"
                            hover "pp_speakers_active"
                        else:
                            idle "pp_speakers_idle"
                            hover "pp_speakers_idle"
                        action NullAction()
                        yalign 0.5
                    if pp_tut_state > 18:
                        text "1" style "pp_criteria_met_style"
                    else:
                        text "1" style "pp_criteria_not_met_style"
    elif (pp_tut_state >= 5 and pp_tut_state < 11) or (pp_tut_state >= 21 and pp_tut_state < 25):

        imagebutton:
            xpos 123 * persistent.scale_factor
            ypos 630 * persistent.scale_factor
            if pp_tut_state > 22:
                idle "pp_jamie_1_1_idle"
                hover "pp_jamie_1_1_idle"
            else:
                idle "pp_jamie_1_0_idle"
                hover "pp_jamie_1_0_idle"
            action NullAction()

        imagebutton at pp_happiness_zoom:
            idle "pp_happiness1"
            hover "pp_happiness1"
            xalign 0.49
            yalign 0.69
        text "29%" style "pp_info_happiness_style" xpos 922 * persistent.scale_factor ypos 640 * persistent.scale_factor
        vbox:
            xalign 0.28
            yalign 0.665
            xminimum 800 * persistent.scale_factor
            xmaximum 800 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "{size=-%d}Let's have a lot of Decor at the party! 3 of them!{/size}" % (25 * persistent.scale_factor) style "pp_criteria_not_met_style"
            hbox:
                spacing 50 * persistent.scale_factor
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        idle "pp_liquor_idle"
                        hover "pp_liquor_idle"
                        action NullAction()
                        yalign 0.5
                    text "1" style "pp_criteria_not_met_style"
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        if pp_tut_state > 22:
                            idle "pp_food_active"
                            hover "pp_food_active"
                        else:
                            idle "pp_food_idle"
                            hover "pp_food_idle"
                        action NullAction()
                        yalign 0.5
                    if pp_tut_state > 22:
                        text "1" style "pp_criteria_met_style"
                    else:
                        text "1" style "pp_criteria_not_met_style"
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        idle "pp_snacks_idle"
                        hover "pp_snacks_idle"
                        action NullAction()
                        yalign 0.5
                    text "1" style "pp_criteria_not_met_style"
    elif pp_tut_state >= 30:

        imagebutton:
            xpos 123 * persistent.scale_factor
            ypos 630 * persistent.scale_factor
            if pp_tut_state < 32 or pp_tut_state > 33:
                idle "pp_nick_2_1_idle"
                hover "pp_nick_2_1_idle"
            else:
                idle "pp_nick_2_0_idle"
                hover "pp_nick_2_0_idle"
            action NullAction()

        imagebutton at pp_happiness_zoom:
            idle "pp_happiness2"
            hover "pp_happiness2"
            xalign 0.49
            yalign 0.69

        text "57%" style "pp_info_happiness_style" xpos 922 * persistent.scale_factor ypos 640 * persistent.scale_factor

        vbox:
            xalign 0.28
            yalign 0.665
            xminimum 800 * persistent.scale_factor
            xmaximum 800 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            if pp_tut_state != 32 and pp_tut_state != 33:
                text "{size=-%d}Let's not have any Drugs at this party, ok?{/size}" % (25 * persistent.scale_factor) style "pp_criteria_met_style"
            else:
                text "{size=-%d}Let's not have any Drugs at this party, ok?{/size}" % (25 * persistent.scale_factor) style "pp_criteria_not_met_style"
            hbox:
                spacing 50 * persistent.scale_factor
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        idle "pp_decor_idle"
                        hover "pp_decor_idle"
                        action NullAction()
                        yalign 0.5
                    text "2" style "pp_criteria_not_met_style"
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        idle "pp_kegs_idle"
                        hover "pp_kegs_idle"
                        action NullAction()
                        yalign 0.5
                    text "1" style "pp_criteria_not_met_style"
                hbox:
                    xminimum 150 * persistent.scale_factor
                    imagebutton:
                        idle "pp_girls_idle"
                        hover "pp_girls_idle"
                        action NullAction()
                        yalign 0.5
                    text "3" style "pp_criteria_not_met_style"



    text "Items" style "pp_header_style" xalign 0.82 yalign 0.02
    text "Guests" style "pp_header_style" xalign 0.697 yalign 0.28
    text "Supplies" style "pp_header_style" xalign 0.935 yalign 0.28
    text "Activities" style "pp_header_style" xalign 0.82 yalign 0.54

    hbox:
        xalign 0.97
        yalign 0.125
        spacing 20 * persistent.scale_factor
        for x in range(0,len(pp_icons_limited_list)):
            vbox:
                if pp_active_icon == x:
                    text pp_icons_limited_list[x] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
                else:
                    text pp_icons_limited_list[x] style "pp_icon_style" yalign 0.5 xalign 0.5
                imagebutton:
                    if pp_active_icon == x:
                        idle "pp_"+pp_icons_limited_list[x].lower()+"_hover"
                    else:
                        idle "pp_"+pp_icons_limited_list[x].lower()+"_idle"
                    hover "pp_"+pp_icons_limited_list[x].lower()+"_hover"
                    if pp_tut_state == 28 and x == 2:
                        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", x),SetVariable("pp_tut_state",pp_tut_state+1))
                    elif pp_tut_state == 19 and x == 3:
                        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", x),SetVariable("pp_tut_state",pp_tut_state+1))
                    elif (pp_tut_state >= 19 and pp_tut_state < 22) or pp_tut_state > 28:
                        action NullAction()
                    else:
                        action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", x))
                    yalign 0.5
                    xalign 0.5
                if pp_tut_inventory_limited_list[x] > 0:
                    if pp_bought_tut_this_round[x] > 0:
                        text "{color=00ff00}{size=+%d}%d{/size}{/color}" % ((10 * persistent.scale_factor),pp_tut_inventory_limited_list[x]) style "pp_icon_style" yalign 0.5 xalign 0.5
                    else:
                        text "{size=+%d}%d{/size}" % ((10 * persistent.scale_factor),pp_tut_inventory_limited_list[x]) style "pp_icon_style" yalign 0.5 xalign 0.5
                else:
                    text "{color=ff0000}{size=+%d}%d{/size}{/color}" % ((10 * persistent.scale_factor),pp_tut_inventory_limited_list[x]) style "pp_icon_style" yalign 0.5 xalign 0.5
    hbox:
        xalign 0.7
        yalign 0.41
        spacing 20 * persistent.scale_factor
        vbox:
            if pp_active_icon == 1+len(pp_icons_limited_list):
                text pp_icons_unlimited_list[1] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[1] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 1+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[1].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[1].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[1].lower()+"_hover"
                if (pp_tut_state >= 19 and pp_tut_state < 22) or pp_tut_state > 28:
                    action NullAction()
                else:
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 1+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
        vbox:
            if pp_active_icon == 2+len(pp_icons_limited_list):
                text pp_icons_unlimited_list[2] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[2] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 2+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[2].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[2].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[2].lower()+"_hover"
                if (pp_tut_state >= 19 and pp_tut_state < 22) or pp_tut_state > 28:
                    action NullAction()
                else:
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 2+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
    hbox:
        xalign 0.956
        yalign 0.41
        spacing 20 * persistent.scale_factor
        vbox:
            if pp_active_icon == len(pp_icons_limited_list):
                text pp_icons_unlimited_list[0] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[0] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[0].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[0].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[0].lower()+"_hover"
                if (pp_tut_state >= 19 and pp_tut_state < 22) or pp_tut_state > 28:
                    action NullAction()
                else:
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
        vbox:
            if pp_active_icon == 3+len(pp_icons_limited_list):
                text pp_icons_unlimited_list[3] style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text pp_icons_unlimited_list[3] style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 3+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[3].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[3].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[3].lower()+"_hover"
                if (pp_tut_state >= 19 and pp_tut_state < 22) or pp_tut_state > 28:
                    action NullAction()
                else:
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 3+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5
        vbox:
            if pp_active_icon == 4+len(pp_icons_limited_list):
                text "Trash Cans" style "pp_icon_selected_style" yalign 0.5 xalign 0.5
            else:
                text "Trash Cans" style "pp_icon_style" yalign 0.5 xalign 0.5
            imagebutton:
                if pp_active_icon == 4+len(pp_icons_limited_list):
                    idle "pp_"+pp_icons_unlimited_list[4].lower()+"_hover"
                else:
                    idle "pp_"+pp_icons_unlimited_list[4].lower()+"_idle"
                hover "pp_"+pp_icons_unlimited_list[4].lower()+"_hover"
                if (pp_tut_state >= 19 and pp_tut_state < 22) or pp_tut_state > 28:
                    action NullAction()
                else:
                    action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_active_icon", 4+len(pp_icons_limited_list)))
                yalign 0.5
                xalign 0.5
            text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (10 * persistent.scale_factor) style "pp_icon_style" yalign 0.5 xalign 0.5


    vpgrid:
        xalign 1.0
        yalign 0.76
        rows len(pp_tut_activity_list)
        cols 3
        xminimum 750 * persistent.scale_factor

        yspacing 45 * persistent.scale_factor
        xoffset 20 * persistent.scale_factor
        for x in range (0,len(pp_tut_activity_list)):
            for y in range (0,len(pp_tut_activity_list[x])):
                if len(pp_tut_activity_list[x]) < 3 and y == 0:
                    textbutton " " text_style "pp_icon_style" xminimum 230 * persistent.scale_factor action NullAction()
                if pp_tut_activity_list[x][y][1] > 0:
                    if pp_tut_activity_choices[x]==y:
                        textbutton "{u}%s{/u} ({color=fe9416}$%d{/color})" % (pp_tut_activity_list[x][y][0],pp_tut_activity_list[x][y][1]) text_style "pp_activity_selected_style" xminimum 250 * persistent.scale_factor action NullAction()
                    else:
                        if pp_tut_activity_list[x][y][1] <= pp_tut_money + pp_tut_activity_list[x][pp_tut_activity_choices[x]][1]:
                            textbutton "%s ({color=fe9416}$%d{/color})" % (pp_tut_activity_list[x][y][0],pp_tut_activity_list[x][y][1]) text_style "pp_activity_style" xminimum 250 * persistent.scale_factor action (Play("sfx1", "sound_effects/coin.mp3", loop = False),SetVariable("pp_tut_money",pp_tut_money-pp_tut_activity_list[x][y][1]+pp_tut_activity_list[x][pp_tut_activity_choices[x]][1]),SetDict(pp_tut_activity_choices,x,y))
                        else:
                            textbutton "%s ({color=fe9416}$%d{/color})" % (pp_tut_activity_list[x][y][0],pp_tut_activity_list[x][y][1]) text_style "pp_activity_style_disabled" xminimum 250 * persistent.scale_factor action NullAction()
                else:
                    if pp_tut_activity_choices[x]==y:
                        textbutton "{u}%s{/u}" % pp_tut_activity_list[x][y][0] text_style "pp_activity_selected_style" xminimum 250 * persistent.scale_factor action NullAction()
                    else:
                        textbutton "%s" % pp_tut_activity_list[x][y][0] text_style "pp_activity_style" xminimum 250 * persistent.scale_factor action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False),SetVariable("pp_tut_money",pp_tut_money+pp_tut_activity_list[x][pp_tut_activity_choices[x]][1]), SetDict(pp_tut_activity_choices,x,y))
    vbox:
        xalign 0.615
        yalign 0.77
        spacing 40 * persistent.scale_factor
        text "I" style "pp_activity_number_style"
        text "II" style "pp_activity_number_style"
        text "III" style "pp_activity_number_style"

    vbox:
        xalign 0.76
        yalign 0.975
        xminimum 400 * persistent.scale_factor
        text "{size=-%d}{color=ffed00}Money:{/color} {color=fe9416}$[pp_tut_money]{/color}{/size}" % (5 * persistent.scale_factor) style "pp_stat_style"
        text "{size=-%d}{color=ffed00}Multiplier:{/color} {color=e51475}[pp_tut_multiplier]x{/color}{/size}" % (5 * persistent.scale_factor) style "pp_stat_style"
        text "{size=-%d}{color=ffed00}Score:{/color} 0{/size}" % (5 * persistent.scale_factor) style "pp_stat_style"


    if pp_active_icon >= 0:
        if pp_active_icon < len(pp_icons_limited_list):
            hbox:
                xalign 0.89 yalign 0.92 xminimum 300 * persistent.scale_factor
                text pp_icons_limited_list[pp_active_icon] style "pp_stat_text_style" xalign 0.5
            hbox:
                xalign 0.905 yalign 0.93
                imagebutton:
                    idle "pp_"+pp_icons_limited_list[pp_active_icon].lower()+"_idle"
                    hover "pp_"+pp_icons_limited_list[pp_active_icon].lower()+"_idle"
                    action NullAction()
            hbox:
                xalign 0.998 yalign 0.95 xminimum 170 * persistent.scale_factor xoffset 15 * persistent.scale_factor
                vbox:
                    if pp_tut_money >= pp_price_limited_list[pp_active_icon]:
                        if pp_tut_state == 15 and pp_active_icon == 7:
                            textbutton "{size=-%d}Buy {color=fe9416}$%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_buy_style" action (Play("sfx1", "sound_effects/coin.mp3", loop = False),SetVariable("pp_tut_money", pp_tut_money - pp_price_limited_list[pp_active_icon]),SetDict(pp_tut_inventory_limited_list,pp_active_icon,pp_tut_inventory_limited_list[pp_active_icon]+1),SetVariable("pp_tut_state",pp_tut_state+1),SetDict(pp_bought_tut_this_round,pp_active_icon,pp_bought_tut_this_round[pp_active_icon]+1))
                        else:
                            textbutton "{size=-%d}Buy {color=fe9416}$%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_buy_style" action NullAction()
                    else:
                        textbutton "{size=-%d}{color=ff0000}Buy $%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_stat_style" action NullAction()
                    if pp_bought_tut_this_round[pp_active_icon] and pp_tut_inventory_limited_list[pp_active_icon] > 0:
                        textbutton "{size=-%d}Sell {color=fe9416}$%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_buy_style" action NullAction()
                    else:
                        textbutton "{size=-%d}{color=ff0000}Sell $%d{/color}{/size}" % ((5 * persistent.scale_factor), pp_price_limited_list[pp_active_icon]) text_style "pp_stat_style" action NullAction()
        else:
            hbox:
                xalign 0.89 yalign 0.92 xminimum 300 * persistent.scale_factor
                text pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)] style "pp_stat_text_style" xalign 0.5
            hbox:
                xalign 0.905 yalign 0.93
                imagebutton:
                    idle "pp_"+pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)].lower()+"_idle"
                    hover "pp_"+pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)].lower()+"_idle"
                    action NullAction()
            hbox:
                xalign 0.998 yalign 0.925 xminimum 170 * persistent.scale_factor xoffset 20 * persistent.scale_factor
                text "{size=+%d}{color=ffed00}∞{/color}{/size}" % (20 * persistent.scale_factor) style "pp_stat_text_style"
    hbox:
        xalign 0.96
        yalign 0.976
        xminimum 300 * persistent.scale_factor
        xmaximum 300 * persistent.scale_factor
        if pp_active_icon >= 0:
            if pp_active_icon < len(pp_icons_limited_list):
                if pp_icons_limited_dependency_list[pp_active_icon] != "":
                    text "{size=-%d}Activated by %s{/size}" % ((10 * persistent.scale_factor), pp_icons_limited_dependency_list[pp_active_icon]) style "pp_stat_style" xalign 0.5
                else:
                    text " " style "pp_stat_style"
            else:
                $ tmp_str = ""
                for i in range(0,len(pp_icons_limited_dependency_list)):
                    if pp_icons_limited_dependency_list[i] == pp_icons_unlimited_list[pp_active_icon-len(pp_icons_limited_list)]:
                        $ tmp_str += pp_icons_limited_list[i] + " "
                if tmp_str != "":
                    text "{size=-%d}Activates [tmp_str]{/size}" % (10 * persistent.scale_factor) style "pp_stat_style" xalign 0.5
                else:
                    text " " style "pp_stat_style"
        else:
            text " " style "pp_stat_style"

    imagebutton:
        idle "pp_x_button_idle"
        hover "pp_x_button_hover"
        xalign 0.985
        yalign 0.025
        if from_game_tut or pp_tut_state == 40:
            action (Play("sfx1", "sound_effects/interlude/select_choice.mp3", loop = False), Hide("pp_tutorial_screen"), Return())
        else:
            action NullAction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

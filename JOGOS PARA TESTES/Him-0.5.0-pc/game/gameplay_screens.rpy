default screen_tooltip = ""  
default time_of_day = "morning"
default angry = False
default anger_duration = 0
default cycle = 0

default in_bedroom = False
default in_kitchen = False
default in_throne = False
default in_roof = False
default in_blacksmith = False
default in_guild = False
default in_brothel = False

default overview_open = False
default stats_open = False
default all_options = False
default mc_overview_open = False
default quest_screen_open = False
default map_screen_open = False
default irda_city_map = False
default world_map = False
default show_pregnancy_timer_screen = True

default got_map = False
default mx = "Master"
default rx = "Sir"

init python:
    current_objective = ""
    second_objective = ""
    third_objective = ""

default mc_marital = "single"
default mc_residency = "none"
default mc_job = "none"
default mc_card_reg = False

screen mc_stats():
    if mc_overview_open:
        add "mc_stats_main"

        text "Irda Citizenship Card" size 60 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 380 xanchor 0.5 yanchor 0.5

        text "[mc]" size 70 color "#cf436b" xpos 0.478 ypos 0.295 font "candara.ttf"
        text "[mc_coin]" size persistent.choices_text_size color "#FFFFFF" xpos 0.497 ypos 0.655 font "Lora-VariableFont_wght.ttf"
        
        text "Sex: Male" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 838 ypos 580 xanchor 0.5 yanchor 0.5
        text "Race: Human" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1285 ypos 580 xanchor 0.5 yanchor 0.5
        text "Date: 4th Reed, 607 AE" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1710 ypos 638 xanchor 0.5 yanchor 0.5

        text "Coin:" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1285 ypos 920 xanchor 0.5 yanchor 0.5

        text "Honor" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1285 ypos 730 xanchor 0.5 yanchor 0.5
        text "HIM" size persistent.choices_text_size color "#cf4343" font "candara_bold.ttf" xpos 840 ypos 730 xanchor 0.5 yanchor 0.5
        text "HERO" size persistent.choices_text_size color "#43c3cf" font "candara_bold.ttf" xpos 1710 ypos 730 xanchor 0.5 yanchor 0.5

        if mc_card_reg:
            text "This document certifies full citizenship within the Kingdom of Irda. The bearer is recognized as a lawful citizen and entitled to all rights, protections, and privileges under Irdan law. Warning: Loss or defacement of this document must be reported without delay to the nearest guard post for reissue.":
                size 15 color "#ffffff" font "candara_bold.ttf" xpos 1285 ypos 1050 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
        else:
            text "This document grants provisional citizenship within the Kingdom of Irda. The bearer is entitled to basic rights and protections under Irdan law until full registration is completed. Warning: Loss or defacement of this document must be reported without delay to the nearest guard post for reissue.":
                size 15 color "#ffffff" font "candara_bold.ttf" xpos 1285 ypos 1050 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

        if mc_marital == "single":
            text "Marital Status: Single" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 860 ypos 638 xanchor 0.5 yanchor 0.5
        elif mc_marital == "married":
            text "Marital Status: Married" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 860 ypos 638 xanchor 0.5 yanchor 0.5
        elif mc_marital == "divorced":
            text "Marital Status: Divorced" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 860 ypos 638 xanchor 0.5 yanchor 0.5
        
        if mc_residency == "none":
            text "Residency: None" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1285 ypos 638 xanchor 0.5 yanchor 0.5
        elif mc_residency == "castle":
            text "Residency: Castle Irda" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1285 ypos 638 xanchor 0.5 yanchor 0.5

        if mc_job == "none":
            text "Job: None" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1730 ypos 580 xanchor 0.5 yanchor 0.5
        if mc_job == "royal_servant":
            text "Job: Royal Servant" size persistent.choices_text_size color "#fff" font "candara_bold.ttf" xpos 1730 ypos 580 xanchor 0.5 yanchor 0.5

        if not in_scene93:
            imagebutton auto "tutorial_bj_back_%s":
                focus_mask True
                action [SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", True)]
            text "CLOSE":
                size 70 color "#fff" font "candara_bold.ttf" xpos 1280 ypos 1165 xanchor 0.5 yanchor 0.5

        if mc_karma >= 10:
            add "karma_lvl10"
            text "Hero (Lvl 10)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 9:
            add "karma_lvl9"
            text "Saviour (Lvl 9)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 8:
            add "karma_lvl8"
            text "Noble (Lvl 8)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 7:
            add "karma_lvl7"
            text "Virtuous (Lvl 7)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 6:
            add "karma_lvl6"
            text "Kind (Lvl 6)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 5:
            add "karma_lvl5"
            text "Neutral (Lvl 5)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 4:
            add "karma_lvl4"
            text "Selfish (Lvl 4)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 2:
            add "karma_lvl3"
            text "Dishonorable (Lvl 3)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 2:
            add "karma_lvl2"
            text "Corrupt (Lvl 2)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        elif mc_karma >= 1:
            add "karma_lvl1"
            text "Him (Lvl 1)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
        else:
            add "karma_lvl1"
            text "Him (Lvl 1)" size 20 color "#fff" font "candara_bold.ttf" xpos 1285 ypos 810 xanchor 0.5 yanchor 0.5
            
screen mc_quests():
    if quest_screen_open:
        add "quest_screen"

        imagebutton auto "tutorial_bj_back_%s":
            focus_mask True
            action [SetVariable("quest_screen_open", False), SetVariable("free_roam_arrows", True)]
        text "CLOSE":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1280 ypos 1165 xanchor 0.5 yanchor 0.5
        
        vbox:
            xpos 0.360
            ypos 0.16
            
            text "[current_objective]" size 30 color "#FFFFFF" font "Lora-VariableFont_wght.ttf"
            text "[second_objective]" size 30 color "#FFFFFF" font "Lora-VariableFont_wght.ttf"
            text "[third_objective]" size 30 color "#FFFFFF" font "Lora-VariableFont_wght.ttf"


screen free_roam_choices:
    imagebutton auto "quests_%s":
        focus_mask True
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        add "free_roam_choices_main"

        if mc_permission_reb and not mc_rejected_wedding_reb:
            if not mc_friend_reb:
                button:
                    focus_mask True
                    action Jump("free_roam_reb")
                    add "free_roam_main_choice2"
                    text "Talk to Rebecca": 
                        size persistent.free_roam_choices_text_size color "#cf436b" hover_color "#851737" font "candara_bold.ttf" xpos 735 ypos 525 xanchor 0.5 yanchor 0.5

            else:
                button:
                    focus_mask True
                    action Jump("free_roam_reb")
                    add "free_roam_main_choice2"
                    text "Talk to Rebecca": 
                        size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 735 ypos 525 xanchor 0.5 yanchor 0.5

        else:
            text "Talk to Rebecca": 
                size persistent.free_roam_choices_text_size color "#818181" font "candara_bold.ttf" xpos 735 ypos 525 xanchor 0.5 yanchor 0.5

        if mc_market_first:
            button:
                focus_mask True
                action Jump("scene29_market")
                add "free_roam_main_choice4"
                text "Go to the Market": 
                    size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 795 xanchor 0.5 yanchor 0.5

        elif not mc_met_reham or not mc_met_nadia:
            button:
                focus_mask True
                action Jump("free_roam_market")
                add "free_roam_main_choice4"
                text "Go to the Market":
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 795 xanchor 0.5 yanchor 0.5
        
        elif in_scene34 and mc_harem_nadia and not mc_harem_talk_nadia:
            button:
                focus_mask True
                action Jump("mc_harem_talk_nadia")
                add "free_roam_main_choice4"
                text "Go to the Market": 
                    size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 795 xanchor 0.5 yanchor 0.5

        else:
            button:
                focus_mask True
                action Jump("free_roam_market2")
                add "free_roam_main_choice4"
                text "Go to the Market": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 795 xanchor 0.5 yanchor 0.5
                    

        button:
            focus_mask True
            action Jump("free_roam_diana")
            add "free_roam_main_choice5"
            text "Go to the Brothel": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 930 xanchor 0.5 yanchor 0.5
        
        if mc_harem_yuuhi:
            if not yuuhi_harem_training_finished and not yuuhi_sex_times == 0:
                button:
                    focus_mask True
                    action Jump("free_roam_yuuhi")
                    add "free_roam_main_choice3"
                    text "Visit Yuuhi": 
                        size persistent.free_roam_choices_text_size color "#cf436b" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 655 xanchor 0.5 yanchor 0.5

            else:
                button:
                    focus_mask True
                    action Jump("free_roam_yuuhi")
                    add "free_roam_main_choice3"
                    text "Visit Yuuhi": 
                        size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 655 xanchor 0.5 yanchor 0.5

        else:
            if mc_armor_timer == 0 and not mc_got_armor:
                if not mc_met_nadia:
                    button:
                        focus_mask True
                        action Jump("scene31_nope")
                        add "free_roam_main_choice3"
                        text "Visit Yuuhi": 
                            size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 655 xanchor 0.5 yanchor 0.5

                else:
                    button:
                        focus_mask True
                        action Jump("scene31")
                        add "free_roam_main_choice3"
                        text "Visit Yuuhi": 
                            size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 655 xanchor 0.5 yanchor 0.5

            else:
                button:
                    focus_mask True
                    action Jump("free_roam_yuuhi")
                    add "free_roam_main_choice3"
                    text "Visit Yuuhi": 
                        size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 655 xanchor 0.5 yanchor 0.5

        if not mc_maia_left:
            button:
                focus_mask True
                action Jump("free_roam_maia")
                add "free_roam_main_choice1"
                text "Talk to Maia": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 380 xanchor 0.5 yanchor 0.5

        elif mc_maia_left and not mc_maia_left_talk:
            button:
                focus_mask True
                action Jump("free_roam_maia_left")
                add "free_roam_main_choice1"
                text "Talk to Maia": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 380 xanchor 0.5 yanchor 0.5

        else:
            text "Talk to Maia": 
                    size persistent.free_roam_choices_text_size color "#818181" font "candara_bold.ttf" xpos 728 ypos 380 xanchor 0.5 yanchor 0.5

        if in_scene30:
            if not mc_armor_timer == 0:
                if not mc_met_nadia:
                    button:
                        focus_mask True
                        action Jump("free_roam_before_sleep")
                        add "free_roam_main_choice6"
                        text "End Day": 
                            size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
                else:
                    button:
                        focus_mask True
                        action Jump("free_roam_before_sleep")
                        add "free_roam_main_choice6"
                        text "End Day": 
                            size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
            
            else:
                text "End Day": 
                    size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
                
        elif in_scene32:
            button:
                focus_mask True
                action Jump("scene32_2")
                add "free_roam_main_choice6"
                text "Go to the Guild": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
                
        elif in_scene34:
            if mc_harem_nadia and not mc_harem_talk_nadia:
                button:
                    focus_mask True
                    action Jump("mc_harem_talk_nadia_no")
                    add "free_roam_main_choice6"
                    text "End Day": 
                        size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
            else:
                button:
                    focus_mask True
                    action Jump("free_roam_before_sleep")
                    add "free_roam_main_choice6"
                    text "End Day": 
                        size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5

        elif in_scene35:
            button:
                focus_mask True
                action Jump("scene35_part2")
                add "free_roam_main_choice6"
                text "Go to the Guild": 
                    size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5

        elif in_scene35_2:
            if in_scene35_2_timer == 0:
                button:
                    focus_mask True
                    action Jump("scene35_fin")
                    add "free_roam_main_choice6"
                    text "Head Out": 
                        size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
            else:
                button:
                    focus_mask True
                    action Jump("free_roam_before_sleep")
                    add "free_roam_main_choice6"
                    text "End Day": 
                        size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5
        
        elif in_scene64:
            button:
                focus_mask True
                action Jump("scene64")
                add "free_roam_main_choice6"
                text "End Day": 
                    size persistent.free_roam_choices_text_size color "#FFD700" hover_color "#851737" font "candara_bold.ttf" xpos 728 ypos 1069 xanchor 0.5 yanchor 0.5

default maia_sex_tab = False
default maia_sex_tab_regular = False
default maia_sex_tab_slave = False
default maia_sex_tab_toys = False
default maia_sex_tab_clothes = False
default is_maia_talk = False


screen is_maia():
    modal True
    if all_options:
        add "is_maia_choices_main"
        
        
        button:
            focus_mask True
            action [SetVariable("is_maia_talk", True), SetVariable("all_options", False)]
            add "free_roam_maia_op1"
            text "Talk": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
            
        if maia_happy and mc_maia_no_sex_real:
            button:
                focus_mask True
                action [SetVariable("is_maia_talk", True), SetVariable("all_options", False)]
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
        
        elif maia_happy:
            button:
                focus_mask True
                action [SetVariable("maia_sex_tab_regular", True), SetVariable("all_options", False)]
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        else:
            button:
                focus_mask True
                action Jump("maia_no_sex")
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("maia_getfour")
            add "free_roam_maia_op3"
            text "Play": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("maia_mc_rename")
            add "free_roam_maia_op4"
            text "\"Refer to me as...\"": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 795 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("free_roam_main_label")
            add "free_roam_maia_op5"
            text "Leave": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 933 xanchor 0.5 yanchor 0.5
    
    if is_maia_talk:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
            action [SetVariable("maia_talk_choice4", True), SetVariable("maia_talk_choice2", False), SetVariable("maia_talk_choice3", False), SetVariable("maia_talk_choice1", False), SetVariable("maia_talk_choice5", False), Jump("is_maia_talk")]
        text "\"What do you think about me?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 

        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_maia_talk_pregnant")
        text "\"How is your pregnancy?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("maia_talk_choice1", True), SetVariable("maia_talk_choice2", False), SetVariable("maia_talk_choice3", False), SetVariable("maia_talk_choice4", False), SetVariable("maia_talk_choice5", False), Jump("is_maia_talk")]
        text "\"How are you doing?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("maia_talk_choice2", True), SetVariable("maia_talk_choice1", False), SetVariable("maia_talk_choice3", False), SetVariable("maia_talk_choice4", False), SetVariable("maia_talk_choice5", False), Jump("is_maia_talk")]
        text "\"I want to know more about you.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 
        
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("maia_talk_choice3", True), SetVariable("maia_talk_choice2", False), SetVariable("maia_talk_choice1", False), SetVariable("maia_talk_choice4", False), SetVariable("maia_talk_choice5", False), Jump("is_maia_talk")]
        text "\"How are they treating you?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action [SetVariable("all_options", True), SetVariable("is_maia_talk", False)]
        text "Back": 
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

        if not mc_told_maia_nadia:
            imagebutton auto "main_choices_left_op1_%s":
                focus_mask True
                action Jump("free_roam_maia_nadia")
            text "\"What do you think about me being with other woman?\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600

        if mc_told_maia_nadia:
            if maia_happy and not maia_sad:
                if not mc_told_maia_slaver and mc_met_slaver:
                    imagebutton auto "main_choices_left_op1_%s":
                        focus_mask True
                        action Jump("free_roam_maia_talk_slaver")
                    text "Talk about the merchant":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True 

                if not mc_told_maia_guild and mc_talked_eireen:
                    imagebutton auto "main_choices_left_op2_%s":
                        focus_mask True
                        action Jump("free_roam_maia_talk_guild")
                    text "Talk about the guild":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True 

                if not mc_told_maia_ogre:
                    imagebutton auto "main_choices_left_op3_%s":
                        focus_mask True
                        action Jump("free_roam_maia_talk_ogre")
                    text "Talk about the ogre":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

                if mc_told_maia_slaver and not mc_told_maia_witch and mc_met_witch:
                    imagebutton auto "main_choices_left_op1_%s":
                        focus_mask True
                        action Jump("free_roam_maia_talk_witch")
                    text "Talk about the witch":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True 
    
    if maia_sex_tab_regular:
        add "is_maia_choices_main2"
        
        button:
            focus_mask True
            action Jump("is_maia_hj1")
            add "free_roam_maia_op1"
            text "Handjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
        
        button:
            focus_mask True
            action Jump("is_maia_tj1")
            add "free_roam_maia_op2"
            text "Titjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_maia_bj")
            add "free_roam_maia_op3"
            text "Blowjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

        if in_scene18:
            button:
                focus_mask True
                action Jump("is_maia_sex_notyet")
                add "free_roam_maia_op4"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 795 xanchor 0.5 yanchor 0.5
        else:
            button:
                focus_mask True
                action Jump("is_maia_sex")
                add "free_roam_maia_op4"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 795 xanchor 0.5 yanchor 0.5
        
        button:
            focus_mask True
            action Jump("is_maia_footjob")
            add "free_roam_maia_op5"
            text "Footjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 933 xanchor 0.5 yanchor 0.5
        
        button:
            focus_mask True
            action [SetVariable("maia_sex_tab_regular", False), SetVariable("all_options", True)]
            add "free_roam_maia_op6"
            text "Back": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 1070 xanchor 0.5 yanchor 0.5

default is_reb_sex_first = True
default is_reb_talk = False
default mc_told_reb_maia = False
default mc_told_reb_yuuhi = False
default mc_told_reb_diana = False
screen is_reb():
    modal True
    if all_options:
        add "is_diana_choices_main"

        button:
            focus_mask True
            action [SetVariable("is_reb_talk", True), SetVariable("all_options", False)]
            add "free_roam_maia_op1"
            text "Talk": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
        
        if is_reb_sex_first:
            button:
                focus_mask True
                action Jump("is_reb_sex_first")
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
        else:
            button:
                focus_mask True
                action [SetVariable("reb_sex_tab_regular", True), SetVariable("all_options", False)]
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        if in_scene54:
            button:
                focus_mask True
                action Jump("scene55_taskboard")
                add "free_roam_maia_op3"
                text "Leave": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
        else:
            button:
                focus_mask True
                action Jump("free_roam_main_label")
                add "free_roam_maia_op3"
                text "Leave": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

    if is_reb_talk:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_reb_talk_pregnant")
        text "\"How's your pregnancy?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("reb_talk_choice1", True), SetVariable("reb_talk_choice2", False), SetVariable("reb_talk_choice3", False), SetVariable("reb_talk_choice4", False), SetVariable("reb_talk_choice5", False), Jump("is_reb_talk")]
        text "\"How are you doing?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("reb_talk_choice2", True), SetVariable("reb_talk_choice1", False), SetVariable("reb_talk_choice3", False), SetVariable("reb_talk_choice4", False), SetVariable("reb_talk_choice5", False), Jump("is_reb_talk")]
        text "\"I want to know more about you.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("reb_talk_choice4", True), SetVariable("reb_talk_choice2", False), SetVariable("reb_talk_choice3", False), SetVariable("reb_talk_choice1", False), SetVariable("reb_talk_choice5", False), Jump("is_reb_talk")]
        text "\"What do you think about me?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action [SetVariable("all_options", True), SetVariable("is_reb_talk", False)]
        text "Back":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

        if not mc_told_reb_maia:
            imagebutton auto "main_choices_left_op1_%s":
                focus_mask True
                action Jump("free_roam_reb_talk_maia")
            text "Talk about Maia":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        if not mc_told_reb_yuuhi and mc_harem_yuuhi:
            imagebutton auto "main_choices_left_op2_%s":
                focus_mask True
                action Jump("free_roam_reb_talk_yuuhi")
            text "Talk about Yuuhi":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True 
        if not mc_told_reb_diana and (
            persistent.scene5_p3_replay or 
            persistent.scene6_p3_replay or 
            persistent.scene7_p3_replay):
            imagebutton auto "main_choices_left_op3_%s":
                focus_mask True
                action Jump("free_roam_reb_talk_diana")
            text "Talk about Diana":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if reb_sex_tab_regular:
        add "is_reb_sec_choices_main"
        button:
            focus_mask True
            action Jump("is_reb_hj_first")
            add "free_roam_maia_op1"
            text "Handjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_reb_fj_first")
            add "free_roam_maia_op2"
            text "Footjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action [SetVariable("all_options", True), SetVariable("reb_sex_tab_regular", False)]
            add "free_roam_maia_op3"
            text "Back": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

default yuuhi_sex_times = 1

default is_yuuhi_talk = False
default yuuhi_sex_tab_regular = False
screen is_yuuhi():
    modal True
    if all_options:
        add "is_diana_choices_main"
        
        button:
            focus_mask True
            action [SetVariable("is_yuuhi_talk", True), SetVariable("all_options", False)]
            add "free_roam_maia_op1"
            text "Talk": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
        
        if mc_harem_yuuhi:
            if not yuuhi_harem_training_finished:
                if not yuuhi_sex_times <= 0:
                    button:
                        focus_mask True
                        action Jump("yuuhi_harem_training")
                        add "free_roam_maia_op2"
                        text "Sex": 
                            size persistent.free_roam_choices_text_size color "#cf436b" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
                else:
                    button:
                        focus_mask True
                        action Jump("is_yuuhi_sex_limit")
                        add "free_roam_maia_op2"
                        text "Sex": 
                            size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

            elif yuuhi_harem_training_finished:
                button:
                    focus_mask True
                    action [SetVariable("yuuhi_sex_tab_regular", True), SetVariable("all_options", False)]
                    add "free_roam_maia_op2"
                    text "Sex": 
                        size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        else:
            button:
                focus_mask True
                action Jump("yuuhi_sex_not_harem")
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("free_roam_main_label")
            add "free_roam_maia_op3"
            text "Leave": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

    if is_yuuhi_talk:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
            action Jump("is_yuuhi_talk_op4")
        text "\"What do you think about me?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 

        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [SetVariable("yuuhi_talk_choice4", True), SetVariable("yuuhi_talk_choice2", False), SetVariable("yuuhi_talk_choice3", False), SetVariable("yuuhi_talk_choice1", False), SetVariable("yuuhi_talk_choice5", False), Jump("is_yuuhi_talk")]
        text "\"How is your pregnancy?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("yuuhi_talk_choice1", True), SetVariable("yuuhi_talk_choice2", False), SetVariable("yuuhi_talk_choice3", False), SetVariable("yuuhi_talk_choice4", False), SetVariable("yuuhi_talk_choice5", False), Jump("is_yuuhi_talk")]
        text "\"How are you doing?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("yuuhi_talk_choice2", True), SetVariable("yuuhi_talk_choice1", False), SetVariable("yuuhi_talk_choice3", False), SetVariable("yuuhi_talk_choice4", False), SetVariable("yuuhi_talk_choice5", False), Jump("is_yuuhi_talk")]
        text "\"I want to know more about you.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
        
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("yuuhi_talk_choice3", True), SetVariable("yuuhi_talk_choice2", False), SetVariable("yuuhi_talk_choice1", False), SetVariable("yuuhi_talk_choice4", False), SetVariable("yuuhi_talk_choice5", False), Jump("is_yuuhi_talk")]
        text "Talk about Maia":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action [SetVariable("yuuhi_talk_choice5", False), SetVariable("yuuhi_talk_choice2", False), SetVariable("yuuhi_talk_choice3", False), SetVariable("yuuhi_talk_choice4", False), SetVariable("yuuhi_talk_choice1", False), SetVariable("is_yuuhi_talk", False), SetVariable("all_options", True)]
        text "Back":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True
    
    if yuuhi_sex_tab_regular:
        add "is_yuuhi_sec_regular_main"

        button:
            focus_mask True
            action Jump("is_yuuhi_hj1")
            add "free_roam_maia_op1"
            text "Handjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_yuuhi_bj1")
            add "free_roam_maia_op2"
            text "Blowjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_yuuhi_asex1")
            add "free_roam_maia_op3"
            text "Sex": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
        
        button:
            focus_mask True
            action Jump("is_yuuhi_fj1")
            add "free_roam_maia_op4"
            text "Footjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 793 xanchor 0.5 yanchor 0.5
            
        button:
            focus_mask True
            action [SetVariable("yuuhi_sex_tab_regular", False), SetVariable("all_options", True)]
            add "free_roam_maia_op5"
            text "Back": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 931 xanchor 0.5 yanchor 0.5 


default is_diana_talk = False
default diana_sex_tab = False
default diana_sex_tab_regular = False
default diana_sex_tab_clothing = False


default diana_tj_price = "1 Bronze Coin"
default diana_bj_price = "2 Bronze Coins"
default diana_vsex_price = "4 Bronze Coins"
default diana_asex_price = "6 Bronze Coins"

default diana_rtop_price = "2 Bronze Coins"
default diana_rall_price = "4 Bronze \nCoins"
default diana_plug_price = "1 Silver Coin"

screen is_diana():
    modal True
    if all_options:

        if mc_harem_diana or mc_friend_diana:
            add "is_diana_choices_main2"
        else: 
            add "is_diana_choices_main"
        
        if mc_harem_diana or mc_friend_diana:
            if not brothel_coin == 0:
                button:
                    focus_mask True
                    action Jump("is_diana_buy_brothel")
                    add "free_roam_maia_op3"
                    text "Buy the Brothel": 
                        size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action [SetVariable("is_diana_talk", True), SetVariable("all_options", False)]
            add "free_roam_maia_op1"
            text "Talk": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5

        if is_diana_sex_limit <= 0:
            button:
                focus_mask True
                action Jump("is_diana_sex_limit")
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
        else:
            button:
                focus_mask True
                action [SetVariable("diana_sex_tab_regular", True), SetVariable("all_options", False)]
                add "free_roam_maia_op2"
                text "Sex": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        if mc_harem_diana or mc_friend_diana:
            button:
                focus_mask True
                action Jump("free_roam_main_label")
                add "free_roam_maia_op4"
                text "Leave": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 795 xanchor 0.5 yanchor 0.5
        else:
            button:
                focus_mask True
                action Jump("free_roam_main_label")
                add "free_roam_maia_op3"
                text "Leave": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
        
    if is_diana_talk:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("is_diana_talk_pregnant")
        text "\"How's your pregnancy?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("diana_talk_choice1", True), SetVariable("diana_talk_choice2", False), SetVariable("diana_talk_choice3", False), SetVariable("diana_talk_choice4", False), SetVariable("diana_talk_choice5", False), Jump("is_diana_talk")]
        text "\"How are you doing?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("diana_talk_choice2", True), SetVariable("diana_talk_choice1", False), SetVariable("diana_talk_choice3", False), SetVariable("diana_talk_choice4", False), SetVariable("diana_talk_choice5", False), Jump("is_diana_talk")]
        text "\"Do you need something?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("diana_talk_choice5", False), SetVariable("diana_talk_choice2", False), SetVariable("diana_talk_choice3", False), SetVariable("diana_talk_choice4", False), SetVariable("diana_talk_choice1", False), SetVariable("is_diana_talk", False), SetVariable("all_options", True)]
        text "Back":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True 

    if diana_sex_tab_regular:
        add "is_diana_sex_choices_main"

        button:
            focus_mask True
            action Jump("is_diana_tj1")
            add "free_roam_maia_op1"
            text "Titjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_diana_bj1")
            add "free_roam_maia_op2"
            text "Blowjob": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_diana_vsex1")
            add "free_roam_maia_op3"
            text "Vaginal Sex": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 650 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action Jump("is_diana_asex1")
            add "free_roam_maia_op4"
            text "Anal Sex": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 791 xanchor 0.5 yanchor 0.5

        button:
            focus_mask True
            action [SetVariable("diana_sex_tab_regular", False), SetVariable("all_options", True)]
            add "free_roam_maia_op5"
            text "Back": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 929 xanchor 0.5 yanchor 0.5 

        
        text "[diana_tj_price]" size 30 color "#FFFFFF" xpos 0.62 ypos 0.25 font "Lora-VariableFont_wght.ttf"
        text "[diana_bj_price]" size 30 color "#FFFFFF" xpos 0.62 ypos 0.345 font "Lora-VariableFont_wght.ttf"
        text "[diana_vsex_price]" size 30 color "#FFFFFF" xpos 0.62 ypos 0.44 font "Lora-VariableFont_wght.ttf"
        text "[diana_asex_price]" size 30 color "#FFFFFF" xpos 0.62 ypos 0.533 font "Lora-VariableFont_wght.ttf"

screen getfour_diff():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("maia_getfour_easy")
    text "\"Go easy on me.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("maia_getfour_hard")
    text "\"Don't hold back!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default guild_strength = 43
default guild_strength_change = ""
screen guild_strength():
    add "guild_strength"

    text "Guild strength: [guild_strength]" size persistent.dialogue_text_size color "#cf436b" xpos 0.833 ypos 0.172 font "Lora-VariableFont_wght.ttf"

screen guild_strength_change():
    text "[guild_strength_change]" size persistent.dialogue_text_size color "#FFFFFF" xpos 0.957 ypos 0.12 font "Lora-VariableFont_wght.ttf"

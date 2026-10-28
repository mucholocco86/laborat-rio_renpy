screen stat_change():
    if karma_more:
        add "karma_more"
    elif karma_less:
        add "karma_less"

transform fade_in:
    alpha 0.0
    linear 1.0 alpha 1.0
    
screen freeroam_edit1():
    text "3 Days until the armor is ready" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("free_roam_maia_freeroam_edit1")
    text "Return to the castle":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("free_roam_diana")
    text "Visit the brothel":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("free_roam_yuuhi")
    text "Visit Yuuhi":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen bonus_scene1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("bonus_scene1")
    text "\"I'm still not finished.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "{i}Get the cloth":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default bonus_scene1_vaginal = False
default bonus_scene1_anal = False
default bonus_scene1_pov = False

screen bonus_scene1_sex0():
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("bonus_scene1_vaginal")
    text "Vaginal":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("bonus_scene1_anal")
    text "Anal":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen bonus_scene1_sex():
    if not bonus_scene1_pov:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("bonus_scene1_pov")
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        if bonus_scene1_vaginal:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("bonus_scene1_vaginal")
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("bonus_scene1_anal")
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not bonus_scene1_vaginal:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("bonus_scene1_vaginal")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
        add "main_choices_op3_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    else:
        add "main_choices_op2_idle"
        text "Vaginal":
            size persistent.choices_text_size color "818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
            
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("bonus_scene1_anal")
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("bonus_scene1_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen irda_city_map():
    add "irda_city_map2"
    
screen scene2_choice1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene2_choice1_lie")
    text "Lie":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene2_choice1_truth")
    text "Tell the truth":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene02_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene02_choice02_op1")
    text "\"Single.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene02_choice02_op2")
    text "\"Married.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene02_choice02_op3")
    text "\"Divorced.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen s02_hover_areas():
    add "2_s9_axe_hover"
    add "2_s9_ogre_hover"
    add "2_s9_cage_hover"

screen scene02_search():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s02_hover_areas")
        ]
        unhovered [
            Hide("s02_hover_areas")
        ]

    modal True 
    imagebutton auto "2_s9_ogre_%s":
        focus_mask True
        action Jump("scene02_search_ogre")

    imagebutton auto "2_s9_axe_%s":
        focus_mask True
        action Jump("scene02_search_axe")
    
    imagebutton auto "2_s9_cage_%s":
        focus_mask True
        action Jump("scene02_search_cage")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene03")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene04_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice02_peek")
    text "Take a peek":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice02_intro")
    text "Introduce yourself":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5  italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene04_choice02_nothing")
    text "Stay silent":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene04_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice03_refuse")
    text "Refuse the offer":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Follow her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    
default scene04_choice05_talked = False
screen scene04_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice00_ask1")
    text "\"Tell me about the Queen.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice00_ask2")
    text "\"You sounded racist towards that elf.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene04_choice00_ask3")
    text "\"The streets were really quiet.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    if scene04_choice05_talked:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene04_choice00_c")
        text "\"That's all I needed to know for now.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

default free_roam_arrows = True
screen scene04_free_roam1():
    key "K_UP" action Jump("scene04_free_roam1_up")
    key "K_LEFT" action Jump("scene04_free_roam1_left")
    key "K_RIGHT" action Jump("scene04_free_roam1_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 

        
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam1_up")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam1_left")

        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam1_right")

screen scene04_free_roam2():
    key "K_UP" action Jump("scene04_free_raom_end0")
    key "K_DOWN" action Jump("scene04_free_roam3_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_raom_end0")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam3_down")

default scene04_free_roam_coin = True
default scene04_free_roam_poster = True

screen scene04_free_roam3():
    key "K_DOWN" action Jump("scene04_free_roam3_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene04_free_roam_coin:
        imagebutton auto "scene04_coin_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam_coin")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam3_down")

screen scene04_free_roam4():
    key "K_UP" action Jump("scene04_free_roam4_up")
    key "K_LEFT" action Jump("scene04_free_roam4_left")
    key "K_RIGHT" action Jump("scene04_free_roam4_right")
    key "K_DOWN" action Jump("scene04_free_roam3_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
        
    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam4_up")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam4_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam4_right")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam3_down")

screen scene04_free_roam5():
    key "K_DOWN" action Jump("scene04_free_roam5_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam5_down")

screen scene04_free_roam6():
    key "K_DOWN" action Jump("scene04_free_roam5_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene04_free_roam_poster:
        imagebutton auto "scene04_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene04_free_roam5_down")

screen scene04_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Return()
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene04_free_roam_end")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5
        
screen scene04_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice06_op2")
    text "\"I'll help you out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice06_op3")
    text "\"Sorry, this sounds too risky.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene04_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice08_bj")
    text "\"I'm still not satisfied...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"That's enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene04_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"I'd rather get some rest.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice09_op2")
    text "\"I'm fine. No need to worry.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene04_choice10():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice10_tits")
    text "\"Breasts.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice10_ass")
    text "\"Ass.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene04_choice10_feet")
    text "\"Feet.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene04_choice10_personality")
    text "\"Personality.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

screen scene04_choice11():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice07_pussy")
    text "\"Show me your pussy.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice07_tits")
    text "\"Show me your breasts.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Return()
    text "\"I don't need anything in return.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

screen scene04_choice08_2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene04_choice08_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene04_choice08_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene05_choice01():
    #text "Diana: Like what you see?" size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 1 ypos 1 

    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_choice01_yes")
    text "\"I do.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene05_choice01_small")
    text "\"I like them bigger.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen s05_hover_areas():
    add "scene05_is01_face_hover"
    add "scene05_is01_leftbob_hover"
    add "scene05_is01_rightbob_hover"

screen scene05_is01():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s05_hover_areas")
        ]
        unhovered [
            Hide("s05_hover_areas")
        ]

    imagebutton auto "scene05_is01_face_%s":
        focus_mask True
        action Jump("scene05_is01_face")

    imagebutton auto "scene05_is01_leftbob_%s":
        focus_mask True
        action Jump("scene05_is01_leftbob")
    
    imagebutton auto "scene05_is01_rightbob_%s":
        focus_mask True
        action Jump("scene05_is01_rightbob")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_is01_continue")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True


screen scene05_tutorial():

    add "interaction_tutorial"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Jump("scene05_choice01_yes2")

screen scene04_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_tj3")
    text "\"Yes!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene05_no_rimming")
    text "\"Hell no!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene05_choice02_enablebuttons = True
default scene05_choice02_cumbuttons = False
screen scene05_choice02():
    if scene05_no_rimming:
        if scene05_choice02_enablebuttons:
            imagebutton auto "scene05_choice02_hj_%s":
                focus_mask True
                action Jump("scene05_choice02_hj")
        
            imagebutton auto "scene05_choice02_hjballs_%s":
                focus_mask True
                action Jump("scene05_choice02_hjballs")
        
            imagebutton auto "scene05_choice02_tj_%s":
                focus_mask True
                action Jump("scene05_choice02_tj")
              
            imagebutton auto "scene05_choice02_cum_%s":
                focus_mask True
                action [SetVariable("scene05_choice02_cumbuttons", True), SetVariable("scene05_choice02_enablebuttons", False)]

        if scene05_choice02_cumbuttons:
            imagebutton auto "scene05_choice02_cumtj_%s":
                focus_mask True
                action Jump("scene05_choice02_tj_cum")

    else:
        if scene05_choice02_enablebuttons:
            imagebutton auto "scene05_choice02_hj_%s":
                focus_mask True
                action Jump("scene05_choice02_hj")
        
            imagebutton auto "scene05_choice02_hjballs_%s":
                focus_mask True
                action Jump("scene05_choice02_hjballs")
        
            imagebutton auto "scene05_choice02_tj_%s":
                focus_mask True
                action Jump("scene05_choice02_tj")
        
            imagebutton auto "scene05_choice02_rtj_%s":
                focus_mask True
                action Jump("scene05_choice02_rtj")
        
            imagebutton auto "scene05_choice02_cum_%s":
                focus_mask True
                action [SetVariable("scene05_choice02_cumbuttons", True), SetVariable("scene05_choice02_enablebuttons", False)]

        if scene05_choice02_cumbuttons:
            imagebutton auto "scene05_choice02_cumtj_%s":
                focus_mask True
                action Jump("scene05_choice02_tj_cum")
        
            imagebutton auto "scene05_choice02_cumrtj_%s":
                focus_mask True
                action Jump("scene05_choice02_rtj_cum")

screen scene05_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_tj2")
    text "Titjob":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_diana_bj_before")
    text "Blowjob":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_diana_vsex_before")
    text "Vaginal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_diana_asex2_before")
    text "Anal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene05_choice04():
    if scene05_choice02_enablebuttons:        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_diana_tj_sitting")
        text "Titjob 1":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("is_diana_tj_lying")
        text "Titjob 2.":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("is_diana_tj_reverse")
        text "Titjob 3 (Rimming).":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action Jump("scene05_choice02_tj_cum")
        text "Cum": 
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene05_choice02_hj():
    imagebutton auto "scene05_choice02_faster_%s":
        focus_mask True
        action Jump("scene05_hj_fast")
    
    imagebutton auto "scene05_choice02_slower_%s":
        focus_mask True
        action Jump("scene05_hj_slow")
    
    imagebutton auto "scene05_choice02_continue_%s":
        focus_mask True
        action Jump("scene05_tj")

screen scene05_choice02_tj():
    imagebutton auto "scene05_choice02_faster_%s":
        focus_mask True
        action Jump("scene05_tj_fast")
    
    imagebutton auto "scene05_choice02_slower_%s":
        focus_mask True
        action Jump("scene05_tj_slow")
    
    imagebutton auto "scene05_choice02_cum_%s":
        focus_mask True
        action Jump("scene05_tj_cum")

screen scene05_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_choice05_op1")
    text "\"Do your thing.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene05_choice05_op2")
    text "\"You're really beautiful, Diana.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

screen scene05_choice06():
    imagebutton auto "scene05_choice06_op1_%s":
        focus_mask True
        action Jump("scene05_choice06_op1")

    imagebutton auto "scene05_choice06_op2_%s":
        focus_mask True
        action Jump("scene05_choice06_op2")

screen scene05_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_choice07_op1")
    text "\"That's not leeching. That's surviving.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene05_choice07_op2")
    text "Pull her closer":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene05_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_choice08_op1")
    text "{i}Let her in":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"No. Please go away.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene05_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_choice09_op1")
    text "{i}Request her services":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene05_choice09_op2")
    text "{i}Let her leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

screen scene05_choice10():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene05_choice09_op3")
    text "\"Goodnight, Diana.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene05_choice10_op2")
    text "\"You're really beautiful. I regret not meeting you sooner.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600

#SCENE7 FREE ROAM ############################################################################################################
default scene07_free_roam_coin = True
default scene07_free_roam_poster = True
screen scene07_free_roam1():
    key "K_UP" action Jump("scene07_free_roam1_up")
    key "K_LEFT" action Jump("scene07_free_roam1_left")
    key "K_RIGHT" action Jump("scene07_free_roam1_right")
    key "K_DOWN" action Jump("scene07_free_roam_end")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam1_up")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam1_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam1_right")
        
        imagebutton auto "free_roam_end2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam_end")

screen scene07_free_roam1_right():
    key "K_DOWN" action Jump("scene07_free_roam")

    if scene07_free_roam_coin:
        imagebutton auto "scene07_coin_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam_coin")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam")
        
screen scene07_free_roam1_left():
    key "K_DOWN" action Jump("scene07_free_roam")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam")

screen scene07_free_roam1_up():
    key "K_RIGHT" action Jump("scene07_free_roam2_right")
    key "K_DOWN" action Jump("scene07_free_roam")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam2_right")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam")

screen scene07_free_roam2_right():
    key "K_DOWN" action Jump("scene07_free_roam1_up")

    if scene07_free_roam_poster:
        imagebutton auto "scene07_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam_poster")
    
    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
        
    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene07_free_roam1_up")

screen scene07_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Return()
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene07_continue")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5

screen scene07_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene07_choice01_op1")
    text "\"Lovers.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene07_choice01_op2")
    text "\"Friends.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene07_choice01_op3")
    text "\"Nothing.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene08_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene08_choice01_op1_nope")
    text "\"I want to wed the princess too!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene08_choice01_op2")
    text "\"It's nothing...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene09_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene09_choice01_grab")
    text "Grab her breast":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Let her talk":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene09_choice0():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene09_choice0_op1")
    text "Tease her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene09_choice0_op2")
    text "\"Let's go.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene09_choice00():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene09_choice00_op2")
    text "\"Wait for me outside.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene09_choice00_op1")
    text "\"Get in.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default lookatface = True
default lookatchest = False
default lookathip = False
default showtongue = False
default test_throat = False
default spreadpussy = False
default mastur01_first = True
screen scene10_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("lookatface", True), SetVariable("lookatchest", False), SetVariable("lookathip", False), SetVariable("showtongue", False), SetVariable("test_throat", False), Jump("scene10_choice01_lookatface")]
    text "Look at face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    if lookatface:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action [SetVariable("showtongue", True), Jump("scene10_choice01_showmouth")]
        text "\"Open your mouth.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5
        
        if showtongue:
            imagebutton auto "main_choices_left_op2_%s":
                focus_mask True
                action [SetVariable("test_throat", True), Jump("scene10_choice01_showtongue")]
            text "\"Show me your tongue.\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5

            if test_throat:
                imagebutton auto "main_choices_left_op3_%s":
                    focus_mask True
                    action Jump("scene10_choice01_testthroat")
                text "Test her throat":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("lookatface", False), SetVariable("lookatchest", True), SetVariable("lookathip", False), Jump("scene10_choice01_lookatchest")]
    text "Look at chest":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    if lookatchest:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action Jump("scene10_choice01_playnips")
        text "\"Play with your nipples.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action [SetVariable("lookatface", False), SetVariable("lookatchest", False), SetVariable("lookathip", True), SetVariable("spreadpussy", False), Jump("scene10_choice01_lookathip")]
    text "Look at hip":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

    if lookathip:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action [SetVariable("spreadpussy", True), Jump("scene10_choice01_spreadpussy")]
        text "\"Spread your pussy.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5

        if spreadpussy:
            imagebutton auto "main_choices_left_op2_%s":
                focus_mask True
                action Jump("scene10_choice01_pee")
            text "\"Do you feel like taking a piss?\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

            imagebutton auto "main_choices_left_op3_%s":
                focus_mask True
                action Jump("scene10_choice01_lookanus")
            text "Look at her anus":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            
            if mastur01_first:
                imagebutton auto "main_choices_left_op4_%s":
                    focus_mask True
                    action [SetVariable("mastur01_first", False), Jump("scene10_choice01_mastur")]
                text "\"Can you show me how you masturbate?\"":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

            else:
                imagebutton auto "main_choices_left_op4_%s":
                    focus_mask True
                    action Jump("scene10_choice01_mastur_second")
                text "\"Start masturbating again.\"":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene10_choice01_finish")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True


screen scene09_choice000():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene09_choice000_op1")
    text "Put them in their place":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene09_choice000_op2")
    text "Play along":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene10_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene10_choice02_yes")
    text "\"I do.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene10_choice02_likeass")
    text "\"I like your cute butt more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene10_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene10_choice03_cum")
    text "\"Cum!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene10_choice03_stop")
    text "\"Stop.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene10_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene10_choice01_mastur_second_cum")
    text "\"Go ahead.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene10_choice01_mastur_second_notyet")
    text "\"Not yet.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene11_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene11_choice01_slap")
    text "Spank her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene12")
    text "Do nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene12_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene12_choice01_op1")
    text "Take a peak":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene13_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene13_choice01_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene13_choice01_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene13_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene13_choice04_op1")
    text "Offer to help":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene13_choice04_op2")
    text "\"Sounds tough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene13_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene13_choice05_op1")
    text "Cover her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene13_choice05_op2")
    text "Take a peek":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene13_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene13_choice02_vaginal")
    text "Vaginal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene13_choice02_anal")
    text "Anal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene13_choice03_firsttime = True
default scene13_choice03_enablebuttons = True
default scene13_choice03_cumbuttons = False
default scene13_choice03_inside = False
default scene13_choice03_outside = False

screen scene13_choice03():
    if scene13_choice03_enablebuttons:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene13_choice03_vaginal")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            
        if scene13_choice03_firsttime:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action [SetVariable("scene13_choice03_firsttime", False), Jump("scene13_choice03_anal")]
            text "Anal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene13_choice03_analtwo")
            text "Anal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    if not scene13_choice03_cumbuttons:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("scene13_choice03_cumbuttons", True), SetVariable("scene13_choice03_enablebuttons", False)]
        text "Cum":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if scene13_choice03_cumbuttons:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [SetVariable("scene13_choice03_inside", True), Jump("scene13_climax")]
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("scene13_choice03_outside", True), Jump("scene13_climax")]
        text "Cum outside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene13_choice04_enablebuttons = True
default scene14_choice04_switch = False
default scene14_choice04_switch2 = False
screen scene13_choice04():
    if scene13_choice04_enablebuttons:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
            action Jump("scene13_choice04_bj")
        text "Blowjob":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene13_choice04_glans")
        text "Glans licking":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("scene14_choice04_switch", True), SetVariable("scene13_choice04_enablebuttons", False)]
        text "Doggystyle":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene13_choice04_m")
        text "Missionary":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("scene14_choice04_switch2", True), SetVariable("scene13_choice04_enablebuttons", False)]
        text "Tabletop doggystyle":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action Jump("scene14")
        text "\"That's enough!\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5
        
    if scene14_choice04_switch:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene13_choice04_ds_vaj")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene13_choice04_ds_anal")
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    elif scene14_choice04_switch2:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene13_choice04_tds_vaj")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene13_choice04_tds_anal")
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if bonus_scene2:
        if bonus_scene2_handjob2:
            imagebutton auto "main_choices_left_op1_%s":
                focus_mask True
                action Jump("bonus_scene2_handjob")
            text "Handjob":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_left_op1_%s":
                focus_mask True
                action Jump("bonus_scene2_handjob2")
            text "Handjob 2":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("bonus_scene2_thighjob")
        text "Thighjob":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    if bonus_scene2_cum_first:
        imagebutton auto "main_choices_left_op3_%s":
            focus_mask True
            action Jump("bonus_scene2_cum")
        text "Cum":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True


screen scene14_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene14_choice01_peek")
    text "Take a peek":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene14_choice01_bow")
    text "Bow":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene14_choice02():
    imagebutton auto "scene14_choice02_op1_%s":
        focus_mask True
        action Jump("scene14_choice02_op1")

    imagebutton auto "scene14_choice02_op2_%s":
        focus_mask True
        action Jump("scene14_choice02_op2")

screen scene14_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene14_choice03_op1")
    text "Kill her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Supress impulsive thought":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True


screen scene14_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene14_choice04_op1")
    text "\"That's right. I want you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene14_choice04_op2")
    text "\"That's not true.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene14_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene14_choice05_op1")
    text "Ask her on a date":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene14_choice05_op2")
    text "\"I have to leave now, princess.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene16_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene16_choice01_op1")
    text "\"You need to be punished.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene16_choice01_op2")
    text "\"It's fine.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene16_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene16_choice02_op1")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene16_choice02_op2")
    text "\"I'm too tired right now...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene16_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene16_choice03_op1")
    text "\"You need to calm down, Maia.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene16_choice03_op2")
    text "Tease her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene17_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene17_choice01_spank")
    text "Spank":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene17_choice01_fanus")
    text "Finger her anus":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene17_choice01_fpussy")
    text "Finger her pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene17_continue")
    text "\"That's enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene17_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene17_choice01_fanus_stop")
    text "Stop":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene17_choice01_fanus_keep")
    text "Keep fingering":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene17_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene17_choice03_apologize")
    text "\"I'm sorry, Maia. I didn't mean to go so hard.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene17_choice03_go")
    text "\"You can go now.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    
screen scene18_ending_screen():
    add "ending_screen"
    imagebutton auto "ending_screen_continue_%s":
        focus_mask True
        action Return()

screen scene18_choice_maia():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene18_choice_maia_op1")
    text "\"No. Rebecca is just a one time thing.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene18_choice_maia_op2")
    text "\"Yes. There might be more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene18_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Get up":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

default scene18_coin = True
default scene18_poster = True

screen scene18_free_roam():
    key "K_LEFT" action Jump("scene18_free_roam_left")
    key "K_RIGHT" action Jump("scene18_free_roam_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_right")

screen scene18_free_roam_right():
    key "K_UP" action Jump("scene18_free_roam_up")
    key "K_DOWN" action Jump("scene18_free_roam_main_0")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_up")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_main_0")

screen scene18_free_roam_up():
    key "K_DOWN" action Jump("scene18_free_roam_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene18_poster:
        imagebutton auto "scene18_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_right")

screen scene18_free_roam_up2():
    key "K_UP" action Jump("scene18_free_roam_up2")
    key "K_DOWN" action Jump("scene18_free_roam_main_0")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_up2")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_main_0")
        
        imagebutton auto "free_roam_end2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene14_0")

screen scene18_free_roam_up3():
    key "K_UP" action Jump("scene18_free_roam_maia")
    key "K_DOWN" action Jump("scene18_free_roam_left")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene18_coin:
        imagebutton auto "scene18_coin_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_coin")

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_maia")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene18_free_roam_left")

screen scene18_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Return()
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene19")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5
        
screen scene19_choice01():
    add "irda_city_map1"

screen scene20_choice01():
    if not mc_talked_orym:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene20_choice01_op1")
        text "Approach the elven man":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Approach the elven man":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    if not mc_talked_kat_first:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene20_choice01_op2")
        text "Approach the two girls":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Approach the two girls":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    if not mc_talked_gaius:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene20_choice01_op3")
        text "Approach the armored man":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Approach the armored man":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene21")
    text "Approach Eireen, the guild mistress":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
screen warning_screen():
    tag menu
    text "Warning":
        size 50 color "#ff0000" font "candara_bold.ttf" xpos 1275 ypos 560 xanchor 0.5 yanchor 0.5

    text "This game is intended for audiences who are 18 or older. Select \"I'm 18+\" to continue.":
        size 50 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1200

    imagebutton auto "warning_screen_continue_%s":
        focus_mask True
        action Return()
    text "I'm 18+":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 885 xanchor 0.5 yanchor 0.5

screen tutorial_screen_start():
    tag menu
    add "17_s28"  

    imagebutton auto "17_s28_continue_%s":
        focus_mask True
        action Return()  

screen scene_maia_sleep1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_maia_night")
    text "Masturbate":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("free_roam_sleep")
    text "Sleep":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default tutorial_dashboard = True
screen gameplay_map_tutorial():
    if tutorial_dashboard:
        add "19_s9"
        imagebutton auto "map_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Map")
            unhovered SetVariable("screen_tooltip", "")
            action [SetVariable("map_screen_open", True), SetVariable("tutorial_dashboard", False)]
    
    if map_screen_open:
        add "irda_map_screen"
        imagebutton auto "irda_castle_%s":
                focus_mask True
                #action Jump("queen_call")

        if quest1_queen_talkq_speakToDarius:
            imagebutton auto "irda_guild_%s":
                focus_mask True
                action Jump("scene20")

        if quest1_queen_talkq_speakToDarius:
            imagebutton auto "irda_blacksmith_%s":
                focus_mask True
                #action Jump("queen_call")

        imagebutton auto "irda_brothel_%s":
                focus_mask True
                #action Jump("queen_call")
        
        imagebutton auto "irda_guardpost_%s":
                focus_mask True
                #action Jump("queen_call")
        
        imagebutton auto "irda_barn_%s":
                focus_mask True
                #action Jump("queen_call")

        imagebutton auto "irda_map_screen_close_%s":
                focus_mask True
                #action [SetVariable("map_screen_open", False)] 

default tutorial_dashboard2 = True
screen gameplay_map_tutorial2():
        add "irda_map_screen"

        imagebutton auto "irda_castle_%s":
            focus_mask True
            #action Jump("queen_call")

        imagebutton auto "irda_guild_%s":
            focus_mask True
            #action Jump("scene22")

        imagebutton auto "irda_blacksmith_%s":
            focus_mask True
            action Return()

        imagebutton auto "irda_brothel_%s":
            focus_mask True
            #action Jump("queen_call")
        
        imagebutton auto "irda_guardpost_%s":
            focus_mask True
            #action Jump("queen_call")
        
        imagebutton auto "irda_barn_%s":
            focus_mask True
            #action Jump("queen_call")

        imagebutton auto "irda_map_screen_close_%s":
            focus_mask True
            #action [SetVariable("map_screen_open", False)] 

default yuuhi_saw_choice = False
screen scene22_choice01():
    imagebutton auto "scene22_choice01_angry_%s":
        focus_mask True
        action Jump("scene22_choice01_angry")
    
    imagebutton auto "scene22_choice01_funny_%s":
        focus_mask True
        action Jump("scene22_choice01_funny")

screen scene23_choice01():
    imagebutton auto "scene23_choice01_sure_%s":
        focus_mask True
        action Jump("scene23_choice01_sure")
    
    imagebutton auto "scene23_choice01_busy_%s":
        focus_mask True
        action Jump("scene23_choice01_busy")

screen scene23_choice02():
    imagebutton auto "scene23_choice02_op1_%s":
        focus_mask True
        action Return()

    imagebutton auto "scene23_choice02_op2_%s":
        focus_mask True
        action Jump("scene23_choice02_op2")

screen scene23_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene23_choice03_op1")
    text "Keep pants on":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene23_choice03_op2")
    text "Take off pants":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene24_tutorial():
    add "24_s19"
    imagebutton auto "24_s19_continue_%s":
        focus_mask True
        action Return()

screen s24_hover_areas1():
    add "24_s2_rightbob_hover"
    add "24_s2_leftbob_hover"

screen s24_hover_areas2():
    add "24_s12_feet_hover"

screen scene24_choice01():
    #big fucking mess
    if not yuuhi_lookchest:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [SetVariable("yuuhi_lookchest", True), SetVariable("yuuhi_lookass", False), SetVariable("yuuhi_lookfeet", False), SetVariable("yuuhi_feettouch_first", False), SetVariable("yuuhi_touchedfoot", False), SetVariable("start_wiggle", False), Jump("scene24_choice01_lookchest")]
        text "Look at breasts":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op1_idle"
        text "Look at breasts":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not yuuhi_lookass:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action [SetVariable("yuuhi_lookchest", False), SetVariable("yuuhi_lookass", True), SetVariable("yuuhi_lookfeet", False), SetVariable("yuuhi_feettouch_first", False), SetVariable("yuuhi_touchedfoot", False), SetVariable("start_wiggle", False), Jump("scene24_choice01_lookass")]
        text "Look at ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Look at ass":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not yuuhi_lookfeet:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("yuuhi_lookchest", False), SetVariable("yuuhi_lookass", False), SetVariable("yuuhi_lookfeet", True), SetVariable("yuuhi_feettouch_first", True), SetVariable("start_wiggle", False), Jump("scene24_choice01_lookfeet")]
        text "Look at feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Look at feet":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if yuuhi_lookchest:
        imagebutton:
            idle "interact_indicator_idle"
            hover "interact_indicator_hover"
            focus_mask True
            action NullAction()
            hovered [
                Show("s24_hover_areas1")
            ]
            unhovered [
                Hide("s24_hover_areas1")
            ]

        imagebutton auto "24_s2_rightbob_%s":
            focus_mask True
            action Jump("scene24_rightbob")

        imagebutton auto "24_s2_leftbob_%s":
            focus_mask True
            action Jump("scene24_leftbob")
    
    if yuuhi_lookass:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action Jump("scene24_choice03_anus")
        text "Finger anus":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("scene24_choice03_pussy")
        text "Finger pussy":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if yuuhi_lookfeet:
        imagebutton:
            idle "interact_indicator_idle"
            hover "interact_indicator_hover"
            focus_mask True
            action NullAction()
            hovered [
                Show("s24_hover_areas2")
            ]
            unhovered [
                Hide("s24_hover_areas2")
            ]

        if yuuhi_feettouch_first:
            imagebutton auto "24_s12_feet_%s":
                focus_mask True
                action [SetVariable("yuuhi_touchedfoot", True), SetVariable("yuuhi_feettouch_first", False), Jump("scene24_feet")]
            
            imagebutton auto "main_choices_left_op1_%s":
                focus_mask True
                action [SetVariable("yuuhi_feettouch_first", False), SetVariable("start_wiggle", True), SetVariable("yuuhi_feettouch_first", False), Jump("scene24_wiggle")]
            text "\"Wiggle your toes.\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5

    if start_wiggle:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action [SetVariable("start_wiggle", False), SetVariable("yuuhi_feettouch_first", True), Jump("scene24_choice01_lookfeet")]
        text "\"Stop.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5
        
    if yuuhi_touchedfoot:
        imagebutton auto "24_s13_feet_%s":
            focus_mask True
            action [SetVariable("yuuhi_feettouch_first", True), SetVariable("yuuhi_touchedfoot", False), Jump("scene24_choice01_lookfeet")]

        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action [SetVariable("yuuhi_touchedfoot", False), Jump("scene24_lick")]
        text "Lick foot":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if yuuhi_saw_choice:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene25")
        text "\"That's enough.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

default scene24_choice02_already = False
default scene24_choice02_harem = False
default scene24_choice02_dont = False

screen scene24_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene24_choice02_op1")
    text "Tell her about Maia":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene24_choice02_op2")
    text "\"Why do you want to get married?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene24_choice02_op4")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen harem_tutorial01():
    add "24_s21"
    imagebutton auto "24_s21_continue_%s":
        focus_mask True
        action Return()

screen scene25_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene25_choice01_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene25_choice01_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene25_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene25_choice02_swallow", True), Jump("scene25_choice01_inside2")] 
    text "\"Swallow it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene25_choice02_spit", True), Jump("scene25_choice01_inside2")] 
    text "\"You can spit it out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene26_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene26_choice01_refuse", True), Return()] 
    text "\"I don't want any animals in my room.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene26_choice01_accept", True), Return()] 
    text "\"Sure, I don't mind.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene26_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene26_choice02_accept", True), Return()] 
    text "\"Fine... But you better keep an eye on him.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene26_choice02_refuse", True), Return()] 
    text "\"I said no.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene26_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene26_choice03_sex", True), Return()] 
    text "\"Let's get some sleep.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene26_choice03_smile", True), Return()] 
    text "\"I want to see your smile.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene26_choice04():
    imagebutton auto "scene26_choice04_sex_%s":
        focus_mask True
        action [SetVariable("scene26_choice04_sex", True), Return()] 
    
    imagebutton auto "scene26_choice04_busy_%s":
        focus_mask True
        action [SetVariable("scene26_choice04_busy", True), Return()] 

default scene27_all_options = True
default scene27_suck = True
default scene27_deep = True
default scene27_choose_cumsuck = False
default scene27_choose_cumdeep = False

screen scene27_sex():
    if scene27_all_options:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene27_sex_kiss")
        text "\"Kiss it.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene27_sex_lick")
        text "\"Lick it.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    if scene27_suck:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("scene27_suck", False), Jump("scene27_sex_suck")]
        text "\"Suck it.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("scene27_all_options", False), SetVariable("scene27_cum_options", True), SetVariable("scene27_choose_cumsuck", True), SetVariable("scene27_choose_cumdeep", False), Jump("scene27_cum_options")]
        text "Cum in mouth":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if scene27_deep:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("scene27_deep", False), Jump("scene27_sex_deep")]
        text "Deepthroat":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("scene27_all_options", False), SetVariable("scene27_cum_options", True), SetVariable("scene27_choose_cumdeep", True), SetVariable("scene27_choose_cumsuck", False), Jump("scene27_cum_options")]
        text "Cum in throat":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

default scene27_cinside = False
default scene27_coutside = False
screen scene27_sex_cum_options():
    if scene27_choose_cumsuck:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [SetVariable("scene27_cinside", True), Jump("scene27_sex_cuminside")]
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    elif scene27_choose_cumdeep:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [SetVariable("scene27_cinside", True), Jump("scene27_sex_cuminside")]
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene27_coutside", True), Jump("scene27_sex_cumoutside")]
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        

default scene27_swallow = False
default scene27_spit = False

screen scene27_sex_swallow_spit():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene27_swallow", True), Jump("scene27_sex_cuminside2")]
    text "\"Swallow it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene27_spit", True), Jump("scene27_sex_cuminside2")]
    text "\"You can spit it out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene27_choice02_sex = False
default scene27_choice02_enough = False

screen scene27_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene27_choice02_enough", True), Return()]
    text "\"I've had enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene27_choice02_sex", True), Return()]
    text "\"Get on the bed.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene27_sleepwith = False
default scene27_refuse = False
screen scene27_choice03():
    imagebutton auto "scene27_choice03_with_%s":
        focus_mask True
        action [SetVariable("scene27_sleepwith", True), Return()]
        
    imagebutton auto "scene27_choice03_refuse_%s":
        focus_mask True
        action [SetVariable("scene27_refuse", True), Return()]

default scene27_choice04_all_options = True
default scene27_choice04_cum_options = False
default scene27_choice04_cum_inside_puss = False
default scene27_choice04_cum_inside_ass = False
default scene27_choice04_cum_outside = False
default scene27_choice04_cummies = False
default scene27_choice04_all_options2 = False

screen scene27_choice04():
    if scene27_choice04_all_options:
        if scene27_choice04_all_options2:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action [SetVariable("scene27_choice04_cum_inside_puss", True), SetVariable("scene27_choice04_cum_inside_ass", False), SetVariable("scene27_choice04_cummies", True), Jump("scene27_choice04_vag2")]
            text "Vaginal sex":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action [SetVariable("scene27_choice04_cum_inside_ass", True), SetVariable("scene27_choice04_cum_inside_puss", False), SetVariable("scene27_choice04_cummies", True), Jump("scene27_choice04_anal")]
            text "Anal sex":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        else:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action [SetVariable("scene27_choice04_cum_inside_puss", True), SetVariable("scene27_choice04_cum_inside_ass", False), SetVariable("scene27_choice04_cummies", True), Jump("scene27_choice04_vag")]
            text "Vaginal sex":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action [SetVariable("scene27_choice04_cum_inside_ass", True), SetVariable("scene27_choice04_cum_inside_puss", False), SetVariable("scene27_choice04_cummies", True), Jump("scene27_choice04_anal")]
            text "Anal sex":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        if scene27_choice04_cummies:  
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action [SetVariable("scene27_choice04_cum_options", True), SetVariable("scene27_choice04_all_options", False)]
            text "Cum":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    elif scene27_choice04_cum_options:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene27_choice04_cum_inside")
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene27_choice04_cum_outside")
        text "Cum outside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True


default scene27_slow = False
default scene27_allin = False
screen scene27_choice05_vag():
    imagebutton auto "scene27_choice05_slow_%s":
        focus_mask True
        action [SetVariable("scene27_slow", True), Jump("scene27_choice04_vag2")]
        
    imagebutton auto "scene27_choice05_allin_%s":
        focus_mask True
        action [SetVariable("scene27_allin", True), Jump("scene27_choice04_vag2")]

screen scene27_choice05_ass():
    imagebutton auto "scene27_choice05_slow_%s":
        focus_mask True
        action [SetVariable("scene27_slow", True), Jump("scene27_choice04_anal2")]
        
    imagebutton auto "scene27_choice05_allin_%s":
        focus_mask True
        action [SetVariable("scene27_allin", True), Jump("scene27_choice04_anal2")]

default scene28_with = False
default scene28_refuse = False
screen scene28_choice01():
    imagebutton auto "scene27_choice03_with_%s":
        focus_mask True
        action Jump("scene28_with")
        
    imagebutton auto "scene27_choice03_refuse2_%s":
        focus_mask True
        action Jump("scene28_refuse")


default scene29_coin = True
default scene29_poster = True

screen scene29_free_roam():
    key "K_UP" action Jump("scene29_free_roam_up")
    key "K_LEFT" action Jump("scene29_free_roam_left")
    key "K_RIGHT" action Jump("scene29_free_roam_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_up")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_right")

default visited_slady = False

screen scene29_free_roam_right():
    if not mc_has_strawberries:
        key "K_UP" action Jump("scene29_free_roam_right_up")
    else:
        key "K_UP" action Jump("scene29_free_roam_right_up_no")

    key "K_LEFT" action Jump("scene29_free_roam")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        if not mc_has_strawberries:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene29_free_roam_right_up")
        else:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene29_free_roam_right_up_no")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam")

screen scene29_free_roam_left():
    key "K_RIGHT" action Jump("scene29_free_roam")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene29_coin:
        imagebutton auto "scene29_coin_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_coin")

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam")

screen scene29_free_roam_up():
    key "K_UP" action Jump("scene29_free_roam_end")
    key "K_LEFT" action Jump("scene29_free_roam_up_left")
    key "K_RIGHT" action Jump("scene29_free_roam_up_right")
    key "K_DOWN" action Jump("scene29_free_roam")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_end")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_up_left")

        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_up_right")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam")

screen scene29_free_roam_right_up():
    key "K_UP" action Jump("scene29_free_roam_left")
    key "K_LEFT" action Jump("scene29_free_roam")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_left")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam")

screen scene29_free_roam_up_right():
    key "K_LEFT" action Jump("scene29_free_roam_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene29_poster:
        imagebutton auto "scene29_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_poster")

    if free_roam_arrows:
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_up")

screen scene29_free_roam_up_left():
    key "K_RIGHT" action Jump("scene29_free_roam_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene29_free_roam_up")

screen scene29_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Jump("scene29_free_roam_up")
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene29_continue")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5

screen yuuhi_talk_maia_choice():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("yuuhi_talk_maia_choice_love")
    text "\"I love her.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("yuuhi_talk_maia_choice_hate")
    text "\"I don't love her.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene29_choice03():
    if not mc_flirted_slady:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene29_choice03_op1")
        text "\"You.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    else:
        if not mc_flirted_slady_twice:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene29_choice03_op1_2")
            text "\"You.\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice03_op2")
    text "\"Do you have strawberries?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene29_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_strawberries")
    text "Pay":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_nostrawberries")
    text "\"Nevermind.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene29_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice05_op1")
    text "Throw him a bronze coin":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice05_op2")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice06():
    if not mc_met_nadia:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene29_choice06_op1")
        text "Talk to Nadia":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not mc_met_reham:
        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("scene29_choice06_op2")
        text "Check out the merchant":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice07():
    imagebutton auto "scene29_choice07_op1_%s":
        focus_mask True
        action Jump("scene29_choice07_op1")
    
    imagebutton auto "scene29_choice07_op2_%s":
        focus_mask True
        action Jump("scene29_choice07_op2")

    imagebutton auto "scene29_choice07_op3_%s":
        focus_mask True
        action Jump("scene29_choice07_op3")

screen scene29_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice08_op1")
    text "Kiss her first":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice08_op2")
    text "Stand behind her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice09():
    if not scene29_spank_count == 5:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene29_choice09_op1")
        text "Spank her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice09_op2")
    text "Stick it in her pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene29_choice09_op3")
    text "Stick it in her ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice10():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice10_op1")
    text "\"Tell me more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice10_op2")
    text "\"I'm not interested.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene29_choice11_front = False
default scene29_choice11_back = False
default scene29_choice11_feet = False
default scene29_choice11_cheeks = False

screen s29_hover_areas():
    add "scene29_choice11_lb_hover"
    add "scene29_choice11_rb_hover"
    add "scene29_choice11_face_hover"

screen s29_hover_areas2():
    add "scene29_choice11_ass_hover"

screen s29_hover_areas3():
    add "scene29_choice11_feet_hover"

screen scene29_choice11():
    if not scene29_choice11_front:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene29_choice11_op1")
        text "Front body":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op1_idle"
        text "Front body": 
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not scene29_choice11_back:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene29_choice11_op2")
        text "Backside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Backside":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not scene29_choice11_feet:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene29_choice11_op3")
        text "Look at feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else: 
        add "main_choices_op3_idle"
        text "Look at feet":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene29_choice11_op4")
    text "\"That's enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

    if scene29_choice11_front:
        imagebutton:
            idle "interact_indicator_idle"
            hover "interact_indicator_hover"
            focus_mask True
            action NullAction()
            hovered [
                Show("s29_hover_areas")
            ]
            unhovered [
                Hide("s29_hover_areas")
            ]

        imagebutton auto "scene29_choice11_lb_%s":
            focus_mask True
            action Jump("scene29_choice11_lb")
        
        imagebutton auto "scene29_choice11_rb_%s":
            focus_mask True
            action Jump("scene29_choice11_rb")
        
        imagebutton auto "scene29_choice11_face_%s":
            focus_mask True
            action Jump("scene29_choice11_face")
    
    if scene29_choice11_back:
        imagebutton:
            idle "interact_indicator_idle"
            hover "interact_indicator_hover"
            focus_mask True
            action NullAction()
            hovered [
                Show("s29_hover_areas2")
            ]
            unhovered [
                Hide("s29_hover_areas2")
            ]

        imagebutton auto "scene29_choice11_ass_%s":
            focus_mask True
            action Jump("scene29_choice11_ass")

    if scene29_choice11_feet:
        imagebutton:
            idle "interact_indicator_idle"
            hover "interact_indicator_hover"
            focus_mask True
            action NullAction()
            hovered [
                Show("s29_hover_areas3")
            ]
            unhovered [
                Hide("s29_hover_areas3")
            ]

        imagebutton auto "scene29_choice11_feet_%s":
            focus_mask True
            action Jump("scene29_choice11_feet")

    if scene29_choice11_cheeks:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action Jump("scene29_choice11_ipussy")
        text "Inspect pussy":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("scene29_choice11_iass")
        text "Inspect ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice11_2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Punch her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice11_op1")
    text "Supress impulsive thought":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice11_3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice11_good")
    text "\"She's pretty good!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice11_fine")
    text "\"She's fine.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene29_choice11_bad")
    text "\"Eh... Not my type.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene29_nadia_sex():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_nadia_sex_faster")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("nadia_sex_pos_toggle"), 
            If(nadia_sex_pos_toggle, Jump("is_nadia_sex2"), Jump("is_nadia_sex1"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if is_nadia_anim_asex1 or is_nadia_anim_asex2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("is_nadia_anim_vsex1", True), SetVariable("is_nadia_anim_asex1", False), SetVariable("is_nadia_anim_asex2", False), Jump("is_nadia_vsex")]
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if is_nadia_anim_vsex1 or is_nadia_anim_vsex2:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("is_nadia_anim_asex1", True), SetVariable("is_nadia_anim_vsex1", False), SetVariable("is_nadia_anim_vsex2", False), Jump("is_nadia_asex")]
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("is_nadia_sex_cum_inside")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene29_ren_quest01():
    imagebutton auto "scene29_ren_quest01_choice1_%s":
        focus_mask True
        action Jump("scene29_ren_quest01_choice1")
        
    imagebutton auto "scene29_ren_quest01_choice2_%s":
        focus_mask True
        action Jump("scene29_ren_quest01_choice2")
    
    imagebutton auto "scene29_ren_quest01_choice3_%s":
        focus_mask True
        action Jump("scene29_ren_quest01_choice3")

screen scene29_ren_quest_search_main():
    imagebutton auto "scene29_ren_quest_search_cellar_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_cellar")
        
    imagebutton auto "scene29_ren_quest_search_barrels_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_barrels")
    
    imagebutton auto "scene29_ren_quest_search_shelf_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_shelf")

    imagebutton auto "scene29_ren_quest_search_fire_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_fire")
    
    imagebutton auto "scene29_ren_quest_search_table_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_table")

screen scene29_ren_quest_search_cellar():
    imagebutton auto "scene29_ren_quest_search_cellar_barrels_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_cellar_barrels")
    
    imagebutton auto "scene02_choice01_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_main")

screen scene29_ren_quest_search_barrels():
    imagebutton auto "scene29_ren_quest_search_barrels_barrels_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_cellar_barrels")

    imagebutton auto "scene02_choice01_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_main")

screen scene29_ren_quest_search_shelf():
    imagebutton auto "scene29_ren_quest_search_shelf_bottles_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_shelf_bottles")
    
    imagebutton auto "scene29_ren_quest_search_shelf_bottle1_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_shelf_bottle2")
    
    imagebutton auto "scene29_ren_quest_search_shelf_bottle2_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_shelf_bottle1")
    
    imagebutton auto "scene29_ren_quest_search_shelf_pot_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_shelf_pot")
    
    imagebutton auto "scene29_ren_quest_search_shelf_earrings_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_shelf_earrings")

    imagebutton auto "scene02_choice01_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_main")

screen scene29_ren_quest_search_fire():
    imagebutton auto "scene29_ren_quest_search_fire_pot_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_fire_pot")
    
    imagebutton auto "scene29_ren_quest_search_fire_fire_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_fire_fire")
    
    imagebutton auto "scene02_choice01_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_main")

screen scene29_ren_quest_search_table():
    imagebutton auto "scene29_ren_quest_search_table_pac_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_table_pac")
    
    imagebutton auto "scene02_choice01_%s":
        focus_mask True
        action Jump("scene29_ren_quest_search_main")
    
screen scene29_choice02():
    imagebutton auto "scene29_choice02_choice1_%s":
        focus_mask True
        action Jump("scene29_choice02_choice1")
    
    imagebutton auto "scene29_choice02_choice2_%s":
        focus_mask True
        action Jump("scene29_choice02_choice2")
    
    imagebutton auto "scene29_choice02_choice3_%s":
        focus_mask True
        action Jump("scene29_choice02_choice3")

screen scene29_choice0():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice0_op1")
    text "Inspect her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice0_op2")
    text "\"I want to talk to her instead.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene29_choice00():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice00_op1")
    text "Help her out":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice00_op2")
    text "\"I don't wanna get involved.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene29_choice000():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice000_op1")
    text "Pay her first":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice000_op2")
    text "Drink":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene29_choice000_op3")
    text "\"I'm lactose intolerant.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene29_choice0000():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice0000_op1")
    text "\"I am.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice0000_op2")
    text "\"The girl outside...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene29_choice00000():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice00000_op2")
    text "\"I just wanted to help, that's all.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice00000_op1")
    text "\"I did this because of you, Nadia.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene29_choice000000():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene29_choice000000_op1")
    text "\"Of course.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene29_choice000000_op2")
    text "\"Maybe another time...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene30_choice01():
    imagebutton auto "scene30_choice01_op1_%s":
        focus_mask True
        action Jump("scene30_choice01_op1")

    imagebutton auto "scene30_choice01_op2_%s":
        focus_mask True
        action Jump("scene30_choice01_op2")

screen free_roam_maia_talk_ogre():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("free_roam_maia_talk_ogre_op1")
    text "Keep lying":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("free_roam_maia_talk_ogre_op2")
    text "Tell her the truth":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen free_roam_maia_talk_harem():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("free_roam_maia_talk_harem_op1")
    text "\"You're the only one I need.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("free_roam_maia_talk_harem_op2")
    text "\"I want to be with other women too.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene31_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene31_choice01_moti")
    text "\"I need some 'motivation'.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene31_choice01_no")
    text "\"Nope. All set.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene31_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene31_choice02_op1")
    text "Punch him":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene31_choice02_op2")
    text "\"Leave before I call the guards.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene31_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene31_choice03_op1")
    text "\"Yes.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene31_choice03_op2")
    text "\"I have buisness with her.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene31_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene31_choice04_op1")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene31_choice04_op2")
    text "\"Sorry, Yuuhi. But we're not... like that.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene31_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene31_choice05_op1")
    text "\"Alright, alright. I'm coming.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene31_choice05_op2")
    text "\"Maybe another time, Yuuhi.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen gameplay_map_tutorial3():
        add "irda_map_screen"
        imagebutton auto "irda_castle_%s":
                focus_mask True
                #action Jump("queen_call")
        imagebutton auto "irda_guild_%s":
            focus_mask True
            #action Jump("scene20")

        imagebutton auto "irda_blacksmith_%s":
            focus_mask True
            #action Jump("queen_call")

        imagebutton auto "irda_brothel_%s":
                focus_mask True
                #action Jump("queen_call")
        
        imagebutton auto "irda_guardpost_%s":
                focus_mask True
                #action Jump("queen_call")
        
        imagebutton auto "irda_barn_%s":
                focus_mask True
                action Jump("scene33_barn")


screen scene34_witch2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene34_witch2_consent")
    text "Give consent":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene34_witch2_escape")
    text "Try to escape":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
screen scene34_witch2_escape():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5
    
    if mc_karma <= 3:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≤ 3) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma <= 3:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [SetVariable("quest_witch_amelia_dead", True), Jump("scene34_witch2_dead")]
        text "Kill her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene34_witch2_dead_fail")
        text "Kill her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("quest_witch_amelia_alive", True), Jump("scene34_witch2_alive")]
    text "Incapacitate her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
screen scene34_witch2_consent_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene34_witch2_consent_after():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("quest_witch_amelia_alive_free", True), SetVariable("quest_witch_amelia_alive", True), Jump("scene34_witch2_consent_let")]
    text "\"Well, this is awkward...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("quest_witch_amelia_alive", True), Jump("scene34_witch2_consent_attack")]
    text "Attack":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen diana_birth_scene():
    imagebutton auto "birth_scene_watch_%s":
        focus_mask True
        action Jump("diana_birth_scene2")
    
    imagebutton auto "birth_scene_skip_%s":
        focus_mask True
        action Return()

screen maia_birth_scene():
    imagebutton auto "birth_scene_watch_%s":
        focus_mask True
        action Jump("maia_birth_scene2")
    
    imagebutton auto "birth_scene_skip_%s":
        focus_mask True
        action Return()
screen yuuhi_harem_training2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("yuuhi_harem_training2_dwipe")
    text "\"Don't wipe it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("yuuhi_harem_training2_wipe")
    text "\"You can wipe it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen yuuhi_harem_training2_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_hj_faster_training")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_hj_pov_toggle"), 
            If(yuuhi_hj_pov_toggle, Jump("is_yuuhi_hj_pov2_training"), Jump("is_yuuhi_hj_pov1_training"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("yuuhi_harem_training2_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen yuuhi_harem_training2_second_controls():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_hj_faster_training_second")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_hj_pov_toggle"), 
            If(yuuhi_hj_pov_toggle, Jump("is_yuuhi_hj_pov2_training_second"), Jump("is_yuuhi_hj_pov1_training_second"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("yuuhi_harem_training_hj_second_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_hj_pov1_training:
    $ is_yuuhi_anim_hj1 = True
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = False
    $ yuuhi_hj_pov_toggle = True
    $ yuuhi_hj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj1 with dissolve
    call screen yuuhi_harem_training2_controls with dissolve

label is_yuuhi_hj_pov2_training:
    $ is_yuuhi_anim_hj1 = False
    $ is_yuuhi_anim_hj2 = True
    $ is_yuuhi_anim_hj3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj2 with dissolve
    yuuhi "A-Are you staring at my breasts?"
    call screen yuuhi_harem_training2_controls with dissolve

label is_yuuhi_hj_pos2_training:
    $ is_yuuhi_anim_hj1 = False
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj3 with dissolve
    call screen yuuhi_harem_training2_controls with dissolve

label is_yuuhi_hj_faster_training:
    scene black with Dissolve(0.3)
    if is_yuuhi_anim_hj1:
        show is_yuuhi_anim_hj1_faster with dissolve
        hide is_yuuhi_anim_hj1 with dissolve
        yuuhi "Hmph! Hmph!"
        yuuhi "Does it not hurt when I go faster?"
        mc "It feels better."
        call screen yuuhi_harem_training2_controls with dissolve
    elif is_yuuhi_anim_hj2:
        show is_yuuhi_anim_hj2_faster with dissolve
        hide is_yuuhi_anim_hj2 with dissolve
        yuuhi "Mhmmm~"
        mc "Your hands are really soft."
        yuuhi "Right? I use tools all the time but I'm really careful."
        call screen yuuhi_harem_training2_controls with dissolve
    else:
        show is_yuuhi_anim_hj3_faster with dissolve
        hide is_yuuhi_anim_hj3 with dissolve
        yuuhi "I see why you like this position now~"
        call screen yuuhi_harem_training2_controls with dissolve

label is_yuuhi_hj_pov1_training_second:
    $ is_yuuhi_anim_hj1 = True
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = False
    $ yuuhi_hj_pov_toggle = True
    $ yuuhi_hj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj1 with dissolve
    call screen yuuhi_harem_training2_second_controls with dissolve

label is_yuuhi_hj_pov2_training_second:
    $ is_yuuhi_anim_hj1 = False
    $ is_yuuhi_anim_hj2 = True
    $ is_yuuhi_anim_hj3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj2 with dissolve
    call screen yuuhi_harem_training2_second_controls with dissolve

label is_yuuhi_hj_pos2_training_second:
    $ is_yuuhi_anim_hj1 = False
    $ is_yuuhi_anim_hj2 = False
    $ is_yuuhi_anim_hj3 = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_hj3 with dissolve
    call screen yuuhi_harem_training2_second_controls with dissolve

label is_yuuhi_hj_faster_training_second:
    if is_yuuhi_anim_hj1:
        show is_yuuhi_anim_hj1_faster with dissolve
        hide is_yuuhi_anim_hj1 with dissolve
        yuuhi "{i}Hmph! Hmph!{/i}"
        call screen yuuhi_harem_training2_second_controls with dissolve
    elif is_yuuhi_anim_hj2:
        show is_yuuhi_anim_hj2_faster with dissolve
        hide is_yuuhi_anim_hj2 with dissolve
        yuuhi "{i}Mhmmm~{/i}"
        call screen yuuhi_harem_training2_second_controls with dissolve
    else:
        show is_yuuhi_anim_hj3_faster with dissolve
        hide is_yuuhi_anim_hj3 with dissolve
        yuuhi "{i}Hmmm~{/i}"
        call screen yuuhi_harem_training2_second_controls with dissolve

screen is_yuuhi_bj_controls_train1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_faster_train1")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_controls_train1_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_bj_pov1_train1:
    $ is_yuuhi_anim_bj1 = True
    $ is_yuuhi_anim_bj2 = False
    $ is_yuuhi_anim_bj3 = False
    $ yuuhi_bj_pov_toggle = True
    $ yuuhi_bj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj1 with dissolve
    call screen is_yuuhi_bj_controls with dissolve

label is_yuuhi_bj_faster_train1:
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj1_faster with dissolve
    hide is_yuuhi_anim_bj1 with dissolve
    yuuhi "{i}*gag* Auchh!!{/i}"
    call screen is_yuuhi_bj_controls_train1 with dissolve

screen is_yuuhi_bj_controls_train1_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_controls_train1_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_controls_train1_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_bj_choice1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("yuuhi_harem_training_bj_first_kiss")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("yuuhi_harem_training_bj_first_apologize")
    text "Apologize":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_bj_controls_train2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_faster_train2")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_bj_pov_toggle"), 
            If(yuuhi_bj_pov_toggle, Jump("is_yuuhi_bj_pov1_train2"), Jump("is_yuuhi_bj_pov2_train2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_controls_train2_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_bj_controls_train2_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_controls_train2_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_bj_controls_train2_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_bj_pov1_train2:
    $ is_yuuhi_anim_bj1 = False
    $ is_yuuhi_anim_bj2 = True
    $ is_yuuhi_anim_bj3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj2 with dissolve
    call screen is_yuuhi_bj_controls_train2 with dissolve

label is_yuuhi_bj_pov2_train2:
    $ is_yuuhi_anim_bj1 = False
    $ is_yuuhi_anim_bj2 = False
    $ is_yuuhi_anim_bj3 = True
    $ yuuhi_bj_pov_toggle = True
    $ yuuhi_bj_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_bj3 with dissolve
    call screen is_yuuhi_bj_controls_train2 with dissolve

label is_yuuhi_bj_faster_train2:
    scene black with Dissolve(0.3)
    if is_yuuhi_anim_bj2:
        show is_yuuhi_anim_bj2_faster with dissolve
        hide is_yuuhi_anim_bj2 with dissolve
        yuuhi "{i}*gag* Aghh!!{/i}"
        call screen is_yuuhi_bj_controls_train2 with dissolve
    else:
        show is_yuuhi_anim_bj3_faster with dissolve
        hide is_yuuhi_anim_bj3 with dissolve
        yuuhi "{i}*Glllck~!*{/i} Mmm!"
        call screen is_yuuhi_bj_controls_train2 with dissolve
    
screen is_yuuhi_sex_choice1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_sex_choice1_shove")
    text "Shove it in her mouth":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("yuuhi_harem_training_asex_first2")
    text "Put it away":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_asex_controls_train1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_faster_train")
    text "Faster":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("yuuhi_asex_pov_toggle"), 
            If(yuuhi_asex_pov_toggle, Jump("is_yuuhi_asex_pov2_train"), Jump("is_yuuhi_asex_pov1_train"))
        ]

    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_controls_train_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen is_yuuhi_asex_controls_train_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_controls_train_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("is_yuuhi_asex_controls_train_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

label is_yuuhi_asex_pov1_train:
    $ is_yuuhi_anim_asex1 = True
    $ is_yuuhi_anim_asex2 = False
    $ is_yuuhi_anim_asex3 = False
    $ yuuhi_asex_pov_toggle = True
    $ yuuhi_asex_pos_toggle = True
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_asex2 with dissolve
    call screen is_yuuhi_asex_controls_train1 with dissolve

label is_yuuhi_asex_pov2_train:
    $ is_yuuhi_anim_asex1 = False
    $ is_yuuhi_anim_asex2 = True
    $ is_yuuhi_anim_asex3 = False
    scene black with Dissolve(0.3)
    show is_yuuhi_anim_asex3 with dissolve
    call screen is_yuuhi_asex_controls_train1 with dissolve

label is_yuuhi_asex_faster_train:
    scene black with Dissolve(0.3)
    if is_yuuhi_anim_asex1:
        show is_yuuhi_anim_asex2_faster with dissolve
        hide is_yuuhi_anim_asex2 with dissolve
        yuuhi "{i}Ah!{/i} Oh! Sl-slower!"
        call screen is_yuuhi_asex_controls_train1 with dissolve
    elif is_yuuhi_anim_asex2:
        show is_yuuhi_anim_asex3_faster with dissolve
        hide is_yuuhi_anim_asex3 with dissolve
        yuuhi "M-mercy on my butthole, [mc]!"
        call screen is_yuuhi_asex_controls_train1 with dissolve

screen pregnancy_timer():
    add "pregnancy_timer_main"
    imagebutton auto "pregnancy_timer_slow_%s":
        focus_mask True
        action Jump("pregnancy_timer_slow")

    imagebutton auto "pregnancy_timer_fast_%s":
        focus_mask True
        action Jump("pregnancy_timer_fast")
    
    imagebutton auto "pregnancy_timer_real_%s":
        focus_mask True
        action Jump("pregnancy_timer_real")

screen yuuhi_harem_check():
    add "yuuhi_harem_check_main"
    imagebutton auto "yuuhi_harem_check_no_%s":
        focus_mask True
        action Jump("yuuhi_harem_check_no")

    imagebutton auto "yuuhi_harem_check_yes_%s":
        focus_mask True
        action Jump("yuuhi_harem_check_yes")

default yuuhi_harem_check = True
label yuuhi_harem_check_no:
    $ yuuhi_harem = False
    $ yuuhi_harem_check = False
    call screen gameplay with dissolve

label yuuhi_harem_check_yes:
    $ yuuhi_harem = True
    $ yuuhi_harem_check = False
    call screen gameplay with dissolve

label pregnancy_timer_fast:
    $ pregnancy_time = 30
    $ show_pregnancy_timer_screen = False
    call screen gameplay with dissolve

label pregnancy_timer_slow:
    $ pregnancy_time = 90
    $ show_pregnancy_timer_screen = False
    call screen gameplay with dissolve

label pregnancy_timer_real:
    $ pregnancy_time = 274
    $ show_pregnancy_timer_screen = False
    call screen gameplay with dissolve

screen scene35_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene35_choice01_op1")
    text "Scream at the top of your lungs":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene35_choice01_op2")
    text "Throw a pebble at her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene35_choice01_op3")
    text "Bow dramatically":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene35_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene35_choice02_op1")
    text "\"I still want to talk to you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene35_choice02_op2")
    text "\"Works for me.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene35_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene35_choice03_op1")
    text "Kneel and kiss her foot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene35_choice03_op2")
    text "\"I'm not gonna do that.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene35_choice03_2():
    imagebutton auto "scene35_choice03_op1_%s":
        focus_mask True
        action Jump("scene35_choice03_op1")
    
    imagebutton auto "scene35_choice03_op2_%s":
        focus_mask True
        action Jump("scene35_choice03_op2_2")

screen scene35_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene35_choice04_op1")
    text "Start licking her foot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene35_choice04_op2")
    text "Stand up":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
screen scene35_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene35_choice05_op1")
    text "\"I'll go now.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene35_choice05_op2")
    text "\"I'll prepare first.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene35_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene35_choice06_op1")
    text "Reminisce the past":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene35_choice06_op2")
    text "Move in":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene35_choice06_ending():
    add "scene35_choice06_ending"
    imagebutton auto "4_s23_continue_%s":
        focus_mask True
        action Return()
    

screen chapter1_ending():
    add "chapter1_journey_main"
    imagebutton auto "4_s23_continue_%s":
        focus_mask True
        action Return()


default scene36_choice1_continue = False
screen scene36_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene36_choice01_op1")
    text "\"Why do you travel alone?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene36_choice01_op3")
    text "\"Why are you going to the Pleasure Queen?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene36_choice01_op2")
    text "\"Where are you from?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
    if scene36_choice1_continue:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene36_continue")
        text "Sleep":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene36_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene36_choice02_op1")
    text "Alex has a pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene36_choice02_op2")
    text "Alex has a dick":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene36_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene36_choice03_op1")
    text "Look at feet":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene36_continue3")
    text "Try to sleep":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen s37_hover_areas():
    add "intro16_hover"

screen scene37_phone():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s37_hover_areas")
        ]
        unhovered [
            Hide("s37_hover_areas")
        ]

    imagebutton auto "intro16_%s":
        focus_mask True
        action Return()

screen scene37_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Drift away":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

default alex_sex_pov_toggle_37 = False
default alex_sex_speed_toggle_37 = False
default scene37_sex1 = False
default scene37_sex2 = False
screen scene37_choice02():
    if not alex_sex_speed_toggle_37:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene37_choice02_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene37_choice02_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("alex_sex_pov_toggle_37"), 
            If(alex_sex_pov_toggle_37, Jump("scene37_sex2"), Jump("scene37_sex1"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene37_alex_cum1")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

default alex_sex_speed_toggle_37_2 = False
screen scene37_choice03():
    if not alex_sex_speed_toggle_37_2:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene37_choice03_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene37_choice03_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene37_alex_cum2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen cum():
    add "images/custom_gui/global/cum_flash.webp":
        at flash_anim

transform flash_anim:
    alpha 1.0
    linear 0.2 alpha 0.0

screen scene37_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene37_choice04_op1")
    text "Settle for feet":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene37_choice04_op2")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default alex_feet_pov_toggle_37 = False
default alex_feet_speed_toggle_37 = False
default scene37_feet1 = False
default scene37_feet2 = False
screen scene37_feet():
    if not alex_feet_speed_toggle_37:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene37_feet_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene37_feet_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("alex_feet_pov_toggle_37"), 
            If(alex_feet_pov_toggle_37, Jump("scene37_feet1"), Jump("scene37_feet2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene37_alex_feet_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene39_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene39_choice01_op1")
    text "Take a peek":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene40")
    text "Go with Ymir":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene40_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene40_choice01_op1")
    text "\"I don't mind some help.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene40_choice01_op2")
    text "\"I'll wash by myself.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene40_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene40_choice02_op1")
    text "Accept your fate (Submissive)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene40_choice02_op2")
    text "Stand up to her (Dominant)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True
    
screen scene40_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene40_choice03_op1")
    text "Focus on pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene40_choice03_op2")
    text "Focus on ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene40_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene40_choice04_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

default scene40_choice05_end = False
screen scene40_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Spank":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if scene40_choice05_end:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene40_d_continue")
        text "Continue":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene40_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene40_choice06_op1")
    text "Spank":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene40_d_continue")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene40_7_speed = False
default scene40_7_cpov = False
default scene40_7_pov1 = False
default scene40_7_pov2 = False
screen scene40_choice07():
    if not scene40_7_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene40_7_bj_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene40_7_bj_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("scene40_7_cpov"), 
            If(scene40_7_cpov, Jump("scene40_7_pov1"), Jump("scene40_7_pov2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene40_7_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene40_choice08():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5

    if mc_karma <= 4:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≤ 4) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma <= 4:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene40_choice08_op1")
        text "\"I'll do it myself. (Slap her)\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene40_choice08_op1")
        text "\"I'll do it myself. (Slap her)\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene40_choice08_op2")
    text "Agree with Ysella":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene40_choice08_op3")
    text "\"It's fine. I wasn't agaisnt it or anything\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene41_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene41_choice01_op1")
    text "\"I'm good.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene41_choice01_op2")
    text "\"I need some comforting.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene41_hj_speed = False
default scene41_hj_cpov = False
default scene41_hj1 = False
default scene41_hj2 = False
screen scene41_choice02():
    if not scene41_hj_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene41_hj_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene41_hj_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("scene41_hj_cpov"), 
            If(scene41_hj_cpov, Jump("scene41_hj1"), Jump("scene41_hj2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene41_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen update0_2_3_end():
    add "update0_2_3_ending"
    imagebutton auto "update0_2_3_ending_c_%s":
        focus_mask True
        action Return()


screen qte_tutorial():
    add "tutorial_bg"
    text "Tutorial":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 550 xanchor 0.5 yanchor 0.5
    text "Tap the inner cube when the shrinking cube fits perfectly inside it!":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "tutorial_bj_continue_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1270 ypos 1175 xanchor 0.5 yanchor 0.5

init python:
    import math
    import time
    def create_circle(size, color):
        return AlphaMask(
            Solid(color, xysize=(size, size)),
            Solid("#FFF", xysize=(size, size)),
            operator="and"
        )
    
    green_circle = create_circle(100, "#43c3cf")

    def _quick_event_click(current_radius, target_radius):
        diff = abs(current_radius - target_radius)
        if diff <= 3:
            result = "Perfect"
        elif diff <= 30:
            result = "Good"
        else:
            result = "Bad"
        return [
            SetScreenVariable("result_text", result),
            SetScreenVariable("result_shown", True),
            SetScreenVariable("shrinking", False)
        ]

transform pulse_green:
    zoom 1.0
    linear 0.1 zoom 1.2
    linear 0.1 zoom 1.0

transform pulse_yellow:
    zoom 1.0
    linear 0.1 zoom 1.2
    linear 0.1 zoom 1.0

transform pulse_red:
    zoom 1.0
    linear 0.05 zoom 1.3
    linear 0.1 zoom 1.0

transform fade_out_fast:
    linear 0.3 alpha 0.0

screen quick_event():
    default target_radius = 50         
    default outer_radius = 150        
    default shrinking = True
    default result_shown = False
    default result_text = ""
    default shrink_speed = 90.0        

    # Background dim
    #add "#0008"

    fixed:
        xalign 0.5
        yalign 0.5
        xysize (300, 300)

        $ current_red = create_circle(int(outer_radius*2), "#cf4343")

        if result_text == "Perfect":
            add current_red at circle_shape, pulse_green
        elif result_text == "Good":
            add current_red at circle_shape, pulse_yellow
        elif result_text == "Bad":
            add current_red at circle_shape, pulse_red
        elif result_text == "Missed":
            add current_red at circle_shape, fade_out_fast
        else:
            add current_red at circle_shape

    
        add green_circle at circle_shape

        
        button:
            xysize (300, 300)
            xalign 0.5
            yalign 0.5
            sensitive shrinking
            action _quick_event_click(outer_radius, target_radius)

    
    timer 0.01 repeat True action If(
        shrinking,
        SetScreenVariable("outer_radius", max(target_radius, outer_radius - shrink_speed * 0.01)),
        None
    )

    
    if shrinking and outer_radius <= target_radius:
        timer 0.01 action [
            SetScreenVariable("result_text", "Missed"),
            SetScreenVariable("result_shown", True),
            SetScreenVariable("shrinking", False)
        ]

    
    if result_shown:
        text result_text:
            size persistent.choices_text_size
            xalign 0.5
            yalign 0.8
            color ("#00FF00" if result_text == "Perfect"
                else "#FFFF00" if result_text == "Good"
                else "#FF0000" if result_text in ["Bad", "Missed"]
                else "#FFFFFF")
            outlines [(2, "#000", 0, 0)]
        
        timer 1.0 action Return(result_text)

transform circle_shape:
    anchor (0.5, 0.5)
    align (0.5, 0.5)


default scene42_coin = True
default scene42_poster1 = True
default scene42_poster2 = True

screen scene42_free_roam():
    key "K_UP" action Jump("scene42_forward")
    key "K_LEFT" action Jump("scene42_left")
    key "K_DOWN" action Jump("scene42_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_forward")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_left")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_down")
        
        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam")

screen scene42_up():
    if not mc_met_heiter:
        key "K_UP" action Jump("scene42_heiter")
    key "K_DOWN" action Jump("scene42_up_down")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene42_poster1:
        imagebutton auto "scene42_poster1_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_poster1")

    if free_roam_arrows:
        if not mc_met_heiter:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_heiter")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_up_down")
        
        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam_forward")

screen scene42_down():
    key "K_DOWN" action Jump("scene42_down_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene42_coin:
        imagebutton auto "scene42_coin_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_free_roam_coin")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_down_up")
        
        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam_down")

screen scene42_left():
    key "K_UP" action Jump("scene42_left_up")
    key "K_DOWN" action Jump("scene42_afterwell")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_left_up")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_afterwell")

        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam_left")

screen scene42_left_up():
    key "K_UP" action Jump("scene42_left_up_up")
    if not mc_met_sigrun:
        key "K_LEFT" action Jump("scene42_sigrun")
    key "K_DOWN" action Jump("scene42_left")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_left_up_up")

        if not mc_met_sigrun:
            imagebutton auto "left_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_sigrun")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_left")
        
        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam_left_up")

screen scene42_left_up_up():
    if not mc_met_werewolf_villager:
        key "K_UP" action Jump("scene42_werewolf_villager")
    key "K_LEFT" action Jump("scene42_left_up_up_left")
    key "K_DOWN" action Jump("scene42_left_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        if not mc_met_werewolf_villager:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_werewolf_villager")

        imagebutton auto "left_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_left_up_up_left")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_left_up")

        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam_left_up_up")

screen scene42_left_up_up_left():
    key "K_DOWN" action Jump("scene42_left_up_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene42_poster2:
        imagebutton auto "scene42_poster2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_poster2")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene42_left_up_up")
    
        if mc_met_sigrun and mc_met_heiter and mc_met_well_villager:
            imagebutton auto "free_roam_end2_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene42_end_freeroam_left_up_up_left")
                

screen scene42_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Return()
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene42_continue")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5

screen scene42_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene42_choice01_op1")
    text "Participate":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene42_choice01_op2")
    text "Refuse":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene42_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene42_choice02_op1")
    text "Stay and participate":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene42_choice02_op2")
    text "Leave the village":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene43_forward():
    key "K_UP" action Return()

    imagebutton auto "up_%s":
        focus_mask True
        action Return()

screen scene43_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice01_op1")
    text "Push the man":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice01_op2")
    text "Take the plunge":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene43_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice02_correct")
    text "\"Fear.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice02_wrong")
    text "\"Power.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene43_choice02_wrong")
    text "\"Death.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

default mc_answered_temp = False
screen scene43_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("mc_answered_temp", True), Jump("scene43_choice03_wrong")]
    text "\"Temptation.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice03_wrong")
    text "\"Love.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene43_choice03_correct")
    text "\"Desire.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene43_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice04_wrong")
    text "\"A ghost.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice04_correct")
    text "\"An echo.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene43_choice04_wrong")
    text "\"A thought.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene43_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice05_op1")
    text "\"Fine. I won't mate with your wife.":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice05_op2")
    text "\"No. We fight as intended.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene43_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice06_op1")
    text "Convince Alex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice06_op2")
    text "Try to sleep":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene43_ltits = False
default scene43_lpussy = False
default scene43_lfeet = False

screen scene43_choice07():
    if not scene43_ltits:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene43_choice07_ltits")
        text "Look at breasts":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op1_idle"
        text "Look at breasts":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True


    if persistent.alex_p:
        if not scene43_lpussy:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene43_choice07_lpussy")
            text "Look at pussy":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            add "main_choices_op2_idle"
            text "Look at pussy":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    elif persistent.alex_d:
        if not scene43_lpussy:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene43_choice07_lpussy")
            text "Look at cock":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            add "main_choices_op2_idle"
            text "Look at cock":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not scene43_lfeet:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene43_choice07_lfeet")
        text "Look at feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Look at feet":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene43_choice07_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    
    if scene43_ltits:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action Jump("scene43_choice07_ltits_inspect")
        text "Inspect":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("scene43_choice07_ltits_touch")
        text "Touch":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    elif scene43_lpussy:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action Jump("scene43_choice07_lpussy_inspect")
        text "Inspect":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("scene43_choice07_lpussy_touch")
        text "Touch":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
        if persistent.alex_p:
            imagebutton auto "main_choices_left_op3_%s":
                focus_mask True
                action Jump("scene43_choice07_lpussy_sniff")
            text "Sniff":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    elif scene43_lfeet:
        imagebutton auto "main_choices_left_op1_%s":
            focus_mask True
            action Jump("scene43_choice07_lfeet_inspect")
        text "Inspect":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_left_op2_%s":
            focus_mask True
            action Jump("scene43_choice07_lfeet_touch")
        text "Touch":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
        imagebutton auto "main_choices_left_op3_%s":
            focus_mask True
            action Jump("scene43_choice07_lfeet_sniff")
        text "Sniff":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 292 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene43_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice08_op1")
    text "\"Not in the mood.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice08_op2")
    text "\"Sounds fun. Sure.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene43_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice09_shoulder")
    text "\"Shoulder?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice09_hand")
    text "\"Hand?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene43_choice09_cheek")
    text "\"Cheek?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

default scene43_mcmouth = False
default scene43_mcneck = False
default scene43_mcchest = False
default scene43_nose = False
default scene43_lips = False
screen scene43_choice10():
    if not scene43_mcmouth:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene43_choice10_mcm")
        text "Put it in your mouth":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    if not scene43_mcneck:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene43_choice10_mcn")
        text "Put it on your neck":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    if not scene43_mcchest:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene43_choice10_mcc")
        text "Put it on your chest":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene43_choice11():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene43_choice09_nose")
    text "\"Nose?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice09_ear")
    text "\"Ear?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene43_choice09_lips1")
    text "\"Lips?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

default scene43_boobs1 = True
screen scene43_choice12():
    if scene43_boobs1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene43_choice09_boobs1")
        text "\"Boobs?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene43_choice09_boobs2")
        text "\"It's definitely your boobs.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene43_choice09_hair")
    text "\"Hair?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene43_choice09_lips2")
    text "\"Lips?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

default mc_date_adaroza = False
default mc_date_adaroza_win = False
default mc_date_adaroza_win_fin = False
default mc_date_adaroza_fail = False
default mc_date_adaroza_points = 0

default mc_date_annette = False
default mc_date_annette_win = False
default mc_date_annette_win_fin = False
default mc_date_annette_points = 0

default mc_date_sigrun = False
default mc_date_sigrun_win = False
default mc_date_sigrun_fail= False
default mc_date_sigrun_win_fin = False
default mc_date_sigrun_points = 0

default mc_knows_cabin = False

default mc_date_adaroza_final = False
default mc_date_annette_final = False
default mc_date_sigrun_final = False

screen scene46_choice0():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_sex_roza_eatp")
    text "Eat Roaz's pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_sex_roza_eata")
    text "Eat Roaz's ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene46_sex_ada_eatp")
    text "Eat Ada's pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene46_sex_ada_eata")
    text "Eat Ada's ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene46_adaroza_sex_0")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene46_choice01():
    add "scene46_choice01_choices_main"

    if not mc_date_adaroza and not mc_date_adaroza_fail:
        button:
            focus_mask True
            action Jump("scene46_adaroza")
            add "free_roam_maia_op1"
            text "Visit Ada and Roza": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
    elif mc_date_adaroza_win and not mc_date_adaroza_win_fin:
        add "scene46_choice01_adaroza_heart" xpos 0.1 ypos 0.009
        button:
            focus_mask True
            action Jump("scene46_adaroza_sex")
            add "free_roam_maia_op1"
            text "Visit Ada and Roza": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
    else:
        text "Visit Ada and Roza":
            size persistent.free_roam_choices_text_size color "#818181" font "candara.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
    
    if not mc_date_annette and not mc_date_annette_win:
        button:
            focus_mask True
            action Jump("scene47_annette")
            add "free_roam_maia_op2"
            text "Visit Annette": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
    elif mc_date_annette_win and not mc_date_annette_win_fin:
        add "scene46_choice01_ann_heart" xpos 0.1 ypos 0.024
        button:
            focus_mask True
            action Jump("scene47_annette_sex")
            add "free_roam_maia_op2"
            text "Visit Annette": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
    else:
        text "Visit Annette":
            size persistent.free_roam_choices_text_size color "#818181" font "candara.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5


    if not mc_let_aldwin_win:
        if not mc_date_sigrun and not mc_date_sigrun_fail:
            button:
                focus_mask True
                action Jump("scene48_sigrun")
                add "free_roam_maia_op3"
                text "Visit Sigrun": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
        elif mc_date_sigrun_win and not mc_date_sigrun_win_fin and not mc_date_sigrun_final:
            add "scene46_choice01_sig_heart" xpos 0.1 ypos 0.034
            button:
                focus_mask True
                action Jump("scene48_sigrun_sex")
                add "free_roam_maia_op3"
                text "Visit Sigrun": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
        else:
            text "Visit Sigrun":
                size persistent.free_roam_choices_text_size color "#818181" font "candara.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
    else:
        text "Visit Sigrun":
            size persistent.free_roam_choices_text_size color "#818181" font "candara.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

screen scene46_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_choice02_op1")
    text "\"Safe? Maybe. Satisfied? Definitely.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_choice02_op2")
    text "\"I'd do my best. I'm not perfect but I try.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene46_choice02_op3")
    text "\"With me? Always.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene46_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_choice03_op1")
    text "\"Her loyalty.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_choice03_op2")
    text "\"Her body.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene46_choice03_op3")
    text "\"Her spirit.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene46_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_choice04_op1")
    text "\"Honestly? I prefer them smaller.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_choice04_op2")
    text "\"Big breasts are better.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene46_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_choice05_op1")
    text "\"Roza.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_choice05_op2")
    text "\"You're both incredible in your own ways.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene46_choice05_op3")
    text "\"Ada.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene46_choice05_op4")
    text "\"Whoever moans louder.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

default scene46_bj1_speed = False
default scene46_bj1_cpov = False
default scene46_bj1_1 = False
default scene46_bj1_2 = False

screen scene46_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [
            ToggleVariable("scene46_bj1_cpov"), 
            If(scene46_bj1_cpov, Jump("scene46_bj1_2"), Jump("scene46_bj1_1"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_adaroza_bj2")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True


default scene46_bj2_speed = False
default scene46_bj2_roza = False
screen scene46_choice07():
    if scene46_bj2_roza:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene46_bj2_ada")
        text "Switch to Ada":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene46_bj2_roza")
        text "Switch to Roza":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_bj2_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene46_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_choice06_ci_ada")
    text "Cum inside (Ada)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_choice06_ci_roza")
    text "Cum outside (Roza)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene46_choice06_co")
    text "Cum outside (Both)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene46_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene46_sex_roza")
    text "Roza":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_sex_ada")
    text "Ada":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene46_sex_speed = False
default scene46_sex_roza = False
screen scene46_choice010():
    if not scene46_sex_roza:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene46_sex_ada")
        text "Switch to Ada":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene46_sex_roza")
        text "Switch to Roza":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene46_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene47_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice01_op1")
    text "\"You're sweet.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice01_op2")
    text "\"Shy, but I bet you're wild underneath.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene47_choice01_op3")
    text "\"A little weird, but cute.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene47_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice02_op1")
    text "\"I would run away.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice02_op2")
    text "\"Depends on what you did.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene47_choice02_op3")
    text "\"Of course.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene47_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice03_op1")
    text "\"Go for a second round.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice03_op2")
    text "\"Hold you close. I love to cuddle afterwards.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene47_choice03_op3")
    text "\"Say thanks and fall asleep.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene47_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice04_op1")
    text "Comfort her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice04_op2")
    text "Suggest anal":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene47_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice05_op1")
    text "\"You need to take a shower...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice05_op2")
    text "\"Good. Don't wash.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
        
screen scene47_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice06_op1")
    text "\"You look beautiful.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice06_op2")
    text "\"You still look dirty.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene47_bj_speed = False
default scene47_bj_cpov = False
default scene47_bj1 = False
default scene47_bj2 = False
screen scene47_sex2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [
            ToggleVariable("scene47_bj_cpov"), 
            If(scene47_bj_cpov, Jump("scene47_bj1"), Jump("scene47_bj2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_bj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene47_bj_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_bj_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_bj_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene47_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice07_op1")
    text "\"I'd like a footjob first.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice07_op2")
    text "\"Let's begin.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene47_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene47_choice08_op1")
    text "Cum on feet":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene47_choice08_op2")
    text "\"I'll finish inside you!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene47_fj():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

default is_annette_anim_vsex1 = False
default is_annette_anim_vsex2 = False

default annette_sex_pov_toggle = True
default annette_sex_pos_toggle = True

default is_annette_anim_asex = False

screen is_annette_sex_sex1():
    if not is_annette_anim_asex:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action [
                ToggleVariable("annette_sex_pos_toggle"), 
                If(annette_sex_pos_toggle, Jump("is_annette_sex2"), Jump("is_annette_sex1"))
            ]
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op1_idle"
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if is_annette_anim_asex:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("is_annette_sex1")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if mc_suggest_anal_annette:
        if is_annette_anim_vsex1 or is_annette_anim_vsex2:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("is_annette_asex")
            text "Anal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            add "main_choices_op3_idle"
            text "Anal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("is_annette_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene48_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene48_choice01_op1")
    text "\"Get lucky and have fun.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_choice01_op2")
    text "\"I wanted to help this village.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene48_choice01_op3")
    text "\"Just going with the flow.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene48_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene48_choice02_op1")
    text "\"It's part of who she is.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_choice02_op2")
    text "\"As long as she wasn't whoring around, I don't care.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene48_choice02_op3")
    text "\"It depends on the past.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene48_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene48_choice03_op1")
    text "\"Warmth.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_choice03_op2")
    text "\"Honesty.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene48_choice03_op3")
    text "\"A good time.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene48_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene48_choice04_op1")
    text "\"You shouldn't have!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_choice04_op2")
    text "\"Better this way.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene48_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene48_choice05_op1")
    text "\"Let's get straight to it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_choice05_op2")
    text "\"I'd love to feel your breasts first.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

default scene48_tj_speed = False
default scene48_tj_cpov = False

screen scene48_tj():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene48_tj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

default scene48_sex_speed = False
default scene48_sex_cpov = False
default scene48_sex1 = False
default scene48_sex2 = False
screen scene48_sex():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [
            ToggleVariable("scene48_sex_cpov"), 
            If(scene48_sex_cpov, Jump("scene48_sex1"), Jump("scene48_sex2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene48_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"(Yes!)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene48_sex1")
    text "\"(No.).\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene49_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene49_choice01_op1")
    text "Take it":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene49_choice01_op2")
    text "Refuse":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene27_sex02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene27_sex02_op1")
    text "Eat ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene27_sex02_op2")
    text "Eat pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene50_choice01():
    if mc_karma >= 7:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene50_choice01_op1")
        text "Help Alex":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene50_choice01_op1")
        text "Attack Gaius":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene50_choice01_op2")
    text "Do nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene50_choice01_new():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5
    
    if mc_karma >= 7:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≥ 7) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma >= 7:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Return()
        text "Stop and give Alex a hand":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Stop and give Alex a hand":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene50_choice01_op2_new")
    text "Keep attacking Gaius":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene50_ending_screen():
    add "ending_screen_030"
    imagebutton auto "ending_screen_030_continue_%s":
        focus_mask True
        action Return()

screen delayed_sound_loop(sound, delay=1.5):
    timer delay repeat True action Play("sound", sound)

screen scene52_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene52_choice01_op1")
    text "Accept the coin":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene52_choice01_op2")
    text "Decline":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene52_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene52_choice02_op1")
    text "\"I want coin.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene52_choice02_op2")
    text "\"I want... you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene52_choice02_op3")
    text "\"I don't want anything.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene53_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene53_choice01_op1")
    text "\"Let's do it properly, then.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene53_choice01_op2")
    text "\"I'm too tired for that.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
        
screen scene53_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene53_choice02_op1")
    text "Kiss her again":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene53_maia")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene53_bj_speed = False
default scene53_bj_cpov = False
default scene53_bj1 = False
default scene53_bj2 = False
screen scene53_maia1():
    if not scene53_bj_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene53_bj_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene53_bj_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("scene53_bj_cpov"), 
            If(scene53_bj_cpov, Jump("scene53_bj1"), Jump("scene53_bj2"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene53_bj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene53_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene53_choice03_op1")
    text "Tease clit":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene53_choice03_op2")
    text "Spread pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene53_choice03_op3")
    text "\"Spread your legs\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene53_maia2")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

default s53_vsex1 = True
default s53_vsex2 = False

default s53_pov_toggle = True
default s53_speed = False

default s53_asex1 = False
default s53_asex2 = False

default s53_asex_first = True
screen s53_sex():
    if not s53_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("s53_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("s53_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("s53_pov_toggle"), 
            If(s53_pov_toggle, Jump("s53_sex2"), Jump("s53_sex1"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if s53_asex1 or s53_asex2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("s53_vsex1", True), SetVariable("s53_asex1", False), SetVariable("s53_asex2", False), Jump("s53_sex1")]
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    if s53_vsex1 or s53_vsex2:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("s53_asex1", True), SetVariable("s53_vsex1", False), SetVariable("s53_vsex2", False), Jump("s53_sex1")]
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("s53_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen s53_sex2():
    if not s53_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("s53_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("s53_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [
            ToggleVariable("s53_pov_toggle"), 
            If(s53_pov_toggle, Jump("s53_sex2"), Jump("s53_sex1"))
        ]
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if s53_asex1 or s53_asex2:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action [SetVariable("s53_vsex1", True), SetVariable("s53_asex1", False), SetVariable("s53_asex2", False), Jump("s53_sex2")]
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    if s53_vsex1 or s53_vsex2:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action [SetVariable("s53_asex1", True), SetVariable("s53_vsex1", False), SetVariable("s53_vsex2", False), Jump("s53_sex2")]
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("s53_sex_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene54_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene54_choice01_op1")
    text "\"Resolve it peacfully.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene54_choice01_op2")
    text "\"Go to war with Reiner.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene54_choice01_op3")
    text "\"Use Reiner as leverage.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
screen scene54_choice00():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Accept marrying Rebecca":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene54_choice00_op2")
    text "\"I'll protect her, but I don't want to marry her.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene54_choice00_op3")
    text "\"Can I just have a coin reward instead?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene54_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene54_choice02_op1")
    text "Kiss her hand":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene54_choice02_op2")
    text "Kneel and kiss her hand":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene54_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene54_4")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene54_choice03_op2")
    text "Pet her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
screen scene54_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene54_choice04_op1")
    text "Take a peek":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene54_5")
    text "Wait for her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene54_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene54_choice05_op1")
    text "\"I'm not hungry.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene54_choice05_op2")
    text "Take a bite":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default update0_3_1_tasks = True
default update0_3_1_tasks_counter = 0
default update0_3_1_tasks_armor = False
default update0_3_1_tasks_massage = False
default update0_3_1_tasks_tax = False
default update0_3_1_tasks_trial = False
default update0_3_1_tasks_dispute = False

default update0_3_1_tasks_armor_fin = False
default update0_3_1_tasks_massage_fin = False
default update0_3_1_tasks_massage_fin_uncomplete = False
default update0_3_1_tasks_tax_fin = False
default update0_3_1_tasks_trial_fin = False
default update0_3_1_tasks_dispute_fin = False
default update0_3_1_tasks_dispute_fin_success = False


screen update0_3_1_tasks():
    if update0_3_1_tasks:
        if mc_went_date1_reb and not mc_rejected_wedding_reb:
            add "update0_3_1_tasks_choices_main2"
        else:
            add "update0_3_1_tasks_choices_main"

        if not update0_3_1_tasks_armor_fin:
            button:
                focus_mask True
                action [SetVariable("update0_3_1_tasks_armor", True), SetVariable("update0_3_1_tasks", False)]
                add "steward_tasks_op1"
                text "Armor test": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2005 ypos 449 xanchor 0.5 yanchor 0.5
        else:
            text "Armor test": 
                size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2005 ypos 449 xanchor 0.5 yanchor 0.5
            
        if not update0_3_1_tasks_massage_fin:
            button:
                focus_mask True
                action [SetVariable("update0_3_1_tasks_massage", True), SetVariable("update0_3_1_tasks", False)]
                add "steward_tasks_op2"
                text "Massage Request": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2005 ypos 585 xanchor 0.5 yanchor 0.5
        else:
            text "Massage Request": 
                    size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2005 ypos 585 xanchor 0.5 yanchor 0.5

        if not update0_3_1_tasks_tax_fin:
            button:
                focus_mask True
                action [SetVariable("update0_3_1_tasks_tax", True), SetVariable("update0_3_1_tasks", False)]
                add "steward_tasks_op3"
                text "Corrupt Tax Collector": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2005 ypos 729 xanchor 0.5 yanchor 0.5
        else:
            text "Corrupt Tax Collector": 
                size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2005 ypos 729 xanchor 0.5 yanchor 0.5

        if not update0_3_1_tasks_trial_fin:
            button:
                focus_mask True
                action [SetVariable("update0_3_1_tasks_trial", True), SetVariable("update0_3_1_tasks", False)]
                add "steward_tasks_op4"
                text "Drug Trial": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2007 ypos 860 xanchor 0.5 yanchor 0.5
        else:
            text "Drug Trial": 
                size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2007 ypos 860 xanchor 0.5 yanchor 0.5

        if not update0_3_1_tasks_dispute_fin:
            button:
                focus_mask True
                action [SetVariable("update0_3_1_tasks_dispute", True), SetVariable("update0_3_1_tasks", False)]
                add "steward_tasks_op5"
                text "Marriage Dispute": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 995 xanchor 0.5 yanchor 0.5

        else:
            text "Marriage Dispute": 
                size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 995 xanchor 0.5 yanchor 0.5

        if mc_went_date1_reb and not mc_rejected_wedding_reb:
            button:
                focus_mask True
                action Jump("free_roam_reb_main_before")
                add "steward_tasks_op6"
                text "Visit Rebecca": 
                    size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2007 ypos 1140 xanchor 0.5 yanchor 0.5

    if update0_3_1_tasks_armor:
        add "update0_3_1_tasks_armor"
        imagebutton auto "steward_tasks_refuse_%s":
            focus_mask True
            action [SetVariable("update0_3_1_tasks_armor", False), SetVariable("update0_3_1_tasks", True)]
        text "Set aside":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1020 ypos 1250 xanchor 0.5 yanchor 0.5

        imagebutton auto "steward_tasks_accept_%s":
            focus_mask True
            action Jump("scene56")
        text "Accept":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1520 ypos 1250 xanchor 0.5 yanchor 0.5

    if update0_3_1_tasks_massage:
        add "update0_3_1_tasks_massage"
        imagebutton auto "steward_tasks_refuse_%s":
            focus_mask True
            action [SetVariable("update0_3_1_tasks_massage", False), SetVariable("update0_3_1_tasks", True)]
        text "Set aside":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1020 ypos 1250 xanchor 0.5 yanchor 0.5

        imagebutton auto "steward_tasks_accept_%s":
            focus_mask True
            action Jump("scene57")
        text "Accept":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1520 ypos 1250 xanchor 0.5 yanchor 0.5
    
    if update0_3_1_tasks_tax:
        add "update0_3_1_tasks_tax"
        imagebutton auto "steward_tasks_refuse_%s":
            focus_mask True
            action [SetVariable("update0_3_1_tasks_tax", False), SetVariable("update0_3_1_tasks", True)]
        text "Set aside":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1020 ypos 1250 xanchor 0.5 yanchor 0.5

        imagebutton auto "steward_tasks_accept_%s":
            focus_mask True
            action Jump("scene58")
        text "Accept":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1520 ypos 1250 xanchor 0.5 yanchor 0.5

    if update0_3_1_tasks_trial:
        add "update0_3_1_tasks_trial"
        imagebutton auto "steward_tasks_refuse_%s":
            focus_mask True
            action [SetVariable("update0_3_1_tasks_trial", False), SetVariable("update0_3_1_tasks", True)]
        text "Set aside":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1020 ypos 1250 xanchor 0.5 yanchor 0.5

        imagebutton auto "steward_tasks_accept_%s":
            focus_mask True
            action Jump("scene59")
        text "Accept":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1520 ypos 1250 xanchor 0.5 yanchor 0.5
    
    if update0_3_1_tasks_dispute:
        add "update0_3_1_tasks_dispute"
        
        imagebutton auto "steward_tasks_refuse_%s":
            focus_mask True
            action [SetVariable("update0_3_1_tasks_dispute", False), SetVariable("update0_3_1_tasks", True)]
        text "Set aside":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1020 ypos 1250 xanchor 0.5 yanchor 0.5

        imagebutton auto "steward_tasks_accept_%s":
            focus_mask True
            action Jump("scene60")
        text "Accept":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1520 ypos 1250 xanchor 0.5 yanchor 0.5

screen scene56_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene56_choice01_op1")
    text "\"Pussy\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene56_choice01_op2")
    text "\"...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene56_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene56_choice02_op1")
    text "\"That's enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene56_choice02_op2")
    text "\"Now pee...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene57_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene57_choice01_op1")
    text "\"Don't waste my time.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene57_choice01_op2")
    text "Give her a massage":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default scene57_choice02_f = False
default scene57_choice02_b = False

default scene57_choice02_f_first = True
default scene57_choice02_b_first = True

default scene57_choice02_f_soles_first = True
default scene57_choice02_f_toes_first = True
default scene57_choice02_b_breast_first = True
default scene57_choice02_b_nipple_first = True
default scene57_choice02_b_tummy_first = True

default scene57_finish = False

screen s57_hover_areas():
    if scene57_choice02_f:
        add "57_f_sole_hover"
        add "57_f_toes_hover"
    if scene57_choice02_b:
        add "57_f_breast_hover"
        add "57_f_nipple_hover"
        add "57_f_tummy_hover"

screen scene57_choice02():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s57_hover_areas")
        ]
        unhovered [
            Hide("s57_hover_areas")
        ]
    
    if not scene57_choice02_b:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene57_choice02_b")
        text "Look at breasts":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op1_idle"
        text "Look at breasts":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not scene57_choice02_f:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene57_choice02_f")
        text "Look at feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Look at feet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if scene57_finish:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene57_2")
        text "Continue":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    if scene57_choice02_f:
        imagebutton auto "57_f_sole_%s":
            focus_mask True
            action Jump("scene57_choice02_f_soles")
        
        imagebutton auto "57_f_toes_%s":
            focus_mask True
            action Jump("scene57_choice02_f_toes")

    if scene57_choice02_b:
        imagebutton auto "57_f_breast_%s":
            focus_mask True
            action Jump("scene57_choice02_b_breast")
        
        imagebutton auto "57_f_nipple_%s":
            focus_mask True
            action Jump("scene57_choice02_b_nipple")
        
        imagebutton auto "57_f_tummy_%s":
            focus_mask True
            action Jump("scene57_choice02_b_tummy")

screen scene58_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene58_choice01_op1")
    text "Good cop approach":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene58_choice01_op2")
    text "Bad cop approach":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene58_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene58_choice02_op1")
    text "Accept bribe":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene58_choice02_op2")
    text "Send him to the dungeon":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene58_choice02_op3")
    text "\"Return all the money you stole\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene58_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene58_choice03_op1")
    text "\"I want more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene58_choice03_op2")
    text "Take it":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene59_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene59_choice01_op1")
    text "\"Orally.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene59_choice01_op2")
    text "\"Rectally.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene60_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene60_choice01_op1")
    text "Try to resolve it peacefully":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene60_choice01_op2")
    text "Propose divorce":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

default scene61_hj_speed = False
screen scene61_hj():
    if not scene61_hj_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene61_hj_faster")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene61_hj_slower")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene61_hj_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene61_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene61_2")
    text "Get in the bed":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"I have to go...":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene61_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene61_choice02_op1")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"You need to calm down.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene61_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene61_choice03_op1")
    text "\"I'm busy right now.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene61_choice03_op2")
    text "Follow her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
screen scene62_choice01():
    if mc_helped_ruby:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene62_choice01_op1")
        text "Marry her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene62_choice01_op2")
    text "Order life sentence":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene62_choice01_op3")
    text "Order her execution":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene62_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene62_choice02_op1")
    text "I only married you to save you":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Say nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
screen s51_note():
    add "51_note"
    imagebutton auto "update0_2_3_ending_c_%s":
        focus_mask True
        action Return()

screen scene64_free_roam1():
    key "K_UP" action Return()
    imagebutton auto "up_%s":
        focus_mask True
        action Return()

screen scene64_free_roam2():
    key "K_UP" action Return()
    imagebutton auto "up_%s":
        focus_mask True
        action Return()

screen scene64_free_roam3():
    key "K_UP" action Return()
    imagebutton auto "up_%s":
        focus_mask True
        action Return()

screen scene64_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene64_choice01_op1")
    text "\"I have to leave.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice01_op2")
    text "Stay with Maia":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene64_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene64_choice02_op1")
    text "Finger ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice02_op2")
    text "Finger pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene64_choice02_op3")
    text "\"Let's just relax.\" (Remove hand)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
screen scene64_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene64_choice03_op1")
    text "\"You have to drink it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice03_op2")
    text "\"It's fine. You don't have to.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene64_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene64_choice04_op1")
    text "Handjob 1":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice04_op2")
    text "Handjob 2":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene64_choice04_op3")
    text "Fingering":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene64_choice04_op4")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene64_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene64_choice05_op1")
    text "\"You're always beautiful.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice05_op2")
    text "\"I liked your old outfit more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene64_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene64_choice06_op1")
    text "\"I'm not gonna risk it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice06_op2")
    text "Grope her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene64_choice07():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5

    if mc_karma <= 5:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≤ 5) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma <= 5:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene64_choice07_op1")
        text "Grope her ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene64_choice07_op1_fail")
        text "Grope her ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene64_choice07_op2")
    text "Back off":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene66_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene66_choice01_op1")
    text "\"I'll do it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene66_choice01_op2")
    text "\"You need to find someone else.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene66_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene66_choice02_op1")
    text "\"Do a cute pose.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene66_choice02_op2")
    text "\"Polish my boots.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene66_choice02_op3")
    text "\"Nevermind. You can leave.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene67_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene67_choice01_op1")
    text "Give her a silver coin (10 coins)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene67_choice01_op2")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
screen scene68_choice01_1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice01_1_op1")
    text "Inspect body":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice01_1_op2")
    text "Inspect weapon":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene68_choice01_1_op3")
    text "Inspect personality":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene68_choice01_1_op4")
    text "Judge":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    
screen scene68_choice02_1_j():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice02_1_op1")
    text "\"In.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice02_1_op2")
    text "\"Out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene68_choice01_2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice01_2_op1")
    text "Inspect body":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice01_2_op2")
    text "Inspect weapon":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene68_choice01_2_op3")
    text "Inspect... breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene68_choice01_2_op4")
    text "Judge":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    
screen scene68_choice02_2_j():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice02_2_op1")
    text "\"In.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice02_2_op2")
    text "\"Out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene68_choice01_3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice01_3_op1")
    text "Inspect body":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice01_3_op2")
    text "Inspect weapon":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene68_choice01_3_op3")
    text "Inspect personality":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene68_choice01_3_op4")
    text "Judge":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    
screen scene68_choice02_3_j():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice02_3_op1")
    text "\"In.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice02_3_op2")
    text "\"Out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene68_choice02_4_j():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice02_4_op1")
    text "\"In.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice02_4_op2")
    text "\"Out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene68_choice02_5_j():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene68_choice02_5_op1")
    text "\"In.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene68_choice02_5_op2")
    text "\"Out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene69_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene69_choice01_op1")
    text "\"I'm interested...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene69_choice01_op2")
    text "Slap her hand away":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene69_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene69_choice02_op1")
    text "Blowjob 1":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene69_choice02_op2")
    text "Blowjob 2":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene69_choice02_op3")
    text "Blowjob 3":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene69_choice02_op4")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene70_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene70_choice01_op1")
    text "Offer foot massage":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene70_choice01_op2")
    text "\"Good luck with that.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene70_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene70_choice02_op1")
    text "Finish":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene70_choice02_op2")
    text "Put toes in mouth":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen test():
    imagebutton auto "gallery_gui_scene_box6_c5_%s":
        focus_mask True
        action [SetVariable("in_scene_replay", True), Replay("is_reb_fj1_00000")]


screen scene71_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene71_choice01_op1")
    text "\"I like being led.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene71_choice01_op2")
    text "\"In between.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene71_choice01_op3")
    text "\"I like to take charge.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
        
screen scene71_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene71_choice02_op1")
    text "\"You're on!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene71_choice02_op2")
    text "\"Let's play without the prize.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene71_choice02_op3")
    text "\"I don't want to play.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene72_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene72_choice01_op1")
    text "Roll dice for better loot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_choice01_op2")
    text "\"Just loot it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene72_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene72_choice02_op1")
    text "Roll dice for better loot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_choice02_op2")
    text "\"Just loot it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene72_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene72_choice03_op1")
    text "Roll dice to help them":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_choice03_op2")
    text "\"Nah, let them enjoy.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene72_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s72_dMAIN")
    text "Return to the main chamber":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"Not yet.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene72_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene72_choice05_op1")
    text "Roll dice to resist temptation":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_choice05_op2")
    text "\"I give in...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene72_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene72_choice06_op1")
    text "Roll dice for better loot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_choice06_op2")
    text "\"Just loot it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene72_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Cuddle with Rebecca":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_choice07_op2")
    text "\"I have other things to do.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen rnr_map():
    add "rnr_map"
    if in_rnr_1:
        add "rnr_map_point1"
    elif in_rnr_2:
        add "rnr_map_point2"
    elif in_rnr_3:
        add "rnr_map_point3"
    elif in_rnr_4:
        add "rnr_map_point4"
    elif in_rnr_5:
        add "rnr_map_point5"
    elif in_rnr_6:
        add "rnr_map_point6"
    elif in_rnr_7:
        add "rnr_map_point7"
    elif in_rnr_8:
        add "rnr_map_point8"
    elif in_rnr_9:
        add "rnr_map_point9"
    elif in_rnr_10:
        add "rnr_map_point10"
    elif in_rnr_11:
        add "rnr_map_point11"
    elif in_rnr_12:
        add "rnr_map_point12"
    elif in_rnr_13:
        add "rnr_map_point13"
    elif in_rnr_14:
        add "rnr_map_point14"
    elif in_rnr_15:
        add "rnr_map_point15"
    elif in_rnr_16:
        add "rnr_map_point16"
    elif in_rnr_17:
        add "rnr_map_point17"
    elif in_rnr_18:
        add "rnr_map_point18"
    elif in_rnr_19:
        add "rnr_map_point19"
    elif in_rnr_20:
        add "rnr_map_point20"
    elif in_rnr_21:
        add "rnr_map_point21"
    elif in_rnr_22:
        add "rnr_map_point22"
    elif in_rnr_23:
        add "rnr_map_point23"
    elif in_rnr_24:
        add "rnr_map_point24"

    if rnr_shrine_goblin:
        add "rnr_map_ll_shrine_green"
    elif not rnr_shrine_goblin and not s72_dLEFT_LEFT_shrine_first:
        add "rnr_map_ll_shrine_red"

    if rnr_shrine_werewolf:
        add "rnr_map_shrine2_green"
    elif not rnr_shrine_werewolf and not s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_first:
        add "rnr_map_shrine2_red"

    if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_done:
        add "rnr_map_shrine3_green"
    elif not s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_done and not s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine_first:
        add "rnr_map_shrine3_red"
    
    if s72_dRIGHT_RIGHT_shrine_lit:
        add "rnr_map_shrine4_green"
    elif not s72_dRIGHT_RIGHT_shrine_lit and not s72_dRIGHT_RIGHT_shrine_first:
        add "rnr_map_shrine4_red"

    if rnr_shrine_spider:
        add "rnr_map_shrine5_green"
    elif not rnr_shrine_spider and not s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_first:
        add "rnr_map_shrine5_red"
    
    if rnr_shrines == 5:
        add "rnr_map_main_green"

screen s72_dMAIN():
    use rnr_map

    key "K_UP" action Jump("s72_dMAIN_note")
    key "K_LEFT" action Jump("s72_dLEFT")
    key "K_RIGHT" action Jump("s72_dRIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dMAIN_note")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT")

screen s72_dLEFT():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT")
    key "K_DOWN" action Jump("s72_dMAIN")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"
    
    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dMAIN")

screen s72_dRIGHT():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT")
    key "K_DOWN" action Jump("s72_dMAIN")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dMAIN")

screen s72_dLEFT_LEFT():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT_LEFT")
    key "K_LEFT" action Jump("s72_dLEFT_LEFT_shrine")
    key "K_RIGHT" action Jump("s72_dLEFT_LEFT_cat")
    key "K_DOWN" action Jump("s72_dLEFT")


    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_shrine")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_cat")
    
screen s72_dLEFT_LEFT_LEFT():
    use rnr_map

    key "K_RIGHT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT")


    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if s72_dLEFT_LEFT_LEFT_chest:
        imagebutton auto "72_d6_chest_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_chest")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT")

screen s72_dLEFT_LEFT_LEFT_RIGHT():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP")
    key "K_RIGHT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT")

screen s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT():
    use rnr_map

    key "K_LEFT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT")

screen s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT():
    use rnr_map

    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT_chest:
        imagebutton auto "72_d10_chest_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT_LEFT_chest")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_RIGHT")

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP")
    key "K_LEFT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT")

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT():
    use rnr_map

    key "K_LEFT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta")
    key "K_RIGHT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_tenta")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP")

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_poster:
        imagebutton auto "72_d14_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_poster")

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP")

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP():
    use rnr_map

    key "K_RIGHT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP")

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT():
    use rnr_map
    
    key "K_UP" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_UP")
    key "K_LEFT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine")
    key "K_RIGHT" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_groblin")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_UP")

        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_groblin")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_shrine")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP")

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT_UP():
    use rnr_map

    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_UP_UP_RIGHT")

screen s72_dLEFT_LEFT_cat():
    use rnr_map

    key "K_DOWN" action Jump("s72_dLEFT_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT")

screen s72_dLEFT_LEFT_shrine():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT_shrine_fight")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_shrine_fight")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT")

screen s72_dLEFT_LEFT_shrine_fight():
    use rnr_map

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if rnr_wrong_choices:
        if not scene72_rnr_shrine1_op1:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene72_rnr_shrine1_op1")
            text "\"A wide swing!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        if not scene72_rnr_shrine1_op2:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene72_rnr_shrine1_op2")
            text "\"Try to reason with it!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    if not scene72_rnr_shrine1_op3:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene72_rnr_shrine1_op3")
        text "\"A precise, downward chop!\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine():
    use rnr_map

    key "K_UP" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight")
    key "K_DOWN" action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()
            
    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT")


screen s72_dLEFT_LEFT_LEFT_RIGHT_UP_LEFT_shrine_fight():
    use rnr_map
    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if not scene72_rnr_shrine2_op1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene72_rnr_shrine2_op1")
        text "\"Flank him, Becky!\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    if rnr_wrong_choices:
        if not scene72_rnr_shrine2_op2:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene72_rnr_shrine2_op2")
            text "\"Sweep the legs!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
        
        if not scene72_rnr_shrine2_op3:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("scene72_rnr_shrine2_op3")
            text "\"A wild spinning splash!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen s72_dRIGHT_RIGHT():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_RIGHT")
    key "K_LEFT" action Jump("s72_dRIGHT_RIGHT_key")
    key "K_RIGHT" action Jump("s72_dRIGHT_RIGHT_shrine")
    key "K_DOWN" action Jump("s72_dRIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT")

        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_shrine")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_key")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT")

screen s72_dRIGHT_RIGHT_shrine():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_shrine_fight")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_shrine_fight")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT")

screen s72_dRIGHT_RIGHT_shrine_fight():
    use rnr_map
    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30
        
    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if rnr_wrong_choices:
        if not scene72_rnr_shrine4_op1:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene72_choice04_op1")
            text "\"Disarm it!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        if not scene72_rnr_shrine4_op3:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene72_choice04_op3")
            text "\"Shatter its leg!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene72_choice04_op2")
    text "\"Cleave it right down the middle!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen s72_dRIGHT_RIGHT_RIGHT():
    use rnr_map

    key "K_LEFT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    imagebutton auto "72_d20_chest_%s":
        focus_mask True
        keyboard_focus False
        action Jump("s72_d20_chest")

    if s72_dRIGHT_RIGHT_RIGHT_poster:
        imagebutton auto "72_d20_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_poster")

    if free_roam_arrows:
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP():
    use rnr_map

    key "K_LEFT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT")
    key "K_RIGHT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT():
    use rnr_map

    key "K_RIGHT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT_statue")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_RIGHT_statue")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_poster:
        imagebutton auto "72_d24_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_poster")

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT():
    use rnr_map

    key "K_RIGHT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_chest:
        imagebutton auto "72_d26_chest_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_chest")

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_UP")
    key "K_LEFT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider")
    key "K_RIGHT" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_UP")

        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_witch")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_UP():
    use rnr_map

    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider():
    use rnr_map

    key "K_UP" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight")
    key "K_DOWN" action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP")

    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30

    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP")

screen s72_dRIGHT_RIGHT_RIGHT_LEFT_UP_LEFT_LEFT_LEFT_UP_spider_fight():
    use rnr_map
    add "rnr_health_main"
    text "Vitality: [rnr_health]" size 45 color "#FFFFFF" xpos 0.033 ypos 0.174 font "Lora-VariableFont_wght.ttf"

    if screen_tooltip:
        frame:
            pos (renpy.get_mouse_pos()[0] + 20, renpy.get_mouse_pos()[1] + 20)
            background Solid("#000000CC")
            padding (10, 5)
            text screen_tooltip:
                color "#FFFFFF"
                size 30
        
    if rnr_rune1 and not rnr_rune1_used:
        imagebutton auto "rnr_rune_insight_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Can be Used During Fights to Show The Correct Action")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(store, "rnr_wrong_choices", False)
                    or setattr(store, "rnr_rune1_used", True)
                    or setattr(store, "screen_tooltip", "")
                ) if rnr_in_fight else renpy.notify("You're not in a fight!")
            )

    if rnr_rune2 and not rnr_rune2_used:
        imagebutton auto "rnr_rune_secondlife_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Will be Used Automatically to Revive You Upon Death")
            unhovered SetVariable("screen_tooltip", "")
            action NullAction()

    if rnr_potion1:
        imagebutton auto "rnr_potion1_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion1", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )
        
    if rnr_potion2:
        imagebutton auto "rnr_potion2_%s":
            focus_mask True
            keyboard_focus False
            hovered SetVariable("screen_tooltip", "Restores 5 Vitality Points")
            unhovered SetVariable("screen_tooltip", "")
            action Function(
                lambda: (
                    setattr(
                        store,
                        "rnr_health",
                        min(rnr_health + 5,
                            30 if (rnr_wand and rnr_bracers)
                            else 25 if (rnr_bracers or rnr_wand)
                            else 20
                        )
                    )
                    or setattr(store, "rnr_potion2", False)
                    or setattr(store, "screen_tooltip", "")
                )
                if rnr_health < (
                    30 if (rnr_wand and rnr_bracers)
                    else 25 if (rnr_bracers or rnr_wand)
                    else 20
                )
                else renpy.notify("You're already at full health.")
            )

    if rnr_wrong_choices:
        if not scene72_rnr_shrine5_op1:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene72_rnr_shrine5_op1")
            text "\"Aim for the mouth.\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
        if not scene72_rnr_shrine5_op2:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("scene72_rnr_shrine5_op2")
            text "\"Aim for the legs!\"":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene72_rnr_shrine5_op3")
    text "\"Charge straight in! Go for the belly!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene73_choice01():
    add "is_maia_choices_main"

    if not scene73_choice_clothes:
        button:
            focus_mask True
            action Jump("scene73_choice01_op1") 
            add "free_roam_maia_op1"
            text "Cum on clothes": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5
    else:
        text "Cum on clothes": 
            size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2017 ypos 378 xanchor 0.5 yanchor 0.5

    if not scene73_choice_face:
        button:
            focus_mask True
            action Jump("scene73_choice01_op2") 
            add "free_roam_maia_op2"
            text "Cum on face": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5
    else:
        text "Cum on face": 
            size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 520 xanchor 0.5 yanchor 0.5

    if not scene73_choice_breasts:
        button:
            focus_mask True
            action Jump("scene73_choice01_op3")
            add "free_roam_maia_op3"
            text "Cum on breasts": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5
    else:
        text "Cum on breasts": 
            size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 657 xanchor 0.5 yanchor 0.5

    if not scene73_choice_belly:
        button:
            focus_mask True
            action Jump("scene73_choice01_op4")
            add "free_roam_maia_op4"
            text "Cum on belly": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 795 xanchor 0.5 yanchor 0.5
    else:
        text "Cum on belly": 
            size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 795 xanchor 0.5 yanchor 0.5

    if not scene73_choice_feet:
        button:
            focus_mask True
            action Jump("scene73_choice01_op5")
            add "free_roam_maia_op5"
            text "Cum on feet": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 933 xanchor 0.5 yanchor 0.5
    else:
        text "Cum on feet": 
            size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 933 xanchor 0.5 yanchor 0.5

    if scene73_choices >= 3:
        button:
            focus_mask True
            action Jump("scene73_choice01_op6")
            add "free_roam_maia_op6"
            text "Finish": 
                size persistent.free_roam_choices_text_size color "#fff" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 1070 xanchor 0.5 yanchor 0.5
    else:
        text "Finish": 
            size persistent.free_roam_choices_text_size color "#818181" hover_color "#851737" font "candara_bold.ttf" xpos 2015 ypos 1070 xanchor 0.5 yanchor 0.5

screen scene73_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene73_choice02_op1")
    text "Dominate her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene73_choice02_op2")
    text "Let her rest":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene73_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene73_choice03_op2")
    text "\"...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene73_choice03_op1")
    text "Spank her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene73_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene75_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene75")
    text "Give her a massage":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"You should sleep it off instead\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

default s75_s5_part2 = False
default s75_s5_shoulder = False
default s75_s5_lback = False
default s75_s5_butt = False
default s75_s5_thighs = False
default s75_s5_feet = False
default s75_massage_counter = 0


screen s75_hover_areas():
    if not s75_s5_part2:
        if not s75_s5_shoulder:
            add "75_s5_shoulder_hover"
        if not s75_s5_lback:
            add "75_s5_lback_hover"
    else:
        if not s75_s5_butt:
            add "75_s5_butt_hover"
        if not s75_s5_thighs:
            add "75_s5_thighs_hover"
        if not s75_s5_feet:
            add "75_s5_feet_hover"

screen scene75_choice02():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s75_hover_areas")
        ]
        unhovered [
            Hide("s75_hover_areas")
        ]

    if not s75_s5_part2:
        if not s75_s5_shoulder:
            imagebutton auto "75_s5_shoulder_%s":
                focus_mask True
                action Jump("scene75_choice02_op1") 
        
        if not s75_s5_lback:
            imagebutton auto "75_s5_lback_%s":
                focus_mask True
                action Jump("scene75_choice02_op2") 

    else:
        if not s75_s5_butt:
            imagebutton auto "75_s5_butt_%s":
                focus_mask True
                action Jump("scene75_choice02_op3")
        
        if not s75_s5_thighs:
            imagebutton auto "75_s5_thighs_%s":
                focus_mask True
                action Jump("scene75_choice02_op4")
        
        if not s75_s5_feet:
            imagebutton auto "75_s5_feet_%s":
                focus_mask True
                action Jump("scene75_choice02_op5")
    
    if s75_massage_counter >= 4:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene75_2")
        text "Continue":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene75_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene75_4")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene75_3")
    text "\"We really shouldn't.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene75_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene75_choice04_op1")
    text "Kiss pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene75_choice04_op2")
    text "Kiss anus":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene75_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene75_choice05_op1")
    text "\"Let's go with anal.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene75_choice05_op2")
    text "\"We should do it normally for your first time.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500


screen scene75_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene75_choice06_op1")
    text "Doggystlye 1":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene75_choice06_op2")
    text "Doggystlye 2":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene75_choice06_op3")
    text "Missionary":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene75_choice06_op4")
    text "Missionary (Kissing)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene75_choice06_op5")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene75_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene75_choice07_op2")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene75_choice07_op1")
    text "Cum on face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene76_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene76_choice01_op1")
    text "Smoke":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene76_choice01_op2")
    text "\"Nah.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 

screen update_0_3_3end():
    add "update_0_3_3end"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Return()

screen scene79_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene79_choice01_op2")
    text "Let her go":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene79_choice01_op1")
    text "Slap her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene79_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene79_1")
    text "Leave the castle":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene79_2")
    text "Stay":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene79_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene79_choice03_op2")
    text "Break down the door":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene79_choice03_op1")
    text "Sneak through the back":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene79_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene79_choice04_op2")
    text "\"Show me the way, Negumi.":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene79_choice04_op1")
    text "Punch him":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene79_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene79_choice05_op2")
    text "\"No. You stay here.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene79_choice05_op1")
    text "\"Fine. Lead the way.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene81_choice00():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5

    if mc_karma <= 3:
        add "choice_unlocked"
    else:
        add "choice_locked"

    text "Honor (LVL ≤ 3) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5
    
    if mc_karma <= 3:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene82_choice04_op2")
        text "\"Coin's safer in my pocket.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene82_choice04_op2_woah")
        text "\"Coin's safer in my pocket.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice04_op1")
    text "Pay her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene81_choice00_op3")
    text "Back off":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene81_choice000():
    imagebutton auto "scene81_choice00_op1_2_%s":
        focus_mask True
        action Return()

    imagebutton auto "scene81_choice00_op2_2_%s":
        focus_mask True
        action Jump("scene81_choice00_op3")
    

screen scene81_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene81_choice01_op1")
    text "\"I'm sorry you had to go through this.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene81_choice01_op2")
    text "\"Get yourself together! (Slap her)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

screen scene81_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene81_choice02_op1")
    text "\"How can I even help?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene81_choice02_op2")
    text "\"I don't think I can trust you anymore.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene81_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene81_choice03_op1")
    text "\"Let's break the world.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene81_choice03_op2")
    text "\"You still have to earn my trust.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    if not mc_slap_alex or not mc_angry_alex:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene81_choice03_op3")
        text "Kiss her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Kiss her":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene82_choice_maia():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice_maia_op1")
    text "\"I've already told her that I wouldn't be monogamous.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice_maia_op2")
    text "\"She's the only one for me.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene82_choice_maia_op3")
    text "\"We didn't talk about it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene82_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice01_op1")
    text "\"Because I want you to be my servant.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice01_op2")
    text "\"It's nothing. I was just wondering.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene82_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice02_op1")
    text "\"Just taking basic care of me. Nothing more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice02_op2")
    text "\"Serving me however I wish.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene82_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice03_op1")
    text "Release her gently":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice03_op2")
    text "Squeeze her hand":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene82_choice04():
    imagebutton auto "scene82_choice04_op1_%s":
        focus_mask True
        action Jump("scene82_choice04_op1")
    
    imagebutton auto "scene82_choice04_op2_%s":
        focus_mask True
        action Jump("scene82_choice04_op2")

screen scene82_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice05_op1")
    text "\"I want you to keep me warm.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if mc_harem_reham_dom_dom:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene82_choice05_op2")
        text "\"Nothing for now.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene82_choice05_op2")
        text "\"Nothing for now.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene82_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice06_op1")
    text "Deny her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice06_op2")
    text "Make her beg for it":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene82_reham1():
    if not scene82_reham1_speed:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene82_reham1_fast")
        text "Faster":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene82_reham1_slow")
        text "Slower":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_reham1_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene82_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice07_op1")
    text "\"Go ahead.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice07_op2")
    text "\"No. It's enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene82_reham2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_reham2_hj1")
    text "Handjob 1":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_reham2_hj2")
    text "Handjob 2":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene82_reham2_hj_feet")
    text "Handjob 1 (Feet smother)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene82_reham2_hj_pro")
    text "Handjob 3 (Prostate stimulation)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene82_reham2_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene82_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice08_op1")
    text "Take a rest":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice08_op2")
    text "Tease her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene82_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice09_op1")
    text "\"Are you jealous?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice09_op2")
    text "\"So what?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene82_choice09_op3")
    text "Apologize":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene82_choice10():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice10_op1")
    text "\"Listen to Reham. Go back inside.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice10_op2")
    text "\"Maia can stay. Let her be.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene82_choice11():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene82_choice11_op1")
    text "Spank her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene82_choice11_op2")
    text "Carry her inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene83_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene83_choice01_op1")
    text "\"We'll rescue the princess now.\" (Agree with Alex)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene83_choice01_op2")
    text "\"We don't need the risk.\" (Agree with Reham)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene84_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_choice01_op1")
    text "\"You being with me is the most important role.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_choice01_op2")
    text "\"I'll find you something.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene84_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_choice02_op1")
    text "\"I prefer things the way they are.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_choice02_op2")
    text "\"Yeah, that sounds nice.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene84_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_choice03_op1")
    text "Kiss her harder":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_choice03_op2")
    text "\"We shouldn't do this now.":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene84_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_choice04_op1")
    text "\"'Sir' is fine.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_choice04_op2")
    text "\"Call me by my name.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene84_choice04_op3")
    text "\"How about 'Master'?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene84_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_choice05_op1")
    text "Vaginal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_choice05_op2")
    text "Anal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene84_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("s84_cum_inside", True), Return()]
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("s84_cum_outside", True), Return()]
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

default s84_maia4_a = False
default s84_maia4_v = False

screen scene84_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_choice07_op1")
    text "Let her rest":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("s84_maia4_a", True), Jump("scene84_choice07_op2")]
    text "Slam into her ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action [SetVariable("s84_maia4_v", True), Jump("scene84_choice07_op2")]
    text "Slam into her pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene84_maia():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_maia_op1")
    text "Lick pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_maia_op2")
    text "Lick anus":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene84_maia2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_maia2_op1")
    text "\"Hold it in.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene84_maia2_op2")
    text "\"Let it out. It's fine.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene84_maia3():
    if not scene84_maia3_bj:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene84_maia3_pov")
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op1_idle"
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not scene84_maia3_bj:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene84_maia3_bj")
        text "Blowjob":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Blowjob":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not s84_maia3_v:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene84_maia3_vag")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if not s84_maia3_a:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene84_maia3_anal")
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op4_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene84_maia3_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene84_maia4():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene84_maia4_pov")
    text "Change POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if not s84_maia4_v:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene84_maia4_v")
        text "Vaginal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op2_idle"
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not s84_maia4_a:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene84_maia4_a")
        text "Anal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        add "main_choices_op3_idle"
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene84_maia4_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen update_0_4_0end():
    add "update_0_4_0end"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Jump("Update0_4_0_end")
              

screen scene85_choice1():
    if mc_console_maia:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene85_choice01_op1")
        text "Kiss Maia":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene85_choice01_op2")
        text "Kiss Reham":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True


        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene85_choice01_op3")
        text "Kiss both":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene85_choice01_op4")
        text "Leave":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene85_choice01_op2")
        text "Kiss her": 
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene85_choice01_op4")
        text "Leave":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene86_choice1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene86_choice01_op1")
    text "\"You stink\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene86_choice01_op2")
    text "Say nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene86_choice2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene86_choice02_op1")
    text "Hold her shoulder":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene86_choice02_op2")
    text "Hold her waist":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene86_choice3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene86_choice03_op1")
    text "\"Yes, with all my heart.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene86_choice03_op2")
    text "\"I have to believe.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene86_choice03_op3")
    text "\"We don't have a choice.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene87_choice1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene87_choice01_op1")
    text "\"I actually don't mind it!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene87_choice01_op2")
    text "\"You first. Get off.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene87_choice2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene87_choice02_op1")
    text "Attack":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene87_choice02_op2")
    text "\"Start talking.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene87_choice3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene87_choice03_op1")
    text "\"Calm down. I'll think about it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene87_choice03_op2")
    text "\"I don't want to attract more trouble.":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

screen scene87_choice4():
    if not scene87_live:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene87_choice04_op1")
        text "\"Where does he live?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "\"Where does he live?\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    if not scene87_describe:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene87_choice04_op2")
        text "\"Describe him to me.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "\"Describe him to me.\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    if not scene87_ask_prize:
        imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("scene87_choice04_op3")
        text "\"What's my prize?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op3_%s":
                focus_mask True
        text "\"What's my prize?\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

    if scene87_live and scene87_describe:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene87_choice04_op4")
        text "\"That's all I need to know.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "\"(I need to know more...)\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5

screen scene88_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene88_choice01_op1")
    text "Toss a coin to him":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene88_choice01_op2")
    text "\"Some of your details seem off.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene88_choice01_op3")
    text "Walk away":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene89_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene89_choice01_op1")
    text "Approach quietly":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene89_choice01_op2")
    text "Give her a spank":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
screen scene89_choice02():
    if not mc_choose_not_amelia:
        if quest_witch_amelia_dead:
            text "Amelia is dead" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5
            add "choice_locked"
        else:
            if quest_witch_amelia_alive_free:
                text "Amelia is alive and free" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5
                add "choice_unlocked"
            else:
                text "Amelia is captured" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5
                add "choice_locked"

    if quest_witch_amelia_alive_free:
        if not mc_choose_not_amelia:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene89_choice02_op1")
            text "Choose Amelia the witch":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene89_choice02_op1_2")
        text "Choose Amelia the witch":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene89_choice02_op2")
    text "Choose Ava the royal examiner":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene89_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene89_choice03_op1")
    text "\"I still want her help.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene89_choice03_op2")
    text "\"You're right. I should think this more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5  textalign 0.5 xmaximum 500

screen scene90_choice1():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene90_choice01_op1")
    text "Stand behind her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not mc_dont_getit:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene90_choice01_op2")
        text "\"What are you doing?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene90_choice01_op2_2")
        text "\"I still don't get it...?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene90_choice01_op3")
    text "\"Stop. This isn't a good time.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

default scene90_remove_skirt = False
screen scene90_choice2():
    if not scene90_remove_skirt:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene90_choice02_op1")
        text "Remove skirt":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene90_choice02_op4")
        text "Finger anus":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene90_choice02_op2")
    text "Grope breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene90_choice02_op3")
    text "Remove shoe":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if scene90_remove_skirt:
        imagebutton auto "main_choices_op4_%s":
                focus_mask True
                action Jump("scene90_choice02_op5")
        text "Finger pussy":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    if scene90_remove_skirt and scene90_choice02_op4_first:
        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action Jump("scene90_choice02_op6")
        text "Pull out your cock":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene90_choice3():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene90_choice03_op1")
    text "\"Please!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene90_choice03_op2")
    text "\"I don't want you to do it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene90_choice4():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene90_choice04_op1")
    text "Caress foot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene90_choice04_op2")
    text "Sniff foot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene90_choice04_op3")
    text "Stand up":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene91_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice01_op1")
    text "Suggest chainmail armor":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice01_op2")
    text "Suggest hardened leather armor":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene91_choice01_op3")
    text "Suggest hide armor":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene91_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice02_op1")
    text "\"You want to... have sex with me?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice02_op2")
    text "\"You want to... show me your feet?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene91_choice02_op3")
    text "\"You want to... show me your breasts?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400

screen scene91_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice03_op1")
    text "\"Deal. Show me those breasts.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice03_op2")
    text "\"No. You'll pay the full price.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene91_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice04_op1")
    text "\"Get out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice04_op2")
    text "\"We'll do it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene91_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice05_op1")
    text "\"If Gaius falls, it'll be by my blade.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice05_op2")
    text "\"I was actually hoping to recruit Gaius.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene91_choice05_op3")
    text "\"Good. Let them tear each other apart.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene91_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice06_op1")
    text "\"Don't go. True friends won't gamble with your life.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice06_op2")
    text "\"Go with them. Prove your courage.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene91_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice07_op1")
    text "Take the coin":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice07_op2")
    text "\"Keep it for yourself, Yuuhi.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene91_choice08():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5

    if mc_karma >= 8:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≥ 8) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma >= 8:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene91_choice08_op1")
        text "\"I'll pay you back by restoring this city.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene91_choice08_op1_2")
        text "\"I'll pay you back by restoring this city.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice08_op2")
    text "\"It's a deal.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene91_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene91_choice09_op1")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene91_choice09_op2")
    text "\"Goodbye, Yuuhi.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene92_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene92_choice01_op1")
    text "\"Do what you wish to me!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene92_choice01_op2")
    text "\"I changed my mind...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene92_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene92_choice02_op1")
    text "\"Nevermind, I'll do what you say.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene92_choice02_op2")
    text "\"Find someone else. I'm still leaving.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene92_choice02_op3")
    text "Attack":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene93_free_roam():
    key "K_UP" action Jump("scene93_free_roam_up")
    key "K_LEFT" action Jump("scene93_free_roam_left")
    key "K_RIGHT" action Jump("scene93_free_roam_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

        
    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_right")
    
screen s93_hover_areas1():
    add "93_cage_hover"

screen scene93_free_roam_left():
    key "K_DOWN" action Jump("scene93")
    if not scene93_free_roam_pixie_first:
        imagebutton:
            idle "interact_indicator2_idle"
            hover "interact_indicator2_hover"
            keyboard_focus False
            focus_mask True
            action NullAction()
            hovered [
                Show("s93_hover_areas1")
            ]
            unhovered [
                Hide("s93_hover_areas1")
            ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        if not scene93_free_roam_pixie_first:
            imagebutton auto "93_cage_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene93_free_roam_pixie")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93")
    
screen s93_hover_areas2():
    add "93_device_hover"

screen scene93_free_roam_right():
    key "K_DOWN" action Jump("scene93")
    imagebutton:
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s93_hover_areas2")
        ]
        unhovered [
            Hide("s93_hover_areas2")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "93_device_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_right_device")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93")

screen s93_hover_areas3():
    add "93_door_hover"

screen scene93_free_roam_up():
    key "K_UP" action Jump("scene93_free_roam_end")
    key "K_LEFT" action Jump("scene93_free_roam_up_left")
    key "K_RIGHT" action Jump("scene93_free_roam_up_right")
    key "K_DOWN" action Jump("scene93")

    imagebutton:
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s93_hover_areas3")
        ]
        unhovered [
            Hide("s93_hover_areas3")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "93_door_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_door")
        
        imagebutton auto "free_roam_end2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_end")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_right")


screen s93_hover_areas4():
    add "93_could_hover"
    add "93_skull_hover"

screen scene93_free_roam_up_right():
    key "K_DOWN" action Jump("scene93_free_roam_up")

    imagebutton:    
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s93_hover_areas4")
        ]
        unhovered [
            Hide("s93_hover_areas4")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene93_free_roam_up_right_poster:
        imagebutton auto "93_s8_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_right_poster")

    if free_roam_arrows:
        imagebutton auto "93_could_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_right_could")
        
        imagebutton auto "93_skull_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_right_skull")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up")

screen s93_hover_areas5():
    add "93_ball_hover"
    add "93_chalice_hover"
    add "93_book_hover"

screen scene93_free_roam_up_left():
    key "K_DOWN" action Jump("scene93_free_roam_up")

    imagebutton:
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s93_hover_areas5")
        ]
        unhovered [
            Hide("s93_hover_areas5")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "93_ball_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_left_ball")
        
        imagebutton auto "93_chalice_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_left_chalice")
        
        imagebutton auto "93_book_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up_left_book")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene93_free_roam_up")

screen scene93_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Return()
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene94")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5

screen scene94_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene94_choice01_op1")
    text "\"Please!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene94_choice01_op2")
    text "\"I don't want that!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene94_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene94_2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene94_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene94_choice03_op1")
    text "Beg desperately":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene94_choice03_op2")
    text "Say nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene94_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene94_4")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene94_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene95_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene95_choice01_op1")
    text "\"I'd love to impregnate you myself.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene95_choice01_op2")
    text "\"Just keep it a souvineer.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene95_choice01_op3")
    text "\"It's a stupid idea. I'd never want that to happen.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600

screen scene95_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene95_choice02_op1")
    text "\"You're too close. Back off.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene95_choice02_op2")
    text "Say nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene97_free_roam():
    key "K_UP" action Jump("scene97_free_roam_up")
    key "K_LEFT" action Jump("scene97_free_roam_left")
    key "K_RIGHT" action Jump("scene97_free_roam_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:        
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_up")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_right")


screen s97_hover_areas1():
    add "97_drawer_hover"

screen scene97_free_roam_left():
    key "K_DOWN" action Jump("scene97")

    if not mc_angry_kat1 and not scene97_drawer_first:
        imagebutton:
            idle "interact_indicator2_idle"
            hover "interact_indicator2_hover"
            keyboard_focus False
            focus_mask True
            action NullAction()
            hovered [
                Show("s97_hover_areas1")
            ]
            unhovered [
                Hide("s97_hover_areas1")
            ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        if not mc_angry_kat1 and not scene97_drawer_first:
            imagebutton auto "97_drawer_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene97_drawer")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97")

screen s97_hover_areas2():
    add "97_drawer_pantie1_hover"
    add "97_drawer_pantie2_hover"

screen scene97_drawer():
    key "K_DOWN" action Jump("scene97_free_roam_left")

    imagebutton:
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s97_hover_areas2")
        ]
        unhovered [
            Hide("s97_hover_areas2")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "97_drawer_pantie1_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_drawer_pantie1")
        
        imagebutton auto "97_drawer_pantie2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_drawer_pantie2")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_left")

screen scene97_free_roam_right():
    key "K_DOWN" action Jump("scene97")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene97_free_roam_right_poster:
        imagebutton auto "97_s3_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_right_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97")

screen scene97_pantie():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene97_drawer_pantie2_2")
    text "Sniff panties":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Put them back":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen s97_hover_areas3():
    add "97_feet_hover"

screen scene97_free_roam_up():
    key "K_UP" action Jump("scene97")
    key "K_LEFT" action Jump("scene97_free_roam_up_left")
    key "K_RIGHT" action Jump("scene97_free_roam_up_right")
    key "K_DOWN" action Jump("scene97")

    imagebutton:
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s97_hover_areas3")
        ]
        unhovered [
            Hide("s97_hover_areas3")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "free_roam_end2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_end")

        imagebutton auto "97_feet_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_feet")
        
        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_up_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_up_right")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97")

screen s97_hover_areas4():
    add "97_kat_hover"

screen scene97_free_roam_up_left():
    key "K_DOWN" action Jump("scene97_free_roam_up")

    imagebutton:
        idle "interact_indicator2_idle"
        hover "interact_indicator2_hover"
        keyboard_focus False
        focus_mask True
        action NullAction()
        hovered [
            Show("s97_hover_areas4")
        ]
        unhovered [
            Hide("s97_hover_areas4")
        ]

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if free_roam_arrows:
        imagebutton auto "97_kat_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_kat")
        
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_up")

screen scene97_free_roam_up_right():
    key "K_DOWN" action Jump("scene97_free_roam_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene97_free_roam_up_right_poster:
        imagebutton auto "97_s6_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_up_right_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene97_free_roam_up")

screen scene97_free_roam_end():
    add "note_bg"
    text "End free roam?":
        size 60 color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "note_bg_no_%s":
        focus_mask True
        action Return()
    text "No":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1080 ypos 1010 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "note_bg_yes_%s":
        focus_mask True
        action Jump("scene97_2")
    text "Yes":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1490 ypos 1010 xanchor 0.5 yanchor 0.5

screen scene97_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene97_choice01_op1")
    text "\"Hot.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene97_choice01_op2")
    text "\"Like an idiot?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene97_choice01_op3")
    text "\"Like a freak who did terrible things?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene97_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene97_choice02_op1")
    text "\"No, Kat. There's a lot on my mind.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene97_choice02_op2")
    text "\"I already have someone. Do you mind sharing?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene97_choice02_op3")
    text "Test her loyalty":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene97_choice02_op4")
    text "\"There's no need. I want your mouth now.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene97_choice03():
    if mc_harem_kat:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene97_choice03_op1")
        text "\"Break that contract. I don't want to cheat.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene97_choice03_op2")
        text "\"I don't want to cheat.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene97_choice02_op3")
    text "Test her loyalty":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene97_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene97_choice04_op1")
    text "\"Start barking.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene97_choice04_op2")
    text "\"Kiss my boot.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene97_choice04_op3")
    text "\"Tell me you're nothing without my cock.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene98_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene98_choice01_op1")
    text "\"Let's do it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene98_choice01_op2")
    text "\"Share my cum with her. Have her swallow it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene98_choice01_op3")
    text "\"No. I don't want to get on her bad side.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene98_kat():
    if scene98_kat_bj1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene98_kat_bj2")
        text "Switch position":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene98_kat_bj1")
        text "Switch position":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if s98_eat_pussy:
        if scene98_kat_bj1:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene98_kat_bj1")
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene98_kat_bj2")
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene98_kat_pussy")
        text "Eat pussy":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene98_kat_bj_cum1")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene100_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene100_choice01_op1")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene100_choice01_op2")
    text "Kill Ava":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene101_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene101_choice01_op1")
    text "Nod":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene101_choice01_op2")
    text "Stay still":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
screen update0_4_1_end():
    add "update0_4_1_ending"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Return()

screen scene102_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene102_choice01_op1")
    text "Give the sword to Alex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene102_choice01_op2")
    text "Give the sword to Reham":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene103_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene103_choice01_op1")
    text "\"Get down from there!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene103_choice01_op2")
    text "Let her talk":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene103_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene103_choice02_op1")
    text "Spar with Thulkin":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene103_choice02_op2")
    text "\"I won't help you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    if not mc_asked_maia_opinion:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene103_choice02_op3")
        text "Ask what Maia thinks":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene103_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene103_choice03_op1")
    text "Punch him":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene103_choice03_op2")
    text "Fight fair":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene103_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene103_choice04_op1")
    text "\"Wait. I'll help you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene103_choice04_op2")
    text "Let them leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene103_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene103_choice05_op1")
    text "\"Let's move\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene103_choice05_op2")
    text "Say goodbye to Maia and Reham first":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True

screen scene104_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice01_op1")
    text "\"My own safety comes first.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice01_op2")
    text "\"My first priority would be my loved ones.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene104_choice01_op3")
    text "\"I would.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene104_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice02_op1")
    text "Catch her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice02_op2")
    text "Let her fall on your face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene104_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice03_op1")
    text "Go with Alex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice03_op2")
    text "Go with Millicent":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene104_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice04_op1")
    text "\"You should have been more aware.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice04_op2")
    text "\"Don't blame yourself.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene104_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice05_op1")
    text "\"The way you fight. It's beautiful.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice05_op2")
    text "\"It's nothing.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene104_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice06_op1")
    text "Protect Alex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice06_op2")
    text "Throw your sword and kill the Chieftain":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True textalign 0.5 xmaximum 400

screen scene104_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice07_op1")
    text "Subdue the Chieftain":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice07_op2")
    text "Behead the Chieftain":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene104_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene104_choice08_op1")
    text "Order him to ravage villages":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene104_choice08_op2")
    text "Order him to fight other goblins":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene105_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice01_op1")
    text "\"Until next time.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice01_op2")
    text "Kiss her back":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene105_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice02_op1")
    text "Tell them about Amelia the Witch":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice02_op2")
    text "Tell them about the cultists village":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene105_choice02_op3")
    text "Tell them about your world":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 italic True

screen scene105_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice03_op1")
    text "Sleep with Reham":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice03_op2")
    text "\"I'd prefer to be alone.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene105_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice04_op1")
    text "\"There's much to think about other than you\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice04_op2")
    text "\"Every second.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 

screen scene105_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice05_op1")
    text "Sleep with Maia":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice05_op2")
    text "\"You should go. I'll stay for a bit.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 400 

screen scene105_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice06_op1")
    text "\"Maia should start first.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice06_op2")
    text "\"Reham should take the lead.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene105_choice06_op3")
    text "\"Nobody's starting anything. I'm too tired for this.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene105_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene105_choice07_op1")
    text "\"That's right.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene105_choice07_op2")
    text "\"No. She's doesn't have to if she's uncomfortable.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 

screen scene106_bj():
    if not s106_bj_reham:
        if scene106_bj2_reham:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene106_bj2_op1")
            text "\"Your turn, Reham.\" Blowjob 1":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        else:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene106_bj_op1")
            text "\"Your turn, Reham.\" Blowjob 1":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "\"Your turn, Reham.\" Blowjob 1":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    if not s106_bj_maia:   
        if scene106_bj2_maia:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene106_bj2_op2")
            text "\"Your turn, Maia.\" Blowjob 2":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene106_bj_op2")
            text "\"Your turn, Maia.\" Blowjob 2":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "\"Your turn, Maia.\" Blowjob 2":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    if not s106_bj_share:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene106_bj2_op3")
        text "\"Both at once.\" Blowjob 3":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "\"Both at once.\" Blowjob 3":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

    if not s106_bj_share:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene106_bj_op4")
        text "{i}Cum":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene106_bj_cum_b")
        text "{i}Cum":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene106_bj_op4():
    if s106_bj_maia:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene106_bj_cum_m")
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene106_bj_cum_r")
        text "Cum inside":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene106_bj_cum_b")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene106_sex_maia_v():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene106_sex_maia_v")
    text "Vaginal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene106_sex_maia_a")
    text "Anal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene106_presex():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene106_sex_reham_v")
    text "Vaginal sex":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if not scene106_reham_anal_rejected:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene106_sex_reham_a")
        text "Anal sex":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Anal sex":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene106_sex2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene106_sex_reham_v2")
    text "Vaginal sex (Reham)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if mc_harem_reham_dom or mc_harem_reham_dom_dom:
        if scene106_reham_anal:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene106_sex_reham_a2")
            text "Anal sex (Reham)":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene106_sex_reham_a")
            text "Anal sex (Reham)":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Anal sex (Reham)":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene106_sex_maia_v2")
    text "Vaginal sex (Maia)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene106_sex_maia_a2")
    text "Anal sex (Maia)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene106_sex():
    if scene106_sex_mis:
        if scene106_sex_maia:
            if scene106_sex_v:
                imagebutton auto "main_choices_op1_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_v")
                text "Switch to Reham":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            else:
                if mc_harem_reham_dom or mc_harem_reham_dom_dom:
                    imagebutton auto "main_choices_op1_%s":
                        focus_mask True
                        action Jump("scene106_sex_reham_a")
                    text "Switch to Reham":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
                else:
                    imagebutton auto "main_choices_op1_%s":
                        focus_mask True
                        action Jump("scene106_sex_reham_v")
                    text "Switch to Reham":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene106_sex_v:
                imagebutton auto "main_choices_op1_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_v")
                text "Switch to Maia":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op1_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_a")
                text "Switch to Maia":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        if scene106_sex_maia:
            if scene106_sex_v:
                imagebutton auto "main_choices_op1_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_v2")
                text "Switch to Reham":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            else:
                if mc_harem_reham_dom or mc_harem_reham_dom_dom:
                    imagebutton auto "main_choices_op1_%s":
                        focus_mask True
                        action Jump("scene106_sex_reham_a2")
                    text "Switch to Reham":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
                else:
                    imagebutton auto "main_choices_op1_%s":
                        focus_mask True
                        action Jump("scene106_sex_reham_v2")
                    text "Switch to Reham":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene106_sex_v:
                imagebutton auto "main_choices_op1_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_v2")
                text "Switch to Maia":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op1_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_a2")
                text "Switch to Maia":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if scene106_sex_mis:
        if not scene106_sex_maia:
            imagebutton auto "main_choices_op0_%s":
                focus_mask True
                action Jump("scene106_sex_pov")
            text "Change POV":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op0_%s":
                focus_mask True
            text "Change POV":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True

    
    if scene106_sex_mis:
        if scene106_sex_maia:
            if scene106_sex_v:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_v2")
                text "Doggystyle":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_a2")
                text "Doggystyle":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene106_sex_v:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_v2")
                text "Doggystyle":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_a2")
                text "Doggystyle":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        if scene106_sex_maia:
            if scene106_sex_v:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_v")
                text "Missionary":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_a")
                text "Missionary ":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene106_sex_v:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_v")
                text "Missionary ":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op2_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_a")
                text "Missionary ":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not scene106_sex_v:
        if scene106_sex_mis:
            if scene106_sex_maia:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_v")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_v")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene106_sex_maia:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_v2")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("scene106_sex_reham_v2")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if not scene106_sex_a:
        if scene106_sex_mis:
            if scene106_sex_maia:
                imagebutton auto "main_choices_op4_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_a")
                text "Anal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
            else:
                if scene106_reham_anal:
                    imagebutton auto "main_choices_op4_%s":
                        focus_mask True
                        action Jump("scene106_sex_reham_a")
                    text "Anal":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
                else:
                    imagebutton auto "main_choices_op4_%s":
                        focus_mask True
                    text "Anal":
                        size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene106_sex_maia:
                imagebutton auto "main_choices_op4_%s":
                    focus_mask True
                    action Jump("scene106_sex_maia_a2")
                text "Anal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
            else:
                if scene106_reham_anal:
                    imagebutton auto "main_choices_op4_%s":
                        focus_mask True
                        action Jump("scene106_sex_reham_a2")
                    text "Anal":
                        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
                else:
                    imagebutton auto "main_choices_op4_%s":
                        focus_mask True
                    text "Anal":
                        size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True


    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene106_sex_cum")
    text "Cum": 
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene106_sex_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action [SetVariable("scene106_cum_inside", True), Jump("scene106_cum")]
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action [SetVariable("scene106_cum_inside", False), Jump("scene106_cum")]
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene106_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene106_choice01_op1")
    text "\"That's not happening. Prepare for more.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene106_choice01_op2")
    text "Sleep":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene107_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice01_op1")
    text "\"Of course. You'll find someone nice.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice01_op2")
    text "\"You'll have that life. I'll make sure of it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene107_choice01_op3")
    text "\"I should get going.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene107_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice02_op1")
    text "Follow her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice02_op2")
    text "Ignore her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene107_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice03_op1")
    text "Give her 100 coins (1 gold coin)":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True 
    
    if mc_harem_nadia:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene107_choice03_op2")
        text "\"We can find another way!\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
        
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene107_choice03_op3")
        text "Let her leave":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene107_choice03_op3")
        text "Let her leave":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene107_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice04_op1")
    text "\"Because I still want to be with you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice04_op2")
    text "\"I'm just trying to help.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene107_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice05_op2")
    text "\"Go. I didn't want you anyway.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice05_op1")
    text "Slam the door shut before she leaves":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene107_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice06_op1")
    text "Stay with Nadia for a bit":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice06_op2")
    text "\"We'll sip tea together later.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene107_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice07_op1")
    text "\"I made a pact with a demon lord.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice07_op2")
    text "\"Magic!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene107_choice07_op3")
    text "\"I'm not sure myself.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene107_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice08_op1")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice08_op2")
    text "Take a peek":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene107_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice09_op1")
    text "\"Your breasts.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice09_op2")
    text "\"Ah... nothing.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene107_choice10():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_choice10_op1")
    text "Touch her breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene107_choice10_op2")
    text "\"I just wanted to stare. That's all.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen s107_hover_areas():
    add "s107_right_b_hover"
    add "s107_left_b_hover"
    add "s107_nipples_hover"

screen scene107_boobs():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s107_hover_areas")
        ]
        unhovered [
            Hide("s107_hover_areas")
        ]

    modal True 
    imagebutton auto "s107_right_b_%s":
        focus_mask True
        action Jump("scene107_boobs_right_b")

    imagebutton auto "s107_left_b_%s":
        focus_mask True
        action Jump("scene107_boobs_left_b")
    
    imagebutton auto "s107_nipples_%s":
        focus_mask True
        action Jump("scene107_boobs_nipples")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene107_boobs_fin")
    text "Finish":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene108_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene108_choice01_op1")
    text "Give her a pat on the ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene108_choice01_op2")
    text "Supress impulsive thought":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene108_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene108_choice02_op1")
    text "\"You'll be my queen.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene108_choice02_op2")
    text "\"You'll be one of my close harem girls.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene108_choice02_op3")
    text "\"You'll be a regular maid.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene108_choice02_op4")
    text "\"You won't have any position. Tell me. Now.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene109_choice01():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5
    
    if mc_karma >= 10:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL = 10) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma >= 10:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene109_choice01_op1")
        text "Sacrifice yourself":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene109_choice01_op1_2")
        text "Sacrifice yourself":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene109_choice01_op2")
    text "Stay and listen":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen update0_4_1_end():
    add "update0_4_2_ending"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Return()

screen scene111_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene111_choice01_op1")
    text "\"Fine. Show me the way.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene111_choice01_op2")
    text "\"Find someone else.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene111_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene111_choice02_op1")
    text "\"Revoke all of your slaves.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene111_choice02_op2")
    text "\"I want more coin.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene111_choice02_op3")
    text "\"That's good enough.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene111_choice03():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5
    
    if mc_karma <= 4:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≤ 4) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma <= 4:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene111_choice03_op1")
        text "Accept Jenny's deal":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Accept Jenny's deal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene111_choice03_op2")
    text "\"Put the sword down, Lena.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene111_choice03_op3")
    text "Do nothing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene111_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene111_choice04_op1")
    text "\"Think of Serena!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene111_choice04_op2")
    text "Attack":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene111_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene111_choice05_op1")
    text "Go with Jenny":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene111_choice05_op2")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene111_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene111_choice06_op1")
    text "\"I'll make sure you have enough of me for a while.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene111_choice06_op2")
    text "\"I just remembered that I have something. I need to go.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 600

screen scene112_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene112_choice01_op1")
    text "\"You are.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene112_choice01_op2")
    text "\"You're pretty, but not the prettiest.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene112_choice01_op3")
    text "\"Not even close.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene112_sex():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene112_sex_pov")
    text "Switch POV":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if not scene112_sex_bj:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene112_sex_bj")
        text "Blowjob":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene112_sex")
        text "Sex":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not scene112_sex_bj:
        if scene112_sex_a:
            imagebutton auto "main_choices_op4_%s":
                focus_mask True
                action Jump("scene112_sex_vag")
            text "Vaginal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op4_%s":
                focus_mask True
            text "Vaginal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

        if scene112_sex_v:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("scene112_sex_anal")
            text "Anal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Anal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Vaginal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "Anal":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    if not scene112_sex_bj:
        imagebutton auto "main_choices_op5_%s":
            focus_mask True
            action Jump("scene112_sex_cum")
        text "Cum": 
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op5_%s":
            focus_mask True
        text "Cum": 
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene112_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene112_choice02_op1")
    text "Push for it":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene112_choice02_op2")
    text "Back off":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene112_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene112_choice03_op1")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene112_choice03_op2")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene113_choice01():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5
    
    if mc_karma == 1:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL = 1) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma == 1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene113_choice01_op1")
        text "Kill her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Kill her":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene113_choice01_op2")
    text "Scare her off":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene113_choice01_op3")
    text "\"I don't want to hurt you, Alice.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene113_choice02():
    if not mc_failed_buy_brothel:
        if mc_friend_diana or mc_harem_diana:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene114")
            text "Buy the brothel":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
            text "???":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if mc_helped_lena:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene115")
        text "Go to the stables":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene115_0")
        text "Go to the stables":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene116")
    text "Return to the hideout":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene114_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice01_op1")
    text "\"Making sure the girls are attractive.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice01_op2")
    text "\"Charging the highest prices possible.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene114_choice01_op3")
    text "\"Keeping the girls safe and well taken care of.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene114_choice01_op4")
    text "\"Having the best alcohol and entertainment.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene114_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice02_op1")
    text "\"Call the guards.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice02_op2")
    text "\"Let the girl handle it. It builds character.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene114_choice02_op3")
    text "\"Offer him a free drink to calm down.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene114_choice02_op4")
    text "\"Step in personally and remove him.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene114_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice03_op1")
    text "\"Support her until the child is born.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice03_op2")
    text "\"Fire her. She can't work anymore.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene114_choice03_op3")
    text "\"Give her a bonus and wish her luck.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene114_choice03_op4")
    text "\"Force her to keep working.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene114_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice04_op1")
    text "\"Yeah. Let's turn it into a tavern.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice04_op2")
    text "\"Actually, I prefer if it remaind a brothel.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene114_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice05_op1")
    text "\"The Drunken Bastard.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice05_op2")
    text "\"Gronko's Rest.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    if not mc_brothel_name_fail:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene114_choice05_op3")
        text "\"The New Queen is a Bitch.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "\"The New Queen is a Bitch.\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene114_choice05_op4")
    text "Custom name":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen scene114_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice06_op1")
    text "\"We'll keep the same name.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice06_op2")
    text "Custom name":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene114_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice07_op1")
    text "Hire workers":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice07_op2")
    text "\"I'll leave it up to you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
screen scene114_choice08():
    add "ruby_cv"

    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice08_op1")
    text "Interview":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice08_op2")
    text "Dismiss":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene114_choice09():
    add "sarah_cv"
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice09_op1")
    text "Interview":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice09_op2")
    text "Dismiss":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene114_choice10():
    if not ruby_q1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene114_choice10_op1")
        text "\"Tell me about yourself.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "\"Tell me about yourself.\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if not ruby_q2:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene114_choice10_op2")
        text "\"How can you contribute to our buisness?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "\"How can you contribute to our buisness?\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if not ruby_q3:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene114_choice10_op3")
        text "\"Do you have any past experience?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "\"Do you have any past experience?\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if not ruby_q4:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene114_choice10_op4")
        text "\"Why do you want to work here?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "\"Why do you want to work here?\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene114_choice10_op5")
    text "Conclude interview": 
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene114_choice11():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice11_op1")
    text "\"Keep your mouth dry. You're hired.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice11_op2")
    text "\"You're dismissed.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene114_choice11_op3")
    text "\"Get on your knees.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene114_choice12():
    if not sarah_q1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene114_choice12_op1")
        text "\"Do you have past experiance?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        if mc_hired_ruby_after_bj:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene114_bj1")
            text "Glans licking":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op1_%s":
                focus_mask True
                action Jump("scene114_bj1")
            text "\"Do you have past experiance?\"":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if not sarah_q2:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene114_choice12_op2")
        text "\"How would you handle a rude customer?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        if mc_hired_ruby_after_bj:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene114_bj2")
            text "Blowjob":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
            text "\"How would you handle a rude customer?\"":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if not sarah_q3:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene114_choice12_op3")
        text "\"What are your strengths and weaknesses?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        if mc_hired_ruby_after_bj:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("scene114_bj3")
            text "Deepthroat":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "\"What are your strengths and weaknesses?\"":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    if not sarah_q4:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene114_choice12_op4")
        text "\"How do you feel about working here?\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "\"How do you feel about working here?\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene114_choice12_op5")
    text "Conclude interview": 
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene114_choice13():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene114_choice13_op1")
    text "\"You're hired.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene114_choice13_op2")
    text "\"You're dismissed.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene114_choice14():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
    text "Buy the brothel":
        size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if mc_helped_lena:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene115")
        text "Go to the stables":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene115_0")
        text "Go to the stables":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene116")
    text "Return to the hideout":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene115_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene115_choice01_op1")
    text "Tell the truth":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene115_choice01_op2")
    text "Lie":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene115_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene115_choice02_op1")
    text "Remove your pants":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene115_choice02_op2")
    text "\"Better not...\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen update_0_4_3end():
    add "update_0_4_3_end"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Return()
        
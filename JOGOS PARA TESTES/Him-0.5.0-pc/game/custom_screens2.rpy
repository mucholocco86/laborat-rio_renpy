screen interact_tutorial():
    add "tutorial_bg"
    text "Tutorial":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 550 xanchor 0.5 yanchor 0.5
    text "When the hand icon appears in the top-right corner, it means you can interact with certain parts of the scene.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
    text "Hover over the hand icon to highlight the areas you can interact with.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 950 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "tutorial_bj_continue_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1270 ypos 1175 xanchor 0.5 yanchor 0.5

screen free_roam_tutorial1():
    add "tutorial_bg"
    text "Free Roam Tutorial":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 550 xanchor 0.5 yanchor 0.5
    text "Use the on-screen arrows to explore the area.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
    text "You can also use your keyboard's arrow keys to move around.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 950 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "tutorial_bj_continue_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1270 ypos 1175 xanchor 0.5 yanchor 0.5

screen free_roam_tutorial2():
    add "tutorial_bg"
    text "Free Roam Tutorial":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 550 xanchor 0.5 yanchor 0.5
    text "Keep an eye out!":
        size persistent.tutorial_text_size color "#ff0000" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
    text "There are valuable posters and coin hidden throughout the world!":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 950 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "tutorial_bj_continue_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1270 ypos 1175 xanchor 0.5 yanchor 0.5

screen free_roam_tutorial3():
    add "tutorial_bg"
    add "mc_idle"
    text "Free Roam Tutorial":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 550 xanchor 0.5 yanchor 0.5
    text "Use the Stats button to check your stats. Your actions can raise or lower your Honor.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
    text "Certain actions will depend on your honor level.":
        size persistent.tutorial_text_size color "#ff0000" font "candara_bold.ttf" xpos 1275 ypos 950 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "tutorial_bj_continue_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1270 ypos 1175 xanchor 0.5 yanchor 0.5

screen free_roam_tutorial4():
    add "tutorial_bg"
    add "quests_idle"
    text "Free Roam Tutorial":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 550 xanchor 0.5 yanchor 0.5
    text "Use the Journal button if you're unsure of what to do next.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1275 ypos 740 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "tutorial_bj_continue_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1270 ypos 1175 xanchor 0.5 yanchor 0.5

default free_roam_tutorial5 = True
default free_roam_tutorial6 = False
default free_roam_tutorial7 = False
default free_roam_tutorial8 = False

screen free_roam_tutorial5():
    
    if free_roam_tutorial5:
        add "free_roam2_turorial1"
        text "Free Roam Tutorial 2":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 400 xanchor 0.5 yanchor 0.5
        text "\nFor a brief period, you'll have the freedom to explore the world using the navigation menu. \n\nOnce you progress the main story, this window will close, so explore while you can.":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 650 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
        imagebutton auto "free_roam2_continue2_%s":
            focus_mask True
            action [SetVariable("free_roam_tutorial5", False), SetVariable("free_roam_tutorial6", True)]
        text "CONTINUE":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1850 ypos 1040 xanchor 0.5 yanchor 0.5

    elif free_roam_tutorial6:
        add "free_roam2_turorial1"
        text "Free Roam Tutorial 2":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 400 xanchor 0.5 yanchor 0.5
        text "White choices are optional locations. \n\nVisit them at your own pace, they're there for interacting and talking with other characters.":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 650 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
        imagebutton auto "free_roam2_continue2_%s":
            focus_mask True
            action [SetVariable("free_roam_tutorial6", False), SetVariable("free_roam_tutorial7", True)]
        text "CONTINUE":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1850 ypos 1040 xanchor 0.5 yanchor 0.5

    elif free_roam_tutorial7:
        add "free_roam2_turorial2"
        text "Free Roam Tutorial 2":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 400 xanchor 0.5 yanchor 0.5
        text "Pink choices are side-quests. \n\nThose are also optional. You can choose to engage with them on your own.":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 650 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
        imagebutton auto "free_roam2_continue2_%s":
            focus_mask True
            action [SetVariable("free_roam_tutorial7", False), SetVariable("free_roam_tutorial8", True)]
        text "CONTINUE":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1850 ypos 1040 xanchor 0.5 yanchor 0.5

    elif free_roam_tutorial8:
        add "free_roam2_turorial3"
        text "Free Roam Tutorial 2":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 400 xanchor 0.5 yanchor 0.5
        text "Gold choices are essential to the main story. \n\nSelecting them will advance the plot forward.":
            size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 650 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000
        imagebutton auto "free_roam2_continue2_%s":
            focus_mask True
            action Return()
        text "CONTINUE":
            size 70 color "#fff" font "candara_bold.ttf" xpos 1850 ypos 1040 xanchor 0.5 yanchor 0.5

screen free_roam_tutorial6():
    add "free_roam2_turorial1"
    text "Free Roam Tutorial 2":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 400 xanchor 0.5 yanchor 0.5
    text "White choices are optional locations. Visit them at your own pace, they're there for interacting and talking with other characters.":
        size persistent.tutorial_text_size color "#fff" font "candara_bold.ttf" xpos 1850 ypos 650 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 1000

    imagebutton auto "free_roam2_continue2_%s":
        focus_mask True
        action Return()
    text "CONTINUE":
        size 70 color "#fff" font "candara_bold.ttf" xpos 1850 ypos 1040 xanchor 0.5 yanchor 0.5

screen scene115_sex():
    if not scene115_sex_tj:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene115_sex_tj")
        text "Titjob":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Titjob":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if not scene115_sex_cow:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene115_sex_cow")
        text "Cowgirl":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Cowgirl":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not scene115_sex_lay:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene115_sex_lay")
        text "Sideways":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Sideways":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    if not scene115_sex_tj:
        if scene115_sex_cow:
            if scene115_sex_v:
                imagebutton auto "main_choices_op4_%s":
                    focus_mask True
                    action Jump("scene115_sex_cow_a")
                text "Anal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op4_%s":
                    focus_mask True
                    action Jump("scene115_sex_cow_v")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
        else:
            if scene115_sex_v:
                imagebutton auto "main_choices_op4_%s":
                    focus_mask True
                    action Jump("scene115_sex_lay_a")
                text "Anal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op4_%s":
                    focus_mask True
                    action Jump("scene115_sex_lay_v")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        if scene115_sex_v:
            imagebutton auto "main_choices_op4_%s":
                focus_mask True
            text "Anal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op4_%s":
                focus_mask True
            text "Vaginal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene115_sex_cum_0")
    text "Cum": 
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene115_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene115_sex_cum")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene115_sex_cum_no")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene115_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene115_choice04_op1")
    text "\"I'll take responsibility.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene115_choice04_op2")
    text "\"Get rid of it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene116_choice01():
    if mc_agree_help_amelia_milking:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene116_choice01_op1")
        text "Call out to Amelia the witch":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene116_choice01_op1_0")
        text "Call out to Amelia the witch":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not ava_dead:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene116_choice01_op2")
        text "Send a letter to Ava":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene116_choice01_op2_0")
        text "Send a letter to Ava":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not mc_agree_help_amelia_milking and ava_dead:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene116_choice01_op3")
        text "\"I have no one to help.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 

screen scene116_choice02():
    if not ava_dead and not mc_princess_kat_saved:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene116_choice02_op1")
        text "Send a letter to Kat":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Send a letter to Kat":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    if mc_agree_help_thulkin:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene116_choice02_op2")
        text "Send a letter to Thulkin":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
        
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene116_choice02_op3")
        text "Send a letter to Millicent":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Send a letter to Thulkin":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
        
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Send a letter to Millicent":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True


    if ava_dead and not mc_agree_help_thulkin:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene116_choice02_op4")
        text "\"We'll take care of it ourselves.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene116_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene116_choice03_op1")
    text "Purchase 100 coins worth of supplies":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene116_choice03_op2")
    text "Purchase 300 coins worth of supplies":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene116_choice03_op3")
    text "Purchase 500 coins worth of supplies":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene116_choice04():
    if mc_agree_help_thulkin:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene116_choice04_op1")
        text "\"You're right. I'll pick another.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "\"You're right. I'll pick another.\"":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "\"She's strong. It'll be fine.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

default princess_timer = 30

screen scene117_maze1():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"

    key "K_UP" action Jump("scene117_maze_up")

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
            action Jump("scene117_maze_up")

screen scene117_maze2():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"

    key "K_UP" action Jump("scene117_maze_up_up")
    key "K_LEFT" action Jump("scene117_maze_up_left")
    key "K_RIGHT" action Jump("scene117_maze_up_right")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if free_roam_arrows:
        if not scene117_maze_up_up:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_up")

        if not scene117_maze_up_left:
            imagebutton auto "left_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_left")
        
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right")

screen scene117_maze3():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"

    key "K_DOWN" action Jump("scene117_maze_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if scene117_maze3_poster:
        imagebutton auto "117_sewer3_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_left_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up")

screen scene117_maze4():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_UP" action Jump("scene117_maze_up_right_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if scene117_maze4_poster:
        imagebutton auto "117_sewer5_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_poster")

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up")

screen scene117_maze5():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_UP" action Jump("scene117_maze_up_right_up_up")
    key "K_RIGHT" action Jump("scene117_maze_up_right_up_right")

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
            action Jump("scene117_maze_up_right_up_up")
        
        if not scene117_maze_up_right_up_right:
            imagebutton auto "right_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_right_up_right")

screen scene117_maze6():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_DOWN" action Jump("scene117_maze_up_right_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if scene117_maze6_poster:
        imagebutton auto "117_sewer7_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_right_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up")

screen scene117_maze7():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_UP" action Jump("scene117_maze_up_right_up_up_up")
    key "K_RIGHT" action Jump("scene117_maze_up_right_up_up_right")
    key "K_LEFT" action Jump("scene117_maze_up_right_up_up_left")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if free_roam_arrows:
        if not scene117_maze_up_right_up_up_up:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_right_up_up_up")
        
        if not scene117_maze_up_right_up_up_right:
            imagebutton auto "right_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_right_up_up_right")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_up_left")

screen scene117_maze8():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_DOWN" action Jump("scene117_maze_up_right_up_up")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if scene117_maze8_poster:
        imagebutton auto "117_sewer9_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_up_up_poster")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_up")

screen scene117_maze9():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_DOWN" action Jump("scene117_maze_up_right_up_up")

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
            action Jump("scene117_maze_up_right_up_up")

screen scene117_maze10():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_UP" action Jump("scene117_maze_up_right_up_up_left_up")

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
            action Jump("scene117_maze_up_right_up_up_left_up")

screen scene117_maze11():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_UP" action Jump("scene117_maze_up_right_up_up_left_up")
    key "K_LEFT" action Jump("scene117_maze_up_right_up_up_left_up_left")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if free_roam_arrows:
        if not scene117_maze_up_right_up_up_left_up_up:
            imagebutton auto "up_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_right_up_up_left_up_up")

        imagebutton auto "left_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_up_left_up_left")

screen scene117_maze12():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_DOWN" action Jump("scene117_maze_up_right_up_up_left_up")

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
            action Jump("scene117_maze_up_right_up_up_left_up")


screen scene117_maze13():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_RIGHT" action Jump("scene117_maze_up_right_up_up_left_up_left_right")
    key "K_LEFT" action Jump("scene117_maze_up_right_up_up_left_up_left_left")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
    
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]
    
    if scene117_maze13_poster:
        imagebutton auto "117_sewer14_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_up_left_up_left_poster")

    if free_roam_arrows:
        imagebutton auto "right_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene117_maze_up_right_up_up_left_up_left_right")

        if not scene117_maze_up_right_up_up_left_up_left_left:
            imagebutton auto "left_%s":
                focus_mask True
                keyboard_focus False
                action Jump("scene117_maze_up_right_up_up_left_up_left_left")

screen scene117_maze14():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_DOWN" action Jump("scene117_maze_up_right_up_up_left_up_left")

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
            action Jump("scene117_maze_up_right_up_up_left_up_left")

screen scene117_maze15():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"
    
    key "K_UP" action Jump("scene117_maze_up_right_up_up_left_up_left_right_up")

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
            action Jump("scene117_maze_up_right_up_up_left_up_left_right_up")

screen scene117_choice01():
    add "princess_timer"
    text "Timer: [princess_timer] minutes" size persistent.dialogue_text_size color "#cf436b" xpos 0.824 ypos 0.172 font "Lora-VariableFont_wght.ttf"

    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene117_choice01_op1")
    text "Attempt to yank the chain":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    if not mc_minthra_princess_refuse:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene117_choice01_op2")
        text "Seek Minthra's help":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Seek Minthra's help":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene117_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene117_choice02_op1")
    text "Sacrifice Lewis and Joan":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene117_choice02_op2")
    text "Leave the princess":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene117_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"(I promise.)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
        
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene117_choice03_op2")
    text "\"(Forget it. I'll do this on my own.)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene118_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice01_op1")
    text "\"Your brother?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice01_op2")
    text "\"Your father?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene118_choice01_op3")
    text "\"Your lover back home?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene118_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice02_op1")
    text "\"I need you focused. Stop thinking about him.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice02_op2")
    text "\"You will.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene118_choice02_op3")
    text "\"He'll manage if he's your brother.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene118_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice03_op1")
    text "Let Reham talk":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice03_op2")
    text "\"We need to talk to your king.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene118_choice03_op3")
    text "\"We're here on vacation.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene118_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice04_op1")
    text "Go back to Maia and Reham":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice04_op2")
    text "Intervene":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene118_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice05_op2")
    text "\"Reham is right. Go and get your wife back.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice05_op3")
    text "\"Listen to your father, Reham.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene118_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice06_op1")
    text "Follow after Reham":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice06_op2")
    text "\"We won't do anything. They made their choice.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene118_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice07_op1")
    text "Attack":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice07_op2")
    text "\"I'll pay off their debt.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene118_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice08_op1")
    text "Hold back":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene118_choice08_op2")
    text "Punch his head off":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene118_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene118_choice09_op1")
    text "Pay 700 coins":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if mc_took_aldwin_gift:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene118_choice09_op2")
        text "Give him Aldwin's bracelet":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "???":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene118_choice09_op3")
    text "Attack":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene119_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice01_op1")
    text "\"I couldn't let them take you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice01_op2")
    text "\"They were annoying, I wanted to get rid of them.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene119_choice01_op3")
    text "\"I expect a reward for my trouble.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene119_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice02_op1")
    text "\"Lead the way.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice02_op2")
    text "\"Forget it. I have places to be.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene119_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice03_op1")
    text "\"Be straight with him. He has to stop gambling.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice03_op2")
    text "\"You don't have to deal with this. Leave him.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene119_choice03_op3")
    text "\"You should make up. You need each other.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene119_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice04_op1")
    text "\"Don't bury your problems. Talk to me.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice04_op2")
    text "Enjoy the tea in silence":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene119_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice05_op1")
    text "\"Because you deserve better.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice05_op2")
    text "Hold her hand":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene119_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice06_op2")
    text "\"Give him another chance.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice06_op1")
    text "\"Leave him.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5

screen scene119_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene119_choice07_op1")
    text "\"I'm staying here. Weather you like it or not.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene119_choice07_op2")
    text "\"I can support the family.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene119_choice07_op3")
    text "Let Yasmine speak":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen scene120_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice01_op1")
    text "\"I'm her husband.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice01_op2")
    text "\"She's family.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene120_choice01_op3")
    text "\"Just a friend.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 

screen scene120_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_3")
    text "\"Let's go. The stars look pretty.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice02_op2")
    text "\"No. You need to rest.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene120_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice03_op1")
    text "\"I want us to have another chance.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice03_op2")
    text "\"That's fine. I'm just happy that you're here.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene120_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice04_op1")
    text "\"Your eyes are as blue as the sky.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice04_op2")
    text "\"Your eyes are like an ocean I can drown in.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene120_choice04_op3")
    text "\"Your eyes are like egg yolks if they were blue.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene120_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice05_op1")
    text "\"I like your haircut.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice05_op2")
    text "\"Your silky hair flows like melted gold.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene120_choice05_op3")
    text "\"Your bright hair makes me think of the sun\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene120_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice06_op1")
    text "\"I'll follow you to the ends of the world.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice06_op2")
    text "\"I'll never leave you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene120_choice06_op3")
    text "\"I'll always stay with you to the end.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene120_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice07_op1")
    text "Tongue her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_5")
    text "Let her go":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene120_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene120_choice08_op1")
    text "Kneel":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene120_choice08_op2")
    text "Keep standing":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene124_choice00():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"There's one thing Irda is better at.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene124_choice00_op2")
    text "\"Let's sit. I'm tired.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene124_choice000():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"There's one thing Irda is better at.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene124_choice000_op2")
    text "\"Let's sit. I'm tired.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene124_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene124_choice01_op2")
    text "\"The sceneary looks better.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene124_choice01_op1")
    text "\"It doesn't have you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene124_choice01_op3")
    text "\"The food.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene124_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene124_choice02_op1")
    text "Tell her about your world":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene124_choice02_op2")
    text "\"Let's change the subject.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene124_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene124_choice03_op1")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene124_choice03_op2")
    text "\"Not now. You need rest.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene125_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene125_choice01_op2")
    text "\"The sceneary looks better.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene125_choice01_op1")
    text "\"It doesn't have you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene125_choice01_op3")
    text "\"The food.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene125_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene125_choice02_op1")
    text "\"Thank you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene125_choice02_op2")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene125_choice02_op3")
    text "\"I'd like to be rewarded.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene126_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene126_choice01_op1")
    text "Request something from her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene126_choice01_op2")
    text "\"I don't need anything from you at the moment.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene126_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene126_choice02_op1")
    text "\"I want to touch your breasts.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    if mc_princess_success:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene126_choice02_op2")
        text "\"Go get the princess some wine.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene126_choice02_op2")
        text "\"Go get the queen some wine.\"":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene126_choice02_op3")
    text "\"Nevermind.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen s126_hover_areas():
    add "126_boobs_hover"
    add "126_nips_hover"

screen scene126_boobs():
    imagebutton:
        idle "interact_indicator_idle"
        hover "interact_indicator_hover"
        focus_mask True
        action NullAction()
        hovered [
            Show("s126_hover_areas")
        ]
        unhovered [
            Hide("s126_hover_areas")
        ]

    modal True 
    imagebutton auto "126_boobs_%s":
        focus_mask True
        action Jump("scene126_boobs")

    imagebutton auto "126_nips_%s":
        focus_mask True
        action Jump("scene126_nips")
    
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene126_boobs2")
    text "Continue":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

screen scene126_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene126_choice03_op1")
    text "Slap her breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene126_choice03_op2")
    text "Give her a kiss":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene127_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene127_choice01_op1")
    text "\"Sure. Come take a look.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene127_choice01_op2")
    text "\"I'd rather you don't.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene127_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene127_choice02_op1")
    text "\"(He arouses me.)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene127_choice02_op2")
    text "\"(He doesn't arouse me.)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene127_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene127_choice03_op1")
    text "\"(His feminine body.)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene127_choice03_op2")
    text "\"(I like men too.)\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene127_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene127_choice04_op1")
    text "\"It's because of you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene127_choice04_op2")
    text "\"It's nothing, just the water. Promise.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene127_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene127_choice05_op1")
    text "Encourage him to become a girl":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene127_choice05_op2")
    text "Comforte him to stay a femenine boy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

screen scene127_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene127_choice06_op1")
    text "Push further":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene127_choice06_op2")
    text "Stop":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    
screen scene128_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene128_choice01_op2")
    text "\"No. I'll take the bed. You sleep on the couch.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Return()
    text "Sleep on the couch":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene129_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice01_op1")
    text "Squeeze her breasts":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice01_op2")
    text "\"Now is not a good time.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 

screen scene129_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice02_op1")
    text "Attack while he's distracted":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice02_op2")
    text "\"That's enough, Vic. You're talking to me.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene129_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice03_op1")
    text "Keep your hand away":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice03_op2")
    text "Hold her hand":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene129_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice04_op1")
    text "\"He really doesn't desereve you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice04_op2")
    text "\"You look stunning tonight.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene129_choice04_op3")
    text "\"Want me to touch something else?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene129_choice05():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice05_op1")
    text "Kiss her":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice05_op2")
    text "\"I just wanted to comfort you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene129_choice06():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice06_op1")
    text "\"You did your hair?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice06_op2")
    text "\"Are you wearing a new dress?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene129_choice06_op3")
    text "\"Is it your makeup?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5
    
    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("scene129_choice06_op4")
    text "\"You look tired.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 

screen scene129_choice07():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice07_op3")
    text "\"It's nothing.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice07_op1")
    text "\"Did I ever mention how important you are to me?\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene129_choice07_op2")
    text "\"Come sit on my lap.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5

screen scene129_choice08():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice08_op1")
    text "\"I want you to help me with my erection.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice08_op2")
    text "\"I want you to stay with me.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene129_choice09():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Return()
    text "\"Let's do it.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice09_op2")
    text "\"I'd rather not wake them up.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
screen scene129_choice10():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene129_choice10_op1")
    text "\"I'm hard for you.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene129_choice10_op2")
    text "Hug her tighter":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene129_choice11():
    if not s129_maia_choice1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene129_choice11_op1")
        text "Do a backflip":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Do a backflip":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    if not s129_maia_choice2:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
            action Jump("scene129_choice11_op2")
        text "Invite her on a date":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Invite her on a date":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not s129_maia_choice3:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene129_choice11_op3")
        text "Try to talk to her":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Try to talk to her":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    
    if not s129_maia_choice4:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene129_choice11_op4")
        text "Start crying":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "Start crying":
            size persistent.choices_text_size color "818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene129_choice11_op5")
    text "Leave": 
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

default scene131_choice01 = False
default scene131_choice02 = False
default scene131_choice03 = False
default scene131_choice04 = False

screen scene131_choice01():
    if not scene131_choice01:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("scene131_choice01_op1")
        text "Talk about princess Rebecca":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Talk about princess Rebecca":
            size persistent.choices_text_size color "818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    if not scene131_choice02:
        if mc_told_maia_reham_other_world:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("scene131_choice01_op2")
            text "Tell her more about your world":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
            text "Tell her more about your world":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op2_%s":
            focus_mask True
        text "Tell her more about your world":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    if not scene131_choice03:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
            action Jump("scene131_choice01_op3")
        text "Talk about what to do after everything is over":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op3_%s":
            focus_mask True
        text "Talk about what to do when everything is over":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    if not scene131_choice04:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
            action Jump("scene131_choice01_op4")
        text "Talk about working at the palace":
            size persistent.choices_text_size color "fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True
    else:
        imagebutton auto "main_choices_op4_%s":
            focus_mask True
        text "Talk about working at the palace":
            size persistent.choices_text_size color "818181" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    imagebutton auto "main_choices_op5_%s":
        focus_mask True
        action Jump("scene131_choice01_op5")
    text "End date": 
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1340 xanchor 0.5 yanchor 0.5 italic True

screen scene134_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene134_choice01_op1")
    text "\"I'll wear it on my own. You can leave.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene134_choice01_op2")
    text "\"Go ahead. If it'll be faster.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene134_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene134_choice02_op1")
    text "\"I'll help with that. I want to drink your milk.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene134_choice02_op2")
    text "\"I didn't need to see that. Get out.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene134_choice02_op3")
    text "\"You need take better care of yourself.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene134_choice03():
    text "Honor level: [mc_karma]" size 40 color "#fff" font "BebasNeue_Regular.ttf" xpos 2400 ypos 60 xanchor 0.5 yanchor 0.5
    
    if mc_karma <= 4:
        add "choice_unlocked"
    else:
        add "choice_locked"
    text "Honor (LVL ≤ 4) required" size 31 color "#fff" font "BebasNeue_Regular.ttf" xpos 2260 ypos 765 xanchor 0.5 yanchor 0.5

    if mc_karma <= 4:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("s134_servants")
        text "Keep sucking":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Keep sucking":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
            
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene134_choice03_op2")
    text "Let go":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene134_choice04():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene134_choice03_op1")
    text "Demand Aylin to give you a blowjob":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene134_choice04_op2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene134_choice05():
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene134_choice04_op2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen scene135_choice01():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene135_choice01_op1")
    text "\"Let's give those bards something to sing about!\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene135_choice01_op2")
    text "\"That's enough sulking. Let's move.\"":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 textalign 0.5 xmaximum 500

screen scene135_choice02():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene135_choice02_op2")
    text "Gather wood":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene135_choice02_op1")
    text "Offer to help with her feet":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        
screen scene135_choice03():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("scene135_choice03_op1")
    text "Sniff her foot":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("scene135_choice03_op2")
    text "Lick her toes":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("scene135_choice03_op3")
    text "Let go":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

default scene135_free_roam_poster1 = True
default scene135_free_roam_poster2 = True
default scene135_free_roam_poster3 = True

default scene135_free_roam_stick1 = True
default scene135_free_roam_stick2 = True
default scene135_free_roam_stick3 = True

screen scene135_wood1():
    key "K_UP" action Jump("scene135_wood2")
    key "K_DOWN" action Jump("scene135_wood3")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 
        
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene135_free_roam_poster1:
        imagebutton auto "135_s47_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood1_poster")

    if scene135_free_roam_stick1:
        imagebutton auto "135_s47_stick1_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood1_stick")

    if free_roam_arrows:
        imagebutton auto "up_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood2")

        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood3")

screen scene135_wood2():
    key "K_DOWN" action Jump("scene135_wood1")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 

        
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene135_free_roam_poster2:
        imagebutton auto "135_s48_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood2_poster")

    if scene135_free_roam_stick2:
        imagebutton auto "135_s48_stick2_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood2_stick")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood1")

screen scene135_wood3():
    key "K_DOWN" action Jump("scene135_wood1")

    imagebutton auto "quests_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", True), SetVariable("mc_overview_open", False), SetVariable("free_roam_arrows", False), Show("mc_quests")] 

        
    imagebutton auto "mc_%s":
        focus_mask True
        keyboard_focus False
        action [SetVariable("quest_screen_open", False), SetVariable("mc_overview_open", True), SetVariable("free_roam_arrows", False), Show("mc_stats")]

    if scene135_free_roam_poster3:
        imagebutton auto "135_s49_poster_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood3_poster")

    if scene135_free_roam_stick3:
        imagebutton auto "135_s49_stick3_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood3_stick")

    if free_roam_arrows:
        imagebutton auto "down_%s":
            focus_mask True
            keyboard_focus False
            action Jump("scene135_wood1")

screen s124_reb_choice1():
    if not s124_reb_choice1_op1:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
            action Jump("s124_reb_choice1_op1")
        text "Finger her ass":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op1_%s":
            focus_mask True
        text "Finger her ass":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("s124_reb_choice1_op2")
    text "Make her cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen s124_reb_choice2():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s124_reb_choice2_op1")
    text "Fuck her pussy":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("s124_reb_choice2_op2")
    text "Fuck her ass":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("s124_reb_choice4_op1")
    text "Let her sleep":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

default s124_thighjob = False
default s124_pronebone = False
default s124_reversecow = False
default s124_anal = False
default s124_vaginal = False

screen s124_reb_choice3():
    imagebutton auto "main_choices_op0_%s":
        focus_mask True
        action Jump("s124_pronebone")
    text "Pronebone":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s124_reversecow")
    text "Reverse cowgirl":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("s124_thighjob")
    text "Thighjob":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

    if not s124_thighjob:
        if s124_pronebone:
            if s124_anal:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("s124_pronebone_vaginal")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("s124_pronebone_anal")
                text "Anal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            if s124_anal:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("s124_reversecow_vaginal")
                text "Vaginal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            else:
                imagebutton auto "main_choices_op3_%s":
                    focus_mask True
                    action Jump("s124_reversecow_anal")
                text "Anal":
                    size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
    else:
        if s124_anal:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Vaginal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Anal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("s124_reb_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen s124_reb_choice4():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s124_reb_choice4_op1")
    text "Leave":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("s124_reb_choice4_op2")
    text "Give her a kiss":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("s124_reb_choice4_op3")
    text "Wipe your cock on her face":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

default s130_standing = False
default s130_sitting = False
default s130_anal = False
default s130_vaginal = False

screen s30_sex():
    if s130_standing:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
            action Jump("s130_POV")
        text "Change POV":
            size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True
    else:
        imagebutton auto "main_choices_op0_%s":
            focus_mask True
        text "Change POV":
            size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 702 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s130_position")
    text "Change position":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True
    
    if s130_standing:
        if s130_vaginal:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
            text "Vaginal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("s130_standing_vaginal")
            text "Vaginal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

        if s130_anal:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Anal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("s130_standing_anal")
            text "Anal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
            
    else:
        if s130_vaginal:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
            text "Vaginal":
                size persistent.choices_text_size color "818181" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op2_%s":
                focus_mask True
                action Jump("s130_sitting_vaginal")
            text "Vaginal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
        if s130_anal:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
            text "Anal":
                size persistent.choices_text_size color "#818181" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True
        else:
            imagebutton auto "main_choices_op3_%s":
                focus_mask True
                action Jump("s130_sitting_anal")
            text "Anal":
                size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op4_%s":
        focus_mask True
        action Jump("s130_cum")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1214 xanchor 0.5 yanchor 0.5 italic True

screen s130_sex_cum():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s130_sex_cum_inside")
    text "Cum inside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("s130_sex_cum_outside")
    text "Cum outside":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True

screen s130_hj():
    imagebutton auto "main_choices_op1_%s":
        focus_mask True
        action Jump("s130_hj1")
    text "Handjob 1":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 832 xanchor 0.5 yanchor 0.5 italic True

    imagebutton auto "main_choices_op2_%s":
        focus_mask True
        action Jump("s130_hj2")
    text "Handjob 2":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 959 xanchor 0.5 yanchor 0.5 italic True
    
    imagebutton auto "main_choices_op3_%s":
        focus_mask True
        action Jump("s130_cum2")
    text "Cum":
        size persistent.choices_text_size color "#fff" font "candara.ttf" xpos 2260 ypos 1086 xanchor 0.5 yanchor 0.5 italic True

screen update0_5_0_end():
    add "update0_5_0_ending"
    imagebutton auto "tutorial_continue_%s":
        focus_mask True
        action Return()
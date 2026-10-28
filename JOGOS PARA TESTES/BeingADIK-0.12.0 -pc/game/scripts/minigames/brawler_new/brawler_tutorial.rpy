screen brawler_tutorial_screen:
    tag brawler_tutorial_screen
    modal True
    add "bn_skill_bg"
    add "bn_scroll_lines" at bn_line_transform
    add "bn_tut_ol"

    text "Tutorial" style "brawler_skill_header_style" xalign 0.06 yalign 0.05

    default bn_tut_page = 1
    text "{size=-%d}Page %d of 8{/size}" % ((50 * persistent.scale_factor), bn_tut_page) style "brawler_skill_header_style" xalign 0.22 yalign 0.095
    textbutton "{size=+%d}Next{/size}" % (5 * persistent.scale_factor) text_style "brawler_menu_diff_style":
        xalign 0.435 yalign 0.08
        if bn_tut_page == 8:
            action Function(bn_play_failed_click,0,0,0)
        else:
            action Function(bn_play_click,0,0,0),SetScreenVariable("bn_tut_page",min(bn_tut_page+1,8))
    textbutton "{size=+%d}Previous{/size}" % (5 * persistent.scale_factor) text_style "brawler_menu_diff_style":
        xalign 0.335 yalign 0.08
        if bn_tut_page == 1:
            action Function(bn_play_failed_click,0,0,0)
        else:
            action Function(bn_play_click,0,0,0),SetScreenVariable("bn_tut_page", max(bn_tut_page-1,1))
    if bn_tut_page == 1:
        text "{size=-%d}Brawler{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_1"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 650 * persistent.scale_factor
            xmaximum 650 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "Brawler has been upgraded, but it plays much like its predecessor with a few key differences.\n\nClick Skills from the main menu to bring up the Skills menu, where you can improve your stats and select a special attack after you unlock one.\n\nThe {color=ffe059}skill points{/color} from the old version of Brawler won't carry over, but your starting stats will be slightly higher depending on how many {color=ffe059}skill points{/color} you used to have. These {color=00b0ff}skill points{/color} are colored {color=00b0ff}blue{/color} and cannot be changed.\n\nIf you did not max out your {color=ffe059}skill points{/color} in the previous version of Brawler, you will start earning {color=00b0ff}skill points{/color} before you can earn {color=ffe059}skill points{/color}." style "brawler_tut_text_style"
        text "{color=ffe059}Skills{/color} - Click the gray bars to allocate any available {color=ffe059}skill points{/color}.\nYou gain {color=ffe059}skill points{/color} as a reward from certain fights." style "brawler_tut_text2_style":
            xalign 0.78
            yalign 0.85
    elif bn_tut_page == 2:
        text "{size=-%d}Stats{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_1"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 687 * persistent.scale_factor
            xmaximum 687 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "{color=ffe059}Power{/color} - Determines how much damage you deal.\n\n{color=ffe059}Stamina{/color} - Determines the number of stamina bars.\n\n{color=ffe059}Speed{/color} - Increases the time to input your actions.\n\n{color=ffe059}Block{/color} - Reduces the damage taken when blocking.\n\n{color=ffe059}Counter{/color} - Increases your counter-attack chance.\n\n{color=ffe059}Rage{/color} - Increases the Rage start value." style "brawler_tut_text_style"
        text "{color=ffe059}Skills{/color} - Click the gray bars to allocate any available {color=ffe059}skill points{/color}.\nYou gain {color=ffe059}skill points{/color} as a reward from certain fights." style "brawler_tut_text2_style":
            xalign 0.78
            yalign 0.85
    elif bn_tut_page == 3:
        text "{size=-%d}Attacking{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_2"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 687 * persistent.scale_factor
            xmaximum 687 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "To attack in Brawler, press the corresponding arrow button. These are the possible words and what kind of attack they do." style "brawler_tut_text_style"
            text "{color=bb433b}Failed attacks{/color}\nMISS   FAIL   NOPE   SLIP   BAD\n\n{color=ffe059}Normal attacks{/color}\nHIT   WEAK   FIST   THUD   KICK   LOW   HIGH\n\n{color=1df400}Powerful attacks{/color} (1 stamina)\nSUPER   POWER   COMBO   OUCH   BREAK{color=ffe059}**{/color}\n\n{color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font} mode{/color} (≥2 {color=00b0ff}stamina{/color})\nRAGE\n\n{color=fe9416}Special attack{/color} (2 {color=00b0ff}stamina{/color})\nSPECIAL" style "brawler_tut_text3_style" yoffset -70 * persistent.scale_factor xoffset 50 * persistent.scale_factor
        text "{color=ffe059}**{/color} On top of being a powerful attack, BREAK drains up to two of the opponent's {color=00b0ff}stamina{/color} bars." style "brawler_tut_text2_style":
            xalign 0.09
            yalign 0.85
            xmaximum 600 * persistent.scale_factor
        text "{color=ffe059}Attacking{/color} - The words for attacking are randomized.\nPress the directional arrow for the attack you want, but be quick.\nThere is a timer for every action in Brawler." style "brawler_tut_text2_style":
            xalign 0.78
            yalign 0.85
    elif bn_tut_page == 4:
        text "{size=-%d}Stamina{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_2"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 687 * persistent.scale_factor
            xmaximum 687 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "A new feature in Brawler is the {color=00b0ff}Stamina{/color} gauge.\n{color=1df400}Powerful attacks{/color}, {color=fe9416}Special attacks{/color}, {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font} mode{/color}, and Dodging use {color=00b0ff}stamina{/color}.\n\n{color=1df400}Powerful attacks{/color} use 1 {color=00b0ff}stamina{/color} bar.\n\n{color=fe9416}Special attacks{/color} use 2 {color=00b0ff}stamina{/color} bars.\n\n{color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font} mode{/color} uses all available {color=00b0ff}stamina{/color} bars, but it needs at least 2 {color=00b0ff}stamina{/color} bars to activate.\n\nDodging uses half of a {color=00b0ff}stamina{/color} bar.\n\nEach time before you attack or defend, you regenerate ½ {color=00b0ff}stamina{/color} bar." style "brawler_tut_text_style"
        text "{color=ffe059}Stamina{/color} - The stamina bars are shown under your and your opponent's health bars.\nThe opponent uses his stamina for powerful attacks." style "brawler_tut_text2_style":
            xalign 0.82
            yalign 0.85
    elif bn_tut_page == 5:
        text "{size=-%d}Attacking{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_3"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 650 * persistent.scale_factor
            xmaximum 650 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "After selecting an attack, enter the arrow combination. This works in the same way as in the old version of Brawler.\n\nWhen playing Hard difficulty, the reaction times will be faster, and there may be more arrows for the attacks." style "brawler_tut_text_style"
        text "{color=ffe059}Attacking{/color} - Enter the arrows as shown on the screen.\nIf you press the wrong arrow or take too long to enter the combination, your attack will fail." style "brawler_tut_text2_style":
            xalign 0.85
            yalign 0.85
    elif bn_tut_page == 6:
        text "{size=-%d}Rage mode{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_4"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 650 * persistent.scale_factor
            xmaximum 650 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "{color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font} mode{/color} is a new attack that uses all your {color=00b0ff}stamina{/color} in a potentially devastating attack. You need at least 2 {color=00b0ff}stamina{/color} to use it.\n\nAfter selecting {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font}{/color} as your attack, enter the arrow shown on the screen. For every arrow you input correctly, your {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font}{/color} multiplier will increase by one. If you input an incorrect arrow, the multiplier will decrease by one.\n\nWhen the timer runs out, your {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font}{/color} multiplier will determine the damage from the {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font}{/color} attack.\n\nThe more {color=00b0ff}stamina{/color} you use when starting {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font}{/color}, the more time you will get to enter the attack.\n\nUpgrading {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font}{/color} will let you start {color=e10d00}{font=fonts/ApeMount.ttf}Rage{/font} mode{/color} at a higher multiplier every time." style "brawler_tut_text_style"
        text "{color=ffe059}Rage{/color} - The arrow shown on the screen will change after you enter it.\nYour multiplier depends on how many times you can press the correct button." style "brawler_tut_text2_style":
            xalign 0.85
            yalign 0.85
    elif bn_tut_page == 7:
        text "{size=-%d}Defending{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_5"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 650 * persistent.scale_factor
            xmaximum 650 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "To defend, first enter the correct action.\n\n{color=ffe059}DODGE{/color} - Dodging uses ½ {color=00b0ff}stamina{/color}. If you enter the arrow combination correctly, your opponent will miss and you won't lose any health. There is also a chance that you get an opportunity to counter-attack.\n\n{color=ffe059}BLOCK{/color} - Blocking doesn't use {color=00b0ff}stamina{/color}. Enter the arrow combination correctly to block your opponent's attack. New in Brawler is that blocking depletes some of your health but less than getting hit by the actual attack. Dodging is the superior alternative if it's available to use. You cannot counter-attack after blocking an attack." style "brawler_tut_text_style"
        text "{color=ffe059}Defending{/color} - If you have stamina, your safest option is to dodge the attacks.\nBlocking is not as effective as dodging, but it can be upgraded to reduce the damage taken." style "brawler_tut_text2_style":
            xalign 0.85
            yalign 0.85
    else:
        text "{size=-%d}Counter-attack{/size}" % (30 * persistent.scale_factor) style "brawler_skill_header_style" xalign 0.06 yalign 0.16
        add "bn_tutorial_6"
        vbox:
            xalign 0.087 yalign 0.72
            xminimum 650 * persistent.scale_factor
            xmaximum 650 * persistent.scale_factor
            yminimum 740 * persistent.scale_factor
            ymaximum 740 * persistent.scale_factor
            text "There is a chance to get a counter-attack prompt when dodging an attack.\n\nCounter-attacking in the new Brawler version requires you to press spacebar when you see {font=fonts/ApeMount.ttf}{color=fe9416}COUNTER!!!{/color}{/font} on the screen.\n\nIf you're too slow, you will miss the opportunity to counter-attack.\n\nHow often you can counter-attack is determined by your counter stat, which can be upgraded." style "brawler_tut_text_style"
        text "{color=ffe059}Counter-attack{/color} - Press spacebar to counter-attack.\nThis can only happen after successfully dodging an attack." style "brawler_tut_text2_style":
            xalign 0.78
            yalign 0.85

    key "mouseup_2" action (Function(bn_play_click,0,0,0),Show("brawler_menu_screen"),Hide("brawler_tutorial_screen"))
    textbutton "X" action (Function(bn_play_click,0,0,0),Show("brawler_menu_screen"),Hide("brawler_tutorial_screen")) text_style "brawler_skill_x_style" xalign 0.98 yalign 0.02

screen brawler_dwyane_tutorial_screen:
    tag brawler_dwyane_tutorial_screen
    modal False

    add "brawler_mc_bar_bg" xoffset 4 * persistent.scale_factor yoffset 4 * persistent.scale_factor
    add "brawler_mc_healthbar" xoffset 4 * persistent.scale_factor yoffset 4 * persistent.scale_factor

    add "brawler_bars_ol_tutorial"
    text "{size=+%d}{i}You{/i}{/size}" % (5 * persistent.scale_factor) xalign 0.245 yalign 0.017 style "bn_name_style"

    imagebutton:
        if bn_mc_stamina >= 2:
            idle "brawler_mc_stamina_full"
            hover "brawler_mc_stamina_full"
        elif bn_mc_stamina >= 1:
            idle "brawler_mc_stamina_half"
            hover "brawler_mc_stamina_half"
        else:
            idle "brawler_mc_stamina_empty"
            hover "brawler_mc_stamina_empty"
        action NullAction()
        xpos 69 * persistent.scale_factor
        ypos 22 * persistent.scale_factor
    imagebutton:
        if bn_mc_stamina >= 4:
            idle "brawler_mc_stamina_full"
            hover "brawler_mc_stamina_full"
        elif bn_mc_stamina >= 3:
            idle "brawler_mc_stamina_half"
            hover "brawler_mc_stamina_half"
        else:
            idle "brawler_mc_stamina_empty"
            hover "brawler_mc_stamina_empty"
        action NullAction()
        xpos 139 * persistent.scale_factor
        ypos 22 * persistent.scale_factor

    if bn_tut_msg == 1:
        text "Select a Normal attack.\nNormal attacks: HIT, WEAK, FIST, THUD, KICK, LOW, HIGH." xalign 0.05 yalign 0.95 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 2:
        text "Enter the arrow combination using the arrow or WASD keys." xalign 0.5 yalign 0.9 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 3:
        text "The blue bars below your health are stamina bars.\nPowerful attacks, special attacks, dodging, and Rage mode use stamina." xalign 0.02 yalign 0.07 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 4:
        text "Select a Powerful attack.\nPowerful attacks: SUPER, POWER, COMBO, OUCH, BREAK." xalign 0.05 yalign 0.95 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 5:
        text "Stamina regenerates automatically." xalign 0.02 yalign 0.07 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 6:
        text "Rage mode requires at least two full stamina bars.\nRage mode uses all available stamina in one possibly devastating attack." xalign 0.02 yalign 0.07 style "brawler_dwy_tut_style"
        text "Select a RAGE to enter RAGE mode." xalign 0.5 yalign 0.5 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 7:
        vbox:
            xalign 0.5 yalign 0.5
            text "In Rage mode, you have to press the direction shown on the screen." style "brawler_dwy_tut_style" xalign 0.5
            text "Try to get as many correct presses as possible before the time runs out." style "brawler_dwy_tut_style" xalign 0.5
            text "If you press the wrong key, the Rage counter will decrease." style "brawler_dwy_tut_style" xalign 0.5
    elif bn_tut_msg == 8:
        vbox:
            xalign 0.5 yalign 0.5
            text "Get the Rage counter to 10." xalign 0.5 style "brawler_dwy_tut_style"
            text "The higher your Rage counter is, the more damage your attack will deal." xalign 0.5 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 11:
        text "Dodging uses half of a stamina bar.\nYou won't lose health if you dodge successfully.\nBlocking doesn't use stamina." xalign 0.02 yalign 0.07 style "brawler_dwy_tut_style"
        text "If you choose to block, you will always take some damage. A successful block will take less damage than a failed block." xalign 0.95 yalign 0.80 xmaximum 600 * persistent.scale_factor style "brawler_dwy_tut_style"
        text "Choose to dodge." xalign 0.505 yalign 0.53 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 12:
        vbox:
            xalign 0.5
            yalign 0.95
            text "After successfully dodging, there is a small chance that you can counter-attack." xalign 0.5 style "brawler_dwy_tut_style"
            text "If you see COUNTER!!! after dodging, press spacebar to counter-attack." xalign 0.5 style "brawler_dwy_tut_style"
            text "Press spacebar now." xalign 0.5 style "brawler_dwy_tut_style"
    elif bn_tut_msg == 13:
        text "An extensive tutorial of the updated Brawler can be found within the mini-game." xalign 0.5 yalign 0.95 style "brawler_dwy_tut_style"

screen brawler_counter_screen_tutorial:
    tag brawler_counter_screen_tutorial
    modal True
    text "COUNTER!!!" xalign 0.5 yalign 0.8 style "brawler_counter_text_style"
    key "K_SPACE" action (SetVariable("bn_tut_msg",0),Hide("brawler_counter_screen_tutorial"),Jump(jumpLabel))
screen brawler_rage_screen_tutorial:
    tag brawler_rage_screen_tutorial
    modal True

    if bn_combo_idx == 10:
        timer 0.5 action SetVariable("bn_tut_msg",0)
        timer 3 action Function(bn_end_rage_tutorial)
    else:
        key "K_UP" action (SetVariable("bn_combo_input", "up"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "K_RIGHT" action (SetVariable("bn_combo_input", "right"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "K_DOWN" action (SetVariable("bn_combo_input", "down"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "K_LEFT" action (SetVariable("bn_combo_input", "left"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "w" action (SetVariable("bn_combo_input", "up"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "d" action (SetVariable("bn_combo_input", "right"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "s" action (SetVariable("bn_combo_input", "down"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))
        key "a" action (SetVariable("bn_combo_input", "left"), SetVariable("bn_tut_msg",8), Function(bn_evaluate_rage))

    if bn_rage_flash:
        timer 0.5 action SetVariable("bn_rage_flash", False)

    add "brawler_rage_text" at brawler_rage_zoom xalign 0.5 yalign 0.65

    if bn_combo_idx == 10:
        vbox:
            xalign 0.5 yalign 0.898
            text "{i}x%d{/i}!!!" % bn_combo_idx style "brawler_rage_text2_style" xalign 0.5 at brawler_rage_zoom2
    else:
        if bn_rage_flash:
            add "brawler_arrow_%s_hover" % bn_arrow_combination[0] xalign 0.5 yalign 0.80
        else:
            add "brawler_arrow_%s_idle" % bn_arrow_combination[0] xalign 0.5 yalign 0.80

        vbox:
            xalign 0.5 yalign 0.90
            add "brawler_arrow_box"
        vbox:
            xalign 0.5 yalign 0.898
            text "{i}x%d{/i}" % bn_combo_idx style "brawler_rage_text_style" xalign 0.5

screen brawler_arrow_choice_screen_tutorial:
    tag brawler_arrow_choice_screen_tutorial
    modal True

    key "K_UP" action (SetVariable("bn_arrow_input", 0), Function(bn_evaluate_input_tutorial))
    key "K_RIGHT" action (SetVariable("bn_arrow_input", 1), Function(bn_evaluate_input_tutorial))
    key "K_DOWN" action (SetVariable("bn_arrow_input", 2), Function(bn_evaluate_input_tutorial))
    key "K_LEFT" action (SetVariable("bn_arrow_input", 3), Function(bn_evaluate_input_tutorial))
    key "w" action (SetVariable("bn_arrow_input", 0), Function(bn_evaluate_input_tutorial))
    key "d" action (SetVariable("bn_arrow_input", 1), Function(bn_evaluate_input_tutorial))
    key "s" action (SetVariable("bn_arrow_input", 2), Function(bn_evaluate_input_tutorial))
    key "a" action (SetVariable("bn_arrow_input", 3), Function(bn_evaluate_input_tutorial))


    add "brawler_arrow_up_idle" xalign 0.5 yalign 0.7
    vbox:
        xalign 0.5 yalign 0.595
        add "brawler_arrow_box"
    vbox:
        xalign 0.5 yalign 0.595
        text "{i}%s{/i}" % bn_arrow_selection[0] style "brawler_arrow_text_style" xalign 0.5

    add "brawler_arrow_right_idle" xalign 0.55 yalign 0.8
    vbox:
        xalign 0.625 yalign 0.775
        add "brawler_arrow_box"
    vbox:
        xalign 0.622 yalign 0.775
        text "{i}%s{/i}" % bn_arrow_selection[1] style "brawler_arrow_text_style" xalign 0.5

    add "brawler_arrow_down_idle" xalign 0.5 yalign 0.9
    vbox:
        xalign 0.5 yalign 0.96
        add "brawler_arrow_box"
    vbox:
        xalign 0.5 yalign 0.958
        text "{i}%s{/i}" % bn_arrow_selection[2] style "brawler_arrow_text_style" xalign 0.5

    add "brawler_arrow_left_idle" xalign 0.45 yalign 0.8
    vbox:
        xalign 0.375 yalign 0.775
        add "brawler_arrow_box"
    vbox:
        xalign 0.377 yalign 0.775
        text "{i}%s{/i}" % bn_arrow_selection[3] style "brawler_arrow_text_style" xalign 0.5

screen brawler_arrow_combo_screen_tutorial:
    tag brawler_arrow_combo_screen_tutorial
    modal True

    key "K_UP" action (SetVariable("bn_combo_input", "up"), Function(bn_evaluate_combo_tutorial))
    key "K_RIGHT" action (SetVariable("bn_combo_input", "right"), Function(bn_evaluate_combo_tutorial))
    key "K_DOWN" action (SetVariable("bn_combo_input", "down"), Function(bn_evaluate_combo_tutorial))
    key "K_LEFT" action (SetVariable("bn_combo_input", "left"), Function(bn_evaluate_combo_tutorial))
    key "w" action (SetVariable("bn_combo_input", "up"), Function(bn_evaluate_combo_tutorial))
    key "d" action (SetVariable("bn_combo_input", "right"), Function(bn_evaluate_combo_tutorial))
    key "s" action (SetVariable("bn_combo_input", "down"), Function(bn_evaluate_combo_tutorial))
    key "a" action (SetVariable("bn_combo_input", "left"), Function(bn_evaluate_combo_tutorial))


    hbox:
        xalign 0.5
        yalign 0.8
        for direction in range(0,len(bn_arrow_combination)):
            if bn_combo_idx > direction:
                add "brawler_arrow_%s_hover" % bn_arrow_combination[direction]
            else:
                add "brawler_arrow_%s_idle" % bn_arrow_combination[direction]

init python:
    def bn_evaluate_combo_tutorial():
        global bn_combo_input
        global bn_arrow_combination
        global bn_combo_idx
        global jumpLabel
        
        if bn_combo_input == "" or bn_arrow_combination[bn_combo_idx] != bn_combo_input:
            return
        else:
            if bn_combo_idx + 1 < len(bn_arrow_combination):
                bn_combo_idx += 1
            else:
                renpy.hide_screen("brawler_arrow_combo_screen_tutorial")
                renpy.jump(jumpLabel)
        return

    def bn_evaluate_input_tutorial():
        global bn_arrow_input
        global bn_arrow_input_tut
        global jumpLabel
        
        if bn_arrow_input == bn_arrow_input_tut:
            renpy.hide_screen("brawler_arrow_choice_screen_tutorial")
            renpy.jump(jumpLabel)
        return

    def bn_end_rage_tutorial():
        global bn_rage_flash
        global bn_rage_ending
        global jumpLabel
        bn_rage_ending = False
        bn_rage_flash = False
        renpy.hide_screen("brawler_rage_screen_tutorial")
        renpy.jump(jumpLabel)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

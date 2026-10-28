screen brawler_screen:
    tag brawler_screen
    modal True

    default bn_fight_started = 0

    if not bn_game_over:
        add "brawler_%s_neutral" % bn_cpu_name.lower()
    if bn_fight_started == 0:
        timer 1 repeat False action (SetScreenVariable("bn_fight_started",1),Function(bn_play_bell,0,0,0))
        text "Get ready" xalign 0.5 yalign 0.8 style "brawler_go_style" at brawler_ready_zoom
    elif bn_fight_started == 1:
        timer 1 repeat False action SetScreenVariable("bn_fight_started",2)
        text "Fight" xalign 0.5 yalign 0.8 style "brawler_go_style" at brawler_ready_zoom
    else:
        timer 1 repeat False action Function(bn_next_round)

    if bn_showing_img:
        key "K_UP" action NullAction()
        key "K_RIGHT" action NullAction()
        key "K_DOWN" action NullAction()
        key "K_LEFT" action NullAction()
        key "w" action NullAction()
        key "d" action NullAction()
        key "s" action NullAction()
        key "a" action NullAction()
        if not bn_game_over:
            timer bn_img_delay repeat True action Function(bn_hide_image)
        add "brawler_%s_%s" % (bn_cpu_name.lower(),bn_img_name)
    if bn_game_over:
        key "K_UP" action NullAction()
        key "K_RIGHT" action NullAction()
        key "K_DOWN" action NullAction()
        key "K_LEFT" action NullAction()
        key "w" action NullAction()
        key "d" action NullAction()
        key "s" action NullAction()
        key "a" action NullAction()
        if not bn_story_fight:
            timer 3 repeat False action Jump("brawler_after_fight_label")
            if bn_mc_won:
                text "You win!" xalign 0.5 yalign 0.8 style "brawler_go_style" at bn_go_transform
            else:
                text "You lose!" xalign 0.5 yalign 0.8 style "brawler_go_style" at bn_go_transform
        else:
            timer 0.1 repeat False action Jump("brawler_after_fight_label")

    if bn_show_counter:
        text "COUNTER!!!" xalign 0.5 yalign 0.8 style "brawler_counter_text_style"
        key "K_SPACE" action (SetVariable("bn_counter", True), SetVariable("bn_show_counter", True))
        key "K_UP" action NullAction()
        key "K_RIGHT" action NullAction()
        key "K_DOWN" action NullAction()
        key "K_LEFT" action NullAction()
        key "w" action NullAction()
        key "d" action NullAction()
        key "s" action NullAction()
        key "a" action NullAction()

    add "brawler_mc_bar_bg" xoffset 4 * persistent.scale_factor yoffset 4 * persistent.scale_factor
    add "brawler_mc_healthbar" xoffset (4-(567-bn_mc_hp*5.67)) * persistent.scale_factor yoffset 4 * persistent.scale_factor

    add "brawler_cpu_bar_bg" xalign 1.0 yalign 0.0 xoffset -4 * persistent.scale_factor yoffset 4 * persistent.scale_factor
    add "brawler_cpu_healthbar1" xalign 1.0 yalign 0.0 yoffset 4 * persistent.scale_factor:
        if bn_cpu_hp <= 100:
            xoffset (-4+(567-bn_cpu_hp*5.67)) * persistent.scale_factor
        else:
            xoffset -4 * persistent.scale_factor

    add "brawler_cpu_healthbar2" xalign 1.0 yalign 0.0 yoffset 4 * persistent.scale_factor:
        if bn_cpu_hp > 100 and bn_cpu_hp <= 200:
            xoffset (-4+(567-(bn_cpu_hp-100)*5.67)) * persistent.scale_factor
        else:
            xoffset 563 * persistent.scale_factor

    add "brawler_bars_ol"

    text "{size=+%d}{i}You{/i}{/size}" % (5 * persistent.scale_factor) xalign 0.245 yalign 0.017 style "bn_name_style"
    text "{i}[bn_cpu_name]{/i}" xalign 0.77 yalign 0.017 style "bn_name_style"
    textbutton "{color=#ffffff}Opponent 1 HP" action SetVariable("bn_cpu_hp",1) text_size 40 yalign 0.01 xalign 0.5
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
    if bn_mc_stamina_lvl > 2:
        imagebutton:
            if bn_mc_stamina >= 6:
                idle "brawler_mc_stamina_full"
                hover "brawler_mc_stamina_full"
            elif bn_mc_stamina >= 5:
                idle "brawler_mc_stamina_half"
                hover "brawler_mc_stamina_half"
            else:
                idle "brawler_mc_stamina_empty"
                hover "brawler_mc_stamina_empty"
            action NullAction()
            xpos 209 * persistent.scale_factor
            ypos 22 * persistent.scale_factor
    if bn_mc_stamina_lvl > 3:
        imagebutton:
            if bn_mc_stamina >= 8:
                idle "brawler_mc_stamina_full"
                hover "brawler_mc_stamina_full"
            elif bn_mc_stamina >= 7:
                idle "brawler_mc_stamina_half"
                hover "brawler_mc_stamina_half"
            else:
                idle "brawler_mc_stamina_empty"
                hover "brawler_mc_stamina_empty"
            action NullAction()
            xpos 279 * persistent.scale_factor
            ypos 22 * persistent.scale_factor
    if bn_mc_stamina_lvl > 4:
        imagebutton:
            if bn_mc_stamina >= 10:
                idle "brawler_mc_stamina_full"
                hover "brawler_mc_stamina_full"
            elif bn_mc_stamina >= 9:
                idle "brawler_mc_stamina_half"
                hover "brawler_mc_stamina_half"
            else:
                idle "brawler_mc_stamina_empty"
                hover "brawler_mc_stamina_empty"
            action NullAction()
            xpos 349 * persistent.scale_factor
            ypos 22 * persistent.scale_factor

    imagebutton:
        if bn_cpu_stamina >= 2:
            idle "brawler_cpu_stamina_full"
            hover "brawler_cpu_stamina_full"
        elif bn_cpu_stamina >= 1:
            idle "brawler_cpu_stamina_half"
            hover "brawler_cpu_stamina_half"
        else:
            idle "brawler_cpu_stamina_empty"
            hover "brawler_cpu_stamina_empty"
        action NullAction()
        xpos 1766 * persistent.scale_factor
        ypos 22 * persistent.scale_factor
    imagebutton:
        if bn_cpu_stamina >= 4:
            idle "brawler_cpu_stamina_full"
            hover "brawler_cpu_stamina_full"
        elif bn_cpu_stamina >= 3:
            idle "brawler_cpu_stamina_half"
            hover "brawler_cpu_stamina_half"
        else:
            idle "brawler_cpu_stamina_empty"
            hover "brawler_cpu_stamina_empty"
        action NullAction()
        xpos 1696 * persistent.scale_factor
        ypos 22 * persistent.scale_factor
    if bn_cpu_stamina_lvl > 2:
        imagebutton:
            if bn_cpu_stamina >= 6:
                idle "brawler_cpu_stamina_full"
                hover "brawler_cpu_stamina_full"
            elif bn_cpu_stamina >= 5:
                idle "brawler_cpu_stamina_half"
                hover "brawler_cpu_stamina_half"
            else:
                idle "brawler_cpu_stamina_empty"
                hover "brawler_cpu_stamina_empty"
            action NullAction()
            xpos 1626 * persistent.scale_factor
            ypos 22 * persistent.scale_factor
    if bn_cpu_stamina_lvl > 3:
        imagebutton:
            if bn_cpu_stamina >= 8:
                idle "brawler_cpu_stamina_full"
                hover "brawler_cpu_stamina_full"
            elif bn_cpu_stamina >= 7:
                idle "brawler_cpu_stamina_half"
                hover "brawler_cpu_stamina_half"
            else:
                idle "brawler_cpu_stamina_empty"
                hover "brawler_cpu_stamina_empty"
            action NullAction()
            xpos 1556 * persistent.scale_factor
            ypos 22 * persistent.scale_factor

screen brawler_arrow_choice_screen:
    tag brawler_arrow_choice_screen
    modal True
    timer bn_timer action [SetVariable("bn_arrow_input", 4),Function(bn_evaluate_input)]
    key "K_UP" action (SetVariable("bn_arrow_input", 0), Function(bn_evaluate_input))
    key "K_RIGHT" action (SetVariable("bn_arrow_input", 1), Function(bn_evaluate_input))
    key "K_DOWN" action (SetVariable("bn_arrow_input", 2), Function(bn_evaluate_input))
    key "K_LEFT" action (SetVariable("bn_arrow_input", 3), Function(bn_evaluate_input))
    key "w" action (SetVariable("bn_arrow_input", 0), Function(bn_evaluate_input))
    key "d" action (SetVariable("bn_arrow_input", 1), Function(bn_evaluate_input))
    key "s" action (SetVariable("bn_arrow_input", 2), Function(bn_evaluate_input))
    key "a" action (SetVariable("bn_arrow_input", 3), Function(bn_evaluate_input))


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

screen brawler_rage_screen:
    tag brawler_rage_screen
    modal True
    default end_time = time.time() + bn_rage_time
    default current_time = time.time()

    if not bn_rage_ending:
        timer 0.05 repeat True action If(current_time < end_time, true=SetScreenVariable('current_time', time.time()), false=SetVariable("bn_rage_ending", True))
        bar value (end_time-current_time)*100 range bn_rage_time*100 xalign 0.5 yalign 0.95 xmaximum 320 * persistent.scale_factor style "rage_bar_style"

    if bn_rage_ending:
        timer 3 action Function(bn_end_rage)
        key "K_UP" action NullAction()
        key "K_RIGHT" action NullAction()
        key "K_DOWN" action NullAction()
        key "K_LEFT" action NullAction()
        key "w" action NullAction()
        key "d" action NullAction()
        key "s" action NullAction()
        key "a" action NullAction()
    else:
        key "K_UP" action (SetVariable("bn_combo_input", "up"), Function(bn_evaluate_rage))
        key "K_RIGHT" action (SetVariable("bn_combo_input", "right"), Function(bn_evaluate_rage))
        key "K_DOWN" action (SetVariable("bn_combo_input", "down"), Function(bn_evaluate_rage))
        key "K_LEFT" action (SetVariable("bn_combo_input", "left"), Function(bn_evaluate_rage))
        key "w" action (SetVariable("bn_combo_input", "up"), Function(bn_evaluate_rage))
        key "d" action (SetVariable("bn_combo_input", "right"), Function(bn_evaluate_rage))
        key "s" action (SetVariable("bn_combo_input", "down"), Function(bn_evaluate_rage))
        key "a" action (SetVariable("bn_combo_input", "left"), Function(bn_evaluate_rage))

    if bn_rage_flash:
        timer 0.5 action SetVariable("bn_rage_flash", False)

    add "brawler_rage_text" at brawler_rage_zoom xalign 0.5 yalign 0.65

    if bn_rage_ending:
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

screen brawler_arrow_combo_screen:
    tag brawler_arrow_combo_screen
    modal True
    default end_time = time.time() + bn_timer
    default current_time = time.time()
    timer 0.05 repeat True action If(current_time < end_time, true=SetScreenVariable('current_time', time.time()), false=[SetVariable("bn_combo_input", ""),Function(bn_evaluate_combo)])
    key "K_UP" action (SetVariable("bn_combo_input", "up"), Function(bn_evaluate_combo))
    key "K_RIGHT" action (SetVariable("bn_combo_input", "right"), Function(bn_evaluate_combo))
    key "K_DOWN" action (SetVariable("bn_combo_input", "down"), Function(bn_evaluate_combo))
    key "K_LEFT" action (SetVariable("bn_combo_input", "left"), Function(bn_evaluate_combo))
    key "w" action (SetVariable("bn_combo_input", "up"), Function(bn_evaluate_combo))
    key "d" action (SetVariable("bn_combo_input", "right"), Function(bn_evaluate_combo))
    key "s" action (SetVariable("bn_combo_input", "down"), Function(bn_evaluate_combo))
    key "a" action (SetVariable("bn_combo_input", "left"), Function(bn_evaluate_combo))


    hbox:
        xalign 0.5
        yalign 0.8
        for direction in range(0,len(bn_arrow_combination)):
            if bn_combo_idx > direction:
                add "brawler_arrow_%s_hover" % bn_arrow_combination[direction]
            else:
                add "brawler_arrow_%s_idle" % bn_arrow_combination[direction]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

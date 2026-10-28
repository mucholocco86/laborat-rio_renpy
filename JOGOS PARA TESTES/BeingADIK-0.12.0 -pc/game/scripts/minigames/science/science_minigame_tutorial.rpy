style sm_tut_style:
    color "#ffe059"
    font "fonts/cabin-regular.ttf"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 30 * persistent.scale_factor
    text_align 0.5
style sm_tut_style2:
    color "#ffe059"
    font "fonts/cabin-regular.ttf"
    outlines [ (absolute(2), "#2d2d2d", absolute(1), absolute(1)) ]
    size 30 * persistent.scale_factor
    text_align 0.5

screen sm_weigh_tut_screen:
    tag sm_weigh_tut_screen
    modal True
    add "science_minigame_weigh"

    text "Use the + and - buttons to add or remove salt. Try to add 30 units of the blue salt." style "sm_tut_style" xmaximum 700 * persistent.scale_factor xalign 0.95 yalign 0.3

    text "It can be tricky to end up with the exact amount.\nYou can continue the experiment if the weight is slightly off, but your final score will be penalized." style "sm_tut_style" xmaximum 700 * persistent.scale_factor xalign 0.95 yalign 0.85

    text "%s" % sm_weigh_result style "sm_weigh_digit_style" xalign 0.45 yalign 0.88
    vbox:
        xalign 0.85
        yalign 0.40
        text "{size=-%d}%s{/size}" % ((50 * persistent.scale_factor), sm_weigh_result) style "sm_measure_style_yellow" xalign 0.5 yoffset 220 * persistent.scale_factor
        hbox:
            spacing 300 * persistent.scale_factor
            textbutton "-" text_style "sm_weigh_button_style" action Function(sm_weigh_subtract)
            textbutton "+" text_style "sm_weigh_button_style" action Function(sm_weigh_add)
        textbutton "Ok" text_style "sm_measure_button_style" action If (sm_weigh_result > 0, Jump("ep10_science_tut1_label")) xalign 0.5 yoffset 20 * persistent.scale_factor

screen sm_measure_tut_screen:
    tag sm_measure_tut_screen
    modal True
    add "science_minigame_measure_empty"

    if sm_measure_phase == 0:
        text "When measuring liquids, use the + and - buttons to choose the volume to measure.\nChoose to measure 20 units." style "sm_tut_style" xmaximum 700 * persistent.scale_factor xalign 0.85 yalign 0.15

        text "How much do you want to measure?" style "sm_measure_style" xalign 0.9 yalign 0.3
        vbox:
            xalign 0.60
            yalign 0.48
            textbutton "{size=+%d}+{/size}" % (90 * persistent.scale_factor) text_style "sm_measure_button_style" action SetVariable("sm_measure_vol",min(100,sm_measure_vol+10))
            textbutton "{size=+%d}-{/size}" % (90 * persistent.scale_factor) text_style "sm_measure_button_style" action SetVariable("sm_measure_vol",max(0,sm_measure_vol-10)) yoffset -50 * persistent.scale_factor
        vbox:
            text "%s" % sm_measure_vol style "sm_measure_style_yellow" xalign 1.0
            xalign 0.75 yalign 0.45
            xminimum 500 * persistent.scale_factor
        vbox:
            xalign 0.92
            yalign 0.46
            spacing 40 * persistent.scale_factor
            textbutton "Ok" text_style "sm_measure_button_style" action If (sm_measure_vol == 20, (SetVariable("sm_measure_phase", 1)))
            textbutton "Cancel" text_style "sm_measure_button_style" action NullAction()
    elif sm_measure_phase == 1:
        text "To measure a perfect volume, make the arrow stop at the middle of the bar." style "sm_tut_style" xmaximum 700 * persistent.scale_factor xalign 0.90 yalign 0.3
        imagebutton:
            idle "sm_bar"
            hover "sm_bar"
            action NullAction()
            xalign 0.98
            yalign 0.5

        add "sm_arrow_moving"
        vbox:
            xalign 0.78
            yalign 0.42
            spacing 40 * persistent.scale_factor
            textbutton "Try it" text_style "sm_measure_button_style" action (SetVariable("sm_measure_phase", 3),Show("sm_measure_bar_screen"))
    elif sm_measure_phase == 2:
        if sm_measure_result_vol - sm_measure_vol == 0:
            add "sm_measure_%s" % "red" at sm_measure_perfect_transform
        elif sm_measure_result_vol - sm_measure_vol > 3:
            add "sm_measure_%s" % "red" at sm_measure_way_over_transform
        elif sm_measure_result_vol - sm_measure_vol > 0:
            add "sm_measure_%s" % "red" at sm_measure_over_transform
        elif sm_measure_result_vol - sm_measure_vol > -4:
            add "sm_measure_%s" % "red" at sm_measure_under_transform
        else:
            add "sm_measure_%s" % "red" at sm_measure_way_under_transform
        vbox:
            xalign 0.8
            yalign 0.2
            text "{size=+%d}You measured{/size}" % (50 * persistent.scale_factor) style "sm_measure_style" xalign 0.5
            text "%s" % sm_measure_result_vol style "sm_measure_style_yellow" xalign 0.5
        hbox:
            xalign 0.9
            yalign 0.6
            spacing 80 * persistent.scale_factor
            textbutton "Ok" text_style "sm_measure_button_style" action Jump("ep10_science_tut2_label")
            textbutton "Retry ({color=bb433b}-5 seconds{/color})" text_style "sm_measure_button_style" action (SetVariable("sm_measure_phase", 3),Show("sm_measure_bar_screen"))

        text "If you're not satisfied with the measured volume, you can choose to retry. You will lose 5 seconds extra for every retry.\nYour final score will be penalized if your measured volume isn't spot on with what you need." style "sm_tut_style" xmaximum 900 * persistent.scale_factor xalign 0.90 yalign 0.8
    add "sm_measure_line"

screen sm_stirrer_tut_screen:
    tag sm_stirrer_tut_screen
    modal True

    if sm_stirrer_on:
        add "science_minigame_stir_green_bubbles"
    else:
        add "science_minigame_stir_green"

    vbox:
        spacing 50 * persistent.scale_factor
        xalign 0.95 yalign 0.2
        hbox:
            spacing 100 * persistent.scale_factor
            textbutton "Stirrer:" text_style "sm_stir_style" xalign 0.5

            textbutton "On" text_style "sm_stir_button_style" action (Function(sm_play_stirrer),SetVariable("sm_stirrer_on", True))
            textbutton "Off" text_style "sm_stir_button_style" action (Function(sm_play_stirrer_stop),SetVariable("sm_stirrer_on", False))

        hbox:
            spacing 100 * persistent.scale_factor
            textbutton "Speed:" text_style "sm_stir_style" xalign 0.5
            textbutton "Slow" text_style "sm_stir_button_style" action SetVariable("sm_stirrer_mode", 0)
            textbutton "Medium" text_style "sm_stir_button_style" action SetVariable("sm_stirrer_mode", 1)
            textbutton "Fast" text_style "sm_stir_button_style" action SetVariable("sm_stirrer_mode", 2)


        textbutton "Ok" text_style "sm_measure_button_style" action If(sm_stirrer_mode==2 and sm_stirrer_on, [Function(sm_play_stirrer_stop),Jump("ep10_science_tut3_label")]) xalign 0.5

    text "Check the instructions for the stirrer setting you need.\nDon't forget to turn the stirrer on when stirring.\nMake the stirrer stir at Fast speed." style "sm_tut_style" xmaximum 800 * persistent.scale_factor xalign 0.95 yalign 0.5

screen science_tut_screen:
    tag science_tut_screen
    modal True

    if sm_tut_text != 9 and sm_tut_text != 10 and sm_tut_text != 13 and sm_tut_text != 14 and sm_tut_text != 15 and sm_tut_text != 19 and sm_tut_text != 20 and sm_tut_text != 23 and sm_tut_text != 24:
        imagebutton:
            idle "science_minigame_neutral"
            hover "science_minigame_neutral"
            if sm_tut_text == 27:
                action (Jump("ep10_science_tut4_label"))
            elif sm_tut_text == 6 or sm_tut_text == 8 or sm_tut_text == 11 or sm_tut_text == 12 or sm_tut_text == 15 or sm_tut_text == 16 or sm_tut_text == 17 or sm_tut_text == 18:
                action (Function(sm_play_notepad),SetVariable("sm_tut_text", sm_tut_text + 1))
            else:
                action SetVariable("sm_tut_text", sm_tut_text + 1)

    if sm_button_set > 0:
        if sm_button_set == 1:
            vbox:
                xalign 0.105
                yalign 0.7
                textbutton "Pour" text_style "sm_button_menu_style":
                    xalign 0.5
                    action (Function(sm_clear_selection), SetVariable("sm_pour_mode",1), Show("sm_pour_tut_screen"))
                textbutton "Discard" text_style "sm_button_menu_style" action NullAction() xalign 0.5
        elif sm_button_set == 2:
            vbox:
                xalign 0.256
                yalign 0.76
                textbutton "Add to" text_style "sm_button_menu_style":
                    xalign 0.5
                    action (Function(sm_clear_selection), SetVariable("sm_pour_mode",2), Show("sm_pour_tut_screen"))
                textbutton "Discard" text_style "sm_button_menu_style" action NullAction() xalign 0.5
        elif sm_button_set == 3:
            vbox:
                xalign 0.50
                yalign 0.76
                textbutton "Stir settings" text_style "sm_button_menu_style":
                    xalign 0.5
                    action (Function(sm_clear_selection),Show("sm_stir_screen"))
                textbutton "Pour" text_style "sm_button_menu_style":
                    xalign 0.5
                    action (Function(sm_clear_selection), SetVariable("sm_pour_mode",3), Show("sm_pour_tut_screen"))
                textbutton "Discard" text_style "sm_button_menu_style" action NullAction() xalign 0.5
        elif sm_button_set == 4:
            vbox:
                xalign 0.65
                yalign 0.2
                textbutton "Turn in" text_style "sm_button_menu_style":
                    xalign 0.5
                    action Function(sm_clear_selection), SetVariable("sm_tut_text",sm_tut_text+1)
                textbutton "Discard" text_style "sm_button_menu_style" action NullAction() xalign 0.5


    imagebutton:
        idle "sm_notepad_idle"
        hover "sm_notepad_hover"
        focus_mask True
        if sm_tut_text == 6 or sm_tut_text == 11:
            action (Function(sm_play_notepad),SetVariable("sm_tut_text",sm_tut_text+1))
        else:
            action NullAction()


    imagebutton:
        idle "sm_vol_%s_idle" % sm_vol_str
        hover "sm_vol_%s_hover" % sm_vol_str
        focus_mask True
        if sm_tut_text == 14:
            action SetVariable("sm_button_set",1)
        else:
            action NullAction()


    imagebutton:
        idle "sm_scale_%s_idle" % sm_scale_str
        hover "sm_scale_%s_hover" % sm_scale_str
        focus_mask True
        if sm_tut_text == 10:
            action SetVariable("sm_button_set",2)
        else:
            action NullAction()


    imagebutton:
        idle "sm_red_liquid_idle"
        hover "sm_red_liquid_hover"
        focus_mask True
        if sm_tut_text == 13:
            action Jump("ep10_science_tut1b_label")
        else:
            action NullAction()
    imagebutton:
        idle "sm_green_liquid_idle"
        hover "sm_green_liquid_hover"
        focus_mask True
        action NullAction()
    imagebutton:
        idle "sm_blue_liquid_idle"
        hover "sm_blue_liquid_hover"
        focus_mask True
        action NullAction()


    imagebutton:
        idle "sm_red_solids_idle"
        hover "sm_red_solids_hover"
        focus_mask True
        action NullAction()
    imagebutton:
        idle "sm_blue_solids_idle"
        hover "sm_blue_solids_hover"
        focus_mask True
        if sm_tut_text == 9:
            action Jump("ep10_science_tut0_label")
        else:
            action NullAction()


    imagebutton:
        if sm_stirrer_on:
            idle "sm_stirrer_%s_bubbles_idle" % sm_stirrer_str
            hover "sm_stirrer_%s_bubbles_hover" % sm_stirrer_str
        else:
            idle "sm_stirrer_%s_idle" % sm_stirrer_str
            hover "sm_stirrer_%s_hover" % sm_stirrer_str
        focus_mask True
        if sm_tut_text == 15:
            action Jump("ep10_science_tut2b_label")
        elif sm_tut_text == 19:
            action SetVariable("sm_button_set",3)
        else:
            action NullAction()


    imagebutton:
        if sm_bunsen_on:
            idle "sm_bunsen_on_idle"
            hover "sm_bunsen_on_hover"
            focus_mask True
            action NullAction()
        else:
            idle "sm_bunsen_off_idle"
            hover "sm_bunsen_off_hover"
            focus_mask True
            if sm_tut_text == 20:
                action (Function(sm_play_burner),Function(sm_clear_selection),Function(sm_bunsen,True),Jump("ep10_science_tut3b_label"))
            else:
                action NullAction()


    imagebutton:
        if sm_bunsen_on:
            idle "sm_round_%s_bubbles_idle" % sm_round_str
            hover "sm_round_%s_bubbles_hover" % sm_round_str
        else:
            idle "sm_round_%s_idle" % sm_round_str
            hover "sm_round_%s_hover" % sm_round_str
        focus_mask True
        if sm_tut_text == 23:
            action SetVariable("sm_button_set",4)
        else:
            action NullAction()

    if sm_tut_text > 0 or sm_tut_text < 7 or sm_tut_text == 9:

        if sm_tut_text != 3 and sm_tut_text != 4 and sm_tut_text != 5 and sm_tut_text != 6:
            text "Liquids\n{color=#ffffff}Red  Green  Blue{/color}" style "sm_help_style" xalign 0.14 yalign 0.24 text_align 0.5
            text "Volumetric flask" style "sm_help_style" xalign 0.07 yalign 0.42
        if sm_tut_text != 2 and sm_tut_text != 4 and sm_tut_text != 5 and sm_tut_text != 6:
            text "Salts\n{color=#ffffff}Red   Blue{/color}" style "sm_help_style" xalign 0.3 yalign 0.18 text_align 0.5
            text "Scale" style "sm_help_style" xalign 0.27 yalign 0.47
        if sm_tut_text != 2 and sm_tut_text != 3 and sm_tut_text != 5 and sm_tut_text != 6:
            text "Stirrer" style "sm_help_style" xalign 0.498 yalign 0.415
        if sm_tut_text != 2 and sm_tut_text != 3 and sm_tut_text != 4 and sm_tut_text != 6:
            text "Round flask" style "sm_help_style" xalign 0.714 yalign 0.35
            text "Bunsen burner" style "sm_help_style" xalign 0.705 yalign 0.668
        if sm_tut_text != 2 and sm_tut_text != 3 and sm_tut_text != 4 and sm_tut_text != 5:
            text "Notepad" style "sm_help_style" xalign 0.89 yalign 0.34

    if sm_tut_text == 24:
        imagebutton:
            idle "science_minigame_results_red"
            hover "science_minigame_results_red"
            action SetVariable("sm_tut_text", sm_tut_text + 1)


    if sm_tut_text == 0:
        text "In the Science mini-game, your task is to carry out a specific experiment by mixing chemicals within a time limit." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 1:
        text "This is your desk space where you can find every chemical and piece of equipment you need." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 2:
        text "You have liquid chemicals and a volumetric flask to measure them to the far left." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 3:
        text "You have solid chemicals - salts - and a scale to weigh them here." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 4:
        text "You can mix chemicals using the magnetic stirrer." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 5:
        text "You can add chemicals to the round flask and use the burner when necessary." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 6:
        text "The notepad contains all the instructions you need to carry out your experiment. Let's have a look at it." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text > 6 and sm_tut_text < 9 or sm_tut_text == 12 or sm_tut_text == 16 or sm_tut_text == 18 or sm_tut_text == 21 or sm_tut_text == 25:
        add "science_minigame_notes"
        if sm_tut_text == 12:
            text "Step 2 tells you to measure 20 units of red liquid and pour it into the beaker on the stirrer." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
        elif sm_tut_text == 16:
            text "Step 4 tells you to check the color of the solution.\nBased on the color, you either add green liquid or skip this step.\nLet's check the color." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
        elif sm_tut_text == 18:
            text "Step 5 tells us to pour the solution into the round flask and turn on the burner.\nLet's do that." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
        elif sm_tut_text == 21:
            text "Steps 6 and 7 tell us that the solution should boil for 5 seconds. And that we can turn in our mixture if the color is red." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
        elif sm_tut_text == 25:
            text "Buying the Pencil perk from Magnar will let you click the steps in the notepad to check them off as you go.\nThis is an easy way to keep track of your progress when you're doing your experiment, and it's not considered cheating." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
        elif sm_tut_text == 7:
            text "Follow the steps from top to bottom to complete the mini-game. Pay extra attention to steps that have multiple outcomes." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
        else:
            text "Step 1 tells you to weigh 30 units of blue salt and add it to the beaker on the stirrer. Let's do that." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9

        text "{size=+%d}Science 101{/size}" % (20 * persistent.scale_factor) style "sm_notes_style" xalign 0.48 yalign 0.2

        vbox:
            xalign 0.48
            yalign 0.45
            xmaximum 600 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Tutorial Experiment" style "sm_notes_style" xalign 0.5
            if sm_tut_text == 25:
                textbutton "{s}Step 1 - Weigh 30 units of blue salt and add it to the beaker on the stirrer.{/s}" text_style "sm_notes_style":
                    action NullAction()
            else:
                textbutton "Step 1 - Weigh 30 units of blue salt and add it to the beaker on the stirrer." text_style "sm_notes_style":
                    action NullAction()
            if sm_tut_text == 25:
                textbutton "{s}Step 2 - Measure 20 units of red liquid and pour it into the beaker on the stirrer. The color should come out green.{/s}" text_style "sm_notes_style":
                    action NullAction()
            else:
                textbutton "Step 2 - Measure 20 units of red liquid and pour it into the beaker on the stirrer. The color should come out green." text_style "sm_notes_style":
                    action NullAction()
            textbutton "Step 3 - Stir at Fast speed for 5 seconds and wait for the color to change." text_style "sm_notes_style":
                action NullAction()
            textbutton "Step 4 - If the color is blue, measure 10 units of green liquid and pour it into the beaker on the stirrer. But if the solution is colorless, you can skip this step." text_style "sm_notes_style":
                action NullAction()
            textbutton "Step 5 - After the color has changed, pour the solution into the round flask and turn on the burner." text_style "sm_notes_style":
                action NullAction()
            textbutton "Step 6 - Let the solution boil for 5 seconds. If the color is red, your reaction is complete." text_style "sm_notes_style":
                action NullAction()
            textbutton "Step 7 - Turn in your mixture, and let's assess the purity together." text_style "sm_notes_style":
                action NullAction()
    elif sm_tut_text == 9:
        text "Click the blue salt." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 10:
        text "The blue salt has been weighed, and now you have to add it to the beaker on the stirrer.\nClick the scale and choose to add its contents to the stirrer." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 11:
        text "Now that Step 1 is complete, let's have another look at the notepad." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 13:
        text "Click the red liquid." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 14:
        text "Pour the contents of the volumetric flask into the beaker on the stirrer." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 15:
        text "Just like Step 2 said, the color of the solution is green.\nStep 3 tells you to stir at Fast speed for 5 seconds and wait for a color change.\nClick the stirrer." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 17:
        text "The solution is colorless.\nThis means that we can skip Step 4." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 19:
        text "Click the beaker on the stirrer and pour the contents into the round flask." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 20:
        text "Great! Turn on the burner by clicking it." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 22:
        text "The color is red, like Step 6 said, and we can turn it in for assessment.\nNote that if the color wasn't red, we might have done something wrong along the way.\nIn that case, we would have to discard the chemical and start over." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 23:
        text "Click the round flask and turn in the chemical. You will always end the mini-game by turning in a chemical." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 24:
        text "You can buy extra time and a purity boost from Derek and Magnar. Studying Science at your desk in your room will boost the extra time, too." style "sm_tut_style2" xmaximum 500 * persistent.scale_factor xalign 0.93 yalign 0.4
    elif sm_tut_text == 26:
        text "When in doubt about what to do.\n1. Read the step you're at.\n2. Execute it.\n3. Move on to the next step." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9
    elif sm_tut_text == 27:
        text "Be methodical and follow the experiment like a recipe, and you will be a scientist in no time.\nThis concludes the tutorial." style "sm_tut_style2" xmaximum 1600 * persistent.scale_factor xalign 0.5 yalign 0.9

screen sm_pour_tut_screen:
    tag sm_pour_tut_screen
    modal True

    if sm_tut_text == 10:
        vbox:
            xalign 0.50
            yalign 0.68
            textbutton "Add to beaker" text_style "sm_button_menu_style" action (SetVariable("sm_scale_str","empty"),SetVariable("sm_tut_text",11),Hide("sm_pour_tut_screen")) xalign 0.5
    elif sm_tut_text == 14:
        vbox:
            xalign 0.50
            yalign 0.68
            textbutton "Add to beaker" text_style "sm_button_menu_style" action (Function(sm_play_pour),SetVariable("sm_stirrer_str","green"),SetVariable("sm_vol_str","empty"),SetVariable("sm_tut_text",15),Hide("sm_pour_tut_screen")) xalign 0.5
    elif sm_tut_text == 19:
        vbox:
            xalign 0.725
            yalign 0.39
            textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_play_pour),SetVariable("sm_stirrer_str","empty"),SetVariable("sm_round_str","clear"),SetVariable("sm_tut_text",20),Hide("sm_pour_tut_screen")) xalign 0.5

    else:
        if sm_pour_mode == 1:
            vbox:
                xalign 0.105
                yalign 0.67
                textbutton "Cancel" text_style "sm_button_menu_style" action Hide("sm_pour_tut_screen") xalign 0.5
            vbox:
                xalign 0.50
                yalign 0.68
                textbutton "Add to beaker" text_style "sm_button_menu_style" action (Function(sm_add_to_beaker),Hide("sm_pour_tut_screen")) xalign 0.5
            vbox:
                xalign 0.725
                yalign 0.39
                textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_add_to_flask),Hide("sm_pour_tut_screen")) xalign 0.5
        elif sm_pour_mode == 2:
            vbox:
                xalign 0.256
                yalign 0.72
                textbutton "Cancel" text_style "sm_button_menu_style" action Hide("sm_pour_tut_screen") xalign 0.5
            vbox:
                xalign 0.50
                yalign 0.68
                textbutton "Add to beaker" text_style "sm_button_menu_style" action (Function(sm_add_to_beaker),Hide("sm_pour_tut_screen")) xalign 0.5
            vbox:
                xalign 0.725
                yalign 0.39
                textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_add_to_flask),Hide("sm_pour_tut_screen")) xalign 0.5
        elif sm_pour_mode == 3:
            vbox:
                xalign 0.50
                yalign 0.68
                textbutton "Cancel" text_style "sm_button_menu_style" action Hide("sm_pour_tut_screen") xalign 0.5
            vbox:
                xalign 0.725
                yalign 0.39
                textbutton "Add to round flask" text_style "sm_button_menu_style" action (Function(sm_add_to_flask),Hide("sm_pour_tut_screen")) xalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

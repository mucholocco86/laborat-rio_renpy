style sm_notes_style:
    font "fonts/cabin-regular.ttf"
    size 18 * persistent.scale_factor
    color "#2d2d2d"
    hover_color "#bb433b"

screen sm_notes_screen:
    tag sm_notes_screen
    modal True
    imagebutton:
        idle "science_minigame_notes"
        hover "science_minigame_notes"
        action Function(sm_play_notepad),Hide("sm_notes_screen")

    if sm_experiment == 1:
        text "{size=+%d}Science 101{/size}" % (20 * persistent.scale_factor) style "sm_notes_style" xalign 0.48 yalign 0.2
    elif sm_experiment == 2:
        text "{size=+%d}Science 101{/size}" % (20 * persistent.scale_factor) style "sm_notes_style" xalign 0.48 yalign 0.17

    if sm_experiment == 1:
        vbox:
            xalign 0.48
            yalign 0.6
            xmaximum 600 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Experiment 1" style "sm_notes_style" xalign 0.5
            if sm_notes[0]:
                textbutton "{s}Step 1 - Measure %d %s liquid and pour it into the beaker on the stirrer.{/s}" % (sm_experiment_list[0][1],sm_experiment_list[0][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,0,not sm_notes[0]), Function(sm_play_sketch)
            else:
                textbutton "Step 1 - Measure %d %s liquid and pour it into the beaker on the stirrer." % (sm_experiment_list[0][1],sm_experiment_list[0][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,0,not sm_notes[0]), Function(sm_play_sketch)
            if sm_notes[1]:
                textbutton "{s}Step 2 - Weigh %d %s salt and add it to the beaker on the stirrer. The color should come out green.{/s}" % (sm_experiment_list[1][1],sm_experiment_list[1][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,1,not sm_notes[1]), Function(sm_play_sketch)
            else:
                textbutton "Step 2 - Weigh %d %s salt and add it to the beaker on the stirrer. The color should come out green." % (sm_experiment_list[1][1],sm_experiment_list[1][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,1,not sm_notes[1]), Function(sm_play_sketch)
            if sm_notes[2]:
                textbutton "{s}Step 3 - Stir at %s speed for 5 seconds and note the color.{/s}" % sm_experiment_list[2][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,2,not sm_notes[2]), Function(sm_play_sketch)
            else:
                textbutton "Step 3 - Stir at %s speed for 5 seconds and note the color." % sm_experiment_list[2][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,2,not sm_notes[2]), Function(sm_play_sketch)
            if sm_notes[3]:
                textbutton "{s}Step 4 - If the color is clear, measure %d green liquid and pour it into the beaker on the stirrer. But if the color is %s, weigh %d %s salt and add it to the beaker on the stirrer.{/s}"  % (sm_experiment_list[3][2],sm_experiment_list[4][0],sm_experiment_list[4][2],sm_experiment_list[4][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,3,not sm_notes[3]), Function(sm_play_sketch)
            else:
                textbutton "Step 4 - If the color is clear, measure %d green liquid and pour it into the beaker on the stirrer. But if the color is %s, weigh %d %s salt and add it to the beaker on the stirrer."  % (sm_experiment_list[3][2],sm_experiment_list[4][0],sm_experiment_list[4][2],sm_experiment_list[4][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,3,not sm_notes[3]), Function(sm_play_sketch)
            if sm_notes[4]:
                textbutton "{s}Step 5 - Stir at %s speed for 5 seconds and wait for the color to change.{/s}" % sm_experiment_list[5][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,4,not sm_notes[4]), Function(sm_play_sketch)
            else:
                textbutton "Step 5 - Stir at %s speed for 5 seconds and wait for the color to change." % sm_experiment_list[5][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,4,not sm_notes[4]), Function(sm_play_sketch)
            if sm_notes[5]:
                textbutton "{s}Step 6 - After the color has changed, pour the solution into the round flask and turn on the burner.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,5,not sm_notes[5]), Function(sm_play_sketch)
            else:
                textbutton "Step 6 - After the color has changed, pour the solution into the round flask and turn on the burner." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,5,not sm_notes[5]), Function(sm_play_sketch)
            if sm_notes[6]:
                textbutton "{s}Step 7 - Wait 5 seconds. If the solution is colorless, measure %d green liquid and add it to the round flask. If the solution has any other color, weigh %d blue salt and add it to the round flask.{/s}" % (sm_experiment_list[6][1],sm_experiment_list[7][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,6,not sm_notes[6]), Function(sm_play_sketch)
            else:
                textbutton "Step 7 - Wait 5 seconds. If the solution is colorless, measure %d green liquid and add it to the round flask. If the solution has any other color, weigh %d blue salt and add it to the round flask." % (sm_experiment_list[6][1],sm_experiment_list[7][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,6,not sm_notes[6]), Function(sm_play_sketch)
            if sm_notes[7]:
                textbutton "{s}Step 8 - Let the solution boil for 5 seconds. If the color is blue, your reaction is complete.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,7,not sm_notes[7]), Function(sm_play_sketch)
            else:
                textbutton "Step 8 - Let the solution boil for 5 seconds. If the color is blue, your reaction is complete." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,7,not sm_notes[7]), Function(sm_play_sketch)
            if sm_notes[8]:
                textbutton "{s}Step 9 - Turn in your mixture, and let's assess the purity together.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,8,not sm_notes[8]), Function(sm_play_sketch)
            else:
                textbutton "Step 9 - Turn in your mixture, and let's assess the purity together." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,8,not sm_notes[8]), Function(sm_play_sketch)

    elif sm_experiment == 2:

        vbox:
            xalign 0.48
            yalign 0.6
            xmaximum 600 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Experiment 2" style "sm_notes_style" xalign 0.5
            if sm_notes[0]:
                textbutton "{s}Step 1 - Weigh %d %s salt and add it to the beaker on the stirrer.{/s}" % (sm_experiment_list[0][1],sm_experiment_list[0][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,0,not sm_notes[0]), Function(sm_play_sketch)
            else:
                textbutton "Step 1 - Weigh %d %s salt and add it to the beaker on the stirrer." % (sm_experiment_list[0][1],sm_experiment_list[0][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,0,not sm_notes[0]), Function(sm_play_sketch)
            if sm_notes[1]:
                textbutton "{s}Step 2 - Weigh %d %s salt and add it to the beaker on the stirrer.{/s}" % (sm_experiment_list[1][1],sm_experiment_list[1][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,1,not sm_notes[1]), Function(sm_play_sketch)
            else:
                textbutton "Step 2 - Weigh %d %s salt and add it to the beaker on the stirrer." % (sm_experiment_list[1][1],sm_experiment_list[1][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,1,not sm_notes[1]), Function(sm_play_sketch)
            if sm_notes[2]:
                textbutton "{s}Step 3 - Measure %d %s liquid and pour it into the beaker on the stirrer.{/s}" % (sm_experiment_list[2][1],sm_experiment_list[2][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,2,not sm_notes[2]), Function(sm_play_sketch)
            else:
                textbutton "Step 3 - Measure %d %s liquid and pour it into the beaker on the stirrer." % (sm_experiment_list[2][1],sm_experiment_list[2][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,2,not sm_notes[2]), Function(sm_play_sketch)
            if sm_notes[3]:
                textbutton "{s}Step 4 - Stir at %s speed for 10 seconds and wait for the color to change.{/s}" % sm_experiment_list[3][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,3,not sm_notes[3]), Function(sm_play_sketch)
            else:
                textbutton "Step 4 - Stir at %s speed for 10 seconds and wait for the color to change." % sm_experiment_list[3][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,3,not sm_notes[3]), Function(sm_play_sketch)


            if sm_notes[4]:
                textbutton "{s}Step 5 - If the color is blue, measure %d %s liquid and pour it into the beaker on the stirrer. But if the color is clear, weigh %d %s salt and add it to the beaker on the stirrer.{/s}"  % (sm_experiment_list[4][1],sm_experiment_list[4][0],sm_experiment_list[5][1],sm_experiment_list[5][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,4,not sm_notes[4]), Function(sm_play_sketch)
            else:
                textbutton "Step 5 - If the color is blue, measure %d %s liquid and pour it into the beaker on the stirrer. But if the color is clear, weigh %d %s salt and add it to the beaker on the stirrer."  % (sm_experiment_list[4][1],sm_experiment_list[4][0],sm_experiment_list[5][1],sm_experiment_list[5][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,4,not sm_notes[4]), Function(sm_play_sketch)

            if sm_notes[5]:
                textbutton "{s}Step 6 - Stir at %s speed for 5 seconds and wait for the color to change.{/s}" % sm_experiment_list[6][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,5,not sm_notes[5]), Function(sm_play_sketch)
            else:
                textbutton "Step 6 - Stir at %s speed for 5 seconds and wait for the color to change." % sm_experiment_list[6][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,5,not sm_notes[5]), Function(sm_play_sketch)

            if sm_notes[6]:
                textbutton "{s}Step 7 - After the color has changed, pour the solution into the round flask and turn on the burner.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,6,not sm_notes[6]), Function(sm_play_sketch)
            else:
                textbutton "Step 7 - After the color has changed, pour the solution into the round flask and turn on the burner." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,6,not sm_notes[6]), Function(sm_play_sketch)

            if sm_notes[7]:
                textbutton "{s}Step 8 - Wait 10 seconds. If the solution is green, measure %d red liquid and add it to the round flask. If the solution is clear, weigh %d red salt and add it to the round flask.{/s}" % (sm_experiment_list[7][1],sm_experiment_list[8][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,7,not sm_notes[7]), Function(sm_play_sketch)
            else:
                textbutton "Step 8 - Wait 10 seconds. If the solution is green, measure %d red liquid and add it to the round flask. If the solution is clear, weigh %d red salt and add it to the round flask." % (sm_experiment_list[7][1],sm_experiment_list[8][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,7,not sm_notes[7]), Function(sm_play_sketch)

            if sm_notes[8]:
                textbutton "{s}Step 9 - Let the solution boil for 10 seconds. After the color turns blue, turn off the burner.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,8,not sm_notes[8]), Function(sm_play_sketch)
            else:
                textbutton "Step 9 - Let the solution boil for 10 seconds. After the color turns blue, turn off the burner." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,8,not sm_notes[8]), Function(sm_play_sketch)
            if sm_notes[9]:
                textbutton "{s}Step 10 - Let the solution cool down for 10 seconds. If the color turns green, your reaction is complete.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,9,not sm_notes[9]), Function(sm_play_sketch)
            else:
                textbutton "Step 10 - Let the solution cool down for 10 seconds. If the color turns green, your reaction is complete." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,9,not sm_notes[9]), Function(sm_play_sketch)
            if sm_notes[10]:
                textbutton "{s}Step 11 - Turn in your mixture, and let's assess the purity together.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,10,not sm_notes[10]), Function(sm_play_sketch)
            else:
                textbutton "Step 11 - Turn in your mixture, and let's assess the purity together." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,10,not sm_notes[10]), Function(sm_play_sketch)
    elif sm_experiment == 3:

        vbox:
            xalign 0.48
            yalign 0.6
            xmaximum 600 * persistent.scale_factor
            spacing 10 * persistent.scale_factor
            text "Experiment 3" style "sm_notes_style" xalign 0.5
            if sm_notes[0]:
                textbutton "{s}Step 1 - Weigh %d %s salt and add it to the beaker on the stirrer.{/s}" % (sm_experiment_list[0][1],sm_experiment_list[0][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,0,not sm_notes[0]), Function(sm_play_sketch)
            else:
                textbutton "Step 1 - Weigh %d %s salt and add it to the beaker on the stirrer." % (sm_experiment_list[0][1],sm_experiment_list[0][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,0,not sm_notes[0]), Function(sm_play_sketch)
            if sm_notes[1]:
                textbutton "{s}Step 2 - Weigh %d %s salt and add it to the beaker on the stirrer.{/s}" % (sm_experiment_list[1][1],sm_experiment_list[1][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,1,not sm_notes[1]), Function(sm_play_sketch)
            else:
                textbutton "Step 2 - Weigh %d %s salt and add it to the beaker on the stirrer." % (sm_experiment_list[1][1],sm_experiment_list[1][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,1,not sm_notes[1]), Function(sm_play_sketch)
            if sm_notes[2]:
                textbutton "{s}Step 3 - Measure %d %s liquid and pour it into the beaker on the stirrer.{/s}" % (sm_experiment_list[2][1],sm_experiment_list[2][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,2,not sm_notes[2]), Function(sm_play_sketch)
            else:
                textbutton "Step 3 - Measure %d %s liquid and pour it into the beaker on the stirrer." % (sm_experiment_list[2][1],sm_experiment_list[2][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,2,not sm_notes[2]), Function(sm_play_sketch)
            if sm_notes[3]:
                textbutton "{s}Step 4 - Stir at %s speed for 15 seconds and wait for the color to change.{/s}" % sm_experiment_list[3][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,3,not sm_notes[3]), Function(sm_play_sketch)
            else:
                textbutton "Step 4 - Stir at %s speed for 15 seconds and wait for the color to change." % sm_experiment_list[3][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,3,not sm_notes[3]), Function(sm_play_sketch)

            if sm_notes[4]:
                textbutton "{s}Step 5 - After the color has changed, weigh %d %s salt and pour it into the beaker on the stirrer.{/s}"  % (sm_experiment_list[4][1],sm_experiment_list[4][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,4,not sm_notes[4]), Function(sm_play_sketch)
            else:
                textbutton "Step 5 - After the color has changed, weigh %d %s salt and pour it into the beaker on the stirrer."  % (sm_experiment_list[4][1],sm_experiment_list[4][0]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,4,not sm_notes[4]), Function(sm_play_sketch)

            if sm_notes[5]:
                textbutton "{s}Step 6 - Stir at %s speed for 10 seconds and wait for the color to change.{/s}" % sm_experiment_list[6][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,5,not sm_notes[5]), Function(sm_play_sketch)
            else:
                textbutton "Step 6 - Stir at %s speed for 10 seconds and wait for the color to change." % sm_experiment_list[6][0] text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,5,not sm_notes[5]), Function(sm_play_sketch)

            if sm_notes[6]:
                textbutton "{s}Step 7 - After the color has changed, pour the solution into the round flask and turn on the burner.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,6,not sm_notes[6]), Function(sm_play_sketch)
            else:
                textbutton "Step 7 - After the color has changed, pour the solution into the round flask and turn on the burner." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,6,not sm_notes[6]), Function(sm_play_sketch)

            if sm_notes[7]:
                textbutton "{s}Step 8 - Wait 10 seconds. If the solution is clear, weigh %d blue salt and add it to the round flask. If the solution is blue, weigh %d red salt and add it to the round flask.{/s}" % (sm_experiment_list[7][1],sm_experiment_list[8][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,7,not sm_notes[7]), Function(sm_play_sketch)
            else:
                textbutton "Step 8 - Wait 10 seconds. If the solution is clear, weigh %d blue salt and add it to the round flask. If the solution is blue, weigh %d red salt and add it to the round flask." % (sm_experiment_list[7][1],sm_experiment_list[8][1]) text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,7,not sm_notes[7]), Function(sm_play_sketch)

            if sm_notes[8]:
                textbutton "{s}Step 9 - Let the solution boil for 15 seconds. After the color turns red, turn off the burner.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,8,not sm_notes[8]), Function(sm_play_sketch)
            else:
                textbutton "Step 9 - Let the solution boil for 15 seconds. After the color turns red, turn off the burner." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,8,not sm_notes[8]), Function(sm_play_sketch)
            if sm_notes[9]:
                textbutton "{s}Step 10 - Let the solution cool down for 15 seconds. If the color turns green, your reaction is complete.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,9,not sm_notes[9]), Function(sm_play_sketch)
            else:
                textbutton "Step 10 - Let the solution cool down for 15 seconds. If the color turns green, your reaction is complete." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,9,not sm_notes[9]), Function(sm_play_sketch)
            if sm_notes[10]:
                textbutton "{s}Step 11 - Turn in your mixture, and let's assess the purity together.{/s}" text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,10,not sm_notes[10]), Function(sm_play_sketch)
            else:
                textbutton "Step 11 - Turn in your mixture, and let's assess the purity together." text_style "sm_notes_style":
                    if sm_perk_pencil:
                        action SetDict(sm_notes,10,not sm_notes[10]), Function(sm_play_sketch)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

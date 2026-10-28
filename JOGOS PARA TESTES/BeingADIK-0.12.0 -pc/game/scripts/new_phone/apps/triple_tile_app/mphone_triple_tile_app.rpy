init:
    if persistent.triple_tile_highscores == None:
        $ persistent.triple_tile_highscores = [[0,0],[0,0],[0,0]]
    if persistent.triple_tile_highscores_easy == None:
        $ persistent.triple_tile_highscores_easy = [[0,0],[0,0],[0,0]]
    if persistent.triple_tile_challenge == None:
        $ persistent.triple_tile_challenge = False

screen mphone_triple_tile_screen:
    tag mphone_triple_tile_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform

        if not mphone_triple_tile_is_playing:
            add "mphone_triple_tile_bg1"
            vbox:
                xalign 0.5
                yalign 0.26
                textbutton "New Game" text_style "mphone_triple_tile_text_button_style" action Function(mphone_triple_tile_new_game_func) xalign 0.5
            vbox:
                xalign 0.5
                yalign 0.72
                spacing 5 * persistent.scale_factor
                if triple_tile_show_numbers:
                    textbutton "Show Tile Numbers: {color=fe9416}Yes{/color}" text_style "mphone_triple_tile_text_button2_style" action SetVariable("triple_tile_show_numbers", False) xalign 0.5
                else:
                    textbutton "Show Tile Numbers: {color=fe9416}No{/color}" text_style "mphone_triple_tile_text_button2_style" action SetVariable("triple_tile_show_numbers", True) xalign 0.5
                if triple_tile_easy_mode:
                    textbutton "Difficulty: {color=fe9416}Easy{/color}" text_style "mphone_triple_tile_text_button2_style" action SetVariable("triple_tile_easy_mode", False) xalign 0.5
                else:
                    textbutton "Difficulty: {color=fe9416}Normal{/color}" text_style "mphone_triple_tile_text_button2_style" action SetVariable("triple_tile_easy_mode", True) xalign 0.5
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20 * persistent.scale_factor
                text "High Scores" style "mphone_triple_tile_text_high_style" xalign 0.5
                if triple_tile_easy_mode:
                    for i in persistent.triple_tile_highscores_easy:
                        if i[0]!=0:
                            text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Easy{/color}{/size}" % ((8 * persistent.scale_factor),i[0],i[1]) style "mphone_triple_tile_text_style" xalign 0.5
                        else:
                            text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} -{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                else:
                    for i in persistent.triple_tile_highscores:
                        if i[0]!=0:
                            text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Normal{/color}{/size}" % ((8 * persistent.scale_factor),i[0],i[1]) style "mphone_triple_tile_text_style" xalign 0.5
                        else:
                            text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} -{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
            vbox:
                xalign 0.5
                yalign 0.85
                spacing 30 * persistent.scale_factor
                xmaximum 400 * persistent.scale_factor
                if triple_tile_money_available:
                    text "Match three tiles in a row, column, diagonal, or within a cell. You can stack tiles on top of each other in the grid if their slots aren't occupied.\nReach turn [triple_turn_to_beat] to earn {color=00ff00}${/color}." style "mphone_triple_tile_text2_style" xalign 0.5 text_align 0.5
                else:
                    text "Match three tiles in a row, column, diagonal, or within a cell. You can stack tiles on top of each other in the grid if their slots aren't occupied." style "mphone_triple_tile_text2_style" xalign 0.5 text_align 0.5
        else:
            if triple_tile_game_over:
                if triple_tile_turn >= 100 and not triple_tile_easy_mode and not persistent.triple_tile_challenge:
                    add "mphone_triple_tile_bg2"
                    vbox:
                        xalign 0.5
                        yalign 0.75
                        if triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
                            textbutton "Accept gift" text_style "mphone_triple_tile_text_button_style" action (SetVariable("persistent.triple_tile_challenge",True),SetVariable("triple_tile_money_available", False), SetVariable("mphone_triple_tile_is_playing", False))
                        else:
                            textbutton "Accept gift" text_style "mphone_triple_tile_text_button_style" action (SetVariable("persistent.triple_tile_challenge",True),SetVariable("mphone_triple_tile_is_playing", False))
                else:
                    add "mphone_triple_tile_bg1"
                    if triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
                        text "{size=+%d}{color=00ff00}${/color}{color=ffff00} won!{/color}{/size}\n{color=ffff00}{size=-%d}Win more during the next free roam event.{/size}{/color}" % ((20 * persistent.scale_factor),(10 * persistent.scale_factor)) style "mphone_triple_tile_text_style" xalign 0.50 yalign 0.85 text_align 0.5
                    vbox:
                        text "{size=+%d}{color=fe9416}GAME OVER!{/color}{/size}" % (10 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.50 yalign 0.22
                        xalign 0.5
                        yalign 0.26
                        text "{size=-%d}{color=fe9416}Score:{/color} {color=ffff00}[triple_tile_score]{/color}{/size}" % (10 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                        text "{size=-%d}{color=fe9416}Turn:{/color} [triple_tile_turn]{/size}" % (10 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                        if triple_tile_easy_mode:
                            text "{size=-%d}{color=fe9416}Mode:{/color} Easy{/size}" % (10 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                        else:
                            text "{size=-%d}{color=fe9416}Mode:{/color} Normal{/size}" % (10 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 20 * persistent.scale_factor
                        text "High scores" style "mphone_triple_tile_text_high_style" xalign 0.5
                        if triple_tile_easy_mode:
                            for i in range(0,len(persistent.triple_tile_highscores_easy)):
                                if triple_tile_new_high_score > 0:
                                    if persistent.triple_tile_highscores_easy[i][0]!=0 and triple_tile_new_high_score-1 == i:
                                        text "{size=-%d}{color=ffff00}Score %d Turn: %d Easy{/color}{/size}" % ((8 * persistent.scale_factor),persistent.triple_tile_highscores_easy[i][0],persistent.triple_tile_highscores_easy[i][1]) style "mphone_triple_tile_text_style" xalign 0.5
                                    elif persistent.triple_tile_highscores_easy[i][0]!=0:
                                        text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Easy{/color}{/size}" % ((8 * persistent.scale_factor),persistent.triple_tile_highscores_easy[i][0],persistent.triple_tile_highscores_easy[i][1]) style "mphone_triple_tile_text_style" xalign 0.5
                                    else:
                                        text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} -{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                                else:
                                    if persistent.triple_tile_highscores_easy[i][0]!=0:
                                        text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Easy{/color}{/size}" % ((8 * persistent.scale_factor),persistent.triple_tile_highscores_easy[i][0],persistent.triple_tile_highscores_easy[i][1]) style "mphone_triple_tile_text_style" xalign 0.5
                                    else:
                                        text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} -{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                        else:
                            for i in range(0,len(persistent.triple_tile_highscores)):
                                if triple_tile_new_high_score > 0:
                                    if persistent.triple_tile_highscores[i][0]!=0 and triple_tile_new_high_score-1 == i:
                                        text "{size=-%d}{color=ffff00}Score %d Turn: %d Normal{/color}{/size}" % ((8 * persistent.scale_factor),persistent.triple_tile_highscores[i][0],persistent.triple_tile_highscores[i][1]) style "mphone_triple_tile_text_style" xalign 0.5
                                    elif persistent.triple_tile_highscores[i][0]!=0:
                                        text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Normal{/color}{/size}" % ((8 * persistent.scale_factor),persistent.triple_tile_highscores[i][0],persistent.triple_tile_highscores[i][1]) style "mphone_triple_tile_text_style" xalign 0.5
                                    else:
                                        text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} -{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                                else:
                                    if persistent.triple_tile_highscores[i][0]!=0:
                                        text "{size=-%d}{color=fe9416}Score:{/color} %d {color=fe9416}Turn:{/color} %d {color=fe9416}Normal{/color}{/size}" % ((8 * persistent.scale_factor),persistent.triple_tile_highscores[i][0],persistent.triple_tile_highscores[i][1]) style "mphone_triple_tile_text_style" xalign 0.5
                                    else:
                                        text "{size=-%d}{color=fe9416}Score:{/color} - {color=fe9416}Turn:{/color} -{/size}" % (8 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.5
                    vbox:
                        xalign 0.5
                        yalign 0.75
                        if triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
                            textbutton "Try again" text_style "mphone_triple_tile_text_button_style" action (SetVariable("triple_tile_money_available", False),Function(mphone_triple_tile_new_game_func))
                        else:
                            textbutton "Try again" text_style "mphone_triple_tile_text_button_style" action Function(mphone_triple_tile_new_game_func)

            else:
                add "mphone_triple_tile_bg"
                vbox:
                    xalign 0.52
                    yalign 0.15
                    xminimum 470 * persistent.scale_factor
                    xmaximum 470 * persistent.scale_factor
                    text "{color=fe9416}Score:{/color} {color=ffff00}[triple_tile_score]{/color}" style "mphone_triple_tile_text_style"
                    text "{color=fe9416}Turn:{/color} [triple_tile_turn]" style "mphone_triple_tile_text_style"
                if triple_tile_money_available:
                    if triple_tile_turn >= triple_turn_to_beat:
                        text "{size=+%d}{color=00ff00}${/color}{/size}" % (50 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.58 yalign 0.14
                    else:
                        text "{size=+%d}{color=ffffff}${/color}{/size}" % (50 * persistent.scale_factor) style "mphone_triple_tile_text_style" xalign 0.58 yalign 0.14


                vbox:
                    xalign 0.5
                    yalign 0.40
                    yoffset 3 * persistent.scale_factor
                    spacing 5 * persistent.scale_factor
                    for i in range(0,3):
                        hbox:
                            spacing 6 * persistent.scale_factor
                            for j in range(0,3):
                                hbox:
                                    if triple_tile_hovered_tile[0] == i and triple_tile_hovered_tile[1] == j and triple_tile_add_is_possible(i,j,triple_tile_chosen_tile):
                                        imagebutton:
                                            idle "triple_tile_hovered"
                                            hover "triple_tile_hovered"
                                            action NullAction()
                                    else:
                                        imagebutton:
                                            idle "triple_tile_no_hovered"
                                            hover "triple_tile_no_hovered"
                                            action NullAction()
                vbox:
                    xalign 0.5
                    yalign 0.40
                    yoffset 3 * persistent.scale_factor
                    spacing 9 * persistent.scale_factor
                    for i in range(0,3):
                        hbox:
                            spacing 6 * persistent.scale_factor
                            for j in range(0,3):
                                hbox:
                                    for k in range(0,3):
                                        if triple_tile_grid[i][j] == [0,0,0]:
                                            imagebutton:
                                                idle "triple_tile_empty"
                                                hover "triple_tile_empty"
                                                if triple_tile_chosen_tile == -1:
                                                    action NullAction()
                                                else:
                                                    hovered SetVariable("triple_tile_hovered_tile",[i,j])
                                                    unhovered SetVariable("triple_tile_hovered_tile",[-1,-1])
                                                    action Function(triple_tile_add_tile,i,j)
                                        else:
                                            imagebutton:
                                                if triple_tile_show_numbers:
                                                    idle "triple_tile_%ib" % triple_tile_grid[i][j][k]
                                                    hover "triple_tile_%ib" % triple_tile_grid[i][j][k]
                                                else:
                                                    idle "triple_tile_%i" % triple_tile_grid[i][j][k]
                                                    hover "triple_tile_%i" % triple_tile_grid[i][j][k]
                                                if triple_tile_chosen_tile == -1:
                                                    action NullAction()
                                                else:
                                                    hovered SetVariable("triple_tile_hovered_tile",[i,j])
                                                    unhovered SetVariable("triple_tile_hovered_tile",[-1,-1])
                                                    action Function(triple_tile_add_tile,i,j)


                hbox:
                    xalign 0.5
                    yalign 0.8
                    spacing 10 * persistent.scale_factor
                    yoffset 2 * persistent.scale_factor
                    for i in range(0,3):
                        hbox:
                            xoffset (4 - 4*i) * persistent.scale_factor
                            if i == triple_tile_chosen_tile:
                                imagebutton:
                                    idle "triple_tile_selection"
                                    hover "triple_tile_selection"
                                    action NullAction()
                            else:
                                imagebutton:
                                    idle "triple_tile_no_selection"
                                    hover "triple_tile_no_selection"
                                    action NullAction()

                hbox at tt_appear_transform:
                    xalign 0.5
                    yalign 0.8
                    spacing 10 * persistent.scale_factor
                    for i in range(0,3):
                        hbox:
                            if triple_tile_sets[i] == [0,0,0]:
                                for j in range(0,3):
                                    imagebutton:
                                        idle "triple_tile_empty"
                                        hover "triple_tile_empty"
                                        action NullAction()
                            else:
                                for j in range(0,3):
                                    imagebutton:
                                        if triple_tile_show_numbers:
                                            idle "triple_tile_%ib" % triple_tile_sets[i][j]
                                            hover "triple_tile_%ib" % triple_tile_sets[i][j]
                                        else:
                                            idle "triple_tile_%i" % triple_tile_sets[i][j]
                                            hover "triple_tile_%i" % triple_tile_sets[i][j]
                                        action SetVariable("triple_tile_chosen_tile",i)
    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"

    if not mphone_triple_tile_is_playing:
        key "mouseup_2" action Hide("mphone_triple_tile_screen")
    elif triple_tile_game_over:
        if triple_tile_turn >= 100 and not persistent.triple_tile_challenge:
            if triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
                key "mouseup_2" action (SetVariable("persistent.triple_tile_challenge",True),SetVariable("triple_tile_money_available", False),SetVariable("mphone_triple_tile_is_playing", False))
            else:
                key "mouseup_2" action (SetVariable("persistent.triple_tile_challenge",True),SetVariable("mphone_triple_tile_is_playing", False))
        elif triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
            key "mouseup_2" action (SetVariable("triple_tile_money_available", False),SetVariable("mphone_triple_tile_is_playing", False))
        else:
            key "mouseup_2" action SetVariable("mphone_triple_tile_is_playing", False)
    else:
        key "mouseup_2" action Function(triple_tile_force_game_over)
    fixed:
        at mphone_app_transform
        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            if not mphone_triple_tile_is_playing:
                action Hide("mphone_triple_tile_screen")
            elif triple_tile_game_over:
                if triple_tile_turn >= 100 and not persistent.triple_tile_challenge:
                    if triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
                        action (SetVariable("persistent.triple_tile_challenge",True),SetVariable("triple_tile_money_available", False),SetVariable("mphone_triple_tile_is_playing", False))
                    else:
                        action (SetVariable("persistent.triple_tile_challenge",True),SetVariable("mphone_triple_tile_is_playing", False))
                elif triple_tile_money_available and triple_tile_turn >= triple_turn_to_beat:
                    action (SetVariable("triple_tile_money_available", False),SetVariable("mphone_triple_tile_is_playing", False))
                else:
                    action SetVariable("mphone_triple_tile_is_playing", False)
            else:
                action Function(triple_tile_force_game_over)
            xalign 0.5
            yalign mphone_off_yalign
        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

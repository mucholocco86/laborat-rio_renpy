default mphone_playing_shuffle = 0
default shuffle_wins = 0
default shuffle_losses = 0
screen scr_shuffle_game:
    timer 0.1 repeat True action If(e_time > 0, true=SetVariable('e_time', e_time - 0.05), false=[Hide('scr_shuffle_game'), SetVariable("shuffle_losses", shuffle_losses+1),SetVariable("mphone_playing_shuffle",3)])
    bar value e_time range timer_range xalign 0.5 yalign 0.225 xmaximum 426 * persistent.scale_factor
    vbox:
        xalign 0.5
        yalign 0.8
        imagebutton:
            if eco_wrongs <= 1 + gameBoost:
                idle "shuffle_solve"
                hover "shuffle_solve_hover"
                action Function(mphone_shuffle_win)
            else:
                idle "shuffle_solve_disabled"
                hover "shuffle_solve_disabled"
                action NullAction()

        imagebutton:
            idle "shuffle_quit"
            hover "shuffle_quit_hover"
            action (Hide("scr_shuffle_game"),SetVariable("shuffle_losses", shuffle_losses+1),SetVariable("mphone_playing_shuffle",3))

screen mphone_shuffle_screen:
    tag mphone_shuffle_screen
    modal True
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    fixed:
        at mphone_app_transform
        add "mphone_shuffle_bg"

        if mphone_playing_shuffle == 0:
            add "mphone_shuffle_overlay1"
            imagebutton:
                idle "shuffle_brick_%i" % renpy.random.randint(0, 9)
                xalign 0.5
                yalign 0.443
                yoffset 1 * persistent.scale_factor
                action NullAction()
            hbox:
                xalign 0.5
                yalign 0.2
                xmaximum 426 * persistent.scale_factor
                xminimum 426 * persistent.scale_factor
                $ tmpInt = str(round((float)(shuffle_wins)/max(1.0,shuffle_losses), 2))
                text "Wins - %i Losses - %i\nW/L ratio: [tmpInt]" % (shuffle_wins, shuffle_losses) xalign 0.5 text_align 0.5 style "mphone_shuffle_style"
            vbox:
                xalign 0.5
                yalign 0.82
                imagebutton:
                    idle "shuffle_new_game"
                    hover "shuffle_new_game_hover"
                    action (Hide("scr_shuffle_game"),SetVariable("mphone_playing_shuffle", 1), Function(mphone_shuffle_new_game))
                imagebutton:
                    idle "shuffle_quit"
                    hover "shuffle_quit_hover"
                    action (SetVariable("mphone_playing_shuffle",0), Hide("mphone_shuffle_screen"))
        else:

            if mphone_playing_shuffle == 1:
                add "mphone_shuffle_overlay1b"
                imagebutton:
                    idle "shuffle_brick_%i" % game_brick_set
                    hover "shuffle_brick_%i" % game_brick_set
                    xalign 0.5
                    yalign 0.443
                    yoffset 1 * persistent.scale_factor
                    action (SetVariable("mphone_playing_shuffle",2),Show("scr_shuffle_game"))
            elif mphone_playing_shuffle == 2:
                add "mphone_shuffle_overlay1"
                add "mphone_shuffle_overlay2"
                $ mphone_shuffle_update_board()

                vbox:
                    xalign 0.5
                    yalign 0.443
                    yoffset 1 * persistent.scale_factor
                    spacing 0
                    for i in range(0,3):
                        hbox:
                            spacing 0
                            for j in range(i*3,i*3+3):
                                imagebutton:
                                    idle eco_bricks[eco_shf[j]]
                                    if eco_moveable[j]:
                                        if eco_shf[j] != 8:
                                            hover eco_bricks[eco_shf[j]] + "_hover"
                                        else:
                                            hover eco_bricks[eco_shf[j]]
                                        action Function(mphone_shuffle_swap_vars,j)
                                    else:
                                        hover eco_bricks[eco_shf[j]]
                                        action NullAction()

            elif mphone_playing_shuffle == 3:
                if game_money_available:
                    add "mphone_shuffle_overlay3"
                else:
                    add "mphone_shuffle_overlay3b"
                imagebutton:
                    idle "shuffle_brick_%i" % game_brick_set
                    hover "shuffle_brick_%i" % game_brick_set
                    xalign 0.5
                    yalign 0.443
                    yoffset 1 * persistent.scale_factor
                    action NullAction()
                vbox:
                    xalign 0.5
                    yalign 0.85
                    imagebutton:
                        idle "shuffle_restart"
                        hover "shuffle_restart_hover"
                        action (Hide("scr_shuffle_game"),SetVariable("mphone_playing_shuffle", 1), Function(mphone_shuffle_new_game))
                    imagebutton:
                        idle "shuffle_quit"
                        hover "shuffle_quit_hover"
                        action SetVariable("mphone_playing_shuffle",0)
            else:
                if game_money_available:
                    add "mphone_shuffle_overlay4"
                else:
                    add "mphone_shuffle_overlay4b"
                imagebutton:
                    idle "shuffle_brick_%i" % game_brick_set
                    hover "shuffle_brick_%i" % game_brick_set
                    xalign 0.5
                    yalign 0.443
                    yoffset 1 * persistent.scale_factor
                    action NullAction()
                vbox:
                    xalign 0.5
                    yalign 0.85
                    imagebutton:
                        idle "shuffle_restart"
                        hover "shuffle_restart_hover"
                        action (SetVariable("game_money_available",False),Hide("scr_shuffle_game"),SetVariable("mphone_playing_shuffle", 1), Function(mphone_shuffle_new_game))
                    imagebutton:
                        idle "shuffle_quit"
                        hover "shuffle_quit_hover"
                        action (SetVariable("game_money_available",False),SetVariable("mphone_playing_shuffle",0))

    if persistent.golden_phone and persistent.golden_phone_skin_enabled:
        add "mphone_shell_gold"
    else:
        add "mphone_shell"

    if mphone_playing_shuffle == 0:
        key "mouseup_2" action Hide("mphone_shuffle_screen")
    elif mphone_playing_shuffle > 3:
        key "mouseup_2" action (Hide("mphone_shuffle_screen"), SetVariable("game_money_available",False))
    elif mphone_playing_shuffle > 2:
        key "mouseup_2" action Hide("mphone_shuffle_screen")
    else:
        key "mouseup_2" action (Hide("scr_shuffle_game"),SetVariable("shuffle_losses", shuffle_losses+1),SetVariable("mphone_playing_shuffle",3))

    fixed:
        at mphone_app_transform
        imagebutton at mphone_off_transform:
            idle "mphone_off_circle_idle"
            hover "mphone_off_circle_hover"
            if mphone_playing_shuffle == 0:
                action Hide("mphone_shuffle_screen")
            elif mphone_playing_shuffle > 3:
                action (Hide("mphone_shuffle_screen"), SetVariable("game_money_available",False))
            elif mphone_playing_shuffle > 2:
                action Hide("mphone_shuffle_screen")
            else:
                action (Hide("scr_shuffle_game"),SetVariable("shuffle_losses", shuffle_losses+1),SetVariable("mphone_playing_shuffle",3))
            xalign 0.5
            yalign mphone_off_yalign
        add "mphone_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

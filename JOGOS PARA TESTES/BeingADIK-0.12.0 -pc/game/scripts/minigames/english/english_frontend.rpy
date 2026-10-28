init python:
    import time
screen english_screen:
    tag english_screen
    modal True

    if eng_total3 > 0:
        add "english_board_36"
    else:
        add "english_board_46"
    imagebutton:
        idle "english_main_text"
        hover "english_main_text"
        action NullAction()
        xpos 990 * persistent.scale_factor
        ypos 120 * persistent.scale_factor
    if eng_cheated:
        imagebutton:
            idle "english_main_text_cheated"
            hover "english_main_text_cheated"
            action NullAction()
            xpos 990 * persistent.scale_factor
            ypos 120 * persistent.scale_factor

    default end_time = time.time() + e_time
    default current_time = time.time()
    timer 0.05 repeat True action If(current_time < end_time, true=SetScreenVariable('current_time', time.time()), false=Function(eng_test_done))
    bar value (end_time-current_time)*100 range e_time*100 xalign 0.76 yalign 0.17 xmaximum 320 * persistent.scale_factor at alpha_dissolve:
        style "english_bar_style"

    key "A" action Function(eng_input_func, "a")
    key "B" action Function(eng_input_func, "b")
    key "C" action Function(eng_input_func, "c")
    key "D" action Function(eng_input_func, "d")
    key "E" action Function(eng_input_func, "e")
    key "F" action Function(eng_input_func, "f")
    key "G" action Function(eng_input_func, "g")
    key "H" action Function(eng_input_func, "h")
    key "I" action Function(eng_input_func, "i")
    key "J" action Function(eng_input_func, "j")
    key "K" action Function(eng_input_func, "k")
    key "L" action Function(eng_input_func, "l")
    key "M" action Function(eng_input_func, "m")
    key "N" action Function(eng_input_func, "n")
    key "O" action Function(eng_input_func, "o")
    key "P" action Function(eng_input_func, "p")
    key "Q" action Function(eng_input_func, "q")
    key "R" action Function(eng_input_func, "r")
    key "S" action Function(eng_input_func, "s")
    key "T" action Function(eng_input_func, "t")
    key "U" action Function(eng_input_func, "u")
    key "V" action Function(eng_input_func, "v")
    key "W" action Function(eng_input_func, "w")
    key "X" action Function(eng_input_func, "x")
    key "Y" action Function(eng_input_func, "y")
    key "Z" action Function(eng_input_func, "z")
    key "a" action Function(eng_input_func, "a")
    key "b" action Function(eng_input_func, "b")
    key "c" action Function(eng_input_func, "c")
    key "d" action Function(eng_input_func, "d")
    key "e" action Function(eng_input_func, "e")
    key "f" action Function(eng_input_func, "f")
    key "g" action Function(eng_input_func, "g")
    key "h" action Function(eng_input_func, "h")
    key "i" action Function(eng_input_func, "i")
    key "j" action Function(eng_input_func, "j")
    key "k" action Function(eng_input_func, "k")
    key "l" action Function(eng_input_func, "l")
    key "m" action Function(eng_input_func, "m")
    key "n" action Function(eng_input_func, "n")
    key "o" action Function(eng_input_func, "o")
    key "p" action Function(eng_input_func, "p")
    key "q" action Function(eng_input_func, "q")
    key "r" action Function(eng_input_func, "r")
    key "s" action Function(eng_input_func, "s")
    key "t" action Function(eng_input_func, "t")
    key "u" action Function(eng_input_func, "u")
    key "v" action Function(eng_input_func, "v")
    key "w" action Function(eng_input_func, "w")
    key "x" action Function(eng_input_func, "x")
    key "y" action Function(eng_input_func, "y")
    key "z" action Function(eng_input_func, "z")
    key "K_RETURN" action Function(eng_enter_word)
    key "K_SPACE" action Function(eng_shuffle_func)
    key "K_BACKSPACE" action Function(eng_del_func)

    text "%s" % eng_chars_word xalign 0.745 yalign 0.525 xminimum 350 * persistent.scale_factor style "eng_style_word2"

    hbox:
        xalign 0.82 yalign 0.365 xminimum 350 * persistent.scale_factor
        text "%s" % eng_word style "eng_style_word"

    if eng_lists_used[0]:
        vbox:
            xalign 0.52
            yalign eng_yalign[4]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            text "%d %%" % eng_perc3 style "eng_style_titles"
        vbox:
            xalign 0.265
            yalign eng_yalign[0]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            vpgrid:
                cols 5
                spacing 5 * persistent.scale_factor
                for item in eng_completed_list3:
                    text "%s  " % item style "eng_style_words"
                for noitem in range(0,eng_total3 - len(eng_completed_list3)):
                    text "    " style "eng_style_words"
    if eng_lists_used[1]:
        vbox:
            xalign 0.52
            yalign eng_yalign[5]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            text "%d %%" % eng_perc4 style "eng_style_titles"
        vbox:
            xalign 0.265
            yalign eng_yalign[1]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            vpgrid:
                cols 4
                spacing 5 * persistent.scale_factor
                for item in eng_completed_list4:
                    text "%s  " % item style "eng_style_words" xminimum 100 * persistent.scale_factor
                for noitem in range(0,eng_total4 - len(eng_completed_list4)):
                    text "     " style "eng_style_words" xminimum 100 * persistent.scale_factor
    if eng_lists_used[2]:
        vbox:
            xalign 0.52
            yalign eng_yalign[6]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            text "%d %%" % eng_perc5 style "eng_style_titles"
        vbox:
            xalign 0.265
            yalign eng_yalign[2]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            vpgrid:
                if currentEpisode == 12:
                    cols 4
                else:
                    cols 3
                spacing 5 * persistent.scale_factor
                for item in eng_completed_list5:
                    text "%s  " % item style "eng_style_words"
                for noitem in range(0,eng_total5 - len(eng_completed_list5)):
                    text "      " style "eng_style_words"
    if eng_lists_used[3]:
        vbox:
            xalign 0.52
            yalign eng_yalign[7]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            text "%d %%" % eng_perc6 style "eng_style_titles"
        vbox:
            xalign 0.265
            yalign eng_yalign[3]
            spacing 40 * persistent.scale_factor
            xminimum 600 * persistent.scale_factor
            xmaximum 600 * persistent.scale_factor
            vpgrid:
                cols 3
                spacing 5 * persistent.scale_factor
                for item in eng_completed_list6:
                    text "%s  " % item style "eng_style_words"
                for noitem in range(0,eng_total6 - len(eng_completed_list6)):
                    text "       " style "eng_style_words"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

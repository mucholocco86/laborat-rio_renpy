################################################################################
## Warning Screen — BlueFox.au v1.2.0
################################################################################
##
## Content warning shown once at the start of the game. Replaces the old
## warning.png so we get real typography, a proper fade, and interaction
## instead of a baked-in image.
##
################################################################################

################################################################################
## Transforms
################################################################################

transform warning_screen_fade_in:
    alpha 0.0
    linear 1.2 alpha 1.0

################################################################################
## Screen
################################################################################

screen warning_screen():
    modal True
    zorder 300

    key "skip"        action NullAction()
    key "toggle_skip" action NullAction()
    key "fast_skip"   action NullAction()
    key "game_menu"   action NullAction()
    key "rollback"    action NullAction()
    key "K_s"         action NullAction()
    key "K_F5"        action NullAction()
    key "K_F9"        action NullAction()
    key "K_TAB"       action NullAction()
    key "K_LCTRL"     action NullAction()
    key "K_RCTRL"     action NullAction()
    key "K_ESCAPE"    action NullAction()

    add Solid("#000000")

    fixed:
        at warning_screen_fade_in

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 24

            text _("WARNING!"):
                style "warning_title_text"
                xalign 0.5

            add Solid("#d10089") xalign 0.5 xysize (280, 2)

            null height 12

            text _("Please be advised that this game contains sexually explicit material\nand should not be viewed by minors."):
                style "warning_body_text"
                text_align 0.5
                xalign 0.5

            null height 8

            text _("This is a work of fiction. Names, characters, places and incidents\nare products of the author's imagination or are used fictitiously.\nAny resemblance to actual events or persons, living or dead, is entirely coincidental."):
                style "warning_body_text"
                text_align 0.5
                xalign 0.5

            null height 8

            text _("All characters in this story are over 18 years of age."):
                style "warning_body_text"
                text_align 0.5
                xalign 0.5

            null height 40

            textbutton _("CONTINUE >"):
                xalign 0.5
                action Return()
                style "warning_button"

################################################################################
## Styles
################################################################################

style warning_title_text is default:
    font gui.name_text_font
    size 84
    color "#ff2a2a"
    kerning 8
    outlines []

style warning_body_text is default:
    font gui.text_font
    size 26
    color "#f0e8f5"
    kerning 1
    line_spacing 10
    outlines []

style warning_button is default:
    background None
    hover_background Solid("#d1008922")
    padding (20, 8)

style warning_button_text is default:
    font gui.interface_text_font
    size 22
    color "#f0e8f5"
    hover_color "#ffffff"
    kerning 6
    outlines []

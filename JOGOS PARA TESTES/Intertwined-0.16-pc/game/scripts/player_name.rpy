################################################################################
## Player Name — BlueFox.au v1.2.0
################################################################################
##
## Custom player-name entry screen shown at the start of a new game. Replaces
## the plain renpy.input prompt with a styled input that integrates with the
## controller on-screen keyboard.
##
################################################################################

################################################################################
## Transforms
################################################################################

transform player_name_screen_fade_in:
    alpha 0.0
    linear 0.8 alpha 1.0

################################################################################
## Screen
################################################################################

screen player_name_screen():
    modal True
    zorder 300

    ## Pre-fill with the name from a previous playthrough.
    default entered_name = persistent.player_name or "Nico"

    add Solid("#000000")

    fixed:
        at player_name_screen_fade_in

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 22

            text _("WHO ARE YOU?"):
                style "player_name_title_text"
                xalign 0.5

            ## Thin magenta divider.
            add Solid("#d10089") xalign 0.5 xysize (280, 2)

            null height 6

            text _("Enter the name you'd like to be known by."):
                style "player_name_prompt_text"
                xalign 0.5

            null height 16

            $ _name_iv = ScreenVariableInputValue("entered_name", default=not is_controller_active())
            button:
                xalign 0.5
                xysize (620, 68)
                padding (24, 12)
                background None
                hover_background Solid("#4ceefc11")
                key_events True
                action [
                    Function(osk_activate_for, _name_iv, "entered_name"),
                    Function(osk_force_show),
                ]

                ## Cyan underline.
                add Solid("#4ceefc") yalign 1.0 xysize (572, 2)

                input:
                    id "name_input"
                    value _name_iv
                    default False
                    length 20
                    allow " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'"
                    xalign 0.5
                    yalign 0.0
                    style "player_name_input_text"

            null height 8

            textbutton _("CONTINUE >"):
                xalign 0.5
                sensitive entered_name.strip() != ""
                action Return(entered_name.strip())
                style "player_name_button"

    ## Pressing Enter submits when the field is non-blank.
    if entered_name.strip() != "":
        key "K_RETURN"    action Return(entered_name.strip())
        key "K_KP_ENTER"  action Return(entered_name.strip())

################################################################################
## Styles
################################################################################

style player_name_title_text is default:
    font gui.name_text_font
    size 72
    color "#ffffff"
    kerning 8
    outlines []

style player_name_prompt_text is default:
    font gui.text_font
    size 24
    color "#f0e8f5"
    kerning 1
    line_spacing 8
    outlines []

style player_name_hint_text is default:
    font gui.text_font
    size 16
    color "#8b7a99"
    kerning 2
    outlines []

style player_name_input_text is default:
    font gui.name_text_font
    size 44
    color "#4ceefc"
    kerning 4
    caret Solid("#4ceefc", xysize=(2, 44))
    outlines []

style player_name_button is default:
    background None
    hover_background Solid("#d1008922")
    insensitive_background None
    padding (20, 8)

style player_name_button_text is default:
    font gui.interface_text_font
    size 22
    color "#f0e8f5"
    hover_color "#ffffff"
    insensitive_color "#5a4a66"
    kerning 6
    outlines []

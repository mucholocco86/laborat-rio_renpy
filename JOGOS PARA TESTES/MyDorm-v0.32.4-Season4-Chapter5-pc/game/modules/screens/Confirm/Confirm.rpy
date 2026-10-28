screen Confirm (message, yes_action, no_action, width=0.425, height=0.225):
    use ModalScreen (no_action, ModalBackgroundColor)
    $ messages = message.split ("\n")
    frame style "ConfirmFrame":
        xysize (width, height)
        use Borders ()
        vbox style "MyDormBoxCentered":
            for message in messages:
                text message style "TextMediumCentered"
            hbox style "MyDormBoxCentered":
                button:
                    action yes_action
                    style "MyDormButton"
                    text _("Sí") style "MyDormButton_text"
                button:
                    action no_action
                    style "MyDormButton"
                    text _("No") style "MyDormButton_text"
    key "game_menu" action no_action
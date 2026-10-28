screen GameSaveName (slotIndex, frameMargin):
    python:
        buttonAction = {
            "apply" : [ Hide ("GameSaveName"), FileSave (slotIndex, confirm = False) ],
            "cancel" : [ Hide ("GameSaveName") ]
        }
        boxHeight = 0.5
        boxWidth = 0.3
    use ModalScreen (buttonAction ["cancel"], ModalBackgroundColor)
    frame style "ConfirmFrame":
        xysize (boxHeight, boxWidth)
        use Borders ()
        hbox style "MyDormBoxCentered":
            vbox style "MyDormBox":
                image FileScreenshot (slotIndex) xalign 0.5
            vbox style "MyDormBoxCentered":
                text FileTime (slotIndex, format = "{#file_time}%B %d %Y, %H:%M") style "TextMediumCentered"
                text FileSaveName (slotIndex) style "TextMediumCentered"
                null height MenuGridSpacing
                text _("Introduce un nuevo nombre para tu partida:") style "TextMediumCentered"
                frame style "MyDormInputFrame":
                    input value VariableInputValue ("save_name")
                hbox style "MyDormBoxCentered":
                    button:
                        action buttonAction ["apply"]
                        style "MyDormButton"
                        text _("Aplicar") style "MyDormButton_text"
                    button:
                        action buttonAction ["cancel"]
                        style "MyDormButton"
                        text _("Cancelar") style "MyDormButton_text"
    key "K_RETURN" action buttonAction ["apply"]
    key "K_ESCAPE" action buttonAction ["cancel"]
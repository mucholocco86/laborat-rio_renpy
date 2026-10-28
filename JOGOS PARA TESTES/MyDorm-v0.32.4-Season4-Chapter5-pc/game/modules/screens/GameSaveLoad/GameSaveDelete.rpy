screen GameSaveDelete (slotIndex, frameMargin):
    python:
        buttonAction = {
            "yes" : [ Hide ("GameSaveDelete"), FileDelete (slotIndex, confirm = False) ],
            "cancel" : [ Hide ("GameSaveDelete") ]
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
                text _("¿Quieres eliminar este guardado?") style "TextMediumCentered"
                hbox style "MyDormBoxCentered":
                    button:
                        action buttonAction ["yes"]
                        style "MyDormButton"
                        text _("Sí") style "MyDormButton_text"
                    button:
                        action buttonAction ["cancel"]
                        style "MyDormButton"
                        text _("Cancelar") style "MyDormButton_text"
    key "K_RETURN" action buttonAction ["yes"]
    key "K_ESCAPE" action buttonAction ["cancel"]
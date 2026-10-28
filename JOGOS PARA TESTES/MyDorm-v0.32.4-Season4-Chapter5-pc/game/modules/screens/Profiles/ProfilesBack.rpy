screen ProfilesBack(buttonLabel = _("Atrás"), marginLeft = 0, marginTop = 0, marginRight = 0, marginBottom = 0):
    frame:
        style "ProfilesFrameBack"
        margin (marginLeft * 2, marginTop * 2, marginRight * 2, marginRight * 2)
        pos (1.0 - marginRight, marginTop)
        button:
            if buttonLabel == _("Atrás"):
                action [ SelectedIf (False), ShowMenu ("Profiles", None) ]
            else:
                action [ SelectedIf (False), Return () ]
            style "MyDormButton"
            text renpy.translate_string (buttonLabel) style "MyDormButton_text"
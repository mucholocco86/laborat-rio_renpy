screen ProfilesScrollingImageBack(characterProfile=None,marginLeft=0, marginTop=0, marginRight=0, marginBottom=0):
    frame:
        style "ProfilesFrameBack"
        margin (marginLeft * 2, marginTop * 2, marginRight * 2, marginRight * 2)
        pos (1.0 - marginRight, marginTop)
        has button:
            action [ SelectedIf (False), ShowMenu ("Profiles", characterProfile) ]
            style "MyDormButton"
        text _("Atrás") style "MyDormButton_text"

screen Profiles(selectedCharacter = None):
    tag profiles
    use ModalScreen ()
    use ScreenBackground (MenuScreenLeft, MenuScreenLeft, MenuScreenLeft, MenuScreenLeft)
    use ProfileKeyBinds ()
    modal True
    python:
        framePadding = MenuScreenLeft * 2   # What?
        gridSize = 5                        # How many girls per line
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenLeft)
        marginRight = getScreenDim (MenuScreenLeft)
        marginBottom = getScreenDim (MenuScreenLeft)
        buttonBackLabel = _("Cerca")
        if selectedCharacter is not None:
            buttonBackLabel = _("Atrás")
    if selectedCharacter is None:
        use ProfilesList (gridSize)
    else:
        use ProfileDetails (selectedCharacter)
    use ProfilesBack (buttonBackLabel, marginLeft, marginTop, marginRight, marginBottom)
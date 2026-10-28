screen MenuButton (givenLabel="", givenIcon="", givenAction=[], givenTrigger=True, showButtonText=False, isSquare=False, iconIsImage=False, isActive=False, noInvert=False):
    python:
        hasIcon = givenIcon != ""
        isInsensitive = not givenTrigger and len (givenAction) > 0
# is this a currently active sub tab for on of the pages with a tab?
        currentScreen = renpy.current_screen ().screen_name [0]
        if givenIcon == "":
            isCurrentTab = False
        else:
            isCurrentTab = currentScreen.find (givenIcon.replace (" ", "")) != -1
        for tabbedPage in ("Help", "Settings"):
            if currentScreen == myDormMenu.toScreenName (tabbedPage, givenIcon):
                isCurrentTab = True

        if hasIcon:
            imgDim = renpy.image_size (icons [givenIcon])
            if not iconIsImage:
                imgBrightness = 1.0
                if isInsensitive:
                    imgBrightness = -0.6
                # every screen can only exist once and the button label should be accordingly
                # except it is a tabbed screen, then the toScreenName() is used to determine the tabs screen name
                # so if the current screen name starts with the given label, then it's either the screen name or the beginning of the tabbed screen name
                # the image brightness should be changed for the "main screen button" and "tab screen button"
                if isCurrentTab or isActive:
                    imgBrightness = -1.0
                if noInvert:
                    givenIcon = icons [givenIcon]
                else:
                    givenIcon = Transform (Image (icons [givenIcon]), matrixcolor = InvertMatrix (imgBrightness))
    button:
        if givenTrigger:
            action givenAction
        selected (isCurrentTab or isActive)
        style "MenuNavigationButton"
        yalign 0.5
        hbox:
            spacing int (persistent.menuButtonSize / 2)
            python:
                fsize = persistent.menuButtonSize
                showTextLabel = givenLabel != "" and (persistent.menuButtonShowText or showButtonText)
            if iconIsImage or not showTextLabel:
                $ fsize = int (persistent.menuButtonSize * 1.25) - 1
            yalign 0.5
            if hasIcon and persistent.menuButtonShowIcons:
                $ imgDimX = int (fsize / imgDim [1] * imgDim [0])
                image givenIcon:
                    xsize imgDimX
                    yalign 0.5
                    ysize fsize
            if showTextLabel:
                text givenLabel:
                    style "MenuNavigationButtonText" + ("" if not isInsensitive else "Insensitive")
                    size fsize
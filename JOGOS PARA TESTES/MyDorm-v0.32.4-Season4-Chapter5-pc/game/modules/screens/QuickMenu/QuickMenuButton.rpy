screen QuickMenuButton (givenLabel="", givenIcon="", givenAction=[]):
    python:
        keybindFontSize = int (persistent.quickmenuSize / 2)
        if keybindFontSize < 18: # but we want to be able to read the walkthrough info and i.e. 10px would be really tiny
            keybindFontSize = 18
        _ttTexts = tooltipTexts ["QuickMenu"]
        isInsensitive = False
        if givenLabel == "Q.Load" and not renpy.can_load ("quick-1"):
            isInsensitive = True
        imgBrightness = 1.0
        if isInsensitive:
            imgBrightness = -0.6
        givenImage = Transform (Image (icons [givenIcon]), matrixcolor = InvertMatrix (imgBrightness))
        if givenLabel == "Config":
            givenAction = [ ShowMenu (myDormMenu.getCurrentTab ("Settings")) ]
        tooltipText = ""
        if givenIcon in _ttTexts:
            _ttText = _ttTexts [givenIcon]
            _ttKey = True
            for _ttValue in _ttText:
                _ttValue = _ttValue.strip ()
                if _ttValue:
                    # Why this not-Ren'Py way to add the font size?
                    # We're still in the python box, so Ren'Py doesn't recognize the variable yet...
                    # ... or some other Ren'Py BS resulting in "NameError: Name 'keybindFontSize' is not defined."
                    tooltipText += ("{size=" + str (keybindFontSize) + "}{i}Shortcut: " if _ttKey else "") + _ttValue + ("{/i}{/size}" if _ttKey else "") + "\n"
                _ttKey = False  # Shortcut/HotKey is the first entry
    button:
        action givenAction
        style "QuickmenuButton"
        tooltip tooltipText.strip ()
        padding (int (persistent.quickmenuSize/3), int (persistent.quickmenuSize/3))
        if persistent.quickmenuShowText and persistent.quickmenuPosition in [ "left", "right" ]:
            xsize persistent.quickmenuSize * (7 if persistent.quickmenuShowIcons else 5)
        hbox:
            spacing int (persistent.quickmenuSize / 3)
            xalign 0.0
            if persistent.quickmenuShowText and persistent.quickmenuPosition in [ "left", "right" ]:
                xfill True
            if persistent.quickmenuShowIcons:
                image givenImage:
                    xysize (persistent.quickmenuSize, persistent.quickmenuSize)
                    yalign 0.5
            if persistent.quickmenuShowText:
                text givenLabel:
                    style "MenuNavigationButtonText" + ("" if not isInsensitive else "Insensitive")
                    outlines [ ( persistent.quickmenuOutlineThickness, sixDigitColor (persistent.quickmenuOutlineColor) + toPercent (persistent.quickmenuOutlineOpacity, "hex"), 0, 0 ) ]
                    size persistent.quickmenuSize
                    if persistent.quickmenuPosition == "right":
                        xalign 1.0
                        text_align 1.0
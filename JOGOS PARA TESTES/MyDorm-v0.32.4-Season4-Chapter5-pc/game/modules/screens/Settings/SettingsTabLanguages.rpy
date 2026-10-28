screen SettingsTabLanguages ():
    tag menu
    use Settings ()
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
        toggleOptions = { _("Sí") : True, _("No") : False }
        languagesPerRow = 5
    vpgrid style "MenuVPGrid":
        cols languagesPerRow
        margin (marginLeft * 2, 0, marginRight * 2, 0)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
        for index in range (0, languagesPerRow):
            null height persistent.menuButtonSize
        for language in languages:
            vbox:
                hbox style "MyDormBox":
                    use Button (language ["label"], Language (language ["tl"]), xsize=1.0)
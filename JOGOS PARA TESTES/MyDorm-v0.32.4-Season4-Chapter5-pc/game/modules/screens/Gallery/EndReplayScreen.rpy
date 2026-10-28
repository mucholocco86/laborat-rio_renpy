screen EndReplayScreen ():
    tag end_replay
    python:
        menuMarginX = getScreenDim (0.025)
        menuMarginY = getScreenDim (0.025, False)
        menuSpacing = menuMarginX * getSmallerScreenDimension ()
    frame style "MenuScreenButtonsFrame":
        pos (1.0 - menuMarginX, menuMarginY)
        hbox:
            spacing menuSpacing
            use MenuButton (_("Finalizar repetición"), "Quit", [ EndReplay () ], True)
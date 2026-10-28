screen ProfilesList(gridSize):
    modal True
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenLeft)
        marginRight = getScreenDim (MenuScreenLeft)
        marginBottom = getScreenDim (MenuScreenLeft)
    use ProfilesListTitle (_("Selección de personajes:"), gridSize, marginLeft, marginTop, marginRight, marginBottom)
    python:
        characterProfileGroups = []
        # Household and neighbors
        characterProfileGroups += [ [ mar, emm, nor, dap, eri, mee, bet, sca, ama, eva ] ]
        # Friends
        characterProfileGroups += [ [ kia, eil, oma, sam, sim, mad, meg ] ]
        # Students 1
        characterProfileGroups += [ [ cri, deb, hai, kal, kat, kim, lis, nia, pat, sai, zoe ] ]
    vpgrid style "MenuVPGrid":
        cols gridSize
        margin (marginLeft * 2, marginTop * 2, marginRight * 2, marginBottom * 2)
        mousewheel True
        pos (marginLeft, 0.1)
        scrollbars "vertical"
        xspacing MenuGridSpacing
        xysize (1.0 - marginLeft - marginRight * 2, 0.9 - marginTop - marginBottom)
        yspacing MenuGridSpacing * 2
        yfill True
        # List characters per group
        for characterProfileList in characterProfileGroups:
            $ characterProfileCounter = 0
            for characterProfile in characterProfileList:
                if characterProfile._var ("is known"):
                    $ characterProfileCounter += 1
                    use ProfilesCharacterSelect (characterProfile)
            $ startFillLoop = characterProfileCounter % gridSize
            if startFillLoop > 0:
                for index in range (startFillLoop, gridSize):
                    null

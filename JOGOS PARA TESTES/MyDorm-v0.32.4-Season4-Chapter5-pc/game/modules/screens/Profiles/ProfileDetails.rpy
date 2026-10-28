screen ProfileDetails(characterProfile, gridSize = 2):
    tag profiles
    modal True
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenLeft)
        marginRight = getScreenDim (MenuScreenLeft)
        marginBottom = getScreenDim (MenuScreenLeft)
    use ProfilesListTitle (characterProfile.name.first_name + " " + characterProfile.name.last_name, gridSize, marginLeft, marginTop, marginRight, marginBottom, characterProfile)
    vpgrid style "MenuVPGrid":
        cols 1
        margin (marginLeft * 2, marginTop * 2, marginRight * 2, marginBottom * 2)
        pos (marginLeft, 0.1)
        xspacing MenuGridSpacing
        xysize (1.0 - marginLeft - marginRight * 2, 0.9 - marginTop - marginBottom)
        yspacing MenuGridSpacing * 2
        yfill True
        hbox:
            box_reverse True
            use ProfileDetailsImage (characterProfile)
            use ProfileDetailsBio (characterProfile)
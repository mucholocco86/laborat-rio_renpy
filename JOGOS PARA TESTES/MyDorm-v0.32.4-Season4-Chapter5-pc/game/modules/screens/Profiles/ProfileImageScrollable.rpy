screen ProfileImageScrollable(characterProfile, profileImageLarge):
    tag profiles
    use ModalScreen ()
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenLeft)
        marginRight = getScreenDim (MenuScreenLeft)
        marginBottom = getScreenDim (MenuScreenLeft)
        pdplImageSize = renpy.image_size(profileImageLarge)
        viewportWidth = 1920
        viewportHeight = max(pdplImageSize[1],1080)
        if pdplImageSize[0] < 1920:
            spacerWidth = int((1920-pdplImageSize[0])/2)
        else:
            spacerWidth = 0
    use ScreenBackground (0,0,0,0)
    viewport:
        xysize(viewportWidth, viewportHeight)
        scrollbars "vertical"
        mousewheel True
        draggable True
        arrowkeys True
        hbox:
            null width spacerWidth
            imagebutton:
                idle profileImageLarge
                hover profileImageLarge
                action [ SelectedIf (False), ShowMenu ("Profiles", characterProfile) ]
    use ProfilesScrollingImageBack(characterProfile, marginLeft, marginTop, marginRight, marginBottom)

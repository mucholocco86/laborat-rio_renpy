screen MenuTitle (menuLabel):
    python:
        menuMarginX = getScreenDim (MenuScreenLeft, False)
        menuMarginY = getScreenDim (0.025)
    frame style "MyDormFrame":
        pos (menuMarginX, menuMarginY)
        vbox:
            text "[config.name!t]":
                style "MenuTitleGameName"
            if menuLabel == "":
                text "[config.version]" style "MenuTitleLabel"
            else:
                text menuLabel style "MenuTitleLabel"
            # for debugging tab screen names
            # text str (renpy.current_screen ().screen_name [0]) style "MenuTitleLabel"
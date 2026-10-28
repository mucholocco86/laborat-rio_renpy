# semi-transparent background for menu screens
# takes margins in percent of the smaller screen dimension (height/width)
screen ScreenBackground (left=MenuScreenLeft, top=MenuScreenTop, right=MenuScreenRight, bottom=MenuScreenBottom):
    python:
#        (MenuMarginLeft, MenuMarginTop, MenuMarginRight, MenuMarginBottom) = getMenuScreenValues (0.025, 0.5, 0.025, 0.1)
        
        menuMarginLeft = getScreenDim (left)
        menuMarginTop = getScreenDim (top, False)
        menuMarginRight = getScreenDim (right)
        menuMarginBottom = getScreenDim (bottom, False)
    frame style "ScreenBackgroundFrame":
        if MenuScreenBorders:
            use Borders ()
        area (left, top, 1.0 - left - right, 1.0 - top - bottom)
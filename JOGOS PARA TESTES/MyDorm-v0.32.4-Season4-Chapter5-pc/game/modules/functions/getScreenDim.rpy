init python:
    def getScreenDim (calcVal, isForWidth=True):
        if isinstance (calcVal, float):
            calcVal = calcVal * getSmallerScreenDimension ()
        return calcVal / (config.screen_width if isForWidth else config.screen_height)
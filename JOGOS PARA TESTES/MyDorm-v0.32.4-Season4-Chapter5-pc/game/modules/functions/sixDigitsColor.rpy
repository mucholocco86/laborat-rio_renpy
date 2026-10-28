init -9999 python:
    def sixDigitColor (colorString):
        colorStringLen = len (colorString)
        if colorStringLen == 6:
            cString = "#" + colorString
        elif colorStringLen in (3, 4):
            cString = ("#" if colorStringLen == 3 else "")
            for index in range (1, 4):
                cString += str (colorString [index]) + str (colorString [index])
        else:
            cString = colorString
        return cString
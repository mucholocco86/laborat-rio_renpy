screen Button (label="", action=NullAction, style="MyDormButton", tooltip="", xsize=None):
    button:
        action action
        style style
        text label style style + "_text"
        tooltip tooltip
        if xsize is not None:
            xsize xsize

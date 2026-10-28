screen choice (items, **kwargs):
    python:
        cn = "{color=#ddd}"
        cg = "{color=#0f0}"
        cr = "{color=#f00}"
        cc = "{/color}"
        # Walkthrough info is half the size of the normal dialogue text
        wtFontSize = int (persistent.dialogueWhatSize / 2)
        if wtFontSize < 18: # but we want to be able to read the walkthrough info and i.e. 10px would be really tiny
            wtFontSize = 18
        choiceIndex = 0
        outlineColor = sixDigitColor (persistent.dialogueWhatOutlineColor) + toPercent (persistent.dialogueWhatOutlineOpacity, "hex")
        idleOpacity = persistent.dialogueBoxOpacity
        if idleOpacity < 0.2:
            idleOpacity = 0.3
        hoverOpacity = idleOpacity / (2 if idleOpacity > 0.5 else 0.5)
        if hoverOpacity == 1.0:
            hoverOpacity = 0.25
        elif hoverOpacity == 0.0:
            hoverOpacity = 0.25
        xAlign = 0.5
        if persistent.choicePosition == "left":
            xAlign = 0.0
        elif persistent.choicePosition == "right":
            xAlign = 1.0
        xPos = xAlign
        if persistent.quickmenuShowText:
            if persistent.quickmenuPosition == "left" and persistent.choicePosition == "left":
                xPos += ((persistent.quickmenuSize * (7 if persistent.quickmenuShowIcons else 5)) + MenuGridSpacing) / config.screen_width
            elif persistent.quickmenuPosition == "right" and persistent.choicePosition == "right":
                xPos += ((persistent.quickmenuSize * -1 * (7 if persistent.quickmenuShowIcons else 5)) - MenuGridSpacing) / config.screen_width
        elif persistent.quickmenuShowIcons:
            if persistent.quickmenuPosition == "left" and persistent.choicePosition == "left":
                xPos += (persistent.quickmenuSize * 2 + MenuGridSpacing / 2) / config.screen_width
            elif persistent.quickmenuPosition == "right" and persistent.choicePosition == "right":
                xPos += (persistent.quickmenuSize * -2 - MenuGridSpacing / 2) / config.screen_width
        if persistent.quickmenuPosition != "left" and persistent.choicePosition == "left":
            xPos += -0.001
        if persistent.quickmenuPosition != "right" and persistent.choicePosition == "right":
            xPos += 0.001
    vbox:
        anchor (xAlign, 0.5)
        align (xAlign, 0.5)
        #xpos xAlign + (0.001 if persistent.choicePosition == "right" else (-0.001 if persistent.choicePosition == "left" else 0.0))
        xpos xPos
        spacing MenuGridSpacing / 3
        ypos 0.5 + (MenuGridSpacing / 3 * 2) / config.screen_height
        for choice in items:
            if choice.kwargs.get ("menuTitle"):
                frame:
                    background None
                    padding (0.01, 0.001, 0.01, 0)
                    xalign xAlign
                    label choice.caption:
                        text_outlines [ ( persistent.dialogueWhatOutlineThickness, outlineColor, 0, 0 ) ]
                        text_size 45
                        text_color "#f90"
            elif choice.kwargs.get ("headline"):
                frame:
                    background None
                    padding (0.01, 0.001, 0.01, 0)
                    xalign xAlign
                    label choice.caption:
                        text_outlines [ ( persistent.dialogueWhatOutlineThickness, outlineColor, 0, 0 ) ]
            elif choice.kwargs.get ("subheadline"):
                frame:
                    background None
                    padding (0.01, 0.001, 0.01, 0)
                    xalign xAlign
                    text choice.caption:
                        outlines [ ( persistent.dialogueWhatOutlineThickness, outlineColor, 0, 0 ) ]
                        text_align xAlign
                        color "#0f9"
                        xalign xAlign
                        yalign 0.5
            else:
                button:
                    background Frame (Transform ("gui/textbox.png", alpha = idleOpacity), 1.0, 1.0)
                    hover_background Frame (Transform ("gui/textbox.png", alpha = hoverOpacity), 1.0, 1.0)
                    padding (0.01, 0.005, 0.01, 0.005)
                    xalign xAlign
                    if persistent.choicePosition == "middle":
                        xsize 0.75
                    xmaximum 0.75
                    yalign 0.5
                    action choice.action
                    python:
                        choiceIndex += 1
                        choiceKeyShortcut = choiceIndex
                        if choiceKeyShortcut == 10:
                            choiceKeyShortcut = 0
                        captionLinesLength = 1
                        choiceCaption = renpy.translate_string (choice.caption)
                        if persistent.walkthrough:
                            wt = choice.kwargs.get ("wt", None)
                            if wt is not None:
                                wt = renpy.translate_string (wt)
                                wt = wt.split ("\n")
                                for wtChunk in wt:
                                    wtChunk = renpy.translate_string (wtChunk)
                                    wtChunk = renpy.translate_string ("\n" + wtChunk)
                                    if wtChunk is not None:
                                        captionLinesLength += wt.count ("\n")
                                        choiceCaption += "{i}{size=[wtFontSize]}"
                                        choiceCaption += wtChunk
                                        choiceCaption += "{/i}{/size}"
                    hbox:
                        yalign 0.5
                        spacing (MenuGridSpacing / 2)
                        if persistent.choicePosition == "middle":
                            xfill True
                        if persistent.choicePosition in [ "left", "middle" ]:
                            hbox:
                                spacing (MenuGridSpacing / 2)
                                yalign 0.5
                                text str (choiceKeyShortcut if choiceKeyShortcut < 11 else " "):
                                    xalign xAlign
                                    yalign 0.5
                                    text_align xAlign
                                    outlines [ ( persistent.dialogueWhatOutlineThickness, outlineColor, 0, 0 ) ]
                                frame:
                                    background Solid (outlineColor)
                                    xsize int (persistent.dialogueWhatSize / 10)
                                    ysize int ((persistent.dialogueWhatSize + (wtFontSize * (captionLinesLength - 1))) * 1.5)
                        hbox:
                            if persistent.choicePosition == "middle":
                                xfill True
                            yalign 0.5
                            text choiceCaption:
                                xalign xAlign
                                yalign 0.5
                                text_align xAlign
                                outlines [ ( persistent.dialogueWhatOutlineThickness, outlineColor, 0, 0 ) ]
                        if persistent.choicePosition in [ "right" ]:
                            hbox:
                                spacing (MenuGridSpacing / 2)
                                yalign 0.5
                                frame:
                                    background Solid (outlineColor)
                                    xsize int (persistent.dialogueWhatSize / 10)
                                    ysize int ((persistent.dialogueWhatSize + (wtFontSize * (captionLinesLength - 1))) * 1.5)
                                text str (choiceKeyShortcut if choiceKeyShortcut < 11 else " "):
                                    xalign xAlign
                                    yalign 0.5
                                    text_align xAlign
                                    outlines [ ( persistent.dialogueWhatOutlineThickness, outlineColor, 0, 0 ) ]
                                    size persistent.dialogueWhatSize
                if choiceKeyShortcut < 10:
                    key str (choiceKeyShortcut) action choice.action
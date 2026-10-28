init 1000:
    screen input (prompt, defaultValue="", multiple=(1,1)):
        python:
            # splitting the multiple-tuple; we actually only need the numberOfBlocks for window width calculation
            blockNumber, numberOfBlocks = multiple
            # the gradient at the top of the text box
            # we only want that, so that the name of the speaker starts below that
            gradientHeight = 25
            gradientHeightInPercent = float (gradientHeight / defaultSettings ["screen"]["height"])
            # calculating height of the textbox, keeping in mind that the gradient is meant to be above the textbox
            windowYSizeInPercent = float (persistent.dialogueBoxHeight) / float (defaultSettings ["screen"]["height"])
            windowYSize = float (windowYSizeInPercent) + float (gradientHeightInPercent)
            # calculating additional height for the quick menu
            if persistent.quickmenuPosition:
                buttonTextSize = int (persistent.quickmenuSize) + int (persistent.quickmenuOutlineThickness * 2)
                windowYSize += buttonTextSize / defaultSettings ["screen"]["height"]
            # calculating the window width depending on number of blocks, so that the padding stays the same for one and more simultaneous speakers
            # also, max setting for textbox width might not be screen width, so we recalculate it to make it max 100% of screen width
            windowXSizeInPercent = float (persistent.dialogueBoxWidth) / float (defaultSettings ["screen"]["width"])
            windowXSize = windowXSizeInPercent
            # calculating the padding which is the screen width (1.0 = 100%) minus the width of the textbox
            #
            # if there are more blocks, the %-ile padding stays the same, but the px padding shrinks to 1/numberOfBlocks,
            # since each block is 1/numberOfBlocks in width of the screen
            # to keep the padding the same, we multiply that padding with the number of blocks
            # if numberOfBlocks > 1:
            #     windowXSize = 1.0 - (1.0 - windowXSize) * numberOfBlocks    
            inputPadding = int (persistent.dialogueWhatSize / 8)    
            inputPrompt = prompt.strip ("{i}").strip ("{/i}").strip ("(").replace (")", "", 1)
            replacements = {
                "(" : "{i}(",
                ")" : "){/i}"
            }
            for replacementFrom, replacementTo in replacements.items ():
                inputPrompt = inputPrompt.replace (replacementFrom, replacementTo)
        style_prefix "say"
        window:
            id "window"
            ysize windowYSize
            yanchor 1.0
            if numberOfBlocks == 1:
                xanchor 0.5
            else:
                if blockNumber == 1:
                    xanchor 0.0
                else:
                    xanchor 1.0
            xfill True
            xpos 0.5
            frame:
                background Transform (Frame ("gui/textbox.webp", 0, 0), alpha=persistent.dialogueBoxOpacity)
                pos (0, 0)
                xsize 1.0
                ysize 25
            frame:
                background Solid (sixDigitColor ("#000") + toPercent (persistent.dialogueBoxOpacity, "hex"))
                pos (0, 25)
                xsize 1.0
                yfill True
            vbox:
                xanchor 0.5
                xpos 0.5
                # spacing from the top of the textbox / space between top of textbox and top of actors name.
                ypos int (gradientHeight / 2)
                # line height is percepted best if it's 1.4 to 1.6 of the font of the respective line
                # 1/3 of the font size bumps the line height to around 1.43 (without spacing above text, that doesn't matter for the name)
                spacing 0
                window:
                    id "namebox"
                    style "namebox"
                    background None
                    xsize windowXSize
                    xfill True
                    #xsize windowXSize   # we need all three xsize declarations, so that multiple(x,1) and multiple(1,2+) work
                    text "":
                        id "who"
                        outlines [ (persistent.dialogueWhoOutlineThickness, sixDigitColor ("#000") + toPercent (persistent.dialogueWhoOutlineOpacity, "hex"), 0, 0) ]
                        size persistent.dialogueWhoSize
                        xpos 0.0
                        xalign 0.0
                        xsize 1.0
                        xfill True
                text renpy.translate_string (inputPrompt):
                    id "what"
                    outlines [ (persistent.dialogueWhatOutlineThickness, sixDigitColor ("#000") + toPercent (persistent.dialogueWhatOutlineOpacity, "hex"), 0, 0) ]
                    size persistent.dialogueWhatSize
                    xpos 0.0
                    xalign 0.0
                    xsize 1.0
                    xfill True
                    ypos int (persistent.dialogueWhoSize * 1.6)
                    color "#fff"
                frame:
                    background Solid ("#fff9")
                    anchor (0.0, 1.0)
                    xysize (0.25, persistent.dialogueWhatSize + 4 * inputPadding)
                    padding (inputPadding, inputPadding, inputPadding, inputPadding * 3)
                    input:
                        id "input"
                        default defaultValue
                        outlines [ ( persistent.dialogueWhatOutlineThickness, sixDigitColor (persistent.dialogueWhatOutlineColor) + toPercent (persistent.dialogueWhatOutlineOpacity, "hex"), 0, 0 ) ]
                        size persistent.dialogueWhatSize
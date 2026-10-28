# screen say (who, what, bottomMargin=False):
#     style_prefix "say"
#     python:
# # box size calculations from variable settins
#         lineHeightMult = 1.5
#         textLinesBecauseOfFontSize = 1
#         if persistent.dialogueWhatSize > 12:
#             textLinesBecauseOfFontSize = 2
#         if persistent.dialogueWhatSize > 24:
#             textLinesBecauseOfFontSize = 3
#         if persistent.dialogueWhatSize > 36:
#             textLinesBecauseOfFontSize = 4
#         whoLineHeight = int (persistent.dialogueWhoSize * lineHeightMult)
#         whatBoxHeight = int (persistent.dialogueWhatSize * lineHeightMult * textLinesBecauseOfFontSize)
#         qnBoxHeight = int (persistent.quickmenuSize * 2 + MenuGridSpacing / 2)
#         inputPadding = int (persistent.dialogueWhatSize / 2)
#         dialogueBoxHeight = whoLineHeight + whatBoxHeight + inputPadding # this is, so the height of the say box and input box is always the same
#         if persistent.quickmenuPosition == "bottom":
#             dialogueBoxHeight += qnBoxHeight
#         hasWho = who is not None        # check if this text has an actor
#         # if not hasWho and not centered: # if it does not have an actor and is not a "system message"
#         #     who = narrator              # set actor to narrator
#         #     hasWho = True
#         isThought = what.startswith ("{i}") and what.endswith ("{/i}")
#         if who == "":
#             hasWho = False
#         if hasWho and not isinstance (who, str):
#             who = str (who)
#     window:
#         background Frame (Transform ("gui/textbox.png", alpha = persistent.dialogueBoxOpacity), 15, 15)
#         id "window"
#         ysize dialogueBoxHeight
#         if bottomMargin: # used in settings preview
#             yanchor 0.0
#             ypos 1.0 - bottomMargin
#         if hasWho:
#             window:
#                 id "namebox"
#                 style "namebox"
#                 text who:
#                     id "who"
#                     if bottomMargin: # used in settings preview
#                         style "label"
#                     if isThought: # thought indicators are removed with functions/say_menu_text_filter
#                         italic True
#                     outlines [ ( persistent.dialogueWhoOutlineThickness, sixDigitColor (persistent.dialogueWhoOutlineColor) + toPercent (persistent.dialogueWhoOutlineOpacity, "hex"), 0, 0 ) ]
#                     size persistent.dialogueWhoSize
#         text what:
#             id "what"
#             if bottomMargin: # used in settings preview
#                 style "dialogue"
#             outlines [ ( persistent.dialogueWhatOutlineThickness, sixDigitColor (persistent.dialogueWhatOutlineColor) + toPercent (persistent.dialogueWhatOutlineOpacity, "hex"), 0, 0 ) ]
#             size persistent.dialogueWhatSize
#             ypos whoLineHeight

init 1000:
    screen say(who, what, multiple=(1,1)):
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
        #style_prefix "say"
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
                    if who is None:
                        $ who = ""
                    text who:
                        id "who"
                        outlines [ (persistent.dialogueWhoOutlineThickness, sixDigitColor ("#000") + toPercent (persistent.dialogueWhoOutlineOpacity, "hex"), 0, 0) ]
                        size persistent.dialogueWhoSize
                        xpos 0.0
                        xalign 0.0
                        xsize 1.0
                        xfill True
                    text what:
                        id "what"
                        outlines [ (persistent.dialogueWhatOutlineThickness, sixDigitColor ("#000") + toPercent (persistent.dialogueWhatOutlineOpacity, "hex"), 0, 0) ]
                        size persistent.dialogueWhatSize
                        xpos 0.0
                        xalign 0.0
                        xsize 1.0
                        xfill True
                        ypos int (persistent.dialogueWhoSize * 1.6)
                        color "#fff"

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

    screen multiple_say(who, what, multiple):
        use say (who, what, multiple)

init 1000:
    style namebox:
        align (0.0, 0.0)
        margin (0, 0, 0, 0)
        padding (0, 0, 0, 0)

    style say_label:
        align (0.0, 0.0)
        margin (0, 0, 0, 0)
        padding (0, 0, 0, 0)

    style say_dialogue:
        properties gui.text_properties("dialogue")  # ToDo: Find general settings Ren'Py suggests, use them here directly and adjust to customizable textbox
        align (0.0, 0.0)
        margin (0, 0, 0, 0)
        padding (0, 0, 0, 0)
    
    style input_prompt is say_dialogue

    style say_window:
        anchor (0.5, 1.0)
        background None
        pos (0.5, 1.001)
        xalign 0.5
        xfill True

    style input_window is say_window

    style multiple2_window is say_window:   # This is intentionally not multiple2_say_window!
        xanchor 0.0
        xsize 0.5

    style block1_multiple2_say_window is multiple2_window:
        xfill False
        xpos 0.0

    style block2_multiple2_say_window is block1_multiple2_say_window:
        xpos 0.5

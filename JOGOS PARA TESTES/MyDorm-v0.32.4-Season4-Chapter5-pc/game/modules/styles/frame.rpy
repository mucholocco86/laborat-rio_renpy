style MyDormFrame is frame:
    background None
    
# Save and Load Screen

style GameSaveLoadFileSlotEditFrame:
    align (0.0, 0.0)
    anchor (0.0, 0.0)
    background Solid (GameSaveLoadFileSlotBackgroundColor)
    padding (2, 2)
    pos (0.0, 0.0)
    
style GameSaveLoadFileSlotDeleteFrame is GameSaveLoadFileSlotEditFrame:
    align (1.0, 0.0)
    anchor (1.0, 0.0)
    pos (1.0, 0.0)

style GameSaveLoadFileSlotFrame:
    align (0.5, 1.0)
    anchor (0.5, 1.0)
    background Solid (GameSaveLoadFileSlotBackgroundColor)
    padding (10, 10)
    ypos 1.0
    text_align 0.5
    xsize 1.0

# Main Menu

style MenuDevSupportFrame is MyDormFrame:   # only in Main Menu, not in "Game Menu"
    anchor (0.0, 1.0)

style MenuNavigationBackToMainMenuButtonFrame is MyDormFrame:
    anchor (0.0, 1.0)

style MenuNavigationGeneralButtonsFrame is MyDormFrame:
    anchor (0.5, 1.0)

style MenuNavigationQuitButtonFrame is MyDormFrame:
    anchor (1.0, 1.0)

style MenuScreenButtonsFrame is MyDormFrame:
    anchor (1.0, 0.0)

style SettingsTabFrame is MyDormFrame

style ScreenBackgroundFrame:
    background Solid (ScreenBackgroundColor)
    anchor (0.0, 0.0)
    modal True

# Confirmation Screens

style ConfirmFrame:
    align (0.5, 0.5)
    background Solid (ScreenBackgroundColor)
    modal True

style ModalScreenFrame is MyDormFrame:
    modal True

style ModalScreenFrame:
    anchor (0.0, 0.0)
    align (0.5, 0.5)
    background None
    margin (0, 0, 0, 0)
    modal True
    padding (0, 0, 0, 0)
    xysize (1.0, 1.0)

# Frames to highlight Input fields

style MyDormInputFrame:
    xfill True
    area (0.0, 0.0, 0.9, 35)
    background Solid (InputBackgroundColor)
    padding (5, 2, 5, 8)

style ProfilesFrameBack is frame:
    background None
    xanchor 1.0

style ProfilesImageButtonFrame is frame:
    background Solid ("#ffffff99")

style ProfilesImageButtonFrameNext is ProfilesImageButtonFrame:
    anchor (0.0, 1.0)
    pos (0.0, 1.0)
    # anchor (1.0, 1.0) # for centered buttons
    # pos (0.5, 1.0)

style ProfilesImageButtonFramePrevious is ProfilesImageButtonFrame:
    anchor (1.0, 1.0)
    pos (1.0, 1.0)
    # anchor (0.0, 1.0) # for centered buttons
    # pos (0.5, 1.0)

init -1: # needs to be declared before ProfilesInputButton, which comes alphabetically before ProfilesInputFrame, so we set the init offset manually
    style ProfilesInputFrame:
        background Solid (MenuButtonBackgroundColorSelected)
        padding (ButtonTextSize, int (ButtonTextSize / 3))
        xsize 200
        ysize int (ButtonTextSize * 2.0)
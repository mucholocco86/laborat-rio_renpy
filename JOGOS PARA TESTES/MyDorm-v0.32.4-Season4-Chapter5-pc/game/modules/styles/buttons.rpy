style MyDormButton:
    background Solid (ButtonBackgroundColorIdle)
    hover_background Solid (ButtonBackgroundColorHover)
    idle_background Solid (ButtonBackgroundColorIdle)
    selected_background Solid (ButtonBackgroundColorSelected)
    outlines [ (ButtonTextOutlineThickness, ButtonTextOutlineColor, 0, 0) ]
    padding (ButtonTextSize, int (ButtonTextSize / 3))
    text_align 0.5

style ProfilesButton is MenuNavigationButton:
    right_margin 10
    outlines [ (ButtonTextOutlineThickness, ButtonTextOutlineColor, 0, 0) ]
    padding (ButtonTextSize, int (ButtonTextSize / 3))
    text_align 0.5

style ProfilesButton_text is MenuNavigationButtonText:
    size ButtonTextSize
    xalign 0.5


style ProfilesButtonNoMargin is ProfilesButton:
    right_margin 0

# Settings
style MyDormButtonMute is MenuDefaultButton:
    xysize (None, None)

style MyDormButton_text:
    color ButtonTextColorIdle
    hover_color ButtonTextColorHover
    idle_color ButtonTextColorIdle
    insensitive_color ButtonTextColorInsensitive
    selected_color ButtonTextColorSelected
    outlines [ (ButtonTextOutlineThickness, ButtonTextOutlineColor, 0, 0) ]
    size ButtonTextSize
    xalign 0.5
    
style MyDormButtonMute_text is MyDormButton_text:
    size ButtonTextSizeSmall

# Confirm screens

style ConfirmButtons is MyDormButton

style ModalScreenButton:
    area (0.0, 0.0, 1.0, 1.0)
    anchor (0.0, 0.0)
    background Solid (MenuScreenModalBackgroundColor)
    margin (0, 0, 0, 0)
    padding (0, 0, 0, 0)
    xysize (1.0, 1.0)

# Menu Navigations

style MenuNavigationButton:
    background Solid (MenuButtonBackgroundColorIdle)
    hover_background Solid (MenuButtonBackgroundColorHover)
    idle_background Solid (MenuButtonBackgroundColorIdle)
    insensitive_background Solid (MenuButtonBackgroundColorInsensitive)
    selected_background Solid (MenuButtonBackgroundColorSelected)
    padding (0.01, 0.01)

style QuickmenuButton is MenuNavigationButton:
    background Solid (ButtonBackgroundColorIdle)
    hover_background Solid (ButtonBackgroundColorHover)
    idle_background Solid (ButtonBackgroundColorIdle)
    xalign 0.0

style GameSaveLoadFileSlotsButton:
    background Solid (MenuButtonBackgroundColorIdle)
    xsize 384
    ysize 216

style MenuDefaultButton is MyDormButton:
    align (0.5, 0.5)
    anchor (0.0, 0.5)
    pos (0.0, 0.5)
    xysize (MenuLabelTextSize, MenuLabelTextSize)

style ProfilesInputButton:
    take ProfilesInputFrame
    color "#000000"
    background Solid (MenuButtonBackgroundColorSelected)
    hover_background Solid (ButtonBackgroundColorHover)
    idle_background Solid (MenuButtonBackgroundColorSelected)
    insensitive_background Solid (MenuButtonBackgroundColorInsensitive)
    selected_background Solid (ButtonBackgroundColorSelected)

style ProfilesInputButton_text:
    size ButtonTextSize
    color "#000000"
    idle_color "#000000"
    hover_color "#000000"
    selected_color "#000000"
    insensitive_color "#cccccc"
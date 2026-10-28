style Profile_text:
    align (0.5, 0.5)

style SectionTitle_text is MenuTitleGameName

style TextSmall:
    size TextSmallFontSize

style TextSmallHighlight is TextSmall:
    bold True
    color "#cc9966"

style TextSmallCentered is TextSmall:
    xalign 0.5

style TextSmallCenteredHighlight is TextSmallHighlight:
    xalign 0.5

style TextMedium:
    size TextMediumFontSize

style TextMediumCentered is TextMedium:
    xalign 0.5

style TextLarge:
    size TextLargeFontSize

style TextLargeCentered is TextLarge:
    xalign 0.5

# Main Menu and Title Screen
style MenuNavigationButtonText:
    color MenuButtonTextColorIdle
    hover_color MenuButtonTextColorHover
    selected_color MenuButtonTextColorSelected
    outlines [ (MenuButtonOutlineThickness, MenuButtonOutlineColor, 0, 0) ]

style MenuNavigationButtonTextInsensitive:
    color MenuButtonTextColorInsensitive

style MenuTitleGameName:
    color MenuLabelTextColor
    outlines [ (MenuLabelTextOutlineThickness, MenuLabelTextOutlineColor, 0, 0) ]
    size MenuLabelTextSizeTitle
    
style MenuTitleLabel is MenuTitleGameName:
    size MenuLabelTextSize

style MenuText is text:
    outlines [ (MenuTextOutlineThickness, MenuTextOutlineColor, 0, 0) ]
    xsize 1.0

style MenuSettingsValueText:
    outlines [ (MenuTextOutlineThickness, MenuTextOutlineColor, 0, 0) ]
    xalign 1.0
    xpos MenuLabelTopMargin * -1
    yalign 0.5

#### Quick Menu
style QuickMenuButtonText:
    color QuickMenuTextColorIdle
    idle_color QuickMenuTextColorIdle
    insensitive_color QuickMenuTextColorInsensitive
    hover_color QuickMenuTextColorHover
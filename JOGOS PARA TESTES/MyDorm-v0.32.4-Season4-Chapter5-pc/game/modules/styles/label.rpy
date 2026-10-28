style MenuLabel:
    bottom_margin MenuLabelTopMargin
    top_margin MenuLabelTopMargin

style SectionTitle is MenuLabel

style ProfileLabel is MenuLabel:
    bottom_margin 0
    top_margin 0

style MenuLabel_text:
    color MenuLabelTextColor
    outlines [ (MenuLabelTextOutlineThickness, MenuLabelTextOutlineColor, 0, 0) ]
    size MenuLabelTextSize
    underline MenuLabelUnderlined

style ProfileLabel_text is MenuLabel_text

style HistoryLabel is MenuLabel:
    bottom_margin 0

style HistoryLabel_text is MenuLabel_text:
    underline MenuLabelUnderlined
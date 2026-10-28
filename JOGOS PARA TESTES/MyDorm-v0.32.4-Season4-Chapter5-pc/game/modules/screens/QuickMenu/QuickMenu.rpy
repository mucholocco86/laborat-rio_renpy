screen QuickMenu ():
    tag quick_menu
    if not persistent.quickmenuHidden:
        $ quickMenuButtonList = getQuickMenuButtons ()
        zorder 100
        python:
            menuSpacing = int (MenuGridSpacing / 2)
            # quickmenu positioning
            xAlign = 0.5
            yAlign = 0.0
            if persistent.quickmenuPosition == "left":
                xAlign = 0.0
                yAlign = 0.5
            elif persistent.quickmenuPosition == "right":
                xAlign = 1.0
                yAlign = 0.5
            elif persistent.quickmenuPosition == "bottom":
                yAlign = 1.0
        if quick_menu:
            frame style "MyDormFrame":
                anchor (xAlign, yAlign)
                align (xAlign, yAlign)
                id "QuickMenuFrame"
                if persistent.quickmenuPosition == "left":
                    xpos 0.0 - int (menuSpacing / 2) / config.screen_height
                elif persistent.quickmenuPosition == "right":
                    xpos 1.0 + int (menuSpacing / 2) / config.screen_width
                elif persistent.quickmenuPosition == "top":
                    ypos 0.0 - int (menuSpacing / 2) / config.screen_height
                else:
                    ypos 1.0 + int (menuSpacing / 2) / config.screen_height
                background Frame (Transform ("gui/textbox.png", alpha = persistent.dialogueBoxOpacity), 15, 15)
                modal True
                if persistent.quickmenuPosition in [ "left", "right" ]:
                    vbox:
                        spacing menuSpacing
                        for buttonLabel, (buttonIcon, buttonAction) in quickMenuButtonList.items ():
                            use QuickMenuButton (buttonLabel, buttonIcon, buttonAction)
                else:
                    hbox:
                        spacing menuSpacing
                        for buttonLabel, (buttonIcon, buttonAction) in quickMenuButtonList.items ():
                            use QuickMenuButton (buttonLabel, buttonIcon, buttonAction)
    $ tooltip = GetTooltip ()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                background Frame (Transform ("gui/textbox.png", alpha = persistent.dialogueBoxOpacity), 15, 15)
                text tooltip:
                    outlines [ ( persistent.quickmenuOutlineThickness, sixDigitColor (persistent.quickmenuOutlineColor) + toPercent (persistent.quickmenuOutlineOpacity, "hex"), 0, 0 ) ]
                    size persistent.quickmenuSize
    use QuickMenuKeyBinds ()
    if _in_replay:
        use EndReplayScreen ()
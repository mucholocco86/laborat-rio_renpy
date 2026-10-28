screen MenuDevSupport ():
    python:
        menuMarginX = getScreenDim (0.025)
        menuMarginY = getScreenDim (0.025, False)
        menuSpacing = int (MenuGridSpacing / 2)
        buttons = []
        buttons.append ([ _("Discord"), "Discord", [ OpenURL ("https://discord.gg/D5hNSYN9BM") ], True ])
        buttons.append ([ _("Subscribestar"), "Subscribestar", [ OpenURL ("https://subscribestar.adult/tropecitagames") ], True ]) 
        buttons.append ([ _("Patreon"), "Patreon", [ OpenURL ("https://www.patreon.com/bePatron?u=70740879") ], True ])
        buttons1 = []
        buttons1.append ([ _("Steam S1"), "SteamS1", [ OpenURL ("https://store.steampowered.com/app/3510160") ], True ])
        buttons1.append ([ _("Steam S2"), "SteamS2", [ OpenURL ("https://store.steampowered.com/app/4178920") ], True ])
        buttons1.append ([ "Steam S3", "SteamS3", [ OpenURL ("https://store.steampowered.com/app/4873630/My_Dorm__Season_3/") ], True ])
    frame style "MenuNavigationBackToMainMenuButtonFrame":
        pos (0.0 + menuMarginX, 1 - menuMarginY)
        hbox style "MyDormBoxLeft":
            spacing menuSpacing
            vbox style "MyDormBoxLeft":
                spacing menuSpacing
                hbox style "MyDormBoxLeft":
                    spacing menuSpacing
                    for (buttonLabel, buttonIcon, buttonAction, buttonTrigger) in  buttons [0:] :
                        use MenuButton ("", buttonIcon, buttonAction, buttonTrigger, noInvert = True)
                hbox style "MyDormBoxCentered":
                    spacing menuSpacing
                    for (buttonLabel, buttonIcon, buttonAction, buttonTrigger) in buttons1 [0:]:
                        use MenuButton ("", buttonIcon, buttonAction, buttonTrigger, noInvert = True)
                    if hasPatch:
                        use MenuButton (_("Parentesco") if persistent.family else _("Clonación"), "Family", [ SelectedIf (ToggleField (persistent, "family")), Function (myDorm.toggleFamily) ], True, isActive = persistent.family)

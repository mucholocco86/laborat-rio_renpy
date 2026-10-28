screen SettingsTabChoices ():
    tag menu
    use Settings (MenuScreenBottomSettingsDialogue)
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottomSettingsDialogue, False)
    vpgrid style "MenuVPGrid":
        cols 3
        margin (marginLeft * 2, 0, marginRight * 2, 0)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
# Choice Menu Settings
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "choicePosition", defaultSettings ["choicePosition"])), "MenuDefaultButton")
                text " "
                label _("Posición del opciones") style "MenuLabel"
                $ buttons = [ (_("Izquierdo"), "left"), (_("Centrado"), "middle"), (_("Derecho"), "right") ]
            hbox style "MyDormBox":
                for btn, btnPos in buttons:
                    use Button (btn, SelectedIf (SetField (persistent, "choicePosition", btnPos.lower ())))
        null height 0   # null item to fill the vpgrig up to cols value
        null height 0   # null item to fill the vpgrig up to cols value
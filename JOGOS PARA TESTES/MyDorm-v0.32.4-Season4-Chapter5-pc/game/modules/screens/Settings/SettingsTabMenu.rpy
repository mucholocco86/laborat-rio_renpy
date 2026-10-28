screen SettingsTabMenu ():
    tag menu
    use Settings ()
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
    vpgrid style "MenuVPGrid":
        cols 3
        margin (marginLeft * 2, 0, marginRight * 2, 0)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
# Button Settings
        vbox:
            hbox:
                use Button (" ", [ SelectedIf (persistent.menuButtonShowIcons == defaultSettings ["menuButtonShowIcons"] and persistent.menuButtonShowText == defaultSettings ["menuButtonShowText"]), SetField (persistent, "menuButtonShowIcons", defaultSettings ["menuButtonShowIcons"]), SetField (persistent, "menuButtonShowText", defaultSettings ["menuButtonShowText"]) ], "MenuDefaultButton")
                text " "
                label _("Botones de menú") style "MenuLabel"
                $ options = { _("Iconos") : ["menuButtonShowIcons", _("Texto")], _("Texto") : ["menuButtonShowText", _("Iconos")] }
            hbox style "MyDormBox":
                for buttonLabel, varName in options.items ():
                    python:
                        counterOption = options [varName [1]][0]
                        varName = varName [0]
                        buttonAction = []
                        buttonAction.append (ToggleField (persistent, varName))
                        isSelected = False
                        if  getattr (persistent, varName):
                            buttonAction.append (SetField (persistent, counterOption, True))
                            isSelected = True
                        buttonAction.append (SelectedIf (isSelected))
                    use Button (buttonLabel, buttonAction)
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "menuButtonSize", defaultSettings ["menuButtonSize"])), "MenuDefaultButton")
                text " "
                label _("Tamaño del botón") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "menuButtonSize", offset = MenuButtonSizeMin, range = MenuButtonSizeMax - MenuButtonSizeMin, style="slider")
                text "[persistent.menuButtonSize]" style "MenuSettingsValueText"
        null height 0   # null item to fill the vpgrig up to cols value
# Quick Menu Settings (Show Icons/Text/Q.Menu Position)
        vbox:
            hbox:
                use Button (" ", [ SelectedIf (persistent.quickmenuShowIcons == defaultSettings ["quickmenuShowIcons"] and persistent.quickmenuShowText == defaultSettings ["quickmenuShowText"]), SetField (persistent, "quickmenuShowIcons", defaultSettings ["quickmenuShowIcons"]), SetField (persistent, "quickmenuShowText", defaultSettings ["quickmenuShowText"]) ], "MenuDefaultButton")
                text " "
                label _("Botones de menú rápido") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varName in { _("Iconos") : ["quickmenuShowIcons", _("Texto")], _("Texto") : ["quickmenuShowText", _("Iconos")] }.items ():
                    python:
                        counterOption = options [varName [1]][0]
                        varName = varName [0]
                        buttonAction = []
                        buttonAction.append (ToggleField (persistent, varName))
                        isSelected = False
                        if  getattr (persistent, varName):
                            buttonAction.append (SetField (persistent, counterOption, True))
                            isSelected = True
                        buttonAction.append (SelectedIf (isSelected))
                    use Button (buttonLabel, buttonAction)
        vbox:
            hbox:
                button:
                    action SelectedIf (SetField (persistent, "quickmenuPosition", defaultSettings ["quickmenuPosition"]))
                    style "MenuDefaultButton"
                    text " "
                text " "
                label _("Posición de menú rápido") style "MenuLabel"
            hbox style "MyDormBox":
                for btn, btnPos in [ (_("Izquierdo"), "left"), (_("Superior"), "top") , (_("Derecho"), "right"), (_("Inferior"), "bottom") ]:
                    use Button (btn, SelectedIf (SetField (persistent, "quickmenuPosition", btnPos.lower ())))
        null height 0   # null item to fill the vpgrig up to cols value
# Quick Menu Hidden / Shown Buttons
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "quickmenuHidden", defaultSettings ["quickmenuHidden"])), "MenuDefaultButton")
                text " "
                label _("Hacer invisible el menú rápido") style "MenuLabel"
            hbox style "MyDormBox":
                $ options = { _("Sí") : True, _("No") : False }
                for buttonLabel, varValue in options.items ():
                    use Button (buttonLabel, SelectedIf (SetField (persistent, "quickmenuHidden", varValue)))
        vbox:
            python:
                buttons = {
                    _("Salir") : "Quit",
                    _("Historia") : "History",
                    _("Guardar/Cargar") : "SaveLoad",
                    _("Guardar/Cargar R.") : "QSaveQLoad",
                    _("Saltar") : "Skip",
                    _("Retroceder") : "RollBackFwd"
                }
                btnActionList = []
                isSelected = True
                for btn in buttons.values ():
                    btnField = "quickmenuButtons" + btn
                    isSelected = isSelected and getattr (persistent, btnField) == defaultSettings [btnField]
                    btnActionList.append (SetField (persistent, btnField, defaultSettings [btnField]))
                btnAction = [ SelectedIf (isSelected) ]
                btnAction += btnActionList
                btnIndex = 0
            hbox:
                use Button (" ", btnAction, "MenuDefaultButton")
                text " "
                label _("Botones de menú rápido") style "MenuLabel"
            hbox style "MyDormBox":
                box_wrap True
                for btnLabel, btnField in buttons.items ():
                    $ btnIndex += 1
                    if btnIndex < 4:
                        $ btnField = "quickmenuButtons" + btnField
                        button:
                            action SelectedIf (ToggleField (persistent, btnField))
                            style "MyDormButton"
                            bottom_margin MenuGridSpacing
                            text btnLabel style "MyDormButton_text"
        vbox:
            python:
                buttons = {
                    _("Salir") : "Quit",
                    _("Historia") : "History",
                    _("Guardar/Cargar") : "SaveLoad",
                    _("Guardar/Cargar R.") : "QSaveQLoad",
                    _("Saltar") : "Skip",
                    _("Retroceder") : "RollBackFwd"
                }
                btnIndex = 0
            hbox:
                label " " style "MenuLabel"
            hbox style "MyDormBox":
                box_wrap True
                for btnLabel, btnField in buttons.items ():
                    $ btnIndex += 1
                    if btnIndex > 3:
                        $ btnField = "quickmenuButtons" + btnField
                        button:
                            action SelectedIf (ToggleField (persistent, btnField))
                            style "MyDormButton"
                            bottom_margin MenuGridSpacing
                            text btnLabel style "MyDormButton_text"
# Quick Menu Text Settings
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "quickmenuOutlineOpacity", defaultSettings ["quickmenuOutlineOpacity"])), "MenuDefaultButton")
                text " "
                label _("Opacidad contorno menú rápido") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "quickmenuOutlineOpacity", range = 1.0, style="slider")
                text toPercent (persistent.quickmenuOutlineOpacity, "str") style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "quickmenuOutlineThickness", defaultSettings ["quickmenuOutlineThickness"])), "MenuDefaultButton")
                text " "
                label _("Grosor contorno menú rápido") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "quickmenuOutlineThickness", range = 5, style="slider")
                text "[persistent.quickmenuOutlineThickness]" style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "quickmenuSize", defaultSettings ["quickmenuSize"])), "MenuDefaultButton")
                text " "
                label _("Tamaño de fuente menú rápido") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "quickmenuSize", offset = 10, range = 50, style="slider")
                text "[persistent.quickmenuSize]" style "MenuSettingsValueText"
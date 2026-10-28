screen SettingsTabGeneral ():
    tag menu
    use Settings ()
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
        toggleOptions = { _("Sí") : True, _("No") : False }
    vpgrid style "MenuVPGrid":
        cols 3
        margin (marginLeft * 2, 0, marginRight * 2, 0)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
# Language / Walkthrough / Pregnancy Content
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "walkthrough", defaultSettings ["walkthrough"])), "MenuDefaultButton")
                text " "
                label _("Walkthrough") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in toggleOptions.items ():
                    use Button (buttonLabel, SelectedIf (SetField (persistent, "walkthrough", varValue)))
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "pregnancy", defaultSettings ["pregnancy"])), "MenuDefaultButton")
                text " "
                label _("Contenido del embarazo") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in toggleOptions.items ():
                    use Button (buttonLabel, SelectedIf (SetField (persistent, "pregnancy", varValue)))
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "lactation", defaultSettings ["lactation"])), "MenuDefaultButton")
                text " "
                label _("Contenido de lactancia") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in toggleOptions.items ():
                    use Button (buttonLabel, SelectedIf (SetField (persistent, "lactation", varValue)))
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "urination", defaultSettings ["urination"])), "MenuDefaultButton")
                text " "
                label _("Fetiche de orina") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in toggleOptions.items ():
                    use Button (buttonLabel, SelectedIf (SetField (persistent, "urination", varValue)))
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "lesbian", defaultSettings ["lesbian"])), "MenuDefaultButton")
                text " "
                label _("Contenido lésbico") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in toggleOptions.items ():
                    use Button (buttonLabel, SelectedIf (SetField (persistent, "lesbian", varValue)))
        null
# Display, Rollback, Skip
        vbox:
            hbox:
                use Button (" ", Preference ("display", "fullscreen"), "MenuDefaultButton")
                text " "
                label _("Visualización de la pantalla") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in { _("Ventana") : "window", _("Pantalla completa") : "fullscreen" }.items ():
                    use Button (buttonLabel, Preference ("display", varValue))
        vbox:
            hbox:
                use Button (" ", Preference ("rollback side", "disable"), "MenuDefaultButton")
                text " "
                label _("Click para retroceder") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in { _("Deshabilitado") : "disable", _("Izquierdo") : "left", _("Derecho") : "right" }.items ():
                    use Button (buttonLabel, Preference ("rollback side", varValue))
        vbox:
            hbox:
                use Button (" ", [ SelectedIf (not preferences.skip_unseen and not preferences.skip_after_choices and not preferences.transitions), SetField (preferences, "skip_unseen", False), SetField (preferences, "skip_after_choices", False), SetField (preferences, "transitions", 0) ], "MenuDefaultButton")
                text " "
                label _("Saltar/Avance.A") style "MenuLabel"
            hbox style "MyDormBox":
                for buttonLabel, varValue in { _("No Visto") : "skip", _("D. de las opciones") : "after choices", _("Transiciones") : "transitions" }.items ():
                    use Button (buttonLabel, Preference (varValue, "toggle"))
# Audio settings
        vbox:
            hbox:
                use Button (" ", [ SelectedIf (preferences.get_volume ("music") == config.default_music_volume), Function (preferences.set_volume, "music", config.default_music_volume) ], "MenuDefaultButton")
                text " "
                label _("Volumen de la música") style "MenuLabel"
                text " "
                if config.has_music or config.has_sound or config.has_voice:
                    use Button (_("Silenciar todo"), Preference ("all mute", "toggle"), "MyDormButtonMute")
            hbox:
                python:
                    if preferences.get_mute ("music"):
                        barValue = 0
                        barText = _("silenciado")
                    else:
                        barValue = Preference ("music volume")
                        barText = toPercent (preferences.get_volume ("music"), "str")
                bar:
                    value barValue
                    style "SettingsBar"
                text barText style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", [ SelectedIf (preferences.get_volume ("sfx") == config.default_sfx_volume), Function (preferences.set_volume, "sfx", config.default_sfx_volume) ], "MenuDefaultButton")
                text " "
                label _("Volumen de sonido/SFX") style "MenuLabel"
            hbox:
                python:
                    if preferences.get_mute ("sfx"):
                        barValue = 0
                        barText = _("silenciado")
                    else:
                        barValue = Preference ("sound volume")
                        barText = toPercent (preferences.get_volume ("sfx"), "str")
                bar value barValue style "SettingsBar"
                text barText style "MenuSettingsValueText"
#        vbox:
#            hbox:
#                use Button (" ", [ SelectedIf (preferences.get_volume ("voice") == config.default_voice_volume), Function (preferences.set_volume, "voice", config.default_voice_volume) ], "MenuDefaultButton")
#                text " "
#                label _("Volumen de voz") style "MenuLabel"
#            hbox:
#                python:
#                    if preferences.get_mute ("voice"):
#                        barValue = 0
#                        barText = _("silenciado")
#                    else:
#                        barValue = Preference ("voice volume")
#                        barText = toPercent (preferences.get_volume ("voice"), "str")
#                bar value barValue style "SettingsBar"
#                text barText style "MenuSettingsValueText"

screen SettingsTabDialogue ():
    tag menu
    use Settings (MenuScreenBottomSettingsDialogue)
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottomSettingsDialogue, False)
# Settings content
    vpgrid style "MenuVPGrid":
        cols 3
        margin (marginLeft * 2, 0, marginRight * 2, 0)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
# General Text Settings
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (preferences, "text_cps", 40)), "MenuDefaultButton")
                text " "
                label _("Velocidad del texto")  style "MenuLabel"
            hbox:
                bar value Preference ("text speed")
                text str (int (preferences.text_cps)) style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (preferences, "afm_time", 15)), "MenuDefaultButton")
                text " "
                label _("Tiempo de avance automático")  style "MenuLabel"
            hbox:
                bar value Preference ("auto-forward time")
                text str (int (preferences.afm_time)) style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueBoxOpacity", defaultSettings ["dialogueBoxOpacity"])), "MenuDefaultButton")
                text " "
                label _("Opacidad del fondo del texto") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueBoxOpacity", range = 1.0, style = "slider")
                text toPercent (persistent.dialogueBoxOpacity, "str") style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueBoxHeight", defaultSettings ["dialogueBoxHeight"])), "MenuDefaultButton")
                text " "
                label _("Altura del cuadro de texto") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueBoxHeight", range = 500, style = "slider")
                text str (persistent.dialogueBoxHeight) + "px" style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueBoxWidth", defaultSettings ["dialogueBoxWidth"])), "MenuDefaultButton")
                text " "
                label _("Ancho del campo de texto") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueBoxWidth", range = 1900, style = "slider")
                text str (persistent.dialogueBoxWidth) + "px" style "MenuSettingsValueText"
        null height 20
# Actor Settings
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueWhoOutlineOpacity", defaultSettings ["dialogueWhoOutlineOpacity"])), "MenuDefaultButton")
                text " "
                label _("Contorno opacidad personaje") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueWhoOutlineOpacity", range = 1.0, style="slider")
                text toPercent (persistent.dialogueWhoOutlineOpacity, "str") style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueWhoOutlineThickness", defaultSettings ["dialogueWhoOutlineThickness"])), "MenuDefaultButton")
                text " "
                label _("Grosor del contorno personaje") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueWhoOutlineThickness", range = 5, style="slider")
                text "[persistent.dialogueWhoOutlineThickness]" style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueWhoSize", defaultSettings ["dialogueWhoSize"])), "MenuDefaultButton")
                text " "
                label _("Tamaño de fuente personaje") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueWhoSize", offset = WhoFontSizeMin, range = WhoFontSizeMax - WhoFontSizeMin, style="slider")
                text "[persistent.dialogueWhoSize]" style "MenuSettingsValueText"
# Actor's Text Settings
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueWhatOutlineOpacity", defaultSettings ["dialogueWhatOutlineOpacity"])), "MenuDefaultButton")
                text " "
                label _("Opacidad del contorno de texto") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueWhatOutlineOpacity", range = 1.0, style="slider")
                text toPercent (persistent.dialogueWhatOutlineOpacity, "str") style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueWhatOutlineThickness", defaultSettings ["dialogueWhatOutlineThickness"])), "MenuDefaultButton")
                text " "
                label _("Grosor del contorno de texto") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueWhatOutlineThickness", range = 5, style="slider")
                text "[persistent.dialogueWhatOutlineThickness]" style "MenuSettingsValueText"
        vbox:
            hbox:
                use Button (" ", SelectedIf (SetField (persistent, "dialogueWhatSize", defaultSettings ["dialogueWhatSize"])), "MenuDefaultButton")
                text " "
                label _("Tamaño de fuente de texto") style "MenuLabel"
            hbox:
                bar value FieldValue (persistent, "dialogueWhatSize", offset = WhatFontSizeMin, range = WhatFontSizeMax - WhatFontSizeMin, style="slider")
                text "[persistent.dialogueWhatSize]" style "MenuSettingsValueText"

# Preview window
#    use say (settingsDemoWho.name, settingsDemoWhat, MenuScreenBottomSettingsDialogue)
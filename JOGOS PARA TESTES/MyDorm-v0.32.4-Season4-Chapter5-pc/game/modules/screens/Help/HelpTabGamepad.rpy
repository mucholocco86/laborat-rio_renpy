screen HelpTabGamepad ():
    tag menu
    use Help ()
    python:
        marginLeft = getScreenDim (MenuScreenLeft)
        marginTop = getScreenDim (MenuScreenTop, False)
        marginRight = getScreenDim (MenuScreenRight)
        marginBottom = getScreenDim (MenuScreenBottom, False)
    vpgrid style "MenuVPGrid":
        cols 1
        margin (marginLeft * 2, 0, marginRight * 2)
        pos (marginLeft, marginTop)
        xspacing MenuGridSpacing
        yspacing MenuGridSpacing * 2
        xysize (1.0 - marginLeft - marginRight, 1.0 - marginTop - marginBottom)
        mousewheel True
        scrollbars "vertical"
        yfill True
        vbox:

            label _("Gatillo derecho A / Botón inferior") style "MenuLabel"
            text _("Avanza el diálogo y activa la interfaz.") style "MenuText"

            label _("Gatillo izquierdo / Botón superior izquierdo") style "MenuLabel"
            text _("Vuelve al diálogo anterior.") style "MenuText"

            label _("Botón superior derecho") style "MenuLabel"
            text _("Avanza al diálogo posterior.") style "MenuText"

            label _("Cruceta / Sticks") style "MenuLabel"
            text _("Navegar por la interfaz.") style "MenuText"

            label _("Inicio, Guía") style "MenuLabel"
            text _("Accede al menú del juego.") style "MenuText"

            label _("Botón Y / Botón superior") style "MenuLabel"
            text _("Oculta la interfaz de usuario.") style "MenuText"

            button:
                top_margin MenuLabelTopMargin
                action GamepadCalibrate ()
                style "MyDormButton"
                text _("Calibrar") style "MyDormButton_text"
            null height MenuLabelTextSize * 2
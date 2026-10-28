screen HelpTabMouse ():
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

            label _("Boton izquierdo del raton") style "MenuLabel"
            text _("Avanza el diálogo y activa la interfaz.") style "MenuText"

            label _("Botón central del ratón") style "MenuLabel"
            text _("Oculta la interfaz de usuario.") style "MenuText"

            label _("Botón derecho del ratón") style "MenuLabel"
            text _("Accede al menú del juego.") style "MenuText"

            label _("Rueda del ratón hacia arriba") style "MenuLabel"
            text _("Vuelve al diálogo anterior.") style "MenuText"

            label _("Rueda del ratón hacia abajo") style "MenuLabel"
            text _("Avanza al diálogo posterior.") style "MenuText"

            null height MenuLabelTextSize * 2
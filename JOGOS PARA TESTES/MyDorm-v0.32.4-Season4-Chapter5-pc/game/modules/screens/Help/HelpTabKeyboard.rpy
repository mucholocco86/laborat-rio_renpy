screen HelpTabKeyboard ():
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
            label _("Tecla enter") style "MenuLabel"
            text _("Avanza el diálogo y activa la interfaz.") style "MenuText"

            label _("Espacio") style "MenuLabel"
            text _("Avanza el diálogo sin seleccionar opciones.") style "MenuText"
            
            label _("Teclas de flecha") style "MenuLabel"
            text _("Navegar por la interfaz.") style "MenuText"

            label _("Tecla de escape") style "MenuLabel"
            text _("Accede al menú del juego.") style "MenuText"

            label _("Tecla de control") style "MenuLabel"
            text _("Salta el diálogo mientras se mantiene presionado.") style "MenuText"

            label _("Tecla de tabulación") style "MenuLabel"
            text _("Alterna el salto de diálogo.") style "MenuText"

            label _("Página arriba") style "MenuLabel"
            text _("Vuelve al diálogo anterior.") style "MenuText"

            label _("Página abajo") style "MenuLabel"
            text _("Avanza al diálogo posterior.") style "MenuText"

            label _("H") style "MenuLabel"
            text _("Oculta la interfaz de usuario.") style "MenuText"

            label _("S") style "MenuLabel"
            text _("Toma una captura de pantalla.") style "MenuText"

            label _("V") style "MenuLabel"
            text _("Alterna la asistencia {a=https://www.renpy.org/l/voicing}autovoicing{/a}.") style "MenuText"

            label _("Tecla de mayúsculas + A") style "MenuLabel"
            text _("Abre el menú de accesibilidad.") style "MenuText"

            if hasattr (config, "console"):
                label _("Mayúsculas + O") style "MenuLabel"
                text _("Abre la consola.") style "MenuText"

            if hasattr (config, "developer"):
                label _("Mayúsculas + D") style "MenuLabel"
                text _("Abre las herramientas de desarrollador.") style "MenuText"
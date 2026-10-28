init -100 python:
    tooltipTexts = { "MainMenu" : {}, "QuickMenu" : {} }
    tooltipTexts ["QuickMenu"].update ({
        _("Atrás") :            [ "B",  _("Retroceder una línea de diálogo.") ],
        _("Adelante") :         [ "N",  _("Avanzar una línea de diálogo.") ],
        _("Adelante A.") :      [ "",   _("Avanzar automáticamente el diálogo. El tiempo de avance depende de la configuración del diálogo.") ],
        _("Saltar") :           [ "",   _("Omitir el diálogo hasta que se requiera la interacción del jugador.") ],
        _("Historial") :        [ "J",  _("Abrir historial de diálogo.") ],
        _("Guardar R.") :       [ "",   _("Guardar el juego en una ranura de guardado rápido.") ],
        _("Guardar") :          [ _("Botón derecho del mouse"),   _("Abrir la selección de guardar juego para guardar su progreso.") ],
        _("Cargar") :           [ "L",  _("Abrir la selección de guardar juego para cargar un juego anterior.") ],
        _("Cargar R.") :        [ "",   _("Cargue el último guardado rápido.") ],
        _("Configuración") :    [ "Tecla de escape",    _("Abrir la pantalla de configuración.") ],
        _("Biografías") :       [ "P",  _("Lee biografías de personajes o cambia nombres y opciones de juego.") ],
        _("Salir") :            [ "Q",  _("Salir de la aplicación.") ]
    })
    tooltipTexts ["MainMenu"].update ({
        _("Nuevo juego") :      [ "",   _("Comenzar un nuevo juego desde el principio.") ],
        _("Menú principal") :   [ "",   _("Volver al menú principal. Todo el progreso no guardado se perderá.") ],
        _("Guardar") :          [ "",   _("Abrir la selección de guardar juego para guardar su progreso.") ],
        _("Cargar") :           [ "",   _("Abrir la selección de guardar juego para cargar un juego anterior.") ],
        _("Configuración") :    [ "",   _("Abrir la pantalla de configuración.") ],
        _("General") :          [ "",   _("Cambiar la configuración general del juego.") ],
        _("Menú") :             [ "",   _("Cambiar cómo se muestra el menú o lo que se muestra en el menú rápido.") ],
        _("Diálogo") :          [ "",   _("Configuraciones para cambiar la apariencia del cuadro de diálogo y las opciones.") ],
        _("Acerca de") :        [ "",   _("Información sobre el juego y su desarrollo.") ],
        _("Ayuda") :            [ "",   _("Información útil sobre las teclas de acceso rápido utilizadas en este juego.") ],
        _("Mando de juegos") :  [ "",   _("Ver cómo navegar por el juego con un gamepad o calibrar su dispositivo de entrada.") ],
        _("Teclado") :          [ "",   _("Ver qué teclas de acceso rápido están disponibles para el juego.") ],
        _("Ratón") :            [ "",   _("Información sobre cómo navegar por el juego con el ratón.") ],
        _("Borrar") :           [ "",   _("Eliminar esta partida guardada de tu dispositivo.") ],
        _("Rebautizar") :       [ "",   _("Darle un nuevo nombre a tu partida guardada.") ]
    })
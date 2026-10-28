init -99 python:
    Decisions ["Martha"] = {
        0 : ("route",               _("Relación"),          _("Estás en una relación con [mar]")),
        1 : ("fittingRoom",         _("Voyeur"),            _("Estabas espiando a [mar] en el probador")),
        2 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [mar] lo antes posible."),  "route"),
        3 : ("lewd",                _("Nombre lascivo"),    "LewdInputTrigger",                                         "route"),
        4 : ("pregnant",            _("Embarazada"),        _("[mar] está embarazada"),                                 "route"),
        5 : ("anal",                "Anal",                 _("Anal activado con [mar]"),                               "analChance")
    }

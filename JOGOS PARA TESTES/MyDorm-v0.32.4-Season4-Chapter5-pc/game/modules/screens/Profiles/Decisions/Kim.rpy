init -99 python:
    Decisions ["Kim"] = {
        0 : ("rp",      _("Puntos de relación"),    "RPTrigger"),
        1 : ("makeup",  _("Usando maquillaje"),     _("Animaste a [kim] a ocultar su vitíligo. Esto hizo que perdieras puntos de relación con ella y los demás estudiantes.")),
        2 : ("route",               _("Relación"),          _("Estás en una relación con [kim]"), "chanceRoute"),
        3 : ("saved",               _("Salvar al soldado [kim]"),          _("Salvaste a [kim] en el barco de Ichigo"), "chanceSaved"),
        4 : ("pregnant",            _("Embarazada"),        _("[kim] está embarazada."),                                                "route"),

    }

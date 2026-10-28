init -99 python:
    Decisions ["Alexia"] = {
        0 : ("route",               _("Relación"),          _("Estás en una relación con [oma]")),
        1 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [oma] lo antes posible."),  "route"),
        2 : ("pregnant",            _("Embarazada"),        _("[oma] está embarazada"),                                 "route"),
    }
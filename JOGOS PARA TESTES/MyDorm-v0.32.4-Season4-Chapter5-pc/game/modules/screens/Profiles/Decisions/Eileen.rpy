init -99 python:
    Decisions ["Eileen"] = {
        0 : ("route",               _("Relación"),          _("Estás en una relación con [eil]")),
        1 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [eil] lo antes posible."),  "route"),
        2 : ("pregnant",            _("Embarazada"),          _("[eil] está embarazada"),                                 "route"),
    }
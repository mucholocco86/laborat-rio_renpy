init -99 python:
    Decisions ["Saira"] = {
        0 : ("route",               _("Relación"),          _("Estás en una relación con [sai]")),
        1 : ("routeSecondChance",   _("2da oportunidad"),   _("No besaste a [sai] en el aeropuerto."),  "route"),
        2 : ("pregnant",    _("Embarazada"),    _("[sai] está embarazada"),             "route"),
    }

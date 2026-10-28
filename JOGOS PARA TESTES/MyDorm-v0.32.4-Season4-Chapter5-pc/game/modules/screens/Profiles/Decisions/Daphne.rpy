init -99 python:
    Decisions ["Daphne"] = {
        0 : ("breakup",             _("Romper"),            _("Terminaste tu relación con [dap]")),
        1 : ("route",               _("Relación"),          _("Estás en una relación con [dap]")),
        2 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [dap] lo antes posible."),      "route"),
        3 : ("romance",             _("Romance"),           _("Seguiste la ruta romántica con [dap], sin corromperla."),    "route"),
        4 : ("pregnant",            _("Embarazada"),        _("[dap] está embarazada"),                                     "route"),
    }
init -99 python:
    Decisions ["Norah"] = {
        0 : ("route",               _("Relación"),          _("Estás en una relación con [nor]")),
        1 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [nor] lo antes posible."),  "route"),
        2 : ("pregnant",            _("Embarazada"),        _("[nor] está embarazada"),                                 "route"),
        3 : ("anal",                _("Anal"),              _("Anal activado con [nor]."),                              "route"),
    }

init -99 python:
    Decisions ["Samantha"] = {
        0 : ("breakup",             _("Romper"),            _("Terminaste tu relación con [sam].")),
        1 : ("route",               _("Relación"),          _("Estás en una relación con [sam].")),
        2 : ("massage",             _("Masaje"),            _("Le dijiste a [sam] que la reacción de tu cuerpo cuando te masajeó no fue aleatoria.")),
        3 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [sam] lo antes posible."),  "route"),
        4 : ("naturalPubicHair",    _("Pelo natural"),      _("El vello púbico de [sam] será indomable."),              "route"),
        5 : ("pregnant",            _("Embarazada"),        _("[sam] está embarazada."),                                "route"),
    }

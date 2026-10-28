init -99 python:
    Decisions ["Lisa"] = {
        0 : ("rp",          _("Puntos de relación"),        "RPTrigger"),
        1 : ("hug",         _("Un abrazo tranquilizador"),  _("Para calmar a [lis] le diste un abrazo.")),
        2 : ("escorted",    _("Se un caballero"),           _("Le ofreciste a [lis] acompañarla para que se sintiera más segura.")),
        3 : ("route",               _("Relación"),          _("Estás en una relación con [lis]")),
        4 : ("pregnant",            _("Embarazada"),        _("[lis] está embarazada."),                                                "route"),
        5 : ("anal",            _("Anal"),        _("Anal activado con [lis]."),                                                "route"),
    }

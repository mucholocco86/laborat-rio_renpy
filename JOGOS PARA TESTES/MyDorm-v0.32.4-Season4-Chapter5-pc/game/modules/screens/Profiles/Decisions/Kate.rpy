init -99 python:
    Decisions ["Kate"] = {
        0 : ("rp",              _("Puntos de relación"),    "RPTrigger"),
        1 : ("lesbianContent",  _("Contenido lésbico"),     _("[kat] puede unirse a tríos y más.")),
        2 : ("slim",            _("[kat] delgada"),         _("Convenciste a [kat] para que hiciera más ejercicio y comiera más sano.")),
        3 : ("route",           _("Relación"),              _("Estás en una relación con [kat].") , "chanceRoute"),
        4 : ("pregnant",        _("Embarazada"),            _("[kat] está embarazada.") , "route"),
        5 : ("foodplay",        _("Juego con Comida"),      _("Dejaste que [kat] se comiera el chocolate.") , "route"),
        6 : ("cumswap",         _("Beso blanco"),              _("Besaste a [kat] después de que ella probara el sabor de tu semen.") , "route"),
    }

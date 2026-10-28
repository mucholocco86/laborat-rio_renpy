init -99 python:
    Decisions ["Deborah"] = {
        0 : ("rp",      _("Puntos de relación"),    "RPTrigger"),
        1 : ("laptop",  _("Computadora portátil"),  _("Le dijiste a [deb] que no se preocupara por la computadora portátil, ya que podía tomar prestada la tuya.")),
        2 : ("route",               _("Relación"),          _("Estás en una relación con [deb]")),
        3 : ("pregnant",            _("Embarazada"),        _("[deb.nick] está embarazada."), "route"), 
    }

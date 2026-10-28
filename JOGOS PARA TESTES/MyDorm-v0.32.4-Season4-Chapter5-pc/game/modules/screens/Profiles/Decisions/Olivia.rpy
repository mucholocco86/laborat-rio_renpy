init -99 python:
    Decisions ["Olivia"] = {
        0 : ("mcKnowsSickness", _("Sabe sobre enfermedad"), _("[mc] sabe sobre la enfermedad de [mee]")),
        1 : ("route",               _("Relación"),          _("Estás en una relación con [mee]")),
        2 : ("iceCream",            _("Helado"),            _("Comerás helado hecho con leche materna"), "chanceIceCream"),
    }

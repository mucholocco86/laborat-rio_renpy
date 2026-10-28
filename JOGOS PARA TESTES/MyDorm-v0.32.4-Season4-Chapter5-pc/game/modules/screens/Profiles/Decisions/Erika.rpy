init -99 python:
    Decisions ["Erika"] = {
        0 : ("route",               _("Relación"),              _("Estás en una relación con [eri]")),
        1 : ("routeSecondChance",   _("2da oportunidad"),       _("No empezaste tu relación con [eri] lo antes posible."),                  "route"),
        2 : ("routeThirdChance",    _("3ra oportunidad"),       _("Comenzaste tu relación con [eri] en la última oportunidad posible."),    "route"),
        3 : ("broughtToWorkOnDay6", _("Acompañado al trabajo"), _("El día 6 acompañaste a [eri] al trabajo."),                              "route"),
        4 : ("pregnant",            _("Embarazada"),            _("[eri] está embarazada."),                                                "route"),
        5 : ("knowsNorahPregnancy", _("El embarazo de [nor]"),  _("[eri] sabe del embarazo de [nor]."),                                     "route"),
    }
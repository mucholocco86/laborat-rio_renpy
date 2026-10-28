init -99 python:
    Decisions ["Madison"] = {
        0 : ("route",       _("Relación"),              _("Estás en una relación con [mad]")),
        1 : ("romance",     _("Romance"),               _("Tienes una relación romántica con [mad]"),   "route"),
        2 : ("dom",         _("[mad] dominante"),       _("Eres sumiso a [mad]"),                       "route"),
        3 : ("sub",         _("Sumisa [mad]"),          _("[mad] es sumisa contigo."),                  "route"),
        4 : ("pregnant",    _("Embarazada"),            _("[mad] está embarazada"),                     "route"),
        5 : ("fart",        _("Pedo"),                  _("Te tiraste un pedo delante de [mad.nick]"),  "chanceFart")
    }

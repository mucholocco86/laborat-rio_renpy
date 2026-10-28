init -99 python:
    Decisions ["Emma"] = {
        0 : ("chat",                _("Chat"),              _("Hablaste con [emm] sobre los besos después de la fiesta de \"The Twins\" el día 4.")),
        1 : ("route",               _("Relación"),          _("Estás en una relación con [emm]")),
        2 : ("routeSecondChance",   _("2da oportunidad"),   _("No empezaste tu relación con [emm] lo antes posible."),  "route"),
        3 : ("help",                _("Voyeur"),            _("Ayudaste a [emm] a masturbarse cuando ella vino a dormir a tu cama.")),
        4 : ("pregnant",            _("Embarazada"),        _("[emm] está embarazada"),                                 "route"),
        5 : ("reggaeton",           _("Nombre lascivo para MC"), "MCLewdInputTrigger",                                  "route"),
        6 : ("anal",                _("Contenido anal"),    _("Contenido anal habilitado para [emm]"),                  "route"),
        7 : ("plug",                _("Juego anal"),        _("Plug play habilitado para [emm]"),                       "route"),
        8 : ("spanking",            _("Azotaina"),          _("Contenido de nalgadas habilitado para [emm]"),           "route"),
        9 : ("hadAnal",             _("Sexo Anal"),         _("Tuviste sexo anal con [emm] durante el sexo grupal"),    "foursome")
    }

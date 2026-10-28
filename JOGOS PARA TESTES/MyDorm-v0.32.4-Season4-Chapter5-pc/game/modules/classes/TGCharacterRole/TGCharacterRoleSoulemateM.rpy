init 5 python:
    class TGCharacterRoleSoulmateM (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("compañero de vida")
            self.longPlural = _("compañeros de vida")
            self.short = _("compañerito de vida")
            self.shortPlural = _("compañeritos de vida")
            self.nick = _("compañerito de vida")
            self.nickPlural = _("compañeritos de vida")
init 5 python:
    class TGCharacterRoleSoulmateF (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("compañera de vida")
            self.longPlural = _("compañeras de vida")
            self.short = _("compañerita de vida")
            self.shortPlural = _("compañeritas de vida")
            self.nick = _("compañerita de vida")
            self.nickPlural = _("compañeritas de vida")
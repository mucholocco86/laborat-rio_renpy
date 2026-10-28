init 5 python:
    class TGCharacterRoleHousemateF (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("compañera de piso")
            self.longPlural = _("compañeras de piso")
            self.short = _("compañerita de piso")
            self.shortPlural = _("compañeritas de piso")
            self.nick = _("compañerita de piso")
            self.nickPlural = _("compañeritas de piso")
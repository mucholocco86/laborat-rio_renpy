init 5 python:
    class TGCharacterRoleHousemateM (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("compañero de piso")
            self.longPlural = _("compañeros de piso")
            self.short = _("compañerito de piso")
            self.shortPlural = _("compañeritos de piso")
            self.nick = _("compañerito de piso")
            self.nickPlural = _("compañeritos de piso")
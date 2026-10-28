init 5 python:
    class TGCharacterRoleRoommateM (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("compañero de cuarto")
            self.longPlural = _("compañeros de cuarto")
            self.short = _("compañerito de cuarto")
            self.shortPlural = _("compañeritos de cuarto")
            self.nick = _("compañerito de cuarto")
            self.nickPlural = _("compañeritos de cuarto")
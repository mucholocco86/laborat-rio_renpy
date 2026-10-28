init 5 python:
    class TGCharacterRoleRoommateF (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("compañera de cuarto")
            self.longPlural = _("compañeras de cuarto")
            self.short = _("compañerita de cuarto")
            self.shortPlural = _("compañeritas de cuarto")
            self.nick = _("compañerita de cuarto")
            self.nickPlural = _("compañeritas de cuarto")
init 5 python:
    class TGCharacterRoleGrandaunt (TGCharacterRole):
        def __init__ (self):
            super ().__init__ ()
            self.long = _("tía abuela")
            self.longPlural = _("tía abuelas")
            self.short = _("tía abuela")
            self.shortPlural = _("tía abuelas")
            self.nick = _("tía abuela")
            self.nickPlural = _("tía abuelas")
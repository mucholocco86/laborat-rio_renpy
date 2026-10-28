init 5 python:
    class TGCharacterRoleCustom (TGCharacterRole):
        def __init__ (self, long = "", longPlural = "", short = "", shortPlural = "", nick = "", nickPlural = ""):
            empty = [ None, "" ]
            super ().__init__ ()
            self.long = long
            if longPlural in empty:
                longPlural = long
            self.longPlural = longPlural
            if short in empty:
                short = long
            self.short = short
            if shortPlural in empty:
                shortPlural = longPlural
            self.shortPlural = shortPlural
            if nick in empty:
                nick = short
            self.nick = nick
            if nickPlural in empty:
                nickPlural = shortPlural
            self.nickPlural = nickPlural
init python:
    class TGCharacterRole ():

        def __add__ (self, other):  return str (self) + str (other)
        def __str__ (self): return self.long

        def __delLong (self):   self.__long = ""
        def __getLong (self):   return self.__long
        def __setLong (self, newValue):
            if isinstance (newValue, str):  self.__long = newValue
            else:                           self.__long = ""
        long = property (__getLong, __setLong, __delLong, "Long version of the role. I.e. 'mother'")
        l = long

        def __getLongUpper (self):  return self.long.title ()
        upper = property (__getLongUpper, None, None, "Long uppercase version of the role. I.e. 'Mother'")
        longUpper   = upper
        longupper   = upper
        upperLong   = upper
        upperlong   = upper
        u           = upper
        lu          = upper
        ul          = upper

        def __delNick (self):   self.__nick = ""
        def __getNick (self):   return self.__nick
        def __setNick (self, newValue):
            if isinstance (newValue, str):  self.__nick = newValue
            else:                           self.__nick = ""
        nick = property (__getNick, __setNick, __delNick, "nick version of the role. I.e. 'mommy'")
        n = nick

        def __delNickPlural (self): self.__nickPlural = ""
        def __getNickPlural (self): return self.__nickPlural
        def __setNickPlural (self, newValue):
            if isinstance (newValue, str):  self.__nickPlural = newValue
            else:                           self.__nickPlural = ""
        nickPlural  = property (__getNickPlural, __setNickPlural, __delNickPlural, "Plural nick version of the role. I.e. 'mommies'")
        pluralnick  = nickPlural
        pn          = nickPlural
        np          = nickPlural

        def __getNickPluralUpper (self):  return self.nickPlural.title ()
        nickPluralUpper = property (__getNickPluralUpper, None, None, "Plural nick uppercase version of the role. I.e. 'Mommies'")
        nickpluralupper = nickPluralUpper
        nickUpperPlural = nickPluralUpper
        nickupperplural = nickPluralUpper
        pluralNickUpper = nickPluralUpper
        pluralnickupper = nickPluralUpper
        pluralUpperNick = nickPluralUpper
        pluraluppernick = nickPluralUpper
        upperNickPlural = nickPluralUpper
        uppernickplural = nickPluralUpper
        upperPluralNick = nickPluralUpper
        upperpluralnick = nickPluralUpper
        npu             = nickPluralUpper
        nup             = nickPluralUpper
        pnu             = nickPluralUpper
        pun             = nickPluralUpper
        unp             = nickPluralUpper
        upn             = nickPluralUpper

        def __getNickUpper (self):  return self.nick.title ()
        nickUpper   = property (__getNickUpper, None, None, "Short version of the role. I.e. 'Mommy'")
        nickupper   = nickUpper
        upperNick   = nickUpper
        uppernick   = nickUpper
        nu          = nickUpper
        un          = nickUpper

        def __delPlural (self): self.__longPlural = ""
        def __getPlural (self): return self.__longPlural
        def __setPlural (self, newValue):
            if isinstance (newValue, str):  self.__longPlural = newValue
            else:                           self.__longPlural = ""
        plural = property (__getPlural, __setPlural, __delPlural, "Plural version of the role. I.e. 'mothers'")
        p = plural

        def __getPluralUpper (self):  return self.plural.title ()
        pluralUpper = property (__getPluralUpper, None, None, "Short version of the role. I.e. 'Mothers'")
        pluralupper = pluralUpper
        upperPlural = pluralUpper
        upperplural = pluralUpper
        pu          = pluralUpper
        up          = pluralUpper

        def __delShort (self):  self.__short = ""
        def __getShort (self):  return self.__short
        def __setShort (self, newValue):
            if isinstance (newValue, str):  self.__short = newValue
            else:                           self.__short = ""
        short = property (__getShort, __setShort, __delShort, "Short version of the role. I.e. 'mom'")
        s = short

        def __delShortPlural (self):    self.__shortPlural = ""
        def __getShortPlural (self):    return self.__shortPlural
        def __setShortPlural (self, newValue):
            if isinstance (newValue, str):  self.__shortPlural = newValue
            else:                           self.__shortPlural = ""
        shortPlural = property (__getShortPlural, __setShortPlural, __delShortPlural, "Plural version of the role. I.e. 'moms'")
        shortplural = shortPlural
        pluralShort = shortPlural
        pluralshort = shortPlural
        ps          = shortPlural
        sp          = shortPlural

        def __getShortPluralUpper (self):  return self.shortPlural.title ()
        shortPluralUpper    = property (__getShortPluralUpper, None, None, "Short plural uppercase version of the role. I.e. 'Moms'")
        shortpluralupper    = shortPluralUpper
        shortUpperPlural    = shortPluralUpper
        shortupperplural    = shortPluralUpper
        pluralShortUpper    = shortPluralUpper
        pluralshortupper    = shortPluralUpper
        pluralUpperShort    = shortPluralUpper
        pluraluppershort    = shortPluralUpper
        upperShortPlural    = shortPluralUpper
        uppershortplural    = shortPluralUpper
        upperPluralShort    = shortPluralUpper
        upperpluralshort    = shortPluralUpper
        spu                 = shortPluralUpper
        sup                 = shortPluralUpper
        psu                 = shortPluralUpper
        pus                 = shortPluralUpper
        usp                 = shortPluralUpper
        ups                 = shortPluralUpper

        def __getShortUpper (self):  return self.short.title ()
        shortUpper  = property (__getShortUpper, None, None, "Short version of the role. I.e. 'Mom'")
        shortupper  = shortUpper
        upperShort  = shortUpper
        uppershort  = shortUpper
        su          = shortUpper
        usp         = shortUpper

        def __getLower (self): return self.long.lower ()
        lower  = property (__getLower, None, None, "Short version of the role. I.e. 'Mom'")
    
        def title (self): return self.longUpper
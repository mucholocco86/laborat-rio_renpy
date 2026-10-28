init 5 python:
    class TGCharacterName ():

        def __init__ (self, parent, who, surname="", nick="", mcSName = "", lewd="", mc="", mcLewd=""):
            self.__defaultName = str (who)  # the default name of the character, will be used if the name is set to "" or deleted
            self.__defaultNick = str (nick) # the default name of the character, will be used if the name is set to "" or deleted
            self.__parent = parent
            self.name = str (who)           # what is this character called
            self.surname = surname          # what is this characteres family name?
            self.nick = nick                # what is this character called by people, when not using their name or role
            self.mcSName = mcSName          # what is this character called by the MC on a regular basis
            self.lewd = lewd                # what is this character called by the MC while being lewd
            self.mc = mc                    # what is the MC called regularly, if this character doesn't use his name, role or lewd name
            self.mcLewd = mcLewd            # what is the MC called while being lewd

        def __add__ (self, other):  return str (self) + str (other)
        def __set__ (self, other):  self.firstname = str (other)
        def __str__ (self):         return self.firstname

        def __getDefaultName (self): return str (self.__defaultName)
        defaultName = property (__getDefaultName, None, None, "Returns the original name of the character")

        def __delName (self):   self.name = ""
        def __getName (self):
#            if self.__parent.useNick:
            if self.__parent._var ("uses nick"):
                return self.nick.title ()
            return self.__name
        def __setName (self, newValue):
            if self.__defaultName != newValue:
                self.nick = newValue
            else:
                self.nick = self.__defaultNick
            if not isinstance (newValue, str):  newValue = ""
            newValue = newValue.strip ()
            if newValue == "":  newValue = self.__defaultName
            self.__name = newValue
        name        = property (__getName, __setName, __delName, "What is this character called?")
        forename    = name
        firstname   = name
        first_name  = name
        first       = name
        f           = name

        def __getRealName (self):
            return self.__name
        realName    = property (__getRealName, None, None, "The real first name, without check for nickname!")
        rname       = realName
        nameNotNick = realName
        fname       = realName

        def __delSurname (self):    self.surname = ""
        def __getSurname (self):    return self.__surname
        def __setSurame (self, newValue):
            if not isinstance (newValue, str):  newValue = ""
            newValue = newValue.strip ()
            self.__surname = newValue
        surname     = property (__getSurname, __setSurame, __delSurname, "What is this characteres family name?")
        familyname  = surname
        lastname    = surname
        last_name   = surname
        last        = surname
        lname       = surname
        l           = surname

        def __delNickname (self):   self.nick = ""
        def __getNickname (self):   return self.__nick if self.__nick else self.__name
        def __setNickname (self, newValue):
            if not isinstance (newValue, str):  newValue = ""
            newValue = newValue.strip ()
            self.__nick = newValue.title ()
        nick        = property (__getNickname, __setNickname, __delNickname, "What is this character called by people, when not using their name or role?")
        nickname    = nick
        nick_name   = nick
        n           = nick

        def __delLewdname (self):   self.lewd = ""
        def __getLewdname (self):   return self.__lewd if self.__lewd else self.name
        def __setLewdname (self, newValue):
            if not isinstance (newValue, str):  newValue = ""
            #self.__lewd = newValue.title ()
            self.__lewd = newValue
        lewd        = property (__getLewdname, __setLewdname, __delLewdname, "What is this character called by the MC while being lewd?")
        lewdname    = lewd
        l           = lewd

        def __delMCName (self):   self.mcName = ""
        def __getMCName (self):   return self.__mcName
        def __setMCName (self, newValue):
            if (not isinstance (newValue, str) or newValue == "") and "mc" in globals ():
                if isinstance (globals ()["mc"], TGCharacter):
                    newValue = str (globals ()["mc"].name)
            if not isinstance (newValue, str) or newValue == "":
                newValue = ""
            #self.__mcName = newValue.title ()
            self.__mcName = newValue
        mcName      = property (__getMCName, __setMCName, __delMCName, "What is the MC called regularly, if this character doesn't use his name, role or lewd name?")
        mcname      = mcName
        mc_name     = mcName
        mc          = mcName

        def __delMCLewdName (self):   self.mcLewdName = ""
        def __getMCLewdName (self):   return self.__mcLewdName
        def __setMCLewdName (self, newValue):
            if not isinstance (newValue, str):  newValue = ""
            #self.__mcLewdName = newValue.title ()
            self.__mcLewdName = newValue
        mcLewdName      = property (__getMCLewdName, __setMCLewdName, __delMCLewdName, "What is the MC called while being lewd?")
        mclewdname      = mcLewdName
        mc_lewdname     = mcLewdName
        mcLewd          = mcLewdName
        mclewd          = mcLewdName
        mc_lewd         = mcLewdName
        mcl             = mcLewdName
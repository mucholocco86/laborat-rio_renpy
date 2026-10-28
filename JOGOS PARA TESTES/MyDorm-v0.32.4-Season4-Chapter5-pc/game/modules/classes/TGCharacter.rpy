init 15 python:
    class TGCharacter (ADVCharacter):

        # default relationship points every character starts with
        # also the value it will default back to if attribute is deleted
        ___rpDefault = 0
        # min/max for relationship points
        # if this is set to None, min/max will be ignored; DO NOT set to 0 if you want this setting to be ignored!
        # else if relationship points go below/above min/max, they will be set to this value
        ___rpMaximum = None
        ___rpMinimum = None

        __cumInsideForPregnancy = 3 # currently not in use; will be used in a proper… property

        defaultNames = { }
        defaultNicks = { }

        def __init__ (self, who=renpy.character.NotSet, kind=None, **properties):
            ADVCharacter.__init__ (self, str (who), kind=kind, **properties)
            self.__variables = {
                "bool" : [],
                "int" :  {},
                "str" :  {}
            }
            self.__defaultName = who
            # properties not handled by ADVCharacter
            # default values for default/min/max relationship points of the character
            self.__rpDefault = self.___rpDefault if not "rpMinimum" in properties else properties ["rpDefault"]
            self.__rpMinimum = self.___rpMinimum if not "rpMinimum" in properties else properties ["rpMinimum"]
            self.__rpMaximum = self.___rpMaximum if not "rpMaximum" in properties else properties ["rpMaximum"]
            if "isMC" in properties:                self._var ("isMC", properties ["isMC"], intention = "set")
            if "color" in properties:               self.color = properties ["color"]
            elif "colour" in properties:            self.color = properties ["colour"]
            if "familyname" in properties:          surname = properties ["familyname"]
            elif "family_name" in properties:       surname = properties ["family_name"]
            elif "lastname" in properties:          surname = properties ["lastname"]
            elif "last_name" in properties:         surname = properties ["last_name"]
            elif "lname" in properties:             surname = properties ["lname"]
            elif "surname" in properties:           surname = properties ["surname"]
            else:                                   surname = None
            if "nick" in properties:                nick = properties ["nick"]
            elif "nickname" in properties:          nick = properties ["nickname"]
            else:                                   nick = None
            if "isFamily" in properties:            self.isSeenAsFamily = True
            else:                                   self.isSeenAsFamily = False
            if "lewd" in properties:                lewd = properties ["lewd"]
            elif "lewdname" in properties:          lewd = properties ["lewdname"]
            elif "lewd_name" in properties:         lewd = properties ["lewd_name"]
            else:                                   lewd = None
            if "mc" in properties:                  mc = properties ["mc"]
            elif "mcname" in properties:            mc = properties ["mcname"]
            elif "mc_name" in properties:           mc = properties ["mc_name"]
            else:                                   mc = None
            if "mclewd" in properties:              mcLewd = properties ["mclewd"]
            elif "mcLewd" in properties:            mcLewd = properties ["mcLewd"]
            elif "mc_lewd" in properties:           mcLewd = properties ["mc_lewd"]
            else:                                   mcLewd = None
            if "desc" in properties:                properties.update ({ "description" : properties ["desc"] }) # if there is a short property alternative, catch them here
            if "description" in properties:         self.description = properties ["description"]
            else:                                   del self.description
            if "role" in properties:                role = properties ["role"]
            else:                                   role = ""
            useNick = False
            if "usesNick" in properties:            useNick = properties ["usesNick"]
            elif "useNick" in properties:           useNick = properties ["useNick"]
            self.useNick    = useNick
            pregnant = False
            if "preg" in properties:                pregnant = properties ["preg"]
            if "pregnancy" in properties:           pregnant = properties ["pregnancy"]
            if "pregnant" in properties:            pregnant = properties ["pregnant"]
            self._var ("pregnant", pregnant, "set")
            if "rp" in properties:                      rp = properties ["rp"]
            elif "relationshipPoints" in properties:    rp = properties ["relationshipPoints"]
            else:                                       rp = self.__rpDefault
            self.rp (rp)
            self.name = TGCharacterName (self, who, surname, nick, lewd, mc, mcLewd)
            self.roles = TGCharacterRoles ()
            self.role = role
            if not self._var ("isMC"):
                self.relmc = ""
                self.rel = ""
            self.profilePicture = self.name.lname + "_" + self.name.fname
            self.profileImages = []
            self.defaultProfileImageIndex = 0

        def __str__ (self): return str (self.name.first_name)

### Properties for the character
# _delX set to some kind of default value
# _getX just return the value
# handle faulty values or set to valid values
# Be the good coder and DON'T call the "private" properties directly!
# Have short alternative properties like "desc"/"preg" for "decription"/"pregnant"

# Who color, in case we need it for a "Thought Character"
        def __delColor (self):              self.__color = None
        def __getColor (self):              return self.__color
        def __setColor (self, value):
            if isinstance (value, str):
                if value.startswith ("#"):
                    value = value [1:]
                if len (value) == 3:
                    fullValue = ""
                    for index in range (0,3):
                        for jndex in range (0, 2):
                            fullValue += value [index]
                    if fullValue != "":
                        value = fullValue
                value = "#" + value

        def initProfileImages (self):
            if not getattr (self, "profileImages", None): self.profileImages = []

        def addProfileImage (self, imageName, imageFilter = None):
            self.initProfileImages ()
            self.profileImages.append ((imageName, imageFilter))
        
        def isProfileImageAvailable (self, imageName):
            for profileImage, profileImageFilter in self.profileImages:
                if profileImage == imageName:
                    if profileImageFilter is None:
                        return True
                    if isinstance (profileImageFilter, str):
                        return bool (self._var (profileImageFilter))
                    elif isinstance (profileImageFilter, list):
                        isAvailable = True
                        for imageFilter in profileImageFilter:
                            isAvailable = isAvailable and bool (self._var (imageFilter))
                        return isAvailable
            return False
    
        def isProfileImageIndexAvailable(self, imageIndex):
            if not self.profileImages or imageIndex < 0 or imageIndex >= len(self.profileImages):
                return False
            return self.isProfileImageAvailable(self.profileImages[imageIndex][0])

# Original name of the character
        def __getDefaultName (self):    return self.name.defaultName
        defaultName = property (__getDefaultName, None, None, "Return original name of the character")
        dn = defaultName

# Character Descriptions
        def __delDescription (self):            self.__description = None
        def __getDescription (self):            return self.__description
        def __setDescription (self, value):
            if value == None or value == "":    del self.description
            elif isinstance (value, str):       self.__description = value
        description = property (__getDescription, __setDescription, __delDescription, "A description of the character")
        desc        = description

# Name properties
        def __getCalledByMC (self):
            if persistent.family and self.isSeenAsFamily:
                return self.name.mcSName         # e.g. Mamá or Hermana; role s .. short; u .. uppercase
            else:
                return self.name.first_name # just the name
        calledByMC  = property(__getCalledByMC, None, None, "Used in dialogue by MC talking to parents/siblings or children talking to parents")
        byMC        = calledByMC            # only use if applicable, like don't use with Em but only with Martha *lol*
        bymc        = calledByMC
        mc          = calledByMC

        def setLewdName (self, newValue): self.name.lewd = str (newValue)
        def setMCLewdName (self, newValue): self.name.mcLewd = str (newValue)

        def __delNickname (self):               del self.name.nick
        def __getNickname (self):               return self.name.nick
        def __setNickname (self, value):
            if value == None or value == "":    del self.nick
            elif isinstance (value, str):       self.name.nick = str (value)
        nickname = property(__getNickname, __setNickname, __delNickname)
        nick    = nickname
        n       = nickname

        def setName (self, newName):
            if isinstance (newName, str):
                self.name.first_name = newName

# is this the Main Character
        def __delIsMainCharacter (self):    self.isMC = False
        def __getIsMainCharacter (self):    return self.__isMC
        def __setIsMainCharacter (self, value):
            if isinstance (value, int):     value = True if value > 0 else False
            elif value == "True":           value = True
            if isinstance (value, bool):    self.__isMC = value
            else:                           del self.isMC
        isMainCharacter = property (__getIsMainCharacter, __setIsMainCharacter, __delIsMainCharacter, "bool value to determine if this character is the MC")
        isMC = isMainCharacter

        def __getRole (self):   return self.roles.role
        def __setRole (self, value):
            self.roles.addRole (value, True)
        role = property (__getRole, __setRole, None, "Get primary role or add a new role")

        def __getRoleShortUpper (self): return self.roles.role.su
        rsu = property (__getRoleShortUpper, None, None, "Get primary role in short form uppercase.")

# Pregnancy stuff
        def __delPregnancy (self):          self._var ("pregnant", False)
        def __getPregnancy (self):          return self._var ("pregnant")
        def __setPregnancy (self, value, intention="set"):
            if isinstance (value, int):     value = value > 0
            elif value == "True":           value = True
            if isinstance (value, bool):    self._var ("pregnant", value)
        pregnancy   = property (__getPregnancy, __setPregnancy, __delPregnancy, "Pregnancy status")
        pregnant    = pregnancy
        preg        = pregnancy

        def rp (self, newValue=None, intention="get"):
            if newValue is None:
                intention = "get"
            else:
                if isinstance (newValue, float):
                    newValue = int (newValue)
                if not isinstance (newValue, int):
                    return "value is of " + type (newValue) + " only int supported"
                else:
                    if self.__rpMinimum is not None and currentRp + self.rp_score < self.__rpMinimum:
                        intention = "set"
                        newValue = self.__rpMinimum
                    if self.__rpMaximum is not None and currentRp + self.rp_score > self.__rpMaximum:
                        intention = "set"
                        newValue = self.__rpMaximum
                    if intention not in [ "add", "set" ]:
                        itention = "add"
                    self._var ("relationshipPoints", newValue, intention)
            return self.rp_score

        def __getRP (self):
            returnValue = self._var ("relationshipPoints")
            if isinstance (returnValue, bool):
                return 0
            return returnValue
        rp_score = property (__getRP, None, None, "get current relationship points")
        rps = rp_score
        _rp = rp_score

# Relationship Points
        def __delRelationshipPoints (self): self.__relationshipPoints = 0
        def __getRelationshipPoints (self): return self.__relationshipPoints
        def __setRelationshipPoints (self, newValue):
            if isinstance (newValue, int):
                if self.__rpMinimum is not None and newValue < self.__rpMinimum:
                    newValue = self.__rpMinimum
                if self.__rpMaximum is not None and newValue > self.__rpMaximum:
                    newValue = self.__rpMaximum
                self.__relationshipPoints = newValue
        relationshipPoints = property (__getRelationshipPoints, __setRelationshipPoints, __delRelationshipPoints, "Relationship points")

# Character Descriptions
#        def __delUseNick (self):            self.__useNick = False
        def __delUseNick (self):            self._var ("uses nick", False)
#        def __getUseNick (self):            return self.__useNick
        def __getUseNick (self):            return self._var ("uses nick")
        def __setUseNick (self, value):
            if isinstance (value, bool):
                self.__useNick = value
                self._var ("uses nick", bool)
        useNick     = property (__getUseNick, __setUseNick, __delUseNick, "Decides if the character should return the actual name or the nickname for __str__")
        usesNick    = useNick
        un          = useNick


# Character _ function for boolean values
# Don't call directly, just give _ a bool value and it will delegate to this function
#
# remove setattr, so the only option to access these attributes is via the _ function
# less opportunity to change the e.g. char.age and forget about char._("age")
# since char.age wouldn't change char._("age") and it's currently not planned to work on proxy property/attribute bla bla
        def __boolVariable (self, variableName, value=False, intention="get", valueType=None):
            if intention == "set" and not variableName in self.__variables ["bool"] and value:
                self.__variables ["bool"].extend ([ variableName ])
            if intention == "del" and variableName in self.__variables ["bool"]:
                self.__variables ["bool"].remove (variableName)
            return variableName in self.__variables ["bool"]

        def __intVariable (self, variableName, valueToAdd=0, intention="get", valueType=None):
            if isinstance (valueToAdd, str): valueToAdd = 0
            if intention == "add":
                if variableName in self.__variables ["int"]:
                    valueToAdd += self.__variables ["int"][variableName]
                self.__variables ["int"].update ({ variableName : valueToAdd })
                return valueToAdd
            if intention == "set":
                self.__variables ["int"].update ({ variableName : valueToAdd })
                return valueToAdd
            elif intention == "del" and variableName in self.__variables ["int"]:
                del self.__variables ["int"][variableName]
            elif variableName in self.__variables ["int"]:
                return self.__variables ["int"][variableName]

        def __strVariable (self, variableName, newValue, intention="get", valueType=None):
            listTypeTrigger = valueType in [ list, None ]
            if not isinstance (newValue, str): newValue = str (newValue)
            if intention == "compare":  return variableName in self.__variables ["str"] and self.__variables ["str"][variableName] == newValue
            if intention == "in":       return variableName in self.__variables ["str"] and newValue in self.__variables ["str"][variableName]
            elif intention == "set":
                self.__variables ["str"].update ({ variableName : newValue })
                return newValue
            elif intention == "add":
                separator = "," if listTypeTrigger else ""
                if variableName not in self.__variables ["str"]:
                    self.__variables ["str"].update ({ variableName : "" })
                newValue = self.__variables ["str"][variableName] + separator + newValue
                newValue = self.__strCorrectList (newValue)
                self.__variables ["str"].update ({ variableName : newValue })
                # return newValue
            elif intention == "del" and variableName in self.__variables ["str"]:
                if newValue == "":
                    del self.__variables ["str"][variableName]
                elif newValue != "":
                    newValue = self.__variables ["str"][variableName].replace (newValue, "")
                    newValue = self.__strCorrectList (newValue)
                    if newValue != "":
                        self.__variables ["str"].update ({ variableName : newValue })
                    else:
                        del self.__variables ["str"][variableName]
                    return newValue
                elif not listTypeTrigger and not isinstance (newValue, str):
                    return "Unknown valueType for __strVariable. Only None and list known"
            elif variableName in self.__variables ["str"]:
                return self.__variables ["str"][variableName]
            return False

        def __strCorrectList (self, value):
            value = value.replace (", ", ",")
            while value.find (",,") > -1:   value.replace (",,", ",")
            return value.strip (",")

# Character is "variable"
# Removing a bool value is the same as settin it to False
# Removing an integer value needs remove=True as parameter
# if "intention" is "False" or "delete" (see below), the variable will be removed
        def _var (self, variableName, variableValue="", intention="get", valueType=None):
            returnValue = False
            callFunction = ""
            if intention in [ "del", "delete", "rem", "remove", False ]:    intention = "del"
            elif intention in [ "change", "set" ]:                          intention = "set"
            elif intention in [ "add" ]:                                    intention = "add"
            elif intention in [ "compare", "is" ]:                          intention = "compare"
            elif intention in [ "in" ]:                                     intention = "in"
            for dictKey in self.__variables.keys ():
                if isinstance (self.__variables [dictKey], list):
                    if variableName in self.__variables [dictKey]:          callFunction = "__" + dictKey + "Variable"
                else:
                    if variableName in self.__variables [dictKey].keys ():  callFunction = "__" + dictKey + "Variable"
            if callFunction == "" and variableValue is not None:
                if isinstance (variableValue, bool):    callFunction = "__boolVariable"
                elif isinstance (variableValue, int):   callFunction = "__intVariable"
                elif isinstance (variableValue, str):   callFunction = "__strVariable"
            if callFunction == "__boolVariable" and intention == "get":
                if variableValue is True and variableValue != "":   intention = "set"
                if variableValue is False:  intention = "del"
            elif callFunction == "__intVariable" and intention == "get" and isinstance (variableValue, int):
                if variableValue != "":     intention = "add"
                if variableValue is False:  intention = "del"
            elif callFunction == "__strVariable" and intention == "get" and variableValue != "":
                valueType = list if valueType in [ list, None ] else valueType
                if variableName not in self.__variables ["str"]:    intention = "set"
                else:                                               intention = "in" if valueType == list else "compare"
      
            if callFunction != "":
                if callFunction == "__boolVariable":    callFunction = self.__boolVariable
                if callFunction == "__intVariable":     callFunction = self.__intVariable
                if callFunction == "__strVariable":     callFunction = self.__strVariable
                #return callFunction + " " + intention + " to " + str (variableValue)
                returnValue = callFunction (variableName, variableValue, intention, valueType)
            return returnValue

        def setDefaultProfileImageIndex(self, imageIndex):
            # using setattr to avoid non-existent attribute error in case defaultProfileImageIndex is not set yet;
            # since this attribute is introduced in a later update, there may be already created characters
            # that don't have this attribute, so setattr will just create it for them when needed
            setattr(self, "defaultProfileImageIndex", imageIndex)
        
        def getDefaultProfileImageIndex(self):
            # see setDefaultProfileImageIndex for explanation on setattr/getattr usage
            return getattr(self, "defaultProfileImageIndex", 0)

        def isDefaultProfileImageIndex(self, imageIndex):
            # see setDefaultProfileImageIndex for explanation on setattr/getattr usage
            return imageIndex == getattr(self, "defaultProfileImageIndex", 0)
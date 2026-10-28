init 10 python:
    class TGCharacterRoles ():

        registeredRoles = {
            "placeholder"   : TGCharacterRoleCustom (),
            "aunt"          : TGCharacterRoleAunt (),
            "boyfriend"     : TGCharacterRoleBoyfriend (),
            "brother"       : TGCharacterRoleBrother (),
            "buddy"         : TGCharacterRoleBuddy (),
            "classmateF"    : TGCharacterRoleClassmateF (),
            "classmateM"    : TGCharacterRoleClassmateM (),
            "classmate"     : TGCharacterRoleClassmateF (),
            "cousinF"       : TGCharacterRoleCousinF (),
            "cousinM"       : TGCharacterRoleCousinM (),
            "cousin"        : TGCharacterRoleCousinF (),
            "father"        : TGCharacterRoleFather (),
            "fiance"        : TGCharacterRoleFiance (),
            "fiancee"       : TGCharacterRoleFiancee (),
            "friendF"       : TGCharacterRoleFriendF (),
            "friendM"       : TGCharacterRoleFriendM (),
            "friend"        : TGCharacterRoleFriendF (),
            "housemateF"    : TGCharacterRoleHousemateF (),
            "housemateM"    : TGCharacterRoleHousemateM (),
            "housemate"     : TGCharacterRoleHousemateF (),
            "girlfriend"    : TGCharacterRoleGirlfriend (),
            "grandaunt"     : TGCharacterRoleAunt (),
            "grandfather"   : TGCharacterRoleGrandfather (),
            "grandmother"   : TGCharacterRoleGrandmother (),
            "landlady"      : TGCharacterRoleLandlady (),
            "landlord"      : TGCharacterRoleLandlord (),
            "mother"        : TGCharacterRoleMother (),
            "neighbor"      : TGCharacterRoleNeighborF (),
            "neighborF"     : TGCharacterRoleNeighborF (),
            "neighborM"     : TGCharacterRoleNeighborM (),
            "nephew"        : TGCharacterRoleNephew (),
            "niece"         : TGCharacterRoleNiece (),
            "roommateF"     : TGCharacterRoleRoommateF (),
            "roommateM"     : TGCharacterRoleRoommateM (),
            "roommate"      : TGCharacterRoleRoommateF (),
            "soulmateF"     : TGCharacterRoleSister (),
            "soulmateM"     : TGCharacterRoleSoulmateF (),
            "soulmate"      : TGCharacterRoleSoulmateM (),
            "sister"        : TGCharacterRoleSister (),
            "uncle"         : TGCharacterRoleUncle ()
        }

        def __init__ (self):
            self.__roles = []
        
        def __delRoles (self):  self.__roles = []
        def __getRoles (self):  return self.__roles
        def __setRoles (self, role = ""):
            primary = False
            if role is None:
                role = ""
            if isinstance (role, dict):
                if "role" in role:
                    newRole = role ["role"]
                if "primary" in role:
                    primary = role ["primary"]
                role = newRole
            if isinstance (role, str):
                if role == "":
                    role = "placeholder"
                if role in self.registeredRoles:
                    role = self.registeredRoles [role]
                else:
                    role = TGCharacterRoleCustom (role)
            if not isinstance (primary, bool):
                primary = False
            if primary:
                for index in range (0, len (self.__roles)):
                    self.__roles [index]["primary"] = False
            self.__roles += [ { "role" : role, "primary" : primary } ]
        roles = property (__getRoles, __setRoles, __delRoles, "List of character roles")
        list = roles

        def __getRole (self):
            for role in self.__roles:
                if role.get ("primary", False):
                    return role.get ("role", TGCharacterRoleCustom ())
            return role.get ("role", TGCharacterRoleCustom ())
        role = property (__getRole, None, None, "Primary character role")

        def addRole (self, role = TGCharacterRoleCustom (), primary = False):
            if len (self.roles) == 0:
                primary = True
            self.roles = { "role" : role, "primary" : primary }
            return self.roles

        def delete (self, role):
            roleToDelete = None
            if len (self.roles) > 0:
                if isinstance (role, TGCharacterRole):
                    for index in range (0, len (self.roles)):
                        if self.roles [index]["role"].long == role.long:
                            del self.roles [index]
                            break
                elif isinstance (role, str):
                    for index in range (0, len (self.roles)):
                        if self.roles [index]["role"].long == role:
                            del self.roles [index]
                            break
                hasPrimary = False
                for index in range (0, len (self.roles)):
                    if self.roles [index]["primary"]:
                        hasPrimary = True
                        break
                if not hasPrimary and len (self.roles) > 0:
                    self.roles [0]["primary"] = True
                return self.roles
            
init 100:
###############################################################################
###############################################################################
### ONLY STUFF THAT DOES NOT CHANGE AND DOESN'T NEED TO BE IN THE SAVEGAME  ###
###   EVERYTHING ELSE, LIKE NEW CHARACTERS GOES INTO THE BEGINNING OF THE   ###
###                     CHAPTER LIKE YOU DID IN PART 1!                     ###
###############################################################################
###############################################################################
### strings we might need in dialgoue
    define mother = _("la exnovia del padre")
    define Aunt = ""
    define your_nephew = _("prácticamente tu sobrino")

### Character Roles
# You can define roles here, they are unchangable, as far as we are concerned.
# If we need to change a role, we remove the old role and add a new.
# Mostly stuff Riam needs to worry about
### Character Roles


### narrators
    define trop             = TGCharacter ("Tropecita Games", color = "#9ac", what_italic = True, who_italic = True)
    define riam             = TGCharacter ("Riam Mar", color = "#9ac", what_italic = True, who_italic = True)
    define tropriam         = TGCharacter ("[trop] & [riam]", color = "#9ac", what_italic = True, who_italic = True)
    define settingsDemoWho  = TGCharacter (_("Narradora"), color = "#9ac")

### others
    define gorila   = TGCharacter (_("Gorila"), color = "#285bda")
    define guy1     = TGCharacter (_("Tipo 1"))
    define guy2     = TGCharacter (_("Tipo 2"))
    define jac      = TGCharacter ("Jack", color = "#ff3c33")
    define man      = TGCharacter (_("Hombre"), color = "#9f483a")
    define mj       = TGCharacter (_("Señora Russell"), color="#35f3ff")
    define ton      = TGCharacter ("Tony", color = "#285bda")
    define todas    = TGCharacter (_("Todas"), color = "#ff3c33")
    define wom      = TGCharacter (_("Mujer"), color = "#f9ff33")
    define kev      = TGCharacter ("Kevin", color="#35f3ff")
    define pwom     = TGCharacter (_("Mujer Policía"), color="#285bda")
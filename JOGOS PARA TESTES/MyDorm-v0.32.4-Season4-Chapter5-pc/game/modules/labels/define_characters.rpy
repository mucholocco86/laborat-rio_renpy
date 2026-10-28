# label define_characters:
# # narrator
#     define narrator         = TGCharacter ("Narrator", color = "#9ac", what_italic = True, who_italic = True)
#     define settingsDemoWho  = TGCharacter ("Narrator", color = "#9ac")
# # gen. family
#     define ana      = TGCharacter ("Mysterious Girl 2", color = "#3b6e49")
#     define eva      = TGCharacter ("Mysterious Girl 1", color = "#abf707")
# # family
#     $ defaultNames
#     define mc       = TGCharacter (TGCharacter.defaultNames ["mc"], color = "#9042f5", isMC = True)
#     define mcp      = TGCharacter ("[mc]", color = "#9042f5", what_italic = True)
#     define dad      = TGCharacter ("Dad")
#     define dap      = TGCharacter (TGCharacter.defaultNames  ["dap"], color = "#e85613", lname = "Marks", nick = "Daph")
#     define emm      = TGCharacter (TGCharacter.defaultNames  ["emm"], color = "#8f497b", lname = "Marks", nick = "Em")
#     define eri      = TGCharacter (TGCharacter.defaultNames  ["eri"], color = "#7b7b7b", lname = "Marks", nick = "Eri")
#     define mom      = TGCharacter (TGCharacter.defaultNames  ["mom"], color = "#ebebeb", lname = "Marks", nick = "Martha")
# #    $ mar           = "Martha" #   make this mom.name
# #    $ Mom = momm    = "Martha" #   make this mom.nick and mom.nick_lower
# #    $ mother        = "Father's ex-girlfriend" #   make this mom.description or mom.desc
#     define nor      = TGCharacter (TGCharacter.defaultNames  ["nor"], color = "#ab2c49", lname = "Marks", mc_role = "almost your nephew")
#     $ Aunt          = ""   #   make this nor.nick
#     $ your_nephew   = "almost your nephew"  #   make this nor.mc_role.
#     define noremm   = TGCharacter ("[nor] and [emm]",   color = "#ff3c33")  # will automatically adjust when Norah and Emma are renamed
# # friends
#     define eil      = TGCharacter ("Eileen", color = "#4fff33")
#     define jam      = TGCharacter ("Jamaal", color = "#8b7b7b")
#     define mad      = TGCharacter ("Maddie")
#     define meg      = TGCharacter ("Megan", color = "#d4b34a")
#     define oma      = TGCharacter ("Officer Martinez", color = "#285bda")
#     define pwom     = TGCharacter ("Policewoman", color = "#285bda")
#     define sam      = TGCharacter ("Mrs. Washington", color = "#8f483a")
#     define sca      = TGCharacter ("Scarlett", color = "#33f3ff")
#     define sim      = TGCharacter ("Simone", color = "#8f483a")
#     define sop      = TGCharacter ("Sophie")
# # Students
#     define kim      = TGCharacter ("Kim", color = "#f9ff33")
#     define kat      = TGCharacter ("Kathy", color = "#fc0335")
#     define lis      = TGCharacter ("Lisa", color = "#ebe7a2")
#     define deb      = TGCharacter ("Debbie", color = "#0324fc")
#     define sai      = TGCharacter ("Saira", color = "#d4b34a")
# # others
#     define gorila   = TGCharacter ("Bouncer", color = "#285bda")
#     define guy1     = TGCharacter ("Guy 1")
#     define guy2     = TGCharacter ("Guy 2")
#     define jac      = TGCharacter ("Jack", color = "#ff3c33")
#     define man      = TGCharacter ("Man", color = "#9f483a")
#     define ton      = TGCharacter ("Tony", color = "#285bda")
#     define todas    = TGCharacter ("All of them", color = "#ff3c33")
#     define wom      = TGCharacter ("Woman", color = "#f9ff33")
# # Character translations are in modules/Translations/Characters
# # The translateCharacters is found in modules/_shared/functions
# #    translateCharacters (persistent.lang)
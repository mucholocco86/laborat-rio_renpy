init python:
    walkthrough.addGeneralInfo ({   # use addGeneralInfo to give info's about what this choice implies for future content; e.g.: Route permanently closed
        "C001" : {   # target file; name without path and file extension
            "en" : {    # target language
                201 : { # target line number of "menu" tag
                    "Yes" : {
                        # use index for ordering multiple entries to one choice
                        # color -1 = orange/negative; 0 = white/neutral; +1 = blue/positive
                        0 : { "color" : 1, "value" : "Farewell sex with [sai]" }    # what's this choice about
                    },
                }
            }
        }
    })
    walkthrough.addInfoAboutVariables ({    # use this to indicate a change in relationship points or the harem counter
        "thisIsAnExample" : {   # target file; name without path and file extension; keep the rpy files, if someone want's them, they can get them anyway
            "example" : {   # target language
                123 : { # target line number of "menu" tag
                    "Yes" : { "[sai]" : { "Relationship" : +1 } }   # which characters variable effects this choice and by how much? For Bool, describe it in the general info; ToDo: Add differenciation for numbers and bool in Walkthrough class
                }
            }
        }
    })
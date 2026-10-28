screen ProfilesCharacterSelect(characterProfile):
    modal True
    python:
        if not hasattr (characterProfile, "profilePicture"):
            setattr (characterProfile, "profilePicture", (characterProfile.name.last_name + "_" + characterProfile.defaultName).lower ())
        profileImage = "images/profiles/characters/" + characterProfile.profilePicture
        fileExtensions = [ "png", "webp" ]
        hasProfileImage = False
        for fileExtension in fileExtensions:
            profileImageWithExtension = profileImage + "." + fileExtension
            if renpy.loadable (profileImageWithExtension):
                hasProfileImage = True
                profileImage = profileImageWithExtension
                break
        if not hasProfileImage:
            profileImage = "images/profiles/characters/" + (characterProfile.name.last_name + "_" + characterProfile.defaultName).lower ()
            for fileExtension in fileExtensions:
                profileImageWithExtension = profileImage + "." + fileExtension
                if renpy.loadable (profileImageWithExtension):
                    hasProfileImage = True
                    profileImage = profileImageWithExtension
                    break
    button:
        action [ ShowMenu ("Profiles", characterProfile) ]
        focus_mask True
        xalign 0.5
        yalign 1.0
        xysize (300, 300)
        if hasProfileImage:
            image profileImageWithExtension:
                xysize (300, 300)
        else:
            image icons ["NotAvailable"]:
                xysize (300, 300)
        $ stats = {
            "route" : ("Heart", _("En una relación con [mc]")),
            "breakup" : ("Broken Heart", _("relación rota")),
            "pregnant" : ("Pregnant", _("Esperando a la bebé de [mc]")),
            "engaged" : ("Bride", _("Prometida con [mc]"))
        }
        frame:
            background Solid ("#0009")
            xanchor 0.0
            xsize 300
            yalign 1.0
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 5
                python:
                    characterName = characterProfile.name.name
                    if characterProfile._var ("usesNick"):
                        characterName = characterProfile.nick
                text characterName xalign 0.5 yalign 1.0 outlines [ (1, "#000", 0, 0) ]
                for statVariable, (statIcon, statTooltip) in stats.items ():
                    if characterProfile._var (statVariable):
                        image Transform (icons [statIcon], matrixcolor = InvertMatrix()):
                            xysize (26, 26)
                            yalign 0.5
                    if statVariable == "route" and not characterProfile._var (statVariable):
                        image Transform (icons ["RP"], matrixcolor = InvertMatrix()) xysize (26, 26) yalign 0.5
                        if characterProfile._var ("uses RP") and characterProfile.rp_score > 0:
                            text str (characterProfile.rp_score)

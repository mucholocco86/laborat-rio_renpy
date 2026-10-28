label patchC13:
    python:
        if isinstance (mar, TGCharacter):
            if "MarthaPregnant" in globals ():
                mar._var ("pregnant", MarthaPregnant)
                del MarthaPregnant
            if "MeganRoute" in globals ():
                meg._var ("route", MeganRoute)
                del MeganRoute
            if "MeganPregnant" in globals ():
                meg._var ("pregnant", MeganPregnant)
                del MeganPregnant
            if mee._var ("jobs"):
                mee._var ("job", mee._var ("jobs"))
                mee._var ("jobs", intention = "del")
            if mar._var ("traits, metal"):
                mar._var ("traits, mental", mar._var ("traits, metal"))
                mar._var ("jobs", intention = "traits, metal")
            if nor._var ("traits, metal"):
                nor._var ("traits, mental", nor._var ("traits, metal"))
                nor._var ("jobs", intention = "traits, metal")
            #if emm._var ("traits, physical", _("impulsiva"), intention = "in"):
            #    emm._var ("traits, mental", _("impulsiva"))
            #    emm._var ("traits, mental", _("impaciente"), "add", list)
            #    emm._var ("traits, physical", _("impulsiva"), "del", list)
            #    emm._var ("traits, physical", _("impaciente"), "del", list)
            #if sca._var ("traits, physical", _("personas con discapacidad auditiva"), intention = "in"):
            #    sca._var ("traits, physical", _("discapacidad auditiva"), "add", list)
            #    sca._var ("traits, physical", _("personas con discapacidad auditiva"), "del", list)
            if eva._var ("traits, metal"):
                eva._var ("traits, mental", eva._var ("traits, metal"))
                eva._var ("jobs", intention = "traits, metal")
            kal._var ("birthday", "2021-09-09")
            kal._var ("age", 18, "set")
            kal._var ("height", 171, "set")
            kal._var ("job", _("estudiante"))
            sai._var ("age", 20, "set")
            sai._var ("height", 179, "set")
            for characterProfile in [ cri, deb, hai, kal, kat, kim, lis, nia, pat, zoe ]:
                characterProfile._var ("uses RP", True)
            filePath = "images/profiles/"
            for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
                characterProfile._var ("is known", True)
                characterProfile.initProfileImages ()
#                if len (characterProfile.profileImages) == 0:
#                    filePrefix = characterProfile.defaultName.lower ()
#                    for fileIndex in range (7):
#                        fileName = filePrefix + "_" + str (fileIndex)
#                        hadImage = False
#                        for fileExtension in [ "webp", "png" ]:
#                            if renpy.loadable (filePath + fileName + "." + fileExtension):
#                                hadImage = True
#                                characterProfile.addProfileImage (fileName, [ "route", "pregnant" ] if fileIndex > 5 else ("route" if fileIndex > 4 else None))
#                        if not hadImage:
#                            break

    jump patchC13End

init 10 python:
    config.label_overrides.update ({
        "after_load" : "patchC13",
        "patchC13End" : "after_load"
    })

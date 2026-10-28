label patchImportFromPart1:
    call defineCharacters from _call_defineCharacters

    riam "Ahora aplicamos algunos parches para que todo el progreso de la parte 1 funcione con la parte 2."
    python:
        eStr = [ "", None ] # empty string check, will be deleted later
        persistent.walkthrough = wt
        del wt

################################################################################
### Kinks

        persistent.pregnancy = Pregnancy
        persistent.lactation = Lactation
        persistent.lesbian = lesbian
        persistent.urination = Urination
        del Pregnancy, Lactation, lesbian, Urination

    riam "Parcheando la configuración general. Puedes revisarla y cambiarla en cualquier momento en la pestaña de configuración general."

################################################################################
### Martha - mom
    python:
        if "mom_name" not in globals (): mom_name = ""
        mar.name.first_name = mom_name if mom_name not in eStr else "Martha"
        mar._var ("route", MarthaRoute)
        mar._var ("fittingRoom", probadorMartha)
        mar._var ("routeSecondChance", MarthaCafe)
        if "MarSexName" not in globals (): MarSexName = ""
        if "MarthaPregnant" not in globals (): MarthaPregnant = False
        if "MarSex" not in globals (): MarSex = False
        mar._var ("lewd", MarSexName)
        mar._var ("pregnant", MarthaPregnant)
        mar.name.lewd = _("Mamá") if MarSexName else mar.name.first_name
        del mom_name, MarthaRoute, probadorMartha, MarthaCafe, MarSex, MarSexName, MarthaPregnant

################################################################################
### Emma - emm

        if "emm_name" not in globals (): emm_name = ""
        emm.name.first_name = emm_name if emm_name not in eStr else "Emma"
        emm.name.mcLewd = EmmaDaddy if EmmaDaddy not in eStr else mc.name.first_name
        emm._var ("chat", EmmaChat)
        emm._var ("route", EmmaRoute)
        emm._var ("routeSecondChance", EmmaRouteJacuzzi)
        if "HelpEmma" not in globals (): HelpEmma = False
        emm._var ("help", HelpEmma)
        emm._var ("pregnant", EmmaPregnant)
        emm._var ("reggaeton", EmmaReggaeton)
        emm._var ("anal", AnalEmma)
        emm._var ("plug", PlugEmma)
        emm._var ("spanking", SpankEmma)
        del emm_name, EmmaDaddy, EmmaRoute, EmmaRouteJacuzzi, HelpEmma, EmmaPregnant, EmmaReggaeton, AnalEmma, PlugEmma, SpankEmma

################################################################################
### Norah - nor

        if "nor_name" not in globals (): nor_name = ""
        nor.name.first_name = nor_name if nor_name not in eStr else "Norah"
        nor._var ("route", NorahRoute)
        nor._var ("routeSecondChance", NorahHand)
        nor._var ("pregnant", NorahPregnant)
        del nor_name, NorahRoute, NorahHand, NorahPregnant

################################################################################
### Erika - eri

        if "eri_name" not in globals (): eri_name = ""
        eri.name.first_name = eri_name if eri_name not in eStr else "Erika"
        eri._var ("route", BeatingToilet)
        eri._var ("route", ErikaRoute)
        eri._var ("routeSecondChance", not BeatingToilet and not ErikaSauna and ErikaRoute)
        eri._var ("routeThirdChance", not BeatingToilet and ErikaSauna)
        eri._var ("broughtToWorkOnDay6", TakeErikaWork6)
        eri._var ("pregnant", ErikaPregnant)
        eri._var ("knowsNorahPregnancy", ErikaKnowsNorahPregnancy)
        del eri_name, ErikaRoute, BeatingToilet, ErikaSauna, TakeErikaWork6, ErikaPregnant

################################################################################
### Daphne - dap + Scarlett - sca

        mc._var ("routeDapSca", DaphneScarlettRoute)

################################################################################
### Daphne - dap - Part B

        if "dap_name" not in globals (): dap_name = ""
        if "DaphneAlone" not in globals (): DaphneAlone = False
        dap.name.first_name = dap_name if dap_name not in eStr else "Daphne"
        dap._var ("breakup", DaphneBreakup)
        dap._var ("route", not DaphneBreakup and (DaphneScarlettRoute or DaphneRoute))
        dap._var ("routeSecondChance", not DaphneBreakup and DaphneAlone)
        dap._var ("romance", not DaphneBreakup and DaphneRomance)
        del dap_name, DaphneBreakup, DaphneRoute, DaphneAlone, DaphneRomance
        # del DaphneScarlettRoute after Scarlett patching

################################################################################
### Scarlett - sca

        if "ScarlettAlone" not in globals (): ScarlettAlone = False
        sca._var ("breakup", ScarlettBreakup)
        sca._var ("route", not ScarlettBreakup and (DaphneScarlettRoute or ScarlettRoute))
        sca._var ("routeSecondChance", not ScarlettBreakup and ScarlettAlone)
        sca._var ("anal", AnalScarlett)
        sca._var ("plug", PlugScarlett)
        sca._var ("pregnant", ScarlettPregnant)
        del DaphneScarlettRoute, ScarlettBreakup, ScarlettRoute, ScarlettAlone, AnalScarlett, PlugScarlett, ScarlettPregnant

################################################################################
### Eileen - eil

        eil._var ("route", EileenRoute)
        eil._var ("routeSecondChance", not EileenCafe3 and EileenRoute)
        eil._var ("pregnant", EileenPregnant)
        del EileenRoute, EileenCafe3, EileenPregnant

################################################################################
### Alexia - oma

        oma._var ("route", AlexiaRoute)
        oma._var ("routeSecondChance", AlexiaRoute and not AlexiaAtPolice)
        oma._var ("pregnant", AlexiaPregnant)
        del AlexiaRoute, AlexiaAtPolice, AlexiaPregnant

################################################################################
### Samantha - sam

        if "SamanthaNatural" not in globals (): SamanthaNatural = False
        if "SamanthaPregnant" not in globals (): SamanthaPregnant = False
        sam._var ("breakup", SamanthaBreakUp)
        sam._var ("route", not SamanthaBreakUp and SamanthaRoute)
        sam._var ("massage", SamanthaMassage)
        sam._var ("routeSecondChance", not SamanthaBreakUp and not SamanthaMassage and SamanthaRoute)
        sam._var ("naturalPubicHair", SamanthaNatural)
        sam._var ("pregnant", SamanthaPregnant)
        del SamanthaBreakUp, SamanthaRoute, SamanthaMassage, SamanthaNatural, SamanthaPregnant

################################################################################
### Simone - sim

        sim._var ("route", SimoneRoute)
        sim._var ("pregnant", SimonePregnant)
        del SimoneRoute, SimonePregnant

################################################################################
### Megan - meg

        meg._var ("route", MeganRoute)
        meg._var ("pregnant", MeganPregnant)
        del MeganRoute, MeganPregnant

################################################################################
### Maddie - mad

        mad._var ("blackmail", MaddieBlackmail)
        # MaddieRoute = MaddieRomance or (MaddieBlackmail and (MaddieDom or MaddieSub or MaddieRomance))
        # MaddieRomance at the end already covered at the beginning of the statement
        mad._var ("route", MaddieRomance or (MaddieBlackmail and (MaddieDom or MaddieSub))) # ToDo MaddieRoute what how why
        mad._var ("romance", MaddieRomance)
        mad._var ("dom", MaddieDom)
        mad._var ("sub", MaddieSub)
        del MaddieBlackmail, MaddieRomance, MaddieDom, MaddieSub

    riam "Parcheando a todas las chicas de la primera parte de la primera parte, ¿están confundidas? Sí yo también."

    python:

################################################################################
### Best Meemaw - mee

        mee._var ("mcKnowsSickness", MCKnowsMeemawSickness)
        del MCKnowsMeemawSickness

################################################################################
### MC

        if "mc_name" not in globals (): mc_name = ""
        mc.name.first = mc_name if mc_name not in eStr else "Mark"
        mc._var ("truthOrDare", c04s010_MC_V)
        mc._var ("edmundsStory", EdmundStory)
        mc._var ("relationships", Relationships)
        mc._var ("acceptedHarem", AcceptedHarem)
        mc._var ("wantsChildren", WantsChildren)
        del mc_name, c04s010_MC_V, EdmundStory, Relations, Relationships

################################################################################
### other males

        jon._var ("blackmailed", BlackmailJonas)

################################################################################
### First batch of students

        deb._var ("laptop", LaptopDebbie)
        kat._var ("lesbianContent", KateLesbianContent)
        kat._var ("slim", KateSlim)
        kim._var ("makeup", KimMakeup)
        lis._var ("hug", HugLisa)
        lis._var ("escorted", EscortLisa)
        del LaptopDebbie, KateLesbianContent, KateSlim, KimMakeup, HugLisa, EscortLisa

        deb.rp (PDeb)
        kat.rp (PKat)
        kim.rp (PKim)
        lis.rp (PLis)
        del PDeb, PKat, PKim, PLis

    $ del eStr

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
            if emm._var ("traits, physical", _("impulsiva"), intention = "in"):
                emm._var ("traits, mental", _("impulsiva"))
                emm._var ("traits, mental", _("impaciente"), "add", list)
                emm._var ("traits, physical", _("impulsiva"), "del", list)
                emm._var ("traits, physical", _("impaciente"), "del", list)
            if sca._var ("traits, physical", _("personas con discapacidad auditiva"), intention = "in"):
                sca._var ("traits, physical", _("discapacidad auditiva"), "add", list)
                sca._var ("traits, physical", _("personas con discapacidad auditiva"), "del", list)
            if eva._var ("traits, metal"):
                eva._var ("traits, mental", eva._var ("traits, metal"))
                eva._var ("jobs", intention = "traits, metal")
            for characterProfile in [ cri, deb, hai, kal, kat, kim, lis, nia, pat, zoe ]:
                characterProfile._var ("uses RP", True)
            filePath = "images/profiles/"
            for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim ]:
                characterProfile._var ("is known", True)
                characterProfile.initProfileImages ()
                if len (characterProfile.profileImages) == 0:
                    filePrefix = characterProfile.defaultName.lower ()
                    for fileIndex in range (7):
                        fileName = filePrefix + "_" + str (fileIndex)
                        hadImage = False
                        for fileExtension in [ "webp", "png" ]:
                            if renpy.loadable (filePath + fileName + "." + fileExtension):
                                hadImage = True
                                characterProfile.addProfileImage (fileName, [ "route", "pregnant" ] if fileIndex > 5 else ("route" if fileIndex > 4 else None))
                        if not hadImage:
                            break

    call updateRoles from _call_updateRoles
    riam "¡Parcheado todo!"
    return

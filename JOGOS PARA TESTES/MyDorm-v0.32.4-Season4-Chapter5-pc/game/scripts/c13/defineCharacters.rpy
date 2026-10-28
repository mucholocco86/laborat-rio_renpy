init 1000 python:
    def mom_actor (what, **kwargs):
        global mar
        say (mar.bymc, what, **kwargs)

label defineCharacters:
    ##### Children first, then their parents. That way, adding the roles can be done where the character is created
    ##### This is more important for isFamily != True, since they use custome rules for their relationship
    ##### But we want to keep it the same everywhere
    python:
    ### family
        if "mc" not in globals () or not isinstance (mc, TGCharacter):
            mc = TGCharacter ("Mark", color = "#9042f5", lname = "Marks", isMC = True)

        if "mcp" not in globals () or not isinstance (mcp, TGCharacter):
            mcp = TGCharacter ("[mc]", color = mc.color, what_italic = True, isMC = True)

        if "eri" not in globals () or not isinstance (eri, TGCharacter):
            eri = TGCharacter ("Erika", color = "#7b7b7b", lname = "Marks", nick = "Eri", isFamily = True)

            eri._var ("birthday", "2021-08-26")
            eri._var ("age", 18)
            eri._var ("height", 177)
            eri._var ("job", _("estudiante"))
            # clone stuff and patch related roles are done via myDorm.toggleFamily () at the end of the file and when the button in the main menu is pressed
            eri._var ("traits, physical", _("tatuajes"))
            eri._var ("traits, physical", _("pelirroja natural"), "add", list)
            eri._var ("traits, mental", _("romantico"))

        if "dap" not in globals () or not isinstance (dap, TGCharacter):
            dap = TGCharacter ("Daphne", color = "#e85613", lname = "Marks", nick = "Daph", isFamily = True)
            dap._var ("birthday", "2021-08-26")
            dap._var ("age", 18)
            dap._var ("height", 177)
            dap._var ("job", _("estudiante"))
            dap._var ("traits, physical", _("pecas"))
            dap._var ("traits, mental", _("astuto"))

        if "emm" not in globals () or not isinstance (emm, TGCharacter):
            emm = TGCharacter ("Emma", color = "#8f497b", lname = "Marks", nick = "Em", isFamily = True)
            emm._var ("birthday", "2021-07-23")
            emm._var ("age", 18)
            emm._var ("height", 181)
            emm._var ("job", _("estudiante"))
            emm._var ("traits, physical", _("impulsiva"))
            emm._var ("traits, physical", _("impaciente"), "add", list)
            emm._var ("traits, physical", _("a ella le gusta el rosa"), "add", list)

        if "dad" not in globals () or not isinstance (dad, TGCharacter):
            dad = TGCharacter ("Edmund", color = "#ffffff", lname = "Marks", isFamily = True)
            dad.roles.addRole ("dad")

        if "mar" not in globals () or not isinstance (mar, TGCharacter):
            mar = TGCharacter ("Martha", color = "#ebebeb", lname = "Marks", nick = "Martha", isFamily = True)
            mar._var ("birthday", "2021-06-12")
            mar._var ("age", 40)
            mar._var ("height", 180)
            mar._var ("job", _("encargado del Dormitorio"))
            mar._var ("profession", _("Cocinera"))
            mar._var ("traits, metal", _("depresión"))

            if "mom" in globals ():
                del mom
            # this is a proxy for Martha for her display name when she talks, so she can be displayed by what MC calls her instead of her name
            mom = mom_actor

        if "nor" not in globals () or not isinstance (nor, TGCharacter):
            nor = TGCharacter ("Norah", color = "#ab2c49", lname = "Marks", isFamily = True)
            nor._var ("birthday", "2021-05-24")
            nor._var ("age", 45)
            nor._var ("height", 178)
            nor._var ("job", _("gerente de dormitorio"))
            nor._var ("profession", _("Administración de Empresas"))
            nor._var ("traits, metal", _("Persona insegura"))

        if "mee" not in globals () or not isinstance (mee, TGCharacter):
            mee = TGCharacter ("Olivia", color = "#ffeedd", lname = "Bladagan", nick = "Meemaw", usesNick = True)
            mee._var ("birthday", "2021-10-12")
            mee._var ("age", 66)
            mee._var ("jobs", _("jubilada"))
            mee._var ("profession", _("agente de bienes raíces"))

        if "bet" not in globals () or not isinstance (bet, TGCharacter):
            bet = TGCharacter ("Betty", color = "#8ad8e4", lname = "Cavendish")
            bet._var ("birthday", "2021-02-26")
            bet._var ("age", 64)
            bet._var ("job", _("monja"))
            bet._var ("profession", _("Cirujana"))

        if "noremm" not in globals () or not isinstance (noremm, TGCharacter):
            noremm = TGCharacter ("[nor] and [emm]",   color = "#ff3c33")  # will automatically adjust when Norah and Emma are renamed

        bet.roles.delete (_("la hermana de [mee]"))
        bet.roles.addRole (_("la tía de [mar] y [nor]"))

        mee.roles.addRole (_("la madre de [mar] y [nor]"))

        mar.roles.addRole (_("la hija de [mee]"))
        mar.roles.addRole (_("la sobrina de [bet]"))
        mar.roles.addRole (_("la hermana de [nor]"))

        nor.roles.addRole (_("la hija de [mee]"))
        nor.roles.addRole (_("la sobrina de [bet]"))
        nor.roles.addRole (_("la hermana de [mar]"))

    ### extended family

        if "ama" not in globals () or not isinstance (ama, TGCharacter):
            ama = TGCharacter ("Amanda", color = "#3b6e49", lname = "Gilford")
            ama._var ("birthday", "2021-08-01")
            ama._var ("age", 18)
            ama._var ("height", 177)
            ama._var ("job", _("agente de operaciones especiales"))
#            ama._var ("job", _("estudiante"), "add", list)
            ama._var ("profession", _("agente de operaciones especiales"))

        if "eva" not in globals () or not isinstance (eva, TGCharacter):
            eva = TGCharacter ("Eva", color = "#abf707", lname = "Gilford")
            eva._var ("birthday", "2021-09-30")
            eva._var ("age", 18)
            eva._var ("height", 177)
            eva._var ("job", _("agente de operaciones especiales"))
#            eva._var ("job", _("estudiante"), "add", list)
            eva._var ("profession", _("agente de operaciones especiales"))
            eva._var ("traits, physical", _("impulsiva"))
            eva._var ("traits, physical", _("impaciente"), "add", list)

    ### friends

        if "eil" not in globals () or not isinstance (eil, TGCharacter):
            eil = TGCharacter ("Eileen", color = "#4fff33", lname = "Lamb")
            eil.roles.addRole (_("ex novia"))
            eil.roles.addRole (_("amiga con beneficios"))
            eil._var ("birthday", "2021-03-04")
            eil._var ("age", 21)
            eil._var ("height", 180)
            eil._var ("job", _("barista"))

        if "kia" not in globals () or not isinstance (kia, TGCharacter):
            kia = TGCharacter ("Kiara", color = "#b234c9", lname = "Lamb")
            kia.roles.addRole (_("amiga"))
            kia._var ("birthday", "2021-08-03")
            kia._var ("age", 46)
            kia._var ("job", _("Bibliotecaria"))
            kia._var ("profession", _("Bibliotecaria"))
            kia.roles.addRole (_("madre de [eil]"))

        eil.roles.addRole (_("la hija de [kia]"))
        eil.roles.addRole (_("amiga de [eri] y [oma]"))

        if "oma" not in globals () or not isinstance (oma, TGCharacter):
            oma = TGCharacter ("Alexia", color = "#285bda", lname = "Martinez", nick = "Alex")
            oma.roles.addRole (_("amiga de [eil]"))
            oma.roles.addRole (_("conocida"))
            oma._var ("birthday", "2021-07-22")
            oma._var ("age", 24)
            oma._var ("height", 179)
            oma._var ("job", _("Oficial de policía"))
            oma._var ("profession", _("Oficial de policía"))

        if "sim" not in globals () or not isinstance (sim, TGCharacter):
            sim = TGCharacter ("Simone", color = "#8f483a", lname = "Washington")
            sim._var ("birthday", "2021-10-13")
            sim._var ("age", 19)
            sim._var ("height", 182)
            sim._var ("job", _("Salvavidas"))

        if "jam" not in globals () or not isinstance (jam, TGCharacter):
            jam = TGCharacter ("Jamaal", color = "#8b7b7b", lname = "Washington")
            jam.roles.addRole (_("colega"))
            jam.roles.addRole (_("el hermano de [sim]"))

        if "sam" not in globals () or not isinstance (sam, TGCharacter):
            sam = TGCharacter ("Samantha", color = "#8f483a", lname = "Washington", nick = "Sam")
            sam._var ("birthday", "2021-01-17")
            sam._var ("age", 41)
            sam._var ("height", 175)
            sam.roles.addRole (_("madre de [sim] y [jam]"))
            sam.roles.addRole (_("amiga de la familia"))
            jam.roles.addRole (_("el hijo de [sam]"))
            sim.roles.addRole (_("la hija de [sam]"))
            sim.roles.addRole (_("la hermana de [jam]"))
            sam._var ("traits, mental", _("Adicta al trabajo"))

        if "mad" not in globals () or not isinstance (mad, TGCharacter):
            mad = TGCharacter ("Madison", color ="#c4ff33", lname = "Chang", nick="Maddie")
            mad.roles.addRole (_("amiga de [mar]"))
            mad.roles.addRole (_("conocida"))
            mad._var ("usesNick", True)
            mad._var ("birthday", "2021-05-01")
            mad._var ("age", 25)
            mad._var ("height", 181)
            mad._var ("job", _("Empleado de ventas"))

        if "meg" not in globals () or not isinstance (meg, TGCharacter):
            meg = TGCharacter ("Megan", color = "#d4b34a", lname = "Peel", nick = "Meg")
            meg.roles.addRole (_("amiga"))
            meg._var ("birthday", "2021-07-04")
            meg._var ("age", 23)
            meg._var ("height", 177)
            meg._var ("job", _("cantante"))

        if "sca" not in globals () or not isinstance (sca, TGCharacter):
            sca = TGCharacter ("Scarlett", color = "#33f3ff", lname = "Russell")
            sca.roles.addRole (_("conocida"))
            sca.roles.addRole (_("colega de [dap]"))
            sca._var ("birthday", "2021-10-15")
            sca._var ("age", 18)
            sca._var ("height", 181)
            sca._var ("job", _("estudiante"))
            sca._var ("traits, physical", _("personas con discapacidad auditiva"))

        if "scav" not in globals () or not isinstance (scav, TGCharacter):
            scav = TGCharacter (_("Scarlett en el video"), color = "#33f3ff")

        if "sop" not in globals () or not isinstance (sop, TGCharacter):
            sop = TGCharacter ("Sophie")

        if "kim" not in globals () or not isinstance (kim, TGCharacter):
            kim = TGCharacter ("Kim", color = "#f9ff33", lname = "Brown")
            kim.roles.addRole (_("conocida"))
            kim._var ("birthday", "2021-11-03")
            kim._var ("age", 19)
            kim._var ("height", 180)
            kim._var ("job", _("estudiante"))
            kim._var ("job", _("modelo a tiempo parcial"), "add", list)
            kim._var ("job", _("anfitriona a tiempo parcial"), "add", list)

        if "kat" not in globals () or not isinstance (kat, TGCharacter):
            kat = TGCharacter ("Kate", color = "#fc0335", lname = "Moreno")
            kat.roles.addRole (_("conocida"))
            kat._var ("usesNick", True)
            kat._var ("birthday", "2021-12-23")
            kat._var ("age", 20)
            kat._var ("height", 171)
            kat._var ("job", _("estudiante"))

        if "lis" not in globals () or not isinstance (lis, TGCharacter):
            lis = TGCharacter ("Lisa", color = "#ebe7a2", lname = "Selden")
            lis.roles.addRole (_("conocida"))
            lis._var ("birthday", "2021-11-03")
            lis._var ("age", 20)
            lis._var ("height", 175)
            lis._var ("job", _("estudiante"))

        if "deb" not in globals () or not isinstance (deb, TGCharacter):
            deb = TGCharacter ("Deborah", color = "#0324fc", lname = "Selden", nick = "Debbie")
            deb._var ("usesNick", True)
            deb._var ("birthday", "2021-10-26")
            deb._var ("age", 19)
            deb._var ("height", 191)
            deb._var ("job", _("estudiante"))

        if "sai" not in globals () or not isinstance (sai, TGCharacter):
            sai = TGCharacter ("Saira", color = "#d4b34a", lname = "Singh")
            sai.roles.addRole (_("Amiga con beneficios"))
            sai._var ("birthday", "2021-04-21")
            sai._var ("age", 20)
            sai._var ("height", 179)
            sai._var ("job", _("estudiante"))

    ### second batch

        if "kal" not in globals () or not isinstance (kal, TGCharacter):
            kal = TGCharacter ("Kalyani", color = "#af6d16", lname = "Singh", nick = "Kaly")
            sai._var ("birthday", "2021-09-09")
            sai._var ("age", 18)
            sai._var ("height", 171)
            sai._var ("job", _("estudiante"))

        if "pat" not in globals () or not isinstance (pat, TGCharacter):
            pat = TGCharacter ("Patricia", color = "#40bdce", lname = "Robinson", nick = "Patty")
            pat._var ("birthday", "2021-01-02")
            pat._var ("age", 18)
            pat._var ("height", 177)
            pat._var ("job", _("estudiante"))

        if "zoe" not in globals () or not isinstance (zoe, TGCharacter):
            zoe = TGCharacter ("Zoe", color = "#5f40ce", lname = "Perceval")
            zoe._var ("birthday", "2021-05-28")
            zoe._var ("age", 18)
            zoe._var ("height", 174)
            zoe._var ("job", _("estudiante"))

        if "cri" not in globals () or not isinstance (cri, TGCharacter):
            cri = TGCharacter ("Christine", color = "#5f40ce", lname = "Song", nick = "Christy")
            cri._var ("birthday", "2021-08-07")
            cri._var ("age", 18)
            cri._var ("height", 162)
            cri._var ("job", _("estudiante"))

        if "nia" not in globals () or not isinstance (nia, TGCharacter):
            nia = TGCharacter ("Nia", color = "#5f40ce", lname = "Serrat")
            nia._var ("birthday", "2021-08-20")
            nia._var ("age", 18)
            nia._var ("job", _("estudiante"))

        if "hai" not in globals () or not isinstance (hai, TGCharacter):
            hai = TGCharacter ("Hailey", color = "#5f40ce", lname = "Jenkinson")
            hai._var ("birthday", "2021-09-03")
            hai._var ("age", 18)
            hai._var ("height", 159)
            hai._var ("job", _("estudiante"))


    ### others

        if "jon" not in globals () or not isinstance (jon, TGCharacter):
            jon = TGCharacter ("Jonas", color = "#663300", lname = "Salinger")
        if "zeu" not in globals () or not isinstance (zeu, TGCharacter):
            zeu      = TGCharacter ("Zeus", color = "#ff9300")
            fzeu     = TGCharacter (_("Puto Gato"), color = "#ff9300")
        gorila   = TGCharacter (_("Gorila"), color = "#285bda")
        guy1     = TGCharacter (_("Tipo 1"))
        guy2     = TGCharacter (_("Tipo 2"))
        jac      = TGCharacter ("Jack", color = "#ff3c33")
        man      = TGCharacter (_("Hombre"), color = "#9f483a")
        mj       = TGCharacter (_("Señora Russell"), color="#31f3ff")
        ton      = TGCharacter ("Tony", color = "#285bda")
        todas    = TGCharacter (_("Todas"), color = "#ff3c33")
        wom      = TGCharacter (_("Mujer"), color = "#f9ff33")
        kev      = TGCharacter ("Kevin", color="#25f3ff")
        pwom     = TGCharacter (_("Mujer Policía"), color="#285bda")
        erc      = TGCharacter ("Eric", color = "#663300")
        gra      = TGCharacter ("Grant", color = "#ffffff")
        gav      = TGCharacter ("Gavin", color = "#669300", lname = "Gates")
        gog      = TGCharacter (_("Grant (o Gavin)"), color = "#ffffff")
        tra      = TGCharacter (_("Transportista"), color = "#ffffff")
        wotv     = TGCharacter (_("Mujer en la TV"), color = "#fb948e")
        matv     = TGCharacter (_("Hombre en la TV"), color = "#4d84e5")
        mara     = TGCharacter (_("Hombre en la Radio"), color = "#663300")
        cho      = TGCharacter (_("Chófer"), color = "#ffffff")
        was      = TGCharacter (_("Camarera"), color = "#ffffff")
        wai      = TGCharacter (_("Camarero"), color = "#ffffff")
        hor      = TGCharacter (_("Horno"), color = "#ffffff")
        if "sol" not in globals () or not isinstance (sol, TGCharacter):
            sol = TGCharacter ("Solomon", color = "#6c0615")
        if "aar" not in globals () or not isinstance (aar, TGCharacter):
            aar = TGCharacter ("Aaron", color = "#62b587", lname = "Aldama")

        myDorm.toggleFamily () # this corrects the relationship depending on patch status, it will not change the value of persistent.family
    python:
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg, kal, pat, zoe, cri, nia, hai ]:
            characterProfile._var ("is known", True)
            characterProfile.initProfileImages ()
            while len (characterProfile.profileImages) < 16:
                characterProfile.addProfileImage ("notAvailable" , False)

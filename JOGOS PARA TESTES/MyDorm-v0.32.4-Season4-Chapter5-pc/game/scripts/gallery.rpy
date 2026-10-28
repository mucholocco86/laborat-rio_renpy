init 100 python:
    # title     ..  the title displayed below the frame
    # label     ..  the replay label
    # girls     ..  girls involved in the scene
    # kinks     ..  involved kinks
    # lewd      ..  the lewdness level of the scene
    #               0   holding hands
    #               10  exploring several positions / activities involving insertion a/v or extreme orgasm in another way
    if not persistent.haveBeenRenamed2:
        persistent.mc = "Mark"
        persistent.mom = "Martha"
        persistent.emm = "Emma"
        persistent.emmNick = "Emm"
        persistent.nor = "Norah"
        persistent.eri = "Erika"
        persistent.eriNick = "Eri"
        persistent.dap = "Daphne"
        persistent.dapNick = "Daph"
        renpy.save_persistent()

    replay_scope = {
        "mc" : TGCharacter (persistent.mc, color = "#9042f5", isMC = True),
        "mcp" : TGCharacter (persistent.mc, color = "#9042f5", what_italic = True, isMC = True),
        "mar" : TGCharacter (persistent.mom, color = "#ebebeb", lname = "Marks", nick = "Martha", isFamily = True),
        "mom" : TGCharacter (persistent.mom, color = "#ebebeb", lname = "Marks", nick = "Martha", isFamily = True),
        "nor" : TGCharacter (persistent.nor, color = "#ab2c49", lname = "Marks", isFamily = True),
        "eri" : TGCharacter (persistent.eri, color = "#7b7b7b", lname = "Marks", nick = persistent.eriNick, isFamily = True),
        "dap" : TGCharacter (persistent.dap, color = "#e85613", lname = "Marks", nick = persistent.dapNick, isFamily = True),
        "emm" : TGCharacter (persistent.emm, color = "#8f497b", lname = "Marks", nick = persistent.emmNick, isFamily = True),
        "dad" : TGCharacter ("Edmund", color = "#ffffff", lname = "Marks", isFamily = True),
        "mee" : TGCharacter ("Olivia", color = "#ffeedd", lname = "Pitt", nick = "Meemaw", usesNick = True),
        "bet" : TGCharacter ("Betty", color = "#8ad8e4", lname = "Cavendish"),
        "ama" : TGCharacter ("Amanda", color = "#3b6e49", lname = "Gilford"),
        "eva" : TGCharacter ("Eva", color = "#abf707", lname = "Gilford"),
        "eil" : TGCharacter ("Eileen", color = "#4fff33", lname = "Lamb"),
        "sam" : TGCharacter ("Samantha", color = "#8f483a", lname = "Washington", nick = "Sam"),
        "kia" : TGCharacter ("Kiara", color = "#b234c9", lname = "Lamb"),
        "oma" : TGCharacter ("Alexia", color = "#285bda", lname = "Martinez", nick = "Alex"),
        "sim" : TGCharacter ("Simone", color = "#8f483a", lname = "Washington"),
        "jam" : TGCharacter ("Jamaal", color = "#8b7b7b", lname = "Washington"),
        "sam" : TGCharacter ("Samantha", color = "#8f483a", lname = "Washington", nick = "Sam"),
        "mad" : TGCharacter ("Madison", color ="#c4ff33", lname = "Chang", nick="Maddie"),
        "meg" : TGCharacter ("Megan", color = "#d4b34a", lname = "Peel", nick = "Meg"),
        "sca" : TGCharacter ("Scarlett", color = "#33f3ff", lname = "Russell"),
        "scav" : TGCharacter (_("Scarlett en el video"), color = "#33f3ff"),
        "sop" : TGCharacter ("Sophie"),
        "kim" : TGCharacter ("Kim", color = "#f9ff33", lname = "Brown"),
        "kat" : TGCharacter ("Kate", color = "#fc0335", lname = "Moreno"),
        "lis" : TGCharacter ("Lisa", color = "#ebe7a2", lname = "Selden"),
        "deb" : TGCharacter ("Deborah", color = "#0324fc", lname = "Selden", nick = "Debbie"),
        "sai" : TGCharacter ("Saira", color = "#d4b34a", lname = "Singh"),
        "jon" : TGCharacter ("Jonas", color = "#663300"),
        "zeu" : TGCharacter ("Zeus", color = "#663300"),
        "sol" : TGCharacter ("Solomon", color = "#6c0615"),
        "kev" : TGCharacter ("Kevin", color="#25f3ff"),
        "mj"  : TGCharacter (_("Señora Russell"), color="#31f3ff"),
        "aar" : TGCharacter ("Aaron", color = "#6c0615"),
        "nia" : TGCharacter (persistent.niaName, color = "#bab55d", lname = "Serrat"),
        "pat" : TGCharacter (persistent.patName, color = "#40bdce", lname = "Robinson", nick = persistent.patNick),
        "cri" : TGCharacter (persistent.criName, color = "#dcf4a7", lname = "Song", nick = persistent.criNick),
        "zoe" : TGCharacter (persistent.zoeName, color = "#5f40ce", lname = "Perceval"),
        "hai" : TGCharacter (persistent.haiName, color = "#7cb2db", lname = "Jenkinson"),
        "kal" : TGCharacter ("Kalyani", color = "#af6d16", lname = "Singh", nick = "Kaly"),
        "gav" : TGCharacter ("Gavin", color = "#669300", lname = "Gates"),
        "olg" : TGCharacter ("Olga", color="#65f3ff"),
        "dam" : TGCharacter("Damien", color="#ffcc80"),
        "carl" : TGCharacter("Carl", color="#ce93d8"),
        "fred" : TGCharacter("Frederic", color="#ef9a9a"),
        "mael" : TGCharacter("Mael", color="#afcc80"),
        "flo" : TGCharacter("Floyd", color="#1e93d8"),
        "vin" : TGCharacter("Vincent", color="#5f9a9a"),
        "cal" : TGCharacter("Caleb", color="#7fcc80"),
        "car" : TGCharacter("Caroline", color="#ff0080"),
        "alb" : TGCharacter("Alba", color="#af0080"),
        "lar" : TGCharacter("Lara", color="#9acfe6"),
        "geo" : TGCharacter("George", color="#36f040"),
        "gid" : TGCharacter("Gideon", color="#36f040"),
        "ass" : TGCharacter(_("Asistente"), color="#0f9a9a"),
        "erc" : TGCharacter ("Eric", color = "#663300"),
        "usn" : Character("Usnavy", color="#0BCDF4"),
        "saa" : TGCharacter ("Saar", color = "#27f5ee"),
        "dec" : Character("Declan", color="#ffcc80"),
        "cl4" : Character(_("Todos los clones"), color="#00cc80"),
        "cl1" : Character("Hank", color="#afcc80"),
        "cl2" : Character("Heinrich", color="#facc80"),
        "cl3" : Character("Hugo", color="#0fcc80"),
        "ces" : TGCharacter("Cesar", color = "#163300"),
        "fra" : TGCharacter("Frank", color = "#363330"),
        "hen" : TGCharacter("Henry", color = "#ff3300"),
        "isr" : TGCharacter("Isard", color = "#e3ff00"),
        "jan" : TGCharacter("Jan", color = "#e3ff00"),
        "kei" : TGCharacter("Keylor", color="#0BCDF4"),
        "ich" : TGCharacter ("Ichigo", color="#ffc300"),
        "AuxReplay" : False,
        "Whatif" : False,
        "weds" : 8,
        "salary" : False,
    }
    emmg = persistent.emm

    gallery_girl_filter = _("All")
    gallery_kink_filter = _("All")
    gallery_items = [
        {
            "title" : _("Renombrar a los personajes de la galería"),
            "image" : "00-rename",
            "label" : "mrS3_renameScene",
            "girls" : [ "Scarlett" , persistent.dap , "Maddie" , persistent.eri , persistent.emm , persistent.mom, persistent.nor ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 30 - Tres chicas para ti"),
            "image" : "c28s001_155a",
            "label" : "c28s001_foursome",
            "girls" : [ "Saira" , "Eileen" , "Alexia" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Lesbian" , "Anal" , "Cowgirl" , "Reverse cowgirl" , "Cunnilingus" , "Cumshot" , "Creampie" , "Handjob" , "Fingering" , "Blowjob" , "Doggy" , "Group sex" , "Topless" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 30 - My Residence - Laoise, Alejandra y Aishwarya"),
            "image" : "c28s001_1000",
            "label" : "c28s001_noFoursome",
            "girls" : [ "Saira" , "Eileen" , "Alexia" ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 30 - Un paseo nocturno"),
            "image" : "c28s002_070c",
            "label" : "c28s002_Kim",
            "girls" : [ "Saira" , "Debbie" , "Lisa" , "Kim" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 30 - Una disculpa pendiente"),
            "image" : "c28s002_100a",
            "label" : "c28s002_SimGrateful",
            "girls" : [ "Simone" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 30 - Muchas cosas por probar"),
            "image" : "c28s003_170a",
            "label" : "c28s003_SimLewd",
            "girls" : [ "Simone" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Cowgirl" , "Cunnilingus" , "Cumshot" , "Creampie" , "Handjob" , "Fingering" , "Blowjob" , "Topless" , "Deep throat"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 30 - My Residence - Nina"),
            "image" : "c28s003_1000",
            "label" : "c28s003_noSimLewd",
            "girls" : [ "Simone" ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Desayuno con dónuts"),
            "image" : "c28s004_065a",
            "label" : "c28s004_MarRing",
            "girls" : [ persistent.mom ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Un trabajo nuevo"),
            "image" : "c28s004_150a",
            "label" : "c28s004_ScaGetsJob",
            "girls" : [ persistent.mom , persistent.dap , "Scarlett" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Un libro, una fiesta, y unos anillos"),
            "image" : "c28s004_250a",
            "label" : "c28s004_DebKiaraTalk",
            "girls" : [ "Kiara" , "Debbie" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Las chicas nuevas"),
            "image" : "c28s005_005b",
            "label" : "c28s005_EriNor",
            "girls" : [ persistent.eri , persistent.nor , persistent.zoeName , persistent.criName , persistent.patName , persistent.haiName , "Kalyani" , persistent.niaName ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Eligiendo vestidos"),
            "image" : "c28s004_500a",
            "label" : "c28s004_LisaDress",
            "girls" : [ "Lisa" , "Eva" , persistent.emm ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Una conversación inesperada"),
            "image" : "c28s005_200a",
            "label" : "c28s005_GavCall",
            "girls" : [ "Eva" , persistent.emm ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Comprando trajes"),
            "image" : "c28s005_350a",
            "label" : "c28s005_AmaMad",
            "girls" : [ "Amanda" , "Maddie" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Una mapa con indicaciones"),
            "image" : "c28s006_730a",
            "label" : "c28s006_Kim",
            "girls" : [ "Kim" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Missionary" , "Cunnilingus" , "Creampie" , "Topless" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - ¿Un universo paralelo?"),
            "image" : "c28s002_230a",
            "label" : "c28s002_Kat",
            "girls" : [ "Kate" , "Samantha" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - My Residence - Meg"),
            "image" : "c28s006_1000",
            "label" : "c28s006_noKimLewd",
            "girls" : [ "Kim" ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Un chófer esperando"),
            "image" : "c28s007_025c",
            "label" : "c28s007_Lis",
            "girls" : [ "Lisa" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Reencuentro"),
            "image" : "c28s007_100a",
            "label" : "c28s007_Kev",
            "girls" : [  ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - Ricos y Famosos"),
            "image" : "c29s001_055c",
            "label" : "c29s001_LisParty",
            "girls" : [ "Lisa" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31/32 - Dr. Princess y Mrs. Hyde"),
            "image" : "c29s002_930pv",
            "label" : "c29s002_LisLewd",
            "girls" : [ "Lisa" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Cowgirl" , "Anal" , "Standing sex" , "Reverse cowgirl" , "Cunnilingus" , "Creampie" , "Topless" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 31 - My Residence - Karen"),
            "image" : "c29s002_1000a",
            "label" : "c29s001_noLis",
            "girls" : [ "Lisa" ],
            "kinks" : [ "No sex" , "My Residence"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - Problema Resuelto"),
            "image" : "c29s003_010a",
            "label" : "c29s003_KatKiss",
            "girls" : [ "Kate" , persistent.mom ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - Pícnic"),
            "image" : "c29s003_180f",
            "label" : "c29s003_KimPicnic",
            "girls" : [ "Kim" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - Una llamada desde Florida"),
            "image" : "c29s004_010a",
            "label" : "c29s004_BetMeeCall",
            "girls" : [ "Kim" , "Betty" , "Meemaw"],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - Café y Planes"),
            "image" : "c29s004_100a",
            "label" : "c29s004_SamMegMarTattoo",
            "girls" : [ persistent.mom , "Samantha" , "Megan"],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - Piscina y Sexo en Grupo"),
            "image" : "c29s006_200d",
            "label" : "c29s006_KiaSim",
            "girls" : [ "Kiara" , "Simone" , persistent.eri ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - La habitación gótica"),
            "image" : "c29s005_235a",
            "label" : "c29s005_EriLewd",
            "girls" : [ persistent.eri ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Blowjob" , "Cunnilingus" , "Standing sex" , "Missionary" , "Creampie" , "Topless" , "Doggy" , "Cowgirl" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - My Residence - Lagertha y Nellie"),
            "image" : "c29s005_045d",
            "label" : "c29s005_noEriLewd",
            "girls" : [ persistent.nor , persistent.eri ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - Madre e Hija"),
            "image" : "c29s005_450d",
            "label" : "c29s005_NorLewd",
            "girls" : [ persistent.eri , persistent.nor ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Blowjob" , "Cunnilingus" , "Standing sex" , "Missionary" , "Creampie" , "Topless" , "Doggy" , "Cowgirl" , "Anal" , "Group sex" , "Lesbian" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 32 - My Residence - Nellie"),
            "image" : "c29s005_045f",
            "label" : "c29s005_noNorLewd",
            "girls" : [ persistent.nor , persistent.eri ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - Más planes"),
            "image" : "c29s006_010d",
            "label" : "c29s006_AmaEmm",
            "girls" : [ persistent.emm , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - El catálogo"),
            "image" : "c29s006_400b",
            "label" : "c29s006_DebEil",
            "girls" : [ "Eileen" , "Debbie" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - Otro Café"),
            "image" : "c29s006_600a",
            "label" : "c29s006_SaiEvaMad",
            "girls" : [ "Eva" , "Maddie" , "Saira" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - ¿Ocultan algo?"),
            "image" : "c29s007_005b",
            "label" : "c29s007_OmaLis",
            "girls" : [ "Lisa" , "Alexia" , "Kate" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - Piscina, DnD, y Amistades"),
            "image" : "c29s007_100b",
            "label" : "c29s007_DapDebSca",
            "girls" : [ "Debbie" , persistent.dap , "Scarlett" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - Lo que todos hacemos antes de dormir"),
            "image" : "c29s007_300a",
            "label" : "c29s007_KiaWatersports",
            "girls" : [ "Kiara" ],
            "kinks" : [ "Lewd" , "Watersports" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - Como dos hermanas"),
            "image" : "c29s009_005a",
            "label" : "c30s001_DapScaLewd",
            "girls" : [ persistent.dap , "Scarlett" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Blowjob" , "Cunnilingus" , "Creampie" , "Topless" , "Doggy" , "Cowgirl" , "Group sex" , "Reverse cowgirl" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 33 - My Residence - Laura y Sky"),
            "image" : "c30s001_1000a",
            "label" : "c30s001_noDapScaLewd",
            "girls" : [ persistent.dap , "Scarlett" ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 34 - Amanda y sus tests"),
            "image" : "c30s002_150a",
            "label" : "c30s002_pregnancyTests",
            "girls" : [ "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 34 - Beso de buenos días"),
            "image" : "c30s002_265a",
            "label" : "c30s002_KatKiss",
            "girls" : [ "Kate" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 34 - Recogiendo a las chicas"),
            "image" : "c30s002_520d",
            "label" : "c30s002_getEriEilSca",
            "girls" : [ "Eileen" , "Scarlett" , persistent.eri ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 34 - Hay algún secreto ahí"),
            "image" : "c30s002_335a",
            "label" : "c30s002_AfterDinner",
            "girls" : [ "Kate" , "Kim" , "Debbie" , persistent.eri , persistent.emm ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 34 - Una velada sorprendente"),
            "image" : "c30s002_345a",
            "label" : "c30s002_LisSlap",
            "girls" : [ "Lisa" , "Amanda" , "Eva" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 34 - Pesadilla"),
            "image" : "c30s002_475d",
            "label" : "c30s002_SolomonDream",
            "girls" : [ "Scarlett" , "Kiara" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 35 - La acosadora"),
            "image" : "c30s003_040a",
            "label" : "c30s003_KatWakeUp",
            "girls" : [ "Kate" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 35 - Una nueva camarera"),
            "image" : "c30s003_200d",
            "label" : "c30s003_MarShopping",
            "girls" : [ "Scarlett" , "Eileen" , persistent.dap , persistent.mom ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 35 - Hagamos una porno"),
            "image" : "c30s005_005b",
            "label" : "c30s005_EmmLewd",
            "girls" : [ persistent.emm ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Creampie" , "Doggy" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 35 - My Residence - Irma"),
            "image" : "c30s005_1000a",
            "label" : "c30s005_noEmmLewd",
            "girls" : [ persistent.emm ],
            "kinks" : [ "No sex" , "My Residence" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 35 - El rincón de pensar"),
            "image" : "c30s004_005d",
            "label" : "c30s004_Eva",
            "girls" : [ "Eva" , "Lisa" , "Debbie" , persistent.nor , "Amanda"],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - Haciendo planes"),
            "image" : "c30s004_250a",
            "label" : "c30s004_EmmMarEri",
            "girls" : [ persistent.mom , persistent.eri , persistent.emm ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - No te necesitan"),
            "image" : "c30s004_400a",
            "label" : "c30s004_NorGetsBetMee",
            "girls" : [ persistent.nor ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - Taxista"),
            "image" : "c30s004_500b",
            "label" : "c30s004_getJam",
            "girls" : [ "Samantha" , "Alexia" , "Megan" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - El Maestro de Ceremonias"),
            "image" : "c30s006_020a",
            "label" : "c30s006_wedding",
            "girls" : [ "Saira", persistent.mom, persistent.eri, persistent.emm, persistent.nor, persistent.dap, "Scarlett", "Eileen", "Samantha", "Simone", "Alexia", "Eva", "Maddie", "Megan", "Amanda", "Meemaw", "Kate", "Kim", "Debbie", "Lisa", "Betty", "Kiara" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - Bienvenidas y despedidas"),
            "image" : "c30s007_350a",
            "label" : "c30s007_MeeBetAtHome",
            "girls" : [ "Saira", persistent.mom, persistent.eri, persistent.emm, persistent.nor, persistent.dap, "Scarlett", "Eileen", "Samantha", "Simone", "Alexia", "Eva", "Maddie", "Megan", "Amanda", "Meemaw", "Kate", "Kim", "Debbie", "Lisa", "Betty", "Kiara" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - ¿Lesbiana?"),
            "image" : "c31s001_995pv",
            "label" : "c31s001_katLewd",
            "girls" : [ "Kate" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Creampie" , "Cowgirl" , "Food play" ,  "Snowballing" , "Cunnilingus" , "Blowjob" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 36 - Una buena amiga"),
            "image" : "c31s001_010d",
            "label" : "c31s001_noKatLewd",
            "girls" : [ "Kate" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 37 - Un tenedor"),
            "image" : "c31s002_005b",
            "label" : "c31s002_lisFork",
            "girls" : [ "Lisa" ],
            "kinks" : [ "Lewd" , "Missionary" , "Cowgirl" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 37 - Una despedida"),
            "image" : "c31s002_105_lis5",
            "label" : "c31s002_noLis",
            "girls" : [ "Lisa" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 37 - Despedidas y/o noches de bodas con retraso"),
            "image" : "c31s002_105_eri3",
            "label" : "c31s002_firstDayWedding",
            "girls" : [ "Eileen" , persistent.eri , "Eva" , "Kim" , "Megan" , "Saira" , "Samantha" , "Scarlett"],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Missionary" , "Cowgirl" , "Cunnilingus" , "Doggy" , "Fingering" , "Side sex" , "Blowjob" , "Reverse cowgirl" , "Standing sex"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 37 - La última despedidas del día"),
            "image" : "c31s002_105_kia5",
            "label" : "c31s002_kiaChurch",
            "girls" : [ "Kiara"],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Missionary" , "Cowgirl" , "Cunnilingus" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 38 - Alimentando un fetiche"),
            "image" : "c31s003_930dv",
            "label" : "c31s003_norExhibitionists",
            "girls" : [ persistent.nor ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Standing sex" , "Blowjob" , "Cunnilingus" , "Anal sex" , "Exhibitionism" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 38 - Despedidas y/o noches de bodas con retraso"),
            "image" : "c31s002_205e",
            "label" : "c31s002_secondDayWedding",
            "girls" : [ "Alexia" , persistent.dap , "Debbie" , persistent.emm , "Maddie" , persistent.mom , "Meemaw" , "Simone"],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Missionary" , "Cowgirl" , "Cunnilingus" , "Doggy" , "Fingering" , "Side sex" , "Blowjob" , "Reverse cowgirl" , "Standing sex" , "Lactation"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 38 - La despedida final"),
            "image" : "c31s002_250m",
            "label" : "c31s002_farewell",
            "girls" : [ "Alexia" , persistent.dap , "Debbie" , persistent.emm , "Maddie" , persistent.mom , "Meemaw" , "Simone" , "Eileen" , persistent.eri , "Eva" , "Kim" , "Megan" , "Saira" , "Samantha" , "Scarlett" , "Betty" , "Amanda"],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 38 - Despegue"),
            "image" : "c31s004_005d",
            "label" : "c31s004_flight1",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 38 - ¿Un club exclusivo?"),
            "image" : "c31s004_910pv",
            "label" : "c31s004_mileHighClub",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "Lewd" , "Standing sex" , "Vaginal sex"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 38 - Una monja en un avión"),
            "image" : "c31s004_375a",
            "label" : "c31s004_noMileHighClub",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Aterrizaje"),
            "image" : "c31s004_115d",
            "label" : "c31s004_flight2",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Sorpresas"),
            "image" : "c31s005_005a",
            "label" : "c31s005_AarPicksUp",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Tu nueva casa"),
            "image" : "c31s005_250b",
            "label" : "c31s005_houseArrival",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Caroline"),
            "image" : "c31s006_720d",
            "label" : "c31s006_Caroline",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Una visita turística"),
            "image" : "c31s006_550f",
            "label" : "c31s006_baseArrival",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Una reunión complicada"),
            "image" : "c31s006_250a",
            "label" : "c31s006_departmentMeeting",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Una reunión aún más complicada"),
            "image" : "c31s006_180d",
            "label" : "c31s006_cloneMeeting",
            "girls" : [ "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 39 - Decisiones difíciles"),
            "image" : "c31s006_865a",
            "label" : "c31s006_DanielsFate",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 40 - El secreto de Amanda"),
            "image" : "c31s007_095e",
            "label" : "c31s007_AmaTour",
            "girls" : [ "Eva" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 41 - Cirugía"),
            "image" : "c31s007_250a",
            "label" : "c31s007_surgery",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 41 - My Residence - Mandy"),
            "image" : "c32s002_585e",
            "label" : "c32s002_noAma",
            "girls" : [ "Amanda" ],
            "kinks" : [ "No sex" , "My Residence"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 41 - Una Puesta de Sol y unos Corales"),
            "image" : "c32s001_055d",
            "label" : "c32s001_AmaDate",
            "girls" : [ "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Días 41/42 - La primera vez"),
            "image" : "c32s001_900pv",
            "label" : "c32s001_AmaLewd",
            "girls" : [ "Amanda"],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Cowgirl" , "Cunnilingus" , "Doggy" , "Side sex" , "Blowjob" , "Anal" , "Standing sex"],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 43 - Día de Entrenamiento"),
            "image" : "c32s002_350h",
            "label" : "c32s002_trainingCamp",
            "girls" : [ "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 44 - Dirigir una Empresa no es fácil"),
            "image" : "c32s002_090a",
            "label" : "c32s002_choices",
            "girls" : [ "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 46 - La Camioneta"),
            "image" : "c32s003_045a",
            "label" : "c32s003_EmmPickup",
            "girls" : [ "Betty" , persistent.emm ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 47 - Preguntas y Fotos"),
            "image" : "c32s003_150a",
            "label" : "c32s003_JamPics",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 48 - Un Brazo rebelde"),
            "image" : "c32s003_250a",
            "label" : "c32s003_GavArm",
            "girls" : [ "Betty" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 50 - Caroline también tiene Corazón"),
            "image" : "c32s003_510e",
            "label" : "c32s003_redecor",
            "girls" : [  ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 50 - Genética y Dinero"),
            "image" : "c32s003_540a",
            "label" : "c32s003_MaelDrug",
            "girls" : [  ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 52 - Eric"),
            "image" : "c32s004_005f",
            "label" : "c32s004_Eric",
            "girls" : [ "Amanda" , "Eva" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día ?? - Rutina"),
            "image" : "c32s004_115u",
            "label" : "c32s004_routine",
            "girls" : [ "Alexia" , persistent.dap , "Debbie" , persistent.emm , "Maddie" , persistent.mom , "Meemaw" , "Simone" , "Eileen" , persistent.eri , "Eva" , "Kim" , "Megan" , "Saira" , "Samantha" , "Scarlett" , "Betty" , "Amanda" , persistent.nor , "Kate" , "Lisa" , "Kiara"],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Reverse cowgirl" , "Cunnilingus" , "Doggy" , "Side sex" , "Missionary" , "Standing sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 60 - Visitas"),
            "image" : "c32s004_220a",
            "label" : "c32s004_MarSamArrival",
            "girls" : [ persistent.mom , "Samantha" , "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 60 - Una Noche caliente bajo las Estrellas"),
            "image" : "c32s005_030a",
            "label" : "c32s005_MarSamThreesome",
            "girls" : [ persistent.mom , "Samantha" ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Cowgirl" , "Cunnilingus" , "Fingering" , "Anal" , "Lesbian" , "Blowjob" , "Missionary" , "Standing sex" , "Group sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 60 - Durmiendo en el Balcón"),
            "image" : "c32s005_005h",
            "label" : "c32s005_noThreesome",
            "girls" : [ persistent.mom , "Samantha" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 61 - Un Despertar bajo el Sol del Caribe"),
            "image" : "c32s005_820pv",
            "label" : "c32s005_MarLewd",
            "girls" : [ persistent.mom ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Side sex" , "Reverse cowgirl" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 61 - Despertar"),
            "image" : "c32s005_010aa",
            "label" : "c32s005_noMarLewd",
            "girls" : [ persistent.mom ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 61 - Sexo en la piscina"),
            "image" : "c32s005_850pv",
            "label" : "c32s005_SamLewd",
            "girls" : [ persistent.mom ],
            "kinks" : [ "Lewd" , "Vaginal sex" , "Standing sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 61 - My Residence - Sabrina"),
            "image" : "c32s005_425e",
            "label" : "c32s005_noSamLewd",
            "girls" : [ persistent.mom ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Días 61/62 - Visitando la Isla"),
            "image" : "c32s006_010ba",
            "label" : "c32s006_AmaSecTeam",
            "girls" : [ persistent.mom , "Samantha" , "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 64 - La primera Estudiante"),
            "image" : "c32s006_165a",
            "label" : "c32s006_Hailey",
            "girls" : [ persistent.dap , persistent.haiName ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 66 - Gavin"),
            "image" : "c32s006_260c",
            "label" : "c32s006_Gav",
            "girls" : [ "Betty" , "Amanda" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
        {
            "title" : _("Día 69 - Una Secta"),
            "image" : "c32s007_070a",
            "label" : "c32s007_cult",
            "girls" : [ persistent.criName , persistent.niaName , "Eva" ],
            "kinks" : [ "No sex" ],
            "lewd"  : 10    # not used in this gallery
        },
    ]

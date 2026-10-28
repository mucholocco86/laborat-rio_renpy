label questionnaire: # this is the start of part 2 if the game was not imported
    call defineCharacters from _call_defineCharacters_1
    $ renpy.block_rollback()
    $ qm_profiles_disabled= True
    #if "NoT3" not in globals ():
    #    $ NoT3=True
    #if not NoT3:
    #    "Veo que no has cargado una partida de la Parte 1, con lo que tendré que hacerte una batería de preguntas para configurar las variables necesarias para continuar."
    $ renpy.mark_label_seen("c27s006_Teaser")
    $ renpy.mark_label_seen("c27s006_NoThreesome")
    $ persistent.walkthrough = True
    $ aar = TGCharacter ("Aaron", color = "#62b587", lname = "Gilford")

################################################################################
### Kinks

    #mom "Hi, I'm [mar]! With translation it should still be [mar]. [mc] calls me [mar.mc!t]."



    play music "music/Stardust.ogg"
    scene c13s000_pregnancy with dissolve
    jam "Sobre fetiches."
    $ persistent.pregnancy = True
    $ persistent.lactation = False
    $ mc._var ("wantsChildren", False)
    $ persistent.lesbian = False
    $ kat._var ("lesbianContent", False)
    $ persistent.urination = False
    menu qKinkPregnancy:
        jam "¿Quieres activar los embarazos durante la partida? Si no quieres, habrá otra decisión para activar tener hijos entre el fin de juego y el epílogo."
        "Sí.":
            $ persistent.pregnancy = True
        "No.":
            $ persistent.pregnancy = False

    scene c13s000_lactancy with dissolve
    if persistent.pregnancy or not persistent.pregnancy:
        python:
            wt1 = _("Lactancia activada.")
            wt2 = _("Lactancia desactivada.\nSe podrá activar posteriormente para Meemaw.")
        menu qLactation:
            jam "¿Has activado la lactancia para todas las chicas?"
            "¡Por supuesto!" (wt = wt1):
                $ persistent.lactation = True
            "No es uno de mis fetiches." (wt = wt2):
                $ persistent.lactation = False
        $ resetWalkthrough ()

    scene c13s000_wantschildren with dissolve
    menu qWantsChildren:
        jam "¿Quieres tener hijos en el epílogo incluso con las chicas que estés en ruta pero no hayas dejado embarazadas?"
        "Sí":
            $ mc._var ("wantsChildren", True)
        "No.":
            $ mc._var ("wantsChildren", False)

    scene c13s000_lesbian with dissolve
    menu qKinkLesbianContent:
        jam "¿Habilitaste el contenido lésbico en la noche del juego de Verdad o Reto?"
        "Sí.":
            $ persistent.lesbian = True
        "No. Lo bloqueé.":
            $ persistent.lesbian = False

    if not persistent.lesbian:
        scene c13s000_katelesbian with dissolve
        menu qKateLesbianContent:
            jam "Kate parece ser lesbiana. ¿Has cambiado de opinión sobre el contenido lésbico en las escenas de sexo en grupo (siempre con [mc] presente.)?"
            "Desbloquear todo el contenido lésbico durante las escenas de sexo en grupo.":
                python:
                    persistent.lesbian = True
                    kat._var ("lesbianContent", True)
            "Desbloquear el contenido lésbico {b}solo{/b} para las escenas de sexo en grupo en las que aparezca Kate.":
                $ kat._var ("lesbianContent", True)
            "Continuar con el contenido lésbico bloqueado para todas las chicas durante los tríos.":
                pass
    else:
        $ kat._var ("lesbianContent", True)

    scene c13s000_urination with dissolve
    menu qUrination:
        jam "¿Has activado el fetiche de Orina?"
        "Sí.":
            $ persistent.urination = True
        "No.":
            $ persistent.urination = False

    scene c13s000_mc with dissolve
    $ mc.name.first_name = renpy.input (_("Y tú eres mi hermano de otra madre. ¿Quieres cambiarte el nombre?"), default = "Mark")

################################################################################
### Martha - mom

    scene c10s009_215 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    $ mc._var("relationships", 0 , "set")
    $ mar.name.first_name = renpy.input (_("Esta es [mar!t]. ¿Quieres cambiarle el nombre?"), default = "Martha")
    menu qMarthaRouteMarthaSecond:
        "¿Estás en una relación con [mar!t]?"
        "Sí, abrí la relación viendo películas.":
            $ mar._var ("route", True)
            $ mar._var ("routeSecondChance", False)    # this does essientially nothing, but you can keep it for your sanity if you want.
        "Sí, abrí la relación en el café justo antes de ir de compras.":
            $ mar._var ("route", True)
            $ mar._var ("routeSecondChance", True)
        "No, no quiero una relación con [mar!t].":
            $ mar._var ("route", False)                # this does essientially nothing, but you can keep it for your sanity if you want.
            $ mar._var ("routeSecondChance", False)    # this does essientially nothing, but you can keep it for your sanity if you want.

    if mar._var ("route"):
        scene c02s008_099a with dissolve
        $ mc._var ("relationships", 1)
        menu qMarthaFittingRoom:
            "¿Espiaste a [mar!t] en el probador de la tienda de [mad.nick]?"
            "Sí.":
                $ mar._var ("fittingRoom", True)
            "No.":
                pass

        scene c10s009_340pv with dissolve
        menu qMarthaSexName:
            "¿Cómo llamas a [mar!t] durante el sexo?"
            "Mamá":
                python:
                    mar._var ("lewd", True)
                    mar.name.lewd = _("Mamá") # opposite to mar.name.mcLewd, which would be the name mom uses for MC
            "Por su nombre":
                $ mar.name.lewd = mar.name.first_name

        if persistent.pregnancy:
            menu qMarthaPregnant:
                "¿Has dejado embarazada a [mar!t]?"
                "Sí.":
                    $ mar._var ("pregnant", True)
                "No.":
                    pass
        else:
            $ mar._var ("pregnant", False)
    else:
        $ mar._var ("pregnant", False)


################################################################################
### Emma - emm

    scene c01s005_040 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    $ emm.name.first_name = renpy.input (_("Esta es [emm]. ¿Quieres cambiarle el nombre?"), default = "Emma")
    python:
        if emm.name.first_name != "Emma":
            emm.name.nick = emm.name.first_name
    menu qEmmaRouteEmmaSecond:
        "¿Estás en una relación con [emm]?"
        "Sí. La besé en su habitación.":
            $ emm._var ("route", True)
        "Sí. La besé en el jacuzzi.":
            $ emm._var ("route", True)
            $ emm._var ("routeSecondChance", True)
        "No. No quiero una relación con [emm].":
            pass

    if emm._var ("route"):
        scene c07s011_435a with dissolve
        $ mc._var ("relationships", 1, "add")
        menu qEmmaReggaeton:
            "¿Qué le dijiste a [emm] sobre su lenguaje soez durante el sexo?"
            "No me importa mientras tú estés cómoda":
                $ emm._var ("reggaeton", True)
                $ EmmaReggaeton = True
            "No me gusta demasiado":
                pass

        menu qEmmaDaddy:
            "¿Qué le dijiste a [emm] sobre llamarte Papi durante el sexo?"
            "Puedes seguir llamándome Papi si quieres":
                $ emm.name.mcLewd = "Papi"
            "Prefiero que me llames por mi nombre":
                $ emm.name.mcLewd = mc.name.first_name
            "Prefiero que me llames otra cosa":
                python:
                    emm.name.mcLewd = renpy.input ("Me gustaría que me llamaras (Por defecto Papi)", default = _("Papi"))

        scene c11s012_175a with dissolve
        menu qAnalEmmaPlugEmma:
            "¿Activaste alguno de los modos anales con [emm]?"
            "Anal y Plug play activado para [emm].":
                python:
                    emm._var ("anal", True)
                    emm._var ("plug", True)
            "Anal y Plug play desactivado para [emm].":
                pass
            "Anal desactivado para [emm]. Plug play activado.":
                $ emm._var ("plug", True)

        menu qSpankEmma:
            "¿Activaste las cachetadas con [emm]?"
            "Cachetadas activadas para [emm].":
                $ emm._var ("spanking", True)
            "Cachetadas desactivadas para [emm].":
                pass

        if persistent.pregnancy:
            scene c11s012_415c with dissolve
            menu qEmmmaPregnant:
                "¿Has dejado embarazada a [emm]?"
                "Sí.":
                    $ emm._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Norah - nor

    scene c02s004_010 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    $ nor.name.first_name = renpy.input (_("Esta es [nor]. ¿Quieres cambiarle el nombre?"), default = "Norah")
    menu qNorahRouteNorahSecond:
        "¿Estás en una relación con [nor]?"
        "Sí, la dejé entrar en la ducha.":
            $ nor._var ("route", True)
        "Sí, pero no la dejé entrar en la ducha.":
            $ nor._var ("route", True)
            $ nor._var ("routeSecondChance", True)
        "No, no quiero una relación con [nor].":
            pass

    if nor._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            menu qNorahPregnant:
                "¿Has dejado embarazada a [nor]?"
                "Sí.":
                    $ nor._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Erika - eri

    scene c01s005_055 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    $ eri.name.first_name = renpy.input (_("Esta es [eri]. ¿Quieres cambiarle el nombre?"), default = "Erika")
    python:
        if eri.name.first_name != "Erika":
            eri.name.nick = eri.name.first_name
    menu qErikaRouteErikaSecondErikaThird:
        "¿Estás en una relación con [eri]?"
        "Sí, Jack y yo nos peleamos en el baño.":
            $ eri._var ("route", True)
        "Sí, Jack me pegó en la puerta del club. Después le dije la verdad a [eri] sobre las fotos.":
            $ eri._var ("route", True)
            $ eri._var ("routeSecondChance", True)
        "Sí, Jack me pegó en la puerta del club. Después le mentí a [eri] sobre las fotos.\nHasta la sauna no estuvimos en una relación.":
            $ eri._var ("route", True)
            $ eri._var ("routeThirdChance", True)
        "No, no quiero una relación con [eri].":
            pass

    menu qTakeErikaWork6:
        "¿Llevaste a [eri] al trabajo el primer domingo?"
        "Sí. Para librarme de lavar los platos.":
            $ eri._var ("broughtToWorkOnDay6", True)
        "Sí. Mientras lavaba los platos se le averió el coche a [nor].":
            pass

    if eri._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            menu qErikaPregnant:
                "¿Has dejado a [eri] embarazada?"
                "Sí.":
                    $ eri._var ("pregnant", True)
                "No.":
                    pass
    if nor._var("pregnant"):
        scene c10s006_230a with dissolve
        menu qErikaKnowsNorahPregnancy:
            "¿[eri] sabe del embarazo de [nor]?"
            "Sí.":
                $ eri._var ("knowsNorahPregnancy", True)
            "No.":
                pass



################################################################################
### Daphne - dap - Part A

    scene c01s005_035 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    $ dap.name.first_name = renpy.input (_("Esta es [dap]. ¿Quieres cambiarle el nombre?"), default = "Daphne")
    python:
        if dap.name.first_name != "Daphne":
            dap.name.nick = dap.name.first_name

################################################################################
### Daphne - dap + Scarlett - sca

    scene c02s001_015 with dissolve
    menu qDaphneScarlettRouteDaphneRouteScarlettRoute:
        "¿Enseñaste a [dap] y Scarlett a besar en lecciones conjuntas?"
        "Sí.":
            $ dap._var ("route", True)
            $ sca._var ("route", True)
            $ mc._var ("routeDapSca", True)
        "No.":
            pass

################################################################################
### Daphne - dap - Part B

    if not mc._var ("routeDapSca"):
        scene c04s006_035 with dissolve
        menu qDaphneRouteDaphneSecond:
            "¿Aceptaste darle clases por separado a [dap]?"
            "Sí.":
                $ dap._var ("route", True)
                $ dap._var ("routeSecondChance", True)
            "No.":
                pass

    if dap._var ("route"):
        scene c05s010_057 with dissolve
        menu qDaphneRomance:
            "¿Qué tipo de relación empezaste con [dap]?"
            "Romance. Ella confesó que estaba enamorada de mí.":
                $ dap._var ("romance", True)
            "Corrupción inversa. Intentó corromperme, ¡como si yo necesitara que me corrompan!":
                pass

    if not mc._var ("routeDapSca") and dap._var ("romance"):
        scene c09s003_025 with dissolve
        menu qDaphneBreakup:
            "¿Rompiste con [dap] cuando tuviste ocasión?"
            "No.":
                pass
            "Sí.":
                $ dap._var ("route", False)
                $ dap._var ("romance", False)
                $ dap._var ("breakup", True)

    if dap._var ("route"):
        $ mc._var ("relationships", 1, "add")
        #Season 3Q
        menu qDaphnePregnant:
            "¿[dap] está embarazada?"
            "Sí.":
                $ dap._var("pregnant", True)
            "No.":
                $ dap._var("pregnant", False)


################################################################################
### Scarlett - sca

    if not mc._var ("routeDapSca"):
        scene c05s004_090 with dissolve
        menu qScarlettRouteScarlettSecond:
            "¿Aceptaste darle clases por separado a Scarlett?"
            "Sí.":
                $ sca._var ("route", True)
                $ sca._var ("routeSecondChance", True)
            "No.":
                pass

    if not mc._var ("routeDapSca") and sca._var ("route"):
        scene c09s005_020 with dissolve
        menu qScarlettBreakup:
            "¿Rompiste con Scarlett cuando tuviste ocasión?"
            "No.":
                pass
            "Sí.":
                $ sca._var ("route", False)
                $ sca._var ("breakup", True)

    if sca._var ("route"):
        $ mc._var ("relationships", 1, "add")
        scene c11s015_310a with dissolve
        menu qAnalScarlettPlugScarlett:
            "¿Activaste alguno de los modos anales con Scarlett?"
            "Anal y Plug play activado para Scarlett.":
                python:
                    sca._var ("anal", True)
                    sca._var ("plug", True)
            "Anal y Plug play desactivado para Scarlett.":
                pass
            "Anal desactivado para Scarlett. Plug play activado.":
                $ sca._var ("plug", True)

        if persistent.pregnancy:
            menu qScarlettPregnant:
                "¿Has dejado a Scarlett embarazada?"
                "Sí.":
                    $ sca._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Eileen - eil

    scene c04s007_310 with dissolve
    menu qEileenRouteEileenSecond:
        "¿Estás en una relación con Eileen?"
        "Sí, la acompañé al baño en el café.":
            $ eil._var ("route", True)
        "Sí, empecé la relación en el bosque.":
            $ eil._var ("route", True)
            $ eil._var ("routeSecondChance", True)
        "No, no quiero una relación con Eileen.":
            pass

    if eil._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            menu qEileenPregnant:
                "¿Has dejado embarazada a Eileen?"
                "Sí.":
                    $ eil._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Alexia - oma

    scene c10s004_145a with dissolve
    menu:
        "¿Estás en una relación con Alexia?"
        "Sí, acepté ir a entrenar con ella en cuanto me lo propuso.":
            $ oma._var ("route", True)
        "Sí, no acepté ir a entrenar con ella, pero me la encontré cuando salí a correr.":
            $ oma._var ("route", True)
            $ oma._var ("routeSecondChance", True)
        "No. No quiero una relación con Alexia.":
            pass

    if oma._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            menu qAlexiaPregnant:
                "¿Has dejado embarazada a Alexia?"
                "Sí.":
                    $ oma._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Samantha - sam

    scene c08s005_185 with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    menu qSamanthaRouteSamanthaSecond:
        "¿Empezaste una relación con Samantha? Si es así despues te preguntaré si rompiste. Esta pregunta es solo sobre si la empezaste."
        "Sí. Le confesé mis sentimientos mientras me ponía el ungüento en mi habitación.":
            $ sam._var ("route", True)
        "Sí. Le confesé mis sentimientos mientras me ponía el ungüento en su casa.":
            $ sam._var ("route", True)
            $ sam._var ("routeSecondChance", True)
        "No. No quiero una relación con Samantha.":
            pass

    if sam._var ("route"):
        scene c08s006_090 with dissolve
        menu qSamanthaNatural:
            "¿Qué le dijiste a Samantha sobre su vello púbico?"
            "Me gusta al natural.":
                $ sam._var ("naturalPubicHair", True)
            "Lo perfiero afeitado.":
                pass

        scene c08s005_620 with dissolve
        menu qSamanthaBreakUp:
            "Empezaste una relación con Samantha, pero ¿la rompiste más tarde durante vuestra cita?"
            "No. No podría hacerle eso.":
                pass
            "Sí, me agobió su pasado.":
                $ sam._var ("route", False)
                $ sam._var ("breakup", True)

    if sam._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            scene c05s005_375 with dissolve
            menu qSamanthaPregnant:
                "¿Has dejado embarazada a Samantha?"
                "Sí.":
                    $ sam._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Simone - sim

    scene c07s009_080 with dissolve
    menu qSimoneRoute:
        "¿Estás en una relación con Simone?"
        "Sí.":
            $ sim._var ("route", True)
        "No. No quiero una relación con Simone.":
            pass

    if sim._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            scene c10s003_145a with dissolve
            menu qSimonePregnant:
                "¿Has dejado embarazada a Simone?"
                "Sí.":
                    $ sim._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Maddie - mad

    scene c09s015_020 with dissolve
    menu qMaddieBlackmail:
        "¿Estás en una relación con Maddie?"
        "Sí.":
            python:
                mad._var ("route", True)
                mad._var ("romance", True)
        "No.":
            pass

    if mad._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if mar._var ("fittingRoom"):
            scene c06s006_080 with dissolve
            python:
                mad._var ("blackmail", True)
                wt1 = _("Maddie Dominante.")
                wt2 = _("Maddie Sumisa.")
                wt3 = _("Romance")
            menu:
                "¿Cómo reaccionaste a su intento de chantaje?"
                "Lo dejamos en un empate." (wt = wt3):
                    $ mad._var ("romance", True)
                "Acepté el chantaje." (wt = wt1):
                    $ mad._var ("dom", True)
                "Le di la vuelta al chantaje." (wt = wt2):
                    $ mad._var ("sub", True)
            $ resetWalkthrough ()
        #Season 3Q
        menu qMaddiePregnant:
            "¿[mad.nick] está embarazada?"
            "Sí.":
                $ mad._var("pregnant", True)
            "No.":
                $ mad._var("pregnant", False)
        $ resetWalkthrough ()


################################################################################
### Megan - meg

    scene c02s013_030c with dissolve
    menu qMeganRoute:
        "¿Estás en una relación con Megan?"
        "Sí.":
            $ meg._var ("route", True)
        "No.":
            pass

    if meg._var ("route"):
        $ mc._var ("relationships", 1, "add")
        if persistent.pregnancy:
            scene c07s008_465 with dissolve
            menu:
                "¿Has dejado embarazada a Megan?"
                "Sí.":
                    $ meg._var ("pregnant", True)
                "No.":
                    pass

################################################################################
### Group and mc

    scene c04s010_065b with dissolve
    menu qc04s010_MC_V:
        "En el juego de Verdad o Reto, ¿qué elegiste?"
        "Verdad.":
            $ mc._var ("truthOrDare", True)
        "Reto.":
            pass

    scene c07s010_005 with dissolve
    menu qEdmundStory:
        "¿Le cogiste el teléfono a tu padre cuando llamó?"
        "Sí.":
            $ mc._var ("edmundsStory", True)
        "No.":
            pass

    scene c08s003_140 with dissolve
    menu qBlackmailJonas:
        "Cuando Jonas, el Decano de la universidad, intentó aprovecharse de [mar!t], ¿qué hiciste?"
        "Amenazar con pegarle":
            pass
        "Marcarte un farol y chantajearle":
            $ jon._var ("blackmailed", True)

    scene c11s004_185e with dissolve
    menu qMCKnowsMeemawSickness:
        "Cuando Tía Betty y [mar!t] estaban hablando en la cocina, ¿te paraste a escuchar a escondidas?"
        "Sí.":
            $ mee._var ("mcKnowsSickness", True)
        "No.":
            pass
    #Season 3Q
    menu qMeemawRoute:
        "¿Estás en una relación con Olivia?"
        "Sí.":
            $ mee._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            pass

    python:
        wt1 = _("Hay algún punto extra con esta opción.")
        wt2 = _("Hay algunas preguntas. 26 preguntas, para ser precisos. ¡Lo siento!")
    scene black with dissolve
    menu:
        "¿Quieres maximizar los valores de las relaciones para todas las estudiantes?"
        "Poner todas las relaciones al máximo" (wt = wt1):
            $ deb.rp (44)
            $ kat.rp (42)
            $ kim.rp (43)
            $ lis.rp (50)
        "Responder todas las preguntas individualmente." (wt = wt2):
            $ deb.rp (0)
            $ kat.rp (0)
            $ kim.rp (0)
            $ lis.rp (0)

            scene c09s010_145 with dissolve
            python:
                wt1 = "[cg]Kim +2[cc]"
                wt2 = "[cr]Kim -1[cc]"
            menu:
                "¿Intentaste ayudar a Kim cuando se cayó en el aeropuerto?"
                "Sí." (wt = wt1):
                    $ kim.rp (+2)
                "No." (wt = wt2):
                    $ kim.rp (-1)
            $ resetWalkthrough ()

            scene c09s010_340 with dissolve
            python:
                wt1 = "[cg]Lisa +1, Debbie +2[cc]"
                wt2 = "[cg]Lisa +2[cc]"
            menu:
                "¿A cual de las dos hermanas te acercaste primero en el aeropuerto?"
                "Acercarte primero a Debbie." (wt = wt1):
                    $ deb.rp (2)
                    $ lis.rp (1)
                "Acercarte primero a Lisa." (wt = wt2):
                    $ lis.rp (2)
            $ resetWalkthrough ()

            scene c09s010_310 with dissolve
            python:
                wt1 = "[cg]Lisa +2, Debbie +1[cc]"
                wt2 = "[cg]Lisa +1, Debbie +2[cc]"
                wt3 = "[cr]Lisa -1, Debbie -1[cc]"
            menu:
                "¿Qué dijiste cuando Lisa te pidió ayuda con las maletas?"
                "Eso es trabajo del botones, ¿no?" (wt = wt1):
                    python:
                        deb.rp (1)
                        lis.rp (2)
                "Déjame mirar lo de la maleta de Debbie." (wt = wt2):
                    python:
                        deb.rp (2)
                        lis.rp (1)
                "Pongo las maletas en el carro y voy a mirar lo de la maleta de Debbie." (wt = wt3):
                    python:
                        deb.rp (-1)
                        lis.rp (-1)
            $ resetWalkthrough ()

            scene c09s010_385 with dissolve
            $ wt1 = "[cg]Debbie +1[cc]"
            menu qLaptopDebbie:
                "¿Te ofreciste a prestarle tu portátil a Debbie cuando le perdieron el equipaje?"
                "Y no te preocupes por el portátil, te puedo dejar el mío." (wt = wt1):
                    python:
                        deb._var ("laptop", True)
                        deb.rp (1)
                "No decir nada":
                    pass
            $ resetWalkthrough ()

            scene c09s010_430 with dissolve
            $ wt1 = "[cg]Lisa +1[cc]"
            menu:
                "¿Te reíste de Lisa (aunque ella no se diera cuenta) haciendo bromas sobre el papel higiénico?"
                "Creo que el papel higiénico es reciclado. *Risa*" (wt = wt1):
                    $ lis.rp (1)
                "La verdad es que no lo sé":
                    pass
            $ resetWalkthrough ()

            scene c09s010_475 with dissolve
            python:
                wt1 = "[cg]Kim +2, Debbie +2, Kate +2[cc]"
                wt2 = "[cr]Kim -1, Debbie -1, Kate -1[cc]"
            menu:
                "¿Defendiste a las chicas cuando los dos críos se metieron con ellas?"
                "Sí." (wt = wt1):
                    python:
                        deb.rp (2)
                        kat.rp (2)
                        kim.rp (2)
                "No." (wt = wt2):
                    python:
                        deb.rp (-1)
                        kat.rp (-1)
                        kim.rp (-1)
            $ resetWalkthrough ()

#            scene c09s010_575b with dissolve
#            python:
#                wt1 = "[cg]Debbie + 5[cc]"
#                wt2 = "[cr]Debbie - 5[cc]"
#            menu:
#                "¿Como reaccionaste cuando Debbie compró el top nuevo en la tienda de Maddie?"
#                "¡Wow, Debbie!" (wt = wt1):
#                    $ deb.rp (5)
#                "No está mal, para quien le gusten las chicas musculosas." (wt = wt2):
#                    $ deb.rp (-5)
#            $ resetWalkthrough ()

#            scene c09s010_585a with dissolve
#            python:
#                wt1 = "[cg]Debbie +5[cc]"
#                wt2 = "[cr]Debbie -2[cc]"
#            menu:
#                "¿Qué dijiste cuando Debbie hizo referencia a que a los chicos no les gusta salir con mujeres más altas?"
#                "A mí me importa más la persona que el físico." (wt = wt1):
#                    $ deb.rp (5)
#                "Sí, normalmente es así." (wt = wt2):
#                    $ deb.rp (-2)
#            $ resetWalkthrough ()

            scene c09s011_045b with dissolve
            python:
                wt1 = "[cg]Lisa + 1, Kate + 1, Debbie + 1[cc]"
                wt2 = "[cr]Lisa - 1, Kate -1, Debbie - 1[cc]"
            menu:
                "Cuando llegasteis a casa, para entrar las maletas, ¿hiciste alguna broma cuando Lisa bromeó (esta vez) sobre ser el botones? ¿O la trataste como a una princesa?"
                "Si quieres dejo las tuyas aquí, Lisa. *Risa*" (wt = wt1):
                    python:
                        deb.rp (1)
                        kat.rp (1)
                        lis.rp (1)
                "No me gustaría que te mancharas el vestido." (wt = wt2):
                    python:
                        deb.rp (-1)
                        kat.rp (-1)
                        lis.rp (-1)
            $ resetWalkthrough ()

            scene c09s013_155a with dissolve
            python:
                wt1 = "[cg]Kate + 1[cc]"
                wt2 = "[cr]Kate - 1[cc]"
            menu:
                "Cuando Kate te preguntó si eras el único hombre de la familia, ¿qué respondiste?"
                "Sí, mi tío Mike murió hace 16 años y [nor] no se ha vuelto a casar." (wt = wt1):
                    $ kat.rp (1)
                "Sí, soy el único hombre pero, sin querer ser maleducado... No creo que sea de tu incumbencia." (wt = wt2):
                    $ kat.rp (-1)
            $ resetWalkthrough ()

            scene c09s013_205 with dissolve
            $ wt1 = "[cg]Kim + 1[cc]"
            menu:
                "Cuando Kim se ofreció a posar para [emm], ¿qué dijiste?"
                "Gracias por prestarte a la sesión de fotos." (wt = wt1):
                    $ kim.rp (1)
                "No decir nada":
                    pass
            $ resetWalkthrough ()

            scene c09s013_275 with dissolve
            python:
                wt1 = "[cg]Lisa + 1[cc]"
                wt2 = "[cr]Lisa - 5[cc]"
            menu:
                "Cuando Lisa te habló de la protesta en la playa, sobre hacer hogeras, y te preguntó si te reías de ella, ¿qué le contestaste?"
                "No, no me estoy riendo de vuestras intenciones, sino de vuestras formas." (wt = wt1):
                    $ lis.rp (1)
                "Es que es irrisorio. Has venido en avión y ahora vas a hacer hogueras." (wt = wt2):
                    $ lis.rp (-5)
            $ resetWalkthrough ()

            scene c09s014_015 with dissolve
            "Cuando Kate comentó que había muchas mujeres guapas en la casa y que te habría sido difícil encontrar novia en el instituo, dijiste que encontraste a Eileen que no desentonaría en la casa."
            $ wt1 = "[cg]Kate +2, Debbie +1[cc]"
            menu:
                "¿Dijiste algo más?"
                "Igual que no desentonáis vosotras." (wt = wt1):
                    python:
                        deb.rp (1)
                        kat.rp (2)
                "No decir nada":
                    pass
            $ resetWalkthrough ()

            scene c10s003_005 with dissolve
            $ wt1 = "[cg]Kate +1, Debbie +1[cc]"
            menu:
                "Cuando llevaste a Kate a la peluquería y a Debbie a la piscina, ¿te ofreciste a recogerlas?"
                "Sí." (wt = wt1):
                    python:
                        deb.rp (1)
                        kat.rp (1)
                "No.":
                    pass
            $ resetWalkthrough ()

            scene c10s007_250a with dissolve
            $ wt1 = "[cg]Lisa +5, Kim +1[cc]"
            menu qEscortLisa:
                "Cuando Lisa estaba nerviosa porque iba a llegar Anthony, ¿Te ofreciste a acompañarla?"
                "Sí." (wt = wt1):
                    python:
                        kim.rp (1)
                        lis.rp (5)
                        lis._var ("escorted", True)
                "No.":
                    pass
            $ resetWalkthrough ()

            scene c10s007_200 with dissolve
            python:
                wt1 = "[cg]Kim +3, Lisa +1[cc]"
                wt2 = "[cg]Kim +4[cc], [cr]Lisa -1[cc]"
                wt3 = "[cr]Kim -2[cc], [cg]Lisa +2[cc]"
            menu:
                "Cuando dijiste que [emm] estaba guapa con el nuevo peinado y maquillaje. ¿Dijiste algo más?"
                "Las tres lo sois." (wt = wt1):
                    python:
                        kim.rp (3)
                        lis.rp (1)
                "Igual que lo es Kim." (wt = wt2):
                    python:
                        kim.rp (5)
                        lis.rp (-1)
                "Igual que lo es Lisa." (wt = wt3):
                    python:
                        kim.rp (-2)
                        lis.rp (2)
                "No decir nada":
                    pass
            $ resetWalkthrough ()

            scene c10s009_165b with dissolve
            python:
                wt1 = "[cg]Kate + 1[cc]"
                wt2 = "[cr]Kate - 1[cc]"
            menu:
                "Cuando Kate apareció con el nuevo peinado y su color natural, ¿qué disjiste?"
                "Te queda mejor que el morado" (wt = wt1):
                    $ kat.rp (1)
                "Me gustaba más el morado" (wt = wt2):
                    $ kat.rp (-1)
                "Los dos me gustan por igual.":
                    pass
            $ resetWalkthrough ()

            scene c11s001_235 with dissolve
            $ wt1 = "[cg]Lisa + 3[cc], [cg]Debbie + 2[cc], [cg]Kim + 1[cc]"
            menu:
                "Cuando estabáis corriendo en el bosque, preguntaste por la cita de Lisa. ¿Dijiste algo más?"
                "¿Sabéis si está bien?" (wt = wt1):
                    python:
                        deb.rp (2)
                        kim.rp (1)
                        lis.rp (3)
                "No decir nada":
                    pass
            $ resetWalkthrough ()

            scene c11s001_310a with dissolve
            python:
                wt1 = "[cg]Kim + 3[cc], [cg]Debbie + 1[cc]"
                wt2 = "[cr]Kim - 1[cc], [cr]Debbie - 1[cc]"
            menu:
                "Cuando Kim estuvo a punto de caerse corriendo en el bosque, ¿cómo reaccionaste?"
                "Evitar que Kim se caiga." (wt = wt1):
                    python:
                        deb.rp (1)
                        kim.rp (3)
                "No hacer nada." (wt = wt2):
                    python:
                        deb.rp (-1)
                        kim.rp (-1)
            $ resetWalkthrough ()

            scene c11s001_365 with dissolve
            python:
                wt1 = "[cr]Debbie -5[cc], [cr]Kim -5[cc]"
                wt2 = "[cg]Debbie +1[cc], [cg]Kim +1[cc]"
            menu qCheckGirlsChanging:
                "Cuando Debbie y Kim se estaban cambiando detrás de los arbustos, ¿qué hiciste?"
                "No mirar o dejar de mirar antes de que te pillaran." (wt = wt2):
                    python:
                        deb.rp (1)
                        kim.rp (1)
                "Mirar hasta que te pillaron." (wt = wt1):
                    python:
                        deb.rp (-5)
                        kim.rp (-5)
                        mc._var ("checkGirlsChanging", True)
            $ resetWalkthrough ()

            scene c11s001_455a with dissolve
            python:
                wt1 = "[cg]Kim + 5[cc]"
                wt2 = "[cr]Kim - 1[cc]"
            menu:
                "Cuando Kim dijo que era un bicho raro debido a su piel, ¿qué dijiste?"
                "¿Bicho raro? Para nada." (wt = wt1):
                    $ kim.rp (5)
                "No decir nada." (wt = wt2):
                    $ kim.rp (-1)
            $ resetWalkthrough ()

            python:
                wt1 = "[cg]Lisa + 4[cc], [cg]Debbie + 3[cc], [cg]Kate + 2[cc], [cg]Kim + 2[cc]"
                wt2 = "[cg]Lisa + 2[cc], [cg]Debbie + 1[cc], [cr]Kate - 1[cc], [cr]Kim - 1[cc]"
                wt3 = "[cr]Kate - 2[cc]"
            scene c11s006_185b with dissolve
            menu qListenDebbieLisa:
                "Después de que Lisa llegara con Alexia, ¿te paraste a escuchar la conversación de Debbie y Lisa?"
                "Sí.":
                    $ mc._var ("listenedInDebbieLisa", True)
                    menu:
                        "Cuando Kate te pilló escuchando, ¿qué excusa le diste?"
                        "Sólo intentaba saber si Lisa estaba bien." (wt = wt1):
                            $ deb.rp (3)
                            $ kat.rp (2)
                            $ kim.rp (2)
                            $ lis.rp (4)
                        "Sólo intentaba saber como le había ido la cita a Lisa." (wt = wt2):
                            $ deb.rp (1)
                            $ kat.rp (-1)
                            $ kim.rp (-1)
                            $ lis.rp (2)
                        "Sólo me he parado un momento de camino a mi habitación." (wt = wt3):
                            $ kat.rp (-2)
                "No.":
                    pass
            $ resetWalkthrough ()


            $ wt1 = "[cg]Lisa +3[cc]"
            scene c12s001_110a with dissolve
            menu qHugLisa:
                "¿Abrazaste a Lisa después de su pesadilla?"
                "Sí." (wt = wt1):
                    python:
                        lis.rp (3)
                        lis._var ("hug", True)
                "No hacer nada.":
                    pass
            $ resetWalkthrough ()

            python:
                wt1 = "[cg]Kim + 10[cc], [cg]Kate +4[cc], [cg]Debbie +6[cc], [cg]Lisa +2[cc]"
                wt2 = "[cr]Kim - 30[cc], [cr]Kate -6[cc], [cr]Debbie -10[cc], [cr]Lisa -4[cc]"
                if kim.rp () < 14:
                    wt2 = wt2 + _("\n[cr]Tendrás que conseguir puntos en la última gran decisión con Kim para poder abrir la ruta.[cc]")
                elif kim.rp () < 9:
                    wt2 = wt2 + _("\n[cr]Tendrás que conseguir el 84-100\% de los puntos que quedan con Kim para poder abrir la ruta.[cc]")
                else:
                    wt2 = wt2 + _("\n[cr]No podrás abrir la ruta con Kim.[cc]")
            scene c12s001_185a with dissolve
            menu qKimMakeup:
                "¿Qué le dijiste a Kim sobre su maquillaje corporal?"
                "Debería mostrarse como es." (wt = wt1):
                    $ deb.rp (6) # might need to switch to this
                    $ kat.rp (4)
                    $ kim.rp (10)
                    $ lis.rp (2)
                "Debería esconder su condición." (wt = wt2):
                    $ kim._var ("makeup", True)
                    $ deb.rp (-10)
                    $ kat.rp (-6)
                    $ kim.rp (-30)
                    $ lis.rp (-4)
            $ resetWalkthrough ()

#            if deb._var ("laptop"):
#                scene c12s001_335a with dissolve
#                python:
#                    wt1 = "[cg]Debbie + 1[cc]"
#                    wt2 = ""
#                    if deb.rp_score <= -26:
#                        wt2 = _("[cr]No podrás abrir la ruta con Debbie[cc]")
#                menu:
#                    "Llamaste Deb a Debbie y le sorprendió. ¿Qué razón le diste para hacerlo?"
#                    "Suelo acortar el nombre de las personas que me caen bien." (wt = wt1):
#                        $ deb.rp (1)
#                    "Lo siento, se me ha escapado." (wt = wt2):
#                        pass
#                $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_155a with dissolve
            menu:
                "¿Qué le dijiste a [kat] cuando comentó que tú saliendo con [eil] en el instituto dabas una esperanza a los gordos?"
                "Podrías conseguir a cualquier chica que quisieras." (wt="{color=#0f0}Kate + 5{/color}"):
                    $ kat.rp (5)
                "Sólo fue un golpe de suerte." (wt="{color=#f00}Kate - 3{/color}"):
                    $ kat.rp (-3)
            $ resetWalkthrough()
            #Season 3Q
            scene c14s005_005mc with dissolve
            $ wt1 = "[cg]Kim +5[cc]"
            $ wt2 = ""
            menu qKimBeach:
                "¿Qué le dijiste a [kim] cuando te tocó bailar en la playa?"
                "¿Quieres que les demos un espectáculo?"  (wt = wt1):
                    $ kim.rp (5)
                "Déjame el escenario y riéte de mí mientras bailo." (wt=wt2):
                    pass
            $ resetWalkthrough()
            #Season 3Q
            $ Aux = True
            $ Aux2 = True
            $ wt1 = "Kim + 6"
            $ wt2 = "Kate + 8"
            $ wt3 = "Lisa + 4"
            $ wt4 = "Debbie + 10"
            $ wt5 = "Kim + 6, Kate + 8, Lisa + 4, Debbie + 10"
            while Aux2:
                menu qBeachKisses:
                    "¿A quién besaste en la playa?"
                    "A Kim. Podrás elegir más si quedan más chicas disponibles." (wt=wt1) if not kim._var ("kissedBeach"):
                        $ kim.rp (6)
                        $ Aux = False
                        $ kim._var ("kissedBeach" , True)
                    "A Kate. Podrás elegir más si quedan más chicas disponibles." (wt=wt2) if not kat._var ("kissedBeach"):
                        $ kat.rp (8)
                        $ Aux = False
                        $ kat._var ("kissedBeach" , True)
                    "A Lisa. Podrás elegir más si quedan más chicas disponibles." (wt=wt3) if not lis._var ("kissedBeach"):
                        $ lis.rp (4)
                        $ Aux = False
                        $ lis._var ("kissedBeach" , True)
                    "A Debbie. Podrás elegir más si quedan más chicas disponibles." (wt=wt4) if not deb._var ("kissedBeach"):
                        $ deb.rp (10)
                        $ Aux = False
                        $ deb._var ("kissedBeach" , True)
                    "Besarlas a todas." (wt=wt5) if Aux:
                        $ kim.rp (6)
                        $ kat.rp (8)
                        $ lis.rp (4)
                        $ deb.rp (10)
                        $ kim._var ("kissedBeach" , True)
                        $ kim._var ("kissedBeach" , True)
                        $ kim._var ("kissedBeach" , True)
                        $ kim._var ("kissedBeach" , True)
                        $ Aux2 = False
                    "A ninguna más.":
                        $ Aux2 = False
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s010_575b with dissolve
            $ wt1 = "Debbie + 10."
            $ wt2 = ""
            menu qDebbieFlower:
                "¿Le pusiste una flor en el pelo a Debbie?"
                "Sí." (wt=wt1):
                    $ deb._var ("flower", True)
                "No." (wt=wt2):
                    pass
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_275 with dissolve
            $ wt1 = "Lisa + 5."
            $ wt2 = ""
            menu qLisaAnthony:
                "¿Qué le dijiste a Lisa cuando quiso hablarte de Anthony durante la primera cena con Amanda?"
                "Si es importante para ti, es importante para mí." (wt = wt1):
                    $ lis.rp (5)
                "Cuéntamelo, luego decidimos si era importante." (wt = wt2):
                    pass
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_155a with dissolve
            $ wt1 = "Kate +5"
            $ wt2 = ""
            menu qKateLakeInvitation:
                "¿Invitaste a Kate a subir corriendo al lago?"
                "Sí." (wt = wt1):
                    $ kat.rp (5)
                "No." (wt = wt2):
                    pass
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_155a with dissolve
            $ wt1 = "Kate +10"
            $ wt2 = ""
            menu qKateHit:
                "¿Le tiraste los trastos a Kate durante la fiesta en el Jazz Corner?"
                "Sí." (wt = wt1):
                    $ kat.rp (10)
                "No." (wt = wt2):
                    pass
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_275 with dissolve
            $ wt1 = "Lisa +5"
            $ wt2 = "Lisa -25"
            menu qLisaDance:
                "¿Bailaste con Lisa en la fiesta en el Jazz Corner?"
                "Sí." (wt = wt1):
                    $ lis.rp (5)
                "No." (wt = wt2):
                    $ lis.rp (-25)
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_275 with dissolve
            $ wt1 = "Lisa +10"
            $ wt2 = ""
            menu qLisaPolitics:
                "¿Animaste a Lisa a que se metiera en política?"
                "Sí." (wt = wt1):
                    $ lis.rp (10)
                "No." (wt = wt2):
                    pass
            $ resetWalkthrough ()
            #Season 3Q
            scene c09s013_205 with dissolve
            $ wt1 = "Kim +5"
            $ wt2 = "Kim -5"
            menu qKimDance:
                "¿Bailaste con Kim en la fiesta en el Jazz Corner?"
                "Sí." (wt = wt1):
                    $ kim.rp (5)
                "No." (wt = wt2):
                    $ kim.rp (-5)
            $ resetWalkthrough ()
    $ resetWalkthrough ()
    "Relaciones establecidas en: Kim = [kim.rp_score], Kate = [kat.rps], Lisa = [lis._rp]" #", Debbie = [deb.rp_score]"
    #Season 3Q
    scene c09s010_575b with dissolve
    $ wt1 = ""
    $ wt2 = ""
    menu:
        "¿Estás en una relación con Debbie?"
        "Sí." (wt=wt1):
            $ deb._var ("route", True)
            $ mc._var("relationships", 1, "add")
        "No." (wt=wt2):
            pass
    $ resetWalkthrough ()




################################################################################
### kate - kat
    python:
        wt1 = _("Kate estará más delgada en el Acto III.")
        wt2 = _("Kate mantendrá su figura en el Acto III.")
    scene c11s006_500 with dissolve
    menu qKateSlim:
        "¿Qué hiciste cuando Kate te contó sus problemas de azúcar en la sangre?"
        "Convencer a Kate para hacer más deporte y comer más sano." (wt = wt1):
            $ kat._var ("slim", True)
        "Convencer a Kate SOLO para hacer más deporte." (wt = wt2):
            pass
    $ resetWalkthrough ()

################################################################################
### Saira - sai

    scene c11s005_135a with dissolve
    menu:
        "Durante la videoconferencia con Saira, ¿seguiste escuchando cuando ella pensó que había colgado?"
        "Sí.":
            $ sai._var ("listen", True)
        "No.":
            pass
    #Season 3Q
    menu qSairaRoute:
        "¿Estás en una relación con [sai]?"
        "Sí.":
            $ sai._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ sai._var("route", False)
    #Season 3Q
    if sai._var("route"):
        menu qSairaPregnancy:
            "¿[sai] está embarazada?"
            "Sí.":
                $ sai._var("pregnant", True)
            "No.":
                $ sai._var("pregnant", False)
        menu qSairaChance:
            "¿Cuándo empezaste la relación con Saira?"
            "En el aeropuerto.":
                pass
            "En mi habitación.":
                $ sai._var ("routeSecondChance", True)

#########################################
### Kiara
    #Season 3Q
    scene c19s005_400a with dissolve
    menu qKiaraRoute:
        "¿Estás en una relación con [kia]?"
        "Sí.":
            $ kia._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ kia._var("route", False)

###############################################
### DnD
    #Season 3Q
    scene c20s002_330a with dissolve
    menu qBeagan:
        "Durante la partida de DnD, ¿tuviste sexo con el Beagan, el hada de Scarlett?"
        "Sí.":
            $ sca._var ("rejectedBeagan" , False)
        "No.":
            $ sca._var ("rejectedBeagan" , True)
    if not sca._var("rejectedBeagan"):
        scene c20s003_365a with dissolve
        menu qPia:
            "Durante la partida de DnD, ¿tuviste sexo con el Pia, la semielfa de [dap]?"
            "Sí.":
                $ dap._var ("rejectedPia" , False)
            "No.":
                $ dap._var ("rejectedPia" , True)
        scene c20s003_640a with dissolve
        menu qPaulaAelia:
            "Durante la partida de DnD, ¿tuviste un trío con el Paula y Aelia, el ángel de [emm] y el demonio de [eri]?"
            "Sí.":
                $ mc._var ("rejectedAeliaPaula" , False)
            "No.":
                $ mc._var ("rejectedAeliaPaula" , True)


#############################################
### Others
    scene black with dissolve
    menu qAnthony:
        "Mientras comías con [eil] escuchaste a alguien hablar por teléfono."
        "Te giras a mirar quién es":
            $ mc._var ("knowsAnthony", True)
        "No es asunto tuyo":
            $ mc._var ("knowsAnthony", False)

    call updateRoles from _call_updateRoles_1
################################################################################
#### Season 3 questions
    call s3q from _call_s3q


################################################################################
### Settings
    scene black with dissolve
    menu qWalkthrough:
        "¿Quieres activar el Walkthrough? Mostrará información adicional para algunas de preguntas."
        "Sí.":
            $ persistent.walkthrough = True
        "No.":
            $ persistent.walkthrough = False

    if hasPatch:
        menu qFamilyPatch:
            "¿Quieres jugar con el parche familiar?"
            "Sí.":
                $ persistent.family = True
            "No.":
                $ persistent.family = False
    else:
        $ persistent.family = False

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


    stop music fadeout (1.5)
    $ renpy.mark_label_seen("c27s006_Teaser")
    $ renpy.mark_label_seen("c27s006_NoThreesome")
    $ qm_profiles_disabled = False
    return

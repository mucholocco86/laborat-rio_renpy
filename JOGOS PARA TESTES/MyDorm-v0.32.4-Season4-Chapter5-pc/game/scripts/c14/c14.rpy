label c14:
    python:
        if "MarthaPregnant" in globals ():
            mar._var("pregnant", MarthaPregnant)
            del MarthaPregnant
        if "MeganRoute" in globals ():
            meg._var("route", MeganRoute)
            del MeganRoute
        if "MeganPregnant" in globals ():
            meg._var("pregnant", MeganPregnant)
            del MeganPregnant
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
            characterProfile._var("is known", True)
            characterProfile.initProfileImages ()
            while len (characterProfile.profileImages) > 0:
                characterProfile.profileImages.pop (0) # first remove
        oma.addProfileImage ("alexia_0")
        oma.addProfileImage ("notAvailable")
        oma.addProfileImage ("notAvailable")
        oma.addProfileImage ("alexia_3")
        oma.addProfileImage ("alexia_4")
        oma.addProfileImage ("notAvailable")
        oma.addProfileImage ("notAvailable")
        oma.addProfileImage ("notAvailable")
        oma.addProfileImage ("alexia_8", ["route", "itchio"])
        ama.addProfileImage ("amanda_0")
        ama.addProfileImage ("amanda_1")
        bet.addProfileImage ("betty_0")
        bet.addProfileImage ("notAvailable")
        bet.addProfileImage ("notAvailable")
        bet.addProfileImage ("betty_3")
        bet.addProfileImage ("betty_4")
        dap.addProfileImage ("daphne_0")
        dap.addProfileImage ("daphne_1")
        dap.addProfileImage ("daphne_2")
        dap.addProfileImage ("daphne_3")
        dap.addProfileImage ("notAvailable")
        dap.addProfileImage ("daphne_5")
        dap.addProfileImage ("notAvailable")
        dap.addProfileImage ("notAvailable")
        dap.addProfileImage ("daphne_8", ["route", "itchio"])
        deb.addProfileImage ("deborah_0")
        deb.addProfileImage ("deborah_1")
        deb.addProfileImage ("deborah_2")
        deb.addProfileImage ("deborah_3")
        eil.addProfileImage ("notAvailable")
        eil.addProfileImage ("notAvailable")
        eil.addProfileImage ("notAvailable")
        eil.addProfileImage ("eileen_3")
        eil.addProfileImage ("eileen_4")
        eil.addProfileImage ("notAvailable")
        eil.addProfileImage ("notAvailable")
        eil.addProfileImage ("notAvailable")
        eil.addProfileImage ("eileen_8", ["route", "itchio"])
        emm.addProfileImage ("emma_0")
        emm.addProfileImage ("emma_1")
        emm.addProfileImage ("emma_2")
        emm.addProfileImage ("emma_3")
        emm.addProfileImage ("emma_4")
        emm.addProfileImage ("emma_5")
        emm.addProfileImage ("notAvailable")
        emm.addProfileImage ("emma_7", ["route", "itchio"])
        emm.addProfileImage ("emma_8", ["route", "itchio"])
        eri.addProfileImage ("erika_0")
        eri.addProfileImage ("erika_1")
        eri.addProfileImage ("notAvailable")
        eri.addProfileImage ("erika_3")
        eri.addProfileImage ("erika_4")
        eri.addProfileImage ("erika_5")
        eri.addProfileImage ("notAvailable")
        eri.addProfileImage ("notAvailable")
        eri.addProfileImage ("erika_8", ["route", "itchio"])
        eva.addProfileImage ("eva_0")
        eva.addProfileImage ("eva_1")
        kat.addProfileImage ("kate_0")
        kia.addProfileImage ("kiara_0")
        kia.addProfileImage ("notAvailable")
        kia.addProfileImage ("notAvailable")
        kia.addProfileImage ("notAvailable")
        kia.addProfileImage ("kiara_4")
        kim.addProfileImage ("kim_0")
        kim.addProfileImage ("notAvailable")
        kim.addProfileImage ("kim_2")
        kim.addProfileImage ("kim_3")
        lis.addProfileImage ("lisa_0")
        mad.addProfileImage ("maddie_0")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("notAvailable")
        mad.addProfileImage ("maddie_8")
        mar.addProfileImage ("martha_0")
        mar.addProfileImage ("martha_1", "route")
        mar.addProfileImage ("martha_2")
        mar.addProfileImage ("martha_3")
        mar.addProfileImage ("martha_4")
        mar.addProfileImage ("martha_5")
        mar.addProfileImage ("notAvailable")
        mar.addProfileImage ("martha_7")
        mar.addProfileImage ("martha_8", ["route", "itchio"])
        meg.addProfileImage ("megan_0")
        meg.addProfileImage ("notAvailable")
        meg.addProfileImage ("notAvailable")
        meg.addProfileImage ("notAvailable")
        meg.addProfileImage ("megan_4")
        meg.addProfileImage ("notAvailable")
        meg.addProfileImage ("notAvailable")
        meg.addProfileImage ("notAvailable")
        meg.addProfileImage ("megan_8")
        nor.addProfileImage ("norah_0")
        nor.addProfileImage ("norah_1")
        nor.addProfileImage ("norah_2")
        nor.addProfileImage ("norah_3")
        nor.addProfileImage ("notAvailable")
        nor.addProfileImage ("norah_5")
        nor.addProfileImage ("notAvailable")
        nor.addProfileImage ("norah_7")
        nor.addProfileImage ("norah_8", ["route", "itchio"])
        mee.addProfileImage ("olivia_0")
        mee.addProfileImage ("olivia_1")
        sai.addProfileImage ("saira_0")
        sai.addProfileImage ("saira_1")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("notAvailable")
        sai.addProfileImage ("saira_8")
        sam.addProfileImage ("samantha_0")
        sam.addProfileImage ("samantha_1")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("samantha_4")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("notAvailable")
        sam.addProfileImage ("samantha_7", ["route", "itchio"])
        sam.addProfileImage ("samantha_8", ["route", "itchio"])
        sca.addProfileImage ("scarlett_0")
        sca.addProfileImage ("scarlett_1")
        sca.addProfileImage ("scarlett_2")
        sca.addProfileImage ("notAvailable")
        sca.addProfileImage ("notAvailable")
        sca.addProfileImage ("scarlett_5")
        sca.addProfileImage ("notAvailable")
        sca.addProfileImage ("scarlett_7", ["route", "itchio"])
        sca.addProfileImage ("scarlett_8", ["route", "itchio"])
        sim.addProfileImage ("simone_0")
        sim.addProfileImage ("simone_1")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("notAvailable")
        sim.addProfileImage ("simone_8", ["route", "itchio"])
    if sam._var("route"):
        call c14s001_ContinuationSam from _call_c14s001_ContinuationSam
    else:
        call c14s001_ContinuationNoSam from _call_c14s001_ContinuationNoSam
    if eri._var("routeSecondChance") or eri._var("routeThirdChance"):
        $ eri._var("route", True)
    call c14s002_Pool from _call_c14s002_Pool
    call c14s003_SairaChat from _call_c14s003_SairaChat
    call c14s004_ToTheBeach from _call_c14s004_ToTheBeach
    call c14s005_BallGame from _call_c14s005_BallGame
    call c14s006_Christmas from _call_c14s006_Christmas
    call c14s007_MaddieDnD from _call_c14s007_MaddieDnD
    return
label c14s001_ContinuationSam:
    if _in_replay:
        $ mc._var("relationships", 1, intention = "set")
        call mrS3_sim_route from _call_mrS3_sim_route_11
        call mrS3_sam_blackPanther from _call_mrS3_sam_blackPanther_3
        if sim._var("route"):
            menu:
                "¿En cuántas relaciones estabas en ese momento?"
                "2, sólo [sam] y [sim]":
                    $ mc._var("relationships", 2, intention = "set")
                "3":
                    $ mc._var("relationships", 3, intention = "set")
                "4":
                    $ mc._var("relationships", 4, intention = "set")
                "5":
                    $ mc._var("relationships", 5, intention = "set")
                "6":
                    $ mc._var("relationships", 6, intention = "set")
                "7":
                    $ mc._var("relationships", 7, intention = "set")
                "8":
                    $ mc._var("relationships", 8, intention = "set")
                "9":
                    $ mc._var("relationships", 9, intention = "set")
                "10":
                    $ mc._var("relationships", 10, intention = "set")
                "11":
                    $ mc._var("relationships", 11, intention = "set")
                "12":
                    $ mc._var("relationships", 12, intention = "set")
                "13":
                    $ mc._var("relationships", 13, intention = "set")
    call BlinkXP("c14s001_005", "h") from _call_BlinkXP_407
    play music ("music/Epic-Adventure-Action.ogg")
    sim "¿Qué estás haciendo, Mamá?"
    if not itchio:
        call BlinkXP("c14s001_010", "h") from _call_BlinkXP_408
    else:
        scene itchio with dissolve
    sam "No es lo que parece..."
    $ renpy.notify ("Profile image unlocked")
    call BlinkXP("c14s001_015", "d") from _call_BlinkXP_409
    if sim._var("route"):
        sim "No, claro. Estar desnuda sentada encima de la polla de mi novio en el sofá no es lo que parece."
    else:
        sim "No, claro. Estar desnuda sentada encima de la polla de [mc] en el sofá no es lo que parece."
    if not sam._var("naturalPubicHair"):
        scene c14s001_020a with dissolve
        sim "Si hasta te has depilado..."
    if not itchio:
        call BlinkXP("c14s001_025", "d") from _call_BlinkXP_410
    else:
        scene itchio with dissolve
    sam "[sim], puedo explicarlo..."
    call BlinkXP("c14s001_030", "d") from _call_BlinkXP_411
    sim "Por supuesto, que puedes. [mc] ha venido a tomar té y pastitas, os habéis tirado el té por encima y os habéis tenido que desnudar, ¿verdad?"
    sim "Estoy en shock... tu sabías lo que [mc] significaba para mí..."
    if sim._var("route"):
        mc "[sim], ya te dije que..."
        call BlinkXP("c14s001_035", "d") from _call_BlinkXP_412
        sim "¿Y tú? ¿Tú lo sabías...?"
        sim "Claro que lo sabías, que tonterías estoy diciendo... tienes que pasártelo de puta madre follándonos a las dos..."
        mc "[sim], te dije que podía haber otras chicas..."
        call BlinkXP("c14s001_040", "d") from _call_BlinkXP_413
        sim "Sí, pero no me dijiste que una de ellas era mi madre..."
        if not itchio:
            scene c14s001_045AnBlink with dissolve #adBlink
        else:
            scene itchio with dissolve
        sam "Espera... espera... ¿Tu novio? ¿Estáis saliendo?"
        call BlinkXP("c14s001_050", "d") from _call_BlinkXP_414
        sim "Sí, Mamá, o lo estábamos hasta hace dos minutos..."
        call BlinkXP("c14s001_055", "d") from _call_BlinkXP_415
        sam "¿Y qué es eso de que te estás follando a las dos?"
        if not itchio:
            call BlinkXP("c14s001_055b", "h") from _call_BlinkXP_416
        else:
            scene itchio with dissolve
        sam "{b}¿Te estás follando a mi niña?{/b}"
        mc "[sam.nick]..."
        if not itchio:
            call BlinkXP("c14s001_060", "h") from _call_BlinkXP_417
        else:
            scene itchio with dissolve
        sam "{b}¡Fuera de mi casa!{/b}"
        mc "[sam.nick], déjame hablar..."
        if not itchio:
            call BlinkXP("c14s001_065", "d") from _call_BlinkXP_418
        else:
            scene itchio with dissolve
        sam "¡No quiero oírte! Nos has engañado a las dos, a la una con la otra... no quiero volver a verte aquí..."
        sam "¡Y además te has aprovechado de mi niña!"
        mc "[sam.nick], no os he engañado a ninguna..."
        if not itchio:
            call BlinkXP("c14s001_060", "h") from _call_BlinkXP_419
        else:
            scene itchio with dissolve
        sam "{b}¡Fuera... de... mi... puta... casa!{/b}"
        call BlinkXP("c14s001_070", "d") from _call_BlinkXP_420
        sim "No. También es mi casa y quiero que se quede."
        if not itchio:
            call BlinkXP("c14s001_075", "d") from _call_BlinkXP_421
        else:
            scene itchio with dissolve
        sam "No sabes lo que estás diciendo, [sim]. ¡Nos ha engañado a las dos! ¡Lo quiero fuera de aquí! {b}¡Ya!{/b}"
        call BlinkXP("c14s001_080", "d") from _call_BlinkXP_422
        sim "A mí no. A mí me dijo que podía ser que saliera con otras mujeres."
        if not itchio:
            call BlinkXP("c14s001_085", "d") from _call_BlinkXP_423
        else:
            scene itchio with dissolve
        sam "¿Y tú lo aceptaste?"
        call BlinkXP("c14s001_090", "d") from _call_BlinkXP_424
        sim "¡Sí, lo acepté! Y hasta que no hablemos de lo que acabo de ver, sigue siendo mi novio. No tienes derecho a echarlo."
        if not itchio:
            call BlinkXP("c14s001_095", "d") from _call_BlinkXP_425
        else:
            scene itchio with dissolve
        sam "Pero..."
        call BlinkXP("c14s001_100", "d") from _call_BlinkXP_426
        sim "Mamá, siempre me has dicho que si tenía novio podría traerlo a casa sin problemas. Pues aquí está, aunque lo hayas traído tú para follártelo. No voy a dejar que lo eches."
        if not itchio:
            call BlinkXP("c14s001_105", "d") from _call_BlinkXP_427
        else:
            scene itchio with dissolve
        sam "Pero... a mí sí que me ha engañado..."
        mc "No, [sam]. Tú me dijiste que habías hablado con [mar] y que no te importaba compartir..."
        call BlinkXP("c14s001_110", "v") from _call_BlinkXP_428
        sim "¿Qué? ¿Estás saliendo también con tu madre?"
        if not itchio:
            call BlinkXP("c14s001_115", "d") from _call_BlinkXP_429
        else:
            scene itchio with dissolve
        sam "No, fue una conversación hipotética. En aquel momento yo no pensaba que acabaría así... aquí... delante de mi hija..."
        call BlinkXP("c14s001_120", "d") from _call_BlinkXP_430
        sim "¡Ufff! Me había asustado..."
        mc "[sam.nick], no te dije que estaba con otras mujeres por que tú me dijiste eso... lo tomé como que no te importaba..."
        if not itchio:
            call BlinkXP("c14s001_125", "d") from _call_BlinkXP_431
        else:
            scene itchio with dissolve
        sam "¿Cómo no me va a importar? ¿Cómo crees que me puedo sentir sabiendo que sales con mi hija?"
        sam "Hace un momento decías que no las preferías jóvenes..."
        mc "Y no las prefiero jóvenes, [sam.nick]. ¿Todo esto es por el tema de la edad otra vez?"
        mc "Me gusta [sim] y estoy con ella, no por la edad que tiene, sino por quién es. Por cómo es. Y tú me gustas por cómo eres. Me da lo mismo la edad que tengas. Sólo parece importarte a ti."
        stop music fadeout (1.5)
        call BlinkXP("c14s001_130", "d") from _call_BlinkXP_432
        sim "*Risa*"
        if not itchio:
            scene c14s001_135a with dissolve
        else:
            scene itchio with dissolve
        mc "¿Qué pasa?" (multiple=2)
        sam "¿De qué te ríes?" (multiple=2)
        call BlinkXP("c14s001_140", "d") from _call_BlinkXP_433
        sim "Me acabo de dar cuenta de lo ridículo de la situación..."
        play music ("music/On-The-Rise.ogg")
        if not itchio:
            scene c14s001_135b with dissolve
        else:
            scene itchio with dissolve
        mc "No te entiendo" (multiple=2)
        sam "¿Qué te parece ridículo de todo esto?" (multiple=2)
        call BlinkXP("c14s001_145", "d") from _call_BlinkXP_434
        sim "Primero que los dos estáis en pelotas en medio del salón."
        if not itchio:
            call BlinkXP("c14s001_150", "h") from _call_BlinkXP_435
        else:
            scene itchio with dissolve
        sam "¡Oops! ¡[mc], tápate!"
        mc "No es nada que no hayáis visto antes las dos, no quiero interrumpir a [sim] antes de saber el resto de los puntos por lo que la situación le parece ridícula."
        call BlinkXP("c14s001_155", "d") from _call_BlinkXP_436
        sim "Os dais cuenta de que soy yo quien os ha pillado, ¿verdad?"
        if not itchio:
            call BlinkXP("c14s001_160", "d") from _call_BlinkXP_437
        else:
            scene itchio with dissolve
        sam "Sí, claro, pero no veo qué tiene que ver con que sea ridículo."
        mc "Yo creo que sé por dónde va."
        call BlinkXP("c14s001_165", "d") from _call_BlinkXP_438
        sim "Os he pillado yo y me he enfadado, pero parece que la más ofendida seas tú, Mamá. Y estás aquí en pelotas, gesticulando y enfadada..."
        sim "Es gracioso. Quieres echar de {b}nuestra{/b} casa a {b}nuestro{/b} novio, sin tener en cuenta mi opinión. Tan solo porque las dos salimos con él."
        if not itchio:
            call BlinkXP("c14s001_170", "d") from _call_BlinkXP_439
        else:
            scene itchio with dissolve
        sam "Y porque nos ha engañado..."
        call BlinkXP("c14s001_175", "d") from _call_BlinkXP_440
        sim "A mí no, Mamá. Me lo dijo antes de aceptar salir conmigo, o de que yo aceptara salir con él. Y si lo he entendido bien, tú también le diste autorización."
        if not itchio:
            call BlinkXP("c14s001_180", "d") from _call_BlinkXP_441
        else:
            scene itchio with dissolve
        sam "Pero era en un caso hipotético..."
        call BlinkXP("c14s001_185", "d") from _call_BlinkXP_442
        sim "Y la hipótesis se convirtió en realidad. ¿Estarías igual si en vez de conmigo se estuviera acostando con [mar]? Dejemos de lado lo raro que sería. ¿Te enfadaría igual?"
        if not itchio:
            call BlinkXP("c14s001_180", "d") from _call_BlinkXP_443
        else:
            scene itchio with dissolve
        sam "Supongo que no..."
        call BlinkXP("c14s001_190", "d") from _call_BlinkXP_444
        sim "Y si hubiera vuelto con [eil] tampoco, ¿verdad?"
        if not itchio:
            call BlinkXP("c14s001_195", "d") from _call_BlinkXP_445
        else:
            scene itchio with dissolve
        sam "No sé... quizás un poco más..."
        call BlinkXP("c14s001_200", "d") from _call_BlinkXP_446
        sim "Entonces si saliera con [mar] no te enfadarías, con [eil] un poco, y porque sale conmigo te pones hecha una furia."
        sim "¿Puedes ver el patrón? Cuanto más joven sea la chica más te enfadas. Creo que el problema está en que te sientes amenazada por chicas más jóvenes."
        if not itchio:
            call BlinkXP("c14s001_205", "h") from _call_BlinkXP_447
        else:
            scene itchio with dissolve
        sam "{b}¡No es eso!{/b} Con [mar] lo habíamos hablado, aunque solo fuera en broma. Si volviera con [eil]... todos lo esperábamos..."
        sam "¿Pero tú? ¡Tú eres mi niña! No puedo dejar que nadie se aproveche de ti..."
        call BlinkXP("c14s001_210", "d") from _call_BlinkXP_448
        sim "Nadie se está aprovechando, Mamá. Yo estuve de acuerdo. No me imaginaba que también estuviera contigo, pero estuve de acuerdo."
        sim "Y posiblemente siga estándolo una vez acabemos esta conversación y tenga un momento para hablar con mi novio."
        if not itchio:
            call BlinkXP("c14s001_215", "d") from _call_BlinkXP_449
        else:
            scene itchio with dissolve
        sam "{b}Nuestro{/b}."
        call BlinkXP("c14s001_220", "d") from _call_BlinkXP_450
        sim "Hace un momento lo querías echar de casa. ¿Ahora vuelve a ser nuestro novio?"
        if not itchio:
            call BlinkXP("c14s001_225", "d") from _call_BlinkXP_451
        else:
            scene itchio with dissolve
        sam "Tu novio. Mi hombre. Yo también voy a tener que hablar con él, pero aún no he roto con él... ni le he roto la cara a hostias."
        sam "Supongo que tiene mucho que ver con que... haya mantenido la boca cerrada este rato..."
        call BlinkXP("c14s001_230", "d") from _call_BlinkXP_452
        sim "Es que es un tipo listo... sale con las dos..."
        if not itchio:
            call BlinkXP("c14s001_235", "d") from _call_BlinkXP_453
        else:
            scene itchio with dissolve
        sam "Sí... "
        call BlinkXP("c14s001_240", "d") from _call_BlinkXP_454
        sim "Y ahora que está arreglado..."
        if not itchio:
            call BlinkXP("c14s001_245", "d") from _call_BlinkXP_455
        else:
            scene itchio with dissolve
        sam "¡No hay nada arreglado! ¡Tú y yo tenemos que hablar de muchas cosas!"
        call BlinkXP("c14s001_250", "d") from _call_BlinkXP_456
        sim "Sí, pero preferiría no hacerlo delante de [mc]. ¿Por qué no vas a ponerte algo mientras yo hablo con él un momento?"
        if not itchio:
            scene c14s001_255a with dissolve
        else:
            scene itchio with dissolve
        sim "Ver esto botando cada vez que te alteras me está desconcentrando."
        if not itchio:
            call BlinkXP("c14s001_260", "h") from _call_BlinkXP_457
        else:
            scene itchio with dissolve
        sam "¡[sim]!"
        mc "¿Puedo ir yo también a ponerme algo?"
        call BlinkXP("c14s001_265", "d") from _call_BlinkXP_458
        sim "No, tu quédate aquí."
        if not itchio:
            scene c14s001_270a with dissolve
        else:
            scene itchio with dissolve
        sam "Cuidado con lo que hacéis. No me gustaría pillaros haciendo algo inapropiado... *Risa*"
        call BlinkXP("c14s001_275", "f") from _call_BlinkXP_459
        mc "Tú dirás, pero quiero que quede claro que no te he engañado en ningún momento."
        sim "Lo sé."
        call BlinkXP("c14s001_280", "d") from _call_BlinkXP_460
        sim "¿Cuánto tiempo llevas con mi madre?"
        mc "Desde el día que fui a la comisaría."
        call BlinkXP("c14s001_285", "d") from _call_BlinkXP_461
        sim "Es decir, antes de salir conmigo... mmmm..."
        sim "¿Hay más chicas? ¿Cuántas?"
        if mc._var("relationships") > 2:
            mc "Sí, las hay."
            call BlinkXP("c14s001_290", "d") from _call_BlinkXP_462
            sim "¿Cuántas?"
            mc "No sé si debería decirlo..."
            call BlinkXP("c14s001_295", "d") from _call_BlinkXP_463
            sim "Te acabo de pillar con mi madre. Dame algo de información, la voy a necesitar cuando hable con ella."
            sim "No te estoy preguntando quienes son, tan solo cuantas aparte de mi madre y de mí."
            if mc._var("relationships") == 3:
                mc "OK, estoy con otra chica aparte de vosotras."
                call BlinkXP("c14s001_300", "d") from _call_BlinkXP_464
                sim "¿Sólo una? No me parece una mala cifra. Casi esperaba 10 u 11."
            else:
                $ Aux = mc._var("relationships")-2
                mc "OK, estoy con [Aux] chicas aparte de vosotras."
                call BlinkXP("c14s001_300", "d") from _call_BlinkXP_465
                sim "¿[Aux] más? Eres insaciable..."
        else:
            mc "No, no hay ninguna más aparte de vosotras."
        call BlinkXP("c14s001_305", "d") from _call_BlinkXP_466
        sim "¿Va a haber más?"
        mc "Te dije cuál era la situación y lo aceptaste. Tu madre lo aceptó implícitamente al decir que no le importaría compartirme."
        mc "No puedo saber si va a haber más, [sim]. No puedo saber si al salir al rellano voy a encontrar otra chica que me guste tanto como vosotras."
        mc "¿Qué querrías que hiciera en ese caso?"
        call BlinkXP("c14s001_310", "d") from _call_BlinkXP_467
        sim "Ignorarla..."
        mc "Pero..."
        call BlinkXP("c14s001_315", "d") from _call_BlinkXP_468
        sim "Pero entonces también hubieras tenido que ignorarme a mí porque ya estabas con mi madre."
        mc "Exacto. Nuestra relación es diferente de las habituales, no es mejor ni peor."
        if mc._var("relationships") > 2:
            mc "Mientras nos haga felices a los tres y a quien sea que esté también en esta relación, la podemos continuar. Lo que menos quiero es que alguien salga herido."
        else:
            mc "Mientras nos haga felices a los tres la podemos continuar. Lo que menos quiero es que alguien salga herido."
        call BlinkXP("c14s001_320", "d") from _call_BlinkXP_469
        sim "Lo dices como si los tres estuviéramos en una relación poliamorosa. Espero que no quieras hacer un trío conmigo y con mi madre."
        mc "Si pensara que eso os iba a hacer felices, os lo propondría. Pero creo que hay líneas rojas que no deberíamos cruzar, creo que solo con proponerlo te incomodaría a ti."
        call BlinkXP("c14s001_325", "d") from _call_BlinkXP_470
        sim "¿A mí? ¿No a mi madre?"
        mc "Creo que tu madre podría estar más abierta a la idea de un trío que tú, aunque no si tú estás involucrada. Pero con la persona correcta..."
        call BlinkXP("c14s001_330", "d") from _call_BlinkXP_471
        sim "{b}¿Qué?{/b} ¿Mi madre en un trío? Estás loco..."
        call BlinkXP("c14s001_335", "d") from _call_BlinkXP_472
        sim "¿Y de dónde has sacado la idea de que yo no estaría dispuesta? Con la persona adecuada..."
        mc "¿Y quién sería esa persona adecuada, [sim]? Y no digas ninguna actriz famosa a quien no conocemos."
        call BlinkXP("c14s001_340", "d") from _call_BlinkXP_473
        sim "{i}(¡Mielda! ¡Piensa, [sim]! Alguien con quién él nunca tendría sexo...){/i}"
        call BlinkXP("c14s001_345", "d") from _call_BlinkXP_474
        sim "[mar], por ejemplo. O [nor]. [emm], [dap], o [eri]. Incluso con tu abuela también serviría..."
        sim "{i}(¡Uff! Resuelto...){/i}"
        mc "Veo que tienes un fetiche con mi familia. *Risa*"
        call BlinkXP("c14s001_350", "h") from _call_BlinkXP_475
        sim "{b}¿Qué? ¡No!{/b} No es eso..."
        mc "Bueno, si surge la oportunidad les preguntaré si están interesadas en un trío contigo. *Risa*"
        call BlinkXP("c14s001_355", "h") from _call_BlinkXP_476
        if mc._var("relationships") > 3:
            sim "{b}¿Qué?{/b} ¿Estás con alguna de ellas? ¿Con todas?"
        else:
            sim "{b}¿Qué?{/b} ¿Estás con alguna de ellas?"
        mc "Ya sabes la respuesta a eso. Tan solo he dicho que les preguntaré si surge la oportunidad."
        call BlinkXP("c14s001_360", "d") from _call_BlinkXP_477
        sim "Bueno, la próxima vez que te vea y estén ellas delante, te besaré y las observaré para comprobar si ponen la misma cara que tenía yo hace unos minutos."
        mc "*Risa* Eso podría ser muy divertido. Ahora que tu madre ya sabe lo nuestro, parece que no te importa hacerlo público."
        call BlinkXP("c14s001_365", "d") from _call_BlinkXP_478
        sim "No quiero parecer una perra celosa, pero sería una forma de marcar territorio si alguna de ellas tiene ideas... controvertidas. *Risa*"
        mc "¿Controvertidas?"
        call BlinkXP("c14s001_370", "d") from _call_BlinkXP_479
        sim "Es tu familia... no sé cómo llamar a que te estuvieras acostando con tus primas... ya me cuesta saber cómo llamar a que te acuestes con mi madre y conmigo..."
        mc "¿Un hombre feliz? *Risa*"
        call BlinkXP("c14s001_375", "d") from _call_BlinkXP_480
        sim "*Risa* ¡Capullo!"
        mc "Pero volviendo al tema de tu madre. ¿Estamos bien?"
        call BlinkXP("c14s001_380", "d") from _call_BlinkXP_481
        sim "Sí, estamos bien. Verla tan enfadada y azorada al mismo tiempo me ha hecho darme cuenta de una cosa..."
        sim "Lleva una semana cantando mientras cocina. Canta fatal, pero canta. Y haciendo cuentas, empezó a hacerlo cuando... empezasteis lo vuestro..."
        sim "No había cantado desde que murió mi padre. ¿Quién soy yo para negarle eso?"
        mc "Te entiendo. Sabes que lo único que quiero es haceros felices. A las dos."
        call BlinkXP("c14s001_385", "d") from _call_BlinkXP_482
        sim "Nunca me atrevería a hacerte elegir entre las dos."
        mc "Haces bien. No me gusta que me pongan entre la espada y la pared."
        call BlinkXP("c14s001_390", "d") from _call_BlinkXP_483
        sim "Lo sé, hace 10 años que te conozco. Seguro que quién te dé a elegir no es la elegida. No soy tan tonta como para caer en esa trampa."
        call BlinkXP("c14s001_395", "d") from _call_BlinkXP_484
        sam "¿Trampa? ¿Qué trampa?"
        call BlinkXP("c14s001_400", "d") from _call_BlinkXP_485
        sim "En la que caería quien intentase hacer que [mc] eligiera entre dos cosas. Ya sean amigos... o chicas."
        call BlinkXP("c14s001_405", "d") from _call_BlinkXP_486
        sam "Ninguna de las dos vamos a hacerlo, ¿verdad?"
        sam "Es una elección que debemos tomar nosotras. Él puede elegir seguir con las dos o con ninguna."
        call BlinkXP("c14s001_410", "d") from _call_BlinkXP_487
        sim "Entonces va a ser con las dos. Una vez pasada la sorpresa, no pienso renunciar a él. Tú puedes hacerlo si quieres."
        call BlinkXP("c14s001_415", "d") from _call_BlinkXP_488
        sam "Entonces dejémoslo en que tú y yo vamos a tener que hablar para ver cómo nos organizamos."
        sam "Y para ver como se lo decimos a Jamaal..."
        call BlinkXP("c14s001_420", "d") from _call_BlinkXP_489
        sim "Eso va a ser lo más difícil. Se va a estar riendo de nosotras por compartir hombre. Y además {b}este{/b} hombre."
        mc "Hey, que estoy aquí..."
        call BlinkXP("c14s001_425", "d") from _call_BlinkXP_490
        sam "Pero vas a estarlo por poco tiempo. Creo que es hora de que te vayas, tengo mucho que hablar con mi hija y no va a ser agradable si tú estás delante."
        mc "¿Estás bien, [sam]?"
        call BlinkXP("c14s001_430", "d") from _call_BlinkXP_491
        sam "Sí y no. No puedo estar bien sabiendo que no soy suficiente para ti."
        sam "Por otro lado... no te enfades, [sim]... saber que tampoco es suficiente para ti mi niña de 19 años... lo suaviza un poco..."
        call BlinkXP("c14s001_435", "h") from _call_BlinkXP_492
        sim "¡Mamá! Empezó a salir conmigo después de ti. Él no podía saber si yo sería suficiente."
        mc "¡Chicas, parad!"
        mc "Cualquiera de las dos sería suficiente para cualquier hombre."
        if mc._var("relationships") == 2:
            mc "Si para vosotras es un problema que esté con las dos a la vez..."
        elif mc._var("relationships") == 3:
            mc "Si para vosotras es un problema que esté con las dos a la vez y con la otra chica..."
        else:
            mc "Si para vosotras es un problema que esté con las dos a la vez y con el resto de las chicas..."
        mc "Si sois capaces de decidir, cívicamente, cual corta conmigo..."
        scene c14s001_440a with dissolve
        sam "¿Qué? ¡No! ¡No podríamos!" (multiple=2)
        sim "¡Las dos te querríamos para nosotras!" (multiple=2)
        mc "Entonces la decisión la habéis tomado vosotras."
        call BlinkXP("c14s001_445", "d") from _call_BlinkXP_493
        if mc._var("relationships") == 2:
            sam "Imagínate cómo se quedaría la otra. Prefiero compartirte a tener que cederte, aunque sea a mi hija."
            call BlinkXP("c14s001_450", "d") from _call_BlinkXP_494
            sim "Yo tampoco querría cederte. Y ser la que se queda contigo sería casi peor..."
        else:
            sam "Imagínate cómo se quedaría la otra. Prefiero compartirte a tener que cederte, aunque sea a mi hija."
            call BlinkXP("c14s001_450", "d") from _call_BlinkXP_495
            sim "Yo tampoco querría cederte. Y ser la que se queda contigo sería casi peor..."
            if mc._var("relationships") == 3:
                sim "¿Y la otra chica? ¿Qué pasaría con ella? Supongo que la \"ganadora\" de entre nosotras tendría que negociar con ella..."
            else:
                sim "¿Y las otras chicas? ¿Qué pasaría con ellas? Supongo que la \"ganadora\" de entre nosotras tendría que negociar con ellas..."
            mc "Esa sería la idea. Todo muy cívico."
            call BlinkXP("c14s001_455", "d") from _call_BlinkXP_496
            sam "Pues entonces ve olvidándote de nos peleemos por ti para que después se te pueda quedar otra."
            call BlinkXP("c14s001_460", "d") from _call_BlinkXP_497
            sim "Prefiero tener una parte de ti a no tener nada y pelearme con mi madre por el camino."
        mc "Entonces todo arreglado."
        call BlinkXP("c14s001_465", "d") from _call_BlinkXP_498
        sam "Todo no. Ahora es cuando te vas y me dejas tener una conversación larguísima con mi hija."
        call BlinkXP("c14s001_470", "d") from _call_BlinkXP_499
        sim "Pero si ya lo hemos hablado todo, ¿no?..."
        call BlinkXP("c14s001_475", "h") from _call_BlinkXP_500
        sim "¡Oh, no!..."
        call BlinkXP("c14s001_480", "d") from _call_BlinkXP_501
        sam "¡Oh, sí! Vamos a tener la conversación de las abejas y las flores."
        call BlinkXP("c14s001_485", "h") from _call_BlinkXP_502
        sim "¡Pero, Mamá! Ya sé todo eso... ya no soy virgen."
        call BlinkXP("c14s001_490", "d") from _call_BlinkXP_503
        sam "Razón de más para tenerla. Y añadiré todo el catálogo de anticonceptivos y ETSs."
        mc "Entonces yo me voy a vestir... yo ya tuve esa charla con [mar]."
        call BlinkXP("c14s001_495", "d") from _call_BlinkXP_504
        sam "Sí, no es una charla que me gustaría tener con mi hombre. *Risa*"
        scene black with dissolve
        "Unos minutos después..."
        scene c14s001_500a with dissolve
        mc "Yo me voy a ir y os voy a dejar con vuestra charla."
        call BlinkXP("c14s001_505", "d") from _call_BlinkXP_505
        sim "No sin antes despedirte como es debido."
        mc "{b}¿Qué?{/b} ¿Delante de tu madre?"
        call KissXP("c14s001_510", "d") from _call_KissXP_10
        sam "Es lo primero que hemos hablado. Si las dos sabemos que la otra sale contigo, no hay razón para esconderse."
        sam "Y no me perdería un beso tuyo por nada del mundo."
        call KissXP("c14s001_515", "d") from _call_KissXP_11
        sim "Yo tampoco."
        mc "Esto no me lo esperaba... pero me gusta. Me gusta mucho."
        call BlinkXP("c14s001_520", "d") from _call_BlinkXP_506
        sim "Si estás volviendo a pensar en un trío, olvídalo. Eso es lo segundo que hemos hablado y ninguna de las dos quiere un trío."
        call BlinkXP("c14s001_525", "d") from _call_BlinkXP_507
        if mc._var("relationships") > 2:
            sam "Al menos con la otra presente. Con otra chica quizás, pero no voy a tener sexo delante de mi hija."
        else:
            sam "No voy a tener sexo con mi hija delante."
        mc "Bueno, todo se hablará. *Risa* Solo de pensarlo..."
        call BlinkXP("c14s001_530", "d") from _call_BlinkXP_508
        sam "Ni se te ocurra acabar esa frase diciendo que te has puesto duro. *Risa* No quiero tener la primera discusión con [sim] para ver quién te ayuda a bajar esa erección."
        call BlinkXP("c14s001_535", "d") from _call_BlinkXP_509
        sim "Bueno, no discutiríamos. Tú ya has tenido tu ración de [mc] hoy. Sería mi turno. *Risa*"
        call BlinkXP("c14s001_540", "d") from _call_BlinkXP_510
        sam "¿Ves lo que provocas? Vete y déjanos hablar tranquilas. Nos vemos mañana."
        mc "¿Mañana?"
        sam "Sí, mientras os dejaba tiempo para hablar, he llamado a [mar]. Mañana [nor] y ella iban a ir a la playa. Nos hemos apuntado y vamos a ir toda la familia."
        call BlinkXP("c14s001_545", "d") from _call_BlinkXP_511
        sim "Suena raro lo de la familia... aunque lo éramos en todos los sentidos menos en el nombre. Pensar que [emm] es mi cuñada..."
        call BlinkXP("c14s001_550", "d") from _call_BlinkXP_512
        sam "Calla, calla. [mar] es más joven que yo y es mi suegra. *Risa*"
        mc "*Risa* Entonces nos vemos mañana. Os quiero."
        scene c14s001_500b with dissolve
        sim "Y nosotras a ti." (multiple=2)
        sam "Nosotras también." (multiple=2)
        stop music fadeout (1.5)
    else:
        call BlinkXP("c14s001_555", "h") from _call_BlinkXP_513
        sim "¿Y tú? Tú decidiste no salir conmigo para poder follarte tranquilamente a mi madre..."
        mc "No es eso y lo sabes, [sim]. Ya te dije por qué no podía salir contigo por si algo salía mal."
        call BlinkXP("c14s001_560", "d") from _call_BlinkXP_514
        sim "¿Y con mi madre no te importa?"
        call BlinkXP("c14s001_565", "d") from _call_BlinkXP_515
        sam "Si que le importa, pero decidimos correr el riesgo."
        mc "La situación es diferente..."
        scene c14s001_570a with dissolve
        stop music fadeout (1.5)
        sim "¡Estaré en mi habitación! Podéis seguir follando si queréis."
        scene c14s001_570b with hpunch
        play sound "music/DoorSlam.ogg"
        "*Portazo*"
        call BlinkXP("c14s001_575", "d") from _call_BlinkXP_516
        sam "Déjame hablar con ella mientras te vistes. Creo que será mejor que te vayas."
        mc "Yo también lo creo. Y creo que sería bueno que tú también te pusieras algo. Si entras ahí así sería un recordatorio de cómo nos ha pillado."
        call BlinkXP("c14s001_580", "d") from _call_BlinkXP_517
        sam "Tienes razón. Déjame ponerme algo."
        scene black
        "[sam] se pone una bata y va a hablar con [sim] mientras tú te vistes."
        scene c14s001_570b with dissolve
        mc "Ya estoy vestido. Voy a irme."
        sam "*Desde la habitación de [sim]* Espera un segundo, por favor."
        "Se escuchan susurros dentro de la habitación y [sam] sale al cabo de un minuto."
        call BlinkXP("c14s001_585", "d") from _call_BlinkXP_518
        sam "Llamare a [mar] para ir mañana a la playa. La piscina va a estar cerrada un par de días y creo que sería bueno para [sim] pasar un rato con toda la familia."
        mc "Eso suena genial. ¿Cómo se lo está tomando?"
        call BlinkXP("c14s001_590", "d") from _call_BlinkXP_519
        sam "Se le está pasando el enfado, pero no creo que sea buen momento para que hables con ella ahora mismo. El enfado que se le está pasando es conmigo."
        sam "El enfado contigo, aunque injusto, le va a costar algo más."
        mc "Entonces me voy a ir."
        call BlinkXP("c14s001_595", "d") from _call_BlinkXP_520
        sam "Será lo mejor."
        mc "Al menos ahora no me tengo que esconder para hacer esto."
        mc "Te quiero."
        call KissXP("c14s001_510", "d") from _call_KissXP_12
        sam "Yo también."
    scene black with dissolve
    "Conduces a casa pensando en lo que ha ocurrido y en el resultado. Pese a que paras a llenar el depósito, el camino de vuelta te parece un momento."
    return
label c14s001_ContinuationNoSam:
    scene black with dissolve
    if sim._var("route"):
        "Conduces a casa pensando en la pobre [sim] y en cómo va a ir esa conversación sobre abejas y flores."
    else:
        "Conduces a casa pensando en esas empanadas que está preparando [sam]. Te hubiera gustado quedarte a cenar, pero ahora mismo tu lugar está en casa."
    $ renpy.notify ("Profile image unlocked")
    "Paras a llenar el depósito antes de llegar."
    return
label c14s002_Pool:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_25
        call mrS3_eri_route from _call_mrS3_eri_route_16
        call mrS3_nor_route from _call_mrS3_nor_route_15
    scene c14s002_005a with dissolve
    "Al llegar a casa encuentras a [nor] y [eri] tomando el sol en la piscina."
    play music ("music/Morning-Sun.ogg")
    mc "Buenos días, chicas. Se me hace raro veros solas aquí con tanta gente en casa. ¿Dónde están el resto?"
    call BlinkXP("c14s002_010", "d") from _call_BlinkXP_521
    nor "[dap], [emm], [sca], y [mar] acaban de salir para ir de compras."
    call BlinkXP("c14s002_015", "d") from _call_BlinkXP_522
    eri "Tía Betty y la abuela siguen en el centro. Se van a unir a las compras y después recogerán a Kiara y [eil]."
    mc "¿Cuántas horas trabaja [eil] hoy? ¿Tú no tenías que estar en el trabajo?"
    call BlinkXP("c14s002_020", "d") from _call_BlinkXP_523
    eri "No, que va, yo he trabajado cuatro horas esta mañana. [eil] hoy abre y cierra, se va a pasar 12 horas allí."
    call BlinkXP("c14s002_025", "d") from _call_BlinkXP_524
    nor "Debbie y Kate han ido a la universidad con [sai]. Y Kim y Lisa aún no han vuelto y las recogerán allí."
    call BlinkXP("c14s002_030", "d") from _call_BlinkXP_525
    eri "¿Por qué no te unes a nosotras? No es que tú tengas que ponerte moreno, pero nos puedes hacer compañía."
    if nor._var("route") or eri._var("route"):
        mc "Dejadme que me cambie y bajo en un momento."
    else:
        mc "Tengo que mirar unas cosas por internet, con lo que os dejaré disfrutar del sol tranquilamente."
        scene c14s002_005b with dissolve
        nor "Entonces te vemos luego."
        eri "Hasta luego, [mc]."
        stop music fadeout (1.5)
        return
    if nor._var("route"):
        call BlinkXP("c14s002_035", "d") from _call_BlinkXP_526
        nor "¿No vas a darme un beso antes de irte?"
        call KissXP("c14s002_040", "d") from _call_KissXP_13
        mc "Claro que sí. Deberíamos hacerlo público cuanto antes. No me gusta perderme besos tuyos."
        if eri._var("route"):
            call BlinkXP("c14s002_045", "d") from _call_BlinkXP_527
            eri "¿Y míos?"
            call KissXP("c14s002_050", "d") from _call_KissXP_14
            mc "Tuyos tampoco. Por eso quiero hacerlo público."
        else:
            call BlinkXP("c14s002_055", "d") from _call_BlinkXP_528
            eri "¡Qué monos sois, por el amor de Dios!"
    else:
        call BlinkXP("c14s002_045", "d") from _call_BlinkXP_529
        eri "¿No vas a darme un beso antes de irte?"
        call KissXP("c14s002_050", "d") from _call_KissXP_15
        mc "Claro que sí. Deberíamos hacerlo público cuanto antes. No me gusta perderme besos tuyos."
    call BlinkXP("c14s002_060", "d") from _call_BlinkXP_530
    nor "A menos que quieras que mi madre empiece a matar a gente, mejor esperar para hacerlo público... ya viste como se puso cuando me quedé en ropa interior delante tuyo..."
    call BlinkXP("c14s002_065", "h") from _call_BlinkXP_531
    eri "{b}¿Qué?{/b} ¿Cuándo ha pasado eso?"
    call BlinkXP("c14s002_070", "d") from _call_BlinkXP_532
    nor "¡Oops! Ayer..."
    mc "Creo que te voy a dejar explicándoselo mientras me cambio. Bajo en dos minutos."
    scene black with dissolve
    "Unos minutos después..."
    call BlinkXP("c14s002_075", "d") from _call_BlinkXP_533
    eri "¿No pensabais explicármelo?"
    mc "No es que os quisiéramos ocultar nada, es que no tenemos toda la información. Nos dijeron que en unos días nos darían más información."
    mc "Os lo pensábamos explicar cuando tuviéramos más datos. No servía de nada preocuparos por esto."
    call BlinkXP("c14s002_080", "d") from _call_BlinkXP_534
    eri "No me refiero a lo de las empresas y el secuestro, eso puedo llegar a entenderlo. Sino a lo de la abuela. ¿Nadie ha pensado que me gustaría saber que la abuela está enferma?"
    call BlinkXP("c14s002_085", "d") from _call_BlinkXP_535
    nor "No está enferma, cielo. Es un desorden hormonal. Producir leche puede ser embarazoso, pero no es una enfermedad."
    call BlinkXP("c14s002_090", "d") from _call_BlinkXP_536
    eri "Vale, pero nadie nos lo pensaba contar, ¿verdad? Ya tenemos 18, pero nos seguís tratando como a niñas pequeñas."
    mc "No es eso, [eri]. Es algo que debe explicar ella cuando esté preparada."
    call BlinkXP("c14s002_095", "d") from _call_BlinkXP_537
    eri "Pero los dos lo sabíais. Me siento como si me hubierais dejado de lado. Y [emm] y [dap] van a sentirse igual cuando se enteren. ¿Tía [mar] lo sabe?"
    call BlinkXP("c14s002_100", "d") from _call_BlinkXP_538
    nor "No creo que lo sepa. Tu abuela usa la bomba en casa."
    if mee._var("mcKnowsSickness"):
        mcp "(Sí que lo sabe, pero no puedo decíroslo, lo mismo que lo de su cáncer. Parece que [nor] no lo sabe, acaba de decir que no está enferma.)"
    call BlinkXP("c14s002_105", "d") from _call_BlinkXP_539
    eri "Que no lo sepa Tía [mar] casi me hace sentir mejor... al menos no me siento tan dejada de lado."
    mc "Entonces ¿todo arreglado?"
    call BlinkXP("c14s002_110", "d") from _call_BlinkXP_540
    eri "Sí, de momento. Pero lo del secuestro todavía me parece demencial..."
    call BlinkXP("c14s002_115", "d") from _call_BlinkXP_541
    nor "Ya te he dicho que te contaremos más cuando sepamos más. ¿Podemos disfrutar del sol?"
    call BlinkXP("c14s002_120", "d") from _call_BlinkXP_542
    eri "Perfecto. Me ibas a poner crema cuando ha llegado [mc]."
    mc "Si queréis os la pongo yo."
    call BlinkXP("c14s002_125", "d") from _call_BlinkXP_543
    eri "Genial."
    call BlinkXP("c14s002_130", "d") from _call_BlinkXP_544
    nor "Empieza por [eri]. Tiene la piel más sensible."
    scene c14s002_135An with dissolve #d-e/punch-f/punch
    eri "¡Hey! ¡Está fría!"
    mc "Es más divertido que echarla en las manos. *Risa*"
    call BlinkXP("c14s002_140", "d") from _call_BlinkXP_545
    nor "*Risa* Eres malvado, [mc]."
    scene c14s002_145AnBlink with dissolve #d-e-f/ounch-g/punch-blink
    nor "¡Hey! No eres malvado. ¡Eres un capullo! *Risa*"
    call BlinkXP("c14s002_150", "d") from _call_BlinkXP_546
    nor "Ahora voy a tener que notar como la crema va resbalando por la espalda hasta que acabes con [eri]."
    mc "No hay por qué. Tengo dos manos y hay dos espaldas."
    call BlinkXP("c14s002_155", "d") from _call_BlinkXP_547
    eri "¿Eres capaz de hacer dos cosas a la vez? *Risa*"
    mc "Ahora lo comprobaréis."
    scene c14s002_900pv
    show c14s002_900v
    nor "Pues no lo hace nada mal."
    eri "Podría decirse que lo hace mejor que tú con dos manos."
    if eri._var("route"):
        nor "A ti lo que te gusta es notar las manos fuertes de tu novio masajeándote la espalda."
    else:
        nor "A ti lo que te gusta es notar las manos fuertes de mi novio masajeándote la espalda."
    eri "No te lo voy a negar..."
    nor "Pon crema en las piernas de [eri], pero céntrate en ella esta vez. Usa las dos manos."
    scene c14s002_905pv
    hide c14s002_900v
    show c14s002_905v
    eri "Me podría acostumbrar a esto, es como un masaje super relajante."
    mc "Es una técnica que aprendí en Portland, cuando hice el curso de masaje."
    nor "¿Cuándo pensabas decírnoslo?"
    eri "Yo lo sabía. Me lo dijo [emm]."
    mc "Voy a por tus piernas, [nor]."
    nor "No voy a decir que no. Quiero probar esa técnica que..."
    scene c14s002_910pv
    hide c14s002_905v
    show c14s002_910v
    nor "¡Wow! ¡Es fantástico! Puedo notar como se me descarga la tensión por segundos."
    eri "Ya te lo he dicho, Mamá. Es increíble. Podría volver al trabajo fresca como una rosa ahora."
    mc "Gracias. Un placer ser de ayuda."
    nor "Creo que vas a tener que comprar nuestro silencio con más masajes de estos."
    eri "Imagínate si las 15 lo supieran y todas te pidiéramos masajes todos los días..."
    mc "Saldríais perdiendo. Habría menos [mc] para vosotras. *Risa*"
    nor "Ahí nos has pillado... *Risa* Mejor mantener el secreto."
    stop music fadeout (1.5)
    $ menu1 = _("Ver la escena con")
    $ menu2 = _("Ver la escena con")
    $ menu3 = _("Ver la escena con")
    if itchio:
        scene itchio with dissolve
        "Pasáis una tarde agradable hasta que las chicas vuelven de compras."
        return
    if nor._var("route") and eri._var("route"):
        call c14s002_NorEri from _call_c14s002_NorEri
        scene black with dissolve
        hide c14s002_910v
        "Estás en ruta con [eri] y [nor], pero ¿qué hubiera pasado si la situación hubiera sido diferente?"
        $ menu1 = _("Volver a ver la escena con")
    elif nor._var("route"):
        call c14s002_Nor from _call_c14s002_Nor
        scene black with dissolve
        hide c14s002_910v
        "Estás en ruta con [nor], pero ¿qué hubiera pasado si la situación hubiera sido diferente?"
        $ menu2 = _("Volver a ver la escena con")
    else:
        call c14s002_Eri from _call_c14s002_Eri
        scene black with dissolve
        hide c14s002_910v
        "Estás en ruta con [eri], pero ¿qué hubiera pasado si la situación hubiera sido diferente?"
        $ menu3 = _("Volver a ver la escena con")
    $ SceneReplay = True
    while SceneReplay:
        menu qPoolSide:
            "¿Quieres ver alguna de las escenas alternativas?"
            "[menu1!t] [eri] y [nor].":
                call c14s002_NorEri from _call_c14s002_NorEri_1
            "[menu2!t] [nor].":
                call c14s002_Nor from _call_c14s002_Nor_1
            "[menu3!t] [eri].":
                call c14s002_Eri from _call_c14s002_Eri_1
            "Seguir con la historia.":
                $ SceneReplay = False
    return
label c14s002_NorEri:
    play music ("music/Bolero.ogg")
    scene c14s001_650An with dissolve
    nor "Déjame desabrocharme esto para que puedas volver a mi espalda. No quiero líneas blancas."
    mc "Ahora mismo vuelvo a ella..."
    call BlinkXP("c14s001_655", "h") from _call_BlinkXP_548
    eri "¡Mamá!"
    mc "¿Qué pasa, [eri]? Solo es una espalda..."
    call BlinkXP("c14s001_660", "d") from _call_BlinkXP_549
    nor "Cielo, te tienes que acostumbrar a que [mc] ya ha visto todo lo que hay que ver. No se va a asustar por verme la espalda."
    call BlinkXP("c14s001_665", "d") from _call_BlinkXP_550
    eri "Lo sé, pero ¿y si vuelve la abuela?"
    mc "Si vuelve Meemaw, únicamente hay una espalda al descubierto."
    scene c14s001_670AnBlink with dissolve #d (650b) - e - Blink
    nor "Ya no..."
    mc "Me gusta este cambio..."
    nor "Después de lo tuyo ayer, esto parece casi una broma."
    call BlinkXP("c14s001_675", "d") from _call_BlinkXP_551
    eri "Estáis locos... me encanta..."
    mc "Yo lo estoy, por vosotras dos... pero es el momento de ponerle crema a tu madre en la espalda."
    scene c14s001_680a with dissolve
    nor "No te dejes ningún rincón."
    mc "No pensaba hacerlo."
    call BlinkXP("c14s001_685", "d") from _call_BlinkXP_552
    eri "Yo voy a cerrar los ojos un poco mientras le pones la crema... me está molestando el sol."
    mc "¿Quieres que vaya a buscar tus gafas de sol?"
    eri "No hace falta. Con cerrar los ojos un ratito tengo suficiente."
    call BlinkXP("c14s001_690", "d") from _call_BlinkXP_553
    nor "Entonces sigue con esa espalda."
    mc "A tus órdenes."
    scene c14s001_700pv with dissolve
    show c14s001_700v
    "Empiezas a masajear el culo de [nor] sin ningún pudor. Ella da un respingo."
    call BlinkXP("c14s001_705", "h") from _call_BlinkXP_554
    nor "*Susurrando* ¿Qué haces? [eri] está ahí mismo..."
    mc "*Susurrando* Confía en mí..."
    scene c14s001_705d with dissolve
    eri "¿Que estáis susurrando? *Bostezo* Casi me quedo dormida después del masaje de piernas..."
    call BlinkXP("c14s001_710", "d") from _call_BlinkXP_555
    nor "Nada, nada... le estaba diciendo como me está gustando a mí."
    scene c14s001_705d with dissolve
    eri "Vale... seguid y despertarme cuando sea mi siguiente turno de masaje..."
    scene c14s001_700pv with dissolve
    show c14s001_700v
    mc "No te preocupes, [eri] que en un momento continuaré contigo. Déjame ocuparme de tu madre antes."
    nor "*Gemido contenido* Justo ahí... un poco más de presión..."
    mc "*Susurrando* Para no querer incluir tu culo en nuestros juegos, parece que lo tienes sensible..."
    nor "*Susurrando y gimiendo* Calla y sigue..."
    scene c14s001_715pv with dissolve
    hide c14s001_700v
    show c14s001_715v
    mc "*Susurrando* Como quieras..."
    nor "*Susurrando* Me estás matando... *Jadeo contenido*"
    mc "Como soy buena persona, voy a cambiar a [eri]."
    scene c14s001_705d with dissolve
    eri "¿Es mi turno ya?"
    mc "Sí, cielo. Voy a seguir con tus piernas un poco más ahora que te has relajado un poco."
    scene c14s001_720a with dissolve
    hide c14s001_715v
    eri "Mmmmm... que bueno eres haciendo eso... pero ¿solo la pierna izquierda?"
    mc "Eres camarera. ¿Con qué mano llevas la bandeja?"
    eri "Con la izquierda..."
    mc "Supongo que entonces es la pierna que más cargas, ¿no?"
    eri "Tiene lógica... pero da lo mismo... tú sigue..."
    scene c14s001_725AnBlink with dissolve #Blink with punch
    nor "*Susurrando* {b}¿Qué?{/b}"
    mc "¡Hush! Deja que [eri] disfrute de su masaje. Ya te llegará tu turno."
    scene c14s002_920pv
    hide c14s001_720v
    show c14s002_920v
    eri "Eso, Mamá, yo he esperado mientras te daba el masaje a ti. Ahora te toca a ti esperar."
    nor "*Suspiro* Vale... no diré nada... más."
    mcp "(Ahora viene lo más complicado...)"
    scene c14s001_730AnBlink with dissolve #Blink with punch d-e-f-g-Blink
    eri "*Susurrando* ¿Qué haces?... ¿Crees que puedes hacerlo sin que mi madre se entere?"
    mc "*Susurrando* Si contienes tus gemidos, sí."
    eri "*Susurrando* Entonces continúa..."
    scene c14s002_960pv
    hide c14s002_920v
    show c14s002_960v
    nor "*Gemido contenido* ¿Qué andáis susurrando?"
    eri "Nada... *Jadeo silenciado* le estaba comentando lo de los gorros..."
    nor "*Respiración entrecortada* Ha sido... una idea original... por parte de [sca]..."
    eri "*Gemido* {b}¡SÍ!{/b}... Justo ahí, [mc]... creo que tengo un nudo justo ahí..."
    scene c14s001_735pv
    hide c14s002_960v
    show c14s001_735v
    mc "¿Qué es eso de los gorros?"
    eri "*Gemido* Una idea de [sca]... celebrar la Navidad en verano..."
    nor "*Gemido acallado* Es lo que han ido... a comprar [mar]... *Jadeo silenciado* y las chicas..."
    eri "*Susurro* [mc], si sigues así... *Gemido* mi madre nos va a pillar..."
    call BlinkXP("c14s001_740", "d") from _call_BlinkXP_556
    nor "*Gemido* ¿Pillaros? ¿Crees que susurras suficientemente bajo? *Jadeo* ¿O que contienes los gemidos?"
    nor "*Respiración entrecortada* Tu madre está... recibiendo el mismo tratamiento que tú..."
    call BlinkXP("c14s001_745", "h") from _call_BlinkXP_557
    eri "{b}¿Qué?{/b}"
    mc "No creerías que iba a daros prioridad a una de vosotras, ¿verdad?"
    scene c14s001_735pv
    show c14s001_735v
    eri "Pero... con mi madre delante... *Gemido*"
    nor "*Jadeo* Ese gemido te ha delatado... *Gemido* Incluso con tu madre delante lo estás disfrutando..."
    mc "Creo que las dos tenéis un punto exhibicionista. De [nor] ya lo sabíamos, pero [eri]..."
    eri "¿Yo? ¡No! *Gemido*"
    scene c14s001_750pv
    hide c14s001_735v
    show c14s001_750v
    mc "Nos estás diciendo que no te ponía la posibilidad de que [nor] nos pillara..."
    nor "*Gemido* Y quiere que la creamos..."
    mc "Y ahora que tu madre te está mirando mientras tu orgasmo se acerca tampoco te estás poniendo más, ¿verdad?"
    eri "*Gemido* Quizás un poco... más"
    call BlinkXP("c14s001_755", "d") from _call_BlinkXP_558
    nor "*Gemido* No hay nada malo en ello... cielo... *Jadeo* A mí me está poniendo cachonda... verte disfrutar y que me veas a mí."
    mc "Y a mí me está poniendo veros disfrutar a las dos..."
    nor "Tu calla... *Risa* Esto es una cosa entre madre e hija... *Gemido*"
    scene c14s001_765pv
    hide c14s001_750v
    show c14s001_765v
    nor "Continúa así, cielo. *Gemido* Estoy muy cerca..."
    eri "Yo también, *Gemido* mi vida."
    mc "Ahora me vais a decir que os está poniendo cachondas la idea de correros a la vez mientras os cogéis de la mano."
    eri "¡Sí! *Gemido* ¡Me pone mucho que mi madre... *Jadeo* me mire mientras nuestro novio hace que esté... a punto de correrme!"
    mc "Córrete para nosotros, [eri]."
    scene c14s001_760An with dissolve
    "[nor] extiende la mano hacia [eri]. Ella se la coge, en un gesto que recordarás toda la vida. Tus dos chicas disfrutando de tus manos mientras se cogen las suyas."
    "Ciertamente, es un momento entre madre e hija. Un momento en el que estás feliz de participar."
    "El contacto entre ellas dura un segundo."
    call OrgasmX("c14s001_775") from _call_OrgasmX_10 #eri
    "El cuerpo de [eri] es el primero en explotar. Lo hace en una fuente de fluidos mientras su cuerpo se retuerce bajo tus dedos."
    eri "¡Joder, SÍ! *JADEO* ¡Es super intenso!"
    scene c14s001_760b with dissolve
    "Un momento más tarde es [eri] la que extiende su mano y aprieta la de [nor], buscando su apoyo, su aprobación."
    eri "¡No pares! ¡Llegan más!"
    call OrgasmX("c14s001_770b") from _call_OrgasmX_11 #nor
    "En ese momento [nor] también llega al orgasmo. Otra explosión como no había tenido nunca."
    nor "¡Por Dios! *GEMIDO* ¡Es buenísimo!"
    scene c14s001_780a with dissolve
    "Continúas apretando sus clítoris mientras sus orgasmos llegan por fin al final, dejándolas finalmente exhaustas."
    scene c14s001_780b with dissolve
    eri "Ha sido increíble. No sabía que me pudiera correr así..."
    nor "Creo que lo de corrernos juntas ha sido lo que lo ha propiciado... nunca me había corrido delante de ninguna chica..."
    mc "¿Nunca? ¿Y ninguna chica se había corrido delante tuyo?"
    call BlinkXP("c14s001_785", "d") from _call_BlinkXP_559
    if persistent.family:
        nor "Bueno... que no salga de aquí, pero... tu madre... cuando le enseñé a masturbarse..."
        mc "¿Qué? ¿Enseñaste a mamá a masturbarse?"
        nor "A veces olvidas que soy cinco años mayor que ella... ¿quién le iba a enseñar? ¿Mi madre?"
    else:
        nor "No, nunca. Es la primera vez..."
    call BlinkXP("c14s001_790", "d") from _call_BlinkXP_560
    nor "Estás preciosa cuando te corres, cielo. Me ha gustado que compartamos este momento."
    call BlinkXP("c14s001_795", "d") from _call_BlinkXP_561
    eri "Tú también. No te había visto ser... tan tú... nunca. Ha sido como si te liberaras..."
    mc "Las dos estáis preciosas. Las dos sois preciosas. Veros correros juntas ha sido un espectáculo. Que os veáis mutuamente... creo que ha destapado algo en vosotras."
    scene c14s001_780c with dissolve
    nor "Y creo que ahora le debemos algo a nuestro chico, ¿no, cielo?"
    eri "No sé como no ha reventado el bañador. Seguro que está enorme ahí dentro."
    nor "Aparta las tumbonas, [eri]. Veamos que sorpresa nos tiene guardada aquí dentro."
    scene c14s001_800a with fade
    nor "Pues sí, tenías razón. Enorme y duro como una piedra."
    eri "Solo de verlo me está entrando hambre."
    nor "¿Quieres hacer los honores?"
    eri "¿Por qué no empezamos una por cada lado?"
    mc "Chicas, estoy muy sensible después de tanto rato empalmado..."
    scene c14s001_805An with dissolve #abc
    hide c14s001_765v
    mc "Pero no voy a decir que no a eso."
    eri "¿Te gusta, cielo?"
    mc "Mucho."
    scene c14s001_805e with dissolve
    nor "Te gusta ver como tus dos mujeres chupan tu astil a la vez, ¿verdad?"
    mc "No puedes imaginar cuanto."
    scene c14s001_805d with dissolve
    eri "¿Y te pone que seamos tu tía y tu prima? ¿Que seamos madre e hija?"
    mc "¡Ufff! Una barbaridad..."
    if not persistent.family:
        mcp "(Sobretodo que {b}tú creas{/b} que sois madre e hija.)"
    scene c14s001_805e with dissolve
    nor "¿Es la primera vez que estás con una madre y con su hija?"
    mc "Sí, y es la primera vez que una madre y una hija me están matando de anticipación."
    scene c14s001_800An with dissolve #bf
    nor "Entonces será mejor que no le hagamos sufrir más, ¿no crees, cielo?"
    eri "Creo que se ha ganado que le demos el placer que se merece."
    nor "Empieza tú, cielo. Yo lo caté ayer..."
    eri "Como quieras, Mamá."
    scene c14s001_810pv
    hide c14s001_805v
    show c14s001_810v
    "[eri] engulle tu glande mientras [nor] se dedica a tus pelotas. La imagen es increíble. La sensación es maravillosa."
    nor "Me encanta ver como los perfectos labios de mi hija engullen tu polla."
    nor "¿Lo está haciendo bien?"
    mc "Lo está haciendo perfecto. Y antes de que preguntes quien lo hace mejor, debes saber que no contestaré a esa pregunta."
    eri "*Gemido ahogado*"
    scene c14s001_800c with dissolve
    eri "Esa sería una pregunta injusta... es mi primera vez..."
    mc "Y lo estás haciendo genial, cielo. Pero sabemos lo competitiva que puede ser tu madre."
    nor "¿Competitiva yo? No iba a preguntar eso... o al menos delante de [eri]..."
    scene c14s001_800d with dissolve
    eri "¿Tu quieres que continúe hasta que se corra y no te deje probarlo? *Risa*"
    nor "No, cielo. Pero puedes continuar si quieres."
    mc "Chicas, no discutáis ahora... me estaba poniendo muy cachondo"
    scene c14s001_800e with dissolve
    eri "No estabamos discutiendo, cielo. Solo bromeábamos."
    eri "Pero quiero ver esos labios rojos alrededor de tu polla. A lo mejor puedo aprender algo..."
    nor "Lo estabas haciendo muy bien, cariño, ¿verdad, [mc]?."
    mc "Genial, pero si [eri] ha pedido que continúes tú, ¿se lo vas a negar?"
    scene c14s001_815pv
    hide c14s001_810v
    show c14s001_815v
    "[nor] no responde y se apodera de tu polla, introduciéndosela profundamente en la boca."
    eri "¡Wow! Yo no soy capaz de metérmela tanto... ¿te gusta más así?"
    mc "Lo que tú hacías con la lengua era perfecto. Lo que hace tu madre con toda la boca es increíble. Son dos sensaciones diferentes."
    nor "*Gemido ahogado*"
    eri "Creo que mi madre quiere decir algo, pero no la acabo de entender. No recuerda que no se debe hablar con la boca llena. *Risa*"
    mc "Chicas, estoy a punto de llegar..."
    eri "¿Donde quieres acabar?"
    $ Aux3 = False
    if persistent.walkthrough:
        if persistent.lesbian:
            $ wt1 = _("Posibilidad de beso blanco.")
        else:
            $ wt1 = _("Posibilidad de beso blanco sin contenido lésbico.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte en la boca de [nor]." (wt = wt1):
            call c14s002_CumInNor from _call_c14s002_CumInNor
            $ Aux2 = False
        "Correrte en la boca de [eri]." (wt = wt1):
            call c14s002_CumInEri from _call_c14s002_CumInEri
            $ Aux2 = False
        "Correrte en sus caras." (wt = wt2):
            $ Aux2 = True
            call c14s002_CumOnFaces from _call_c14s002_CumOnFaces
    $ resetWalkthrough ()
    mc "¿Ya estáis pensando en la próxima? Yo puedo estar listo en cinco minutos..."
    stop music fadeout (1.5)
    if Aux2: #corrida cara
        scene c14s001_890An2 #a (coche) e (Miran entrada) g (se miran) f (miran a MC)
    else:
        scene c14s001_890An #a (coche) b (Miran entrada) c (se miran) d (miran a MC)
    if Aux3:
        "Justo cuando se vuelven de poner de rodillas delante tuyo oís el motor de un coche y la verja abriéndose. Os han dado el tiempo justo para acabar, aunque no para un segundo round."
    else:
        "Justo en ese momento oís el motor de un coche y la verja abriéndose. Os han dado el tiempo justo para acabar, aunque no para un segundo round."
    eri "¡Oh, mierda! Un poco más y nos pillan. Vamos a meternos en la piscina..."
    scene c14s001_895a with dissolve
    mc "Espera... [nor]"
    play sound ("music/Splash.ogg")
    scene c14s001_895An with dissolve #b-c #tira el top al agua
    mcp "(Espero que lo coja antes de que la vea alguien.)"
    call BlinkXP ("c14s002_685" , "f") from _call_BlinkXP_562
    "Te terminas de subir el bañador justo cuando aparece [mar]."
    play music ("music/ChillUkelele.ogg")
    mom "Hola, [mc]. ¿Estás solo?"
    mc "No, [eri] y [nor] están buceando."
    call c14s002_PartyExplanation from _call_c14s002_PartyExplanation
    scene c14s001_900a with dissolve
    mc "Mira, por ahí vuelven de su buceo."
    scene c14s001_900b with dissolve
    nor "Hola, [mar]. Qué pronto habéis vuelto."
    eri "Hola, Tía [mar]. ¿Lo habéis comprado todo?"
    call BlinkXP("c14s002_400", "d") from _call_BlinkXP_563
    mom "Sí, nos ha costado encontrar un gorro para ti, pero lo tenemos todo."
    call BlinkXP("c14s002_400b", "h") from _call_BlinkXP_564
    mom "¡Oops! *Susurrando* [nor], tu bikini no está... donde debería."
    scene c14s001_905AnBlink with dissolve #efg Blink
    nor "¡Oops! Nada que no hayaís visto ninguno, ¿no? Somos todo chicas... y [mc], que ha visto a las chicas mil veces."
    call BlinkXP("c14s001_905b", "d") from _call_BlinkXP_565
    mom "Vale, pero no hace falta que te exhibas..."
    mc "¿Un gorro para [eri]? No tiene la cabeza grande. *Risa*"
    call BlinkXP("c14s002_410", "d") from _call_BlinkXP_566
    mom "Si es difícil encontrar gorros navideños en Julio, imagínate encontrarlos negros. Tu prima tiene alergia al rojo."
    call BlinkXP("c14s001_910", "d") from _call_BlinkXP_567
    eri "Y al rosa. *Risa*"
    call BlinkXP("c14s002_420", "d") from _call_BlinkXP_568
    mom "Calla, calla, que [emm] ha encontrado un gorro rosa."
    scene c14s001_910d with dissolve
    nor "Lo de [emm] con el rosa..."
    eri "¡Eso tengo que verlo!"
    mc "Id vosotras. Yo prefiero la sorpresa mañana. Iré a ducharme."
    scene c14s001_910e with dissolve
    nor "Hasta luego, [mc]."
    eri "¡Vale! Nos vemos luego."
    call BlinkXP("c14s002_435", "d") from _call_BlinkXP_569
    mom "Hasta luego, [mc]."
    scene c14s002_440c with dissolve
    stop music fadeout (1.5)
    "Las tres se van, riéndose de algo que no puedes escuchar. Tan parecidas y diferentes a la vez."
    scene black with dissolve
    return
label c14s002_CumInNor:
    call OrgasmX("c14s001_820") from _call_OrgasmX_12
    "Explotas en la boca de [nor] mientras [eri] le sujeta la cabeza."
    mc "¡Mpfft!"
    eri "¡Déjame algo para mí!"
    call BlinkXP("c14s001_825", "d") from _call_BlinkXP_570
    "Después de limpiar tu polla, [nor] te mira inquisitivamente."
    mc "¿Me estás preguntando que hacer con la corrida?"
    scene c14s001_830An with dissolve #aba
    "[nor] asiente."
    if persistent.walkthrough:
        if persistent.lesbian:
            $ wt1 = _("Beso blanco.")
        else:
            $ wt1 = _("Beso blanco sin contenido lésbico.")
        $ wt2 = _("Sin consecuencias.")
    menu:
        "Compártelo con [eri]." (wt = wt1):
            scene c14s001_835An with dissolve #abc
            "Las dos te miran con sorpresa inicial, pasando después a una sonrisa de pillería tras mirarse."
            scene c14s001_835An2 with dissolve #dh
            "[nor] se incorpora un poco antes de dejar caer tu corrida en la boca abierta de [eri]."
            mc "¡Wow! Eso ha sido muy tórrido..."
            if persistent.lesbian:
                scene c14s001_835e with dissolve
                if persistent.family:
                    "[nor] deja caer su cabeza hasta que sus labios rozan los de su hija, para sorpesa de ésta."
                else:
                    "[nor] deja caer su cabeza hasta que sus labios rozan los de la que pasa por su hija, para sorpesa de ésta."
                scene c14s001_835f with dissolve
                "[eri] tarda un segundo en devolverle el beso a su madre. Si antes era tórrido, ahora casi podrías arder solo con ver esa imagen."
                mc "¡Wow! Eso es mejor todavía..."
            scene c14s001_835g with dissolve
            nor "¿Qué te ha parecido?"
            mc "¡Increíble! Que dos mujeres como vosotras me coman así... sin palabras..."
            if persistent.lesbian:
                mc "Y el beso final... ¡Ufff!"
            eri "Después de la sorpresa inicial ha sido una experiencia impresionante..."
            scene c14s001_840e with dissolve
            nor "La próxima vez lo podemos hacer al revés si quieres..."
            eri "¡Genial! Quiero repetir esto, ha sido una pasada..."
        "Trágatelo si quieres." (wt = wt2):
            scene c14s001_840An with dissolve #a-d
            "[nor] hace caso de tu petición sin dudar, mientras [eri] os mira a ambos con cara de sorpresa."
            eri "¡Wow! Eso ha sido muy tórrido, Mamá."
            scene c14s001_840e with dissolve
            nor "La próxima vez puedes hacerlo tú, cielo. A los chicos les gusta. O al menos a [mc]."
            eri "Lo haré, lo haré... Quiero repetir esto, ha sido una pasada..."
        "Escúpelo si quieres." (wt = wt2):
            scene c14s001_845An with dissolve #a-c
            $ Aux3 = True
            "[nor] se levanta a escupir tu corrida en una de las macetas y vuelve unos segundos después."
            scene c14s001_845d with dissolve
            eri "Tendrías que habértelo tragado... he leído que a los chicos les gusta."
            nor "La próxima vez..."
            eri "No, no. La próxima vez me toca a mí. Quiero continuar esto, ha sido una pasada... y nuestro chico puede correrse otra vez, ¿no?"
    $ resetWalkthrough ()
    return
label c14s002_CumInEri:
    call OrgasmX("c14s001_850") from _call_OrgasmX_13
    "Explotas en la boca de [eri] mientras [nor] le sujeta la cabeza."
    mc "¡Mpfft!"
    nor "¡Recógela toda, no te dejes nada!"
    call BlinkXP("c14s001_855", "d") from _call_BlinkXP_571
    "Después de limpiar tu polla, [eri] te mira inquisitivamente."
    mc "¿Me estás preguntando que hacer con la corrida?"
    scene c14s001_860An with dissolve #aba
    "[eri] asiente."
    if persistent.walkthrough:
        if persistent.lesbian:
            $ wt1 = _("Beso blanco.")
        else:
            $ wt1 = _("Beso blanco sin contenido lésbico.")
        $ wt2 = _("Sin consecuencias.")
    menu:
        "Compártelo con tu madre." (wt = wt1):
            scene c14s001_865An with dissolve #abc
            "Las dos te miran con sorpresa inicial, pasando después a una sonrisa de pillería tras mirarse."
            scene c14s001_865An2 with dissolve #dh
            "[eri] se incorpora un poco antes de dejar caer tu corrida en la boca abierta de [nor]."
            mc "¡Wow! Eso ha sido muy tórrido..."
            if persistent.lesbian:
                scene c14s001_865e with dissolve
                if persistent.family:
                    "[eri] deja caer su cabeza hasta que sus labios rozan los de su madre, para sorpesa de ésta."
                else:
                    "[eri] deja caer su cabeza hasta que sus labios rozan los de la que pasa por su madre, para sorpesa de ésta."
                scene c14s001_865f with dissolve
                "[nor] tarda un segundo en devolverle el beso a su hija. Si antes era tórrido, ahora casi podrías arder solo con ver esa imagen."
                mc "¡Wow! Eso es mejor todavía..."
            scene c14s001_835g with dissolve
            eri "¿Qué te ha parecido?"
            mc "¡Increíble! Que dos mujeres como vosotras me coman así... sin palabras..."
            if persistent.lesbian:
                mc "Y el beso final... ¡Ufff!"
            nor "Después de la sorpresa inicial ha sido una experiencia impresionante..."
            scene c14s001_840e with dissolve
            eri "La próxima vez lo podemos hacer al revés si quieres..."
            nor "¡Genial! Quiero repetir esto, ha sido una experiencia preciosa..."
        "Trágatelo si quieres." (wt = wt2):
            scene c14s001_870An with dissolve #a-d
            "[eri] hace caso de tu petición sin dudar, mientras [nor] os mira a ambos con cara de sorpresa."
            nor "¡Wow! Eso ha sido muy tórrido, cielo. Tu primera mamada y tragando como una campeona."
            scene c14s001_840e with dissolve
            eri "La próxima vez puedes hacerlo tú, Mamá. He leído que a los chicos les gusta. O al menos parece que a [mc] le gusta."
            nor "Lo sé y lo haré... Quiero repetir esto, ha sido una pasada..."
        "Escúpelo si quieres." (wt = wt2):
            scene c14s001_875An with dissolve #abc
            $ Aux3 = True
            "[eri] se levanta a escupir tu corrida en una de las macetas y vuelve unos segundos después."
            scene c14s001_875d with dissolve
            nor "Tendrías que habértelo tragado... creo que a [mc] le gusta."
            eri "La próxima vez..."
            nor "No, no. La próxima vez me toca a mí. Quiero continuar esto, ha sido una pasada... y nuestro chico puede correrse otra vez, ¿no?"
    $ resetWalkthrough ()
    return
label c14s002_CumOnFaces:
    call OrgasmX("c14s001_880") from _call_OrgasmX_14
    "Explotas en una fuente de semen, que rocía ambas caras, que lo reciben con una mezcla de sorpresa y placer."
    mc "¡Mpfft!"
    nor "Esto es muchísimo..."
    eri "Me parece que es más que la última vez... pero claro, no lo ví, estaba dentro de mí."
    scene c14s001_885a with dissolve
    nor "Cuanto más cachondo se pone más cantidad se corre."
    eri "Eso quiere decir que le ha puesto muy cachondo hacer esto con nosotras, ¿no?"
    mc "No os podéis llegar a imaginar cuanto."
    scene c14s001_885b with dissolve
    nor "Pues tenemos que repetirlo..."
    eri "La próxima vez... ¿podrás acabar en mi boca?"
    return
label c14s002_Nor:
    play music ("music/Bolero.ogg")
    call BlinkXP("c14s002_200", "d") from _call_BlinkXP_572
    eri "¿Sabéis una cosa? Ahora que [mc] ha acabado de ponerme crema, creo que voy a ir a la azotea a tomar el sol... Con la humedad de la piscina... voy a empezar a sudar..."
    eri "Y ahí arriba puedo hacer topless sin que ningún camionero me vea por encima de las vallas al pasar."
    mc "¿Quieres que subamos contigo? Te vas a aburrir allí sola..."
    call BlinkXP("c14s002_205", "d") from _call_BlinkXP_573
    nor "[mc]..."
    call BlinkXP("c14s002_210", "d") from _call_BlinkXP_574
    eri "Mejor quedaos aquí vosotros. No estaría cómoda haciendo topless delante tuyo."
    eri "Hasta luego, pasadlo bien."
    call BlinkXP("c14s002_215", "d") from _call_BlinkXP_575
    nor "Hasta luego, cielo."
    mc "Nos vemos, [eri]."
    call BlinkXP("c14s002_220", "d") from _call_BlinkXP_576
    mc "¿Me lo parece o nos ha querido dejar solos?"
    nor "Lo ha hecho. Supongo que decir que habría menos tú para nosotras le ha hecho recordar que estamos juntos."
    nor "Aunque no vayamos a hacer nada... inapropiado... en la piscina, quiere dejarnos espacio."
    mc "Siempre la he querido, pero ahora podría subir a besarla. Si no fuera porque entonces te dejaría a ti sola, y..."
    call BlinkXP("c14s002_225", "d") from _call_BlinkXP_577
    nor "Sí, su gesto perdería todo el sentido si me dejas aquí sola. *Risa*"
    mc "Y sobre lo de no hacer nada, ya se verá."
    call BlinkXP("c14s002_230", "d") from _call_BlinkXP_578
    nor "No creerás que vamos a..."
    mc "A acabar ese masaje que he empezado. Todavía queda mucha piel por recubrir de crema."
    scene c14s001_650An with dissolve
    nor "Déjame desabrocharme esto para que puedas volver a mi espalda. No quiero líneas blancas."
    scene c14s001_670AnBlink with dissolve
    nor "Y ahora ya puedes continuar. Sin lineas blancas en ningún sitio."
    scene c14s002_915pv
    show c14s002_915v
    mc "Me encanta el tacto de tu piel, ahora sin la parte de arriba del bikini lo puedo disfrutar más."
    nor "¿Grasiento por la crema? *Risa*"
    mc "No me refiero a eso y lo sabes."
    scene c14s001_700pv
    hide c14s002_915v
    show c14s001_700v
    nor "Eso me parece bien."
    "La piel de [nor] es suave como la seda, tus manos resbalan por su culo ayudadas por la crema."
    nor "Me gusta... casi demasiado..."
    scene c14s001_725AnBlink with dissolve #Blink with punch
    nor "Hey... eso no necesita crema. Nunca llega a darle el sol..."
    mc "Pues ahora está llegando, con lo que hay que protegerlo."
    scene c14s002_920pv
    hide c14s001_700v
    show c14s002_920v
    mc "Cielo, estás mojadísima... ¿cuándo te has puesto cachonda?"
    nor "*Gemido* He empezado a ponerme cuando has llegado. He seguido cuando me has dado el masaje, y me he terminado de empapar en cuanto mi hija se ha ido."
    mc "Con lo que esperabas algo... ¿cómo lo has llamado? ¿inapropiado?"
    nor "*Jadeo* No lo esperaba... pero lo deseaba... Aunque te tuve ayer en mi cama... se me ha hecho eterno..."
    mc "Lo tenemos que resolver. No puede ser que te tenga tan cerca todos los días y no pueda besarte como es debido... ni hacer otras cosas..."
    scene c14s002_925pv
    hide c14s002_920v
    show c14s002_925v
    nor "*Gemido* No voy a discutir ahora... esa paja está siendo buenísima..."
    mc "Entonces..."
    nor "*Jadeo* Me refiero a... que no quiero discutir... no a que vaya a aceptar... lo que pidas..."
    mc "Entonces calla y concéntrate en lo que estás sintiendo."
    scene c14s002_920pv
    hide c14s002_925v
    show c14s002_920v
    "Por raro que parezca, consigues que tu novia te haga caso. Seguramente mañana recibas una llamada del Doctor Xabier preguntándote por ese superpoder."
    "Te concentras en acompasar tu ritmo a los jadeos que salen de su boca, mientras notas la humedad de [nor] en tus dedos con cada caricia en su coño."
    "Por un momento te sientes observado. Sabes que no hay nadie en casa y hubieras oído los coches al llegar. O el autobús de la universidad."
    "La sensación se vuelve más potente tal como empiezan a pasar los minutos, hasta que descubres quién os está observando."
    scene c14s002_260b with dissolve
    mc "Creo que [eri] y tú hacéis la pareja perfecta madre e hija. La exhibicionista y la voyeur... nos está mirando desde la terraza."
    call BlinkXP("c14s002_255", "d") from _call_BlinkXP_579
    nor "Lo sé. *Gemido* Hace un rato que la he visto... *Jadeo*"
    mc "¿Te pone?"
    call BlinkXP("c14s002_265", "d") from _call_BlinkXP_580
    nor "Mucho... *Jadeo* creo que mi exhibicionismo acaba de subir de nivel con esto..."
    mc "¿Te falta mucho para llegar?"
    scene c14s002_925pv
    hide c14s002_920v
    show c14s002_925v
    nor "Estoy a punto... *Jadeo*"
    mc "Debe ser por ese punto exhibicionista, seguro..."
    nor "¿Por qué ... *Gemido* lo dices?"
    mc "Es la primera vez que estamos en un sitio donde nos pueden pillar, aparte de la primera vez cuando nos pilló [eri]..."
    call OrgasmX("c14s001_770") from _call_OrgasmX_15 #nor
    nor "¡JODER! *GEMIDO* ¡SI! ¡Justo ahí!"
    "La explosión del cuerpo de [nor] te pilla por sorpresa. No has notado las señales habituales. ¿Realmente le pone la idea de que la pillen?"
    call BlinkXP("c14s002_280", "d") from _call_BlinkXP_581
    nor "Eso ha sido intenso..."
    mc "Ha sido la primera vez que tienes un orgasmo así..."
    call BlinkXP("c14s002_285", "d") from _call_BlinkXP_582
    nor "No sabía que fuera capaz de hacerlo. Cuando has dicho lo de que nos pueden pillar... ha sido un subidón..."
    mc "Bueno, técnicamente ya nos habían pillado. Tenemos espectadores. ¿Sigue mirando?"
    scene c14s002_260a with dissolve
    nor "Sí, creo que lo está disfrutando a su manera. Eso también me ha puesto muy cachonda."
    call BlinkXP("c14s002_290", "d") from _call_BlinkXP_583
    nor "Aunque me parece que hemos terminado el espectáculo demasiado pronto para ella. Dame un segundo que me recupere y voy a por ti. Sigamos con el espectáculo."
    mc "Déjame ponerte crema por delante mientras tanto."
    call BlinkXP("c14s002_295", "d") from _call_BlinkXP_584
    nor "Ahí llego yo."
    mc "Pero no creo que [eri] lo disfrute tanto si lo haces tú."
    call BlinkXP("c14s002_300", "d") from _call_BlinkXP_585
    nor "¿A ti también te pone que nos mire?"
    mc "Digamos que no me importa que mire y que se merece un premio por habernos dejado a solas. *Risa*"
    call BlinkXP("c14s002_305", "f") from _call_BlinkXP_586
    nor "Por cierto, tú y yo tenemos una ducha pendiente. Con sexo. He soñado muchas veces con aquel día."
    mc "Cuando quieras, además esos orgasmos explosivos quedarán un poco diluidos. No cerraremos el pestillo para que tengas la sensación de que nos pueden pillar."
    call BlinkXP("c14s002_310", "d") from _call_BlinkXP_587
    nor "¿Te gustan?"
    mc "Sí, dan una sensación de... no sé... de mejor orgasmo..."
    nor "No sé decirte si mejor o peor. Diferente y muy intenso..."
    call BlinkXP("c14s002_315", "d") from _call_BlinkXP_588
    nor "¡Hey! No te olvides de las gemelas, las he destapado por algo y no querrás que se quemen. *Risa*"
    scene c14s002_320a with dissolve
    mc "Por supuesto que no. Y si tenemos que dar el espectáculo, mejor darlo del todo, ¿no?"
    nor "No me voy a quejar. Me encanta notar tus manos en cualquier parte de mi cuerpo."
    scene c14s002_320b with dissolve
    "Te limpias el dedo de crema en el bañador antes de llevarlo a sus labios."
    mc "¿Aquí también?"
    scene c14s002_320c with dissolve
    nor "¡Ñam! Incluso en los dientes."
    scene c14s002_320d with dissolve
    mc "¿Y aquí?"
    nor "Uno de los mejores sitios. Se ponen duros solo con que te acerques."
    scene c14s002_320e with dissolve
    mc "¿Qué me dices de aquí?"
    nor "*Gemido* Que está muy sensible, pero me encanta."
    mc "No sé por qué, pero me lo parecía."
    call BlinkXP("c14s002_325", "d") from _call_BlinkXP_589
    nor "*Jadeo* Pero yo también quiero algo en mis manos. No quiero ser la única que reciba placer."
    scene c14s002_330a with dissolve
    "En un rápido movimiento, [nor] baja tu bañador y coge tu enhiesta polla en su mano, empezando a masturbarte."
    nor "¿Ves? *Jadeo* Me gusta más así, de la otra forma me siento... *Gemido* demasiado pasiva..."
    scene c14s002_935pv
    hide c14s002_930v
    show c14s002_935v
    "[nor] continúa masturbándote tras un reajuste de la postura digno de un contorsionista para darte acceso a sus tesoros."
    "La masturbación mutua mientras sois observados por [eri] es muy excitante a la vez que placentera."
    scene c14s002_940pv
    hide c14s002_935v
    show c14s002_940v
    nor "*Gemido* ¿Estás cerca de correrte?"
    mc "Ni de lejos. Acabamos de empezar. ¿Tú?"
    nor "*Jadeo* Ya te he dicho que estaba sensible... *Gemido* No voy a durar mucho y me gustaría que nos corriéramos juntos..."
    mc "No te preocupes por eso, preocúpate por disfrutar. No podemos saber cuándo será la próxima vez que tengamos la casa para nosotros."
    scene c14s002_935pv
    hide c14s002_940v
    show c14s002_935v
    nor "Pero es que... *Gemido* no querría que te... *Jadeo* quedaras a medias..."
    "Empiezas a hacer más presión sobre su clítoris en cada movimiento, notando como su cuerpo se tensa, acercándose al clímax. Esta vez las señales son claras."
    mc "No me voy a quedar a medias, tenemos tiempo..."
    mc "Y si llega toda la familia, tendremos más público."
    call OrgasmX("c14s002_345") from _call_OrgasmX_16
    nor "*GEMIDO* ¡Joder! ¡Aquí llega! ¡Por Dios!"
    "Otra vez [nor] vuelve a explotar en un mar de fluidos que emanan de su cuerpo entre espasmos de placer."
    "Su cuerpo se retuerce en oleadas mientras tú aprietas su clítoris para alargar al máximo su orgasmo."
    "En ningún momento ella suelta tu polla. Sus espasmos hacen que no pueda seguir con sus movimientos, pero se mantiene agarrada a ella como si su vida dependiera de ello."
    "Poco a poco su cuerpo empieza a relajarse tras las últimas contracciones de su clímax."
    call BlinkXP("c14s002_350", "d") from _call_BlinkXP_590
    nor "Estoy enferma... has dicho lo de tener más público y me he imaginado a [mar], a mi madre, y a [dap] uniéndose a [eri] en la azotea..."
    nor "Me he corrido al momento..."
    mc "Y te has dejado a las estudiantes, a [emm], y a Tía Betty. *Risa* Por no hablar de Kiara y [eil]."
    call BlinkXP("c14s002_355", "d") from _call_BlinkXP_591
    nor "Betty me daría mal rollo si me la imaginara de monja. *Risa*"
    nor "Pero dejemos el tema por ahora. Tu amigo requiere mi atención antes de que se te ocurra volver a tocarme."
    scene c14s002_945pv
    hide c14s002_935v
    show c14s002_945v
    "[nor] rodea tu polla con sus labios y empieza a hacer recorridos cortos a lo largo de tu astil."
    "Cada vez que tiene tu capullo al alcance de su lengua realiza un movimiento circular en el que te da la impresión de que rodea tu glande por completo."
    "La sensación de la presión perfecta de sus rojos labios sumada a los jugueteos de su lengua hacen que te acerques al orgasmo a pasos agigantados."
    "La paja anterior te ha dejado más cerca de lo que hubieras pensado, y ver tu polla en la boca de [nor] un día después de la última vez es una imagen increíble."
    scene c14s002_950pv
    hide c14s002_945v
    show c14s002_950v
    mc "Sigue así, [nor]. Lo estás haciendo genial."
    nor "*Gemido*"
    "[nor] empieza a hacer más presión con sus labios, aprisionando tu astil entre esas dos bellezas oscuras."
    "Tu excitación crece a la vez que el frenesí con el que su lengua acaricia tu glande."
    "Los ruidos húmedos que hace en cada movimiento se suman a sus gemidos para producir una combinación perfecta que llena tus sentidos."
    mc "[nor], estoy a punto."
    "A ella no le importa que estés a punto. Esta vez no te va a dejar decidir dónde quieres correrte. Quiere acabar la mamada a su manera."
    call OrgasmX("c14s002_370") from _call_OrgasmX_17
    hide c14s002_950v
    "Explotas dentro de su boca liberando todo el semen que has acumulado desde que os habéis quedado solos."
    mc "¡Mpfft!"
    "Pese a tu aviso, [nor] se sorprende con tu descarga y no es capaz de retener en su boca todo tu semen."
    scene c14s002_375AnBlink with dissolve #defg-Blink
    nor "¿Te ha gustado, cielo? Me da la impresión de que cada vez te corres en mayor cantidad..."
    mc "[nor], has estado increíble. La excitación de los últimos minutos ha sido impresionante."
    mc "Se te ha escapado un poco por la comisura de los labios..."
    "Justo en ese momento oís el motor de un coche y la verja abriéndose. Os han dado el tiempo justo para acabar, aunque no para un segundo round."
    stop music fadeout (1.5)
    scene c14s002_380AnBlink with dissolve #1_890a, d, blink
    nor "¡Oh, mierda! Un poco más y nos pillan. Voy a meterme en la piscina..."
    scene c14s002_380e with dissolve
    mc "Espera..."
    play sound ("music/Splash.ogg")
    scene c14s001_895An2 with dissolve #b-d #tira el top al agua
    mcp "(Espero que lo coja antes de que la vea alguien)"
    call BlinkXP ("c14s002_685", "f") from _call_BlinkXP_592
    "Te terminas de subir el bañador justo cuando aparece [mar]."
    play music ("music/ChillUkelele.ogg")
    mom "Hola, [mc]. ¿Estás solo?"
    mc "No, [nor] está buceando y [eri] en la azotea tomando el sol."
    call c14s002_PartyExplanation from _call_c14s002_PartyExplanation_1
    scene c14s002_390a with dissolve
    mc "Mira, por ahí vuelve [nor] de su buceo."
    call BlinkXP("c14s002_395", "d") from _call_BlinkXP_593
    nor "Hola, [mar]. ¿Lo habéis comprado todo?"
    call BlinkXP("c14s002_400", "d") from _call_BlinkXP_594
    mom "Sí, nos ha costado encontrar un gorro para [eri], pero lo tenemos todo."
    call BlinkXP("c14s002_400b", "h") from _call_BlinkXP_595
    mom "¡Oops! *Susurrando* [nor], tu bikini no está... donde debería."
    scene c14s001_905AnBlink with dissolve #efg Blink
    nor "¡Oops! Nada que no hayaís visto ninguno, ¿no? Somos todo chicas... y [mc], que ha visto a las chicas mil veces."
    call BlinkXP("c14s001_905b", "d") from _call_BlinkXP_596
    mom "Vale, pero no hace falta que te exhibas..."
    mc "¿Un gorro para [eri]? No tiene la cabeza grande. *Risa*"
    call BlinkXP("c14s002_410", "d") from _call_BlinkXP_597
    mom "Si es difícil encontrar gorros navideños en Julio, imagínate encontrarlos negros. Tu prima tiene alergia al rojo."
    call BlinkXP("c14s002_415", "d") from _call_BlinkXP_598
    nor "Y al rosa. *Risa*"
    call BlinkXP("c14s002_420", "d") from _call_BlinkXP_599
    mom "Calla, calla, que [emm] ha encontrado un gorro rosa."
    call BlinkXP("c14s002_425", "d") from _call_BlinkXP_600
    nor "¡Eso tengo que verlo!"
    mc "Id vosotras. Yo prefiero la sorpresa mañana. Iré a ducharme."
    call BlinkXP("c14s002_430", "d") from _call_BlinkXP_601
    nor "¡Vale! Nos vemos luego."
    call BlinkXP("c14s002_435", "d") from _call_BlinkXP_602
    mom "Hasta luego, [mc]."
    scene c14s002_440a with dissolve
    stop music fadeout (1.5)
    "Las dos se van, riéndose de algo que no puedes escuchar. Tan parecidas y diferentes a la vez."
    scene black with dissolve
    return
label c14s002_Eri:
    play music ("music/Bolero.ogg")
    call BlinkXP("c14s002_500", "d") from _call_BlinkXP_603
    nor "¿Sabéis una cosa? Ahora que [mc] ha acabado de ponerme crema, creo que voy a ir a la azotea a tomar el sol... Con la humedad de la piscina... voy a empezar a sudar..."
    nor "Y ahí arriba puedo hacer topless sin que ningún camionero me vea por encima de las vallas al pasar."
    mc "¿Quieres que subamos contigo? Te vas a aburrir allí sola..."
    call BlinkXP("c14s002_505", "d") from _call_BlinkXP_604
    eri "[mc]..."
    call BlinkXP("c14s002_510", "d") from _call_BlinkXP_605
    nor "Mejor quedaos aquí vosotros. No estaría cómoda haciendo topless delante tuyo. Mi exhibicionismo no llega a tanto... todavía."
    nor "Hasta luego, pasadlo bien."
    call BlinkXP("c14s002_515", "d") from _call_BlinkXP_606
    eri "Hasta luego, Mamá."
    mc "Nos vemos, [nor]."
    call BlinkXP("c14s002_520", "d") from _call_BlinkXP_607
    mc "¿Me lo parece o nos ha querido dejar solos?"
    eri "Lo ha hecho. Supongo que decir que habría menos tú para nosotras le ha hecho recordar que estamos juntos."
    eri "Aunque no vayamos a hacer nada... inapropiado... en la piscina, quiere dejarnos espacio."
    mc "Siempre la he querido, pero ahora podría subir a besarla. Si no fuera porque entonces te dejaría a ti sola, y..."
    call BlinkXP("c14s002_525", "d") from _call_BlinkXP_608
    eri "Sí, su gesto perdería todo el sentido si me dejas aquí sola. *Risa*"
    mc "Y sobre lo de no hacer nada, ya se verá."
    call BlinkXP("c14s002_530", "d") from _call_BlinkXP_609
    eri "No creerás que vamos a..."
    mc "A acabar ese masaje que he empezado. Todavía queda mucha piel por recubrir de crema."
    scene c14s002_955pv
    show c14s002_955v
    eri "Eso me parece bien."
    "La piel de [eri] es suave como la seda, tus manos resbalan por su culo ayudadas por la crema."
    eri "Me gusta... casi demasiado..."
    mc "A mí me encanta el tacto de tu piel."
    eri "¿Grasiento por la crema? *Risa*"
    mc "No me refiero a eso y lo sabes."
    scene c14s002_540An with dissolve
    eri "Hey... eso no necesita crema. Nunca llega a darle el sol..."
    mc "Pues ahora está llegando, con lo que hay que protegerlo."
    scene c14s002_960pv
    hide c14s002_955v
    show c14s002_960v
    mc "Cielo, estás mojadísima... ¿cuándo te has puesto cachonda?"
    eri "*Gemido* He empezado a ponerme cuando has llegado. He seguido cuando me has dado el masaje, y me he terminado de empapar en cuanto mi madre se ha ido."
    mc "Con lo que esperabas algo... ¿cómo lo has llamado? ¿inapropiado?"
    eri "*Jadeo* No lo esperaba... pero lo deseaba... han pasado muchos... días desde la última vez que... estuvimos a solas..."
    mc "Lo tenemos que resolver. No puede ser que te tenga tan cerca todos los días y no pueda besarte como es debido... ni hacer otras cosas..."
    scene c14s002_965pv
    hide c14s002_950v
    show c14s002_965v
    eri "*Gemido* No voy a discutir ahora... esa paja está siendo buenísima..."
    mc "Entonces..."
    eri "*Jadeo* Me refiero a... que no quiero discutir... no a que vaya a aceptar... lo que pidas..."
    mc "Entonces calla y concéntrate en lo que estás sintiendo."
    scene c14s002_960pv
    hide c14s002_965v
    show c14s002_960v
    "Por raro que parezca, consigues que tu novia te haga caso. Seguramente mañana recibas una llamada del Doctor Xabier preguntándote por ese superpoder."
    "Te concentras en acompasar tu ritmo a los jadeos que salen de su boca, mientras notas la humedad de [eri] en tus dedos con cada caricia en su coño."
    "Por un momento te sientes observado. Sabes que no hay nadie en casa y hubieras oído los coches al llegar. O el autobús de la universidad."
    "La sensación se vuelve más potente tal como empiezan a pasar los minutos, hasta que descubres quién os está observando."
    scene c14s002_560a with dissolve
    mc "Creo que tu madre ha sumado el voyerismo al exhibicionismo... nos está mirando desde la terraza."
    call BlinkXP("c14s002_555", "d") from _call_BlinkXP_610
    eri "Lo sé. *Gemido* Hace un rato que la he visto... *Jadeo*"
    mc "¿Te pone?"
    call BlinkXP("c14s002_565", "d") from _call_BlinkXP_611
    eri "Mucho... *Jadeo* creo que he heredado la vena exhibicionista de mi madre..."
    mc "¿Te falta mucho para llegar?"
    scene c14s002_965pv
    hide c14s002_960v
    show c14s002_965v
    eri "Estoy a punto... *Jadeo*"
    mc "Debes tener ese punto exhibicionista, seguro..."
    eri "¿Por qué ... *Gemido* lo dices?"
    mc "Sauna, playa y piscina... nuestras tres veces han sido donde nos pueden pillar..."
    call OrgasmX("c14s002_575") from _call_OrgasmX_18
    eri "¡JODER! *GEMIDO* ¡SI! ¡Justo ahí!"
    "La explosión del cuerpo de [eri] te pilla por sorpresa. No has notado las señales habituales. ¿Realmente le pone la idea de que la pillen?"
    call BlinkXP("c14s002_580", "d") from _call_BlinkXP_612
    eri "Eso ha sido intenso..."
    mc "Ha sido la primera vez que tienes un orgasmo así..."
    call BlinkXP("c14s002_585", "d") from _call_BlinkXP_613
    eri "No sabía que fuera capaz de hacerlo. Cuando has dicho lo de que nos pueden pillar... ha sido un subidón..."
    mc "Bueno, técnicamente ya nos habían pillado. Tenemos espectadores. ¿Sigue mirando?"
    scene c14s002_560b with dissolve
    eri "Sí, creo que lo está disfrutando a su manera. Eso también me ha puesto muy cachonda."
    call BlinkXP("c14s002_590", "d") from _call_BlinkXP_614
    eri "Aunque me parece que hemos terminado el espectáculo demasiado pronto para ella. Dame un segundo que me recupere y voy a por ti. Sigamos con el espectáculo."
    mc "Déjame ponerte crema por delante también."
    call BlinkXP("c14s002_595", "d") from _call_BlinkXP_615
    eri "Ahí llego yo."
    mc "Pero no creo que tu madre lo disfrute tanto si lo haces tú."
    call BlinkXP("c14s002_600", "d") from _call_BlinkXP_616
    eri "¿A ti también te pone que nos mire?"
    mc "Digamos que no me importa que mire y que se merece un premio por habernos dejado a solas. *Risa*"
    call BlinkXP("c14s002_605", "d") from _call_BlinkXP_617
    eri "Por cierto, nuestras tres veces tienen otro componente en común. Sauna, playa y piscina. Agua."
    mc "Espero que, a partir de ahora, también tengan en común esos orgasmos explosivos."
    call BlinkXP("c14s002_610", "d") from _call_BlinkXP_618
    eri "¿Te gustan?"
    mc "Sí, dan una sensación de... no sé... de mejor orgasmo..."
    eri "No sé decirte si mejor o peor. Diferente y muy intenso..."
    mc "Voy a seguir con la crema."
    call BlinkXP("c14s002_615", "d") from _call_BlinkXP_619
    eri "¡Hey! Esas no necesitan crema. *Risa* Van tapadas."
    scene c14s002_615d with dissolve
    mc "Ya no. Y si tenemos que dar el espectáculo, mejor darlo del todo, ¿no?"
    scene c14s002_620a with dissolve
    eri "No me voy a quejar. Me encanta notar tus manos en cualquier parte de mi cuerpo."
    "Te limpias el dedo de crema en el bañador antes de llevarlo a sus labios."
    scene c14s002_620b with dissolve
    mc "¿Aquí también?"
    scene c14s002_620c with dissolve
    eri "¡Ñam! Incluso en los dientes."
    scene c14s002_620d with dissolve
    mc "¿Y aquí?"
    eri "Uno de los mejores sitios. Se ponen duros solo con que los toques."
    scene c14s002_620e with dissolve
    mc "¿Qué me dices de aquí?"
    eri "*Gemido* Que está muy sensible, pero me encanta."
    mc "No sé por qué, pero me lo parecía."
    call BlinkXP("c14s002_625", "d") from _call_BlinkXP_620
    eri "*Jadeo* Pero yo también quiero algo en mis manos. No quiero que vuelva a pasar como en la sauna."
    mc "¿Te vas a quedar dormida? ¿Tan malo soy?"
    eri "Al revés... *Gemido* eres tan bueno que me dejas sin energía para después."
    scene c14s002_630a with dissolve
    "En un rápido movimiento, [eri] baja tu bañador y coge tu enhiesta polla en su mano, empezando a masturbarte."
    eri "¿Ves? *Jadeo* Me gusta más así, de la otra forma me siento... *Gemido* demasiado pasiva..."
    scene c14s002_975pv
    hide c14s002_970v
    show c14s002_975v
    "[eri] continúa masturbándote tras un reajuste de la postura digno de un contorsionista para darte acceso a sus tesoros."
    "La masturbación mutua mientras sois observados por [nor] es muy excitante a la vez que placentera."
    scene c14s002_980pv
    hide c14s002_975v
    show c14s002_980v
    eri "*Gemido* ¿Estás cerca de correrte?"
    mc "Ni de lejos. Acabamos de empezar. ¿Tú?"
    eri "*Jadeo* Ya te he dicho que estaba sensible... *Gemido* No voy a durar mucho y me gustaría que nos corriéramos juntos..."
    mc "No te preocupes por eso, preocúpate por disfrutar. No podemos saber cuándo será la próxima vez que tengamos la casa para nosotros."
    scene c14s002_975pv
    hide c14s002_980v
    show c14s002_975v
    eri "Pero es que... *Gemido* no querría que te... *Jadeo* quedaras a medias..."
    "Empiezas a hacer más presión sobre su clítoris en cada movimiento, notando como su cuerpo se tensa, acercándose al clímax. Esta vez las señales son claras."
    mc "No me voy a quedar a medias, tenemos tiempo..."
    mc "Y si llega toda la familia, tendremos más público."
    call OrgasmX("c14s002_645") from _call_OrgasmX_19
    eri "*GEMIDO* ¡Joder! ¡Aquí llega! ¡Por Dios!"
    "Otra vez [eri] vuelve a explotar en un mar de fluidos que emanan de su cuerpo entre espasmos de placer."
    "Su cuerpo se retuerce en oleadas mientras tú aprietas su clítoris para alargar al máximo su orgasmo."
    "En ningún momento ella suelta tu polla. Sus espasmos hacen que no pueda seguir con sus movimientos, pero se mantiene agarrada a ella como si su vida dependiera de ello."
    "Poco a poco su cuerpo empieza a relajarse tras las últimas contracciones de su clímax."
    call BlinkXP("c14s002_650", "d") from _call_BlinkXP_621
    eri "¿Estoy enferma?... has dicho lo de tener más público y me he imaginado a tu madre, a la abuela, a [dap] y a [emm] uniéndose a mi madre en la azotea..."
    eri "Me he corrido al momento..."
    mc "Y te has dejado a las estudiantes y a Tía Betty. *Risa* Por no hablar de Kiara y [eil]."
    call BlinkXP("c14s002_655", "d") from _call_BlinkXP_622
    eri "Tía Betty me daría mal rollo si me la imaginara de monja. *Risa*"
    eri "Pero dejemos el tema por ahora. Tu amigo requiere mi atención antes de que se te ocurra volver a tocarme."
    scene c14s002_985pv with fade
    hide c14s002_975v
    show c14s002_985v
    "[eri] rodea tu polla con sus labios y empieza a hacer recorridos cortos a lo largo de tu astil."
    "Cada vez que tiene tu capullo al alcance de su lengua realiza un movimiento circular en el que te da la impresión de que rodea tu glande por completo."
    "La sensación de la presión perfecta de sus negros labios sumada a los jugueteos de su lengua hacen que te acerques al orgasmo a pasos agigantados."
    "La paja anterior te ha dejado más cerca de lo que hubieras pensado, y ver tu polla en la boca de [eri] por primera vez es una imagen increíble."
    scene c14s002_990pv
    hide c14s002_985v
    show c14s002_990v
    mc "Sigue así, [eri]. Lo estás haciendo genial."
    eri "*Gemido*"
    "[eri] empieza a hacer más presión con sus labios, aprisionando tu astil entre esas dos bellezas oscuras."
    "Tu excitación crece a la vez que el frenesí con el que su lengua acaricia tu glande."
    "Los ruidos húmedos que hace en cada movimiento se suman a sus gemidos para producir una combinación perfecta que llena tus sentidos."
    mc "[eri], estoy a punto."
    "A ella no le importa que estés a punto. Es la primera vez que te hace una mamada y quiere acabarla a su manera."
    call OrgasmX("c14s002_670") from _call_OrgasmX_20
    "Explotas dentro de su boca liberando todo el semen que has acumulado desde que os habéis quedado solos."
    mc "¡Mpfft!"
    "Pese a tu aviso, [eri] se sorprende con tu descarga y no es capaz de retener en su boca todo tu semen."
    scene c14s002_675AnBlink with dissolve
    eri "¿Qué tal lo he hecho? Ya sabes que ha sido mi primera vez..."
    mc "[eri], has estado increíble. La excitación de los últimos minutos ha sido impresionante."
    mc "Se te ha escapado un poco por la comisura de los labios..."
    "Justo en ese momento oís el motor de un coche y la verja abriéndose. Os han dado el tiempo justo para acabar, aunque no para un segundo round."
    scene c14s002_680An with dissolve #c14s001_890a, abc
    stop music fadeout (1.5)
    eri "¡Oh, mierda! Un poco más y nos pillan. Voy a meterme en la piscina..."
    scene c14s002_680e with dissolve
    mc "Espera..."
    play sound ("music/Splash.ogg")
    call BlinkXP ("c14s002_685", "f") from _call_BlinkXP_623
    "Te terminas de subir el bañador justo cuando aparece [mar]."
    play music ("music/ChillUkelele.ogg")
    mom "Hola, [mc]. ¿Estás solo?"
    mc "No, [eri] está buceando y [nor] en la azotea tomando el sol."
    call c14s002_PartyExplanation from _call_c14s002_PartyExplanation_2
    scene c14s002_690a with dissolve
    mc "Mira, por ahí vuelve [eri] de su buceo."
    call BlinkXP("c14s002_695", "d") from _call_BlinkXP_624
    eri "Hola, Tía [mar]. ¿Lo habéis comprado todo?"
    call BlinkXP("c14s002_400", "d") from _call_BlinkXP_625
    mom "Sí, nos ha costado encontrar un gorro para ti, pero lo tenemos todo."
    call BlinkXP("c14s002_400b", "h") from _call_BlinkXP_626
    mom "¡Oops! *Susurrando* [eri], tu bikini no está... donde debería."
    scene c14s002_700An with dissolve #2_695a-d-e-f-g
    eri "*Susurrando* ¡Oops! "
    mc "¿Un gorro para ella? No tiene la cabeza grande. *Risa*"
    call BlinkXP("c14s002_410", "d") from _call_BlinkXP_627
    mom "Si es difícil encontrar gorros navideños en Julio, imagínate encontrarlos negros. Tu prima tiene alergia al rojo."
    call BlinkXP("c14s002_705", "d") from _call_BlinkXP_628
    eri "Y al rosa. *Risa*"
    call BlinkXP("c14s002_420", "d") from _call_BlinkXP_629
    mom "Calla, calla, que [emm] ha encontrado un gorro rosa."
    call BlinkXP("c14s002_710", "d") from _call_BlinkXP_630
    eri "¡Eso tengo que verlo!"
    mc "Id vosotras. Yo prefiero la sorpresa mañana. Iré a ducharme."
    call BlinkXP("c14s002_715", "d") from _call_BlinkXP_631
    eri "¡Vale! Nos vemos luego."
    call BlinkXP("c14s002_435", "d") from _call_BlinkXP_632
    mom "Hasta luego, [mc]."
    scene c14s002_440b with dissolve
    stop music fadeout (1.5)
    "Las dos se van, riéndose de algo que no puedes escuchar. Tan parecidas y diferentes a la vez."
    scene black with dissolve
    return
label c14s002_PartyExplanation:
    call BlinkXP("c14s002_450", "d") from _call_BlinkXP_633
    if mar._var("route"):
        mom "*Susurrando* Lástima... quería hablar contigo... y darte un beso como Dios manda ahora que todas han ido a dejar las compras a casa de [nor]."
        mc "*Susurrando* Habrá tiempo más tarde. ¿Por qué no subes a mi habitación esta noche?"
    else:
        mom "Genial, [emm] ha subido a tu habitación las cosas que hemos comprado."
    mc "¿Qué habéis comprado?"
    call BlinkXP("c14s002_455", "d") from _call_BlinkXP_634
    mom "Cosas para la fiesta de mañana."
    mc "¿Fiesta? ¿Qué fiesta?"
    call BlinkXP("c14s002_460", "d") from _call_BlinkXP_635
    mom "Claro, tú no estabas. [dap] nos ha dicho que [sca] comentó hace unos días de hacer una fiesta de Navidad en Verano."
    mom "Hemos pensado que sería bueno ir mañana a la playa en familia, para que [sca] se sienta más bienvenida."
    mom "Y nos hemos ido de compras, bañadores, gorros de Santa Claus, adornos navideños... Es difícil encontrar todo eso en Julio. También hemos comprado comida y bebida."
    mc "¿Y me habéis comprado algo a mí también?"
    call BlinkXP("c14s002_465", "d") from _call_BlinkXP_636
    mom "Sí, un bañador rojo y un gorro de Santa."
    if mar._var("route"):
        call BlinkXP("c14s002_470", "d") from _call_BlinkXP_637
        mom "*Susurrando* Vas a estar super sexy. Me costará resistirme a quitártelo a mordiscos."
    mc "*Risa* ¿Un bañador rojo? ¿Todos vamos a ir de rojo? Vamos a parecer los Socorristas de la Playa."
    call BlinkXP("c14s002_475", "d") from _call_BlinkXP_638
    mom "No todos. [eri] nos ha dicho que como le comprásemos algo rojo tendríamos que ir a la playa nudista, que no se lo pensaba poner."
    mom "La mayoría de los bikinis de [nor] son rojos, y [emm] también tiene. También hemos comprado para las chicas nuevas."
    call BlinkXP("c14s002_480", "d") from _call_BlinkXP_639
    mom "Lo de pedirles sus tallas de bikini ha sido una conversación rara por teléfono. *Risa* \"Hola, soy tu casera, ¿me dices tu talla de ropa interior?\" *Risa*"
    mom "Y para hacer una Navidad completa, me ha llamado [sam] para decir de ir un día a la playa en familia. ¡Qué casualidad!"
    return
label c14s003_SairaChat:
    scene black with dissolve
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        call mrS3_sai_route from _call_mrS3_sai_route_13
        call mrS3_sam_route from _call_mrS3_sam_route_10
        call mrS3_sim_route from _call_mrS3_sim_route_12
        call mrS3_sca_route from _call_mrS3_sca_route_14
        call mrS3_emm_route from _call_mrS3_emm_route_25
        call mrS3_eil_route from _call_mrS3_eil_route_13
        call mrS3_nor_route from _call_mrS3_nor_route_16
        call mrS3_eri_route from _call_mrS3_eri_route_17
        if mc._var("relationships") < 4:
            menu:
                "¿Cuantas relaciones tienes?"
                "1" if mc._var("relationships") <=1:
                    $ mc._var("relationships", 1, intention = "set")
                "2" if mc._var("relationships") <=2:
                    $ mc._var("relationships", 2, intention = "set")
                "3" if mc._var("relationships") <=3:
                    $ mc._var("relationships", 3, intention = "set")
                "Más de 3":
                    $ mc._var("relationships", 4, intention = "set")
    if nor._var("route") or eri._var("route"):
        "Recoges la crema solar y entras en casa. Ha faltado muy poco para que os pillen..."
        mcp "(Me da lo mismo. Ójala pudiera hacer público con quién estoy saliendo y no tuviera que preocuparme de guardar secretos.)"
        mcp "(Con [nor] y [eri] se ha demostrado que hacerlo público fue una buena idea.)"
        if sam._var("route") and sim._var("route"):
            mcp "(Con [sam] y [sim] no ha ido nada mal. Aunque no sea de la forma que hubiera querido.)"
        elif sam._var("route") and not sim._var("route"):
            mcp "(Con [sam] y [sim] ha ido bastante mal. Si se lo hubiéramos contado antes seguramente hubiera ido mejor.)"
        elif sim._var("route"):
            mcp "(Con [sam] y [sim] no ha ido nada mal. Aunque no sea de la forma que hubiera querido, al final ha sido casi gracioso. Pobre [sim]...)"
    "Subes a tu habitación, te das una ducha y te tumbas a descansar un rato."
    "No pasa mucho tiempo antes de que suenen unos nudillos en la puerta."
    scene c14s003_005 with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    sai "Soy yo, [sai]. ¿Estás ahí? ¿Puedo pasar?"
    mc "Pasa, [sai]."
    play music ("music/RayOfHope.ogg")
    call BlinkXP ("c14s003_010" , "d") from _call_BlinkXP_640
    sai "Hola, no sé si molesto..."
    if sai._var("route"):
        mc "Lo que me molestaría sería que no me dieras un beso..."
        call KissXP ("c14s003_015" , "d") from _call_KissXP_16
        if sca._var("route") or eil._var("route"):
            sai "No sabía si podía... eso de que salgas con más chicas... me desconcierta..."
        else:
            sai "No sabia si podía..."
        mc "Siempre podrás besarme, al menos cuando estemos solos."
        call BlinkXP ("c14s003_020" , "d") from _call_BlinkXP_641
        sai "¿No puedo hacerlo delante de tu familia? ¿Te avergüenzas de mí?"
        if mc._var("relationships") > 1:
            mc "[sai], no me avergüenzo de ti, pero es complicado ahora mismo. Tienes que saber que desde que volví a casa he empezado con alguien."
            mc "Pasa, sientate. Vamos a tener que hablar..."
            call BlinkXP ("c14s003_025" , "f") from _call_BlinkXP_642
            if sca._var("route"):
                sai "Lo sé, con la tal [sca]... parece una buena chica..."
                if eil._var("route"):
                    sai "Y, obviamente, has vuelto con [eil]... de alguna forma me lo esperaba..."
            elif eil._var("route"):
                sai "Lo sé. Obviamente, has vuelto con [eil]... de alguna forma me lo esperaba..."
            if (mc._var("relationships")==2 and sca._var("route") and not eil._var("route")) or (mc._var("relationships")==2 and eil._var("route") and not sca._var("route")):
                mc "Sí, salgo con ella y contigo. No hay nadie más, pero prácticamente nadie sabe lo mío con ella. Déjame acalararlo y todo será más... normal."
            elif mc._var("relationships")==3 and sca._var("route") and eil._var("route"):
                mc "Sí, salgo con ellas y contigo. No hay nadie más, pero prácticamente nadie sabe lo mío con ellas. Déjame acalararlo y todo será más... normal."
            elif mc._var("relationships")>3:
                mc "Pero prácticamente nadie lo sabe. Déjame acalararlo y todo será más... normal."
                mc "También debes saber que salgo con alguien más. Y no me preguntes con quién, por favor."
        else:
            mc "[sai], no me avergüenzo de ti, pero es complicado ahora mismo."
            mc "Pasa, sientate. Vamos a tener que hablar..."
        call BlinkXP ("c14s003_030" , "d") from _call_BlinkXP_643
        sai "Entonces... ¿A qué a venido el beso en el aeropuerto? No lo entiendo..."
        mc "[sai], mi vida se ha complicado desde que volví a Newport. No pensaba que volvería a verte..."
        call BlinkXP ("c14s003_035" , "h") from _call_BlinkXP_644
        sai "¡Te dije que vendría a visitarte!"
        mc "Sí, pero no a vivir en casa."
        mc "Y a lo que me refería era que no sabía si volvería a verte a corto plazo. Deseaba volver a verte, que cuando acabaras el año que te queda me llamases..."
        mc "Pero no sabía si sucedería. No me dijiste que pensabas mudarte aquí."
        call BlinkXP ("c14s003_040" , "d") from _call_BlinkXP_645
        sai "Lo sé. Y sé que debería haberlo hecho."
        mc "Sí, deberías."
        call BlinkXP ("c14s003_045" , "d") from _call_BlinkXP_646
        sai "Entonces... ¿Quieres que dejemos lo nuestro?"
        sai "Sólo he venido para el curso de verano. El transfer de Portland a Newport todavía está en proceso..."
        sai "Si no quieres estar conmigo... lo paralizaría y volvería a Portland a acabar la carrera."
        mc "[sai], en ningún momento he dicho que no quiera estar contigo..."
        call BlinkXP ("c14s003_050" , "d") from _call_BlinkXP_647
        sai "¿Entonces...? No entiendo nada..."
        if mc._var("relationships") > 1:
            mc "Pero no puedo estar contigo como estábamos en Portland. O para ser más exactos, sí, precisamente como estábamos en Portland."
            mc "Allí teníamos una relación abierta. Ninguno de los dos hizo nada fuera de la relación, pero los dos aceptamos que el otro pudiera hacerlo."
            mc "¿Serías capaz de volver a aceptar una relación así?"
        else:
            mc "Pero no quiero estar contigo como estábamos en Portland."
            mc "Allí teníamos una relación abierta. Ninguno de los dos hizo nada fuera de la relación, pero los dos aceptamos que el otro pudiera hacerlo."
            mc "¿Serías capaz de volver a aceptar una relación así? Yo no."
        call BlinkXP ("c14s003_055" , "d") from _call_BlinkXP_648
        sai "Sabes por qué teniamos esa relación, ¿verdad?"
        mc "Me gustaría escuchárlo de tus labios. En Portland diste unas razones, en la videoconferencia parecían otras."
        call BlinkXP ("c14s003_060" , "d") from _call_BlinkXP_649
        sai "No me quería enamorar de ti."
        mc "Eso es una tontería, [sai]..."
        sai "No lo es. Si teníamos una relación así, no podía darte por seguro nunca. Si un día no venías a mi casa, podía pensar que estabas con otra..."
        mc "Nunca estuve con nadie más..."
        sai "Lo sé. Si lo hubieras hecho me lo hubieras dicho."
        call BlinkXP ("c14s003_065" , "d") from _call_BlinkXP_650
        sai "Pero no funcionó."
        sai "Me enamoré hasta las trancas."
        sai "Y sólo me di cuenta cuando me dijiste que volvías aquí. Me di cuenta de que te perdía..."
        mc "Y por alguna razón no quisiste formalizar la relación entonces."
        call BlinkXP ("c14s003_070" , "d") from _call_BlinkXP_651
        sai "¡Porque hubiera sido injusto para ti, cabeza de chorlito!"
        mc "¿Para mí? ¿Por qué?"
        call BlinkXP ("c14s003_075" , "d") from _call_BlinkXP_652
        sai "En ese momento no pensaba en transferirme. Solo pensaba en que te podía perder para siempre."
        sai "No quería tenerte esperando un año a que acabara la carrera."
        sai "No sabía que había un curso de verano aquí que me podía ir bien. Que podríamos pasar el verano juntos."
        mc "Y decidiste apuntarte sin decirme nada."
        call BlinkXP ("c14s003_080" , "d") from _call_BlinkXP_653
        sai "Tenía que volver a India. Tenía que convencer a mis padres de que me dejasen cambiar de Universidad..."
        sai "Cuando llegué a Goa... todo fue más fácil de lo que esperaba. Kalyani, mi prima, también empieza la Universidad este año, fue una aliada increíble."
        sai "Y creí que al menos mirarías los expedientes de las chicas que iban a vivir contigo... y que me llamarías."
        mc "Sé que no es excusa, pero he estado muy ocupado, y de eso se ocupan [nor] y [mar]."
        call BlinkXP ("c14s003_085" , "d") from _call_BlinkXP_654
        sai "Por eso te llamé desde Barcelona. No sabía si te habías enfadado o si no te habías enterado."
        mc "Y te dejaste la videoconferencia abierta..."
        call BlinkXP ("c14s003_090" , "d") from _call_BlinkXP_655
        sai "Y dije cosas que no debería haber dicho... sobre [eil]..."
        if mc._var("relationships") > 1:
            mc "Lo sé. Por eso te pregunto ¿Serías capaz de volver a aceptar una relación abierta? Esta vez yo sí que estoy con alguien más..."
        else:
            mc "Lo sé. Por eso te pregunto ¿Realmente quieres una relación abierta?"
        call BlinkXP ("c14s003_095" , "d") from _call_BlinkXP_656
        sai "No lo sé."
        sai "Cuando me has besado en el aeropuerto todo ha parecido que volvía a estar... no sé... donde debería..."
        if mc._var("relationships") > 1:
            sai "Cuando me he enterado que no vas a estar solo conmigo... todo se ha roto... no sé como explicarlo..."
            mc "Es la misma relación que tú quisiste tener en Portland."
        else:
            sai "Por supuesto que te quiero para mí sola, pero llevo un mes pensando en si estarías con [eil] o no..."
            mc "No lo estoy. Ni con nadie."
        call BlinkXP ("c14s003_100" , "d") from _call_BlinkXP_657
        sai "Lo sé. Pero allí sabía... creía... que no ibas a estar con nadie. No eres de los que se acuestan con la primera que pasa si no sientes nada por ella..."
        if mc._var("relationships") > 1:
            mc "[sai], si estoy con alguien más, es porque estoy tan enamorado de ella como lo estoy de ti."
        else:
            mc "[sai], si estuviera con alguien más, sería porque estaría tan enamorado de ella como lo estoy de ti."
            mc "Pero no lo estoy. Eso es lo importante."
        call BlinkXP ("c14s003_105" , "h") from _call_BlinkXP_658
        sai "{b}¿Qué?{/b} ¿Sigues enamorado de mí?"
        mc "Si crees que estar separados algo más de un mes va a hacer que cambien mis sentimientos... creía que me conocías más..."
        call BlinkXP ("c14s003_110" , "d") from _call_BlinkXP_659
        sai "¿Puedo besarte ahora? ¿Abrazarte?"
        mc "No necesitas pedir permiso aquí..."
        call KissXP ("c14s003_115" , "d") from _call_KissXP_17
        "Repetís el beso del aeropuerto. Esta vez con mucha más seguridad. Hablar las cosas casi siempre las resuelve..."
    else:
        mc "No, pasa. ¿Te puedo ayudar en algo?..."
        call BlinkXP ("c14s003_020" , "d") from _call_BlinkXP_660
        sai "¿Que si me puedes ayudar en algo? Ayúdame a entender qué ha pasado en el aeropuerto"
        mc "[sai], no ha pasado nada. Tienes que saber que desde que volví a casa he empezado con alguien."
        mc "Pasa, sientate. Vamos a tener que hablar..."
        if mc._var("relationships") > 0:
            call BlinkXP ("c14s003_025" , "d") from _call_BlinkXP_661
            if sca._var("route"):
                sai "Lo sé, con la tal [sca]... parece una buena chica..."
                if eil._var("route"):
                    sai "Y, obviamente, has vuelto con [eil]... de alguna forma me lo esperaba..."
            elif eil._var("route"):
                sai "Lo sé. Obviamente, has vuelto con [eil]... de alguna forma me lo esperaba..."
            if (mc._var("relationships")==1 and sca._var("route") and not eil._var("route")) or (mc._var("relationships")==2 and eil._var("route") and not sca._var("route")):
                mc "Sí, salgo con ella, pero prácticamente nadie sabe lo mío con ella. Déjame acalararlo y todo será más... normal."
            elif mc._var("relationships")==2 and sca._var("route") and eil._var("route"):
                mc "Sí, salgo con las dos, pero prácticamente nadie sabe lo mío con ellas. Déjame acalararlo y todo será más... normal."
            elif mc._var("relationships")>2:
                mc "Pero prácticamente nadie lo sabe. Déjame acalararlo y todo será más... normal."
                mc "También debes saber que salgo con alguien más. Y no me preguntes con quién, por favor."
        call BlinkXP ("c14s003_030" , "d") from _call_BlinkXP_662
        sai "Entonces... ¿A qué a venido el beso en el aeropuerto? No lo entiendo... ¿un beso en la mejilla?"
        mc "[sai], mi vida se ha complicado desde que volví a Newport. No pensaba que volvería a verte..."
        call BlinkXP ("c14s003_035" , "h") from _call_BlinkXP_663
        sai "¡Te dije que vendría a visitarte!"
        mc "Sí, pero no a vivir en casa."
        mc "Y a lo que me refería era que no sabía si volvería a verte a corto plazo. Deseaba volver a verte, que cuando acabaras el año que te queda me llamases..."
        mc "Pero no sabía si sucedería. No me dijiste que pensabas mudarte aquí."
        call BlinkXP ("c14s003_040" , "d") from _call_BlinkXP_664
        sai "Lo sé. Y sé que debería haberlo hecho."
        mc "Sí, deberías."
        call BlinkXP ("c14s003_045" , "d") from _call_BlinkXP_665
        sai "Entonces... ¿Quieres que dejemos lo nuestro?"
        sai "Sólo he venido para el curso de verano. El transfer de Portland a Newport todavía está en proceso..."
        sai "Si no quieres estar conmigo... lo paralizaría y volvería a Portland a acabar la carrera."
        mc "[sai], en ningún momento he dicho que no quiera estar contigo... pero necesito tiempo."
        call BlinkXP ("c14s003_050" , "d") from _call_BlinkXP_666
        sai "¿Entonces...?"
        if mc._var("relationships") > 0:
            mc "Pero no puedo estar contigo como estábamos en Portland. O para ser más exactos, sí, precisamente como estábamos en Portland."
            mc "Allí teníamos una relación abierta. Ninguno de los dos hizo nada fuera de la relación, pero los dos aceptamos que el otro pudiera hacerlo."
            mc "¿Serías capaz de volver a aceptar una relación así?"
        else:
            mc "Pero no quiero estar contigo como estábamos en Portland."
            mc "Allí teníamos una relación abierta. Ninguno de los dos hizo nada fuera de la relación, pero los dos aceptamos que el otro pudiera hacerlo."
            mc "¿Serías capaz de volver a aceptar una relación así? Yo no."
        call BlinkXP ("c14s003_055" , "d") from _call_BlinkXP_667
        sai "Sabes por qué teniamos esa relación, ¿verdad?"
        mc "Me gustaría escuchárlo de tus labios. En Portland diste unas razones, en la videoconferencia parecían otras."
        call BlinkXP ("c14s003_060" , "d") from _call_BlinkXP_668
        sai "No me quería enamorar de ti."
        mc "Eso es una tontería, [sai]..."
        sai "No lo es. Si teníamos una relación así, no podía darte por seguro nunca. Si un día no venías a mi casa, podía pensar que estabas con otra..."
        mc "Nunca estuve con nadie más..."
        sai "Lo sé. Si lo hubieras hecho me lo hubieras dicho."
        call BlinkXP ("c14s003_065" , "d") from _call_BlinkXP_669
        sai "Pero no funcionó."
        sai "Me enamoré hasta las trancas."
        sai "Y sólo me di cuenta cuando me dijiste que volvías aquí. Me di cuenta de que te perdía..."
        mc "Y por alguna razón no quisiste formalizar la relación entonces."
        call BlinkXP ("c14s003_070" , "d") from _call_BlinkXP_670
        sai "¡Porque hubiera sido injusto para ti, cabeza de chorlito!"
        mc "¿Para mí? ¿Por qué?"
        call BlinkXP ("c14s003_075" , "d") from _call_BlinkXP_671
        sai "En ese momento no pensaba en transferirme. Solo pensaba en que te podía perder para siempre."
        sai "No quería tenerte esperando un año a que acabara la carrera."
        sai "No sabía que había un curso de verano aquí que me podía ir bien. Que podríamos pasar el verano juntos."
        mc "Y decidiste apuntarte sin decirme nada."
        call BlinkXP ("c14s003_080" , "d") from _call_BlinkXP_672
        sai "Tenía que volver a India. Tenía que convencer a mis padres de que me dejasen cambiar de Universidad..."
        sai "Cuando llegué a Goa... todo fue más fácil de lo que esperaba. Kalyani, mi prima, también empieza la Universidad este año, fue una aliada increíble."
        sai "Y creí que al menos mirarías los expedientes de las chicas que iban a vivir contigo... y que me llamarías."
        mc "Sé que no es excusa, pero he estado muy ocupado, y de eso se ocupan [nor] y [mar]."
        call BlinkXP ("c14s003_085" , "d") from _call_BlinkXP_673
        sai "Por eso te llamé desde Barcelona. No sabía si te habías enfadado o si no te habías enterado."
        mc "Y te dejaste la videoconferencia abierta..."
        call BlinkXP ("c14s003_090" , "d") from _call_BlinkXP_674
        sai "Y dije cosas que no debería haber dicho... sobre [eil]..."
        if mc._var("relationships") > 0:
            mc "Lo sé. Por eso te pregunto ¿Serías capaz de volver a aceptar una relación abierta? Esta vez yo sí que estoy con alguien más..."
        else:
            mc "Lo sé. Por eso te pregunto ¿Realmente quieres una relación abierta?"
        call BlinkXP ("c14s003_095" , "d") from _call_BlinkXP_675
        sai "No lo sé."
        sai "Cuando me has besado en la mejilla en el aeropuerto todo ha parecido que... no sé... que se derrumbaba..."
        if mc._var("relationships") > 0:
            sai "Cuando me he enterado que estás con alguien... todo se ha roto... no sé como explicarlo..."
            mc "Si volvieramos a estar juntos, sería la misma relación que tú quisiste tener en Portland."
        else:
            sai "Por supuesto que te quiero para mí sola, pero llevo un mes pensando en si estarías con [eil] o no..."
            mc "No lo estoy. Ni con nadie."
        call BlinkXP ("c14s003_100" , "d") from _call_BlinkXP_676
        sai "Lo sé. Pero en Portland sabía... creía... que no ibas a estar con nadie. No eres de los que se acuestan con la primera que pasa si no sientes nada por ella..."
        if mc._var("relationships") > 0:
            mc "[sai], si estoy con alguien más, es porque estoy tan enamorado de ella como lo estaba de ti."
        else:
            mc "[sai], si estuviera con alguien más, sería porque estaría tan enamorado de ella como lo estaba de ti."
            mc "Pero no lo estoy. Eso es lo importante."
        call BlinkXP ("c14s003_105" , "h") from _call_BlinkXP_677
        sai "{b}¿Qué?{/b} ¿Estabas?"
        mc "Mi vida se ha complicado mucho... tengo muchos frentes abiertos ahora mismo, y no solo a nivel amoroso."
        mc "Verte, pese a que lo esperaba después de la video conferencia, no ha dejado de ser una sorpresa."
        call BlinkXP ("c14s003_110" , "d") from _call_BlinkXP_678
        sai "¿Puedo al menos abrazarte ahora?"
        mc "No necesitas pedir permiso para eso..."
    call BlinkXP ("c14s003_120" , "d") from _call_BlinkXP_679
    sai "Te he echado de menos..."
    mc "Y yo a ti..."
    mc "Pero tenemos que hablar de muchas cosas, analizar cómo nos sentimos. ¿Te importa si nos tomamos un tiempo antes de tomar alguna decisión?"
    call BlinkXP ("c14s003_125" , "d") from _call_BlinkXP_680
    sai "Creo que será lo mejor. Hoy ha sido una montaña rusa de emociones. No me esperaba del todo esta recepción..."
    sai "Realmente no sé lo que me esperaba..."
    mc "¿Te han dicho lo de mañana en la playa? Podemos volver a hablar si quieres..."
    call BlinkXP ("c14s003_130" , "d") from _call_BlinkXP_681
    sai "Sí, me lo han dicho. Pero de hoy a mañana no creo que cambie mucho. Hay muchas cosas que tenemos que hablar y..."
    scene c14s003_005 with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    emm "Soy yo."
    mc "Pasa, [emm]."
    if emm._var("route"):
        scene c14s003_135AnBlink with dissolve #sorpresa-enfado
        emm "¡Oops! No sabía que {b}ésta{/b} estaba aquí..."
    else:
        scene c14s003_140AnBlink with dissolve #sorpresa-sonrisa
        emm "¡Oops! No sabía que estabas acompañado..."
    mc "¿Querías algo?"
    emm "Sí, la cena está casi lista. Mamá me ha dicho que te avise."
    call BlinkXP ("c14s003_145" , "d") from _call_BlinkXP_682
    mc "Ya seguiremos hablando mañana, [sai]."
    sai "Genial. ¿Hablamos en la playa?"
    mc "Perfecto."
    stop music fadeout (1.5)
    if emm._var("route"):
        call BlinkXP ("c14s003_150" , "h") from _call_BlinkXP_683
        emm "*Gruñido*"
    scene black with dissolve
    "Pasáis una agradable noche en familia, una familia a la que se ha añadido [sca]. Kiara y [eil] se unen a vosotros en la cena. A este paso tendréis que comprar una mesa más grande."
    "[eil] está en su salsa, hablando con toda la familia, a la que conoce desde hace años y poniéndose al día con todo el mundo."
    "[sca], [mar], y [nor] intentan integrar a Kiara en la conversación. Se la ve un poco desubicada. No está acostumbrada a una familia así, ni a cenas llenas de risas."
    "No se habla de ninguno de los temas escabrosos del día. Es el momento de dejarlos atrás."
    return
label c14s004_ToTheBeach:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_17
        call mrS3_nor_route from _call_mrS3_nor_route_17
        if nor._var("route"):
            menu:
                "¿Crees que [nor] está embarazada?"
                "Sí":
                    $ nor._var("pregnant" , True)
                "No":
                    $ nor._var("pregnant" , False)
        else:
            $ nor._var("pregnant" , False)
            call mrS3_eri_route from _call_mrS3_eri_route_18
    centered "{size=+20}{b}DÍA 16 – MIÉRCOLES{/b}{/size}"
    play music ("music/Vacation-Vibe.ogg")
    "El día siguiente es un torbellino de actividad."
    scene c14s004_005a with dissolve
    "Acabar de preparar la comida... aunque unas colaboran más que otras..."
    "Kate y Betty se dedican a aligerar la carga. Después dirán que así había menos cosas que bajar a los coches."
    scene c14s004_005c with fade
    "Coger todos los artilugios de playa... Habiendo una piscina, ¿quién quiere ir a la playa? Lleváis años sin pisar la playa, al menos en familia."
    "Casi todo el mundo tiene buena parte del día libre hoy, con lo que es el día perfecto."
    "Subirlo todo a los coches... Todo el mundo colabora con lo que puede."
    "Si ayer parecíais una familia subiendo las cosas de [sca] a su habitación, hoy lo sois."
    scene c14s004_005d with fade
    "Incluso Lisa y [sai] colaboran antes de ir a la universidad. Esperan llegar para comer a la playa y unirse a la celebración navideña."
    "Kim y Debbie tienen clase por la tarde. Kate se va a saltar sus clases, demasiado cercanas a la hora de comer, y prefiere pasar el día con la familia. La Familia."
    scene c14s004_005e with fade
    "Llevas a Lisa y [sai] a la universidad antes de ir a volver a casa a recoger un nuevo cargamento de chicas. 16 personas viviendo en casa y solo tres coches..."
    scene c14s004_005f with fade
    "Por fin llegáis a la playa. [sam] y [sim] se unirán más tarde. Jamaal no va a poder venir. Algo sobre una indigestión por comer demasiadas empanadas."
    scene black with dissolve
    stop music fadeout (1.5)
    "Vas al chiringuito a mear antes de descargar las cosas."
    play music ("music/Beach.ogg")
    scene c14s004_010d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_010" , "d") from _call_BlinkXP_684
    mc "¿Os ayudo a algo con la comida?"
    mom "No hace falta. Estos son los últimos túpers y comeremos en el merendero. Las mujeres vamos a quedarnos poniéndonos morenas mientras las chicas juegan en el agua."
    mc "Déjame al menos llevarlos hasta las sombrillas."
    call BlinkXP ("c14s004_015" , "d") from _call_BlinkXP_685
    mom "Supongo que no te apetece tumbarte con nosotras a tomar el sol..."
    mc "Yo me quedaría, pero sabes que me aburro muchísimo estando tirado en la toalla estilo lagarto sin hacer nada."
    call BlinkXP ("c14s004_020" , "d") from _call_BlinkXP_686
    mom "Lo sé, cariño. ¿Por qué no ayudas a Betty con las sillas?"
    mc "¡Dejo los túpers en las toallas y voy! Te quiero."
    scene c14s004_025d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_025" , "d") from _call_BlinkXP_687
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ bet.profileImages.pop (2) # first remove
        $ bet.profileImages.insert (2, ("betty_2", None)) # then add new
    mc "Tía Betty, vengo a ayudarte con las sillas."
    bet "No hace falta, cielo. Ya casi las he llevado todas con la ayuda de las chicas."
    mc "Por cierto, ¿ese es el modelo de bikini oficial del Vaticano? Lo veo... demasiado sexy, ¿no?"
    call BlinkXP ("c14s004_030" , "d") from _call_BlinkXP_688
    bet "*Risa* ¿Sexy yo? Hay que llevarte a que te revisen la vista."
    bet "Es un antiguo bañador de [nor], de cuando se estaba adelgazando. Es en el único bañador que cabía yo."
    mc "Tenemos que renovarte el vestuario. No puedes ir con el hábito a todas partes"
    call BlinkXP ("c14s004_035" , "d") from _call_BlinkXP_689
    bet "Tienes razón... debería comprarme más ropa... el hábito..."
    bet "El hábito no lo puedo usar para todo..."
    mc "Betty, ¿ha pasado algo?"
    call BlinkXP ("c14s004_040" , "d") from _call_BlinkXP_690
    bet "No, nada... ¿puedes ir a ayudar a Olivia con la sombrilla? Ya me ocupo yo de llevar el resto de las sillas."
    mc "¡Voy! Te quiero."
    scene c14s004_045d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    $ renpy.notify ("Profile image unlocked")
    $ mee.addProfileImage ("olivia_2")
    call BlinkXP ("c14s004_045" , "d") from _call_BlinkXP_691
    mee "¿Quieres algo, cariño?"
    mc "Tía Betty me ha enviado a que te ayude con la sombrilla."
    call BlinkXP ("c14s004_050" , "d") from _call_BlinkXP_692
    mee "Gracias, cielo, pero la acabo de derrotar una vez ha parado el viento."
    mc "Casi parecías una stripper cogida a esa barra. *Risa*"
    call BlinkXP ("c14s004_050b" , "d") from _call_BlinkXP_693
    mee "¡[mc]!"
    mc "Perdona, me estoy empezando a sentir un poco inútil y eso me frustra. Parece que no me necesitáis para nada."
    call BlinkXP ("c14s004_055" , "d") from _call_BlinkXP_694
    mee "Cariño, estás rodeado de mujeres que no te han visto en años. No voy a decir que no te necesitemos, siempre te necesitaremos, pero sabemos apañarnos solas."
    mc "No es que me ayudes mucho. *Risa*"
    call BlinkXP ("c14s004_060" , "d") from _call_BlinkXP_695
    mee "Ven que te de un abrazo. Esto seguro que ayuda."
    mc "Por supuesto que sí, Meemaw."
    call BlinkXP ("c14s004_065" , "d") from _call_BlinkXP_696
    mee "Deberías ir a ayudar a [nor]. Está trayendo las neveras."
    mc "¿Las? ¿En plural? ¡Voy! Te quiero."
    scene c14s004_070d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_070" , "d") from _call_BlinkXP_697
    mc "¿Qué haces llevando eso?"
    nor "Solo son un par de neveras, cielo."
    if nor._var("pregnant"):
        mc "En tu estado no deberías llevar ni una. Ya las llevo yo."
        call BlinkXP ("c14s004_075" , "d") from _call_BlinkXP_698
        nor "Aún no sabemos nada. Todavía faltan días para que sea fiable, y no me voy a quedar parada por si acaso..."
        mc "¿Prefieres arriesgarte? Ahora me vas a decir que también vas a beber vino en la comida..."
        call BlinkXP ("c14s004_080" , "d") from _call_BlinkXP_699
        nor "No pensaba hacerlo. Ya viste en la cena de anoche que sólo bebí agua. Pese a las miradas raras de [mar]."
        mc "Lo ví..."
        call BlinkXP ("c14s004_085" , "d") from _call_BlinkXP_700
        nor "Aunque para hoy le pedí a [mar] que comprara cava sin alcohol, con la excusa de que era para que las chicas también puedan brindar."
    else:
        mc "¿Sólo? ¿Te parecen pocas? ¿Qué llevas ahí? Ya las llevo yo."
        call BlinkXP ("c14s004_075" , "d") from _call_BlinkXP_701
        nor "¡No soy una floja! Solo son las bebidas. Las neveras con la comida se las han llevado las chicas."
        mc "Y ¿necesitamos dos neveras para la bebida?"
        call BlinkXP ("c14s004_085" , "d") from _call_BlinkXP_702
        nor "Todo el mundo bebe cosas diferentes. Esta vez incluso tenemos cava sin alcohol para que las chicas también puedan brindar."
    mc "[nor], las chicas ya tienen 18, pueden beber alcohol si quieren. Y lo hacen..."
    call BlinkXP ("c14s004_090" , "d") from _call_BlinkXP_703
    nor "Lo sé, pero hoy no van a controlar cuanto beben, entre la comida y los brindis... Es Navidad. *Risa*"
    mc "Me parece una buena excusa para tener cava sin alcohol. Bien pensado."
    call BlinkXP ("c14s004_095" , "d") from _call_BlinkXP_704
    nor "Puedes dejar las neveras bajo la sombrilla. Yo iré a por la crema al coche."
    mc "¿Algo más en lo que pueda ayudar?"
    call BlinkXP ("c14s004_100" , "d") from _call_BlinkXP_705
    nor "No, creo que ya está todo... a menos que quieras ponernos crema solar a todas las que nos quedamos en las toallas."
    if nor._var("route") or eri._var("route"):
        call BlinkXP ("c14s004_105" , "d") from _call_BlinkXP_706
        nor "Aunque ya sabemos como acaba eso cuando tú estás cerca..."
        mc "Mejor voy a pasar, por lo que pueda ser."
    else:
        mc "Si queréis, por mí ningún problema."
        call BlinkXP ("c14s004_105" , "d") from _call_BlinkXP_707
        nor "Lo estaba diciendo en broma, cielo. Estando cinco mujeres aquí, sería raro que nos pusieras la crema tú, ¿no?"
    nor "Puedes ir con las chicas. Iban a jugar a algo en el agua."
    mc "¡Voy! Te quiero."
    scene c14s004_110d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ kia.profileImages.pop (2) # first remove
        $ kia.profileImages.insert (2, ("kiara_2", None)) # then add new
    call BlinkXP ("c14s004_110" , "d") from _call_BlinkXP_708
    mc "¡Oh, Kiara! No te había visto desde que hemos llegado. Te sienta bien ese bañador."
    kia "Gracias, [mc]. Estaba ayudando a Betty con las sillas. Te he visto irte en dirección a Olivia."
    mc "Ahora me siento más inutil todavía. Me ha dicho que no necesitaba mi ayuda..."
    call BlinkXP ("c14s004_115" , "d") from _call_BlinkXP_709
    kia "La mía tampoco, pero como me tratan entre algodones, no ha podido negarse a que la ayudara. *Risa*"
    mc "¿Cómo está el brazo?"
    call BlinkXP ("c14s004_120" , "d") from _call_BlinkXP_710
    kia "Duele menos, pero aún duele un poco. El ungüento que me dió [sam] es fantástico."
    mc "Eso está genial."
    mc "¿Estáis a gusto en casa de [nor]? Si no, podéis volver a mi cama."
    call BlinkXP ("c14s004_125" , "d") from _call_BlinkXP_711
    kia "No te preocupes, la casa es fantástica y [nor] nos está tratando increíblemente bien."
    kia "De lo que tengo ganas es de que llegue mañana para poder ir a casa a por más ropa. El bikini me lo ha dejado [emm], era la talla más parecida a la mía, aunque sea mucho más alta."
    mc "No tengas prisa. Hoy vuelve Alexia a Newport. A ver si puede acompañarnos mañana. De uniforme a ser posible."
    call BlinkXP ("c14s004_130" , "d") from _call_BlinkXP_712
    kia "No creo que sea necesario. Solomon no estará."
    mc "De todas formas se lo pediré. Yo si que os acompañaré, deberéis cargar las cosas en la camioneta."
    call BlinkXP ("c14s004_135" , "d") from _call_BlinkXP_713
    kia "¿Te importa si lo hablamos mañana? Prefiero no pensar en eso hasta que llegue el momento... Volver a mi propia casa como si fuera una ladrona..."
    mc "No te preocupes. Lo hablamos mañana. Ven aquí."
    call BlinkXP ("c14s004_140" , "d") from _call_BlinkXP_714
    kia "Gracias, [mc]. Por todo. Por acogernos en tu familia y por ayudarnos."
    mc "No le des más vueltas. Es Navidad. *Risa*"
    call BlinkXP ("c14s004_145" , "d") from _call_BlinkXP_715
    kia "Bueno, voy a sentarme bajo la sombrilla. Pelirroja y blanca de piel es receta para quemarme."
    mc "Perfecto, nos vemos luego."
    scene c14s004_150d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_150" , "d") from _call_BlinkXP_716
    mc "Hey, [dap]. ¿Donde vas con esa pelota?"
    dap "Kate nos ha convencido a para jugar al juego aquel que explicó en la piscina el otro día. El parecido a Verdad o Reto con la pelota"
    mc "Recuerda cómo acabó la última vez que jugamos... no demasiado bien."
    call BlinkXP ("c14s004_155" , "d") from _call_BlinkXP_717
    dap "Lo sé, pero ahora es un poco diferente. Nos va a servir para conocernos más. [sca] casi no ha tratado con Kim, Debbie, y Kate, y ahora viviendo en casa..."
    mc "Como queráis, pero quizás hoy no sería el mejor día para crear malos rollos. Es Navidad."
    call BlinkXP ("c14s004_160" , "d") from _call_BlinkXP_718
    dap "No te preocupes. Los malos rollos en los juegos siempre los crea [emm] cuando se pica, y se ha ido a dar un paseo por la playa con [eri] y [eil]."
    mc "Entonces... Kate, Kim, Debbie, [sca], tú, y yo, ¿no?"
    call BlinkXP ("c14s004_165" , "d") from _call_BlinkXP_719
    dap "¿Tú también te apuntas? ¿No crees que les vas a cortar el rollo a las chicas?"
    mc "O les corto el rollo o evito que os desmadréis todas. Tenéis mucho peligro."
    call BlinkXP ("c14s004_170" , "d") from _call_BlinkXP_720
    dap "¡Nuestro salvador ha llegado! *Risa*"
    mc "Siempre dispuesto a ayudar. *Risa*"
    if dap._var("route"):
        call BlinkXP ("c14s004_175" , "d") from _call_BlinkXP_721
        dap "Hablando de ayudar... ¿Pudiste reservar mesa en el sitio que te mandé para esta noche?"
        mc "Sí. Les llamé por teléfono. El tío que me atendió hablaba raro, pero al final hice la reserva."
        mc "Por un momento parecía que había un error, había otra reserva a nombre de otros Marks, pero al final el error fue del tío raro."
        call BlinkXP ("c14s004_180" , "d") from _call_BlinkXP_722
        dap "¿Hablaba raro? ¿A qué te refieres?"
        mc "Tenía un acento que no localicé. Europeo seguro, pero no sé de donde."
        dap "No entraste en la web del restaurante, ¿verdad?"
        mc "No, ¿tenía que haberlo hecho? Sólo les llamé por teléfono."
        call BlinkXP ("c14s004_185" , "d") from _call_BlinkXP_723
        dap "Ahora que lo pienso, no, mejor que no lo hayas hecho. Así será una sorpresa."
        mc "Ahora me has picado la curiosidad."
        call BlinkXP ("c14s004_190" , "d") from _call_BlinkXP_724
        dap "Prométeme que no lo vas a mirar."
        mc "*Risa* Prometido. Si es tan importante para ti, deseo concedido."
        call BlinkXP ("c14s004_195" , "d") from _call_BlinkXP_725
        dap "No solo es un caballero sino que también es un genio que concede deseos."
    call BlinkXP ("c14s004_200" , "d") from _call_BlinkXP_726
    dap "¿Vamos?"
    mc "Después de ti."
    scene c14s004_205d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    $ renpy.notify ("Profile image unlocked")
    $ kat.addProfileImage ("notAvailable")
    $ kat.addProfileImage ("kate_2")
    call BlinkXP ("c14s004_205" , "d") from _call_BlinkXP_727
    kat "¿Te unes al juego, [mc]?"
    mc "Si no os molesta..."
    scene c14s004_210d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_210" , "d") from _call_BlinkXP_728
    deb "No nos puede molestar. Si estás tú a lo mejor se cortan un poco con las preguntas."
    mc "Se lo estaba comentando a [dap]. Estos juegos pueden crear malos rollos si la cosa se desmadra."
    scene c14s004_215d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_215" , "d") from _call_BlinkXP_729
    kim "Somos todos adultos, no nos vamos a enfadar por un juego. Puede ser divertido."
    mc "La última vez que jugamos a Verdad o Reto hubo enfados. No me fío demasiado. *Risa*"
    scene c14s004_220d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s004_220" , "d") from _call_BlinkXP_730
    sca "Pero hoy solo está [dap]. [dap] sin [emm] cerca es como un gatito. *Risa*"
    mc "¿Dulce y achuchable?"
    call BlinkXP ("c14s004_225" , "d") from _call_BlinkXP_731
    sca "Eso también, *Gruñido* pero me refería a que mantenía las uñas guardadas. *Risa*"
    todas "*Risa*"
    call BlinkXP ("c14s004_230" , "d") from _call_BlinkXP_732
    kat "¿Quieres saber las reglas del juego? Hablando con [sca] hemos mezclado las suyas y las mías."
    menu:
        "Cuéntamelas, por favor.":
            kat "Jugamos en el agua y nos ponemos en círculo. Quien falle en recoger la pelota escoge Verdad o Reto que es propuesto por quien se la lanzó."
            kat "La pregunta o el reto van girando en el sentido de las agujas del reloj hasta llegar a quien lo propuso."
            mc "¿Nos podemos negar a responder de alguna forma?"
            call BlinkXP ("c14s004_235" , "d") from _call_BlinkXP_733
            kat "Normalmente sí, pagando prenda. Pero tú solo podrías negarte una vez. *Risa*"
            kat "Y es posible que después de eso las chicas perdieran interés en el juego. *Risa*"
            mc "OK, entonces vamos obligados a lo que elija la persona de nuestra derecha, o tres personas más allá."
            call BlinkXP ("c14s004_240" , "d") from _call_BlinkXP_734
            sca "Exacto. Como hicimos jugando a la botella hace unos días."
            mc "Vale, parece divertido."
        "Mejor me sorprendéis.":
            call BlinkXP ("c14s004_235" , "d") from _call_BlinkXP_735
            kat "Despues no te llames a engaño cuando te caigan retos chungos. *Risa*"
            mc "Me arriesgaré. *Risa*"
    stop music fadeout (1.5)
    return
label c14s005_BallGame:
    if _in_replay:
        $ AuxReplay = 0
        $ mc._var("relationships" , 0 , "set")
        $ kat._var("relationshipPoints", 0, intention = "set")
        $ lis._var("relationshipPoints", 0, intention = "set")
        call mrS3_edmund_story from _call_mrS3_edmund_story_6
        call mrS3_dap_route from _call_mrS3_dap_route_18
        call mrS3_sca_route from _call_mrS3_sca_route_15
        if mc._var("relationships") < 2:
            call mrS3_rels from _call_mrS3_rels_35
        menu:
            "¿Cuántos Puntos de Relación tienes con Kim?"
            "Menos de -20":
                $ kim._var("relationshipPoints", -21, intention = "set")
            "Menos de -15":
                $ kim._var("relationshipPoints", -16, intention = "set")
            "Entre -15 y 0":
                $ kim._var("relationshipPoints", 0, intention = "set")
            "Más de 0":
                $ kim._var("relationshipPoints", 1, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Debbie?"
            "Menos de -5":
                $ deb._var("relationshipPoints", -6, intention = "set")
            "Entre -5 y -1":
                $ deb._var("relationshipPoints", -1, intention = "set")
            "Entre 0 y 4":
                $ deb._var("relationshipPoints", 4, intention = "set")
            "5 o más":
                $ deb._var("relationshipPoints", 6, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Kate?"
            "Menos de -7":
                $ kat.rp (-8)
            "-7 o más":
                $ kat.rp (0)
        menu:
            "¿Cuántos Puntos de Relación tienes con Lisa?"
            "Menos de -4":
                $ lis.rp (-5)
            "-4 o más":
                $ lis.rp (0)
    scene c14s005_005An with fade #kat-XXXX-dap-kim #AN
    play music ("music/beach_long02.ogg")
    "Os situáis aproximadamente en un círculo y empezáis a pasaros la pelota."
    "Poco a poco, es cada vez más aparente que a Kim es a quién más le cuesta cazar la pelota. Recuerdas la caída en el aeropuerto y la casi caída en el bosque."
    "Debbie pilla todas las pelotas sin esfuerzo, al igual que, sorprendentemente, Kate."
    "Después de unas cuantas preguntas y retos inocentes la cosa se va caldeando poco a poco."
    "Las chicas son cruéles y le pasan la pelota cada vez más a Kim."
    scene c14s005_005kimf1 with dissolve
    "No tarda mucho en que a Kim se le escape una pelota que le pasa [dap]."
    call BlinkXP ("c14s005_010" , "d") from _call_BlinkXP_736
    dap "¿Verdad o reto, Kim?"
    call BlinkXP ("c14s005_015" , "d") from _call_BlinkXP_737
    kim "¡Verdad!"
    call BlinkXP ("c14s005_010" , "d") from _call_BlinkXP_738
    dap "¿Tienes novio?"
    if dap._var("route"):
        dap "Y si tienes más de uno, ¿cuantos?"
    call BlinkXP ("c14s005_020" , "d") from _call_BlinkXP_739
    kim "No... Pasa la pregunta a [mc], ¿no?"
    mc "Yo tampoco tengo novio. Pasa la pregunta a Debbie"
    call BlinkXP ("c14s005_025" , "d") from _call_BlinkXP_740
    if mc._var("relationships") > 1:
        if dap._var("route") or sca._var("route"):
            dap "¡Hey! En tu caso deberías decir si tienes novia... o novias... y cuantas si hay más de una..."
        else:
            dap "Me refería a si tenías novia."
    mc "No es lo que has preguntado, [dap]. Para la siguiente, si quieres desperdiciar una pregunta en eso, sabes que la tienes que formular de otra forma. *Risa*"
    call BlinkXP ("c14s005_030" , "d") from _call_BlinkXP_741
    dap "*Gruñido* Vale... ¿Debbie?"
    call BlinkXP ("c14s005_035" , "d") from _call_BlinkXP_742
    deb "No, yo tampoco tengo novio. ¿Kate?"
    call BlinkXP ("c14s005_040" , "d") from _call_BlinkXP_743
    kat "No, y antes de que lo preguntéis, nunca he tenido. Tampoco novia ahora mismo. Saca Kim."
    scene c14s005_005An with dissolve #kim-XXXX-kat-dap #AN
    "Saca Kim y vuelve a hacerse la ronda de pases."
    scene c14s005_005dapf1 with dissolve
    "Pese a la insistencia de las chicas en pasárle la pelota a Kim, esta vez Kate consigue que [dap] falle."
    call BlinkXP ("c14s005_050" , "d") from _call_BlinkXP_744
    kat "¿Verdad o reto, [dap]?"
    call BlinkXP ("c14s005_045" , "d") from _call_BlinkXP_745
    dap "¡Verdad!"
    call BlinkXP ("c14s005_050" , "d") from _call_BlinkXP_746
    kat "¿Eres virgen?"
    mc "Kate..."
    call BlinkXP ("c14s005_055" , "d") from _call_BlinkXP_747
    dap "No pasa nada, [mc]. Sí, lo soy. ¿[sca]?"
    call BlinkXP ("c14s005_060" , "d") from _call_BlinkXP_748
    if sca._var("route"):
        sca "Nope. ¿Kim?"
    else:
        sca "Yo también. ¿Kim?"
    call BlinkXP ("c14s005_065" , "d") from _call_BlinkXP_749
    kim "Más que la Virgen María. ¿[mc]?"
    mc "Yo no. ¿Debbie?"
    call BlinkXP ("c14s005_070" , "d") from _call_BlinkXP_750
    deb "Yo también lo soy. Saca [dap]."
    scene c14s005_005An with dissolve #dap-XXXX-deb-kim #AN
    "Los lanzamientos aumentan de velocidad y dificultad. Debbie y Kate siguen haciéndolo sin esfuerzo, [dap] y [sca] empiezan a sufrir. Para Kim es casi una pesadilla."
    scene c14s005_005kimf2 with dissolve
    "Esta vez Debbie le lanza una pelota a Kim que, pese a que parece fácil, ella no puede pillar."
    call BlinkXP ("c14s005_075b" , "d") from _call_BlinkXP_751
    deb "¿Verdad o reto, Kim?"
    call BlinkXP ("c14s005_075c" , "d") from _call_BlinkXP_752
    kim "¡Reto!"
    call BlinkXP ("c14s005_075b" , "d") from _call_BlinkXP_753
    deb "Rebajemos un poco el tono de las confidencias ¡Haznos un baile sexy!"
    call BlinkXP ("c14s005_075" , "d") from _call_BlinkXP_754
    kim "Pero soy muy torpe... y ser sexy con el agua por encima de la cintura..."
    mc "Kim, eres modelo, seguro que sabes bailar."
    call BlinkXP ("c14s005_080" , "d") from _call_BlinkXP_755
    kim "Bueno, sí, algo... pero nunca he bailado en el agua... mejor salgo a la orilla..."
    scene c14s005_085pv with dissolve
    show c14s005_085v
    kim "¿Así va bien?"
    todas "¡Fantástico!"
    kim "Pues ahora le toca a [mc]"
    mc "*Risa* Empieza a no gustarme este juego."
    call BlinkXP ("c14s005_090" , "d") from _call_BlinkXP_756
    hide c14s005_085v
    "Te acercas a Kim, en la orilla, y le susurras al oído."
    if persistent.walkthrough:
        if kim.rps > -15:
            $ wt1 = "[cg]Kim +5[cc]"
        elif kim.rps >= -20:
            $ wt1 = _("[cg]Kim +5[cc] [cn](necesario para abrir su ruta más tarde.)[cc]")
        else:
            $ wt1 = _("Kim +5 (la ruta ya está cerrada)")

        if kim.rps < -15:
            $ wt2 = _("No podrás abrir la ruta con Kim.")
        else:
            $ wt2 = ""
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¿Quieres que les demos un espectáculo?"  (wt = wt1):
            $ kim.rp (5)
            mc "*Susurrando* No va a bailar nadie más, podríamos aprovechar y enseñarles cómo se hace..."
            if kim.rps > 0:
                $ kim._var("danceOnTheBeach", True) #RIAM, track this one, Please
            else:
                kim "No, no. Te toca dar el espectáculo a ti solo. Yo ya lo he hecho."
        "Déjame el escenario y riéte de mí mientras bailo." (wt=wt2):
            $ Aux = False
    $ resetWalkthrough ()
    if not kim._var("danceOnTheBeach"):
        scene c14s005_095pv with dissolve
        kat "¡Mueve ese cuerpo!"
        dap "¡Demuéstranos el ritmo que llevas dentro!"
        show c14s005_095v
        play music ("music/Rio-Samba.ogg")
        sca "¡Olé! ¡Ese ritmo caribeño solo se puede llevar en la sangre!"
        deb "Parece que haya nacido en Cuba o en Aruba."
        kim "No entiendo por que nos ibamos a reir de ti. ¡Lo estás haciendo genial!"
        stop music fadeout (1.5)
        scene c14s005_100An with dissolve #aba
        hide c14s005_095v
        mc "Se acabó el espectáculo por hoy. Saca Kim."
        play sound "music/applause.ogg"
        kat "Chicas, todas las pelotas a [mc]. A ver si se le escapa alguna y nos hace otro baile."
    else:
        kim "*Susurrando* Por mí genial. ¿Qué se te ha ocurrido?"
        mc "¿Confías en mí?"
        kim "Sí."
        scene c14s005_115a with dissolve
        mc "¿Qué tal se te dan los bailes latinos?"
        kim "Fatal, pero probemos. *Risa* Eres una caja de sorpresas."
        play music ("music/TheMatador.ogg")
        scene c14s005_115An with dissolve #bcdefgh-repeat
        "Empezáis a bailar sin necesidad de música."
        "Parece que hayáis bailado juntos multitud de veces en alguna vida pasada."
        "Vuestros cuerpos se adaptan perfectamente a los movimientos del otro, sin necesidad de palabras, tan solo con un gesto el otro ya sabe lo que tiene que hacer."
        "Dónde moverse."
        "Cómo hacerlo."
        "El sonido del mar es suficiente música para vosotros."
        "No sabes cuánto tiempo habéis bailado antes de que vuestro público empiece a aplaudiros, substituyendo la inexistente música con sus palmadas."
        "Esas palmadas os recuerdan que, aunque lo haya parecido durante unos instantes, no estáis solos en la playa."
        stop music fadeout (1.5)
        "Acabáis vuestro baile, para deleite de vuestro público."
        scene c14s005_115i with dissolve
        play sound "music/applause.ogg"
        todas "*Aplausos*"
        kim "*Susurrando* ¡Ha sido increíble, [mc]! ¡No había bailado así en mi vida!"
        mc "*Susurrando* Nadie podría imaginar que se te dan fatal los bailes latinos."
        mc "¿Volvemos al círculo? Te toca sacar..."
        call BlinkXP ("c14s005_120" , "d") from _call_BlinkXP_757
        deb "¡Ha sido un espectáculo, chicos! El mejor reto que se me podía haber ocurrido."
        call BlinkXP ("c14s005_125" , "d") from _call_BlinkXP_758
        dap "No sabía que bailabas así, [mc]."
        if dap._var("route"):
            call BlinkXP ("c14s005_125b" , "d") from _call_BlinkXP_759
            dap "{i}(Ahora me arrepiento de no haber escogido un sitio donde bailar esta noche para nuestra cita.){/b}"
        call BlinkXP ("c14s005_130" , "d") from _call_BlinkXP_760
        sca "¡Increíble!"
        if sca._var("route"):
            sca "{i}(Tengo que convencerle para que me enseñe a bailar así. Estoy empapada solo de imaginarme en el lugar de Kim.){/i}"
        call BlinkXP ("c14s005_135" , "d") from _call_BlinkXP_761
        kat "¡Vaya dos bailarines! Kim, que forma más sensual de moverte..."
        kat "Chicas, todas las pelotas a [mc]. A ver si se le escapa alguna y nos saca a bailar a las demás. *Risa*"
    mc "Kate, ¿estás segura que quieres que se me escape una pelota?"
    play music ("music/beach_long02.ogg")
    call BlinkXP ("c14s005_105" , "h") from _call_BlinkXP_762
    kat "{b}¿Qué?... ¡No!{/b} ¡No me refería a una de esas pelotas...!"
    mc "Yo tampoco, malpensada. *Risa* Me refería a que si la pelota me la tira [dap] también te va a tocar bailar a ti. *Risa*"
    call BlinkXP ("c14s005_110" , "d") from _call_BlinkXP_763
    sca "Parece que Kate tiene más interés en las pelotas de [mc] del que pensábamos. *Risa*"
    todas "*Risa*"
    scene c14s005_005An with dissolve #kim-XXXX-dap-sca
    "Saca Kim y volveis a hacer otra ronda."
    scene c14s005_005scaf1 with dissolve
    "Esta vez [dap] consigue que [sca] falle."
    call BlinkXP ("c14s005_140" , "d") from _call_BlinkXP_764
    dap "¿Verdad o reto, [sca]?"
    call BlinkXP ("c14s005_145" , "d") from _call_BlinkXP_765
    sca "Antes de que pidas otro baile para que [mc] nos saque a bailar... *Risa* ¡Verdad!"
    call BlinkXP ("c14s005_140" , "d") from _call_BlinkXP_766
    dap "Como todos lleváis poco tiempo en casa, y teniendo en cuenta que no me podéis nombrar a mí ni a [mc] aunque lo seamos... ¿Quién os cae mejor de nuestra familia y por qué?"
    call BlinkXP ("c14s005_150" , "d") from _call_BlinkXP_767
    sca "¡Eso es injusto! ¡No puedo elegir! Todos me habéis tratado genial."
    call BlinkXP ("c14s005_140" , "d") from _call_BlinkXP_768
    dap "Pues tienes que elegir."
    call BlinkXP ("c14s005_155" , "d") from _call_BlinkXP_769
    sca "Mmmmm... [nor]."
    call BlinkXP ("c14s005_140" , "d") from _call_BlinkXP_770
    dap "Falta el por qué..."
    mc "[dap]..."
    scene c14s005_160AnBlink with dissolve
    sca "No pasa nada..."
    sca "Supongo que es por contraste con lo que estoy acostumbrada... podría haber elegido a [mar] por las mismas razones. Son como debería ser una madre de verdad."
    scene c14s005_165 with hpunch
    dap "¡Oh! ¡Lo siento, [sca]! No había pensado en ello..."
    call BlinkXP ("c14s005_160b" , "d") from _call_BlinkXP_771
    sca "Ya he dicho que no pasa nada. Formar parte de esta familia es maravilloso... algún día se lo tendré que decir a ellas..."
    sca "¿Kim?"
    call BlinkXP ("c14s005_170" , "d") from _call_BlinkXP_772
    kim "A mí [emm] me cae genial. Me caéis bien todos, pero con [emm] he pasado más tiempo."
    kim "[mc], ¿tú también tienes que contestar?"
    mc "Me niego. Si queréis pago prenda, pero no puedo elegir entre los miembros de la familia."
    call BlinkXP ("c14s005_175" , "d") from _call_BlinkXP_773
    dap "Creo que te podemos perdonar. No queremos que enseñes lo que llevas debajo del bañador, ¿verdad, chicas?"
    scene c14s005_180AnBlink with dissolve #sca-kim-deb-kat-175Blink bcde
    todas "*Risa* No, no, mejor que no."
    dap "Entonces le toca contestar a Debbie."
    call BlinkXP ("c14s005_185" , "d") from _call_BlinkXP_774
    if deb.rps > 5:
        deb "Realmente con quien más me he relacionado ha sido con [mc], pero si no lo puedo nombrar, supongo que [eri]. Compartimos algunos gustos y es una chica super dulce."
    else:
        deb "Todas habéis sido encantadoras con nosotras, pero si solo puedo nombrar a una, supongo que [eri]. Compartimos algunos gustos y es una chica super dulce."
    deb "¿Kate?"
    call BlinkXP ("c14s005_190" , "d") from _call_BlinkXP_775
    kat "Estoy con Debbie. Sois todas increíbles, pero si tengo que elegir solo a una, Betty. Hemos tenido unas cuantas conversaciones muy interesantes con unos dónuts en medio. *Risa*"
    call BlinkXP ("c14s005_195" , "d") from _call_BlinkXP_776
    kat "Mirad quién viene por allí."
    scene c14s005_200d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    $ renpy.notify ("Profile image unlocked")
    $ lis.addProfileImage ("notAvailable")
    $ lis.addProfileImage ("lisa_2")
    call BlinkXP ("c14s005_200" , "d") from _call_BlinkXP_777
    lis "Hola, chicos. Han suspendido una clase y he podido venir antes. Me han dicho que estabais aquí jugando a algo. ¿Me puedo unir?"
    mc "Por supuesto. Es una versión de Verdad o Reto que han diseñado Kate y [sca]."
    lis "OK. ¡Me apunto!"
    scene c14s005_205An1 with dissolve #205a-sca-205c-kate despistada-205d-Kate falla
    "Después de explicarle las normas, saca [sca], se la pasa a Kate, y esta falla. Parece que su mirada no estaba siguiendo la pelota."
    call BlinkXP ("c14s005_060" , "d") from _call_BlinkXP_778
    sca "Kate, ¿Verdad o Reto?"
    call BlinkXP ("c14s005_210" , "d") from _call_BlinkXP_779
    kat "¡Verdad! No me vais a hacer bailar *Risa*"
    call BlinkXP ("c14s005_060" , "d") from _call_BlinkXP_780
    sca "¿Alguien de los que estamos aquí te resulta sexualmente atractiva?... ¿O atractivo?"
    mc "[sca]..."
    call BlinkXP ("c14s005_215" , "d") from _call_BlinkXP_781
    kat "No tengo por qué negarlo. Estaría ciega si no encontrara a nadie de este círculo atractiva. ¿Os habéis visto?"
    todas "*Risa incómoda*"
    kat "[dap], te toca."
    call BlinkXP ("c14s005_220" , "d") from _call_BlinkXP_782
    dap "Sí..."
    scene c14s005_225AnBlink with hpunch #lis-Kim-Deb-Kat-Sorprendidas-220Blink
    dap "Sacas tú, Kate."
    scene c14s005_205An2 with dissolve #205b-kat-205e-kim despistada-205f-kim falla
    "La revelación de [dap] hace que ninguna de las chicas esté concentrada en el juego. Obviamente Kim no caza la pelota."
    call BlinkXP ("c14s005_230" , "d") from _call_BlinkXP_783
    kat "Kim, ¿Verdad o Reto?"
    call BlinkXP ("c14s005_235" , "d") from _call_BlinkXP_784
    if kim._var("danceOnTheBeach"):
        kim "*Risa* Os estáis poniendo muy chungas con las confidencias. ¡Reto! Así puedes pedirle a [mc] que nos saque a bailar a todas. *Risa*"
    else:
        kim "*Risa* Os estáis poniendo muy chungas con las confidencias. ¡Reto! *Risa*"
    call BlinkXP ("c14s005_230" , "d") from _call_BlinkXP_785
    stop music fadeout (1.5)
    kat "Había pensado en un reto-confidencia..."
    call BlinkXP ("c14s005_235" , "d") from _call_BlinkXP_786
    kim "*Risa* Qué miedo me das... Recuerda que duermo en la misma habitación que tú y me puedo vengar por la noche. *Risa*"
    call BlinkXP ("c14s005_230" , "d") from _call_BlinkXP_787
    play music ("music/CCFunk.ogg")
    kat "*Risa. No me das miedo. Si te sientes atraída por alguien del círculo, bésalo."
    mc "¡Kate! ¡Eso es pasarse!"
    scene c14s005_240AnBlink with dissolve
    kim "No pasa nada, [mc]. Me apetece saber quién besa a quién."
    kim "¿Y si alguien se siente atraído por más de una persona? ¿Y si la persona a la que fuera a besar no quiere que la bese?"
    call BlinkXP ("c14s005_230b" , "d") from _call_BlinkXP_788
    kat "Si te sientes atraída por más de una persona, las besas a todas. Si alguien se siente incómodo con que lo besen, puede rechazar el beso."
    call BlinkXP ("c14s005_240" , "d") from _call_BlinkXP_789
    kim "OK..."
    if persistent.lesbian:
        scene c14s005_245An with dissolve #Beso(d)-(lis-deb-Sca-Dap Sorprendidas)-Beso(d)
        "Kim se dirige a Kate y le planta un beso en los lábios."
        call BlinkXP ("c14s005_245" , "h") from _call_BlinkXP_790
        kat "¿Qué?"
        call BlinkXP ("c14s005_250" , "d") from _call_BlinkXP_791
        kim "Eso es otra pregunta. *Risa*"
        kim "Me acabo de dar cuenta de que no te he pedido permiso... espero que no te haya importado. *Risa*"
        call BlinkXP ("c14s005_245b" , "d") from _call_BlinkXP_792
        kat "No... no..."
    if kim.rps > 0:
        call BlinkXP ("c14s005_255" , "d") from _call_BlinkXP_793
        kim "¿Puedo?"
        mc "Por supuesto."
        scene c14s005_255An with dissolve #255d sonrisa-255e beso-(425-lis, deb, sca, dap, kat sorprendidas)-beso-sonrisa #AN
        "Vuestros labios se juntan en un beso tierno y suave."
        if kim._var("danceOnTheBeach"):
            "Durante del baile ha habido una preciosa conexión entre vosotros que ahora hace que salten chispas."
        call BlinkXP ("c14s005_255b" , "d") from _call_BlinkXP_794
        kim "Gracias."
        mc "¿Gracias? ¿Por qué? Soy yo quien debería dártelas."
        kim "Si me hubieras rechazado me hubiera sentido fatal ahora mismo..."
    call BlinkXP ("c14s005_240" , "d") from _call_BlinkXP_795
    if persistent.lesbian or kim.rps > 0:
        kim "Nadie más. Lo siento, chicas."
    else:
        kim "No, no hay nadie. ¿[mc]?"
    if dap._var("route"):
        call c14s005_KissDaphne from _call_c14s005_KissDaphne
    else:
        mcp "(Besar a [dap] no estaría bien después de lo que pasó con las lecciones.)"
    if sca._var("route"):
        call c14s005_KissScarlett from _call_c14s005_KissScarlett
    else:
        mcp "(Sabiendo lo que siente por mí, no estaría bien besar a [sca].)"
    $ Aux = True
    $ continueTheLoop = True #RIAM. Don't track this one. Will be deleted
    $ kissedGirls = 0 #RIAM. Don't track this one. Will be deleted
    if persistent.walkthrough:
        $ wt1 = "Kim + 6"
        $ wt2 = "Kate + 8"
        $ wt3 = "Lisa + 4"
        $ wt4 = "Debbie + 10"
        $ wt5 = "Kim + 6, Kate + 8, Lisa + 4, Debbie + 10"
    else:
        $ wt1 = ""
        $ wt2 = ""
        $ wt3 = ""
        $ wt4 = ""
        $ wt5 = ""
    while continueTheLoop:
        menu:
            "¿A quién quieres besar?"
            "Besar a Kim" (wt=wt1) if not kim._var("kissedBeach"):
                call c14s005_KissKim from _call_c14s005_KissKim
            "Besar a Kate" (wt=wt2) if not kat._var("kissedBeach"):
                call c14s005_KissKate from _call_c14s005_KissKate
            "Besar a Lisa" (wt=wt3) if not lis._var("kissedBeach"):
                call c14s005_KissLisa from _call_c14s005_KissLisa
            "Besar a Debbie" (wt=wt4) if not deb._var("kissedBeach"):
                call c14s005_KissDebbie from _call_c14s005_KissDebbie
            "Besarlas a todas" (wt=wt5) if Aux:
                call c14s005_KissKim from _call_c14s005_KissKim_1
                call c14s005_KissKate from _call_c14s005_KissKate_1
                call c14s005_KissLisa from _call_c14s005_KissLisa_1
                call c14s005_KissDebbie from _call_c14s005_KissDebbie_1
            "Continuar jugando":
                $ continueTheLoop = False
    $ resetWalkthrough ()
    if dap._var("route") or sca._var("route") or kissedGirls > 0:
        mc "Ya está. Nadie más."
    else:
        mc "No voy a besar a nadie. Sois maravillosas, pero..."
    mc "¿Debbie?"
    python:
        del continueTheLoop
    if deb.rps > 0:
        if deb._var("kissedBeach"):
            call BlinkXP ("c14s005_365" , "d") from _call_BlinkXP_796
            "No te sorprende que Debbie se plante delante tuyo después del beso que habéis compartido hace un momento."
            deb "¿Puedo devolverte el beso que me has dado?... No es que no me haya gustado... no me refiero a eso..."
            mc "Lo sé, Debbie. Me siento muy halagado de que quieras hacerlo."
            mcp "(Si la rechazara se moriría de vergüenza. Si ha sido lo suficientemente valiente como para dar el paso, se merece que no la humillen.)"
            scene c14s005_355An2 with dissolve #360a, 355a-beso, 425-sorpresa Lisa, beso, 370a
            "El segundo beso es infinitamente mejor que el primero. La ternura sigue siendo la misma, pero la inseguridad {b}casi{/b} ha desaparecido."
            "Debbie se siente aceptada, se siente diferente. Por primera vez en su vida, se siente atractiva."
            call BlinkXP ("c14s005_370" , "d") from _call_BlinkXP_797
            deb "¡Phew! *Susurrando* El segundo ha parecido diferente que el primero."
            mc "*Susurrando* En el primero te he besado yo, en este nos hemos besado. La diferencia es enorme."
        else:
            call BlinkXP ("c14s005_365" , "d") from _call_BlinkXP_798
            "Te sorprende que Debbie se plante delante tuyo. Nunca hubieras dicho que se sintiera atraído por ti... A ver si al final va a resultar que eres tonto para estas cosas..."
            deb "¿Te importaría si...?"
            mc "No, Debbie. Para nada. Solo es un juego."
            mcp "(Si la rechazara se moriría de vergüenza. Si ha sido lo suficientemente valiente como para dar el paso, se merece que no la humillen.)"
            call BlinkXP ("c14s005_345" , "d") from _call_BlinkXP_799
            deb "*Susurrando* Hay un problema... Yo... *ininteligible*"
            mc "*Susurrando* No te entiendo, Debbie"
            deb "*Susurrando* Déjame decírtelo al oído..."
            call BlinkXP ("c14s005_350" , "d") from _call_BlinkXP_800
            deb "*Susurrando* Quiero hacerlo, pero... no sé... nunca he besado a nadie..."
            mc "*Susurrando* Entonces corrijamos esa injusticia."
            scene c14s005_355An with dissolve #360a, beso, 425-sorpresa estudiantes, dap y sca, beso, 360a
            "La mayoría de hombres se sorprenderían de que una mujer tan grande, tan musculosa, tan dura externamente, fuera capaz de semejeante ternura en su primer beso."
            "La mayoría de hombres no tienen la suerte de conocer a Debbie."
            "Debbie se siente aceptada, se siente diferente. Por primera vez en su vida, se siente atractiva."
            call BlinkXP ("c14s005_360" , "d") from _call_BlinkXP_801
            deb "¡Phew!"
            mc "¿Bien?"
            deb "Mucho mejor de lo que podría haber esperado... Gracias."
            mc "Gracias a ti, por dejarme ser el primero."
        call BlinkXP ("c14s005_375" , "d") from _call_BlinkXP_802
        deb "Por mi parte ya está."
    else:
        call BlinkXP ("c14s005_375" , "d") from _call_BlinkXP_803
        deb "Nadie por mi parte."
    stop music fadeout (1.5)
    mc "¿Seguimos jugando?"
    play music ("music/Fragile-Beauty.ogg")
    call BlinkXP ("c14s005_380" , "d") from _call_BlinkXP_804
    dap "Creo que ya sería hora de acercarnos a donde estan las madres... por si necesitan ayuda..."
    if kissedGirls > 0:
        dap "{i}(La que se puede liar aquí ahora podría ser complicada. Mejor dejar el juego mientras siga siéndolo.){/i}"
    mc "Como queráis... ha sido un juego interesante... Me lo he pasado muy bien."
    if kat._var("kissedBeach"):
        call BlinkXP ("c14s005_385" , "d") from _call_BlinkXP_805
        if not kat._var("kissRejected"):
            kat "{i}(Tú sí... pero ¿tenías que hacerme dudar de si hay algún hombre que merece la pena?){/i}"
            kat "{i}(¿Mereces la pena, [mc] Marks? ¿Me harás daño si me abro a ti?){/i}"
        else:
            kat "{i}(Tú sí... pero ¿tenías que hacerme dudar de si hay algún hombre que merece la pena? ¿Estabas jugando conmigo? ¿Realmente querías besarme?){/i}"
            kat "{i}(¿Mereces la pena, [mc] Marks? ¿Me harás daño si me abro a ti?){/i}"
        if persistent.lesbian:
            kat "{i}(¿Y Kim? Si lo de [mc] ha sido una sorpresa... lo de Kim... Realmente lo esperaba de Debbie, me debe fallar el radar...)"
    elif persistent.lesbian:
        kat "{i}(Sobretodo interesante... ¿Kim? Nunca lo hubiera dicho... Realmente lo esperaba de Debbie, me debe fallar el radar...)"
    if kim._var("kissedBeach") and kim.rps > 6:
        call BlinkXP ("c14s005_390" , "d") from _call_BlinkXP_806
        kim "{i}(Vale, nos hemos besado dos veces, pero tan solo son besos... y era un juego... No te montes películas en la cabeza, Kim.){/i}"
    elif kim._var("kissedBeach") or kim.rps > 0:
        call BlinkXP ("c14s005_390" , "d") from _call_BlinkXP_807
        kim "{i}(Vale, nos hemos besado, pero tan solo ha sido un beso... y era un juego... No te montes películas en la cabeza, Kim.){/i}"
    if (kim._var("kissedBeach") or kim.rps > 0) and kim._var("danceOnTheBeach"):
        call BlinkXP ("c14s005_390" , "d") from _call_BlinkXP_808
        kim "{i}(Y el baile... que forma de bailar... si todo lo hace con la misma pasión como besar y bailar...){/i}"
    elif kim._var("danceOnTheBeach"):
        call BlinkXP ("c14s005_390" , "d") from _call_BlinkXP_809
        kim "{i}(Ha sido muy divertido... que forma de bailar... si todo lo hace con la misma pasión como bailar...){/i}"
    if lis._var("kissedBeach"):
        call BlinkXP ("c14s005_395" , "d") from _call_BlinkXP_810
        if not lis._var("kissRejected"):
            lis "{i}(¡Me ha besado! Al menos me ha pedido permiso... y era solo un juego... no he engañado a nadie...){/i}"
            lis "{i}(Deja de engañarte a ti misma, Lisa, no sales con Anthony, no ha dado ningún paso para que salgáis, pero... ¿realmente quieres que lo haga?){/i}"
        else:
            lis "{i}(¡Ha intentado besarme! Al menos me ha pedido permiso... y era solo un juego... pero no puedo engañar a Anthony...){/i}"
            lis "{i}(Deja de engañarte a ti misma, Lisa, no sales con Anthony, no ha dado ningún paso para que salgáis, pero... ¿realmente quieres que lo haga?){/i}"
    if deb._var("kissedBeach") and not deb._var("kissRejected"):
        call BlinkXP ("c14s005_395" , "d") from _call_BlinkXP_811
        lis "{i}(¡Ha besado a Debbie! ¡Y después no ha rechazado su beso!){/i}"
        lis "{i}(Solo por lo bien que la ha hecho sentir, ya me tiene que caer bien... tengo que tratarlo mejor. Solo hay que verla.){/i}"
        lis "{i}(¿Estás jugando con ella, [mc]? ¡Ni se te ocurra hacerle daño!){/i}"
    elif deb._var("kissRejected"):
        call BlinkXP ("c14s005_395" , "d") from _call_BlinkXP_812
        lis "{i}(¡Ha querido besar a Debbie!){/i}"
        lis "{i}(¿Estás jugando con ella, [mc]? ¡Ni se te ocurra hacerle daño!){/i}"
    if deb._var("kissedBeach") or deb.rps > 0:
        call BlinkXP ("c14s005_400" , "d") from _call_BlinkXP_813
        deb "{i}(¡Mi primer beso!){/i}"
        if deb._var("kissedBeach") and not deb._var("kissRejected"):
            deb "{i}(¡Y ha sido él el que ha venido a por mí!){/i}"
        else:
            deb "{i}(He tenido que dárselo yo, pero... ¡Qué beso!){/i}"
    elif deb._var("kissRejected"):
        call BlinkXP ("c14s005_405" , "d") from _call_BlinkXP_814
        deb "{i}(¡Ha querido besarme! Y yo lo he rechazado... Era lo lógico, ¿no?){/i}"
        deb "{i}(Rechazar al primer chico que ha querido besarme... Totalmente lógico...){/i}"
    if kissedGirls > 0:
        call BlinkXP ("c14s005_410" , "d") from _call_BlinkXP_815
        if kissedGirls == 1:
            sca "{i}(Pobre chica... no sabe lo que le ha caído encima... seguramente ahora le está dando vueltas a la cabeza sobre lo que ha pasado...){/i}"
            if sca._var("route"):
                sca "{i}(¿Tengo que ponerme nerviosa por tener que compartirlo con ella?){/i}"
        else:
            sca "{i}(Pobres chicas... no saben lo que les ha caído encima... seguramente ahora le están dando vueltas a la cabeza sobre lo que ha pasado...){/i}"
            if sca._var("route"):
                sca "{i}(¿Tengo que ponerme nerviosa por tener que compartirlo con ellas?){/i}"
    scene c14s005_415a with fade
    "Volvéis a la sombrilla, donde las mujeres están teniendo una conversación animada."
    call BlinkXP ("c14s005_420" , "d") from _call_BlinkXP_816
    mom "¿Ya os habéis cansado de jugar en el agua?"
    mc "A [dap] se le ha ocurrido la idea de venir a preguntaros si necesitáis ayuda."
    mom "Muy buena idea. ¿Puedes ir a buscar hielo? Una de las neveras parece que se ha roto y el hielo se está fundiendo muy rápido."
    mc "Sí, ahora mismo voy."
    scene c14s005_415b with dissolve
    dap "No te preocupes, [mc]. Ya vamos nosotras, a ver si encontramos a [eri], [emm], y [eil] por el camino. Es un paseo corto a la gasolinera."
    mc "¿No queréis que vaya con el coche?"
    sca "No es necesario. Así las chicas seguimos conociéndonos un poco más."
    stop music fadeout (1.5)
    if kissedGirls > 0 or dap._var("route") or sca._var("route"):
        mcp "(Y así podéis hablar del último reto sin que yo esté delante, ¿cierto?)"
    mc "OK, como queráis."
    python:
        del kissedGirls
    return
label c14s005_KissDaphne:
    call BlinkXP ("c14s005_260" , "d") from _call_BlinkXP_817
    "Te acercas a [dap], que te recibe con una mirada pícara. Sabéis que esta noche habrá más besos, y que este tan solo es el primero que os dais en público."
    mc "¿Te importa sí...?"
    dap "¿Cómo me va a importar?"
    scene c14s005_265An with dissolve #260a, 265a-beso, 425-sorpresa estudiantes, 265a-beso, 260a
    if persistent.family:
        "No quieres ni imaginar lo que deben pensar ahora mismo las estudiantes. Estás besando a tu prima delante de ellas..."
    else:
        "No quieres ni imaginar lo que deben pensar ahora mismo las estudiantes. Estás besando a la que creen que es tu prima delante de ellas..."
    return
    call BlinkXP ("c14s005_260" , "d") from _call_BlinkXP_818
    mc "¿Bien?"
    dap "¡Genial!"
    return
label c14s005_KissScarlett:
    call BlinkXP ("c14s005_270" , "d") from _call_BlinkXP_819
    "Te acercas a [sca], que te mira nerviosa. Los dos sabéis que no es vuestro primer beso, pero es la primera vez que os besáis delante de alguien diferente de [dap]."
    mc "¿Me permites?"
    sca "Claro que sí."
    scene c14s005_275An with dissolve #270a, 275a-beso, sorpresa estudiantes, 275a-beso, 270a #AN
    "Vuestros labios se juntan en un beso apasionado. Tan solo puedes imaginar la cara de sorpresa de las estudiantes."
    if mc._var("edmundsStory"):
        "Si tan solo supieran que es posible que estés besando a tu medio hermana... esa cara sí que querrías verla."
    call BlinkXP ("c14s005_270" , "d") from _call_BlinkXP_820
    mc "¿Estás bien?"
    sca "No podría estar mejor."
    return
label c14s005_KissKim:
    $ kim._var("kissedBeach", True) #RIAM, track this one, Please
    $ kim.rp (6)
    $ Aux = False
    $ kissedGirls = kissedGirls + 1
    if kissedGirls == 4:
        $ continueTheLoop = False
    call BlinkXP ("c14s005_280" , "d") from _call_BlinkXP_821
    if kim.rps > 6:
        "Te acercas a Kim que después de su beso, te espera expectante."
    else:
        "Te acercas a Kim. Ella no te ha besado, y no sabes cómo va a reaccionar."
    mc "¿Puedo?"
    kim "Por supuesto"
    scene c14s005_285An with dissolve #280a, 285a, 285b beso, sorpresa estudiantes, dap y sca, 285b beso
    if kim.rps > 0:
        if kim.rps > 6:
            "Es vuestro segundo beso en apenas unos minutos. Este sabe diferente. Saber que la atracción es mutua lo hace diferente."
        else:
            "Es vuestro primer beso. No entiendes por qué no ha querido besarte y ahora ha aceptado ser besada. Podrías pensar que ha sido por no avergonzarte, pero sus labios cuentan otra historia."
    else:
        "Es un beso frío. Te permite besarla, pero ella no pone el alma en el beso. Si quieres ganártela vas a tener que trabajártelo más."
    call BlinkXP ("c14s005_280" , "d") from _call_BlinkXP_822
    mc "Gracias. *Susurrando* Por no haberme rechazado."
    if kim.rps > 0:
        kim "*Susurrando con la respiración entrecortada* No se me hubiera ocurrido hacerlo."
    else:
        kim "*Susurrando* Es lo menos que podía hacer."
    return
label c14s005_KissKate:
    $ kat._var("kissedBeach", True) #RIAM, track this one, Please
    $ kat.rp (8)
    $ Aux = False
    $ kissedGirls = kissedGirls + 1
    if kissedGirls == 4:
        $ continueTheLoop = False
    call BlinkXP ("c14s005_290" , "h") from _call_BlinkXP_823
    "Te aproximas a Kate. No sabes cómo se lo va a tomar. Tú tampoco estás muy seguro de que no te vaya a rechazar."
    kat "¿Qué? ¿Yo?"
    mc "*Susurrando* Sí, tú. Ya es hora de que recibas el primer beso de un chico... si lo quieres."
    if kat.rps > 0:
        kat "Si no te importa..."
        scene c14s005_295An with dissolve #295a, 295b-beso1, sorpresa estudiantes, dap y sca, 295b-beso1
        "Vuestras bocas se buscan con nerviosismo. Ninguno de los dos sabéis lo que vais a experimentar cuando vuestros labios se rocen."
        scene c14s005_295An2 with dissolve #295c-beso2-295b-beso1-295c-beso2, 300a
        "El contacto es electrizante. Vuestras bocas se abren, vuestras lenguas se buscan. Debéis hacer un esfuerzo para parar el beso."
        call BlinkXP ("c14s005_300" , "d") from _call_BlinkXP_824
        mc "¿Estamos bien?"
        kat "*Susurrando con la respiración entrecortada* ¿Bien?... Sí... bien..."
        kat "{i}(No puede ser... no me gustan los chicos... ¿qué tiene de especial este?){/i}"
    else:
        call BlinkXP ("c14s005_305" , "d") from _call_BlinkXP_825
        kat "*Susurrando* Si no te importa... te lo agradezco, pero... quizás en otra ocasión."
        mc "*Susurrando* Ningún problema. Si algún día lo quieres, solo tienes que pedirlo."
        $ kat._var("kissRejected", True) #RIAM, track this one, Please
    return
label c14s005_KissLisa:
    $ lis._var("kissedBeach", True) #RIAM, track this one, Please
    $ lis.rp (4)
    $ Aux = False
    $ kissedGirls = kissedGirls + 1
    if kissedGirls == 4:
        $ continueTheLoop = False
    call BlinkXP ("c14s005_310" , "h") from _call_BlinkXP_826
    "La cara de incredulidad de Lisa lo dice todo. Hace unos días en vez de incredulidad habría sido de desprecio. Lisa ha cambiado mucho en unos pocos días."
    lis "¡No puede ser que quieras besarme!"
    mc "Es un juego, Lisa. No te voy a pedir que te cases conmigo. Y solo lo haré si tú quieres. Kate ha sido benévola con esa norma."
    call BlinkXP ("c14s005_315" , "d") from _call_BlinkXP_827
    lis "Pero... yo... Anthony..."
    mc "Lo entiendo. Si no quieres no pasa nada..."
    if lis.rps > 0:
        lis "*Susurrando* Pero es que sí que quiero..."
        mc "No te he oído, Lisa..."
        call BlinkXP ("c14s005_320" , "d") from _call_BlinkXP_828
        lis "Que sí que quiero... Solo es un juego y no estoy saliendo oficialmente con nadie... No quiero crear malos rollos por un juego."
        scene c14s005_325An with dissolve #330a, 325-beso, sorpresa estudiantes, dap y sca, beso, 330a
        "Creías que Lisa iba a tener más experiencia besando, pero tan solo se deja llevar. El beso es más tierno que sensual, pero al acabar ves en su mirada que se ha forjado un vínculo entre vosotros."
        call BlinkXP ("c14s005_330" , "d") from _call_BlinkXP_829
        mc "Gracias, Lisa. Por seguir el juego."
        lis "*Susurrando* Gracias a ti... por tratarme como una persona normal..."
    else:
        call BlinkXP ("c14s005_335" , "d") from _call_BlinkXP_830
        lis "¿Te molestaría mucho que te rechazara? No sé qué hay entre Anthony y yo y... si hay algo... no querría empezarlo sabiendo que he besado a otro chico antes que a él."
        mc "No, Lisa, lo entiendo perfectamente."
        lis "A mí no me gustaría que me hicieran eso, por mucho que sea un juego... no quiero tratar a otros como no me gustaría que me trataran."
        mc "No te preocupes. Eso te honra."
        $ lis._var("kissRejected", True) #RIAM, track this one, Please
    return
label c14s005_KissDebbie:
    $ deb._var("kissedBeach", True) #RIAM, track this one, Please
    $ deb.rp (10)
    $ Aux = False
    $ kissedGirls = kissedGirls + 1
    if kissedGirls == 4:
        $ continueTheLoop = False
    call BlinkXP ("c14s005_340" , "h") from _call_BlinkXP_831
    "Debbie no puede creerse que te estés acercando a ella. Estás seguro de que no es consciente del efecto que puede provocar en los hombres."
    deb "*Susurrando* ¿No te estás equivocando, [mc]? Soy yo, Debbie..."
    mc "No, no me equivoco. Kate ha dicho que bese a quien me atraiga... y tú lo haces."
    mc "Pero solo lo haré si quieres, si me permites hacerlo, Kate al menos nos ha dejado esa opción."
    if deb.rps > 0:
        call BlinkXP ("c14s005_345" , "d") from _call_BlinkXP_832
        deb "*Susurrando* Quiero, pero... *ininteligible*"
        mc "*Susurrando* No te entiendo, Debbie"
        deb "*Susurrando* Déjame decírtelo al oído..."
        call BlinkXP ("c14s005_350" , "d") from _call_BlinkXP_833
        deb "*Susurrando* Quiero, pero... no sé... nunca me han besado..."
        mc "*Susurrando* Entonces déjame corregir esa injusticia."
        scene c14s005_355An with dissolve #350a, 355b-beso, sorpresa estudiantes, dap y sca, beso, 360a
        "La mayoría de hombres se sorprenderían de que una mujer tan grande, tan musculosa, tan dura externamente, fuera capaz de semejeante ternura en su primer beso."
        "La mayoría de hombres no tienen la suerte de conocer a Debbie."
        call BlinkXP ("c14s005_360" , "d") from _call_BlinkXP_834
        deb "¡Phew!"
        mc "¿Bien?"
        deb "Mucho mejor de lo que podría haber esperado... Gracias."
        mc "Gracias a ti, por dejarme ser el primero."
    else:
        call BlinkXP ("c14s005_345" , "d") from _call_BlinkXP_835
        deb "Me siento muy halagada, [mc], pero debo declinar. Lo siento."
        mc "No pasa nada, tan solo es un juego."
        deb "{i}(Sí, solo es un juego, pero en el que reconoces estar atraído por mí. ¡Por mí!){/i}"
        $ deb._var("kissRejected", True) #RIAM, track this one, Please
    return
label c14s006_Christmas:
    if _in_replay:
        $ mc._var("relationships" , 0, "set")
        call mrS3_edmund_story from _call_mrS3_edmund_story_7
        call mrS3_dap_route from _call_mrS3_dap_route_19
        call mrS3_sca_route from _call_mrS3_sca_route_16
        if not sca._var("route"):
            menu:
                "¿Besaste a Kate en el Verdad o Reto?"
                "Sí":
                    $ kat._var("kissedBeach" , True)
                "No":
                    $ kat._var("kissedBeach" , False)
                    menu:
                        "¿Besaste a Kim en el Verdad o Reto?"
                        "Sí":
                            $ kim._var("kissedBeach" , True)
                        "No":
                            $ kim._var("kissedBeach" , False)
                            menu:
                                "¿Besaste a Debbie en el Verdad o Reto?"
                                "Sí":
                                    $ deb._var("kissedBeach" , True)
                                "No":
                                    $ deb._var("kissedBeach" , False)
                                    menu:
                                        "¿Besaste a Lisa en el Verdad o Reto?"
                                        "Sí":
                                            $ lis._var("kissedBeach" , True)
                                        "No":
                                            $ lis._var("kissedBeach" , False)
                                            menu:
                                                "¿Te besó Kim en el Verdad o Reto?"
                                                "Sí":
                                                    $ kim._var("relationshipPoints", 5, intention = "set")
                                                "No":
                                                    $ kim._var("relationshipPoints", 0, intention = "set")
                                                    menu:
                                                        "¿Te besó Debbie en el Verdad o Reto?"
                                                        "Sí":
                                                            $ deb._var("relationshipPoints", 5, intention = "set")
                                                        "No":
                                                            $ deb._var("relationshipPoints", 0, intention = "set")
        call mrS3_oma_route from _call_mrS3_oma_route_10
        call mrS3_meg_route from _call_mrS3_meg_route_5
        call mrS3_mar_route from _call_mrS3_mar_route_26
        call mrS3_nor_route from _call_mrS3_nor_route_18
        call mrS3_emm_route from _call_mrS3_emm_route_26
        call mrS3_eri_route from _call_mrS3_eri_route_19
        call mrS3_eil_route from _call_mrS3_eil_route_14
        call mrS3_sam_route from _call_mrS3_sam_route_11
        call mrS3_sim_route from _call_mrS3_sim_route_13
        call mrS3_sai_route from _call_mrS3_sai_route_14
    play music ("music/Beach.ogg")
    if dap._var("route") or sca._var("route") or kat._var("kissedBeach") or kim._var("kissedBeach") or deb._var("kissedBeach") or lis._var("kissedBeach") or persistent.lesbian or kim.rps>0 or deb.rps>0:
        call BlinkXP ("c14s006_005" , "d") from _call_BlinkXP_836
        mom "¿Ha pasado algo? Se las veía incómodas."
        mc "Lo de siempre. Un juego de Verdad o Reto que se va de las manos."
        call BlinkXP ("c14s006_010" , "d") from _call_BlinkXP_837
        bet "No me digas que os habéis tenido que desnudar. Tú y seis chicas. Es como acababa en la universidad..."
        mc "No, no te preocupes. Solo ha llegado a unos besos."
        bet "Entonces habéis jugado la versión para todos los públicos. *Risa*"
        todas "*Risa*"
    mc "Aparte del hielo, ¿necesitáis que vaya a buscar algo más?"
    call BlinkXP ("c14s006_015" , "d") from _call_BlinkXP_838
    nor "No, en cuanto vuelvan las chicas y lleguen [sam] y [sim], iremos a comer."
    mc "¿Os importa si invito a una amiga a la comida? No sé si llegará a tiempo, pero está sola en la ciudad y pasar la Navidad sola..."
    call BlinkXP ("c14s006_020" , "d") from _call_BlinkXP_839
    mee "Eres consciente de que no es Navidad, ¿verdad? Solo hacemos esto porque a [sca] le pareció divertido hacer una excursión familiar a la playa."
    mc "Lo sé, pero si celebramos la Navidad, lo hacemos con toda la familia y amigos."
    mee "Si es por eso, entonces, llámala."
    mc "Dadme un momento y ahora vuelvo."
    stop music fadeout (1.5)
    scene c14s006_025a with dissolve
    "Intentas hacer una videoconferencia con Alexia, pero está conduciendo. Lo único que consigues es una llamada de voz."
    play music ("music/Motor.ogg")
    if oma._var("route"):
        mc "Buenos días, mi amor."
        oma "Buenos días, mi vida. ¿Querías algo? Estoy conduciendo."
        mc "Aparte de escuchar tu voz..."
    else:
        mc "Buenos días, Alexia."
        oma "Buenos días, [mc]. ¿Querías algo? Estoy conduciendo."
    mc "¿A qué hora llegas a Newport?"
    oma "En poco más de una hora. Hace un rato que he pasado Santa Barbara."
    mc "¿Tienes un bikini rojo? ¿O verde?"
    oma "¿Qué? ¿Por qué?"
    mc "Te va a parecer raro, pero estamos haciendo una fiesta navideña en la playa, y quería saber si quieres venir a comer."
    oma "Sabes que estamos en Julio, ¿verdad?"
    mc "Sí, lo sé. Ha sido idea de [sca], una amiga... ¡Uff! Te tengo que contar muchas cosas que han pasado desde que te fuiste."
    mc "¿Pero tienes el bikini rojo o verde?"
    oma "Más bien rosa y verde."
    mc "Sirve. ¿Gorro de Santa?"
    oma "*Risa* ¡Estáis locos!"
    mc "*Risa* ¿Tienes o no tienes?"
    oma "*Risa* ¡Claro que tengo!"
    "Después de darle las indicaciones para llegar a la parte de la playa donde estáis."
    mc "Entonces te veo en una hora. En bikini y con el gorro de Santa."
    if oma._var("route"):
        mc "Te veo pronto, mi amor. Te quiero."
        oma "Hasta ahora, mi vida. No puedes imaginar lo que te he echado de menos."
    else:
        mc "Te veo pronto, Alexia."
        oma "Hasta ahora, [mc]."
    scene c14s006_025b with dissolve
    stop music fadeout (1.5)
    "La siguiente llamada seguramente sea más complicada."
    play music ("music/Sunny-Skies.ogg")
    call BlinkXP ("c14s006_030" , "d") from _call_BlinkXP_840
    if meg._var("route"):
        mc "Buenos días, preciosa. ¿Estás en la playa?"
        meg "Buenos días, guapo. Sí, veo que tú también. Podríamos haber ido juntos."
    else:
        mc "Buenos días, [meg]. ¿Estás en la playa?"
        meg "Buenos días, [mc]. Sí, veo que tú también. Podríamos haber ido juntos."
    mc "Por eso te llamaba. Estamos haciendo una comida navideña familiar en la playa... no preguntes... y te llamaba para preguntarte si querías unirte."
    mc "Veo que ya llevas un bañador rojo. *Risa*"
    if meg._var("route"):
        mc "Déjame verlo..."
        scene c14s006_035d with dissolve:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXP ("c14s006_035b" , "d") from _call_BlinkXP_841
        mc "¡Sexy!"
        meg "*Risa* ¿Contento?"
        mc "Lo estaría si estuvieras aquí y pudiera arrancártelo en vez de solo verlo. *Risa*"
        mc "Pero a lo que íbamos. ¿Vienes?"
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ meg.profileImages.pop (2) # first remove
        $ meg.profileImages.insert (2, ("megan_2", None)) # then add new
    call BlinkXP ("c14s006_035" , "d") from _call_BlinkXP_842
    meg "No puedo, [mc]. Hoy trabajo aquí, en Westport, y tengo el coche en el mecánico. No podía ir y volver, y no voy a hacer que dejes a tu familia para venir a buscarme y traerme de nuevo."
    mc "Vaya, qué lástima. ¿Cómo vendrás a trabajar el fin de semana a Newport?"
    call BlinkXP ("c14s006_040" , "d") from _call_BlinkXP_843
    meg "Si aún no tengo el coche arreglado, cogeré el autobús y me quedaré en un motel las tres noches."
    mc "¡De eso nada! Ya iré a buscarte y te quedas a dormir en casa."
    if mar._var("route"):
        if persistent.family:
            mc "Recuerda que mi madre te dijo que vinieras a dormir a casa cuando estuvieras en la ciudad."
        else:
            mc "Recuerda que [mar] te dijo que vinieras a dormir a casa cuando estuvieras en la ciudad."
    call BlinkXP ("c14s006_045" , "d") from _call_BlinkXP_844
    meg "No quiero ser una molestia, [mc]."
    mc "No lo vas a ser. Seguro que a todo el mundo le encanta conocerte, y así conoces a toda la familia."
    call BlinkXP ("c14s006_050" , "d") from _call_BlinkXP_845
    meg "Haces muy difícil rechazar la oferta. Perfecto entonces, ¿nos vemos el viernes? ¿Me podrás recoger en la estación de autobuses si no me han arreglado el coche?"
    mc "Espera un momento... ¿tienes algo para beber ahí?"
    meg "Sí, tengo un refresco."
    mc "Espera un momento."
    scene black with dissolve
    "Vas a buscar una cerveza a las neveras y reanudas la videoconferencia."
    call BlinkXP ("c14s006_055" , "d") from _call_BlinkXP_846
    meg "¿Por qué preguntabas lo de la bebida?"
    mc "Ya te he dicho que estamos haciendo una fiesta Navideña, y no quería colgar sin brindar contigo."
    call BlinkXP ("c14s006_060" , "d") from _call_BlinkXP_847
    if meg._var("route"):
        mc "¡Feliz Navidad, cariño!"
        meg "¡Estás loco, pero me encanta! ¡Feliz Navidad, cielo!"
    else:
        mc "¡Feliz Navidad, [meg]!"
        meg "¡Estás loco! ¡Feliz Navidad, cielo!"
    call BlinkXP ("c14s006_065" , "d") from _call_BlinkXP_848
    mc "Te recojo el viernes en la estación de autobuses si no tienes el coche. Avísame a qué hora llegas."
    if meg._var("route"):
        meg "¡Perfecto! Hasta el viernes. Te quiero."
        mc "¡Yo más!"
    else:
        mc "¡Perfecto! Hasta el viernes. Y gracias."
        meg "Nos vemos el viernes."
    stop music fadeout (1.5)
    call BlinkXP ("c14s006_070" , "f") from _call_BlinkXP_849
    mc "Ya está. Alexia se unirá a nosotros en la comida."
    play music ("music/Beach.ogg")
    nor "¡Genial! Parece una buena chica."
    scene c14s006_075a with dissolve
    bet "Y muy guapa..."
    mee "Sí, si la hubierais visto en el aeropuerto... Iba un poco arreglada y estaba guapísima. Lástima que sea un poco mayor para nuestro [mc]."
    if nor._var("route") and mar._var("route"):
        scene c14s006_075b with hpunch
        mar "*Risa*" (multiple=2)
        nor "*Carcajada*" (multiple=2)
        scene c14s006_075e with dissolve
    elif nor._var("route"):
        scene c14s006_075c with hpunch
        nor "*Risa*"
        scene c14s006_075e with dissolve
    elif mar._var("route"):
        scene c14s006_075d with hpunch
        mom "*Risa*"
        scene c14s006_075e with dissolve
    mc "*Risa*"
    call BlinkXP ("c14s006_080" , "d") from _call_BlinkXP_850
    mee "¿He dicho algo gracioso?"
    mc "Un poco, Meemaw. Siempre decís que parezco más mayor de mi edad. Sería injusto que yo juzgase a las mujeres por la suya."
    call BlinkXP ("c14s006_085" , "d") from _call_BlinkXP_851
    mee "Pero tienes que salir con chicas de tu edad. ¿Qué harías con dos viejas como Betty o yo?"
    mc "Un trío con mucho cuidado por si os rompéis. *Risa*"
    _("Todas menos Meemaw") "*Risa*"
    scene c14s006_090a with hpunch
    mee "¡Ni se te ocurra bromear con eso!"
    bet "Me parece que no está bromeando, Olivia. *Risa* Creo que nuestro chico tiene razón..."
    call BlinkXP ("c14s006_095" , "d") from _call_BlinkXP_852
    mee "Pero nosotras somos... somos..."
    mc "Dos mujeres preciosas a las que quiero mucho y que me quieren a mí. Si fuera posible... Pero tranquilízate, estaba de broma. Sé que tú nunca aceptarías, Meemaw."
    scene c14s006_090b with hpunch
    mee "¿Yo? ¿Y Betty sí?"
    bet "Quizás no con [mc], pero en otras circunstancias, ¿quién sabe qué hubiera pasado?"
    scene c14s006_090c with dissolve
    mom "Tía Betty nos ha salido pícara. *Risa*" (multiple=2)
    nor "*Risa* Tía, me acabas de sorprender mucho." (multiple=2)
    mc "Yo solo veo cinco mujeres hermosas. No veo la edad que sumáis entre todas."
    call BlinkXP ("c14s006_100" , "d") from _call_BlinkXP_853
    kia "Porque te has dejado la calculadora en casa. *Risa*"
    todas "*Risa*"
    mc "Mamá, pásame otra cerveza, por favor."
    call BlinkXP ("c14s006_105" , "d") from _call_BlinkXP_854
    mom "¿Ya te has acabado la que te acabas de llevar? Deberías frenar un poco con el alcohol, ¿no?"
    mc "No, tranquila. Creo que acabo de ver a alguien y voy a saludarla."
    mom "¿Alguien?"
    stop music fadeout (1.5)
    mc "Cosas mías, Mamá."
    play music ("music/Sad-Piano.ogg")
    scene c14s006_110d with dissolve:
        xalign 1.0
        linear 5.0 xalign 0.0
    pause (5.0)
    $ renpy.notify ("Profile image unlocked")
    $ eva.addProfileImage ("eva_2")
    call BlinkXP ("c14s006_110" , "d") from _call_BlinkXP_855
    mc "Buenos días, Eva. No es un buen sitio para esconderse, ¿no?"
    eva "Buenos días, [mc]. Es difícil esconderse en una playa casi vacía."
    call BlinkXP ("c14s006_115" , "d") from _call_BlinkXP_856
    eva "Y más aún si vienes aquí y llamas la atención sobre mí."
    mc "Lo siento, pero estamos de celebración navideña y os quería incluír. ¿Amanda está por aquí?"
    call BlinkXP ("c14s006_120" , "h") from _call_BlinkXP_857
    eva "¿Incluirnos? ¿A nosotras? ¿Por qué?"
    mc "Es fácil. Es una celebración familiar. Y sois parte de la famila. De una forma rara, pero lo sois."
    if persistent.family:
        mc "Sois los clones de mi hermana y de mis primas. Por raro que parezca, desde que ayer le vi la cara a Amanda, no puedo evitar pensar en vosotras como parte de la familia."
    else:
        mc "Mi hermana y mis primas son clones vuestros. Por raro que parezca, desde que ayer le vi la cara a Amanda, no puedo evitar pensar en vosotras como parte de la familia."
    call BlinkXP ("c14s006_125" , "d") from _call_BlinkXP_858
    eva "No somos {b}tu{/b} familia. Amanda es {b}mi{/b} familia. No vosotros."
    if not persistent.family:
        eva "Ni siquiera tu \"hermana\" y tus \"primas\" son tu familia."
    mc "Te equivocas en eso, Eva. Yo decido quién es mi familia, no la sangre que corre por nuestras venas."
    mc "Puede que tu no me consideres parte de tu familia, pero yo si que os considero familia a vosotras dos. No puedo mirarte a la cara y no ver a [dap] o a [eri]."
    call BlinkXP ("c14s006_130" , "d") from _call_BlinkXP_859
    eva "Lo que tú digas..."
    mc "Pero no me has respondido, ¿Amanda también está por aquí?"
    call BlinkXP ("c14s006_135" , "d") from _call_BlinkXP_860
    eva "No... está en la base. ¿Por qué?"
    mc "Porque, aunque te parezca ridículo después de lo que acabas de decirme, quiero felicitaros la Navidad a las dos. La Navidad es para pasarla en familia, ¿no?"
    call BlinkXP ("c14s006_140" , "d") from _call_BlinkXP_861
    eva "Pero... ¿tú eres tonto? ¡No es Navidad! ¡Y ya te he dicho que no somos tu familia!"
    mc "Y yo te he dicho que tu concepto de familia y el mío son diferentes. ¿Puedes llamarla?"
    call BlinkXP ("c14s006_145" , "d") from _call_BlinkXP_862
    mc "Te he traído una cerveza si sirve de algo..."
    eva "Gracias... supongo... Aquí tienes a Amanda..."
    call BlinkXP ("c14s006_150" , "d") from _call_BlinkXP_863 #tablet con Amanda
    mc "Hola, Amanda. ¿Qué te pasa?"
    ama "Nada, nada... se me ha metido algo en el ojo..."
    mc "¿Nos estabas escuchando?"
    call BlinkXP ("c14s006_155" , "d") from _call_BlinkXP_864 #no tablet
    ama "Sí, Eva siempre tiene el micro abierto..."
    mc "Pues debes saber que lo que le he dicho a ella, también se aplica a ti."
    mc "Espero que un día os podáis sentar en la mesa con nosotros en Navidad o en Acción de Gracias. O en cumpleaños. O cuando sea."
    call BlinkXP ("c14s006_160" , "d") from _call_BlinkXP_865
    ama "Gracias, pero no será posible. Nuestra misión con vosotros casi ha acabado... dudo que nos veamos demasiado después. "
    ama "De todas formas, eso levantaría demasiadas liebres. No sé cómo se lo tomarían [emm], [dap] y [eri]."
    mc "Seguramente fliparian al principio. Después os recibirían con los brazos abiertos. Es posible que os debamos la vida..."
    scene c14s006_165a with dissolve #visto desde arriba. Amanda en la tablet
    eva "*Susurrando* ¿Solo posible?"
    ama "¡Eva!"
    mc "¿Qué? No te he entendido..."
    scene c14s006_165b with dissolve
    eva "No... nada..."
    scene c14s006_165c with dissolve
    mc "¿Eso es un arma? ¿Has traído un arma a la playa?"
    call BlinkXP ("c14s006_170" , "d") from _call_BlinkXP_866
    eva "A menos que quieras que proteja a {b}tu{/b} familia tirandoles conchas de almeja a los tipos malos... la tengo que llevar encima."
    stop music fadeout (1.5)
    mc "Bueno, pues entonces creo que me llevaré la cerveza. Armas y alcohol..."
    call BlinkXP ("c14s006_175" , "d") from _call_BlinkXP_867
    play music ("music/Acoustic-Inspirational.ogg")
    eva "Si se te ocurre tocar mi cerveza, me obligarás a usar la pistola. *Risa*"
    mc "¡Coño! Sabes reírte y hacer bromas..."
    if persistent.family:
        mc "Creía que más que un clon eras un robot."
    call BlinkXP ("c14s006_180" , "d") from _call_BlinkXP_868
    ama "Ahí te ha pillado, Eva. *Risa*"
    scene c14s006_165b with dissolve
    eva "*Gruñido*"
    call BlinkXP ("c14s006_185" , "d") from _call_BlinkXP_869
    ama "[mc], deberías irte ya. [emm], [eri], y [eil] se acercan a vuestra posición y si te ven descubrirán a Eva."
    mc "Bueno, chicas, entonces tan solo desearos Feliz Navidad."
    call BlinkXP ("c14s006_190" , "d") from _call_BlinkXP_870
    ama "Feliz Navidad, [mc]."
    mc "Feliz Navidad, Amanda."
    mc "Eva, ¿brindas conmigo o me tengo que llevar la cerveza?"
    call BlinkXP ("c14s006_195" , "d") from _call_BlinkXP_871
    eva "Feliz Navidad, [mc]."
    mc "Feliz Navidad, Eva."
    mc "Espero volver a veros pronto."
    call BlinkXP ("c14s006_200" , "d") from _call_BlinkXP_872
    ama "Nos verás. Vete ya. Hacia el noreste para interceptar a las chicas."
    mc "No seas como mi GPS, no tengo una brújula en el reloj. ¿Dónde coño está el noreste?"
    ama "*Risa* Hacia el merendero..."
    mc "Hasta otra, chicas."
    scene c14s006_200d with fade
    ama "Te dije que no era mal tipo. Ha sido muy bonito lo que ha dicho."
    eva "*Susurrando* Y ha traído cerveza. Sin querer meterse en mis bragas por ello."
    ama "¿Te puedes imaginar teniendo una familia como esa?"
    eva "*Susurrando* Estaría bien pasar una Navidad con una familia de verdad por una vez."
    if mar._var("route") or emm._var("route") or nor._var("route") or dap._var("route") or eri._var("route") or sca._var("route"):
        eva "*Susurrando* Aunque viendo como trata a la familia, no me extrañaría que realmente quisiera meterse en nuestras bragas. *Risa*"
    elif mc._var("relationships") > 0:
        eva "*Susurrando* Aunque viendo como trata a lo que llama familia, no me extrañaría que realmente quisiera meterse en nuestras bragas. *Risa*"
    ama "Sé que eso no te importaría demasiado. *Risa*"
    eva "*Susurrando* Yo tengo suficiente contigo, hermanita. Y que conste que hablo de la Navidad."
    ama "También sé que eso es mentira. *Risa*"
    eva "*Gruñido* Te acabas de ganar que te cuelgue. Hasta luego. Feliz Navidad."
    ama "Feliz Navidad, Eva."
    stop music fadeout (1.5)
    scene black with dissolve
    "Te diriges hacia el merendero (sí, sí, hacia el jodido noreste), con la esperanza de interceptar a las chicas a tiempo."
    play music ("music/Happy-Sun.ogg")
    scene c14s006_205d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ eri.profileImages.pop (2) # first remove
        $ eri.profileImages.insert (2, ("erika_2", None)) # then add new
    call BlinkXP ("c14s006_205" , "d") from _call_BlinkXP_873
    mc "Hola, chicas. ¿Qué tal el paseo?"
    eri "Bien, hemos estado charlando y poniéndonos al día."
    scene c14s006_210d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c14s006_210" , "d") from _call_BlinkXP_874
    emm "¿Nos hemos perdido algo?"
    mc "Una partida de Verdad o Reto con las chicas..."
    if dap._var("route") or sca._var("route") or kat._var("kissedBeach") or kim._var("kissedBeach") or deb._var("kissedBeach") or lis._var("kissedBeach") or persistent.lesbian or kim.rps>0 or deb.rps>0:
        mc "Qué se ha ido un poco de las manos. No aprenderemos nunca."
        call BlinkXP ("c14s006_215" , "d") from _call_BlinkXP_875
        emm "¿[dap] haciendo de las suyas?"
        mc "No, esta vez ha sido Kate, pero no ha habido malos rollos."
    scene c14s006_220d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ eil.profileImages.pop (2) # first remove
        $ eil.profileImages.insert (2, ("eileen_2", None)) # then add new
    call BlinkXP ("c14s006_220" , "d") from _call_BlinkXP_876
    eil "¿Dónde están ahora?"
    mc "Han ido a por hielo a la gasolinera. Tenemos una nevera con una fuga."
    mc "Y de paso a ver si os encontraban."
    call BlinkXP ("c14s006_225" , "d") from _call_BlinkXP_877
    eri "Ah, pues podemos ir a la gasolinera a buscarlas y las ayudamos..."
    mc "Así os enteráis de lo que ha pasado en la partida, ¿no? *Risa*"
    if emm._var("route"):
        call BlinkXP ("c14s006_230" , "d") from _call_BlinkXP_878
        emm "¿Puedo hablar un momento contigo antes de irnos?"
        mc "Sí, claro. ¿Nos perdonáis un momento?"
        scene c14s006_235a with dissolve
        eil "Por supuesto." (multiple=2)
        eri "No tengáis prisa." (multiple=2)
        call BlinkXP ("c14s006_240" , "d") from _call_BlinkXP_879
        mc "¿Qué pasa, [emm]?"
        emm "Bueno... sé que querías que hiciéramos público lo nuestro... y creo que [eri] lo debería saber."
        mc "Cuando quieras. El día de Verdad o Reto querías restregárselo por la cara..."
        call BlinkXP ("c14s006_245" , "d") from _call_BlinkXP_880
        emm "Y me dijiste que no lo hiciera porque lo de Jack estaba muy reciente. Me acuerdo."
        emm "Entonces ¿no te importaría que lo supiera?"
        mc "No, cuando estés preparada, se lo decimos."
        scene c14s006_250An with dissolve #AN Emma se va mirándote, y se gira hacia eri y eileen, desenfocadas.
        emm "¡Genial! Porque se me ha escapado... Ahora no te puedes enfadar."
        emm "Chicas, no le importa que se me haya escapado. ¡Uff!"
        mc "{b}¿QUÉ?{/b}"
        call BlinkXP ("c14s006_255" , "d") from _call_BlinkXP_881
        eil "Estábamos hablando de chicos..."
        call BlinkXP ("c14s006_260" , "d") from _call_BlinkXP_882
        eri "Y [emm] estaba todo el rato \"mi chico esto, mi chico aquello\"..."
        call BlinkXP ("c14s006_265" , "d") from _call_BlinkXP_883
        emm "Y una de las veces he dicho \"[mc] esto, [mc] aquello\". Lo siento, supongo que querías estar cuando se lo dijésemos."
        emm "Tenías que haberles visto las caras..."
        mc "Pues sí. Me hubiera gustado estar... Sólo me puedo imaginar su sorpresa... lástima que no la pueda ver ya."
        if eri._var("route"):
            scene c14s006_235b with dissolve
            "[eri] capta el sentido de tus palabras y te mira inquisitivamente. Asientes con la cabeza."
            call BlinkXP ("c14s006_270" , "d") from _call_BlinkXP_884
            eri "Bueno, no puedes ver la mía, pero puedes ver la de [emm]."
            call BlinkXP ("c14s006_275" , "d") from _call_BlinkXP_885
            emm "¿La mía? ¿Por qué? Yo ya sabía que salía con él."
            call BlinkXP ("c14s006_280" , "d") from _call_BlinkXP_886
            eri "Porque yo también salgo con él, [emm]."
            scene c14s006_285An with hpunch #AN Eri-MC-repeat
            emm "{b}¿Qué?{/b}"
            emm "¡No me jodáis! ¡Con eso no se bromea!"
            emm "¿Me lo estáis diciendo en serio?"
            emm "¡Por el amor de Dios! ¡Decid algo!"
            mc "Sí, [emm]. Estamos saliendo juntos."
            scene c14s006_285c with hpunch #abrazo. Eri con cara de flipe
            emm "¡Joder, [eri]! No quiero saber lo mal que lo has pasado..."
            eri "¿Qué? ¿Yo? ¿Mal? ¡No te entiendo!"
            call BlinkXP ("c14s006_290" , "d") from _call_BlinkXP_887
            emm "Con lo mal que se te da guardar secretos, tenerme que ocultar algo así..."
            mc "[emm], a quien se le da mal guardarlos es a ti..."
            if mar._var("route"):
                call BlinkXP ("c14s006_295" , "d") from _call_BlinkXP_888
                emm "No me digas eso, que bien he guardado el de..."
                mc "¡[emm]!"
                call BlinkXP ("c14s006_300" , "d") from _call_BlinkXP_889
                emm "¡Oops! ¡Casi!"
            else:
                call BlinkXP ("c14s006_295" , "d") from _call_BlinkXP_890
                emm "No me digas eso. Siempre he guardado tus secretos... bueno... casi siempre..."
            call BlinkXP ("c14s006_310" , "d") from _call_BlinkXP_891
            eri "¿Algún secreto más que quieras compartir con nosotros, [mc]?"
            if eil._var("route"):
                mc "Yo no, pero..."
                call BlinkXP ("c14s006_315" , "d") from _call_BlinkXP_892
                eil "Yo también salgo con él, [emm]."
                call BlinkXP ("c14s006_320" , "d") from _call_BlinkXP_893
                emm "Bueno, de ti ya me lo imaginaba..."
                call BlinkXP ("c14s006_325" , "d") from _call_BlinkXP_894
                eil "¿Qué? ¿Desde cuando?"
                call BlinkXP ("c14s006_330" , "d") from _call_BlinkXP_895
                emm "Desde que me dijo que estaría con otras chicas."
                emm "A ver, si estaba conmigo y quería estar con otras... tú tenías que ser una de las otras."
                emm "Además, eso de llevar a [eri] cada día al café... pero claro, si también sale con ella..."
                emm "Todos os veíamos antes de que se fuera a Portland y erais la pareja perfecta. Yo incluso lloré un poquito cuando rompisteis."
                scene c14s006_335a with hpunch #anrazo a eil y eri. Las dos flipando
                emm "¡Joder! ¡Las tres saliendo con el mismo chico!"
                if mar._var("route"):
                    emm "No me imagino a nadie con la que me importase menos compartirlo que con vosotras... bueno, sí... pero soy una tumba."
                else:
                    emm "No me imagino a nadie con la que me importase menos compartirlo que con vosotras..."
                eil "*Susurrando* Se ha roto." (multiple=2)
                eri "*Susurrando* Creía que nos iba a matar." (multiple=2)
            else:
                mc "Ninguno que esté en mi poder compartir. Y si [emm] sabe alguno, mejor que tenga esa preciosa boca cerrada."
                if oma._var("route"):
                    mc "Igual que vas a hacer tú, ¿no?"
                scene c14s006_335b with hpunch #anrazo a eri. Eri flipando
                emm "¡Joder! ¡Las dos saliendo con el mismo chico!"
                if mar._var("route"):
                    emm "No me imagino a nadie con la que me importase menos compartirlo que contigo... bueno, sí... pero soy una tumba."
                else:
                    emm "No me imagino a nadie con la que me importase menos compartirlo que contigo..."
                eri "*Susurrando* Se ha roto."
        elif eil._var("route"):
            scene c14s006_235c with dissolve
            "[eil] capta el sentido de tus palabras y te mira inquisitivamente. Asientes con la cabeza."
            call BlinkXP ("c14s006_345" , "d") from _call_BlinkXP_896
            eil "Bueno, no puedes ver la mía, pero puedes ver la de [emm]."
            call BlinkXP ("c14s006_275" , "d") from _call_BlinkXP_897
            emm "¿La mía? ¿Por qué? Yo ya sabía que salía con él."
            call BlinkXP ("c14s006_315" , "d") from _call_BlinkXP_898
            eil "Yo también salgo con él, [emm]."
            call BlinkXP ("c14s006_320" , "d") from _call_BlinkXP_899
            emm "Bueno, de ti ya me lo imaginaba..."
            call BlinkXP ("c14s006_325" , "d") from _call_BlinkXP_900
            eil "¿Qué? ¿Desde cuando?"
            call BlinkXP ("c14s006_330" , "d") from _call_BlinkXP_901
            emm "Desde que me dijo que estaría con otras chicas."
            emm "A ver, si estaba conmigo y quería estar con otras... tú tenías que ser una de las otras."
            emm "Además, eso de llevar a [eri] cada día al café..."
            emm "Todos os veíamos antes de que se fuera a Portland y erais la pareja perfecta. Yo incluso lloré un poquito cuando rompisteis."
            scene c14s006_335c with hpunch #anrazo a eil. eil flipando
            emm "¡Joder! ¡Las dos saliendo con el mismo chico!"
            if mar._var("route"):
                emm "No me imagino a nadie con la que me importase menos compartirlo que contigo... bueno, sí... pero soy una tumba."
            else:
                emm "No me imagino a nadie con la que me importase menos compartirlo que contigo..."
            eil "*Susurrando* Se ha roto."
    scene c14s006_350d with dissolve
    emm "Bueno, vamos a la gasolinera. A ver si somos capaces de sacarle información a las chicas sobre lo que ha pasado en el Verdad o Reto."
    mc "[emm]..."
    eri "Lo que pasa en Las Vegas se queda en Las Vegas, [emm]."
    eil "Y no digas que ha pasado en Newport. Ya sabes lo que significa el dicho."
    call BlinkXP ("c14s006_350" , "d") from _call_BlinkXP_902
    emm "Significa que no tengo que preguntar, pero seguro que hay alguna que no es tan buena guardando secretos como yo."
    todas "*Risa*"
    if emm._var("route"):
        call KissXP ("c14s006_355" , "d") from _call_KissXP_18
        emm "Te quiero. Mola salir a la luz. Lo tenemos que hacer con toda la familia."
        mc "Yo también te quiero."
    if eri._var("route") and emm._var("route"):
        call KissXP ("c14s006_360" , "d") from _call_KissXP_19
        eri "Nos vemos ahora, mi amor."
        mc "Os espero en las sombrillas, mi vida."
    if eil._var("route") and emm._var("route"):
        call KissXP ("c14s006_365" , "d") from _call_KissXP_20
        eil "Recuerda a quien le diste el título de primera concubina. Te quiero."
        mc "Yo más. Y no lo olvidaré nunca."
        scene c14s006_350e with fade #de espaldas yéndose
        emm "¿Qué es eso del título de primera concubina?"
        eil "Nada, una tontería. Sabes qué es una concubina, ¿no?"
        eri "Y sabes que cuando un hombre tiene varias mujeres se llama harén, ¿verdad?"
        emm "Emmm... claro que lo sé... no soy tonta..."
    scene black with dissolve
    stop music fadeout (1.5)
    "Vuelves hacia las sombrillas y te das cuenta de que ha llegado más gente en el rato que has estado fuera."
    play music ("music/Beach.ogg")
    if sam._var("route") and not sim._var("route"):
        scene c14s006_370d with dissolve:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXP ("c14s006_370" , "d") from _call_BlinkXP_903
        mc "Hola, [sim], que bien que hayáis llegado."
        sim "[mc]..."
    else:
        scene c14s006_370bd with dissolve:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXP ("c14s006_370b" , "d") from _call_BlinkXP_904
        mc "Hola, [sim], que bien que hayáis llegado."
        sim "[mc], sí, hemos tardado más porque mi madre no encontraba el pareo. Hace siglos que no venimos a la playa."
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ sim.profileImages.pop (2) # first remove
        $ sim.profileImages.insert (2, ("simone_2", None)) # then add new
    scene c14s006_375d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ sam.profileImages.pop (2) # first remove
        $ sam.profileImages.insert (2, ("samantha_2", None)) # then add new
    call BlinkXP ("c14s006_375" , "d") from _call_BlinkXP_905
    mc "[sam.nick], estás preciosa de rojo."
    sam "Gracias. Ha sido una buena idea. Al menos hacemos algo diferente."
    if sim._var("route") or sam._var("route"):
        play music ("music/Tribal.ogg")
    if sim._var("route"):
        call BlinkXP ("c14s006_380" , "d") from _call_BlinkXP_906
        sim "Por cierto, hay algo que quiero hacer."
        mc "Si quieres, por mí ningún problema."
        scene c14s006_385AnBlink with dissolve #380a-385d(beso)-e(Martha sorprendida)-f(Norah sorprendida)-g(Kiara sorprendida)-h(Meemaw contenta)-i(Betty contenta)-d(beso)-385Blink
        "La seguridad que le da a [sim] que su madre ya sepa lo vuestro se nota en sus labios."
        call BlinkXP ("c14s006_385" , "d") from _call_BlinkXP_907
        sim "*Susurrando* ¡Mielda! He cerrado los ojos y no he mirado si alguna se ha enfadado."
        mc "*Susurrando* Más que enfadadas, sorprendidas."
    if sam._var("route"):
        call BlinkXP ("c14s006_390" , "d") from _call_BlinkXP_908
        if sim._var("route"):
            sam "*Susurrando* Creo que es mi turno. Si a alguien le da un infarto, tengo el desfibrilador en el coche."
        else:
            sam "*Susurrando* Voy a hacer algo. Si a alguien le da un infarto, tengo el desfibrilador en el coche."
        mc "*Susurrando* Adelante. Soy tuyo para hacer lo que quieras."
        sam "*Susurrando* Lo que quiera no, pero esto sí."
        scene c14s006_395AnBlink with dissolve #390a-395d(beso)-385e(Martha sorprendida)-385f(Norah sorprendida)-385g(Kiara sorprendida)-395h(Meemaw sorprendida)-395i(Betty sorprendida)-d(beso)-395Blink
        "Besar a [sam] delante de todo el mundo tiene algo especial."
        call BlinkXP ("c14s006_395" , "d") from _call_BlinkXP_909
        sam "*Susurrando* ¿Ha pasado algo? Me da miedo mirar..."
        mc "*Susurrando* Ningún infarto de momento."
    if sam._var("route") or sim._var("route"):
        call BlinkXP ("c14s006_400" , "d") from _call_BlinkXP_910
        mee "No sabía que lo de saludar con un beso también lo hacías fuera de la familia, [mc]."
        call BlinkXP ("c14s006_405" , "d") from _call_BlinkXP_911
        nor "No, Mamá, creo que no lo estás pillando..."
        if nor._var("route"):
            call BlinkXP ("c14s006_410" , "d") from _call_BlinkXP_912
            nor "Es tan buen momento como cualquier otro, ¿no?"
            mc "Siempre es buen momento para lo que vas a hacer, cielo."
            scene c14s006_415AnBlink with dissolve #410a-415d(beso)-385e(Martha sorprendida)-385g(Kiara sorprendida)-395h(Meemaw sorprendida)-395i(Betty sorprendida)-415j(Sam sorprendida)-415k(Simone sorprendida)-d(beso)
            "El mundo desaparece a vuestro alrededor. Da lo mismo quién esté ahí, qué caras pongan, o qué piensen de vuestro beso."
            call BlinkXP ("c14s006_415" , "d") from _call_BlinkXP_913
            nor "*Susurrando* Si me desheredan será culpa tuya. *Risa*"
            mc "*Susurrando* Pero ¿ha valido la pena?"
            nor "*Susurrando* Por supuesto. Solo espero que a mi madre no le de un infarto. *Risa*"
            mc "*Susurrando* No te preocupes. [sam] siempre lleva un desfibrilador en el coche. *Risa*"
            "En ese momento os dáis cuenta de que se escuchan voces airadas a vuestro alrededor."
            call BlinkXP ("c14s006_420" , "d") from _call_BlinkXP_914
            mee "... es tu sobrino! ¿Cómo puedes hacer algo así? Además le doblas la edad..."
            call BlinkXP ("c14s006_425" , "d") from _call_BlinkXP_915
            nor "Mamá, tú siempre has dicho una frase que me ha gustado. No eliges de quién te enamoras. Yo no elegí a [mc], pero me enamoré de él."
            if sam._var("route") and sim._var("route"):
                mc "Meemaw, nos queremos. Igual que quiero a [sam] y a [sim]..."
            elif sam._var("route"):
                mc "Meemaw, nos queremos. Igual que quiero a [sam]..."
            else:
                mc "Meemaw, nos queremos. Igual que quiero a [sim]..."
            if mar._var("route"):
                call BlinkXP ("c14s006_430" , "d") from _call_BlinkXP_916
                if persistent.family:
                    mom "Igual que me quiere a mí, Mamá. No quería que te enterases así, pero..."
                    call BlinkXP ("c14s006_435" , "h") from _call_BlinkXP_917
                    mee "No, ¡tú no! ¡Es tu hijo!"
                else:
                    mom "Igual que me quiere a mí, Olivia. No quería que te enterases así, pero..."
                    call BlinkXP ("c14s006_435" , "h") from _call_BlinkXP_918
                    mee "No, ¡tú no! ¡Lo has criado como a tu hijo!"
                call c14s006_KissMartha from _call_c14s006_KissMartha
        elif mar._var("route"):
            call BlinkXP ("c14s006_430" , "d") from _call_BlinkXP_919
            if persistent.family:
                mom "Desde luego que no lo estás pillando, Mamá. No quería que te enterases así, pero..."
                call BlinkXP ("c14s006_435" , "h") from _call_BlinkXP_920
                mee "No, ¡tú no! ¡Es tu hijo!"
            else:
                mom "Desde luego que no lo estás pillando, Olivia. No quería que te enterases así, pero..."
                call BlinkXP ("c14s006_435" , "h") from _call_BlinkXP_921
                mee "No, ¡tú no! ¡Lo has criado como a tu hijo!"
            call c14s006_KissMartha from _call_c14s006_KissMartha_1
        elif sam._var("route") and sim._var("route"):
            call BlinkXP ("c14s006_450" , "h") from _call_BlinkXP_922
            mee "¿Estáis todos locos? ¿Sabéis lo que estáis haciendo? ¿Con una madre y su hija?"
        elif sam._var("route"):
            call BlinkXP ("c14s006_450" , "h") from _call_BlinkXP_923
            mee "¿Estáis locos? ¿Sabéis lo que estáis haciendo? ¿Con una mujer que te dobla la edad?"
        if not nor._var("route") and not mar._var("route"):
            scene c14s006_455a with dissolve #Sam-MC-Simone
            if not sim._var("route"):
                sam "[mc] está saliendo conmigo, Olivia." (multiple=2)
                sim "Y yo apoyo a mi madre." (multiple=2)
            elif not sam._var("route"):
                sim "[mc] está saliendo conmigo, Olivia." (multiple=2)
                sam "Y yo apoyo a mi hija." (multiple=2)
            else:
                sam "[mc] está saliendo con las dos, Olivia." (multiple=2)
                sim "Y las dos lo aceptamos." (multiple=2)
        elif mar._var("route") and not nor._var("route"):
            if not sim._var("route"):
                scene c14s006_455c with dissolve #sim-sam-mc-mar
                mom "Sí, estoy saliendo con [mc]."
                sam "[mc] también está saliendo conmigo, Olivia." (multiple=2)
                sim "Y yo apoyo a mi madre." (multiple=2)
            elif not sam._var("route"):
                scene c14s006_455b with dissolve #sam-sim-mc-mar
                mom "Sí, estoy saliendo con [mc]."
                sim "[mc] también está saliendo conmigo, Olivia." (multiple=2)
                sam "Y yo apoyo a mi hija." (multiple=2)
            else:
                scene c14s006_455c with dissolve #sim-sam-mc-mar
                mom "Sí, estoy saliendo con [mc]."
                sam "[mc] está saliendo con las dos, Olivia." (multiple=2)
                sim "Y las dos lo aceptamos." (multiple=2)
        elif not mar._var("route") and nor._var("route"):
            if not sim._var("route"):
                scene c14s006_455e with dissolve #sim-sam-mc-nor
                nor "Sí, estoy saliendo con [mc]."
                sam "[mc] también está saliendo conmigo, Olivia." (multiple=2)
                sim "Y yo apoyo a mi madre." (multiple=2)
            elif not sam._var("route"):
                scene c14s006_455d with dissolve #sam-sim-mc-nor
                nor "Sí, estoy saliendo con [mc]."
                sim "[mc] también está saliendo conmigo, Olivia." (multiple=2)
                sam "Y yo apoyo a mi hija." (multiple=2)
            else:
                scene c14s006_455e with dissolve #sim-sam-mc-nor
                nor "Sí, estoy saliendo con [mc]."
                sam "[mc] está saliendo con las dos, Olivia." (multiple=2)
                sim "Y las dos lo aceptamos." (multiple=2)
        elif mar._var("route") and nor._var("route"):
            if not sim._var("route"):
                scene c14s006_455g with dissolve #sim-sam-mc-mar-nor
                mom "Sí, estoy saliendo con [mc]." (multiple=2)
                nor "Y yo también, Mamá." (multiple=2)
                sam "[mc] también está saliendo conmigo, Olivia." (multiple=2)
                sim "Y yo apoyo a mi madre." (multiple=2)
            elif not sam._var("route"):
                scene c14s006_455f with dissolve #sam-sim-mc-mar-nor
                mom "Sí, estoy saliendo con [mc]." (multiple=2)
                nor "Y yo también, Mamá." (multiple=2)
                sim "[mc] también está saliendo conmigo, Olivia." (multiple=2)
                sam "Y yo apoyo a mi hija." (multiple=2)
            else:
                scene c14s006_455g with dissolve #sim-sam-mc-mar-nor
                mom "Sí, estoy saliendo con [mc]." (multiple=2)
                nor "Y yo también, Mamá." (multiple=2)
                sim "[mc] está saliendo con las dos, Olivia." (multiple=2)
                sam "Y las dos lo aceptamos." (multiple=2)
        mc "Y no tenemos por qué defender nuestra relación delante de nadie, Meemaw. Ni necesitamos la autorización de nadie."
        call BlinkXP ("c14s006_460" , "d") from _call_BlinkXP_924
        bet "*Risa* Sigue así, hermanita. Si sigues protestando, los vas a unir más todavía."
        if sam._var("route") or nor._var("route") or mar._var("route"):
            call BlinkXP ("c14s006_465" , "d") from _call_BlinkXP_925
            mee "¿Tú no ves que sea una locura?"
            call BlinkXP ("c14s006_470" , "d") from _call_BlinkXP_926
            bet "Claro que sí. Igual de locura que nuestros padres vieron que te casaras con John. Y eso os unió aún más."
            call BlinkXP ("c14s006_475" , "d") from _call_BlinkXP_927
            mee "¡Pero eso es porque eran unos clasistas y John estaba sin blanca! ¿Tú ves esto normal?"
            if nor._var("route") or mar._var("route"):
                mee "¡Son familia, por el amor de Dios!"
            else:
                mee "¡La diferencia de edad es enorme!"
            call BlinkXP ("c14s006_480" , "d") from _call_BlinkXP_928
            bet "Y cuantos más impedimentos pongas, más fuerte se va a hacer su relación. ¿No lo puedes ver?"
            bet "En África he visto relaciones de todo tipo. Las que tú consideras normales y las que no. De los dos tipos han funcionado y de los dos tipos se han roto."
            bet "Esto parece especial, ¿no?"
            call BlinkXP ("c14s006_485" , "d") from _call_BlinkXP_929
            mee "*Gruñido* Especial es una forma suave de llamarlo."
            call BlinkXP ("c14s006_490" , "d") from _call_BlinkXP_930
            bet "Y nuestro [mc] también es especial, ¿no?"
            call BlinkXP ("c14s006_485" , "d") from _call_BlinkXP_931
            mee "*Gruñido* Sí, ya se ve que es especial."
            call BlinkXP ("c14s006_490" , "d") from _call_BlinkXP_932
            bet "¿Por qué no le das un voto de confianza a ver que sale de esta relación?"
            call BlinkXP ("c14s006_485" , "d") from _call_BlinkXP_933
            mee "*Gruñido* ¡Qué fácil es para ti decirlo!"
            call BlinkXP ("c14s006_495" , "d") from _call_BlinkXP_934
            kia "Sé que me voy a meter en un asunto familiar en el que no pinto nada, pero escuchadme un momento, por favor."
            kia "Cuando [mc] empezó a salir con mi [eil], no veía ningún futuro a esa relación. Me parecía que [mc] no era lo suficientemente bueno para mi hija."
            call BlinkXP ("c14s006_500" , "d") from _call_BlinkXP_935
            mee "¿Qué? ¿Estás diciendo que mi nieto no era lo suficientemente bueno?"
            call BlinkXP ("c14s006_490b" , "d") from _call_BlinkXP_936
            bet "Déjala acabar, por Dios, Olivia."
            call BlinkXP ("c14s006_495" , "d") from _call_BlinkXP_937
            kia "Gracias, Betty."
            kia "Si me hubiera opuesto a su relación, la hubiera hecho más fuerte artificialmente. Y el tiempo me demostró que estaba equivocada."
            kia "Si hay alguien capaz de sacar adelante esta relación, por diferente que sea, es [mc]."
            mc "Gracias, Kiara."
            mc "Por cierto, las chicas no saben nada y solo es decisión nuestra cuándo y dónde decírselo, con lo que cuento con vuestra discrección."
            scene c14s006_505a with dissolve
            kia "Ningún problema. Estoy totalmente de acuerdo y es un asunto vuestro."
            mee "*Gruñido* Vale."
            bet "Es lo lógico. La noticia puede caer como una bomba."
            scene c14s006_505b with dissolve
            mc "Perfecto, porque por allí vienen con el hielo. Espero que tengamos la fiesta en paz y no le amargues la Navidad a nadie, Meemaw."
            call BlinkXP ("c14s006_510" , "d") from _call_BlinkXP_938
            mee "*Gruñido* Vale. Pero tú y yo vamos a tener que hablar cuando lleguemos a casa."
        else:
            call BlinkXP ("c14s006_515" , "d") from _call_BlinkXP_939
            mee "No estoy protestando. Tan solo creía que era una cosa que hacía dentro de la familia."
            scene c14s006_505b with dissolve
            mc "Por allí vienen las chicas con el hielo."
        stop music fadeout (1.5)
    else:
        scene c14s006_505b with dissolve
        mc "Por allí vienen las chicas con el hielo."
    play music ("music/Beach.ogg")
    mc "Ya solo faltan por llegar Alexia y [sai], y podremos ir a comer."
    scene black with dissolve
    "Mientras esperáis a Alexia y [sai], se van formando grupitos de conversación."
    scene c14s006_510d with dissolve
    if sam._var("route") or sim._var("route"):
        "[mar] y [nor] se apartan para discutir lo que acaba de pasar tras lanzarte una mirada indicándote que no te acerques."
    else:
        "[mar] y [nor] se apartan para charlar después de indicarte con una mirada que no te acerques."
    scene c14s006_510e with fade
    if sam._var("route"):
        "[sam] y Kiara empiezan a charlar. Supones por los gestos que la conversación va tanto sobre el brazo como sobre el beso."
        "Tienes que darle las gracias a Kiara en algún momento, pero prefieres no acercarte."
    else:
        "[sam] y Kiara empiezan a charlar sobre el brazo."
    scene c14s006_515f with fade
    "[dap] y [sca] han secuestrado a [sim] y ha empezado a presentarles a las chicas. Hasta ahora solo conocía a Debbie."
    scene c14s006_515d with fade
    "[emm] y [eil] se quedan apartadas. Parece que tienen cosas que decirse."
    if emm._var("route"):
        "Tan solo esperas que a [emm] no se le escapen más secretos de los necesarios."
    scene c14s006_515e with fade
    stop music fadeout (1.5)
    "[eri] acude a hacer compañía a Meemaw y Betty, que parecían a punto de tener una discusión."
    play music ("music/Dark-Score.ogg")
    scene c14s006_520d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ sai.profileImages.pop (2) # first remove
        $ sai.profileImages.insert (2, ("saira_2", None)) # then add new
    call BlinkXP ("c14s006_520" , "d") from _call_BlinkXP_940
    "A lo lejos ves aparecer a [sai]. Parece que se ha cambiado nada más bajar del taxi que la ha traído de la universidad."
    scene c14s006_525An
    "[emm] te hace señas para que te acerques mientras llama a [sai]."
    emm "¡[sai]! Ven aquí, quiero presentarte a alguien."
    call BlinkXP ("c14s006_530" , "d") from _call_BlinkXP_941
    sai "Hola, [emm]. Gracias por mandarme la ubicación. Como Lisa se ha ido antes, no sabía donde era."
    if emm._var("route"):
        call BlinkXP ("c14s006_535" , "d") from _call_BlinkXP_942
        emm "No pasa nada, lo mejor para nuestras clientas, ¿no?"
    else:
        call BlinkXP ("c14s006_540" , "d") from _call_BlinkXP_943
        emm "No pasa nada, para eso estamos las amigas, ¿no?"
    emm "Por cierto, te presento a [eil]. [eil], esta es [sai]."
    call BlinkXP ("c14s006_545" , "d") from _call_BlinkXP_944
    if eil._var("route"):
        sai "Así que tú eres la famosa [eil], con la que {b}rompió{/b} antes de estar conmigo, ¿no? Encantada. de. conocerte."
    else:
        sai "Así que tú eres la famosa [eil], la {b}ex-novia{/b} del instituto, ¿no? Encantada. de. conocerte."
    call BlinkXP ("c14s006_550" , "d") from _call_BlinkXP_945
    eil "Y tú eres la ex-novia de Portland... Ah, no, perdona... la {b}follamiga{/b} de Portland. No sé si puedo decir lo mismo sobre conocerte."
    call BlinkXP ("c14s006_555" , "d") from _call_BlinkXP_946
    emm "Bueno, os dejo aquí a los tres para que os pongáis al día. Voy a hablar con la abuela antes de que muerda a Tía Betty."
    mc "*Susurrando* Sabes que la puedes haber liado, ¿no?"
    emm "Tarde o temprano se tenían que conocer. Las dos viven en casa... Suerte con las fieras. *Risa*"
    scene c14s006_560a with dissolve
    sai "Me alegra conocerte por fin. Solo había visto fotos tuyas. Estabas mejor en las fotos."
    eil "Bueno, al menos de mí estaba lo suficientemente orgulloso como para enseñar fotos. Yo no sabía el aspecto que tenías. No me sorprende."
    mc "Chicas..."
    scene c14s006_565b with dissolve
    sai "Bueno, a lo mejor no quería enseñarte fotos mías para que no te sintieras mal."
    eil "O es posible que sea por que se avergonzaba de haber salido... perdón, haberse acostado contigo."
    mc "Chicas, dejadlo ya, por favor."
    scene c14s006_565c with dissolve
    sai "Al menos yo no me lié con nadie una vez lo dejamos, putón."
    eil "¿Quién coño querría liarse contigo? Si le tuviste que dejar la puerta abierta a que se liara con otras... Fea."
    scene c14s006_565d with dissolve
    sai "¿Ya se ha ido?" (multiple=2)
    eil "¿No nos ve?" (multiple=2)
    mc "¿Qué? ¿Quién?"
    stop music fadeout (1.5)
    sai "Tu hermana." (multiple=2)
    eil "[emm]." (multiple=2)
    mc "Sí... ya se ha ido. ¿Por qué?"
    play music ("music/SaveMe.ogg")
    call BlinkXP ("c14s006_570" , "h") from _call_BlinkXP_947
    eil "¿Qué tal el primer día de clase?"
    sai "Muy pesado, pero por fin ha acabado y me puedo relajar con vosotras."
    mc "¿Qué? ¿Qué está pasando aquí? No entiendo nada."
    scene c14s006_575a with dissolve
    eil "[sai] y yo nos conocimos anoche, nos presentó [eri]."
    sai "Estaba en la piscina tomando el aire después de cenar. Tenía que digerir la conversación contigo. Entonces llegaron las dos."
    scene c14s006_575b with dissolve
    eil "Digamos que la conversación empezó más o menos como la de ahora, pero [eri] puso paz."
    sai "Bueno, fue un poco más suave..."
    scene c14s006_575c with dissolve
    eil "Sí, te has pasado con lo de putón. Además tú eso no lo debías saber... y solo fueron un par de citas, no me acosté con nadie."
    sai "¿Y lo de llamarme fea? ¿Tenemos 10 años, [eil]? *Risa*"
    mc "Estoy flipando..."
    call BlinkXP ("c14s006_580" , "d") from _call_BlinkXP_948
    eil "[eri] nos dijo que no nos sorprendiéramos si [emm] intentaba enfrentarnos hoy de alguna forma."
    if emm._var("route"):
        eil "{i}(Y ahora que sé que está contigo, la entiendo perfectamente. Si peleábamos delante tuyo nos ridiculizaríamos a nosotras mismas.){/i}"
    eil "Supongo que tener a dos ex-novias en la misma comida navideña podía ser un riesgo."
    scene c14s006_585d with dissolve
    sai "¿Ya no soy la follamiga? *Risa* ¿He ascendido a ex-novia?"
    call BlinkXP ("c14s006_585" , "d") from _call_BlinkXP_949
    sai "Después de lo que dijo [eri], [eil] y yo estuvimos hablando largo y tendido."
    if eil._var("route"):
        sai "Tú me habías dicho que estabas con [eil]. Era raro estar hablando con ella en la piscina, después de un mes comiéndome la cabeza."
    else:
        sai "Tú me habías dicho que no habías vuelto con [eil], pero era raro estar hablando con ella en la piscina después de un mes comiéndome la cabeza."
    call BlinkXP ("c14s006_590" , "d") from _call_BlinkXP_950
    eil "Empezamos como dos perras celosas, especialmente [sai], y acabamos contándonos los mejores momentos que hemos pasado contigo."
    if eil._var("route") and sai._var("route"):
        eil "Parece que vuelves a estar con las dos... sí, a [sai] se le escapó. Haces bien, [sai] será una buena incorporación al harén."
    elif eil._var("route") and not sai._var("route"):
        eil "Parece que vuestro reencuentro fue más frío que el nuestro, pero deberías pensártelo. [sai] sería una buena incorporación al harén."
    elif not eil._var("route") and sai._var("route"):
        eil "Parece que vuestro reencuentro no fue tan frío como el nuestro... sí, a [sai] se le escapó. Haces bien, [sai] será una buena incorporación al harén."
    elif not eil._var("route") and not sai._var("route"):
        eil "Parece que nuestros reencuentros contigo fueron igual de frío, pero deberías pensártelo. [sai] sería una buena incorporación al harén."
    mc "¿Qué? ¿Le has dicho lo del harén?"
    if sai._var("route") and mc._var("relationships")==1:
        mc "No hay harén, solo estoy saliendo con [sai]."
    elif not sai._var("route") and mc._var("relationships")==1:
        if eil._var("route"):
            mc "No hay harén, solo estoy saliendo contigo."
        else:
            mc "No hay harén, solo estoy saliendo con una chica."
    call BlinkXP ("c14s006_595" , "d") from _call_BlinkXP_951
    sai "Después de hablar bastante rato..."
    if eil._var("route") and sai._var("route"):
        sai "Nos dimos cuenta de que si estás con las dos es porque te metimos en la cabeza la relación abierta y el haren."
    elif eil._var("route") and not sai._var("route"):
        sai "Nos dimos cuenta de que si estás con [eil] y yo puedo tener una oportunidad, es porque te metimos en la cabeza la relación abierta y el haren."
    elif not eil._var("route"):
        if sai._var("route"):
            sai "Me dí cuenta que [eil] proponiendote el harén, quizá me haya dado la oportunidad que necesitaba para volver contigo."
        else:
            sai "Me dí cuenta que [eil] proponiendote el harén, quizá me de la oportunidad que necesitaba para volver contigo en el futuro."
    scene c14s006_600a with dissolve
    sai "Después nos pasamos un rato riendo." (multiple=2)
    eil "Y comparando notas. *Risa*" (multiple=2)
    sai "Descubrimos que no somos rivales." (multiple=2)
    eil "Y decidimos hacernos amigas." (multiple=2)
    scene c14s006_600b with dissolve
    eil "[sai] no podía creerse que [emm] fuera a intentar algo como lo que ha hecho, pero yo la conozco mejor."
    if emm._var("route"):
        sai "Traté poco con ella ayer, parecía enfadada, pero creía que tenía que ver con la situación de [sca]."
    else:
        sai "Traté poco con ella ayer, parecía una chica muy agradable."
    mc "Es muy agradable... cuando quiere. Supongo que querrá después de que le de unos azotes. *Risa*"
    scene c14s006_600c with dissolve
    eil "Déjale creer que nos hemos peleado. Será una pequeña victoria en su cabeza."
    sai "Y nos dará tiempo de planear nuestra venganza. *Risa*"
    stop music fadeout (1.5)
    mc "Haced que parezca un accidente. Por allí viene la última invitada y sospecharía enseguida de vosotras."
    play music ("music/Salsa.ogg")
    scene c14s006_605d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ renpy.notify ("Profile image unlocked")
        $ oma.profileImages.pop (2) # first remove
        $ oma.profileImages.insert (2, ("alexia_2", None)) # then add new
    call BlinkXP ("c14s006_605" , "d") from _call_BlinkXP_952
    mc "Alexia, ven. Quiero presentarte a alguien."
    mc "Alexia, [sai]. [sai], Alexia."
    scene c14s006_605e with dissolve
    oma "Encantada de conocerte, [sai]. ¿Eres la última estudiante?"
    sai "Sí, llegué ayer. ¿Eres amiga de la familia?"
    oma "Más o menos. He tenido que ayudar a [mc] en algunas cosas."
    oma "Hola, [eil]. Tenemos que hablar."
    call BlinkXP ("c14s006_610" , "d") from _call_BlinkXP_953
    mc "¿Qué tal el viaje, Alexia?"
    oma "Muy pesado, pero al menos ya estoy aquí."
    oma "Me tienes que contar qué querías el lunes cuando me llamaste."
    mc "Te tengo que contar muchas cosas, Alexia, pero habrá tiempo."
    mc "Creo que te estaban esperando para comer. A estas alturas Tía Betty se tiene que estar muriendo de hambre."
    stop music fadeout (1.5)
    scene black with dissolve
    "Recogéis las sombrillas y las sillas y os dirigís al merendero."
    play music ("music/jingle-bells-orchestra.ogg")
    "[emm] y [sca] reparten gorros navideños para todos."
    scene c14s006_615a with dissolve #deb-eri-sam-bet
    "Después de lo que ha pasado durante la mañana, no te extraña que los grupos se entremezclen."
    scene c14s006_615b with dissolve #kim-ale-dap-mar
    "No parece haber diferencia entre familia, estudiantes, y las chicas de la ciudad."
    scene c14s006_615c with dissolve #sai-sim-mee-sca
    "Todo el mundo parece dispuesto a pasárselo bien y disfrutar de la comida."
    scene c14s006_615d with dissolve #kat-eil-nor
    "Algunos gorros duran poco en las cabezas y acaban encima de la mesa. Hace demasiado calor para llevarlos en pleno verano."
    scene c14s006_615e with dissolve #lis-kia-emm
    "Es vuestra primera Navidad juntos. ¿Quién sabe cómo será la próxima, la de verdad?"
    if meg._var("route") and mad._var("route"):
        scene c14s006_615f with fade #megan,maddie,eva y amanda
    elif meg._var("route"):
        scene c14s006_615g with fade #megan,eva y amanda
    elif mad._var("route"):
        scene c14s006_615h with fade #maddie,eva y amanda
    else:
        scene c14s006_615i with fade #eva y amanda
    "Hay más gente que te gustaría que estuviera aquí. Y todavía faltan por llegar las últimas estudiantes. En la Navidad de verdad estarán."
    "¿Pero habrá vuelto Meemaw a Florida por entonces? ¿Tía Betty estará en algún hospital de África?"
    call BlinkXP ("c14s006_620" , "f") from _call_BlinkXP_954
    "La sonrisa de [sca] te saca de tus ensoñaciones."
    sca "¿Pasa algo, [mc]? Te veo ausente..."
    mc "No, cielo, no pasa nada. Solo estaba pensando en la próxima Navidad, la de verdad."
    scene c14s006_625AnBlink with dissolve #AN se quita el gorro
    sca "La verdad es que ésta ha salido un poco sosa, ¿cierto? Al final es un día de playa comiendo con ridículos gorros navideños."
    mc "¡Hey! No es nada sosa. No había visto nunca a 19 personas pasándoselo bien juntos sin malos rollos. Y menos habiendo familia en la mezcla."
    call BlinkXP ("c14s006_630" , "d") from _call_BlinkXP_955
    sca "La verdad es que tienes una familia increíble. Gracias por acogerme, [mc]. A [nor], a [mar] y a las chicas las he inundado de gracias, pero si no hubiera sido por ti..."
    mc "No hace falta que des las gracias. Y te equivocas en una cosa, no tengo una familia increíble. La tenemos. Tú, yo, las chicas..."
    mc "Mira lo que has conseguido que hagamos y dime que no parecemos una gran familia."
    sca "*Risa* Nada que ver con mi concepto de familia. No hay nadie discutiendo. Me podría acostumbrar a esto."
    mc "Lo harás. No pensamos dejarte escapar. *Risa*"
    call BlinkXP ("c14s006_640" , "d") from _call_BlinkXP_956
    sca "¡Vamos a hacernos una foto juntos!"
    mc "¿Una selfie?"
    sca "No, tonto, una foto de toda la familia junta."
    mc "¡Vamos!"
    scene black with dissolve
    "[sca] propone la foto y todo el mundo responde entusiasmado."
    scene c14s006_645An with dissolve #AN aba color/bn/color
    todas "¡Feliz Navidad!"
    "Con el paso del tiempo, los que salís en la foto consideraréis ese momento como el pistoletazo de salida para vuestra familia."
    "Las chicas que se unirán a la familia en los próximos meses mirarán la foto deseando haber estado allí, haber formado parte de la familia desde el primer día."
    "Nadie lo sabe en ese momento, pero esa foto acabará en el despacho de la primera Gobernadora de California muchos años después."
    "Y más años después todavía, estará encima del escritorio Resolute, en el despacho Oval. Pero esa es otra historia."
    scene black with dissolve
    "Después de la foto todo el mundo sigue con sus conversaciones. Si la conversación era animada antes, ahora lo es incluso más."
    call BlinkXP ("c14s006_650" , "d") from _call_BlinkXP_957
    dap "Nos deberiamos ir yendo, [mc]."
    mc "¿A dónde?"
    call BlinkXP ("c14s006_655" , "d") from _call_BlinkXP_958
    dap "No te acuerdas, ¿verdad? Tenemos que ir a la tienda de Maddie para hacer vuestros personajes de DnD."
    mc "Pues no, no me acordaba para nada."
    mc "Vamos a despedirnos de todo el mundo, cogemos unos gorros, y vamos para allí. Voy a ver si queda alguna botella de cava."
    call BlinkXP ("c14s006_660" , "d") from _call_BlinkXP_959
    dap "¿Cava? ¿Gorros?"
    mc "No querrás dejar a Maddie sin celebrar la Navidad, ¿verdad? *Risa*"
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c14s006_KissMartha:
    call BlinkXP ("c14s006_440" , "d") from _call_BlinkXP_960
    mom "¿Te importa?"
    mc "No, hace tiempo que lo estaba deseando."
    scene c14s006_445AnBlink with dissolve #440a-445d(beso)-445f(Norah sorprendida)-385g(Kiara sorprendida)-395h(Meemaw sorprendida)-395i(Betty sorprendida)-415j(Sam sorprendida)-415k(Simone sorprendida)-d(beso)-445Blink
    if nor._var("route"):
        "Tal como ha pasado con [nor], el mundo vuelve a desaparecer. Sabes que la voz de Meemaw está subiendo de tono, pero decides no escucharla."
    else:
        "El mundo desaparece a vuestro alrededor. Sabes que la voz de Meemaw está subiendo de tono, pero decides no escucharla."
    call BlinkXP ("c14s006_445" , "d") from _call_BlinkXP_961
    mom "No sabes que peso de encima me he quitado."
    mc "Lo sé. Salir a la luz es una sensación increíble."
    mom "Ahora viene el problema. ¿Nos giramos y las escuchamos?"
    call BlinkXP ("c14s006_450" , "h") from _call_BlinkXP_962
    mee "¿Estáis todos locos? ¿Sabéis lo que estáis haciendo?"
    return
label c14s007_MaddieDnD:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_20
        call mrS3_mad_route from _call_mrS3_mad_route_15
        if mad._var("route"):
            call mrS3_mad_type from _call_mrS3_mad_type
    "Llegáis a la tienda de ropa y Maddie está sola, no hay ningún cliente."
    play music ("music/Acoustic-Inspirational.ogg")
    call BlinkXP ("c14s007_005" , "d") from _call_BlinkXP_963
    mad "Buenas tardes, [dap]. [mc]."
    mc "Hola, Maddie. ¿No tienes clientes hoy?"
    mad "No suele haber clientes a esta hora en los días laborables. Un poco más tarde quizás."
    call BlinkXP ("c14s007_010" , "d") from _call_BlinkXP_964
    dap "Entonces genial. Podemos hacer vuestros personajes sin interrupción."
    mc "Pero antes vamos a brindar, ¿no?"
    call BlinkXP ("c14s007_015" , "d") from _call_BlinkXP_965
    mad "¿Brindar? ¿Por qué?"
    mc "Hemos celebrado una fiesta navideña en la playa y te hemos traído un poco de cava... sin alcohol, que tú estás trabajando y yo tengo que conducir luego."
    mad "¿Navidad? ¿En Julio? ¿Para eso queríais los gorros de Santa ayer?"
    call BlinkXP ("c14s007_020" , "d") from _call_BlinkXP_966
    dap "Sí, por lo visto es una costumbre italiana y [sca], mi amiga, leyo sobre ella. Lo propuso y lo hemos hecho. *Risa*"
    mc "Ha sido divertido. Un dia de playa normal y comida con los gorros. Mucho espíritu navideño sin que nadie discutiera."
    call BlinkXP ("c14s007_025" , "d") from _call_BlinkXP_967
    dap "Y sin regalos..."
    mc "¿Quieres un regalo? Estás en una tienda de ropa... corre de mi cuenta. *Risa*"
    call BlinkXP ("c14s007_030" , "d") from _call_BlinkXP_968
    mad "Estáis locos, pero trae ese champagne. *Risa*"
    mc "Es cava..."
    mad "Bueno, lo que sea. *Risa*"
    scene c14s007_035 with dissolve
    mc "Feliz Navidad, Maddie."
    dap "¡Feliz Navidad!" (multiple=2)
    mad "¡Feliz Navidad, chicos!" (multiple=2)
    call BlinkXP ("c14s007_040" , "d") from _call_BlinkXP_969
    dap "¿Podemos hacer los personajes ya? He traído la tablet para apuntar los datos. En casa, [emm] hará una ilustración de vuestros personajes y tendréis la hoja de personaje en papel."
    mc "Me vas a tener que explicar como funciona todo."
    dap "Ningún problema. Ya te expliqué el mundo. Ahora te enseñaré las reglas."
    call BlinkXP ("c14s007_045" , "d") from _call_BlinkXP_970
    mad "Deberías explicarme el mundo a mí también."
    mc "Es super original, al menos para alguien que nunca ha jugado a esto."
    menu:
        "Yo quiero volver a escucharla.":
            $ Aux = True
        "Mientras se la explicas, voy al lavabo.":
            $ Aux = False
    if Aux:
        call BlinkXP ("c14s007_050" , "d") from _call_BlinkXP_971
        dap "Imagínate nuestro mundo a finales del Siglo II. El Imperio Romano está en su auge. Entonces se abren una serie de portales a otros mundos y entran los diferentes seres de fantasía."
        dap "Elfos, orcos, enanos, dragones... Pero no solo entran ellos, sino que además sus Dioses les acompañan. Y también la magia."
        call BlinkXP ("c14s007_055" , "d") from _call_BlinkXP_972
        mad "Pobres romanos. Les va a caer la del pulpo."
        mc "Yo pensé lo mismo, pero espera..."
        call BlinkXP ("c14s007_060" , "d") from _call_BlinkXP_973
        dap "Esos pueblos aparecen muy al norte y muy al sur. Elfos, Enanos y Medianos en Escandinavia, los pueblos faericos en las Islas Británicas, y los Orcos y Goblins en Siberia."
        dap "Hay otras razas en otras partes del planeta de las que vuestros personajes no han oído hablar, con lo que no entraré en ello."
        dap "La parte que nos interesa es Europa. La partida se desarrolla en lo que hoy en día es Austria."
        call BlinkXP ("c14s007_065" , "d") from _call_BlinkXP_974
        mad "Déjame adivinar, los pueblos que llegan se pelan a los Germanos y los Alpes se convierten en la frontera."
        call BlinkXP ("c14s007_070" , "d") from _call_BlinkXP_975
        dap "Más o menos. Los Germanos desaparecen, son absorbidos, o se refugian en el Imperio, y los Enanos fundan sus reinos en la cara norte de los Alpes."
        dap "Los elfos atraviesan la Galia y se establecen en lo que sería España, Portugal y el sur de Francia."
        dap "Los romanos no tienen nada que hacer sin magia en ese momento y reciben hostias en todos lados. En menos de un siglo han perdido toda Europa Occidental."
        dap "Pero junto con las razas invasoras también han llegado Dioses que no son adorados por ninguna raza. Esos Dioses se identifican con el Panteón Romano y empiezan a dar poderes a sus sacerdotes."
        call BlinkXP ("c14s007_075" , "d") from _call_BlinkXP_976
        mad "Y eso equilibra la balanza. Las legiones con clérigos curándolas pueden ser un espectáculo."
        mad "¿Qué hay del Cristianismo?"
        call BlinkXP ("c14s007_080" , "d") from _call_BlinkXP_977
        dap "Prácticamente desaparece, igual que el judaísmo. En un mundo con múltiples Dioses dando poderes a sus clérigos, el precepto del único Dios verdadero no se sustenta."
        dap "Y ningún Dios quiere dar poderes a los sacerdotes de esos Dioses. Si lo hacen, estarían negando la existencia de otros Dioses que está muy clara."
        call BlinkXP ("c14s007_085" , "d") from _call_BlinkXP_978
        mad "Me gusta, tiene lógica. Pero aún queda la magia de los magos... Los elfos tienen y los romanos no."
        call BlinkXP ("c14s007_090" , "d") from _call_BlinkXP_979
        dap "Los humanos no somos tontos del todo y en el primer siglo de luchas la gente aprende cómo funciona la magia. Los nuevos Dioses les ayudan a entenderlo."
        call BlinkXP ("c14s007_095" , "d") from _call_BlinkXP_980
        dap "Total que la paz se establece al cabo de un siglo y medio. El norte de los Alpes y de los Cárpatos son los Reinos Enanos."
        dap "España, Portugal y el sur de Francia es territorio elfo. Italia, los Balcanes, Turquía, y toda la costa del Mediterraneo menos lo que tienen los elfos es Romano."
        call BlinkXP ("c14s007_100" , "d") from _call_BlinkXP_981
        dap "Pasan los siglos y los Enanos empiezan a expandirse echando a los Elfos de sus territorios. El Macizo Central de Francia, los Pirineos, y al final toda España."
        dap "En este mundo la enemistad de Elfos y Enanos nace ahí. Los Elfos que quedan tienen que pedir asilo en el Imperio Romano, que se parece más al final de la Edad Media."
        dap "Ahí empieza el equivalente del Renacimiento en este mundo. Algunos siglos antes. En lo que sería nuestro Siglo X, pero sin Cristianismo nadie le llama así."
        call BlinkXP ("c14s007_105" , "d") from _call_BlinkXP_982
        mad "Me gusta. ¿Y qué pasa en Asia? Querría hacerme un personaje que viniera de allí, si es posible."
        call BlinkXP ("c14s007_110" , "d") from _call_BlinkXP_983
        dap "Ningún problema. Los Orcos le han dado de hostias a los Chinos. No hay ningún Dios que les quiera ayudar porque ponen a su Emperador al mismo nivel que los Dioses."
        mc "Creo que yo eso no lo tengo que saber, ¿no? Mientras se lo explicas voy al lavabo. ¿Dónde está, Maddie?"
    call BlinkXP ("c14s007_115" , "d") from _call_BlinkXP_984
    mad "La puerta de la izquierda de los probadores da a un pasillo. Ahí está el lavabo."
    mc "OK, Ahora vuelvo."
    scene c14s007_120 with fade
    "Acabas de lavarte las manos después de hacer eso que solo puedes hacer sentado, cuando..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mad "*A través de la puerta* ¿Te encuentras bien? Ya hemos acabado mi personaje."
    mc "Si, ahora salgo. Habéis sido muy rápidas."
    mad "*A través de la puerta* Con la aplicación que tiene [dap] en la tablet el personaje se hace muy rápido."
    call BlinkXP ("c14s007_125" , "f") from _call_BlinkXP_985
    mc "¿Qué te has hecho?"
    mad "*Risa* Tendrás que esperar a la partida para descubrirlo. Puede ser muy divertido."
    if mad._var("romance"):
        call KissXP ("c14s007_130a" , "d") from _call_KissXP_21
        mad "Tenía ganas de estar a solas contigo. Feliz Navidad."
        mc "Feliz Navidad, preciosa."
        call BlinkXP ("c14s007_135" , "d") from _call_BlinkXP_986
        mad "¿Quieres que volvamos a quedar el viernes en mi casa?"
        mc "Por mí genial. ¿Otra película?"
        call BlinkXP ("c14s007_140" , "d") from _call_BlinkXP_987
        mad "Para no acabar de verla, mejor no empezarla, ¿no?"
        mc "Tienes razón. ¿Te recojo a las 6 como la semana pasada?"
        call BlinkXP ("c14s007_145" , "d") from _call_BlinkXP_988
        mad "Perfecto. A ver si esta vez no te tienes que ir con prisas."
        mc "¡Mierda! Me acabo de acordar que es posible que tenga que recoger a una amiga en Westport el viernes. Pero no sé a que hora, ni siquiera si tendré que ir a buscarla."
        call KissXP ("c14s007_150a" , "d") from _call_KissXP_22
        mad "Lástima. Si no puedes venir a recogerme, podemos quedar directamente en mi casa."
        mc "En cuanto sepa algo te lo digo. Espero poder venir."
    elif mad._var("dom"):
        call KissXP ("c14s007_130b" , "d") from _call_KissXP_23
        mad "Quería hacer esto, pero no quería dejarte en evidencia delante de tu prima. Feliz Navidad, [mc]."
        mc "Feliz Navidad, Ama."
        call BlinkXP ("c14s007_155" , "d") from _call_BlinkXP_989
        mad "Pásame a buscar el viernes a las 6 como la semana pasada e iremos a mi casa."
        mc "Como quieras. ¿Otra película?"
        call BlinkXP ("c14s007_160" , "d") from _call_BlinkXP_990
        mad "Para no acabar de verla, mejor no empezarla. Tengo otros planes para ti."
        mc "Espero que esos planes incluyan hablar de lo nuestro... si quieres."
        call BlinkXP ("c14s007_165" , "d") from _call_BlinkXP_991
        mad "Si te portas bien, sí, podremos hablar. Quedamos a las 6 entonces."
        mc "¡Mierda! Me acabo de acordar que es posible que tenga que recoger a una amiga en Westport el viernes. Pero no sé a que hora, ni siquiera si tendré que ir a buscarla."
        mc "En cuanto sepa algo te lo digo."
        call BlinkXP ("c14s007_170" , "d") from _call_BlinkXP_992
        mad "¿Antepones a una amiga antes que a mí?"
        mc "Antepongo a cualquiera que me necesite antes que cualquier otra cosa. Espero que no te moleste."
        call BlinkXP ("c14s007_175" , "d") from _call_BlinkXP_993
        mad "¿Y si yo te necesitara en ese mismo momento?"
        mc "Si fuera algo que no puede esperar, tendrías preferencia... Ama."
        call KissXP ("c14s007_150b" , "d") from _call_KissXP_24
        mad "Respuesta adecuada."
    elif mad._var("sub"):
        call KissXP ("c14s007_130c" , "d") from _call_KissXP_25
        mc "Tenía ganas de hacer esto desde que he entrado. Feliz Navidad, Maddie"
        mad "Gracias. Feliz Navidad, [mc]."
        mcp "(¿Gracias? ¿Por el beso o por celebrar la Navidad con ella?)"
        call BlinkXP ("c14s007_180" , "d") from _call_BlinkXP_994
        mad "¿Querrías que volvamos a quedar el viernes en mi casa?"
        mc "Sí, podemos ver otra película o continuar donde lo dejamos."
        call BlinkXP ("c14s007_185" , "d") from _call_BlinkXP_995
        mad "Como quieras. Aún tenemos mas de media película por ver. Y mucho que continuar si quieres hacerlo."
        mc "Ya veremos. Te recojeré a las 6 como la semana pasada."
        call BlinkXP ("c14s007_190" , "d") from _call_BlinkXP_996
        mad "Como queras. A ver si esta vez tenemos suerte y no te tienes que ir con prisas."
        mc "¡Mierda! Me acabo de acordar que es posible que tenga que recoger a una amiga en Westport el viernes. Pero no sé a que hora, ni siquiera si tendré que ir a buscarla."
        call KissXP ("c14s007_150c" , "d") from _call_KissXP_26
        mad "Lástima. Si no puedes venir a recogerme, podemos quedar directamente en mi casa."
        mcp "(¿Lástima? ¿Tiene ganas de que vaya? ¿De ser dominada?)"
        mc "En cuanto sepa algo te lo digo."
    if mad._var("route"):
        mad "Si no volvemos ya, [dap] empezará a sospechar."
    else:
        mad "Si has acabado, [dap] te está esperando."
    mc "Entonces vamos, aún tengo que hacer mi personaje."
    call BlinkXP ("c14s007_195" , "d") from _call_BlinkXP_997
    "Ciertamente, con la aplicación diseñáis a Vilfredo il Bisteccone muy rápido."
    "Teniendo en cuenta que te tiene que explicar las normas, tardáis bastante más de lo que ha tardado Maddie, pero menos de lo que hubieras pensado."
    scene c14s007_200a with dissolve
    dap "Bueno, pues ya hemos acabado. El domingo jugaremos la partida. ¡Qué ganas tengo!"
    mad "¿Me mandáis un mensaje con vuestra dirección? No sé dónde vivís."
    mc "No te preocupes, ya te pasaré a buscar."
    scene c14s007_200b with dissolve
    dap "Hasta el domingo, Maddie."
    mad "Nos vemos, [dap]."
    call BlinkXP ("c14s007_005" , "d") from _call_BlinkXP_998
    mad "Avísame cuando vengas a buscarme. Te veo el domingo, [mc]."
    mc "Te llamo cuando esté llegando a tu casa... mándame un mensaje con la dirección."
    if dap._var("route"):
        call BlinkXP ("c14s007_205" , "f") from _call_BlinkXP_999
        "De nuevo en la camioneta..."
        dap "¿Preparado para empezar nuestra cita?"
        mc "¿Sin pasar por casa a ducharnos o cambiarnos?"
        call BlinkXP ("c14s007_210" , "d") from _call_BlinkXP_1000
        dap "No te preocupes. Te podrás duchar y cambiarte donde vamos."
        mc "¿Cambiarme? No he traído ropa..."
        call BlinkXP ("c14s007_215" , "d") from _call_BlinkXP_1001
        dap "No sabes nada, [mc] Marks. Todo está planeado."
    else:
        scene black with dissolve
        "Volvéis a casa y las chicas aún no han llegado. La playa siempre te ha agotado, por mucho que te guste disfrutarla en familia."
        "Después de darte una ducha, el cansancio se apodera de ti y te quedas dormido."
    stop music fadeout (1.5)
    return

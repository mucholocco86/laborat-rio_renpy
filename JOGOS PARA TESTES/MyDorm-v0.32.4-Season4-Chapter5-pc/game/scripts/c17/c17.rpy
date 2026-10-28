label c17:
    call c17s001_AmandaDinner from _call_c17s001_AmandaDinner
    $ Aux = 0
    if mar._var("pregnancyDiscovered"):
        $ Aux = Aux + 1
    if nor._var("pregnancyDiscovered"):
        $ Aux = Aux + 1
    if oma._var("pregnancyDiscovered"):
        $ Aux = Aux + 1
    if eil._var("pregnancyDiscovered"):
        $ Aux = Aux + 1
    $ mc._var("pregnancies", Aux)
    if mad._var("route"):
        call c17s002_MaddieDate from _call_c17s002_MaddieDate
    else:
        call c17s002_MaddieResidence from _call_c17s002_MaddieResidence
    #Saturday
    call c17s003_DapScaTests from _call_c17s003_DapScaTests
    call c17s003_BettyMassage from _call_c17s003_BettyMassage
    if eil._var("pregnancyDiscovered"):
        call c17s003_TellKiara from _call_c17s003_TellKiara
    call c17s003_AmandaLunch from _call_c17s003_AmandaLunch
    if eri._var("route"):
        call c17s003_EriPregnancyResult from _call_c17s003_EriPregnancyResult
    if meg._var("route"):
        call c17s004_MeganLewd from _call_c17s004_MeganLewd #lewd First sex, then test result
    call c17s005_EvaDinner from _call_c17s005_EvaDinner
    return
label c17_updateprofiles:
    python:
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
            while len (characterProfile.profileImages) > 0:
                characterProfile.profileImages.pop (0)
    python:
        for characterProfile in [ bet, dap, deb, eil, emm, eri, kat, kia, kim, lis, mar, mee, nor, sai, sam, sca, sim, oma, eva, ama, mad, meg ]:
            characterProfile.addProfileImage ("00-casual", False)
            characterProfile.addProfileImage ("01-date", False)
            characterProfile.addProfileImage ("02-swimsuit", False)
            characterProfile.addProfileImage ("03-sports", False)
            characterProfile.addProfileImage ("04-work", False)
            characterProfile.addProfileImage ("05-costume", False)
            characterProfile.addProfileImage ("06-dnd", False)
            characterProfile.addProfileImage ("07-lingerie", False)
            characterProfile.addProfileImage ("08-nude", False)
            characterProfile.addProfileImage ("09-pregnant", False)
            characterProfile.addProfileImage ("10-pregnantnude", False)
            characterProfile.addProfileImage ("11-special", False)
            characterProfile.addProfileImage ("11-special", False)
            characterProfile.addProfileImage ("11-special", False)
            characterProfile.addProfileImage ("11-special", False)
    $ mar.profileImages.pop (0) # first remove
    $ mar.profileImages.insert (0, ("martha_0", None)) # then add new
    $ mar.profileImages.pop (1) # first remove
    $ mar.profileImages.insert (1, ("martha_1", None)) # then add new
    $ mar.profileImages.pop (2) # first remove
    $ mar.profileImages.insert (2, ("martha_2", None)) # then add new
    $ mar.profileImages.pop (3) # first remove
    $ mar.profileImages.insert (3, ("martha_3", None)) # then add new
    $ mar.profileImages.pop (4) # first remove
    $ mar.profileImages.insert (4, ("martha_4", None)) # then add new
    $ mar.profileImages.pop (5) # first remove
    $ mar.profileImages.insert (5, ("martha_5", None)) # then add new
    $ mar.profileImages.pop (7) # first remove
    $ mar.profileImages.insert (7, ("martha_7", None)) # then add new
    $ mar.profileImages.pop (8) # first remove
    $ mar.profileImages.insert (8, ("martha_8", "route")) # then add new
    $ oma.profileImages.pop (0) # first remove
    $ oma.profileImages.insert (0, ("alexia_0", None)) # then add new
    $ oma.profileImages.pop (2) # first remove
    $ oma.profileImages.insert (2, ("alexia_2", None)) # then add new
    $ oma.profileImages.pop (3) # first remove
    $ oma.profileImages.insert (3, ("alexia_3", None)) # then add new
    $ oma.profileImages.pop (4) # first remove
    $ oma.profileImages.insert (4, ("alexia_4", None)) # then add new
    $ oma.profileImages.pop (8) # first remove
    $ oma.profileImages.insert (8, ("alexia_8", "route")) # then add new
    $ ama.profileImages.pop (1) # first remove
    $ ama.profileImages.insert (1, ("amanda_01", None)) # then add new
    $ ama.profileImages.pop (4) # first remove
    $ ama.profileImages.insert (4, ("amanda_4", None)) # then add new
    $ ama.profileImages.pop (11) # first remove
    $ ama.profileImages.insert (11, ("amanda_11", None)) # then add new
    $ bet.profileImages.pop (0) # first remove
    $ bet.profileImages.insert (0, ("betty_0", None)) # then add new
    $ bet.profileImages.pop (2) # first remove
    $ bet.profileImages.insert (2, ("betty_2", None)) # then add new
    $ bet.profileImages.pop (3) # first remove
    $ bet.profileImages.insert (3, ("betty_3", None)) # then add new
    $ bet.profileImages.pop (4) # first remove
    $ bet.profileImages.insert (4, ("betty_4", None)) # then add new
    $ dap.profileImages.pop (0) # first remove
    $ dap.profileImages.insert (0, ("daphne_0", None)) # then add new
    $ dap.profileImages.pop (1) # first remove
    $ dap.profileImages.insert (1, ("daphne_1", None)) # then add new
    $ dap.profileImages.pop (2) # first remove
    $ dap.profileImages.insert (2, ("daphne_2", None)) # then add new
    $ dap.profileImages.pop (3) # first remove
    $ dap.profileImages.insert (3, ("daphne_3", None)) # then add new
    $ dap.profileImages.pop (5) # first remove
    $ dap.profileImages.insert (5, ("daphne_5", None)) # then add new
    $ dap.profileImages.pop (7) # first remove
    $ dap.profileImages.insert (7, ("daphne_7", None)) # then add new
    $ dap.profileImages.pop (8) # first remove
    $ dap.profileImages.insert (8, ("daphne_8", "route")) # then add new
    $ dap.profileImages.pop (11) # first remove
    $ dap.profileImages.insert (11, ("daphne_11", "route")) # then add new
    $ deb.profileImages.pop (0) # first remove
    $ deb.profileImages.insert (0, ("deborah_0", None)) # then add new
    $ deb.profileImages.pop (1) # first remove
    $ deb.profileImages.insert (1, ("deborah_1", None)) # then add new
    $ deb.profileImages.pop (2) # first remove
    $ deb.profileImages.insert (2, ("deborah_2", None)) # then add new
    $ deb.profileImages.pop (3) # first remove
    $ deb.profileImages.insert (3, ("deborah_3", None)) # then add new
    $ eil.profileImages.pop (0) # first remove
    $ eil.profileImages.insert (0, ("eileen_0", None)) # then add new
    $ eil.profileImages.pop (2) # first remove
    $ eil.profileImages.insert (2, ("eileen_2", None)) # then add new
    $ eil.profileImages.pop (3) # first remove
    $ eil.profileImages.insert (3, ("eileen_3", None)) # then add new
    $ eil.profileImages.pop (4) # first remove
    $ eil.profileImages.insert (4, ("eileen_4", None)) # then add new
    $ eil.profileImages.pop (8) # first remove
    $ eil.profileImages.insert (8, ("eileen_8", "route")) # then add new
    $ emm.profileImages.pop (0) # first remove
    $ emm.profileImages.insert (0, ("emma_0", None)) # then add new
    $ emm.profileImages.pop (1) # first remove
    $ emm.profileImages.insert (1, ("emma_1", None)) # then add new
    $ emm.profileImages.pop (2) # first remove
    $ emm.profileImages.insert (2, ("emma_2", None)) # then add new
    $ emm.profileImages.pop (3) # first remove
    $ emm.profileImages.insert (3, ("emma_3", None)) # then add new
    $ emm.profileImages.pop (4) # first remove
    $ emm.profileImages.insert (4, ("emma_4", None)) # then add new
    $ emm.profileImages.pop (5) # first remove
    $ emm.profileImages.insert (5, ("emma_5", None)) # then add new
    $ emm.profileImages.pop (7) # first remove
    $ emm.profileImages.insert (7, ("emma_7", "route")) # then add new
    $ emm.profileImages.pop (8) # first remove
    $ emm.profileImages.insert (8, ("emma_8", "route")) # then add new
    $ eri.profileImages.pop (0) # first remove
    $ eri.profileImages.insert (0, ("erika_0", None)) # then add new
    $ eri.profileImages.pop (1) # first remove
    $ eri.profileImages.insert (1, ("erika_1", None)) # then add new
    $ eri.profileImages.pop (2) # first remove
    $ eri.profileImages.insert (2, ("erika_2", None)) # then add new
    $ eri.profileImages.pop (3) # first remove
    $ eri.profileImages.insert (3, ("erika_3", None)) # then add new
    $ eri.profileImages.pop (4) # first remove
    $ eri.profileImages.insert (4, ("erika_4", None)) # then add new
    $ eri.profileImages.pop (5) # first remove
    $ eri.profileImages.insert (5, ("erika_5", None)) # then add new
    $ eri.profileImages.pop (8) # first remove
    $ eri.profileImages.insert (8, ("erika_8", "route")) # then add new
    $ eva.profileImages.pop (0) # first remove
    $ eva.profileImages.insert (0, ("eva_0", None)) # then add new
    $ eva.profileImages.pop (2) # first remove
    $ eva.profileImages.insert (2, ("eva_2", None)) # then add new
    $ eva.profileImages.pop (4) # first remove
    $ eva.profileImages.insert (4, ("eva_4", None)) # then add new
    $ kat.profileImages.pop (0) # first remove
    $ kat.profileImages.insert (0, ("kate_0", None)) # then add new
    $ kat.profileImages.pop (2) # first remove
    $ kat.profileImages.insert (2, ("kate_2", None)) # then add new
    $ kia.profileImages.pop (0) # first remove
    $ kia.profileImages.insert (0, ("kiara_0", None)) # then add new
    $ kia.profileImages.pop (2) # first remove
    $ kia.profileImages.insert (2, ("kiara_2", None)) # then add new
    $ kia.profileImages.pop (4) # first remove
    $ kia.profileImages.insert (4, ("kiara_4", None)) # then add new
    $ kim.profileImages.pop (0) # first remove
    $ kim.profileImages.insert (0, ("kim_0", None)) # then add new
    $ kim.profileImages.pop (2) # first remove
    $ kim.profileImages.insert (2, ("kim_2", None)) # then add new
    $ kim.profileImages.pop (3) # first remove
    $ kim.profileImages.insert (3, ("kim_3", None)) # then add new
    $ lis.profileImages.pop (0) # first remove
    $ lis.profileImages.insert (0, ("lisa_0", None)) # then add new
    $ lis.profileImages.pop (2) # first remove
    $ lis.profileImages.insert (2, ("lisa_2", None)) # then add new
    $ mad.profileImages.pop (0) # first remove
    $ mad.profileImages.insert (0, ("maddie_0", None)) # then add new
    $ mad.profileImages.pop (8) # first remove
    $ mad.profileImages.insert (8, ("maddie_8", "route")) # then add new
    $ meg.profileImages.pop (0) # first remove
    $ meg.profileImages.insert (0, ("megan_0", None)) # then add new
    $ meg.profileImages.pop (2) # first remove
    $ meg.profileImages.insert (2, ("megan_2", None)) # then add new
    $ meg.profileImages.pop (4) # first remove
    $ meg.profileImages.insert (4, ("megan_4", None)) # then add new
    $ meg.profileImages.pop (8) # first remove
    $ meg.profileImages.insert (8, ("megan_8", "route")) # then add new
    $ nor.profileImages.pop (0) # first remove
    $ nor.profileImages.insert (0, ("norah_0", None)) # then add new
    $ nor.profileImages.pop (1) # first remove
    $ nor.profileImages.insert (1, ("norah_1", None)) # then add new
    $ nor.profileImages.pop (2) # first remove
    $ nor.profileImages.insert (2, ("norah_2", None)) # then add new
    $ nor.profileImages.pop (3) # first remove
    $ nor.profileImages.insert (3, ("norah_3", None)) # then add new
    $ nor.profileImages.pop (4) # first remove
    $ nor.profileImages.insert (4, ("norah_4", None)) # then add new
    $ nor.profileImages.pop (5) # first remove
    $ nor.profileImages.insert (5, ("norah_5", None)) # then add new
    $ nor.profileImages.pop (7) # first remove
    $ nor.profileImages.insert (7, ("norah_7", None)) # then add new
    $ nor.profileImages.pop (8) # first remove
    $ nor.profileImages.insert (8, ("norah_8", "route")) # then add new
    $ mee.profileImages.pop (0) # first remove
    $ mee.profileImages.insert (0, ("olivia_0", None)) # then add new
    $ mee.profileImages.pop (1) # first remove
    $ mee.profileImages.insert (1, ("olivia_1", None)) # then add new
    $ mee.profileImages.pop (2) # first remove
    $ mee.profileImages.insert (2, ("olivia_2", None)) # then add new
    $ sai.profileImages.pop (0) # first remove
    $ sai.profileImages.insert (0, ("saira_0", None)) # then add new
    $ sai.profileImages.pop (1) # first remove
    $ sai.profileImages.insert (1, ("saira_1", None)) # then add new
    $ sai.profileImages.pop (2) # first remove
    $ sai.profileImages.insert (2, ("saira_2", None)) # then add new
    $ sai.profileImages.pop (8) # first remove
    $ sai.profileImages.insert (8, ("saira_8", None)) # then add new
    $ sam.profileImages.pop (0) # first remove
    $ sam.profileImages.insert (0, ("samantha_0", None)) # then add new
    $ sam.profileImages.pop (1) # first remove
    $ sam.profileImages.insert (1, ("samantha_1", None)) # then add new
    $ sam.profileImages.pop (2) # first remove
    $ sam.profileImages.insert (2, ("samantha_2", None)) # then add new
    $ sam.profileImages.pop (4) # first remove
    $ sam.profileImages.insert (4, ("samantha_4", None)) # then add new
    $ sam.profileImages.pop (7) # first remove
    $ sam.profileImages.insert (7, ("samantha_7", "route")) # then add new
    $ sam.profileImages.pop (8) # first remove
    $ sam.profileImages.insert (8, ("samantha_8", "route")) # then add new
    $ sca.profileImages.pop (0) # first remove
    $ sca.profileImages.insert (0, ("scarlett_0", None)) # then add new
    $ sca.profileImages.pop (1) # first remove
    $ sca.profileImages.insert (1, ("scarlett_1", None)) # then add new
    $ sca.profileImages.pop (2) # first remove
    $ sca.profileImages.insert (2, ("scarlett_2", None)) # then add new
    $ sca.profileImages.pop (5) # first remove
    $ sca.profileImages.insert (5, ("scarlett_5", None)) # then add new
    $ sca.profileImages.pop (7) # first remove
    $ sca.profileImages.insert (7, ("scarlett_7", "route")) # then add new
    $ sca.profileImages.pop (8) # first remove
    $ sca.profileImages.insert (8, ("scarlett_8", "route")) # then add new
    $ sim.profileImages.pop (0) # first remove
    $ sim.profileImages.insert (0, ("simone_0", None)) # then add new
    $ sim.profileImages.pop (1) # first remove
    $ sim.profileImages.insert (1, ("simone_1", None)) # then add new
    $ sim.profileImages.pop (2) # first remove
    $ sim.profileImages.insert (2, ("simone_2", None)) # then add new
    $ sim.profileImages.pop (8) # first remove
    $ sim.profileImages.insert (8, ("simone_8", "route")) # then add new
    $ eva.profileImages.pop (11) # first remove
    $ eva.profileImages.insert (11, ("eva_11", None)) # then add new
    return
label c17s001_AmandaDinner:
    if _in_replay:
        $ sim._var("route" , False)
        $ AuxReplay = True
        call mrS3_mee_route from _call_mrS3_mee_route_13
        call mrS3_mar_route from _call_mrS3_mar_route_39
        if mar._var("route"):
            menu:
                "¿Está embarazada?"
                "Sí":
                    $ mar._var("pregnancyDiscovered" , True)
                "No":
                    $ mar._var("pregnancyDiscovered" , False)
        else:
                $ mar._var("pregnancyDiscovered" , False)
        call mrS3_nor_route from _call_mrS3_nor_route_30
        if nor._var("route"):
            menu:
                "¿Está embarazada?"
                "Sí":
                    $ nor._var("pregnancyDiscovered" , True)
                "No":
                    $ nor._var("pregnancyDiscovered" , False)
        else:
            $ nor._var("pregnancyDiscovered" , False)
        call mrS3_sam_route from _call_mrS3_sam_route_21
        if sam._var("route"):
            call mrS3_sim_route from _call_mrS3_sim_route_20
        call mrS3_oma_route from _call_mrS3_oma_route_16
        if oma._var("route"):
            call mrS3_oma_pregnant from _call_mrS3_oma_pregnant_3
        call mrS3_eil_route from _call_mrS3_eil_route_23
        if eil._var("route"):
            call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_5
        menu:
            "¿Fuiste a correr con Debbie?"
            "Sí":
                $ RunWithDebbie = True
                menu:
                    "¿Estás en una relación con Debbie?"
                    "Sí":
                        $ deb._var("route" , True)
                    "No":
                        $ deb._var("route" , False)
            "No":
                $ RunWithDebbie = False
                $ deb._var("route" , False)
        menu:
            "¿Cuántos Puntos de Relación tienes con Lisa?"
            "Mas de 0":
                $ lis._var("relationshipPoints", 5, intention = "set")
            "Menos de 0":
                $ lis._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Kim?"
            "Mas de 0":
                $ kim._var("relationshipPoints", 5, intention = "set")
            "Menos de 0":
                $ kim._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Intentaste besar a Kim en el Verdad o Reto en la playa?"
            "Sí":
                $ kim._var("kissedBeach" , True)
            "No":
                $ kim._var("kissedBeach" , False)
    call c17_updateprofiles from _call_c17_updateprofiles
    play music ("music/IWonderWhatIllDoToday.ogg")
    mc "¡Amanda! ¡Estás preciosa!"
    call BlinkXP ("c17s001_005" , "d") from _call_BlinkXP_1944
    ama "Gracias, [mc]. Has dicho que para la cena sería mejor un vestido y..."
    mc "Y has elegido uno que te queda perfecto. ¿Vamos?"
    $ renpy.notify ("Profile Image unlocked for Amanda: 12 - Special Business")
    call BlinkXP ("c17s001_010" , "d") from _call_BlinkXP_1945
    ama "Sí, por favor, no quiero llegar tarde y que se lleven una mala primera impresión."
    mc "Amanda, ¿realmente crees que alguien va a mirar el reloj cuando te vean?"
    mc "Todo el mundo está deseando conocerte, y más aún después del éxito de Eva durante la comida."
    call BlinkXP ("c17s001_015" , "h") from _call_BlinkXP_1946
    ama "Gracias, [mc]. No sé qué has hecho, pero ha vuelto entusiasmada."
    mc "¿No tenéis cámaras en la cocina de [nor]?"
    call BlinkXP ("c17s001_020" , "d") from _call_BlinkXP_1947
    ama "Sí, pero he dejado de mirarlas cuando le has presentado a [emm]."
    ama "Me estaba entrando envidia cuando [mar] y [nor] han abrazado a Eva. Más envidia todavía con [eri]."
    call BlinkXP ("c17s001_025" , "d") from _call_BlinkXP_1948
    ama "Pero con [emm] me ha entrado frustración. Ya estaba frustrada por cómo había tratado a [mar] esta mañana, pero..."
    mc "No le des más vueltas. Es [emm], y muchas veces solo necesita que alguien le haga pensar antes de darse cuenta de que su reacción ha sido... excesiva."
    call BlinkXP ("c17s001_030" , "d") from _call_BlinkXP_1949
    ama "Lo sé. Después de estos meses viendo a alguien con mi cara actuando como yo no lo haría nunca... te aseguro que lo sé."
    mc "¿Por eso te teñiste de rubio?"
    scene c17s001_035d with dissolve
    call BlinkXP ("c17s001_035" , "d") from _call_BlinkXP_1950
    ama "¿Q-qué? ¡N-no! Lo hice por si acaso... había que seguiros a distancia. Un color diferente de pelo puede... cambiar la percepción del observador."
    mc "Ah, OK. Como en las películas cuando los espías se ponen una peluca."
    ama "Sí... más o menos... ¿nos vamos?"
    scene black with dissolve
    "Tenéis una conversación tensa en el coche. Casi tienes que sacarle las palabras una a una."
    "Por fin llegáis a casa."
    call BlinkXP ("c17s001_040" , "f") from _call_BlinkXP_1951
    mc "¿Nerviosa?"
    ama "Sí, mucho. Lo de ayer fue... inesperado."
    ama "Lo que me ha contado hoy Eva de lo bien que se lo ha pasado... no sé... me da miedo."
    call BlinkXP ("c17s001_045" , "d") from _call_BlinkXP_1952
    ama "¿Qué pasa si después vendéis la empresa? ¿Qué pasa si, una vez pase la novedad, no queréis que formemos parte de la familia?"
    mc "Eso no va a pasar, Amanda. Al menos lo último."
    mc "No sé si venderemos la empresa o no. Será una decisión familiar, y aunque yo vote una cosa, ellas cinco pueden votar lo contrario."
    call BlinkXP ("c17s001_050" , "d") from _call_BlinkXP_1953
    ama "*Gruñido* Lo sé. Y no saber lo que van a hacer... me tiene nerviosa. Para mí, esta cena no es solo para conocerlas, aunque sea lo más importante..."
    mc "Es también para que te conozcan, para que les pongan cara a las verdaderas víctimas de NTR. Vosotras, Aaron, y el resto, ¿no?"
    call BlinkXP ("c17s001_055" , "d") from _call_BlinkXP_1954
    ama "Eva estaba equivocada. Pillas las cosas más rápido de lo que parece."
    ama "Depende a quién le vendáis la empresa, si no os podemos pagar lo que pidáis, habrá más Aarons y más Erics. Más Fionas."
    mc "Si mi voto decanta la balanza, no venderemos. Pero dudo que mi voto sirva de mucho."
    call BlinkXP ("c17s001_060" , "d") from _call_BlinkXP_1955
    ama "¿Crees que van a querer vender? Entiendo que es mucho dinero..."
    mc "[nor] y [mar] no van a querer que otras chicas o chicos pasen por lo que habéis pasado vosotras. Y estoy seguro de que no sabemos ni la mitad de lo que habéis pasado."
    mc "[dap] ya está haciendo planes para trabajar en NTR. Mejor hacerlo como accionista, ¿no?"
    mc "Y [eri] es tan empática que, en cuanto entienda por lo que habéis pasado, estará en la misma posición que [mar] y [nor]."
    mc "Mi voto y el de [emm] no servirían de nada."
    call BlinkXP ("c17s001_065" , "d") from _call_BlinkXP_1956
    ama "¿Votarías por venderla?"
    mc "No. Si votase por venderla sería para vendérosla a vosotros, pero creo que es mejor no hacerlo. Creo que me gusta la idea de hacer que el viejo NTR desaparezca."
    mc "Crear algo nuevo con lo que tenemos entre manos. Aunque no sé dónde encajaríais vosotras, Aaron, o el resto de los clones en esa visión."
    call BlinkXP ("c17s001_070" , "d") from _call_BlinkXP_1957
    ama "Sobre eso... tengo varias ideas. ¿Te parece bien que tomemos un café un día y lo hablamos?"
    mc "Me parece genial. Ahora deberíamos entrar."
    scene c17s001_085a with fade
    pause (1.0)
    call BlinkXP ("c17s001_075" , "d") from _call_BlinkXP_1958
    mc "Bueno, parece que toda la familia está aquí. *Risa* Vas a sufrir más que Eva."
    ama "*Susurrando* Yo soporto... disfruto más de los abrazos que ella."
    scene c17s001_080An with dissolve
    "[mar] corre hacia Amanda y la envuelve en un abrazo."
    mom "Bienvenida de nuevo a casa, Amanda."
    ama "Gracias, [mar]."
    stop music fadeout (1.5)
    scene c17s001_085b with fade
    "Se repiten las presentaciones y los abrazos de la comida y la misma dinámica. Las chicas, esta vez también con las estudiantes, acaparan a Amanda mientras las mujeres se mantienen apartadas."
    "Decides mantenerte a distancia del grupo de chicas. Sabes que, si te acercas a ellas, vas a ser objeto de bromas y hoy el centro de atención tiene que ser Amanda."
    play music ("music/These-Little-Moments.ogg")
    call BlinkXP ("c17s001_090" , "f") from _call_BlinkXP_1959
    bet "Parece increíble, ¿no? Esta mañana teníamos a una versión de [emm] que se parecía a [dap] y ahora una versión de [eri] con la cara de [emm]."
    mc "Son más complejas que todo eso, Tía Betty. Aparte del obvio parecido físico, en cuanto a personalidad no puedes buscar una correlación total."
    mc "Es cierto que Eva se parece mucho a [emm], pero hay muchos matices. También tiene mucho de ti, como el sentido del humor."
    mc "Y Amanda, pese a que es emocional como [eri], también es inteligente como [dap] o Scarlett."
    call BlinkXP ("c17s001_095" , "d") from _call_BlinkXP_1960
    bet "Tienes razón. La mente juega malas pasadas y, sabiendo que son clones, busca más parecidos de los obvios."
    mc "Sí, a mí también me pasa. Espero que Eva actúe como [emm]. La mayoría de las veces lo hace, pero a veces me sorprende."
    mc "Hoy en la clase de tiro podría haber avergonzado a Meemaw con lo estricta que era al principio."
    call BlinkXP ("c17s001_100" , "d") from _call_BlinkXP_1961
    bet "Hablando de Olivia, ¿cómo ha ido la visita al médico?"
    if mee._var("route"):
        bet "Ha vuelto más contenta de lo que esperaba sabiendo que no va a poder empezar el tratamiento todavía."
    mc "Bueno, estaba un poco decepcionada sobre lo de no poder empezar el tratamiento inmediatamente, pero después se le ha pasado un poco."
    call BlinkXP ("c17s001_105" , "d") from _call_BlinkXP_1962
    bet "Me ha dicho que me tienes que enseñar algo sobre los masajes, que yo no los estaba haciendo bien."
    mc "Es lo que ha dicho la Dra. Milk. Hay una zona que no estás masajeando correctamente."
    call BlinkXP ("c17s001_110" , "d") from _call_BlinkXP_1963
    bet "Mañana, cuando toque darle el masaje, puedes enseñarme, si te va bien."
    mc "Perfecto. No es difícil."
    if mee._var("route"):
        mc "Aunque puede acabar siendo un poco pegajoso. *Risita*"
        call BlinkXP ("c17s001_115" , "d") from _call_BlinkXP_1964
        bet "¿Pegajoso? ¿Por qué? ¿La médico no le sacó la leche antes de los masajes?"
        mc "Sí, pero... por lo que dijo, es posible que no lo sacara todo."
        bet "Mmmmm... Okaaay."
    call BlinkXP ("c17s001_120" , "d") from _call_BlinkXP_1965
    mee "¿Qué estáis planeando vosotros dos? *Risita*"
    mc "Nada especial, Meemaw. Tía Betty me estaba pidiendo que le enseñara mañana lo que hemos hecho hoy."
    mc "Podemos repetir lo de esta mañana si quieres."
    if mee._var("route"):
        call BlinkXP ("c17s001_125a" , "d") from _call_BlinkXP_1966
        mee "¿Qué? {b}¿Todo?{/b}"
        mc "Lo que tú quieras, Meemaw."
        call BlinkXP ("c17s001_130a" , "d") from _call_BlinkXP_1967
        bet "Mmmmm... ¿A qué te refieres con \"todo\", Olivia?"
        mc "La doctora nos ha enseñado dos formas de hacer el masaje. Una por delante, como lo haces tú, y otra desde atrás."
        mc "Ha sido más cómodo hacerlo desde atrás, y con mejor resultado."
        call BlinkXP ("c17s001_135" , "h") from _call_BlinkXP_1968
        mee "¡[mc]!"
        mc "¿Qué? Es cierto..."
        call BlinkXP ("c17s001_130b" , "d") from _call_BlinkXP_1969
        bet "Mmmm... ¿Ha pasado algo?"
        mc "¿Qué quieres que pase? Estábamos en la consulta del médico. *Risa*"
        if mar._var("route") or nor._var("route"):
            $ Aux = 2
            bet "No sé... parece que dejarte a solas con una mujer de la familia tiene cierto riesgo..."
        elif sam._var("route") or sim._var("route") or eil._var("route") or oma._var("route"):
            $ Aux = 0
            if sam._var("route"):
                $ Aux = Aux + 1
            if sim._var("route"):
                $ Aux = Aux + 1
            if oma._var("route"):
                $ Aux = Aux + 1
            if eil._var("route"):
                $ Aux = Aux + 1
            if Aux > 1:
                bet "No sé... parece que dejarte a solas con una mujer tiene cierto riesgo... parece que las colecciones."
        if Aux > 1:
            call BlinkXP ("c17s001_140" , "d") from _call_BlinkXP_1970
            mee "¡Betty! ¡Retira eso ahora mismo!"
            mc "No te alteres, Meemaw. Betty está bromeando. Todos sabemos que no soy tu tipo. *Risa*"
            call BlinkXP ("c17s001_145" , "d") from _call_BlinkXP_1971
            mee "Tienes razón... últimamente estoy muy alterada y no sé por qué..."
            call BlinkXP ("c17s001_130a" , "d") from _call_BlinkXP_1972
        else:
            call BlinkXP ("c17s001_130b" , "d") from _call_BlinkXP_1973
        mc "No te preocupes. Siguiendo con el tema de los masajes. ¿Mañana por la mañana?"
    else:
        call BlinkXP ("c17s001_150" , "d") from _call_BlinkXP_1974
        mee "Sí, así le enseñas a Betty cómo se hace."
    call BlinkXP ("c17s001_155" , "d") from _call_BlinkXP_1975
    bet "Genial. ¿A las 10 en tu habitación?"
    call BlinkXP ("c17s001_160" , "d") from _call_BlinkXP_1976
    mee "OK, a las 10, pero mejor en el baño, después de que me haya extraído la leche."
    stop music fadeout (1.5)
    mc "Genial entonces. Nos vemos a las 10 allí. Voy a hablar con [mar.mc!t] y [nor] un momento. Hasta ahora."
    scene c17s001_165a with fade
    play music ("music/SaveMe.ogg")
    mc "Me sorprendéis."
    mom "¿Qué hemos hecho?" (multiple=2)
    nor "¿Por qué?" (multiple=2)
    mc "En la comida, con Eva, y ahora, con Amanda. Cuando pusisteis la condición de que vinieran a comer y a cenar, creía que no os ibais a separar de ellas."
    scene c17s001_165b with dissolve
    nor "Sabíamos que hoy no íbamos a poder tenerlas para nosotras. Son algo nuevo para todas, pero nosotras estuvimos con ellas ayer un rato."
    mom "Un rato muy corto. Pero las chicas también tienen derecho a estar con ellas y conocerlas. Incluso más que nosotras."
    nor "Y también es bueno que las estudiantes las conozcan. Les hemos puesto un peso encima muy grande con el secreto, aunque todas han reaccionado bien."
    if RunWithDebbie:
        mc "Debbie también ha reaccionado bien pero, claro, tenía a Eva delante. No podía negar lo que estaba viendo."
    mc "Son buenas chicas, y se están integrando muy rápidamente en la familia. Sólo llevan una semana aquí."
    if mar._var("route") or nor._var("route"):
        mc "Y, cambiando de tema, supongo que ya habéis hablado de lo de esta tarde, ¿no?"
        if mar._var("pregnancyDiscovered") and nor._var("pregnancyDiscovered"):
            scene c17s001_165c with dissolve
            mom "¡Sí! Estamos las dos muy ilusionadas. Tenemos muchas ganas de contárselo a todo el mundo."
            nor "Hemos decidido hacerlo la semana que viene, una vez pasen los cumpleaños. El martes o el miércoles... o incluso más adelante."
            if persistent.family:
                nor "Tu madre tiene más ganas de hacerlo que yo. No sé cómo se lo tomará tu abuela."
            else:
                nor "[mar] tiene más ganas de hacerlo que yo. No sé cómo se lo tomará mi madre."
        elif mar._var("pregnancyDiscovered"):
            if nor._var("route"):
                scene c17s001_165d with dissolve
                mom "Sí, nos hubiera gustado quedarnos las dos embarazadas a la vez, pero no ha podido ser. Ahora tan solo lo tenéis que intentar más."
                nor "Hemos pensado que no deberíais contar nada hasta la semana que viene, una vez pasen los cumpleaños. El martes o el miércoles... o incluso más adelante."
            else:
                scene c17s001_165c with dissolve
                nor "¡Sí! Ya me lo ha dicho. ¡Felicidades, Papá!"
                mom "Se lo tenía que contar a alguien, y las chicas están descartadas este fin de semana. Es su fin de semana..."
                mom "He pensado que no deberíamos contarles nada hasta la semana que viene, una vez pasen los cumpleaños. El martes o el miércoles."
            if persistent.family:
                nor "Tu madre tiene más ganas de hacerlo de las que tendría yo. No sé cómo se lo tomará tu abuela."
            else:
                nor "[mar] tiene más ganas de hacerlo de las que tendría yo. No sé cómo se lo tomará mi madre."
        elif nor._var("pregnancyDiscovered"):
            if mar._var("route"):
                scene c17s001_165d with dissolve
                nor "Sí, nos hubiera gustado quedarnos las dos embarazadas a la vez, pero no ha podido ser. Ahora tan solo lo tenéis que intentar más."
                mom "Hemos pensado que no deberíais contar nada hasta la semana que viene, una vez pasen los cumpleaños. El martes o el miércoles..."
            else:
                scene c17s001_165c with dissolve
                mom "¡Sí! Ya me lo ha dicho. ¡Felicidades, Papá!"
                nor "Se lo tenía que contar a alguien, y las chicas están descartadas este fin de semana. Es su fin de semana..."
                nor "He pensado que no deberíamos contarles nada hasta la semana que viene, una vez pasen los cumpleaños. El martes o el miércoles."
            if persistent.family:
                mom "[nor] tiene menos ganas de hacerlo de las que tendría yo. No sabe cómo se lo tomará tu abuela."
            else:
                mom "[nor] tiene menos ganas de hacerlo de las que tendría yo. No sabe cómo se lo Olivia."
        else:
            if mar._var("route") and nor._var("route"):
                scene c17s001_165d with dissolve
                mom "Ha sido decepcionante para las dos, igual que para ti, pero mientras estemos los tres unidos en esto..."
                nor "Ha sido bonito poder apoyarnos la una en la otra... Al menos no mataremos a tu abuela con la noticia."
            elif mar._var("route"):
                scene c17s001_165d with dissolve
                mom "Necesitaba contárselo a alguien, tú te has ido a buscar a Amanda y... Sé que lo tenías que hacer, no estoy echándote nada en cara, pero necesitaba desahogarme."
                if persistent.family:
                    nor "Para eso estamos las hermanas, ¿no? Al menos no mataréis a nuestra madre con la noticia este fin de semana."
                else:
                    nor "Para eso estamos las amigas, ¿no? Al menos no mataréis a mi madre con la noticia este fin de semana."
            elif nor._var("route"):
                scene c17s001_165d with dissolve
                nor "Necesitaba contárselo a alguien, tú te has ido a buscar a Amanda y... Sé que lo tenías que hacer, no estoy echándote nada en cara, pero necesitaba desahogarme."
                if persistent.family:
                    mom "Para eso estamos las hermanas, ¿no? Al menos no mataréis a nuestra madre con la noticia este fin de semana."
                else:
                    mom "Para eso estamos las amigas, ¿no? Al menos no mataréis a mi madre con la noticia este fin de semana."
        mc "Le tenéis mucho miedo a las reacciones de Meemaw. Creo que si le dais un poco de confianza, os va a dar una sorpresa."
        call BlinkXP ("c17s001_170" , "d") from _call_BlinkXP_1977
        nor "Bueno, ya hablaremos. No creo que sea el momento ni el lugar para hablar de esto. No te gires, pero Tía Betty lleva un rato mirando hacia aquí."
        scene c17s001_170d with dissolve
        pause (0.8)
        call BlinkXP ("c17s001_170" , "d") from _call_BlinkXP_1978
        nor "¿Que parte de \"no te gires\" no has entendido? *Risa*"
        mc "Sabes que frases como \"no te gires\" o \"no mires\" no funcionan conmigo, ¿verdad? *Risa*"
        call BlinkXP ("c17s001_175" , "d") from _call_BlinkXP_1979
        mom "Lo peor de todo es que después te atreves a decir que somos nosotras las que somos unas cotillas. *Risa*"
        mc "Y lo sois. *Risa* Voy a hacer un poco de vida social con las estudiantes antes de que Tía Betty siga sospechando."
    call BlinkXP ("c17s001_180" , "d") from _call_BlinkXP_1980
    nor "Hablando de eso, creo que Debbie y Lisa están esperando para hablar contigo. Están mirando hacia aquí."
    stop music fadeout (1.5)
    mc "Pues voy a hablar con ellas, a ver que les han parecido Amanda y Eva. Hablamos luego."
    scene c17s001_185a with fade
    play music ("music/Rise-Up.ogg")
    mc "Hola, chicas. ¿Qué os parece la reunión familiar?"
    deb "¡Alucinante! Después de 15 minutos hablando con Amanda, es como si la conociera de toda la vida. Y con Eva me he sentido igual a mediodía. Son muy simpáticas."
    lis "Yo me he perdido a Eva. Tengo ganas de conocerla mañana en la cena."
    scene c17s001_185b with dissolve
    deb "Eva es más musculosa que Amanda, o a Amanda se le nota menos con ese vestido. Al menos ya no soy la rara de la familia."
    mc "Nunca has sido rara, Debbie. Un cuerpo musculoso puede ser bonito."
    lis "¿Ves? Te lo he dicho siempre. No tienes que acomplejarte de tus músculos."
    mcp "(Yo lo recuerdo de otra forma, al menos cuando fuimos a la tienda de Maddie...)"
    call BlinkXP ("c17s001_190" , "d") from _call_BlinkXP_1981
    lis "¿Te importa si salimos a tomar el aire un momento? Empieza a hacer calor aquí."
    mc "Si, claro."
    lis "Los tres..."
    mc "Por supuesto."
    scene c17s001_185c with fade
    lis "Se agradece el frescor de la tarde. Creo que deberíais cambiar los focos halógenos por LED. Consumen menos y dan menos calor."
    deb "Lisa..."
    scene c17s001_185d with dissolve
    lis "¿Qué? ¡Es verdad! ¡Es un desperdicio de electricidad enorme! Y el planeta..."
    mc "Lisa, ¿pasa algo? Hacía días que no sacabas a relucir el tema del planeta o la contaminación... "
    deb "Suele hacerlo cuando está nerviosa..."
    lis "¡Debbie!"
    mc "¿Por qué estás nerviosa, Lisa?"
    call BlinkXP ("c17s001_195" , "d") from _call_BlinkXP_1982
    lis "Porque te iba a contar algo, pero me acabo de dar cuenta de que es una tontería que posiblemente ni te importe."
    if persistent.walkthrough:
        $ wt1 = "Lisa + 5"
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Si es importante para ti, es importante para mí." (wt = wt1):
            $ lis.rp (5)
        "Cuéntamelo, luego decidimos si era importante." (wt = wt2):
            pass
    call BlinkXP ("c17s001_200" , "d") from _call_BlinkXP_2030
    lis "Anthony y yo... tal como te dije... no me veía con alguien como él... No sentía nada cuando estaba con él."
    lis "Ayer estuvimos hablando y... a él le pasa lo mismo... hemos decidido romper nuestra \"no relación\"."
    call BlinkXP ("c17s001_205" , "d") from _call_BlinkXP_2031
    lis "Creo que ninguno de los dos quería hablar de ello para no hacerle daño al otro... pero los dos queríamos dejar de hacer lo que estábamos haciendo."
    lis "Hemos decidido seguir siendo amigos, pero no vamos a intentar ser algo más."
    mc "¿Te das cuenta como sí era importante? Nunca dudes en contarme algo que te preocupe, Lisa."
    call BlinkXP ("c17s001_210" , "d") from _call_BlinkXP_2032
    if lis.rps > 0:
        lis "De todas formas... a los dos... nos gustan otras personas, con lo que creo que es lo mejor, de todas formas."
        mc "¿Alguien que has conocido desde que has llegado?"
        lis "Sí..."
        mc "¡Eso es fantástico, Lisa! ¡Nos lo tienes que presentar!"
        scene c17s001_185e with dissolve
        lis "Sí, un día te diré quién es..."
        deb "Sobre eso..."
        call BlinkXP ("c17s001_215" , "d") from _call_BlinkXP_2033
    else:
        lis "De todas formas... a él... le gusta otra persona, con lo que creo que es lo mejor, de todas formas."
        call BlinkXP ("c17s001_215" , "d") from _call_BlinkXP_2034
        if deb._var("route"):
            deb "Sobre eso..."
    if deb._var("route"):
        deb "Ahora que estamos aquí los tres... podríamos... ya sabes..."
        mc "Si quieres, sí. Es tu decisión a quién y cuándo decírselo."
        call BlinkXP ("c17s001_220" , "d") from _call_BlinkXP_2035
        deb "Lisa, tengo... tenemos algo que contarte..."
        deb "[mc] y yo estamos... más o menos... saliendo juntos..."
        scene c17s001_225An with dissolve #ab lisa mira alternativamente a MC y a Debbie
        lis "¿Qué? ¿Desde cuándo? ¿Qué es eso de más o menos?"
        mc "Aún no hemos hablado de como llamarlo, pero podríamos decir que esta mañana hemos decidido empezar algo y ver a donde nos lleva."
        call BlinkXP ("c17s001_230" , "d") from _call_BlinkXP_2036 #lis abraza a deb
        lis "¡Es fantástico, Debbie! Nunca hubiera pensado que tendrías novio antes que yo, pero... ¡me alegro muchísimo!"
        deb "Gracias, Lisa... no ha empezado como me había imaginado, pero el resultado ha sido mejor aún."
        mc "Te debo una cita de verdad. *Risa*"
        call BlinkXP ("c17s001_235" , "d") from _call_BlinkXP_2037
        lis "Y tú... más vale que la cuides y no le hagas daño o te las tendrás que ver conmigo."
        mc "No tengo intención de hacerle daño, Lisa. No soy así."
        scene c17s001_185f with dissolve
        lis "Me lo tenéis que contar todo. Lo estáis rodeando de misterio."
        mc "No sé si aquí y ahora es el mejor momento para hacerlo."
        deb "Creo que no, pero deberíamos volver con Amanda, estar un ratito... y, si quieres, volvemos pronto a la habitación y te lo cuento todo... si a [mc] no le importa."
        mc "Adelante, Debbie. Creo que es una conversación entre hermanas en la que no debo estar. Además, yo voy a tenerlo más complicado para desaparecer."
        mc "Tengo que llevar de nuevo a Amanda a su base cuando acabe la cena."
        scene c17s001_185g with dissolve
        lis "Genial, volvamos dentro. Tengo ganas de que me lo expliques todo."
        deb "Deberás tener un poco de paciencia. No nos vamos a ir inmediatamente."
        lis "Pero cuánto antes volvamos, antes nos podremos ir a nuestra habitación, ¿no?"
        deb "Vaaale, vamos."
        scene c17s001_185h with dissolve
        deb "Hasta luego, [mc]. Te buscaré para mi beso de buenas noches antes de irnos."
        mc "Lo estaré esperando."
        if lis.rps > 0:
            lis "Yo también vendré a buscar el mío... si Debbie me deja hacerlo, claro."
            deb "No hay ningún problema en que te bese, ¿verdad?"
            mc "No, Debbie. Que tú y yo hayamos empezado algo, no significa que tengamos que eliminar las buenas costumbres."
    else:
        if lis.rps > 0:
            deb "[emm] tenía razón, te cuesta pillar algunas cosas. *Risita*"
        deb "Lisa, deberíamos entrar y seguir charlando con Amanda un rato. Hoy quiero acostarme pronto."
        scene c17s001_185h with dissolve
        deb "Hasta luego, [mc]."
        lis "Nos vemos dentro."
        mc "Hasta ahora, chicas."
    if eil._var("route") and oma._var("route"):
        call c17s001_EileenAlexiaPregnancyResult from _call_c17s001_EileenAlexiaPregnancyResult
    elif eil._var("route"):
        call c17s001_EileenPregnancyResult from _call_c17s001_EileenPregnancyResult
    elif oma._var("route"):
        call c17s001_AlexiaPregnancyResult from _call_c17s001_AlexiaPregnancyResult
    call BlinkXP ("c17s001_375" , "f") from _call_BlinkXP_1983
    stop music fadeout (1.5)
    "Al volver a la cocina ves como Amanda te hace señas para que vayas a una zona sin gente."
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    mc "¿Qué tal te lo estás pasando?"
    ama "¡Ufff! Es mejor de lo que me había dicho Eva. Es como sentirse parte de algo."
    mc "Y sólo es el primer día que vienes. Espera a que vayan cogiendo confianza."
    call BlinkXP ("c17s001_380" , "d") from _call_BlinkXP_1984
    ama "Eva ya me había advertido. Hay un componente de sentirse un animal exhibido. Todo el mundo quiere saber cosas de nosotras."
    ama "Pero supongo que en un par de días se les pasará. Pese a todo es un momento increíble."
    mc "Olvídalo. Siempre querremos saber más cosas de vosotras."
    mc "Por cierto, saluda a Eva. Supongo que nos está oyendo por el auricular."
    call BlinkXP ("c17s001_385" , "d") from _call_BlinkXP_1985
    ama "No... si nos está oyendo, será a través de los micrófonos de la cocina, pero no llevo auricular hoy."
    mc "¿Por qué?"
    call BlinkXP ("c17s001_390" , "d") from _call_BlinkXP_1986
    ama "Quería... quería que esta experiencia fuera solo mía."
    ama "Sé que puede sonar ridículo, pero Eva y yo hemos vivido toda nuestra vida juntas. Todas nuestras experiencias han sido compartidas."
    ama "La quiero con locura, no me malinterpretes, pero a veces librarse de tu hermana siamesa... es bueno. Raro, pero bueno."
    mc "¿Todas vuestras experiencias?"
    call BlinkXP ("c17s001_395" , "d") from _call_BlinkXP_1987
    ama "¡[mc]! Hay cosas que no se le preguntan a una dama. *Risa*"
    mc "¿Qué? ¡No! No me refería a eso... sea lo que sea a lo que te refieras tú."
    call BlinkXP ("c17s001_400" , "d") from _call_BlinkXP_1988
    ama "No te preocupes. *Risita* Hoy me han preguntado cosas muy raras, y no me hubiera sorprendido si alguna de ellas me hubiera preguntado si Eva y yo éramos pareja."
    mc "¿Qué?"
    call BlinkXP ("c17s001_405" , "d") from _call_BlinkXP_1989
    ama "¿Qué? ¡No! ¡No me refería a que lo fuéramos! ¡No lo somos! ¡A mí me gustan los hombres! Y ya sabes que a Eva también."
    mc "*Risa* Sí, lo sé. Lo de esta mañana ha sido un poco alucinante. \"Me caías mal, pero estás bueno y te iba a echar un polvo aunque eso jodiera tu relación con [eri]\"."
    call BlinkXP ("c17s001_410" , "d") from _call_BlinkXP_1990
    ama "Mi hermana puede ser tan impulsiva como la tuya. Y puede pensar lo mismo en las consecuencias de sus actos. Es decir, nada."
    mc "Lo estoy descubriendo... hablando de la Princesa Rosa..."
    scene c17s001_415a with dissolve
    emm "¿Hablabais de mí? He oído la palabra \"hermana\"... Y estando aquí mis dos hermanos, sólo podía ser yo."
    mcp "(Dos hermanos... me encanta cómo en un par de horas todo el mundo considera a Amanda familia. Lo mismo que ha pasado con Eva.)"
    mc "Sí, hablábamos de lo mucho que os parecéis..."
    scene c17s001_415b with dissolve
    emm "Es normal, ¿no? Al fin y al cabo llevamos los mismos genes."
    ama "... de lo mucho que os parecéis Eva y tú."
    scene c17s001_415c with dissolve
    emm "¡Es verdad! ¡Le he dicho a [mc] que Eva me recordaba a alguien! ¡A mí!"
    call BlinkXP ("c17s001_420" , "d") from _call_BlinkXP_1991
    emm "También le he dicho que es fantástica... lo cual me convierte a mí también en fantástica, ¿no?"
    mc "Sí, [emm], eres fantástica. *Risa*"
    scene c17s001_425a with dissolve
    emm "¡Y el resto de las chicas también lo han dicho! No sólo fantástica, pero otras cosas bonitas también. ¡Eso significa que también piensan lo mismo de mí!"
    mc "*Risa* Bueno... quizás..."
    ama "Sí, estoy segura de que piensan eso de ti."
    scene c17s001_425b with dissolve
    emm "¡Claro! ¡Tú has oído todas nuestras conversaciones! Me tienes que contar todo lo que han dicho de mí."
    ama "Pero eso significaría que también les debería contar al resto lo que han dicho de ellas. Sería lo justo, ¿no?"
    scene c17s001_425c with dissolve
    emm "Mmmm... entonces mejor no... Esta mañana he dicho cosas muy feas de mi madre..."
    call BlinkXP ("c17s001_430" , "d") from _call_BlinkXP_1992
    emm "Pero bueno, os dejo un rato. ¡Voy a decirle a las chicas que me han estado alabando cuando alababan a Eva!"
    mc "¡[emm]!"
    call BlinkXP ("c17s001_435" , "d") from _call_BlinkXP_1993
    mc "Y se fue..."
    ama "Exactamente lo mismo que hubiera hecho Eva. *Risa*"
    call BlinkXP ("c17s001_440" , "d") from _call_BlinkXP_1994
    ama "Creo que voy a volver un rato con las chicas si no te importa. Quiero escuchar lo que dice [emm]."
    mc "Ningún problema, pero sabes perfectamente lo que va a decir. Imagínate lo que diría Eva. *Risa*"
    call BlinkXP ("c17s001_440b" , "d") from _call_BlinkXP_1995
    ama "Sí pero no. Eva y [emm] son muy parecidas en la superficie, pero tienen más matices de los que parece."
    mc "¿Igual que tú con [dap] y [eri]? También con matices, claro."
    call BlinkXP ("c17s001_445" , "d") from _call_BlinkXP_1996
    ama "¿A qué te refieres? ¿Crees que me parezco a [dap] y a [eri]?"
    mc "Eres inteligente como [dap], pero emocional como [eri]. Sólo había que mirarte durante la reunión con Aaron."
    mc "Pasabas de la pose hiper-profesional, que sería [dap], a fundirte cuando [mar] te cogía de la mano o cuando [nor] te abrazaba, que sería [eri]."
    call BlinkXP ("c17s001_450" , "d") from _call_BlinkXP_1997
    ama "No puedes imaginarte lo emocionante que fue para nosotras. Desde que Aaron nos dijo que teníamos que conoceros..."
    ama "Eva y yo habíamos hablado durante horas sobre cómo podía ser esa única reunión. Os íbamos a conocer y no volver a veros..."
    mc "Y ahora estás aquí."
    call BlinkXP ("c17s001_455" , "d") from _call_BlinkXP_1998
    ama "Y tampoco puedes imaginarte lo que llevo dos horas sintiendo. O lo que Eva ha sentido esta mañana."
    mc "No, desde luego que no puedo, pero me alegro de que lo estéis sintiendo. Tú tampoco te puedes imaginar lo que significa para mí la recepción que os ha dado la familia."
    mc "Sabía cómo se iban a comportar, pero verlo... ¡Ufff! Son cosas como esta las que me hacen estar orgulloso de pertenecer a esta familia."
    call BlinkXP ("c17s001_460" , "d") from _call_BlinkXP_1999
    ama "Tienes razones para estarlo. Tienes una familia fantástica y estoy deseando conocer al resto de la familia."
    mc "¿El resto?"
    ama "Samantha, Simone, Jamaal... y no sé si me dejo a alguien más. Supongo que sí."
    mc "Espera un momento... Consideras a Samantha, a Simone y a Jamaal parte de la familia, ¿no?"
    call BlinkXP ("c17s001_465" , "d") from _call_BlinkXP_2000
    ama "Sí, claro. Cuando habláis de ellos, especialmente [mar], [nor], las chicas, y tú, se nota que los consideráis familia."
    mc "Entonces, si se trata de si nosotros consideramos a alguien familia o no..."
    scene c17s001_470pv with dissolve
    $ renpy.movie_cutscene ("c17/c17s001_470vid.webm", loops = 0)
    scene c17s001_475a with dissolve
    call BlinkXP ("c17s001_475" , "d") from _call_BlinkXP_2001
    mc "¿Cómo crees que te consideran todas estas personas?"
    scene c17s001_480a with dissolve
    mc "Chicas, un momento, por favor. ¿Hay alguna de vosotras que, después de todo lo que ha pasado hoy, considere que Eva y Amanda forman parte de la familia?"
    call BlinkXP ("c17s001_485" , "d") from _call_BlinkXP_2002
    mom "¡Claro que forman parte de la familia! Si ellas quieren, por supuesto."
    mcp "(Sabía que ibas a decir eso. Tú y [nor] sois las que primero las aceptasteis.)"
    call BlinkXP ("c17s001_490" , "d") from _call_BlinkXP_2003
    nor "Sólo a ti se te podría ocurrir preguntar una tontería así."
    mcp "(Bueno, tampoco hay que matar al mensajero. *Risa mental*)"
    call BlinkXP ("c17s001_530a" , "d") from _call_BlinkXP_2004
    kat "Es difícil decir que no lo son cuando podrían pasar por hermanas de [dap], [eri], y [emm]."
    mcp "(Te tengo que preguntar que versión te gusta más.)"
    call BlinkXP ("c17s001_500" , "d") from _call_BlinkXP_2005
    bet "Son un regalo divino. ¿Cómo no van a ser parte de esta familia?"
    mcp "(¿Divino? Ciencia, Tía Betty, ciencia.)"
    call BlinkXP ("c17s001_530b" , "d") from _call_BlinkXP_2006
    deb "¿No sentís que desde la playa parecemos una familia? ¿Todas?"
    mcp "(No eres la primera que lo piensa.)"
    call BlinkXP ("c17s001_505" , "d") from _call_BlinkXP_2007
    oma "Si me habéis aceptado a mí..."
    mcp "(¿Cómo no vamos a aceptarte? Debbie lo acaba de decir. Estabas en la playa.)"
    call BlinkXP ("c17s001_510" , "d") from _call_BlinkXP_2008
    kia "Y a nosotras..."
    mcp "(Aunque desde que estuvimos en tu casa te noto un poco distante. Debería hablar contigo.)"
    call BlinkXP ("c17s001_520" , "d") from _call_BlinkXP_2009
    mee "Después de encontrar a mis nuevas nietas, no voy a dejar que nadie se atreva a arrebatármelas."
    mcp "(¡Cómo has cambiado, Meemaw!)"
    call BlinkXP ("c17s001_525" , "d") from _call_BlinkXP_2010
    kim "Sólo llevo aquí una semana. Me siento más en familia de lo que me he sentido en ningún sitio desde que me fui de casa de mis padres."
    mcp "(Espera a llevar un mes, o un año.)"
    call BlinkXP ("c17s001_515" , "d") from _call_BlinkXP_2011
    eil "Formar parte de esta familia es increíble, Amanda. No dejes que nadie te lo impida. Ni siquiera tú misma."
    mcp "(Siempre lo has deseado, ahora se ha hecho realidad.)"
    call BlinkXP ("c17s001_495" , "d") from _call_BlinkXP_2012
    dap "¿Cómo no van a formar parte? Somos ellas y ellas son nosotras."
    mcp "(No lo podías haber expresado mejor.)"
    call BlinkXP ("c17s001_535" , "d") from _call_BlinkXP_2013
    sai "[mc] me había hablado de su familia en Portland. No es difícil de entenderlo una vez lo vives, Amanda."
    mcp "(Y ahora te das cuenta de que no mentía.)"
    call BlinkXP ("c17s001_540" , "d") from _call_BlinkXP_2014
    eri "Dejadnos ser vuestra familia, Amanda. Dejadnos demostraros que tenéis un lugar aquí, con nosotros. Sed nuestra familia también."
    mcp "(¿Dejadnos? Eres maravillosa, [eri].)"
    call BlinkXP ("c17s001_545" , "d") from _call_BlinkXP_2015
    lis "Incluso las recién llegadas nos sentimos así. Si se lo permites... si nos lo permites, no tardarás en darte cuenta."
    mcp "(¿Quién hubiera podido pensar hace sólo una semana que Lisa diría \"nos lo permites\"?)"
    call BlinkXP ("c17s001_550" , "d") from _call_BlinkXP_2016
    sca "En parte gracias a ti tengo esta familia. Quiero que tú también formes parte de ella."
    mcp "(Tú ya formabas parte de la familia, cielo, pero aún no lo sabíamos.)"
    call BlinkXP ("c17s001_555" , "d") from _call_BlinkXP_2017
    emm "¿Cómo vamos a rechazar a la segunda mujer más guapa del mundo? *Risa*"
    mcp "([emm]...)"
    call BlinkXP ("c17s001_560" , "d") from _call_BlinkXP_2018
    emm "Sólo bromeaba. Compartimos cara y genes. Compartamos familia también."
    mcp "(¡Esa es mi hermanita!)"
    call BlinkXP ("c17s001_565" , "d") from _call_BlinkXP_2019
    mc "¿Ves? ¿Te convences ahora?"
    scene c17s001_570An with dissolve #abcd (d con h) le va cambiando la expresión y sale corriendo
    ama "Yo... yo..."
    ama "Necesito un momento..."
    mc "¡Espera Amanda!"
    scene c17s001_480b with dissolve
    mc "Voy a buscarla... ahora volvemos..."
    scene c17s001_575d with fade
    mc "Amanda, ¿estás bien? ¿Qué pasa?"
    ama "N-nada... sólo necesito un momento..."
    mc "Pero ¿estás bien?"
    call BlinkXP ("c17s001_575" , "h") from _call_BlinkXP_2020
    ama "¡Joder, [mc]! ¡Te he dicho que necesito un momento!"
    mc "Vale. Estaré dentro si me necesitas. Estaré dondequiera que me necesites. Siempre."
    scene c17s001_580d with dissolve #toma de los dos, MC yéndose
    pause (0.8)
    scene c17s001_580e with hpunch #le coge de la mano
    pause (0.8)
    scene c17s001_580f with hpunch #le coge de la mano, toma general
    pause (0.8)
    call BlinkXP ("c17s001_580" , "h") from _call_BlinkXP_2021 #abrazo
    ama "*Sollozo* Lo siento, [mc]."
    mc "Shhhh... no hace falta, Amanda. Podemos ser un poco intensos."
    ama "*Sollozo* Eva me había avisado..."
    mc "¿Tan malos somos?"
    call BlinkXP ("c17s001_585" , "d") from _call_BlinkXP_2022 #lo mira sonriendo
    ama "*Sollozo* No me refiero a eso... me había avisado de los ninjas cortadores de cebollas que tenéis en la cocina."
    mc "*Risa* Lo más parecido a unos ninjas que han pisado esa cocina sois vosotras."
    mc "¿Entiendes ahora por qué me siento orgulloso de esta familia?"
    call BlinkXP ("c17s001_590" , "d") from _call_BlinkXP_2023
    ama "*Sollozo* Tienes razones para estarlo... sois increíbles..."
    mc "Pues sabes que solo te falta una cosa para formar parte de esto, ¿verdad?"
    call KissXP ("c17s001_595" , "h") from _call_KissXP_60
    ama "¿Esto? *Risita*"
    mc "No me refería a eso, pero es un paso. *Risa*"
    mc "Quería decir que te falta creerte que puedes formar parte de esta familia. Ya has visto que todas os aceptan y quieren que lo hagáis."
    call BlinkXP ("c17s001_600" , "d") from _call_BlinkXP_2024
    ama "¿Tú te lo creerías en nuestro caso? O en tu propio caso. Conoces a una familia hoy, y hoy mismo te están diciendo que perteneces a esa familia."
    ama "No es normal, [mc]."
    mc "No somos normales, Amanda. Ni nosotros ni vosotras."
    mc "Seguramente con cualquier otra familia sería raro, pero... ¿con los Marks? No."
    mc "Las estudiantes hace una semana que llegaron y puedes ver que empiezan a sentirse parte de la familia."
    mc "No voy a hablar de Eileen o Scarlett, pero puedes ver que Kiara va por el mismo camino, y lleva... ¿cuánto? ¿Tres días aquí?"
    call BlinkXP ("c17s001_605" , "d") from _call_BlinkXP_2025
    ama "¡Pero todas ellas os han conocido durante más tiempo que nosotras!"
    mc "Te equivocas. Hace tres meses que conoces y vigilas a la familia. Que las estudias. Seguramente sabes más de cada uno de nosotros de lo que nosotros conocemos de otros."
    ama "¡Pero ellas no me conocen de nada! ¡Podría ser una asesina en serie!"
    mc "¿Puedes dejar de buscar excusas para no sentirte aceptada? No intentes entendernos, y menos aún entender a las mujeres de la familia. Hace más tiempo que las conozco y aún no lo he conseguido."
    mc "En esta familia todo el mundo es intenso. Aman y odian con intensidad. Los sentimientos brotan a una velocidad que parecería rara fuera de esta casa."
    mc "No lo analices. Disfrútalo. Te quieren en la familia y tú quieres estar en ella. Haz que sea posible. No huyas de nosotros y mañana lo verás de otra forma."
    call BlinkXP ("c17s001_610" , "h") from _call_BlinkXP_2026
    ama "Gracias, [mc]. Por cierto... te odio..."
    mc "¿Por qué? ¿Qué he hecho ahora? Eso ha sonado muy a [emm]."
    ama "Hacía siete años que no lloraba. Ese espectáculo que has dado ahí dentro no era necesario."
    mc "Sí que lo era, Amanda. Era necesario para que vieras que no sólo somos [mar], [nor], y yo los que pensamos así."
    mc "Pero dejemos el tema. ¿Quieres volver dentro?"
    call BlinkXP ("c17s001_615" , "d") from _call_BlinkXP_2027
    ama "Sí, pero... ¿se me ha corrido mucho el maquillaje?"
    mc "No demasiado. Pareces un grafiti de mapache descolorido bajo la lluvia. *Risa*"
    call BlinkXP ("c17s001_620" , "d") from _call_BlinkXP_2028
    ama "¡Capullo! *Risa*"
    ama "Voy al lavabo a arreglarme y ahora vuelvo a la cocina."
    stop music fadeout (1.5)
    mc "Te espero allí."
    call BlinkXP ("c17s001_625" , "f") from _call_BlinkXP_2038
    play music ("music/Fragile-Beauty.ogg")
    kim "¿Está bien?"
    mc "Sí, un poco abrumada, pero bien. Creo que lo que le habéis dicho todas le ha afectado un poco."
    call BlinkXP ("c17s001_630" , "d") from _call_BlinkXP_2039
    kim "Kate y yo estábamos hablando sobre ello mientras estabais fuera."
    kim "Si el primer día 16 mujeres nos hubieran dicho que somos de la familia no sé cómo nos lo hubiéramos tomado. Seguramente nos hubiéramos reído y no nos lo hubiéramos creído."
    kim "O habríamos salido corriendo."
    mc "Kim, tú sabes lo que es una familia. Y ahora entiendes que si lo hubiéramos dicho el primer día lo hubiéramos sentido."
    mc "Tardamos cinco días en decirlo."
    call BlinkXP ("c17s001_635" , "d") from _call_BlinkXP_2040
    kim "Y durante esos cinco días vimos lo suficiente como para saber que lo decíais en serio."
    kim "Para Amanda y Eva es su primer día. Tenlo en cuenta."
    mc "Sí. Tienes razón..."
    $ Aux = 0
    if kim._var("kissedBeach") and kim.rps > 6:
        $ Aux = 1
    elif kim.rps > 0:
        $ Aux = 1
    if Aux == 1:
        mc "Cambiando de tema... no hemos tenido oportunidad de hablar de lo que pasó en la playa."
        call BlinkXP ("c17s001_640" , "d") from _call_BlinkXP_2041
        kim "¿Hay algo de lo que hablar?"
        mc "Me besaste..."
        if kim._var("kissedBeach"):
            kim "Y tú me besaste a mí..."
        else:
            kim "Pero tú no me besaste a mí..."
        mc "Por eso creo que deberíamos hablar."
        call BlinkXP ("c17s001_645" , "d") from _call_BlinkXP_2042
        kim "No sé si es buena idea. Es lo malo de ser familia, ¿no? No estaría bien que me enrollase con alguien de la familia, supongo."
        call BlinkXP ("c17s001_650" , "d") from _call_BlinkXP_2043
        kim "Aquel día... te va a parecer una tontería, incluso más que celebrar la Navidad en verano y que lo único navideño fueran los bikinis y los gorros."
        kim "Celebrar una falsa Navidad, una fiesta que normalmente se pasa en familia, es lo que nos ha llevado a esto."
        kim "Debbie decía que parecía más Navidad que algunas de las Navidades que ha pasado con su familia... de sangre."
        mc "En eso consistía, ¿no? En estrechar lazos con todo el mundo."
        mc "No creía que de ese día saliera un sentimiento tan familiar, pero le doy la bienvenida a que nos sintamos así."
        call BlinkXP ("c17s001_655" , "d") from _call_BlinkXP_2044
        kim "¡Oh! No me malinterpretes... me encanta eso... pero eso podría evitar que tú y yo..."
    call BlinkXP ("c17s001_660" , "d") from _call_BlinkXP_2045
    if kat._var("kissedBeach"):
        kat "¿Cómo están mis dos besucones favoritos?"
    kat "¿Interrumpo algo?"
    call BlinkXP ("c17s001_665" , "d") from _call_BlinkXP_2046
    kim "No, Kate, estábamos hablando de la familia y de cómo de abrumada se ha tenido que sentir Amanda."
    call BlinkXP ("c17s001_670" , "d") from _call_BlinkXP_2047
    kat "Es que yinz habéis dicho cosas muy chulas. Yo solo he remarcado el parecido con las chicas... me siento tonta." #YINZ
    mc "¿Yinz?"
    scene c17s001_680a with dissolve
    kat "Perdón... todos vosotros... argot de Pittsburgh."
    mc "Creo que no lo había oído nunca..."
    kim "Los fans de los Steelers no saben hablar. *Risa* Go Browns!"
    mc "Pero no te tienes que sentir tonta, todas habéis dicho algo que la ha hecho sentir acogida."
    scene c17s001_680b with dissolve
    kat "¿Tú ya se lo has dicho, Kim?"
    kim "No, aún no. Hoy había cosas más importantes de las que hablar."
    mc "¿Qué me tenías que contar?"
    call BlinkXP ("c17s001_685" , "d") from _call_BlinkXP_2048
    kim "No es nada importante. Me han llamado para mi primer trabajillo desde que estoy aquí."
    kim "De azafata en un evento de negocios la semana que viene."
    mc "¡Eso es fantástico, Kim! ¿Estás contenta?"
    call BlinkXP ("c17s001_690" , "d") from _call_BlinkXP_2049
    kim "Por un lado sí, es mi primer trabajo en California. Y sólo han tardado una semana en avisarme..."
    kim "Por otro lado... me han dicho en la agencia que han preguntado específicamente por mí. Temo que sea... ya sabes... por mi piel..."
    mc "No me extrañaría que fuera por eso. Eso te hace única y especial. Única y especialmente hermosa."
    scene c17s001_680c with dissolve
    kat "No te quejes, Kim, a mí nunca me dice cosas así... *Risa*"
    call BlinkXP ("c17s001_695" , "d") from _call_BlinkXP_2050
    kat "¡No es que quiera que me las digas! ¡Son demasiado cursis para mi gusto!"
    mc "Si te sirve de algo, tus ojos entrarían en la competición por los más bonitos que he visto."
    scene c17s001_680d with dissolve
    kim "*Risa* ¿Lo ves Kate? Si te abres a los piropos, los recibes. Y [mc] siempre tiene uno preparado."
    kat "Lo sé, lo sé... Nunca sabes cuándo va a hacer que te ruborices..."
    mc "Si os incomoda, puedo dejar de hacerlo."
    scene c17s001_680e with dissolve
    kat "¡Ni te atrevas!" (multiple=2)
    kim "¡Ni se te ocurra!" (multiple=2)
    scene c17s001_680f with dissolve
    kat "*Risa* ¡Perra mala!" (multiple=2)
    kim "¡Perra celosa! *Risa*" (multiple=2)
    mc "*Risa* No hace falta que os peleéis. Las dos sois preciosas."
    scene c17s001_680g with dissolve
    kat "Vale. Hasta aquí. Me estoy notando las mejillas arder. Y eso que no se puede ser más cursi que tú."
    kim "Creo que te vamos a dejar solo antes de que nos ruboricemos más aún. Vamos a charlar un rato más con Amanda."
    mc "Entonces me quedaré aquí, solo y desconsolado. *Risa*"
    scene c17s001_700An with dissolve #varias imágenes de las chicas
    "El resto de la velada se desarrolla entre risas, anécdotas, y más abrazos."
    "Los grupos se crean, cambian, y se deshacen. Todo el mundo quiere hablar con Amanda. Amanda quiere hablar con todo el mundo."
    "Es un día que difícilmente podrá olvidar. Ni ella ni Eva podrán hacerlo nunca."
    "Es el primero de muchos días por llegar. Pero todo tiene que llegar a su fin, incluso una fantástica cena familiar."
    stop music fadeout (1.5)
    call BlinkXP ("c17s001_705" , "d") from _call_BlinkXP_2029
    ama "[mc], ¿puedo pedirte que me lleves de nuevo a la base?"
    play music ("music/Wonder.ogg")
    ama "Eva apenas durmió ayer y debería relevarla. Y pedir un Under no es lo mejor."
    mc "Ya me imagino que lo de \"lléveme a la base secreta\" no es algo que se pueda hacer. *Risa* Parecería de villano de película de serie B."
    mc "Despidámonos de todo el mundo y te llevo."
    call BlinkXP ("c17s001_710" , "f") from _call_BlinkXP_2051
    "Unos minutos después, en la base..."
    ama "Pues aquí acaba la noche."
    mc "La primera de muchas. Mañana te toca venir a comer, y el domingo es el cumpleaños de las chicas."
    mc "¿Te lo has pasado bien?"
    call BlinkXP ("c17s001_710b" , "d") from _call_BlinkXP_2052
    ama "Si exceptuamos al capullo que me ha hecho llorar, sí. Ha sido increíble."
    mc "Pues solo ha sido la primera. Cuando dejes de sentirte... ¿cómo lo has dicho? Ah, sí, como un animal exhibido... todo será mejor aún."
    mc "Sólo tienes que venir muchas veces a casa."
    call BlinkXP ("c17s001_715" , "d") from _call_BlinkXP_2053
    ama "Y tú y yo tenemos pendiente un café para hablar de mis ideas respecto a NTR."
    mc "¿Te parece bien un día la semana que viene?"
    ama "Perfecto. Ahora voy a relevar a Eva. Se debe estar cayendo de sueño. Pero antes de eso..."
    scene c17s001_720An with dissolve #a-b beso
    ama "Buenas noches, [mc]."
    "El beso de Amanda es un poco más largo de lo que debería ser un beso de buenas noches. No hay lujuria en él, pero hay mucho agradecimiento."
    stop music fadeout (1.5)
    "Mucha tensión liberada."
    scene c17s001_725a with dissolve
    play music ("music/Throne-King.ogg")
    eva "¡Amanda!"
    if not _in_replay:
        $ renpy.notify ("Profile Image unlocked for Eva: 12 - Special Business")
        $ eva.profileImages.pop (11) # first remove
        $ eva.profileImages.insert (11, ("eva_11", None)) # then add new
    scene c17s001_725b with dissolve
    eva "Tengo..."
    scene c17s001_725c with dissolve
    eva "Tengo... buenas..."
    call BlinkXP ("c17s001_725b" , "d") from _call_BlinkXP_2054
    eva "Tengo... buenas... noticias..."
    call BlinkXP ("c17s001_730" , "h") from _call_BlinkXP_2055
    eva "¡Amanda!"
    call BlinkXP ("c17s001_735" , "d") from _call_BlinkXP_2056
    ama "¿Qué pasa, Eva?"
    mc "Hola Eva."
    call BlinkXP ("c17s001_730" , "d") from _call_BlinkXP_2057
    eva "*Gruñido* ¿Qué ha sido ese beso?"
    mc "Nos estábamos despidiendo."
    call BlinkXP ("c17s001_735" , "d") from _call_BlinkXP_2058
    ama "Tan solo era un beso de buenas noches, Eva."
    call BlinkXP ("c17s001_740" , "d") from _call_BlinkXP_2059
    eva "Los besos de buenas noches deberían ser más cortos."
    mc "No hay una duración fijada para los besos, Eva."
    scene c17s001_745An with hpunch #a-b beso
    "Eva se lanza a tus brazos y te da un largo beso. Puedes notar como sus labios se van curvando en una sonrisa de desafío tal como pasan los segundos."
    "Te está desafiando a que cortes el beso, a que le demuestres que ella es menos que su hermana, menos que Amanda."
    "No piensas hacerlo."
    "Es una reacción tan típica de [emm] que sabes cómo acabaría."
    call BlinkXP ("c17s001_750a" , "d") from _call_BlinkXP_2060
    eva "Buenas noches, [mc]."
    call BlinkXP ("c17s001_750b" , "d") from _call_BlinkXP_2061
    eva "Buenas noches, Amanda..."
    call BlinkXP ("c17s001_755" , "d") from _call_BlinkXP_2062
    ama "Pero ¿cuáles eran las noticias?"
    scene c17s001_745c with dissolve #de espaldas yéndose
    eva "Aaron ha conseguido contactar con los agentes que quedaban. Ya no hay nadie en peligro."
    eva "Y ya he cambiado la rueda de la furgoneta. Ya no hará falta que molestes a [mc] para que venga a recogerte."
    mc "No es ninguna..."
    scene c17s001_745d with hpunch #portazo
    "*Blam*"
    call BlinkXP ("c17s001_755b" , "d") from _call_BlinkXP_2063
    mc "... molestia."
    mc "Eso ha sido muy típico de [emm]."
    ama "Creo que vamos a tener que evitar que pasen mucho tiempo juntas. Parece que se retroalimentan."
    mc "Hasta llevaba un vestido rosa..."
    ama "Supongo que se ha estado probando ropa para mañana. *Risita*"
    call KissXP ("c17s001_720" , "d") from _call_KissXP_61
    ama "Voy a ir dentro a hablar con ella. Gracias por esta noche, [mc]. Nos vemos mañana."
    stop music fadeout (1.5)
    mc "Hasta mañana, Amanda."
    return
label c17s001_AlexiaPregnancyResult:
    if _in_replay and not AuxReplay:
        call mrS3_oma_pregnant from _call_mrS3_oma_pregnant_4
    call BlinkXP ("c17s001_350" , "f") from _call_BlinkXP_2064
    stop music fadeout (1.5)
    "Al volver a la cocina, Alexia, que han llegado mientras estabas con las hermanas, se acercan a ti."
    play music ("music/Salsa.ogg")
    oma "Hola, guapísimo. Vengo a arrestarte."
    oma "La máquina debe haber acabado ya."
    mc "¿Quieres ir ahora? La cena..."
    call BlinkXP ("c17s001_355" , "d") from _call_BlinkXP_2065
    oma "No te preocupes, he estado hablando con Betty y con [nor]. Si nos vamos ahora, discretamente, nadie se dará cuenta."
    mc "Vamos entonces."
    call BlinkXP ("c17s001_360" , "f") from _call_BlinkXP_2066
    "En tu habitación..."
    mc "Tu test está en ese cajón, Alexia. Ve a por él. ¿Nerviosa?"
    oma "Un poco. Aún no estoy segura de lo que quiero. Siempre me imaginé teniendo a mi primer hijo a los 30 o así."
    mc "Yo también. Pero solo hay una forma de saberlo. Ve a por él."
    scene c17s001_255d with dissolve
    "..."
    if oma._var("pregnant"):
        call BlinkXP ("c17s001_255a" , "d") from _call_BlinkXP_2067
        $ oma._var("pregnancyDiscovered", True)
        oma "¡Positivo!"
        mc "¡Bien! Parece que has descubierto lo que quieres. Ven aquí."
        oma "Lo he descubierto en el momento en que he puesto la mano en el cajón. He descubierto que quería que saliera verde."
        mc "Ven aquí. Quiero un abrazo de la futura madre."
        call BlinkXP ("c17s001_365" , "f") from _call_BlinkXP_2068
        "Os fundís en un abrazo lleno de alegría y de esperanza en que todo vaya bien durante el embarazo."
    else:
        call BlinkXP ("c17s001_255b" , "d") from _call_BlinkXP_2069
        oma "Negativo..."
        mc "Oh, Alexia, lo siento..."
        oma "No te preocupes, he descubierto que quería que saliera verde en el momento en que he puesto la mano en el cajón. Pero tendremos más oportunidades."
        oma "Los dos somos jóvenes y tenemos mucho tiempo para seguir intentándolo. Intentarlo es divertido."
        mc "Ven aquí. Quiero un abrazo de la futura madre, aunque tardes un poco más."
        call BlinkXP ("c17s001_365" , "f") from _call_BlinkXP_2070
        "Os fundís en un abrazo lleno de esperanza en que la próxima vez cambie el resultado del siguiente test."
    "Es un abrazo lleno de caricias y besos. Es bueno saber que estáis juntos en esto."
    call BlinkXP ("c17s001_265a" , "d") from _call_BlinkXP_2071
    oma "Deberíamos volver a la cena antes de que alguien sospeche de nuestra ausencia."
    if oma._var("pregnant"):
        oma "¿Cuándo quieres decírselo a la familia? Porque quieres decírselo, ¿verdad?"
        mc "Por supuesto que quiero decírselo. Pero este fin de semana siempre ha sido especial para [emm], [dap], y [eri]."
        mc "La presencia de Eva y Amanda ya les ha robado suficiente protagonismo."
        mc "¿Te importa si dejamos pasar unos días?"
        if not eil._var("pregnant"):
            mc "A lo mejor podemos hacer el test de Eileen y sale positivo tras el columpio. Lo podemos hacer mañana por la tarde y lo sabríamos el lunes."
        oma "No tengo ningún problema en esperar. No tengo de qué esconderme, pero entiendo lo que dices."
        call BlinkXP ("c17s001_265b" , "d") from _call_BlinkXP_2072
        mc "Y sobre lo de seguir trabajando..."
        oma "No voy a dejar de trabajar, [mc]. Estoy embarazada, no inválida. Y esto es Newport, no Los Angeles. Aquí no hay peligro de meterme en un tiroteo."
        oma "Cuando el embarazo esté un poco avanzado, quizás pida hacer trabajo de oficina, pero hasta entonces quiero seguir haciendo vida normal."
        mc "Okay, si es lo que te parece bien, no voy a llevarte la contraria."
    oma "Vamos. Tengo ganas de seguir conociendo a Amanda. Me he perdido a Eva esta mañana, pero Amanda me parece muy interesante."
    return
label c17s001_EileenPregnancyResult:
    if _in_replay and not AuxReplay:
        menu:
            "¿Eileen está embarazada?"
            "Si":
                $ eil._var("pregnant" , True)
            "No":
                $ eil._var("pregnant" , False)
    call BlinkXP ("c17s001_300" , "f") from _call_BlinkXP_2073
    stop music fadeout (1.5)
    "Al volver a la cocina, Eileen, que han llegado mientras estabas con las hermanas, se acercan a ti."
    play music ("music/LostVoices.ogg")
    eil "Hola, [mc]. Vengo a secuestrarte."
    eil "Hay una... máquina... que debe haber acabado su proceso."
    mc "¿Quieres ir ahora? La cena..."
    call BlinkXP ("c17s001_305" , "d") from _call_BlinkXP_2074
    eil "No te preocupes, he saludado a todo el mundo y están ocupadas con Amanda."
    eil "Si nos vamos ahora nadie se dará cuenta."
    mc "Vamos entonces."
    call BlinkXP ("c17s001_310" , "f") from _call_BlinkXP_2075
    "En tu habitación..."
    mc "Tu test está en ese cajón, Eileen. Ve a por él. ¿Nerviosa?"
    eil "Un poco. Llevo días pensando y tengo ganas de que salga positivo."
    mc "Yo también. Pero solo hay una forma de saberlo. Ve a por él."
    scene c17s001_260d with dissolve
    "..."
    if eil._var("pregnant"):
        call BlinkXP ("c17s001_260a" , "d") from _call_BlinkXP_2076
        $ eil._var("pregnancyDiscovered", True)
        eil "¡Dos verdes! ¡Positivo! ¡Vamos a ser padres!"
        mc "¡Ven aquí, Mami!"
        call BlinkXP ("c17s001_315" , "f") from _call_BlinkXP_2077
        "Os fundís en un abrazo lleno de alegría y de esperanza en que todo vaya bien durante el embarazo."
    else:
        call BlinkXP ("c17s001_260b" , "d") from _call_BlinkXP_2078
        eil "Verde y rojo... negativo..."
        mc "Lo siento, Eile."
        eil "No pasa nada, cielo. No suele ser el sueño de todas las chicas quedarse embarazada con 21. Y a lo mejor en el columpio lo logramos. Tenemos mucho tiempo."
        mc "Todo el tiempo del mundo. Ven aquí."
        call BlinkXP ("c17s001_315" , "f") from _call_BlinkXP_2079
        "Os fundís en un abrazo lleno de esperanza en que el columpio cambie el resultado del siguiente test."
    "Es un abrazo lleno de caricias y besos. Es bueno saber que estáis juntos en esto."
    call BlinkXP ("c17s001_270" , "d") from _call_BlinkXP_2080
    if eil._var("pregnant"):
        mc "¿Vas a poder seguir trabajando ahora que estás embarazada? No sé si va a ser bueno para el bebé que estés tantas horas de pie."
        eil "No hay ningún problema, [mc]. Hay una camarera en el Triangle Dinner que está embarazada de seis meses y dice que no hay ningún problema."
        mc "¿Has hablado con otras camareras?"
        call BlinkXP ("c17s001_320" , "d") from _call_BlinkXP_2081
        eil "Claro, tenía que estar preparada, ¿no? Después de tantos días con síntomas, he hablado con todo el mundo que he podido... menos con mi madre"
        mc "Bueno, quizás con todo lo que está pasando no sea lo mejor, pero es algo que tú sabes mejor que nadie."
        call BlinkXP ("c17s001_325" , "d") from _call_BlinkXP_2082
        eil "Me gustaría decírselo lo antes posible, si no te importa. Y me gustaría que se lo dijéramos juntos."
        mc "¿Mañana por la mañana te va bien que se lo digamos? Hoy va a ser un poco complicado. Al acabar la cena tengo que llevar a Amanda de nuevo a su base."
        eil "Genial. Mañana se lo contamos. Tengo ganas de ver qué cara pone. ¡Va a ser abuela!"
        mc "Sobre todo hay que decirle que, esta vez, guarde el secreto. Prefiero que no se le vuelva a escapar como en la cocina el otro día."
        eil "Es mala guardando secretos. *Risa* Pero me aseguraré de que este lo guarde."
    eil "Vamos. Tengo ganas de seguir conociendo a Amanda. Es tan diferente a [emm]..."
    return
label c17s001_EileenAlexiaPregnancyResult:
    if _in_replay and not AuxReplay:
        menu:
            "¿Alexia está embarazada?"
            "Si":
                $ oma._var("pregnant" , True)
            "No":
                $ oma._var("pregnant" , False)
        menu:
            "¿Eileen está embarazada?"
            "Si":
                $ eil._var("pregnant" , True)
            "No":
                $ eil._var("pregnant" , False)
    scene c17s001_250a with fade
    stop music fadeout (1.5)
    "Al volver a la cocina, Alexia y Eileen, que han llegado mientras estabas con las hermanas, se acercan a ti."
    play music ("music/ChillUkelele.ogg")
    oma "Hola, [mc]. Quedas arrestado." (multiple=2)
    eil "Hay unas... máquinas... que deben haber acabado su proceso." (multiple=2)
    mc "¿Queréis ir ahora? La cena..."
    scene c17s001_250b with dissolve
    oma "No te preocupes, hemos saludado a todo el mundo y están ocupadas con Amanda."
    eil "Si nos vamos ahora nadie se dará cuenta."
    mc "Vamos entonces."
    scene c17s001_250c with fade
    "En tu habitación..."
    mc "El tuyo está en ese cajón, Alexia. Y el tuyo en el del otro lado de la cama, Eileen."
    oma "¿Nerviosos?"
    eil "Un poco. Llevo días pensando y tengo ganas de que salga positivo."
    mc "Yo también. Los dos."
    oma "Yo aún no estoy segura de lo que quiero. Siempre me imaginé teniendo a mi primer hijo a los 30 o así."
    mc "Venga, chicas. Solo hay una forma de saberlo."
    scene c17s001_255d with dissolve
    "..."
    if oma._var("pregnant"):
        $ oma._var("pregnancyDiscovered", True)
        call BlinkXP ("c17s001_255a" , "d") from _call_BlinkXP_2083
        oma "¡Positivo!"
        mc "¡Bien! Parece que has descubierto lo que quieres. Ven aquí."
        oma "Lo he descubierto en el momento en que he puesto la mano en el cajón. He descubierto que quería que saliera verde."
        mc "Ven aquí. Quiero un abrazo de la futura madre."
    else:
        call BlinkXP ("c17s001_255b" , "d") from _call_BlinkXP_2084
        oma "Negativo..."
        mc "Oh, Alexia, lo siento..."
        oma "No te preocupes, he descubierto que quería que saliera verde en el momento en que he puesto la mano en el cajón. Pero tendremos más oportunidades."
        mc "Ven aquí. Quiero un abrazo de la futura madre, aunque tardes un poco más."
    mc "Eileen, ¿qué ha salido en el tuyo?"
    scene c17s001_260d with dissolve
    "..."
    if eil._var("pregnant"):
        call BlinkXP ("c17s001_260a" , "d") from _call_BlinkXP_2085
        $ eil._var("pregnancyDiscovered", True)
        eil "¡Dos verdes! ¡Positivo! ¡Vamos a ser padres!"
        mc "¡Ven aquí, Mami!"
    else:
        call BlinkXP ("c17s001_260b" , "d") from _call_BlinkXP_2086
        eil "Verde y rojo... negativo..."
        mc "Lo siento, Eile."
        eil "No pasa nada, cielo. No suele ser el sueño de todas las chicas quedarse embarazada con 21. Y a lo mejor en el columpio lo logramos. Tenemos mucho tiempo."
        mc "Todo el tiempo del mundo. Ven aquí."
    scene c17s001_265d with dissolve
    "Los tres os fundís en un abrazo lleno de esperanza por lo que está por llegar."
    if oma._var("pregnant") and eil._var("pregnant"):
        "Os felicitáis mutuamente en un extraño baile de besos y abrazos. Parece ser que esos críos acaban de ganar una tía inesperada."
        "Puedes notar que les ha hecho ilusión quedarse embarazadas a la vez."
    elif oma._var("pregnant") or eil._var("pregnant"):
        "Os felicitáis y consoláis mutuamente en un extraño baile de besos y abrazos. Un positivo y un negativo te dejan un sabor agridulce."
        "Pero parece ser que este crío acaba de ganar una tía inesperada. También hay esperanza en que en breve el segundo test salga positivo."
        "Puedes notar que les hubiera hecho ilusión quedarse embarazadas a la vez."
    else:
        "Os consoláis mutuamente en un extraño baile de besos y abrazos. Dos negativos simultáneos te dejan un sabor amargo en la boca."
        "Pero también ayuda a que ellas se consuelen mutuamente. Hay esperanza en que en breve una nueva ronda de tests cambien los resultados."
        "Puedes notar que les hubiera hecho ilusión quedarse embarazadas a la vez. Es casi mejor que ninguna lo esté a que solo lo estuviera una."
    "La relación entre Eileen y Alexia se ha ido haciendo más fuerte desde aquel día en el lago. Hay que repetirlo."
    call BlinkXP ("c17s001_265a" , "d") from _call_BlinkXP_2087
    oma "Deberíamos volver a la cena antes de que alguien sospeche de nuestra ausencia."
    if oma._var("pregnant"):
        oma "¿Cuándo quieres decírselo a la familia? Porque quieres decírselo, ¿verdad?"
        mc "Por supuesto que quiero decírselo. Pero este fin de semana siempre ha sido especial para [emm], [dap], y [eri]."
        mc "La presencia de Eva y Amanda ya les ha robado suficiente protagonismo."
        mc "¿Te importa si dejamos pasar unos días?"
        if not eil._var("pregnant"):
            mc "A lo mejor podemos hacer el test de Eileen y sale positivo tras el columpio. Lo podemos hacer mañana por la tarde y lo sabríamos el lunes."
        oma "No tengo ningún problema en esperar. No tengo de qué esconderme, pero entiendo lo que dices."
        call BlinkXP ("c17s001_265b" , "d") from _call_BlinkXP_2088
        mc "Y sobre lo de seguir trabajando..."
        oma "No voy a dejar de trabajar, [mc]. Estoy embarazada, no inválida. Y esto es Newport, no Los Angeles. Aquí no hay peligro de meterme en un tiroteo."
        oma "Cuando el embarazo esté un poco avanzado, quizás pida hacer trabajo de oficina, pero hasta entonces quiero seguir haciendo vida normal."
        mc "Okay, si es lo que te parece bien, no voy a llevarte la contraria."
    call BlinkXP ("c17s001_270" , "d") from _call_BlinkXP_2089
    if eil._var("pregnant"):
        mc "¿Vas a poder seguir trabajando ahora que estás embarazada? No sé si va a ser bueno para el bebé que estés tantas horas de pie."
        eil "No hay ningún problema, [mc]. Hay una camarera en el Triangle Dinner que está embarazada de seis meses y dice que no hay ningún problema."
        mc "¿Has hablado con otras camareras?"
        call BlinkXP ("c17s001_320" , "d") from _call_BlinkXP_2090
        eil "Claro, tenía que estar preparada, ¿no? Después de tantos días con síntomas, he hablado con todo el mundo que he podido... menos con mi madre"
        mc "Bueno, quizás con todo lo que está pasando no sea lo mejor, pero es algo que tú sabes mejor que nadie."
        call BlinkXP ("c17s001_325" , "d") from _call_BlinkXP_2091
        eil "Me gustaría decírselo a mi madre lo antes posible, si no te importa. Y me gustaría que se lo dijéramos juntos."
        mc "¿Mañana por la mañana te va bien que se lo digamos? Hoy va a ser un poco complicado. Al acabar la cena tengo que llevar a Amanda de nuevo a su base."
        eil "Genial. Mañana se lo contamos. Tengo ganas de ver qué cara pone. ¡Va a ser abuela!"
        mc "Sobre todo hay que decirle que, esta vez, guarde el secreto. Prefiero que no se le vuelva a escapar como en la cocina el otro día."
        eil "Es mala guardando secretos. *Risa* Pero me aseguraré de que este lo guarde."
    eil "Vamos. Tengo ganas de seguir conociendo a Amanda. Es tan diferente a [emm]..."
    oma "Después de no haber conocido a Eva, me parece buena idea."
    return
label c17s002_MaddieResidence:
    scene c17s002_005e with dissolve
    "Vuelves a casa y te pones a jugar un rato a My Residence."
    "Hoy toca cita con Dee-Dee. La dependienta de la ferretería."
    "Después de jugar un rato te acuestas y no sueñas."
    return
label c17s002_MaddieDate:
    if _in_replay:
        $ mad._var("pregnant" , False)
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
                menu:
                    "¿Espiaste a [mar!t] en el probador de la tienda de [mad.nick]?"
                    "Sí":
                        $ mar._var("fittingRoom", True)
                        menu:
                            "¿Qué tipo de relación tienes con Maddie?"
                            "Romance":
                                $ mad._var("romance", True)
                                $ mad._var("dom", False)
                                $ mad._var("sub", False)
                            "Acepté el chantaje.":
                                $ mad._var("romance", False)
                                $ mad._var("dom", True)
                                $ mad._var("sub", False)
                            "Le di la vuelta al chantaje.":
                                $ mad._var("romance", False)
                                $ mad._var("dom", False)
                                $ mad._var("sub", True)
                    "No":
                        $ mar._var("fittingRoom", False)
                        $ mad._var("romance", True)
                        $ mad._var("dom", False)
                        $ mad._var("sub", False)
            "No":
                $ mar._var("route" , False)
                $ mar._var("fittingRoom", False)
                $ mad._var("romance", True)
                $ mad._var("dom", False)
                $ mad._var("sub", False)
    scene black with dissolve
    "Llamas a Maddie para decirle que vas en camino en cuanto te subes a la camioneta."
    $ Whatif=False
    $ WI=""
    if mad._var("romance"):
        call c17s002_MaddieRomance from _call_c17s002_MaddieRomance
    elif mad._var("sub"):
        call c17s002_MaddieSub from _call_c17s002_MaddieSub
    elif mad._var("dom"):
        call c17s002_MaddieDom from _call_c17s002_MaddieDom
    if not _in_replay:
        $ Whatif=True
    scene black with dissolve
    "Vuelves a casa y te acuestas. Tienes sueños muy extraños."
    while Whatif:
        scene black with dissolve
        menu:
            "Ver la escena de Romance":
                call c17s002_MaddieRomance from _call_c17s002_MaddieRomance_1
                $ WI ="Rom"
            "Ver la escena con Maddie Sumisa":
                $ WI ="Sub"
                call c17s002_MaddieSub from _call_c17s002_MaddieSub_1
            "Ver la escena con Maddie Dominante":
                $ WI ="Dom"
                call c17s002_MaddieDom from _call_c17s002_MaddieDom_1
            "Continuar la historia":
                $ Whatif = False
    return
label c17s002_MaddieDom:
    "Llegas a casa de Maddie mucho más tarde de lo que habías esperado llegar. La verdad es que tenías muchas ganas de verla."
    "Esperas que no esté demasiado enfadada."
    scene c17s002_005d with dissolve
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    call BlinkXP("c17s002_500", "d") from _call_BlinkXP_2092
    play music ("music/Fragile-Beauty.ogg")
    mad "Me estaba impacientando. Desde que has llamado se me ha hecho eterno."
    mc "Lo siento, Maddie. La cosa se ha liado más de lo esperado."
    call KissXP("c17s002_505", "d") from _call_KissXP_62
    mad "Bueno, al menos ya estás aquí. Pasa."
    mc "¿Esa era la sorpresa de la que me hablaste cuando te llamé? Estás preciosa."
    scene c17s002_510d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not Whatif:
        if not _in_replay:
            $ mad.profileImages.pop (7) # first remove
            $ mad.profileImages.insert (7, ("maddie_12", "route")) # then add new
            $ mad.profileImages.pop (11) # first remove
            $ mad.profileImages.insert (11, ("maddie_11", "route")) # then add new
            $ mad.profileImages.pop (12) # first remove
            $ mad.profileImages.insert (12, ("maddie_7", "route")) # then add new
            $ renpy.notify ("Profile Images unlocked for Maddie: 8-12-13 - Lingerie")
    call BlinkXP("c17s002_510" , "d") from _call_BlinkXP_2093
    mad "Esperaba que te gustara, por eso lo he comprado."
    mc "Me encanta. Estás increíble."
    python:
        if "zeu" not in globals () or not isinstance (hm, TGCharacter):
            zeu = TGCharacter ("Zeus", color = "#0023ff")
            cat = TGCharacter (_("Jodido Gato"), color = "#0023ff")
    call c17s002_ZeusArrival from _call_c17s002_ZeusArrival
    stop music fadeout (1.5)
    mad "Antes quiero un beso."
    scene c17s002_520pv with dissolve
    show c17s002_520v with dissolve
    play music ("music/Between-Heaven-And-Earth.ogg")
    "Maddie te atrae hacia sus labios, que se juntan en un beso largamente deseado."
    "Que ella lleve ese mono sexy mientras tú estás completamente vestido le da un punto de cita secreta que te pone cachondo."
    "El tórrido beso hace que cuando vuestros labios se separen, Mjolnir se sienta presionado dentro de tus pantalones."
    call BlinkXP("c17s002_075c", "d") from _call_BlinkXP_2094
    hide c17s002_520v
    mad "[mc]... ¿hace calor aquí o es que me has puesto cachondísima? Creo que tú llevas demasiada ropa..."
    scene c17s002_080cd with dissolve
    pause (0.8)
    call BlinkXP("c17s002_080c", "d") from _call_BlinkXP_2095
    mad "Voy a solucionarlo... esta camisa sobra..."
    mc "Se está mejor, pero aún hace calor."
    call BlinkXP("c17s002_085c", "d") from _call_BlinkXP_2096
    mad "Eliminemos la camiseta de la ecuación, entonces..."
    mc "Mejor, mucho mejor..."
    scene c17s002_090cd with dissolve
    mad "Y estos pantalones..."
    call BlinkXP("c17s002_090c", "d") from _call_BlinkXP_2097
    mad "¡Wow! ¿Ya estás así?"
    mc "Combinación de una chica preciosa desnudándome y el beso de antes... ¿Cómo quieres que esté?"
    mc "Pero ahora es mi turno... ya te he dicho tú también llevas mucha ropa. Si me lo permites, claro."
    call BlinkXP("c17s002_095c", "d") from _call_BlinkXP_2098
    mad "Pues puedes empezar a quitármela cuando quieras."
    mc "Creo que voy a ser más rápido que tú. Hay menos ropa que quitar, aunque me siento tentado de arrancártelo con los dientes."
    mad "Ni se te ocurra..."
    scene c17s002_100cd with dissolve
    pause (0.8)
    call BlinkXP("c17s002_100c", "d") from _call_BlinkXP_2099
    mc "¡Por Dios, Maddie! Tienes un cuerpo precioso..."
    mad "Gracias, [mc]."
    mc "Sigue perfectamente depilado por lo que veo. *Risa*"
    mad "En esta casa solo hay espacio para un animalito peludo. *Risita*"
    play sound ("music/Meow.ogg")
    cat "¡Miau! (El rey es el rey)"
    if mar._var("route"):
        mc "¿Puedes girarte?... nunca he tenido la oportunidad de mirarte bien por detrás... sin estar vestida."
        scene c17s002_100cg with dissolve
        mad "*Risa* ¿Cuándo lo has mirado vestida?"
        mc "El día que nos conocimos. Desde el Banco de los Novios hay unas vistas preciosas de tu culo a través de la celosía."
        mad "Mmmm... Tengo que hacer algo con esa celosía."
    else:
        mc "¿Puedes girarte?... nunca he tenido la oportunidad de mirarte bien por detrás... "
        scene c17s002_100cg with dissolve
    mad "¿Te gusta lo que ves ahora que lo puedes ver bien?"
    mc "Me parece increíblemente bonito."
    call BlinkXP("c17s002_105c", "d") from _call_BlinkXP_2100
    mad "Voy a quitarme los zapatos y vamos a la cama."
    mc "¿Puedes dejártelos puestos, por favor? Estás super sexy sólo con los ellos."
    mad "Te acabas de ganar un premio por lo que acabas de decir. Voy a dejar que me comas. Sé que te gusta."
    mc "Me encanta."
    call BlinkXP("c17s002_110c", "f") from _call_BlinkXP_2101
    mad "¿Te va bien así? No sé a qué esperas. Ven a por tu premio."
    mc "Estaba disfrutando de las vistas. Ahora mismo eres la definición de perfección, estás preciosa."
    scene c17s002_115cpv with dissolve
    show c17s002_115cv with dissolve
    "Entierras tu cara entre sus muslos, siendo recibido por el conocido olor pungente que emana de su vagina."
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    mad "*Respiración entrecortada* ¡Oh, sí! ¡Cuánto te he echado de menos!"
    "El cuerpo de Maddie responde con estremecimientos a los primeros movimientos de tu lengua."
    mad "*Jadeo* Sigue... llevo cachonda toda la tarde esperando este momento..."
    scene c17s002_120pv with dissolve
    hide c17s002_115cv
    show c17s002_120v with dissolve
    "Tu lengua empapa su vagina mientras es empapada a su vez por sus fluidos."
    mad "*Gemido* ¡Oh, [mc]!"
    "Puedes notar cómo el cuerpo de Maddie empieza a vibrar bajo tus manos, anunciando su inminente orgasmo. Ciertamente, debía estar cachonda cuando has llegado."
    mad "*Jadeo* ¡Para! Estoy a punto de correrme y quiero hacerlo contigo dentro de mí. Siéntate."
    scene c17s002_180ad with dissolve
    hide c17s002_120v
    "Sin mediar palabra, Maddie se empala con Mjolnir."
    mad "*Gemido* ¡Joder! Se nota más grande de lo que esperaba... Y no... *Jadeo* no me estoy quejando."
    scene c17s002_185cpv with dissolve
    show c17s002_185cv with dissolve
    "Ella empieza a moverse en recorridos bien medidos, cambiando la velocidad entre un recorrido y el siguiente, sin dejar de besarte en todo el proceso."
    mcp "(¡Joder! Esto es una pasada.)"
    "El control que Maddie ejerce del ritmo es algo que nunca has experimentado. Estás acostumbrado a que ese control lo tengas tú."
    mad "*Jadeo*"
    "La sensación de los gemidos de la hermosa mujer en tu boca tan solo incrementa la excitación."
    scene c17s002_190cpv with dissolve
    hide c17s002_185cv
    show c17s002_190cv with dissolve
    "Al cabo de unos minutos sus piernas empiezan a temblar, anunciando que su segunda ronda de orgasmos se está acercando."
    mad "*Gemido* Me... fallan... las piernas... Ayúdame."
    "Tus manos, que hasta entonces tan solo acariciaban su cuerpo, se convierten en puntos de apoyo que la guían y ayudan en cada recorrido."
    mad "*Jadeo* Estoy a punto... de correrme... otra vez..."
    mc "Córrete para mí, Ama."
    "Como si en esta ocasión fuera ella la que tuviera que obedecerte, el coño de Maddie entra en erupción."
    "La palabra Ama ha tenido su efecto."
    call OrgasmX("c17s002_200c") from _call_OrgasmX_36
    hide c17s002_190cv
    mad "*GEMIDO* ¡Por Zeus! *Jadeo* ¡Este es más intenso que el de la semana pasada!"
    "Su rápida explosión te pilla por sorpresa. A ti todavía te queda un poco para llegar."
    scene c17s002_185cpv with dissolve
    show c17s002_185cv with dissolve
    "Continúas guiando su cuerpo arriba y abajo, un cuerpo cada vez más desmadejado, recorrido por oleadas de orgasmos."
    mad "*Gemido* No te corras dentro."
    "La orden te pilla por sorpresa. Pero vas a obedecerla. Hace mucho que nadie te lo pide."
    "Al menos la orden llega justo a tiempo."
    mad "*JADEO* No puedo parar... de correrme..."
    "Tu clímax se acerca rápidamente, puedes notar cómo la conocida sensación sube por tus piernas mientras Maddie se va convirtiendo en una muñeca rota con cada nuevo orgasmo."
    call OrgasmX("c17s002_525c") from _call_OrgasmX_37
    hide c17s002_185cv
    mc "¡Mpfft!"
    "Sacas a Mjolnir del interior de Maddie justo a tiempo de regar su vientre con tu semen."
    stop sound fadeout (1.5)
    mad "*JADEO* ¡Wow! También debías estar muy cachondo. Eso es mucha leche."
    call BlinkXP("c17s002_210a", "d") from _call_BlinkXP_2102
    mad "*Respiración entrecortada* ¿Te ha gustado?"
    mc "Me ha encantado... ¿Y a ti?"
    mad "Ha sido alucinante... Hacía mucho que no me corría así. Bien hecho."
    mad "Voy a ir a limpiarme antes de que esto se enfríe... pero antes..."
    scene c17s002_215a with dissolve
    "Maddie engulle tu polla para limpiar los últimos resquicios de semen que cubren tu astil."
    mc "Podría acostumbrarme a eso después de cada corrida."
    call BlinkXP("c17s002_220c", "d") from _call_BlinkXP_2103
    mad "Pues acostúmbrate. Me encanta el sabor de tu semen. Y mezclado con mis fluidos... Mmmmm..."
    mc "Sabes que puedes hacer lo que quieras."
    mcp "(Mientras te permita mantener esta ilusión de control.)"
    mad "Pero aún estás duro como una piedra... ¿Esto no baja nunca?"
    mc "Es difícil que baje cuando acaba de salir de tu preciosa boca."
    call BlinkXP("c17s002_160a", "d") from _call_BlinkXP_2104
    mad "Ahora vuelvo. Puedes seguir cotilleando la habitación si quieres."
    mc "¿Me estás llamando cotilla? *Risa*"
    call c17s002_InterludeRomDom from _call_c17s002_InterludeRomDom
    call BlinkXP("c17s002_170c", "f") from _call_BlinkXP_2105
    mad "Ya estoy de vuelta. Limpia para el siguiente round. Espero que esta vez no te que tengas que volver a irte corriendo."
    mc "No, Maddie, hoy soy todo para ti."
    mad "Entonces vuelve a la cama. Se ha acabado la visita turística por la habitación."
    scene c17s002_530ac with dissolve
    "No hace falta que te lo repita."
    "A partir de entonces se suceden un montón de besos..."
    scene c17s002_530bc with dissolve
    "De caricias..."
    scene c17s002_530cc with dissolve
    "Más besos, que van subiendo de intensidad tal como van pasando los minutos."
    call BlinkXP("c17s002_535c", "d") from _call_BlinkXP_2106
    mad "Te necesito dentro de mí. Besas demasiado bien... vuelvo a estar cachonda."
    mad "Túmbate. Quiero ponerme arriba."
    mc "A tus órdenes."
    scene c17s002_230cAn with dissolve
    "Maddie se vuelve a empalar en Mjolnir. Esta vez con menos gracilidad. Claramente sus piernas no se han recuperado todavía."
    mad "¡Ufff!"
    mc "¿Estás bien?"
    call BlinkXP("c17s002_235", "d") from _call_BlinkXP_2107
    mad "Genial... tan solo es que... ¡Por Zeus! Así te siento más dentro todavía..."
    mc "Si quieres cambiamos de posición."
    mad "No he dicho que fuera malo..."
    scene c17s002_240cpv with dissolve
    show c17s002_240cv with dissolve
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    mad "*Gemido* Mañana me va a doler todo... *Jadeo*"
    mad "*Gemido* Siento las piernas como si fueran gelatina..."
    "La falta de gracilidad en el empalamiento continúa en los movimientos"
    "Todo el control que ha tenido antes ha desaparecido. Sin embargo, no por ello es menos placentero."
    mad "*Jadeo* Bendito dolor..."
    scene c17s002_245cpv with dissolve
    hide c17s002_240cv
    show c17s002_245cv with dissolve
    "Ya no hay cambios de ritmo. Se nota que tiene dificultades para mantener un ritmo constante, por mucho que le ayudes con tus caderas."
    mad "*Gemido* Y no solo en las piernas... estás destrozándome el cérvix."
    mc "¿Cambiamos?"
    mad "*Jadeo* Te he dicho que no es malo... está siendo increíble..."
    mad "*Gemido* Aunque no creo que me queden más orgasmos... esto es sólo para ti. Te lo has ganado como premio."
    "No los va a tener si sigue concentrada en corregir el errático ritmo. O en demostrar que ella está al mando."
    "Sí, parece estar disfrutando, pero no lo suficiente."
    scene c17s002_250c with dissolve
    hide c17s002_245cv
    "Te incorporas y la abrazas, hundiendo tu cara entre sus tetas."
    mad "*Gemido* ¡Hey! ¡Así casi no puedo moverme!"
    mad "Aunque me encanta lo que estás haciendo. *Jadeo*"
    call BlinkXP("c17s002_255", "h") from _call_BlinkXP_2108
    "Volteas a Maddie, tumbándola de espaldas, sin salir de su interior. Sus piernas estaban a punto de ceder."
    mad "¡Hey! ¡Y así no puedo moverme en absoluto! *Risa*"
    mcp "(La risa vuelve a aparecer cuando no sigo sus órdenes.)"
    mc "Tú has hecho todo el trabajo hasta ahora. Déjame hacer algo a mí."
    mad "No voy a negar que las piernas me estaban fallando... pero no quería que pensaras que tenía poca resistencia en nuestra primera vez."
    mc "No lo voy a pensar, ama. Pero déjame hacer el trabajo a mí ahora."
    scene c17s002_260pv with dissolve
    show c17s002_260v with dissolve
    "Empiezas a bombear con tus caderas. Las piernas de Maddie apuntando al aire."
    mad "*Gemido* ¡Oh, sí! Puedo notarte en todos mis puntos sensibles..."
    "Intentas reproducir los cambios de ritmo de Maddie en la primera vez. No lo consigues del todo, pero es una buena imitación."
    mad "*Jadeo* Olvida lo que he dicho antes sobre que no me iba a volver a correr... ¡Esto es fantástico!"
    scene c17s002_265cpv with dissolve
    hide c17s002_260v
    show c17s002_265cv with dissolve
    "Saber que está volviendo a disfrutar, que no es algo sólo para ti, hace que tus caderas quieran llevarla al éxtasis."
    mad "*Gemido* ¿Dónde has estado escondido toda mi vida?"
    mad "*Jadeo* ¡Por lo que más quieras, no pares ahora!"
    "No pensabas hacerlo. Puedes notar como el orgasmo de Maddie se acerca."
    "También lo hace el tuyo. "
    mad "*Gemido* Córrete dentro ahora. Pero no lo hagas hasta que lo haga yo."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Maddie embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not mad._var("pregnant") and not Whatif:
            play sound ("music/OldMusicBox5.ogg")
            if not Whatif:
                $ mad._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX("c17s002_270c") from _call_OrgasmX_38
    hide c17s002_265cv
    mad "*GEMIDO* ¡Oh, SÍ! ¡Me corro!"
    call OrgasmX("c17s002_275c") from _call_OrgasmX_39
    mc "¡Mpffft!"
    "Vuestros orgasmos llegan casi simultáneamente. Has aguantado tu orgasmo hasta que has notado sus primeras contracciones."
    "Después te has dejado ir."
    mad "*JADEO* ¡No paran! ¡No te muevas, por favor!"
    "Te mantienes inmóvil, tu polla aún dentro de Maddie, notando como cada uno de sus espasmos intenta exprimir hasta la última gota de tu semen."
    scene c17s002_280aAnBlink with dissolve #primera persona Maddie relajándose
    stop sound fadeout (1.5)
    "Lentamente su cuerpo se va relajando, volviendo a ser la muñeca rota de hace un rato."
    "Si hubiera continuado arriba, a estas alturas se habría derrumbado encima tuyo."
    mad "Ya está... ya han acabado... mañana no voy a poder juntar las piernas."
    call BlinkXP("c17s002_285a", "d") from _call_BlinkXP_2109
    mad "Ha sido totalmente increíble..."
    mad "Creo que tengo unas cuerdas por ahí para poder atarte y que no te vayas nunca."
    mc "No hacen falta las cuerdas. Dime cuando quieres que venga y vendré. Tienes unos secretos que guardar y prefiero mantenerte contenta."
    call BlinkXP("c17s002_290a", "d") from _call_BlinkXP_2110
    mad "No es un mal trato."
    mad "Pero ahora tengo un sable que limpiar. Déjame levantarme..."
    call BlinkXP("c17s002_295a", "d") from _call_BlinkXP_2111
    mad "No tengas ideas raras aunque sigas duro como una piedra... mi resistencia ha llegado hasta aquí."
    mc "Creo que yo también voy a necesitar unos minutos de descanso."
    mad "*Risa* ¿Minutos? ¡Yo voy a necesitar días!"
    mad "Ponte de rodillas. Ese sable me está llamando."
    scene c17s002_300c with dissolve
    "Maddie cumple su promesa y deja a Mjolnir limpio como una patena."
    "Su lengua vuelve a jugar con toda tu longitud tanto en el camino de ida como en el de vuelta."
    call BlinkXP("c17s002_305a", "d") from _call_BlinkXP_2112
    mad "Ya está, limpio como si aquí no hubiera pasado nada. *Risa*"
    mc "Y duro como si estuviera a punto de pasar. *Risa*"
    mad "*Risa* Ya te he dicho que no tuvieras ideas raras."
    mc "No te preocupes. Te daré esos días de descanso. *Risa*"
    stop music fadeout (1.5)
    "El ambiente se ha relajado después de los orgasmos y han vuelto las risas. Ya no es la hembra dominante. Vuelve a ser una chica normal y risueña."
    play music ("music/RayOfHope.ogg")
    "Casi parece una novia. Prefieres esta versión."
    call BlinkXP("c17s002_310a", "d") from _call_BlinkXP_2113
    mad "Túmbate conmigo un rato."
    mc "¿Abrazos? Esa es mi especialidad."
    call BlinkXP("c17s002_315a", "d") from _call_BlinkXP_2114
    mad "Se está bien aquí."
    mc "Ya te he dicho que los abrazos son mi especialidad. *Risa*"
    mad "Y no mentías..."
    mc "Nunca miento, Maddie."
    call BlinkXP("c17s002_320a", "d") from _call_BlinkXP_2115
    mad "Entonces es el momento de preguntarte si te molestaría mucho que no te dejara quedarte a dormir."
    mc "*Risa* ¿Ya te has cansado de mí?"
    call BlinkXP("c17s002_325a", "d") from _call_BlinkXP_2116
    mad "No es eso... me conozco y sé que al despertar querría continuar aunque me doliera todo."
    mad "Y tengo que trabajar en la tienda todo el día... y seguramente llegaría tarde."
    mc "No pasa nada, cielo. Lo entiendo. Mañana yo tengo un día ajetreado también."
    call BlinkXP("c17s002_330a", "d") from _call_BlinkXP_2117
    mad "Pero eso no quiere decir que te tengas que ir ya. Déjame disfrutar de estos abrazos un rato más."
    mc "Disfrutémoslos juntos. *Risa* Una pregunta... ¿por qué no me has dejado correrme dentro la primera vez y me lo has pedido la segunda?"
    call BlinkXP("c17s002_540", "d") from _call_BlinkXP_2118
    mad "Estoy tomando la píldora desde el sábado. La compré el día siguiente de tu última vez aquí. No era por un riesgo de embarazo."
    mad "Era para ver si eras capaz de cumplir una orden como esa. *Risa*"
    mc "Ya has visto que he sido capaz. *Risa*"
    call BlinkXP("c17s002_545", "d") from _call_BlinkXP_2119
    stop music fadeout (1.5)
    mad "Tenía pensado decirte que me limpiaras tu corrida del coño la segunda vez."
    mad "Pero no hubiera podido dejar de correrme. *Risa*"
    play music ("music/Emotional-Piano-Sad.ogg")
    mc "No lo hubiera hecho."
    "Se acabaron las risas."
    call BlinkXP("c17s002_550", "d") from _call_BlinkXP_2120
    mad "¿Qué? ¿Por qué? Tus secretos..."
    mc "El secreto del probador se lo podrías decir a [mar] si quisieras, entonces. El de las chicas no lo vas a contar. Lo has prometido."
    mc "Pero no voy a hacer cosas que me desagraden. Tenlo claro, Maddie, esto está funcionando porque a los dos nos gusta."
    mc "Si intentas humillarme o que haga cosas que me asqueen... se acabó."
    mcp "(E intenta contarle el secreto a [mar]. Lo más probable es que se sienta halagada.)"
    call BlinkXP("c17s002_555", "d") from _call_BlinkXP_2121
    mad "No voy a contar ninguno de tus secretos... me gusta demasiado lo que estamos creando aquí..."
    mad "Aunque me gustaría hacer algunos cambios."
    mc "¿Qué cambios?"
    call BlinkXP("c17s002_560", "d") from _call_BlinkXP_2122
    mad "Tengo que darle unas vueltas al asunto. Te lo diré cuando lo tenga decidido."
    mc "Me lo consultarás cuando lo tengas decidido."
    mad "Sí, eso..."
    call BlinkXP("c17s002_565", "d") from _call_BlinkXP_2123
    mad "Lo siento..."
    mc "No tienes por qué. No has hecho nada que me haya incomodado."
    call BlinkXP("c17s002_570", "d") from _call_BlinkXP_2124
    mad "Pero tenía pensado hacerlo. No lo he hecho porque he pensado en los efectos que tendría en mí, no por cómo te hubiera hecho sentir a ti."
    mc "Pero nos ha servido para poner las cartas sobre la mesa. Y eso es bueno. Nos ha faltado comunicación desde el principio."
    call BlinkXP("c17s002_575", "d") from _call_BlinkXP_2125
    mad "Creo que deberíamos quedar un día y charlar. En un sitio público en el que no vayamos a acabar desnudos."
    stop music fadeout (1.5)
    mc "Me parece una buena idea. Cuando tengas pensados esos cambios, volvemos a hablar del tema. De momento, ven aquí."
    scene c17s002_335a with dissolve
    play music ("music/UnforeseenMotive.ogg")
    "Pasáis un rato charlando y disfrutando del contacto de piel contra piel. Más relajados después de haber aclarado las cosas."
    "Habláis del sueño de Maddie de convertirse en diseñadora de ropa, de lo difícil que es abrirse paso en ese mundillo."
    "Charláis sobre tu familia y sobre la empresa. Tiene mucha curiosidad sobre Eva y Amanda."
    "Poco a poco, los últimos rastros de energía van desapareciendo de Maddie y decides irte antes de que se quede dormida."
    call BlinkXP("c17s002_340a", "f") from _call_BlinkXP_2126
    mad "Entonces... ¿nos vemos el domingo?"
    mc "Sí, te pasaré a buscar antes de ir la comida del cumpleaños. Vamos a ser un montón de gente este año."
    mad "¿Qué me pongo?"
    mc "Por mí, podrías ir así, pero las chicas van a ir con vestidos. Nada demasiado elegante. Y trae algo cómodo para la tarde y la partida de rol. [dap] me dijo que suelen jugar en pijama."
    call BlinkXP("c17s002_345a", "d") from _call_BlinkXP_2127
    mad "No sé si ir en pijama sería demasiado correcto, aún no las conozco demasiado. Pero si todas están en pijama, si yo llevo un vestido parecería ridícula."
    mad "¿Shorts y camiseta?"
    mc "Genial. Los shorts rojos te hacen un culo precioso."
    call BlinkXP("c17s002_350a", "d") from _call_BlinkXP_2128
    mad "*Risa* Me gusta que te fijes en la ropa que llevo."
    mc "Era imposible no fijarse. *Risa* Ese culo debería estar en un museo."
    mad "Entonces no podrías jugar con él la próxima vez. *Risa* Y es una de mis zonas erógenas."
    mc "Y no lo hemos usado hoy..."
    call BlinkXP("c17s002_355a", "d") from _call_BlinkXP_2129
    mad "Y no lo vamos a usar. *Risa* Si no puedo juntar las piernas mañana, al menos espero poder sentarme."
    mc "No es que lo estuviera proponiendo, pero... la próxima vez ya veremos. "
    call KissXP("c17s002_360a", "d") from _call_KissXP_63
    mad "Vete antes de que te vuelva a desnudar."
    mc "Buenas noches, Maddie. Hasta el domingo."
    stop music fadeout (1.5)
    mad "Hasta el domingo, [mc]."
    return
label c17s002_MaddieSub:
    "Llegas a casa de Maddie mucho más tarde de lo que habías esperado llegar. La verdad es que tienes ganas de ver a dónde lleva esto."
    scene c17s002_005d with dissolve
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    call BlinkXP("c17s002_400", "d") from _call_BlinkXP_2130
    play music ("music/AnxiousMarch.ogg")
    mad "Casi creía que no venías. Desde que has llamado se me ha hecho eterno."
    mc "La cosa se ha liado más de lo esperado."
    call KissXP("c17s002_405", "d") from _call_KissXP_64
    mad "Lo importante es que ya estás aquí. Pasa."
    mc "¿Esa era la sorpresa de la que me hablaste cuando te llamé? Estás muy graciosa, y sexy."
    scene c17s002_410d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP("c17s002_410" , "d") from _call_BlinkXP_2131
    mad "¿Te gusta? ¡Miau!"
    if not Whatif:
        if not _in_replay:
            $ mad.profileImages.pop (7) # first remove
            $ mad.profileImages.insert (7, ("maddie_11", "route")) # then add new
            $ mad.profileImages.pop (11) # first remove
            $ mad.profileImages.insert (11, ("maddie_12", "route")) # then add new
            $ mad.profileImages.pop (12) # first remove
            $ mad.profileImages.insert (12, ("maddie_7", "route")) # then add new
            $ renpy.notify ("Profile Images unlocked for Maddie: 8-12-13 - Lingerie")
    mc "Me encanta. No sabía que me iba a encontrar una gatita al llegar."
    python:
        if "zeu" not in globals () or not isinstance (hm, TGCharacter):
            zeu = TGCharacter ("Zeus", color = "#0023ff")
            cat = TGCharacter (_("Jodido Gato"), color = "#0023ff")
    call c17s002_ZeusArrival from _call_c17s002_ZeusArrival_1
    call BlinkXP("c17s002_415", "d") from _call_BlinkXP_2132
    stop music fadeout (1.5)
    mad "Si mi amo quiere, puede empezar por acariciar a su gatita."
    play music ("music/CCFunk.ogg")
    mc "¿Has sido una buena gatita, Maddie?"
    mad "¡Miau!"
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (Tienes un acento horrible, Maddie.)"
    call BlinkXP("c17s002_420", "d") from _call_BlinkXP_2133
    mc "¿Te gusta que te acaricien?"
    mad "Me encanta, pero me gustaría más darle placer a mi amo."
    mc "Pero vas demasiado vestida para ello, ¿verdad?"
    mad "¡Miau!"
    scene c17s002_425d with dissolve
    pause (0.8)
    call BlinkXP("c17s002_425", "d") from _call_BlinkXP_2134
    mad "¿Mejor así?"
    mc "Mucho mejor. Déjate el resto puesto."
    call BlinkXP("c17s002_430", "d") from _call_BlinkXP_2135
    mad "¿A mi amo le gustan mis orejitas? ¿Quiere que me las deje puestas?"
    mc "Si, me encantan..."
    scene c17s002_435d with dissolve #de rodillas
    pause (0.8)
    call BlinkXP("c17s002_435", "d") from _call_BlinkXP_2136 #Desaparece la ropa de MC
    mad "¿Y mis zarpitas?"
    mc "Si les vas a dar ese uso, no me voy a quejar."
    mc "Pero es el momento de que te tumbes en la cama."
    call BlinkXP("c17s002_440", "d") from _call_BlinkXP_2137
    mad "¿Quiere mi amo que me deje los tacones puestos?"
    mc "Te he dicho que te dejaras puesto el resto. Eso incluye los tacones. Estás muy sexy con ellos."
    mc "Lástima que la cola estuviera cosida al disfraz."
    call BlinkXP("c17s002_445", "d") from _call_BlinkXP_2138
    mad "¿Qué quieres decir?... ¡Oh! Ahora lo entiendo... ¡Qué travieso es mi amo!"
    mc "Quizás encuentre algo que pueda solucionar eso. Sube a la cama."
    call BlinkXP("c17s002_110b", "f") from _call_BlinkXP_2139
    mad "¿Así va bien?"
    mc "Perfecta."
    mad "¿Puedo hacer una petición?"
    mc "Claro. Puedes pedir lo que quieras y valoraré si concederlo."
    mad "¿Puedes ponerte en cuclillas encima de mi cabeza?"
    mad "Quiero hacerte una cosa a ver si te gusta."
    mc "Probemos."
    scene c17s002_135bpv with fade
    "Sigues las instrucciones de Maddie mientras ella coge tu enhiesta polla y acerca sus labios a tu escroto."
    mc "Esto promete, Maddie."
    show c17s002_135bv with dissolve
    "No solo promete. En el momento en que Maddie empieza a pajearte, mientras que con su lengua y sus labios te chupa los huevos, descubres que tu gatita sabe lo que está haciendo."
    mc "Maddie, eso es increíble."
    mad "*Slurp*"
    mcp "(Esta chica se desvive por complacerme. Creo que ya no tiene nada que ver con lo que pasó en el probador.)"
    mcp "(Quizás podríamos dar un paso en otra dirección.)"
    "El pensamiento fugaz que pasa por tu mente desaparece tal como ha llegado, abrumado por las sensaciones que Maddie está produciendo en tu cuerpo."
    scene c17s002_130bpv with dissolve
    hide c17s002_135bv
    show c17s002_130bv with dissolve
    "Tú no puedes estar quieto, y empiezas a masturbarla."
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    mad "*Gemido de sorpresa* *Slurp* *Jadeo*"
    mc "Esto tiene que ser mutuo, Maddie. Si no, no es divertido."
    mad "*Gemido afirmativo* *Slurp* *Jadeo*"
    "Puedes notar cómo Maddie se va humedeciendo cada vez más bajo las caricias de tus dedos."
    "Ya estaba húmeda nada más tocarla."
    scene c17s002_135bpv with dissolve
    hide c17s002_130bv
    show c17s002_135bv with dissolve
    mc "¿Te has puesto cachonda mientras esperabas? ¿Mientras imaginabas lo que iba a pasar hoy?"
    mad "*Gemido afirmativo* *Slurp* *Jadeo*"
    mc "¿Te gustaría correrte así? ¿Mientras baño de leche la tripita de mi gatita?"
    mad "*GEMIDO AFIRMATIVO* *Slurp*"
    mc "Y estás a punto de correrte, ¿verdad?"
    mad "*JADEO AFIRMATIVO* *Slurp*"
    mc "No te corras hasta que lo haga yo. Me falta muy poco."
    mad "*Gemido de sorpresa* *Slurp*"
    scene c17s002_130bpv with dissolve
    hide c17s002_135bv
    show c17s002_130bv with dissolve
    "Ambos os dedicáis con más ganas al otro, si es que eso es posible."
    "Tú para comprobar si cumple tus órdenes."
    "Ella para llevarte a nuevas cotas de placer y que le permitas correrse."
    call OrgasmX("c17s002_450") from _call_OrgasmX_40
    hide c17s002_130bv
    mc "¡Mpfft!"
    mad "*JADEO* ¡SÍ!"
    "Ambos os corréis prácticamente a la vez. Tú primero."
    stop sound fadeout (1.5)
    "En el momento en que Maddie nota el primer borbotón de semen saliendo de tu polla, se relaja y se permite correrse."
    "Buena chica. Buena gatita."
    call BlinkXP("c17s002_150b", "f") from _call_BlinkXP_2140
    mad "¿Te ha gustado?"
    mc "Me ha encantado. Nunca había probado esta posición... ¿Y a ti?"
    mad "Ha sido alucinante... Hacía mucho que no me corría así."
    mad "La prohibición de correrme ha hecho que sea... no sé... más intenso."
    mad "¿Puedo ir a limpiarme antes de que esto se enfríe?"
    mc "Sí, por supuesto. Tráeme algo para limpiarme yo también."
    scene c17s002_155b with dissolve
    "Maddie devora tu polla para limpiar los últimos restos de semen."
    "Su juguetona lengua rodea tu astil mientras puedes notar como la punta está a punto de entrar en su garganta."
    call BlinkXP("c17s002_160b", "f") from _call_BlinkXP_2141
    "Un momento después..."
    mad "Dame un momento y ahora vuelvo. Puedes seguir cotilleando la habitación si quieres."
    mc "¿Me estás llamando cotilla? *Risa*"
    call c17s002_InterludeRomDom from _call_c17s002_InterludeRomDom_1
    call BlinkXP("c17s002_170b", "f") from _call_BlinkXP_2142
    mad "Ya estoy de vuelta. Limpia para mi amo. A menos que tengas que volver a irte corriendo."
    mc "No, Maddie, hoy he reservado la noche para ti."
    mad "Entonces, si quieres, vuelve a la cama y deja para otro día la visita turística por la habitación."
    scene c17s002_175ba with dissolve
    "No hace falta que te lo repita."
    "A partir de entonces se suceden un montón de besos..."
    scene c17s002_175bb with dissolve
    "De caricias..."
    scene c17s002_175bc with dissolve
    "Más besos, que van subiendo de intensidad tal como van pasando los minutos."
    call BlinkXP("c17s002_180b", "d") from _call_BlinkXP_2143
    mc "¿Mi gatita vuelve a estar cachonda? Puedo notar el calor que emana de tu entrepierna."
    mad "Mi amo besa demasiado bien... no puedo evitar volver a estar cachonda."
    mc "Pues estás en la posición ideal ahora mismo."
    scene c17s002_180bd with dissolve
    "Sin mediar palabra, Maddie se empala con Mjolnir."
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    mad "*Gemido* ¡Joder! Se nota más grande de lo que esperaba... Y no... *Jadeo* no me estoy quejando. Mi amo está muy bien dotado y tiene a su gatita contenta."
    scene c17s002_185bpv with dissolve
    show c17s002_185bv with dissolve
    "Ella empieza a moverse en recorridos bien medidos, cambiando la velocidad entre un recorrido y el siguiente, sin dejar de besarte en todo el proceso."
    mcp "(¡Joder! Esto es una pasada.)"
    "El control que Maddie ejerce sobre el ritmo es algo que nunca has experimentado. Estás acostumbrado a que ese control lo tengas tú."
    mad "*Jadeo*"
    "La sensación de los gemidos de la felina mujer en tu boca tan solo incrementa la excitación."
    scene c17s002_190bpv with dissolve
    hide c17s002_185bv
    show c17s002_190bv with dissolve
    "Al cabo de unos minutos sus piernas empiezan a temblar, anunciando que su segunda ronda de orgasmos se está acercando."
    mad "*Gemido* Me... fallan... las piernas... Ayúdame, por favor."
    "Tus manos, que hasta entonces tan solo acariciaban su cuerpo, se convierten en puntos de apoyo que la guían y ayudan en cada recorrido."
    mad "*Jadeo* Estoy a punto... de correrme... otra vez..."
    mc "Córrete para mí, Gatita. Esta vez tienes libertad para hacerlo cuando quieras."
    "Como si esa frase la liberase, el coño de Maddie entra en erupción."
    call OrgasmX("c17s002_200b") from _call_OrgasmX_41
    hide c17s002_190bv
    mad "*GEMIDO* ¡Por Zeus! *Jadeo* ¡Este es incluso más intenso que el de antes!"
    "Su rápida explosión te pilla por sorpresa. A ti todavía te queda un rato para llegar."
    "Que haya cumplido tus órdenes ambas veces te pone más cachondo aún, pero por alguna razón no te proporciona felicidad."
    scene c17s002_185bpv with dissolve
    show c17s002_185bv with dissolve
    "Continúas guiando su cuerpo arriba y abajo, un cuerpo cada vez más desmadejado, recorrido por oleadas de orgasmos."
    mad "*Gemido* Puedes correrte dónde quieras. Estoy tomando la píldora desde la semana pasada."
    if mc._var("pregnancies") > 0:
        mcp "(Un embarazo menos del que preocuparme.)"
    else:
        mcp "(Genial, no sé si estoy preparado para ser padre todavía.)"
    mcp "(Además, con este tipo de relación, no sé si sería lo mejor.)"
    "Tu clímax se acerca poco a poco, puedes notar cómo la conocida sensación sube por tus piernas mientras Maddie se va convirtiendo en una muñeca rota con cada nuevo orgasmo."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Maddie embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not Whatif:
            play sound ("music/OldMusicBox5.ogg")
            if not Whatif:
                $ mad._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX("c17s002_205b") from _call_OrgasmX_42
    hide c17s002_185bv
    mc "¡Mpfft!"
    "Explotas en el interior de Maddie llenándola con tu semilla."
    mad "*Gemido* ¡Sí, lléname! ¡Dale a tu gatita toda tu leche!"
    stop sound fadeout (1.5)
    "Cuando tu descarga finaliza, os derrumbáis sobre la cama, todavía abrazados con tu polla dentro de Maddie."
    call BlinkXP("c17s002_210b", "d") from _call_BlinkXP_2144
    mad "¡Ha sido increíble! No recuerdo haberme corrido así nunca."
    mc "Totalmente alucinante, Maddie. Esos cambios de ritmo..."
    mad "Cualquier cosa para complacer a mi amo."
    mad "Déjame limpiarte y nos tumbamos a descansar."
    scene c17s002_215b with dissolve
    "Maddie engulle tu polla para limpiar los últimos resquicios de semen que cubren tu astil."
    mc "Podría acostumbrarme a eso después de cada corrida. *Risita*"
    call BlinkXP("c17s002_220b", "d") from _call_BlinkXP_2145
    mad "Si quieres, puedes acostumbrarte. Me encanta el sabor de la leche de mi amo. Y mezclado con mis fluidos... Mmmmm..."
    mc "Es una cosa que no te prohibiré nunca. No hace falta que pidas permiso."
    mad "Pero aún estás duro como una piedra... ¿Esto no baja nunca?"
    mc "Es difícil que baje cuando acaba de salir de tu preciosa boca. Una gatita como tú lamiendo leche es una visión impresionante."
    call BlinkXP("c17s002_225b", "d") from _call_BlinkXP_2146
    mad "Entonces... ¿Puedes continuar? No me gustaría que desaprovecharas una erección como esta. Aunque sea solo para ti. Dudo que me pueda correr otra vez."
    mc "Puedo continuar si puedes tú. *Risa* Túmbate en la cama."
    scene c17s002_260pv with dissolve
    show c17s002_260v with dissolve
    "Maddie se tumba y la penetras con ternura. Su cuerpo aún no se ha recuperado de la ronda anterior."
    "Empiezas a bombear con tus caderas. Las piernas de Maddie apuntando al aire."
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    mad "*Gemido* ¡Oh, sí! Puedo notarte en todos mis puntos sensibles... *Jadeo* mi amo..."
    "Intentas reproducir los cambios de ritmo de Maddie en la primera vez. No lo consigues del todo, pero es una buena imitación."
    mad "*Jadeo* Olvida lo que he dicho antes sobre que no me iba a volver a correr... ¡Esto es fantástico!"
    scene c17s002_265bpv with dissolve
    hide c17s002_260v
    show c17s002_265bv with dissolve
    "Saber que está volviendo a disfrutar, que no es algo sólo para ti, hace que tus caderas quieran llevarla al éxtasis."
    mad "*Gemido* ¿Dónde has estado escondido toda mi vida?"
    mad "*Jadeo* ¡Por lo que más quieras, no pares ahora!"
    mcp "(La gatita dócil empieza a dar órdenes. Eso es nuevo.)"
    "No tenías intención de parar, pero la orden te ha sorprendido. Puedes notar como el orgasmo de Maddie se acerca."
    "También lo hace el tuyo."
    scene c17s002_260pv with dissolve
    hide c17s002_265bv
    show c17s002_260v with dissolve
    mad "*Gemido* Mañana me va a doler todo... *Jadeo* Me estás destrozando..."
    mad "*Gemido* Siento las piernas como si fueran gelatina..."
    "Toda la gracilidad y control que ha mostrado antes han desaparecido. Se deja hacer, disfrutando de cada una de tus embestidas."
    mad "*Jadeo* Bendito dolor..."
    scene c17s002_265bpv with dissolve
    hide c17s002_260v
    show c17s002_265bv with dissolve
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Maddie embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not mad._var("pregnant") and not Whatif:
            play sound ("music/OldMusicBox5.ogg")
            if not Whatif:
                $ mad._var("pregnant", True)
    $ resetWalkthrough ()
    mc "Córrete para mí, Gatita."
    call OrgasmX("c17s002_270b") from _call_OrgasmX_43
    hide c17s002_265bv
    " "
    call OrgasmX("c17s002_275b") from _call_OrgasmX_44
    mad "*GEMIDO* ¡Oh, SÍ! ¡Me corro!"
    mc "¡Mpffft!"
    "Vuestros orgasmos llegan casi simultáneamente. Más tarde dudaréis si ha sido simultáneo o Maddie ha cumplido con tus órdenes antes de correrte tú."
    "Da lo mismo quién haya sido el primero."
    mad "*JADEO* ¡No paran! ¡No te muevas, por favor!"
    stop sound fadeout (1.5)
    "Te mantienes inmóvil, tu polla aún dentro de Maddie, notando como cada una de sus contracciones intenta exprimir hasta la última gota de tu semen."
    scene c17s002_280bAnBlink with dissolve #primera persona Maddie relajándose
    "Lentamente su cuerpo se va relajando, volviendo a ser la muñeca rota de hace un rato."
    "Si hubiera continuado arriba, a estas alturas se habría derrumbado encima tuyo."
    mad "Ya está... ya han acabado... mañana no voy a poder juntar las piernas."
    call BlinkXP("c17s002_285b", "d") from _call_BlinkXP_2147
    mad "Ha sido totalmente increíble..."
    mad "¿Quieres llevarme como mascota a tu casa?"
    mc "¿Dejarías al pobre Zeus aquí solo? *Risa*"
    call BlinkXP("c17s002_290b", "d") from _call_BlinkXP_2148
    mad "Tienes razón, nos tendrías que adoptar a los dos. *Risa*"
    mad "Pero ahora tengo un sable que limpiar. Déjame levantarme..."
    call BlinkXP("c17s002_295b", "d") from _call_BlinkXP_2149
    mad "Aunque sigas duro como una piedra, creo que no voy a poder seguir... mi resistencia ha llegado hasta aquí."
    mc "Creo que yo también voy a necesitar unos minutos de descanso."
    mad "¿Minutos? ¡Yo voy a necesitar días!"
    mad "¿Te puedes poner de rodillas? Hay leche que limpiar en ese sable, y tu gatita quiere su última ración del día."
    scene c17s002_300b with dissolve
    "Maddie cumple su promesa y deja a Mjolnir limpio como una patena."
    "Su lengua vuelve a jugar con toda tu longitud tanto en el camino de ida como en el de vuelta."
    call BlinkXP("c17s002_305b", "d") from _call_BlinkXP_2150
    mad "Ya está, limpio como si aquí no hubiera pasado nada."
    mc "Y duro como si estuviera a punto de pasar."
    call BlinkXP("c17s002_455b", "d") from _call_BlinkXP_2151
    mad "Siento no poder seguir... siento decepcionarte..."
    mc "No me decepcionas, Maddie. Ha sido muy intenso."
    mc "No te preocupes. Te daré esos días de descanso."
    stop music fadeout (1.5)
    call BlinkXP("c17s002_310b", "d") from _call_BlinkXP_2152
    mc "Túmbate conmigo un rato."
    play music ("music/RayOfHope.ogg")
    mad "¿Abrazos?"
    mc "Esa es mi especialidad, y has sido una buena gatita."
    call BlinkXP("c17s002_315b", "d") from _call_BlinkXP_2153
    mad "Se está bien aquí."
    mc "Ya te he dicho que los abrazos son mi especialidad. Y te los mereces. Has estado impresionante."
    mad "Gracias. Veo que no mentías..."
    mc "Nunca miento, Maddie."
    call BlinkXP("c17s002_320b", "d") from _call_BlinkXP_2154
    mad "Entonces es el momento de preguntarte si te molestaría mucho que no te dejara quedarte a dormir."
    mc "¿Ya te has cansado de mí?"
    call BlinkXP("c17s002_325b", "d") from _call_BlinkXP_2155
    mad "No es eso... me conozco y sé que al despertar querría continuar aunque me doliera todo."
    mad "Y tengo que trabajar en la tienda todo el día... seguramente llegaría tarde."
    mc "No pasa nada, Gatita. Lo entiendo. Mañana yo tengo un día ajetreado también."
    call BlinkXP("c17s002_330b", "d") from _call_BlinkXP_2156
    mad "Pero eso no quiere decir que te tengas que ir ya si no quieres. Se está muy bien aquí."
    mc "Disfrutémoslos juntos."
    scene c17s002_335b with dissolve
    "Pasáis un rato charlando y disfrutando del contacto de piel contra piel."
    "Habláis del sueño de Maddie de convertirse en diseñadora de ropa, de lo difícil que es abrirse paso en ese mundillo."
    "Charláis sobre tu familia y sobre la empresa. Tiene mucha curiosidad sobre Eva y Amanda."
    "Poco a poco, los últimos rastros de energía van desapareciendo de Maddie y decides irte antes de que se quede dormida."
    call BlinkXP("c17s002_340b", "f") from _call_BlinkXP_2157
    mad "Entonces... ¿nos vemos el domingo?"
    mc "Sí, te pasaré a buscar antes de ir la comida del cumpleaños. Vamos a ser un montón de gente este año."
    mad "¿Qué me pongo?"
    mc "Por mí podrías ir así, pero las chicas van a ir con vestidos. Nada demasiado elegante. Y trae algo cómodo para la tarde y la partida de rol. [dap] me dijo que suelen jugar en pijama."
    call BlinkXP("c17s002_345b", "d") from _call_BlinkXP_2158
    mad "No sé si ir en pijama sería demasiado correcto, aún no las conozco demasiado. Pero si todas están en pijama, si yo llevo un vestido parecería ridícula."
    mad "¿Shorts y camiseta?"
    mc "Genial. Los shorts rojos te hacen un culo precioso."
    call BlinkXP("c17s002_350b", "d") from _call_BlinkXP_2159
    mad "Me gusta que te fijes en la ropa que llevo."
    mc "Era imposible no fijarse. Ese culo debería estar en un museo."
    mad "Entonces no podrías jugar con él la próxima vez. Y es una de mis zonas más erógenas."
    mc "Y no lo hemos usado hoy..."
    call BlinkXP("c17s002_355b", "d") from _call_BlinkXP_2160
    mad "Y no lo vamos a usar a menos que me obligues. Si no puedo juntar las piernas mañana, al menos espero poder sentarme."
    mc "No te voy a obligar a nada que no quieras hacer, Maddie. Ya te he dicho que esto consiste en que nos lo pasemos bien los dos."
    call BlinkXP("c17s002_460b", "d") from _call_BlinkXP_2161
    mad "Gracias, [mc]. Cuando empezamos esto... pensé que ibas a ser... no sé... más cruel. Que ibas a aprovecharte de la situación."
    mc "La crueldad no va conmigo, Maddie. Yo no puedo disfrutar si no lo haces tú."
    call KissXP("c17s002_360b", "d") from _call_KissXP_65
    mad "Vete antes de que te vuelva a desnudar."
    mc "Buenas noches, Maddie. Hasta el domingo."
    stop music fadeout (1.5)
    mad "Hasta el domingo, [mc]."
    return
label c17s002_MaddieRomance:
    "Llegas a casa de Maddie mucho más tarde de lo que habías esperado llegar. La verdad es que tenías muchas ganas de verla."
    scene c17s002_005d with dissolve
    play sound ("music/doorbell1.ogg")
    "*Ding-Dong*"
    call BlinkXP("c17s002_005", "d") from _call_BlinkXP_2162
    play music ("music/Stardust.ogg")
    mad "Casi creía que no venías. Desde que has llamado se me ha hecho eterno."
    mc "Lo siento, Maddie. La cosa se ha liado más de lo esperado."
    call KissXP("c17s002_010", "d") from _call_KissXP_66
    mad "Lo importante es que ya estás aquí. Pasa."
    mc "¿Esa era la sorpresa de la que me hablaste cuando te llamé? Estás preciosa."
    scene c17s002_015d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP("c17s002_015" , "d") from _call_BlinkXP_2163
    mad "¿Te gusta?"
    if not Whatif:
        if not _in_replay:
            $ mad.profileImages.pop (7) # first remove
            $ mad.profileImages.insert (7, ("maddie_7", "route")) # then add new
            $ mad.profileImages.pop (11) # first remove
            $ mad.profileImages.insert (11, ("maddie_11", "route")) # then add new
            $ mad.profileImages.pop (12) # first remove
            $ mad.profileImages.insert (12, ("maddie_12", "route")) # then add new
            $ renpy.notify ("Profile Images unlocked for Maddie: 8-12-13 - Lingerie")
    mc "Me encanta. Estás increíble."
    python:
        if "zeu" not in globals () or not isinstance (hm, TGCharacter):
            zeu = TGCharacter ("Zeus", color = "#0023ff")
            cat = TGCharacter (_("Jodido Gato"), color = "#0023ff")
    call c17s002_ZeusArrival from _call_c17s002_ZeusArrival_2
    scene c17s002_070pv with dissolve
    show c17s002_070v
    stop music fadeout (1.5)
    "Vuestros labios se juntan en un beso largamente deseado."
    play music ("music/Bolero.ogg")
    "Que ella lleve el picardías mientras tú estás completamente vestido le da un punto de cita secreta que te pone cachondo."
    "El tórrido beso hace que cuando vuestros labios se separen, Mjolnir se sienta presionado dentro de tus pantalones."
    call BlinkXP("c17s002_075a", "d") from _call_BlinkXP_2164
    mad "[mc]... ¿hace calor aquí o es que me has puesto cachondísima? Creo que tú llevas demasiada ropa..."
    mc "Incluso tú llevas demasiada..."
    scene c17s002_080ad with dissolve
    hide c17s002_070v
    pause (0.8)
    call BlinkXP("c17s002_080a", "d") from _call_BlinkXP_2165
    mad "Déjame solucionarlo... esta camisa sobra..."
    mc "Se está mejor, pero aún hace calor."
    call BlinkXP("c17s002_085a", "d") from _call_BlinkXP_2166
    mad "Eliminemos la camiseta de la ecuación, entonces..."
    mc "Mejor, mucho mejor..."
    scene c17s002_090ad with dissolve
    mad "Y estos pantalones..."
    call BlinkXP("c17s002_090a", "d") from _call_BlinkXP_2167
    mad "¡Wow! ¿Ya estás así?"
    mc "Combinación de una chica preciosa desnudándome y el beso de antes... ¿Cómo quieres que esté?"
    mc "Pero ahora es mi turno... ya te he dicho tú también llevas mucha ropa."
    call BlinkXP("c17s002_095a", "d") from _call_BlinkXP_2168
    mad "Pues puedes empezar a quitármela cuando quieras."
    mc "Creo que voy a ser más rápido que tú. Hay menos ropa que quitar, aunque me siento tentado de arrancártelo con los dientes. *Risa*"
    scene c17s002_100ad with dissolve
    pause (0.8)
    call BlinkXP("c17s002_100a", "d") from _call_BlinkXP_2169
    mc "¡Por Dios, Maddie! Tienes un cuerpo precioso..."
    mad "Gracias, [mc]. Pero aún te queda algo por descubrir."
    scene c17s002_100ae with dissolve
    pause (0.8)
    scene c17s002_100af with dissolve
    mc "Sigue perfectamente depilado por lo que veo. *Risa*"
    mad "En esta casa solo hay espacio para un animalito peludo. *Risita*"
    play sound ("music/Meow.ogg")
    cat "¡Miau! (El rey es el rey)"
    if mar._var("route"):
        mc "Gírate... nunca he tenido la oportunidad de mirarte bien por detrás... sin estar vestida. *Risa*"
        scene c17s002_100ag with dissolve
        mad "*Risa* ¿Cuándo lo has mirado vestida?"
        mc "El día que nos conocimos. Desde el Banco de los Novios hay unas vistas preciosas de tu culo a través de la celosía."
        mad "Mmmm... Tengo que hacer algo con esa celosía."
    else:
        mc "Gírate... nunca he tenido la oportunidad de mirarte bien por detrás... *Risa*"
        scene c17s002_100ag with dissolve
    mad "¿Te gusta lo que ves ahora que lo puedes ver bien?"
    mc "Me parece increíblemente bonito."
    call BlinkXP("c17s002_105a", "d") from _call_BlinkXP_2170
    mad "Déjame quitarme los zapatos y vamos a la cama."
    mc "Déjatelos puestos mejor. Estás super sexy sólo con los ellos."
    mc "Túmbate, por favor, quiero volver a saborearte otra vez."
    mad "Sólo si me dejas probarte a mí después."
    call BlinkXP("c17s002_110a", "f") from _call_BlinkXP_2171
    mad "¿Así?"
    mc "Ahora mismo eres la definición de perfección, estás preciosa."
    scene c17s002_115apv with dissolve
    show c17s002_115av with dissolve
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    "Entierras tu cara entre sus muslos, siendo recibido por el conocido olor pungente que emana de su vagina."
    mad "*Respiración entrecortada* ¡Oh, sí! ¡Cuánto te he echado de menos!"
    "El cuerpo de Maddie responde con estremecimientos a los primeros movimientos de tu lengua."
    mad "*Jadeo* Sigue... llevo cachonda toda la tarde esperando este momento..."
    scene c17s002_120pv with dissolve
    hide c17s002_115av
    show c17s002_120v with dissolve
    "Tu lengua empapa su vagina mientras es empapada a su vez por sus fluidos."
    mad "*Gemido* ¡Oh, [mc]!"
    "Puedes notar cómo el cuerpo de Maddie empieza a vibrar bajo tus manos, anunciando su inminente orgasmo. Ciertamente, debía estar cachonda cuando has llegado."
    mad "*Jadeo* Para, por favor."
    call BlinkXP("c17s002_125", "d") from _call_BlinkXP_2172
    hide c17s002_120v
    mc "¿Pasa algo? ¿No te está gustando?"
    mad "Me está encantando, pero me gustaría aún más si no estuviera aquí pasiva, sólo recibiendo placer."
    mc "Pero es que a mí me encanta dar placer..."
    mad "Y a mí me encanta que sea mutuo, sube a la cama, por favor."
    scene c17s002_130apv with dissolve
    "Maddie te indica como ponerte. No vas a poder seguir usando tu lengua en esa posición."
    "Ella te dice que no te vas a arrepentir."
    show c17s002_130av with dissolve
    "En el momento en que empieza a moverse te das cuenta de que tiene razón. El arrepentimiento no pasa por tu mente."
    mcp "(Con esos movimientos casi parece que quiera arrancarme a Mjolnir del cuerpo. Pero se siente increíble.)"
    mad "*Gemido*"
    "Tus dedos toman el relevo de tu lengua. Maddie sigue gimiendo mientras su boca está ocupada, con lo que demuestra que le está gustando igual... o incluso más."
    mad "*Jadeo*"
    scene c17s002_135apv with dissolve
    hide c17s002_130av
    show c17s002_135av with dissolve
    "Su lengua recorre tu escroto mientras su mano masajea tu polla con un ritmo muy placentero."
    mad "*Gemido*"
    mcp "(Si sigue así no voy a tardar en correrme. Esto es alucinante.)"
    "Los estremecimientos que puedes notar bajo tus dedos confirman que ella está en la misma situación que tú. Su orgasmo se aproxima a la misma velocidad que el tuyo."
    mad "*Jadeo*"
    "Casi parece que estéis haciendo una carrera para comprobar quién hace correrse antes al otro."
    call OrgasmX("c17s002_140a") from _call_OrgasmX_45
    hide c17s002_135av
    mad "*Gemido* ¡Me corroooo!"
    "Si de una carrera se tratara, has ganado... por poco..."
    call OrgasmX("c17s002_145a") from _call_OrgasmX_46
    mc "¡Mpfft!"
    "Sin dejar de masturbarla, riegas el cuerpo de Maddie con tu semen."
    mad "*Jadeo* ¡Sí! ¡Dame tu leche!"
    stop sound fadeout (1.5)
    call BlinkXP("c17s002_150a", "f") from _call_BlinkXP_2173
    mad "¿Te ha gustado?"
    mc "Me ha encantado. Nunca había probado esta posición... ¿Y a ti?"
    mad "Ha sido alucinante... Hacía mucho que no me corría así."
    mad "Déjame ir a limpiarme antes de que esto se enfríe... pero antes..."
    scene c17s002_155a with dissolve
    "Maddie devora tu polla para limpiar los últimos restos de semen."
    "Su juguetona lengua rodea tu astil mientras puedes notar como la punta está a punto de entrar en su garganta."
    call BlinkXP("c17s002_160a", "f") from _call_BlinkXP_2174
    "Un momento después..."
    mad "Dame un momento y ahora vuelvo. Puedes seguir cotilleando la habitación si quieres."
    mc "¿Me estás llamando cotilla? *Risa*"
    call c17s002_InterludeRomDom from _call_c17s002_InterludeRomDom_2
    call BlinkXP("c17s002_170a", "f") from _call_BlinkXP_2175
    mad "Ya estoy de vuelta. Limpia para el siguiente round. A menos que tengas que volver a irte corriendo."
    mc "No, Maddie, hoy soy todo para ti."
    mad "Entonces vuelve a la cama. Se ha acabado la visita turística por la habitación."
    scene c17s002_175aa with dissolve
    "No hace falta que te lo repita."
    "A partir de entonces se suceden un montón de besos..."
    scene c17s002_175ab with dissolve
    "De caricias..."
    scene c17s002_175ac with dissolve
    "Más besos, que van subiendo de intensidad tal como van pasando los minutos."
    call BlinkXP("c17s002_180a", "d") from _call_BlinkXP_2176
    mad "Te necesito dentro de mí. Besas demasiado bien... vuelvo a estar cachonda."
    mc "Pues estás en la posición ideal ahora mismo."
    scene c17s002_180ad with dissolve
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    "Sin mediar palabra, Maddie se empala con Mjolnir."
    mad "*Gemido* ¡Joder! Se nota más grande de lo que esperaba... Y no... *Jadeo* no me estoy quejando."
    scene c17s002_185apv with dissolve
    show c17s002_185av with dissolve
    "Ella empieza a moverse en recorridos bien medidos, cambiando la velocidad entre un recorrido y el siguiente, sin dejar de besarte en todo el proceso."
    mcp "(¡Joder! Esto es una pasada.)"
    "El control que Maddie ejerce del ritmo es algo que nunca has experimentado. Estás acostumbrado a que ese control lo tengas tú."
    mad "*Jadeo*"
    "La sensación de los gemidos de la hermosa mujer en tu boca tan solo incrementa la excitación."
    scene c17s002_190apv with dissolve
    hide c17s002_185av
    show c17s002_190av with dissolve
    "Al cabo de unos minutos sus piernas empiezan a temblar, anunciando que su segunda ronda de orgasmos se está acercando."
    mad "*Gemido* Me... fallan... las piernas... Ayúdame."
    "Con tus manos, que hasta entonces tan solo acariciaban su cuerpo, se convierten en puntos de apoyo que la guían y ayudan en cada recorrido."
    mad "*Jadeo* Estoy a punto... de correrme... otra vez..."
    mc "Córrete para mí, preciosa."
    "Como si tuviera que obedecerte, el coño de Maddie entra en erupción."
    call OrgasmX("c17s002_200a") from _call_OrgasmX_47
    hide c17s002_190av
    mad "*GEMIDO* ¡Por Zeus! *Jadeo* ¡Este es más intenso que el de antes!"
    "Su rápida explosión te pilla por sorpresa. A ti todavía te queda un rato para llegar."
    scene c17s002_185apv with dissolve
    show c17s002_185av with dissolve
    "Continúas guiando su cuerpo arriba y abajo, un cuerpo cada vez más desmadejado, recorrido por oleadas de orgasmos."
    mad "*Gemido* Puedes correrte dónde quieras. Estoy tomando la píldora desde la semana pasada."
    if mc._var("pregnancies") > 0:
        mcp "(Un embarazo menos del que preocuparme.)"
    else:
        mcp "(Genial, no sé si estoy preparado para ser padre todavía.)"
    "Tu clímax se acerca poco a poco, puedes notar cómo la conocida sensación sube por tus piernas mientras Maddie se va convirtiendo en una muñeca rota con cada nuevo orgasmo."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Maddie embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not Whatif:
            play sound ("music/OldMusicBox5.ogg")
            if not Whatif:
                $ mad._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX("c17s002_205a") from _call_OrgasmX_48
    hide c17s002_185av
    mc "¡Mpfft!"
    "Explotas en el interior de Maddie llenándola con tu semilla."
    mad "*Gemido* ¡Sí, lléname! ¡Puedo notar tu leche muy dentro de mí!"
    stop sound fadeout (1.5)
    "Cuando tu descarga finaliza, os derrumbáis sobre la cama, todavía abrazados con tu polla dentro de Maddie."
    call BlinkXP("c17s002_210a", "d") from _call_BlinkXP_2177
    mad "¡Ha sido increíble! No recuerdo haberme corrido así nunca."
    mc "Totalmente alucinante, Maddie. Esos cambios de ritmo..."
    mad "Déjame limpiarte y nos tumbamos a descansar."
    scene c17s002_215a with dissolve
    "Maddie engulle tu polla para limpiar los últimos resquicios de semen que cubren tu astil."
    mc "Podría acostumbrarme a eso después de cada corrida. *Risita*"
    call BlinkXP("c17s002_220a", "d") from _call_BlinkXP_2178
    mad "Pues acostúmbrate. Me encanta el sabor de tu semen. Y mezclado con mis fluidos... Mmmmm..."
    mc "No seré yo el que te prohíba hacerlo. *Risa*"
    mad "Pero aún estás duro como una piedra... ¿Esto no baja nunca?"
    mc "Es difícil que baje cuando acaba de salir de tu preciosa boca."
    call BlinkXP("c17s002_225a", "d") from _call_BlinkXP_2179
    mad "Entonces túmbate, no me gusta desaprovechar una erección tan preciosa."
    mc "A tus órdenes. *Risa*"
    scene c17s002_230aAn with fade #
    "Maddie se vuelve a empalar en Mjolnir. Esta vez con menos gracilidad. Claramente sus piernas no se han recuperado todavía."
    mad "¡Ufff!"
    mc "¿Estás bien?"
    call BlinkXP("c17s002_235", "d") from _call_BlinkXP_2180
    mad "Genial... tan solo es que... ¡Por Zeus! Así te siento más dentro todavía..."
    mc "Si quieres cambiamos de posición."
    mad "No he dicho que fuera malo..."
    scene c17s002_240apv with dissolve
    show c17s002_240av with dissolve
    $renpy.sound.play("music/MaddieMoan.ogg", loop=True)
    mad "*Gemido* Mañana me va a doler todo... *Jadeo*"
    mad "*Gemido* Siento las piernas como si fueran gelatina..."
    "La falta de gracilidad en el empalamiento continúa en los movimientos"
    "Todo el control que ha tenido antes ha desaparecido. Sin embargo, no por ello es menos placentero."
    mad "*Jadeo* Bendito dolor..."
    scene c17s002_245apv with dissolve
    hide c17s002_240av
    show c17s002_245av with dissolve
    "Ya no hay cambios de ritmo. Se nota que tiene dificultades para mantener un ritmo constante, por mucho que le ayudes con tus caderas."
    mad "*Gemido* Y no solo en las piernas... estás destrozándome el cérvix."
    mc "¿Cambiamos?"
    mad "*Jadeo* Te he dicho que no es malo... está siendo increíble..."
    mad "*Gemido* Aunque no creo que me queden más orgasmos... esto es sólo para ti."
    "No los va a tener si sigue concentrada en corregir el errático ritmo."
    "Sí, parece estar disfrutando, pero no lo suficiente."
    scene c17s002_250a with dissolve
    hide c17s002_245av
    "Te incorporas y la abrazas, hundiendo tu cara entre sus tetas."
    mad "*Gemido* ¡Hey! ¡Así casi no puedo moverme!"
    mad "Aunque me encanta lo que estás haciendo. *Jadeo*"
    call BlinkXP("c17s002_255", "h") from _call_BlinkXP_2181
    "Volteas a Maddie, tumbándola de espaldas, sin salir de su interior. Sus piernas estaban a punto de ceder."
    mad "¡Hey! ¡Y así no puedo moverme en absoluto! *Risa*"
    mc "Tú has hecho todo el trabajo hasta ahora. Déjame hacer algo a mí."
    mad "No voy a negar que las piernas me estaban fallando... pero no quería que pensaras que tenía poca resistencia en nuestra primera vez."
    mc "No lo voy a pensar, cielo. Pero déjame seguir a mí."
    scene c17s002_260pv with dissolve
    show c17s002_260v with dissolve
    "Empiezas a bombear con tus caderas. Las piernas de Maddie apuntando al aire."
    mad "*Gemido* ¡Oh, sí! Puedo notarte en todos mis puntos sensibles..."
    "Intentas reproducir los cambios de ritmo de Maddie en la primera vez. No lo consigues del todo, pero es una buena imitación."
    mad "*Jadeo* Olvida lo que he dicho antes sobre que no me iba a volver a correr... ¡Esto es fantástico!"
    scene c17s002_265apv with dissolve
    hide c17s002_260v
    show c17s002_265av with dissolve
    "Saber que está volviendo a disfrutar, que no es algo sólo para ti, hace que tus caderas quieran llevarla al éxtasis."
    mad "*Gemido* ¿Dónde has estado escondido toda mi vida?"
    mad "*Jadeo* ¡Por lo que más quieras, no pares ahora!"
    "No pensabas hacerlo. Puedes notar como el orgasmo de Maddie se acerca."
    "También lo hace el tuyo."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Maddie embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not mad._var("pregnant") and not Whatif:
            play sound ("music/OldMusicBox5.ogg")
            if not Whatif:
                $ mad._var("pregnant", True)
    $ resetWalkthrough ()
    call OrgasmX("c17s002_270a") from _call_OrgasmX_49
    hide c17s002_265av
    " "
    call OrgasmX("c17s002_275a") from _call_OrgasmX_50
    mc "¡Mpffft!"
    mad "*GEMIDO* ¡Oh, SÍ! ¡Me corro!"
    "Vuestros orgasmos llegan casi simultáneamente. Más tarde los dos diréis que el otro ha sido el primero."
    "Da lo mismo quién haya sido el primero."
    mad "*JADEO* ¡No paran! ¡No te muevas, por favor!"
    "Te mantienes inmóvil, tu polla aún dentro de Maddie, notando como cada una de sus contracciones intenta exprimir hasta la última gota de tu semen."
    stop sound fadeout (1.5)
    scene c17s002_280aAnBlink with dissolve #primera persona Maddie relajándose
    "Lentamente su cuerpo se va relajando, volviendo a ser la muñeca rota de hace un rato."
    "Si hubiera continuado arriba, a estas alturas se habría derrumbado encima tuyo."
    mad "Ya está... ya han acabado... mañana no voy a poder juntar las piernas."
    stop music fadeout (1.5)
    call BlinkXP("c17s002_285a", "d") from _call_BlinkXP_2182
    mad "Ha sido totalmente increíble..."
    play music ("music/Wonder.ogg")
    mad "Creo que tengo unas cuerdas por ahí para poder atarte y que no te vayas nunca. *Risa*"
    mc "¿Me dejarías aquí solo cuando te fueras a trabajar? *Risa*"
    call BlinkXP("c17s002_290a", "d") from _call_BlinkXP_2183
    mad "Solo no, con Zeus. *Risa*"
    mad "Pero ahora tengo un sable que limpiar. Déjame levantarme..."
    call BlinkXP("c17s002_295a", "d") from _call_BlinkXP_2184
    mad "No tengas ideas raras aunque sigas duro como una piedra... mi resistencia ha llegado hasta aquí. *Risa*"
    mc "Creo que yo también voy a necesitar unos minutos de descanso."
    mad "*Risa* ¿Minutos? ¡Yo voy a necesitar días!"
    mad "Ponte de rodillas. Ese sable me está llamando."
    scene c17s002_300a with dissolve
    "Maddie cumple su promesa y deja a Mjolnir limpio como una patena."
    "Su lengua vuelve a jugar con toda tu longitud tanto en el camino de ida como en el de vuelta."
    call BlinkXP("c17s002_305a", "d") from _call_BlinkXP_2185
    mad "Ya está, limpio como si aquí no hubiera pasado nada. *Risa*"
    mc "Y duro como si estuviera a punto de pasar. *Risa*"
    mad "*Risa* Ya te he dicho que no tuvieras ideas raras."
    mc "No te preocupes. Te daré esos días de descanso. *Risa*"
    call BlinkXP("c17s002_310a", "d") from _call_BlinkXP_2186
    mad "Túmbate conmigo un rato."
    mc "¿Abrazos? Esa es mi especialidad."
    call BlinkXP("c17s002_315a", "d") from _call_BlinkXP_2187
    mad "Se está bien aquí."
    mc "Ya te he dicho que los abrazos son mi especialidad. *Risa*"
    mad "Y no mentías..."
    mc "Nunca miento, Maddie."
    call BlinkXP("c17s002_320a", "d") from _call_BlinkXP_2188
    mad "Entonces es el momento de preguntarte si te molestaría mucho que no te dejara quedarte a dormir."
    mc "*Risa* ¿Ya te has cansado de mí?"
    call BlinkXP("c17s002_325a", "d") from _call_BlinkXP_2189
    mad "No es eso... me conozco y sé que al despertar querría continuar aunque me doliera todo."
    mad "Y tengo que trabajar en la tienda todo el día... seguramente llegaría tarde."
    mc "No pasa nada, cielo. Lo entiendo. Mañana yo tengo un día ajetreado también."
    call BlinkXP("c17s002_330a", "d") from _call_BlinkXP_2190
    mad "Pero eso no quiere decir que te tengas que ir ya. Déjame disfrutar de estos abrazos un rato más."
    mc "Disfrutémoslos juntos. *Risa*"
    scene c17s002_335a with dissolve
    "Pasáis un rato charlando y disfrutando del contacto de piel contra piel."
    "Habláis del sueño de Maddie de convertirse en diseñadora de ropa, de lo difícil que es abrirse paso en ese mundillo."
    "Charláis sobre tu familia y sobre la empresa. Tiene mucha curiosidad sobre Eva y Amanda."
    "Poco a poco, los últimos rastros de energía van desapareciendo de Maddie y decides irte antes de que se quede dormida."
    call BlinkXP("c17s002_340a", "f") from _call_BlinkXP_2191
    mad "Entonces... ¿nos vemos el domingo?"
    mc "Sí, te pasaré a buscar antes de ir la comida del cumpleaños. Vamos a ser un montón de gente este año."
    mad "¿Qué me pongo?"
    mc "Por mí podrías ir así, pero las chicas van a ir con vestidos. Nada demasiado elegante. Y trae algo cómodo para la tarde y la partida de rol. [dap] me dijo que suelen jugar en pijama."
    call BlinkXP("c17s002_345a", "d") from _call_BlinkXP_2192
    mad "No sé si ir en pijama sería demasiado correcto, aún no las conozco demasiado. Pero si todas están en pijama, si yo llevo un vestido parecería ridícula."
    mad "¿Shorts y camiseta?"
    mc "Genial. Los shorts rojos te hacen un culo precioso."
    call BlinkXP("c17s002_350a", "d") from _call_BlinkXP_2193
    mad "*Risa* Me gusta que te fijes en la ropa que llevo."
    mc "Era imposible no fijarse. *Risa* Ese culo debería estar en un museo."
    mad "Entonces no podrías jugar con él la próxima vez. *Risa* Y es una de mis zonas erógenas."
    mc "Y no lo hemos usado hoy..."
    call BlinkXP("c17s002_355a", "d") from _call_BlinkXP_2194
    mad "Y no lo vamos a usar. *Risa* Si no puedo juntar las piernas mañana, al menos espero poder sentarme."
    mc "No es que lo estuviera proponiendo, pero... la próxima vez ya veremos. "
    call KissXP("c17s002_360a", "d") from _call_KissXP_67
    mad "Vete antes de que te vuelva a desnudar."
    mc "Buenas noches, Maddie. Hasta el domingo."
    stop music fadeout (1.5)
    mad "Hasta el domingo, [mc]."
    return
label c17s002_InterludeRomDom:
    if WI == "":
        if mad._var("romance"):
            call BlinkXP ("c17s002_165a" ,"d") from _call_BlinkXP_2195
        elif mad._var("sub"):
            call BlinkXP ("c17s002_165b" ,"d") from _call_BlinkXP_2196
        elif mad._var("dom"):
            call BlinkXP ("c17s002_165a" ,"d") from _call_BlinkXP_2197
    else:
        if WI == "Rom":
            call BlinkXP ("c17s002_165a" ,"d") from _call_BlinkXP_2198
        elif WI == "Sub":
            call BlinkXP ("c17s002_165b" ,"d") from _call_BlinkXP_2199
        elif WI == "Dom":
            call BlinkXP ("c17s002_165a" ,"d") from _call_BlinkXP_2200
    mad "¿Vas a quedarte en la cama mientras me limpio o vas a cotillear?"
    mc "Se está demasiado solo en esta cama sin hacer nada. *Risa*"
    mad "Pues eso. *Risa*"
    scene c17s002_040c with dissolve
    mc "No me había fijado antes. También tienes decoración y libros sobre gatos. No haré la pregunta tonta de si te gustan los gatos."
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (¿A qué te gustan las estatuas que hacen de mí? ¡Somos vuestros dioses!)"
    mad "*Desde el baño* Me encantan. Zeus es el primero que tengo y quería aprenderlo todo sobre ellos."
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (¿Tengo? Maddie, aún no sabes cómo funciona esto de adorar a un gato, ¿verdad?)"
    scene c17s002_040d with dissolve
    mc "Estos dibujos de vestidos... ¿son tuyos? Son muy chulos..."
    mad "*Desde el baño* Son para un concurso. Es a lo que me quiero dedicar en un futuro, pero es un mercado muy duro."
    mc "Pues me encantan, son muy elegantes."
    mad "*Desde el baño* Es de lo que va el concurso. Pedían diseños de vestidos de ese tipo."
    scene c17s002_040e with dissolve
    mc "¿Te has dado cuenta de que el cuadro tiene una mancha de café?"
    mad "*Desde el baño* Sí, lo sé. Siempre compro los lienzos defectuosos... salen más baratos."
    mad "*Desde el baño* Sé que no está bien, siendo para un regalo, pero no tenía tiempo de comprar lienzos nuevos."
    return
label c17s002_ZeusArrival:
    if WI == "":
        if mad._var("romance"):
            scene c17s002_020a with dissolve
        elif mad._var("sub"):
            scene c17s002_020b with dissolve
        elif mad._var("dom"):
            scene c17s002_020c with dissolve
    else:
        if WI == "Rom":
            scene c17s002_020a with dissolve
        elif WI == "Sub":
            scene c17s002_020b with dissolve
        elif WI == "Dom":
            scene c17s002_020c with dissolve
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (¿Vas a ignorarme después de lo que hice por ti el otro día?)"
    mc "¡Hola, Zeus! ¿Me has echado de menos?"
    if WI == "":
        if mad._var("romance"):
            scene c17s002_025a with dissolve
        elif mad._var("sub"):
            scene c17s002_025b with dissolve
        elif mad._var("dom"):
            scene c17s002_025c with dissolve
    else:
        if WI == "Rom":
            scene c17s002_025a with dissolve
        elif WI == "Sub":
            scene c17s002_025b with dissolve
        elif WI == "Dom":
            scene c17s002_025c with dissolve
    mc "¿Cómo está mi peludo amigo?"
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (Hubiera preferido una latita de atuncito, pero hoy te paso que solo sean caricias. Estás siendo una buena mascota.)"
    mc "¿Me lo parece a mí o estás más cariñoso que el otro día?"
    mad "Nunca lo he visto pedir caricias como te las pide a ti. Cuando vienen mis amigas se mete en mi habitación para no verlas. *Risa*"
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (Tus amigas son como gallinas cuando se ríen. Este tipo te hace sonreír a ti. Hay que cuidarlo aunque no me traiga comida.)"
    if WI == "":
        if mad._var("romance"):
            scene c17s002_030a with dissolve
        elif mad._var("sub"):
            scene c17s002_030b with dissolve
        elif mad._var("dom"):
            scene c17s002_030c with dissolve
    else:
        if WI == "Rom":
            scene c17s002_030a with dissolve
        elif WI == "Sub":
            scene c17s002_030b with dissolve
        elif WI == "Dom":
            scene c17s002_030c with dissolve
    mad "¿Qué quieres, Zeus? ¿Quieres que le enseñe la habitación? ¿Quieres ser la estrella?"
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (¡Ya soy la estrella! Y lo verá en cuanto entre en la habitación.)"
    mc "¿A qué te refieres?"
    mad "Mejor que te lo enseñe. No te rías de mí."
    scene c17s002_035An with dissolve #a-b-c-d
    play sound ("music/Meow.ogg")
    cat "¡Miau! (¡Vamos! ¡Entrad! ¡Que me vea en toda mi gloria!)"
    if WI == "":
        if mad._var("romance"):
            mad "No pensaba en que pasáramos tan pronto a la habitación, pero... Zeus insiste."
        elif mad._var("sub"):
            mad "No creía que quisieras que pasáramos tan pronto a la habitación, pero si Zeus insiste..."
        elif mad._var("dom"):
            mad "No tenía intención de llevarte tan pronto a la habitación, pero Zeus insiste. Y yo también."
    else:
        if WI == "Rom":
            mad "No pensaba en que pasáramos tan pronto a la habitación, pero... Zeus insiste."
        elif WI == "Sub":
            mad "No creía que quisieras que pasáramos tan pronto a la habitación, pero si Zeus insiste..."
        elif WI == "Dom":
            mad "No tenía intención de llevarte tan pronto a la habitación, pero Zeus insiste. Y yo también."
    mc "Mejor no llevarle la contraria, entonces."
    scene c17s002_040a with fade
    mc "¡Wow, Maddie! ¡No sabía que pintabas! Parece un templo dedicado a Zeus."
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (¿Sólo lo parece? Maddie, vas a tener que esforzarte más.)"
    mad "Solo pinto como hobby. Esa es la pared de la fantasía. Gírate."
    scene c17s002_040b with dissolve
    mc "*Risa* Me encantan todas, pero especialmente la del rockero."
    mad "Me divertí mucho pintando esa. Y la que está como un tigre, la pinté el día que lo adopté."
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (Ahí estaba yo, apuntando maneras y siendo fiero.)"
    if WI == "":
        if mad._var("romance"):
            call BlinkXP ("c17s002_045a" ,"d") from _call_BlinkXP_2201
        elif mad._var("sub"):
            call BlinkXP ("c17s002_045b" ,"d") from _call_BlinkXP_2202
        elif mad._var("dom"):
            call BlinkXP ("c17s002_045c" ,"d") from _call_BlinkXP_2203
    else:
        if WI == "Rom":
            call BlinkXP ("c17s002_045a" ,"d") from _call_BlinkXP_2204
        elif WI == "Sub":
            call BlinkXP ("c17s002_045b" ,"d") from _call_BlinkXP_2205
        elif WI == "Dom":
            call BlinkXP ("c17s002_045c" ,"d") from _call_BlinkXP_2206
    mc "¿Y ese cuadro? ¿Es en lo que estás trabajando ahora?"
    play sound ("music/Meow.ogg")
    zeu "¡Miau! (¡Super-michi!)"
    mad "[dap] me dijo que el domingo es su cumpleaños, el de [eri], y el de [emm]."
    mad "Le pregunté si le gustaría un cuadro y me dijo que sí. Este es para ella. Decidí hacerles un cuadro para cada una."
    play sound ("music/Meow.ogg")
    zeu "*Grrr* ¡Miau! (Y con el de [emm] me dieron ganas de cagarme en tu almohada.)"
    mc "Supongo que te ha invitado a la comida del domingo, ¿no?"
    if WI == "":
        if mad._var("romance"):
            call BlinkXP ("c17s002_050a" ,"d") from _call_BlinkXP_2207
        elif mad._var("sub"):
            call BlinkXP ("c17s002_050b" ,"d") from _call_BlinkXP_2208
        elif mad._var("dom"):
            call BlinkXP ("c17s002_050c" ,"d") from _call_BlinkXP_2209
    else:
        if WI == "Rom":
            call BlinkXP ("c17s002_050a" ,"d") from _call_BlinkXP_2210
        elif WI == "Sub":
            call BlinkXP ("c17s002_050b" ,"d") from _call_BlinkXP_2211
        elif WI == "Dom":
            call BlinkXP ("c17s002_050c" ,"d") from _call_BlinkXP_2212
    mad "Sí, me dijo que fuera a comer y me quedara para la partida de DnD. ¿Por qué?"
    mc "Entonces tengo que contarte una cosa. Siéntate, por favor."
    if WI == "":
        if mad._var("romance"):
            call BlinkXP("c17s002_055a", "f") from _call_BlinkXP_2213
        elif mad._var("sub"):
            call BlinkXP("c17s002_055b", "f") from _call_BlinkXP_2214
        elif mad._var("dom"):
            call BlinkXP("c17s002_055c", "f") from _call_BlinkXP_2215
    else:
        if WI == "Rom":
            call BlinkXP("c17s002_055a", "f") from _call_BlinkXP_2216
        elif WI == "Sub":
            call BlinkXP("c17s002_055b", "f") from _call_BlinkXP_2217
        elif WI == "Dom":
            call BlinkXP("c17s002_055c", "f") from _call_BlinkXP_2218
    "Después de La Clonversación..."
    mad "Es increíble. Pero me parece que tomáis demasiados riesgos explicándoselo a tanta gente. Yo incluida."
    if WI == "":
        if mad._var("romance"):
            call c17s002_Rom1 from _call_c17s002_Rom1
        elif mad._var("sub"):
            call c17s002_Sub1 from _call_c17s002_Sub1
        elif mad._var("dom"):
            call c17s002_Dom1 from _call_c17s002_Dom1
    else:
        if WI == "Rom":
            call c17s002_Rom1 from _call_c17s002_Rom1_1
        elif WI == "Sub":
            call c17s002_Sub1 from _call_c17s002_Sub1_1
        elif WI == "Dom":
            call c17s002_Dom1 from _call_c17s002_Dom1_1
    return
label c17s002_Rom1:
    mc "Bueno... tú y yo aún no hemos hablado de lo que somos, pero creo que vamos hacia algún sitio donde la confianza es indispensable."
    call BlinkXP("c17s002_060a", "d") from _call_BlinkXP_2219
    mad "Gracias, [mc]. Creo que tenemos muchas cosas de las que hablar... después de que retrasaras la cita..."
    if mar._var("fittingRoom"):
        mad "Por un momento he pensado que querías cancelarla, en vez de retrasarla. He pensado que... que era porque intenté chantajearte."
        mad "He empezado a montarme películas en mi mente diciéndome que la había cagado por intentarlo... que quizás lo habías pensado mejor y no querías estar conmigo..."
        mc "No, Maddie. Empezamos esto de una forma que no me gustó, pero me está gustando a dónde va."
    else:
        mad "Por un momento he pensado que querías cancelarla, en vez de retrasarla. Que no querías que nos viéramos."
        mc "No, Maddie. Cuando fui a comprarte el disfraz, no tenía intención de empezar nada contigo, pero ahora me está gustando a dónde va esto."
    mc "Y creo que es el momento de comprobarlo, ¿no?"
    return
label c17s002_Sub1:
    mc "Bueno, no creo que mi gatita vaya a hacer nada que me perjudique. A mí o a mi familia."
    mc "Sabes que espié a [mar] en el probador y has guardado el secreto. No por voluntad propia, pero lo has hecho."
    mc "Y no creo que lo revelaras aunque te liberase de sea lo que sea lo que es esto."
    call BlinkXP("c17s002_060b", "d") from _call_BlinkXP_2220
    mad "Nunca haría algo que os perjudique. Cuando has llamado para retrasar la cita... por un momento he pensado que querías cancelarla."
    mad "El corazón me ha dado un vuelco y he descubierto que me gusta lo que tenemos. Que quiero más."
    mad "Me acabas de llamar gatita y he notado mariposas en el estómago. Quiero ser tu gatita, [mc]. Me gusta sentirme indefensa en tus brazos."
    mc "Eres mi gatita, pero no consiste en que estés indefensa. Consiste en que nos lo pasemos bien los dos, no sólo yo."
    mc "Y creo que es el momento de empezar a hacerlo."
    return
label c17s002_Dom1:
    mc "Creo que es algo que debes saber. Sabes que espié a [mar] en el probador y has guardado el secreto."
    mc "Forzándome a esta relación, pero lo has hecho."
    mc "Y estoy seguro de que, si dejásemos esta relación, seguirías guardándolo."
    call BlinkXP("c17s002_060c", "d") from _call_BlinkXP_2221
    mad "No tengo intención de hacer nada que te perjudique. Si acabarais todos en prisión me quedaría sin mi juguete."
    mad "Y sí, puedo guardar los secretos que sean necesarios. Me gusta tenerte. Poseerte. ¿Quién sabe si algún día algo más?"
    mad "Cuándo has llamado para retrasar la cita por un momento he pensado en qué haría si, en vez de retrasarla, la quisieras cancelar."
    mad "¿Contarle el secreto a [mar] o no? He decidido que no lo haría. Quiero que seas mi juguete, pero quiero que lo seas por voluntad propia, no porque te sientas obligado."
    mc "Un día, cuando esté autorizado para hacerlo, te contaré otro secreto. Uno que te demostrará que, si estoy aquí, es porque quiero."
    call BlinkXP("c17s002_065c", "d") from _call_BlinkXP_2222
    mad "Pues, como premio por ello y por la confianza, y sabiendo que te gusta, te voy a permitir de nuevo que me comas. Lo hiciste muy bien el otro día."
    mc "Como mi ama desee. Déjame que te libere de ese mono."
    return
label c17s003_DapScaTests:
    if _in_replay:
        menu:
            "¿Estás en una relación con [dap]?"
            "Sí":
                $ dap._var("route" , True)
            "No":
                $ dap._var("route" , False)
        menu:
            "¿Estás en una relación con Scarlett?"
            "Sí":
                $ sca._var("route" , True)
            "No":
                $ sca._var("route" , False)
        menu:
            "¿Le cogiste el teléfono a tu padre cuando llamó?"
            "Sí":
                $ mc._var("edmundsStory", True)
            "No":
                $ mc._var("edmundsStory", False)
    scene black with dissolve
    centered "{size=+20}{b}DÍA 19 – SÁBADO{/b}{/size}"
    if sca._var("route") or dap._var("route") or mc._var("edmundsStory"):
        play music ("music/ChillUkelele.ogg")
        if sca._var("route") and dap._var("route"):
            "Después de desayunar coges un par de tests de embarazo y vas a la habitación de [dap] y Scarlett."
        elif sca._var("route") or dap._var("route"):
            "Después de desayunar coges un test de embarazo y vas a la habitación de [dap] y Scarlett."
        if mc._var("edmundsStory"):
            "También llevas el test de ADN que Amanda te dio ayer. No sabes cuál de los tests tienes más ganas de que salga positivo."
        scene c17s003_005a with dissolve
        play sound ("music/knock.ogg")
        "*Knock-Knock*"
        mc "Soy yo. ¿Puedo pasar?"
        dap "*A través de la puerta* Sí, entra."
        scene c17s003_005b with dissolve
        mc "Buenos días. Ha llegado el vampiro. Saaaangreeee. *Risa*"
        call KissXP ("c17s003_010" , "d") from _call_KissXP_68
        if dap._var("route"):
            dap "Buenos días, mi amor."
            dap "No va a doler, ¿verdad?"
            mc "Es sólo un pinchazo."
        else:
            dap "Buenos días, [mc]."
        call KissXP ("c17s003_015" , "d") from _call_KissXP_69
        if sca._var("route"):
            sca "Buenos días, guapísimo."
            sca "Tendremos el resultado mañana a estas horas, ¿no?"
            mc "Sí. 24 horas para tenerlo."
            if dap._var("route"):
                call BlinkXP ("c17s003_020" , "d") from _call_BlinkXP_2223
                dap "Si los dos salieran positivos sería un regalo de cumpleaños perfecto."
                dap "Confirmaríamos que voy a ser madre y tía el día de mi cumpleaños."
            else:
                call BlinkXP ("c17s003_020" , "d") from _call_BlinkXP_2224
                dap "Si os saliera positivo sería un regalo de cumpleaños perfecto. Confirmaríais que voy a ser tía el día de mi cumpleaños."
        elif dap._var("route"):
            call BlinkXP ("c17s003_020b" , "d") from _call_BlinkXP_2225
            sca "Tengo ganas de convertirme en la Tía Scarlett."
        if dap._var("route") or sca._var("route"):
            mc "¿Ya os tratáis como hermanas?"
            scene c17s003_005c with dissolve
            dap "¡Por supuesto!" (multiple=2)
            sca "¿Esperabas algo diferente?" (multiple=2)
            mc "*Risa* No."
        scene black with dissolve
        if sca._var("route") and dap._var("route"):
            "Tomas las muestras de sangre y cada una etiqueta su prueba con una pegatina de colores. Las guardáis en un armario, detrás de la ropa de invierno donde nadie lo va a encontrar"
        elif sca._var("route") or dap._var("route"):
            "Tomas las muestras de sangre y guardáis la prueba en un armario, detrás de la ropa de invierno donde nadie lo va a encontrar."
        if mc._var("edmundsStory"):
            call BlinkXP ("c17s003_025" , "d") from _call_BlinkXP_2226
            sca "Y ahora viene mi prueba de ADN, ¿no? ¿Más sangre?"
            mc "No, en este caso es sólo frotar con un hisopo en la parte interior de la mejilla."
            call BlinkXP ("c17s003_030" , "d") from _call_BlinkXP_2227
            dap "Tienes que estar super emocionada. Después de haberte dado por vencida, encontrar esa nueva pista tiene que haber sido increíble."
            scene c17s003_035d with dissolve
            sca "*Ggl GGL*"
            mc "Espera un segundo, que ya acabo."
            call BlinkXP ("c17s003_035" , "d") from _call_BlinkXP_2228
            sca "La verdad es que sí. Ha sido un golpe de suerte. A mi madre no le iba a sacar nada más que mentiras..."
            call BlinkXP ("c17s003_050" , "d") from _call_BlinkXP_2229
            dap "Y supongo que no me vas a decir quién es el candidato."
            call BlinkXP ("c17s003_045" , "d") from _call_BlinkXP_2230
            sca "Ya te he dicho que no puedo. Si sale negativo podría manchar su reputación."
            call BlinkXP ("c17s003_040" , "d") from _call_BlinkXP_2231
            dap "Manchar su reputación... Mmmmm...."
            dap "Pero tú sabes que yo guardaría el secreto, ¿verdad? Sabes que puedes confiar en mi para cualquier cosa."
            call BlinkXP ("c17s003_055" , "d") from _call_BlinkXP_2232
            sca "Sí, [dap], pero pese a todo prefiero no decir nada hasta que no tengamos los resultados."
            call BlinkXP ("c17s003_060" , "d") from _call_BlinkXP_2233
            "... {w} ... {w}... {w}..."
            call BlinkXP ("c17s003_065" , "h") from _call_BlinkXP_2234
            dap "¡Tío Edmund!"
            call BlinkXP ("c17s003_070" , "h") from _call_BlinkXP_2235
            mc "¿Qué?" (multiple=2)
            sca "¿Cómo?" (multiple=2)
            call BlinkXP ("c17s003_075" , "d") from _call_BlinkXP_2236
            dap "Ha sido fácil de deducir. No quieres manchar su reputación diciéndomelo a mí, lo que significa que lo conozco. Y lo tengo que conocer bien."
            dap "La mayoría de los profesores del instituto son demasiado jóvenes para ser tus padres o lo más probable es que estuvieran solteros cuando te concibieron, con lo que no habría reputación que manchar."
            call BlinkXP ("c17s003_080" , "d") from _call_BlinkXP_2237
            if persistent.family:
                dap "Eso dejaba a mi padre, al Tío Daniel, al Tío Dominic, y al Tío Edmund como candidatos."
            else:
                dap "Eso dejaba como candidatos al tío Edmund o a mi padre... bueno... mi padre..."
            dap "Pero tiene que estar vivo porque le estaba mandando dinero a tu madre."
            dap "Además, [mc] lo sabe y está implicado en esto de alguna forma que no me habéis dicho, con lo que... Tío Edmund."
            call BlinkXP ("c17s003_085" , "d") from _call_BlinkXP_2238
            dap "Y si me hubiera equivocado me habríais dicho algo en plan \"No, [dap], y no continúes insistiendo\"."
            dap "En vez de eso habéis dicho \"¿Qué? ¿Cómo?\", con lo que si tenía alguna duda vosotros la habéis resuelto. Soy buenísima en esto. *Risa*"
            mc "Joder, [dap], eres demasiado lista a veces."
            call BlinkXP ("c17s003_090" , "d") from _call_BlinkXP_2239
            sca "Ahora que sabe el secreto tendremos que matarla..."
            mc "Y enterrar su cadáver en el bosque... *Risa*"
            call BlinkXP ("c17s003_095" , "d") from _call_BlinkXP_2240
            dap "Eva y Amanda me protegerán. *Risa*"
            mc "¿La misma Eva que quitó las cámaras de tu habitación y no sabe lo que está pasando ahora?"
            call BlinkXP ("c17s003_100" , "d") from _call_BlinkXP_2241
            dap "*Risa* ¡Oh, mierda!"
            call BlinkXP ("c17s003_105" , "d") from _call_BlinkXP_2242 #abrazo
            if sca._var("route"):
                if persistent.family:
                    dap "Sé que no te querías hacer ilusiones, pero la perspectiva de que seas mi prima de verdad... y... la... hermana... de... [mc]..."
                else:
                    dap "Sé que no vamos a ser primas de sangre, pero la perspectiva de que seas... la... hermana... de... [mc]..."
                call BlinkXP ("c17s003_110" , "h") from _call_BlinkXP_2243
                dap "¡Oh, mierda! ¡Puede que seáis hermanos y que vayáis a tener un hijo juntos!"
                sca "Sí, nos enteramos después de nuestra primera vez..."
                mc "Lo sabemos, [dap]. Pero no queremos tomar ninguna decisión antes de los resultados. Si lo llevo hoy directamente al laboratorio, podemos tenerlos el martes."
            else:
                if persistent.family:
                    dap "Sé que no te querías hacer ilusiones, pero la perspectiva de que seas mi prima de verdad y la hermana de [mc] y [emm]..."
                else:
                    dap "Sé que no vamos a ser primas de sangre, pero la perspectiva de que seas la hermana de [mc]..."
                mc "Por eso no queremos ilusionarnos antes de los resultados. Si salieran negativos... Si lo llevo hoy directamente al laboratorio, podemos tenerlos el martes."
            scene c17s003_115a with dissolve
            dap "¡Pues ya estás tardando en irte! *Risa*" (multiple=2)
            sca "¿El martes? ¡Vete ya! *Risa*" (multiple=2)
            mc "Tengo que explicarle unas cosas a Tía Betty y después lo llevaré. Os veo luego."
            scene black with dissolve
            "Dejas el test de Scarlett en la camioneta y vas al baño donde has quedado con Tía Betty y Meemaw."
        else:
            scene c17s003_120a with dissolve
            dap "Ahora toca esperar." (multiple=2)
            sca "24 horas que se van a hacer larguísimas." (multiple=2)
            mc "Os voy a dejar esperando solas. Tengo que explicarle unas cosas a Tía Betty. Os veo luego."
            scene black with dissolve
            "Te diriges al baño donde has quedado con Tía Betty y Meemaw."
    else:
        "Cuando te despiertas, tras desayunar, te diriges al baño que comparten Tía Betty y Meemaw."
    stop music fadeout (1.5)
    return
label c17s003_BettyMassage:
    if _in_replay:
        menu:
            "¿Estás en una relación con Meemaw?"
            "Sí":
                $ mee._var("route" , True)
            "No":
                $ mee._var("route" , False)
        menu:
            "¿Le cogiste el teléfono a tu padre cuando llamó?"
            "Sí":
                $ mc._var("edmundsStory", True)
            "No":
                $ mc._var("edmundsStory", False)
    "Mientras tanto, en el baño de la planta de Meemaw y Tía Betty..."
    scene c17s003_150a with dissolve
    play music ("music/SadSoul.ogg")
    bet "¿Pasa algo? Te veo pensativa desde el desayuno."
    bet "Sé que te ha molestado no poder empezar el tratamiento aún... ¿O tiene que ver con Amanda y Eva?"
    mee "No, no es por eso... ¿puedo hacerte una pregunta? Y no quiero que me juzgues..."
    bet "Adelante, pregunta lo que quieras. Sabes que estoy aquí para ti."
    call BlinkXP ("c17s003_155" , "d") from _call_BlinkXP_2244
    mee "¿Tú crees que tener un sueño erótico es una forma de poner los cuernos?"
    call BlinkXP ("c17s003_160" , "d") from _call_BlinkXP_2245
    bet "¿Ponerle los cuernos a quién?"
    call BlinkXP ("c17s003_165" , "d") from _call_BlinkXP_2246
    mee "A John, obviamente..."
    call BlinkXP ("c17s003_170a" , "d") from _call_BlinkXP_2247
    bet "Cielo, no le estarías engañando con un sueño ni aunque siguiera entre nosotros. Pero hace 22 años que John se fue."
    bet "No serían cuernos incluso si empezaras una relación con alguien ahora. Le has guardado suficiente luto. [mc] ha vivido toda una vida sin conocerlo."
    call BlinkXP ("c17s003_175" , "h") from _call_BlinkXP_2248
    mee "¿Que tiene que ver [mc] en esto?"
    call BlinkXP ("c17s003_170b" , "d") from _call_BlinkXP_2249
    bet "Nada. Tan solo lo decía porque si él ha vivido toda una vida desde que John murió, es una demostración de que le has guardado el luto suficiente."
    bet "¿Qué has soñado para que estés tan abatida?"
    call BlinkXP ("c17s003_180" , "d") from _call_BlinkXP_2250
    mee "¿Te acuerdas del día que John se declaró? ¿De lo que me dijo sobre la familia?"
    call BlinkXP ("c17s003_190" , "d") from _call_BlinkXP_2251 #John
    bet "¡Cómo voy a olvidarlo! Me lo has explicado mil veces. En su piso, vestido como Tony Menero, y tú como Stephanie Mengano."
    "John" "La familia es lo más importante, no sólo en la que naces, también a la que eliges. Olivia, ¿quieres elegirme para ser tu familia?"
    mee "Pues he soñado que no era John quién me lo decía, sino otro hombre..."
    call BlinkXP ("c17s003_195" , "d") from _call_BlinkXP_2252 #MC
    mc "La familia es lo más importante, no sólo en la que naces, también a la que eliges. Olivia, ¿quieres elegirme para ser tu familia?"
    mee "Me he sentido como si estuviera engañando a John, cambiando el recuerdo de aquel día."
    bet "¿Y eso ha sido el sueño erótico? Siempre pensé que te dio el anillo en una caja, no que lo llevara... ya sabes dónde."
    call BlinkXP ("c17s003_185" , "d") from _call_BlinkXP_2253 #Meemaw
    mee "¡Betty!"
    if mee._var("route"):
        call BlinkXP ("c17s003_200a" , "f") from _call_BlinkXP_2254
        mee "Es que el sueño no acaba ahí... Después soñé con la noche de bodas también con ese hombre..."
        scene c17s003_200b with fade
        mee "Podía notar cómo sus manos recorrían mi piel, como se me erizaba el vello de todo el cuerpo..."
        call BlinkXP ("c17s003_200c" , "f") from _call_BlinkXP_2255
        mee "Pero cuándo estábamos a punto de hacer el amor... te aseguro que lo deseaba en el sueño..."
        call BlinkXP ("c17s003_200d" , "d") from _call_BlinkXP_2256
        mee "Dejé de ser joven y volví a ser la vieja que soy ahora... y seguía deseándolo..."
        call BlinkXP ("c17s003_205" , "d") from _call_BlinkXP_2257
        mee "Me he asustado y me he despertado empapada... en sudor..."
    else:
        call BlinkXP ("c17s003_205" , "d") from _call_BlinkXP_2258
        mee "Es que el sueño no acaba ahí... Después soñé con la noche de bodas también con ese hombre..."
        mee "Por suerte me desperté justo antes de que hiciéramos el amor. Me he despertado empapada... en sudor..."
    call BlinkXP ("c17s003_210a" , "d") from _call_BlinkXP_2259
    bet "¿Sólo empapada en sudor?"
    call BlinkXP ("c17s003_215a" , "d") from _call_BlinkXP_2260
    mee "Betty, estoy hablando en serio..."
    call BlinkXP ("c17s003_210b" , "d") from _call_BlinkXP_2261
    bet "Sólo bromeaba. No, no es ponerle los cuernos a John."
    bet "Después de lo que ha pasado en estos últimos días, cómo [mc] incluyo a Amanda y a Eva en la familia, especialmente anoche con Amanda..."
    bet "No me extraña que hayas soñado con aquellos días. Cuando se declaró y la noche de bodas."
    bet "Empezaste una nueva familia entonces, con John, y ahora la familia está cambiando, mutando en algo nuevo. En algo diferente que ya no incluye a John."
    call BlinkXP ("c17s003_215b" , "d") from _call_BlinkXP_2262
    mee "Debe ser eso... pero ¿por qué otro hombre? Nunca había tenido un sueño con otro hombre..."
    call BlinkXP ("c17s003_220" , "d") from _call_BlinkXP_2263
    bet "Los sueños no tienen por qué tener sentido. Podría ser porque, ahora mismo, es otro hombre el que está moviéndolo todo para crear una familia nueva."
    bet "Si te paras a pensarlo, Alexia, Eileen, Kiara, Samantha, y Simone se están uniendo a la familia gracias a [mc]."
    call BlinkXP ("c17s003_225" , "d") from _call_BlinkXP_2264
    bet "Amanda y Eva en gran parte también. No sé si te diste cuenta de cómo lo buscaban en todo momento. Es como si él fuera su ancla en esta familia."
    bet "Más incluso que [nor] y [mar]."
    call BlinkXP ("c17s003_230" , "d") from _call_BlinkXP_2265
    bet "Y puede que [mc] no se parezca físicamente a John, pero parece mentira lo mucho que se parecen en otras cosas. Especialmente en su concepto de familia."
    bet "Desde el primer día me sentí aceptada por John como parte de vuestra familia. Cada vez que iba a vuestra casa me sentía como se debieron sentir Eva y Amanda ayer..."
    bet "Salvando las diferencias, claro. Yo ya pertenecía a una familia."
    call BlinkXP ("c17s003_235" , "d") from _call_BlinkXP_2266
    mee "La verdad es que sí, su concepto de familia era diferente al de los demás."
    if persistent.family:
        mee "Intentamos inculcarles ese concepto a nuestros hijos, y parece que ha funcionado. Incluso nuestros nietos lo tienen."
    else:
        mee "Intentamos inculcarle ese concepto a [nor], y parece que ha funcionado. Incluso el resto se ha contagiado."
    mee "Especialmente [mc]..."
    call BlinkXP ("c17s003_240" , "d") from _call_BlinkXP_2267
    bet "Es que [mc] se parece mucho a John, y no solo en lo de la familia. Tiene un montón de cosas de él. Cómo trata a la gente, cómo respeta las opiniones de todo el mundo pero es firme en las suyas..."
    bet "Incluso tiene la ingenuidad que tenía John para muchas cosas. Por no hablar de lo mucho que te quiere..."
    call BlinkXP ("c17s003_245" , "d") from _call_BlinkXP_2268
    bet "¡Oh, Libby! Ahora entiendo muchas cosas..."
    bet "¡Has tenido un sueño húmedo con [mc]!"
    call BlinkXP ("c17s003_250" , "d") from _call_BlinkXP_2269
    mee "¿Qué? ¿Estás loca?"
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "*A través de la puerta* Soy yo. ¿Puedo pasar? ¿Estáis vestidas?"
    call BlinkXP ("c17s003_255" , "d") from _call_BlinkXP_2270
    bet "*Risa* Pasa, cariño."
    stop music fadeout (1.5)
    scene black with dissolve
    "Le explicas a Tía Betty todo lo que la Dra. Milk te explicó durante la visita de ayer."
    "Por alguna razón que no entiendes, Tía Betty está especialmente risueña, y os mira con ternura a Olivia y a ti mientras le explicas todo."
    "Olivia está todavía más incómoda que en el hospital. Creías que después de la conversación en el aparcamiento se le habría pasado."
    if mee._var("route"):
        "Tener a Tía Betty delante evita que tengas una erección, con lo que no se repite el episodio de ayer."
        "Además, Olivia rehúye tu contacto, manteniendo su culo lo más alejado posible de Mjolnir."
        "Normal, con lo que le avergonzó el orgasmo de ayer delante de la doctora... No puedes imaginar lo que la avergonzaría delante de su hermana la monja."
    "Cuando terminas las explicaciones, te piden que les dejes intimidad para que Tía Betty pueda practicar."
    "No te crees que quieran que las dejes solas por eso. Si fuera para practicar lo lógico sería que estuvieras tú para corregir los errores, ¿no?"
    if mc._var("edmundsStory"):
        "Aprovechas el tiempo y decides llevar el test de ADN de Scarlett hasta Atascadero tras pasarte el hisopo por el interior de la mejilla."
        "Una hora después vuelves a estar en casa."
    "Cuando estás a punto de entrar en casa, llega un camión de Amazonian. Traen unas cosas que has pedido para el domingo."
    mcp "{i}(Esto me recuerda que tengo que pedir algo más.){/i}"
    return
label c17s003_TellKiara:
    "Justo al acabar el pedido..."
    scene c17s003_300a with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    eil "*A través de la puerta* Somos nosotras. ¿Estás visible?"
    play music ("music/Looking-Forward.ogg")
    mc "Sí, pasad."
    scene c17s003_300b with dissolve
    mc "¿Os puedo ayudar en algo?"
    kia "No sé, Eileen me ha dicho que teníamos que venir."
    mc "Sí, creo que será mejor que te sientes."
    eil "Por un momento casi me había parecido que te habías olvidado."
    call BlinkXP ("c17s003_305" , "d") from _call_BlinkXP_2272
    kia "A ver, contadme el gran secreto. ¿Habéis decidido casaros ya?"
    mc "No es eso, al menos no aún."
    call BlinkXP ("c17s003_310" , "d") from _call_BlinkXP_2273
    eil "A ver, Mamá... lo primero es que me tienes que prometer que no vas a decir nada."
    eil "No queremos que se repita lo de la cocina de anteayer."
    call BlinkXP ("c17s003_315" , "d") from _call_BlinkXP_2274
    kia "Lo siento, creía que todo el mundo lo sabía... es tan obvio..."
    mc "Por eso Eileen te está avisando con antelación. Eres la primera que lo va a saber."
    stop music fadeout (1.5)
    kia "Vaaale... lo prometo."
    play music ("music/Dark-Score.ogg")
    call BlinkXP ("c17s003_320" , "d") from _call_BlinkXP_2275
    eil "No voy a volver a casa cuando acabe la semana que nos dimos de plazo."
    call BlinkXP ("c17s003_325" , "d") from _call_BlinkXP_2276
    kia "¿Por qué? ¿Voy a tener que volver sola?"
    mcp "(Esto no es lo que esperaba.)"
    call BlinkXP ("c17s003_330" , "d") from _call_BlinkXP_2277
    eil "Creo que tú tampoco deberías volver. Con tu sueldo y el mío podemos buscar un sitio para las dos."
    mc "No hace falta que os vayáis, Eile."
    call BlinkXP ("c17s003_335" , "d") from _call_BlinkXP_2278
    kia "Pero ¿por qué no quieres volver a casa?"
    call BlinkXP ("c17s003_340" , "d") from _call_BlinkXP_2279
    eil "Primero porque anoche te oí llorar. Como haces todas las noches desde que estamos aquí cuando crees que me he quedado dormida."
    eil "Tú tampoco quieres volver, pero aún no lo has aceptado."
    call BlinkXP ("c17s003_345" , "d") from _call_BlinkXP_2280
    kia "Es que no lo entiendes... es mi casa... nuestra casa..."
    call BlinkXP ("c17s003_350" , "d") from _call_BlinkXP_2281
    eil "Lo sé. Es nuestra casa, pero no es nuestro hogar. Lo vi claro anoche con Amanda."
    eil "Estás más a gusto aquí de lo que nunca has estado en casa. Y más segura."
    eil "Si no quieres que nos quedemos, no nos quedaremos. No tenemos que imponerles nada."
    mc "No nos estáis imponiendo nada, Eileen."
    call BlinkXP ("c17s003_355" , "d") from _call_BlinkXP_2282
    eil "¡Calla! Estoy hablando con mi madre."
    call BlinkXP ("c17s003_350" , "d") from _call_BlinkXP_2283
    eil "He visto cómo te llevas con todo el mundo. Todo el mundo te quiere y tú empiezas a quererlos."
    eil "No voy a volver a lo que teníamos en nuestra casa."
    call BlinkXP ("c17s003_360" , "d") from _call_BlinkXP_2284
    kia "Vale... ya hablaremos de eso... No es algo con lo que tengamos que molestar a [mc], discutiéndolo delante de él.."
    kia "Pero has dicho \"Primero\". Significa que hay más cosas."
    call BlinkXP ("c17s003_365" , "d") from _call_BlinkXP_2285
    eil "Sí, Mamá, aunque está relacionado."
    eil "Tú eres mi familia."
    eil "También lo es ese hombretón de ahí que me está mirando como si no entendiera nada."
    eil "Y también lo son las chicas."
    call BlinkXP ("c17s003_370" , "d") from _call_BlinkXP_2286
    eil "Quién no es mi familia es Papá."
    call BlinkXP ("c17s003_375" , "d") from _call_BlinkXP_2287
    kia "Pero es tu padre..."
    call BlinkXP ("c17s003_380" , "d") from _call_BlinkXP_2288
    eil "¿Crees que [mc] sería un buen padre, Mamá?"
    call BlinkXP ("c17s003_385" , "d") from _call_BlinkXP_2289
    kia "Claro. Ya sabes que lo quiero mucho. Y no lo querría si no pensara que es bueno."
    mcp "(Aunque llevas un par de días distante conmigo.)"
    call BlinkXP ("c17s003_380" , "d") from _call_BlinkXP_2290
    eil "¿Crees que alguna vez me haría un morado como el que llevas en el brazo?"
    call BlinkXP ("c17s003_390" , "d") from _call_BlinkXP_2291
    kia "No..."
    call BlinkXP ("c17s003_380" , "d") from _call_BlinkXP_2292
    eil "¿Crees que alguna vez me haría desear irme de casa? ¿Con mi hija?"
    call BlinkXP ("c17s003_390" , "d") from _call_BlinkXP_2293
    kia "No..."
    call BlinkXP ("c17s003_395" , "d") from _call_BlinkXP_2294 #tocándose la barriga
    eil "Y ¿crees que nuestra hija tendrá miedo de verlo cuando esté embarazada?"
    eil "¿Que ella tendrá miedo de que le dé una paliza que le haga perder el bebé?"
    call BlinkXP ("c17s003_400" , "d") from _call_BlinkXP_2295 #enfadada
    kia "¡Por supuesto que no! Ya te he dicho..."
    stop music fadeout (1.5)
    call BlinkXP ("c17s003_405" , "d") from _call_BlinkXP_2296 #neutral
    kia "... que es..."
    call BlinkXP ("c17s003_415" , "d") from _call_BlinkXP_2297 #sorprendida
    kia "... un buen hombre."
    call BlinkXP ("c17s003_410" , "d") from _call_BlinkXP_2298 #contenta
    play music ("music/CelticFlute.ogg")
    kia "¡No puede ser! ¿Estás embarazada?"
    call BlinkXP ("c17s003_420" , "d") from _call_BlinkXP_2299
    eil "Sí, Mamá. Estamos embarazados."
    call BlinkXP ("c17s003_425" , "h") from _call_BlinkXP_2300 #abrazo
    kia "¡Felicidades, cielo!"
    eil "Gracias, Mamá. Estamos muy ilusionados."
    scene c17s003_430An with dissolve #d-e(abrazo rapido)-a (se separa)
    kia "Felicidades a ti también, Papá."
    mcp "(Ahora entiendo lo de \"más frío que el abrazo de una suegra\".)"
    mc "Gracias, Kiara."
    call BlinkXP ("c17s003_435" , "d") from _call_BlinkXP_2301
    kia "¿Ya habéis pensado en nombres?"
    scene c17s003_440 with dissolve #Los tres juntos
    eil "No, aún no pero..."
    "A partir de ese momento empieza una larga conversación sobre nombres de bebé, consejos sobre cómo llevar el embarazo, qué hacer y qué no hacer, el trabajo de Eileen..."
    "Kiara dice un montón de cosas en las que no habías pensado y otras que con un poco de sentido común cualquiera podría deducir."
    "Crees que vas a comprarte un libro de esos sobre bebés."
    call BlinkXP ("c17s003_445" , "d") from _call_BlinkXP_2302
    eil "Deberíamos ir bajando para ayudar con la comida. Amanda tiene que estar a punto de llegar."
    mc "Podéis quedaros aquí un rato más hablando de esas cosas que no se habla delante del padre. Ya voy yo a ver si necesitan ayuda."
    call KissXP ("c17s003_450" , "d") from _call_KissXP_70
    eil "Vale, mi amor. Te veo abajo en un rato."
    mc "Hasta ahora, mi vida. Te quiero."
    eil "Yo también."
    call BlinkXP ("c17s003_455" , "d") from _call_BlinkXP_2303
    kia "Si necesitáis ayuda, avisadnos."
    mc "Tranquila, bajad en 20 minutos más o menos."
    stop music fadeout (1.5)
    return
label c17s003_AmandaLunch:
    if _in_replay:
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
            "No":
                $ mar._var("route" , False)
        menu:
            "¿Estás en una relación con [nor]?"
            "Sí":
                $ nor._var("route" , True)
            "No":
                $ nor._var("route" , False)
        menu:
            "¿Estás en una relación con Eileen?"
            "Sí":
                $ eil._var("route" , True)
                menu:
                    "¿Está embarazada?"
                    "Sí":
                        $ eil._var("pregnancyDiscovered" , True)
                    "No":
                        $ eil._var("pregnancyDiscovered" , False)
            "No":
                $ eil._var("route" , True)
                $ eil._var("pregnancyDiscovered" , False)
        menu:
            "¿Estás en una relación con Samantha?"
            "Sí":
                $ sam._var("route" , True)
            "No":
                $ sam._var("route" , False)
        menu:
            "¿Estás en una relación con Simone?"
            "Sí":
                $ sim._var("route" , True)
            "No":
                $ sim._var("route" , False)
    scene black with dissolve
    "Cuando llegas a la cocina, ya está casi todo hecho. Ayudas haciendo el all i oli y preparas las bebidas."
    scene c17s003_500d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP("c17s003_500" , "d") from _call_BlinkXP_2271
    play music ("music/Stardust.ogg")
    "Al poco rato llega Amanda. Esta vez ha venido en la moto de Eva."
    if not _in_replay:
        $ renpy.notify ("Profile Image unlocked for Amanda: 1 - Casual")
        $ ama.profileImages.pop (0) # first remove
        $ ama.profileImages.insert (0, ("amanda_00", None)) # then add new
    ama "No sé si llego demasiado pronto..."
    mc "No te preocupes. Llegas justo a tiempo."
    call KissXP ("c17s003_500b" , "d") from _call_KissXP_71
    ama "Buenos días, [mc]."
    mc "Buenos días, Amanda. Pasa, te están esperando."
    scene c17s003_505a with dissolve
    "La comida sigue la misma dinámica que la cena, aunque esta vez nadie hace llorar a Amanda."
    "Echas de menos aquellos días en los que comíais sentados, pero le estás cogiendo el gusto a estas comidas de pie."
    scene c17s003_505b with dissolve
    "Puedes ver que Megan y [mar] tienen una larga conversación entre ellas, apartadas de todo el mundo."
    scene c17s003_505c with dissolve
    "Amanda pasa más tiempo con las mujeres esta vez. Ayer se retuvieron un poco, pero hoy quieren su ración de la nueva incorporación a la familia."
    "Amanda tardará un poco en dejar de sentirse como un animal exhibido."
    scene c17s003_505d with dissolve
    "Esta vez las chicas tienen una nueva presa. Megan."
    call BlinkXP ("c17s003_510" , "d") from _call_BlinkXP_2304
    nor "Amanda nos ha contado las noticias. Ya no corremos peligro."
    mc "Son grandes noticias. Aaron parece estar haciendo un trabajo fantástico."
    mc "Aún estoy dudando de si debería aceptar el trabajo en Aruba... eso si no vendemos, claro. No sé si estaré a la altura."
    call BlinkXP ("c17s003_515" , "d") from _call_BlinkXP_2305
    nor "[mar] y yo no queremos vender la empresa."
    nor "Hacerlo significaría que habrá más chicas como Eva y Amanda. Mas niñas como Fiona."
    mc "Yo también creo que deberíamos mantenerla en manos de la familia."
    call BlinkXP ("c17s003_520" , "d") from _call_BlinkXP_2306
    nor "Y cuando te refieres a familia, también te refieres a Eva y a Amanda, ¿no?"
    mc "Para mí, ellas son las principales víctimas de NTR. No sólo ellas. También Aaron y el resto de los clones masculinos. Incluidos los que entraron en casa."
    mc "Y, obviamente, ellas son familia. Ya viste cómo se puso Amanda ayer cuando se sintió aceptada. No quiero que nadie les robe eso. Ya le han robado su infancia."
    call BlinkXP ("c17s003_525" , "d") from _call_BlinkXP_2307
    nor "[dap] y [eri] tampoco quieren vender. Estoy muy orgullosa de ellas."
    nor "[emm] dice que tiene dudas, pero no ha dicho sobre qué."
    mc "Hablaré con [emm] sobre ello. Ayer ya quería gastarse el dinero en un coche deportivo... rosa."
    mc "Ya sabes que a veces necesita un empujón en la dirección correcta."
    mc "Ahora te voy a dejar un momento. Tengo que hablar con Kiara y quiero aprovechar ahora que se ha quedado sola."
    call BlinkXP ("c17s003_525b" , "d") from _call_BlinkXP_2308
    nor "Ve. Es casi tan popular como Amanda y Eva. Es difícil que esté sola más de unos minutos. También es novedad, parece mentira que sólo sea su cuarto día en casa."
    stop music fadeout (1.5)
    call BlinkXP ("c17s003_530" , "f") from _call_BlinkXP_2309
    play music ("music/Between-Heaven-And-Earth.ogg")
    mc "¿Qué tal, Kiara?"
    if eil._var("pregnancyDiscovered"):
        kia "Muy contenta con las noticias de antes. *Susurrando* Aunque ser abuela me haga sentir vieja."
        kia "Y alucinando con lo rápido que se está integrando todo el mundo."
    else:
        kia "Alucinando con lo rápido que se está integrando todo el mundo."
    mc "¿Y tú? ¿Qué tal llevas la integración?"
    call BlinkXP ("c17s003_535" , "d") from _call_BlinkXP_2310
    kia "Genial. Me siento muy a gusto aquí, con vosotros."
    kia "Te tengo que dejar. Tenía que comentarle algo a Betty."
    mc "¿He hecho algo malo, Kiara?"
    call BlinkXP ("c17s003_540" , "d") from _call_BlinkXP_2311
    kia "¿Por qué dices eso?"
    mc "Me da la impresión de que me estás evitando desde hace un par de días."
    kia "No... no te estoy evitando."
    mc "¿Entonces qué pasa? Desde que fuimos a tu casa parece que no estás cómoda cuando yo estoy alrededor."
    if mar._var("route") or nor._var("route"):
        mc "¿Es por lo que pasó en la cocina? ¿Por mis relaciones? ¿Por los besos? ¿Por lo que pasó en tu casa con Solomon?"
    elif eil._var("route"):
        mc "¿Es porque estoy con Eileen? ¿Por los besos? ¿Por lo que pasó en tu casa con Solomon?"
    else:
        mc "¿Es por los besos? ¿Por lo que pasó en tu casa con Solomon?"
    call BlinkXP ("c17s003_545" , "d") from _call_BlinkXP_2312
    kia "No es que esté incómoda a tu alrededor..."
    kia "No estoy acostumbrada a que nadie, excepto Eileen, me defienda como hiciste tú en casa."
    scene c17s003_550An #a-b normal-dragón
    kia "Por un momento me sentí como se deben sentir las princesas en los cuentos de hadas. Protegida. Segura."
    if not _in_replay:
        $ renpy.notify ("Profile Image unlocked for Kiara: 7 - DnD")
        $ kia.profileImages.pop (6) # first remove
        $ kia.profileImages.insert (6, ("kiara_6", None)) # then add new
    call BlinkXP ("c17s003_555" , "d") from _call_BlinkXP_2313
    kia "Después... cuando nos abrazamos los tres en el parque... me sentí rara."
    mc "¿Rara? ¿Por qué? Sólo fue un abrazo. Siempre te han gustado mis abrazos."
    call BlinkXP ("c17s003_560" , "d") from _call_BlinkXP_2314
    kia "Si te lo explicara no lo entenderías. Y además me sentiría estúpida explicándotelo."
    mc "Puedes probar a hacerlo. Hay gente que dice que no soy tan tonto como parezco."
    kia "No es eso. Pero no te preocupes. No es que hayas hecho nada... malo."
    scene c17s003_565An with dissolve # a-b-c Mirando a ver si ve a alguien
    "Kiara empieza a comprobar la cocina, claramente buscando a alguien con quien hablar para librarse de ti."
    call BlinkXP ("c17s003_570" , "d") from _call_BlinkXP_2315
    kia "Debería ir a hablar con..."
    call BlinkXP ("c17s003_575" , "h") from _call_BlinkXP_2316 #abrazo, ella sorprendida
    mc "Ve con Betty si tienes que ir, pero no huyas de mí, por favor. No huyas de nosotros."
    scene c17s003_575d with dissolve #abrazo. Ella con los ojos cerrados
    kia "No quiero huir, [mc]."
    kia "Es... es... complicado..."
    scene c17s003_575e with hpunch #se separa
    pause (1.0)
    call BlinkXP ("c17s003_580" , "d") from _call_BlinkXP_2317
    kia "¡No! ¡No es complicado!"
    if eil._var("pregnancyDiscovered"):
        kia "*Susurrando* ¡Vas a ser el padre de mis nietos!"
    elif eil._var("route"):
        kia "*Susurrando* ¡Estás con mi hija!"
    kia "¡Soy una mujer casada!"
    mc "¿Qué? ¿Qué tiene que ver eso?"
    scene c17s003_580d with dissolve
    kia "Ya te he dicho que no lo entenderías si te lo explicaba."
    mc "Pero no me has explicado nada..."
    stop music fadeout (1.5)
    mc "¿Qué me he perdido?"
    play music ("music/SneakySnitch.ogg")
    bet "Al final resultará que no eres tan listo como yo pensaba."
    call BlinkXP ("c17s003_585" , "d") from _call_BlinkXP_2318
    mc "Hola, Tía Betty. ¿Qué quieres decir?"
    bet "No eres capaz de descubrir lo que le pasa a Kiara por ti mismo, ¿verdad?"
    mc "¿Sinceramente? No tengo ni idea de lo que está pasando ni de a qué te refieres."
    call BlinkXP ("c17s003_590" , "d") from _call_BlinkXP_2319
    bet "¿Quieres que te dibuje un plano o prefieres ir a ciegas?"
    mc "Una cosa es ir a ciegas, pero ahora voy sin plano, sin linterna, de noche, con los ojos vendados y las manos atadas."
    bet "Ven conmigo detrás de la isla. Podremos hablar más tranquilos allí."
    call BlinkXP ("c17s003_595" , "f") from _call_BlinkXP_2320
    bet "¿Qué crees que le pasa a Kiara?"
    mc "No tengo ni idea. Todo iba genial hasta el día que fuimos a su casa. Con lo que lo único que se me ocurre es que fuera por lo que pasó con Solomon."
    bet "Estamos hablando del mismo día en que empezamos los saludos con besos otra vez, ¿no? Culpa mía."
    mc "Sí, claro. Fue el mismo día."
    if mar._var("route") or nor._var("route"):
        bet "Después de lo que pasó en la cocina."
    if sam._var("route"):
        bet "Y de que descubriera que estás con Samantha."
    mc "Sí, pero sigo sin ver que tiene que ver eso. Hasta que llegamos a su casa todo iba bien. Cuando nos fuimos también."
    mc "Pero desde que volvimos a casa está distante conmigo. No entiendo ese cambio en los diez minutos que hay de su casa a aquí."
    call BlinkXP ("c17s003_600" , "d") from _call_BlinkXP_2321
    bet "¿Te apetece jugar a un juego?"
    mc "Preferiría que me dijeras que crees que le pasa."
    call BlinkXP ("c17s003_605" , "d") from _call_BlinkXP_2322
    bet "No te lo voy a decir. Podría haber sacado conclusiones equivocadas. Este juego lo inventó Olivia para [emm], pero también puede servir para ti."
    mc "Adelante. Juguemos. Explícame las normas."
    bet "Las normas son fáciles. Yo hago preguntas y tú respondes tras pensar cinco segundos."
    mc "*Risa* Ahora entiendo por qué Meemaw lo inventó para [emm]. Adelante."
    call BlinkXP ("c17s003_610" , "d") from _call_BlinkXP_2323
    bet "Fuiste al rescate de Kiara y Eileen el día que abandonaron su casa, ¿verdad?"
    mc "Sí. Para eso no necesito pensar cinco segundos."
    bet "Cierto. La defendiste cuando apareció Solomon. ¿Cómo crees que se debe sentir después de que la rescataras y la defendieras?"
    mc "Para esta tampoco tengo que pensar. Me lo ha dicho ella. Protegida y segura."
    if sam._var("route") or mar._var("route") or nor._var("route"):
        call BlinkXP ("c17s003_615" , "d") from _call_BlinkXP_2324
        bet "¿Qué crees que debe pensar de tus relaciones?"
        if eil._var("route"):
            bet "¿Y de que, además, estés con su hija?"
        mc "No me lo he planteado. No tiene por qué pensar nada."
        call BlinkXP ("c17s003_620" , "d") from _call_BlinkXP_2325
        bet "Yo en su lugar pensaría que no te importa la edad que tengan las mujeres con las que sales."
        mc "Y acertarías. La edad es sólo un número y no le presto atención en absoluto."
        call BlinkXP ("c17s003_625" , "d") from _call_BlinkXP_2326
        bet "No hagas público eso o todas las abuelas de California empezarán a perseguirte. *Risa*"
        mc "¿Todas? ¿Tú también? *Risa*"
        bet "*Risa* Yo no soy abuela. Solo vieja."
        call BlinkXP ("c17s003_630" , "d") from _call_BlinkXP_2327
        bet "Pero volvamos a Kiara antes de que digas algo inapropiado."
        bet "Un muchacho la rescata dos veces de su marido y la hace sentir protegida y segura. Un muchacho a quien le da lo mismo la edad de su pareja."
    else:
        call BlinkXP ("c17s003_630" , "d") from _call_BlinkXP_2328
        bet "Entonces tenemos a un muchacho que la ha rescatado dos veces de su marido y que la hace sentir protegida y segura."
    if eil._var("route"):
        bet "Y que, para ella, es lo suficientemente bueno como para estar con su hija. Eso es importante y lo tienes que ver con mentalidad de madre."
    $ Aux = 0
    if mar._var("route"):
        $ Aux = Aux+1
    if sam._var("route"):
        $ Aux = Aux+1
    if nor._var("route"):
        $ Aux = Aux+1
    if sim._var("route"):
        $ Aux = Aux+1
    if eil._var("route"):
        $ Aux = Aux+1
    call BlinkXP ("c17s003_630" , "d") from _call_BlinkXP_2329
    if Aux > 1:
        bet "Ese muchacho sale con varias mujeres a la vez por lo que ella sabe."
    elif Aux == 0:
        bet "Ese muchacho está libre como un pájaro."
    elif Aux == 1 and eil._var("route"):
        bet "Pero la novia de ese muchacho es su hija."
    call BlinkXP ("c17s003_635" , "d") from _call_BlinkXP_2330
    bet "Suma a todo eso que te encanta dar abrazos y a ella le encanta que se los des."
    bet "Añade los saludos con besos y... ¡Boom!"
    mc "¿A qué te refieres con \"Boom\"?"
    call BlinkXP ("c17s003_640" , "d") from _call_BlinkXP_2331
    bet "Me estás tomando el pelo, ¿no? No puede ser que no lo estés pillando."
    mc "No, en serio."
    call BlinkXP ("c17s003_645" , "d") from _call_BlinkXP_2332
    bet "Vamos a ver si cambiando la perspectiva lo pillas."
    bet "Imagínate que conoces a una mujer más mayor que tú, fuerte, guapa, sexy y adorable. Pongamos que tiene el físico de Kiara. Además, te hace sentir apreciado."
    mc "OK."
    call BlinkXP ("c17s003_650" , "d") from _call_BlinkXP_2333
    bet "Ahora imagínate que [emm] es un chico y que sale con ella. Tú consideras que esa mujer es buena para [emm]-chico. Que hace que sea mejor persona saliendo con ella."
    bet "Si es lo suficientemente para tu hermano pequeño, también lo sería para ti."
    mc "OK. Espero que a [emm]-chico no le guste demasiado el rosa. Además nunca intentaría nada con nadie que saliera con [emm]-chico."
    call BlinkXP ("c17s003_655" , "d") from _call_BlinkXP_2334
    bet "¡Hush! Esa mujer es muy cariñosa con todo el mundo, tú incluido. Te besa y te abraza a la mínima oportunidad."
    bet "Te defiende cuando te atacan. Incluso llegando a pelearse con otras mujeres por defenderte."
    bet "¿Puedes asegurarme de que no te sentirías atraído por ella?"
    mc "En mi fuero interno seguro que sí, pero si está saliendo con [emm]-chico me mantendría alejado... Código de hombres."
    call BlinkXP ("c17s003_660" , "d") from _call_BlinkXP_2335
    if eil._var("route"):
        bet "Pues creo que lo mismo le está pasando a Kiara. Sales con su hija. Y eres lo suficientemente bueno para ella."
    else:
        bet "Pues creo que lo mismo le está pasando a Kiara. Saliste con su hija. Y eras lo suficientemente bueno para ella."
    bet "Y eres el tipo fuerte, guapo, sexy y adorable que la rescata, la defiende, la abraza y la besa. A quien no le importa la edad de una mujer."
    mc "¿Qué? Creo que te equivocas, Betty. Kiara nunca me vería así. Fue ella la que me besó en la cocina. Si se sintiera así no lo habría hecho."
    call BlinkXP ("c17s003_665" , "d") from _call_BlinkXP_2336
    bet "Mmmm... tienes razón... a menos que cambiase de opinión cuando te peleaste con su marido. Que se diera cuenta entonces."
    mc "Mmmm... Bueno... ha sido desde entonces que está distante..."
    call BlinkXP ("c17s003_670" , "d") from _call_BlinkXP_2337
    bet "¡Sí! ¡Lo sabía! ¡Soy buenísima en esto!"
    mc "Tengo que hablar con ella."
    call BlinkXP ("c17s003_675" , "d") from _call_BlinkXP_2338
    bet "Mejor no lo hagas. Dale tiempo para que se aclare las ideas. Para que ella llegue a sus propias conclusiones."
    bet "De todas formas, ¿qué le ibas a decir? ¿Que hemos estado analizando su comportamiento y que pensamos que puede ser que se sienta atraída por ti?"
    mc "Tienes razón... mejor dejar pasar unos días."
    mc "Pero cambiando de tema... El tipo ese fuerte, guapo, sexy y adorable... Teniendo en cuenta que Kiara nunca ha dicho nada de eso... ¿Es cómo me ves tú?"
    call BlinkXP ("c17s003_680" , "h") from _call_BlinkXP_2339
    bet "¿Qué? ¿Yo? ¡Tengo edad para ser tu abuela!"
    mc "Ya sabes que para mí la edad solo es un número. *Risa* Pero tu rubor ha contestado mi pregunta."
    mc "Me gusta esto de usar tus dotes deductivas contigo. *Risa*"
    call BlinkXP ("c17s003_685" , "d") from _call_BlinkXP_2340
    bet "Creo... creo... que hace mucho rato que nadie se mete con Olivia... voy a dejarte que hables con el resto de las chicas..."
    mc "*Risa* Hasta luego, Tía Be... Hasta luego, Betty. *Risa*"
    stop music fadeout (1.5)
    scene c17s003_690a with fade
    "Unos minutos después..."
    play music ("music/Vacation-Vibe.ogg")
    eri "¿Nos podéis prestar un momento de atención?"
    dap "Hemos pensado en una petición especial para la comida de mañana..."
    emm "Ya que queremos que nuestro cumpleaños sea tan memorable como la fiesta de Navidad..."
    eri "Y hubo personas que no estuvieron en la playa, como Amanda, Eva, Megan, y Jamaal..."
    dap "Y Maddie, la chica de la tienda de ropa, para quienes no la conozcáis."
    emm "Hemos pensado que estaría genial hacer la fiesta en la piscina. Todos en bikini."
    call BlinkXP ("c17s003_695" , "d") from _call_BlinkXP_2341
    eri "Sobre eso, tengo una petición especial que hacerte, Tía [mar]."
    call BlinkXP ("c17s003_700a" , "d") from _call_BlinkXP_2342
    mom "Lo que queráis, cielo."
    scene c17s003_705d with dissolve
    "[eri] lanza una mirada sonriente a [nor] antes de continuar hablando."
    call BlinkXP ("c17s003_705" , "d") from _call_BlinkXP_2343
    eri "Me gustaría que anularas mi regalo de cumpleaños... y lo cambiaras por..."
    eri "Querría que autorizaras a quien quiera a hacer top-less en la piscina. Empezando mañana."
    mcp "([eri], eres maravillosa. Para tu cumpleaños estás pidiendo algo para [nor]. No creo que nadie más vaya a hacer top-less.)"
    call BlinkXP ("c17s003_700b" , "d") from _call_BlinkXP_2344
    mom "Nunca ha estado prohibido, cariño. Nadie ha querido hacerlo nunca, pero nunca lo he prohibido."
    if nor._var("route"):
        mcp "(Aunque el otro día pareció molestarte que [nor] hubiera \"perdido\" el top de su bikini. *Risa mental*)"
    mom "Y antes de que nadie se queje, tampoco nadie ha estado ni estará obligado a hacerlo."
    mcp "(Esa frase va dirigida a Meemaw, estoy seguro. *Risa mental*)"
    call BlinkXP ("c17s003_710" , "d") from _call_BlinkXP_2345
    emm "¡Mamá! ¡No sabía que podíamos!"
    mc "No sabíamos que estuvieras interesada..."
    call BlinkXP ("c17s003_715" , "d") from _call_BlinkXP_2346
    emm "¡Odio las líneas blancas que deja el bikini! ¡Apenas tomo más el sol por eso!"
    todas "*Risa*"
    call BlinkXP ("c17s003_720" , "d") from _call_BlinkXP_2347
    nor "Pues yo añado el jacuzzi a la zona libre de sujetadores para quien quiera. ¡Y añado las braguitas! El jacuzzi pasa a ser zona nudista para quien quiera usarlo."
    nor "Tampoco estaba prohibido, pero ya que parece haber interés, mejor aclararlo."
    call BlinkXP ("c17s003_725" , "f") from _call_BlinkXP_2348
    stop music fadeout (1.5)
    "Unos minutos después, cuando se calma todo el revuelo después de la petición de las chicas..."
    play music ("music/Acoustic-Inspirational.ogg")
    ama "Eva va a adorar la fiesta en bikini. Ayer se estaba quejando de tener que ponerse un vestido dos días seguidos."
    mc "¿Cómo fue la conversación con ella? ¿Estaba muy enfadada?"
    call BlinkXP ("c17s003_730" , "d") from _call_BlinkXP_2349
    ama "Un poco. Me acusó de flirtear contigo. De abrazarte y besarte demasiado. *Risa*"
    mc "Iba a decir típico de [emm]. Pero [emm] se hubiera enfadado conmigo, no contigo."
    mcp "(Como pasó la noche del Twins.)"
    mc "Pero ahora tengo una pregunta... ¿estabas flirteando conmigo? *Risa*"
    mcp "(Después de la conversación con Betty, me parece que debería preguntárselo a cada chica con la que hable. *Risa mental*)"
    call BlinkXP ("c17s003_735" , "d") from _call_BlinkXP_2350
    ama "Ya lo aclaré con ella. Por lo que sí que se va a enfadar es por lo que me acaba de decir [nor]."
    mcp "(Elegante forma de esquivar la pregunta.)"
    mc "¿Qué te ha dicho?"
    call BlinkXP ("c17s003_740" , "d") from _call_BlinkXP_2351
    ama "Que me quede para la cena. Al no haber peligro ya, no es necesario que nadie se quede en la base vigilando las cámaras. Podemos venir las dos a comer y a cenar todos los días."
    ama "De todas formas llevaremos dispositivos que nos avisarán de cualquier intrusión en el perímetro."
    mc "Pero eso es fantástico. ¿Por qué se va a enfadar Eva?"
    call BlinkXP ("c17s003_745" , "d") from _call_BlinkXP_2352
    ama "*Risa* ¿No te lo imaginas? En la cena de hoy, yo habré estado tres veces y ella solo dos."
    ama "Y habré pasado toda la tarde con la familia, mientras ella se pasó la tarde de ayer quitando cámaras."
    mc "Eso sí que es muy típico de [emm]. *Risa*"
    ama "Y de Eva. *Risa*"
    mc "Cualquiera estaría contento de poder venir dos veces al día. Ellas se enfadan. *Risa*"
    call BlinkXP ("c17s003_750" , "d") from _call_BlinkXP_2353
    dap "[mc], lo siento, pero voy a secuestrar a Amanda. Queremos planificar una cosa para esta noche y la necesitamos."
    mc "Supongo que no me vais a decir qué."
    dap "Supones bien. Tú ponte guapo para la cena de esta noche."
    dap "Mientras tanto, podrías avisar a Samantha, Simone, Jamaal, Alexia, y Maddie de que tienen que traer bikini mañana. Esta vez no tiene que ser navideño."
    mc "OK. Voy a mi habitación a hacer las llamadas."
    call BlinkXP ("c17s003_755" , "d") from _call_BlinkXP_2354
    ama "Te veo luego."
    mc "A partir de ahora vamos a tener muchas oportunidades de vernos."
    mc "Cuando no te secuestren."
    scene c17s003_760 with dissolve
    dap "*Brl*"
    stop music fadeout (1.5)
    scene black with dissolve
    "Vas a tu habitación a hacer las llamadas. Esta familia cada vez es más rara. Navidad en bikini, cumpleaños en top-less..."
    "¿Qué va a ser lo próximo? ¿Acción de Gracias nudista?"
    return
label c17s003_EriPregnancyResult:
    "Poco después de acabar las llamadas [eri] entra en tu habitación."
    call KissXP ("c17s003_775" , "d") from _call_KissXP_72
    play music ("music/Happy-Sun.ogg")
    eri "Hola, mi amor."
    mc "Hola, mi vida. ¿Vienes por la prueba? Aún quedan unos minutos y no ha pitado."
    call BlinkXP ("c17s003_780" , "d") from _call_BlinkXP_2355
    eri "Vengo a hacerte una pregunta sobre la prueba."
    mc "Dime."
    eri "¿Te importaría mucho si no la miramos hoy?"
    mc "¿Qué? ¿Por qué? Creía que querías saberlo cuanto antes mejor."
    call BlinkXP ("c17s003_785" , "d") from _call_BlinkXP_2356
    eri "Quería."
    eri "Si quieres que lo miremos ahora, podemos mirarlo, pero preferiría dejar pasar unos días."
    mc "El resultado no va a cambiar, con lo que, si crees que es lo mejor, no tengo ningún problema con ello."
    call BlinkXP ("c17s003_790" , "d") from _call_BlinkXP_2357
    eri "Es muy egoísta por mi parte, pero estoy disfrutando mucho con Amanda, y después estará también Eva..."
    eri "Si sale negativo... no quiero decir que me vaya a deprimir o algo por el estilo..."
    mc "Pero vas a estar pensando en ello en vez de estar conociéndolas."
    call BlinkXP ("c17s003_795" , "d") from _call_BlinkXP_2358
    eri "Exacto. Y mañana, con el cumpleaños, me pasará lo mismo."
    mc "Te entiendo. Pero ¿y si saliera positivo?"
    call BlinkXP ("c17s003_800" , "d") from _call_BlinkXP_2359
    eri "Si saliera positivo estaría pensando en nuestro bebé en vez de estar centrada en lo que pasa a nuestro alrededor."
    eri "Seguramente se me acabaría escapando y eso les robaría protagonismo a Amanda y a Eva. También a [dap] y a [emm]."
    mc "Yo te iba a proponer no decírselo a nadie también. Al menos hasta que pasaran los cumpleaños."
    call KissXP ("c17s003_775" , "d") from _call_KissXP_73
    eri "Y es por estas cosas por las que me enamoré de ti. Siempre pensando en los demás antes que en ti mismo."
    mc "*Risa* Le dijo la sartén al cazo."
    call BlinkXP ("c17s003_805" , "d") from _call_BlinkXP_2360
    eri "¿Yo? Fíjate en lo egoísta que estoy siendo con la prueba de embarazo."
    mc "Y lo generosa que has sido con tu petición de la piscina top-less..."
    call BlinkXP ("c17s003_810" , "d") from _call_BlinkXP_2361
    eri "¿Generosa? ¿Por qué lo dices?"
    mc "Está claro que lo has dicho para que [nor] pueda hacer top-less. Estabas dispuesta a renunciar a tu regalo porque mi madre lo aprobase."
    call BlinkXP ("c17s003_815" , "d") from _call_BlinkXP_2362
    eri "Bueno, sí, mi madre es la que más va a usar el nuevo permiso. Y Kate quien más lo va a disfrutar. *Risa*"
    mc "*Risa* Le has hecho un favor sin saberlo. La cara que ponía mientras mi madre decía que estaba permitido..."
    eri "Pobre chica, no sabía a qué tetas mirar después de eso. *Risa*"
    call BlinkXP ("c17s003_820" , "d") from _call_BlinkXP_2363
    eri "Cambiando de tema, ¿te han dicho que te pongas elegante para esta noche?"
    mc "Sí, me lo ha dicho [dap]. ¿Qué estáis planeando?"
    call BlinkXP ("c17s003_825" , "d") from _call_BlinkXP_2364
    eri "Hace mucho que no salimos a bailar. Y esta vez podré ir con mi novio en vez de... bueno, ya sabes lo que pasó."
    mc "¿Vamos a volver al Twins?"
    call KissXP ("c17s003_775" , "d") from _call_KissXP_74
    eri "Dónde vamos a ir es una sorpresa. Y ahora me tengo que ir a seguir planificándola con las chicas."
    eri "Hasta luego, mi amor. Te quiero."
    mc "Hasta luego, mi vida. Yo también te quiero."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c17s004_MeganLewd:
    if _in_replay:
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
            "No":
                $ mar._var("route" , False)
        menu:
            "¿Estás en una relación con [eri]?"
            "Sí":
                $ eri._var("route" , True)
            "No":
                $ eri._var("route" , False)
        menu:
            "¿Megan está embarazada?"
            "Sí":
                $ meg._var("pregnant" , True)
            "No":
                $ meg._var("pregnant" , False)
    if eri._var("route"):
        "Con todo el mundo en casa de [nor] tienes seis lavabos para elegir. Las dudas te asaltan."
    else:
        "Después de acabar las llamadas vas al lavabo. Con todo el mundo en casa de [nor] tienes seis para elegir. Las dudas te asaltan."
    call BlinkXP ("c17s004_005" , "d") from _call_BlinkXP_2365
    "Cuando vuelves a tu habitación, encuentras a Megan esperándote. "
    play music ("music/NightJazzBeats.ogg")
    mc "Hola preciosa, ¿vienes por el test? Aún queda un rato. "
    meg "Lo sé. Venía a hablar contigo antes del test. Espero que no te moleste que haya entrado."
    mc "No, para nada. "
    call KissXP ("c17s004_010" , "d") from _call_KissXP_75
    meg "Pero antes quiero besar a mi novio. Al padre de mis hijos. "
    mc "*Risa* Aún no sabemos si vamos a tenerlos, Megan. "
    call BlinkXP ("c17s004_015a" , "d") from _call_BlinkXP_2366
    meg "Pero pensar en ello me ha hecho ilusión. Si no sale positivo ahora, me gustaría seguir intentándolo. "
    mc "*Risa* ¿Crees que voy a decir no a eso? "
    call BlinkXP ("c17s004_015b" , "d") from _call_BlinkXP_2367
    meg "Pero no me gusta ir con secretos con tu familia."
    meg "Me parece raro que vayamos a hacer el amor en tu habitación con tu exnovia en la habitación de abajo y tu madre una planta por debajo de ella."
    if mar._var("route"):
        mc "Te he visto hablando con mi madre durante la comida. Me ha dado la impresión de que no ha ido mal, ¿verdad? "
        call BlinkXP ("c17s004_020" , "d") from _call_BlinkXP_2368
        meg "¿Mal? ¡Ha ido super bien! ¡[mar] es fantástica y sorprendente! "
        call BlinkXP ("c17s004_025" , "d") from _call_BlinkXP_2369
        meg "No sabía cómo empezar la conversación con ella, y al final ha sido ella quien la ha empezado conmigo. "
        meg "Me ha pedido que guardara el secreto de que estabais juntos, porque es el fin de semana de las chicas y todo eso. "
        mc "Sí, nadie quiere robarles protagonismo en su fin de semana. Eva y Amanda ya son suficiente robo de protagonismo. "
        call BlinkXP ("c17s004_030" , "d") from _call_BlinkXP_2370
        meg "Pero lo ha planteado de tal forma, que ha sido muy fácil pedirle que ella guardara el secreto de que tú y yo también estamos juntos. *Risita* "
        meg "Te puedes imaginar su cara de sorpresa. Como es normal, no tenía ni idea. "
        mc "Me hubiera gustado estar cuando se lo has dicho, pero... "
        call BlinkXP ("c17s004_035" , "d") from _call_BlinkXP_2371
        meg "Te dije que quería decírselo yo a solas. Compartirte es algo tan diferente de lo que considero normal, que tenía que ser una conversación entre nosotras. "
        mc "Lo sé. Si yo hubiera estado ahí el tono de la conversación seguramente habría sido diferente. "
        call BlinkXP ("c17s004_040" , "d") from _call_BlinkXP_2372
        meg "Seguro que sí. Tal como ha ido, éramos dos mujeres que comparten el mismo hombre. "
        meg "Estábamos poniendo las cartas sobre la mesa y pidiéndonos que guardáramos nuestros secretos mutuos. "
        mc "Tú estabas en una posición de poder al conocer el suyo y le has demostrado buena voluntad al decirle el tuyo. De esa forma os poníais al mismo nivel. "
        call BlinkXP ("c17s004_045" , "d") from _call_BlinkXP_2373
        meg "Exactamente. Al decirle que tú y yo estábamos juntos, su actitud ha cambiado totalmente. "
        meg "Ya no me estaba pidiendo un favor. Estábamos compartiendo algo. Éramos cómplices. "
        mc "Las mujeres sois muy extrañas. "
        call BlinkXP ("c17s004_050" , "d") from _call_BlinkXP_2374
        meg "Sí, lo somos. Si hubieras estado delante la conversación hubiera sido diferente. "
        meg "Ya no hubiéramos sido cómplices que acaban como amigas. Hubiéramos sido perras celosas luchando por nuestro hombre. "
        mc "*Risa* Lo que decía, las mujeres de esta familia sois raras. "
    else:
        mc "No te preocupes por eso, los techos son altos y no se escucha nada entre plantas. "
        call BlinkXP ("c17s004_025" , "d") from _call_BlinkXP_2375
        meg "No me refiero a eso. Me sentiría más cómoda si se lo pudiera decir a tu madre al menos. No sé... imagina que el test sale positivo. "
        mc "Se lo podemos decir cuando quieras... "
        call BlinkXP ("c17s004_055" , "d") from _call_BlinkXP_2376
        meg "No, este fin de semana mejor no. He podido notar lo importante que este fin de semana para las chicas y no quiero que ninguna noticia lo pueda fastidiar. "
        mc "*Risa* Las mujeres de esta familia sois raras. "
    call BlinkXP ("c17s004_060" , "d") from _call_BlinkXP_2377
    meg "¿Qué? ¿Me has incluido en la familia en esa frase? "
    mc "Sí, obviamente. Perdona si voy un poco rápido con esto, pero esta familia está experimentando unos cambios muy rápidos. Lo de aceptar a alguien en la familia se está convirtiendo en costumbre. "
    mc "Además es posible que lleves a nuestro hijo dentro ahora mismo. ¿Cómo no voy a incluirte en la familia? "
    call BlinkXP ("c17s004_065" , "d") from _call_BlinkXP_2378
    if mar._var("route"):
        meg "No lo había visto así... Todo va muy rápido contigo. Es la cuarta vez que nos vemos desde que volviste de la universidad... "
    else:
        meg "No lo había visto así... Todo va muy rápido contigo. Es la segunda vez que nos vemos desde que volviste de la universidad... "
    meg "Y es posible que ya esté embarazada de nuestro hijo... "
    if mar._var("route"):
        mc "¿Cuarta? No me cuadran los números. "
        call BlinkXP ("c17s004_070" , "d") from _call_BlinkXP_2379
        meg "Las dos veces que viniste al Jazz Corner con [mar], cuando nos vimos en Westport, y este fin de semana. "
    else:
        mc "¿Segunda? No me cuadran los números. "
        call BlinkXP ("c17s004_070" , "d") from _call_BlinkXP_2380
        meg "Cuando nos vimos en Westport, y este fin de semana. "
    meg "Cuento este fin de semana como una sola vez. "
    call BlinkXP ("c17s004_075" , "d") from _call_BlinkXP_2381
    meg "Y ahora resulta que tengo una familia nueva de la que no sabía nada. "
    meg "Que hay un test de embarazo a punto de pitar ahí dentro que es posible que me diga que voy a ser madre antes de cumplir los 24. "
    if mar._var("route"):
        meg "Y le acabo de decir a la que podría acabar siendo mi suegra que me estoy acostando con su hijo. "
        if not persistent.family:
            meg "Su hijo que además tampoco es su hijo... "
        meg "Un hijo con el que ella también se acuesta... "
    call BlinkXP ("c17s004_080" , "d") from _call_BlinkXP_2382
    meg "Espero que te des cuenta de que esto es una puta locura... "
    meg "Hace dos semanas no creía que te volviera a ver nunca... "
    mc "Si, un poco locura sí que es, pero bendita locura. "
    call BlinkXP ("c17s004_085" , "d") from _call_BlinkXP_2383
    meg "Bendita, pero no te extrañes de que esté abrumada. Me gustan las cosas ordenadas. Predecibles. Contigo mi vida es cualquier cosa menos predecible y ordenada. "
    mc "Pero doy unos abrazos de puta madre. Y creo que necesitas uno ahora mismo. "
    call BlinkXP ("c17s004_090" , "d") from _call_BlinkXP_2384
    meg "Sí y sí. Tus abrazos son cojonudos y necesitaba uno. Cuanto más pienso en nuestra relación más me explota la cabeza. "
    mc "Pues no pienses, no la analices, déjate llevar. Actúa por instinto. "
    call BlinkXP ("c17s004_095a" , "d") from _call_BlinkXP_2385
    meg "Si actuase por instinto te estaría desnudando ahora mismo. "
    mc "¿Ahora? ¿Antes de saber lo que dice el test de embarazo? "
    call BlinkXP ("c17s004_095b" , "d") from _call_BlinkXP_2386
    meg "Sí. Así, si saliera negativo, el lunes podría hacer otro. Y el martes sabríamos el resultado antes de que tuviera que volver a Westport. "
    meg "Y vuelta a empezar por si sale negativo... "
    mc "Sabes que no necesitas ninguna excusa para que nos acostemos juntos, ¿verdad? "
    call BlinkXP ("c17s004_095c" , "d") from _call_BlinkXP_2387
    meg "Lo sé. Pero ya te he dicho que si no salía positivo querría seguir intentándolo. "
    meg "Te lo he dicho porque no estaba segura de lo nuestro... de si querrías seguir conmigo si no salía positivo. "
    mc "¿Qué? ¿Por qué? "
    call BlinkXP ("c17s004_095d" , "d") from _call_BlinkXP_2388
    meg "¿Tú has visto las mujeres que viven contigo? "
    meg "Todas son bellezas... desde Saira a Lisa, pasando por [eri] o Amanda... o [mar] o [nor]. ¡Joder! Hasta Olivia y Betty tienen su atractivo... "
    if mar._var("route"):
        meg "Y además no tienes reparos en liarte con tu familia... "
    call BlinkXP ("c17s004_095e" , "d") from _call_BlinkXP_2389
    meg "Y después estoy yo... ¡Si hicieran un concurso de belleza en esta casa no me aceptarían ni como jurado! "
    mc "Eso no es cierto, Meg... "
    call BlinkXP ("c17s004_095f" , "d") from _call_BlinkXP_2390
    meg "¡Hush! Déjame hablar. "
    meg "No sabía si lo de Westport fue un calentón que te entró o si realmente querías estar conmigo. "
    meg "No sabía qué pasaría si salía negativo. No sabía que pasaría si salía positivo. No sabía nada... "
    call BlinkXP ("c17s004_125" , "d") from _call_BlinkXP_2391
    meg "Y ahora resulta que me dices que soy parte de la familia. La familia más rara que he visto nunca. "
    meg "{b}¡Antes de saber si estoy embarazada!{/b} Me dices que quieres seguir conmigo salga lo que salga... "
    mc "¿Puedo hablar ya? "
    call BlinkXP ("c17s004_130" , "d") from _call_BlinkXP_2392
    meg "Si... me acabo de comportar como una loca... "
    mc "Un poco. *Risa* Pero vayamos por puntos. "
    mc "¿De dónde has sacado que no ganarías ese concurso de belleza? "
    meg "De que tengo espejos... casi todas tienen cuerpos esculturales... "
    mc "¿Pero alguna tiene tus ojos? "
    call BlinkXP ("c17s004_135" , "d") from _call_BlinkXP_2393
    meg "Supongo que no... aunque con todo esto de la clonación... Tampoco tienen mi barriga o mi enorme culo... "
    mc "Megan, ya te dije que tu culo me encantaba. "
    call BlinkXP ("c17s004_140" , "d") from _call_BlinkXP_2394
    meg "Pero... "
    mc "¡Hush! Déjame hablar a mí ahora. "
    mc "Si estoy contigo es porque me gustas. No me acosté contigo por un calentón. Me acosté contigo porque me pareces preciosa. "
    call BlinkXP ("c17s004_145" , "d") from _call_BlinkXP_2395
    mc "Y quiero seguir acostándome contigo indiferentemente de si el test sale positivo o negativo. "
    mc "Lo de ser familia o no... sé que somos raros. ¿Alguna vez has presentado un novio a tus padres? "
    call BlinkXP ("c17s004_150" , "d") from _call_BlinkXP_2396
    meg "No, pero... {w}bueno... sí... sigue... "
    mcp "(¿Qué? Ahí ha habido algo que no he entendido. Más preguntas sin responder.) "
    mc "¿Cuánto tiempo tiene que pasar antes de que ese novio sea parte de la familia? ¿Hay que llegar a la boda? "
    call BlinkXP ("c17s004_155" , "d") from _call_BlinkXP_2397
    meg "No sé... nunca he estado tanto tiempo con alguien como para considerarlo familia, o que... {w}mi familia... lo considerase parte de ella. "
    mcp "(Otra vez esa pausa.) "
    mc "Pues si estamos juntos, si eres mi novia... si quieres ser mi novia... no hace falta que seas mi prometida o mi esposa para que te considere familia. "
    mc "Si estamos juntos es porque quiero que esto tenga futuro. Me dan lo mismo las etiquetas. Si eres mi novia, mi prometida, o mi esposa. "
    stop music fadeout (1.5)
    scene c17s004_160a with dissolve
    mc "Y volviendo a tu culo... me encanta como llena mis manos. "
    play music ("music/KindofGirl.ogg")
    meg "¡[mc]! "
    mc "¿Qué? "
    mc "Has dicho que si siguieras tu instinto, me estarías desnudando... "
    scene c17s004_160b with dissolve
    mc "Y yo voy a seguir mi instinto. "
    meg "*Risa* Y veo que te dice lo mismo que el mío. "
    scene c17s004_160c with dissolve
    "Aprietas a Megan contra la erección que se ha estado formando dentro de tu pantalón. "
    mc "Y tengo un amigo ahí abajo que también opina lo mismo. Demasiados votos a favor. "
    meg "¿Tienes una erección? ¿Ya? "
    mc "¿Cómo quieres que no la tenga? ¡Tengo el mejor culo del mundo entre mis manos! "
    call BlinkXP ("c17s004_165" , "d") from _call_BlinkXP_2398
    meg "¿Tanto te gusta mi culo? *Risita* "
    mc "Te lo dije en tu piso y te lo vuelvo a repetir. Es un culo precioso. "
    meg "Pues si consigues que uno de esos tests salga positivo te dejaré jugar con él si quieres. *Risita* "
    mc "¿Hay alguna razón para no dejarme jugar con él antes? "
    call BlinkXP ("c17s004_170" , "d") from _call_BlinkXP_2399
    meg "Nunca te voy a dejar hacer un culo-a-vagina, y quiero que te corras siempre dentro de mí hasta que eso salga verde. "
    meg "Con lo que hasta que no tengas los deberes hechos no va a haber culo para ti. *Risita* "
    mc "Si es solo por correrme... no hay problema. *Risa* "
    mc "Tampoco cubanas entonces, ¿no? "
    call BlinkXP ("c17s004_175" , "d") from _call_BlinkXP_2400 #sin camiseta
    meg "No tengo las suficientes tetas para envolver a ese monstruo. *Risa* "
    mc "Pero no por ello son menos deliciosas. "
    scene c17s004_185pv with dissolve
    $renpy.sound.play("music/MeganMoan.ogg", loop=True)
    meg "*Gemido* Con cuidado... llevo cachonda desde que hemos empezado a hablar de nosotros... "
    mc "*Slurp* "
    show c17s004_185v with dissolve #0-59
    "Puedes notar cómo el pezón de Megan, duro desde el primer momento, va reaccionando a cada una de las caricias de tu lengua. "
    meg "*Jadeo* Te he dicho que está sensible... "
    mcp "(No lo has dicho. Sólo has dicho que fuera con cuidado. Y eso estoy haciendo.) "
    "El pezón, cada vez más duro, vuelve a su posición como estirado por un muelle cada vez que tu lengua pierde contacto con él. "
    meg "*Gemido* Es injusto... tú aún estás vestido... "
    scene c17s004_190pv with dissolve
    hide c17s004_185v
    show c17s004_190v with dissolve #0-59
    mc "*Slurp* "
    "Aprovechando su desnudez, tu mano ha recorrido su cuerpo hasta su vagina, empezando a acariciarla suavemente. "
    "Notando lo húmeda que está. "
    meg "*Gemido* Veo que la justicia y tú... no os lleváis muy bien... "
    mcp "(Es difícil ser justos cuando el bocado es tan delicioso... pero tiene razón.) "
    call BlinkXP ("c17s004_195" , "d") from _call_BlinkXP_2401
    hide c17s004_190v
    mc "¿Eso es lo que crees? *Risa* "
    "Dices sin dejar de masturbarla, tan solo retirando tu boca de su pezón lo suficiente para hablarle y mirarla a los ojos. "
    meg "*Gemido* No me hagas pensar demasiado mientras... *Jadeo* me estás haciendo eso... "
    meg "*Jadeo* Pero a mí... *Gemido* También me gustaría tenerte desnudo... "
    mc "Me parece justo... "
    call BlinkXP ("c17s004_180" , "f") from _call_BlinkXP_2402
    meg "Impresionante. Verte así... por mí... sube la autoestima de cualquiera. *Risa* "
    mc "Ya estuve una vez así por ti, y lo volveré a estar siempre. "
    meg "Entonces creo que este es el único concurso de belleza que necesito ganar. *Risa* "
    mc "Ganarías muchos otros si te presentaras, Meg. Eres preciosa. "
    call BlinkXP ("c17s004_200" , "d") from _call_BlinkXP_2403
    meg "Ven aquí. Te quiero notar muy dentro de mí. "
    mc "Me parece que es la mejor orden que me van a dar hoy. *Risa* Una oferta que no puedo rechazar. "
    scene c17s004_105pv with dissolve
    "Penetras a Megan mientras la besas. "
    "Su húmeda raja te recibe a Mjolnir con facilidad. La postura, con sus piernas totalmente abiertas, ayuda. "
    meg "¡Ooof! *Gemido* Sigue siendo gigantesco..."
    mc "No va a encoger en una semana. *Risa*"
    meg "Espero que no lo haga nunca. Me siento llena ahora mismo."
    meg "Es una sensación increíble."
    mc "¿Quieres que espere antes de moverme?"
    meg "Puedes empezar cuando quieras, cielo."
    show c17s004_105v with dissolve
    meg "*Gemido*"
    "Megan empieza a gemir en tu boca en cuanto empiezas a moverte, gemidos entremezclados con el juego de vuestras lenguas."
    meg "*Jadeo*"
    "Tan solo hacen falta unos segundos para que recuerdes que Megan apenas habla durante el sexo."
    meg "*Gemido*"
    "Las reverberaciones de sus gemidos en tu boca son mensaje suficiente para indicarte qué le gusta y qué no."
    meg "*Jadeo*"
    "Le gusta todo."
    scene c17s004_100pv with dissolve
    hide c17s004_105v
    show c17s004_100v with dissolve
    meg "*Gemido*"
    "Tu polla entrando en su húmedo coño se siente como un guante hecho a medida."
    meg "*Jadeo*"
    "Nunca te has puesto un guante empapado, pero dudas de que la sensación sea tan placentera."
    meg "*Gemido*"
    "Dudas de que pueda haber ninguna sensación tan placentera como esta."
    meg "*Jadeo*"
    "Tampoco para Megan."
    scene c17s004_205pv with dissolve
    hide c17s004_100v
    show c17s004_205v with dissolve
    meg "*Gemido*"
    "Ver sus hermosos ojos verdes mientras el movimiento de tus caderas la acercan a su orgasmo es alucinante."
    meg "*Jadeo*"
    "Tan alucinante como la propia Megan."
    meg "*Gemido*"
    "Sus caderas acompañan cada una de tus embestidas, adaptándose al ángulo de tu penetración."
    meg "*Jadeo* ¿Podemos cambiar de postura?"
    "Las primeras palabras de Megan desde que la has penetrado te pillan totalmente por sorpresa."
    mc "¿No te está gustando?"
    meg "Me está encantando... *Gemido* Pero prefiero correrme en otra posición... *Jadeo*"
    mc "Cambiemos entonces, cualquier cosa que me pidas"
    scene c17s004_110pv with fade
    hide c17s004_205v
    show c17s004_110v with dissolve
    "Megan se tumba de costado y la penetras con facilidad otra vez."
    meg "*Gemido* ¡Oh, sí! ¡Mucho mejor ahora! *Jadeo* ¡Y antes ya era fantástico!"
    "Muchas palabras para ser Megan."
    meg "*Gemido*"
    "Eso ya es más normal."
    meg "*Jadeo*"
    "Con una mano libre sin necesitarla como soporte, puedes explorar las tetas de Megan."
    meg "*Gemido*"
    "Maravillosas tetas con durísimos pezones."
    scene c17s004_115pv with fade
    hide c17s004_110v
    show c17s004_115v with dissolve
    meg "*Jadeo*"
    "Tu polla se sigue deslizando, dentro y fuera, como si estuvierais hechos el uno para el otro."
    meg "*Gemido*"
    "Su coño hecho para tu polla, Mjolnir encajando perfectamente dentro de ella."
    meg "*Jadeo*"
    "Puedes notar bajo tus dedos como el cuerpo de Megan empieza a tensarse. Sabes lo que viene ahora."
    meg "*Gemido* Estoy a punto de correrme..."
    mc "Córrete para mí, cielo."
    call OrgasmX ("c17s004_210") from _call_OrgasmX_51
    meg "*GEMIDO* ¡OH, SÍ! *JADEO* {b}¡Sigue!{/b}"
    "No tienes intención de parar. Aún te queda un poco de gasolina en el depósito."
    scene c17s004_120pv with fade
    hide c17s004_115v
    show c17s004_120v with dissolve
    meg "*JADEO*"
    "Las contracciones que produce su orgasmo hace que puedas notar sus paredes vaginales cerrándose sobre tu astil."
    meg "*GEMIDO*"
    "Están intentando llevarte a tu propio clímax. Intentando ordeñar cada gota de la corrida que está por llegar."
    meg "{b}*JADEO*{/b}"
    "Cada vez más apretado, su coño exprime tu polla. Si no fuera por sus fluidos, los movimientos serían más difíciles con cada embestida."
    meg "{b}*GEMIDO*{/b}"
    "Gracias a sus orgasmos, no solo no son más difíciles, sino que son mucho más placenteros."
    meg "{b}*JADEO*{/b}"
    "Tu orgasmo llega como una explosión."
    if meg._var("pregnant"):
        $ meg._var("pregnancyDiscovered", True)
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Megan embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not meg._var("pregnant"):
            play sound ("music/OldMusicBox5.ogg")
            $ meg._var("pregnant", True)
    call OrgasmX ("c17s004_215") from _call_OrgasmX_52
    mc "¡Mpfft!"
    "Llenas el útero de Megan con una abundante corrida."
    meg "{b}*GEMIDO*{/b} ¡SÍ!"
    "No sabes si la dejarás embarazada o si ya lo está, pero descargas suficiente semen como para embarazarla tres veces."
    stop music fadeout (1.5)
    stop sound fadeout (1.5)
    meg "{b}*JADEO*{/b}"
    play sound ("music/buzz-buzz.ogg")
    _("Test de embarazo") "*Buzz*"
    "El test de embarazo pita en ese momento."
    play music ("music/Gypsy-Jazz.ogg")
    call BlinkXP ("c17s004_220" , "f") from _call_BlinkXP_2404
    meg "*Risa* ¡Justo a tiempo!"
    mc "Sí. Unos segundos antes y..."
    meg "¿Te hubiera desconcentrado? *Risa*"
    mc "No, pero lo hubiera ignorado educadamente. *Risa*"
    call BlinkXP ("c17s004_225" , "d") from _call_BlinkXP_2405
    meg "¿Quieres mirarlo ya o puedo descansar unos minutos?"
    mc "El resultado no va a cambiar por unos minutos, cielo."
    mc "Y si es negativo, no pasa nada. En tres días sabremos si lo de ahora mismo ha dado un resultado diferente."
    call BlinkXP ("c17s004_230" , "d") from _call_BlinkXP_2406
    "Os quedáis abrazados por unos momentos en la cama. Tu polla todavía dentro de ella."
    "Puedes notar como Megan está inquieta, incómoda."
    mc "¿Pasa algo, cielo?"
    meg "Sé que te acabo de pedir unos minutos. Pero tengo ganas de mirar el resultado."
    mc "Vamos a mirarlo. Yo también tengo ganas de saberlo."
    mc "Está en los cajones debajo de la televisión."
    meg "Quédate aquí."
    if meg._var("pregnancyDiscovered"):
        call BlinkXP ("c17s004_235" , "f") from _call_BlinkXP_2407
        meg "¡Positivo! ¡Vamos a ser padres! ¿Estás contento?"
        mc "¡No lo podría estar más ahora mismo!"
        call BlinkXP ("c17s004_240" , "d") from _call_BlinkXP_2408
        meg "¿Cómo lo vamos a hacer?"
        mc "¿A qué te refieres?"
        meg "A todo. ¿Dónde vamos a vivir? ¿Newport o Westport? ¿Qué vamos a hacer con nuestros trabajos?"
        mc "¿Quieres que vivamos juntos?"
        call BlinkXP ("c17s004_245" , "d") from _call_BlinkXP_2409
        meg "No quiero criar a nuestro hijo sola. Ni quiero que lo críes sólo tú. Quiero que tenga un padre y una madre con él en todo momento."
        meg "Sé que puede ser complicado, aún vives con [mar]..."
        if mar._var("route"):
            call BlinkXP ("c17s004_250" , "d") from _call_BlinkXP_2410
            meg "Una mujer con la que también sales... y con la que es posible que también quieras tener hijos... ¡Qué complicado es estar contigo!"
        mc "No había pensado en eso... te puedes mudar aquí, supongo... Mi cama es grande..."
        mc "Realmente no había pensado en ninguna de las complicaciones logísticas de tener un hijo contigo."
        call BlinkXP ("c17s004_255" , "d") from _call_BlinkXP_2411
        mc "Pero las resolveremos juntos."
        meg "Bueno, tenemos mucho tiempo para pensar en cómo lo vamos a hacer. Faltan nueve meses para que llegue."
        mc "Pero es bueno que hayas sacado el tema, es algo en lo que no hubiera pensado hasta que fuera tarde."
        call BlinkXP ("c17s004_260" , "d") from _call_BlinkXP_2412
        meg "Ya te digo que hay tiempo. Para lo que se te estaba agotando el tiempo era para darme ese abrazo. *Risa*"
        mc "Sabes que nunca voy corto de ellos. *Risa* Pero tenía que llegar desde la cama."
        call BlinkXP ("c17s004_265" , "d") from _call_BlinkXP_2413
        meg "Ahora me tengo que informar de muchas cosas."
        meg "Me acabo de dar cuenta de que no sé qué coberturas tiene mi seguro médico con respecto al embarazo. No es algo que me hubiese preocupado nunca."
        mc "No te preocupes por eso ahora. Como has dicho hay mucho tiempo."
        mc "¿Tienes pensado algún nombre?"
        call BlinkXP ("c17s004_270" , "d") from _call_BlinkXP_2414
        meg "Richard."
        mc "Me gusta. ¿Y si es niña?"
        meg "Va a ser niño. Tengo esa corazonada. Pero si es niña te dejaré elegir a ti."
        mc "Me parece un buen trato."
        call BlinkXP ("c17s004_275" , "d") from _call_BlinkXP_2415
        meg "¿Quieres decírselo a [mar]?"
        mc "Me gustaría. Pero pasado el fin de semana."
        meg "Ese también parece un buen trato. Enterarnos que estamos embarazados durante este fin de semana... Parece que pasan demasiadas cosas a la vez."
    else:
        call BlinkXP ("c17s004_280" , "d") from _call_BlinkXP_2416
        meg "Negativo. Tendremos que repetirlo el lunes. *Risa*"
        mc "¿Te hace gracia? Creía que querías que saliera positivo."
        call BlinkXP ("c17s004_285" , "d") from _call_BlinkXP_2417
        meg "Y quiero que salga positivo. Pero acabamos de tener el sexo más alucinante del mundo."
        meg "Puede que el siguiente salga positivo, y si no, el siguiente, o el siguiente... no hay ninguna prisa."
        meg "No me voy a decepcionar por no quedarme embarazada a la primera ocasión."
        mc "Me parece un buen plan. Habrá más oportunidades."
        call BlinkXP ("c17s004_290" , "d") from _call_BlinkXP_2418
        meg "Y si son tan buenas como esta... no tengo ninguna prisa."
        meg "*Risa* ¡Tenemos 23 y 21! No es que me vaya a entrar la menopausia mañana o tú vayas a necesitar viagra."
        mc "*Risa* Espero que no."
    call BlinkXP ("c17s004_295" , "d") from _call_BlinkXP_2419
    meg "Ahora me debería ir. Me tengo que duchar y vestirme antes de la cena. Entro a trabajar a las 9:00."
    mc "¿Quieres que te lleve?"
    call BlinkXP ("c17s004_300" , "d") from _call_BlinkXP_2420
    meg "No hace falta, pediré un Under."
    meg "Voy a recoger la ropa, vestirme y a irme."
    mc "Una lástima tapar con ropa tanta belleza."
    call KissXP ("c17s004_305" , "f") from _call_KissXP_76
    "Una vez vestidos... o vestida ella, para ser más exactos, tú tan solo necesitas tu albornoz."
    meg "Te veo en la cena."
    mc "Hasta luego preciosa."
    stop music fadeout (1.5)
    scene black with dissolve
    "Tú también pasas por la ducha y te vistes. Elegante pero informal, tal como han pedido las chicas."
    return
label c17s005_EvaDinner:
    scene black with dissolve
    play sound ("music/RingtoneMC.ogg")
    "Justo cuando acabas de vestirte para la cena, suena el teléfono."
    stop sound
    call BlinkXP ("c17s005_005" , "d") from _call_BlinkXP_2421
    play music ("music/I-Can-Feel-it-Coming.ogg")
    eva "Buenas tardes, [mc]. ¿Ya estás vestido?"
    mc "Hola, Eva. Sí, ¿por qué lo dices?"
    call BlinkXP ("c17s005_010" , "d") from _call_BlinkXP_2422
    eva "Te he visto volver del baño y te he dado un tiempo prudencial para vestirte."
    eva "No me gusta eso de no saber lo que pasa en las habitaciones y solo poder intuirlo."
    mc "*Risa* Bienvenida al mundo normal, Eva."
    mc "¿Puedo ayudarte en algo?"
    call BlinkXP ("c17s005_015" , "d") from _call_BlinkXP_2423
    eva "Tu no vas a beber alcohol esta noche, ¿verdad?"
    eva "En el plan de las chicas, me refiero..."
    mc "Nadie me ha explicado el plan. Por tu pregunta, supongo que me tocará ser el conductor responsable y no beberé."
    call BlinkXP ("c17s005_020" , "d") from _call_BlinkXP_2424
    eva "Contaba con que te tocara conducir."
    eva "Yo quiero poder beber, con lo que no quiero coger la furgoneta de Amanda."
    mc "Lo entiendo..."
    call BlinkXP ("c17s005_025" , "d") from _call_BlinkXP_2425
    eva "¿Podrías venir a buscarme como hiciste ayer con Amanda?"
    mc "Por supuesto. ¿Cuándo quieres que vaya a buscarte?"
    mc "La cena empieza en media hora y eres la invitada de honor de hoy."
    call BlinkXP ("c17s005_030" , "d") from _call_BlinkXP_2426
    eva "¡Yay! Sal dentro de diez minutos de tu casa."
    eva "Aún me tengo que secar el pelo y vestirme. Pero soy mucho más rápida que [emm]."
    eva "En veinte minutos estaré lista. Cuando llegues entra en mi habitación, la puerta por la que me fui anoche."
    mc "Okay. En veinte minutos estaré ahí."
    call BlinkXP ("c17s005_035" , "d") from _call_BlinkXP_2427
    eva "Y... [mc]..."
    mc "Dime, Eva."
    eva "Gracias."
    scene black with dissolve
    "Eva cuelga el teléfono justo después de darte las gracias, sin darte tiempo de contestar."
    scene c17s005_040a with dissolve
    "Sales un par de minutos antes de la hora que te ha indicado Eva y, obviamente, llegas un par de minutos antes de lo indicado."
    "Tienen perfectamente medidas las distancias de la base a tu casa."
    scene c17s005_040b with dissolve
    "Te acercas a la puerta y dejas pasar los dos minutos antes de llamar. No sería buena idea pillarla a medio vestir... o posiblemente sí."
    "*Knock-Knock*"
    mc "Eva, soy yo. ¿Puedo pasar?"
    eva "*A través de la puerta* Sí, pasa. Ya estoy lista."
    scene c17s005_045d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP("c17s005_045" , "d") from _call_BlinkXP_2428
    eva "Hola de nuevo, [mc]."
    if not _in_replay:
        $ renpy.notify ("Profile Image unlocked for Eva: 2 - Formal")
        $ eva.profileImages.pop (1) # first remove
        $ eva.profileImages.insert (1, ("eva_1", None)) # then add new
    mc "¡Wow, Eva! ¡Estás preciosa!"
    mc "Quizás demasiado elegante, pero increíblemente preciosa."
    call BlinkXP ("c17s005_050" , "d") from _call_BlinkXP_2429
    eva "Gracias, [mc]. Me han dicho que me pusiera un vestido bonito y este era el más bonito que tenía."
    eva "¿Crees que voy demasiado bien vestida? Puedo cambiarme en un par de minutos..."
    mc "No hace falta, Eva. Ya te he dicho que estás preciosa."
    scene c17s005_055a with dissolve
    eva "Entonces quiero mi beso de buenos días y nos vamos. Aunque ya sea por la tarde."
    eva "Buenos días, [mc]."
    scene c17s005_055b with hpunch
    "No te deja contestar antes de plantar sus labios sobre los tuyos."
    "Ese beso tiene algo diferente de los anteriores. Después de la conversación con Betty, tendrás que preguntarle."
    stop music fadeout (1.5)
    "Pero mejor en otro momento. No quieres que la primera cena de Eva en casa se ponga extraña antes de empezar."
    return

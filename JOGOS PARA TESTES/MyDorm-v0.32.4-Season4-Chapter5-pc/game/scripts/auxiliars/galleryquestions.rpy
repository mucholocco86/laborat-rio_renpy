label mrS3_sai_listen:
    menu:
        "Durante la videoconferencia con Saira, ¿seguiste escuchando cuando ella pensó que había colgado?"
        "Sí.":
            $ sai._var ("listen", True)
        "No.":
            $ sai._var ("listen", False)
label mrS3_sai_route:
    menu:
        "¿Estás en una relación con [sai]?"
        "Sí.":
            $ sai._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ sai._var("route", False)
            $ sai._var("pregnant", False)
    return
label mrS3_sai_pregnant:
    menu:
        "¿[sai] está embarazada?"
        "Sí.":
            $ sai._var("pregnant", True)
        "No.":
            $ sai._var("pregnant", False)
    return
label mrS3_sai_undiscoveredPregnancy:
    menu:
        "¿[sai] ha confirmado su embarazo?"
        "Sí.":
            $ sai._var("undiscoveredPregnancy", False)
        "No.":
            $ sai._var("undiscoveredPregnancy", True)
    return
label mrS3_mar_route:
    menu:
        "¿Estás en una relación con [mar]?"
        "Sí.":
            $ mar._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ mar._var("route", False)
            $ mar._var("pregnant", False)
    return
label mrS3_mar_pregnant:
    menu:
        "¿[mar] está embarazada?"
        "Sí.":
            $ mar._var("pregnant", True)
        "No.":
            $ mar._var("pregnant", False)
    return
label mrS3_mar_undiscoveredPregnancy:
    menu:
        "¿[mar] ha confirmado su embarazo?"
        "Sí.":
            $ mar._var("undiscoveredPregnancy", False)
        "No.":
            $ mar._var("undiscoveredPregnancy", True)
    return
label mrS3_mar_secondChance:
    menu:
        "¿Cuándo abriste la ruta con [mar]?"
        "Viendo películas.":
            $ mar._var("routeSecondChance", False)
        "En el café, antes de ir de compras.":
            $ mar._var("routeSecondChance", True)
    return
label mrS3_mar_fittingRoom:
    menu:
        "¿Espiaste a [mar] en el probador de la tienda de [mad.nick]?"
        "Sí.":
            $ mar._var("fittingRoom", True)
        "No.":
            $ mar._var("fittingRoom", False)
    return
label mrS3_mar_lewdname:
    menu:
        "¿Cómo llamas a [mar] durante el sexo?"
        "Mamá":
            $ mar.name.lewd = __("Mamá")
        "Por su nombre":
            $ mar.name.lewd = mar.name.firstname
    return

label mrS3_emm_route:
    menu:
        "¿Estás en una relación con [emm]?"
        "Sí.":
            $ emm._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ emm._var("route", False)
            $ emm._var("pregnant", False)
    return
label mrS3_emm_pregnant:
    menu:
        "¿[emm] está embarazada?"
        "Sí.":
            $ emm._var("pregnant", True)
        "No.":
            $ emm._var("pregnant", False)
    return
label mrS3_emm_undiscoveredPregnancy:
    menu:
        "¿[emm] ha confirmado su embarazo?"
        "Sí.":
            $ emm._var("undiscoveredPregnancy", False)
        "No.":
            $ emm._var("undiscoveredPregnancy", True)
    return
label mrS3_emm_reg:
    menu:
        "¿Qué le dijiste a [emm] sobre su lenguaje soez durante el sexo?"
        "No me importa mientras tú estés cómoda":
            $ emm._var ("reggaeton", True)
        "No me gusta demasiado":
            $ emm._var ("reggaeton", False)
    return
label mrS3_emm_papi:
    menu:
        "¿Qué le dijiste a [emm] sobre llamarte Papi durante el sexo?"
        "Puedes seguir llamándome Papi si quieres":
            $ emm.name.mcLewd = "Papi"
        "Prefiero que me llames por mi nombre":
            $ emm.name.mcLewd = mc.name.first_name
    return
label mrS3_emm_hadAnal:
    menu:
        "¿Tuviste sexo anal con [emm]?"
        "Sí.":
            $ emm._var("hadAnal", True)
        "No.":
            $ emm._var("hadAnal", False)
    return

label mrS3_eri_route:
    menu:
        "¿Estás en una relación con [eri]?"
        "Sí.":
            $ eri._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ eri._var("route", False)
            $ eri._var("pregnant", False)
    return
label mrS3_eri_pregnant:
    menu:
        "¿[eri] está embarazada?"
        "Sí.":
            $ eri._var("pregnant", True)
        "No.":
            $ eri._var("pregnant", False)
    return
label mrS3_eri_undiscoveredPregnancy:
    menu:
        "¿[eri] ha confirmado su embarazo?"
        "Sí.":
            $ eri._var("undiscoveredPregnancy", False)
        "No.":
            $ eri._var("undiscoveredPregnancy", True)
    return
label mrS3_beating1:
    menu:
        "¿Te enfrentaste a Jack en el Café de Luca?"
        "Sí.":
            $ mc._var("beatingToilet", True)
            $ eri._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ mc._var("beatingToilet", False)
            $ eri._var("route", False)
    return
label mrS3_eri_chance:
    menu:
        "¿Cómo abriste la relación con [eri]?"
        "Me enfrenté a Jack en el café.":
            $ eri._var("routeSecondChance", False)
            $ eri._var("routeThirdChance", False)
        "Le confesé que yo le dije a Jamaal que le enviara las fotos de Jack después de la noche en el Twins.":
            $ eri._var("routeSecondChance", True)
            $ eri._var("routeThirdChance", False)
        "Le confesé que yo le dije a Jamaal que le enviara las fotos de Jack en la sauna.":
            $ eri._var("routeSecondChance", False)
            $ eri._var("routeThirdChance", True)
    return
label mrS3_eri_pregnacyDiscovered:
    menu:
        "¿[eri] estaba embarazada antes de la noche con [dap] y [emm] (si estás en ruta con ellas)?"
        "Sí.":
            $ eri._var("pregnancyDiscovered", True)
        "No.":
            $ eri._var("pregnancyDiscovered", False)
    return

label mrS3_nor_route:
    menu:
        "¿Estás en una relación con [nor]?"
        "Sí.":
            $ nor._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ nor._var("route", False)
            $ nor._var("pregnant", False)
    return
label mrS3_nor_pregnant:
    menu:
        "¿[nor] está embarazada?"
        "Sí.":
            $ nor._var("pregnant", True)
        "No.":
            $ nor._var("pregnant", False)
    return
label mrS3_nor_undiscoveredPregnancy:
    menu:
        "¿[nor] ha confirmado su embarazo?"
        "Sí.":
            $ nor._var("undiscoveredPregnancy", False)
        "No.":
            $ nor._var("undiscoveredPregnancy", True)
    return
label mrS3_nor_secondChance:
    menu:
        "¿Dónde empezaste la relación con [nor]?"
        "En la ducha.":
            $ nor._var("routeSecondChance", False)
        "En el café.":
            $ nor._var("routeSecondChance", True)
    return
label mrS3_nor_nick:
    menu:
        "¿Cual es el mote que le pusiste a [nor]?"
        "Mi Gordita.":
            $ nor._var("uNick", _("Mi Gordita"))
            $ uNick = _("Mi Gordita")
        "Otra cosa.":
            $ texto = renpy.input (_("¿Cómo quieres llamar cariñosamente a [nor]? Recomiendo que tenga que ver con su peso."))
            $ nor._var("uNick", texto)
            $ uNick = texto
    return
label mrS3_nor_anal:
    menu:
        "¿Habilitaste el sexo anal con [nor]?"
        "Sí.":
            $ nor._var("anal", True)
        "No.":
            $ nor._var("anal", False)
    return
label mrS3_take_eri_work:
    menu:
        "¿Llevaste a [eri] al trabajo el primer domingo?"
        "Sí. Para librarme de lavar los platos.":
            $ eri._var("broughtToWorkOnDay6", True)
        "Sí. Mientras lavaba los platos se le averió el coche a [nor].":
            $ eri._var("broughtToWorkOnDay6", False)
    return

label mrS3_dapSca_route:
    menu:
        "¿Enseñaste a [dap] y Scarlett a besar en lecciones conjuntas?"
        "Sí.":
            $ dap._var("route", True)
            $ sca._var("route", True)
            $ mc._var("routeDapSca", True)
        "No.":
            $ dap._var("route", False)
            $ sca._var("route", False)
            $ mc._var("routeDapSca", False)
    return
label mrS3_dap_route:
    menu:
        "¿Estás en una relación con [dap]?"
        "Sí.":
            $ dap._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ dap._var("route", False)
            $ dap._var("pregnant", False)
    return
label mrS3_dap_romance:
    menu:
        "¿Qué tipo de relación tienes con [dap]?"
        "Romance.":
            $ dap._var("romance", True)
        "Me intenta corromper.":
            $ dap._var("romance", False)
    return
label mrS3_dap_pregnant:
    menu:
        "¿[dap] está embarazada?"
        "Sí.":
            $ dap._var("pregnant", True)
        "No.":
            $ dap._var("pregnant", False)
    return
label mrS3_dap_undiscoveredPregnancy:
    menu:
        "¿[dap] ha confirmado su embarazo?"
        "Sí.":
            $ dap._var("undiscoveredPregnancy", False)
        "No.":
            $ dap._var("undiscoveredPregnancy", True)
    return

label mrS3_sca_route:
    menu:
        "¿Estás en una relación con [sca]?"
        "Sí.":
            $ sca._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ sca._var("route", False)
            $ sca._var("pregnant", False)
    return
label mrS3_sca_pregnant:
    menu:
        "¿[sca] está embarazada?"
        "Sí.":
            $ sca._var("pregnant", True)
        "No.":
            $ sca._var("pregnant", False)
    return
label mrS3_sca_undiscoveredPregnancy:
    menu:
        "¿[sca] ha confirmado su embarazo?"
        "Sí.":
            $ sca._var("undiscoveredPregnancy", False)
        "No.":
            $ sca._var("undiscoveredPregnancy", True)
    return
label mrS3_sca_anal:
    menu:
        "¿Le dijiste a [sca] que te gustaba el sexo anal?"
        "Sí.":
            $ sca._var("anal", True)
        "No.":
            $ sca._var("anal", False)
    return

label mrS3_eil_route:
    menu:
        "¿Estás en una relación con [eil]?"
        "Sí.":
            $ eil._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ eil._var("route", False)
            $ eil._var("pregnant", False)
    return
label mrS3_eil_secondChance:
    menu:
        "¿Dónde empezaste la relación con [eil]?"
        "En el café.":
            $ eil._var("routeSecondChance", False)
        "En el bosque.":
            $ eil._var("routeSecondChance", True)
    return
label mrS3_eil_pregnant:
    menu:
        "¿[eil] está embarazada?"
        "Sí.":
            $ eil._var("pregnant", True)
        "No.":
            $ eil._var("pregnant", False)
    return
label mrS3_eil_undiscoveredPregnancy:
    menu:
        "¿[eil] ha confirmado su embarazo?"
        "Sí.":
            $ eil._var("undiscoveredPregnancy", False)
        "No.":
            $ eil._var("undiscoveredPregnancy", True)
    return

label mrS3_sam_route1:
    menu:
        "¿Le dijiste a [sam] que te gustaba durante el masaje en tu casa?"
        "Sí.":
            $ sam._var("massage", True)
            $ sam._var("routeSecondChance", False)
        "No.":
            $ sam._var("massage", False)
            $ sam._var("routeSecondChance", False)
    return
label mrS3_sam_route:
    menu:
        "¿Estás en una relación con [sam]?"
        "Sí.":
            $ sam._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ sam._var("route", False)
            $ sam._var("pregnant", False)
    return
label mrS3_sam_blackPanther:
    menu:
        "¿Cómo lleva [sam] su vello púbico?"
        "Al natural.":
            $ sam._var("naturalPubicHair", True)
        "Afeitado.":
            $ sam._var("naturalPubicHair", False)
    return
label mrS3_sam_pregnant:
    menu:
        "¿[sam] está embarazada?"
        "Sí.":
            $ sam._var("pregnant", True)
        "No.":
            $ sam._var("pregnant", False)
    return
label mrS3_sam_undiscoveredPregnancy:
    menu:
        "¿[sam] ha confirmado su embarazo?"
        "Sí.":
            $ sam._var("undiscoveredPregnancy", False)
        "No.":
            $ sam._var("undiscoveredPregnancy", True)
    return
label mrS3_sam_pregnancyDiscovered:
    menu:
        "¿Has descubierto que [sam] está embarazada?"
        "Sí.":
            $ sam._var("pregnancyDiscovered", True)
        "No.":
            $ sam._var("pregnancyDiscovered", False)
    return

label mrS3_sim_route:
    menu:
        "¿Estás en una relación con [sim]?"
        "Sí.":
            $ sim._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ sim._var("route", False)
            $ sim._var("pregnant", False)
    return
label mrS3_sim_pregnant:
    menu:
        "¿[sim] está embarazada?"
        "Sí.":
            $ sim._var("pregnant", True)
        "No.":
            $ sim._var("pregnant", False)
    return
label mrS3_sim_undiscoveredPregnancy:
    menu:
        "¿[sim] ha confirmado su embarazo?"
        "Sí.":
            $ sim._var("undiscoveredPregnancy", False)
        "No.":
            $ sim._var("undiscoveredPregnancy", True)
    return
label mrS3_sim_pregnancyBeforeSunday:
    menu:
        "¿[sim] estaba embarazada antes de la fiesta de la piscina?"
        "Sí.":
            $ sim._var("pregnancyDiscovered", True)
        "No.":
            $ sim._var("pregnancyDiscovered", False)
    return
label mrS3_sim_pregnancyDiscovered:
    menu:
        "¿Has descubierto que [sim] está embarazada?"
        "Sí.":
            $ sim._var("pregnancyDiscovered", True)
        "No.":
            $ sim._var("pregnancyDiscovered", False)
    return

label mrS3_oma_route:
    menu:
        "¿Estás en una relación con [oma]?"
        "Sí.":
            $ oma._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ oma._var("route", False)
            $ oma._var("pregnant", False)
    return
label mrS3_oma_pregnant:
    menu:
        "¿[oma] está embarazada?"
        "Sí.":
            $ oma._var("pregnant", True)
        "No.":
            $ oma._var("pregnant", False)
    return
label mrS3_oma_undiscoveredPregnancy:
    menu:
        "¿[oma] ha confirmado su embarazo?"
        "Sí.":
            $ oma._var("undiscoveredPregnancy", False)
        "No.":
            $ oma._var("undiscoveredPregnancy", True)
    return

label mrS3_eva_route:
    menu:
        "¿Estás en una relación con [eva]?"
        "Sí.":
            $ eva._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ eva._var("route", False)
            $ eva._var("pregnant", False)
    return
label mrS3_eva_pregnant:
    menu:
        "¿[eva] está embarazada?"
        "Sí.":
            $ eva._var("pregnant", True)
        "No.":
            $ eva._var("pregnant", False)
    return
label mrS3_eva_undiscoveredPregnancy:
    menu:
        "¿[eva] ha confirmado su embarazo?"
        "Sí.":
            $ eva._var("undiscoveredPregnancy", False)
        "No.":
            $ eva._var("undiscoveredPregnancy", True)
    return
label mrS3_eva_choking:
    menu:
        "¿Activaste el fetiche de asfixia con [eva]?"
        "Sí.":
            $ eva._var("choking", True)
        "No.":
            $ eva._var("choking", False)
    return

label mrS3_mad_route:
    menu:
        "¿Estás en una relación con [mad.nick]?"
        "Sí.":
            $ mad._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ mad._var("route", False)
    return
label mrS3_mad_type:
    menu:
        "¿Qué tipo de relación tienes con [mad.nick]?"
        "Romance. No espié a [mar] o no estoy en una relación con ella.":
            $ mar._var("fittingRoom", False)
            $ mad._var("romance", True)
            $ mad._var("sub", False)
            $ mad._var("dom", False)
        "Romance. Espié a [mar] pero el chantaje no funcionó.":
            $ mar._var("fittingRoom", True)
            $ mad._var("romance", True)
            $ mad._var("sub", False)
            $ mad._var("dom", False)
        "Es sumisa conmigo. Intentó chantajearme pero le di la vuelta al chantaje.":
            $ mar._var("fittingRoom", True)
            $ mad._var("romance", False)
            $ mad._var("sub", True)
            $ mad._var("dom", False)
        "Es dominante conmigo. Me chantajeó y yo le seguí el juego.":
            $ mar._var("fittingRoom", True)
            $ mad._var("romance", False)
            $ mad._var("sub", False)
            $ mad._var("dom", True)
    return
label mrS3_mad_type2:
    menu:
        "¿Qué tipo de relación empezaste con [mad.nick]?"
        "Romance. No espié a [mar] o no estoy en una relación con ella.":
            $ mar._var("fittingRoom", False)
            $ mad._var("romance", True)
            $ mad._var("sub", False)
            $ mad._var("dom", False)
        "Romance. Espié a [mar] pero el chantaje no funcionó.":
            $ mar._var("fittingRoom", True)
            $ mad._var("romance", True)
            $ mad._var("sub", False)
            $ mad._var("dom", False)
        "Era sumisa conmigo. Intentó chantajearme pero le di la vuelta al chantaje.":
            $ mar._var("fittingRoom", True)
            $ mad._var("romance", False)
            $ mad._var("sub", True)
            $ mad._var("dom", False)
        "Era dominante conmigo. Me chantajeó y yo le seguí el juego.":
            $ mar._var("fittingRoom", True)
            $ mad._var("romance", False)
            $ mad._var("sub", False)
            $ mad._var("dom", True)
    return
label mrS3_mad_pregnant:
    menu:
        "¿[mad.nick] está embarazada?"
        "Sí.":
            $ mad._var("pregnant", True)
        "No.":
            $ mad._var("pregnant", False)
    return
label mrS3_mad_undiscoveredPregnancy:
    menu:
        "¿[mad] ha confirmado su embarazo?"
        "Sí.":
            $ mad._var("undiscoveredPregnancy", False)
        "No.":
            $ mad._var("undiscoveredPregnancy", True)
    return

label mrS3_meg_route:
    menu:
        "¿Estás en una relación con [meg]?"
        "Sí.":
            $ meg._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ meg._var("route", False)
    return
label mrS3_meg_pregnant:
    menu:
        "¿[meg] está embarazada?"
        "Sí.":
            $ meg._var("pregnant", True)
        "No.":
            $ meg._var("pregnant", False)
    return
label mrS3_meg_undiscoveredPregnancy:
    menu:
        "¿[meg] ha confirmado su embarazo?"
        "Sí.":
            $ meg._var("undiscoveredPregnancy", False)
        "No.":
            $ meg._var("undiscoveredPregnancy", True)
    return

label mrS3_ama_route:
    menu:
        "¿Estás en una relación con [ama]?"
        "Sí.":
            $ ama._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ ama._var("route", False)
    return
label mrS3_ama_pregnant:
    menu:
        "¿[ama] está embarazada?"
        "Sí.":
            $ ama._var("pregnant", True)
        "No.":
            $ ama._var("pregnant", False)
    return
label mrS3_ama_undiscoveredPregnancy:
    menu:
        "¿[ama] ha confirmado su embarazo?"
        "Sí.":
            $ ama._var("undiscoveredPregnancy", False)
        "No.":
            $ ama._var("undiscoveredPregnancy", True)
    return

label mrS3_kim_route:
    menu:
        "¿Estás en una relación con [kim]?"
        "Sí.":
            $ kim._var("route", True)
            $ kim._var("saved", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ kim._var("route", False)
    return
label mrS3_kim_saved:
    menu:
        "¿'Salvaste' a [kim] en el barco de Ichigo o lo hizo [ama]?"
        "Lo hice yo.":
            $ kim._var("saved", True)
        "Lo hizo [ama].":
            $ kim._var("saved", False)
    return
label mrS3_kim_rps (low, mid, high):
    $ kim.rp (0 , "set")
    menu:
        "¿Cuántos Puntos de Relación tienes con [kim]?"
        "Menos de [low]":
            $ kim.rp (low-1)
        "Entre [low] y [high]":
            $ kim.rp(mid)
        "Más de [high]":
            $ kim.rp(high+1)
    return
label mrS3_kim_makeup:
    menu:
        "¿Qué le dijiste a Kim sobre su maquillaje corporal?"
        "Debería mostrarse como es.":
            $ kim._var ("makeup", False)
        "Debería esconder su condición.":
            $ kim._var ("makeup", True)
    return
label mrS3_kim_pregnant:
    menu:
        "¿[kim] está embarazada?"
        "Sí.":
            $ kim._var("pregnant", True)
        "No.":
            $ kim._var("pregnant", False)
    return
label mrS3_kim_undiscoveredPregnancy:
    menu:
        "¿[kim] ha confirmado su embarazo?"
        "Sí.":
            $ kim._var("undiscoveredPregnancy", False)
        "No.":
            $ kim._var("undiscoveredPregnancy", True)
    return

label mrS3_kat_rps (low, mid, high):
    $ kat.rp (0 , "set")
    menu:
        "¿Cuántos Puntos de Relación tienes con [kat]?"
        "Menos de [low]":
            $ kat.rp (low-1)
        "Entre [low] y [high]":
            $ kat.rp(mid)
        "Más de [high]":
            $ kat.rp(high+1)
    return
label mrS3_kat_slim:
    menu:
        "¿De qué convenciste a [kat]? Ambas opciones arreglaban su problema de salud."
        "De hacer más ejercicio. ([kat] mantendrá su figura inicial.)":
            $ kat._var("slim", False)
        "De hacer más ejercicio y comer más sano. ([kat] estará más delgada en el futuro.)":
            $ kat._var("slim", True)
    return
label mrS3_kat_lesbian:
    menu:
        "¿Habilitaste el contenido lésbico para [kat]?"
        "Sí.":
            $ kat._var("lesbianContent" , True)
        "No.":
            $ kat._var("lesbianContent" , False)
    return
label mrS3_kat_pregnant:
    menu:
        "¿[kat] está embarazada?"
        "Sí.":
            $ kat._var("pregnant", True)
        "No.":
            $ kat._var("pregnant", False)
    return
label mrS3_kat_undiscoveredPregnancy:
    menu:
        "¿[kat] ha confirmado su embarazo?"
        "Sí.":
            $ kat._var("undiscoveredPregnancy", False)
        "No.":
            $ kat._var("undiscoveredPregnancy", True)
    return
label mrS3_kat_route:
    menu:
        "¿Estás en una relación con [kat]?"
        "Sí.":
            $ kat._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ kat._var("route", False)
    return

label mrS3_deb_route:
    menu:
        "¿Estás en una relación con [deb.nick]?"
        "Sí.":
            $ deb._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ deb._var("route", False)
    return
label mrS3_deb_rps (low, mid, high):
    $ deb.rp (0 , "set")
    menu:
        "¿Cuántos Puntos de Relación tienes con [deb.nick]?"
        "Menos de [low]":
            $ deb.rp (low-1)
        "Entre [low] y [high]":
            $ deb.rp(mid)
        "Más de [high]":
            $ deb.rp(high+1)
    return
label mrS3_deb_laptop:
    menu:
        "¿Le prestaste tu portátil a [deb.nick]?"
        "Sí.":
            $ deb._var("laptop", True)
        "No.":
            $ deb._var("laptop", False)
    return
label mrS3_deb_pregnant:
    menu:
        "¿[deb.nick] está embarazada?"
        "Sí.":
            $ deb._var("pregnant", True)
        "No.":
            $ deb._var("pregnant", False)
    return
label mrS3_deb_undiscoveredPregnancy:
    menu:
        "¿[deb] ha confirmado su embarazo?"
        "Sí.":
            $ deb._var("undiscoveredPregnancy", False)
        "No.":
            $ deb._var("undiscoveredPregnancy", True)
    return

label mrS3_lis_rps (low, mid, high):
    $ lis.rp (0 , "set")
    menu:
        "¿Cuántos Puntos de Relación tienes con [lis]?"
        "Menos de [low]":
            $ lis.rp (low-1)
        "Entre [low] y [high]":
            $ lis.rp(mid)
        "Más de [high]":
            $ lis.rp(high+1)
    return
label mrS3_lis_route:
    menu:
        "¿Estás en una relación con [lis]?"
        "Sí.":
            $ lis._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ lis._var("route", False)
    return
label mrS3_lis_pregnant:
    menu:
        "¿[lis] está embarazada?"
        "Sí.":
            $ lis._var("pregnant", True)
        "No.":
            $ lis._var("pregnant", False)
    return
label mrS3_lis_undiscoveredPregnancy:
    menu:
        "¿[lis] ha confirmado su embarazo?"
        "Sí.":
            $ lis._var("undiscoveredPregnancy", False)
        "No.":
            $ lis._var("undiscoveredPregnancy", True)
    return
label mrS3_lis_anal:
    menu:
        "¿Tuviste sexo anal con [lis]?"
        "Sí.":
            $ lis._var("anal", True)
        "No.":
            $ lis._var("anal", False)
    return

label mrS3_mee_knows:
    menu:
        "¿Escuchaste a [bet] y [mar] hablar sobre el cáncer de [mee]?"
        "Sí.":
            $ mee._var("mcKnowsSickness", True)
        "No.":
            $ mee._var("mcKnowsSickness", True)
    return
label mrS3_mee_route:
    menu:
        "¿Estás en una relación con [mee]?"
        "Sí.":
            $ mee._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ mee._var("route", False)
    return

label mrS3_bet_route1:
    menu:
        "¿Le dijiste a [bet] que vuestra relación era posible?"
        "Sí.":
            $ bet._var("route", True)
        "No.":
            $ bet._var("route", False)
    return
label mrS3_bet_route:
    menu:
        "¿Estás en una relación con [bet]?"
        "Sí.":
            $ bet._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ bet._var("route", False)
    return
label mrS3_bet_pregnant:
    menu:
        "¿[bet] está embarazada?"
        "Sí.":
            $ bet._var("pregnant", True)
        "No.":
            $ bet._var("pregnant", False)
    return
label mrS3_bet_undiscoveredPregnancy:
    menu:
        "¿[bet] ha confirmado su embarazo?"
        "Sí.":
            $ bet._var("undiscoveredPregnancy", False)
        "No.":
            $ bet._var("undiscoveredPregnancy", True)
    return

label mrS3_kia_route:
    menu:
        "¿Estás en una relación con [kia]?"
        "Sí.":
            $ kia._var("route", True)
            $ mc._var("relationships", 1, "add")
        "No.":
            $ kia._var("route", False)
    return
label mrS3_kia_pregnant:
    menu:
        "¿[kia] está embarazada?"
        "Sí.":
            $ kia._var("pregnant", True)
        "No.":
            $ kia._var("pregnant", False)
    return
label mrS3_kis_undiscoveredPregnancy:
    menu:
        "¿[kia] ha confirmado su embarazo?"
        "Sí.":
            $ kia._var("undiscoveredPregnancy", False)
        "No.":
            $ kia._var("undiscoveredPregnancy", True)
    return
label mrS3_kia_urination:
    menu:
        "¿Activaste el fetiche de orina con [kia]?"
        "Sí.":
            $ kia._var("urination", True)
        "No.":
            $ kia._var("urination", False)
    return

label mrS3_rels:
    menu:
        "¿En cuántas relaciones estás?"
        "Ninguna" if mc._var("relationships")<1:
            $ mc._var("relationships", 0, "set")
        "Una" if mc._var("relationships")<2:
            $ mc._var("relationships", 1, "set")
        "Dos" if mc._var("relationships") <3:
            $ mc._var("relationships", 2, "set")
        "Tres" if mc._var("relationships") <4:
            $ mc._var("relationships", 3, "set")
        "Más de tres":
            $ mc._var("relationships", 4, "set")
    return
label mrS3_truth_dare:
    menu:
        "En el juego de Verdad o Reto, ¿qué elegiste?"
        "Verdad.\n (Era la opción recomendada.)":
            $ mc._var("truthOrDare", True)
        "Reto.":
            $ mc._var("truthOrDare", False)
    return
label mrS3_edmund_story:
    menu:
        "¿Le cogiste el teléfono a tu padre cuando llamó?"
        "Sí.":
            $ mc._var ("edmundsStory", True)
        "No.":
            $ mc._var ("edmundsStory", False)
    return
label mrS3_wantsChildren:
    menu:
        "¿Has dicho que querías tener hijos?"
        "Sí.":
            $ mc._var("wantsChildren", True)
        "No.":
            $ mc._var("wantsChildren", False)
    return
label mrS3_listenDebLis:
    menu:
        "¿Te paraste a escuchar a [deb.nick] y a [lis]?"
        "Sí.":
            $ mc._var("listenDebLis", True)
        "No.":
            $ mc._var("listenDebLis", False)
    return
label mrS3_salary:
    menu:
        "¿Qué promesa incumpliste de las que le hiciste a los clones?"
        "Incumplir el salario retroactivo.":
            $ salary = True
        "Incumplir el sistema de promociones.":
            $ salary = False
    return
label mrS3_gf:
    call mrS3_sai_route from _call_mrS3_sai_route_3
    if sai._var("route"):
        $ mc._var("relationships", -1, "add")
    else:
        call mrS3_mar_route from _call_mrS3_mar_route_2
        if mar._var("route"):
            $ mc._var("relationships", -1, "add")
        else:
            call mrS3_emm_route from _call_mrS3_emm_route_3
            if emm._var("route"):
                $ mc._var("relationships", -1, "add")
            else:
                call mrS3_eri_route from _call_mrS3_eri_route_4
                if eri._var("route"):
                    $ mc._var("relationships", -1, "add")
                else:
                    call mrS3_dap_route from _call_mrS3_dap_route_3
                    if dap._var("route"):
                        $ mc._var("relationships", -1, "add")
                    else:
                        call mrS3_nor_route from _call_mrS3_nor_route_1
                        if nor._var("route"):
                            $ mc._var("relationships", -1, "add")
                        else:
                            call mrS3_sca_route from _call_mrS3_sca_route_2
                            if sca._var("route"):
                                $ mc._var("relationships", -1, "add")
                            else:
                                call mrS3_eil_route from _call_mrS3_eil_route
                                if eil._var("route"):
                                    $ mc._var("relationships", -1, "add")
                                else:
                                    call mrS3_sam_route from _call_mrS3_sam_route_2
                                    if sam._var("route"):
                                        $ mc._var("relationships", -1, "add")
                                    else:
                                        call mrS3_sim_route from _call_mrS3_sim_route_2
                                        if sim._var("route"):
                                            $ mc._var("relationships", -1, "add")
                                        else:
                                            call mrS3_oma_route from _call_mrS3_oma_route
                                            if oma._var("route"):
                                                $ mc._var("relationships", -1, "add")
                                            else:
                                                call mrS3_mad_route from _call_mrS3_mad_route
                                                if mad._var("route"):
                                                    $ mc._var("relationships", -1, "add")
                                                else:
                                                    call mrS3_meg_route from _call_mrS3_meg_route_1
                                                    if meg._var("route"):
                                                        $ mc._var("relationships", -1, "add")
                                                    else:
                                                        call mrS3_deb_route from _call_mrS3_deb_route_3
                                                        if deb._var("route"):
                                                            $ mc._var("relationships", -1, "add")
                                                        else:
                                                            call mrS3_kia_route from _call_mrS3_kia_route
                                                            if kia._var("route"):
                                                                $ mc._var("relationships", -1, "add")
                                                            else:
                                                                call mrS3_ama_route from _call_mrS3_ama_route_4
                                                                if ama._var("route"):
                                                                    $ mc._var("relationships", -1, "add")
                                                                else:
                                                                    call mrS3_eva_route from _call_mrS3_eva_route_2
    return
label mrS3_rename:
    return
label mrS3_pregnancies(Emm, Eva, Mad, Ama, Kim, Kat, Deb, Lis, Bet, Kia):
    call mrS3_sai_pregnant from _call_mrS3_sai_pregnant_2
    call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_2
    if Emm:
        call mrS3_emm_pregnant from _call_mrS3_emm_pregnant_1
    call mrS3_eri_pregnant from _call_mrS3_eri_pregnant_1
    call mrS3_nor_pregnant from _call_mrS3_nor_pregnant_2
    call mrS3_dap_pregnant from _call_mrS3_dap_pregnant_1
    call mrS3_sca_pregnant from _call_mrS3_sca_pregnant_3
    call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_2
    call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_3
    call mrS3_sim_pregnant from _call_mrS3_sim_pregnant
    call mrS3_oma_pregnant from _call_mrS3_oma_pregnant_1
    if Eva:
        call mrS3_eva_pregnant from _call_mrS3_eva_pregnant
    if Mad:
        call mrS3_mad_pregnant from _call_mrS3_mad_pregnant
    call mrS3_meg_pregnant from _call_mrS3_meg_pregnant_2
    if Ama:
        call mrS3_ama_pregnant from _call_mrS3_ama_pregnant
    if Kim:
        call mrS3_kim_pregnant from _call_mrS3_kim_pregnant
    if Kat:
        call mrS3_kat_pregnant from _call_mrS3_kat_pregnant
    if Deb:
        call mrS3_deb_pregnant from _call_mrS3_deb_pregnant
    if Lis:
        call mrS3_lis_pregnant from _call_mrS3_lis_pregnant
    if Bet:
        call mrS3_bet_pregnant from _call_mrS3_bet_pregnant
    if Kia:
        call mrS3_kia_pregnant from _call_mrS3_kia_pregnant
    return


label mrS3_renameScene:
    "Como esta galería es diferente de las habituales, al no tener nada que ver con tu playthrough, puedes renombrar a los personajes desde aquí."
    "Solo se aplicará a la galería, no a tus playthroughs."
#    if not persistent.haveBeenRenamed2:
#        $ persistent.mc = "Mark"
#        $ persistent.mom = "Martha"
#        $ persistent.emm = "Emma"
#        $ persistent.nor = "Norah"
#        $ persistent.eri = "Erika"
#        $ persistent.dap = "Daphne"
    $ persistent.rename = True
    $ persistent.haveBeenRenamed2 = True
    $ persistent.mc = renpy.input (_("¿Cómo te llamas?"), default = persistent.mc)
    scene black with dissolve
    show martha_4:
        yalign 0.0
    if persistent.family:
        $ textoPregunta = __("Esta es tu madre, ¿quieres cambiarle el nombre?")
    else:
        $ textoPregunta = __("Esta es la ex-novia de tu padre, ¿quieres cambiarle el nombre?")
    $ persistent.mom = renpy.input (textoPregunta, default = persistent.mom)
    show emma_2:
        yalign 0.0
    if persistent.family:
        $ textoPregunta = __("Esta es tu hermana, ¿quieres cambiarle el nombre?")
    else:
        $ textoPregunta = __("Esta es la chica a quién consideras tu hermana, ¿quieres cambiarle el nombre?")
    $ persistent.emm = renpy.input (textoPregunta, default = persistent.emm)
    show norah_1:
        yalign 0.0
    if persistent.family:
        $ textoPregunta = __("Esta es tu tía, ¿quieres cambiarle el nombre?")
    else:
        $ textoPregunta = __("Esta es la vecina de al lado, ¿quieres cambiarle el nombre?")
    $ persistent.nor = renpy.input (textoPregunta, default = persistent.nor)
    show erika_4:
        yalign 0.0
    if persistent.family:
        $ textoPregunta = __("Esta es tu prima, ¿quieres cambiarle el nombre?")
    else:
        $ textoPregunta = __("Esta es la chica a quién consideras tu prima, ¿quieres cambiarle el nombre?")
    $ persistent.eri = renpy.input (textoPregunta, default = persistent.eri)
    show daphne_0:
        yalign 0.0
    if persistent.family:
        $ textoPregunta = __("Esta es tu prima, ¿quieres cambiarle el nombre?")
    else:
        $ textoPregunta = __("Esta es la chica a quién consideras tu prima, ¿quieres cambiarle el nombre?")
    $ persistent.dap = renpy.input (textoPregunta, default = persistent.dap)
    if persistent.dap != "Daphne":
        $ persistent.dapNick = persistent.dap
    else:
        $ persistent.dapNick = "Daph"
    if persistent.emm != "Emma":
        $ persistent.emmNick = persistent.emm
    else:
        $ persistent.emmNick = "Em"
    if persistent.eri != "Erika":
        $ persistent.eriNick = persistent.eri
    else:
        $ persistent.eriNick = "Eri"
    $ renpy.save_persistent()
    "Debes reiniciar el juego por completo para que se apliquen los cambios a la galería."
    return

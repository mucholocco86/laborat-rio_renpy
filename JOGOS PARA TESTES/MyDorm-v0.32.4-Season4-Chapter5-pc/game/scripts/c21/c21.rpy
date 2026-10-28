label c21:
    if dap._var("route") and emm._var("route") and eri._var("route"):
        $ WhatIf4S = False
        call c21s001_Foursome from _call_c21s001_Foursome #************************
    else:
        call c21s001_FoursomeWhatIf from _call_c21s001_FoursomeWhatIf
    call c21s002_PoliceStation from _call_c21s002_PoliceStation
    call c21s002_BettyMassageAndDrivingLicense from _call_c21s002_BettyMassageAndDrivingLicense
    call c21s002_AaronCall from _call_c21s002_AaronCall
    call c21s002_MarChat from _call_c21s002_MarChat
    call c21s002_Megan from _call_c21s002_Megan #Megan goes to Westport
    if kia._var("route"):
        call c21s003_KiaraDate from _call_c21s003_KiaraDate
    else:
        call c21s003_NoKiaraDate from _call_c21s003_NoKiaraDate
    call c21s004_AmandaCoffee from _call_c21s004_AmandaCoffee
    call c21s005_DebRun from _call_c21s005_DebRun #kim, and kate join ***********
    if deb._var("route"):
        call c21s005_DebLake from _call_c21s005_DebLake
    call c21s006_Nor from _call_c21s006_Nor
    return
label c21s001_FoursomeWhatIf:
    scene black with dissolve
    "Hay una escena con [eri], [dap], y [emm], pero no estás en ruta con las tres simultáneamente."
    menu:
        "¿Quieres verlo como una escena alternativa que no afectará a tu partida?"
        "Si":
            $ WhatIf4S = True
            call c21s001_Foursome from _call_c21s001_Foursome_1
        "No":
            pass
    return
label c21s001_Foursome:
    if _in_replay:
        $ WhatIf4S = False
        call mrS3_rename from _call_mrS3_rename
        menu:
            "¿Estás en una relación con [mad.nick]?"
            "Sí":
                $ mad._var("route" , True)
            "No":
                $ mad._var("route" , False)
        menu:
            "¿Estás en una relación con [kia]?"
            "Sí":
                $ kia._var("route" , True)
            "No":
                $ kia._var("route" , False)
        menu:
            "¿Estás en una relación con [sca]?"
            "Sí":
                $ sca._var("route" , True)
                menu:
                    "¿Cogiste el teléfono a tu padre?"
                    "Sí":
                        $ mc._var("edmundsStory" , True)
                    "No":
                        $ mc._var("edmundsStory" , False)
            "No":
                $ sca._var("route" , False)
        menu:
            "¿Estás en una relación con [mar]?"
            "Sí":
                $ mar._var("route" , True)
            "No":
                $ mar._var("route" , False)
        menu:
            "¿Alguna de las chicas ([emm], [eri], [dap]) está embarazada?"
            "Todas":
                $ dap._var("pregnant" , True)
                $ dap._var("pregnancyDiscovered", True)
                $ eri._var("pregnant" , True)
                $ emm._var("pregnant" , True)
            "[eri] es la única":
                $ dap._var("pregnant" , False)
                $ eri._var("pregnant" , True)
                $ emm._var("pregnant" , False)
            "[dap] es la única":
                $ dap._var("pregnant" , True)
                $ dap._var("pregnancyDiscovered", True)
                $ eri._var("pregnant" , False)
                $ emm._var("pregnant" , False)
            "[emm] es la única":
                $ dap._var("pregnant" , False)
                $ eri._var("pregnant" , False)
                $ emm._var("pregnant" , True)
            "[eri] y [dap] están embarazadas":
                $ dap._var("pregnant" , True)
                $ dap._var("pregnancyDiscovered", True)
                $ eri._var("pregnant" , True)
                $ emm._var("pregnant" , False)
            "[eri] y [emm] están embarazadas":
                $ dap._var("pregnant" , False)
                $ eri._var("pregnant" , True)
                $ emm._var("pregnant" , True)
            "[emm] y [dap] están embarazadas":
                $ dap._var("pregnant" , True)
                $ dap._var("pregnancyDiscovered", True)
                $ eri._var("pregnant" , False)
                $ emm._var("pregnant" , True)
            "Ninguna":
                $ dap._var("pregnant" , False)
                $ dap._var("pregnancyDiscovered", False)
                $ eri._var("pregnant" , False)
                $ emm._var("pregnant" , False)
        menu:
            "¿Rechazaste a Beagan, el Hada de [sca], durante la partida de DnD?"
            "No":
                $ sca._var("rejectedBeagan" , False)
                menu:
                    "¿Rechazaste a Aelia y a Paula, los personajes de [eri] y [emm], durante la partida de DnD?"
                    "No":
                        $ mc._var("rejectedAeliaPaula" , False)
                    "Sí":
                        $ mc._var("rejectedAeliaPaula" , True)
            "Sí":
                $ sca._var("rejectedBeagan" , True)
                $ mc._var("rejectedAeliaPaula" , True)
        menu:
            "¿Le dijiste a [emm] que te gustaba el sexo anal?"
            "Sí":
                $ emm._var("anal" , True)
            "No":
                $ emm._var("anal" , False)
    if _in_replay or WhatIf4S:
        scene black with dissolve
        "Al volver a tu habitación..."
        scene c20s007_005a
        emm "¡Has tardado muchísimo en volver!"
        dap "Estábamos a punto de irnos. Menos mal que has llegado ahora."
        if mad._var("route"):
            eri "Creíamos que te ibas a quedar a dormir en casa de [mad.nick]."
        else:
            eri "O de llamarte para saber si te había pasado algo."
    play music ("music/MorningFunnyBeat.ogg")
    call BlinkXPS3 ("c21s001_005" , "d") from _call_BlinkXPS3
    emm "Veníamos a por nuestros regalos de cumpleaños, pero has tardado tanto que se nos han pasado las ganas."
    call BlinkXPS3 ("c21s001_010" , "d") from _call_BlinkXPS3_1
    eri "Las tres nos habíamos comprado esta lencería tan bonita para darte una sorpresa..."
    call BlinkXPS3 ("c21s001_015" , "d") from _call_BlinkXPS3_2
    dap "Pero después de una hora esperándote... mejor nos vamos..."
    mc "Chicas, tenía que llevar a [mad.nick]..."
    if kia._var("route"):
        mc "Y al volver me he encontrado con [kia] abajo..."
    scene c21s001_020a with dissolve
    if mad._var("route") or kia._var("route"):
        emm "Es decir, tus otras novias antes que nosotras, ¿no?"
    else:
        emm "Es decir, el resto de las chicas antes que nosotras, ¿no?"
    eri "Esperábamos más de ti, [mc]."
    dap "Nos has decepcionado."
    mc "¡Pero si ni siquiera sabía que estabais aquí!"
    play sound ("music/DoorSlam.ogg")
    scene c21s001_020b with hpunch
    "*Blam*"
    mcp "(¡Son casi las 2:00 AM! Cuidado con la puerta o vais a despertar a alguien.)"
    eri "*A través de la puerta* *Susurrando* ¡[emm]! ¡Vas a despertar a [sai] y a [meg]!"
    emm "*A través de la puerta* *Susurrando* Lo siento... me he metido demasiado en mi papel. *Risita*"
    dap "*A través de la puerta* *Susurrando* Chicas, ¿creéis que se lo ha creído?"
    mcp "(En cinco minutos están de vuelta... como mucho cinco minutos. Voy a ir desnudándome.)"
    emm "*A través de la puerta* *Susurrando* ¡Por supuesto! En diez segundos abrirá la puerta para venir a buscarnos."
    eri "*A través de la puerta* *Susurrando* No estoy segura. Ya han pasado diez segundos. Creo que sabe que estábamos de broma."
    dap "*A través de la puerta* *Susurrando* Eso nos pasa por hacer caso a los planes de [emm]. Ya os he dicho que era un plan de mierda. Debe estar muy cansado."
    emm "*A través de la puerta* *Susurrando* ¡Hey! El plan era bueno... ¿Habéis visto la cara que ha puesto?"
    dap "*A través de la puerta* *Susurrando* Imaginaos que decide darnos tiempo para que se nos pase el \"enfado\". Sería muy típico de él."
    emm "*A través de la puerta* *Susurrando* ¿Volvemos?"
    eri "*A través de la puerta* *Susurrando* Vamos antes de que se duerma."
    scene c21s001_020c with hpunch
    mc "Hola de nuevo, chicas. *Risa*"
    call BlinkXPS3 ("c21s001_025" , "d") from _call_BlinkXPS3_3
    emm "¿Sabías que íbamos a volver?"
    mc "¡Por supuesto! Dudo que hayáis venido vestidas así todo el camino atravesando la planta de las estudiantes."
    mc "Y dudo que fuerais a volver a vuestras habitaciones así."
    call BlinkXPS3 ("c21s001_030" , "d") from _call_BlinkXPS3_4
    eri "Es cierto, no habíamos contado con eso. Las batas están en el armario."
    mc "Además, creo que han escuchado vuestros susurros desde San Francisco. *Risa*"
    call BlinkXPS3 ("c21s001_035" , "d") from _call_BlinkXPS3_5
    dap "¡No hablábamos tan alto! Y si nos escuchabas, ¿por qué no has salido a buscarnos?"
    mc "Me estaba preparando para cuando volvierais. *Risa*"
    call BlinkXPS3 ("c21s001_040" , "d") from _call_BlinkXPS3_6
    eri "Y no nos has dejado abrir nuestro regalo como castigo, ¿no? *Risa*"
    mc "Nunca os castigaría por intentar hacer una broma. Ni por ninguna otra cosa, para ser sincero. Tan solo os he ahorrado tiempo. *Risa*"
    call BlinkXPS3 ("c21s001_045" , "d") from _call_BlinkXPS3_7
    dap "Sobre el papel, lo de plantarnos las tres en tu habitación parecía una buena idea, pero ahora no sé por dónde empezar..."
    mc "¿Qué tal si venís aquí y vamos descubriéndolo?"
    mc "Me ha sorprendido un poco veros aquí, pero es casi un sueño hecho realidad."
    if not sca._var("rejectedBeagan"):
        call BlinkXPS3 ("c21s001_050" , "d") from _call_BlinkXPS3_8
        dap "Después de lo que ha pasado en la partida de DnD... tú ponías caras, pero nosotras nos podíamos imaginar..."
        if not mc._var("rejectedAeliaPaula"):
            dap "Al menos en mi cabeza, el trío con Aelia, Vilfredo, y Paula ha sido super caliente."
        mc "Os entiendo. A mí me ha pasado lo mismo."
    else:
        call BlinkXPS3 ("c21s001_050" , "d") from _call_BlinkXPS3_9
        dap "Después de lo que ha pasado en la partida de DnD... de haber rechazado a Beagan..."
        dap "Hemos pensado que si no lo hubieras hecho, quizás hubiera acabado con las cuatro en la cama de Vilfredo."
    call BlinkXPS3 ("c21s001_055" , "d") from _call_BlinkXPS3_10
    emm "Para que después digan que DnD no sirve de nada. *Risa*"
    emm "Cuando te has ido a llevar a [mad.nick], casi nos hemos peleado por quién venía a verte. *Risita*"
    call BlinkXPS3 ("c21s001_060" , "d") from _call_BlinkXPS3_11
    eri "Si no hubiera sido por la partida, lo hubiéramos echado a suertes, pero después de jugar... hemos decidido venir las tres."
    if sca._var("route"):
        mc "No quiero sonar desagradecido o avaricioso, pero ¿[sca] no se ha querido unir?"
        call BlinkXPS3 ("c21s001_065a" , "d") from _call_BlinkXPS3_12
        dap "Se lo hemos propuesto, pero ha dicho que era nuestro cumpleaños..."
        if mc._var("edmundsStory"):
            dap "Y que quiere mantener las distancias hasta el martes."
            call BlinkXPS3 ("c21s001_070" , "d") from _call_BlinkXPS3_13
            emm "No lo he entendido. ¿Qué pasa el martes?"
            mcp "(Que llegan los resultados del test de ADN.)"
        else:
            call BlinkXPS3 ("c21s001_070" , "d") from _call_BlinkXPS3_14
            emm "Pero ya ha pasado la medianoche, ya ha acabado el cumpleaños."
    else:
        call BlinkXPS3 ("c21s001_065b" , "d") from _call_BlinkXPS3_15
        dap "Sexo de cumpleaños, y esas cosas. *Risita*"
        call BlinkXPS3 ("c21s001_070" , "d") from _call_BlinkXPS3_16
        emm "Pero ya ha pasado la medianoche, ya ha acabado el cumpleaños."
    call BlinkXPS3 ("c21s001_075" , "d") from _call_BlinkXPS3_17
    eri "Hoy, aunque sea lunes, todavía es nuestro cumpleaños, al menos el de [dap] y el mío."
    call BlinkXPS3 ("c21s001_080" , "d") from _call_BlinkXPS3_18
    emm "Lo siento, chicas, a veces me olvido... especialmente cuando vuestro cumpleaños es después del domingo de la fiesta."
    mc "No le des más vueltas, [emm]. Son cosas que pasan. Le dais tanta importancia a la fiesta del domingo que olvidáis cuándo son los cumpleaños oficiales."
    call BlinkXPS3 ("c21s001_085" , "d") from _call_BlinkXPS3_19
    stop music fadeout (1.5)
    eri "Sobre eso... sabes que me han encantado los pendientes, pero quiero mi regalo de cumpleaños de verdad."
    play music ("music/Sexy-Background-Music.ogg")
    mc "*Risa* No sé a lo que te refieres... pero veo que no llevas los pendientes."
    scene c21s001_090pv
    show c21s001_090v
    pause (2.03)
    scene c21s001_090dv
    eri "No estoy acostumbrada a llevarlos aún. Después de cambiarme me los he quitado."
    emm "¡Ve a por él, [eri]!"
    "Después de un largo día, los ojos te pican un poco y las luces te molestan. Esperas que no vaya a ser un problema para disfrutar de la noche."
    scene c21s001_085d with dissolve
    hide c21s001_090v
    eri "Y en cuanto a mi regalo, me refiero a esto..."
    scene c21s001_095pv with dissolve
    show c21s001_095v
    "[eri] se sienta a horcajadas en tu regazo y empieza un maravilloso beso."
    "El tiempo de los besos a escondidas ha pasado después de la Gran Revelación y los dos os sentís liberados de la presión de mantener el secreto."
    "Vuestros labios se rozan, vuestras lenguas se entrelazan, vuestros alientos se entremezclan."
    call BlinkXPS3("c21s001_260" , "d") from _call_BlinkXPS3_20
    hide c21s001_095v
    emm "Nosotras también queremos nuestra ración de [mc]."
    call BlinkXPS3("c21s001_255" , "d") from _call_BlinkXPS3_21
    dap "No seas impaciente, [emm]. Tenemos toda la noche para compartir a [mc]."
    call BlinkXPS3("c21s001_265" , "d") from _call_BlinkXPS3_22
    eri "Todo vuestro, al menos durante un rato. *Risa* Voy a querer más."
    scene c21s001_270a with dissolve
    "[emm] te tumba en la cama y empieza un delicioso beso"
    scene c21s001_270b with dissolve
    "Al que no tarda en unirse [dap]."
    scene c21s001_270An with dissolve
    "Ambas se van turnando, en un baile casi sincronizado, por una vez sin discutir entre ellas."
    "Un baile complicado donde sus cabezas están a punto de chocar más de una vez entre ellas."
    call BlinkXPS3("c21s001_275" , "d") from _call_BlinkXPS3_23
    if persistent.family:
        "Puedes notar cómo [eri] no se queda inactiva mientras su hermana y su prima te besan."
    else:
        "Puedes notar cómo [eri] no se queda inactiva mientras las otras dos mujeres te besan."
    eri "Tu pierna me molesta, [emm]. Creo que vuestros besos lo han dejado preparado para nosotras."
    emm "Ya estaba así cuando te has levantado de su regazo. *Risita*"
    dap "*Risa* Para ser la que no quería sexo hace tres semanas, eres la primera que acaba con la polla de [mc] en la mano."
    scene c21s001_100pv with dissolve
    show c21s001_100v
    "[eri] empieza a masturbarte lentamente mientras las otras dos mujeres mueven su atención de tus labios a tu polla."
    eri "*Risa* No creo que nunca me canse de besarle, pero lo estabais monopolizando."
    "Tus manos recorren los cuerpos de [emm] y [dap] mientras la de [eri] manejan a Mjolnir."
    emm "*Risa* Y has decidido que Mjolnir estaba demasiado solo... "
    "La noche empieza bien si empieza con risas. Es la primera vez que estás con tres mujeres y la primera vez que ellas están juntas."
    dap "*Risa* Tan solo me pregunto si será capaz de aguantar hasta que las tres tengamos nuestra ración, como diría [emm]... por si acaso, no le des mucha caña, [eri]."
    "Esperas que sí. Aunque estas tres chicas parecen hambrientas."
    scene c21s001_105pv with dissolve
    hide c21s001_100v
    show c21s001_105v
    "El tacto del guante de [eri] recorriendo tu astil y tu glande hace que se sienta muy diferente de otras ocasiones."
    dap "Nunca dejará de sorprenderme lo grande que es..."
    "Y a ti nunca dejará de gustarte que lo comenten. Siempre habrá quien piense que tu tamaño es exagerado. Por suerte tus chicas no piensan así."
    emm "Te podrías dedicar al porno y hacerte millonario. *Risa*"
    "Una vez te lo planteaste, en tu tercer año de universidad, cuando te propusieron participar en una película hecha por estudiantes."
    mc "No creo que fuera capaz de hacerlo. Follar por dinero le quitaría la mayor parte de la diversión, ¿no?"
    "Desechaste la idea un segundo después de que entrara en tu mente. Conociste a [sai] dos días después."
    eri "Además, [emm], ¿estás segura de que querrías que se follase a otras mujeres?"
    call BlinkXPS3("c21s001_280" , "d") from _call_BlinkXPS3_24
    hide c21s001_105v
    "[emm] da un respingo perceptible. Algún día aprenderá a pensar antes de hablar."
    emm "¿Qué? ¡No!"
    call BlinkXPS3("c21s001_285" , "d") from _call_BlinkXPS3_25
    emm "¡Olvida lo que te he dicho! ¡Sólo te permitimos acostarte con gente de la familia! Y eso incluye a las chicas..."
    "Hoy no va a ser ese día."
    mc "OK, olvidado..."
    scene c21s001_110pv with dissolve
    hide c21s001_105v
    show c21s001_110v
    "Sabes que alguna de ellas no va a olvidarlo y a perder la oportunidad de aprovechar el desliz de [emm]."
    dap "¿También a la abuela o a Tía [bet]? *Risa* Las podemos invitar la próxima vez."
    "Lo sabías. [dap] era la mejor candidata para hacerlo."
    emm "*Risa* No puedo imaginarme a Tía [bet] teniendo vida sexual, pero si les hiciera felices..."
    "¡Cómo ha cambiado [emm] en tres semanas!"
    "Ninguna de ellas sabe cómo actuar en esta situación y usan el humor para esconder sus miedos e inseguridades."
    eri "*Risa* Chicas, dejad de decir tonterías o voy a empezar a imaginarme cosas raras."
    "Debes recordar que todas ellas eran vírgenes hace tan solo unos días."
    eri "¡Tenemos a nuestro hombre delante y estáis pensando en con quién se puede o no se puede acostar! ¡Cuckqueans!"
    call BlinkXPS3("c21s001_290" , "d") from _call_BlinkXPS3_26
    "Se levanta como impulsada por un muelle, dejando tu polla huérfana de caricias."
    eri "No sé vosotras, pero a mí me da la sensación de que llevamos demasiada ropa todavía..."
    mc "Tienes razón. *Risa* Soy el único que no tiene nada que quitarse."
    scene c21s001_295a with dissolve
    "[dap] y [emm] se levantan de un salto. Tienes que revisar los muelles de la cama."
    dap "Ayúdame a quitarme esto..."
    emm "Yo me voy a dejar puesto el corsé, es tan sexy..."
    call BlinkXPS3("c21s001_300" , "d") from _call_BlinkXPS3_27
    eri "¿Me dejas tumbarme? Estoy deseando repetir lo de la sauna..."
    mc "*Risa* ¿Tanto sueño tienes?"
    call BlinkXPS3("c21s001_305" , "d") from _call_BlinkXPS3_28
    eri "*Risa* Esta vez no me voy a dormir, no te preocupes."
    mc "Cuento con ello. Túmbate."
    call BlinkXPS3("c21s001_310" , "f") from _call_BlinkXPS3_29
    eri "¿Así va bien, mi vida?"
    mc "No podrías estar más perfecta."
    scene c21s001_120pv with dissolve
    hide c21s001_110v
    show c21s001_120v
    "Hundes tu cara entre sus piernas mientras empiezas a lamer sus zonas más sensibles."
    eri "¡Oh, sí! *Gemido* ¡Es mejor de lo que recordaba!"
    "Su raja está húmeda debido a la anticipación y a las conversaciones sobre tener sexo con otras mujeres."
    eri "*Jadeo* Sigue así... Es increíble..."
    "Su cuerpo sigue cada movimiento de tu cabeza. Tu cabeza sigue la presión de su mano."
    scene c21s001_295b with dissolve
    emm "No os imagináis lo sexis que estáis juntos..."
    if persistent.family:
        dap "Ni siquiera me imaginaba que ver a mi primo comiéndose a mi hermana me iba a poner cachonda."
    else:
        dap "Ni siquiera me imaginaba que ver a [mc] comiéndose a [eri] me iba a poner cachonda."
    scene c21s001_115pv with dissolve
    hide c21s001_120v
    show c21s001_115v
    "Casi no las oyes. Tus sentidos son invadidos por el aroma que emana de [eri], por su sabor, por sus gemidos..."
    eri "¡Oh, Dios mío! *Gemido* ¡Me encanta!"
    "El tacto de tu húmeda lengua mientras recorres su húmedo coño centra toda tu atención."
    eri "*Jadeo* Esto es casi tan bueno como el sexo de verdad..."
    "Solo casi tan bueno..."
    scene c21s001_315b with dissolve:
        xalign 0.4
        yalign 0.28
        zoom 0.5
        linear 2.0 zoom 1.1
    "Estás tan concentrado que no ves el movimiento de [dap] al colocarse entre tus piernas y engullir tu polla."
    dap "Mmmmmm..."
    scene c21s001_125pv
    hide c21s001_115v
    show c21s001_125v
    if persistent.family:
        "Trabajo en cadena, tú das placer a [eri] mientras su hermana te da placer a ti."
    else:
        "Trabajo en cadena, tú das placer a [eri] mientras [dap] te da placer a ti."
    dap "*Sonidos ahogados*"
    "Las lecciones han dado sus frutos y [dap] se está convirtiendo en una experta. Puedes notar el fondo de su garganta al final de cada recorrido."
    eri "*Gemido* Sigue así... [dap]... lo haces saltar de una forma que me está volviendo loca..."
    if persistent.family:
        "Es el sueño de muchos hombres, estar con dos gemelas a la vez, por muy diferentes que sean. Solo falta que [emm] se una."
    else:
        "Es el sueño que muchos hombres no saben que tienen, estar con dos clones a la vez, por muy diferentes que sean. Solo falta que [emm] se una."
    scene c21s001_295c with dissolve
    emm "Hacedme un hueco..."
    scene c21s001_130pv
    hide c21s001_125v
    "[emm] aparta la almohada sobre la que [eri] tenía apoyada la espalda y la reemplaza con su cuerpo."
    emm "Me ponéis cachonda solo con veros... con imaginar que la siguiente puedo ser yo..."
    "Durante el cambio de posición, ni [dap] ni tú permitís que vuestras bocas estén quietas más de un segundo."
    show c21s001_130v
    "Sigues chupando y lamiendo mientras eres chupado y lamido. Los gemidos se entremezclan en tus oídos."
    eri "*Jadeo* ¡Me encanta! *Gemido* Me siento tan... en familia..."
    "No crees que las familia \"normales\" hagan esto muy a menudo. Ellos se lo pierden."
    emm "Lo teníamos que haber grabado... Nuestra primera vez todos juntos."
    "[emm] sigue sorprendiéndote con sus ideas locas. No es un video que quisieras que se filtrara online."
    dap "*Gemido afirmativo*"
    mcp "(Mal momento para estar de acuerdo con [emm], [dap]. *Risa mental*)"
    scene c21s001_320An with hpunch
    hide c21s001_130v
    emm "Creo que es el momento de quitar esto."
    eri "¡[emm]!"
    mcp "(Estoy totalmente de acuerdo.)"
    if persistent.lesbian:
        scene c21s001_320c with dissolve
        if persistent.family:
            emm "Tienes unas tetas fantásticas, prima."
        else:
            emm "Tienes unas tetas fantásticas, [eri]."
        eri "*Gemido* Gracias... se sentían solas sin nadie que les prestara atención."
        call BlinkXPS3("c21s001_325" , "d") from _call_BlinkXPS3_30
        dap "No sabía que te gustaran las chicas, [emm]."
        call BlinkXPS3("c21s001_330" , "d") from _call_BlinkXPS3_31
        emm "No me gustan. Me gustáis vosotras. Y las personas a las que quiero."
        call BlinkXPS3("c21s001_335" , "d") from _call_BlinkXPS3_32
        dap "Pues de las mías olvídate. *Risa* Son territorio [mc]."
        scene c21s001_135pv
        show c21s001_135v
        "Continúas lamiendo el coño de [eri] mientras la boca de [dap] te acerca poco a poco a tu propio orgasmo."
        eri "*Gemido* ¡Sí! *Jadeo* ¡Tengo los pezones tan sensibles como el clítoris! *Gemido* ¡Qué bueno eres con la lengua!"
        "Sabes que está a punto de llegar, lo puedes notar en los movimientos de su cuerpo."
        emm "Córrete para nosotros, [eri]."
        "Lo tórrido de la situación ayuda a que [eri] se haya puesto más cachonda aún."
        dap "*Gemido afirmativo*"
        call OrgasmXS3 ("c21s001_340a") from _call_OrgasmXS3
        hide c21s001_135v
        "[eri] explota en tu boca, llenando tus sentidos con su fuerte aroma y su sabor."
        eri "*GEMIDO* ¡SÍ! *JADEO* ¡Justo así!"
        "Su cuerpo parece derretirse bajo tus dedos, bajo tu lengua, después de toda la tensión acumulada."
        if persistent.family:
            "[emm] estruja el pecho de su prima mientras oleadas de orgasmos la recorren."
            emm "Así, Cucaracha, disfruta de tus primos dándote placer."
        else:
            "[emm] estruja el pecho de [eri] mientras oleadas de orgasmos la recorren."
            emm "Así, Cucaracha, disfruta de tu familia dándote placer."
    else:
        scene c21s001_210pv
        show c21s001_210v
        "Continúas lamiendo el coño de [eri] mientras la boca de [dap] te acerca poco a poco a tu propio orgasmo."
        eri "*Gemido* ¡Sí! *Jadeo* ¡Qué bueno eres con la lengua!"
        "Sabes que está a punto de llegar, lo puedes notar en los movimientos de su cuerpo."
        emm "Córrete para nosotros, [eri]."
        "Lo tórrido de la situación ayuda a que [eri] se haya puesto más cachonda aún."
        dap "*Gemido afirmativo*"
        call OrgasmXS3 ("c21s001_340b") from _call_OrgasmXS3_1
        hide c21s001_210v
        "[eri] explota en tu boca, llenando tus sentidos con su fuerte aroma y su sabor."
        eri "*GEMIDO* ¡SÍ! *JADEO* ¡Justo así!"
        "Su cuerpo parece derretirse bajo tus dedos, bajo tu lengua, después de toda la tensión acumulada."
        if persistent.family:
            emm "Así, Cucaracha, disfruta de la lengua tu primo dándote placer."
        else:
            emm "Así, Cucaracha, disfruta de la lengua de [mc] dándote placer."
    mcp "(Cucaracha parece que se ha convertido en el mote cariñoso...)"
    call BlinkXPS3("c21s001_345" , "d") from _call_BlinkXPS3_33
    emm "[dap], para, por favor."
    mcp "(¿Qué?)"
    "La petición de [emm] te sorprende, tanto por el contenido como por la forma."
    call BlinkXPS3("c21s001_350" , "d") from _call_BlinkXPS3_34
    dap "¿Qué? ¿Por qué? Creo que estaba a punto..."
    "No eres el único sorprendido. No estabas a punto de correrte, pero te estabas acercando rápidamente."
    call BlinkXPS3("c21s001_355" , "d") from _call_BlinkXPS3_35
    if persistent.family:
        emm "¿No quieres ver cómo [mc] le hace el amor a tu hermana?"
    else:
        emm "¿No quieres ver cómo [mc] le hace el amor a [eri]?"
    emm "Yo estoy deseando verlo..."
    "A veces adoras a esta chica. Casi siempre."
    call BlinkXPS3("c21s001_360" , "d") from _call_BlinkXPS3_36
    dap "¡Sí!"
    call BlinkXPS3("c21s001_365" , "d") from _call_BlinkXPS3_37
    eri "Chicas... acabo de tener uno de los mayores orgasmos de mi vida... Todavía lo noto..."
    eri "¿Puedo descansar un poco mientras se dedica a vosotras?"
    call BlinkXPS3("c21s001_370" , "d") from _call_BlinkXPS3_38
    dap "Ahora es cuando estás más sensible. Es el momento de que [mc] te haga el amor."
    call BlinkXPS3("c21s001_375" , "d") from _call_BlinkXPS3_39
    emm "Nosotras podemos esperar. Veros me está poniendo cachondísima..."
    call BlinkXPS3("c21s001_380" , "d") from _call_BlinkXPS3_40
    eri "Nunca voy a decir que no a Mjolnir..."
    mc "Cuando estés lista."
    eri "Ya... aún estoy notando los últimos coletazos del orgasmo..."
    scene c21s001_215pv with fade
    show c21s001_215v
    pause (0.43)
    scene c21s001_215dv
    hide c21s001_215v
    "Cambias de posición y penetras a [eri] en una rápida embestida."
    eri "*JADEO* ¡Ooof!"
    "Está húmeda y caliente. Su orgasmo anterior hace que entres como si de un traje a medida se tratara."
    call BlinkXPS3("c21s001_385" , "d") from _call_BlinkXPS3_41
    mc "¿Estás bien?"
    eri "*Gemido* No se puede estar mejor... Casi me vuelvo a correr..."
    call BlinkXPS3("c21s001_390" , "d") from _call_BlinkXPS3_42
    dap "Te lo he dicho, pero nunca me hacéis caso..."
    call BlinkXPS3("c21s001_395" , "d") from _call_BlinkXPS3_43
    emm "Empieza a bombear, no le dejes perder esa sensación."
    scene c21s001_140pv with dissolve
    show c21s001_140v
    "Empiezas a embestir el coño de [eri] con tus caderas mientras las otras dos chicas os observan."
    eri "*Gemido* ¡Oh, sí! *Jadeo* [dap] tenía razón... *Gemido* Me voy a volver a correr..."
    "Al cabo de unas pocas embestidas, puedes notar como el cuerpo de [eri] empieza a tensarse."
    dap "*Gemido* Te lo he dicho... *Gemido*"
    "Nunca puede perder la ocasión de dejar claro cuando tiene razón. Esta vez, entre gemidos mientras se masturba, suena menos pedante."
    emm "*Jadeo* Sois increíbles... *Gemido* Me pregunto si cuando me folles a mí se verá igual... *Jadeo* Teníamos que haberlo grabado..."
    "Quizás la próxima vez..."
    scene c21s001_145pv with dissolve
    hide c21s001_140v
    show c21s001_145v
    dap "*Gemido* No tenías que haberle dicho a [eva] que retirara las cámaras. *Jadeo*"
    "Prefieres no tener público... al menos más allá de [emm] y [dap]."
    eri "*Jadeo* ¡Estoy a punto de llegar! *GEMIDO* ¡Es increíble!"
    "Por suerte en esta posición eres tú quien lleva el ritmo. El cuerpo desmadejado de [eri] no podría hacerlo ahora mismo."
    emm "*GEMIDO* ¡Yo también! *JADEO* ¡Me ponéis cachondísima!"
    call OrgasmXS3 ("c21s001_400") from _call_OrgasmXS3_2
    "La primera en llegar al orgasmo es [eri]. Su cuerpo se tensa bajo el tuyo antes de liberarse como un muelle."
    eri "*GEMIDO* ¡Oooff! *JADEO* ¡No pares!"
    "Puedes notar como tu clímax se está acercando. [dap] ha hecho un gran trabajo anteriormente. Eres un maestro orgulloso de su pupila."
    eri "*JADEO* ¡Vienen en oleadas!"
    "Empiezas a notar como su coño exprime toda la longitud de tu polla, intentando no dejarte ir."
    call OrgasmXS3 ("c21s001_405") from _call_OrgasmXS3_3
    hide c21s001_145v
    "[emm] se corre pocos segundos después."
    emm "*JADEO* ¡SÍ! *GEMIDO* ¡Sois la mejor porno que he visto nunca!"
    if mar._var("route"):
        "Sabías que [emm] se ponía cachonda viéndote follar con otras mujeres. No sabías que tan rápido."
    else:
        "[emm] lleva un rato diciendo que se ponía cachonda viéndote follar con otras mujeres. No sabías que tan rápido."
    if persistent.lesbian:
        emm "Déjame ayudar..."
        scene c21s001_150pv with dissolve
        show c21s001_150v
        "Sin dejar de masturbarse, [emm] empieza a comerle los pezones a [eri], que sigue acumulando orgasmo tras orgasmo."
    else:
        scene c21s001_140pv with dissolve
        show c21s001_140v
        "[emm] sigue masturbándose mientras os observa, sin perder el ritmo ni un momento pese a su orgasmo."
    eri "*Gemido* Estoy empezando a entumecerme... *JADEO* Bendito entumecimiento... *GEMIDO* ¡Sigue así!"
    "Sus paredes vaginales se cierran sobre tu polla oleada tras oleada, intentando ordeñar una leche que aún no ha llegado."
    dap "*JADEO* Yo también estoy a punto de correrme... *GEMIDO*"
    "Tú también estás muy cerca."
    call OrgasmXS3 ("c21s001_410") from _call_OrgasmXS3_4
    if persistent.family:
        "El orgasmo de [dap] no tarda en llegar entre los ruidos húmedos que producís su hermana y tú."
    else:
        "El orgasmo de [dap] no tarda en llegar entre los ruidos húmedos que producís [eri] y tú."
    dap "*GEMIDO* ¡Sí! *JADEO* ¡OH, SÍ!"
    if persistent.lesbian:
        scene c21s001_150pv with dissolve
        show c21s001_150v
    else:
        scene c21s001_145pv with dissolve
        show c21s001_145v
    "Continúas embistiendo el coño de [eri], cada vez con más velocidad, notando como tu clímax se acerca a pasos agigantados."
    eri "*GEMIDO* Córrete dentro. *JADEO*"
    if persistent.lesbian:
        dap "*Jadeo* Sí, hazlo dentro. *Gemido* Quiero ver cómo te corres dentro de mi hermana."
    else:
        dap "*Jadeo* Sí, hazlo dentro. *Gemido* Quiero ver cómo te corres dentro de [eri]."
    emm "*GEMIDO* *Sonidos ininteligibles*"
    if eri._var("pregnant"):
        $ eri._var("pregnancyDiscovered", True)
    if not eri._var("pregnant") and persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[eri] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                if not WhatIf4S:
                    $ eri._var("pregnant", True)
                play sound ("music/OldMusicBox5.ogg")
        $ resetWalkthrough ()
    call OrgasmXS3 ("c21s001_415") from _call_OrgasmXS3_5
    hide c21s001_150v
    hide c21s001_145v
    "Cuando tu orgasmo llega por fin, no puedes evitar cumplir sus deseos."
    mc "¡Mpffft!"
    "Después de toda la excitación previa, descargas una enorme cantidad de leche en el interior de [eri] mientras sigues bombeando durante un rato."
    eri "*Gemido* ¡No salgas aún! *JADEO* Siguen llegando más orgasmos."
    stop music fadeout (1.5)
    "Puedes notar como su coño, ahora sí, ordeña las últimas gotas de semen de tu polla."
    play music ("music/romantic-day.ogg")
    call BlinkXPS3 ("c21s001_420" , "f") from _call_BlinkXPS3_44
    "Al cabo de unos minutos, cuando el cuerpo de [eri] se ha relajado, sales de su interior y te tumbas a su lado."
    mc "¿Bien?"
    eri "Mejor que bien."
    eri "No me podía imaginar que tener a estas dos dirigiendo la película sería tan tórrido."
    call BlinkXPS3 ("c21s001_425" , "d") from _call_BlinkXPS3_45
    dap "*Risa* Ahora podrás dirigirla tú. Es nuestro turno."
    dap "Al menos cuando [mc] se recupere."
    call BlinkXPS3 ("c21s001_430" , "d") from _call_BlinkXPS3_46
    emm "Deberías limpiar a Mjolnir. Así seguro que se recupera antes."
    $ Aux = False
    if persistent.lesbian:
        call BlinkXPS3 ("c21s001_435a" , "d") from _call_BlinkXPS3_47
        emm "¿Me permites limpiarte, [eri]?"
        scene c21s001_435d with hpunch
        eri "¿Qué?"
        mc "¿Estás segura, [emm]?"
        call BlinkXPS3 ("c21s001_435b" , "d") from _call_BlinkXPS3_48
        emm "No es que quiera repetir lo que te ha hecho [mc]. *Risa* Dudo que fuera tan buena como él."
        emm "Y te recuerdo que sé cómo de bueno es..."
        call BlinkXPS3 ("c21s001_440" , "d") from _call_BlinkXPS3_49
        emm "Pero sería un desperdicio si empieza a chorrear todo eso."
        emm "¿Dejarías que una de tus novias limpiara a otra mientras la tercera prepara a Mjolnir para el siguiente asalto?"
        if persistent.walkthrough:
            $ wt1 = _("[emm] limpia tu corrida del coño de [eri].")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Me parece bien si a [eri] le parece bien." (wt = wt1):
                $ Aux = True
                call BlinkXPS3 ("c21s001_445" , "d") from _call_BlinkXPS3_50
                stop music fadeout (1.5)
                eri "Si a ti no te importa, a mí tampoco. [emm] parece ansiosa. *Risita*"
            "Me parece bien si a [eri] le parece bien.\n Pero no creo que [eri] quiera." (wt = wt2):
                $ Aux = False
                scene c21s001_445d with dissolve
                stop music fadeout (1.5)
                eri "[mc] tiene razón. Mi cuerpo es territorio [mc] desde que plantó el poste de su bandera. *Risita*"
        $ resetWalkthrough ()
    else:
        stop music fadeout (1.5)
    if Aux:
        scene c21s001_450a with fade
        "[emm] en seguida se arrodilla entre las piernas de [eri]."
        play music ("music/SexyLoungeMusic.ogg")
        scene c21s001_220pv with fade
        "[dap] te sorprende subiéndose a horcajadas encima de tu cara antes de meterse tu polla en la boca."
        mc "Esto no me lo esperaba. *Risa* ¿Es algún tipo de indirecta?"
        call BlinkXPS3 ("c21s001_450a" , "d") from _call_BlinkXPS3_51
        dap "*Risa* ¿Tú que crees?"
        scene c21s001_450b with dissolve
        pause (1.2)
        call BlinkXPS3 ("c21s001_450a" , "d") from _call_BlinkXPS3_52
        mc "*Risa* Que no soy el único al que hay que limpiar."
        dap "Pues eso... empieza ya. *Risa* Como diría Tía [mar], eso no se va a limpiar solo."
        scene c21s001_220pv with fade
        show c21s001_220v
        "[dap] empieza a hacer una limpieza profunda de Mjolnir mientras tú lames los fluidos de su anterior orgasmo. Vuelves a sentirte orgulloso de tu alumna."
        dap "*Gemido*"
        "Mientras tanto [emm] lame la mezcla de tu semen con los fluidos de [eri] directamente de su interior."
        emm "*Jadeo* *Slurp*"
        "Es casi reciclaje en familia."
        eri "*Gemido* Creo que ya estoy limpia, [emm], deberías parar..."
        call BlinkXPS3 ("c21s001_455" , "d") from _call_BlinkXPS3_53
        emm "Creo que sí... me estoy poniendo cachonda y necesito que alguien se ocupe de mí ahí abajo."
        "El de [emm] es el único coño al que no le has dedicado ninguna atención."
        emm "Supongo que no estás interesada, ¿no?"
        call BlinkXPS3 ("c21s001_460" , "d") from _call_BlinkXPS3_54
    else:
        scene c21s001_225pv with fade
        "[dap] te sorprende subiéndose a horcajadas encima de tu cara antes de meterse tu polla en la boca."
        play music ("music/SexyLoungeMusic.ogg")
        mc "Esto no me lo esperaba. *Risa* ¿Es algún tipo de indirecta?"
        call BlinkXPS3 ("c21s001_450a" , "d") from _call_BlinkXPS3_55
        dap "*Risa* ¿Tú qué crees?"
        scene c21s001_450b with dissolve
        pause (0.8)
        call BlinkXPS3 ("c21s001_450a" , "d") from _call_BlinkXPS3_56
        mc "*Risa* Que no soy el único al que hay que limpiar."
        dap "Pues eso... empieza ya. *Risa* Como diría Tía [mar], eso no se va a limpiar solo."
        scene c21s001_225pv with fade
        show c21s001_225v
        "[dap] empieza a hacer una limpieza profunda de Mjolnir mientras tú lames los fluidos de su anterior orgasmo."
        dap "*Gemido*"
        "Las reverberaciones de su gemido en tu glande provocan que cualquier signo de flacidez desaparezca de tu polla."
        if persistent.family:
            eri "¡Mi hermana es una gran mamadora! Yo no sería capaz de metérmela tan al fondo."
        else:
            eri "¡[dap] es una gran mamadora! Yo no sería capaz de metérmela tan al fondo."
        "Ciertamente no puedes estar más orgulloso de tu alumna. Está haciendo un trabajo fantástico."
        emm "A mí me está poniendo cachondísima verlos. Necesito que alguien se ocupe de mí ahí abajo."
        "El de [emm] es el único coño al que no le has dedicado ninguna atención."
    eri "Lo siento, [emm]. No es lo mío. Seguro que lo haría fatal."
    call BlinkXPS3 ("c21s001_465" , "d") from _call_BlinkXPS3_57
    hide c21s001_225v
    hide c21s001_220v
    dap "*Gemido* Conmigo tampoco cuentes, pero tengo una idea..."
    scene c21s001_155pv with fade
    show c21s001_155v
    "Después de que [dap] os de órdenes de cómo poneros empieza la locura. Puedes dar placer a tus tres chicas simultáneamente."
    "[dap] cabalga tu polla con maestría. Desde vuestra primera vez, en la bañera del hotel, demostró que le gustaba estar arriba."
    dap "*GEMIDO* ¡Sí! *JADEO* ¡Cómo echaba de menos esto!"
    "Tu lengua se dedica a dar un merecido placer a [emm]. Te extraña que no haya discutido con [dap] sobre quién cabalgaba a Mjolnir primero."
    emm "*JADEO* ¡Tienes razón! *GEMIDO* No me cansaré nunca de esta lengua."
    "Tus dedos entran y salen del coño de [eri] mientras gime en la almohada de al lado."
    if Aux:
        "Aún puedes notar la humedad de la saliva de [emm]."
    eri "*GEMIDO* No me vais a dejar descansar, ¿verdad?"
    "Si no tuvieras la boca ocupada, responderías que podrá descansar cuando te dejen descansar a ti."
    scene c21s001_160pv with fade
    hide c21s001_155v
    show c21s001_160v
    eri "*Gemido* [emm] tenía razón. Veros a los tres... *JADEO* mientras me masturbas... *Gemido* es increíble."
    "Su empapado coño te indica que lo está disfrutando tanto como las otras dos mujeres."
    emm "*Jadeo* No es el momento de decir que siempre tengo razón... *GEMIDO* Pero la tengo."
    "[emm] también está empapada. Tu saliva y sus fluidos se juntan en una maravillosa humedad."
    dap "*GEMIDO* Callaos y disfrutad. *Jadeo* No sabemos cuándo lo volveremos a tener para nosotras solas."
    "Tras esas palabras notas como [emm] acelera el ritmo de sus caderas sobre tu boca, como si tuviera prisa en llegar."
    emm "*Jadeo* Estoy a punto de correrme..."
    call OrgasmXS3 ("c21s001_470") from _call_OrgasmXS3_6
    "Dicho y hecho. Al acabar la frase explota en tu boca."
    emm "*GEMIDO* ¡SÍ! *JADEO* ¡ALUCINANTE!"
    "Sigues chupando su empapado coño mientras masturbas a [eri] y [dap] te cabalga."
    scene c21s001_160pv with fade
    show c21s001_155v
    show c21s001_160v
    "Con movimientos cada vez más espasmódicos, [dap] sigue subiendo y bajando, empalada en tu astil."
    dap "*Gemido* Yo también estoy a punto..."
    "El cuerpo de [eri] te indica que ella también se está acercando a su orgasmo. Has perdido la cuenta de cuántos lleva desde que ha empezado todo."
    eri "*Jadeo* Yo no voy a poder aguantar mucho más... *Gemido*"
    "[emm] sigue corriéndose, orgasmo tras orgasmo, llenando tu boca con sus jugos."
    emm "*GEMIDO* ¡Ngghhh! *JADEO* ¡Ayeee! *GEMIDO*"
    if persistent.family:
        "Estás a punto de reírte por la facilidad de palabra de tu hermana mientras se corre."
    else:
        "Estás a punto de reírte por la facilidad de palabra de [emm] mientras se corre."
    call OrgasmXS3 ("c21s001_475") from _call_OrgasmXS3_7
    hide c21s001_160v
    if persistent.family:
        "Sus primas se unen al orgasmo familiar compartido, prácticamente a la vez."
    else:
        "Las otras dos mujeres se unen al orgasmo de [emm], prácticamente a la vez."
    dap "*GEMIDO* ¡OH, DIOS MÍO! *JADEO* ¡ME ENCANTA!"
    if persistent.family:
        "[dap] consigue el primero de sus orgasmos de esta ronda unos segundos antes que su hermana."
    else:
        "[dap] consigue el primero de sus orgasmos de esta ronda unos segundos antes que [eri]."
    "Sus paredes vaginales se cierran con fuerza sobre tu astil."
    call OrgasmXS3 ("c21s001_480") from _call_OrgasmXS3_8
    "[eri] explota unos segundos después, empapando tus dedos."
    eri "*JADEO* ¡Increíble! *Gemido* ¡Nunca me había corrido tantas veces!"
    "Las oleadas de placer vuelven a recorrer su cuerpo al mismo ritmo que sus espasmos."
    scene c21s001_155pv with dissolve
    show c21s001_155v
    "[dap] sigue cabalgando a Mjolnir como una experimentada valkiria pelirroja mientras su coño aprisiona tu polla en cada recorrido, con cada oleada."
    dap "*GEMIDO* ¡Córrete dentro!"
    if dap._var("pregnancyDiscovered"):
        dap "*JADEO* No me vas a dejar embarazada... *GEMIDO* otra vez..."
    "Teniendo a dos mujeres encima de ti, sería difícil que pudieras elegir otro lugar para hacerlo."
    emm "*GEMIDO* No pienses en eso. *JADEO* ¡Sigue chupando!"
    "Puedes notar cómo tu clímax se va acercando a una enorme velocidad. Quieres dar a tus chicas el máximo placer antes de correrte."
    eri "*JADEO* ¡No puedo más! *GEMIDO* Llevo mil orgasmos..."
    "Tu segundo de la noche llega unos segundos después."
    if not dap._var("pregnant") and persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[dap] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                if not WhatIf4S:
                    $ dap._var("pregnant", True)
                play sound ("music/OldMusicBox5.ogg")
        $ resetWalkthrough ()
    call DoubleOrgasmXS3 ("c21s001_485") from _call_DoubleOrgasmXS3
    hide c21s001_155v
    mc "¡Mpffft!"
    "Inundas el interior de [dap] con una copiosa corrida."
    dap "*JADEO* ¡Sí! ¡Dámela toda!"
    "Puedes notar como tu leche sale a borbotones mientras [dap] te ordeña hasta la última gota."
    eri "*Gemido* ¡Siguen llegando más orgasmos! *Jadeo* ¡Me voy a romper!"
    "Tus dedos saltan dentro de la húmeda raja de [eri] con cada movimiento de [dap], como el resto de tu cuerpo."
    emm "*JADEO* ¡Ughhh! *GEMIDO* ¡Ngyyhh!"
    "Los movimientos de tu lengua se vuelven erráticos, pero no por ello proporcionan menos placer a [emm]."
    scene c21s001_490a with fade
    stop music fadeout (1.5)
    "Poco después, todos os derrumbáis como muñecas desmadejadas. [dap], todavía con tu polla en su interior, se apoya en la espalda de [emm]."
    play music ("music/romantic-day.ogg")
    dap "¡Ufff! Ha sido increíble..."
    "[emm] se tiene que apoyar en la cabecera de la cama, sus piernas apenas la aguantan."
    emm "Estoy de acuerdo... no sé si es porque has mejorado con la lengua o es por el rato que llevo cachonda, pero ha sido el mejor cunnilingus que me has hecho."
    "El cuerpo de [eri], perdida toda tensión, reposa a tu lado."
    eri "Y ahora te toca recibir a Mjolnir. *Risita*"
    mc "Chicas, mi aguante tiene un límite... necesito cinco minutos."
    call BlinkXPS3 ("c21s001_495" , "d") from _call_BlinkXPS3_58
    dap "*Risa* Puede que tu aguante tenga un límite, pero Mjolnir no baja."
    mc "*Risa* Está muy a gusto dentro de ti."
    call BlinkXPS3 ("c21s001_500" , "d") from _call_BlinkXPS3_59
    eri "Déjame limpiarlo para [emm]."
    call BlinkXPS3 ("c21s001_505a" , "d") from _call_BlinkXPS3_60
    emm "¿Qué? Yo estoy agotada..."
    mc "*Risa* Todos sabemos de lo que te quejarías en los próximos meses si eres la única que no tiene sexo hoy, [emm]."
    call BlinkXPS3 ("c21s001_505b" , "d") from _call_BlinkXPS3_61
    emm "¡Eso no es cierto!"
    call BlinkXPS3 ("c21s001_510" , "d") from _call_BlinkXPS3_62
    eri "*Risa* Lo es y lo sabes."
    eri "*Imitando a [emm]* Fui la única que no folló aquella noche... Aún os odio por haberme dejado para la última."
    call BlinkXPS3 ("c21s001_515" , "d") from _call_BlinkXPS3_63
    dap "*Imitando a [emm]* Si hubiera podido tener sexo con él no se hubiera pasado dos semanas diciendo lo buenas que erais vosotras. *Risa*"
    mc "*Imitando a [emm]* Habría sabido quién es la mejor en la cama."
    call BlinkXPS3 ("c21s001_520" , "d") from _call_BlinkXPS3_64
    emm "¡Yo no hablo así! Nunca diría cosas como esas..."
    mc "*Risa* Nunca lo sabremos, [emm]. Y no te vamos a dar la oportunidad de quejarte."
    mc "Mjolnir está preparado para ti. ¿Vas a desaprovecharlo?"
    call BlinkXPS3 ("c21s001_525" , "d") from _call_BlinkXPS3_65
    emm "¡Ni por todo el oro del mundo! *Risa*"
    emm "Si mañana no puedo andar, será culpa vuestra."
    call BlinkXPS3 ("c21s001_530" , "d") from _call_BlinkXPS3_66
    stop music fadeout (1.5)
    eri "*Risa* Ya lo tienes limpio y reluciente. Esta vez me voy a quedar lejos de los dedos de [mc]. Yo sí que estoy agotada."
    play music ("music/SensualJazzMedium2.ogg")
    scene c21s001_170pv with fade
    show c21s001_170v
    "[emm] te cabalga tal como ha hecho [dap] con anterioridad. Ciertamente está agotada y tienes que ayudarle a marcar el ritmo con tus manos."
    emm "*GEMIDO* Casi me vuelvo a correr en cuanto has entrado."
    "[eri] cumple su palabra y se mantiene lejos de ti tras coger una almohada extra del armario."
    eri "*JADEO* A mí me ha pasado lo mismo... *GEMIDO* Que te penetren justo después de tener un orgasmo es alucinante."
    mcp "(¿Esos gemidos? ¿Me ha sustituido por las almohadas o se está tocando?)"
    "No puedes estar seguro, ya que la cabeza de [dap] te tapa la visión mientras te besa. No tienes queja sobre ello, obviamente."
    dap "*Ronroneo afirmativo* *Ronroneo exigente*"
    "Entiendes perfectamente los ronroneos de [dap], te está pidiendo que no olvides que puedes usar una de tus manos en ella."
    scene c21s001_175pv with fade
    hide c21s001_170v
    show c21s001_175v
    "Lo haces."
    dap "*JADEO DE SORPRESA* *Gemido*"
    "El gemido en tu boca te indica que has malinterpretado sus ronroneos. Y que a ella no le importa. Empieza a mover su culo de un lado a otro, intentando maximizar el contacto."
    if persistent.family:
        eri "*GEMIDO* ¡Joder! *JADEO* ¡Me encanta ver cómo masturbas a mi hermana mientras mi prima te folla!"
    else:
        eri "*GEMIDO* ¡Joder! *JADEO* ¡Me encanta ver cómo masturbas a [dap] mientras [emm] te folla!"
    "Una vez [emm] ha pillado el ritmo, es ella la que te está cabalgando salvajemente. Puedes hacer poco más que ayudarle con tu mano."
    emm "*JADEO* ¡Estoy a punto de correrme otra vez! *GEMIDO*"
    "Puedes notarlo en la punta de tus dedos y a lo largo de tu astil."
    call OrgasmXS3 ("c21s001_535") from _call_OrgasmXS3_9
    emm "*GEMIDO* ¡Por el amor de Dios! *JADEO* ¡ES ENORME!"
    "No sabes si se refiere a su orgasmo o a tu polla. Todos estáis muy sensibles a estas alturas y los orgasmos se suceden uno tras otro."
    "Las paredes vaginales de [emm] empiezan a aprisionar tu polla con fuerza, aumentando tu placer."
    call OrgasmXS3 ("c21s001_540") from _call_OrgasmXS3_10
    dap "*JADEO* ¡No puedo más! *GEMIDO* ¡Me encanta!"
    "[dap] explota en tu mano. A estas alturas cualquier roce significa un nuevo orgasmo para las chicas. Tú también estás sensible y notas tu clímax acercarse."
    call OrgasmXS3 ("c21s001_545") from _call_OrgasmXS3_11
    eri "*GEMIDO* ¡Oh, sí!"
    "Cualquier roce, incluso el de unas almohadas en el punto correcto. Casi te sientes celoso de esas almohadas."
    scene c21s001_180pv with fade
    hide c21s001_175v
    show c21s001_180v
    "[emm] sigue cabalgándote entre espasmos, intentando llevarte al orgasmo. Intentando que derrames tu semilla en su interior."
    emm "*GEMIDO* No podría bajar aunque quisiera. *JADEO* Lléname de leche."
    "[dap] reanuda sus besos tras la breve interrupción provocada por su orgasmo."
    dap "*Gemido afirmativo*"
    "Mientras [eri] sigue encontrando placer en su trío particular con las dos almohadas."
    eri "*JADEO* ¡Hazlo, [mc]! *GEMIDO* Llénala de leche."
    "Si existe la reencarnación, quieres ser una almohada la próxima vez."
    "Pero en esta vida eres tan solo un hombre. Un hombre con límites que está a punto de llegar a su tercer orgasmo de la noche."
    if emm._var("pregnant"):
        $ emm._var("pregnancyDiscovered", True)
    if not emm._var("pregnant") and persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[emm] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro" (wt = wt2):
                pass
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                if not WhatIf4S:
                    $ emm._var("pregnant", True)
                play sound ("music/OldMusicBox5.ogg")
        $ resetWalkthrough ()
    call DoubleOrgasmXS3 ("c21s001_550") from _call_DoubleOrgasmXS3_1
    mc "¡Mpffft!"
    "El clímax llega como una nueva explosión de semen, esta vez en el interior de [emm]."
    emm "*GEMIDO* ¡Sí! ¡Está super caliente!"
    "Tu corrida y los fluidos vaginales de [emm] empiezan a mezclarse sin que pueda retenerlos todos en su interior."
    eri "*JADEO* ¡Sois increíbles! *GEMIDO* ¡Es una de las cosas más sexys que he visto!"
    "Los cuatro os estáis corriendo a la vez, disfrutando de la larga sesión de sexo."
    dap "*GEMIDO* *JADEO*"
    "A estas alturas cualquier roce provoca nuevos orgasmos en las tres mujeres. Has perdido la cuenta de cuantas veces se ha corrido cada una."
    stop music fadeout (1.5)
    "Por un momento te planteas olvidarte de la almohada y querer ser mujer en tu próxima vida."
    scene c21s001_555d with fade
    play music ("music/romantic-day.ogg")
    "Tras unos pocos momentos más, las fuerzas os abandonan a todos y os volvéis a derrumbar, inmóviles y jadeantes."
    dap "*Jadeo* Ha sido increíble..."
    "Lo ha sido. Has podido dar placer a tus tres chicas y has sobrevivido a la noche."
    eri "*Jadeo* Tenemos que repetirlo... dentro de unos meses... cuando pueda volver a andar..."
    "Tu polla dentro de [emm] se siente fabulosa, recorrida por sus últimos espasmos vaginales."
    emm "*Jadeo* Si no fuera porque quiero que [mc] siga vivo mañana..."
    "La [emm] que se resistía a follar hace unos minutos ha desaparecido. La [emm] insaciable hace su aparición."
    call BlinkXPS3 ("c21s001_555" , "d") from _call_BlinkXPS3_67
    mc "¿Qué quieres, [emm]? A veces me asustas..."
    emm "Había pensado en perder mi virginidad por detrás hoy... Me he pasado varios días con el plug puesto..."
    if emm._var("anal"):
        emm "Dijiste que te gustaba..."
    else:
        emm "Aunque dijiste que no te ponía demasiado..."
    emm "¿Te apetece? Con lo cachonda que estoy sería el mejor momento. Estoy casi segura de que no va a doler... demasiado."
    if persistent.walkthrough:
        $ wt1 = _("Sexo anal con [emm].")
        $ wt2 = _("Fin de la noche.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Me apetece." (wt = wt1):
            $ Aux = True
            $ emm._var("hadAnal" , True)
        "No me apetece." (wt = wt2):
            $ Aux = False
    $ resetWalkthrough ()
    if not Aux:
        call BlinkXPS3 ("c21s001_560" , "d") from _call_BlinkXPS3_68
        if emm._var("anal"):
            mc "Me gusta, pero creo que por hoy ha habido suficiente. No creo que fuera capaz de darte una buena experiencia ahora mismo."
        else:
            mc "Te dije que no me gustaba, y eso no ha cambiado. Además no creo que fuera capaz de darte una buena experiencia ahora mismo."
        emm "Lo entiendo..."
        call BlinkXPS3 ("c21s001_565" , "d") from _call_BlinkXPS3_69
        if emm._var("anal"):
            emm "Pero no pasa nada, otra vez será... No quiero hacer nada que no disfrutemos los dos..."
        else:
            emm "No te voy a forzar a hacer nada que no te gusta..."
        "Nadie se presta voluntaria para limpiar a Mjolnir esta vez."
    else:
        call BlinkXPS3 ("c21s001_570" , "d") from _call_BlinkXPS3_70
        emm "¡Sí!"
        if persistent.family:
            "Te encanta el entusiasmo que demuestra tu hermana cuando se trata de probar cosas nuevas."
        else:
            "Te encanta el entusiasmo que demuestra [emm] cuando se trata de probar cosas nuevas."
        call BlinkXPS3 ("c21s001_575" , "d") from _call_BlinkXPS3_71
        eri "Yo necesito un descanso lejos de las manos de [mc]... y de las almohadas... Quiero verlo desde el sofá."
        "¡Malditas almohadas! NTR por almohadas, ¿quizás un nuevo género en las novelas visuales?"
        call BlinkXPS3 ("c21s001_580" , "d") from _call_BlinkXPS3_72
        dap "Yo te acompaño. No creo que pueda tener más orgasmos hoy... Al menos no sin romperme del todo..."
        mcp "(Nunca digas nunca, [dap].)"
        call BlinkXPS3 ("c21s001_585" , "d") from _call_BlinkXPS3_73
        emm "Pues estamos tú y yo solos, Mjolnir. Creo que voy a ensalivarte bien para que no me hagas demasiado daño."
        stop music fadeout (1.5)
        mc "Me parece una buena idea. Espero que todos estos días llevando el plug también sirvan."
        play music ("music/Rumba.ogg")
        scene c21s001_235pv
        show c21s001_235v
        "[emm] empieza una lenta mamada en la que no se deja ningún rincón de Mjolnir por recorrer."
        "Prolonga la mamada mucho más de lo necesario para limpiarlo. Continúa pese a que ya estás duro como una piedra."
        call BlinkXPS3 ("c21s001_590a" , "d") from _call_BlinkXPS3_74
        eri "Si sigues así se va a correr y vas a tener que volver a empezar. *Risa*"
        mcp "(Parece que lo está alargando lo máximo posible para retrasar el sexo anal. ¿Se está arrepintiendo?)"
        mc "A mí no me molesta. *Risa*"
        mcp "(Mejor que no se dé cuenta de que sé lo que está pasando por su cabeza. Sigamos la broma.)"
        scene c21s001_590d with fade
        "[emm] abandona su mamada reluctantemente, te obliga a levantarte, y se pone a cuatro patas, invitándote a entrar en su culo."
        emm "¿Te va bien si me pongo así?"
        mc "No sé si va a ser una postura muy cómoda para ti..."
        call BlinkXPS3 ("c21s001_590b" , "d") from _call_BlinkXPS3_75
        if not mc._var("rejectedAeliaPaula"):
            emm "Me ha gustado eso de que te Vilfredo se follara a Aelia como una rana... llevo desde la partida de DnD pensando en esto."
        else:
            emm "Si no hubieras rechazado el sexo en la partida de DnD, Vilfredo se hubiera follado a Aelia como una rana, ya lo habíamos hablado..."
            emm "Llevo desde que hemos acabado la partida pensando en esto."
        emm "Nunca pensé que una partida de DnD me pudiera poner cachonda."
        mc "Pues entonces no hay más que hablar. ¿Quieres otra vez el método tirita?"
        call BlinkXPS3 ("c21s001_595" , "d") from _call_BlinkXPS3_76
        emm "*Risa* No. Pero tampoco quiero que alargues el sufrimiento indefinidamente. Algo intermedio."
        emm "No quiero que la metas un poquito y pares. Rápido pero lento... no sé si me explico."
        mc "*Risa* No te explicas pero te entiendo. He aprendido a interpretarte después de tantos años."
        mc "Vuelve a la posición de la rana."
        scene c21s001_600a with dissolve
        dap "[emm], esa posición era la mezcla perfecta de sexy y ridícula. ¿Estás segura?"
        eri "Si lleva pensándolo desde la partida, creo que está suficientemente segura. No la pongas más nerviosa."
        eri "Acuérdate de lo que me dijiste de tu primera vez y de lo nerviosa que estabas. Para [emm] es lo mismo, aunque el agujero sea diferente."
        scene c21s001_600b with dissolve
        dap "[eri] tiene razón. No me hagas caso, [emm]."
        scene c21s001_590d with fade
        emm "Empieza antes de que me arrepienta."
        scene c21s001_230pv
        show c21s001_230v
        pause (0.84)
        scene c21s001_230dv
        hide c21s001_230v
        "Te colocas detrás de ella y penetras su culo en un solo movimiento. Rápido pero lento, tal como ella te ha pedido."
        emm "¡Ooofff!"
        "Es mucho más estrecho de lo que esperabas después de tantos días usando el plug anal."
        mc "¿Estás bien?"
        scene c21s001_185pv
        show c21s001_185v
        emm "Mejor que con lo de la tirita, desde luego. Pero me siento rellena."
        mc "Si quieres lo podemos dejar. Lo hemos intentado y no es lo que esperabas. No pasa nada."
        emm "No, lo peor ha pasado. Empieza a moverte... lentamente... Creo que ya me voy acostumbrando."
        "La respiración trabajosa de [emm] significa que lo está pasando peor de lo que dice."
        if persistent.family:
            "Pero decirle de parar ahora sería como humillarla delante de sus primas para ella. Por equivocada que esté, tienes que cumplir sus deseos."
        else:
            "Pero decirle de parar ahora sería como humillarla delante de [dap] y [eri] para ella. Por equivocada que esté, tienes que cumplir sus deseos."
        scene c21s001_190pv
        show c21s001_190v
        hide c21s001_185v
        "Empiezas a moverte lentamente, intentando provocarle la mínima incomodidad."
        emm "Sí, así. *Jadeo* Poco a poco. *Jadeo* Evitemos que acabe con una nalga en San Francisco y otra en Los Angeles. *Risa forzada*"
        "No lo está pasando bien, pero es demasiado orgullosa para reconocerlo."
        mc "Voy a ralentizar un poco el ritmo. Me cuesta acostumbrarme a tu culo. Es demasiado estrecho."
        "De esta forma a ella también le dará tiempo a acostumbrarse."
        emm "*Jadeo* Si es lo que tú necesitas..."
        scene c21s001_600c with dissolve
        eri "No tienes que seguir si no lo estás disfrutando, [emm]. Has sido más valiente de lo que seríamos [dap] o yo."
        "Es adorable. Siempre intentando que todos se sientan bien."
        dap "Y [mc] quizás es demasiado grande. Yo no me hubiera atrevido."
        "Saben que le está doliendo, y a ninguna de ellas les gusta ver sufrir a [emm]."
        scene c21s001_195pv
        show c21s001_195v
        hide c21s001_190v
        "Pero el orgullo y la cabezonería de [emm] son muy grandes como para reconocer su error."
        emm "*Jadeo* No os preocupéis... *Jadeo* La incomodidad está pasando..."
        "Los pequeños espasmos que hace cada vez que entras del todo te dicen lo contrario."
        mc "Quizás, si bajas los hombros un poco, pueda entrar en un ángulo mejor."
        "Si no mejora, tendrás que fingir una rampa en el muslo o algo así."
        scene c21s001_205pv
        show c21s001_205v
        hide c21s001_195v
        "Ayudas a [emm] a ajustar su posición con tus manos, marcándole cómo se tiene que poner."
        "Todo cambia de golpe."
        emm "*Gemido* ¡Así sí! *Jadeo* Mucho mejor..."
        "Sus músculos se relajan y puedes entrar y salir con mucha menos resistencia e incomodidad para ella."
        emm "*Gemido* ¡Te odio! *Gemido* Si sabías esto y no me lo has dicho... *Gemido* tengo razones para matarte. *Risa*"
        "Han vuelto las risas, lo que significa que ha empezado a disfrutar."
        scene c21s001_600d with dissolve
        dap "Ahora parece que está disfrutando. *Gemido*"
        "Y parece que, hasta que [emm] no ha empezado a disfrutar, no han empezado a tocarse. Les pone cachondas imaginarse en la situación, disfrutando."
        eri "*Gemido* Ahora hacen una pareja preciosa. *Jadeo*"
        "Estaban sufriendo por el dolor de [emm]. Ahora están disfrutando junto con ella."
        scene c21s001_200pv
        show c21s001_200v
        hide c21s001_205v
        "El cuerpo de [emm] reacciona cada vez mejor. Puedes notar cómo la relajación es absoluta."
        emm "*GEMIDO* ¡Ese movimiento! *GEMIDO* ¡Repítelo!"
        "Sabes a que movimiento se refiere. Has notado tu polla rozando en sitios que no habías notado anteriormente."
        emm "*GEMIDO* ¡Ahí! ¡Justo ahí! *JADEO* ¡Eso me está volviendo loca!"
        "A ti también. Habéis encontrado el punto donde los dos disfrutáis inmensamente."
        scene c21s001_600e with dissolve
        eri "*Gemido* ¡No puedo más! *GEMIDO*"
        "Sus respiraciones entrecortadas indican que sus orgasmos se están acercando tan rápidos como el tuyo."
        dap "*JADEO* Ahora sí que son sexys... *JADEO*"
        "Tan solo necesitaban veros disfrutar a [emm] y a ti para que sus cuerpos reclamaran parte del placer."
        scene c21s001_200pv
        show c21s001_200v
        "Sigues bombeando el culo de [emm], habiendo encontrado el lugar común que es perfecto para ambos."
        emm "*GEMIDO* ¡Me voy a correr! *JADEO* ¡En mi primera vez con [mc] en mi culo!"
        "Su ano empieza a tensarse, haciendo que tu polla se sienta maravillosamente estrujada en cada movimiento."
        emm "*GEMIDO* ¡Córrete dentro! *GEMIDO* ¡Quiero saber lo que se siente! *GEMIDO* ¡Yo estoy a punto!"
        "Tú también estás acercándote al punto de no retorno. Muy rápido."
        call DoubleOrgasmXS3 ("c21s001_605") from _call_DoubleOrgasmXS3_2
        "Las tres chicas llegan a sus orgasmos casi a la vez."
        emm "*GEMIDO* ¡Joder, Joder, JODER! *JADEO* ¡Ngyyya!"
        "¿Cómo se puede comunicar tanto con tan poco?"
        dap "*JADEO* ¡Sí!" (multiple=2)
        eri "*GEMIDO* ¡Oh, que bueno!" (multiple=2)
        "Después de una noche de orgasmos, necesitan muy poco para volver a correrse."
        "Van a necesitar mucho más para poder andar mañana. O [emm] para sentarse."
        call OrgasmXS3 ("c21s001_610") from _call_OrgasmXS3_12
        mc "¡Mpffft!"
        "El orgasmo de [emm] te lleva más allá de tu límite. Hay demasiadas cosas estrujándote y ordeñándote en su interior."
        emm "*GEMIDO* ¡Está super caliente! *JADEO*"
        "Sabes que es tu última bala de la noche. No crees que te quede más gasolina."
        "Tampoco crees que les queden muchas reservas a ninguna de ellas."
        call BlinkXPS3 ("c21s001_615" , "f") from _call_BlinkXPS3_77
        "[emm] se derrumba en la cama cuando su oleada de orgasmos finaliza, demostrando tu teoría de la falta de combustible."
        emm "*Gemido* Si alguien quiere limpiar a Mjolnir... adelante... yo no puedo con mi alma."
        call BlinkXPS3 ("c21s001_620" , "d") from _call_BlinkXPS3_78
        dap "Lo siento, pero yo ya he hecho una limpieza... y no había salido de ningún culo. *Risa*"
        "Al menos le quedan energías para reír."
        call BlinkXPS3 ("c21s001_625" , "d") from _call_BlinkXPS3_79
        eri "*Risa* Creo que yo también voy a pasar... No he estado tan agotada en mi vida."
        "Te va a tocar sacarle brillo a Mjolnir tú mismo. Casi es lo mejor, antes de que El Martillo tenga ideas propias."
        stop music fadeout (1.5)
        mc "No os preocupéis. Ya me limpio yo solo."
        play music ("music/romantic-day.ogg")
    scene c21s001_630d with fade
    "Cuando vuelves a la habitación..."
    mc "Supongo que os queréis quedar a dormir, ¿verdad?"
    "Después de verlas con lencería toda la noche, por alguna razón parecen mucho más niñas ahora."
    call BlinkXPS3 ("c21s001_630" , "d") from _call_BlinkXPS3_80
    emm "O me bajas a mi habitación en brazos o me tendré que quedar a dormir. *Risa*"
    mc "¿Crees que podría cogerte en brazos ahora mismo? *Risa* Y que conste que no te estoy llamando gorda."
    mc "Y antes de que respondas, sí, podría."
    call BlinkXPS3 ("c21s001_635" , "d") from _call_BlinkXPS3_81
    dap "A mí me da mucha pereza ponerme la bata y reptar hasta mi casa, con lo que también me quedo."
    mc "Ya somos tres, ¿[eri]?"
    call BlinkXPS3 ("c21s001_640" , "d") from _call_BlinkXPS3_82
    eri "Después de la Gran Revelación, ya no tiene sentido que no durmamos aquí, ¿no?"
    mc "Tienes razón. Ahora todo el mundo lo sabe y a nadie le va a sorprender."
    call BlinkXPS3 ("c21s001_645" , "d") from _call_BlinkXPS3_83
    emm "Pero vas a tener que mantener las manos y El Martillo quietos. Ninguna de las tres puede tener más sexo ahora mismo."
    mc "No os preocupéis. Creo que Mjolnir va a pasar unos días mirando a todos lados antes de dejarme que lo saque para mear. *Risa* Querrá asegurarse que no estáis."
    scene c21s001_630e with fade
    emm "*Risa* No lo hemos tratado tan mal..."
    eri "*Risa* Pobrecito Mjolnir. Me dan ganas de darle un beso, pero sabemos cómo acabaría."
    dap "*Risa* Es un caballero que se levanta cuando hay una dama en la sala."
    mc "Hacedme un hueco, chicas. ¿Habéis decidido cómo queréis dormir?"
    call BlinkXPS3 ("c21s001_650" , "d") from _call_BlinkXPS3_84
    emm "¡Me pido encima! Ya que no estoy gorda... *Risa*"
    mc "Ligera como una pluma. *Risa*"
    call BlinkXPS3 ("c21s001_655" , "d") from _call_BlinkXPS3_85
    dap "[eri] y yo nos repartiremos tus hombros entonces."
    mc "Quizás no sean las almohadas más cómodas, pero sois bienvenidas."
    call BlinkXPS3 ("c21s001_660" , "d") from _call_BlinkXPS3_86
    eri "Hablando de almohadas... vas a tener que echar a lavar la que he dejado en el armario... Está empapada."
    mc "*Risa* No te preocupes por eso. Dadme un beso y vamos a dormir."
    scene c21s001_665An
    "Todas las chicas te besan por turnos antes de meteros en la cama."
    "La logística de brazos y piernas es complicada durante un momento, hasta que cada uno encontráis vuestra posición."
    "No va a ser la noche más cómoda, pero todos vais a dormir como troncos. Estáis agotados."
    mc "Buenas noches, chicas."
    emm "*Bostezo* Buenas noches, mi amor."
    eri "Buenas noches, cielo. *Bostezo*"
    dap "*Bostezo* Buenas noches, mi vida."
    mc "Os quiero."
    scene c21s001_665e with dissolve
    stop music fadeout (1.5)
    todas "Nosotras también te queremos."
    return
label c21s002_PoliceStation:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_1
    scene black with dissolve
    "Por la mañana, en la comisaría de Policía..."
    scene c21s002_005An with dissolve
    play music ("music/SneakySnitch.ogg")
    "Un hombre sonriente entra en la comisaría."
    sol "Buenos días, Agente. Mi nombre es Solomon Lamb y vengo a poner una denuncia."
    default pol = Character(_("Agente de Policía"), color="#33f3ff")
    pol "Buenos días, Sr. Lamb. ¿En qué puedo ayudarle?"
    call BlinkXPS3 ("c21s002_010" , "d") from _call_BlinkXPS3_87
    sol "¿No deberíamos pasar a su despacho o algo así?"
    pol "Indíqueme primero de qué se trata. La mayoría de las denuncias se toman en este mostrador, para eso está."
    pol "Esto no es Los Angeles ni una película. Nunca se fíe de las películas en cuanto a cómo funciona la Policía de verdad."
    sol "Ah, vale, perdón, es la primera vez que tengo que denunciar a alguien."
    call BlinkXPS3 ("c21s002_015" , "d") from _call_BlinkXPS3_88
    sol "Quiero denunciar a [mc] Marks."
    pol "Un segundo, voy a tomar nota... ¿Por qué quiere denunciarlo?"
    call BlinkXPS3 ("c21s002_020" , "d") from _call_BlinkXPS3_89
    sol "Ayer me disparó."
    call BlinkXPS3 ("c21s002_020" , "h") from _call_BlinkXPS3_90
    pol "¿Qué? ¿Está usted herido?"
    call BlinkXPS3 ("c21s002_025" , "d") from _call_BlinkXPS3_91
    sol "No, falló el disparo y no me dio."
    pol "Eso es muy grave. ¿Dónde ocurrió el intento de asesinato?"
    call BlinkXPS3 ("c21s002_030" , "d") from _call_BlinkXPS3_92
    sol "Mmmm... Intento de asesinato... Sí..."
    call BlinkXPS3 ("c21s002_035" , "d") from _call_BlinkXPS3_93
    sol "En su casa... bueno, no en su casa... fuera de su casa, en la calle..."
    pol "Déjeme apuntarlo. El Sr. [mc] Marks disparó al Sr. Solomon Lamb en la vía pública."
    sol "Exacto... "
    pol "Los moretones que tiene en la cara, ¿también se los hizo el Sr. Marks? ¿O son de un incidente separado?"
    call BlinkXPS3 ("c21s002_040" , "d") from _call_BlinkXPS3_94
    sol "Sí, también. Fue antes de dispararme. En la puerta de su propiedad. Apúntelo."
    pol "Es decir, estaba usted en su propiedad, ¿no?"
    call BlinkXPS3 ("c21s002_045" , "d") from _call_BlinkXPS3_95
    sol "No, no llegué a entrar. Estaba allí... por un tema personal... y me agredió sin venir a cuento ni entrar en su propiedad. Es un tipo muy agresivo."
    pol "Perfecto, me hago una idea de lo que pasó. El Sr. Marks se ha visto envuelto en un par de incidentes violentos previamente."
    call BlinkXPS3 ("c21s002_050" , "d") from _call_BlinkXPS3_96
    sol "¿De verdad? ¡No lo sabía! Teniendo antecedentes, lo detendrán en seguida, ¿verdad?"
    pol "Bueno, primero tenemos que aclarar algunas cosas que no acaban de encajarme."
    pol "¿En qué momento el Sr. Marks sacó el arma? ¿Antes o después de apalizarle a usted?"
    call BlinkXPS3 ("c21s002_055" , "d") from _call_BlinkXPS3_97
    sol "¡No me apalizó! ¡Él recibió tanto o más que yo!"
    pol "Ah, entonces fue una pelea... justa... en la que usted iba ganando. ¿En qué momento sacó el arma?"
    call BlinkXPS3 ("c21s002_060" , "d") from _call_BlinkXPS3_98
    sol "Bueno... no estoy seguro... supongo que fue cuando... lo dejé tirado en el suelo... yo ya me iba hacia mi camioneta cuando oí el disparo."
    pol "Entonces, ¿usted le dio la espalda al Sr. Marks y éste sacó un arma y le disparó?"
    call BlinkXPS3 ("c21s002_065" , "d") from _call_BlinkXPS3_99
    sol "Exacto... supongo que fue entonces cuando sacó el arma. Hasta entonces fue una pelea justa entre hombres... o entre un hombre y un niñato."
    sol "Por eso no venía a denunciarlo por la agresión... sino por el intento de asesinato."
    call BlinkXPS3 ("c21s002_070" , "d") from _call_BlinkXPS3_100
    sol "¡Pelea que, obviamente, no empecé yo! Nunca hubiera empezado una pelea con alguien como ese tipo, por mucho que se lo merezca. No hubiera sido justo para él."
    pol "Perfecto. ¿Hay algún testigo de los hechos?"
    call BlinkXPS3 ("c21s002_075a" , "d") from _call_BlinkXPS3_101
    sol "En su casa había varias mujeres... creo que está formando algún tipo de secta... unas zorras que iban semidesnudas, con las tetas al aire."
    sol "Pero supongo que mentirán para encubrirle."
    call BlinkXPS3 ("c21s002_075b" , "d") from _call_BlinkXPS3_102
    sol "Incluso había una puta rubia que intentó pegarme después del disparo. Por suerte, fui rápido, me metí en mi camioneta y me fui."
    sol "Soy un caballero que nunca ha pegado a una mujer, pero si mi integridad física se viera amenazada..."
    pol "Perfecto. ¿De cuantas pulgadas era la llave Stilson?"
    call BlinkXPS3 ("c21s002_080" , "d") from _call_BlinkXPS3_103
    sol "De 24 pulgadas."
    call BlinkXPS3 ("c21s002_085" , "d") from _call_BlinkXPS3_104
    sol "¿Qué? ¿Qué llave?"
    pol "Con la que usted intentó abrirle el cráneo al Sr. Marks por la espalda, a traición."
    sol "¿Qué? ¡No! ¿Me ha denunciado con esa mentira para cubrirse?"
    call BlinkXPS3 ("c21s002_090" , "d") from _call_BlinkXPS3_105
    oma "No hacía falta que le denunciara. Yo estaba allí, no sé si me recuerda. Era una de las zorras con las tetas al aire."
    oma "Con esto y las grabaciones de seguridad, tengo suficiente para arrestarlo por intentar poner una denuncia falsa."
    oma "Al menos de esta forma, si le meten en prisión, estará a salvo de mi hermana, la rubia que le atizó. Recuerde lo que le dijo sobre el bosque y sobre esconder cadáveres."
    call BlinkXPS3 ("c21s002_095" , "d") from _call_BlinkXPS3_106
    sol "¡No, por favor! ¡No le diga nada!"
    sol "Le juro que no intentaré poner una denuncia sobre ese... ese... sobre ese hombre nunca más."
    call BlinkXPS3 ("c21s002_100" , "d") from _call_BlinkXPS3_107
    oma "Sé que, aparte de un mentiroso, es usted un cobarde."
    oma "Con lo que creo que es lo que más le conviene. Pero quiero algo a cambio."
    call BlinkXPS3 ("c21s002_105" , "d") from _call_BlinkXPS3_108
    sol "¡No tengo dinero! La zorra de mi mujer..."
    call BlinkXPS3 ("c21s002_110" , "d") from _call_BlinkXPS3_109
    oma "Como vuelva a insultar a alguien de mi familia, mi hermana, la rubia, se enterará de esto."
    oma "Y también [mc]. Ya vio lo que le pasó ayer por no parar de insultarlas."
    call BlinkXPS3 ("c21s002_115" , "d") from _call_BlinkXPS3_110
    sol "¡Perdón! Dígame cuánto dinero quiere... haré lo que pueda por conseguirlo..."
    call BlinkXPS3 ("c21s002_120" , "d") from _call_BlinkXPS3_111
    stop music fadeout (1.5)
    oma "No quiero su dinero, pero quiero otras cosas de usted. Va a empezar por...."
    return
label c21s002_BettyMassageAndDrivingLicense:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_2
        menu:
            "¿Estás en una relación con [eri], [dap], y [emm]?"
            "Sí":
                $ eri._var("route" , True)
                $ dap._var("route" , True)
                $ emm._var("route" , True)
            "No":
                $ eri._var("route" , False)
                $ dap._var("route" , False)
                $ emm._var("route" , False)
        menu:
            "¿Cuántas relaciones tienes?"
            "Más de tres":
                $ mc._var("relationships", 4, intention = "set")
                $ Aux = False
            "Entre una y tres":
                $ mc._var("relationships", 2, intention = "set")
                $ Aux = True
            "Ninguna":
                $ mc._var("relationships", 0, intention = "set")
                $ Aux = True
        if Aux:
            menu:
                "¿Estás en una relación con [sai] o [deb.nick]?"
                "Sí":
                    $ deb._var("route" , True)
                "No":
                    $ deb._var("route" , False)
                    $ sai._var("route" , False)
        menu:
            "¿Has pre-abierto la relación con Meemaw?"
            "Sí":
                $ mee._var("route" , True)
            "No":
                $ mee._var("route" , False)
    scene black with dissolve
    "Mientras tanto, en tu habitación..."
    if dap._var("route") and emm._var("route") and eri._var("route"):
        scene c21s002_150a with dissolve
        play sound ("music/knock.ogg")
        "*Knock-Knock*"
        play music ("music/LifeOfAWanderingWizard.ogg")
        bet "*A través de la puerta* Soy yo. ¿Puedo pasar?"
        mc "Un momento, Tía [bet]."
        call BlinkXPS3 ("c21s002_155" , "d") from _call_BlinkXPS3_112
        dap "*Susurrando* ¡Nos hemos quedado dormidas!"
        call BlinkXPS3 ("c21s002_160" , "d") from _call_BlinkXPS3_113
        eri "*Susurrando* Danos un momento para vestirnos."
        call BlinkXPS3 ("c21s002_165" , "d") from _call_BlinkXPS3_114
        emm "Pasa, Tía [bet]."
        emm "*Susurrando* ¿Creéis que aunque nos vistamos no va a saber lo que ha pasado?"
        call BlinkXPS3 ("c21s002_170" , "h") from _call_BlinkXPS3_115
        bet "*Suspiro de sorpresa* ¡Oh!"
        mc "Buenos días, Tía [bet]. ¿Te puedo... te podemos ayudar en algo?"
        call BlinkXPS3 ("c21s002_175" , "d") from _call_BlinkXPS3_116
        bet "No... venía por lo del carnet de conducir, pero si estás... estáis ocupados... ya volveré más tarde."
        call BlinkXPS3 ("c21s002_180" , "d") from _call_BlinkXPS3_117
        eri "No te preocupes, Tía [bet]. Nosotras ya nos íbamos."
        mcp "(No se atreve a mirarla directamente. Pese a lo que ha dicho [emm] se tienen que sentir un poco avergonzadas.)"
        mc "Siéntate un momento, Tía [bet]."
        call BlinkXPS3 ("c21s002_185" , "d") from _call_BlinkXPS3_118
        dap "Sí, quiero darme una ducha..."
        call BlinkXPS3 ("c21s002_190" , "d") from _call_BlinkXPS3_119
        emm "*Risa* ¿Quieres quitarte todo el sudor de anoche?"
        scene c21s002_195a with fade
        eri "Ya os dejamos solos, Tía [bet]."
        dap "Si puedes... no se lo cuentes a nadie."
        mc "¿Vamos a volver a los secretos después de lo de ayer?"
        emm "Por lo que a mí respecta, se lo puedes contar a quien quieras. Estoy orgullosa de que mi novio haya podido complacer a tres mujeres a la vez."
        scene c21s002_195b with dissolve
        emm "No sabes lo que te pierdes siendo monja. *Risa*"
        call BlinkXPS3 ("c21s002_200a" , "d") from _call_BlinkXPS3_120
        bet "No era lo que esperaba encontrarme... Pero no os preocupéis. No es algo que salga en una conversación normal."
        call BlinkXPS3 ("c21s002_200b" , "f") from _call_BlinkXPS3_121
        "Las chicas abandonan la habitación. Ninguna de ellas te da un beso de buenos días."
        bet "¿Te va bien que miremos lo del carnet de conducir ahora?"
        stop music fadeout (1.5)
        mcp "(Es mejor que nos pongamos a hacer lo que ha venido a hacer antes de que quiera meter la nariz en lo que acaba de ver.)"
    else:
        scene c21s002_150b with dissolve
        play sound ("music/knock.ogg")
        "*Knock-Knock*"
        bet "*A través de la puerta* Soy yo. ¿Puedo pasar?"
        mc "Pasa, Tía [bet]."
        call BlinkXPS3 ("c21s002_200c" , "d") from _call_BlinkXPS3_122
        bet "Venía a ver si te iba bien que mirásemos lo del carnet de conducir."
        mc "Siéntate, voy a coger el portátil."
    play music ("music/LostVoices.ogg")
    bet "Aunque supongo que no has desayunado aún."
    mc "No hay ningún problema, hacemos esto y después voy a desayunar. No tengo demasiada hambre, y eso teniendo en cuenta que ayer no cené."
    call BlinkXPS3 ("c21s002_205" , "d") from _call_BlinkXPS3_123
    bet "¿Te vas a poner algo de ropa?"
    mc "No sabía que te molestara, después de lo de aquel día."
    call BlinkXPS3 ("c21s002_210" , "d") from _call_BlinkXPS3_124
    bet "Aquel día no tenías media erección matutina. Es un poco... desconcertante."
    mc "Espérame un momento mientras me pongo unos shorts o algo."
    call BlinkXPS3 ("c21s002_215" , "f") from _call_BlinkXPS3_125
    "Unos minutos después..."
    mc "Pues ya hemos acabado. En una semana deberíamos ir a San Luis para recoger tu nuevo carnet."
    bet "Muchas gracias, [mc]. No hubiera sabido hacerlo si no me hubieras ayudado. No lo ponen fácil para los viejos."
    mc "No eres vieja, Tía [bet]. *Risa* Eres vintage."
    call BlinkXPS3 ("c21s002_220" , "d") from _call_BlinkXPS3_126
    bet "*Risa* ¡Sí, de la época hippy! Me tenías que haber visto con mi caravana rosa. Seguro que Olivia guarda alguna foto."
    mc "¡Esas fotos quiero verlas! ¿Eran de cuando ibas a la universidad?"
    call BlinkXPS3 ("c21s002_225" , "d") from _call_BlinkXPS3_127
    bet "Sí, en vez de alquilar un piso o dormir en una residencia, compré una caravana destartalada que tenía \"Amor Libre\" pintado en un costado."
    bet "Eran los 70 y la aparqué fuera del campus. No te puedes llegar a imaginar la de gente que llamaba a la puerta de la caravana. *Risa*"
    mc "La pregunta es si les abrías la puerta. *Risa*"
    call BlinkXPS3 ("c21s002_230" , "d") from _call_BlinkXPS3_128
    bet "La dejé cerrada muchas más veces de las que la abrí. *Risa* Era una chica bastante decente... o bastante tonta."
    mc "*Risa* Hubiera sido irónico que durmieras en una residencia a los 18 y volvieras a hacerlo ahora."
    call BlinkXPS3 ("c21s002_235" , "d") from _call_BlinkXPS3_129
    if persistent.family:
        bet "Tus bisabuelos estaban preocupados. Hacía poco que habían estrenado una película sobre universitarios que tenían sexo todo el día."
    else:
        bet "Mis padres estaban preocupados. Hacía poco que habían estrenado una película sobre universitarios que tenían sexo todo el día."
    bet "Todo el mundo pensaba que los dormitorios universitarios eran una orgía continua."
    bet "No es que no lo fueran, pero es que la película ni siquiera iba de eso. Nunca me hubieran dado dinero para alojarme en un dormitorio."
    call BlinkXPS3 ("c21s002_240" , "d") from _call_BlinkXPS3_130
    if sai._var("route") or deb._var("route") or mc._var("relationships")>3:
        bet "Aunque si vieran este dormitorio deducirían que no se equivocaban demasiado."
    elif dap._var("route") and emm._var("route") and eri._var("route"):
        bet "Aunque si vieran lo que acabo de ver, deducirían que no se equivocaban demasiado."
    else:
        if persistent.family:
            bet "No sé qué pensarían si supieran que sus nietas regentan un dormitorio."
        else:
            bet "No sé qué pensarían si supieran que su nieta regenta un dormitorio."
    mc "Se darían cuenta de que tienen un montón de bisnietas nuevas. *Risa* Estamos creando una familia enorme."
    stop music fadeout (1.5)
    mc "Pero volviendo a la caravana... ¿Cómo pasaste de una caravana en la que pone Amor Libre a un convento?"
    play music ("music/SadSoul.ogg")
    call BlinkXPS3 ("c21s002_245" , "d") from _call_BlinkXPS3_131
    bet "Me enamoré de la persona equivocada en mi primer año. Estuve enamorada de él durante años."
    bet "Cuando acabé la carrera, me metí en la iglesia. Acabé la especialización en neurocirugía allí."
    bet "Como no dejaba de... encontrármelo, era una forma de evitar las tentaciones y repetir errores."
    bet "Tenía algo de vocación, pero seguramente no me hubiera hecho monja si no hubiera sido por él."
    mc "¿Te hizo daño?"
    call BlinkXPS3 ("c21s002_250" , "d") from _call_BlinkXPS3_132
    bet "No, [mc]. El daño me lo hice yo misma. Él siempre se comportó como la mejor persona que había conocido... hasta entonces."
    bet "Hubo un par de años después de conocerlo que fueron un desastre para mí a nivel personal."
    bet "Para intentar olvidarlo hice cosas de las que no me siento orgullosa. Y me junté con gente que no me hizo bien."
    mc "¿Lo has vuelto a ver?"
    call BlinkXPS3 ("c21s002_255" , "d") from _call_BlinkXPS3_133
    bet "Sí... mmmm... nos seguimos viendo durante bastante tiempo, lo cual lo empeoraba todo."
    bet "Acabé la residencia en el otro lado del país, trabajé en Luisiana un tiempo... no quería quedarme en California..."
    bet "Decidí pedir el traslado a Ghana cuando salió una plaza en un hospital de misioneros. De ahí a Angola, Sudán, Zaire... hasta acabar en Tanzania."
    mc "Tuvo que ser duro, irte tan lejos de la familia..."
    call BlinkXPS3 ("c21s002_260" , "d") from _call_BlinkXPS3_134
    bet "Al principio sí. Después se convirtió en una vida de aventuras, cambiando de país cada pocos años, conociendo sitios y gente nueva."
    bet "No me arrepiento de haberlo hecho. He tenido una vida que mucha gente no puede ni siquiera soñar."
    mc "Lejos de la familia y renunciando a muchas cosas..."
    call BlinkXPS3 ("c21s002_265" , "d") from _call_BlinkXPS3_135
    bet "Todos renunciamos a cosas, [mc]. [mar] me dijo que renunciaste a una buena oferta de trabajo para venir aquí."
    if persistent.family:
        bet "[mar] renunció a su sueño de tener un restaurante propio cuando se casó con tu padre y llegaste tú."
    else:
        bet "[mar] renunció a su sueño de tener un restaurante propio cuando murió Dominic y se vio sola con [emm]."
    call BlinkXPS3 ("c21s002_270" , "d") from _call_BlinkXPS3_136
    bet "¿Te arrepientes de haber vuelto a casa? ¿Crees que [mar] se arrepiente de haber renunciado a su restaurante?"
    mc "No, tienes razón. Renunciamos a cosas pero encontramos otras cosas que se convierten en nuestra vida gracias a ello."
    call BlinkXPS3 ("c21s002_275" , "d") from _call_BlinkXPS3_137
    bet "Hasta que deciden apartarte..."
    mc "Aún no lo sabes, Tía [bet]. Esperemos a la visita a Monterey."
    call BlinkXPS3 ("c21s002_280" , "d") from _call_BlinkXPS3_138
    bet "Ayer estuve pensando sobre eso cuando me fui a la cama... antes de interrumpir vuestra partida."
    bet "Ya sabes que en esto soy como [dap]. Me gusta pensar todos los posibles escenarios."
    mc "No sirve de nada si no sabes qué te van a decir."
    call BlinkXPS3 ("c21s002_285" , "d") from _call_BlinkXPS3_139
    bet "Lo sé, puede que me esté haciendo un mundo y solo sea una visita de cortesía."
    bet "Pero para alguno de los posibles escenarios ya he tomado una decisión."
    mc "¿Qué escenarios? ¿Qué decisiones?"
    call BlinkXPS3 ("c21s002_290" , "d") from _call_BlinkXPS3_140
    bet "No voy a dejar de ser cirujana. Me encanta mi trabajo. Si quieren apartarme o encerrarme, abandonaré la Iglesia y buscaré trabajo como... lego."
    bet "No sé si unirme a Doctores Sin Fronteras o algo así. He colaborado con ellos algunas veces. Sería una forma de poder volver a África."
    bet "Me tendría que volver a certificar, pero..."
    mc "Creo que no deberías tomar decisiones tan precipitadas, Tía [bet], y menos aún sin saber qué es lo que te van a decir."
    mc "Y preferiría que no te fueras, si se diera el caso. Tienes aquí a tu familia, Meemaw se va a mudar también aquí."
    mc "Sé que te encanta África y no voy a pedirte que renuncies a ello, pero sí que voy a pedirte que lo pienses."
    call BlinkXPS3 ("c21s002_295" , "d") from _call_BlinkXPS3_141
    bet "Creo que tienes razón. Quizás me estoy adelantando demasiado."
    call BlinkXPS3 ("c21s002_300" , "d") from _call_BlinkXPS3_142
    bet "Gracias por la conversación, me ha ayudado mucho. Te veo luego."
    bet "Voy a darle el masaje a Olivia antes de que se haga más tarde."
    if mee._var("route"):
        call BlinkXPS3 ("c21s002_305" , "d") from _call_BlinkXPS3_143
        bet "Cuando volví de misa no hacía más que hablar de lo bien que lo habías hecho."
        if mc._var("relationships")>0:
            bet "Por un momento pensé que también iba a confesar que estaba contigo. *Risa*"
        else:
            bet "Por un momento pensé que iba a confesar que estaba contigo. *Risa*"
        mc "*Risa* ¿Te imaginas la cara que hubierais puesto todas?"
    mc "Ve a darle el masaje antes de que se impaciente."
    call BlinkXPS3 ("c21s002_310" , "d") from _call_BlinkXPS3_144
    mc "Pero antes, ¿no tengo beso de buenos días?"
    bet "Sobre eso... si no te importa... Sé que lo propuse yo, pero... preferiría dejar de hacerlo."
    mc "*Risa* ¿Beso demasiado bien y te vienen pensamientos demasiado impuros para una monja?"
    call BlinkXPS3 ("c21s002_315" , "d") from _call_BlinkXPS3_145
    bet "*Risa* ¿Eso es lo que querrías? ¡Creía que eras un buen chico!"
    mc "En serio, si te incomoda no hay ningún problema por dejar de hacerlo."
    call BlinkXPS3 ("c21s002_320" , "d") from _call_BlinkXPS3_146
    bet "¿Recuerdas por qué lo propuse?"
    mc "Para fastidiar a Meemaw."
    bet "Ahora que parece que ya no le importa, no hay razón para seguir haciéndolo."
    call BlinkXPS3 ("c21s002_325" , "d") from _call_BlinkXPS3_147
    bet "No está bien que una monja haga eso. No creo que el Obispo lo aprobara, y menos aún en mi situación."
    mc "Te entiendo. No te preocupes. No hay ningún problema en dejar de hacerlo, pero si alguna de las chicas pregunta, serás tú quien se lo explique."
    scene c21s002_330d with dissolve
    bet "Me parece un trato justo. Te veo luego si no estás muy ocupado. Voy a darle ese masaje a Olivia antes de que se impaciente."
    mc "Espera, Tía [bet]."
    call BlinkXPS3 ("c21s002_330" , "h") from _call_BlinkXPS3_148
    mc "Estoy dispuesto a dejar los besos de lado, pero no los abrazos."
    call BlinkXPS3 ("c21s002_335" , "d") from _call_BlinkXPS3_149
    bet "Nunca voy a permitirte que dejes de dármelos."
    mc "Ahora ya puedes ir a masajear esas tetas."
    scene c21s002_340a with dissolve
    bet "Olivia puede esperar un par de minutos más... se está muy bien aquí."
    mc "Tantos minutos como necesites."
    scene black with dissolve
    stop music fadeout (1.5)
    "Casi diez minutos después, [bet] abandona tu habitación."
    return
label c21s002_AaronCall:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_3
    scene black with dissolve
    "Bajas a desayunar, y al volver a tu habitación..."
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    mcp "(Videoconferencia de un número desconocido, pero el prefijo es de Aruba.)"
    stop sound
    call BlinkXPS3 ("c21s002_350" , "f") from _call_BlinkXPS3_150
    play music ("music/Throne-King.ogg")
    mc "Buenos días, [aar]"
    aar "Hola, [mc]. Te debía una llamada desde hace unos días. ¿Puedes hablar? ¿Estás solo?"
    mc "Sí, llevo varios días esperándola."
    call BlinkXPS3 ("c21s002_355" , "d") from _call_BlinkXPS3_151
    aar "¿Cómo se están portando mis dos chicas? Anoche hablé con ellas y estaban entusiasmadas con... unas muñecas..."
    aar "No quisieron decirme a qué se referían. ¿Le han puesto un mote a alguna de tus chicas?"
    mc "No, [aar], pero si no quisieron decirte de que iba el tema, no voy a ser yo quien lo haga."
    call BlinkXPS3 ("c21s002_360" , "d") from _call_BlinkXPS3_152
    aar "Me parece bien. Pero, ¿cómo se están portando? No me has contestado."
    mc "Muy bien. Se están integrando genial en la familia y todo el mundo las adora."
    call BlinkXPS3 ("c21s002_365" , "d") from _call_BlinkXPS3_153
    aar "Por todo el mundo... te refieres a ti, a [mar] y a [nor], ¿verdad?"
    mc "No, [aar], a toda la familia. ¿Qué crees que querían decir [mar] y [nor] cuando las invitaron a comer y a cenar a casa?"
    call BlinkXPS3 ("c21s002_370" , "d") from _call_BlinkXPS3_154
    aar "Realmente no lo había pensado. Creía que iba a ser... no sé... para conocerse mejor. Algo privado de ellas cuatro."
    mc "[aar], creo que no entiendes a mi familia. Intentamos no guardar secretos, y en este estaban implicadas [eri], [dap], y [emm]."
    call BlinkXPS3 ("c21s002_375" , "d") from _call_BlinkXPS3_155
    aar "Bueno, si es así, supongo que no hay ningún problema porque lo sepan. Ellas también son accionistas de La Compañía."
    mc "Sigues sin entenderlo. Lo sabe toda la familia. Ayer estuvieron en la fiesta de cumpleaños de las chicas. 25 personas."
    call BlinkXPS3 ("c21s002_380" , "d") from _call_BlinkXPS3_156
    aar "¿Qué? No me parece bien, [mc]. No están preparadas para eso y, si el secreto sale a la luz, pueden tener problemas."
    aar "Tus chicas y las mías."
    mc "Sigues sin entenderlo. Tus chicas son mis chicas también. Nuestras chicas. De la familia."
    mc "Nadie va a hacer nada para perjudicarlas. Apostaría mi vida en ello."
    call BlinkXPS3 ("c21s002_385" , "d") from _call_BlinkXPS3_157
    aar "Pero no están preparadas para ese tipo de interacciones sociales... no tienen entrenamiento para eso."
    mc "Pues, al no tener entrenamiento, usaron su instinto. Y se les dio bien. No debes sobreprotegerlas."
    mcp "(De eso ya me ocuparé yo.)"
    call BlinkXPS3 ("c21s002_390" , "d") from _call_BlinkXPS3_158
    aar "No me queda más remedio que confiar en ti, ¿no?"
    mc "Esto es un camino en dos direcciones. Yo he confiado en ti, ahora te toca confiar en mí. Y en ellas. En todos nosotros."
    mc "Pero supongo que no me llamabas solo por eso, ¿no?"
    call BlinkXPS3 ("c21s002_395" , "d") from _call_BlinkXPS3_159
    aar "No. Te llamaba porque ha habido una filtración durante el proceso de toma de poder."
    mc "¿Qué ha pasado?"
    aar "Una de las competidoras de NTR en el mundo de las... operaciones de seguridad... ha recibido información sobre el cambio de propietarios."
    mc "Eso es malo, ¿no? ¿Estamos en peligro otra vez? ¿También tienen clones?"
    call BlinkXPS3 ("c21s002_400" , "d") from _call_BlinkXPS3_160
    aar "No, no es especialmente malo. No van a tomar ninguna acción violenta o ilegal. Y no, no tienen clones, actúan con personal exmilitar."
    aar "Quieren comprar NTR aprovechando lo que consideran una posición de debilidad. ¿Habéis hablado ya sobre si vais a vender vuestras acciones?"
    mc "Yo no voy a venderlas y [dap] tampoco. Supongo que tú, [ama] y [eva] tampoco."
    call BlinkXPS3 ("c21s002_405" , "d") from _call_BlinkXPS3_161
    aar "No, no vamos a vender, con lo que podrían hacerse con un 50\% de la compañía como máximo. No es malo del todo, pero tampoco bueno."
    mc "No creo que [mar], [nor], [emm], o [eri] vayan a querer vender tampoco."
    aar "Eso es mejor todavía, pero deberíais concretarlo. Hoy."
    mc "¿Hoy? ¿Por qué tanta prisa?"
    call BlinkXPS3 ("c21s002_410" , "d") from _call_BlinkXPS3_162
    aar "Uno de sus directivos está en San Diego reunido con vuestra Armada. No me extrañaría que se pusiera en contacto contigo para tener una reunión."
    mc "¿Conmigo? ¿Por qué? ¿Por qué no con [mar] o [nor]?"
    aar "La información filtrada llevaba tu nombre como futuro CEO de la compañía representando al grupo mayoritario de accionistas."
    mc "Vale, pues si se ponen en contacto, con decirle que no estamos interesados en vender hay suficiente, ¿no?"
    call BlinkXPS3 ("c21s002_415" , "d") from _call_BlinkXPS3_163
    aar "Debería haber suficiente, pero tienes que hablarlo antes con tu familia. No puedes tomar una decisión por ellos."
    aar "Incluso sería bueno que te reunieras con él, llevando a [ama] como guardaespaldas. Para saber qué intenciones tienen."
    mc "Si no vamos a vender, ¿qué más da las intenciones que tengan?"
    call BlinkXPS3 ("c21s002_420" , "d") from _call_BlinkXPS3_164
    aar "[mc], la información es poder en este mundo. No creo que seas capaz de sacarle nada, pero [ama] sí que puede conseguir algo de información."
    mc "No me hace ninguna gracia ir a una reunión con un tipo que seguramente sea peligroso sin tener ni idea de nada."
    call BlinkXPS3 ("c21s002_425" , "d") from _call_BlinkXPS3_165
    aar "¿Crees que ese directivo va a ser más peligroso que [ama]? *Risa*"
    mc "*Risa* En eso tienes razón. No voy a estar más protegido con nadie mejor que con ella."
    call BlinkXPS3 ("c21s002_430" , "d") from _call_BlinkXPS3_166
    aar "*Risa* Que no te oiga [eva] decir eso."
    aar "Te la has terminado de ganar con el regalo de las muñecas. Un buen detalle. No la pierdas ahora."
    mc "Espera. Habías dicho que no sabías de qué hablaban con lo de las muñecas."
    call BlinkXPS3 ("c21s002_440" , "d") from _call_BlinkXPS3_167
    aar "Quería comprobar lo leal que eras hacia ellas. Lo de las muñecas era algo simple sobre lo que quizás quisieras fanfarronear."
    aar "Pero siendo algo que puede que para ti no sea importante has guardado lo que creías que era su secreto. Bien hecho."
    mc "No me gustan estos juegos, [aar]."
    call BlinkXPS3 ("c21s002_435" , "d") from _call_BlinkXPS3_168
    aar "A mí tampoco, te lo aseguro. Pero no sé cuánto tiempo voy a poder seguir protegiéndolas. Necesito saber que tú y tu familia lo vais a hacer cuando yo no esté."
    mc "Lo haremos, no te preocupes. ¿No hay nada que pueda frenar el envejecimiento acelerado?"
    call BlinkXPS3 ("c21s002_445" , "d") from _call_BlinkXPS3_169
    aar "No, no hay nada. No voy a durar diez años más. Quizás ni siquiera cinco."
    mc "Lo siento. No tengo palabras..."
    aar "No te preocupes. Hace años que lo tengo asumido."
    call BlinkXPS3 ("c21s002_450" , "d") from _call_BlinkXPS3_170
    aar "Volviendo al tema que nos ocupaba. Si se ponen en contacto contigo desde Iron Fist, la otra compañía, intenta tener una reunión en persona e informa a [ama]."
    mc "De acuerdo. ¿Alguna cosa más?"
    call BlinkXPS3 ("c21s002_455" , "d") from _call_BlinkXPS3_171
    aar "No, eso es todo. ¿Tienes alguna pregunta?"
    mc "Sí. Me dijiste que me dirías de qué te conocía. O de qué me sonabas."
    call BlinkXPS3 ("c21s002_460" , "d") from _call_BlinkXPS3_172
    aar "Supongo que ya lo has pensado, pero... ¿alguna vez te han dicho que pareces mayor de tu edad?"
    mc "Sí. No me digas que yo también soy un clon que envejece más rápido."
    call BlinkXPS3 ("c21s002_465" , "d") from _call_BlinkXPS3_173
    aar "No, no eres un clon. Arnau, Alfred, y yo somos clones tuyos." id c21s002_AaronCall_fca3faa7
    if persistent.family:
        aar "Tus tíos le sacaron células madre a [mar] durante su embarazo, con la excusa de hacer pruebas sobre enfermedades genéticas."
    else:
        aar "Ana se extrajo células madre durante su embarazo. Fuiste el primer sujeto al que lograron clonar."
    call BlinkXPS3 ("c21s002_470" , "d") from _call_BlinkXPS3_174
    aar "No pareces sorprendido."
    mc "Veo una versión joven de tu cara cada día en el espejo. Desde que te conocí, era una de las opciones que barajaba."
    mc "¿Lo saben [ama] y [eva]?"
    call BlinkXPS3 ("c21s002_475" , "d") from _call_BlinkXPS3_175
    aar "No, no lo saben. Y preferiría que no lo supieran. Aunque no me extrañaría que lo sospecharan. Seguramente recuerdan qué aspecto teníamos hace 13 o 14 años."
    aar "Nos parecíamos más a ti de lo que me parezco yo ahora. Un día atarán cabos, pero espero que tarden en hacerlo."
    mc "No te preocupes, no se lo diré. Pero ahora que he confirmado mis sospechas... no sé cómo tratarte."
    call BlinkXPS3 ("c21s002_480" , "d") from _call_BlinkXPS3_176
    aar "*Risa* Es por lo que no quiero que [ama] y [eva] lo sepan. Sería raro para ellas. Puedes tratarme como a un socio."
    aar "No nos vamos a convertir en familia por compartir ADN."
    mc "Me parece bien. Raro, pero bien."
    call BlinkXPS3 ("c21s002_485a" , "d") from _call_BlinkXPS3_177
    aar "Entonces te dejo. Tienes que hablar con tu familia sobre las acciones. Dile a cualquiera de mis chicas que me informe de vuestra decisión, por favor."
    mc "Lo haré. Pero son nuestras chicas."
    aar "La próxima vez que nos veamos, supongo que será aquí, en Aruba. En dos o tres semanas más o menos deberías venir."
    mc "¿Sólo dos o tres semanas?"
    call BlinkXPS3 ("c21s002_485b" , "d") from _call_BlinkXPS3_178
    aar "Más o menos. Hay mucho trabajo que hacer y cuanto antes haya una figura visible, mejor."
    mc "No me gusta la idea pero vale. Nos vemos en dos o tres semanas en Aruba."
    scene black with dissolve
    stop music fadeout (1.5)
    "Tras las despedidas, vuelves a bajar a la cocina. Tienes que hablar con [mar]."
    return
label c21s002_MarChat:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_4
        menu:
            "¿Estás en una relación con [mar]?"
            "Sí":
                $ mar._var("route" , True)
                menu:
                    "¿Estás en una relación con [sam]?"
                    "Sí":
                        $ sam._var("route" , True)
                        menu:
                            "¿Estás en una relación con [emm]?"
                            "Sí":
                                $ emm._var("route" , True)
                            "No":
                                $ emm._var("route" , False)
                    "No":
                        $ sam._var("route" , False)
            "No":
                $ mar._var("route" , False)
    call BlinkXPS3 ("c21s002_500" , "f") from _call_BlinkXPS3_179
    play music ("music/Majestica.ogg")
    if persistent.family:
        mc "Buenos días, Mamá. ¿Tienes un momento?"
    else:
        mc "Buenos días, [mar]. ¿Tienes un momento?"
    mom "Sí, claro. Pareces preocupado. Siéntate conmigo, me estaba preparando un café."
    call BlinkXPS3 ("c21s002_505" , "f") from _call_BlinkXPS3_180
    "Tras explicarle lo que has hablado con [aar] sobre la venta..."
    mom "Ni [nor], ni [eri], ni yo vamos a vender. Ya lo hemos hablado. [emm] todavía no ha dicho nada, pero dudo que quiera vender."
    mom "Para ella es más lógico ser una accionista con ingresos continuos que volverse rica de un día para otro."
    mc "Deberíamos hablarlo con ella. Como ha dicho [aar], no puedo tomar decisiones sobre sus acciones."
    call BlinkXPS3 ("c21s002_510" , "d") from _call_BlinkXPS3_181
    mom "No te preocupes, hablaré con ella hoy mismo."
    if persistent.family:
        mc "Gracias, Mamá."
    else:
        mc "Gracias, [mar]."
    call BlinkXPS3 ("c21s002_515" , "d") from _call_BlinkXPS3_182
    mom "¿Sabes cuándo se van a poner en contacto con nosotros?"
    mc "Ni idea, pero si el tipo está en San Diego y [aar] quiere que tomemos la decisión hoy, supongo que será en breve."
    mc "Mientras no interfiera con lo de [emm] en Monterey... Ese tipo no sabe lo que es enfrentarse a [emm] enfadada."
    call BlinkXPS3 ("c21s002_520" , "d") from _call_BlinkXPS3_183
    mom "*Risa* En ese caso, se enterarían de que [ama] es un corderito sobre el que no hay nada que temer."
    mc "Bueno, pues te voy a dejar. Tengo que llevar a [meg] a la estación de autobuses."
    if mar._var("route") and sam._var("route"):
        call BlinkXPS3 ("c21s002_525" , "d") from _call_BlinkXPS3_184
        mom "Antes de que te vayas..."
        mc "¿Qué ha pasado ahora? *Risa*"
        call BlinkXPS3 ("c21s002_530" , "d") from _call_BlinkXPS3_185
        mom "No, no ha pasado nada... ahora."
        mom "Ayer, cuando estuve en tu habitación... con [sam]..."
        mc "¿Te molestó vernos allí a los dos?"
        call BlinkXPS3 ("c21s002_535" , "h") from _call_BlinkXPS3_186
        mom "¿Qué? ¡No! Me alegra mucho que estés con [sam]. Es una mujer fantástica."
        mc "¿Entonces cuál es el problema?"
        call BlinkXPS3 ("c21s002_540" , "d") from _call_BlinkXPS3_187
        mom "No es que haya ningún problema... durante la fiesta estuvimos hablando..."
        mom "Sabes que todo esto empezó con una broma sobre compartirte..."
        mc "Sí..."
        call BlinkXPS3 ("c21s002_545" , "d") from _call_BlinkXPS3_188
        if emm._var("route"):
            mom "Después de lo que pasó con [emm]..."
        mom "Y sabes que [sam] es mi mejor amiga..."
        mc "Me gusta a donde va esto..."
        call BlinkXPS3 ("c21s002_550" , "d") from _call_BlinkXPS3_189
        mom "¿Me vas a hacer decirlo?"
        mc "*Risa* ¿A qué te refieres? Siempre dices que soy un chico muy inocente que no capta las indirectas."
        call BlinkXPS3 ("c21s002_555" , "d") from _call_BlinkXPS3_190
        mom "*Risa* Y un poco capullo también."
        mc "*Risa* Sí, sí. Soy un capullo. Pero decías que [sam.nick] es tu mejor amiga..."
        call BlinkXPS3 ("c21s002_560" , "d") from _call_BlinkXPS3_191
        mom "Vale... estuvimos hablando..."
        mom "Y nos gustaría compartirte de verdad en el futuro..."
        if emm._var("route"):
            mom "Como hicimos [emm] y yo. Aunque [sam] aún no sabe nada sobre eso."
        mc "Creo que puedo liberar las próximas semanas de mi agenda y haceros un hueco. *Risa* Excepto por lo de [emm] en Monterey, claro."
        mc "Hablando en serio. Me encantaría, pero solo si las dos lo queréis de verdad."
        call BlinkXPS3 ("c21s002_565" , "d") from _call_BlinkXPS3_192
        mom "No estamos diciendo de hacerlo inmediatamente. Quizás cuando vuelvas de Aruba. Las dos queremos tenerte para nosotras solas unas cuantas veces más antes de hacer algo así."
        mom "Pero queríamos saber si te gustaría... hacer un trío con las dos."
        mc "Si alguna vez digo que no me apetece algo así, llévame al médico. *Risa* Algo no funcionará en mi cerebro."
        call KissXPS3 ("c21s002_570a" , "d") from _call_KissXPS3
        mom "Gracias, mi amor. Si hubieras dicho que no, me hubiera sentido estúpida."
        mc "No podría haber rechazado algo así nunca."
        mc "Pero ahora en serio, tengo que ir a llevar a [meg]."
    call BlinkXPS3 ("c21s002_575" , "d") from _call_BlinkXPS3_193
    mom "Una última cosa..."
    mc "Dime."
    mom "¿Qué opinas de [kim]?"
    mc "Me parece que es una chica fantástica, y parece que se está integrando muy bien."
    mc "Diría que, además, se lleva muy bien contigo."
    call BlinkXPS3 ("c21s002_580" , "d") from _call_BlinkXPS3_194
    mom "Sí, creo que en su caso no eres el favorito, sino que me ha tocado a mí. *Risa*"
    call BlinkXPS3 ("c21s002_585" , "d") from _call_BlinkXPS3_195
    mom "¡Y no es que tenga ninguna queja sobre ello! No me malinterpretes."
    mc "Me lo imagino, pero ¿por qué lo preguntabas?"
    call BlinkXPS3 ("c21s002_590" , "d") from _call_BlinkXPS3_196
    mom "Es una chica muy sensible, y ayer intentó hablarme de ti un par de veces, pero nos interrumpieron y no quiso seguir hablando del tema."
    mom "¿Sabes de qué va?"
    mc "Tengo alguna idea sobre ello, pero creo que, si lo quería hablar contigo, debes hablarlo con ella."
    mc "Podría estar equivocado y que quisiera hablar de cualquier otra cosa."
    call BlinkXPS3 ("c21s002_595" , "d") from _call_BlinkXPS3_197
    mom "Creo que tienes razón. No debería habértelo preguntado a ti, sino a ella."
    mom "Ahora deberías irte a buscar a [meg] o vais a llegar tarde."
    stop music fadeout (1.5)
    if mar._var("route"):
        call KissXPS3 ("c21s002_570a" , "d") from _call_KissXPS3_1
        mom "Hasta luego, mi amor."
    if persistent.family:
        mc "Hasta luego, Mamá."
    else:
        if mar._var("route"):
            mc "Hasta luego, mi vida."
        else:
            mc "Hasta luego, [mar]."
    return
label c21s002_Megan:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_5
        menu:
            "¿Estás en una relación con [meg]?"
            "Sí":
                $ meg._var("route" , True)
            "No":
                $ meg._var("route" , False)
    call BlinkXPS3 ("c21s002_600" , "f") from _call_BlinkXPS3_198
    play music ("music/IWonderWhatIllDoToday.ogg")
    "Después de recoger a [meg] en su habitación y llevarla a la estación de autobuses..."
    mc "¿Qué tal lo has pasado el fin de semana?"
    meg "Ha sido genial. Me lo he pasado muy bien y ha sido fantástico conocer a todo el mundo."
    mc "¿Te sientes más a gusto ahora, después de la fiesta de cumpleaños?"
    call BlinkXPS3 ("c21s002_605" , "d") from _call_BlinkXPS3_199
    meg "No me la imaginaba así. Con lo locos que estáis todos, esperaba algo más salvaje. Fue bastante tranquila."
    mc "Creo que la parte más salvaje estuvo en el jacuzzi. Las chicas se lo pasaron muy bien."
    call BlinkXPS3 ("c21s002_610" , "d") from _call_BlinkXPS3_200
    meg "Bueno, Jamaal también se puso muy salvaje cuando tú te fuiste. *Risa* Y no me refiero solo a su capacidad para comer."
    meg "Empezó a contar chistes sobre todo el mundo, menos [mad.nick] y las estudiantes. Supongo que aún no tiene suficiente material."
    mc "Es un monologuista frustrado. *Risa* Por eso le dejo hablar solo muchas veces."
    call BlinkXPS3 ("c21s002_615" , "d") from _call_BlinkXPS3_201
    meg "*Risa* Sois tal para cual. Me encanta cómo os metéis el uno con el otro. Se nota que os queréis."
    mc "Ya sabes que es el deber de cualquier amo querer a su mascota. *Risa*"
    call BlinkXPS3 ("c21s002_620" , "d") from _call_BlinkXPS3_202
    meg "¿Ves? A eso me refiero. *Risa*"
    mc "Hablando de cosas más serias. ¿Cuándo vuelves? ¿Vendrás el próximo fin de semana también?"
    call BlinkXPS3 ("c21s002_625" , "d") from _call_BlinkXPS3_203
    meg "Trabajo hasta el miércoles en Westport y empiezo el viernes aquí de nuevo."
    meg "[mar] me ha dicho que venga el jueves, pero no estoy segura. Normalmente los jueves los aprovecho para hacer la limpieza en casa."
    mc "*Risa* Si no estás en casa no verás si está sucia, y se ensuciará menos."
    call BlinkXPS3 ("c21s002_630a" , "d") from _call_BlinkXPS3_204
    meg "*Risa* ¡Hombres!"
    call BlinkXPS3 ("c21s002_630b" , "d") from _call_BlinkXPS3_205
    meg "Ya veremos. El jueves o el viernes estaré de nuevo aquí. Además ya tendré el coche arreglado."
    mc "Entonces espero verte el jueves."
    if meg._var("route"):
        call BlinkXPS3 ("c21s002_635" , "d") from _call_BlinkXPS3_206
        meg "Tú también puedes venir a mi casa, si quieres. Sólo está a 35 minutos."
        mc "Si puedo lo haré."
    mc "Esta semana va a ser complicada."
    call BlinkXPS3 ("c21s002_640" , "d") from _call_BlinkXPS3_207
    meg "Lo sé. Tienes lo de [emm] entre las otras miles de cosas que tienes que hacer."
    call BlinkXPS3 ("c21s002_645" , "d") from _call_BlinkXPS3_208
    meg "Por allí llega mi autobús."
    if meg._var("route"):
        call KissXPS3 ("c21s002_650" , "d") from _call_KissXPS3_2
    else:
        scene c21s002_650c with dissolve
    meg "Te veo el jueves o el viernes. Seguramente el jueves por la noche."
    mc "Hasta el jueves, [meg]."
    scene c21s002_655An with fade
    "[meg] desaparece en el interior del autobús."
    stop music fadeout (1.5)
    "Te acabas de dar cuenta de que no lleva la maleta que trajo. ¿Ha dejado ropa en casa?"
    return
label c21s003_NoKiaraDate:
    scene c21s003_005a with fade
    "Justo al irse el autobús..."
    play sound ("music/RingtoneMC.ogg")
    "*Ring-Ring*"
    stop sound
    scene c21s003_005b with dissolve
    play music ("music/On-The-Rise.ogg")
    mc "Hola, [ama]. ¿Puedo ayudarte en algo?"
    call BlinkXPS3 ("c21s003_010" , "f") from _call_BlinkXPS3_209
    ama "Solo quería recordarte que hoy habíamos quedado para tomar un café y hablar de mis ideas sobre NTR. ¿A qué hora te iría bien?"
    mc "Estoy en la estación de autobuses ahora mismo. Como algo rápido y podemos quedar. ¿En 30 minutos te va bien?"
    call BlinkXPS3 ("c21s003_015" , "d") from _call_BlinkXPS3_210
    ama "Perfecto. Te mando la dirección de un café que tienes cerca y podemos quedar allí."
    mc "Genial. Te veo en 30 minutos. Hasta ahora."
    ama "Hasta ahora, [mc]."
    stop music fadeout (1.5)
    return
label c21s003_KiaraDate:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_6
        menu:
            "¿Estás en una relación con [eil]?"
            "Sí":
                $ eil._var("route" , True)
                $ mc._var("relationships", 2, intention = "set")
                menu:
                    "¿Sabe que está embarazada?"
                    "Sí":
                        $ eil._var("pregnancyDiscovered" , True)
                    "No":
                        $ eil._var("pregnancyDiscovered" , False)
            "No":
                $ eil._var("route" , False)
                menu:
                    "¿Sales con alguien aparte de [kia]?"
                    "Sí":
                        $ mc._var("relationships", 2, intention = "set")
                    "No":
                        $ mc._var("relationships", 1, intention = "set")

    scene c21s003_005c with fade
    play music ("music/RayOfHope.ogg")
    "Llegas a la biblioteca unos minutos antes de la hora a la que has quedado con [kia]."
    "Pasaste mucho tiempo en tu época del instituto en este edificio."
    "Por un momento dudas si debes entrar o no a buscarla. Decides hacerlo."
    scene c21s003_005d with dissolve
    mcp "(Allí está. Se ha cambiado el peinado y se ha puesto un vestido precioso. Creo que el premio a la elegancia de hoy ya tiene dueño.)"
    mcp "(Y no soy yo.)"
    scene c21s003_005e with dissolve
    "Te acercas tímidamente al mostrador donde está hablando con la Srta. Walker, la bibliotecaria canadiense de tu época de instituto. De Montreal, crees recordar."
    "No sabes cuánto sabe sobre vuestra relación, si es que sabe algo. O de la situación con Solomon."
    mc "Hola, [kia]. Hola..."
    kia "Hola, [mc]. Te presento a Geneviève, mi jefa. Gen, este es [mc], el sobrino de [nor], de quien te he hablado."
    default gen = Character("Geneviève", color="#36f3ff")
    gen "Encantada de conocerte, [mc]."
    mc "Igualmente, Geneviève."
    gen "Puedes llamarme Gen."
    call BlinkXPS3 ("c21s003_020" , "d") from _call_BlinkXPS3_211
    mc "¿Estás lista para irnos?"
    kia "Sí, dame un momento que vaya a por el bolso."
    mc "Perfecto, te espero aquí."
    kia "Será solo un segundo."
    call BlinkXPS3 ("c21s003_025" , "d") from _call_BlinkXPS3_212
    gen "Así que [kia] y [eil] se están alojando en tu casa mientras acaban con el problema de termitas, ¿no?"
    gen "Les estáis haciendo un favor muy grande."
    mcp "(¿Termitas? Está claro que no le ha contado lo de Solomon.)"
    mc "Bueno, no se aloja en mi casa, sino en la de mi tía, [nor]."
    call BlinkXPS3 ("c21s003_030" , "d") from _call_BlinkXPS3_213
    gen "Tú y yo nos conocemos, ¿verdad?"
    mc "Pasaba mucho tiempo aquí cuando iba al instituto."
    call BlinkXPS3 ("c21s003_035" , "d") from _call_BlinkXPS3_214
    gen "*Risa* ¡No llevo tanto tiempo trabajando aquí! Sólo llevo ocho años."
    mc "Y hace cuatro yo estudiaba en el instituto de Newport, Srta. Walker. Es posible que no me reconozca."
    mc "Pasado de peso, con la nariz metida en un libro, con un amigo en silla de ruedas..."
    call BlinkXPS3 ("c21s003_040" , "d") from _call_BlinkXPS3_215
    gen "¿Marks? ¿[mc] Marks? ¡No puede ser!"
    mc "Puede ser. Supongo que no me dejé ningún libro por devolver cuando me fui a la universidad. *Risa*"
    call BlinkXPS3 ("c21s003_045" , "d") from _call_BlinkXPS3_216
    gen "Estoy sorprendida... Un gran cambio..."
    gen "Y ya no soy la Srta. Walker. Ahora soy la Sra. Sky."
    mc "Felicidades, Sra. Sky."
    call BlinkXPS3 ("c21s003_050" , "d") from _call_BlinkXPS3_217
    gen "Puedes seguir llamándome Gen. Ya no eres un adolescente."
    mc "Felicidades, Gen, entonces."
    call BlinkXPS3 ("c21s003_055" , "d") from _call_BlinkXPS3_218
    kia "Ya nos podemos ir, [mc]. No lo entretengas, Gen, o tendré que tomarme más tiempo para comer."
    mc "Nos estábamos poniendo al día. Gen y yo nos conocíamos de mi época de rata de biblioteca."
    call BlinkXPS3 ("c21s003_060" , "d") from _call_BlinkXPS3_219
    mc "Hasta otra, Gen."
    gen "Hasta otra, [mc]."
    call BlinkXPS3 ("c21s003_065" , "d") from _call_BlinkXPS3_220
    kia "Vuelvo en una hora... más o menos."
    call BlinkXPS3 ("c21s003_070" , "f") from _call_BlinkXPS3_221
    kia "¿Dónde has decidido que vayamos a comer?"
    mc "Un restaurante que me ha recomendado Tía [bet]. Es sorprendente que en una semana conozca tantos restaurantes."
    mc "Pero... ¿no hay beso para mí?"
    call BlinkXPS3 ("c21s003_075" , "d") from _call_BlinkXPS3_222
    kia "¿Delante de la biblioteca? Es mi puesto de trabajo... Y Gen conoce a Solomon... y..."
    mc "No te preocupes. Será duro, pero lo entiendo y puedo esperar a cuando llegues a casa."
    mc "No me gustan los secretos, pero entiendo que no quieras hacer público lo nuestro aún, hasta que se resuelva lo de Solomon."
    call BlinkXPS3 ("c21s003_080" , "d") from _call_BlinkXPS3_223
    kia "No es que no quiera hacerlo público. Me da lo mismo que la gente sepa que Solomon y yo hemos roto. No voy a volver con él nunca."
    kia "Pero hace una semana estaba con él y ahora estoy contigo... todo el mundo va a pensar que soy... una zorra que se ha ido con un hombre más joven."
    scene c21s003_085AnBlink with dissolve
    mc "[kia], escúchame. En casa podremos repetir lo de anoche si quieres. Te dije que no teníamos que hacer nada que no quisieras hacer"
    mc "Y si una de las cosas que no quieres hacer es que te bese delante de la biblioteca, no hay ningún problema."
    call BlinkXPS3 ("c21s003_090" , "d") from _call_BlinkXPS3_224
    mc "No quiero estropear nuestra primera... o segunda cita... por una nimiedad como esta."
    mc "Estás preciosa, me encanta lo que te has hecho en el pelo y ese color de pintalabios te favorece mucho."
    mc "Voy a tener muchas ocasiones de comerme ese pintalabios, pero sólo si no lo estropeamos hoy."
    call BlinkXPS3 ("c21s003_095" , "d") from _call_BlinkXPS3_225
    mc "¿Te parece bien si vamos a comer? Mi idea de una cita no es discutir con una preciosa mujer en la calle ni hacerla sentir mal."
    kia "Vamos... pero no creas que te va a ser fácil estropear hoy. Y menos si, como {b}casi{/b} siempre, aciertas en lo que tienes que decir."
    mc "*Risa* Es un defecto con el que tendrás que lidiar. No acierto siempre, pero sí las suficientes veces."
    stop music fadeout (1.5)
    mc "Vamos antes de que se haga más tarde."
    play music ("music/You-Know-Instrumental.ogg")
    call BlinkXPS3 ("c21s003_100" , "f") from _call_BlinkXPS3_226
    mc "No sé por qué no me imaginé que sería una pizzería, habiéndolo recomendado Tía [bet]."
    kia "*Risa* ¿De verdad es tan adicta a la pizza?"
    mc "*Risa* Supongo que la gula es el único pecado que se permite. ¿Y qué mejor que cometerlo con pizza?"
    call BlinkXPS3("c21s003_105" , "d") from _call_BlinkXPS3_227
    "Después de que el camarero os siente en una mesa no tan apartada como te hubiera gustado..."
    mc "¿Qué te apetece comer?"
    kia "Si por mí fuera, haría como [bet] y pediría una pizza, pero entre el tiempo que van a tardar y lo lenta que soy comiendo, la cita no daría para nada más."
    kia "Con lo que creo que pediré esta ensalada. Tiene buena pinta."
    mc "¿Tienes algún plan para después de comer?"
    scene c21s003_110d with dissolve
    pause (0.8)
    call BlinkXPS3("c21s003_110" , "d") from _call_BlinkXPS3_228
    kia "Había pensado en dar un paseo antes de volver a la biblioteca... si te apetece."
    mc "Me encantan los paseos contigo. *Risa* Pero no podremos hacer tantas pausas como anoche."
    call BlinkXPS3 ("c21s003_115" , "d") from _call_BlinkXPS3_229
    kia "*Risa* No me refería a ese tipo de paseo."
    mc "Lo sé. *Risa* Que sean dos ensaladas, pero no le digas a [mar] que he pedido una ensalada en un restaurante."
    call BlinkXPS3 ("c21s003_120" , "d") from _call_BlinkXPS3_230
    kia "*Risa* ¿Por qué?"
    mc "No te creería. *Risa* ¿Pagar por algo verde? Orégano o albahaca, sí. Lechuga, quizás, dentro de una hamburguesa. Broccoli, nunca."
    call BlinkXPS3 ("c21s003_125" , "d") from _call_BlinkXPS3_231
    kia "*Risa* Si fueras hijo mío comerías de todo."
    mc "*Risa* Prefiero ser tu novio y olvidarme del broccoli."
    call BlinkXPS3 ("c21s003_130" , "d") from _call_BlinkXPS3_232
    kia "Yo también... A lo del novio. No tengo ningún problema con el broccoli."
    scene c21s003_130d with dissolve
    mc "Te cedo mi parte de la producción mundial de broccoli. *Risa* Para que veas que tienes un novio generoso."
    call BlinkXPS3 ("c21s003_135" , "d") from _call_BlinkXPS3_233
    kia "*Risa* Es super generoso de tu parte."
    mc "¿Sabes que me encanta verte reír?"
    call BlinkXPS3 ("c21s003_140a" , "d") from _call_BlinkXPS3_234
    kia "Gracias, pero ¿sabes que [eil] me habló de tu costumbre de intentar ruborizarla?"
    mc "*Risa* ¡Maldita chivata!"
    call BlinkXPS3 ("c21s003_140b" , "d") from _call_BlinkXPS3_235
    kia "¡Devuelve esa mano ahí ahora mismo!"
    mc "*Risa* ¡A tus órdenes!"
    call BlinkXPS3 ("c21s003_145" , "d") from _call_BlinkXPS3_236
    if eil._var("route"):
        kia "*Risa* Ahora que las dos salimos contigo, me ha dado algunos consejos. Y me ha explicado algunos de tus trucos para hacerla sentir bien."
    else:
        kia "*Risa* Me ha explicado muchas cosas de cuando salíais juntos. Supongo que quería ponerme en sobre aviso sobre tus viejos trucos para hacerla sentir bien."
    mc "*Risa* Tendré que encontrar trucos nuevos, entonces. La compañía los merece."
    call BlinkXPS3 ("c21s003_150" , "d") from _call_BlinkXPS3_237
    kia "¿Puedo serte sincera?"
    mc "Siempre."
    call BlinkXPS3 ("c21s003_155" , "d") from _call_BlinkXPS3_238
    kia "Si lo que dices es sincero, no me importa que se lo hayas dicho con anterioridad a mi hija. O a otras mujeres."
    kia "No quiero que digas cosas que no sientes sólo para hacerme sentir bien, pero tampoco necesito que inventes frases bonitas cada día."
    kia "Si sientes realmente lo que dices, me va a gustar igualmente."
    mc "Entendido. Entonces... ¿Sabes que me encanta verte reír? *Risa*"
    call BlinkXPS3 ("c21s003_160" , "d") from _call_BlinkXPS3_239
    kia "*Risa* ¡Idiota!"
    mc "*Risa* ¡Hey! Has dicho que podía repetir cosas si era sincero. Y lo he sido. Me encanta verte reír."
    call BlinkXPS3 ("c21s003_165" , "d") from _call_BlinkXPS3_240
    kia "Y a mí me encanta que me hagas reír..."
    call BlinkXPS3 ("c21s003_170" , "d") from _call_BlinkXPS3_241
    kia "Es tan diferente a cuando iba a comer con Solomon..."
    mc "¿Solomon? ¿Quién es Solomon? El nombre me suena. Algo de partir un bebé por la mitad, ¿no?"
    mc "Pero no eres tan mayor como para haber ido a comer con él... *Risa*"
    call BlinkXPS3 ("c21s003_175" , "d") from _call_BlinkXPS3_242
    kia "*Risa* Realmente eres idiota. Me acabas de llamar vieja en nuestra segunda cita."
    mc "¡Oops! El chiste se me ha ido de las manos."
    call BlinkXPS3 ("c21s003_180" , "d") from _call_BlinkXPS3_243
    kia "Sé que no está bien que hable de él en una cita contigo y prometo que será la última vez que lo haga."
    kia "Con él siempre tenía que estar alerta para no decir algo que le molestara."
    kia "Para que no bebiera demasiado."
    kia "Para que no montara un espectáculo si algún hombre me miraba..."
    mc "Lo entiendo, no tenía que ser cómodo."
    call BlinkXPS3 ("c21s003_185" , "d") from _call_BlinkXPS3_244
    kia "No, no lo era. Y a eso me refiero con que esto es diferente."
    kia "Contigo, lo único que tengo que temer es no poder resistir las ganas de besarte en medio del restaurante."
    kia "Me haces sentir... relajada."
    mc "Solomon es una de las personas a las que no me gustaría parecerme. Si alguna vez empiezo a comportarme como él, avísame para dejar de hacerlo."
    call BlinkXPS3 ("c21s003_190" , "d") from _call_BlinkXPS3_245
    kia "Los dos respiráis. *Risa* Creo que ahí acaban las similitudes."
    mc "*Risa* Y, en mi caso, no lo considero un desperdicio de oxígeno."
    kia "*Risa* No, no lo es."
    call BlinkXPS3 ("c21s003_195" , "d") from _call_BlinkXPS3_246
    mc "¿Puedes pedir la ensalada de pasta y un agua con gas para mí? Tengo que ir al lavabo."
    kia "¿Ensalada de pasta? Habías dicho algo verde..."
    mc "La pasta en la ensalada es verde, roja, y blanca. *Risa* No esperabas que pidiera lechuga o endivias, ¿verdad?"
    mc "Paso a paso..."
    call BlinkXPS3 ("c21s003_200" , "d") from _call_BlinkXPS3_247
    kia "*Risa* Vale, aceptaré pasta verde como ensalada. Creo que lleva una ínfima porción de espinacas."
    mc "Suficiente para mí."
    scene c21s003_205An with hpunch
    "Sorprendes a [kia] con un beso antes de ir al lavabo. La sorpresa inicial pasa en seguida."
    call BlinkXPS3 ("c21s003_210" , "d") from _call_BlinkXPS3_248
    kia "Pero..."
    mc "Luego, cielo. *Risa* Tengo que ir al lavabo."
    mc "Y esto no es la puerta de la biblioteca."
    call BlinkXPS3 ("c21s003_215" , "f") from _call_BlinkXPS3_249
    mc "Ya estoy de vuelta. ¿Han tomado nota?"
    kia "Sí. No tenían la ensalada de pasta y te he pedido un combo de lechugas y espinacas."
    mc "*Risa* Un restaurante italiano sin pasta. ¿Se está acabando el mundo?"
    call BlinkXPS3 ("c21s003_220" , "d") from _call_BlinkXPS3_250
    kia "*Risa* Estoy bromeando. He pedido tu ensalada rebosante de calorías."
    kia "Pero te hubieras merecido la lechuga por ese beso a traición. *Risa*"
    mc "Era para que pudieras soportar mejor las ganas de besarme en medio del restaurante. Ahora te puedes relajar aún más."
    call BlinkXPS3 ("c21s003_225" , "d") from _call_BlinkXPS3_251
    kia "A ti nadie te ha dicho nunca que besas muy bien, ¿verdad?"
    mc "Si te soy sincero, me lo han dicho alguna vez. No preguntes quién."
    call BlinkXPS3 ("c21s003_230" , "d") from _call_BlinkXPS3_252
    kia "*Risa* Era una pregunta retórica, idiota. Sé que [eil] te lo ha dicho muchas veces. Alguna vez incluso la oí decírtelo."
    call BlinkXPS3 ("c21s003_235" , "d") from _call_BlinkXPS3_253
    kia "¿Tú crees que un beso como ese va a quitarme las ganas de darte más?"
    mc "Espero que no. Me gusta el sabor de ese pintalabios."
    call BlinkXPS3 ("c21s003_240" , "d") from _call_BlinkXPS3_254
    kia "¡Dios mío! ¿Qué he hecho yo para merecer un idiota como este?"
    mc "Soy el premio por ser una mujer maravillosa. *Risa* Y no se aceptan devoluciones."
    call BlinkXPS3 ("c21s003_245" , "d") from _call_BlinkXPS3_255
    kia "*Risa* No pensaba devolverte a fábrica. No eres {b}tan{/b} defectuoso."
    mc "*Risa* No sé si ofenderme o tomármelo como un cumplido..."
    scene c21s003_250An with dissolve
    "Cuando traen vuestras dos ensaladas (y sí, una ensalada de pasta {b}es{/b} una ensalada) empieza una comida llena de risas."
    "[kia] está relajada y os lo pasáis bien. Habláis de todo y de nada."
    "Habláis de su trabajo, del dormitorio, y de NTR."
    "Charláis sobre [eil] y del resto de las mujeres de la familia."
    "Habláis de vosotros."
    "Pero, sobre todo, os reís mucho. Os reís de todo. De ti y de ella. Del mundo."
    call BlinkXPS3 ("c21s003_250" , "d") from _call_BlinkXPS3_256
    "*Ring-Ring*"
    mc "Tengo que cogerlo, [kia]. Es [ama]. Dame un segundo."
    kia "Todo el tiempo que necesites."
    mc "Hola, [ama]. ¿Puedo ayudarte en algo?"
    call BlinkXPS3 ("c21s003_010" , "f") from _call_BlinkXPS3_257
    ama "Solo quería recordarte que hoy habíamos quedado para tomar un café y hablar de mis ideas sobre NTR. ¿A qué hora te iría bien?"
    mc "Estoy comiendo con [kia]. ¿En una hora y media te va bien?"
    kia "Puedes quedar antes. En 30 minutos tengo que estar de vuelta en la biblioteca."
    call BlinkXPS3 ("c21s003_015" , "d") from _call_BlinkXPS3_258
    ama "La he escuchado. Te mando la dirección de un café que tienes cerca y podemos quedar allí. ¿En una hora?"
    mc "Genial. Te veo en una hora. Hasta dentro de un rato."
    ama "Hasta ahora, [mc]."
    call BlinkXPS3 ("c21s003_255" , "f") from _call_BlinkXPS3_259
    mc "¿Por dónde íbamos?"
    kia "Íbamos por el momento en que pido la cuenta y nos vamos a dar ese paseo antes de que se haga más tarde."
    mc "De acuerdo, pero la cuenta la pido yo. Fui yo quien te invitó a comer. Pago yo."
    call BlinkXPS3 ("c21s003_260" , "d") from _call_BlinkXPS3_260
    kia "Pero..."
    mc "Si quieres pagar tú, vas a tener que invitarme tú a comer. Un trato es un trato."
    mc "Y así es como se consigue una tercera cita. *Risa*"
    call BlinkXPS3 ("c21s003_265" , "d") from _call_BlinkXPS3_261
    kia "Vale, pero la próxima vez será para cenar. Tener que volver al trabajo con prisa no es lo mejor... para una tercera cita."
    mc "Aún tenemos tiempo para ese paseo. Has dicho que tienes que volver en 30 minutos. Que ya deben ser 28."
    mc "Déjame ir al mostrador a pagar, así ganaremos un par de minutos."
    scene c21s003_270a with fade
    "Menos de diez minutos después, en un parque cercano..."
    kia "Y aquí es dónde vengo a comerme los perritos calientes cuando tengo que comer sola. Un libro y mi perrito."
    mc "Lo sé. Vinimos con [sca], en vuestro primer día en casa."
    call BlinkXPS3 ("c21s003_275" , "d") from _call_BlinkXPS3_262
    kia "¡Es verdad! ¡Parece que hace un mes!"
    mc "Mañana hace una semana, [kia]."
    call BlinkXPS3 ("c21s003_280" , "d") from _call_BlinkXPS3_263
    kia "Lo sé. Parece increíble que en una semana mi vida haya dado este vuelco."
    mc "Pero ¿estás contenta de que lo haya dado?"
    call BlinkXPS3 ("c21s003_285" , "d") from _call_BlinkXPS3_264
    kia "No te puedes imaginar cuánto. Y no me refiero sólo a estar contigo. Es todo. Me siento libre por primera vez en años."
    kia "¿Te acuerdas hace unos días, cuando te dije que teníais un castillo precioso como hogar y todas esas tonterías?"
    mc "Fue ayer, [kia]. Estábamos en la piscina, durante la fiesta de cumpleaños."
    call BlinkXPS3 ("c21s003_290" , "d") from _call_BlinkXPS3_265
    kia "¿Ayer? ¿No te lo dije durante la comida con [ama]? Se me mezclan los días... todo ha sido tan intenso..."
    mc "*Risa* Durante la comida con [ama] es cuando saliste corriendo. Eso fue anteayer."
    kia "Me estoy volviendo loca. Todo parece que haya pasado hace muchísimo..."
    call BlinkXPS3 ("c21s003_295" , "d") from _call_BlinkXPS3_266
    kia "Sentirme aceptada por la familia, besarte ayer... por la tarde... hablar con todas las chicas después de eso... y lo que pasó por la noche..."
    kia "Yo llevaba una vida aburrida donde todos los días eran iguales..."
    mc "En casa nunca hay tiempo para aburrirse. Te adaptaste a la familia. También te adaptarás a esto."
    call BlinkXPS3 ("c21s003_300" , "d") from _call_BlinkXPS3_267
    kia "Lo sé, pero ahora mismo, la última semana es un torbellino de recuerdos."
    kia "Llegar a casa, la fiesta en la playa, cuando fuimos a mi antigua casa, intentar evitarte, la fiesta de cumpleaños... el beso... y lo de anoche."
    if eil._var("pregnancyDiscovered"):
        kia "Que voy a ser abuela..."
    kia "Casi no puedo poner los recuerdos en el orden correcto."
    call BlinkXPS3 ("c21s003_305" , "d") from _call_BlinkXPS3_268
    kia "Y ni siquiera hace una semana..."
    mc "Te han pasado muchas cosas importantes en esta semana. Es normal. A veces a mí también me cuesta."
    mc "Pero tengo una pregunta... Después del beso de ayer por la tarde, las chicas te secuestraron durante un buen rato. ¿Qué te dijeron?"
    call BlinkXPS3 ("c21s003_310" , "d") from _call_BlinkXPS3_269
    kia "*Risa* ¡Es una cosa entre chicas! Te puedo decir que todas me felicitaron por haber dejado atrás el pasado."
    kia "Algunas, aunque no te voy a decir quienes, me dieron consejos sobre ti."
    mc "*Risa* ¡Eso es injusto! ¿Habláis de mi a mis espaldas?"
    call BlinkXPS3 ("c21s003_315" , "d") from _call_BlinkXPS3_270
    kia "*Risa* Obviamente. Y duermo con [eil], que es quien más tiempo ha salido contigo."
    kia "Ya te dije que se pasó buena parte de la noche hablándome de ti e intentando convencerme para..."
    mc "Tengo que hablar con ella. No es lo que quería decir cuando le pedía ayuda."
    call BlinkXPS3 ("c21s003_320" , "d") from _call_BlinkXPS3_271
    kia "Sin su insistencia, no hubiéramos hablado anoche en el pasillo ni en la piscina, ni hubiéramos paseado después. Ni estaríamos aquí hoy."
    kia "Ni podría hacer esto."
    scene c21s003_345a with dissolve
    "[kia] te sorprende con un beso en los labios. Tierno y pasional a partes iguales."
    "No es muy largo, pero puedes leer muchas cosas en él. Alivio, felicidad, esperanza..."
    call BlinkXPS3 ("c21s003_325" , "d") from _call_BlinkXPS3_272
    kia "Ya no aguantaba más."
    mc "¡Wow!"
    call BlinkXPS3 ("c21s003_330" , "d") from _call_BlinkXPS3_273
    kia "¿Quieres quitar esa sonrisa de tu cara? ¡La gente va a empezar a mirarnos!"
    mc "¡Wow!"
    call BlinkXPS3 ("c21s003_335" , "d") from _call_BlinkXPS3_274
    kia "¡[mc], por favor! ¡Deja de hacer el tonto!"
    mc "¡Wow! *Risa* Me acabo de enamorar del sabor de aguacate mezclado con tu pintalabios."
    call BlinkXPS3 ("c21s003_340" , "d") from _call_BlinkXPS3_275
    kia "*Risa* ¿Todavía tengo sabor a aguacate?"
    mc "Muy ligero, pero todavía se nota. *Risa* Creo que puedo añadir otra cosa verde al menú. Pero lo tendré que comer de tus labios."
    scene c21s003_345b with dissolve
    "La bibliotecaria pelirroja atrae tu cabeza hasta su altura y vuelve a besarte de una forma que las bibliotecarias deberían tener prohibida."
    "Esta vez es todo pasión, sin rastro de ternura. Pasea su lengua por tus encías, la entrelaza con la tuya, recorre toda tu boca... Te deja sin aliento."
    "Bendito aguacate."
    call BlinkXPS3 ("c21s003_350" , "d") from _call_BlinkXPS3_276
    mc "¡Wow!"
    kia "*Respiración entrecortada* ¡Wow! *Risa* Tenía que colaborar con que lleves una dieta saludable."
    kia "Me podría pasar horas aquí haciendo esto y diciendo Wow. Pero, desafortunadamente, tengo que volver al trabajo."
    mc "Entonces vamos. No quiero que llegues tarde."
    call BlinkXPS3 ("c21s003_355" , "d") from _call_BlinkXPS3_277
    kia "Y tú has quedado con [ama]..."
    mc "Sí, me quiere comentar sus ideas sobre la empresa."
    call BlinkXPS3 ("c21s003_360" , "d") from _call_BlinkXPS3_278
    kia "*Risa* No estaba interrogándote. Sé que no estás con ella. Al menos aún..."
    mc "*Risa* Lo sé. Después de lo de ayer, no tengo secretos y no quiero tenerlos."
    stop music fadeout (1.5)
    mc "¿Vamos?"
    scene c21s003_365a with fade
    play music ("music/RayOfHope.ogg")
    "Unos minutos después, en la biblioteca, justo a la hora en que [kia] tenía que volver..."
    kia "Ya estoy aquí, Gen. Puedes hacer tu pausa para la comida cuando quieras."
    mc "Hola de nuevo, Gen."
    gen "Justo a tiempo, me estaba muriendo de hambre. La biblioteca está vacía, no queda nada pendiente."
    scene c21s003_365b with dissolve
    kia "Pues el puesto de perritos calientes tiene bastante cola ahora. Si necesitas más tiempo no hay ningún problema."
    gen "[kia]... ¿dónde está tu bolso?"
    call BlinkXPS3 ("c21s003_370" , "h") from _call_BlinkXPS3_279
    kia "¡Mierda! Me lo he dejado en el restaurante."
    scene c21s003_365c with dissolve
    kia "¿Puedes cubrirme diez minutos mientras voy a buscarlo?"
    gen "Ningún problema. Ve a ver si lo han encontrado antes de que desaparezca."
    mc "No os preocupéis, voy a llamarles y voy a buscarlo, voy a llegar más rápido que tú con los tacones. Ahora lo traigo."
    mcp "(Espero que siga allí o que lo haya encontrado el camarero cuando nos hemos ido.)"
    call BlinkXPS3 ("c21s003_375" , "d") from _call_BlinkXPS3_280
    kia "Gracias, [mc]. ¿Aviso a [ama] de que vas a llegar tarde?"
    mc "Sí, por favor."
    scene black with dissolve
    "Sales de la biblioteca y empiezas a correr hacia el restaurante mientras les llamas. No cogen el teléfono."
    "Llegas un par de minutos después. Nunca habías corrido tan rápido en tu vida."
    scene c21s003_365d with dissolve
    "El camarero saca el bolso de la barra antes de que puedas recuperar el aliento para pedírselo."
    "Hubiera sido una forma horrible de acabar la segunda cita si [kia] hubiera perdido el bolso."
    scene black with dissolve
    "Vuelves corriendo a la biblioteca. No quieres que [kia] se preocupe por su bolso más de lo necesario. Corres un poco más lento."
    "Quieres mantener un poco de dignidad cuando llegues, y fregar la biblioteca con la lengua no es la mejor forma de hacerlo."
    stop music fadeout (1.5)
    scene c21s003_365e with dissolve
    "Cuando estás a punto de entrar, oyes voces..."
    play music ("music/Tribal.ogg")
    kia "...¡Me da lo mismo que tenga edad para ser mi hijo!"
    gen "[kia], lo digo por tu bien. Los chavales como él sólo quieren una cosa en una mujer de tu edad..."
    kia "Él es diferente..."
    gen "Si supieras las veces que he oído eso..."
    mcp "(Es el momento de intervenir.)"
    scene c21s003_365f with fade
    mc "Hola, [kia], Sra. Sky. Vengo con el bolso. Lo había recogido el camarero en cuanto nos hemos ido."
    kia "¡Gracias a Dios!"
    gen "Gracias, [mc]. [kia] estaba muy preocupada. Y puedes seguir llamándome Gen..."
    scene c21s003_365g with dissolve
    "Ignoras a Geneviève y te arrodillas a los pies de [kia], poniendo el bolso en el suelo."
    call BlinkXPS3 ("c21s003_380" , "v") from _call_BlinkXPS3_281
    kia "¿Qué haces, [mc]?"
    mc "He oído como la Sra. Sky decía que los chavales como yo sólo queremos una cosa con mujeres como tú."
    call BlinkXPS3 ("c21s003_385" , "v") from _call_BlinkXPS3_282 #gen
    mc "No sé lo que quieren otros chavales como yo."
    call BlinkXPS3 ("c21s003_390" , "d") from _call_BlinkXPS3_283
    mc "Yo lo único que quiero es poner el mundo a tus pies, [kia]. Empiezo con un bolso."
    mc "Y también quiero callar a quien opina sobre nosotros sin saber nada sobre lo que hemos pasado."
    kia "Gracias, [mc], pero... ¿puedes levantarte?"
    call BlinkXPS3 ("c21s003_395" , "d") from _call_BlinkXPS3_284
    if mc._var("relationships")>1:
        "Estás enfadado. Mucho. Sabes que tus relaciones pueden hacer que se levante más de una ceja. Pero no estabas preparado para esto."
    else:
        "Estás enfadado. Mucho. Sabes que tu relación con [kia] puede hacer que se levante más de una ceja. Pero no estabas preparado para esto."
    mc "¿Has podido llamar a [ama]?"
    kia "Mi móvil estaba en el bolso... ni siquiera he pensado en ello, y no me he aprendido su número."
    mc "Entonces no te preocupes. Aún llego a tiempo."
    call BlinkXPS3 ("c21s003_400" , "d") from _call_BlinkXPS3_285
    gen "Siento si te he ofendido, [mc]. Sólo intentaba proteger a [kia]."
    "Está nerviosa. Sabe que ha metido la pata. Se le nota más aún el acento francés."
    mc "Me parece loable, pero debería informarse sobre lo que habla antes de decir algo de lo que pueda arrepentirse, Sra. Sky."
    "Tu tono es cortante. Ahora mismo no quieres dar explicaciones ni hablar con esta mujer."
    gen "Gen..."
    mc "Sólo acorto los nombres de mis amigos, Geneviève."
    call BlinkXPS3 ("c21s003_405" , "d") from _call_BlinkXPS3_286
    "Dulcificas tu tono cuando te diriges a [kia]."
    mc "Voy a ir a lo de [ama] antes de que se haga tarde."
    kia "Gracias de nuevo, [mc]."
    mc "Te veo en casa, cielo."
    call BlinkXPS3 ("c21s003_410" , "d") from _call_BlinkXPS3_287
    kia "Espera un momento..."
    mc "¿Falta algo en el bolso?"
    kia "Ni lo sé ni me importa."
    "El bolso continúa en el suelo, donde los has dejado."
    scene c21s003_365h with hpunch
    "[kia] se lanza a tus labios para sorpresa tuya y de Geneviève. Tú has defendido vuestra relación a tu manera."
    "Ella la defiende a la suya."
    "Demostrándole a Geneviève que sus palabras no han conseguido sembrar ninguna duda."
    "También te lo quiere demostrar a ti."
    "Todavía sabe a aguacate."
    call BlinkXPS3 ("c21s003_415" , "d") from _call_BlinkXPS3_288
    kia "¡Wow! *Risa*"
    mc "¡Wow! *Risa*"
    call BlinkXPS3 ("c21s003_420" , "d") from _call_BlinkXPS3_289
    kia "Gracias por todo, cielo."
    "Ese \"por todo\" incluye dar la cara por ella. Quizás por primera vez en su vida alguien lo ha hecho."
    mc "Te veo en casa, preciosa."
    call BlinkXPS3 ("c21s003_425" , "d") from _call_BlinkXPS3_290
    mc "Adiós, Geneviève."
    stop music fadeout (1.5)
    "Te marchas mientras escuchas la despedida murmurada de Geneviève."
    scene black with dissolve
    return
label c21s004_AmandaCoffee:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_7
        menu:
            "¿Estás en una relación con [kia]?"
            "Sí":
                $ kia._var("route" , True)
            "No":
                $ kia._var("route" , False)
    call BlinkXPS3 ("c21s004_005" , "f") from _call_BlinkXPS3_291
    "Llegas al café donde has quedado con [ama]. Era un sitio que no habías visitado nunca anteriormente, pero has venido varias veces en las últimas semanas."
    play music ("music/On-The-Rise.ogg")
    "[ama] ya está allí, con un café y un portátil sobre la mesa."
    call BlinkXPS3 ("c21s004_010" , "d") from _call_BlinkXPS3_292
    mc "Hola, [ama]. No te levantes. ¿Llevas mucho esperando? No llego tarde, ¿verdad?"
    ama "No te preocupes, llevo diez minutos aquí tan solo. He llegado antes de la hora. Y tú llegas super puntual."
    mc "Nunca me ha parecido bien hacer esperar a nadie. Lo considero una falta de respeto hacia el tiempo de los demás."
    call BlinkXPS3 ("c21s004_015" , "d") from _call_BlinkXPS3_293
    ama "No sé cómo lo consigues. Los civiles tenéis unas vidas muy complicadas con un montón de cosas por hacer que se solapan."
    call BlinkXPS3 ("c21s004_020" , "d") from _call_BlinkXPS3_294
    ama "Casi echo de menos la vida organizada de la base en la que siempre sabes qué tienes que hacer a qué hora. Solo casi."
    mc "Yo estoy pensando en fichar una secretaria. *Risa*"
    call BlinkXPS3 ("c21s004_025" , "d") from _call_BlinkXPS3_295
    ama "¿Más mujeres a tu alrededor? *Risa* ¿No tienes suficientes?"
    mc "*Risa* Estaba pensando en fichar a Meemaw para eso. *Risa* Al menos se mantendría activa y se sentiría útil."
    mc "Además, evitaría tener que informar a más personas de los secretos familiares."
    call BlinkXPS3 ("c21s004_030" , "d") from _call_BlinkXPS3_296
    ama "Los secretos parece que van a dejar de serlos. He hablado con [aar] esta mañana. ¿Ha conseguido contactar contigo?"
    mc "Sí, hemos estado hablando sobre la compañía que quiere comprar NTR... ¿Iron Fist se llamaban?"
    call BlinkXPS3 ("c21s004_035" , "d") from _call_BlinkXPS3_297
    ama "Sí, son unos capullos, aunque efectivos."
    ama "Su concepto de operaciones encubiertas es que si no hay supervivientes nadie puede informar. Tienen la sutileza de un ariete... o de [emm]."
    mc "*Risa* No es la primera vez que comparan la sutileza de [emm] con un ariete."
    mc "Pero hablando de Iron Fist, tienen que ser enormes si pueden pagar los nueve o diez dígitos que [aar] dijo que valía NTR."
    call BlinkXPS3 ("c21s004_040" , "d") from _call_BlinkXPS3_298
    ama "No, no lo son. Son grandes, pero más pequeños que nosotros. Quieren aprovechar el vacío de poder para comprar NTR por una fracción de su valor."
    ama "Comprarnos casi triplicaría su cifra de negocio y les proporcionaría contratos a los que no tienen acceso ahora mismo."
    ama "Su negocio de operaciones especiales es algo menos de la mitad del nuestro. Y estamos hablando de cientos de millones."
    mc "Eso es un montón de dinero. ¿Tantas operaciones especiales se hacen?"
    call BlinkXPS3 ("c21s004_045" , "d") from _call_BlinkXPS3_299
    ama "Se hacen muchas. Y son caras. Iron Fist trabaja mucho con los gobiernos de países que Estados Unidos no considera amigables."
    ama "Por eso no tienen acceso a algunos contratos."
    call BlinkXPS3 ("c21s004_050" , "d") from _call_BlinkXPS3_300
    ama "Los clientes principales de NTR son precisamente Estados Unidos y otros países occidentales que no se quieren manchar las manos haciendo algunas cosas."
    ama "Pagan MUY bien por evitar salir en la prensa si algo sale mal."
    mc "Lo entiendo. Como una misión en Burkina Faso donde envían a dos niñas de 14 años. Quedaría mal en la prensa si se emborrachan."
    call BlinkXPS3 ("c21s004_055" , "d") from _call_BlinkXPS3_301
    ama "Sí, a eso me refiero. Esa misión no la podían hacer los Navy SEAL. *Risa* Y no solo porque Burkina no tenga mar."
    ama "Y por eso quería hablar contigo sobre el futuro de NTR. He hecho algunos números con la información que me ha enviado [aar]..."
    mc "Déjame pedir un café y me lo explicas."
    call BlinkXPS3 ("c21s004_070a" , "d") from _call_BlinkXPS3_302
    "[ama] pasa unos 20 minutos explicándote la situación del negocio, hasta que llega a la parte más interesante. El dinero."
    scene c21s004_060b with dissolve
    ama "La parte médica de la compañía es el 12\% de la facturación global de NTR. El 71\% de la facturación proviene de operaciones de Seguridad."
    ama "Puedes ver aquí la mala noticia. La parte médica es la que menos dinero da. Es imposible basar la compañía sólo en eso ahora mismo."
    mc "¿Qué es ese concepto? ¿Servicios de Apoyo?"
    call BlinkXPS3 ("c21s004_065" , "d") from _call_BlinkXPS3_303
    ama "Alquiler de Equipos y Soporte Logístico, básicamente. A otras compañías como NTR, pero más pequeñas. Transporte de operativos, alquiler de equipos, etc."
    mc "¿Podríamos mantener esa parte de la Compañía? No nos involucraríamos en Operaciones Especiales con eso, ¿no?"
    call BlinkXPS3 ("c21s004_070b" , "d") from _call_BlinkXPS3_304
    ama "Déjame mirar una cosa..."
    ama "No sería difícil de hacer. Tenemos los contactos y, si dejamos de ser su competencia, otras compañías podrían requerir nuestros servicios."
    call BlinkXPS3 ("c21s004_070c" , "d") from _call_BlinkXPS3_305
    ama "Bien pensado, pero habría que estudiarlo bien. Y no, no nos involucramos en las operaciones de otras compañías. Solo les damos apoyo."
    mc "Dale trabajo a [aar]. *Risa* Creo que, de momento, sería bueno mantener esa fuente de ingresos."
    mc "Has dicho que es la mala noticia. ¿Hay una buena?"
    scene c21s004_060c with dissolve
    ama "Sí, esta. Y con lo que acabas de decir de mantener los Servicios de Apoyo, es incluso mejor."
    ama "La facturación crece en las tres áreas cada año, pero el crecimiento en el área de Seguridad es casi residual, entre un 2\% y un 5\%."
    ama "El crecimiento en los Servicios de Apoyo es de entre un 15\% y un 18\% anual."
    mc "Eso es una barbaridad de crecimiento."
    call BlinkXPS3 ("c21s004_075" , "d") from _call_BlinkXPS3_306
    ama "La facturación de la parte médica crece entre el 50\% y el 60\%. Y acelerando. Hemos empezado muy abajo y es fácil crecer."
    ama "Es la partida más pequeña, pero el año que viene seguramente superará a los Servicios de Apoyo."
    mc "Déjame hacer unos cálculos..."
    call BlinkXPS3 ("c21s004_080" , "f") from _call_BlinkXPS3_307
    mc "En cinco años, con ese ritmo de crecimiento, podría ser la principal área de negocio."
    ama "Y en dos años, combinada con los Servicios de Apoyo, superarían al área de Seguridad. Yo también he hecho los cálculos."
    scene c21s004_080An with dissolve
    "[ama] pasa los siguientes minutos explicándote todos los cálculos que ha hecho y cómo su plan puede ser realizable."
    "A veces tiene que parar para hacer algún cálculo nuevo debido a la posibilidad de mantener los Servicios de Apoyo."
    "Son cálculos que aburrirían a cualquiera que no fuera un empollón. Por suerte ambos lo sois."
    call BlinkXPS3 ("c21s004_085" , "f") from _call_BlinkXPS3_308
    ama "Y eso sería todo. Creo que, económicamente, el plan es realizable."
    mc "Le veo un problema. ¿Qué hacemos con vosotras? ¿Y con los XY?"
    call BlinkXPS3 ("c21s004_090" , "d") from _call_BlinkXPS3_309
    ama "También he pensado en eso, pero necesito modificarlo."
    ama "No estoy segura de que todos los XY quieran abandonar la vida que llevan. Las misiones dan mucha adrenalina, son como una droga."
    mc "Pero vosotras sí que queréis dejar esas misiones."
    call BlinkXPS3 ("c21s004_095" , "d") from _call_BlinkXPS3_310
    ama "Nosotras somos diferentes. Envejecemos a un ritmo normal. Ellos saben que tienen una juventud limitada y querrán sacarle el máximo partido."
    ama "[eva] y yo nos conformaríamos con un trabajo normal."
    mc "¿Como jefas de seguridad de la base, por ejemplo? Había pensado en eso como opción. En el fondo, la empresa también es vuestra."
    call BlinkXPS3 ("c21s004_100" , "h") from _call_BlinkXPS3_311
    ama "¿Qué? ¡No! ¿Por qué quieres hacernos esto?"
    mc "¿Qué? ¿Haceros qué?"
    call BlinkXPS3 ("c21s004_105" , "d") from _call_BlinkXPS3_312
    ama "¡Mandarnos lejos!"
    ama "¡Os acabamos de encontrar!"
    call BlinkXPS3 ("c21s004_110" , "d") from _call_BlinkXPS3_313
    ama "¡[eva] y yo incluso hemos resuelto nuestras diferencias respecto a ti!"
    mc "No os quiero mandar lejos, [ama]. Yo también voy a ir a Aruba."
    call BlinkXPS3 ("c21s004_115" , "d") from _call_BlinkXPS3_314
    ama "Pero tu volverás... y nosotras, si somos las jefas de seguridad, nos tendremos que quedar allí..."
    if persistent.walkthrough:
        $ wt1 = _("Ruta con [ama] abierta.")
        $ wt2 = _("Ruta con [ama] cerrada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Te quiero cerca de mí." (wt = wt1):
            $ ama._var("route" , True)
        "Quiero que seas parte de la familia." (wt = wt2):
            pass
    $ resetWalkthrough ()
    mc "También necesitaremos a alguien que proteja a los accionistas, ¿no?"
    mc "Y no se me ocurre nadie mejor que vosotras. Podéis turnaros, no sé... ¿Una semana cada una en Aruba mientras la otra está aquí con la familia?"
    if ama._var("route"):
        call BlinkXPS3 ("c21s004_120a" , "d") from _call_BlinkXPS3_315
        ama "Espera... has dicho que me quieres cerca de ti... ¿Significa eso que...?"
        mc "Sí, [ama]. Significa que, si quieres, me encantaría salir contigo."
        mc "Sólo estaba esperando a que [eva] y tú aclararais las cosas para decírtelo."
        call BlinkXPS3 ("c21s004_125" , "d") from _call_BlinkXPS3_316
        ama "¿Decírmelo? ¿Sólo a mí? ¿No quieres estar con [eva]?"
        mc "Eso es algo que [eva] y yo tenemos que hablar. A solas. Los dos. Independientemente de si quiero estar con ella o no."
        ama "Lo entiendo..."
        call BlinkXPS3 ("c21s004_135" , "d") from _call_BlinkXPS3_317
        ama "¿Significa eso que... puedo besarte?"
        mc "No, significa que ahora vamos a tirar las tazas al suelo y vamos a follar encima de la mesa. *Risa*"
        call BlinkXPS3 ("c21s004_130" , "d") from _call_BlinkXPS3_318
        ama "¿Qué? ¿Ahora? ¿Aquí?"
        mc "*Risa* Tenemos que trabajar en tu detección del sarcasmo."
        call BlinkXPS3 ("c21s004_140" , "d") from _call_BlinkXPS3_319
        mc "Claro que vamos a besarnos. ¿Me permites?"
        scene c21s004_145pv with dissolve
        show c21s004_145v
        "[ama] se levanta como impulsada por un muelle y ataca tus labios con furia."
        "\"Atacar\" es la palabra adecuada."
        "Hay furia y pasión en su beso. Creías que iba a ser un beso tímido, pero no podías estar más equivocado."
        "Sólo se separa de tus labios cuando le falta el aire."
        call BlinkXPS3 ("c21s004_150" , "d") from _call_BlinkXPS3_320
        hide c21s004_145v
        ama "¡Wow!"
        mc "*Risa* Estoy de acuerdo. ¡Wow!"
        call BlinkXPS3 ("c21s004_155" , "d") from _call_BlinkXPS3_321
        ama "*Risa* No te rías de mí. Llevo días queriendo hacer esto..."
        call BlinkXPS3 ("c21s004_160" , "d") from _call_BlinkXPS3_322
        ama "¿Sabes cuando quieres algo durante mucho tiempo y lo consigues...? ¿Ese sentimiento de decepción? ¿De vacío al cumplir el objetivo?"
        mc "Sí, conozco ese sentimiento. ¿Decepcionada?"
        call BlinkXPS3 ("c21s004_165" , "d") from _call_BlinkXPS3_323
        ama "*Risa* Tenemos que trabajar en tu costumbre de interrumpir a la gente cuando habla."
        ama "Quería decir que esperaba ese sentimiento, pero no se ha dado. *Risa* Al revés. Tengo ganas de ignorar tu sarcasmo y tirar las tazas al suelo."
        mc "*Risa* Tengo que ser una bestia besando."
        call BlinkXPS3 ("c21s004_170" , "d") from _call_BlinkXPS3_324
        ama "*Risa* No voy a decir ni que sí ni que no. No quiero alimentar tu ego más de lo que ya lo está."
        scene c21s004_175AnBlink with dissolve
        "Te da un rápido beso."
        ama "Siéntate donde estabas, voy al lavabo un momento y seguimos con la reunión."
        mc "¿No quieres que me siente a tu lado?"
        ama "Sí, pero si lo haces no vamos a poder acabar con lo que hemos venido a hacer. Si hay una mesa entre los dos puedo mantener la cabeza centrada en la reunión."
        scene c21s004_175e
        ama "Más o menos."
    else:
        call BlinkXPS3 ("c21s004_120b" , "d") from _call_BlinkXPS3_325
        ama "Espera... Has dicho que quieres que forme parte de la familia, pero no has dicho nada de nosotros."
        ama "¿Significa eso que tú y yo...?"
        mc "Significa que quiero que formes parte de nuestras vidas. Me caes muy bien, [ama], pero a diferencia de ti, te conozco tan solo desde hace unos días."
        call BlinkXPS3 ("c21s004_180" , "d") from _call_BlinkXPS3_326
        mc "No he tenido tiempo de desarrollar sentimientos por ti, y... no creo que lo haga en el futuro. Al menos no como tú quieres."
        mc "Despiertas en mí un sentimiento de protección, pero no uno romántico."
        mc "No quiero darte falsas esperanzas. Creo que tengo que ser sincero sobre eso."
        mc "Que [eva] y tú hayáis tardado tanto en resolver vuestras diferencias, me ha dado tiempo a mí para examinar lo que siento hacia vosotras."
        call BlinkXPS3 ("c21s004_185" , "d") from _call_BlinkXPS3_327
        ama "Lo entiendo y te agradezco la sinceridad..."
        ama "¿Te pasa lo mismo con [eva]? No sé si te va a arrancar la cabeza si le dices algo así."
        mc "Eso es algo que [eva] y yo tenemos que hablar. A solas. Los dos. Independientemente de si quiero estar con ella o no."
        call BlinkXPS3 ("c21s004_190" , "d") from _call_BlinkXPS3_328
        ama "Tienes razón, no debería inmiscuirme."
        ama "Dame un segundo, voy al lavabo."
        mc "El tiempo que necesites."
    call BlinkXPS3 ("c21s004_195" , "f") from _call_BlinkXPS3_329
    "Unos minutos después..."
    ama "Volviendo al tema de los XY..."
    mc "¿No quieres hablar de lo que acaba de pasar?"
    call BlinkXPS3 ("c21s004_200" , "d") from _call_BlinkXPS3_330
    ama "Prefiero no hacerlo ahora. Tenemos que acabar esto y tengo que relevar a [eva]."
    if ama._var("route"):
        ama "Si empiezo a hablar de lo que ha pasado, no vamos a parar y voy a pasarme horas besándote."
        ama "Tendremos mucho tiempo para hablar cuando llegue el momento. Ahora tenemos una reunión que terminar."
    else:
        ama "No tiene sentido hablarlo. Sentimos cosas diferentes por el otro, pero ni quiero ni puedo forzarte a sentir lo que siento yo."
        ama "No me debes ninguna explicación ni yo la quiero, pero tenemos una reunión que terminar."
    mc "De acuerdo, sigamos entonces."
    call BlinkXPS3 ("c21s004_205" , "d") from _call_BlinkXPS3_331
    ama "Contamos con 109 efectivos XY operativos ahora mismo. Aparte de eso hay 19 inoperativos."
    ama "En los próximos diez años, 461 más completarán su crecimiento y formación."
    mcp "(Acaba de aparecer la [ama] fría y profesional para separarse emocionalmente de lo que acaba de pasar.)"
    call BlinkXPS3 ("c21s004_210" , "d") from _call_BlinkXPS3_332
    ama "Como ya te he dicho, si les damos opciones, no todos van a querer abandonar las Operaciones Especiales."
    ama "Pero podremos reubicar a la mayoría en operaciones de Apoyo o en seguridad de la base, especialmente a los nuevos."
    mc "Creo que tenemos que darles la opción de decidir. Tienen tanto derecho como tú o como yo."
    mc "Incluso si quieren desvincularse totalmente de NTR deberíamos aceptarlo."
    mc "¿Cuánta seguridad necesitamos en la base?"
    call BlinkXPS3 ("c21s004_215" , "d") from _call_BlinkXPS3_333
    ama "Ahora mismo hay 36 en tres turnos. Casi todos de las Series J y K, la última y la próxima en ser considerada operativa. Les sirve como entrenamiento."
    scene c21s004_060d with dissolve
    ama "Aquí puedes ver las estadísticas por series. De la K a la T todavía están en crecimiento y formación."
    mc "Hay mucho rojo, incluso entre las series que no han entrado en servicio. Demasiado rojo."
    ama "Alrededor del 7\% son bajas durante el entrenamiento, como Fiona. El resto son bajas operativas. Sumadas al entrenamiento, alrededor del 32\% son bajas."
    mc "Si seguimos con el entrenamiento, hay que cambiar los métodos. No quiero que niños pequeños mueran jugando con explosivos."
    mc "Y me da lo mismo que tengan cuerpos de adultos. No quiero. Punto."
    call BlinkXPS3 ("c21s004_220" , "d") from _call_BlinkXPS3_334
    ama "Me sorprende la empatía que tienes hacia gente que no conoces."
    mc "Os conozco a [eva] y a ti. Y a [aar], aunque sea poco. Tengo suficiente."
    mc "¿Quién se encarga del entrenamiento ahora mismo?"
    call BlinkXPS3 ("c21s004_225" , "d") from _call_BlinkXPS3_335
    ama "Los C y los D, principalmente. Los entrenan como fueron entrenados ellos. Como fuimos entrenadas nosotras."
    mc "Lo primero que quiero hacer cuando llegue a Aruba, entonces, es reunirme con los C y los D. Y quiero sus nombres. No quiero pensar en ellos como letras."
    scene c21s004_225An with dissolve
    "Pasáis los siguientes minutos haciendo planes y números, modificando las ideas de [ama], ampliando la información que tienes sobre la empresa. Tomando más cafés."
    "Al cabo casi una hora, suena una alarma en el móvil de [ama]."
    call BlinkXPS3 ("c21s004_230" , "d") from _call_BlinkXPS3_336
    ama "Voy a tener que irme. Me toca relevar a [eva]. Lleva casi 30 horas sin dormir."
    ama "Recopilaré todos los datos y te los mando. Supongo que en un par de días los tendré hechos."
    mc "Genial. ¿Vais a venir a casa a cenar esta noche?"
    call BlinkXPS3 ("c21s004_235" , "d") from _call_BlinkXPS3_337
    ama "Sí, hemos ido a comer, pero no estabas."
    if kia._var("route"):
        mc "Ya sabes que había quedado para comer con [kia]."
    else:
        mc "Ya sabes que tenía que llevar a [meg] a la estación de autobuses."
    ama "Lo sé..."
    call BlinkXPS3 ("c21s004_240" , "d") from _call_BlinkXPS3_338
    ama "Entonces te veo esta noche."
    if ama._var("route"):
        scene c21s004_145pv with dissolve
        "[ama] se vuelve a lanzar a tus labios, esta vez sin el ansia del beso anterior. Sabe que vendrán más."
    else:
        scene c21s004_245a with dissolve
        "Os dais un abrazo de despedida. Tácitamente, sin necesidad de palabras, habéis decidido que los besos de despedida están de más ahora que habéis aclarado que no estaréis juntos."
    call BlinkXPS3 ("c21s004_250" , "d") from _call_BlinkXPS3_339
    ama "Hasta la noche, [mc]."
    stop music fadeout (1.5)
    mc "Hasta la noche, [ama]."
    scene black with dissolve
    return
label c21s005_DebRun:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_8
        menu:
            "¿Estás en una relación con [deb.nick]?"
            "Sí":
                $ deb._var("route" , True)
                $ mc._var("relationships", 1, intention = "set")
            "No":
                $ deb._var("route" , False)
                $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con [mar]?"
            "Sí":
                $ mar._var("route" , True)
                $ mc._var("relationships", 1)
                menu:
                    "¿Sabe que está embarazada?"
                    "Sí":
                        $ mar._var("pregnancyDiscovered" , True)
                    "No":
                        $ mar._var("pregnancyDiscovered" , False)
            "No":
                $ mar._var("route" , True)
        if mc._var("relationships")<2:
            menu:
                "¿Cuántas relaciones tienes?"
                "Más de una":
                    $ mc._var("relationships", 2, intention = "set")
                "Una":
                    $ mc._var("relationships", 1, intention = "set")
                "Ninguna" if mc._var("relationships")==0:
                    $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Le dijiste a [kat] que debía comer sano (con lo que perdería peso) además de hacer más deporte?"
            "Sí":
                $ kat._var("slim" , True)
            "No":
                $ kat._var("slim" , True)
    call BlinkXPS3 ("c21s005_005" , "d") from _call_BlinkXPS3_340
    "Al llegar a casa te encuentras con [deb.nick] en la puerta."
    play music ("music/Morning-Sun.ogg")
    deb "Buenas tardes, [mc]."
    if deb._var("route"):
        call KissXPS3 ("c21s005_010" , "d") from _call_KissXPS3_3
        mc "Buenas tardes, cielo."
    else:
        mc "Buenas tardes, [deb.nick]."
    mc "¿Sales a correr o vuelves ahora?"
    call BlinkXPS3 ("c21s005_015" , "d") from _call_BlinkXPS3_341
    deb "Salgo ahora. Iba a ir al lago. [kim] y [kat] han salido hace un rato."
    mc "Si me das cinco minutos para cambiarme, te acompaño."
    deb "¡Genial! Te espero en la piscina. [lis] está allí."
    if deb._var("route"):
        call KissXPS3 ("c21s005_010" , "d") from _call_KissXPS3_4
    mc "Hasta ahora."
    scene c21s005_020a with fade
    "Unos minutos después..."
    mc "Hola, [lis]."
    lis "Hola, [mc]. No contéis conmigo para ir a correr. [deb.nick] estaba intentando convencerme."
    if not _in_replay:
        $ lis.profileImages.pop (13) # first remove
        $ lis.profileImages.insert (13, ("lisa_13", None)) # then add new
        $ texto = str(lis.name)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless")
        $ kia.profileImages.pop (1) # first remove
        $ kia.profileImages.insert (1, ("kiara_1", None)) # then add new
        $ eri.profileImages.pop (7) # first remove
        $ eri.profileImages.insert (7, ("erika_7", None)) # then add new
    deb "[lis] prefiere quedarse leyendo y tomando el sol. *Risa*"
    mc "¿Qué estás leyendo?"
    call BlinkXPS3 ("c21s005_025" , "d") from _call_BlinkXPS3_342
    lis "Teoría política. Alguien me hizo pensar el otro día en el Jazz Corner y lo he cogido de la biblioteca de la universidad."
    mc "Siempre es bueno ampliar horizontes."
    lis "No sé si me llevará a algo, pero al menos estoy leyendo información de la que no sabía nada."
    call BlinkXPS3 ("c21s005_030" , "d") from _call_BlinkXPS3_343
    deb "[lis] for President! *Risa* Nuestro ejército sería el mejor vestido del mundo. ¡Giovanni Armani para todos!"
    mc "*Risa* Puede sonar a broma, pero posiblemente la votara dependiendo de su programa."
    call BlinkXPS3 ("c21s005_035" , "d") from _call_BlinkXPS3_344
    lis "*Risa* Mi hermana no confiaría en mí ni como delegada de clase."
    lis "Iros a correr antes de que se os haga más tarde. [kim] y [kat] ya deben estar allí."
    mc "Hasta luego, [lis]."
    call BlinkXPS3 ("c21s005_040" , "f") from _call_BlinkXPS3_345
    mc "Me acabo de dar cuenta de que no llevas mochila hoy. ¿No llevas toalla para bañarte en el lago después de subir corriendo?"
    mc "Yo la he cogido, y también el bañador."
    deb "Mi toalla y el bikini van camino del lago. Lo hemos metido todo en la mochila de [kat] para que suba hasta allí con más peso."
    deb "Si la hacemos correr con la mochila, con algo de peso, quemará más azúcar."
    mc "La estáis ayudando mucho por lo que me dijo el otro día."
    call BlinkXPS3 ("c21s005_045a" , "d") from _call_BlinkXPS3_346
    deb "[kim] se ocupa de hacerle correr, y yo de hacerle nadar."
    if not kat._var("slim"):
        deb "Si alguien se ocupara de hacerle comer sano, podríamos hacer una atleta de ella."
    else:
        deb "Y como [mar] se ocupa de que coma sano, acabará perdiendo mucho peso en los próximos meses."
    mc "No sé si me puedo imaginar a una [kat] atlética. *Risa* A menos que hayan hecho olímpico el levantamiento de pizza."
    call BlinkXPS3 ("c21s005_045b" , "d") from _call_BlinkXPS3_347
    deb "Si lo hicieran, Tía [bet] seguro que se llevaba una medalla. *Risa*"
    if kat._var("slim"):
        deb "Y la pobre [kat] se moriría de envidia. Lleva casi una semana comiendo más sano. Pero aún mira las pizzas de Tía [bet] con envidia."
    else:
        deb "[kat] está comiendo algo más sano, pero todavía no es capaz de resistirse a la pizza, o a los croissants... o a los donuts."
    mc "Resistirse a la pizza es muy duro. *Risa*"
    scene c21s005_100pv with fade
    show c21s005_100v
    deb "¿Y tú? ¿Vas a unirte a alguno de nuestras sesiones de deporte?"
    mc "Me gustaría hacerlo más regularmente, pero es casi imposible. Cuando no es una cosa es otra la que me mantiene ocupado."
    mc "Pero ahora estoy aquí, con lo que podemos contar esto como unirme, ¿no?"
    deb "Sí, pero estoy segura de que todo el mundo te daría la bienvenida si te unieras a las sesiones de yoga."
    mc "*Risa* Me uní una vez, y no soy demasiado flexible. Fue divertido y hacía mucho que no salía a la terraza."
    deb "Ahora lo hacemos en la piscina. La terraza estaba demasiado atestada en cuanto nos unimos [kim], [lis], Tía [bet], y yo."
    mc "Quizás un día me una, si me levanto pronto y tengo ganas de que os riais de mí."
    if deb._var("route"):
        call BlinkXPS3 ("c21s005_050a" , "d") from _call_BlinkXPS3_348
        mc "¿Pasa algo? ¿Por qué te paras? ¿Te has hecho daño?"
        deb "No es eso... estamos a punto de llegar, y... quería besarte antes de hacerlo. No sé si me atreveré delante de las chicas."
        mc "Saben que estamos juntos, con lo que no debería importarles."
        mc "Pero nunca voy a rechazar un beso tuyo, aunque sigan siendo a escondidas. Ven aquí abajo."
        scene c21s005_050An with dissolve
        "Los labios de [deb.nick] recorren los tuyos con tranquilidad. Su lengua es más ansiosa recorriendo tu boca."
        "Es una lástima que, debido a su timidez, no vaya a repetirlo una vez lleguéis al lago."
        call BlinkXPS3 ("c21s005_050b" , "d") from _call_BlinkXPS3_349
        deb "Besarte se ha convertido en mi vicio favorito..."
        mc "*Risa* Yo creía que eras una chica sin vicios, [deb.nick] Selden."
        call BlinkXPS3 ("c21s005_050c" , "d") from _call_BlinkXPS3_350
        deb "Mis vicios sólo son con cosas sanas. *Risa*"
        deb "Vamos antes de que piensen que me ha pasado algo. No saben que he tenido que esperar a que te cambiaras."
        mc "Vamos."
    scene c21s005_055a with fade
    "Unos minutos después..."
    deb "[kat] ha subido más rápido de lo que pensaba. Me imaginaba que las pillaríamos por el camino."
    mc "Es su primera visita al lago, ¿verdad?"
    call BlinkXPS3 ("c21s005_060" , "d") from _call_BlinkXPS3_351
    deb "Sí, desde que le hablaste de él en el Jazz Corner quería subir aquí."
    deb "Hoy [kim] ha pensado que, como no hacía demasiado calor, sería un buen día para hacerlo."
    mc "Ha sido una buena idea. ¿Vamos antes de que se haga más tarde? Aún nos tenemos que cambiar."
    call BlinkXPS3 ("c21s005_065" , "d") from _call_BlinkXPS3_352
    deb "¡Vamos! Te echo una carrera."
    scene c21s005_055b with dissolve
    "[deb.nick] sale disparada sin esperar tu respuesta. Corre como una gacela con esas larguísimas piernas."
    "Bajas trotando, sabes que eres incapaz de pillarla antes de que llegue al lago."
    "Cuando llegas, ella ya se ha metido tras los arbustos para cambiarse."
    scene c21s005_055c with dissolve
    kat "¡Hola, [mc]! Veo que [deb.nick] te ha engañado de alguna forma para que subas hasta aquí. *Risa*"
    kim "Hola, [mc]."
    mc "Hola, chicas. Fui yo quien les enseñó este lago, [kat]. Siempre me ha gustado mucho subir aquí."
    mc "Voy a cambiarme, ahora vuelvo."
    scene black with dissolve
    pause (0.5)
    scene c21s005_055d with dissolve
    mc "Ya estoy. ¿[deb.nick] no ha terminado de cambiarse?"
    scene c21s005_055e with dissolve
    kim "No..."
    kat "Seguramente estará pensando qué bikini ponerse. Con lo que pesaba la mochila, debía llevar 100 o 200. Algunos de ellos hechos de plomo."
    call BlinkXPS3 ("c21s005_070" , "d") from _call_BlinkXPS3_353
    kim "¡Eres una exagerada! *Risa* La mochila no llevaba tantas cosas. Tres toallas, dos bikinis y tu bañador."
    kim "Y el agua... y la crema solar..."
    call BlinkXPS3 ("c21s005_075" , "d") from _call_BlinkXPS3_354
    kat "Entonces es que la mochila está hecha de plomo. *Risa*"
    mc "Con lo bien que te están entrenando estas chicas, no vas a tardar mucho en poder subir aquí sin darte cuenta de si la mochila pesa mucho."
    call BlinkXPS3 ("c21s005_080" , "d") from _call_BlinkXPS3_355
    kim "Lo está haciendo muy bien. El primer día no fue capaz de correr más de unos centenares de metros."
    kim "El plan de entrenamiento de [deb.nick] está dando resultados."
    call BlinkXPS3 ("c21s005_085" , "d") from _call_BlinkXPS3_356
    kat "Un día nadar, otro correr, otro descanso. Mi vida es un infierno dos días de cada tres."
    mc "Pero puedes ver que está funcionando. Hoy has llegado hasta aquí."
    kat "Pero no he perdido ni un gramo..."
    scene c21s005_090d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c21s005_090a" , "d") from _call_BlinkXPS3_357
    deb "Eso es porque estás convirtiendo la grasa en músculo. Pero solo llevas una semana haciéndolo."
    if not _in_replay:
        $ deb.profileImages.pop (13) # first remove
        $ deb.profileImages.insert (13, ("debbie_13", None)) # then add new
        $ texto = str(deb.nick)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 14 - Topless")
    if kat._var("slim"):
        deb "En dos o tres semanas más empezarás a notar como pierdes peso si sigues comiendo sano."
    else:
        deb "Si comieras más sano, empezarías a perder peso en dos o tres semanas."
    deb "Pero ya estás ganando en resistencia, y seguro que tus niveles de azúcar han mejorado."
    call BlinkXPS3 ("c21s005_090b" , "d") from _call_BlinkXPS3_358
    kat "¡Wow, [deb.nick]! Creo que el Día Topless era ayer. [kim] no me ha sorprendido porque ya se apuntó ayer, pero tú..."
    call BlinkXPS3 ("c21s005_090c" , "d") from _call_BlinkXPS3_359
    deb "Ayer, al final de la fiesta, creo que solo quedábamos tú, [lis], y yo sin unirnos."
    mc "Y [meg]."
    call BlinkXPS3 ("c21s005_090d" , "d") from _call_BlinkXPS3_360
    deb "Exacto, y [meg]. Cuando os habéis ido, [lis] ha bajado en topless a la piscina, y he pensado que yo también puedo hacerlo."
    call BlinkXPS3 ("c21s005_090e" , "d") from _call_BlinkXPS3_361
    kim "¡Bien hecho!"
    mcp "(La postura de [kim] en el agua se debía a que estaba en topless. No le importaba cuando estaba a solas con [kat] esperando que llegara [deb.nick].)"
    mcp "(Pero al llegar yo se ha escondido bajo el agua. Hasta que [deb.nick] ha aparecido también en topless. No quería ser la única que mostraba su cuerpo.)"
    call BlinkXPS3 ("c21s005_090f" , "d") from _call_BlinkXPS3_362
    deb "Tú también podrías unirte si hubieras venido con un bikini, [kat]. Estoy segura de que a [mc] no le importaría. *Risa*"
    mc "No. No me importaría. *Risa* Sabéis que no juzgo a nadie lleve las tetas cubiertas o al aire."
    deb "Y, aparte de él, eres la única a quien le interesan las tetas de las demás. *Risa*"
    call BlinkXPS3 ("c21s005_095a" , "d") from _call_BlinkXPS3_363
    kat "Vaaaale... {b}Intentaré{/b} ser más disimulada mirando..."
    call BlinkXPS3 ("c21s005_095b" , "d") from _call_BlinkXPS3_364
    kat "¿Y qué hacéis aquí aparte de admirar el paisaje? Muy bonito, por cierto."
    mc "Nadamos, charlamos, nos tumbamos a descansar..."
    call BlinkXPS3 ("c21s005_105" , "d") from _call_BlinkXPS3_365
    kim "Aunque dudo que quieras nadar después de subir hasta aquí corriendo..."
    call BlinkXPS3 ("c21s005_110" , "d") from _call_BlinkXPS3_366
    kat "Es muy aburrido... Deberíamos haber subido una pelota para jugar como en la playa. Se quedaron muchas preguntas en el tintero cuando la cosa se puso incómoda."
    mc "Por mí puedes hacer las preguntas que quieras, [kat]. No hace falta un juego. Desde ayer se acabaron los secretos."
    call BlinkXPS3 ("c21s005_115" , "d") from _call_BlinkXPS3_367
    kim "¿Sólo puede hacerlas [kat]? *Risa*"
    mc "*Risa* Todas podéis hacer preguntas si queréis. Pero yo preguntaré a quien me pregunte."
    call BlinkXPS3 ("c21s005_120" , "d") from _call_BlinkXPS3_368
    deb "¡Me parece una buena idea! Podemos hacer una ronda donde [kat] pregunta a [mc] y después tiene que responderle, después yo pregunto a [kim] y ella a mí..."
    deb "O incluso podemos proponer retos..."
    mc "Chicas, lo de los retos se os fue de las manos la última vez."
    call BlinkXPS3 ("c21s005_125" , "d") from _call_BlinkXPS3_369
    kat "Porque no nos conocíamos aún..."
    mc "Además, sin el componente de juego, no tendría mucha emoción."
    mc "Tan solo tendría que esperar a que llegase mi turno y hacerle la pregunta a quien quisiera o proponer un reto."
    mc "Y esperar que no quiera vengarse de mí con una pregunta o un reto más comprometedor."
    call BlinkXPS3 ("c21s005_130" , "d") from _call_BlinkXPS3_370
    kim "[mc] tiene razón. Si no hay aleatoriedad y es recíproco, se puede ir muy rápido de las manos. Especialmente si hay varias rondas."
    mc "Con lo que, si queréis hacerme alguna pregunta, sois libres de hacerla. Pero yo también preguntaré."
    call BlinkXPS3 ("c21s005_135a" , "d") from _call_BlinkXPS3_371
    kat "Le quitáis toda la emoción. *Risa*"
    if deb._var("route"):
        call BlinkXPS3 ("c21s005_135b" , "d") from _call_BlinkXPS3_372
        kat "Empiezo yo con las preguntas. ¿Ya te has acostado con [deb.nick]?"
        call BlinkXPS3 ("c21s005_140" , "h") from _call_BlinkXPS3_373
        deb "¡[kat]! ¡Eso es privado entre [mc] y yo!"
        deb "Si vas a mantener esa pregunta, yo también te haré una, y no te va a gustar."
        call BlinkXPS3 ("c21s005_145" , "d") from _call_BlinkXPS3_374
        kat "Tienes razón... lo siento... Me he pasado..."
        kat "Y es verdad que las preguntas recíprocas dan miedo. Creo que lo deberíamos dejar."
        mc "Además, has dicho que se quedaron preguntas en el tintero en la playa. [deb.nick] y yo no salíamos juntos por entonces."
    else:
        kat "Además, eso de las preguntas recíprocas da miedo. Puede escalar demasiado rápido."
    mc "*Risa* Parece que hay alguien que tiene algo que ocultar."
    call BlinkXPS3 ("c21s005_150" , "d") from _call_BlinkXPS3_375
    kim "No todas podemos revelar nuestros secretos en una fiesta de cumpleaños. *Risa forzada*"
    stop music fadeout (1.5)
    mc "¿Pasa algo, [kim]?"
    play music ("music/In-The-Rain.ogg")
    scene c21s005_155a with dissolve
    deb "Vamos a nadar un rato, [kat]."
    kat "Estoy cansada de subir corriendo hasta aquí..."
    scene c21s005_155An with dissolve
    deb "{b}Vamos a nadar un rato, [kat].{/b}"
    kat "¡Oh! ¡Ah! ¡Sí!... Tengo que seguir el entrenamiento..."
    call BlinkXPS3 ("c21s005_160" , "d") from _call_BlinkXPS3_376
    mc "¿Qué pasa, [kim]?"
    kim "No pasa nada, [mc], de verdad..."
    mc "Mírame a los ojos y dime que no pasa nada."
    call BlinkXPS3 ("c21s005_165" , "d") from _call_BlinkXPS3_377
    kim "No pasa..."
    call BlinkXPS3 ("c21s005_170" , "d") from _call_BlinkXPS3_378
    kim "No puedo..."
    mc "¿Ves como pasa algo? Puedes decírmelo si quieres... Sabes que no voy a juzgarte."
    call BlinkXPS3 ("c21s005_175" , "d") from _call_BlinkXPS3_379
    kim "No te preocupes, [mc]. Se me pasará."
    mc "¿De verdad no puedo ayudarte?"
    call BlinkXPS3 ("c21s005_180" , "d") from _call_BlinkXPS3_380
    kim "No. No puedes ayudarme. En serio, no es importante."
    mc "Si no es importante, ¿por qué quieres guardarlo en secreto?"
    if mc._var("relationships") > 0:
        if mc._var("relationships") == 1:
            call BlinkXPS3 ("c21s005_185" , "d") from _call_BlinkXPS3_381
            kim "Porque ya era difícil cuando pensaba que estabas soltero. Pero sales con alguien a quien aprecio mucho, y no me quiero interponer."
            mc "¿Por qué era difícil, [kim]?"
            call BlinkXPS3 ("c21s005_190" , "d") from _call_BlinkXPS3_382
            kim "Porque me habéis aceptado en la familia y... sentiría que estaba traicionando la confianza de [mar] si intentaba salir contigo."
            mc "¿Es de eso de lo que intentabas hablar con [mar] ayer en la fiesta?"
            call BlinkXPS3 ("c21s005_195" , "d") from _call_BlinkXPS3_383
            if mar._var("route"):
                kim "Sí, hasta que reveló que sale contigo."
                if mar._var("pregnancyDiscovered"):
                    kim "Y que está embarazada de ti."
            else:
                kim "Sí, hasta que llegó la hora de las revelaciones. Y descubrí que salías con alguien."
            kim "A partir de ese momento ya no había nada que hablar con [mar]."
            if persistent.walkthrough:
                $ wt1 = "[kim] +15"
                $ wt2 = _("Sin consecuencias.")
            else:
                $ wt1 = ""
                $ wt2 = ""
            menu:
                "Quizás deberías hablar con [mar]." (wt = wt1) if mar._var("route"):
                    $ kim._var("talkWithHarem" , True)
                "Quizás deberías hablar con ella. \nY después con [mar], si te gusta lo que te dice." (wt = wt1) if not mar._var("route"):
                    $ kim._var("talkWithHarem" , True)
                "Te entiendo." (wt = wt2):
                    $ kim._var("talkWithHarem" , False)
            if kim._var("talkWithHarem"):
                call BlinkXPS3 ("c21s005_200" , "h") from _call_BlinkXPS3_384
                kim "{b}¿Qué?{/b} ¿Me estás diciendo que la engañarías?"
                mc "No, [kim]. Si te digo que deberías hablar con ella es porque nunca engañaría a una persona a la que quiero."
                mc "Normalmente cuando engañas a alguien no la pones sobre aviso, ¿no?"
                call BlinkXPS3 ("c21s005_205" , "d") from _call_BlinkXPS3_385
                kim "Tienes razón... Soy una tonta..."
                mc "No lo creo, [kim]. Creo que es una situación diferente de a lo que estás acostumbrada."
                call BlinkXPS3 ("c21s005_215" , "d") from _call_BlinkXPS3_386
                kim "Es una conversación que no sabría ni por dónde empezar..."
                mc "Puedes empezar hablando con ella. En casa intentamos hablarlo todo y poner las cartas sobre la mesa."
                mc "¿Qué es lo peor que puede pasar?"
            else:
                mc "No tengo intención de engañar a nadie. Cuando empezamos a salir juntos no hablamos de exclusividad, pero poco a poco se ha convertido en algo exclusivo."
                call BlinkXPS3 ("c21s005_205" , "d") from _call_BlinkXPS3_387
                kim "Por eso te decía que no había nada de lo que hablar. Ni con [mar] ni contigo. Al menos sobre este tema."
                mc "Sabes que [mar] te aprecia mucho, ¿verdad?"
                call BlinkXPS3 ("c21s005_210" , "d") from _call_BlinkXPS3_388
                kim "¿De verdad?"
                mc "De verdad. Aunque algo no tenga solución, en casa pensamos que va bien hablar las cosas, al menos para desahogarte."
                mc "Y a [mar] se le da bien escuchar. ¿Qué es lo peor que puede pasar?"
        else:
            call BlinkXPS3 ("c21s005_185" , "d") from _call_BlinkXPS3_389
            kim "Porque ya era difícil cuando pensaba que estabas soltero. Pero después de descubrir el harén... no me quiero interponer."
            mc "¿Por qué era difícil, [kim]?"
            call BlinkXPS3 ("c21s005_190" , "d") from _call_BlinkXPS3_390
            kim "Porque me habéis aceptado en la familia y... sentiría que estaba traicionando la confianza de [mar] si intentaba salir contigo."
            mc "¿Es de eso de lo que intentabas hablar con [mar] ayer en la fiesta?"
            call BlinkXPS3 ("c21s005_195" , "d") from _call_BlinkXPS3_391
            if mar._var("route"):
                kim "Sí, hasta que reveló que sale contigo."
                if mar._var("pregnancyDiscovered"):
                    kim "Y que está embarazada de ti."
            else:
                kim "Sí, hasta que llegó la hora de las revelaciones. Y descubrí que tenías un harén."
            kim "A partir de ese momento ya no había nada que hablar con [mar]. No sé si me podría ver en un harén."
            if persistent.walkthrough:
                $ wt1 = "[kim] +15"
                $ wt2 = _("Sin consecuencias.")
            else:
                $ wt1 = ""
                $ wt2 = ""
            menu:
                "Quizás deberías hablar con [mar]. \nY después con las otras chicas, si te gusta lo que te dice." (wt = wt1) if mar._var("route"):
                    $ kim._var("talkWithHarem" , True)
                "Quizás deberías hablar con las chicas. \nY después con [mar], si te gusta lo que te dicen." (wt = wt1) if not mar._var("route"):
                    $ kim._var("talkWithHarem" , True)
                "Te entiendo." (wt = wt2):
                    $ kim._var("talkWithHarem" , False)
            if kim._var("talkWithHarem"):
                call BlinkXPS3 ("c21s005_200" , "d") from _call_BlinkXPS3_392
                kim "{b}¿Qué?{/b} ¿Me estás diciendo que quieres que entre en el harén?"
                mc "No, [kim]. Estoy diciendo que parece que ves el harén con malos ojos. Quizás si hablas con las chicas cambies de opinión."
                call BlinkXPS3 ("c21s005_205" , "d") from _call_BlinkXPS3_393
                kim "No lo veo con malos ojos. Me resulta extraño tan solo. Nunca he conocido a varias mujeres que quisieran compartir su hombre abiertamente."
                kim "Quizás soy demasiado tradicional para este tipo de cosas..."
                mc "Por eso te digo que hables con ellas. Te llevas bien con todas y quizás te puedan explicar por qué aceptaron."
                mc "Y ya sabes que en esta casa nos encanta hablar de todo y que [mar] te aprecia mucho."
                call BlinkXPS3 ("c21s005_210" , "d") from _call_BlinkXPS3_394
                kim "¿De verdad?"
                mc "De verdad. Y aunque no cambies de opinión sobre el harén, al menos podrás hablar con ella para desahogarte."
                mc "Y a [mar] se le da bien escuchar. ¿Qué es lo peor que puede pasar?"
            else:
                mc "Un harén se sale de lo normal y no todo el mundo está preparado para aceptarlo."
                call BlinkXPS3 ("c21s005_205" , "d") from _call_BlinkXPS3_395
                kim "Por eso te decía que no había nada de lo que hablar. Ni con [mar] ni contigo. Al menos sobre este tema."
                mc "Sabes que [mar] te aprecia mucho, ¿verdad?"
                call BlinkXPS3 ("c21s005_210" , "d") from _call_BlinkXPS3_396
                kim "¿De verdad?"
                mc "De verdad. Aunque algo no tenga solución, en casa pensamos que va bien hablar las cosas, al menos para desahogarte."
                mc "Y a [mar] se le da bien escuchar. ¿Qué es lo peor que puede pasar?"
    else:
        call BlinkXPS3 ("c21s005_185" , "d") from _call_BlinkXPS3_397
        kim "Porque intenté hablar de ello con [mar] un par de veces, y nos interrumpieron."
        kim "Ya era difícil antes de eso. Después..."
        mc "¿Por qué era difícil, [kim]?"
        call BlinkXPS3 ("c21s005_190" , "d") from _call_BlinkXPS3_398
        kim "Porque me habéis aceptado en la familia y... sentiría que estaba traicionando la confianza de [mar] si intentaba salir contigo."
        mc "¿Es de eso de lo que intentabas hablar con [mar] ayer en la fiesta?"
        call BlinkXPS3 ("c21s005_195" , "d") from _call_BlinkXPS3_399
        kim "Sí, hasta que Olivia soltó el bombazo sobre su cáncer..."
        kim "Después de lo de Olivia... mis preocupaciones parecían una tontería..."
        kim "A partir de ese momento ya no había nada que hablar con [mar]."
        if persistent.walkthrough:
            $ wt1 = "[kim] +15"
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Quizás deberías hablar con [mar]." (wt = wt1) :
                $ kim._var("talkWithHarem" , True)
            "Te entiendo." (wt = wt2):
                $ kim._var("talkWithHarem" , False)
        if kim._var("talkWithHarem"):
            call BlinkXPS3 ("c21s005_200" , "d") from _call_BlinkXPS3_400
            kim "{b}¿Qué?{/b} ¿Me estás diciendo que querrías salir conmigo?"
            mc "No, [kim]. Estoy diciendo que parece te importa mucho lo que piense [mar]."
            mc "Hasta que no sepas lo que ella piensa no podrás tomar una decisión sobre mí. Ni yo podré tomarla sobre ti."
            call BlinkXPS3 ("c21s005_205" , "d") from _call_BlinkXPS3_401
            kim "Tienes razón... si ahora intentaras besarme, estaría pensando más en cómo se lo voy a decir a ella y en lo que pensaría que en el propio beso."
            mc "Por eso te digo que hables con ella. Sabes que [mar] te aprecia mucho..."
            call BlinkXPS3 ("c21s005_210" , "d") from _call_BlinkXPS3_402
            kim "¿De verdad?"
            mc "De verdad. Y aunque al final decidas que no quieres intentar nada conmigo, al menos lo habrás hablado con ella."
            mc "Y a [mar] se le da bien escuchar. ¿Qué es lo peor que puede pasar?"
        else:
            mc "La noticia de Meemaw trastocó la fiesta durante un rato. Todo el mundo estaba muy aliviado de que lo haya superado."
            call BlinkXPS3 ("c21s005_205" , "d") from _call_BlinkXPS3_403
            kim "Por eso te decía que no había nada de lo que hablar. Ni con [mar] ni contigo. Al menos sobre este tema."
            mc "Sabes que [mar] te aprecia mucho, ¿verdad?"
            call BlinkXPS3 ("c21s005_210" , "d") from _call_BlinkXPS3_404
            kim "¿De verdad?"
            mc "De verdad. Aunque algo parezca una nimiedad, y no digo que lo sea, en casa pensamos que va bien hablar las cosas, al menos para desahogarte."
            mc "Y a [mar] se le da bien escuchar. ¿Qué es lo peor que puede pasar?"
    call BlinkXPS3 ("c21s005_220a" , "d") from _call_BlinkXPS3_405
    if kim._var("talkWithHarem") and not _in_replay:
        $ kim.rp (15)
    kim "*Risa* Que me eche a patadas de la residencia."
    mc "*Risa* Eso no va a pasar y lo sabes. Como mucho, dejará de hacerte tus platos favoritos."
    call BlinkXPS3 ("c21s005_220b" , "d") from _call_BlinkXPS3_406
    kim "*Risa* ¡Nooooo! ¡No puedo renunciar a la cocina de tu madre!"
    mc "*Risa* Ven aquí. Creo que necesitas un abrazo más que unos rollitos de calabacín ahora mismo."
    mc "Y si necesitas más los rollitos, te tendrás que conformar con un abrazo."
    call BlinkXPS3 ("c21s005_225" , "d") from _call_BlinkXPS3_407
    if not mc._var("relationships")==1 or kim._var("talkWithHarem"):
        kim "Gracias por la conversación, [mc]. La necesitaba. Aunque no me has sacado de dudas sobre qué querrías tú... sobre nosotros."
        mc "¿Serviría de algo decirte que quiero salir contigo si tú no estás dispuesta a hacerlo hasta que no tengas esa conversación?"
        mc "¿O que no quiero hacerlo? Lo único que provocaría sería que te pusieras más nerviosa o que no quisieras hablarlo."
        kim "Tienes razón..."
    else:
        kim "Gracias por la conversación, [mc]. La necesitaba."
        mc "Me tienes aquí para hablar siempre que quieras."
    call BlinkXPS3 ("c21s005_230" , "d") from _call_BlinkXPS3_408
    kim "¿Puedo decirte algo raro?"
    mc "Claro. Espero que no digas \"La Familia\". *Risa*"
    if not persistent.family:
        call BlinkXPS3 ("c21s005_235" , "d") from _call_BlinkXPS3_409
        kim "Sé que [mar] no es tu madre ni la de [emm], pero me es muy difícil pensar en ella de otra forma."
        mc "Eso no tiene nada de raro, [kim]. Nos presentamos así a todo el mundo, y es lo que habéis pensado desde que llegasteis."
        mc "¿Crees que [emm] va a dejar de pensar que soy su hermano ahora que lo ha descubierto? Excepto por el enfado del primer día, no lo va a hacer."
        mc "Somos una familia rara, pero somos una familia."
    call BlinkXPS3 ("c21s005_240" , "d") from _call_BlinkXPS3_410
    kim "A eso me refería. Entre la fiesta en la playa y la de ayer, el sentimiento de familia ha crecido mucho."
    kim "Anoche soñé con acción de gracias. Una comida familiar. Estaba mi familia... la de verdad..."
    kim "Pero también estabais todos vosotros. Y no se veía raro en absoluto."
    mc "Si las fiestas cerca del agua producen ese efecto, la próxima la tenemos que hacer aquí. *Risa*"
    call BlinkXPS3 ("c21s005_245" , "d") from _call_BlinkXPS3_411
    kim "Estaría bien. Creo que [lis] y [sai] todavía no han venido. El problema sería subir toda la comida y la bebida..."
    mc "Ni Tía [bet], Meemaw, o Megan. Ni siquiera sé si [mar], [nor], o [sam.nick] han venido alguna vez."
    scene c21s005_250An with dissolve
    "Pasáis los siguientes minutos hablando de fiestas imposibles. El lago, un parque acuático, Aruba..."
    stop music fadeout (1.5)
    "El tema de conversación es lo de menos. Si [kim] necesitaba charlar anteriormente, ahora necesita un largo abrazo."
    play music ("music/Morning-Sun.ogg")
    call BlinkXPS3 ("c21s005_255" , "f") from _call_BlinkXPS3_412
    kat "Chicos, si sigo nadando me voy a convertir en una pasa y no voy a poder bajar hasta casa. ¿Nos cambiamos y nos vamos?"
    call BlinkXPS3 ("c21s005_260" , "d") from _call_BlinkXPS3_413
    kim "Me parece una buena idea. A mí me está entrando un poco de frío."
    if deb._var("route"):
        kim "Pero he monopolizado a [mc] y él no ha podido nadar."
        scene c21s005_265AnBlink with dissolve
        kim "[deb.nick], ¿por qué no te quedas con [mc] y nadáis un rato juntos? Nadar solo es muy aburrido."
        mc "A mí me parece una buena idea."
        call BlinkXPS3 ("c21s005_270" , "d") from _call_BlinkXPS3_414
        deb "A mí también. Podemos volver a jugar a encontrar tesoros."
        call BlinkXPS3 ("c21s005_275a" , "d") from _call_BlinkXPS3_415
        kat "*Risa* ¿Ahora le llamáis así?"
        call BlinkXPS3 ("c21s005_275b" , "d") from _call_BlinkXPS3_416
        kat "Vamos a cambiarnos, [kim]. Dejemos solos a los tortolitos."
        scene c21s005_285d with dissolve
        kat "¿Creéis que [lis] aún estará en la piscina cuando volvamos?"
        mc "*Risa* ¿Te quedaste con ganas ayer de verla en topless?"
        scene c21s005_285e with dissolve
        kat "No es eso... Es que me sorprende que se haya decidido hoy. ¿Alguien se hubiera imaginado a [lis] haciendo topless hace una semana?"
        mc "Yo no, desde luego."
        kim "Yo tampoco. Tiene un cuerpo precioso, pero no le gusta mostrarlo."
        call BlinkXPS3 ("c21s005_275c" , "d") from _call_BlinkXPS3_417
        deb "En la piscina de casa lo hacía muchas veces... cuando no estaban mis padres. ¿Pero hacerlo aquí? No, no me lo hubiera imaginado cuando llegamos."
        deb "Creo que nos hemos adaptado muy rápido y nos sentimos como en casa. Anoche decía que se sentía tonta por no haber hecho topless en la fiesta."
        mc "Supongo que hoy ha decidido resolverlo."
        scene c21s005_280b with fade
        "Al cabo de unos minutos [kim] y [kat] emprenden el camino a casa, dejándoos a [deb.nick] y a ti solos en el lago, donde hace unos días os disteis vuestros primeros besos."
    else:
        mc "Me parece buena idea. Yo estoy cansado después de la fiesta de ayer."
        scene c21s005_280a with fade
        "Al cabo de unos minutos emprendéis el camino a casa."
        scene c21s005_285a with dissolve
        kat "¿Creéis que [lis] aún estará en la piscina cuando volvamos?"
        mc "*Risa* ¿Te quedaste con ganas ayer de verla en topless?"
        scene c21s005_285b with dissolve
        kat "No es eso... Es que me sorprende que se haya decidido hoy. ¿Alguien se hubiera imaginado a [lis] haciendo topless hace una semana?"
        mc "Yo no, desde luego."
        kim "Yo tampoco. Tiene un cuerpo precioso, pero no le gusta mostrarlo."
        scene c21s005_285c with dissolve
        deb "En la piscina de casa lo hacía muchas veces... cuando no estaban mis padres. ¿Pero hacerlo aquí? No, no me lo hubiera imaginado cuando llegamos."
        deb "Creo que nos hemos adaptado muy rápido y nos sentimos como en casa. Anoche decía que se sentía tonta por no haber hecho topless en la fiesta."
        mc "Supongo que hoy ha decidido resolverlo."
        scene c21s005_280a with dissolve
        "Continuáis corriendo y charlando, adaptando el paso para que [kat] no llegue en condiciones deplorables a casa."
        "Llegáis con tiempo suficiente para ducharos antes de cenar."
    stop music fadeout (1.5)
    return
label c21s005_DebLake:
    if _in_replay:
        call mrS3_rename from _call_mrS3_rename_9
    call BlinkXPS3 ("c21s005_285a" , "d") from _call_BlinkXPS3_418
    deb "Pues nos hemos quedado solos..."
    play music ("music/KindofGirl.ogg")
    scene c21s005_290An1 with dissolve
    "En vez de responder, bajas la cabeza de [deb.nick] hasta tu altura y la besas apasionadamente."
    scene c21s005_290An2 with dissolve
    "Vuestras lenguas se entrelazan en un beso que habéis deseado repetir desde la noche en el club de jazz."
    "Los besos de buenos días son un pobre sustituto de los besos de verdad."
    "El beso en el camino ha sido algo rápido para quitaros el mono de la droga que son vuestros labios."
    "Después de unos segundos, de unos siglos, os separáis reluctantemente."
    call BlinkXPS3 ("c21s005_295" , "d") from _call_BlinkXPS3_419
    deb "*Respiración entrecortada* Tengo que quedarme a solas más veces contigo..."
    mc "Siempre que quieras. Sabes donde vivo y donde duermo. *Risa*"
    call BlinkXPS3 ("c21s005_300" , "d") from _call_BlinkXPS3_420
    deb "Sabes que no estoy preparada para dormir contigo todavía..."
    mc "[deb.nick], me refería a que puedes venir cuando quieras a por más besos, no a que te quedaras a dormir."
    call BlinkXPS3 ("c21s005_305" , "d") from _call_BlinkXPS3_421
    deb "¡Oh! ¡Eso sí que puedo hacerlo! No sé por qué no se me había ocurrido."
    mc "Además, ahora todo el mundo sabe que estamos juntos. Podemos besarnos donde queramos."
    call BlinkXPS3 ("c21s005_310" , "d") from _call_BlinkXPS3_422
    deb "Nunca me he sentido cómoda alrededor de parejas que se pasan el día besándose."
    deb "Un beso como los de buenos días no me incomoda. Uno como el que acabamos de darnos..."
    call BlinkXPS3 ("c21s005_315" , "d") from _call_BlinkXPS3_423
    deb "Y no quiero que nadie se sienta incómodo a nuestro alrededor. Quiero compartir nuestra felicidad, no que salgan corriendo en cuanto nos vean."
    mc "*Risa* \"Ahí vienen los besucones. Vámonos.\""
    call BlinkXPS3 ("c21s005_320" , "d") from _call_BlinkXPS3_424
    deb "*Risa* Exactamente eso. [lis] es una de las que no se sentiría cómoda y tendría que escuchar su charla al volver a la habitación."
    mc "*Risa* Eso tiene fácil solución. No vuelvas y ven a la mía."
    mc "Además, creo que [lis] está cambiando mucho. Como has dicho antes, se siente más cómoda alrededor de todo el mundo."
    scene c21s005_330d with dissolve
    mc "Igual que tú. Es una sorpresa muy agradable."
    call BlinkXPS3 ("c21s005_330" , "d") from _call_BlinkXPS3_425
    deb "Siempre he tenido un poco de complejo con mis... inexistentes tetas... Pero el otro día, en el Jazz Corner, un chico maravilloso me demostró que son suficientes..."
    mc "*Risa* ¿Tengo que matar a ese chico maravilloso? ¿Me estás intentando poner celoso?"
    call BlinkXPS3 ("c21s005_335" , "d") from _call_BlinkXPS3_426
    deb "Te lo estoy diciendo en serio, [mc]."
    deb "Puede parecerte una tontería, pero que bailáramos juntos... si se puede llamar bailar a eso... y lo que dijiste sobre mi cuerpo..."
    mc "No dije nada que no sea cierto, [deb.nick]. Me encanta tu cuerpo."
    scene c21s005_335d with dissolve
    mc "No necesitas tener las tetas de Tía [bet] para que sean preciosas."
    deb "¡[mc]! Se me acaba de poner piel de gallina..."
    call BlinkXPS3 ("c21s005_340" , "d") from _call_BlinkXPS3_427
    mc "Espero que no te esté entrando frío, aunque tengo una solución para eso..."
    deb "¿Frío? No exactamente..."
    scene c21s005_345pv with dissolve
    show c21s005_345v
    "Sin retirar tu mano del pecho de [deb.nick], empiezas a besar su cuello, su clavícula, otra vez su cuello."
    deb "Mmmmm... eso me gusta..."
    "Puedes notar como su pezón, duro como una piedra, roza contra la palma de tu mano. No es una teta para estrujar, sino para rozar suavemente."
    deb "*Gemido* No sé qué estás haciendo... pero me encanta..."
    "Habrá tiempo más adelante para estrujarla y mordisquearla. Ahora tan solo quieres excitar más todavía ese maravilloso pezón."
    scene c21s005_350a with dissolve
    hide c21s005_345v
    "Bajas tu cabeza un poco, salpicando de besos el camino que une su clavícula a su pezón."
    deb "*Jadeo* [mc], podría venir alguien..."
    call BlinkXPS3 ("c21s005_355" , "d") from _call_BlinkXPS3_428
    mc "¿Te importaría que nos vieran? ¿O tan solo te molestaría porque nos interrumpirían?"
    deb "Creo que lo segundo..."
    mc "Entonces no les demos tiempo a interrumpirnos."
    scene c21s005_350b with dissolve
    "Por fin llegas a su enhiesto pezón. Ha estado esperándote con ansia durante todo el recorrido de tus labios. Lo saludas con tu lengua."
    deb "*Gemido* ¡Aaah! *Jadeo* ¡Qué bien se siente!"
    scene c21s005_350An with dissolve
    "Dedicas tus labios, tu lengua, tus dientes, al pezón de la sirena durante unos maravillosos momentos."
    deb "*Jadeo* Tengo los pezones muy sensibles, [mc]... *Gemido* Se me está erizando el vello de la nuca..."
    mcp "(No es lo único que tienes erizado, cielo.)"
    scene c21s005_360An with dissolve
    "La musculosa mujer está tan concentrada en el tacto de tu boca en su pezón que no descubre a donde se dirige tu mano hasta que es demasiado tarde."
    deb "*Jadeo* ¡[mc]!"
    "Puedes notar el calor de su entrepierna a través del húmedo bikini."
    call BlinkXPS3 ("c21s005_365" , "d") from _call_BlinkXPS3_429
    mc "Dime, cielo."
    "Empiezas a mover tus dedos por encima de la tela que te separa de su tesoro."
    deb "*Gemido* Te he dicho que no estaba preparada..."
    "Sus palabras expresan dudas. Su cuerpo pide más, aunque sabes... crees... que no vas a poder llegar hasta el final. Habrá tiempo para eso."
    mc "Has dicho que no estabas preparada para acostarte conmigo. Hay muchas cosas que podemos hacer sin acostarnos."
    mc "¿Confías en mí?"
    call BlinkXPS3 ("c21s005_370" , "d") from _call_BlinkXPS3_430
    deb "*Jadeo* Sí..."
    mc "Si hago algo que no te gusta, dímelo y pararé."
    deb "*Gemido* De acuerdo. Hasta ahora me gusta todo... casi demasiado."
    scene c21s005_375An with dissolve
    "Tus labios empiezan a repartir besos lentamente por todo el camino que lleva de su pezón a la goma de su bikini, hasta acabar arrodillado delante de ella."
    "Tan lentamente que, para cuando acabas, ambos estáis casi secos."
    call BlinkXPS3 ("c21s005_380" , "d") from _call_BlinkXPS3_431
    deb "*Gemido* ¿Vas a desnudarme del todo?... Me siento... vulnerable..."
    mc "Si no te importa, me gustaría hacerlo. Verte desnuda para mí por primera vez."
    deb "Adelante... pero después me gustaría verte yo también..."
    scene c21s005_385An1 with dissolve
    "Bajas lentamente un lado de su bikini. Quieres alargar la experiencia lo máximo posible."
    mc "Tu ya me viste, cielo."
    scene c21s005_385An2 with dissolve
    "El otro lado sigue al primero. Queda poco para poder llegar al tesoro de la sirenita."
    deb "¿Cuándo?"
    mc "Cuando apareció el jabalí, aquí mismo."
    scene c21s005_385An3 with dissolve
    "Descubres el tesoro, perfectamente depilado. El aroma que inunda tus sentidos te indica que la preciosa mujer está preparada para más."
    deb "Espero que no estés tan flácido como aquel día."
    mc "*Risa* No lo estoy, no te preocupes."
    scene c21s005_390An with dissolve
    "No puedes resistir la tentación de probarla su sabor por primera vez. Hundes tu cara en su entrepierna."
    deb "*Gemido* ¡Ooooh! *Jadeo*"
    "Tu lengua encuentra una multitud de sensaciones. El frescor de su baño en el lago mezclado con el calor que emana de su interior."
    deb "*Jadeo* ¡Ahhhhh! *Gemido*"
    "El aroma terroso de su excitación y el sabor agridulce de su lubricación."
    call BlinkXPS3 ("c21s005_395" , "d") from _call_BlinkXPS3_432
    mc "Sabes maravillosamente bien, [deb.nick]."
    deb "*Gemido* ¿Ya está? *Jadeo* ¿Sólo eso?"
    mc "*Risa* No, cielo, recuéstate en la piedra que tienes detrás, quiero probarte toda."
    call BlinkXPS3 ("c21s005_500" , "d") from _call_BlinkXPS3_433
    deb "¿Así está bien?"
    "Sus piernas cerradas revelan la inseguridad que siente en ese momento."
    mc "Preciosa. Para empezar, estás perfecta."
    scene c21s005_505An with dissolve
    "Te arrodillas delante de ella y empiezas a recorrer su larguísima pierna con tus labios, salpicando besos por toda su piel hasta llegar a su muslo."
    deb "*Gemido* Me encanta..."
    scene c21s005_510An with dissolve
    "Vuelves a sus pies para hacer el mismo recorrido en su otra pierna."
    call BlinkXPS3 ("c21s005_515" , "d") from _call_BlinkXPS3_434
    deb "*Jadeo* No sabía que podías ser tan delicado..."
    mc "Por ti puedo ser tan delicado como necesites, cielo."
    scene c21s005_520An with dissolve
    "No es necesario decirle que abra las piernas. Tal como tus labios bajan por la curvatura de su muslo, sus piernas se van abriendo para recibir tus besos."
    "Su instinto ancestral toma el control de su cuerpo, preparándolo para algo que no va a llegar hoy."
    "Pero lo que va a suceder puede ser igual de placentero para ella."
    scene c21s005_525An with dissolve
    "Recorres el otro muslo, empezando cerca de la rodilla, acercándote más a su húmeda raja."
    "Su aroma se intensifica tal como van pasando los segundos."
    call BlinkXPS3 ("c21s005_530" , "d") from _call_BlinkXPS3_435
    deb "*Gemido* Me estás matando con la anticipación... *Jadeo*"
    mc "Todo es parte del proceso, cielo. Has dicho que confiabas en mí, ¿no?"
    call BlinkXPS3 ("c21s005_535" , "d") from _call_BlinkXPS3_436
    deb "*Respiración entrecortada* Sí, tú eres el que sabes cómo funciona... *Jadeo* Pero es que parece que lo hagas a propósito."
    mc "Te voy a contar un secreto, mi amor."
    mc "Lo hago a propósito."
    scene c21s005_540An with dissolve
    "Abandonas su muslo para subir hasta sus increíbles abdominales, besando y lamiendo todo el camino."
    deb "*Gemido*"
    "Has evitado acercarte a su zona más sensible. A propósito."
    mc "Me encantan estos abdominales, cielo. Creo que podría pasarme horas besándolos."
    call BlinkXPS3 ("c21s005_545" , "d") from _call_BlinkXPS3_437
    deb "*Jadeo* No lo hagas si quieres volver a casa de una pieza."
    mc "*Risa* Parece que hay alguien ansioso en este lago."
    scene c21s005_550An with dissolve
    "Sigues tu recorrido antes de que pueda contestar. Esta vez hasta sus pezones."
    deb "*Gemido* Te he dicho que están muy sensibles..."
    scene c21s005_555a with dissolve
    "Llegas por fin a su boca. Os fundís en un largo beso antes de que empieces el viaje hacia abajo de nuevo."
    "Durante el viaje hacia arriba, paso a paso se ha ido relajando hasta acabar tumbada sobre la roca. Era una de las cosas que esperabas conseguir."
    scene c21s005_560An with dissolve
    "El viaje hacia abajo es más rápido. No quieres que pierda ni un ápice de excitación antes de llegar a tu destino."
    deb "*Gemido* Date prisa, por favor... *Jadeo*"
    "Te paras en su Monte de Venus."
    call BlinkXPS3 ("c21s005_565" , "d") from _call_BlinkXPS3_438
    mc "¿Preparada?"
    "Su olor es mucho más intenso ahora. Supones que está más excitada de lo que ha estado nunca."
    deb "*Jadeo* Sí... por favor..."
    scene c21s005_400pv with dissolve
    show c21s005_400v
    "Introduces tu cabeza entre sus piernas y empiezas a lamer."
    deb "JADEO* ¡Oh, SÍ! *GEMIDO* ¡Es mucho mejor de lo que podía haber imaginado!"
    "Su sabor también es mucho más intenso que antes. El frescor del lago ha desaparecido. Solo queda el sabor a mujer. A una mujer excitada."
    deb "*GEMIDO* ¡ME ENCANTA! *JADEO* ¡ES INCREÍBLE!"
    "Sus gemidos suben de volumen a la par que sus gritos, espantando a cualquier animalillo cercano."
    "Esperas que no atraiga al jabalí."
    scene c21s005_405pv with dissolve
    hide c21s005_400v
    show c21s005_405v
    "Crees que la has excitado demasiado. Puedes notar bajo tus manos como sus poderosos músculos se van tensando, anunciando su inminente orgasmo."
    deb "*JADEO* ¡SIGUE ASÍ! *GEMIDO* ¡NO ME LO PUEDO CREER!"
    "A ti también te cuesta creer lo mucho que se ha excitado y lo rápido que va a llegar al orgasmo."
    "Os esperan unas maravillosas noches de placer si siempre es igual."
    deb "*GEMIDO* ¡NO PARES! *GEMIDO* ¡ESTOY A PUNTO DE CORRERME!"
    "Continúas lamiendo cada pliegue de sus labios, cada recoveco de su coño. Acaricias su clítoris con tu lengua. Quieres llevarla a un paraíso desconocido de placer."
    "Lo consigues antes de lo que creías posible."
    "Todos los músculos de [deb.nick] se tensan a la vez, a punto de romperse. Sin un gramo de grasa en su cuerpo, puedes notar todas sus fibras bajo tus dedos."
    call OrgasmXS3 ("c21s005_570") from _call_OrgasmXS3_13
    "Los músculos se relajan de forma tan rápida que casi esperas escuchar un \"pop\"."
    deb "*GEMIDO* ¡SÍ! *JADEO* ¡ALUCINANTE! *GEMIDO* ¡IMPRESIONANTE!"
    "El \"pop\" no llega. Pero toda la tensión abandona a [deb.nick] en un segundo."
    "Continúas lamiendo."
    scene c21s005_400pv with dissolve
    hide c21s005_405v
    show c21s005_400v
    "Ella sigue disfrutando de su largo clímax mientras tu disfrutas del sabor de su orgasmo. De su aroma."
    deb "*Gemido* Está siendo larguísimo..."
    "Segundo tras segundo, su cuerpo se va relajando visiblemente, una vez termina el orgasmo que la ha recorrido de arriba a abajo."
    deb "*Jadeo* Puedes parar, [mc]..."
    "Sorprendido por su petición, dejas de lamer."
    call BlinkXPS3 ("c21s005_575" , "d") from _call_BlinkXPS3_439
    hide c21s005_400v
    mc "¿Ya? ¿Quieres que pare?"
    deb "*Jadeo* Sí, ya me he corrido. *Jadeo* Ahora estaba siendo agradable, pero... Me toca a mí."
    mc "¿Sólo un orgasmo?"
    call BlinkXPS3 ("c21s005_580" , "d") from _call_BlinkXPS3_440
    deb "Claro. ¿Cuántos quieres que tenga?"
    mc "Ermmm... No sé... ¿Cinco? ¿Seis? ¿Cuarenta y tres?"
    call BlinkXPS3 ("c21s005_585" , "d") from _call_BlinkXPS3_441
    deb "*Risa* Creo que, si todas las chicas con las que has estado eran multiorgásmicas, has tenido mucha suerte."
    mc "Siempre pensé que eso era un mito, y que todas las mujeres lo eran si lo hacían con la persona adecuada."
    deb "*Risa* ¡Al menos la novata sabe algo sobre sexo que tú no sabes!"
    mc "Estoy anonadado..."
    call BlinkXPS3 ("c21s005_590" , "d") from _call_BlinkXPS3_442
    deb "No es por ti, es por mí. Lo que has hecho ha sido totalmente alucinante."
    mc "Es que estoy pensando que no vas a poder tener orgasmos durante la previa cuando tengamos sexo..."
    deb "Cuando tengamos sexo, si es la mitad de impresionante que esto, no voy a quejarme por no tener orgasmos durante los preliminares. No te preocupes."
    call BlinkXPS3 ("c21s005_595" , "d") from _call_BlinkXPS3_443
    deb "Ahora quiero verte desnudo. Una promesa es una promesa."
    mc "*Risa* Esa es una promesa que puedo cumplir."
    call BlinkXPS3 ("c21s005_600" , "f") from _call_BlinkXPS3_444
    deb "*Jadeo sorprendido* ¡Extraordinario! ¿Dónde guardas eso normalmente?"
    deb "Eres una caja de sorpresas, [mc]."
    mc "*Risa* Mis ojos están aquí arriba."
    call BlinkXPS3 ("c21s005_605" , "d") from _call_BlinkXPS3_445
    deb "¿Puedo tocarlo?"
    mc "*Risa* Me sentiría un poco decepcionado si no lo hicieras."
    call BlinkXPS3 ("c21s005_610" , "d") from _call_BlinkXPS3_446
    deb "¡No te rías de mí!"
    mc "No me río de ti, [deb.nick]... bueno, un poco solo. *Risa*"
    call BlinkXPS3 ("c21s005_615" , "d") from _call_BlinkXPS3_447
    deb "*Risa* Sabes que en cuanto tenga tu tesoro en mis manos podría vengarme, ¿verdad?"
    mc "*Risa* Sí, pero también sé que eres una buena chica."
    call BlinkXPS3 ("c21s005_620" , "f") from _call_BlinkXPS3_448
    deb "¡Es enorme! Casi no me llega la mano para rodearlo... y tengo las manos grandes."
    deb "¿Cómo lo hacen otras chicas con manos más pequeñas?"
    mc "No es necesario rodearlo por completo para que sea agradable. Hay muchas formas de hacerlo."
    mc "¿Primeras impresiones?"
    call BlinkXPS3 ("c21s005_625" , "d") from _call_BlinkXPS3_449
    deb "No me imaginaba que fuera tan grande. Ni tan duro. Ni que estuviera tan caliente."
    mc "Llevo un rato muy excitado."
    call BlinkXPS3 ("c21s005_630" , "d") from _call_BlinkXPS3_450
    deb "Pero aún no te he hecho nada..."
    mc "Me excita mucho lo que yo te he hecho a ti."
    mc "Y la anticipación también ayuda. *Risa*"
    call BlinkXPS3 ("c21s005_635" , "d") from _call_BlinkXPS3_451
    deb "Entiendo. A mí me ha pasado lo mismo. Antes de que me tocaras ya estaba... cachonda."
    deb "Dime si hago algo mal."
    mc "Vale, no es muy difícil. Sólo piensa que es más resistente de lo que piensas y que puedes apretar más de lo que crees."
    deb "¡OK!"
    scene c21s005_425pv
    show c21s005_425v
    pause (1.53)
    scene c21s005_425dv
    "Esperabas una paja y [deb.nick] te sorprende introduciéndose tu polla en la boca."
    "Una boca llena de dientes."
    "Treinta y dos jodidos dientes que han rozado zonas donde un diente nunca debería rozar."
    "Casi has podido contar cada uno de ellos."
    mc "¡Por Dios, [deb.nick]! ¡Los dientes!"
    call BlinkXPS3 ("c21s005_640" , "v") from _call_BlinkXPS3_452
    deb "¡Perdón! ¿Te he hecho daño?"
    mc "No, daño no. Pero no es muy agradable. Labios, boca, y lengua. Nunca dientes."
    "Es la primera vez que tiene una polla cerca. No le puedes exigir más de lo que está haciendo."
    "Pero puedes darle consejos."
    mc "Te he dicho que es resistente, no masticable. *Risa*"
    call BlinkXPS3 ("c21s005_645" , "d") from _call_BlinkXPS3_453
    deb "Lo siento... Voy a probar de nuevo. Dime algo si vuelvo a hacerlo mal."
    mc "No te preocupes. *Risa* Si empiezo a sangrar lo notarás."
    "Una pequeña broma le quita hierro al asunto."
    call BlinkXPS3 ("c21s005_650" , "d") from _call_BlinkXPS3_454
    deb "*Risa* Eso sería literalmente la definición de comerte la polla."
    mc "*Risa* Prefiero que la chupes."
    scene c21s005_410pv
    show c21s005_410v
    hide c21s005_425v
    "Vuelve a introducirse tu polla en la boca. Esta vez con más cuidado. Solo puedes contar dos o tres dientes."
    "Pero son roces leves. No son placenteros, pero tampoco molestos."
    deb "*Jadeo interrogativo*"
    mc "Así vas mucho mejor, cielo..."
    "No puedes esperar que sea una experta en su primera vez."
    deb "*Jadeo afirmativo*"
    "Notas como va cambiando su posición en cada movimiento, cada vez que detecta que un diente roza donde no debería."
    "Pero le cuesta sincronizar sus movimientos con los tuyos."
    scene c21s005_415pv
    show c21s005_415v
    hide c21s005_410v
    "Te agarra el culo para poder hacerlo mejor. De esa forma nota tus movimientos antes de que los hagas."
    deb "*Jadeo interrogativo*"
    "La mejora es increíble. Detecta y se adapta a los involuntarios movimientos de tus caderas."
    "Los dientes parecen desaparecer."
    mc "Muchísimo mejor, cielo. Lo estás haciendo muy bien."
    "Con más confianza, empieza a recorrer tu polla con su lengua dentro de su boca. Siempre has pensado que no debe ser fácil."
    deb "*Jadeo afirmativo*"
    "La excitación previa y las mejoras en la técnica de [deb.nick] te acercan a un clímax que no creías posible hace unos minutos."
    scene c21s005_420pv
    show c21s005_420v
    hide c21s005_415v
    "La sirena acelera el ritmo en cuanto nota los pequeños espasmos en tu polla. Se la introduce más profundamente."
    deb "*Jadeo inseguro*"
    "No sabe si los espasmos son una señal positiva o negativa. Son muy positivos. Su lengua está haciendo maravillas mientras sus labios abrazan tu polla en cada recorrido."
    mc "Sí, cielo, me estoy acercando."
    deb "*Jadeo feliz*"
    "Las ansias de agradar de esta chica os van a proporcionar muchas noches alucinantes."
    "Su primera vez está siendo mucho más alucinante de lo que creías posible."
    "Pero todo llega a su fin..."
    mc "[deb.nick], estoy a punto de llegar..."
    "Ella sigue chupando con avidez."
    call OrgasmXS3 ("c21s005_655") from _call_OrgasmXS3_14
    mc "¡Mpfft!"
    "En cuanto nota los primeros espasmos de tu orgasmo, [deb.nick] te agarra con fuerza por el culo, para evitar que salgas de su boca."
    "Descargas una ingente cantidad de semen en su boca, tu pequeña venganza contra sus dientes."
    call BlinkXPS3 ("c21s005_660" , "d") from _call_BlinkXPS3_455
    deb "*Sonido interrogativo*"
    "Te mira sin saber muy bien qué hacer con la carga de semen que llena sus mejillas."
    mc "Puedes tragarlo o escupirlo, como quieras."
    scene c21s005_665An with dissolve
    "Se decide por escupirlo detrás de la piedra donde le has dado placer unos minutos antes."
    call BlinkXPS3 ("c21s005_665a" , "d") from _call_BlinkXPS3_456
    deb "¿Qué tal lo he hecho?"
    mc "Después de esconder los dientes muy bien, cielo."
    mc "Los hombres no podemos fingir orgasmos. *Risa*"
    call BlinkXPS3 ("c21s005_670" , "d") from _call_BlinkXPS3_457
    deb "*Risa* Es verdad, y las pruebas están ahí."
    mc "¿Y a ti? ¿Qué te ha parecido tu primera experiencia?"
    call BlinkXPS3 ("c21s005_675" , "d") from _call_BlinkXPS3_458
    deb "Me ha gustado. Incluso me he vuelto a poner un poquito cachonda. He entendido lo que has dicho antes de excitarte dando placer."
    mc "¿Quieres que probemos a ver si conseguimos un segundo orgasmo para ti? *Risa*"
    call BlinkXPS3 ("c21s005_680" , "d") from _call_BlinkXPS3_459
    deb "*Risa* Hoy no. Tenemos que volver a casa y aún noto las piernas como si fueran de gelatina del primero."
    call BlinkXPS3 ("c21s005_685" , "d") from _call_BlinkXPS3_460
    deb "Lo que me ha sorprendido ha sido el sabor. Siempre he leído en internet que tenía un sabor desagradable, pero no es verdad."
    mc "Supongo que depende de cada persona."
    call BlinkXPS3 ("c21s005_690" , "d") from _call_BlinkXPS3_461
    deb "Aunque deja un regusto especialmente salado... voy a darme un baño y a enjuagarme en el lago."
    deb "No me atrevo a besarte con este sabor en la boca."
    mc "No hay problema, cielo."
    call BlinkXPS3 ("c21s005_695" , "d") from _call_BlinkXPS3_462
    deb "Ve vistiéndote mientras me bebo medio lago. Se está haciendo tarde y vamos a tener que bajar a casa."
    mc "*Risa* A tus órdenes."
    scene c21s005_700An with dissolve
    "[deb.nick] sale corriendo hacia el lago y se zambulle en el agua de un salto."
    "Es una visión preciosa."
    scene c21s005_705An with dissolve
    "No tiene sentido que empieces a cambiarte si después vas a tener que esperar a que se cambie la sirena."
    "Pasas unos momentos observándola en el agua. Desde luego parece un segundo hogar para ella."
    "Aprovechas para limpiarte la polla de los últimos restos de tu corrida antes de que la chica salga del agua."
    scene c21s005_710d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    if not _in_replay:
        $ deb.profileImages.pop (8) # first remove
        $ deb.profileImages.insert (8, ("debbie_8", None)) # then add new
        $ texto = str(deb.nick)
        $ renpy.notify ("Profile Image unlocked for "+str(texto)+": 9 - Naked")
    call BlinkXPS3 ("c21s005_710" , "d") from _call_BlinkXPS3_463
    deb "¿No ibas a cambiarte?"
    mc "He preferido mirarte. Me encanta lo que veo."
    call BlinkXPS3 ("c21s005_715" , "d") from _call_BlinkXPS3_464
    deb "Me encanta tu respuesta. Ahora ya puedo besarte después de quitarme el sabor a ti."
    mc "*Risa* Nunca voy a decir que no a eso."
    scene c21s005_715d with dissolve
    "Solo hay un rastro del frescor del lago en sus labios. Ningún sabor que no pertenezca a [deb.nick]."
    "Vuestros labios se vuelven a rozar, mientras compartís vuestros alientos."
    call BlinkXPS3 ("c21s005_720" , "d") from _call_BlinkXPS3_465
    deb "Será mejor que paremos o no vamos a llegar a tiempo a casa para la cena."
    mc "No me importaría renunciar a la cena por un segundo round. *Risa*"
    scene c21s005_725a with dissolve
    deb "No será hoy. *Risa* ¡Tengo hambre!"
    mc "*Risa* El sexo da hambre a mi fierecilla."
    scene c21s005_725An with dissolve
    "Descubrís que [kat] se ha llevado la toalla de [deb.nick], con lo que compartís la tuya. Por suerte, no se ha llevado también su ropa."
    "Interrumpís el vestiros con besos, risas, y caricias. Pero finalmente acabáis vestidos. La tarde ya toca a su fin."
    call BlinkXPS3 ("c21s005_730" , "d") from _call_BlinkXPS3_466
    mc "Bueno, creo que toca volver a casa."
    deb "Sí. Me da pena irme de aquí, nos lo hemos pasado muy bien hoy."
    mc "Podemos volver cuando quieras."
    call BlinkXPS3 ("c21s005_735" , "d") from _call_BlinkXPS3_467
    deb "La próxima vez quiero que sea en una cama."
    mc "Hay una cama muy grande en mi habitación."
    call BlinkXPS3 ("c21s005_740" , "d") from _call_BlinkXPS3_468
    deb "Y quiero... llegar hasta el final... si crees que estoy preparada."
    mc "Si crees que lo estás, significa que lo estás."
    call BlinkXPS3 ("c21s005_745" , "d") from _call_BlinkXPS3_469
    deb "Dame unos días para pensar un par de cosas que quiero hablar contigo antes."
    mc "Todo el tiempo que necesites, y puedes hablar conmigo de cualquier cosa que necesites."
    call BlinkXPS3 ("c21s005_750" , "d") from _call_BlinkXPS3_470
    deb "Entonces, ya nos podemos ir. Pero antes..."
    scene c21s005_750d with dissolve
    "Su beso sabe a despedida."
    "Sabes que, pese a que todo el mundo sepa que estáis juntos, no va a besarte así en casa."
    "Al menos por un tiempo, aunque no entiendas por qué."
    stop music fadeout (1.5)
    scene c21s005_280c with fade
    "Al cabo de unos minutos emprendéis el camino a casa."
    "De camino a casa intentas sonsacarle el porqué de la timidez de los besos en casa. No obtienes respuestas."
    "Llegáis con tiempo suficiente para ducharos antes de cenar."
    return
label c21s006_Nor:
    scene black with dissolve
    "La cena pasa sin ningún evento reseñable, muchas risas, muchas anécdotas sobre la fiesta del día anterior que te perdiste por no estar en el sitio adecuado."
    "Era imposible estar en todos sitios, y las chicas tienen muchas cosas que contarse unas a otras."
    "Todas guardan silencio sobre lo que pasó en el jacuzzi."
    "[eva] y [ama] no vienen a cenar. [ama] llama para decir que no se encuentran bien. Nada de lo que preocuparse, pero prefieren quedarse en la base."
    if nor._var("route"):
        call c21s006_Teaser from _call_c21s006_Teaser
    return
label c21s006_Teaser:
    call BlinkXPS3 ("c21s006_005" , "d") from _call_BlinkXPS3_471
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    "Al final de la noche, cuando estás ayudando a [nor] a recoger los platos..."
    nor "¿Te apetece subir a mi habitación cuando acabemos? Parece que hace siglos que no estamos a solas."
    mc "Me apetece siempre. Tú también podrías venir a mi habitación."
    call BlinkXPS3 ("c21s006_010" , "d") from _call_BlinkXPS3_472
    nor "Podría, pero hay menos posibilidades de que alguien nos interrumpa en la mía."
    mc "*Risa* Tienes razón. Mi habitación parece un aeropuerto últimamente, con tantas entradas y salidas."
    call BlinkXPS3 ("c21s006_015" , "d") from _call_BlinkXPS3_473
    nor "*Susurrando* ¿Acabas tú de recoger mientras yo subo y me voy poniendo guapa para ti?"
    mc "Ya estás guapa para mí, mi amor. Pero ve subiendo si quieres. En cinco minutos estoy allí."
    nor "Que sean diez."
    scene c21s006_015d with fade
    "Diez minutos después..."
    "*Knock-Knock*"
    mc "Soy yo. ¿Puedo pasar?"
    nor "*A través de la puerta* Pasa, mi amor."
    scene c21s006_020d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c21s006_020" , "d") from _call_BlinkXPS3_474
    nor "Espero que te guste esto. Lo he comprado hoy en la tienda de [mad.nick]."
    stop music fadeout (1.5)
    mc "¡Me encanta!"
    return

label c31:
    default dam = Character("Damien", color="#ffcc80")
    default carl = Character("Carl", color="#ce93d8")
    default fred = Character("Frederic", color="#ef9a9a")
    default mael = Character("Mael", color="#afcc80")
    default flo = Character("Floyd", color="#1e93d8")
    default vin = Character("Vincent", color="#5f9a9a")
    default cal = Character("Caleb", color="#7fcc80")
    default car = Character("Caroline", color="#ff0080")
    default alb = Character("Alba", color="#af0080")
    default lar = Character("Lara", color="#9acfe6")
    default geo = Character("George", color="#36f040")
    default gid = Character("Gideon", color="#36f040")
    default ass = Character(_("Asistente"), color="#0f9a9a")
    if kat._var("route"):
        call c31s001_katLewd from _call_c31s001_katLewd #jugar con comida
    else:
        call c31s001_noKatLewd from _call_c31s001_noKatLewd
    #DayChange
    call c31s002_morning from _call_c31s002_morning
    if lis._var("route"):
        call c31s002_lisFork from _call_c31s002_lisFork
    else:
        call c31s002_noLis from _call_c31s002_noLis
    call c31s002_firstDayWedding from _call_c31s002_firstDayWedding
    call c31s002_kiaChurch from _call_c31s002_kiaChurch #last scene
    #DayChange
    call c31s003_norExhibitionists from _call_c31s003_norExhibitionists
    call c31s002_secondDayWedding from _call_c31s002_secondDayWedding
    call c31s002_farewell from _call_c31s002_farewell #8
    $ dam = Character("Damien", color="#ffcc80")
    $ carl = Character("Carl", color="#ce93d8")
    $ fred = Character("Frederic", color="#ef9a9a")
    $ mael = Character("Mael", color="#afcc80")
    $ flo = Character("Floyd", color="#1e93d8")
    $ vin = Character("Vincent", color="#5f9a9a")
    $ cal = Character("Caleb", color="#7fcc80")
    $ car = Character("Caroline", color="#ff0080")
    $ alb = Character("Alba", color="#af0080")
    $ lar = Character("Lara", color="#9acfe6")
    $ geo = Character("George", color="#36f040")
    $ gid = Character("Gideon", color="#36f040")
    $ ass = Character(_("Asistente"), color="#0f9a9a")
    call c31s004_flight1 from _call_c31s004_flight1 #9
    if bet._var("route"):
        call c31s004_mileHighClub from _call_c31s004_mileHighClub #betLewd 10
    else:
        call c31s004_noMileHighClub from _call_c31s004_noMileHighClub #10
    call c31s004_flight2 from _call_c31s004_flight2 #11
    call c31s005_AarPicksUp from _call_c31s005_AarPicksUp #Ama realizes 12
    call c31s005_houseArrival from _call_c31s005_houseArrival #13
    #DayChange viernes
    call c31s006_Caroline from _call_c31s006_Caroline #14
    call c31s006_baseArrival from _call_c31s006_baseArrival #15
    call c31s006_departmentMeeting from _call_c31s006_departmentMeeting #16
    call c31s006_cloneMeeting from _call_c31s006_cloneMeeting #17
    call c31s006_DanielsFate from _call_c31s006_DanielsFate #MC wants to wait for Eva 18
    #day change sabado
    call c31s007_AmaTour from _call_c31s007_AmaTour #she shows secret place. They meet a D different from Damien and MC confuses him, but rectifies in time 19
    #day change domingo
    call c31s007_surgery from _call_c31s007_surgery #20
    call c31s007_ama from _call_c31s007_ama
    return

label c31s001_noKatLewd:
    if _in_replay:
        call mrS3_kat_slim from _call_mrS3_kat_slim_5
        call mrS3_rels from _call_mrS3_rels_39
        play music ("music/AmbientPianoStrings.ogg")
        call c30s007_noKatLewd from _call_c30s007_noKatLewd_1
    else:
        play music ("music/AmbientPianoStrings.ogg")
    call BlinkXS4("c31s001_005") from _call_BlinkXS4_1323
    mc "[kat], espera..."
    kat "¿Qué pasa?"
    mc "Creo que voy a estar muy ocupado en los próximos días y has traído un par de gofres."
    mc "¿Quieres quedarte y comerte uno conmigo?"
    call BlinkXS4("c31s001_010") from _call_BlinkXS4_1324
    kat "*Risa* Nunca digo que no a un gofre."
    if kat._var("slim"):
        kat "Y esta semana aún me puedo saltar la dieta una vez."
    mc "Pásame unos shorts del armario, por favor."
    scene c31s001_010d with fade
    "Después de vestirte te sientas con [kat] a comeros los gofres en el sofá."
    "No tiene nada que ver con la no-cita."
    "La tensión que había aquel día ya se resolvió y ahora tan solo sois dos amigos comiendo algo a altas horas de la noche."
    "Dos amigos que se ríen de lo que hubiera podido pasar si no lo hubierais resuelto."
    if mc._var("relationships") > 1:
        "[kat] incluso bromea sobre que se podría haber tatuado algo relacionado con la no-cita si se hubiera tenido que casar contigo hoy."
        "Quizás un gofre. Aunque seguramente no lo hubiera hecho."
    "Son unos gofres que saben a despedida. No sabes si vas a tener mucho tiempo para pasarlo a solas con [kat] en los próximos dos días."
    scene c31s001_010e with fade
    "Demasiado pronto, o demasiado tarde si os tenéis que fiar del reloj, [kat] te da un abrazo antes de irse."
    "Es un abrazo que dice que te va a echar de menos, aunque sus labios no pronuncien las palabras. Tú también la echarás de menos."
    scene c31s001_010f with fade
    "Te acuestas sólo y duermes como un lirón."
    stop music fadeout (1.5)
    "Tienes un extraño sueño en el que [kat] se tatúa un gofre en el hombro."
    return
label c31s001_katLewd:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_kat_slim from _call_mrS3_kat_slim_6
        call mrS3_eil_route from _call_mrS3_eil_route_27
        call mrS3_sai_route from _call_mrS3_sai_route_23
        call mrS3_rels from _call_mrS3_rels_40
        play music ("music/Bolero.ogg")
        call c30s007_KatLewd from _call_c30s007_KatLewd_1
    else:
        play music ("music/Bolero.ogg")
    scene c31s001_015a with fade
    call BlinkXS4("c31s001_015") from _call_BlinkXS4_1325
    "Te levantas de la cama y te acercas a la hermosa mujer."
    mc "Pero antes, quiero besar a mi esposa, y para eso necesito quitarte los gofres de las manos."
    kat "Lo... que... quieras..."
    mc "¿Pasa algo, [kat]?"
    call BlinkXS4("c31s001_020") from _call_BlinkXS4_1326
    kat "Estas desnudo..."
    mc "Lo sé. No es la primera vez que me ves así."
    kat "Lo sé. Pero esto se está volviendo... demasiado real..."
    mc "Permíteme dejar los gofres en la cama."
    call BlinkXS4("c31s001_025") from _call_BlinkXS4_1327 #agachado dejando los gofres
    kat "¡Joder, [mc]! Podrías partir nueces con ese culo..."
    mc "*Risa* Gracias, supongo."
    kat "No me des las gracias. Verte los huevos desde aquí es una visión... rara."
    call BlinkXS4("c31s001_030") from _call_BlinkXS4_1328
    mc "*Risa* ¿No te gustan mis huevos?"
    kat "Me gustas tú. Algunas partes específicas de ti... no tanto."
    mc "Supongo que nos pasa a todos..."
    call BlinkXS4("c31s001_035") from _call_BlinkXS4_1329
    kat "¿Hay algo específico de mí que no te guste? Aparte de mi peso..."
    mc "Tu peso forma parte de ti. Lo único que no me gusta son tus labios."
    call BlinkXS4("c31s001_040") from _call_BlinkXS4_1330
    kat "¿Qué les pasa a mis labios?"
    mc "Que no están besando los míos."
    call BlinkXS4("c31s001_045") from _call_BlinkXS4_1331
    kat "*Risa* Desde luego eres idiota..."
    mc "Creo que tú eres más idiota, si no has pillado la indirecta."
    kat "¿Quién te ha dicho que no la he pillado?"
    scene c31s001_900pv with dissolve
    show c31s001_900v
    "No hace falta que habléis más. Sus labios buscan los tuyos. Los tuyos buscan los suyos."
    "Notas cómo el beso empieza nervioso por su parte, pero es una sensación que va diluyéndose tal como pasan los segundos."
    "No llega a desaparecer del todo, pero ella está mucho menos tensa que cuando vuestros labios se han unido."
    scene c31s001_905pv with dissolve
    show c31s001_905v
    hide c31s001_900v
    "Los labios de [kat], húmedos y carnosos, empiezan a presionar contra los tuyos cada vez con más ansia." id c31s001_katLewd_6c7ddb23
    "Su lengua empieza a jugar con la tuya con más seguridad, reclamando el premio a su valentía."
    "Tus dedos recorren las generosas curvas de su espalda mientras tu polla empieza a crecer."
    scene c31s001_050a with fade
    call BlinkXS4("c31s001_050") from _call_BlinkXS4_1332
    hide c31s001_905v
    kat "Creo que acabas de conseguir que empape otras bragas."
    mc "Espero que no tengas más bragas para cambiarte. Volvería a intentar empaparlas."
    call BlinkXS4("c31s001_055") from _call_BlinkXS4_1333
    kat "..."
    mc "¿Pasa algo [kat]?"
    call BlinkXS4("c31s001_060") from _call_BlinkXS4_1334
    kat "Te lo he dicho antes. Esto se está volviendo demasiado real."
    $ ready1 = False
    if kat._var("slim"):
        mc "Si tienes dudas, podemos esperar..."
        if persistent.walkthrough:
            $ wt1 = _("Escena de sexo con [kat].")
            $ wt2 = _("Más elecciones después.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "A que estés preparada." (wt=wt1):
                $ ready1 = True
            "A que hayas llegado al peso al que quieres llegar." (wt=wt2):
                stop music fadeout (1.5)
                call BlinkXS4("c31s001_065") from _call_BlinkXS4_1335 #triste
                kat "Sabía que no podía ser tan bonito, y que tú no podías ser tan perfecto..."
                play music ("music/Sad-Piano.ogg")
                kat "Creo que será mejor que lo dejemos aquí, [mc]."
                mc "¿Qué quieres decir?"
                call BlinkXS4("c31s001_070") from _call_BlinkXS4_1336
                kat "Sabía que mi peso sería un problema... Sé el tipo de chicas a las que estás acostumbrado..."
                kat "No entro dentro de los cánones de belleza habituales... Casi lo primero de lo que has hablado ha sido mi peso."
                if persistent.walkthrough:
                    $ wt1 = _("Escena de sexo con [kat].")
                    $ wt2 = _("Ruptura con [kat].")
                else:
                    $ wt1 = ""
                    $ wt2 = ""
                menu:
                    "No me refería a eso." (wt=wt1):
                        call BlinkXS4("c31s001_075") from _call_BlinkXS4_1337
                        kat "¿A qué te referías, entonces?"
                        mc "Sé que estás haciendo un esfuerzo muy grande para llevar una vida más sana y bajar de peso."
                        mc "Y es posible que creas que vas a disfrutar mucho más esto entonces."
                        call BlinkXS4("c31s001_080") from _call_BlinkXS4_1338
                        kat "No te entiendo..."
                        mc "Has estado mucho más nerviosa durante el beso de lo que has estado en los últimos días."
                        mc "Y nos hemos besado muchas veces en la última semana. Cada vez que nos hemos visto. Sé cómo besas."
                        call BlinkXS4("c31s001_085") from _call_BlinkXS4_1339
                        kat "Es normal, ¿no? Aún lo estoy asimilando..."
                        mc "Sí, lo es. Por eso he dicho lo del peso. Te daría tiempo de asimilar todo lo que está pasando."
                        stop music fadeout (1.5)
                        mc "Tiempo para estar preparada..."
                        play music ("music/Bolero.ogg")
                    "Tienes razón." (wt=wt2):
                        mc "He hablado sin pensar, pero creo que, haciéndolo, he dicho lo que más me preocupaba de estar contigo."
                        call BlinkXS4("c31s001_090") from _call_BlinkXS4_1340
                        $ kat._var("route", False)
                        $ kat._var("breakup", True)
                        $ kat._var("engaged", False)
                        $ mc._var("relationships", -1, "add")
                        kat "Sabes que acabas de sonar muy superficial, ¿verdad?"
                        kat "Pero me alegra que lo hayas hecho. No puedo evitarlo si no te excito lo suficiente."
                        mc "No es eso, [kat]..."
                        call BlinkXS4("c31s001_095") from _call_BlinkXS4_1341
                        kat "Es precisamente eso, [mc]. Lo primero que ves en mí cuando eliminas los filtros, es mi peso."
                        kat "Creía que eras diferente, pero..."
                        mc "Lo siento..."
                        call BlinkXS4("c31s001_100") from _call_BlinkXS4_1342
                        kat "No hace falta que lo sientas. Había una posibilidad ínfima de que esto saliera bien."
                        kat "Al menos hemos descubierto la verdad antes de que pase nada de lo que nos podamos arrepentir."
                        scene c31s001_100d with dissolve
                        kat "Voy a prepararme algo para comer. Te veo mañana."
                        mc "Aquí hay dos gofres..."
                        call BlinkXS4("c31s001_105") from _call_BlinkXS4_1343
                        kat "Esos gofres los he traído para ti porque no te hemos dejado cenar. No me los voy a comer contigo."
                        kat "Ahora mismo quiero estar lejos de ti. Espero que lo entiendas."
                        scene c31s001_105d with hpunch
                        play sound ("music/Portazo.ogg")
                        "*Blam*"
                        "Da un portazo al salir."
                        kat "*A través de la puerta* *Para sí misma* ¡Al menos no me tatué un estúpido anillo!"
                        "Te sientes mal porque sabes que, por hablar sin pensar, le has hecho daño."
                        scene c31s001_010f with fade
                        "Te acuestas sólo y te cuesta un buen rato dormirte. No haces más que darle vueltas a lo de [kat]."
                        "Las palabras, aunque dichas sin mala intención, pueden hacer más daño que los hechos."
                        stop music fadeout (1.5)
                        "Te preguntas si, después de esto, podréis seguir siendo amigos."
                        return
    else:
        mc "Podemos esperar a que estés preparada."
    call BlinkXS4("c31s001_110") from _call_BlinkXS4_1344
    kat "¿Preparada? No creo que vaya a estar más preparada que hoy."
    kat "Si tenía alguna duda, desapareció mientras me hacía el tatuaje."
    kat "Nunca te tatúes un gofre en dos colores. Duele que te cagas."
    mc "*Risa* No tengo intención de tatuarme un gofre. Ni nada en concreto."
    mc "Si lo hubieras hecho rectangular, a lo gofre belga, quizás hubiera dolido menos al tener menos superficie que rellenar con tinta."
    call BlinkXS4("c31s001_115") from _call_BlinkXS4_1345
    kat "Pero entonces no hubiera sido nuestro gofre de nuestra no-cita."
    mc "Tienes razón."
    call BlinkXS4("c31s001_120") from _call_BlinkXS4_1346
    kat "*Risa* ¿Me vas a regalar una camiseta que ponga eso?"
    mc "No creo. Me han dicho que, si me la compro yo, nunca más me darán la razón."
    call BlinkXS4("c31s001_125") from _call_BlinkXS4_1347
    kat "Pues entonces prefiero no llevar una camiseta así."
    kat "Pero se te van a enfriar los gofres. Deberías comértelos ya."
    mc "Tienes razón."
    scene c31s001_130An with dissolve
    kat "Mmmmm... No me refería a ese gofre, pero no voy a protestar."
    mc "*Smooch* Te he dicho que este es el gofre del que más hambre tengo."
    mc "*Smooch* Aunque tengo más hambre de ti todavía."
    if not kat._var("slim") or ready1:
        call BlinkXS4("c31s001_135") from _call_BlinkXS4_1348
        kat "¿Estás seguro de querer esto, [mc]?"
        mc "*Smooch* ¿Qué quieres decir?"
        kat "No soy [sai] o [eil]. Nunca voy a estar tan delgada como ellas..."
        mc "Mírame, [kat]."
        call BlinkXS4("c31s001_140") from _call_BlinkXS4_1349
        kat "Espero que no sea ahora cuando me dices que no quieres salir con una chica que parece una albóndiga y que todo esto era una broma cruel."
        mc "No, ahora es cuando te digo que no pareces una albóndiga."
        mc "Es cuando te digo que si estoy contigo es porque me gustas como eres."
        mc "No quiero que pienses que solo me gusta un tipo de chica concreto. Me gustas tú."
        mc "[sai] y [eil] no están aquí. Tú sí. Y estoy ansioso por descubrir lo que nos depara esta noche."
        call BlinkXS4("c31s001_145") from _call_BlinkXS4_1350
        kat "Pero..."
        mc "Sabes que los hombres no podemos disimular cuando algo nos excita, ¿verdad?"
        scene c31s001_150d with dissolve
        pause (1.5)
        call BlinkXS4("c31s001_150") from _call_BlinkXS4_1351
        kat "*Risita* Vale. Me has convencido."
        mc "¿Y sabes qué es lo que me va a excitar un montón? Quitarte ese camisón."
    else:
        mc "Y no puedo esperar a quitarte ese camisón."
    mc "Cuando estés preparada."
    call BlinkXS4("c31s001_155") from _call_BlinkXS4_1352 #Mirando a la puerta levanta los brazos
    kat "Cuando quieras..."
    mc "Si lo tengo que hacer cuando quiera, debería viajar en el tiempo. Llevo diez minutos queriendo hacerlo."
    call BlinkXS4("c31s001_160") from _call_BlinkXS4_1353
    kat "*Risa* Estoy segura de que eso sonaba mejor en tu cabeza cuando lo has pensado."
    mc "Solo depende de si lo único que pretendía con esa frase era hacerte reír."
    scene c31s001_165An with dissolve
    kat "*Risita* ¿Para poder desnudarme por sorpresa?"
    mc "¿Era una sorpresa?"
    kat "*Risita* No."
    mc "Mírame."
    call BlinkXS4("c31s001_170") from _call_BlinkXS4_1354
    mc "¿Hay alguna razón para que te estés tapando?"
    kat "Porque..."
    mc "Espero que esa frase no continúe con 'porque no tengo las tetas como las de [sai] o [eil].'"
    call BlinkXS4("c31s001_175") from _call_BlinkXS4_1355
    kat "Creo que me empiezas a conocer demasiado bien..."
    kat "¿Tú las has visto...?"
    call BlinkXS4("c31s001_180") from _call_BlinkXS4_1356
    kat "*Risa* Vale, sí. Es una pregunta estúpida. Claro que las has visto."
    if not eil._var("route") and not sai._var("route"):
        kat "Saliste con las dos..."
    elif eil._var("route") and not sai._var("route"):
        kat "Saliste con las dos y has vuelto con [eil]..."
    elif sai._var("route") and not eil._var("route"):
        kat "Saliste con las dos y has vuelto con [sai]..."
    else:
        kat "Saliste con las dos y has vuelto con ellas..."
    mc "¿Las tetas de cuál de ellas te gustan más?"
    call BlinkXS4("c31s001_185") from _call_BlinkXS4_1357
    kat "¿QUÉ? ¿ME ESTÁS PREGUNTANDO SOBRE MI PREFERENCIA EN CUANTO A TETAS?"
    mc "Tú has sacado el tema de conversación, y es un gusto que compartimos."
    mc "¿Cuál de ellas crees que tiene mejores tetas?"
    call BlinkXS4("c31s001_190") from _call_BlinkXS4_1358
    kat "Las de [sai] son enormes, pero las de [eil] son perfectas en su tamaño. Sería una elección muy difícil."
    kat "Por norma, diría que las de [sai], pero..."
    call BlinkXS4("c31s001_195") from _call_BlinkXS4_1359
    kat "¿Y tú? ¿Qué tetas prefieres?"
    scene c31s001_195An with dissolve
    mc "Estas. Ahora mismo son las únicas que me importan."
    "[kat] mira sus tetas como si descubriese que hace un par de minutos que ha retirado sus manos."
    call BlinkXS4("c31s001_200") from _call_BlinkXS4_1360
    kat "Eso no responde mi pregunta, pero me gusta la respuesta."
    mc "Es la única respuesta que me vas a sacar esta noche sobre ese tema."
    scene c31s001_200d with hpunch
    "La chica medio desnuda salta a tus brazos, obligándote a incorporarte y buscando tus labios, como tantas veces ha hecho en los últimos días."
    "Si necesitaba que le dieran seguridad, tus palabras han cumplido su función."
    scene c31s001_200An with dissolve
    "Por muchas veces que hable sobre su peso, [kat] es suficientemente ligera como para que la lleves en brazos a la cama."
    "No es ningún esfuerzo que requiera que tus labios se separen de los suyos."
    scene c31s001_205An1 with dissolve
    "En ese momento los besos empiezan a subir de temperatura."
    "Casi parece una batalla para decidir quién besa a quién."
    "Dejas que ella gane por momentos la batalla que ninguno de los dos sabéis que estáis luchando."
    "Una batalla en la que no hay perdedores."
    "Pero siempre retomas el control al cabo de unos segundos."
    "A tus ancestros guerreros (estás seguro de que los tienes) no les gusta perder una batalla, aunque sea ficticia." id c31s001_katLewd_3bc33495
    scene c31s001_205An2 with dissolve
    play sound ("music/Slap.ogg")
    "Uno de los pies de [kat] golpea el bote de chocolate, que acaba tirado en el suelo."
    "Es la señal que interrumpe la agradable batalla."
    "Hay que quitar los gofres del colchón antes de que suceda un accidente."
    scene c31s001_210a with fade
    call BlinkXS4("c31s001_210") from _call_BlinkXS4_1361
    stop music fadeout (1.5)
    "[kat] aprovecha para quitarse los zapatos mientras guardas el edredón."
    play music ("music/NightJazzBeats.ogg")
    kat "¿Sabes de algún país que esté atravesando una sequía extrema ahora mismo?"
    mc "Me acabas de descolocar. ¿Por qué lo preguntas?"
    kat "Para mandarles mis bragas. Si las escurren bien, creo que podrían llenar el Lago Victoria, si tienen problemas de agua."
    mc "*Risa* Claro que sí, cielo, y con tu primer orgasmo podemos convertir el Valle de la Muerte en un pantano."
    call BlinkXS4("c31s001_215") from _call_BlinkXS4_1362
    kat "*Risa* ¡Mierda! Eso ha sido mejor que lo del Lago Victoria."
    mc "Pero si tan empapadas están tus bragas, creo que debería ser el momento para quitarlas, ¿no?"
    call BlinkXS4("c31s001_220") from _call_BlinkXS4_1363
    kat "No queremos que lo que cubren se resfríe..."
    kat "*Risa* ¡Y que se ponga a estornudar! ¿Cómo sonaría el estornudo de un coño?"
    mc "*Risa* A veces piensas en unas cosas... un poco extrañas."
    call BlinkXS4("c31s001_225") from _call_BlinkXS4_1364
    kat "Tengo la cabeza pensando cosas a mil por hora las 24 horas del día desde que me besaste en la piscina."
    kat "O incluso desde la no-cita..."
    kat "No puedes esperar que todos mis pensamientos sean coherentes."
    mc "No espero eso ni siquiera de mis propios pensamientos, [kat]."
    mc "Pero creo que voy a retirar esas bragas empapadas."
    scene c31s001_230An with dissolve
    "Llevas tus manos a la cinturilla de sus bragas, donde esperas un par de segundos antes de retirarlas."
    "Querías darle la oportunidad de pararte antes de quitarle las bragas que, realmente, están empapadas. Te alegras de que no lo haya hecho." id c31s001_katLewd_5c51b3b7
    call BlinkXS4("c31s001_235") from _call_BlinkXS4_1365
    kat "Pues esta soy yo... Ya no hay nada más que esconder."
    mc "Ni ninguna razón para hacerlo. Me encanta lo que veo."
    kat "¿Cómo sigue esto? ¿Qué hacemos ahora?"
    call BlinkXS4("c31s001_240") from _call_BlinkXS4_1366
    "Te levantas y te diriges a la puerta, caminando de espaldas, sin perder de vista su cara de sorpresa, todavía con sus bragas en la mano."
    kat "¿Dónde vas?"
    mc "Tengo que mandar esto a Etiopía antes de que se sequen para que llenen el Lago Victoria."
    call BlinkXS4("c31s001_245") from _call_BlinkXS4_1367
    kat "*Risa* ¡Mi marido es idiota!"
    "Tras hacerla reír, dejas las empapadas bragas en el mueble de la televisión."
    mc "¿Qué he hecho ahora?"
    kat "¡El Lago Victoria no está en Etiopía! Kenia está en medio."
    mc "¿Realmente crees que me preocupa si un pequeño error geográfico estropea la broma?"
    mc "La culpa es tuya por no haber dicho el Lago Michigan."
    call BlinkXS4("c31s001_250") from _call_BlinkXS4_1368
    kat "Para el Michigan necesitarías mandar también las bragas del otro día. Tiene más o menos el doble de capacidad del Victoria."
    mc "¿Me vas a dar una clase de geografía lacustre?"
    kat "Lo estudié en limnología. Quería demostrarte que te has casado con una chica lista."
    mc "¿Limno-qué? Mejor no contestes. Prefiero que generes lagos sobre mis sábanas." id c31s001_katLewd_bad62c5c
    call BlinkXS4("c31s001_255") from _call_BlinkXS4_1369
    kat "¿Me estás haciendo reír para que me olvide de lo que está a punto de pasar?"
    mc "No. Te hago reír porque me encanta oírte reír. No necesito ninguna otra razón para hacerlo."
    mc "Para que te olvides de lo que está a punto de pasar tengo otras opciones."
    call BlinkXS4("c31s001_260") from _call_BlinkXS4_1370
    kat "¿Qué opciones?"
    mc "Hacer que pase."
    scene c31s001_265An with dissolve
    "Te agachas entre las piernas entreabiertas de [kat], que se van abriendo cada vez más, guiándote a tu objetivo."
    kat "*GEMIDO*"
    "El primer contacto de tu lengua con su clítoris produce un escalofrío en la chica y un enorme gemido."
    call BlinkXS4("c31s001_270") from _call_BlinkXS4_1371
    mc "¿Sigues dándole vueltas a lo que va a pasar? ¿O puedo continuar haciendo que pase?"
    kat "Puedes continuar. Ahora mismo tengo el cerebro... No sé ni cómo lo tengo..."
    scene c31s001_920pv with dissolve
    show c31s001_920v
    #hide c31s001_905v
    "Continuas. Tu lengua parece seca en comparación con el lago que [kat] tiene entre sus piernas."
    kat "*Gemido* ¡Justo ahí! *Jadeo*"
    "'Ahí' es un término relativo cuando estás recorriendo cada pliegue de su coño."
    kat "*Jadeo* ¡Joder! *Gemido* ¡Eres bueno en esto! *Jadeo*"
    "Te lo tomas como un cumplido. Siempre habías oído que una mujer conoce mejor el cuerpo de otra de lo que ningún hombre puede hacer."
    scene c31s001_915pv with dissolve
    show c31s001_915v
    hide c31s001_920v
    "Te preocupaba no estar a la altura de las experiencias previas de [kat] cuando llegara este momento."
    kat "*Gemido* ¿Dónde has aprendido eso? *Jadeo* ¡Se siente increíble! *Gemido*"
    "Parece que te preocupabas por nada. Parece que nadie había rozado su corta barba contra los labios de [kat]."
    "Prefieres no imaginarte a un par de lesbianas barbudas. A cada cual lo suyo, pero prefieres ser el único barbudo en una relación."
    kat "*Jadeo* Si sigues así... *Gemido* me voy a correr en seguida... *Jadeo*"
    scene c31s001_910pv with dissolve
    show c31s001_910v
    hide c31s001_915v
    "Eso formaba parte del plan. Si empieza a tener orgasmos, se olvidará de las dudas que le quedaran."
    kat "*Gemido* ¡Por todos los gofres del mundo! *Jadeo* ¡Eso es alucinante! *Gemido*"
    "Has vuelto a dedicar tu lengua a recorrer su coño, esta vez centrándote cada vez más en excitar su clítoris."
    kat "*JADEO* ¡ESTÁ LLEGANDO! *GEMIDO* ¡PUEDO NOTARLO! *JADEO*"
    "Tú también notas en las yemas de tus dedos cómo su pierna se empieza a tensar al unísono con el resto de su cuerpo."
    call OrgasmXS4("c31s001_275") from _call_OrgasmXS4_48
    kat "*GEMIDO* ¡JODER! *JADEO* ¡AQUÍ ESTÁ! *GEMIDO* ¡SÍ! *JADEO*"
    "Ella explota en tu boca antes de acabar sus entrecortadas frases, regando tu lengua con una increíble combinación de sabores."
    "Es el sabor habitual, pero con pequeños matices que mejoran la sensación, haciéndolo único."
    "A veces crees que podrías reconocer a cada una de las mujeres con las que has estado por el sabor de sus orgasmos."
    "Sigues lamiendo para recoger con tu lengua cada una de las gotas de sus fluidos."
    scene c31s001_280a with fade #partir de 270
    call BlinkXS4("c31s001_280") from _call_BlinkXS4_1372
    "Al cabo de un momento, cuando su cuerpo empieza a relajarse y se derrumba sobre la cama..."
    mc "¿Cómo estás?"
    kat "¿Cómo estoy? Flipando. Anonadada. Entusiasmada. Incrédula."
    mc "¿Incrédula?"
    call BlinkXS4("c31s001_285") from _call_BlinkXS4_1373
    kat "[sai] me dijo que eras MUY bueno en esto. Decía que leías el cuerpo de una mujer de una forma que ella no creía que pudiera ser posible."
    kat "Yo creía que ella estaba exagerando. Me equivocaba."
    mc "Me lo tomaré como que te ha gustado."
    call BlinkXS4("c31s001_290") from _call_BlinkXS4_1374
    kat "Sólo hay una cosa que no me ha gustado. No he podido devolverte el favor."
    kat "Y no digas que esto no va de devolver favores."
    mc "No va de devolver favores."
    call BlinkXS4("c31s001_295") from _call_BlinkXS4_1375
    kat "*Risa* ¡Te he dicho que no me lo digas!"
    mc "Pero es verdad. Esto va de ti y de mí. No de quién hace qué ni en qué orden. Ni de llevar la cuenta de cuántos orgasmos llevamos cada uno." id c31s001_katLewd_5701d64f
    kat "Bueno, ahora creo que es mi turno. Túmbate."
    scene c31s001_300a with fade
    call BlinkXS4("c31s001_300") from _call_BlinkXS4_1376
    "Intercambiáis posiciones y [kat] te mira como preguntándose cómo empezar la mamada que supones que va a hacerte."
    kat "Es mucho más grande de lo que imaginaba. Y tengo mucha imaginación. Y ya lo había visto, pero ahora parece más grande."
    mc "*Risa* No voy a pedir disculpas por ello."
    call BlinkXS4("c31s001_305") from _call_BlinkXS4_1377
    "La chica se agacha y toca por primera vez una polla, mirándola hipnotizada. Eres el afortunado propietario de la primera polla que toca."
    kat "También está más caliente de lo que esperaba... Pero igual de dura de lo que suponía."
    mc "Bueno, has acertado una de tres. De momento estás suspendida."
    call BlinkXS4("c31s001_310") from _call_BlinkXS4_1378
    kat "Pues tendré que hacer algo para que el profesor me suba la nota, ¿no?"
    kat "En las pelis porno funciona."
    mc "Creo que también funciona en la vida real."
    scene c31s001_315a with fade
    call BlinkXS4("c31s001_315") from _call_BlinkXS4_1379
    "[kat] te sorprende sentándose a horcajadas sobre ti. Puedes notar el calor que emana de su coño en tu polla. Parece que no va a haber mamada."
    kat "*Gemido* Nunca me ha gustado suspender."
    mc "Creo que acabas de subir algunas décimas tu nota."
    scene c31s001_315d with dissolve
    "Sus todavía empapados labios parecen abrazar la base de tu astil de forma que parecen hechos para encajar perfectamente."
    kat "*Gemido* Noto como tu polla... pulsa... contra mi clítoris. Es MUY agradable."
    mc "Si quieres, puedes deslizarte sobre el astil. Creo que te va a gustar."
    call BlinkXS4("c31s001_320") from _call_BlinkXS4_1380
    kat "¿Quieres que esto sea el inicio de una hermosa amistad entre nuestras partes nobles?"
    mc "*Risa* Ese es el objetivo."
    scene c31s001_940pv with fade
    show c31s001_940v
    hide c31s001_910v
    "[kat] empieza a deslizar sus labios a lo largo de tu astil, tras reajustar su postura, tal como le has indicado."
    kat "*Gemido* Tenías razón. *Jadeo* Esto es AÚN más agradable. *Gemido*"
    "La chica parece que le ha perdido el miedo que le pudiera tener a Mjolnir. Es un gran paso en la buena dirección."
    kat "*Jadeo* ¡Me encanta! *Gemido*"
    "Es como si su coño te estuviera haciendo una paja sin manos. Una maravillosa y húmeda paja sin manos."
    scene c31s001_945pv with dissolve
    show c31s001_945v
    hide c31s001_940v
    "[kat] ajusta su posición buscando mayor tracción, sin conseguirlo."
    "Una de sus rodillas no llega a tocar el colchón y se impulsa con su muslo contra el tuyo."
    kat "*Gemido* Esto es como masturbarme usándote a ti. *Jadeo*"
    kat "*Jadeo* Por alguna razón es más excitante que cualquier paja que me haya hecho. *Gemido*"
    "Esa es la razón por la que el sexo sin penetración existe. La experiencia compartida hace que mejore una barbaridad."
    scene c31s001_950pv with dissolve
    show c31s001_950v
    hide c31s001_945v
    "Ella vuelve a ajustar su posición, buscando hacer tracción esta vez con el tobillo en vez de con la rodilla. Esta vez lo consigue."
    kat "*GEMIDO* ¡Ahora sí! *JADEO* ¡Es increíble! *GEMIDO*"
    "Sus movimientos, con algo de espasmódico en ellos, denotan que ella está mucho más cerca de su segundo orgasmo que tú del primero de los tuyos."
    kat "*JADEO* ¡ESTOY A PUNTO DE CORRERME! *GEMIDO* ¡OTRA VEZ! *JADEO*"
    "Tus caderas se mueven al mismo ritmo que las de la chica. Intentando maximizar el contacto."
    call OrgasmXS4("c31s001_325") from _call_OrgasmXS4_49
    kat "*GEMIDO* ¡OH, SÍ! *JADEO* ¡ALUCINANTE! *GEMIDO*"
    "Los placenteros espasmos del orgasmo empiezan a recorrer a [kat] de arriba a abajo, haciendo que sus movimientos se vuelvan más inconexos."
    "Ella busca movimientos más largos, que recorran toda tu polla."
    scene c31s001_330An with dissolve
    "Pero, durante otro reajuste de postura, uno de sus movimientos es demasiado largo."
    "En el camino de vuelta se empala en Mjolnir."
    kat "*JADEO*"
    call OrgasmXS4("c31s001_335") from _call_OrgasmXS4_50 #Sorpresa, dolor, placer
    "Su cara refleja todas las emociones que le embargan en unos segundos en los que se queda inmóvil."
    kat "*GEMIDO*"
    "Sorpresa primero, seguida de una expresión de dolor que pasa brevemente para ser sustituida por una de placer."
    call BlinkXS4("c31s001_340") from _call_BlinkXS4_1381
    "De vuelta a la sorpresa cuando su cerebro se da cuenta de lo que ha pasado."
    kat "*Gemido* ¿Qué has hecho?"
    mc "¿Yo? Sólo he estado quieto."
    mc "¿Cómo estás? Si es incómodo o hay alguna otra razón..."
    call BlinkXS4("c31s001_345") from _call_BlinkXS4_1382
    kat "Me siento rara. Muy rara con tu polla dentro de mí."
    kat "Pero rara en plan bien. Y no pienso bajar de aquí. Déjame cambiar de posición."
    scene c31s001_350a with fade #partir de la 965
    call BlinkXS4("c31s001_350") from _call_BlinkXS4_1383
    kat "Mucho mejor así. Antes la rodilla no me llegaba al colchón y... era incómodo hasta que he encontrado la mejor posición."
    mc "Lo importante es que estés cómo..."
    scene c31s001_960pv with dissolve
    show c31s001_960v
    hide c31s001_950v
    "No te deja acabar la frase antes de empezar a cabalgarte."
    kat "*Gemido* Calla y fóllame. *Jadeo*"
    "Es su primera vez con una polla dentro, pero, una vez la sorpresa inicial ha pasado, se comporta como una experta cabalgadora."
    kat "*Jadeo* ¡No duele nada! *Gemido*"
    "Algún día le preguntarás por sus experiencias previas con el sexo. Hoy no será ese día."
    scene c31s001_955pv with dissolve
    show c31s001_955v
    hide c31s001_960v
    "Mjolnir se dobla en un ángulo que no creías que fuera posible, guiado por los labios de la chica hacia el interior de su coño."
    kat "*GEMIDO* ¡ESTO NO PUEDE ESTAR PASANDO! *JADEO*"
    "Su cuerpo vibra de una forma que empiezas a conocer. Una forma que adorarás en los próximos años."
    "Su siguiente orgasmo está llamando a las puertas. Se ha empalado en medio de un orgasmo y su excitación no ha desaparecido durante la corta conversación."
    kat "*JADEO* ¡VOY A CORRERME OTRA VEZ! *GEMIDO* ¡NO ME LO PUEDO CREER! *JADEO*"
    "Tú no tienes ningún problema para creértelo. Su cuerpo te dice lo que sus palabras confirman."
    call OrgasmXS4("c31s001_355") from _call_OrgasmXS4_51
    kat "*GEMIDO* ¡POR EL AMOR DE DIOS! *JADEO* ¡ESTO ES ALUCINANTE! *GEMIDO*"
    "Su coño se cierra con fuerza sobre tu astil, mientras lo riega con sus fluidos."
    "Sus paredes vaginales parecen un húmedo guante apretando la longitud de tu polla con una fuerza inusitada."
    scene c31s001_970pv with dissolve
    show c31s001_970v
    hide c31s001_965v
    "Pero ella no deja de cabalgarte. Ha descubierto una nueva droga recorriendo su cuerpo."
    "Encadenar orgasmo tras orgasmo puede ser muy poderoso."
    kat "*JADEO* ¡NO SABÍA QUE ESTO PODÍA SER ASÍ! *GEMIDO*"
    "La primera experiencia con una polla dentro también puede ser muy poderosa."
    kat "*GEMIDO* ¡NO PUEDO PARAR DE CORRERME! *JADEO*"
    scene c31s001_965pv with dissolve
    show c31s001_965v
    hide c31s001_955v
    "Tu orgasmo repta... o hace un sprint... por tus muslos empujado por las contracciones de su coño."
    "No vas a poder aguantar mucho más."
    kat "*JADEO* ¡CÓRRETE CONMIGO! *GEMIDO* ¡CORRETE DENTRO! *JADEO*"
    "Ella no va a hacer nada para sacar tu pulsante polla de su interior. Y tú no quieres llevarle la contraria."
    "Un simple movimiento de tus caderas podría sacar tu polla de su húmedo nuevo hogar. Lo hubieras hecho si no te hubiera pedido lo contrario."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[kat] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    if persistent.pregnancy:
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ kat._var("pregnant", True)
                $ kat._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    call OrgasmXS4("c31s001_360") from _call_OrgasmXS4_52
    mc "¡Mpfft!"
    "Finalmente explotas dentro del coño de [kat], llenándola con tu semen hasta agotar su capacidad de mantenerlo dentro."
    kat "*GEMIDO* ¡SÍ! *JADEO* ¡EXPERIENCIA COMPLETA! *GEMIDO*"
    "No puedes imaginarte la reprogramación que ha tenido que hacer [kat] de su cerebro en el último mes."
    "De lesbiana convencida que desconfiaba de los hombres, a recibir su primera descarga de semen mientras experimenta orgasmo tras orgasmo."
    scene c31s001_365a with fade
    call BlinkXS4("c31s001_365") from _call_BlinkXS4_1384
    "Cuando los espasmos que recorren vuestros cuerpos finalizan, [kat] ajusta su posición antes de hablar, sin desempalarse de Mjolnir."
    kat "*Gemido* Eso ha sido alucinante..."
    mc "*Risa* Lo tomaré como que tu primera experiencia con un hombre ha sido positiva."
    call BlinkXS4("c31s001_370") from _call_BlinkXS4_1385
    kat "Ha sido alucinante..."
    stop music fadeout (1.5)
    scene c31s001_370d with dissolve #se tapa la cara con una mano
    kat "Espera..."
    call BlinkXS4("c31s001_375") from _call_BlinkXS4_1386
    play music ("music/On-The-Rise.ogg")
    kat "Ha sido increíble. Ha sido la hostia. Han sido los mejores orgasmos de mi vida. Me han hecho explotar la cabeza."
    kat "Ya está. Ya puedo decir alguna palabra diferente de 'alucinante'."
    mc "Bueno, si te han hecho explotar la cabeza, es normal que tu cerebro no funcione."
    mc "*Risa* O que funcione peor de lo habitual."
    call BlinkXS4("c31s001_380") from _call_BlinkXS4_1387
    kat "*Risa* ¡Eres un capullo! Pero no te mataré hoy."
    mc "*Risa* ¿Hoy? Gracias, supongo."
    kat "*Risa* ¡Tengo demasiada hambre después de esto como para matar a nadie! Ya sabes... después tendría que limpiar la sangre..."
    mc "Pues creo que tenemos un par de gofres fríos esperándonos."
    call BlinkXS4("c31s001_385") from _call_BlinkXS4_1388
    kat "No creo que pueda llegar al sofá. Mis piernas parecen gelatina ahora mismo."
    mc "No te preocupes. Ya traigo los gofres a la cama."
    mc "Si yo he podido comerte a ti, tú puedes comerte un gofre."
    scene c31s001_390a with fade
    call BlinkXS4("c31s001_390") from _call_BlinkXS4_1389
    kat "No pienso dejar que caiga ninguna miga de gofre en la cama, no te preocupes."
    kat "Seguramente me pasaría toda la noche moviéndome si hubiera alguna miga."
    mc "¿Quiere decir eso que te vas a quedar a dormir?"
    scene c31s001_395a with hpunch
    call BlinkXS4("c31s001_395") from _call_BlinkXS4_1390
    kat "¡Oops! Solo si quieres... He dado por hecho que..."
    mc "Claro que quiero, [kat]. Es nuestra noche de bodas."
    mc "Pero me sorprende que seas tan princesa durmiendo. Lo digo por lo de las migas."
    call BlinkXS4("c31s001_400") from _call_BlinkXS4_1391
    kat "*Risa* Lo de ser una princesa se lo dejo a [lis]. Yo podría dormir encima de una plantación de guisantes."
    kat "En mi caso, es por practicidad. Comía galletas a escondidas en la cama y mi madre me echaba la bronca si descubría migas."
    kat "Empecé a detectar cada pequeña miga que hubiera en la cama. Seguía comiendo galletas, pero mi madre no lo podía descubrir."
    mc "Me parece una buena explicación, aunque ahora no tienes que esconderte para comer."
    call BlinkXS4("c31s001_405") from _call_BlinkXS4_1392
    kat "Lo sé. Sé que mi madre lo hacía por mi bien. Siempre he estado gorda."
    mc "Siempre ha habido más [kat] de la que disfrutar."
    kat "A lo que voy es que ahora ya no como por comer... a menos que esté nerviosa."
    call BlinkXS4("c31s001_410") from _call_BlinkXS4_1393
    if kat._var("slim"):
        kat "Y casi ni eso desde que me pusisteis a dieta."
        mc "*Risa* Nadie te puso a dieta. Decidiste hacerlo tú."
    else:
        kat "Por suerte no me convencisteis para que me pusiera a dieta."
    mc "Comer un gofre a estas horas no se puede considerar estar a dieta."
    scene c31s001_415An with dissolve
    kat "¡Oops! ¡Lo siento! Te aseguro que no lo he hecho a propósito."
    mc "No te preocupes. Voy a limpiarme. Empieza a comer antes de que los gofres se enfríen más todavía."
    call BlinkXS4("c31s001_420") from _call_BlinkXS4_1394
    kat "Si quieres... puedo ocuparme de limpiarte yo..."
    kat "No me gustaría desperdiciar ese delicioso chocolate... Ni lo que hay debajo."
    if persistent.walkthrough:
        $ wt1 = _("Juegos con comida habilitados con [kat].")
        $ wt2 = _("Juegos con comida deshabilitados con [kat].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Con el hambre que hay en el mundo..." (wt=wt1):
            $ kat._var("foodplay", True)
            mc "A mí tampoco me gustaría que lo desperdiciaras."
            mc "Pero no hace falta que escondas el bote de chocolate. No creo que me vayas a manchar más."
            kat "No me tientes..."
            call c31s001_foodplay1 from _call_c31s001_foodplay1
        "No te preocupes..." (wt=wt2):
            $ kat._var("foodplay", False)
            mc "Voy a limpiarme y te dejo que acabes de repasar 'el plato'."
            call c31s001_noFoodplay from _call_c31s001_noFoodplay
    "Su boca, húmeda y caliente, apenas llega a abarcar el grosor de Mjolnir."
    "Al menos no has notado ningún diente durante el proceso."
    show c31s001_930v
    hide c31s001_965v
    "[kat] empieza a hacer unos movimientos sorprendentemente complejos para ser su primera vez."
    kat "*Slurp inquisitivo*"
    mc "Lo estás haciendo genial, cielo."
    "No mientes. Aunque visualmente has tenido la sensación de que un par de veces sus dientes iban a rozar tu glande, no lo han hecho en ningún momento."
    "Te preguntas si es normal que pienses que está monísima cuando tiene sus mejillas hinchadas mientras se dedica a darte placer."
    scene c31s001_935pv with dissolve
    show c31s001_935v
    hide c31s001_930v
    "Te da la impresión de que mueve la cadera buscando frotar su coño contra la polla que tiene en la boca. Parece que antes le ha gustado."
    "Lástima que tu campo visual no te permita comprobarlo. Deberías cubrir toda la habitación de espejos."
    kat "*Gemido* *Slurp* *Gemido*"
    "Puedes notar cómo [kat] se va excitando con cada lametón, con cada vez que tu glande toca la entrada de su garganta sin provocarle arcadas."
    "No sabes cuánto aguantarás o si la chica te llevará al orgasmo antes de decidir que quiere cambiar de posición."
    scene c31s001_925pv with dissolve
    show c31s001_925v
    hide c31s001_935v
    "Pero vas a disfrutar de cada segundo que dure esto. De eso no hay duda."
    kat "*Jadeo* *Slurp excitado* *Jadeo*"
    "Sus jadeos y gemidos, al inicio y al final de cada uno de los movimientos de su cabeza, provocan unas increíbles vibraciones en tu glande."
    kat "*Gemido* *Slurp cachondo* *Gemido*"
    "Si no fuera porque tiene las dos manos ocupadas estás seguro de que ella se estaría masturbando en este momento."
    "Sus gemidos cada vez suenan más excitados, incluso con la boca llena de tu polla."
    call BlinkXS4("c31s001_455") from _call_BlinkXS4_1395 #partir de 450
    kat "*Gemido* No puedo más. *Jadeo* Te necesito dentro de mí. *Gemido*"
    mc "*Risa* Creo que he creado un monstruo."
    call BlinkXS4("c31s001_460") from _call_BlinkXS4_1396
    kat "*Risa* Sí, el monstruo comedor de galletas y de gofres se ha convertido también en el monstruo adicto a las pollas."
    scene c31s001_460d with dissolve
    kat "*Smooch* Un monstruo adicto a esta polla en concreto."
    mc "Espero que nunca necesites probar ninguna otra. Ya tengo suficiente NTR en mi vida."
    scene c31s001_465a with fade
    pause (1.5)
    scene c31s001_465b with vpunch
    "Tu esposa se empala en Mjolnir sin mediar palabra. Ya no hay dudas ni miedo."
    kat "*GEMIDO*"
    call BlinkXS4("c31s001_470") from _call_BlinkXS4_1397 #Partir de 980
    kat "*Gemido* No te preocupes. *Jadeo* No va a haber otra polla en mi vida. *Gemido* Y ahora, empieza a follarte a tu mujer. *Jadeo*"
    mc "*Risa* No llevamos ni 24 horas casados y ya me estás dando órdenes."
    scene c31s001_975pv with dissolve
    show c31s001_975v
    hide c31s001_925v
    "Son órdenes que no tienes ningún problema en cumplir. Estabas deseando tomar un papel más activo en la noche de bodas."
    kat "*Jadeo* ¡Me encanta! *Gemido* ¡Esto es tremendo! *Jadeo*"
    "Tus caderas actúan por voluntad propia. Mjolnir empieza a sentirse muy a gusto en el coño de [kat]."
    kat "*Gemido* ¡Sigue así! *Jadeo* ¡Estás tocando puntos que no sabía ni que tenía! *Gemido*"
    "Acabas de empezar, con lo que vas a continuar así. Más aún teniendo en cuenta que tu esposa lo está disfrutando."
    scene c31s001_980pv with dissolve
    show c31s001_980v
    hide c31s001_975v
    "Y tú tienes las mejores vistas posibles en el proceso."
    "Difícilmente podrías imaginar que la noche podría ir así cuando empezó."
    kat "*Jadeo* ¡Sí, semental! *Gemido* ¡Continúa follándome! *Jadeo*"
    "Cuando creías que ibas a encontrar una mujer tímida, has descubierto una mujer desinhibida que sabe lo que quiere y no teme pedirlo."
    kat "*GEMIDO* ¡ESTOY A PUNTO! *JADEO* ¡OTRA VEZ! *GEMIDO*"
    "Y que, además, es muy rápida a la hora de llegar al orgasmo."
    call OrgasmXS4("c31s001_475") from _call_OrgasmXS4_53
    kat "*JADEO* ¡SÍ! *GEMIDO*"
    "Ya no le queda aliento para seguir hablando y corriéndose al mismo tiempo."
    "La noche está siendo muy intensa para ella."
    scene c31s001_985pv with dissolve
    show c31s001_985v
    hide c31s001_980v
    "Más por inercia que por voluntad, ella sigue botando sobre tu polla, con movimientos cada vez menos coordinados."
    "Tu orgasmo se acerca impulsado por las contracciones que su coño produce en tu astil, aunque aún te queda para llegar."
    kat "*GEMIDO*"
    "La preciosa mujer, cada vez más cansada, sigue siendo recorrida por oleadas de orgasmos que no le permiten mantener una conversación."
    "Siempre has preferido eso a los gemidos exagerados que, a veces, parecen fingidos y sacados de una peli porno."
    call BlinkXS4("c31s001_480") from _call_BlinkXS4_1398
    "De pronto, [kat] para todos sus movimientos."
    kat "*Jadeo* Lo siento. *Jadeo* No puedo más. *Jadeo* No me quedan fuerzas. *Jadeo*"
    mc "¿Quieres que cambiemos de posición?"
    kat "*Jadeo* Sí, por favor. *Jadeo*"
    mc "Túmbate."
    scene c31s001_485a with fade
    scene c31s001_485An
    "Ella se tumba donde le has indicado y la penetras rápidamente."
    kat "*GEMIDO*"
    "Tu instinto animal está tomando el control y no quiere retrasar más el orgasmo que estabas cerca de alcanzar."
    scene c31s001_995pv with dissolve
    show c31s001_995v
    hide c31s001_985v
    "Con el enorme e increíble culo de [kat] entre tú y su coño, apenas llegas a penetrarla tan solo con la punta de la polla."
    "Los movimientos son más lentos que en la posición anterior para evitar que tu glande se salga del todo en una de las embestidas."
    kat "*JADEO* ¡Eso se siente diferente! *GEMIDO* ¡Me encanta! *JADEO*"
    "Justo cuando estás a punto de perder el control es cuando más control necesitas."
    "Por otra parte, concentrar todas las sensaciones en la parte superior de tu polla las hace más intensas."
    scene c31s001_895pv with dissolve
    show c31s001_895v
    hide c31s001_995v
    kat "*GEMIDO* ¡Me gusta mucho así...! *JADEO* Es más íntimo... *GEMIDO*"
    "Más íntimo, pero menos profundo. El resultado sigue siendo el mismo para ella. Sus orgasmos siguen llegando."
    "Su cabeza, moviéndose ya sin apenas fuerzas al ritmo de tus embestidas, te recuerda por un momento a uno de esos odiosos perros de salpicadero."
    "La diferencia en este caso es que nunca te cansarás de ver la cabeza de [kat] rebotando durante sus larguísimos clímax."
    kat "*JADEO* Estás durando más que antes... *GEMIDO* No quiero que esto acabe... *JADEO*"
    scene c31s001_990pv with dissolve
    show c31s001_990v
    hide c31s001_895v
    "Cada vez te queda menos para acabar. La sensación de bombear con tu glande en su húmedo coño te está llevando irremisiblemente al orgasmo."
    "Sus dedos presionando sus labios al unísono no hacen más que incrementar tu placer."
    kat "*GEMIDO* ¡ME HE CASADO CON UN SEMENTAL! *JADEO*"
    "Estás a punto de volver a llenarla, con lo que el nombre suena adecuado."
    "Tu orgasmo empieza a subir por tus pantorrillas mientras tus caderas siguen con su rítmico movimiento."
    scene c31s001_890pv with dissolve
    show c31s001_890v
    hide c31s001_990v
    "Con cada vez menos combustible en el depósito, sabes que el final se acerca."
    mc "Estoy a punto de correrme, [kat]. ¿Dónde quieres que me corra?"
    "Su coño se cierra con fuerza sobre tu glande, coincidiendo un nuevo orgasmo con la expectación que crean tus palabras."
    kat "*JADEO* ¡DONDE QUIERAS! *GEMIDO*"
    "Después de haber experimentado la experiencia completa, tal como la ha llamado ella, ya le da lo mismo dónde acabes."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[kat] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro. Ir a por el bebé." (wt=wt2) if not kat._var("pregnant"):
            $ kat._var("pregnant", True)
            $ kat._var("undiscoveredPregnancy", True)
            play sound ("music/OldMusicBox5.ogg")
            call c31s001_inside from _call_c31s001_inside
            $ inside = True
        "Correrte dentro." (wt = wt1):
            call c31s001_inside from _call_c31s001_inside_1
            $ inside = True
        "Correrte en su estómago." (wt=wt1):
            call c31s001_outside from _call_c31s001_outside
            $ inside = False
    "Una gran forma de acabar una noche de bodas increíble."
    kat "*GEMIDO* ¡ESTÁ SÚPER CALIENTE! *JADEO*"
    "Tras tanto rato reteniendo el orgasmo, la temperatura de tu semen es lo que menos te importa."
    scene c31s001_500a with fade
    call BlinkXS4("c31s001_500") from _call_BlinkXS4_1399
    stop music fadeout (1.5)
    "Cuando vuestras respiraciones se normalizan al cabo de un minuto..."
    play music ("music/i-feel-alive.ogg")
    kat "Ha sido... alucinante..."
    mc "*Risa* Creo que tenemos que ampliar tu vocabulario post-orgásmico."
    call BlinkXS4("c31s001_505") from _call_BlinkXS4_1400
    kat "*Risa* Me compraré un diccionario para la próxima vez, a ver si mi marido deja de quejarse."
    mc "No me quejo. Sólo me río de ti."
    call BlinkXS4("c31s001_510") from _call_BlinkXS4_1401
    kat "No dejes de hacerlo nunca."
    mc "No pienso hacerlo."
    call BlinkXS4("c31s001_515") from _call_BlinkXS4_1402
    if inside:
        kat "Mi marido me ha llenado tanto que está empezando a salirse de mi coño."
    else:
        kat "Mi marido ha pintado un cuadro abstracto en mi barriga. Y 'la pintura' está empezando a correrse."
    kat "¿Tienes algo con lo que me pueda limpiar? No me apetece salir desnuda al descansillo."
    mc "¿Temes encontrarte con alguien?"
    call BlinkXS4("c31s001_520") from _call_BlinkXS4_1403
    kat "*Risa* Dudo que alguien suba a esta planta esta noche."
    kat "Si alguien había olvidado que yo iba a pasar la noche aquí, creo que mis gritos se lo han recordado."
    mc "Tienes pañuelos en ese cajón."
    kat "No te levantes."
    scene c31s001_525a with fade
    call BlinkXS4("c31s001_525") from _call_BlinkXS4_1404
    kat "Mmmm..."
    mc "¿Qué estás pensando, cielo? Me siento observado como se debe sentir una pizza cuando Tía [bet] está mirando."
    kat "No te equivocas demasiado."
    scene c31s001_525d with dissolve
    "Sin decir una palabra, se mete tu polla en la boca, limpiando los restos de tu corrida mezclados con sus fluidos."
    kat "*Slurp*"
    "En tu sensible estado post-orgásmico, cada lengüetazo manda relámpagos de placer que recorren todo tu cuerpo iniciándose en la punta de tu polla."
    call BlinkXS4("c31s001_530") from _call_BlinkXS4_1405
    kat "Tenía que probarlo..."
    mc "¿Y?"
    call BlinkXS4("c31s001_535") from _call_BlinkXS4_1406
    kat "Está mezclado con mi sabor. El tuyo es más salado. El mío más amargo."
    kat "Creo que tendré que probar cuál es tu sabor sin mezclarlo con el mío algún día. Pero no va a ser hoy. No tengo fuerzas."
    mc "No hay prisa. Habrá muchas más noches como esta."
    call BlinkXS4("c31s001_540") from _call_BlinkXS4_1407
    kat "¿Te puedo coger prestado un albornoz o una bata?"
    mc "¿Vas a ducharte ahora?"
    call BlinkXS4("c31s001_545") from _call_BlinkXS4_1408
    kat "*Risa* ¿No me has escuchado antes? No quiero ir desnuda por el descansillo."
    kat "Y tengo la intención de besar a mi marido antes de dormir. Con lo que necesito enjuagarme."
    kat "No creo que quieras probar el sabor de tu semen en mis labios."
    if persistent.walkthrough:
        $ wt1 = _("Beso blanco habilitado con [kat].")
        $ wt2 = _("Beso blanco deshabilitado con [kat].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "No me importa, siempre y cuando sea en tus labios." (wt = wt1):
            $ kat._var("cumswap", True)
        "Hay un albornoz en el armario." (wt=wt2):
            $ kat._var("cumswap", False)
            scene c31s001_545d with fade
            kat "No hace falta que te levantes. Vuelvo en un minuto o dos."
            scene c31s001_545e with dissolve
            "Las ventajas de tener un lavabo al lado del gimnasio son increíbles a veces."
            "Dudas que [kat] tuviera fuerzas para bajar una planta y volverla a subir."
            "Te imaginas teniendo que ir a buscarla y subiéndola en brazos por la escalera."
            scene c31s001_550a with fade
            call BlinkXS4("c31s001_550") from _call_BlinkXS4_1409
            "[kat] vuelve mucho más rápido de lo que pensabas, sacándote de tus ensoñaciones."
            kat "Creo que es el momento de ese beso."
            mc "Sólo si te quitas el albornoz. Esta cama es territorio sin ropa."
            scene c31s001_555a with fade
            call BlinkXS4("c31s001_555") from _call_BlinkXS4_1410
            "Tras devolver el albornoz al armario..."
            kat "¿Mejor así? ¿Tengo permiso para volver a la cama?"
            mc "Mucho mejor. Y permiso concedido."
    scene c31s001_555d with dissolve
    "Tu esposa se lanza a besar tus labios con fiereza a la vez que ternura. Ha sido una noche muy especial para ambos."
    if kat._var("cumswap"):
        "Puedes reconocer su sabor y, por eliminación, el tuyo en su boca. La combinación no es desagradable."
    else:
        "Su boca sabe a colutorio, con un ligero sabor a hierbabuena."
    call BlinkXS4("c31s001_560") from _call_BlinkXS4_1411
    kat "Creo que deberíamos dormir. Se está haciendo tarde y mañana tengo clase."
    mc "¿No va a haber tercer asalto?"
    call BlinkXS4("c31s001_565") from _call_BlinkXS4_1412
    kat "*Risa* ¿Tercer asalto? Si me acercas la polla, mi coño se va a cerrar como un mejillón enfadado."
    kat "Todo lo contrario que mis piernas, que no se van a poder cerrar en días."
    mc "*Risa* ¿Los mejillones se enfadan?"
    call BlinkXS4("c31s001_570a") from _call_BlinkXS4_1413
    kat "Es una broma de cuando hice el primer curso de la carrera. No la entenderías."
    mc "Prueba a explicármela."
    call BlinkXS4("c31s001_570b") from _call_BlinkXS4_1414
    kat "Quizás otro día. Sigo pensando que deberíamos dormir."
    mc "Me parece bien. No quiero que pidas el divorcio por agotamiento."
    mc "Sólo quiero hacerte una pregunta antes de dormir."
    call BlinkXS4("c31s001_575") from _call_BlinkXS4_1415
    kat "Si no tiene que ver con mejillones enfadados..."
    mc "Nada que ver. ¿La noche ha sido como pensabas que sería?"
    call BlinkXS4("c31s001_580") from _call_BlinkXS4_1416
    kat "No. Pensaba que sería... diferente. Esperaba que fuera como ha sido, sin posturas concretas, pero no me atrevía a pensar que fuera tan buena."
    mc "Entonces supongo que no te arrepientes de haberte casado conmigo."
    call BlinkXS4("c31s001_585") from _call_BlinkXS4_1417
    kat "No me arrepiento. Me arrepiento de no haber tenido el valor de intentar empezar algo antes, pero no de haberme casado contigo."
    kat "Sé que ha parecido muy forzado y muy acelerado. Aparte de un par de besos..."
    mc "Aparte de un par de docenas de besos..."
    call BlinkXS4("c31s001_590") from _call_BlinkXS4_1418
    kat "Bueno, sí, eso... Aparte de esos besos, no hemos tenido tiempo de hacer cosas de pareja."
    kat "Me hubiera gustado hacer más cosas contigo. Y no me refiero al sexo. O no me refiero ÚNICAMENTE al sexo."
    mc "Bueno, habrá tiempo para eso cuando vuelva de Aruba. Tenemos una vida para hacer cosas juntos."
    scene c31s001_590d with hpunch
    kat "¡Joder!"
    mc "¿Qué pasa?"
    call BlinkXS4("c31s001_595") from _call_BlinkXS4_1419
    kat "Te has corrido dentro de mí..."
    if inside:
        kat "Dos veces..."
    mc "Tú me lo has pedido..."
    kat "¿Y si me quedo embarazada?"
    mc "Pues tendremos que buscar un nombre o buscar una solución."
    call BlinkXS4("c31s001_600") from _call_BlinkXS4_1420
    kat "¿Así de fácil es para ti?"
    mc "Es como se ha hecho siempre, ¿no?"
    mc "Quiero pasar el resto de mi vida contigo. Nos acabamos de casar. Si tiene que venir un bebé, que venga. Buscaremos un nombre."
    mc "Si no quieres que venga, buscaremos una solución."
    call BlinkXS4("c31s001_605") from _call_BlinkXS4_1421
    kat "De alguna forma retorcida, tienes razón. Solo hay dos opciones. Y la 'solución' no voy a usarla si pasa. Bueno... si tú..."
    mc "Me parece bien."
    call BlinkXS4("c31s001_610") from _call_BlinkXS4_1422 #riéndose
    kat "*Risa* ¿Sabes lo que más me jode?"
    if kat._var("slim"):
        kat "Después de estar haciendo dieta todo este tiempo, no voy a estar delgada."
        kat "Es posible que me hayas convertido en una gorda para los próximos nueve meses. Y el peso que pierda lo gane con el bebé."
    else:
        kat "Voy a estar más gorda aún. Al menos durante nueve meses."
    mc "Eso solo significa que habrá más [kat] para que yo pueda disfrutarla."
    mc "*Risa* Además, solo son nueve meses. Y durante el embarazo te tienes que cuidar y puedes tener antojos de croissants... o de gofres."
    mc "Eso si hay embarazo, claro."
    scene c31s001_610d with dissolve
    "A tu esposa, embarazada o no, parece que le gusta la respuesta."
    "Se lanza a tus labios con ternura y pasión."
    "Desafortunadamente, también sin fuerzas."
    scene c31s001_610e with dissolve
    "Los gofres yacen olvidados en su plato mientras os besáis durante un largo rato."
    "El único gofre que te importa está tatuado en la espalda de la mujer que te está besando."
    "Es un beso que sabe a noche de bodas, pero también a despedida. En menos de 48 horas vuelas hacia Aruba."
    if kat._var("cumswap"):
        "El sabor de tu semen prácticamente ha desaparecido de sus labios."
    scene c31s001_610f with dissolve
    "Tras el largo beso, apagáis la luz y os preparáis para pasar vuestra primera noche juntos."
    "La primera de muchas."
    mc "Buenas noches, cielo."
    stop music fadeout (1.5)
    "La única contestación que recibes es una respiración pesada y tranquila."
    return
label c31s001_foodplay1:
    scene c31s001_425a with fade
    call BlinkXS4("c31s001_425") from _call_BlinkXS4_1423
    stop music fadeout (1.5)
    "[kat] se arrodilla entre tus piernas tras quitar los gofres de la cama y te mira de forma pícara."
    play music ("music/KindofGirl.ogg")
    kat "Creo que nunca he tenido tantas ganas de comer chocolate."
    scene c31s001_430a with dissolve
    "Con un decidido lametón, empieza a devorar el chocolate que recubre tu polla."
    kat "*Slurp* La combinación de sabores es rara, pero agradable."
    mc "*Risa* ¿Vas a hacer una crítica gastronómica?"
    scene c31s001_430b with dissolve
    kat "*Slurp* Puedo notar tres sabores... El mío, el del chocolate, y supongo que el otro es el tuyo. Es el sabor más salado."
    mc "Teniendo en cuenta dónde estaba el 'plato' hace un rato y para que lo has usado, tiene lógica."
    scene c31s001_430c with dissolve
    kat "*Slurp* Ya está casi limpio. Es una lástima que esto tenga que acabar ahora que ha vuelto a crecer."
    mc "¿Quién ha dicho que tenga que acabar?"
    scene c31s001_430d with dissolve
    "Miras el bote de nata mientras una idea se forma en tu cabeza y te imaginas a [kat] recubierta de la deliciosa sustancia blanca."
    scene c31s001_930pv with hpunch
    "Antes de que puedas proponerlo, la punta de tu polla desaparece en la boca de [kat]. Crees que acabará con otro tipo de sustancia blanca."
    "Mientras mirabas el bote de nata, ha desaparecido hasta la última gota de chocolate."
    return
label c31s001_noFoodplay:
    call BlinkXS4("c31s001_435") from _call_BlinkXS4_1424
    kat "Límpiate mientras recojo los platos."
    mc "¿No decías que tenías hambre? No has tocado el gofre aún."
    call BlinkXS4("c31s001_440") from _call_BlinkXS4_1425
    kat "Como has dicho tú antes, de lo que más hambre tengo es de ti. Solo de pensar en comerme el chocolate me he empezado a poner cachonda."
    kat "Y como he dicho yo antes, aún tengo que devolverte el favor."
    call BlinkXS4("c31s001_445") from _call_BlinkXS4_1426
    kat "¡Y no protestes!"
    mc "*Risa* A sus órdenes, mi comandante."
    mc "Pero no hace falta que escondas el bote de chocolate. No creo que me vayas a manchar más."
    scene c31s001_450a with fade
    call BlinkXS4("c31s001_450") from _call_BlinkXS4_1427
    stop music fadeout (1.5)
    "Tras limpiarte, te sientas en la cama y [kat] se arrodilla entre tus piernas. Ha vuelto a hacer desaparecer los gofres."
    play music ("music/KindofGirl.ogg")
    kat "Dime si hago algo mal. Es la primera vez que hago esto."
    mc "Si lo haces tan bien como lo has hecho antes, no voy a tener que darte instrucciones."
    scene c31s001_930pv with hpunch
    "Aunque quisieras dárselas, no hubieras tenido tiempo. la punta de tu polla desaparece en la boca de [kat]."
    return
label c31s001_inside:
    call OrgasmXS4("c31s001_490") from _call_OrgasmXS4_54
    mc "¡Mpfft!"
    "Una vez más explotas dentro de tu esposa, volviéndola a llenar hasta que tu semen empieza a bajar por tu astil."
    return
label c31s001_outside:
    call OrgasmXS4("c31s001_495") from _call_OrgasmXS4_55
    mc "¡Mpfft!"
    "Esta vez explotas sobre su estómago, pintando una obra de arte sobre un lienzo que es una obra de arte por sí mismo."
    return
label c31s002_morning:
    scene black with dissolve
    play music ("music/From-Above.ogg")
    centered "{size=+20}{b}DÍA 37 – MIÉRCOLES{/b}{/size}"
    scene c31s002_005a with fade
    if kat._var("route"):
        "Cuando te despiertas, [kat] ya se ha ido a clase. O eso supones."
        "Después de lo de anoche, creías que despertarías con [kat] a tu lado, mirándote."
    else:
        "Te despiertas relativamente temprano. Aunque seguramente algunas de las chicas ya estarán en clase."
    "Decides bajar a desayunar antes de que se haga demasiado tarde."
    return
label c31s002_lisFork:
    if _in_replay:
        call mrS3_kat_route from _call_mrS3_kat_route_8
        call mrS3_ama_route from _call_mrS3_ama_route_18
        call mrS3_rels from _call_mrS3_rels_41
        call mrS3_lis_pregnant from _call_mrS3_lis_pregnant_2
        call c31s002_morning from _call_c31s002_morning_1
    scene c31s002_005b with fade
    $renpy.sound.play("music/woodclick.ogg", loop=True)
    scene c31s002_005An with dissolve
    "Al entrar en la cocina..."
    mc "¿Qué estás haciendo, [lis]?"
    call BlinkXS4("c31s002_010") from _call_BlinkXS4_1428
    stop sound
    lis "¡Oh! ¡Buenos días, cielo! Estaba comprobando si podía... Bueno, ya ves lo que estaba haciendo..."
    mc "¿Estabas aburrida? ¿Eso no se hace normalmente con un cuchillo?"
    call BlinkXS4("c31s002_015") from _call_BlinkXS4_1429
    lis "*Risa* Recuerda que me casé contigo. No soy idiota."
    call BlinkXS4("c31s002_020") from _call_BlinkXS4_1430
    lis "Si lo hiciera con un cuchillo me podría hacer... daño."
    mc "¿Pasa algo, [lis]?"
    call BlinkXS4("c31s002_025") from _call_BlinkXS4_1431
    lis "Que mi marido es un idiota y aún no me ha besado."
    mc "*Guiño* Mi mujer es una vaga y aún ha dado la vuelta al mostrador."
    scene c31s002_025d with fade
    "Tu mujer deja el tenedor encima de la tabla de cortar y, tras rodear el mostrador, se lanza a tus brazos pidiendo su beso de buenos días."
    "Sienta bien pensar en ella como tu esposa."
    call BlinkXS4("c31s002_030") from _call_BlinkXS4_1432
    mc "Buenos días, mi amor."
    lis "Buenos días, cielo."
    mc "¿A qué venía lo del tenedor?"
    call BlinkXS4("c31s002_035") from _call_BlinkXS4_1433
    lis "[eva] y [ama] me dijeron una cosa hace unos días y estaba comprobando algo."
    mc "No seas tan misteriosa. ¿Qué te dijeron y qué estabas comprobando?"
    call BlinkXS4("c31s002_040") from _call_BlinkXS4_1434
    lis "Creen que es posible que mi mente no funcione bien y que no pueda sentir dolor."
    mc "No puede ser. En Los Angeles te dolían los pies..."
    scene c31s002_045a with fade
    call BlinkXS4("c31s002_045") from _call_BlinkXS4_1435
    "Después de explicarte la teoría de [ama] y [eva]..."
    lis "Pero no tengo forma de comprobarlo. Si me pincho con el tenedor, noto la presión y me... duele."
    lis "Como sé que tiene que doler, ya no sé si me duele de verdad o es mi cerebro que me está engañando."
    lis "Por eso estaba probando lo del tenedor. Si me pincho sin darme cuenta, sabré si me duele de verdad."
    mc "No creo que funcione así. Notarías la presión igualmente."
    mc "¿Por qué no vas al médico? No sé si eso es algo que se pueda detectar con... no sé... ¿un análisis de sangre?"
    call BlinkXS4("c31s002_050") from _call_BlinkXS4_1436
    lis "Ya he hablado con [sam.nick] y con Tía [bet]."
    lis "Dicen que es muy raro que, si tengo esa condición, nadie lo haya descubierto antes."
    lis "Ni mis niñeras, ni mis padres... ni yo."
    mc "Sí, sería raro que no te dieras cuenta al... no sé... rasparte las rodillas al subir a un árbol, o quemarte mientras cocinas..."
    call BlinkXS4("c31s002_055") from _call_BlinkXS4_1437
    lis "*Risa* ¿Con quién crees que te has casado? No he subido a un árbol en mi vida, y lo de cocinar..."
    lis "Cuando me fui a Phoenix, mis amigas me regalaron un libro."
    mc "¿Un libro de cocina?"
    call BlinkXS4("c31s002_060") from _call_BlinkXS4_1438
    lis "Más o menos. 'El microondas: Ese gran desconocido que puede salvarte la vida'."
    mc "*Risa* Jamaal me regaló '¿Cómo tener tu cuarto como un cerdo (Manual del perfecto estudiante)?'"
    mc "Creo que tenemos que cambiar de amigos."
    call BlinkXS4("c31s002_065") from _call_BlinkXS4_1439
    lis "Bueno, aquel libro me fue muy bien... En casa siempre había alguien a quien pedirle que cocinara algo."
    lis "No es que no hubiera usado nunca el microondas... Si me quería calentar un vaso de leche sabía hacerlo..."
    mc "No creo que te den una estrella Michelon por calentarte un vaso de leche."
    mc "Pero volviendo al tema importante... Aparte de hablar con [sam.nick] y con Tía [bet]..."
    call BlinkXS4("c31s002_070") from _call_BlinkXS4_1440
    lis "[sam.nick] me ha programado una cita en el hospital la semana que viene."
    lis "Pero para poder estar seguros me tendrán que hacer un estudio genético. Y odio las agujas."
    mc "*Risa contenida*"
    call BlinkXS4("c31s002_075") from _call_BlinkXS4_1441
    lis "¿Qué es tan gracioso?"
    mc "No, nada..."
    call BlinkXS4("c31s002_080") from _call_BlinkXS4_1442 #enfadada
    lis "¿QUÉ. ES. TAN. GRACIOSO?"
    mc "No es nada. Una tontería que se me ha pasado por la cabeza. Pero no es el momento de hablar de ello."
    lis "Si no me lo explicas ahora, posiblemente no haya otro momento. [eva] me enseñó a disparar..."
    mc "Vale, vale... Cuando has dicho que odias las agujas... He pensado que, quizás, si al final no sientes dolor, dejarás de odiarlas..."
    mc "Me ha parecido más gracioso cuando lo he pensado que ahora que lo digo en voz alta..."
    call BlinkXS4("c31s002_085") from _call_BlinkXS4_1443
    lis "*Risa* ¡Eres un idiota! ¡Las tonterías que se te ocurren cuando estoy hablando de algo serio!"
    mc "Por eso decía que no era el momento de hablar de ello..."
    scene c31s002_025e with dissolve
    "Por alguna razón que no comprendes, te has ganado un beso."
    "Prefieres no preguntar qué has hecho para ganártelo."
    call BlinkXS4("c31s002_090") from _call_BlinkXS4_1444
    lis "Gracias por estar siempre cuando necesito que alguien haga el tonto a mi alrededor."
    lis "Me estaba comiendo la cabeza innecesariamente con todo esto, cuando a lo mejor no me pasa nada."
    mc "Bueno, hacer el tonto se me da bien. Y actuar inteligentemente también. Me casé contigo, ¿no?"
    scene c31s002_090d with dissolve
    "[lis] se gira sin mediar palabra y se dirige hacia la tabla de cortar y el tenedor."
    mc "¿He dicho algo malo?"
    scene c31s002_095a with fade
    call BlinkXS4("c31s002_095") from _call_BlinkXS4_1445
    "La chica no dice nada hasta que no ha terminado de meter todo en el lavavajillas. Como si estuviera midiendo sus próximas palabras."
    lis "Me has recordado que no tuvimos noche de bodas. Podemos tener un post-desayuno de bodas."
    "Comprendes por qué ha sopesado sus palabras antes de decirlas."
    "No debe ser fácil para una chica que ha perdido la virginidad hace menos de una semana decir '¿follamos?' sin sentirse un poco frívola."
    mc "Pre-desayuno, en mi caso. Pero me parece una idea estupenda."
    call BlinkXS4("c31s002_100a") from _call_BlinkXS4_1446
    lis "Pues tendré que ser tu desayuno... Antes de que tenga que irme a la universidad."
    if mc._var("relationships")>1:
        if mc._var("relationships")==2 and ama._var("route"):
            pass
        if mc._var("relationships")==2 and kat._var("route"):
            pass
        if mc._var("relationships")==3 and kat._var("route") and ama._var("route"):
            pass
        else:
            lis "Y antes de que a alguien más se le ocurra la misma idea."
    mc "Creo que va a ser el mejor desayuno de la historia."
    scene c31s002_100b with fade
    scene c31s002_100An with dissolve
    "Al llegar a su habitación, tenéis una tórrida sesión de sexo."
    if persistent.pregnancy and not lis._var("pregnant"):
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[lis] embarazada.")
        menu:
            "Es la última oportunidad de dejar embarazada a [lis] antes del viaje a Aruba."
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ lis._var("pregnant", True)
                $ lis._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    "Es más corta de lo que ninguno de los dos querríais, pero las clases de [lis] no van a esperar."
    scene black with dissolve
    stop music fadeout (1.5)
    "Cuando La Princesa se va a la universidad, por fin puedes ir a desayunar algo. Las fuerzas empiezan a flaquear."
    return
label c31s002_noLis:
    scene c31s002_105_lis5
    "[lis] pasa por tu habitación poco después de que desayunes."
    "No habláis de nada en concreto, pero sabes que quería pasar un rato a solas contigo antes de irse a clase."
    "Antes de que te vayas a Aruba."
    stop music fadeout (1.5)
    "El día siguiente, el último que vas a estar en casa, va a ser complicado que paséis tiempo juntos, con lo que quiere adelantar la despedida."
    return
label c31s002_firstDayWedding:
    if _in_replay:
        call mrS3_sai_route from _call_mrS3_sai_route_24
        if sai._var("route"):
            call mrS3_sai_pregnant from _call_mrS3_sai_pregnant_4
            if sai._var("pregnant"):
                call mrS3_sai_undiscoveredPregnancy from _call_mrS3_sai_undiscoveredPregnancy
        call mrS3_sam_route from _call_mrS3_sam_route_25
        if sam._var("route"):
            call mrS3_sam_pregnant from _call_mrS3_sam_pregnant_4
            if sam._var("pregnant"):
                call mrS3_sam_undiscoveredPregnancy from _call_mrS3_sam_undiscoveredPregnancy
        call mrS3_sca_route from _call_mrS3_sca_route_30
        if sca._var("route"):
            call mrS3_sca_pregnant from _call_mrS3_sca_pregnant_5
            if sca._var("pregnant"):
                call mrS3_sca_undiscoveredPregnancy from _call_mrS3_sca_undiscoveredPregnancy
        call mrS3_eil_route from _call_mrS3_eil_route_28
        if eil._var("route"):
            call mrS3_eil_pregnant from _call_mrS3_eil_pregnant_6
            if eil._var("pregnant"):
                call mrS3_eil_undiscoveredPregnancy from _call_mrS3_eil_undiscoveredPregnancy
        call mrS3_eri_route from _call_mrS3_eri_route_36
        if eri._var("route"):
            call mrS3_eri_pregnant from _call_mrS3_eri_pregnant_5
            if eri._var("pregnant"):
                call mrS3_eri_undiscoveredPregnancy from _call_mrS3_eri_undiscoveredPregnancy
        call mrS3_eva_route from _call_mrS3_eva_route_21
        if eva._var("route"):
            call mrS3_eva_pregnant from _call_mrS3_eva_pregnant_2
        call mrS3_kim_route from _call_mrS3_kim_route_16
        if kim._var("route"):
            call mrS3_kim_pregnant from _call_mrS3_kim_pregnant_1
        call mrS3_meg_route from _call_mrS3_meg_route_11
        if meg._var("route"):
            call mrS3_meg_pregnant from _call_mrS3_meg_pregnant_3
            if meg._var("pregnant"):
                call mrS3_meg_undiscoveredPregnancy from _call_mrS3_meg_undiscoveredPregnancy
    if lis._var("route"):
        $ weds = 1
    else:
        $ weds = 0
    play music ("music/RhythmPlay.ogg")
    if sai._var("route"):
        $ prg = False
        scene c31s002_105_saiAn
        $ weds = weds + 1
        "[sai] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        if persistent.pregnancy and not sai._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[sai] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [sai] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ sai._var("pregnant", True)
                    $ sai._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[sai] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_sai4
        if sai._var("undiscoveredPregnancy") and not prg:
            $ sai._var("undiscoveredPregnancy", False)
            "[sai] te informa de que está embarazada antes de irse. Es una gran noticia que compartís con alegría."
            "No se lo va a decir a sus padres de momento. No quiere que pueda afectar a la llegada de [kal]."
    else:
        scene c31s002_105_sai5
        "[sai] se asoma por tu habitación para pasar un rato a solas contigo."
    "El momento, aunque breve, sirve como despedida de la hermosa mujer de ojos oscuros. No vais a tener mucho más tiempo a solas antes de que te vayas."
    if eri._var("route"):
        $ prg = False
        scene c31s002_105_eriAn
        $ weds = weds + 1
        if weds > 1:
            "La siguiente en aparecer es [eri], que también quiere un rato a solas contigo."
        else:
            "[eri] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        if persistent.pregnancy and not eri._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[eri] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [eri] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ eri._var("pregnant", True)
                    $ eri._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[eri] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_eri4
        if eri._var("undiscoveredPregnancy") and not prg:
            $ eri._var("undiscoveredPregnancy", False)
            "[eri] te informa de que está embarazada antes de irse. Si es niña se llamará Hope. No hacéis planes por si es niño."
    else:
        scene c31s002_105_eri5
        "[eri] pasa un rato contigo antes de irse a trabajar."
    "Cada momento con [eri] sabe siempre a poco. Esta vez, sabiendo que sirve como despedida, parece incluso más corto."
    if sca._var("route"):
        $ prg = False
        scene c31s002_105_scaAn
        $ weds = weds + 1
        if weds > 1:
            "Tras un pequeño descanso, [sca] aparece en tu habitación. También quiere su primera ración de sexo como mujer casada."
        else:
            "[eri] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        if persistent.pregnancy and not sca._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[sca] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [sca] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ sca._var("pregnant", True)
                    $ sca._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[sca] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_sca4
        if sca._var("undiscoveredPregnancy") and not prg:
            $ sca._var("undiscoveredPregnancy", False)
            "[sca] te informa de que está embarazada antes de irse. No habéis decidido ningún nombre todavía, pero hablaréis de ello en las próximas semanas."
            if persistent.family and mc._var("edmundsStory"):
                "En cuanto el embrión esté un poco desarrollado, quiere hacer pruebas genéticas para asegurarse de que no hay ningún problema."
        "Cuando [sca] abandona tu habitación, entiendes perfectamente el dicho de que lo bueno, si breve..."
    else:
        scene c31s002_105_sca5
        "[sca] también quiere pasar unos últimos momentos contigo antes de que llegue tu partida."
        if persistent.family and mc._var("edmundsStory"):
            "Haber descubierto que tiene un medio hermano y 'perderlo' durante varios meses le da un punto triste a la despedida."
        else:
            "La despedida tiene un punto triste. Hace poco más de un mes que has vuelto y te vuelves a ir, esta vez por varios meses."
    if eil._var("route"):
        $ prg = False
        scene c31s002_105_eilAn
        $ weds = weds + 1
        if weds > 1:
            "No pasa mucho tiempo antes de que [eil] llame a tu puerta y tengáis una tórrida sesión de sexo."
        else:
            "[eil] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        "La noche de bodas tan largamente planeada queda reducida a un encuentro breve y acrobático a media mañana."
        if persistent.pregnancy and not eil._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[eil] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [eil] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ eil._var("pregnant", True)
                    $ eil._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[eil] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_eil4
        if eil._var("undiscoveredPregnancy") and not prg:
            $ eil._var("undiscoveredPregnancy", False)
            "[eil] te informa de que está embarazada antes de irse. Os habéis pasado años intentando evitarlo, pero ahora es una alegría inmensa."
        "Otra vez te toca separarte de la preciosa animadora, como hace tres años. Esta vez sabes que será diferente y que la distancia no romperá vuestra relación."
    else:
        scene c31s002_105_eil5
        "Otra vez te toca separarte de la preciosa animadora, como hace tres años. Pero esta vez sabes que volverás, y que no hay una relación que se pueda romper por la distancia."
    if sam._var("route"):
        $ prg = False
        scene c31s002_105_samAn
        $ weds = weds + 1
        if weds > 1:
            "[sam] llama a tu puerta casi con timidez. Ella también quiere su noche de bodas, aunque sea mediodía."
        else:
            "[sam] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        "La sesión de sexo es tan excitante como breve."
        if persistent.pregnancy and not sam._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[sam] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [sam] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ sam._var("pregnant", True)
                    $ sam._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[sam] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_sam4
        if sam._var("undiscoveredPregnancy") and not prg:
            $ sam._var("undiscoveredPregnancy", False)
            "[sam] te informa de que está embarazada antes de irse."
            "La enfermera que lleva dentro empieza a preocuparse por lo que ella llama un embarazo geriátrico antes de que la acalles con un beso."
    else:
        scene c31s002_105_sam5
        "[sam] pasa a visitarte después de acabar su turno en el hospital. El rato que pasáis juntos sabe a despedida."
    "Se va a hacer duro estar separado de [sam] durante tantos meses. Esperas que pasen volando con lo ocupado que vas a estar."
    "Tan solo esperas que no se enfade demasiado cuando descubra lo que habéis planeado [nor] y tú para ayudarle con su deuda."
    if eva._var("route"):
        $ prg = False
        scene c31s002_105_evaAn
        $ weds = weds + 1
        if weds > 1:
            "Una preciosa mercenaria llama a tu puerta poco tiempo después."
        else:
            "[eva] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        "Si su primera vez fue salvaje, esta vez no lo es menos."
        if persistent.pregnancy and not eva._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[eva] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [eva] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ eva._var("pregnant", True)
                    $ eva._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[eva] te informará por videoconferencia de su embarazo cuando estés en Aruba. No va a poder aguantarse hasta que os veáis."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_eva4
        if eva._var("pregnant") and not prg:
            $ eva._var("undiscoveredPregnancy", False)
            "[eva] te informa de que está embarazada antes de irse. Se ríe ante la ironía de quedarse embarazada el mismo día que perdió la virginidad."
            "No se puede imaginar lo común que puede llegar a ser si no se toman las medidas adecuadas."
            if persistent.family:
                "También te dice que quiere hablar con un tal [mael] en Aruba sobre las implicaciones de que un clon se quede embarazado."
    else:
        scene c31s002_105_eva5
        "[eva] pasa a verte poco después de la hora de la comida. Pasáis un rato hablando de NTR, pero ninguno está centrado en la conversación."
        "Sabéis que el otro está pensando en el tiempo que vas a estar en Aruba sin ella."
    "Sabéis que sólo vais a estar un mes separados, pero también sabéis que va a parecer una eternidad."
    if meg._var("route"):
        $ prg = False
        scene c31s002_105_megAn
        $ weds = weds + 1
        if weds > 1:
            "Tras un breve descanso, [meg] llama a tu puerta."
        else:
            "[meg] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        "El sexo con ella sabe a despedida, pero no es menos maravilloso por ello."
        if persistent.pregnancy and not meg._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[meg] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [meg] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ meg._var("pregnant", True)
                    $ meg._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[meg] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_meg4
        if meg._var("undiscoveredPregnancy") and not prg:
            $ meg._var("undiscoveredPregnancy", False)
            "[meg] te informa de que está embarazada antes de irse. Ahora sabe que tiene una familia que va a apoyarla durante el embarazo."
            "Aunque el padre del bebé se va a perder la mayoría del proceso."
    else:
        scene c31s002_105_meg5
        "[meg] también pasa a visitarte. Pasáis un rato charlando y te promete que vendrá a casa todo lo que pueda mientras estés fuera."
        "Se ha integrado tanto en la familia que quiere asegurarse de que todo el mundo esté bien."
    "Cuando llega la despedida de verdad, no hay tristeza, sino esperanza porque el reencuentro llegue pronto."
    "Tiene que volver a Westport para trabajar esta noche, con lo que ni siquiera se podrá quedar a cenar."
    if kim._var("route"):
        $ prg = False
        scene c31s002_105_kimAn
        $ weds = weds + 1
        if weds > 1:
            "A media tarde, la hermosa [kim] te visita en tu habitación."
        else:
            "[kim] no tuvo su noche de bodas, pero eso no quiere decir que no vaya a recuperar el tiempo perdido."
        "Vuestra segunda vez juntos es incluso mejor que la primera. Ya no hay dudas. Ya no hay dolor."
        if persistent.pregnancy and not kim._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[kim] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [kim] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ kim._var("pregnant", True)
                    $ kim._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[kim] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_105_kim4
        if kim._var("undiscoveredPregnancy") and not prg:
            $ kim._var("undiscoveredPregnancy", False)
            "[kim] te informa de que está embarazada antes de irse. Habláis un poco de cómo puede afectar a su carrera."
            "Ya ha empezado a pensar en ideas sobre un canal de MeTube para recomendar ejercicios para embarazadas."
    else:
        scene c31s002_105_kim5
        "[kim] pasa a verte poco antes de la cena. Ella también quiere pasar un rato a solas contigo."
    "La despedida llega demasiado pronto. Tu última cena en casa por una temporada está a punto de llegar."
    stop music fadeout (1.5)
    "Al final nunca hicisteis aquellas fotos que propuso [emm], y no habrá tiempo antes de que te vayas."
    return
label c31s002_kiaChurch:
    if _in_replay:
        call mrS3_kia_route from _call_mrS3_kia_route_20
        call mrS3_kia_pregnant from _call_mrS3_kia_pregnant_2
        if kia._var("pregnant"):
            $ kia._var("undiscoveredPregnancy", True)
    play music ("music/SeeingHeaven.ogg")
    if not kia._var("route"):
        scene c31s002_105_kia5
        "[kia] te acompaña a tu habitación mientras charláis después de cenar."
        "Es una razón como otra cualquiera para pasar unos últimos momentos contigo antes del día de tu partida."
        scene black with dissolve
        stop music fadeout (1.5)
        "Después de un día con tantas despedidas, duermes como un lirón."
    else:
        $ prg = False
        scene c31s002_105_kiaAn
        $ weds = weds + 1
        if weds > 1:
            "Después de cenar, [kia] entra en tu habitación dispuesta a tener su noche de bodas, aunque sea con retraso."
        else:
            "[kia] no tuvo su noche de bodas ayer, pero eso no quiere decir que no vaya a recuperar el tiempo perdido después de la cena."
        "El sexo con ella es tierno y salvaje a la vez, tal como lo fue en el hotel donde pasasteis vuestra primera noche juntos."
        if persistent.pregnancy and not kia._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[kia] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [kia] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ kia._var("pregnant", True)
                    $ kia._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[kia] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        if kia._var("undiscoveredPregnancy") and not prg:
            scene c31s002_110a with fade
            call BlinkXS4("c31s002_110") from _call_BlinkXS4_1447
            "Después de la tórrida sesión de sexo..."
            $ kia._var("undiscoveredPregnancy", False)
            kia "Por cierto, estoy embarazada..."
            mc "¿Qué? ¿Ya lo sabes?"
            call BlinkXS4("c31s002_115") from _call_BlinkXS4_1448
            kia "*Risa* No de ahora, idiota. Me hice el test por si en nuestra primera noche juntos..."
            mc "¡Eso es genial! Supongo que no lo esperabas, pero ¿estás contenta?"
            call BlinkXS4("c31s002_120") from _call_BlinkXS4_1449
            kia "Estoy contenta. Y sorprendida. ¿A mi edad y al primer intento?"
            mc "Dices intento como si hubiera sido algo planeado..."
            call BlinkXS4("c31s002_125") from _call_BlinkXS4_1450
            kia "En el momento en que me pediste que me casara contigo, pensé que, a mi edad, sería difícil que pudiera darte hijos..."
            kia "Eso me puso un poco triste... No en ese momento. Las emociones y cómo fue la noche no dejaron espacio para la tristeza."
            kia "Pero al día siguiente..."
            mc "Aunque no hubiera pasado, no tendrías que ponerte triste. Hay suficiente alegría en estar contigo."
            call BlinkXS4("c31s002_130") from _call_BlinkXS4_1451
            kia "Eso lo piensas ahora. Quizás en unos años pensarías diferente..."
            kia "Pero a lo que iba es a que pensé que seguramente, si pasaba, nos llevaría unos cuantos intentos."
            kia "Por eso digo que estoy sorprendida de que haya pasado al primero."
            mc "Bueno... Primer intento... No sé cuántas veces lo intentamos aquella noche."
            call BlinkXS4("c31s002_135") from _call_BlinkXS4_1452
            kia "*Risa* ¡Es verdad! Nos pasamos toda la noche teniendo sexo. ¿Diez? ¿Quince veces?"
            kia "No creía que fuera posible algo así. Ni para mí ni para ti."
            mc "*Risa* Me alegro de que estuvieras equivocada. Y del resultado."
            call BlinkXS4("c31s002_140") from _call_BlinkXS4_1453
            kia "Yo también. Ahora tengo ganas de ver cómo se desarrolla el embarazo. A mi edad..."
            mc "No le des tantas vueltas a la edad. Estoy seguro de que todas las mujeres de la familia te van a cuidar."
            mc "Y de que [sam.nick] va a estar comprobando cada uno de los parámetros del embarazo sin casi dejarte vivir."
            call BlinkXS4("c31s002_145") from _call_BlinkXS4_1454
            kia "Aún no se lo he dicho a nadie, ni siquiera a [eil.nick]."
            kia "No quería que me empezaran a agobiar con que me cuidara antes de la boda y de que te fueras. Y quería que fueras el primero en saberlo."
            kia "Bueno, la única que lo sabe es [ama], de cuando hicimos el test."
            mc "Creo que has hecho bien. Estoy seguro de que, si [sam.nick] lo supiera, ya tendrías una visita programada en el hospital."
            mc "Aunque no creo que sirviera de nada."
            call BlinkXS4("c31s002_150") from _call_BlinkXS4_1455
            kia "Y los médicos se sorprenderían un poco si les dijera que estoy embarazada de doce días. Habría que explicar cómo lo sabemos."
            mc "¿Ya hace doce días?"
            call BlinkXS4("c31s002_155") from _call_BlinkXS4_1456
            kia "Sí, [mc]. Doce días ya. No hemos tenido mucho tiempo para estar juntos desde aquel día."
            mc "Bueno, no sé si aguantaré diez o quince veces hoy, pero..."
            call BlinkXS4("c31s002_160") from _call_BlinkXS4_1457
            kia "Ni lo pienses. Mañana vas a tener un día muy largo y tienes que descansar. Si acabaste la mitad de agotado que yo, hoy no lo vamos a repetir."
            mc "Vaya..."
            call BlinkXS4("c31s002_170") from _call_BlinkXS4_1458
            mc "*Risa* ¿Me creerías si te dijera que no estuve cansado en todo el día?"
            kia "*Risa* Creía que no mentías nunca..."
            mc "Touché. Aunque una pregunta no es una mentira."
            call BlinkXS4("c31s002_165") from _call_BlinkXS4_1459
            kia "Tengo ganas de saber qué piensan todas las cotillas de la iglesia cuando me vean aparecer con mi barriguita de embarazada."
            mc "Y con un marido ausente..."
            kia "Tendré que asegurarme de que sepan que el bebé no es de [sol] sino de mi nuevo marido."
            mc "Creo que lo del nuevo marido les va a sorprender tanto como lo del embarazo. Eres católica al fin y al cabo..."
            call BlinkXS4("c31s002_105_kia4") from _call_BlinkXS4_1460
            kia "Me da lo mismo de lo que se sorprendan. Lo único que me importa es que ahora soy una mujer libre y feliz."
            kia "Y que tengo un marido con el que voy a dormir la última noche que va a estar en casa en mucho tiempo."
            mc "En demasiado tiempo."
        else:
            scene c31s002_105_kia4a with fade
            call BlinkXS4("c31s002_105_kia4") from _call_BlinkXS4_1461
            "Después de la tórrida sesión de sexo..."
            kia "Y ahora deberíamos ir a dormir. Mañana tienes un día demasiado largo y tienes que descansar."
            mc "¿Sólo una vez hoy?"
            kia "No todas nuestras noches tienen que ser de diez o quince veces, [mc]."
            mc "*Risa* Tenía que intentarlo."
            call BlinkXS4("c31s002_170") from _call_BlinkXS4_1462
            kia "*Risa* No creía que fuera posible algo así. Ni para mí ni para ti. Pero si acabaste la mitad de agotado que yo, hoy no lo vamos a repetir."
            mc "*Risa* ¿Me creerías si te dijera que no estuve cansado en todo el día?"
            kia "*Risa* Creía que no mentías nunca..."
            mc "Touché. Aunque una pregunta no es una mentira."
        scene c31s002_170d with dissolve
        "Os metéis en la cama y no tardáis en quedaros dormidos."
        stop music fadeout (1.5)
        "El día ha sido largo y estás seguro de que no hubieras aguantado las diez o quince veces. Quizás tres o cuatro veces más como máximo..."
    return
label c31s003_norExhibitionists:
    if _in_replay:
        call mrS3_nor_route from _call_mrS3_nor_route_35
        if nor._var("route"):
            call mrS3_nor_pregnant from _call_mrS3_nor_pregnant_5
            if nor._var("pregnant"):
                call mrS3_nor_undiscoveredPregnancy from _call_mrS3_nor_undiscoveredPregnancy
            call mrS3_eri_route from _call_mrS3_eri_route_37
            if eri._var("route"):
                call mrS3_nor_anal from _call_mrS3_nor_anal
            $ fromPrevious = False
            call mrS3_rels from _call_mrS3_rels_42
    $ prg = False
    scene black with dissolve
    play music ("music/Stardust.ogg")
    centered "{size=+20}{b}DÍA 38 – JUEVES{/b}{/size}"
    scene c31s002_005a with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    "Te despierta el sonido de unos nudillos en tu puerta."
    nor "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    mc "Sí, pasa."
    call BlinkXS4("c31s003_010") from _call_BlinkXS4_1463
    nor "Buenos días. ¿Vas a usar la camioneta esta mañana?"
    mc "Buenos días, [nor]. No tengo nada planificado. ¿Necesitas algo?"
    call BlinkXS4("c31s003_015") from _call_BlinkXS4_1464
    nor "Mi coche no arranca... otra vez. ¿Puedo cogerte prestada la camioneta?"
    mc "No hay problema. ¿Dónde tienes que ir?"
    nor "A San Luis. Tengo que firmar unos papeles."
    mc "¿Algo importante? ¿A qué hora tienes que estar allí?"
    call BlinkXS4("c31s003_020") from _call_BlinkXS4_1465
    nor "Tengo que estar allí en una hora. Solo es una actualización de datos para la sociedad de la residencia de estudiantes y firmar tu despido."
    mc "¿Me vas a despedir?"
    call BlinkXS4("c31s003_025") from _call_BlinkXS4_1466
    nor "*Risa* Llevas menos de dos meses trabajando para nosotras y ahora te coges seis meses de vacaciones en Aruba."
    nor "*Risa* ¡Y mira qué hora es y todavía estás en la cama!"
    nor "Creo que son razones suficientes como para despedirte."
    mc "Yo también lo creo."
    mc "En vez de prestarte la camioneta, te voy a llevar yo. Será mi último servicio a la empresa."
    call BlinkXS4("c31s003_030") from _call_BlinkXS4_1467
    nor "¿No te fías de mí conduciendo?"
    mc "No voy a responder a esa pregunta. Tan solo diré que espero que mi camioneta siga funcionando cuando vuelva."
    mc "Y que tú tengas un coche nuevo."
    mc "Voy a ducharme, vestirme, desayunar, y nos vamos."
    if nor._var("route"):
        call BlinkXS4("c31s003_035") from _call_BlinkXS4_1468
        nor "¿Y no vas a besar a tu esposa?"
        if mc._var("relationships")>1:
            mc "*Risa* ¿A cuál de ellas?"
            nor "*Risa* ¡Capullo! ¡La única que hay en tu habitación!"
        mc "¡Por supuesto que sí!"
        scene c31s003_035d with dissolve
        "Te levantas de la cama, totalmente desnudo, y abrazas a tu esposa mientras tus labios recorren los suyos."
        "Vas a echar de menos esos rojos labios mientras estés en Aruba."
        call BlinkXS4("c31s003_040") from _call_BlinkXS4_1469
    else:
        call BlinkXS4("c31s003_045") from _call_BlinkXS4_1470
    nor "Voy a cambiarme de zapatos y a prepararte el desayuno mientras te duchas."
    mc "Gracias, [nor]."
    nor "*Risa* No me des las gracias. Si no lo hago, llegaremos tarde."
    scene drive_day with fade
    "Tras desayunar, llevas a [nor] a San Luis Obispo, donde firma unos papeles y tu despido."
    "No hay indemnización."
    scene c31s003_050a with fade
    call BlinkXS4("c31s003_050") from _call_BlinkXS4_1471 #2000
    mc "Si no fuera porque soy el dueño y CEO de una empresa milmillonaria, estaría en el paro."
    nor "*Risa* Si no fueras el CEO de una empresa milmillonaria, no te irías a Aruba, con lo que no hubiera tenido que despedirte."
    mc "Touché."
    mc "Mmmmm..."
    call BlinkXS4("c31s003_055") from _call_BlinkXS4_1472 #1000
    nor "¿Qué pasa?"
    mc "He hecho una relación de ideas rara..."
    nor "¿Qué ha pasado por esa cabeza tuya?"
    mc "He pensado en tu exhibicionismo..."
    call BlinkXS4("c31s003_060") from _call_BlinkXS4_1473 #0
    nor "¡Uff! He estado tan ocupada que no he podido seguir... explorándolo. ¿Por qué has pensado en eso?"
    mc "Se me ha ocurrido que, si me visitas en Aruba, sería un buen sitio para seguir explorándolo."
    mc "No sé si hay playas nudistas allí."
    call BlinkXS4("c31s003_065") from _call_BlinkXS4_1474 #-1000
    nor "Ya lo he mirado. No hay ninguna playa nudista. Incluso el topless está prohibido en las playas públicas."
    nor "Solo se puede hacer en algunas playas privadas que pertenecen a resorts. Aunque la gente va a playas apartadas para una experiencia de... ropa opcional."
    mc "No lo sabía. Creía que, como son medio europeos, estaría permitido en todos sitios. Al menos hacer topless."
    call BlinkXS4("c31s003_070") from _call_BlinkXS4_1475 #-2000
    nor "Creo que tenemos una percepción de los europeos un poco distorsionada a este lado del charco."
    nor "Cuando estuve en Barcelona, era común ver gente en topless en la playa, pero a la que te alejabas 300 yardas de la arena, tenías que ponerte una camiseta."
    nor "No podías ir en bikini a la que te alejabas de la playa."
    call BlinkXS4("c31s003_075") from _call_BlinkXS4_1476 #-3000
    nor "Realmente era chocante ver a varias chicas en topless rodeadas de familias con niños y que nadie le diera ninguna importancia."
    nor "En aquella época, aquí en Newport no era demasiado común fuera de algunas playas apartadas."
    mc "A eso me refería con lo de que siendo Aruba medio europea..."
    call BlinkXS4("c31s003_080") from _call_BlinkXS4_1477 #Bosque
    nor "Supongo que hay muchas mujeres que prefieren no hacerlo por si les hacen fotos. Ahora todo el mundo lleva una cámara encima."
    nor "Aruba vive del turismo. Especialmente turismo americano. Hay muchos retrógrados en este país."
    mc "Entonces habrá que buscar otro sitio donde puedas explorar tu exhibicionismo..."
    stop music fadeout (1.5)
    if persistent.walkthrough:
        $ wt1 = _("Escena de exhibicionismo y sexo en público.")
        $ wt2 = _("Escena de exhibicionismo.")
        $ wt3 = _("Sin consecuencias. Fin de la escena.")
    else:
        $ wt1 = ""
        $ wt2 = ""
        $ wt3 = ""
    menu:
        "Quítate el top." (wt=wt1) if nor._var("route"):
            call c31s003_norNude from _call_c31s003_norNude
            if _in_replay:
                $ fromPrevious = True
            call c31s003_norSex from _call_c31s003_norSex
            call c31s003_returnHome from _call_c31s003_returnHome
        "Quítate el top." (wt=wt2) if not nor._var("route"):
            call c31s003_norNude from _call_c31s003_norNude_1
            call c31s003_returnHome from _call_c31s003_returnHome_1
        "No decir nada." (wt=wt3):
            call c31s003_noNorNude from _call_c31s003_noNorNude
    return
label c31s003_norNude:
    play music ("music/SneakySnitch.ogg")
    call BlinkXS4("c31s003_085") from _call_BlinkXS4_1478
    nor "¿QUÉ? ¿Estás loco?"
    mc "Estamos en una carretera por la que no pasa casi nadie a esta hora. Y estás dentro de la camioneta."
    mc "Es un buen momento para hacerlo, ¿no?"
    call BlinkXS4("c31s003_090") from _call_BlinkXS4_1479
    nor "Pero... ¿y si nos cruzamos con alguien que nos conozca?"
    mc "En eso consiste el exhibicionismo, ¿no? En que te vean o, como mínimo, que tengas el riesgo de que te vean."
    call BlinkXS4("c31s003_095") from _call_BlinkXS4_1480 #3500
    nor "Mmmm... ¿Sabes una cosa? ¡Tienes razón!"
    "Por un momento creías que no iba a aceptar."
    mc "Sigo pensando que me debería comprar una camiseta que diga 'Tengo razón. Da lo mismo cuando leas esto'."
    scene c31s003_100a with fade
    call BlinkXS4("c31s003_100") from _call_BlinkXS4_1481 #sin pantalones 3000
    nor "*Risa* Entonces nunca estaríamos de acuerdo contigo."
    mc "Te he dicho que te quitaras el top, no los shorts."
    nor "Bueno, paso a paso... ¿Quieres que me lo quite todo?"
    mc "Déjate los zapatos. Tengo una idea."
    scene c31s003_105d with fade #bragas colgando de un pie 2500
    pause (1.5)
    call BlinkXS4("c31s003_105") from _call_BlinkXS4_1482 #sin bragas 2000
    nor "Nadie se va a dar cuenta de si llevo zapatos o no, dentro de la camioneta."
    mc "¿Por eso has empezado por los shorts y las bragas?"
    nor "Quería saber si me encontraría cómoda..."
    mc "¿Y estás cómoda?"
    scene c31s003_110a with fade
    call BlinkXS4("c31s003_110") from _call_BlinkXS4_1483 #topless 1500
    nor "Cómoda y cachonda..."
    if not nor._var("route"):
        mc "*Risa* No sé si deberías decirme eso... Pero es un paso en la buena dirección."
        call BlinkXS4("c31s003_115") from _call_BlinkXS4_1484 #1000
        nor "No te preocupes, no voy a hacerme un dedo en el coche. Eso sería incómodo para los dos..."
    else:
        mc "*Risa* Es un paso en la buena dirección. Aunque espero que puedas esperar unos minutos."
        call BlinkXS4("c31s003_115") from _call_BlinkXS4_1485 #1000
        nor "No te preocupes, no voy a hacerme un dedo en el coche ni a hacerte nada... aún. Seguramente tendríamos un accidente..."
    mc "Estoy de acuerdo..."
    call BlinkXS4("c31s003_120") from _call_BlinkXS4_1486 #500
    nor "Por aquí no se va a casa..."
    mc "Lo sé. Te he dicho que tenía una idea."
    nor "¿Qué idea? A veces me das miedo."
    mc "Ya te he dicho que nadie pasa por esta carretera. ¿Quieres saber cómo te sentirás si alguien te ve?"
    call BlinkXS4("c31s003_125") from _call_BlinkXS4_1487 #0
    nor "El riesgo de que me vean me está excitando... No sé cómo me sentiré si me ven de verdad."
    mc "Pues lo vas a descubrir en breve. Ahí tienes el primer espectador."
    scene c31s003_125d with dissolve
    "En dirección contraria a la vuestra aparece un coche. Es imposible saber quién conduce."
    "No sabes si [nor] se tapará o dejará que la vean en su actual estado."
    scene c31s003_125e with dissolve
    "Con el coche acercándose rápidamente, [nor] toma la decisión que no podías haber imaginado que tomaría."
    "Con sus antebrazos junta sus tetas en un canalillo que... podría provocar accidentes."
    nor "¡Me encanta esto!"
    scene c31s003_125f with dissolve
    "La cara del pobre hombre al cruzarse con vosotros denota sorpresa."
    "Imaginas que hace mucho que no ve unas tetas tan perfectas como las de [nor], si es que las ha visto alguna vez."
    call BlinkXS4("c31s003_130") from _call_BlinkXS4_1488
    mc "¿Qué tal? ¿Cómo te has sentido?"
    nor "¡Increíblemente bien! Gracias por esto. Nunca hubiera hecho algo así sin ti. ¿Has visto su cara?"
    mc "No me des las gracias todavía. No hemos acabado aún."
    call BlinkXS4("c31s003_135") from _call_BlinkXS4_1489
    nor "¿Qué vamos a hacer ahora?"
    mc "Te he dicho que tenía una idea. De momento, puedes seguir enseñándole las tetas a todos los coches que se crucen con nosotros."
    nor "*Risa* ¡Voy a llegar a casa empapadísima!"
    if not nor._var("route"):
        mc "*Risa* Demasiada información, [nor]..."
    else:
        mc "*Risa* Esa es la idea..."
    mc "Pero en ningún momento he dicho que fuéramos a ir a casa."
    call BlinkXS4("c31s003_140") from _call_BlinkXS4_1490
    nor "¿Qué? ¿Dónde vamos?"
    mc "Lo sabrás en unos minutos."
    mc "De momento, intenta que nadie tenga un accidente mientras le enseñas las tetas."
    scene c31s003_145a with fade
    call BlinkXS4("c31s003_145") from _call_BlinkXS4_1491
    "Unos minutos después, paras al lado de un pequeño parque. Nunca hay nadie aquí. Nadie vive cerca."
    "No sabes qué hace este parque a cientos de yardas de la casa más cercana. Siempre has supuesto que es uno de esos proyectos urbanísticos que nunca se completaron."
    nor "¿Por qué has parado?"
    mc "Para que te bajes de la camioneta."
    call BlinkXS4("c31s003_150") from _call_BlinkXS4_1492
    nor "¿QUÉ?"
    mc "Quiero que atravieses el parque andando. No hay nadie, con lo que puedes pasearte desnuda."
    mc "Yo daré la vuelta con la camioneta y te esperaré al otro lado."
    call BlinkXS4("c31s003_155") from _call_BlinkXS4_1493
    nor "No sé si estoy preparada para esto... ¿A plena luz del día?"
    mc "En un parque desierto, da lo mismo si es de día o de noche. No te va a ver nadie."
    mc "Y esta tarde me voy a Aruba. No tendré muchas oportunidades de desafiar tus límites en los próximos meses."
    call BlinkXS4("c31s003_160") from _call_BlinkXS4_1494
    nor "Tienes razón... Y no hace falta que te compres la camiseta."
    nor "Tan solo prométeme una cosa."
    mc "¿Qué?"
    scene c31s003_165a with fade
    call BlinkXS4("c31s003_165") from _call_BlinkXS4_1495
    nor "*Risa* Que no te vas a ir y dejarme aquí tirada y desnuda."
    mc "*Risa* Te lo prometo."
    scene c31s003_170a with fade
    "Das la vuelta al parque y aparcas la camioneta justo a la salida."
    "Sabes que casi nunca hay nadie en este parque, pero 'casi' es la palabra clave. Al menos no había nunca nadie cuando estabas en el instituto."
    "Prefieres que [nor] pueda meterse corriendo en la camioneta si pasa algún imprevisto."
    "No hay rastro de [nor] por ningún lado. Decides esperar unos minutos antes de ir a buscarla."
    scene c31s003_170b with dissolve
    "De pronto, [nor] asoma la cabeza por la otra entrada del parque."
    "La seguridad que tenía hace un momento ha desaparecido. Parece que se ha dado cuenta de que esto es real."
    "Los dos minutos que la has dejado sola han hecho aparecer las dudas en ella."
    "Le haces gestos para que se acerque a ti."
    scene c31s003_925pv
    show c31s003_925v
    pause (10.0)
    scene c31s003_925dv
    hide c31s003_925v
    "Ella empieza a avanzar reluctantemente, mirando alrededor a cada paso, como si hubiera voyeurs escondidos detrás de cada arbusto en el vacío parque."
    "Su cara refleja una inseguridad que no estaba ahí hace unos minutos."
    "Es diferente andar al descubierto que enseñarle las tetas a un coche en dirección contraria durante un segundo."
    "Se siente más expuesta."
    scene c31s003_895a with hpunch
    "De pronto se para, sorprendida."
    "Estabas tan centrado en ella que no estabas prestando atención a tu alrededor."
    "Ahora oyes una voz acercándose."
    scene c31s003_895i with dissolve
    wom "Sí, Carla, te espero en el parque. Yo ya he hecho mi rutina de yoga esta mañana."
    wom "Tienes que hacer más ejercicio. A nuestra edad no nos podemos quedar sentadas todo el día viendo reality shows."
    wom "Da lo mismo que empiece a hacer calor. Vas a venir a caminar conmigo sí o sí. Hasta luego. No tardes."
    scene c31s003_895j with dissolve
    mc "Buenos días, Señora. Hace un buen día para hacer ejercicio."
    wom "Buenos días. Ciertamente es un buen día. Si mi amiga no fuera tan vaga..."
    mc "Que disfruten del ejercicio."
    scene c31s003_895b with dissolve
    pause (1.0)
    scene c31s003_895c with dissolve
    "[nor] aprovecha que estás entreteniendo a la anciana para esconderse tras un árbol."
    "No es una secuoya, con lo que su imponente culo asoma por uno de los costados."
    scene c31s003_895k with dissolve
    wom "¿Usted también ha venido a hacer ejercicio?"
    if nor._var("route"):
        mc "No, Señora. Estoy esperando a mi esposa. Supongo que no tardará."
    else:
        mc "No, Señora. Estoy esperando a mi tía. Supongo que no tardará."
    wom "Que la espera se le haga breve. Voy a sentarme."
    mc "Disfrute de su día de ejercicio, Señora."
    scene c31s003_895d with dissolve
    pause (1.0)
    scene c31s003_895e with dissolve
    "La mujer se sienta en uno de los bancos del parque, mirándote con poco disimulo."
    "Admites que un tipo en un parque vacío, apoyado en el muro que lo rodea, puede parecer un poco sospechoso."
    scene c31s003_895f with dissolve
    "[nor] aprovecha que la anciana tiene su atención centrada en ti para asomar por detrás del árbol."
    "Su cara, interrogándote, te dice que te está pidiendo indicaciones. Se encuentra desnuda en un parque con una invitada inesperada."
    "Te encoges de hombros."
    "Ella sólo tiene dos opciones. Salir del parque por donde ha entrado o seguir hasta donde la estás esperando."
    "Pero es una decisión que tiene que tomar ella."
    scene c31s003_930pv
    show c31s003_930v
    pause (4.63)
    scene c31s003_930dv
    hide c31s003_930v
    "[nor] toma la decisión correcta y empieza a andar con un paso exageradamente despreocupado."
    "Es casi como si fuera una chiquilla dando saltitos por el bosque mientras recoge flores."
    "Difícilmente tendrá una oportunidad tan buena como esta para explorar su fetiche."
    scene c31s003_895g with dissolve
    "Finalmente se para a unos metros de la mujer, que la mira con la boca abierta."
    nor "Buenos días, Señora. Hace un día espectacular para hacer yoga desnuda."
    wom "Buenos... días... Sí. Un... buen... día... para... hacer... yoga..."
    nor "Que disfrute de su día, Señora. Namaste."
    scene c31s003_935pv
    show c31s003_935v
    pause (5.43)
    scene c31s003_935dv
    hide c31s003_935v
    "Sin esperar respuesta, [nor] camina hacia ti con paso mucho más seguro, como si la anciana no existiera. Disfrutando cada paso."
    "Se acaba de dar cuenta de que no tiene que disimular lo que está haciendo delante de desconocidos."
    "Acaba de dar un paso enorme en la aceptación de su fetiche."
    call BlinkXS4("c31s003_895h") from _call_BlinkXS4_1496
    nor "*Risa* Te voy a matar."
    mc "*Risa* ¿Por qué? Creo que ha ido genial. Has conseguido que no le dé un infarto a la pobre señora."
    nor "Menos mal que estaba el árbol para poder esconderme."
    mc "Lo que se dice esconderte..."
    call BlinkXS4("c31s003_890") from _call_BlinkXS4_1497
    nor "¿Qué? ¿Se me veía?"
    if nor._var("route"):
        mc "Se te veía un poco de ese hermoso culo que tienes por uno de los lados del árbol."
    else:
        mc "Se te veía un poco del culo por uno de los lados del árbol."
    call BlinkXS4("c31s003_885") from _call_BlinkXS4_1498
    nor "Ya te dije que tenía el culo gordo. *Risa* Al menos no se me veía por LOS DOS LADOS del árbol."
    if nor._var("route"):
        mc "Y yo te dije que me encanta ese culo."
    mc "¿Nos vamos a casa?"
    call BlinkXS4("c31s003_880") from _call_BlinkXS4_1499
    if nor._var("route"):
        nor "Creo que no hemos acabado aquí. Aún hay algo que quiero hacer."
        mc "¿Poner nerviosas a más ancianas? Aún no ha cerrado la boca desde que la has saludado..."
        nor "Y eso me está poniendo más cachonda aún. No creo que pueda aguantar hasta llegar a casa."
        mc "Me gusta hacia dónde va esto."
    else:
        nor "Será mejor que nos vayamos. ¿La anciana ya ha cerrado la boca?"
        mc "No. Creo que se le ha desencajado la mandíbula cuando te ha visto y no sé si la podrá volver a cerrar."
        nor "*Risa* Creo que si empezara a masturbarme aquí sería demasiado para ella."
        mc "Demasiada información, [nor]. Creo que sería demasiado incluso para mí."
        mc "Vámonos a casa antes de que hagas alguna locura."
    stop music fadeout (1.5)
    return
label c31s003_noNorNude:
    scene drive_day with fade
    "Volvéis a casa, en silencio. Parece que los dos estáis pensando en algún buen sitio donde ella pueda explorar su exhibicionismo."
    return
label c31s003_returnHome:
    scene c31s003_175e with fade
    play music ("music/Stardust.ogg")
    "Cuando estáis a punto de entrar en la camioneta, oís la voz de la anciana en el parque."
    wom "Menos mal que has llegado, Carla."
    wom "Si hubieras venido unos minutos antes, hubieras visto a una mujer preciosa desnuda por aquí."
    "Carla" "¿Qué? ¿Qué hacía desnuda?"
    wom "Según ella, estaba haciendo yoga. Pero creo que estaba mintiendo."
    "Carla" "¿Por qué crees eso?"
    wom "Porque no llevaba calzado adecuado para hacer yoga. ¡Iba con sandalias!"
    "Os cuesta contener la risa."
    scene drive_day with fade
    "Subís a la camioneta y conduces hacia casa mientras [nor] sigue enseñando las tetas a los conductores en dirección contraria."
    "Después de lo que ha pasado en el parque, parece que esto la excita menos que cuando lo ha hecho por primera vez."
    if nor._var("route"):
        "Lo de la anciana y el sexo mientras sólo un muro os separaba de ella ha sido muy excitante."
        "Más de lo que enseñarle sus tetas a un desconocido conduciendo en dirección contraria cada pocos minutos puede ser."
    else:
        "Lo de la anciana ha sido mucho más excitante de lo que enseñarle las tetas a un desconocido conduciendo en dirección contraria cada pocos minutos puede ser."
    scene c31s003_180a with fade
    call BlinkXS4("c31s003_180") from _call_BlinkXS4_1500
    "A media milla de casa..."
    mc "¿Quieres que pare antes de volver a casa para que te vistas?"
    nor "Creo que no hace falta. Déjame en la puerta de mi casa."
    mc "Estoy muy orgulloso de ti."
    call BlinkXS4("c31s003_185") from _call_BlinkXS4_1501
    nor "No lo hubiera podido hacer si no me lo hubieras propuesto. Ha sido muy... divertido."
    nor "Creo que lo repetiremos cuando vuelvas de Aruba."
    mc "¿No vas a repetirlo mientras esté fuera?"
    call BlinkXS4("c31s003_190") from _call_BlinkXS4_1502
    nor "Me siento más segura haciéndolo si estás tú cerca."
    if nor._var("route"):
        nor "No creo que quiera hacerlo si no estás. Además, hoy ha sido una anciana, pero podría haber sido un hombre."
        nor "Y no quiero que ningún hombre... ni nadie... me vea desnuda si no está mi marido cerca."
        nor "Contigo es una experiencia compartida. Sin ti, sería... raro."
    else:
        nor "Creo que estaría demasiado nerviosa como para excitarme."
    mc "Bueno, pues tendrás que esperar a que vuelva, si no vienes a visitarme a Aruba."
    call BlinkXS4("c31s003_195") from _call_BlinkXS4_1503
    nor "*Risa* Aunque vaya a visitarte a Aruba, no lo haré."
    nor "No quiero que me arresten en otro país. Me gustaría volver a casa de una pieza."
    nor "Y ahora te voy a dejar. Supongo que tienes muchas cosas que hacer antes de viajar esta tarde."
    mc "No demasiado. Tengo ya todo preparado."
    scene c31s003_195d with fade
    nor "Pues entonces te veo luego para la despedida."
    mc "Hasta luego, [nor]."
    "Se ha ido dejándose la ropa y el bolso."
    call BlinkXS4("c31s003_305") from _call_BlinkXS4_1504
    "Un segundo después vuelve sobre sus pasos. En el momento en que la ves volver, coges el bolso y la ropa del asiento trasero."
    nor "Sin el bolso no voy a poder entrar en casa. La ropa te la puedes quedar si quieres, como un recordatorio del día de hoy."
    if nor._var("undiscoveredPregnancy") and not prg:
        nor "Por cierto, estoy embarazada."
        scene c31s003_195e with fade
        "Sin darte tiempo a responder, vuelve a atravesar la puerta de la valla con una sonrisa pícara en la boca."
        "Tienes más razones todavía para acabar con los asuntos en Aruba lo antes posible."
    else:
        scene c31s003_195e with fade
        "Se vuelve a ir, con una sonrisa pícara en la boca."
    stop music fadeout (1.5)
    return
label c31s003_norSex:
    scene c31s003_200d with fade
    play music ("music/SexyLoungeMusic.ogg")
    "[nor] abre la puerta trasera de la camioneta mientras te regala una vista impresionante de su culo."
    call BlinkXS4("c31s003_200") from _call_BlinkXS4_1505
    nor "Siéntate ahí."
    mc "¿Aquí? Creía que iba a ser..."
    call BlinkXS4("c31s003_205") from _call_BlinkXS4_1506
    nor "¿Dentro de la camioneta? ¿Y perder la oportunidad de que la señora esa venga a cotillear?"
    mc "Hoy estás salvaje..."
    nor "Más salvaje estaré cuando te sientes. Además, es culpa tuya..."
    scene c31s003_210d with fade
    mc "¿Estoy bien aquí?"
    nor "Estarás mejor cuando nos libremos de estos shorts."
    call BlinkXS4("c31s003_210") from _call_BlinkXS4_1507
    nor "Ahora estás mejor. Y ya estás preparado para mí."
    mc "Llevas un rato paseándote desnuda por aquí. ¿Cómo querías que estuviera?"
    nor "Tumbado. Quiero que estés tumbado."
    scene c31s003_215a with fade
    call BlinkXS4("c31s003_215") from _call_BlinkXS4_1508
    mc "¿Aquí estoy bien?"
    nor "Ahí estás perfecto."
    scene c31s003_215d with fade
    "[nor] se sube de pie a la camioneta. La visión de su espectacular culo y sus perfectas piernas casi cubren todo tu campo visual."
    mc "Bonitas piernas. ¿A qué hora abren?"
    nor "*Risa* Dentro de un rato. Pero antes..."
    scene c31s003_215e with hpunch
    "Ella se agacha para dejar su coño a la altura de tu boca."
    nor "*Risa* Espero que no te sientas dominado. No es mi intención..."
    "Su cristalina risa le hubiera quitado cualquier componente de dominación a la postura si no lo hubieran hecho sus palabras."
    mc "Sabes que siempre me ha gustado... comer."
    scene c31s003_915pv with dissolve
    show c31s003_915v
    "No hace falta que digáis nada más. A ti siempre te ha gustado comer, y a ella siempre le ha gustado tener tu polla en la boca."
    nor "*Jadeo* *Slurp* *Gemido*"
    "Siempre es una palabra demasiado absoluta. Tan solo hace un mes que estáis juntos. Pero parece que lo habéis estado desde siempre."
    nor "*Gemido* *Slurp* *Jadeo*"
    if nor._var("pregnant") and not nor._var("undiscoveredPregnancy"):
        "En un mes la has dejado embarazada y te has casado con ella. Quizás el concepto 'un mes' no signifique tanto tiempo para todo el mundo."
    else:
        "En un mes te has casado con ella. Quizás el concepto 'un mes' no signifique tanto tiempo para todo el mundo."
    scene c31s003_920pv with dissolve
    show c31s003_920v
    hide c31s003_915v
    "Dejas de lamer durante un segundo para observar las fabulosas vistas. Ha sido un mes que ha parecido una vida al lado de [nor]."
    nor "*Jadeo* *Slurp inquisitivo* *Gemido*"
    "Sus rojos labios alrededor de tu astil nunca serán algo de lo que te canses. Ni por lo bien que encajan, ni por las sensaciones que hacen recorrer tu cuerpo."
    nor "*Gemido* *Slurp enfadado* *Jadeo*"
    "Si sigue así, no vas a tardar en proporcionarle el segundo desayuno."
    call BlinkXS4("c31s003_220") from _call_BlinkXS4_1509
    nor "¿Te has olvidado de cómo funciona esto? ¿O es que ahora que estamos casados tengo que hacer yo todo el trabajo?"
    mc "Me he quedado anonadado con las vistas..."
    scene c31s003_225a with fade #Sentada, quitandose zapatos
    call BlinkXS4("c31s003_225") from _call_BlinkXS4_1510
    nor "Pues esto es trabajo de dos. Si no vas a hacer el tuyo, baja de la camioneta mientras me quito los zapatos."
    mc "Lo siento..."
    scene c31s003_230a with fade #de pie
    call BlinkXS4("c31s003_230") from _call_BlinkXS4_1511
    nor "No lo sientas. Ahora vas a trabajar tú."
    mc "¿Contra la pared? ¡Te vas a destrozar la espalda!"
    call BlinkXS4("c31s003_235") from _call_BlinkXS4_1512
    nor "*Risa* Por eso me casé con un chico joven y fuerte. Te va a tocar mantenerme en brazos."
    "Cuando la ves así te preguntas si la fama de femme fatale que tenía cuando volviste a casa era totalmente inmerecida."
    "La tenía reprimida, pero estaba dentro de ella. Tan solo hacía falta una sesión de exhibicionismo para que apareciera."
    nor "Y recuerda que no soy ligera precisamente."
    mc "Para mí eres ligera como una pluma. *Risa* Recuerda que soy un chico joven y fuerte."
    scene c31s003_235d with fade
    "Te acercas a ella y la besas apasionadamente, sin dejar que su espalda o su cabeza toquen la rugosa pared."
    "Pensar en su maravilloso culo repleto de arañazos te provoca un escalofrío, y no de placer precisamente."
    scene c31s003_235e with vpunch
    "Sin dejar de besarla, la levantas en vilo y apuntas tu polla a la entrada de su coño."
    nor "*Jadeo*"
    if persistent.family:
        "Sin que tus labios liberen los suyos, ese jadeo es la única muestra de sorpresa que tu tía puede mostrar."
    else:
        "Sin que tus labios liberen los suyos, ese jadeo es la única muestra de sorpresa que [nor] puede mostrar."
    scene c31s003_240An with dissolve
    "Después de todo lo que ha pasado durante la mañana estás tan cachondo como lo está ella."
    "Tus caderas actúan casi por voluntad propia y penetras su húmedo coño con un rápido movimiento."
    nor "*GEMIDO*"
    scene c31s003_900pv with dissolve
    show c31s003_900v
    hide c31s003_920v
    "Sin darle tiempo a reaccionar, empiezas a bombear mientras te aseguras de que su espalda está a una distancia segura de la pared."
    nor "*Jadeo* ¡Oh, sí! *Gemido* ¡Necesitaba esto! *Jadeo*"
    "Tanto como lo necesitabas tú. Nada más penetrarla, una sensación conocida ha empezado a reptar por tus pantorrillas."
    nor "*Gemido* No sé si quiero... *Jadeo* que la señora se asome a ver qué son estos ruidos... *Gemido*"
    "Ahora mismo, preferirías que no lo hiciera. Ser interrumpido por una señora teniendo un infarto no entra en tus planes."
    scene c31s003_910pv with dissolve
    show c31s003_910v
    hide c31s003_900v
    if persistent.family:
        "Pero, por cómo el coño de tu tía se cierra sobre tu astil, parece que a ella no le desagrada la idea."
    else:
        "Pero, por cómo el coño de [nor] se cierra sobre tu astil, parece que a ella no le desagrada la idea."
    nor "*Jadeo* ¡Está siendo una mañana alucinante! *Gemido* ¡Sigue follándome! *Jadeo*"
    "Ella lo dice como si tú pudieras parar el movimiento de tus caderas. No podrías aunque quisieras. Y no quieres."
    nor "*Gemido* ¡Teníamos que haber hecho esto antes! *Jadeo*"
    "Quizás no hubiera sido lo mismo sin tu partida acercándose. Quizás ni siquiera hubiera salido el tema de conversación."
    scene c31s003_905pv with dissolve
    show c31s003_905v
    hide c31s003_910v
    "Pero te alegras de que haya sido hoy. Tendréis una nueva experiencia compartida en los meses que vais a pasar separados."
    nor "*JADEO* ¡Estoy a punto de correrme! *GEMIDO* Estás tocando todos los puntos correctos. *JADEO*"
    "La perspectiva de ser pillados hace que su orgasmo se acerque aún más rápido de lo normal."
    nor "*GEMIDO* ¡Fóllame más duro! *JADEO* ¡Más profundo! *GEMIDO*"
    "Lo harías si no fuera porque la posición y aguantar a [nor] en brazos mientras proteges su espalda es lo suficientemente complicado."
    call OrgasmXS4("c31s003_245") from _call_OrgasmXS4_56 #a-240b-b
    nor "*JADEO* ¡JODER! *GEMIDO* ¡SÍ! *JADEO*"
    if persistent.family:
        "No tienes ni tiempo ni medios para cambiar el ritmo antes de que tu tía explote alrededor de tu polla."
    else:
        "No tienes ni tiempo ni medios para cambiar el ritmo antes de que [nor] explote alrededor de tu polla."
    "Parece uno de los orgasmos más intensos que habéis compartido. Su exhibicionismo ha sido por fin alimentado como debía."
    nor "*GEMIDO* ¡ES SUPER INTENSO! *JADEO*"
    "Esperas que la señora esté escuchando música mientras espera a su amiga. A un volumen muy alto."
    if eri._var("route") and nor._var("anal"):
        call BlinkXS4("c31s003_250") from _call_BlinkXS4_1513
        nor "*Gemido* El otro día me encantó por detrás... *Jadeo* ¿Quieres repetir? *Gemido*"
        call c31s003_analMenu from _call_c31s003_analMenu
    elif not eri._var("route"):
        call BlinkXS4("c31s003_250") from _call_BlinkXS4_1514
        nor "*Gemido* Siempre has hecho referencias a mi culo... *Jadeo* ¿Quieres probarlo? *Gemido*"
        call c31s003_analMenu from _call_c31s003_analMenu_1
    else:
        call c31s003_orgasmPussy from _call_c31s003_orgasmPussy
    stop music fadeout (1.5)
    return
label c31s003_analMenu:
    $ resetWalkthrough()
    if persistent.walkthrough:
        if eri._var("route"):
            $ wt1 = _("Sexo anal con [nor].")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = _("Sexo anal activado con [nor].")
            $ wt2 = _("Sexo anal desactivado con [nor].")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¡Por supuesto!" (wt=wt1):
            $ nor._var("anal", True)
            call c31s003_anal from _call_c31s003_anal
        "No." (wt=wt2):
            "La pregunta llega tarde para ti. Las contracciones de su orgasmo te han llevado hasta tu límite."
            if not eri._var("route"):
                $ nor._var("anal", False)
            call c31s003_orgasmPussy from _call_c31s003_orgasmPussy_1
    return
label c31s003_orgasmPussy:
    if persistent.pregnancy and not nor._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[nor] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ nor._var("pregnant", True)
                $ nor._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
                $ prg = True
            "Correrte dentro." (wt = wt2):
                pass
    call OrgasmXS4("c31s003_255") from _call_OrgasmXS4_57
    hide c31s003_905v
    mc "¡Mpfft!"
    if persistent.family:
        "Explotas sin poder evitarlo en el interior de tu tía, llenando su coño hasta que tu semen empieza a recorrer tu astil, ayudado por la gravedad."
    else:
        "Explotas sin poder evitarlo en el interior de [nor], llenando su coño hasta que tu semen empieza a recorrer tu astil, ayudado por la gravedad."
    nor "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME! *JADEO*"
    "Os quedáis inmóviles un momento mientras notas cómo tu semen llega a la base de tu polla. La mayoría se queda dentro de [nor]."
    scene c31s003_260a with fade
    call BlinkXS4("c31s003_260") from _call_BlinkXS4_1515
    "Unos segundos después..."
    nor "*Gemido* Ha sido increíble. *Jadeo* Gracias por esto... *Gemido*"
    mc "¿Gracias?"
    nor "No creo que hubiera podido hacer esto sin ti."
    mc "*Risa* Espero que nunca hagas esto sin mí. Ya voy a tener demasiado NTR en los próximos meses como para que vayas haciendo esto con otros."
    call BlinkXS4("c31s003_265") from _call_BlinkXS4_1516
    nor "*Risa* ¡Eres idiota! Sabes a lo que me refiero."
    "Las pequeñas convulsiones de su risa hacen que se escape un poco más de semen del interior de su coño."
    mc "Lo sé. Para mí ha sido un honor ayudarte a alimentar a tu fetiche."
    call BlinkXS4("c31s003_270") from _call_BlinkXS4_1517
    nor "Y ahora deberíamos irnos, antes de que la señora decida por fin venir a investigar los ruidos."
    nor "No hemos sido silenciosos precisamente..."
    mc "TÚ no has sido silenciosa. Yo he estado calladito."
    mc "Pero tienes razón. Deberíamos irnos."
    return
label c31s003_anal:
    scene c31s003_275a with fade
    "Tras dejarla en el suelo, [nor] se desempala y te presenta su maravilloso culo."
    "No tiene ni un rasguño."
    nor "Cuando quieras. Ve con cuidado... Creo que a veces olvidas lo enorme que es Mjolnir."
    mc "*Risa* Te aseguro que no lo olvido nunca."
    scene c31s003_275b with fade
    "Te acercas por detrás y apoyas tu glande sobre su estrecho agujero."
    mc "¿Preparada?"
    nor "Tanto como puedo estarlo."
    scene c31s003_275An with dissolve
    if persistent.family:
        "Penetras el culo de tu tía lentamente, intentando ser consciente de sus reacciones por si tienes que parar."
    else:
        "Penetras el culo de [nor] lentamente, intentando ser consciente de sus reacciones por si tienes que parar."
    nor "*Jadeo* ¡Mmmm! *Gemido*"
    "Con los fluidos de su orgasmo actuando como lubricante, Mjolnir se adapta perfectamente al estrecho canal."
    mc "¿Estás bien?"
    if eri._var("route"):
        nor "*Gemido* Estoy bien rellena. *Jadeo* Pero mucho mejor que el otro día. *Gemido*"
    else:
        nor "*Gemido* Estoy bien rellena. *Jadeo* Pero mucho mejor de lo que esperaba. *Gemido*"
    nor "Puedes empezar cuando quieras, antes de que la anciana venga..."
    scene c31s003_940pv with dissolve
    show c31s003_940v
    hide c31s003_905v
    "No crees que, ahora mismo, a ninguno de los dos os importara tener público."
    "Estáis lo suficientemente excitados como para que ni siquiera un estadio lleno de gente mirándoos fuera suficiente como para cortaros el rollo."
    nor "*Jadeo* ¡Me encanta! *Gemido* ¡Sigue! *Jadeo*"
    "El estrecho agujero de [nor] se cierra con fuerza sobre tu polla a cada movimiento, mostrando que está tan excitada como tú."
    "No crees que ni siquiera le importara ahora mismo a ella si una cámara de televisión estuviera grabándoos y retransmitiendo en directo por la televisión nacional."
    scene c31s003_950pv with dissolve
    show c31s003_950v
    hide c31s003_940v
    "Es posible que incluso la excitase más todavía."
    nor "*JADEO* ¡ES INCREÍBLE! *GEMIDO* ¡MÁS PROFUNDO! *JADEO*"
    "La excitación por tener sexo en público es el mejor lubricante que existe."
    nor "*GEMIDO* ¡VOY A CORRERME OTRA VEZ! *JADEO*"
    "Toda esta excitación sin saber que la anciana está esperando a una amiga que podría aparecer en cualquier momento por detrás de la camioneta."
    call OrgasmXS4("c31s003_280") from _call_OrgasmXS4_58
    nor "*JADEO* ¡SÍ! *GEMIDO* ¡JODER! *JADEO!"
    "El orgasmo de [nor] llega cuando el tuyo está empezando a acercarse."
    "Su ano se cierra con fuerza sobre tu astil, haciendo que cada embestida sea aún más placentera."
    scene c31s003_945pv with dissolve
    show c31s003_945v
    hide c31s003_950v
    if persistent.family:
        "Continúas embistiendo el increíble culo de tu preciosa tía, sabiendo que no vas a poder aguantar mucho más."
    else:
        "Continúas embistiendo el increíble culo de la preciosa mujer, sabiendo que no vas a poder aguantar mucho más."
    if eri._var("route"):
        "Tu segunda vez con [nor] por la puerta trasera es incluso mejor que la primera."
    else:
        "Tu primera vez con [nor] por la puerta trasera es incluso mejor de lo que podías haber esperado."
    nor "*GEMIDO* ¡No pares! *JADEO*"
    "Tus caderas no quieren parar. Tú tampoco."
    "Las sensaciones se agolpan en tu polla a la vez que tus muslos se tensionan de una forma que solo puede anunciar la llegada del orgasmo."
    call OrgasmXS4("c31s003_285") from _call_OrgasmXS4_59
    hide c31s003_945v
    mc "¡Mpfft!"
    if persistent.family:
        "Explotas sin poder evitarlo en el interior de tu tía, llenando su culo hasta que tu semen empieza a recorrer tu astil, ayudado por la gravedad."
    else:
        "Explotas sin poder evitarlo en el interior de [nor], llenando su culo hasta que tu semen empieza a recorrer tu astil, ayudado por la gravedad."
    nor "*JADEO* ¡SÍ! *GEMIDO* ¡LLÉNAME! *JADEO*"
    "Os quedáis inmóviles un momento mientras notas cómo tu semen llega a la base de tu polla. La mayoría se queda dentro de [nor]."
    scene c31s003_290a with fade
    call BlinkXS4("c31s003_290") from _call_BlinkXS4_1518
    "Unos segundos después..."
    nor "*Gemido* Ha sido increíble. *Jadeo* Gracias por esto... *Gemido*"
    mc "¿Gracias?"
    nor "No creo que hubiera podido hacer esto sin ti."
    mc "*Risa* Espero que nunca hagas esto sin mí. Ya voy a tener demasiado NTR en los próximos meses como para que vayas haciendo esto con otros."
    call BlinkXS4("c31s003_295") from _call_BlinkXS4_1519
    nor "*Risa* ¡Eres idiota! Sabes a lo que me refiero."
    "Las pequeñas convulsiones de su risa hacen que se escape un poco más de semen del interior de su culo."
    mc "Lo sé. Para mí ha sido un honor ayudarte a alimentar a tu fetiche."
    call BlinkXS4("c31s003_300") from _call_BlinkXS4_1520
    nor "Y ahora deberíamos irnos, antes de que la señora decida por fin venir a investigar los ruidos."
    nor "No hemos sido silenciosos precisamente..."
    mc "TÚ no has sido silenciosa. Yo he estado calladito."
    mc "Pero tienes razón. Deberíamos irnos."
    return
label c31s002_secondDayWedding:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_46
        if emm._var("route"):
            call mrS3_emm_pregnant from _call_mrS3_emm_pregnant_3
            if emm._var("pregnant"):
                call mrS3_emm_undiscoveredPregnancy from _call_mrS3_emm_undiscoveredPregnancy
        call mrS3_dap_route from _call_mrS3_dap_route_36
        if dap._var("route"):
            call mrS3_dap_pregnant from _call_mrS3_dap_pregnant_3
            if dap._var("pregnant"):
                call mrS3_dap_undiscoveredPregnancy from _call_mrS3_dap_undiscoveredPregnancy
        call mrS3_sim_route from _call_mrS3_sim_route_25
        if sim._var("route"):
            call mrS3_sim_pregnant from _call_mrS3_sim_pregnant_2
            if sim._var("pregnant"):
                call mrS3_sim_undiscoveredPregnancy from _call_mrS3_sim_undiscoveredPregnancy
        call mrS3_oma_route from _call_mrS3_oma_route_20
        if oma._var("route"):
            call mrS3_oma_pregnant from _call_mrS3_oma_pregnant_5
            if oma._var("pregnant"):
                call mrS3_oma_undiscoveredPregnancy from _call_mrS3_oma_undiscoveredPregnancy
        call mrS3_mad_route from _call_mrS3_mad_route_21
        if mad._var("route"):
            call mrS3_mad_pregnant from _call_mrS3_mad_pregnant_2
            if mad._var("pregnant"):
                call mrS3_mad_undiscoveredPregnancy from _call_mrS3_mad_undiscoveredPregnancy
        call mrS3_mee_route from _call_mrS3_mee_route_16
        call mrS3_deb_route from _call_mrS3_deb_route_30
        if deb._var("route"):
            call mrS3_deb_pregnant from _call_mrS3_deb_pregnant_3
        call mrS3_mar_route from _call_mrS3_mar_route_47
        if mar._var("route"):
            call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_6
            if mar._var("pregnant"):
                call mrS3_mar_undiscoveredPregnancy from _call_mrS3_mar_undiscoveredPregnancy
    $ weds = 0
    play music ("music/RhythmPlay.ogg")
    if emm._var("route"):
        $ prg = False
        scene c31s002_215An
        $ weds = weds + 1
        "Al llegar a tu habitación, [emm] te está esperando. Ella también quiere su noche de bodas, aunque sea por la mañana y con dos días de retraso."
        if persistent.pregnancy and not emm._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[emm] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [emm] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ emm._var("pregnant", True)
                    $ emm._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[emm] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_215d
        if emm._var("undiscoveredPregnancy") and not prg:
            $ emm._var("undiscoveredPregnancy", False)
            "[emm] te informa de que está embarazada antes de irse. Vas a ser padre y tío a la vez."
    else:
        scene c31s002_215e
        "[emm] está esperándote en tu habitación cuando llegas. Quiere pasar un rato contigo antes de que te marches a Aruba."
    "Los minutos pasan mientras charláis y reís, pero [emm] abandona la habitación tras recibir una notificación en el móvil."
    if oma._var("route"):
        $ prg = False
        scene c31s002_200An
        $ weds = weds + 1
        "[oma] aparece poco después. Parece que la notificación en el móvil de [emm] era una forma de decirle que se había acabado su tiempo."
        "[oma] y tú sacáis el máximo provecho del tiempo que la aplicación de [sca] os permite."
        if persistent.pregnancy and not oma._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[oma] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [oma] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ oma._var("pregnant", True)
                    $ oma._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[oma] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_200d
        if oma._var("undiscoveredPregnancy") and not prg:
            $ oma._var("undiscoveredPregnancy", False)
            "[oma] te informa de que está embarazada antes de irse. Sabes que será una gran madre, aunque necesitará entrenarse con 'La Chancla'."
    else:
        scene c31s002_200e
        "[oma] aparece poco después. Parece que la notificación en el móvil de [emm] era una forma de decirle que se había acabado su tiempo."
    "Pasáis un rato charlando antes de que su móvil suene. Empiezas a odiar esa aplicación."
    if dap._var("route"):
        $ prg = False
        scene c31s002_205An
        $ weds = weds + 1
        "[dap] te sorprende plantándose totalmente desnuda en tu habitación. Ella también quiere su despedida especial."
        if persistent.pregnancy and not dap._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[dap] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [dap] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ dap._var("pregnant", True)
                    $ dap._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[dap] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_205d
        if dap._var("undiscoveredPregnancy") and not prg:
            $ dap._var("undiscoveredPregnancy", False)
            "[sca] te informa de que está embarazada antes de irse."
            "En cuanto el embrión esté un poco desarrollado, quiere hacer pruebas genéticas para asegurarse de que no hay ningún problema."
            if persistent.family:
                "Quiere asegurarse de que no hay ningún problema porque seáis primos."
            else:
                "Quiere asegurarse de que no hay ningún problema porque ella sea un clon de [eva]."
    else:
        scene c31s002_205e
        "[dap] aparece en tu habitación para pasar unos últimos minutos contigo."
    "Aprovecha unos momentos para planear las partidas de DnD que haréis por videoconferencia."
    "[dap] abandona tu habitación demasiado pronto. Pero la puñetera aplicación no perdona."
    if deb._var("route"):
        $ prg = False
        scene c31s002_210An
        $ weds = weds + 1
        "Poco después, [deb.nick] llama a tu puerta."
        "La noche de bodas que no pudisteis tener se reduce a un encuentro breve pero maravilloso."
        if persistent.pregnancy and not deb._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[deb] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [deb] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ deb._var("pregnant", True)
                    $ deb._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[deb] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_210d
        "Después del sexo, mientras esperáis que suene la temida notificación, charláis durante un rato que sabe a despedida."
    else:
        scene c31s002_210e
        "Un rato después, es [deb.nick] quien llama a tu puerta. También quiere despedirse de ti."
    "Promete intentar visitarte en Aruba. Solo promete intentarlo. Tiene demasiadas cosas en marcha ahora mismo."
    if mad._var("route"):
        $ prg = False
        scene c31s002_220An
        $ weds = weds + 1
        "[mad.nick] llama a tu puerta y espera fuera hasta que la entras en brazos. El fetiche de esta chica con el matrimonio..."
        "Después tenéis una mini-noche de bodas, aunque los dos pensáis que vuestra verdadera noche de bodas fue la última vez que estuviste en su apartamento."
        if persistent.pregnancy and not mad._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[mad.nick] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [mad] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ mad._var("pregnant", True)
                    $ mad._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[mad.nick] te informará por videoconferencia de su embarazo cuando estés en Aruba." id c31s002_secondDayWedding_82669ce1
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_220d
        if mad._var("pregnant") and not prg:
            $ mad._var("undiscoveredPregnancy", False)
            "[mad.nick] te informa de que está embarazada antes de irse."
            "Al final no ha podido resistirse a hacerse la prueba de embarazo porque quería saberlo antes de que te fueras."
    else:
        scene c31s002_220e
        "[mad.nick] pasa a visitarte después de acabar su turno en la tienda. El rato que pasáis juntos sabe a despedida." id c31s002_secondDayWedding_444a06bd
    "Prometes intentar estar en la siguiente gala de premios a la que asista, ya que a la de San Francisco seguramente no podrás llegar."
    if mee._var("route"):
        $ prg = False
        if persistent.lactation:
            scene c31s002_230Anwm
        else:
            scene c31s002_230Annm
        $ weds = weds + 1
        "Al cabo de un rato, [mee] llama a tu puerta. Vuestra sesión de sexo es tan corta como explosiva."
        "Vuestra primera cita sigue siendo un listón muy alto."
        scene c31s002_230d
    else:
        scene c31s002_230e
        "[mee] también te visita. Lo vuestro ha sido prácticamente un visto y no visto."
    "Ella acaba de llegar de Florida y no habéis tenido mucho tiempo para estar juntos. Ahora eres tú el que se va."
    "La despedida es triste, pero los dos sabéis que unos meses pueden pasar muy rápido."
    "Tan solo esperas que se comporte bien mientras estás fuera."
    if sim._var("route"):
        $ prg = False
        scene c31s002_235An
        $ weds = weds + 1
        "[sim] llama a tu puerta poco después, falta de aliento como si hubiera subido corriendo las escaleras."
        "No le dejas recuperarlo antes de desnudarla y tumbarla en la cama."
        "El sexo es corto y explosivo. Parece mentira que [sim] fuera virgen tan solo hace unas semanas."
        if persistent.pregnancy and not sim._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[sim] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [sim] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ sim._var("pregnant", True)
                    $ sim._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[sim] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_235d
        if sim._var("undiscoveredPregnancy") and not prg:
            $ sim._var("undiscoveredPregnancy", False)
            "[sim] te informa de que está embarazada antes de irse. Se ríe al pensar en cómo va a entrenar cuando le empiece a crecer la barriga."
            "Tú no puedes evitar pensar en que sus marcas empeoraron cuando le empezaron a crecer las tetas."
            "Quizás debería cambiar de especialidad y nadar en estilo espalda."
    else:
        scene c31s002_235e
        "[sim] llega sin aliento a tu habitación para pasar unos últimos minutos contigo."
        "Aprovechas que no puede responder para bromear sobre ella un rato."
    "La despedida es triste, pero ambos sabéis que habéis estado separados con anterioridad y seguisteis siendo amigos."
    if sim._var("route"):
        "Ahora vuestra relación es diferente, mucho más sólida."
    if mar._var("route"):
        $ prg = False
        scene c31s002_225An
        $ weds = weds + 1
        "[mar] aparece poco antes de la hora en la que has quedado con [ama] y [bet]."
        "Quería tener sexo de despedida contigo sin tener que preocuparse de una notificación en el móvil."
        if mc._var("relationships")>1:
            "Por eso ha elegido el último turno."
        "El sexo con ella es tan maravilloso y tierno como siempre. Sabéis que este viaje es una pausa tan solo."
        if persistent.pregnancy and not mar._var("pregnant"):
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("[mar] embarazada.")
            menu:
                "Es la última oportunidad de dejar embarazada a [mar] antes del viaje a Aruba."
                "Correrte dentro. Ir a por el bebé." (wt=wt2):
                    $ mar._var("pregnant", True)
                    $ mar._var("undiscoveredPregnancy", True)
                    $ prg = True
                    play sound ("music/OldMusicBox5.ogg")
                    "[mar] te informará por videoconferencia de su embarazo cuando estés en Aruba."
                "Correrte dentro." (wt = wt1):
                    pass
                    $ prg = False
        scene c31s002_225d
        if mar._var("undiscoveredPregnancy") and not prg:
            $ sim._var("undiscoveredPregnancy", False)
            "[mar] te informa de que está embarazada antes de irse. La alegría la embarga después del primer test fallido de hace unas semanas."
            if persistent.family:
                "No hay preocupación en su voz porque sea un bebé producto del incesto."
    else:
        scene c31s002_225e
        "[mar] aparece poco antes de la hora en la que has quedado con [ama] y [bet]."
        "Quería tener un momento para despedirse de ti sin tener que preocuparse de una notificación en el móvil."
    stop music fadeout (1.5)
    play sound ("music/notification.ogg")
    "Al final, llega la temida notificación. Esta vez no es la aplicación de [sca], sino [emm] enviándole un WhatsUp diciendo que [ama] y [bet] te están esperando."
    return
label c31s002_farewell:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_48
    play music ("music/Sad-Cinematic.ogg")
    scene c31s002_farewellAn
    "La despedida es corta y, pese a todo, da tiempo para que haya ojos llorosos y risas."
    "Algunos abrazos son muy emotivos, como el que [eva] y [ama] comparten. Nunca han estado tanto tiempo separadas como van a estar ahora."
    "Incluso Jamaal promete que va a cuidar de las chicas en un momento de debilidad."
    call BlinkXS4("c31s002_255") from _call_BlinkXS4_1594
    mom "Deberíamos irnos ya o no podréis cumplir con el plan de vuelo."
    mc "Tienes razón. Odio las despedidas. ¿Nos vamos?"
    call BlinkXS4("c31s002_260") from _call_BlinkXS4_1595
    mom "Os llevo y así traeré tu camioneta de vuelta a casa."
    mom "La camioneta de [emm] por unos meses."
    mc "Espero que la camioneta siga siendo negra cuando vuelva."
    call BlinkXS4("c31s002_265") from _call_BlinkXS4_1596
    mom "*Risa* No te preocupes, no le dejaré pintarla de rosa. Y no es que ella YA me lo haya pedido..."
    mc "*Risa* Aún no se ha enfriado mi asiento y ya está haciendo planes para destrozar la camioneta."
    mom "Vámonos."
    scene c31s002_270a with fade
    "Unos minutos después, en el aeropuerto..."
    mom "Cuídate, Tía [bet]. No dejes que [mc] haga ninguna tontería cuando estéis allí."
    bet "No te preocupes. Creo que es el más maduro de los dos. Él debería evitar que yo haga alguna tontería."
    mc "Creo que eso va a ser trabajo de [ama]..."
    call BlinkXS4("c31s002_275") from _call_BlinkXS4_1597
    ama "A mí no me metáis en eso. O sí. Al primero que haga alguna tontería lo pondré a correr varias vueltas alrededor de la base."
    ama "Y tendrá prohibida la pizza durante una semana."
    mc "Creo que acabas de dar con la clave para que Tía [bet] se comporte bien."
    scene c31s002_270b with dissolve
    mom "Y tú... Ten cuidado con la gente de allí. Es posible que todo haya cambiado en el tiempo que has estado fuera."
    mom "Si necesitas cualquier consejo que te pueda dar, estoy a una llamada de distancia."
    ama "¿Y si lo que necesito es hablar contigo de cualquier cosa que no tenga que ver con la empresa?"
    mom "Entonces estoy a una videoconferencia de distancia."
    call BlinkXS4("c31s002_280") from _call_BlinkXS4_1598
    bet "*Risa* No estoy segura de si [mar] se pondría tan sentimental si fuera [emm] la que se va durante un mes."
    mc "Estoy seguro de que se pondría IGUAL de sentimental."
    scene c31s002_270c with dissolve
    mom "Por supuesto que sí."
    call BlinkXS4("c31s002_285") from _call_BlinkXS4_1599
    mom "Y a ti... Creo que no tengo ningún consejo que darte."
    mom "Pero te voy a echar mucho de menos."
    mc "Yo también te voy a echar de menos. Hablaremos un montón por videoconferencia, no te preocupes."
    if mar._var("route"):
        call KissXS4("c31s002_290") from _call_KissXS4_26
    else:
        scene c31s002_270d with dissolve
    mc "Te quiero."
    mom "Yo también te quiero."
    scene black with dissolve
    stop music fadeout (1.5)
    "La despedida de [mar] se hace demasiado corta. Pero hay un avión esperando."
    return
label c31s004_flight1:
    if _in_replay:
        call mrS3_bet_route from _call_mrS3_bet_route_13
    scene c31s004_005d with fade
    play music ("music/Fretless.ogg")
    "Un tipo del personal del aeropuerto recoge vuestras maletas y os lleva hasta el avión, donde hay una asistente de vuelo esperándoos."
    "Os acercáis a ella mientras el tipo carga vuestro equipaje. [ama] y [bet] llevan relativamente poco."
    "Se va a ganar el sueldo del día con tu equipaje."
    call BlinkXS4("c31s004_005") from _call_BlinkXS4_1600
    alb "Buenas tardes, Sr. Marks, Srta. Cavendish. Hola, [ama]."
    if bet._var("route"):
        "[bet] no la saca de su error diciéndole que ya no es 'Srta.'"
    alb "Soy [alb], y seré su asistente de vuelo. Espero que tengan un viaje agradable."
    mc "Gracias, [alb]. Veo que conoces a [ama]. ¿Eres personal de NTR?"
    call BlinkXS4("c31s004_010") from _call_BlinkXS4_1601
    alb "Sí, Sr. Marks. Tanto los pilotos como yo formamos parte del Departamento de Soporte."
    alb "Antes de que lo pregunte, los pilotos son... no son clones."
    mc "No lo iba a preguntar. Si hacen bien su trabajo, no creo que tenga importancia."
    call BlinkXS4("c31s004_015") from _call_BlinkXS4_1602
    alb "Si quieren subir a bordo, el plan de vuelo indica que despegaremos en unos minutos."
    alb "El vuelo nos llevará alrededor de seis horas, con lo que llegaremos alrededor de las 3:15 AM a Aruba, hora local."
    mc "Perfecto. Subamos"
    scene c31s004_020a with fade
    call BlinkXS4("c31s004_020") from _call_BlinkXS4_1603
    "Una vez en el avión, [alb] os guía hasta vuestros asientos y os indica que os preparéis para el despegue, que se produce unos minutos después."
    mc "[alb] ha dicho algo... 'los pilotos son...', pero no ha acabado la frase. La ha cambiado a 'no son clones.'"
    mc "¿Sabes a qué se refería?"
    ama "Seguramente iba a decir 'humanos' o 'normales'. Habrá cambiado el final de la frase porque no sabe qué piensas de los clones."
    ama "Y ahora eres el gran jefe. Acostúmbrate a que la gente vaya con pies de plomo a tu alrededor."
    if persistent.family:
        mc "¡Eso es inaceptable! [eva] o tú sois tan normales o humanas como ella."
    else:
        mc "¡Eso es inaceptable! [eri], [dap], o [emm] son tan normales o humanas como ella."
    call BlinkXS4("c31s004_025") from _call_BlinkXS4_1604
    ama "*Risa* Espero que no. [alb] es un poco cabeza hueca. Pero no es mala chica."
    call BlinkXS4("c31s004_030") from _call_BlinkXS4_1605
    ama "Pero hablando en serio, parte del personal transversal piensa eso de los clones."
    if persistent.family:
        ama "Piensan que somos un producto, que no llegamos a ser personas completas."
    else:
        ama "Piensan que son un producto, que no llegamos a ser personas completas."
    mc "Hablaré con ella después del despegue. Es una de las cosas que tenemos que cambiar."
    call BlinkXS4("c31s004_035") from _call_BlinkXS4_1606
    bet "Creo que no deberías hacerlo. No es el momento de cambiar la opinión de una persona, porque no lo vas a conseguir."
    bet "Tienes que demostrar que tú ves a los clones como personas, pero lo tienes que demostrar con acciones, no con palabras."
    bet "Y no va a servir de nada que la chica se esté preocupando durante todo el viaje por si la vas a despedir por un desliz que ha corregido a tiempo."
    mc "Tienes razón, no puedo echarle la bronca por algo que no ha dicho."
    call BlinkXS4("c31s004_040") from _call_BlinkXS4_1607
    ama "Además, no serviría de nada. Las personas que tienen esa opinión no van a cambiarla por lo que puedas decirles."
    ama "Si ven a los clones como herramientas de usar y tirar, sólo podrán cambiar de opinión cuando hagas cambios que les demuestren lo contrario."
    mc "Pues habrá que empezar a ver qué medidas podemos tomar en ese sentido."
    mc "Tenemos seis horas por delante para empezar a hacer planes."
    call BlinkXS4("c31s004_045") from _call_BlinkXS4_1608
    bet "Mientras vosotros trabajáis, yo voy a aprovechar para echar una siesta en ese sofá de ahí atrás."
    bet "Si llegamos a Aruba a las 3, y mañana hay que levantarse temprano, prefiero adelantar un poco de sueño."
    mc "No lo había pensado. Vamos a dormir muy poco esta noche."
    call BlinkXS4("c31s004_050") from _call_BlinkXS4_1609
    mc "¿Quieres dormir algo tú también?"
    ama "Ahora mismo no tengo nada de sueño. Trabajar un rato me parece una buena idea."
    mc "Entonces, vamos a hacer una lluvia de ideas para lo que podemos hacer en los próximos días."
    scene c31s004_055An with dissolve
    "Mientras [ama] y tú trabajáis durante las siguientes tres horas, [bet] duerme silenciosamente en el sofá de detrás vuestro."
    "Una vez te dijo que, durante su tiempo en África, aprendió a quedarse dormida cada vez que tenía la oportunidad de hacerlo."
    "Nunca podía saber cuándo llegaría una urgencia que la tendría despierta durante varias horas."
    "Hablando con [ama] sobre las cosas que podéis hacer una vez lleguéis a Aruba, aparecen muchas ideas interesantes."
    "Pero necesitas más datos sobre cómo llevarlas a cabo."
    return
label c31s004_noMileHighClub:
    scene c31s004_370a with fade
    call BlinkXS4("c31s004_370") from _call_BlinkXS4_1610
    "Cuando ya es noche cerrada, mientras sobrevoláis el Golfo de Méjico..."
    bet "*Risa*"
    ama "Creía que estabas durmiendo, Tía [bet]."
    mc "Creíamos que te ibas a pasar todo el viaje durmiendo."
    scene c31s004_375a with fade
    call BlinkXS4("c31s004_375") from _call_BlinkXS4_1611
    bet "Este vuelo se me está haciendo eterno. Supongo que Aruba todavía queda lejos. ¿Cuánto he dormido?"
    mc "Unas tres horas. Ya hemos salido de los Estados Unidos."
    call BlinkXS4("c31s004_155") from _call_BlinkXS4_1612
    ama "Aún quedan otras tres horas más, más o menos. Relájate, [bet]."
    mc "*Risa* Le da tiempo de echarse otra siesta."
    call BlinkXS4("c31s004_380") from _call_BlinkXS4_1613
    mc "¿De qué te reías?"
    bet "Me he despertado hace unos minutos y, como no quería molestaros, estaba mirando unos videos de MeTube que me han mandado."
    bet "En uno salía una monja a la que pillaban teniendo sexo en un avión. Aunque se veía que era un decorado."
    call BlinkXS4("c31s004_385") from _call_BlinkXS4_1614
    ama "El Mile High Club. Es un clásico."
    mc "Nunca lo he encontrado demasiado interesante. Un lavabo de avión es un espacio demasiado pequeño."
    call BlinkXS4("c31s004_390") from _call_BlinkXS4_1615
    ama "*Risa* Un espacio donde los que estén se tienen que llevar MUY bien."
    mc "*Risa* Visto así..."
    call BlinkXS4("c31s004_395") from _call_BlinkXS4_1616
    bet "*Risa* Siempre me he imaginado cómo debe ser tener sexo en un avión mientras hay turbulencias."
    mc "*Risa* Sexo movido."
    call BlinkXS4("c31s004_400") from _call_BlinkXS4_1617
    ama "En este avión sería más fácil. El lavabo de atrás es grande. Y detrás del último mamparo hay una cama."
    mc "¿Hay una cama y [bet] está durmiendo en el sofá?"
    call BlinkXS4("c31s004_405") from _call_BlinkXS4_1618
    bet "*Risa* No te metas con mi sofá. Es súper cómodo."
    bet "Y me voy a volver a él ahora mismo. Os dejo seguir trabajando."
    bet "Despertadme cuando lleguemos a Aruba."
    stop music fadeout (1.5)
    mc "Buenas noches, Tía [bet]."
    return
label c31s004_mileHighClub:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_19
        call mrS3_bet_pregnant from _call_mrS3_bet_pregnant_2
    scene c31s004_150a with fade
    call BlinkXS4("c31s004_150") from _call_BlinkXS4_1619
    "Cuando estáis sobrevolando el Golfo de Méjico..."
    bet "Este vuelo se me está haciendo eterno. Supongo que Aruba todavía queda lejos. ¿Cuánto he dormido?"
    mc "Unas tres horas. Ya hemos salido de los Estados Unidos."
    call BlinkXS4("c31s004_155") from _call_BlinkXS4_1620
    ama "Aún quedan otras tres horas más, más o menos. Relájate, [bet]."
    stop music fadeout (1.5)
    mc "*Risa* Le da tiempo de echarse otra siesta."
    call BlinkXS4("c31s004_160") from _call_BlinkXS4_1621
    play music ("music/LePrunierenFleur.ogg")
    bet "Relajarme... sí. O hacer algo más interesante."
    bet "[ama]... ¿te importa si te robo a tu jefe un rato? Me lo llevo al lavabo."
    call BlinkXS4("c31s004_165") from _call_BlinkXS4_1622
    ama "¿El lavabo de un jet privado? Clásico, por lo que he leído. ¿Quieres entrar en el Mile High Club?"
    call BlinkXS4("c31s004_170") from _call_BlinkXS4_1623
    bet "Siempre me ha parecido una tontería. Hasta que me he despertado y me habéis dicho que quedan tres horas para llegar."
    mc "*Risa* Creo que es la razón menos romántica por la que me han propuesto sexo."
    call BlinkXS4("c31s004_175") from _call_BlinkXS4_1624
    ama "Adelante. Pero no tardéis demasiado. Luego necesito continuar hablando con él."
    ama "Y [bet]... procura no hacerte daño. Los lavabos de avión son diminutos."
    call BlinkXS4("c31s004_180") from _call_BlinkXS4_1625
    bet "*Risa* Qué graciosa."
    mc "¿Nadie me pregunta a mí?"
    scene c31s004_180d with dissolve
    bet "No."
    call BlinkXS4("c31s004_185") from _call_BlinkXS4_1626
    ama "No. Sabemos lo que responderías, con lo que... ¿para qué hacerlo?"
    ama "Por cierto, usad el lavabo de atrás, es más grande que el de la parte delantera."
    mc "*Risa* Gracias, [ama]. Creo que [bet] te lo agradecerá."
    call BlinkXS4("c31s004_190") from _call_BlinkXS4_1627 #con la mano extendida
    bet "¿Tú quieres follar o no? *Risa* Si sigues bromeando sobre esta pobre anciana a lo mejor me lo pienso..."
    mc "Ni una broma más. Te lo prometo."
    call BlinkXS4("c31s004_195") from _call_BlinkXS4_1628
    mc "¿Estás segura? Ahí dentro caben justo dos personas de pie si se llevan bien."
    bet "Por eso mismo hay que ser creativos, cielo."
    call BlinkXS4("c31s004_200") from _call_BlinkXS4_1629
    mc "Bueno. Aquí estamos. 40,000 pies o así."
    bet "45,000. Lo he mirado antes de entrar. Eso tiene que contar como ocho cuotas y media de entrada en el club..."
    mc "*Risa* Creo que no funciona así."
    call BlinkXS4("c31s004_205a") from _call_BlinkXS4_1630
    bet "[ama] tenía razón. Este lavabo es más grande que el otro. En el otro hubiera sido más problemático."
    mc "Sigue siendo pequeño..."
    call BlinkXS4("c31s004_205b") from _call_BlinkXS4_1631
    "[bet] echa el pestillo. Una turbulencia leve hace vibrar levemente el mamparo."
    bet "No queremos que [alb] venga a preguntar si estamos bien, ¿verdad?"
    mc "Nope."
    mc "¿Cómo quieres...? Porque el espacio no da para grandes acrobacias."
    call BlinkXS4("c31s004_210") from _call_BlinkXS4_1632
    bet "Lo sé, lo sé. Mi espalda tampoco da para grandes acrobacias. Seamos prácticos."
    bet "Lo primero que hay que hacer es eliminar esos pantalones."
    mc "Me parece una idea estupenda."
    scene c31s004_215a with fade
    call BlinkXS4("c31s004_215") from _call_BlinkXS4_1633
    bet "¡Bendita juventud! Ya estás preparado."
    mc "¿Esperabas algo diferente? Ha empezado a despertarse en cuanto lo has propuesto."
    bet "No. Me encanta que mi marido se ponga así incluso antes de desnudarme."
    mc "Querrás decir quitarte los pantalones, ¿no?"
    scene c31s004_220d with dissolve
    pause (2.0)
    call BlinkXS4("c31s004_220") from _call_BlinkXS4_1634 #se quita el top
    bet "No, cielo. Si lo hacemos, lo hacemos bien."
    mc "Esto se pone muy interesante."
    call BlinkXS4("c31s004_225") from _call_BlinkXS4_1635
    bet "Aún quedan mis shorts... Debería haber traído falda, si lo hubiera pensado antes."
    mc "*Risa* ¿Te hubieras quitado el top y dejado la falda?"
    call BlinkXS4("c31s004_230") from _call_BlinkXS4_1636
    bet "*Risa* Hubiera sido una combinación interesante..."
    mc "Quizás en otra ocasión."
    scene c31s004_235a with dissolve
    pause (1.5)
    scene c31s004_235b with fade
    "Te arrodillas y eliminas los pantalones que cubren el hermoso cuerpo de [bet]."
    "Te sorprende que no lleve bragas."
    call BlinkXS4("c31s004_240") from _call_BlinkXS4_1637
    mc "Me imagino que algo sí que tenías pensado, si ibas comando."
    bet "Después de ducharme he descubierto que había guardado todas las bragas limpias en la maleta. No me apetecía abrirla..."
    mc "Bendita maleta."
    scene c31s004_240d with hpunch
    "Hundes tu cara entre sus piernas. Está completamente mojada."
    bet "*Gemido* No, así no... *Jadeo*"
    call BlinkXS4("c31s004_245") from _call_BlinkXS4_1638
    mc "¿Hay algo malo en ello?"
    bet "Por muy prometedor que sea, te quiero dentro de mí."
    scene c31s004_250a with fade
    call BlinkXS4("c31s004_250") from _call_BlinkXS4_1639
    "[bet] apoya las manos en el lavabo y mira a tu reflejo en el espejo con una sonrisa directa."
    bet "Así. Tú de pie, yo apoyada. Simple, efectivo y sin riesgo de que me quede doblada como un pretzel."
    mc "*Risa* Eres la mujer más práctica que conozco."
    bet "Y la más lista. Por eso funciona esto entre nosotros."
    scene c31s004_250d with dissolve
    "Te acercas a ella por detrás, posando las manos en sus caderas. [bet] suspira al notar su contacto."
    bet "*Jadeo* Me estás matando de anticipación. *Gemido*"
    mc "Tú tienes tu ritmo, yo el mío."
    bet "*Gemido* Bien, bien. Sigue. *Jadeo* Pero no me tengas así hasta que aterricemos. *Gemido*"
    scene c31s004_250e with dissolve
    "Tu mano recorre la espalda de la ex-monja, que se apoya más firmemente en el lavabo, relajando los hombros."
    "Tu polla apunta directamente a la entrada de su túnel del amor."
    call BlinkXS4("c31s004_255") from _call_BlinkXS4_1640
    bet "{b}Esto{/b} sí que hace que el viaje merezca la pena."
    mc "Aún no hemos empezado."
    bet "Lo sé. Y si no empiezas pronto...."
    scene c31s004_255d with dissolve
    pause (1.5)
    scene c31s004_255d with hpunch
    "El avión pasa por una pequeña bolsa de aire. El balanceo produce una penetración involuntaria y una cascada de risas."
    bet "*Gemido risueño* ¡Buen timing! *Jadeo*"
    mc "*Risa* El piloto colabora. Le subiré el sueldo."
    call BlinkXS4("c31s004_260") from _call_BlinkXS4_1641
    bet "Creo que, técnicamente, ya hemos entrado en el Club, ¿no?"
    mc "Como has dicho antes, si lo hacemos, lo hacemos bien."
    scene c31s004_915pv with dissolve
    show c31s004_915v
    "La postura es sencilla pero funciona. Usando el lavabo como apoyo, sin exigir flexibilidad a unas articulaciones que llevan más de seis décadas de servicio."
    bet "*Gemido* Así... *Jadeo* Despacio. *Gemido*"
    "El coño de la cirujana se cierra con fuerza sobre tu astil. Sus gemidos se mezclan con el ronroneo constante de los motores."
    bet "*Jadeo* Me está excitando mucho... *Gemido* Saber que [ama] está al otro lado del mamparo. *Jadeo*"
    "Los gemidos de [bet] son suaves. Dudas que [ama] los pueda escuchar desde su asiento."
    scene c31s004_260d with fade
    "Te equivocas."
    scene c31s004_935pv with fade
    show c31s004_935v
    hide c31s004_915v
    "El espejo te devuelve la imagen de los ambos moviéndoos lentamente."
    mc "¿Bien así?"
    bet "*Gemido* Perfectamente bien así. *Jadeo*"
    "El lavabo cruje levemente al ritmo de tus embestidas. El sonido es tapado por los gemidos de [bet], que van subiendo de volumen."
    bet "*Jadeo* Justo ahí. *Gemido* Me encanta. *Jadeo*"
    "Su coño vuelve a exprimir tu astil con un abrazo húmedo y caliente."
    scene c31s004_925pv with dissolve
    show c31s004_925v
    hide c31s004_935v
    "Vuestros movimientos, lentos y acompasados, son tan placenteros como tiernos."
    "Por suerte el lavabo es más grande que el de un avión comercial y no hay mucha diferencia con la vez que tuvisteis sexo en la ducha en Monterey."
    bet "*GEMIDO* ¡Esto es súper excitante! *JADEO*"
    "Sería súper excitante en un lavabo de un hotel, en una piscina, o en un desierto."
    "Para ti, lo que lo hace excitante es la compañía, no el lugar."
    scene c31s004_930pv with dissolve
    show c31s004_930v
    hide c31s004_925v
    "Aunque el Mile High Club ha cogido tanta fama que no te hubiera gustado desaprovechar la oportunidad."
    "A pesar de que no eres de los que hacen las cosas porque otros lo hayan hecho anteriormente."
    "Tampoco es algo que vayas a colgar en tus redes sociales."
    bet "*JADEO* ¡ESTOY A PUNTO DE CORRERME! *GEMIDO* ¡MI PRIMERA VEZ EN UN AVIÓN! *JADEO*"
    "Pero estás seguro de que [bet] lo comentará en el grupo de WhatsUp de las chicas."
    call OrgasmXS4("c31s004_265") from _call_OrgasmXS4_60
    bet "*GEMIDO* ¡SÍ! *JADEO* ¡INCREÍBLE! *GEMIDO*"
    "Los gemidos de [bet] incrementan aún más su volumen al llegar al primero de sus orgasmos."
    "Ahora estás seguro de que [ama] no necesitará leerlo en el chat."
    scene c31s004_920pv with dissolve
    show c31s004_920v
    hide c31s004_930v
    "Sigues bombeando mientras los movimientos de la ex-monja se vuelven más descoordinados."
    bet "*JADEO* No pares... *GEMIDO* mientras aguante... *JADEO*"
    "Sus piernas empiezan a tener problemas para seguir tus movimientos, pero quieres que sea ella la que proponga un cambio de postura."
    "Es su fantasía al fin y al cabo, aunque tú también la estés disfrutando."
    bet "*GEMIDO* Casi no me sostengo... *JADEO*"
    call BlinkXS4("c31s004_270") from _call_BlinkXS4_1642
    bet "*Jadeo* Necesito un cambio de postura. *Gemido* Mis piernas parecen flanes... *Jadeo*"
    mc "¿Cómo quieres hacerlo?"
    scene c31s004_275a with fade
    call BlinkXS4("c31s004_275") from _call_BlinkXS4_1643
    "Tía [bet] se da la vuelta y se sienta sobre la única superficie plana donde cabe su culo."
    "El plástico cruje bajo su peso. No le das demasiada importancia."
    bet "*Gemido* Así. *Jadeo* Aunque este avión va a necesitar revisión después de nosotros. *Gemido*"
    mc "Lo cargaré a gastos de empresa."
    call BlinkXS4("c31s004_280") from _call_BlinkXS4_1644
    bet "*Risa* ¡[mc]!"
    mc "*Risa* ¿Qué? Técnicamente es un viaje de trabajo."
    scene c31s004_280d with dissolve
    "La hermosa mujer te agarra por la camiseta y te besa apasionadamente."
    "No os habíais besado desde que entrasteis en el lavabo. El sexo sin besos no es igual de bueno."
    scene c31s004_285b with dissolve
    pause (1.5)
    scene c31s004_285a with hpunch
    "Vuestras caderas se buscan durante el beso."
    "Mjolnir conoce el camino a su hogar."
    scene c31s004_290a with dissolve
    pause (1.5)
    scene c31s004_290b with fade
    bet "*Jadeo* Esta camiseta sobra. *Gemido* Quiero notar tu pecho contra mis tetas. *Jadeo*"
    mc "Una idea estupenda."
    bet "*Gemido* Lo sé. *Jadeo* Pero empieza a moverte ya. *Gemido*"
    scene c31s004_900pv with dissolve
    show c31s004_900v
    hide c31s004_920v
    "La urgencia en su voz impulsa tus caderas. Bueno... su urgencia y esa sensación que había empezado a trepar por tus pantorrillas."
    bet "*JADEO* ASÍ MEJOR. *GEMIDO*"
    "En esta postura la puedes penetrar mucho más profundamente que antes. Su culo no es un obstáculo."
    bet "*GEMIDO* SI SIGUES ASÍ VOY A VOLVER A CORRERME. *JADEO*"
    "Vas a seguir así. Y ella va a seguir corriéndose. Ser mujer tiene algunas ventajas increíbles."
    scene c31s004_910pv with dissolve
    show c31s004_910v
    hide c31s004_900v
    "Ella se abraza con fuerza a ti con su siguiente ronda de orgasmos."
    "Parece que piense que la diminuta plataforma de plástico ya no es suficiente para soportar su peso."
    bet "*JADEO* ¡POR DIOS! *GEMIDO* ¡ESTE ES MEJOR AÚN! *JADEO*"
    "Te abraza con su brazo en tu hombro, con sus piernas en tu cintura, con su coño alrededor de tu astil."
    "Empiezas a verle lo excitante a tener sexo en el lavabo de un avión. Tus piernas empiezan a tensarse."
    scene c31s004_905pv with dissolve
    show c31s004_905v
    hide c31s004_910v
    "Tus caderas toman el control como si tuvieran una mente propia, marcando un ritmo cómodo para ambos."
    "Un ritmo que permite a tu orgasmo seguir trepando por tus muslos."
    bet "*GEMIDO* ¡SIGUE ASÍ! *JADEO* ¡NO PUEDO PARAR DE CORRERME! *GEMIDO*"
    "Aunque te gustaría continuar hasta aterrizar en la isla, incluso tú tienes tus límites."
    "Y esos límites se están acercando a una velocidad endiablada."
    if persistent.pregnancy and not bet._var("pregnant"):
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[bet] embarazada.")
        menu:
            "Correrte dentro. Ir a por el bebé." (wt=wt2):
                $ bet._var("pregnant", True)
                $ bet._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt1):
                pass
    call OrgasmXS4("c31s004_295") from _call_OrgasmXS4_61
    mc "¡Mpfft!"
    "Tu resistencia llega a su límite y explotas llenado el coño de tu esposa hasta que unas gotas empiezan a deslizarse por tu astil."
    bet "*JADEO* ¡SÍ! *GEMIDO*"
    "Tus piernas tiemblan con las últimas embestidas, hasta que tus caderas deciden quedarse inmóviles."
    scene c31s004_300a with fade
    call BlinkXS4("c31s004_300") from _call_BlinkXS4_1645
    stop music fadeout (1.5)
    "Minutos después, el silencio relativo del lavabo solo lo rompe vuestra respiración combinada y el eterno zumbido de los reactores."
    play music ("music/LifeOfAWanderingWizard.ogg")
    bet "Hecho."
    mc "Hecho."
    bet "El Mile High Club. Oficialmente somos miembros."
    mc "Con honores. *Risa* Aunque no nos van a dar un carnet ni una insignia."
    mc "¿La cadera bien?"
    call BlinkXS4("c31s004_305") from _call_BlinkXS4_1646
    bet "La cadera, la espalda y todo lo demás. Estoy perfectamente, no soy de porcelana."
    mc "Nunca lo he pensado."
    call BlinkXS4("c31s004_310") from _call_BlinkXS4_1647
    bet "Bien. Que no se te olvide. O tendré que demostrarte que sigo siendo capaz de aguantar una sesión larga de sexo."
    mc "*Risa* ¿Qué es lo que no se me tenía que olvidar?"
    call BlinkXS4("c31s004_315") from _call_BlinkXS4_1648
    bet "*Risa* Vámonos antes de que [ama] venga a ver si me he roto."
    mc "*Risa* Espero que no le tengas que demostrar nada a ella."
    scene c31s004_320a with fade
    call BlinkXS4("c31s004_320") from _call_BlinkXS4_1649
    "Al volver a vuestros asientos..."
    ama "¿Todo bien?"
    call BlinkXS4("c31s004_325") from _call_BlinkXS4_1650
    bet "De maravilla."
    call BlinkXS4("c31s004_330") from _call_BlinkXS4_1651
    ama "¿El avión sigue entero?"
    mc "Estructuralmente sólido."
    call BlinkXS4("c31s004_335") from _call_BlinkXS4_1652
    ama "Bien. Entonces, si todavía tienes energía, tenemos que mirar un par de documentos que he encontrado mientras estabais ahí."
    mc "Ahora mismo."
    call BlinkXS4("c31s004_340") from _call_BlinkXS4_1653
    bet "Por cierto, el lavabo, aunque pequeño, es más que suficiente."
    if ama._var("route"):
        bet "Por si algún día lo quieres probar."
    call BlinkXS4("c31s004_345") from _call_BlinkXS4_1654
    ama "Creo que, si algún día quiero entrar en el Club en este avión, usaría la cama que hay más allá del último mamparo."
    scene c31s004_350An with dissolve
    bet "¿Qué? ¿Hay una cama? ¿Por qué no nos lo has dicho? ¿Tú lo sabías?"
    mc "No, pero creo que le hubiera quitado un poco la sensación de estar en un avión."
    call KissXS4("c31s004_355") from _call_KissXS4_27
    call BlinkXS4("c31s004_355") from _call_BlinkXS4_1655
    bet "Tienes razón. Me voy al sofá de nuevo y os dejo trabajar. Necesito descansar un rato."
    scene c31s004_360a with fade
    call BlinkXS4("c31s004_360") from _call_BlinkXS4_1656
    "[bet] se desploma en el sofá con una sonrisa enorme, mira por la ventanilla el océano azul iluminado por la Luna bajo las nubes."
    "Suspira satisfecha."
    stop music fadeout (1.5)
    bet "{i}(45,000 pies. No está mal para una anciana de sesenta y cuatro.){/i}"
    return
label c31s004_flight2:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_20
    scene c31s004_060a with fade
    play music ("music/Fretless.ogg")
    "No pasa mucho rato antes de que [ama] se quede dormida."
    "Continúas leyendo algunos de los informes que [aar] te ha enviado."
    "Hay 1,247 pares de botas en la base. Le sigue una distribución por tallas y cuántos individuos usan cada talla."
    scene c31s004_060b with dissolve
    "[bet] se ha quedado dormida poco después de volver a su sofá."
    "Envidias esa capacidad de poderse quedar dormida rápidamente en cualquier circunstancia."
    scene c31s004_060An with dissolve
    "Cada vez te cuesta más mantener los ojos abiertos."
    "Entre el cansancio del largo día de despedidas y lo aburridos que son los informes de [aar], se convierte en una lucha titánica."
    scene black with dissolve
    "Una lucha que pierdes cuando aún quedan dos horas para aterrizar."
    centered "{size=+20}{b}DÍA 39 – VIERNES{/b}{/size}"
    scene c31s004_065An with dissolve
    alb "Señor, estamos a punto de aterrizar. Deberían abrocharse los cinturones."
    call BlinkXS4("c31s004_065") from _call_BlinkXS4_1657
    mc "Gracias, [alb]. Voy a despertar a [ama] y a Tía [bet]."
    alb "Gracias, Señor."
    scene c31s004_070d with fade
    "Sacudes suavemente a [ama]."
    if ama._var("route"):
        mc "Cielo, despierta. Estamos a punto de aterrizar."
    else:
        mc "[ama], despierta. Estamos a punto de aterrizar."
    play music ("music/WarIsComing.ogg")
    scene c31s004_070An with dissolve
    "Su despertar no es como esperabas."
    call BlinkXS4("c31s004_070") from _call_BlinkXS4_1658
    ama "¡Lo siento! ¿Te he hecho daño?"
    play music ("music/SaveMe.ogg")
    "No quieres hacerla sentir mal, con lo que bromeas sobre el asunto."
    mc "*Risa* Nada que una semana con el brazo en cabestrillo no pueda resolver."
    mc "Estamos a punto de aterrizar. [alb] ha venido a avisarnos de que nos pongamos los cinturones."
    mc "Voy a despertar a [bet]."
    scene c31s004_075a with fade
    call BlinkXS4("c31s004_075") from _call_BlinkXS4_1659
    "Cuando te levantas, [bet] ya se está desperezando."
    bet "No hace falta que me despiertes. Me quedo dormida rápido, y me despierto igual de rápido."
    mc "Perfecto. ¿Vienes a sentarte con nosotros para el aterrizaje?"
    bet "Voy."
    scene c31s004_080d with dissolve
    mc "¿Qué pasa [ama]? No me has roto nada..."
    call BlinkXS4("c31s004_080") from _call_BlinkXS4_1660
    ama "Podía haberlo hecho. Este viaje me está poniendo los nervios de punta. Volver a la base..."
    ama "Siempre voy a ser la misma persona desquiciada entrenada para matar..."
    mc "Si quitas 'la misma' y 'desquiciada' de esa frase, estoy de acuerdo, pero eres mucho más."
    mc "Y no eres la misma que se fue hace meses de Aruba. No eres ni siquiera la misma que vino con [aar] a casa."
    call BlinkXS4("c31s004_085") from _call_BlinkXS4_1661
    bet "[mc] tiene razón. ¿Cuánto hace que te conocemos? ¿Tres semanas?"
    call BlinkXS4("c31s004_090") from _call_BlinkXS4_1662
    ama "Ayer hizo tres semanas que conocí a [mar] y a [nor]. Hoy hará tres semanas que conocí al resto. Secuestros aparte, claro."
    ama "Porque ya es mañana, ¿verdad?"
    mc "Sí, ya es mañana. Incluso en casa."
    call BlinkXS4("c31s004_095") from _call_BlinkXS4_1663
    bet "¿Te acuerdas de la chica que vino aquel día a cenar? Porque yo sí que me acuerdo."
    bet "Eras más tímida de lo que eres hoy. Más insegura. ¡Te dábamos miedo!"
    mc "A mí también me daría miedo conocer a una familia como la nuestra."
    call BlinkXS4("c31s004_100") from _call_BlinkXS4_1664
    mc "Pero ahora formas parte de ella. Has encontrado amigas nuevas. Hermanas. Una familia nueva que no sustituye tu familia anterior."
    "Después de lo que pasó con [eva], prefieres aclarar que aceptar la nueva familia no significa traicionar a la antigua."
    mc "Has crecido como persona. Como mujer."
    if ama._var("route"):
        mc "Incluso te has casado."
        call BlinkXS4("c31s004_105") from _call_BlinkXS4_1665
        ama "*Risa* No sé si eso es bueno o malo."
        mc "¡Hey!"
        call BlinkXS4("c31s004_110") from _call_BlinkXS4_1666
        bet "*Risa* No sabemos qué gusto tenías para los hombres antes, con lo que no podemos saber si has evolucionado para bien o para mal."
        mc "¡Hey! Estoy aquí. Lo sabéis, ¿verdad?"
        call BlinkXS4("c31s004_115") from _call_BlinkXS4_1667
        bet "A ver, si antes le gustaba Jason Moanoa y se ha acabado casando contigo..."
        mc "*Risa* Si a Jason le quitas la fama, el dinero, el pelo, la barba, y los músculos... ¿Qué tiene que no tenga yo?"
        scene c31s004_115d with dissolve
        bet "*Risa* Nada, nada..." (multiple=2)
        ama "*Risa* ¿Talento para actuar?" (multiple=2)
        mc "¡Paren este avión, quiero bajarme!"
        call BlinkXS4("c31s004_120") from _call_BlinkXS4_1668
        bet "Pero hablando en serio..."
        bet "Lo que quería decir [mc], aunque le guste darle muchas vueltas a todo, es que no eres la misma que conocimos hace tres semanas."
    else:
        call BlinkXS4("c31s004_120") from _call_BlinkXS4_1669
        bet "Lo que quiere decir [mc], aunque le guste darle muchas vueltas a todo, es que no eres la misma que conocimos hace tres semanas."
    bet "Ya no sois [eva] y tú contra el mundo. Ahora nos tenéis a nosotros también."
    bet "Nadie se mete con un Marks sin que 23 personas le salten al cuello."
    mc "Y si no, siempre podemos mandar a Jamaal a atropellarlo. Aunque salta poco."
    scene c31s004_125An with dissolve
    ama "No podría hacer esto sin vosotros. Gracias..."
    call BlinkXS4("c31s004_130") from _call_BlinkXS4_1670
    ama "Y sobre lo de atropellar a alguien... *Risita* Creo que cuando conozcáis a un tal [dam], un clon de la serie D, os entrarán ganas de hacerlo."
    alb "*Megafonía* Aterrizaremos en unos minutos. Recuerden abrocharse los cinturones."
    mc "Bueno, creo que el viaje de verdad empieza ahora. No es nada que no podamos hacer juntos."
    stop music fadeout (1.5)
    mc "Y si hay que atropellar al tal [dam], se le atropella."
    return
label c31s005_AarPicksUp:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_21
        call mrS3_bet_route from _call_mrS3_bet_route_14
    scene c31s005_005a with fade
    play music ("music/Krampus Workshop.ogg")
    "Una vez el avión aterriza, va directamente a lo que parece un hangar militar."
    "[aar] os está esperando con un coche dentro del hangar."
    scene c31s005_005g with dissolve
    pause (1.5)
    scene c31s005_005h with dissolve
    "A [ama] se le ilumina la cara al verlo por la ventanilla."
    scene c31s005_005An with dissolve
    "Y hace lo que nunca hubieras esperado de alguien como [ama]."
    "Por su cara de sorpresa, [aar] tampoco lo hubiera esperado nunca."
    call BlinkXS4("c31s005_010") from _call_BlinkXS4_1671
    ama "No tenías que haberte molestado en venir."
    aar "Era lo menos que podía hacer..."
    call BlinkXS4("c31s005_015") from _call_BlinkXS4_1672
    mc "[aar], es un placer verte en persona en vez de hacerlo a través de una pantalla."
    aar "Lo mismo digo, [mc]. Tenía ganas de traspasarte el trabajo de CEO."
    call BlinkXS4("c31s005_020") from _call_BlinkXS4_1673
    aar "*Susurrando* ¿Qué le habéis hecho a [ama]?"
    mc "*Risa* Enseñarle a mostrar lo que siente. Es un buen cambio."
    scene c31s005_025An with dissolve
    ama "Jeetje mina*! ¡[aar] es tu clon! \n* ¡Madre mía! en holandés."
    call BlinkXS4("c31s005_030") from _call_BlinkXS4_1674
    mc "Te dije que lo descubriría en el momento en que nos viera juntos."
    aar "Tenía que intentarlo."
    call BlinkXS4("c31s005_035") from _call_BlinkXS4_1675
    ama "¿Tú lo sabías? ¿Por qué no me dijiste nada?"
    mc "Se lo prometí a [aar]. Me dijo que quería contároslo él."
    call BlinkXS4("c31s005_040a") from _call_BlinkXS4_1676
    bet "Si por videoconferencia era obvio, solo un ciego no lo descubriría viéndoos juntos."
    mc "Ya, es lo que pensé."
    call BlinkXS4("c31s005_040b") from _call_BlinkXS4_1677
    ama "¿Tú también lo sabías? ¿[eva] también lo sabe? ¿Soy la única idiota que no lo sabía?"
    mc "No, [ama]. [eva] tampoco lo sabe. [aar] quería decíroslo en persona."
    call BlinkXS4("c31s005_045") from _call_BlinkXS4_1678
    aar "Creo que pequé un poco de ingenuo."
    mc "¿Sólo un poco?"
    call BlinkXS4("c31s005_050") from _call_BlinkXS4_1679
    ama "Bueno, sabíamos que eras el clon de alguien. No sabíamos de quién."
    ama "¿Cuándo lo descubriste? ¿Por qué no nos dijiste nada?"
    call BlinkXS4("c31s005_055") from _call_BlinkXS4_1680
    aar "Yo lo sé desde hace unos meses, cuando empezó la Guerra Clon. Pero no era el momento de decir nada."
    aar "Me extrañó que no dijerais nada el día que conocimos a [mar] y a [nor], con lo que pensé que no era demasiado obvio."
    call BlinkXS4("c31s005_060") from _call_BlinkXS4_1681
    aar "Hace años que no tengo tu aspecto, y no creo que las chicas lo recuerden."
    mc "Creo que tiene más que ver con lo impactadas que estaban por conocer a [mar] y a [nor]."
    mc "Me parece que no nos miraron más de un par de veces."
    call BlinkXS4("c31s005_065") from _call_BlinkXS4_1682
    ama "Supongo que debe ser eso. He tardado menos de un minuto en verlo ahora."
    mc "Es normal que no tuvieras más que ojos para [mar] y [nor] aquel día, cielo."
    call BlinkXS4("c31s005_070") from _call_BlinkXS4_1683
    if ama._var("route"):
        ama "*Risa* Al menos sé que mi marido no se va a quedar calvo."
        mc "*Risa* Eso también me da cierta alegría a mí."
        mc "Aunque yo sería un calvo orgulloso si pasara, de esos que se rapan al cero. Nada de pelucas para mí."
        call BlinkXS4("c31s005_075") from _call_BlinkXS4_1684
        aar "¿Qué? ¿Marido? ¿De qué va esto? ¿Es algún tipo de tapadera?"
        mc "Creo que [ama] tiene que explicarte algunas cosas, [aar]."
    else:
        ama "*Risa* Al menos sabes que no te vas a quedar calvo."
        mc "*Risa* Eso también me da cierta alegría a mí."
        mc "Aunque yo sería un calvo orgulloso si pasara, de esos que se rapan al cero. Nada de pelucas para mí."
    call BlinkXS4("c31s005_080") from _call_BlinkXS4_1685
    bet "¿Podemos hablar de calvicies y de todo lo que queráis de camino a la base?"
    bet "Es tarde y deberíamos descansar antes de empezar el día mañana."
    call BlinkXS4("c31s005_085") from _call_BlinkXS4_1686
    aar "No vais a dormir en la base. Os voy a llevar a la Casa del CEO."
    mc "Creía que la Casa del CEO estaba en la base..."
    call BlinkXS4("c31s005_090") from _call_BlinkXS4_1687
    aar "No. Ni Richards ni Daniels quisieron nunca vivir en la base. La casa está a unos quince kilómetros. Unas diez millas para vosotros."
    mc "¿Tú también vives ahí? Has sido CEO en funciones..."
    aar "Yo vivo en la base, con el resto de los chicos. Nada ha cambiado respecto a eso."
    call BlinkXS4("c31s005_095") from _call_BlinkXS4_1688
    aar "Por cierto... bienvenida, [bet]. No me han dejado saludarte."
    mc "Ve preparando la expresión de sorpresa, [aar]."
    scene c31s005_095d with dissolve
    aar "¿A qué te refieres?"
    scene c31s005_100a with hpunch
    call BlinkXS4("c31s005_100") from _call_BlinkXS4_1689 #aar sorprendido, mirándote y abriendo y cerrando la boca
    bet "¿Qué es eso de extender la mano? Eres el clon de mi sobrino-nieto. ¡Eres familia!"
    "[aar] entiende a qué te referías un segundo demasiado tarde."
    mc "*Risa* Me refería a eso, [aar]."
    mc "Y [aar] no cree que seamos familia por compartir genes, {b}Tía{/b} [bet]."
    "Remarcas el 'Tía' para dejar claro que sois familia."
    bet "¡Tonterías!"
    if not persistent.family:
        "Da lo mismo que [bet] y tú no compartáis genes. Sois familia porque elegís serlo."
    if ama._var("route") and bet._var("route"):
        "También esperas que, remarcando el 'Tía', [bet] no diga nada sobre que vosotros también estáis casados."
        "No quieres que a [aar] le explote la cabeza nada más veros. No sabrías llegar a la Casa del CEO. ¿Quizás [ama] lo sepa?"
    call BlinkXS4("c31s005_105") from _call_BlinkXS4_1690
    "Tras unos incómodos segundos para [aar], [bet] le suelta y da un par de pasos atrás."
    bet "Bueno, ya hemos hecho las presentaciones. La próxima vez espero que me devuelvas el abrazo, [aar]."
    mc "Deja que su cerebro vuelva a funcionar antes de exigirle cosas para la próxima vez."
    call BlinkXS4("c31s005_110") from _call_BlinkXS4_1691
    aar "¿Qué? ¿Va a haber próxima vez?"
    "El duro mercenario parece ridículo, incomodado por los abrazos de una anciana."
    mc "*Risa* No sabes nada, [aar] Gilford."
    call BlinkXS4("c31s005_115") from _call_BlinkXS4_1692
    ama "Eso es de una serie de la TV, [aar]."
    ama "Y sí. Va a haber un montón de próximas veces. Ya te acostumbrarás."
    ama "Los Marks somos una familia de abrazadores. Los Gilford deberíamos aprender mucho de los Marks."
    "Te encanta que se incluya en las dos familias en una sola frase."
    mc "Y ahora creo que nos deberíamos ir antes de que a [aar] le dé una apoplejía."
    scene c31s005_120a with fade
    "Tras despediros de [alb] y de los pilotos, subís a la limusina y emprendéis el viaje a la que va a ser tu casa durante los próximos meses."
    "[aar] actúa de chófer mientras [ama] se sienta a su lado y le explica todo lo que ha pasado desde que él volvió a Aruba."
    "Las palabras y la emoción de la hermosa mujer resuenan en las calles vacías, iluminando la noche con su sonrisa."
    "Ella no habla de misiones o de dispositivos de vigilancia. Habla de familia. Explica risas y abrazos. Habla de las chicas y de Jamaal."
    if ama._var("route"):
        "Habla de vuestra boda."
    "[bet] y tú sólo intervenís cuando [ama] se deja algún detalle que consideráis importante."
    "Ninguno de los dos queréis interrumpir la ilusión con la que la mercenaria está explicando su nueva vida."
    "La [ama] que casi te rompe el brazo en el avión ha desaparecido de nuevo, aunque sabes que aún está ahí dentro."
    "[aar] sobrevive al viaje sin apoplejías ni infartos de corazón. A duras penas."
    stop music fadeout (1.5)
    "Lo cual es una suerte. Él es quien conduce."
    return
label c31s005_houseArrival:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_22
    scene c31s005_150a with fade
    play music ("music/Inspiring-Upbeat-Ambient.ogg")
    "Llegáis a la Casa del CEO cerca de las 4 AM. Hay un par de coches en el garaje, aparte de la limusina en la que llegáis."
    "Habías visto fotos del interior, pero algo no te cuadra. Lo que has visto en las fotos no cabe en ese edificio."
    call BlinkXS4("c31s005_155") from _call_BlinkXS4_1693
    bet "Creía que sería más grande..."
    bet "Sin ánimo de ofender, pero parece una choza y un edificio pequeño."
    bet "No es que me queje. La terraza en la choza parece impresionante y he vivido en sitios peores."
    call BlinkXS4("c31s005_160") from _call_BlinkXS4_1694
    aar "El nombre oficial es Una Casa en el Acantilado. Hay dos plantas por debajo de lo que veis."
    aar "Esto sólo es la cocina, el salón y la terraza. En la siguiente planta están las habitaciones."
    mc "¿Y en la tercera planta?"
    call BlinkXS4("c31s005_165") from _call_BlinkXS4_1695
    aar "La habitación del pánico. Oficialmente llamada El Bunker."
    aar "Hay comunicaciones seguras con la base desde esa habitación, en caso de ataque o de querer seguir alguna operación desde aquí."
    aar "También hay una pequeña armería y la sala de vigilancia."
    mc "¿Tenemos personal de seguridad?"
    call BlinkXS4("c31s005_170") from _call_BlinkXS4_1696
    ama "No. Le dije a [aar] que no era necesario para esta noche."
    ama "Nadie sabe que veníamos y la casa lleva algunas semanas vacía, con lo que no esperamos necesitarlo."
    call BlinkXS4("c31s005_175") from _call_BlinkXS4_1697
    ama "Además, no quería que te cruzaras con ningún operativo hasta que no sepamos qué esperar de cada uno de ellos."
    mc "Me parece muy inteligente."
    call BlinkXS4("c31s005_180") from _call_BlinkXS4_1698
    aar "Ahora deberíais descansar. Mañana vais a tener un día muy largo."
    mc "Creo que tienes razón. ¿Nos vemos mañana en la base?"
    call BlinkXS4("c31s005_185") from _call_BlinkXS4_1699
    aar "Sí, la primera reunión la tienes a las 10 AM, con los jefes de departamento. Yo también estaré allí."
    aar "Pero antes tienes agendado que te enseñen las instalaciones, con lo que deberías estar allí sobre las 8 AM."
    mc "Perfecto. Nos vemos allí entonces."
    scene c31s005_190An with dissolve
    "Tanto [bet] como [ama] se despiden de [aar] con un abrazo después de que os ayude a meter el equipaje en la cocina."
    "A este paso, se va a acostumbrar muy rápido a los abrazos de los Marks, aunque no quiera formar parte de la familia."
    "Sólo hace falta que [eva] y un par más de las chicas vengan y lo abracen... No le quedará más remedio que cambiar de opinión."
    "De alguna forma es tu hermano también."
    "Se va conduciendo la limusina. Por un momento has pensado que dejaría la limusina y cogería el Humvee."
    scene c31s005_195a with fade
    call BlinkXS4("c31s005_195") from _call_BlinkXS4_1700
    ama "Creo que deberíamos ir a dormir ya. Os enseño vuestras habitaciones."
    mc "¿Habías estado aquí antes?"
    call BlinkXS4("c31s005_200") from _call_BlinkXS4_1701
    ama "Nunca, pero sé mirar un plano y puedo guiaros a las habitaciones que [aar] os ha asignado."
    ama "Ni Richards ni Daniels querían que las chicas formáramos parte del equipo de seguridad de la mansión."
    mc "¿Había alguna razón para eso?"
    call BlinkXS4("c31s005_205") from _call_BlinkXS4_1702
    ama "Decían que podíamos hacer cosas más interesantes que mirar un monitor."
    mc "Y tenían razón. Pese a ello te has pasado los últimos meses haciéndolo."
    call BlinkXS4("c31s005_210") from _call_BlinkXS4_1703
    ama "*Risa* Y si no fuera por [emm] y [kat]... bueno, y por el resto... hubiera sido muy aburrido."
    mc "No te voy a quitar la razón en eso."
    call BlinkXS4("c31s005_215") from _call_BlinkXS4_1704
    bet "Chicos, os recuerdo que son más de las 4. Tenemos que dormir algo si mañana tenemos que estar en la base a las 8."
    mc "¿Vas a dormir más? ¡Te has pasado casi todo el vuelo durmiendo!"
    call BlinkXS4("c31s005_220") from _call_BlinkXS4_1705
    bet "*Risa* A mi edad, una chica necesita su sueño reparador."
    call BlinkXS4("c31s005_225") from _call_BlinkXS4_1706
    ama "Dejad las maletas grandes en la cocina. Mañana lo recogeremos todo. Hoy es tarde para ponerse a deshacer maletas."
    ama "Coged lo imprescindible para pasar la noche."
    mc "El neceser y poco más."
    scene c31s005_230d with dissolve
    "[ama] acompaña primero a [bet] a su habitación, antes de guiarte a la tuya."
    "Es justo como en las fotos que habías visto, con unas espectaculares vistas del Caribe."
    call BlinkXS4("c31s005_230") from _call_BlinkXS4_1707
    ama "Esta es la habitación principal. Ahí tienes el baño y ahí unas escaleras para bajar a la habitación del pánico."
    mc "Espero no tener que usarlas nunca."
    ama "Yo también. La casa nunca ha recibido un ataque, con lo que esa habitación sólo se ha usado como centro de mando y vigilancia."
    if ama._var("route"):
        call KissXS4("c31s005_235") from _call_KissXS4_28
    call BlinkXS4("c31s005_235") from _call_BlinkXS4_1708
    ama "Buenas noches, [mc]. Te veo mañana... O en unas dos horas y media."
    mc "Buenas noches, cielo. Descansa."
    scene c31s005_240d with dissolve
    mc "[ama]..."
    call BlinkXS4("c31s005_240") from _call_BlinkXS4_1709
    ama "¿Sí...?"
    mc "¿Vas a estar bien? Si quieres quedarte a dormir, esa cama es grande."
    call BlinkXS4("c31s005_245") from _call_BlinkXS4_1710
    ama "No te preocupes por mí. Estaré bien. Pero gracias de todos modos."
    mc "Si me necesitas, sabes dónde vivo."
    stop music fadeout (1.5)
    ama "Lo tendré en cuenta. Descansa."
    scene c31s005_250a with fade
    "Te desnudas y te aseas. Te dejas los boxers puestos por si una de las dos mujeres quiere hacer su aparición en la habitación."
    "No tienes sueño después del rato que has dormido en el avión."
    mcp "(Mañana va a ser un día interesante.)"
    scene c31s005_250b with fade
    play music ("music/Beach.ogg")
    "Te sirves un zumo de piña y sales al balcón de la habitación."
    "El Caribe brilla bajo las estrellas."
    "Si no has perdido el sentido de la orientación, crees que este balcón da al Este, con lo que te despertará el sol cuando salga."
    scene c31s005_250d with dissolve
    "Sólo te puedes imaginar cómo se vería la casa desde una barca en el mar."
    "Seguramente ahora es una masa oscura contra el cielo. Tienes que verla de día."
    mcp "(Debería irme a dormir. No daría muy buena impresión si el CEO se duerme en las reuniones de su primer día.)"
    stop music fadeout (1.5)
    scene c31s005_250c with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/1000lichter.ogg")
    "Unos nudillos te sacan de tus ensoñaciones. Hay costumbres que nunca cambian, aunque cambies de país."
    ama "*A través de la puerta* Soy yo. ¿Puedo pasar?"
    mc "Sí, entra."
    call BlinkXS4("c31s005_255") from _call_BlinkXS4_1711
    mc "¿Te has olvidado algo?"
    ama "Aceptar tu oferta de quedarme a dormir."
    ama "He visto luz en tu balcón y..."
    mc "No tienes que darme explicaciones para aceptar una oferta que te he hecho yo."
    call BlinkXS4("c31s005_260") from _call_BlinkXS4_1712 #abrazo
    ama "Esto va a ser muy duro..."
    mc "Nada que no podamos superar juntos, [ama]."
    mc "Y has sobrevivido a la habitación de [emm] sin arrancarte los ojos."
    mc "No creo que unos clones vayan a poder contigo."
    call BlinkXS4("c31s005_265") from _call_BlinkXS4_1713
    ama "El problema no van a ser los clones... O al menos no van a ser el problema principal."
    ama "No sé cómo el resto del personal va a tomarse los cambios que queremos hacer en la empresa."
    mc "Yo tampoco, pero ¿sabes una cosa?"
    call BlinkXS4("c31s005_270") from _call_BlinkXS4_1714
    ama "¿Qué?"
    mc "Es algo que empezaremos a descubrir mañana. No nos preocupemos hoy."
    if ama._var("route"):
        mc "Hoy lo único que quiero es dormir con mi esposa. Aunque sólo sean dos horas y media."
        call BlinkXS4("c31s005_275") from _call_BlinkXS4_1715
        ama "Dos horas y cuarto. Pero solo va a ser dormir..."
        mc "Sí, no te preocupes. No quiero que nuestra primera vez sea así, ni tan rápido."
    mc "Además, hoy estamos cansados del viaje."
    call BlinkXS4("c31s005_280") from _call_BlinkXS4_1716
    ama "Tienes razón. Y no. No te voy a comprar esa camiseta."
    mc "*Risa* Creo que al final la tendré que encargar online."
    if ama._var("route"):
        call KissXS4("c31s005_285") from _call_KissXS4_29
    call BlinkXS4("c31s005_285") from _call_BlinkXS4_1717
    ama "Entonces, vamos a la cama."
    mc "Después de ti."
    scene c31s005_285e with fade
    ama "Por cierto... Había oído que dormías desnudo. No sé si sentirme decepcionada."
    mc "Es algo que puedo solucionar, si quieres."
    ama "*Risa* Me parece que no quiero."
    if ama._var("route"):
        ama "Al menos hoy."
    ama "Recuerda que tuvimos cámaras en tu habitación. Ya he visto todo lo que había que ver."
    mc "Cambiando de tema, me encanta el camisón de Zeus."
    ama "Lo compré antes de conocerlo, con lo que solo era un camisón con un montón de gatos."
    mc "¿Vas a tardar mucho en acostarte?"
    ama "No..."
    scene c31s005_285f with fade
    "Finalmente, [ama] decide apagar las luces y meterse en la cama contigo."
    "Nada más acomodaros en brazos del otro, caéis dormidos como troncos bajo la luz de la luna que se filtra por el ventanal."
    "El día ha sido más largo de lo que ninguno esperabais y el cansancio ha hecho mella en vosotros."
    stop music fadeout (1.5)
    if ama._var("route"):
        "Duermes con tu esposa por primera vez. Aunque sean poco más de dos horas."
        "Vas a tener un mes para dormir con ella un montón de noches."
    return
label c31s006_Caroline:
    scene c31s006_700a with fade
    call BlinkXS4("c31s006_700") from _call_BlinkXS4_1718
    play music ("music/Clear-Air.ogg")
    "Después de desayunar, [ama] os lleva hasta la base. Está a menos de 30 minutos de la casa."
    ama "Bueno, ya estamos aquí. Esta es la base principal de NTR."
    mc "Es impresionante. Aunque parece una fábrica más que lo que imaginas como una base militar."
    call BlinkXS4("c31s006_705") from _call_BlinkXS4_1719
    bet "Ha actuado como fábrica de clones, de muerte, y de infelicidad durante mucho tiempo."
    mc "Tienes razón..."
    call BlinkXS4("c31s006_710") from _call_BlinkXS4_1720
    ama "Vamos a empezar la visita por la persona más importante con quién tendrás que lidiar en los próximos meses."
    mc "¿[mael], el Jefe del Departamento Científico? ¿O [vin], de Contabilidad? Creía que teníamos una reunión con ellos después."
    call BlinkXS4("c31s006_715") from _call_BlinkXS4_1721
    ama "[car], tu secretaria."
    "Ese dedo índice señalando al cielo es una postura tan Marks... No llevas un día aquí y ya estás echando de menos a la familia."
    mc "Eso no me lo esperaba. He leído su ficha... Era la secretaria de Daniels... Y de Richards antes que él."
    mc "Y la de Tío Mike. Lleva aquí desde que la empresa se mudó a Aruba."
    ama "Es leal a la empresa, no al CEO de turno. Si te la ganas, será de gran ayuda para ti."
    ama "No podrás hacer que esto funcione sin su ayuda. Conoce todo y a todos."
    ama "Y que no te engañe su aspecto. Podría masticar balas, si quisiera."
    call BlinkXS4("c31s006_720") from _call_BlinkXS4_1722
    bet "Una secretaria puede hacerte la vida muy fácil o muy difícil."
    bet "Creo que [ama] tiene razón en que sea la primera persona que conozcas."
    bet "Y recuerda, las primeras impresiones son importantes. No la cagues."
    mc "*Risa* Me tranquiliza la confianza que depositáis en mí."
    mc "Vamos a conocer a la temible [car]."
    scene c31s006_720d with fade
    ama "Caroline, te presento a [mc] Marks. El nuevo CEO."
    ama "También ha venido [bet] Cavendish, la cirujana que va a operar a [gav]."
    car "Encantada de conocerlos. Espero que la casa estuviera a su gusto, Sr. Marks."
    mc "Igualmente, [car]."
    mc "La casa es impresionante, gracias."
    call BlinkXS4("c31s006_725") from _call_BlinkXS4_1723
    car "Hoy tiene una agenda apretada, Sr. Marks."
    mc "Llámame [mc], por favor."
    car "Lo primero es la visita turística a las instalaciones principales de la base."
    call BlinkXS4("c31s006_730") from _call_BlinkXS4_1724
    bet "*Risa* Lo de 'visita turística' ha sonado gracioso, [car]."
    call BlinkXS4("c31s006_735") from _call_BlinkXS4_1725
    car "Es la primera vez que tenemos que enseñarle la base a un CEO. Hasta ahora, los CEOs anteriores habían ascendido desde las filas de la empresa."
    car "Se habían ganado el derecho a estar aquí después de años de servicio."
    mc "Espero poder ganarme ese derecho."
    call BlinkXS4("c31s006_740") from _call_BlinkXS4_1726
    car "Yo también lo espero, Sr. Marks."
    car "Ha habido un problema con David, el operativo que tenía que hacer su visita."
    scene c31s006_740d with dissolve
    ama "¿Está bien?"
    car "Tan solo un esguince en el tobillo. Estoy esperando que [aar] me diga quién lo va a sustituir en la visita."
    scene c31s006_740e with dissolve
    ama "No te preocupes por eso. Dile a [aar] que yo voy a enseñarle la base a [mc]."
    car "Me parece una buena solución. Si tenemos que esperar a [aar], seguramente tendríamos que reducir la duración de visita."
    mc "Entonces un problema arreglado. ¿Algo más?"
    call BlinkXS4("c31s006_745") from _call_BlinkXS4_1727
    car "Después de la visita, tiene la reunión con los jefes de departamento. En dos horas."
    mc "Bien, [car]."
    scene c31s006_750An with dissolve
    play sound ("music/Bam-bam-baa.ogg")
    bet "Bam Bam Baa."
    scene c31s006_755d with dissolve #car la mira mal
    car "..."
    call BlinkXS4("c31s006_755") from _call_BlinkXS4_1728
    car "Después tiene una reunión con Soporte Informático, donde le harán una pequeña formación sobre el software de la empresa."
    car "Y, cuando tenga un momento, le tengo que dar el Manual del Empleado, donde encontrará toda la información que necesite."
    car "He dejado espacio suficiente entre ambas reuniones para que no vaya estresado de tiempo en su primer día."
    mc "Gracias, [car]."
    scene c31s006_760d with dissolve #Mira a [bet] que pone cara de inocente
    pause (1.5)
    call BlinkXS4("c31s006_760") from _call_BlinkXS4_1729
    car "Por la tarde, tiene una reunión con [aar]. Le dará un informe {b}{u}exhaustivo{/u}{/b} sobre su gestión estos días."
    mc "Eso suena a que tú también has sufrido los informes de [aar]."
    call BlinkXS4("c31s006_765") from _call_BlinkXS4_1730
    car "Los informes ejecutivos deberían ser concisos, Sr. Marks."
    mc "[mc]."
    car "Usted no va a tener tiempo para preocuparse de si el stock de munición va a durar nueve meses o nueve meses y dos días."
    mc "Estoy de acuerdo."
    call BlinkXS4("c31s006_770") from _call_BlinkXS4_1731
    car "Deberían irse ahora si no quieren recortar la visita. Hablaremos después cuando acabe la primera reunión."
    mc "Perfecto, [car]."
    scene c31s006_770d with fade
    mc "[bet], creo que has olvidado lo de la primera impresión."
    bet "No lo he olvidado. Pero, desde que he oído su nombre, tengo esa canción en la cabeza."
    bet "Y si se centra en la tía excéntrica del CEO, tu parecerás mejor en comparación."
    ama "No sé de qué canción estáis hablando ni he entendido tu gesto, Tía [bet]."
    scene c31s006_770e with dissolve
    bet "Hay que empezar a trabajar en tu educación musical, mi niña. ¡Es un clásico del 69!"
    ama "Ya habrá tiempo para eso. Ahora deberíamos empezar la visita."
    stop music fadeout (1.5)
    mc "Cuando quieras. Creo que yo me hubiera perdido un par de veces a estas alturas."
    return
label c31s006_cloneMeeting:
    scene c31s006_005a with fade
    play music ("music/Exciting Trailer.ogg")
    "Más tarde, de nuevo en la sala de reuniones y después de las presentaciones..."
    mc "Gracias a todos por venir con tan poca antelación. Sé que esto es nuevo para muchos de vosotros."
    mc "Lo primero es presentarme. Soy [mc] Marks y actúo como el nuevo CEO. Esto es tan nuevo para mí como para vosotros."
    mc "Mi intención es escucharos. Tenéis la palabra para plantear lo que necesitéis."
    call BlinkXS4("c31s006_010") from _call_BlinkXS4_1521
    aar "Apreciamos el gesto, [mc]. Los chicos llevan tiempo queriendo hablar con la dirección. Nunca antes se les había dado esta oportunidad."
    call BlinkXS4("c31s006_015") from _call_BlinkXS4_1522
    ama "[mc] ha querido que esta reunión sea abierta y sin filtros. Podéis hablar con libertad."
    ama "[mc] es... diferente de la anterior dirección."
    call BlinkXS4("c31s006_020") from _call_BlinkXS4_1523
    dam "¿En serio? ¿Podemos pedir lo que queramos?"
    dam "Porque yo tengo una lista bastante interesante..."
    call BlinkXS4("c31s006_025") from _call_BlinkXS4_1524
    gav "[dam], por favor. Empecemos por lo importante. Consensuamos una serie de puntos ayer."
    call BlinkXS4("c31s006_030") from _call_BlinkXS4_1525
    fred "[gav] tiene razón. Hay cosas urgentes sobre la mesa."
    call BlinkXS4("c31s006_035") from _call_BlinkXS4_1526
    carl "He preparado un resumen de las peticiones que acordamos en la reunión previa."
    carl "Si os parece, las voy repasando una a una."
    mc "Adelante, Carl."
    call BlinkXS4("c31s006_040") from _call_BlinkXS4_1527
    carl "La primera petición es de índole personal. Los operativos quieren poder llevar barba, o cambiar su corte de pelo. El reglamento actual lo prohíbe."
    carl "[aar] es el único operativo que verás con barba en la base, y eso es porque se la dejó crecer mientras estaba... fuera de servicio."
    call BlinkXS4("c31s006_045") from _call_BlinkXS4_1528
    dam "Llevo dos años queriendo dejarme la barba. ¡Dos años!"
    call BlinkXS4("c31s006_050") from _call_BlinkXS4_1529
    gav "Es una cuestión de identidad. Para nosotros... significa más de lo que parece."
    mc "Entiendo. ¿Hay alguna razón operativa para mantener esa restricción, [ama]?"
    call BlinkXS4("c31s006_055") from _call_BlinkXS4_1530
    ama "Ninguna que yo vea. En algunas misiones de infiltración puede ser relevante, pero eso se puede gestionar caso por caso."
    ama "Siempre y cuando no interfiera con el equipo... máscaras de gas, cascos, visores nocturnos... no veo ningún problema."
    mc "De acuerdo. A partir de ahora, cada operativo puede llevar el estilo personal que prefiera."
    mc "Si hay una misión que requiera un aspecto concreto, se os comunicará con antelación."
    scene c31s006_005b with dissolve
    gav "Gracias, [mc]. De verdad."
    fred "Era lo mínimo, pero se agradece."
    dam "¡Por fin! Voy a dejarme unas patillas épicas."
    aar "[dam]..."
    scene c31s006_005c with dissolve #(todos se llevan las manos a la cabeza)
    dam "¿Qué? ¡Es legítimo!"
    scene c31s006_005d with dissolve
    "Carl decide ignorar a su compañero y seguir con las peticiones."
    carl "La segunda petición es más delicada. Se trata de Eric."
    fred "Eric está retenido desde hace un mes, acusado de traición."
    dam "Nunca me cayó bien... Nadie de la E me caía bien, pero es injusto."
    aar "Actuó contra los propietarios de la empresa, sí. Pero hay contexto."
    mc "Lo sé. Estuve revisando el expediente. Seguía órdenes de Daniels. Era su superior..."
    call BlinkXS4("c31s006_060") from _call_BlinkXS4_1531
    ama "Un superior que ahora también está bajo arresto, dicho sea de paso."
    ama "Un superior que ordenó los asesinatos de mis hermanas, de los A y de tu familia."
    call BlinkXS4("c31s006_065") from _call_BlinkXS4_1532
    gav "Nadie dice que Eric sea buena gente ni mucho menos. Pero estaba atrapado entre dos fuegos. No tenía elección real."
    call BlinkXS4("c31s006_070") from _call_BlinkXS4_1533
    fred "Nosotros tampoco la teníamos, en aquellos tiempos. Hacíamos lo que nos mandaban... O había consecuencias."
    fred "Yo estuve en la otra operación en ese momento... Íbamos engañados y, si Eric debe estar arrestado, también lo deberíamos estar [gav] o yo."
    mc "Soy consciente de eso. La estructura anterior no dejaba margen para la desobediencia."
    call BlinkXS4("c31s006_075") from _call_BlinkXS4_1534
    fred "Lo siento, [ama]..."
    "[ama] no se molesta en contestar. Beatrice y Diana murieron a manos del grupo al que pertenecía [fred]."
    call BlinkXS4("c31s006_080") from _call_BlinkXS4_1535
    dam "Eric no es un traidor. Es alguien que sobrevivió como pudo. Se mantuvo fiel a quién estaba al mando en ese momento."
    call BlinkXS4("c31s006_085") from _call_BlinkXS4_1536
    carl "La petición formal es su liberación inmediata y la retirada de los cargos."
    mc "No voy a tomar esa decisión hoy a la ligera. Necesito revisar el caso completo."
    mc "Pero os doy mi palabra de que lo estudiaré personalmente. Eric tendrá una revisión justa."
    carl "Con eso nos conformamos. Por ahora, señor."
    "Ese 'señor' al final de la frase suena casi a un desafío a que no cumplas tu palabra."
    call BlinkXS4("c31s006_090") from _call_BlinkXS4_1537
    carl "Tercera petición: los operativos solicitan un régimen de permisos para salir de la base."
    carl "Actualmente no pueden abandonar el perímetro sin una misión activa."
    scene c31s006_090d with dissolve
    fred "Llevamos años sin poder ir a un bar, a un cine, a ver a nadie."
    dam "Sin poder ligar, vamos a lo importante."
    gav "Sin poder respirar aire que no sea este."
    aar "Es una de las restricciones más duras. Los mantiene aislados del mundo."
    mc "¿Eso es literal? ¿No podéis salir en ningún caso?"
    call BlinkXS4("c31s006_095") from _call_BlinkXS4_1538
    ama "Era la norma, sí. Control total de movimientos."
    mc "Eso es... inaceptable. No sois prisioneros."
    call BlinkXS4("c31s006_100") from _call_BlinkXS4_1539
    fred "Durante años nos trataron como si lo fuéramos."
    mc "Eso se acabó. Vamos a establecer un sistema de permisos inmediatamente."
    mc "Salidas individuales con preaviso razonable. Nada de pedir permiso como si fuerais niños."
    scene c31s006_100d with dissolve
    gav "¿En serio?"
    mc "En serio. Ya no sois esclavos. Nunca debisteis serlo."
    aar "Eso... significa mucho, [mc]. Más de lo que imaginas."
    dam "¡Sí! ¡Libertad! ¡Primera parada: cualquier sitio que no sea aquí!"
    fred "Gracias, [mc]."
    scene c31s006_100e with dissolve
    "Hay un silencio breve en la sala. Varios de los clones intercambian miradas."
    "Aún no los conoces lo suficiente como para interpretar esas miradas, pero detectas un componente de esperanza."
    call BlinkXS4("c31s006_105") from _call_BlinkXS4_1540
    carl "La cuarta petición está relacionada con [gav]."
    carl "Los operativos quieren que todos los que perdieron extremidades o sufrieron heridas graves reciban el mismo tratamiento que se ha aprobado para [gav]."
    carl "Dentro de lo posible y de la disponibilidad de prótesis y otros dispositivos, claro."
    call BlinkXS4("c31s006_110") from _call_BlinkXS4_1541
    gav "No me parece justo que yo tenga esta oportunidad y los demás no. Hay varios chicos más con amputaciones. Y otros con daños permanentes."
    mc "¿Cuántos operativos están en esa situación?"
    call BlinkXS4("c31s006_115") from _call_BlinkXS4_1542
    aar "Con amputaciones, 19 contando a [gav]. [gav] es el más... reciente. Y el único para quien tenemos preparada una prótesis."
    aar "Se estaba trabajando en la que va a ser su prótesis antes del... incidente."
    aar "Con secuelas permanentes graves, otros seis o siete."
    aar "[carl] entraría en esta categoría por su ojo, por ejemplo, pero no tenemos ningún dispositivo que le pueda ayudar."
    call BlinkXS4("c31s006_120") from _call_BlinkXS4_1543
    ama "Las prótesis de alta gama no crecen en los árboles. Habría que estudiar el coste del desarrollo."
    ama "Ni siquiera sé lo que tenemos disponible, aparte del brazo de [gav]."
    mc "Lo sé. Pero es lo correcto. No puedo mirar hacia otro lado."
    mc "No os prometo que sea inmediato, pero está en mi lista de prioridades reales."
    mc "Hablaré con Caleb. Si pudo hacer el prototipo en su tiempo libre..."
    scene c31s006_120d with dissolve
    fred "Con eso nos vale por ahora."
    gav "Gracias, [mc]. Por todos ellos."
    dam "Oye, y si me ponen una prótesis de brazo aunque tenga los dos..."
    dam "¿Tendría tres brazos? Pregunto por curiosidad científica."
    scene c31s006_120e with dissolve
    carl "[dam]..."
    dam "Era broma. Mayormente."
    call BlinkXS4("c31s006_125") from _call_BlinkXS4_1544
    carl "Quinta petición: Salario. Los operativos consideran que la compensación no refleja el riesgo ni la naturaleza de su trabajo."
    "En ese momento descubres qué hay raro cada vez que [carl] habla."
    "Nunca dice 'nosotros' o 'los clones'. Siempre habla de 'los operativos', como si quisiera distanciarse emocionalmente de las peticiones."
    call BlinkXS4("c31s006_130") from _call_BlinkXS4_1545
    fred "Llevamos años sin ningún ingreso... Tan solo dos cosas: manutención y vivienda."
    fred "Has dicho que no somos esclavos. Pero eso se parece mucho a la esclavitud. Sin un sueldo, lo seguiremos siendo."
    mc "Es una petición razonable. No voy a decir que no."
    mc "Pero necesito sentarme a revisar los números antes de comprometer cifras concretas."
    call BlinkXS4("c31s006_135") from _call_BlinkXS4_1546
    ama "Las finanzas de NTR no están en su mejor momento tras los últimos meses, [fred]."
    mc "Aun así, esto tiene que cambiar. La empresa os lo debe."
    scene c31s006_135d with dissolve
    gav "Nadie espera que lo soluciones hoy, [mc]."
    dam "Yo sí, un poco."
    fred "[dam]..."
    dam "Estoy de broma. Más o menos."
    dam "Pero creo que un aumento del 40%% estaría bien."
    scene c31s006_135e with dissolve
    gav  "Te das cuenta de que un 40%% de cero sigue siendo cero, ¿verdad?"
    fred "¿No había otro D que pudiera venir a esta reunión?"
    carl "Los D... No hay mucho donde elegir..."
    dam "¡Hey! Somos los mejores..."
    aar "Sí, en decir gilipolleces."
    mc "Tened paciencia. Pero sabed que lo tomo en serio."
    call BlinkXS4("c31s006_140") from _call_BlinkXS4_1547
    dam "Hablando de compensaciones... yo tenía otra petición que creo que no llegó al orden del día."
    dam "¿Qué hay de coches deportivos? Uno para cada operativo. Al menos para los que somos suficientemente mayores para conducir..."
    call BlinkXS4("c31s006_145") from _call_BlinkXS4_1548
    carl "[dam], eso ya lo discutimos en la reunión anterior. Lo descartamos en los primeros cinco minutos."
    scene c31s006_145d with dissolve
    dam "Sí, pero parece que [mc] está abierto a cosas que creíamos que rechazaría. Igual él lo ve diferente."
    carl "Lo verá igual que nosotros. Es una petición absurda. Ya ha puesto la excusa de los fondos..."
    dam "¡Es una petición legítima de bienestar del empleado!"
    carl "Un Ferrarini no es bienestar del empleado, [dam]."
    dam "¿Y tú qué sabes? ¿Has probado a conducir un Ferrarini?"
    gav "[dam], por favor..."
    mc "Aprecio el entusiasmo, [dam]. Pero creo que podemos centrar el presupuesto en otras cosas."
    scene c31s006_145e with dissolve
    ama "Cosas mucho más urgentes."
    dam "Bien. Pero que conste en acta que lo intenté."
    aar "Consta, consta. No te preocupes. También voy a hacer constar que eres idiota."
    call BlinkXS4("c31s006_150") from _call_BlinkXS4_1549
    carl "Volviendo a los salarios. La petición incluye que el salario, si se aprueba, sea retroactivo. Varios años atrás."
    call BlinkXS4("c31s006_155") from _call_BlinkXS4_1550
    fred "Llevamos mucho tiempo trabajando sin cobrar lo que merecíamos. Es una deuda real. Y no solo económica."
    fred "Que nos empecéis a pagar ahora no resolverá la injusticia histórica."
    mc "Entiendo la lógica. Y tenéis razón. Moralmente y legalmente."
    mc "El problema es que ahora mismo no hay fondos suficientes para asumir esa cantidad."
    scene c31s006_155d with dissolve
    gav "¿De cuánto estamos hablando?"
    ama "Con los años acumulados y el número de operativos, sería una cifra muy considerable."
    fred "Lo sabemos. Pero eso no hace que la deuda desaparezca."
    dam "Claro que no. Trabajamos. Arriesgamos la vida. Merecemos que se nos reconozca."
    mc "Tenéis razón. Completamente. Pero si prometo algo que no puedo cumplir, os estaré fallando igual que la dirección anterior."
    mc "Necesito estudiar cómo compensaros de otra forma."
    call BlinkXS4("c31s006_160") from _call_BlinkXS4_1551
    fred "¿De qué forma?"
    mc "Aún no lo sé. Pero lo buscaré. Os lo prometo."
    call BlinkXS4("c31s006_165") from _call_BlinkXS4_1552
    carl "Con todo el respeto, [mc], hemos escuchado promesas antes."
    mc "Lo sé, [carl]. Y entiendo que esas promesas ya no valen mucho para vosotros."
    mc "Solo puedo pediros tiempo y demostrarlo con hechos."
    call BlinkXS4("c31s006_170a") from _call_BlinkXS4_1553
    gav "Escuchadme un momento. Llevamos media hora en esta reunión."
    gav "Estamos hablando de las promesas que se nos hicieron y no se cumplieron. Y la mejor de esas promesas fue mejorar el rancho."
    call BlinkXS4("c31s006_170b") from _call_BlinkXS4_1554
    gav "[mc] ha dicho que sí a la barba y a los permisos. Se ha comprometido a estudiar lo de Eric, a las prótesis y a los salarios."
    gav "Daniels no nos dejaba ni entrar a esta sala. Y Richards, antes de él, no era mucho mejor en esto."
    gav "Démosle el beneficio de la duda. Al menos durante un tiempo..."
    scene c31s006_170d with dissolve
    fred "Es verdad. Tienes razón."
    dam "Tú vas a tener un brazo nuevo y te ha prometido llevarte con él a los Estados Unidos. Es normal que le apoyes..."
    carl "No creo que el apoyo de [gav] tenga nada que ver con eso."
    call BlinkXS4("c31s006_180") from _call_BlinkXS4_1555
    gav "No tiene nada que ver con eso, [dam]. Te lo prometo. Yo estaba allí cuando... lo de Eric. Daniels nunca hubiera actuado como actuó [mc]."
    gav "Seguramente hubiera ordenado a [ama] y a [eva] que nos ejecutaran a todos."
    mcp "(En aquella época ni siquiera sabía cómo se llamaban. No se me hubiera ocurrido ordenarles algo.)"
    mcp "(Y que os mataran no estaría entre las órdenes que les hubiera dado, si hubiera podido darles alguna.)"
    gav "No digo que nos conformemos con migajas. Pero hay que reconocer la diferencia."
    gav "[mc] está escuchando. Eso ya es algo que ninguno de nosotros esperaba hace un mes... O hace una hora."
    scene c31s006_180d with dissolve
    dam "[gav] tiene razón. Y yo, que soy el más quejica, lo reconozco."
    aar "El chico tiene cabeza. Me refiero a [gav], no a [dam]..."
    mc "Gracias, [gav]. Eso... significa mucho."
    ama "Y no son solo promesas vacías. [mc] lleva días trabajando en esto desde que asumió el cargo."
    ama "[aar] y yo le hemos inundado con información. Pensad que para él tampoco debe ser fácil."
    call BlinkXS4("c31s006_185") from _call_BlinkXS4_1556
    carl "Creo que estamos exigiendo a [mc] que asuma los errores de la anterior dirección. Es su primer día aquí y de momento nos está escuchando."
    carl "No digo que renunciemos a nuestras peticiones, pero creo que deberíamos darle el beneficio de la duda."
    "Sorprendentemente, todos asienten. Te das cuenta de que [carl] te empieza a caer bien. Y crees que tú empiezas a caerle bien a él."
    call BlinkXS4("c31s006_190") from _call_BlinkXS4_1557
    carl "Continuemos, pues. La siguiente petición es la más importante para muchos de nosotros."
    carl "Los operativos quieren poder elegir su futuro. Su posición dentro de NTR. Y, a largo plazo, poder rescindir sus contratos si así lo deciden."
    scene c31s006_190d with dissolve
    "La sala queda en silencio unos segundos. Es la petición que más les ilusiona de todas las que han hecho. Puedes leerlo en sus caras."
    aar "Esta es la que más nos importa. A todos."
    fred "No queremos ser propiedad de nadie. Ya fuimos propiedad de la empresa una vez, y [aar] nos ha dicho que no se va a repetir."
    mc "Lo sé."
    dam "Queremos poder decir 'me quiero ir' y que sea una opción real. No una sentencia."
    gav "O quedarnos. Pero que sea nuestra elección."
    mc "Os escucho. Y os entiendo."
    mc "Cambiar de posición dentro de la empresa: eso lo podemos empezar a estructurar en breve."
    mc "Que cada uno pueda postularse para roles distintos, formarse, crecer. Eso sí. Siempre y cuando la persona sea válida para ese rol."
    scene c31s006_190e with dissolve
    "Ninguno puede ocultar su sonrisa... O su sorpresa."
    ama "Tendremos que crear un sistema de promoción interno, pero es viable."
    mc "En cuanto a rescindir contratos... eso es más complejo."
    mc "No porque no quiera permitíroslo., sino porque hay implicaciones legales, de seguridad, de vuestro propio origen."
    mc "Sois personas. Merecéis elegir. Pero tengo que asegurarme de que esa salida os proteja."
    mc "No quiero sonar paternalista, pero tampoco quiero que os vayáis y que el mundo de fuera os trate peor de lo que os trató este sitio."
    scene c31s006_190f with dissolve
    fred "¿Eso es un 'no'?"
    mc "Es un 'trabajaremos juntos en ello para que sea un sí a su debido tiempo. En breve'."
    aar "No creo que podamos esperar una respuesta más positiva sobre este tema."
    gav "Yo me quedo. Que conste. Pero quiero saber que podría irme si quisiera."
    mc "Eso es exactamente lo que vamos a garantizar. No hoy, pero lo haremos."
    mc "Y quiero trabajar con vosotros para que nadie quiera rescindir ese contrato."
    call BlinkXS4("c31s006_195") from _call_BlinkXS4_1558
    "[carl] tiene una sonrisa en la cara cuando empieza a hablar. Cada vez estás más convencido de que le gusta lo que está oyendo en esta reunión."
    carl "Última petición de la lista oficial. Solicitamos documentación con identidades alternativas."
    carl "Pasaportes y otra documentación con nombres reales para poder movernos por el mundo con cierta normalidad."
    mc "Eso es... ilegal. Y no sabría por dónde empezar. Es terreno complicado..."
    scene c31s006_195d with dissolve
    fred "Somos clones ilegales de personas vivas, [mc]. Ya estamos en terreno complicado."
    aar "No tenemos identidades reconocidas. No existimos para el mundo oficial."
    gav "No podemos coger un vuelo comercial. No podemos abrir una cuenta bancaria. No podemos existir fuera de estas paredes sin ser fantasmas."
    dam "O criminales. Aunque no hayamos hecho nada."
    call BlinkXS4("c31s006_200") from _call_BlinkXS4_1559
    if persistent.family:
        ama "Tienen razón, [mc]. Nuestra situación legal es... peculiar."
    else:
        ama "Tienen razón, [mc]. Su situación legal es... peculiar."
    ama "Sin esa documentación, la promesa de poder abandonar la empresa sería una promesa vacía."
    mc "Lo sé. Y es un problema real que necesita una solución real."
    mc "Documentación alternativa no es algo que pueda aprobar ahora mismo. Hay un coste logístico importante. Y hay riesgos legales para NTR."
    call BlinkXS4("c31s006_205") from _call_BlinkXS4_1560
    fred "¿Más riesgos que los que corremos nosotros cada día en el campo?"
    mc "No. Tienes razón, [fred]."
    mc "Voy a estudiar cuánto costaría y cómo hacerlo de la forma más segura posible."
    mc "Para vosotros y para la empresa. No os digo que no. Os digo que necesito pensar."
    mc "Supongo que alguno de los gobiernos con los que hemos trabajado podría ayudar, pero..."
    scene c31s006_205d with dissolve
    aar "Es más de lo que esperábamos."
    gav "Con eso me vale."
    stop music fadeout (1.5)
    dam "Yo quiero un nombre guay. Algo como... Dan Steel. Dan está muerto. Me puedo quedar con su nombre."
    scene c31s006_205e with dissolve
    play music ("music/Higher-Instrumental.ogg")
    carl "[dam], por el amor de..."
    dam "¡Es para el pasaporte! ¡Hay que pensarlo con tiempo!"
    fred "A veces me pregunto cómo ha sobrevivido tantas misiones."
    dam "Carisma. Puro y simple."
    scene c31s006_205f with dissolve
    "La tensión inicial se ha disipado. La sala tiene ahora un ambiente más cálido. Como si confiaran en ti."
    "No por lo que les ha contado [aar] en los últimos días, sino por lo que han escuchado salir de tu boca."
    "Miras a cada uno de los presentes antes de hablar."
    mc "Bien. Creo que, si no tenéis más peticiones, hemos cubierto todo lo que había sobre la mesa."
    mc "Quiero que sepáis que esta no es la última reunión. Es la primera."
    ama "[mc] tiene pensado establecer un canal directo para que podáis trasladar nuevas peticiones."
    aar "Eso... nunca había existido antes."
    mc "Pues existe ahora. Y quiero que lo uséis."
    fred "¿Cuándo es la próxima reunión?"
    mc "En unas semanas. Necesito tiempo para avanzar en los temas pendientes."
    mc "No quiero convocaros hasta tener algo concreto que ofreceros. Avances en lo que habéis pedido hoy."
    gav "Nos parece bien."
    carl "Tomaré nota de los acuerdos alcanzados y los pendientes de resolución."
    dam "Y yo tomaré nota de los nombres guais por si hay pasaportes."
    scene c31s006_205g with dissolve
    aar "[dam]..."
    dam "*Risa* ¡Lo hago por el equipo!"
    "Algunos no pueden ocultar sus sonrisas bajo los aspavientos que produce la última tontería de [dam]."
    "Crees que es la primera vez que esa sala escucha las risas de clones."
    mc "Una cosa más antes de que os vayáis."
    scene c31s006_205h with dissolve
    "Te pones de pie. Todos te miran por un momento antes de que empieces a hablar. Sabes que tienes su atención."
    mc "Sé lo que habéis vivido aquí. Lo que os hicieron. Lo que os negaron. Nunca podré entender del todo por lo que pasasteis."
    mc "Pero no puedo cambiar el pasado. Lo único que puedo hacer es asegurarme de que el futuro sea diferente."
    mc "No como favor. Como obligación. Esta empresa os lo debe. Yo os lo debo."
    scene c31s006_210An with dissolve
    "Nadie habla por un momento, mientras vuelves a sentarte. Se miran entre ellos antes de reaccionar."
    "Pese a todo lo que se ha dicho en la reunión, aún hay sorpresa en sus voces cuando empiezan a hablar."
    fred "Es la primera vez que alguien en ese cargo dice algo así."
    carl "O que alguien en ese cargo se digna a escucharnos."
    gav "Y lo dice en serio. Eso se nota."
    aar "Gracias, [mc]. De parte de todos. También de los que no están aquí."
    ama "Nos vemos en unas semanas, entonces."
    call BlinkXS4("c31s006_215") from _call_BlinkXS4_1561
    carl "Creo que esta reunión ha terminado. Deberíamos dejar a [mc], [ama] y [aar] para que discutan lo que hemos hablado aquí."
    call BlinkXS4("c31s006_220") from _call_BlinkXS4_1562
    aar "Voy a empezar a preparar toda lo documentación necesaria para que tomes las decisiones teniendo toda la información."
    mc "Toda la información {b}relevante{/b}, [aar]. No necesito saber cuánta espuma de afeitar vamos a ahorrar porque ahora se puedan dejar barba."
    call BlinkXS4("c31s006_225") from _call_BlinkXS4_1563
    aar "*Risa* ¿Soy demasiado minucioso en mis informes?"
    mc "*Risa* Yo no diría eso. No sé qué palabra se podría usar para 'tres grados de magnitud por encima de demasiado minucioso'."
    aar "*Risa* Vale. Nada de espuma de afeitar ni de tiempos que ahorraremos en la peluquería."
    scene c31s006_215d with fade
    "La reunión se disuelve lentamente. Los clones salen hablando entre ellos."
    "Por primera vez, hay algo parecido a la esperanza en el cuartel general de NTR. Al menos entre los clones."
    dam "Yo ya estoy pensando en mis patillas. Quizás sean mejor que una barba..."
    gav "[dam], para ya."
    dam "¡Son un símbolo de libertad!"
    call BlinkXS4("c31s006_230") from _call_BlinkXS4_1564
    mc "[ama]..."
    ama "¿Sí?"
    mc "¿Crees que lo haremos bien?"
    call BlinkXS4("c31s006_235") from _call_BlinkXS4_1565
    ama "Creo que ya lo estás haciendo bien."
    stop music fadeout (1.5)
    "Asientes, pensativo. Hay mucho trabajo por delante. Pero hoy, al menos, alguien escuchó a las personas que más han sufrido en NTR."
    return
label c31s006_departmentMeeting:
    scene c31s006_250a with fade
    play music ("music/Passing Action.ogg")
    "Al entrar en la sala, todo el mundo se sienta rápidamente. El futuro brazo de [gav] tiene un aspecto impresionante."
    "Tienes que retenerte para acercarte a mirarlo con detalle. Parece sacado de una película de ciencia ficción."
    "Descubres que vas a odiar esta sala nada más entrar. Es oscura y opresiva. En línea con la imagen de la empresa."
    scene c31s006_250b with fade
    "[aar] hace las presentaciones. Nadie se levanta a estrecharte la mano."
    aar "[flo], Jefe del Departamento Comercial."
    scene c31s006_250c with fade
    aar "[vin], Jefe del Departamento Financiero."
    scene c31s006_250d with fade
    aar "[mael], Jefe del Departamento de Clonación y Medicina."
    scene c31s006_250e with fade
    aar "[cal], Departamento de Clonación y Medicina."
    "Notas la ausencia del término 'Jefe' al nombrar a [cal]. Es el diseñador del brazo."
    scene c31s006_250a with fade
    mc "Bien. Gracias a todos por venir."
    scene c31s006_250g with dissolve
    "Señalas el brazo electromecánico antes de continuar. Te hubiera gustado mirarlo con detenimiento antes de empezar la reunión."
    "Todos lo miran, siguiendo la dirección que tu mano señala."
    mc "Sé que no es la forma más habitual de empezar una reunión de dirección, pero quería tenerlo aquí."
    mc "Para recordarme, y recordaros, de qué somos capaces cuando miramos en la dirección correcta."
    scene c31s006_250a with dissolve
    mc "Antes de entrar en materia, me gustaría que cada uno me diese un resumen de su área."
    mc "¿En qué estado de la empresa? Sin adornos. Empecemos por ti, [aar]."
    call BlinkXS4("c31s006_255") from _call_BlinkXS4_1566
    aar "De acuerdo. El Área Operaciones está activa y a pleno rendimiento."
    aar "Tenemos compromisos firmados con varios clientes para los próximos dos trimestres: Colombia, Estados Unidos, Reino Unido, y Francia."
    aar "En total son siete contratos de distinta envergadura, todos en fase de ejecución o preparación avanzada."
    aar "Los equipos de campo están operativos. No hay bajas graves en este momento, salvo el caso de [gav], que ya conocéis."
    call BlinkXS4("c31s006_260b") from _call_BlinkXS4_1567
    aar "Aparte de eso tenemos varios contratos de soporte con otras PMCs. Iron Fist y Walküre son nuestros principales clientes en ese área."
    aar "Atlas y Chimera son clientes con contratos más pequeños, pero más continuos. Te mandé una lista detallada del resto de clientes."
    mc "Lo sé. La vi. Y vi que incluía clientes con los que hace diez años que no trabajamos ya."
    call BlinkXS4("c31s006_260") from _call_BlinkXS4_1568
    "[aar] hace oídos sordos a tu crítica velada antes de continuar."
    aar "El problema es que todos esos contratos, los de operaciones y los de soporte, tienen fechas de entrega."
    aar "Si tocamos la estructura operativa, necesito saberlo con tiempo suficiente para no dejar a nadie tirado a mitad de una misión."
    mc "Entendido."
    call BlinkXS4("c31s006_265") from _call_BlinkXS4_1569
    mc "[flo], ¿Departamento Comercial?"
    flo "El panorama es interesante. Tenemos negociaciones abiertas con el Gobierno de Colombia para tres operaciones encubiertas de medio plazo."
    flo "Con Estados Unidos hay conversaciones preliminares sobre seis operaciones extra aparte de las que ya están contratadas. El contacto con ellos es sólido."
    flo "Reino Unido y Francia tienen una operación en marcha cada uno. Estoy en negociaciones con Francia para ampliar nuestra área de actuación al Sahel."
    flo "Todos son clientes que pagan bien y que repiten."
    call BlinkXS4("c31s006_270") from _call_BlinkXS4_1570
    flo "China e Israel han querido contratarnos en diversas ocasiones, pero Richards nunca quiso llegar a un acuerdo con ellos. Pagan bien."
    flo "Corea del Norte e Irán se han puesto en contacto varias veces, pero estaban vetados porque nos podría acarrear perder contratos con otros clientes."
    call BlinkXS4("c31s006_275") from _call_BlinkXS4_1571
    flo "Dicho esto... y sé que puede sonar raro viniendo de mí... creo que hay un mercado enorme esperando en el sector médico."
    flo "Alta tecnología, equipamiento hospitalario y dispositivos de consumo."
    flo "Si pivotamos bien, podríamos competir en un sector con márgenes muy distintos y mucha menos exposición legal."
    mc "Eso es exactamente la dirección en la que quiero que pensemos. Gracias."
    call BlinkXS4("c31s006_280") from _call_BlinkXS4_1572
    mc "[vin], los números."
    vin "Sí, los números."
    vin "Fondos disponibles: doscientos doce millones de dólares. Costes operativos mensuales: veintiséis millones."
    vin "Lo que significa que, sin ingresos nuevos, tenemos algo más de ocho meses antes de que la situación se vuelva... incómoda."
    "Tiene una de esas voces que hacen parecer la deriva continental algo divertido de escuchar."
    call BlinkXS4("c31s006_285") from _call_BlinkXS4_1573
    vin "Sin embargo, en el próximo trimestre esperamos la entrada de ciento ochenta y tres millones por operaciones ya realizadas y pendientes de cobro."
    vin "Así que, en términos estrictamente financieros, estamos bien."
    mc "¿Bien bien, o bien de momento?"
    scene c31s006_285d with dissolve
    vin "Bien de momento, como siempre en esta industria. Pero bien."
    vin "El anterior CEO, Daniels... era de la opinión de que los números siempre cuadraban si sabías dónde mirar."
    mc "Daniels está en prisión por cosas como esa, [vin]."
    call BlinkXS4("c31s006_290") from _call_BlinkXS4_1574
    vin "Sí. Ya lo sé."
    "Hace una pausa breve antes de continuar."
    vin "Solo era un comentario sobre su filosofía contable. No sobre sus otros... hobbies."
    "Te acabas de dar cuenta de que tiene unas manos ridículamente pequeñas."
    "Te cuesta un pequeño esfuerzo contener la risa imaginándotelo contando billetes con esas manos."
    call BlinkXS4("c31s006_295") from _call_BlinkXS4_1575
    mc "[mael], tu turno."
    "La actitud de [mael] te resulta incómoda."
    "Es la actitud de alguien que lleva años esperando que le pregunten esto para poder decir exactamente lo contrario de lo que quieren oír."
    mael "El departamento de clonación y genética es el núcleo tecnológico real de esta empresa."
    mael "Todo lo demás, las operaciones, los contratos, incluso ese brazo que tenéis ahí en la mesa..."
    call BlinkXS4("c31s006_300") from _call_BlinkXS4_1576
    mael "Todo eso existe porque nosotros llevamos más de 20 años empujando los límites de lo que la biología y la ciencia permite."
    mael "Tenemos en este momento cuarenta y dos sujetos en fase de gestación avanzada. Nacerán en las próximas semanas."
    call BlinkXS4("c31s006_305") from _call_BlinkXS4_1577
    mael "Son seres humanos viables, y tendremos que decidir qué hacer con ellos independientemente de cualquier decisión estratégica."
    mael "[aar] ha dicho que quieres cerrar el Departamento de Clonación. Me parece un error."
    mc "¿Por qué? ¿Si dejamos de producir clones? ¿Qué perdemos exactamente?"
    call BlinkXS4("c31s006_310") from _call_BlinkXS4_1578
    mael "Perdemos el conocimiento vivo. La clonación no es solo un producto, es un proceso."
    mael "Cada serie nos enseña algo nuevo sobre expresión génica, sobre diferenciación celular, sobre límites del desarrollo embrionario."
    mael "Si cerramos el grifo, en cinco años habremos perdido capacidad técnica que tardamos décadas en construir."
    mc "Entiendo la lógica. Pero... no sé..."
    mc "¿No podríamos mantener ese conocimiento haciendo... no sé... clones de animales o algo así? ¿Clonar un páncreas suelto para trasplantes?"
    "Te sientes un poco estúpido. Deberías haber estudiado alternativas para el departamento central de NTR."
    "Te parece que estás hablando por hablar. Por fin entiendes cómo se siente [emm] muchas veces."
    call BlinkXS4("c31s006_315") from _call_BlinkXS4_1579
    mael "¿Un páncreas suelto?"
    mc "O lo que sea. Un riñón. Estoy improvisando, no soy biólogo o genetista."
    mael "No, ya... ya veo que estás improvisando."
    "Su tono parece decir que, si tuviera un arma en las manos ahora mismo, preferiría apretar el gatillo a tener que lidiar contigo."
    call BlinkXS4("c31s006_320") from _call_BlinkXS4_1580
    "[mael] hace una inspiración profunda antes de continuar, como si se estuviera armando de paciencia para explicarle algo básico a un niño."
    mael "Los animales serían viables, sí."
    mael "No habría problema legal en Aruba, y desde el punto de vista técnico nos permitiría mantener las habilidades del equipo y seguir investigando."
    mael "Cerdos, primates, incluso animales en peligro de extinción si queremos darle un ángulo de imagen pública positivo."
    call BlinkXS4("c31s006_325") from _call_BlinkXS4_1581
    mael "Los órganos humanos aislados son otro cantar."
    mael "Es técnicamente posible, pero hay obstáculos enormes: vascularización, rechazo inmunológico, maduración fuera de un organismo completo. No está resuelto."
    mael "Sería un proyecto de investigación, no un producto a corto plazo."
    mc "Pero ¿merece la pena intentarlo?"
    call BlinkXS4("c31s006_330") from _call_BlinkXS4_1582
    mael "Tengo que estudiarlo con más detalle antes de darte una respuesta honesta."
    mael "Lo que sí puedo decirte es que la idea de mantener el departamento abierto con esa orientación... no me disgusta. De hecho, me gusta."
    "Un leve sentimiento de sorpresa recorre la mesa. Parece que nadie esperaba que [mael] aceptara tan fácilmente el cambio."
    call BlinkXS4("c31s006_335") from _call_BlinkXS4_1583
    mael "La mayoría de los productos médicos que ha salido de mi departamento han sido accidentes felices."
    mael "Efectos colaterales de investigación en la que íbamos en otra dirección. ¿Sabes cómo nació nuestra prueba rápida de embarazo?"
    scene c31s006_335d with dissolve
    flo "¿La que empezaremos a comercializar en la Unión Europea el mes que viene?"
    mael "Sí, esa misma."
    call BlinkXS4("c31s006_340") from _call_BlinkXS4_1584
    mael "Pues nació porque estábamos estudiando marcadores moleculares en embriones de primera fase y uno de mis investigadores detectó algo raro."
    mael "Había una molécula que el cuerpo produce mucho antes de que los niveles de hCG, la hormona del embarazo tradicional, sean detectables."
    mael "Detectamos embarazos con varias semanas de antelación respecto a cualquier test del mercado."
    call BlinkXS4("c31s006_345") from _call_BlinkXS4_1585
    mael "¿Estábamos buscando eso? No. Estábamos buscando otra cosa completamente distinta."
    mael "Pero así es como funciona la investigación de frontera. Si cierras el laboratorio, cierras también unas puertas que no sabes que están ahí."
    mael "Puede que las puertas ni siquiera existan o que lo que haya detrás no valga la pena, pero a veces..."
    mc "Lo entiendo..."
    scene c31s006_345d with dissolve
    "[bet], que hasta ese momento había estado mirando el brazo con la concentración de alguien que toma el pulso a un paciente, levanta la vista."
    bet "Perdona que interrumpa... ¿cuántos de esos cuarenta y dos sujetos tienen anomalías genéticas detectadas en esta fase?"
    mael "Ninguno. Nuestros clones son perfectos dentro de los parámetros. Nada que no hayamos gestionado antes."
    bet "¿Y el protocolo si hay complicaciones en el... nacimiento?"
    mael "Tenemos equipo médico interno especializado en ello."
    bet "¿Neonatólogos?"
    mael "Contratados externamente cuando es necesario."
    bet "De acuerdo. Solo preguntaba."
    scene c31s006_345e with dissolve
    "[bet] vuelve a mirar el brazo. No parece del todo satisfecha con la respuesta, pero no insiste."
    stop music fadeout (1.5)
    mc "Bien. Sigamos. [cal]."
    call BlinkXS4("c31s006_350") from _call_BlinkXS4_1586
    play music ("music/SadSoul.ogg")
    "[cal] no ha hablado hasta ahora. Ha estado mirando el brazo, igual que [bet], aunque con una expresión muy distinta."
    "La de alguien que mira con orgullo algo que construyó con sus propias manos porque nadie le prestó suficiente atención."
    "Es uno de los pocos clones que han dejado las operaciones de campo y se han reciclado a otras funciones con éxito."
    cal "El brazo es funcional. Todas las pruebas que hemos podido hacer sin una implantación real dan resultados dentro de los parámetros esperados."
    cal "El sistema de integración neuromuscular es lo más delicado."
    cal "Básicamente le decimos al sistema nervioso periférico que ese trozo de titanio y goma es una extremidad, y esperamos que se lo crea."
    scene c31s006_350d with dissolve
    flo "¿Y se lo cree?"
    cal "Los modelos de simulación dicen que sí. Pero hasta que no lo hagamos en una persona de verdad, es teoría."
    flo "Claro, claro..."
    "[flo] asiente con esa forma de asentir que tiene la gente cuando en realidad está pensando en otra cosa. Quizás está empezando a pensar dónde puede venderlo."
    mc "¿Qué puede hacer ese brazo que no pueda hacer uno natural?"
    call BlinkXS4("c31s006_355") from _call_BlinkXS4_1587
    cal "En términos de fuerza, bastante más. No vamos a convertir a [gav] en el Soldado de Otoño, que quede claro."
    cal "Pero sí tendrá en ese brazo una fuerza muscular equivalente a entre dos y tres veces la de su brazo original."
    call BlinkXS4("c31s006_360") from _call_BlinkXS4_1588
    cal "El control fino, las tareas de precisión, eso va a requerir rehabilitación y tiempo. Es un proceso."
    cal "No es una mejora instantánea, es una recuperación con ventajas adicionales."
    mc "¿Y podríamos hacer lo mismo con otras extremidades? ¿Piernas, por ejemplo? ¿O manos...?"
    call BlinkXS4("c31s006_365") from _call_BlinkXS4_1589
    cal "En principio, la arquitectura es extrapolable. Las piernas tienen más masa, más carga estructural, el sistema de equilibrio añade complejidad..."
    cal "Una mano o un antebrazo serían sencillos de diseñar partiendo del brazo. El problema sería el peso total y la autonomía de las baterías."
    call BlinkXS4("c31s006_370") from _call_BlinkXS4_1590
    cal "Pero si la operación de [gav] sale bien, no veo por qué no."
    cal "Es trabajo, no magia. Y ya hemos hecho el trabajo más difícil."
    scene c31s006_370d with dissolve
    bet "¿Cuánto tiempo llevas desarrollando esto?"
    cal "Siete años. En mi tiempo libre."
    bet "¿En tu tiempo libre?"
    cal "La empresa no consideró que fuera una prioridad hasta que les puse el prototipo encima de la mesa."
    scene c31s006_375e with dissolve
    bet "¿Y tú tienes...?"
    cal "¿Una mano mecánica? ¿Yo? No. Nunca llegué a subir tan arriba en la lista de prioridades."
    bet "Pues eso es lo primero que deberíamos arreglar cuando terminemos con [gav]."
    scene c31s006_375f with dissolve
    "[bet] te mira como pidiendo disculpas por si se ha extralimitado."
    "[cal] no dice nada, pero te mira con una mezcla de expectación y esperanza."
    mc "Estoy de acuerdo con esa propuesta."
    vin "Desde el punto de vista presupuestario, una unidad adicional del prototipo no debería suponer un..."
    mc "[vin], no es una decisión presupuestaria. Es una deuda."
    vin "De acuerdo."
    call BlinkXS4("c31s006_380") from _call_BlinkXS4_1591
    flo "Si me permitís retomar el hilo comercial un momento..."
    flo "Si la operación de [gav] es un éxito, y estoy convencido de que lo será, estamos ante algo que no existe en ningún sitio."
    call BlinkXS4("c31s006_385") from _call_BlinkXS4_1592
    flo "No hay ninguna prótesis en el mercado con este nivel de integración neuromuscular."
    flo "Ninguna. Lo he estudiado y los competidores más avanzados están a años de distancia."
    flo "El mercado potencial es enorme: militares, civiles, deportistas de élite, accidentes laborales, enfermedades degenerativas..."
    flo "Podríamos ir desde el segmento premium hospitalario hasta acuerdos con seguros médicos. Es exactamente el tipo de producto de alta tecnología del que hablabas, [mc]."
    mc "Es exactamente eso."
    scene c31s006_385d with dissolve
    ama "Aunque habría que resolver antes la cuestión de las patentes. Si esto se desarrolló dentro de la empresa en tiempo... ¿libre, dijiste?"
    cal "Sí."
    ama "Eso puede crear ambigüedad en la propiedad intelectual. Habría que limpiar eso antes de lanzarnos al mercado."
    cal "Lo que sea necesario."
    stop music fadeout (1.5)
    mc "Bien. Entonces vamos a recapitular lo que tenemos sobre la mesa, literal y metafóricamente."
    play music ("music/Thematador.ogg")
    scene c31s006_385e with dissolve
    mc "Las operaciones encubiertas comprometidas para los próximos dos trimestres se van a cumplir. [aar], no vamos a dejar contratos sin cerrar."
    aar "Gracias."
    scene c31s006_385f with dissolve
    mc "[flo], las negociaciones con Colombia y con Estados Unidos siguen adelante por ahora."
    mc "China e Israel hay que estudiarlas con cuidado. Corea del Norte e Irán continúan vetadas o corremos el riesgo de sanciones."
    mc "Pero quiero que empieces a explorar en paralelo contactos en el sector médico."
    mc "Hospitales, aseguradoras, fondos de inversión sanitarios. No para mañana, pero quiero saber qué hay ahí fuera."
    mc "También quiero saber qué tecnologías tenemos que se puedan vender o empezar a fabricar y de las que no hayamos explorado las posibilidades comerciales."
    flo "Considéralo hecho."
    scene c31s006_385g with dissolve
    mc "[mael], quiero en dos semanas un informe sobre la viabilidad real de mantener el departamento de clonación orientado a animales y a investigación de órganos."
    mc "Sin compromisos por ninguna parte, solo datos."
    mael "Dos semanas. De acuerdo."
    mc "Los cuarenta y dos sujetos que están en gestación... vamos a garantizar que tengan un recibimiento digno y que se les dé una salida adecuada, sea la que sea."
    mc "No somos los que éramos. No creo que se conviertan en operativos de campo."
    scene c31s006_385h with dissolve
    mc "[vin], necesito que me prepares tres escenarios financieros."
    mc "Uno con la empresa tal como está, uno con el cierre progresivo de operaciones encubiertas, y uno con una inversión seria en la línea médica."
    mc "Números reales, no proyecciones optimistas."
    vin "¿Cuándo?"
    mc "La semana que viene."
    vin "Claro."
    scene c31s006_385i with dissolve
    mc "[ama], seguridad operativa durante la transición. Necesito que nadie de fuera sepa que estamos cambiando de rumbo hasta que estemos listos para contarlo nosotros."
    ama "Entendido."
    scene c31s006_385j with dissolve
    mc "Y [cal]..."
    mc "Lo que habéis hecho tú y tu equipo es extraordinario."
    mc "Quiero que la operación de [gav] sea un éxito, y quiero que tú tengas tu mano."
    mc "En ese orden, pero quiero las dos cosas."
    cal "De acuerdo."
    scene c31s006_385k with dissolve
    bet "He revisado el protocolo de implantación tres veces y tengo algunas sugerencias para el procedimiento que me gustaría comentar contigo, [cal], antes de entrar a quirófano."
    cal "Cuando quieras."
    bet "¿Esta tarde?"
    cal "Esta tarde."
    scene c31s006_385l with dissolve
    flo "¿Sabéis lo que sería una historia de marketing perfecta?"
    flo "El ingeniero que diseñó la prótesis porque la necesitaba, recibiendo la prótesis que diseñó. Eso vale más que cualquier campaña publicitaria."
    cal "No soy una campaña publicitaria, [flo]."
    flo "Ya lo sé. Por eso funcionaría."
    scene c31s006_385m with dissolve
    ama "[flo]..."
    flo "¿Qué? Es verdad."
    ama "Es verdad. Y aun así..."
    vin "Si hemos terminado con la parte emotiva... ¿podemos cerrar esta reunión? Tengo que preparar tres informes..."
    mc "Creo que no hay nada más de lo que hablar."
    scene c31s006_385n with dissolve
    "La gente se empieza a levantar."
    "[bet] rodea la mesa despacio y se detiene junto al brazo electromecánico. Lo mira de cerca, sin tocarlo, como si estuviera leyendo algo escrito en él."
    bet "¿Cuánto pesa? Parece más pesado que en las especificaciones que me mandasteis."
    call BlinkXS4("c31s006_390") from _call_BlinkXS4_1593
    cal "Este es el prototipo. Pesa un poco más que el que implantarás. Cuatro kilos cien gramos. Y no tiene las baterías."
    cal "El que le pondrás a [gav], tres kilos ochocientos gramos al completo."
    "Suena como un padre orgulloso."
    scene c31s006_390d with dissolve
    bet "Menos de lo que esperaba."
    cal "Era un requisito de diseño. Si pesa demasiado, el hombro lo paga a largo plazo."
    bet "Pensaste en todo."
    cal "Tuve siete años para hacerlo."
    scene c31s006_390e with dissolve
    vin "*Murmurando para sí mismo* Daniels también creía que lo tenía todo pensado."
    "Prefieres no contestar y te diriges con [ama] a tu despacho para revisar los expedientes de los clones con los que te reunirás en poco más de una hora."
    scene c31s006_390f with fade
    "Te detienes un momento frente a una ventana."
    "Fuera, el Caribe brilla a lo lejos con esa indiferencia perfecta que tiene el mar cuando no sabe que alguien está mirándolo."
    "Alguien que acaba de heredar una empresa ilegal y la intención, todavía sin forma precisa, de convertirla en algo distinto."
    stop music fadeout (1.5)
    "Es un buen comienzo. O al menos, es un comienzo."
    return
label c31s006_baseArrival:
    call BlinkXS4("c31s006_400") from _call_BlinkXS4_1732
    play music ("music/UnforeseenMotive.ogg")
    ama "Por aquí. Intentaré no abrumarte, pero hay mucho que ver."
    mc "Tranquila. Prefiero verlo todo de una vez y hacerme una idea real del sitio."
    ama "Como quieras. Empezamos por los dormitorios de la tropa."
    scene c31s006_405a with fade
    call BlinkXS4("c31s006_405") from _call_BlinkXS4_1733
    ama "Aquí duermen los operativos. Literas, taquillas individuales, zona común al fondo."
    mc "Es... funcional."
    call BlinkXS4("c31s006_410") from _call_BlinkXS4_1734
    ama "Es lo más amable que se puede decir."
    mc "¿Cuántos comparten habitación?"
    call BlinkXS4("c31s006_415") from _call_BlinkXS4_1735
    ama "Dieciséis por módulo. Hay seis módulos en este bloque. Hay seis bloques." id c31s006_baseArrival_d9244d75
    mc "¿Y esto no ha cambiado en años?"
    ama "No. La dirección anterior no veía motivo para mejorar lo que consideraba suficiente."
    mc "Pues yo sí lo veo."
    call BlinkXS4("c31s006_420a") from _call_BlinkXS4_1736
    ama "Lo sé."
    mc "¿Creciste aquí?"
    call BlinkXS4("c31s006_420b") from _call_BlinkXS4_1737
    ama "En un módulo más pequeño, sólo para las chicas. Es básicamente lo mismo, pero nuestra zona común es más grande."
    ama "Teníamos que especializarnos en más cosas, con lo que debíamos entrenar con dispositivos diferentes."
    mc "Lo entiendo."
    call BlinkXS4("c31s006_425") from _call_BlinkXS4_1738
    bet "Yo diría que huele a vestuario de polideportivo, pero no quiero ser cruel... con los polideportivos." id c31s006_baseArrival_db787fdc
    mc "¿Tú también lo notas?"
    bet "Llevo aquí cinco minutos y ya me estoy acostumbrando. Eso da más miedo."
    call BlinkXS4("c31s006_430") from _call_BlinkXS4_1739
    ama "Ventilación deficiente. Está en la lista de reformas pendientes desde hace dos años."
    mc "Avísame cuando suba a la primera posición de esa lista."
    stop music fadeout (1.5)
    ama "Anotado. Sigamos con la visita." id c31s006_baseArrival_53dd844a
    scene c31s006_435a with fade
    call BlinkXS4("c31s006_435") from _call_BlinkXS4_1740
    play music ("music/Wonder.ogg")
    ama "Laboratorio principal. Análisis, desarrollo de protocolos, investigación aplicada."
    mc "¿Aplicada a qué exactamente?"
    ama "Mejoras de rendimiento físico, tratamientos de recuperación, adaptaciones para el campo."
    ama "Y, obviamente, mejoras en los protocolos de clonación."
    call BlinkXS4("c31s006_440") from _call_BlinkXS4_1741
    bet "Este sitio va a hacer las delicias de [dap] y [sca]..."
    mc "No entiendo qué son la mitad de las cosas que estoy viendo, pero todo parece de alta tecnología."
    call BlinkXS4("c31s006_445") from _call_BlinkXS4_1742
    ama "[mael], el jefe del Departamento Científico, es un sibarita cuando se trata de pedir equipamiento."
    ama "Y la parte más interesante es la que se ha desarrollado aquí, como tecnología propia."
    mc "Eso podría ser la piedra fundacional de lo que queremos hacer para el cambio de orientación de la empresa."
    call BlinkXS4("c31s006_450") from _call_BlinkXS4_1743
    ama "Creo que tenemos una buena base para empezar a crecer, pero en la reunión de dentro de un rato te quedará más claro."
    mc "¿Todo esto estaba operativo antes de que yo llegara?"
    ama "El laboratorio, sí. Aunque algunos proyectos se paralizaron con el cambio de dirección."
    mc "¿Cuáles?"
    call BlinkXS4("c31s006_455") from _call_BlinkXS4_1744
    ama "Los que no eran rentables a corto plazo. Que casualmente eran los más interesantes."
    mc "¿Puedo ver qué estaba paralizado?"
    ama "Te preparo un informe. Pero ahora seguimos."
    mc "¿No hay nadie trabajando?"
    call BlinkXS4("c31s006_460") from _call_BlinkXS4_1745
    ama "Creo que hay varias reuniones de equipo, donde están ultimando la información que te presentarán en breve."
    ama "Me parece que nadie se quería cruzar contigo antes de esa reunión."
    stop music fadeout (1.5)
    mc "Entiendo."
    scene c31s006_465a with fade
    call BlinkXS4("c31s006_465") from _call_BlinkXS4_1746
    play music ("music/Dark-Score.ogg")
    ama "Sala de clonación 1."
    mc "Por el amor de Dios."
    call BlinkXS4("c31s006_470") from _call_BlinkXS4_1747
    if persistent.family:
        ama "Sí. [eva] y yo nacimos ahí dentro."
    else:
        ama "Sí. [eri], [dap] y [emm] nacieron ahí dentro."
    ama "Hacía años que no venía aquí..."
    if persistent.family:
        "Te sientes tentado de abrazar a la mercenaria, pero la carga emocional que hay en su voz te dice que no es el mejor momento."
    else:
        "La carga emocional que hay en su voz te indica que, pese a que ella no ha nacido en esa sala, no es un lugar agradable para ella."
    mc "¿Sigue activa?"
    call BlinkXS4("c31s006_475") from _call_BlinkXS4_1748
    ama "Sí, todos los tubos de clonación están llenos. [mael] te podrá dar datos sobre ellos."
    ama "No te voy a dar los números ahora mismo."
    mc "¿Por qué no?"
    call BlinkXS4("c31s006_480") from _call_BlinkXS4_1749
    ama "Porque estamos de tour y prefiero que llegues a la reunión de hoy con la cabeza despejada."
    call BlinkXS4("c31s006_485") from _call_BlinkXS4_1750
    bet "Es su forma de decir que son números que impresionan."
    mc "¿Lo son?"
    bet "Mucho. He hablado con [mael] estos últimos días."
    call BlinkXS4("c31s006_490") from _call_BlinkXS4_1751
    mc "¿Qué hacemos con todo esto? ¿Con la sala, con el equipo?"
    ama "Ese es exactamente el tipo de pregunta que necesitamos que hagas tú en la reunión. Y que la respondas."
    mc "No tengo respuesta todavía."
    ama "No la necesitas hoy."
    mc "¿Podemos entrar? [bet] se va a dejar la nariz en el cristal..." id c31s006_baseArrival_3a77c5a2
    call BlinkXS4("c31s006_495") from _call_BlinkXS4_1752
    ama "No con la ropa de calle. Hay que entrar con trajes de protección y pasar un proceso de desinfección antes."
    ama "Se entra por detrás. Esta puerta solo se usa cuando no hay ningún proceso de clonación en marcha y la sala no necesita ser estéril."
    mc "Me parece lógico."
    call BlinkXS4("c31s006_500") from _call_BlinkXS4_1753
    bet "Hay cosas que llevan tiempo digerir. Creo que esta sala es una de ellas."
    mc "¿Tú cómo lo llevas? A mí se me están poniendo los pelos de punta."
    bet "Me voy a centrar en ser útil. En hacer lo que sé hacer."
    stop music fadeout (1.5)
    bet "No voy a juzgar lo que se ha hecho aquí con anterioridad. Juzgaré si no se deja de hacer."
    scene c31s006_505a with fade
    call BlinkXS4("c31s006_505") from _call_BlinkXS4_1754
    play music ("music/CelticFlute.ogg")
    ama "Instalaciones médicas. Quirófanos, recuperación, consultas."
    mc "Impresiona. Es más grande de lo que esperaba."
    call BlinkXS4("c31s006_510") from _call_BlinkXS4_1755
    bet "Supongo que se necesita un hospital pequeño en un sitio así."
    bet "Imagino que las heridas pueden ser diversas, sabiendo a lo que se dedica la empresa."
    call BlinkXS4("c31s006_515") from _call_BlinkXS4_1756
    ama "Diversas es una palabra muy diplomática."
    call BlinkXS4("c31s006_520") from _call_BlinkXS4_1757
    bet "Soy médico. La diplomacia es parte del trabajo."
    mc "¿Cuántas camas de recuperación hay?"
    call BlinkXS4("c31s006_525") from _call_BlinkXS4_1758
    ama "Veinticuatro. Aunque hemos llegado a tener más ocupación de la deseable."
    mc "¿Y ahora mismo?"
    call BlinkXS4("c31s006_530") from _call_BlinkXS4_1759
    ama "Nueve pacientes, por lo que he leído. Desde una gripe hasta... [gav] y varios heridos de la Guerra Clon."
    mc "¿[gav] aún está aquí?"
    call BlinkXS4("c31s006_535") from _call_BlinkXS4_1760
    bet "Después de hablar con él, he creído que sería lo mejor que se mantuviera en un entorno controlado."
    bet "Puede salir de su habitación y moverse por la base, pero no más excursiones a la playa de momento."
    mc "¿Va a funcionar bien lo del brazo?"
    call BlinkXS4("c31s006_540") from _call_BlinkXS4_1761
    bet "Va a funcionar mejor que el original. No es una exageración, es una maravilla de la ingeniería."
    bet "Tengo ganas de ver el aparato real. Hasta ahora solo he visto fotos y planos."
    mc "¿Cuándo es la intervención?"
    call BlinkXS4("c31s006_545") from _call_BlinkXS4_1762
    bet "El domingo. Si todo va bien, en dos semanas estará en fisioterapia." id c31s006_baseArrival_2a7468a5
    mc "¿Y [gav] sabe cómo va a quedar?"
    call BlinkXS4("c31s006_550") from _call_BlinkXS4_1763
    bet "Le expliqué cada paso. Me preguntó si podría volver al campo."
    mc "¿Y?"
    bet "Le dije que probablemente sí. Que el brazo no iba a ser su límite."
    mc "¿Y él, cómo reaccionó?" id c31s006_baseArrival_457c1076
    scene c31s006_550d with dissolve
    ama "Se debió poner contento."
    bet "Se le iluminó la cara. Fue bonito."
    ama "No me lo habías contado."
    bet "Confidencialidad médico-paciente..."
    ama "Gracias por hacer esto, de verdad." id c31s006_baseArrival_0dd13cac
    bet "Es mi trabajo. Pero también... después de hablar con el chico... me importa."
    scene c31s006_550e with dissolve
    ama "Tenemos que seguir. El hangar nos espera."
    bet "Yo me voy a quedar aquí. No tengo ningún interés en ver armas. A ver si puedo encontrar a alguien que me enseñe esto en profundidad."
    scene c31s006_550f with dissolve
    ama "¿Sabrás encontrar la sala de reuniones? Tenemos una en cuarenta minutos con los jefes de departamento."
    bet "No lo había pensado..."
    ama "Segunda puerta a la derecha del ascensor en el segundo piso."
    stop music fadeout (1.5)
    bet "Encontraré algo parecido a eso y confiaré en la intuición."
    scene c31s006_555a with fade
    call BlinkXS4("c31s006_555") from _call_BlinkXS4_1764
    play music ("music/AnxiousMarch.ogg")
    mc "¿Cuánto tiempo llevamos? No me gustaría llegar tarde a la reunión."
    ama "Quedan cuarenta minutos. Tenemos margen." id c31s006_baseArrival_2bfccbf6
    mc "¿Qué hay en el hangar?"
    ama "Vehículos operativos. Lo que usamos en el campo de entrenamiento."
    scene c31s006_560a with fade
    call BlinkXS4("c31s006_560") from _call_BlinkXS4_1765
    ama "Hangar principal. Aquí guardamos los vehículos de uso habitual."
    mc "Hay más de lo que pensaba."
    ama "NTR opera en entornos variados. Necesitamos versatilidad."
    mc "¿Me los explicas?"
    call BlinkXS4("c31s006_565") from _call_BlinkXS4_1766
    ama "Vehículos ligeros para reconocimiento y desplazamiento rápido. Camiones para logística y personal."
    ama "Los AFV para zonas con resistencia moderada. Y los IFV para operaciones de combate directo."
    ama "Muchos de ellos son capturas que hemos traído a la base para poder entrenar con ellos y conocer diversos tipos de vehículos."
    scene c31s006_565d with dissolve
    "Sigues con la mirada sus gestos, intentando adivinar qué vehículo corresponde a qué siglas. Solo eres capaz de ponerle nombre a los camiones."
    mc "¿Estos son los vehículos que alquilamos a otras empresas?"
    call BlinkXS4("c31s006_570") from _call_BlinkXS4_1767
    ama "Algunos de ellos. En la mayoría de las misiones de infiltración no usamos vehículos terrestres o nos los proporcionan en el destino." id c31s006_baseArrival_3a71b47d
    ama "La mayoría se usa para entrenar o para transporte."
    mc "Espera. ¿Eso de ahí es un tanque?"
    scene c31s006_575d with dissolve
    ama "¿Ese?"
    call BlinkXS4("c31s006_575a") from _call_BlinkXS4_1768
    ama "No, no es un tanque." id c31s006_baseArrival_b5e6776f
    mc "Parece un tanque."
    ama "Tiene cadenas, torreta y un cañón. Lo entiendo. Pero no es un tanque."
    "Parece genuinamente sorprendida de que no lo sepas. A ti te sigue pareciendo un tanque."
    mc "¿Qué es entonces?"
    call BlinkXS4("c31s006_575b") from _call_BlinkXS4_1769
    ama "Un IFV. Vehículo de combate de infantería. Un Bradley, si quieres el nombre específico."
    ama "Ese en concreto salió del Líbano hace unos años."
    mc "¿Cuál es la diferencia entre un IFV y un tanque?"
    call BlinkXS4("c31s006_580") from _call_BlinkXS4_1770
    ama "Un tanque está diseñado para destruir otros vehículos acorazados y posiciones blindadas."
    ama "El IFV lleva infantería al combate y les da apoyo de fuego. Es otra filosofía."
    mc "¿Y NTR no tiene tanques?"
    call BlinkXS4("c31s006_585") from _call_BlinkXS4_1771
    ama "No. Ni los necesitamos."
    mc "¿Por qué no?"
    ama "NTR no hace guerra convencional. No somos un ejército. Hacemos operaciones de precisión, espionaje, extracción, eliminación..."
    ama "Un tanque en ese contexto es un problema logístico enorme y una señal muy visible."
    mc "No queremos visibilidad."
    call BlinkXS4("c31s006_590a") from _call_BlinkXS4_1772
    ama "Exacto. Los IFV nos dan protección y potencia de fuego sin anunciar que venimos."
    "Su sonrisa te dice que has acertado. Se la ve contenta de que empieces a entender su mundo. Un mundo que va a ser el tuyo también."
    ama "Si cae uno en nuestras manos en una misión, estamos entrenados para usarlo a nivel básico, pero no es lo normal."
    mc "Tiene sentido."
    call BlinkXS4("c31s006_590b") from _call_BlinkXS4_1773
    ama "Además, mover los tanques, mantenerlos, tripularlos... requiere infraestructura que no tenemos aquí."
    ama "Y capturar un tanque es mucho más raro, con lo que no necesitamos ese entrenamiento."
    mc "Entiendo. ¿Cuántos IFV tenemos?"
    call BlinkXS4("c31s006_595") from _call_BlinkXS4_1774
    ama "Cuatro operativos de diferentes modelos. Un par más inoperativos, pero también los usamos para entrenamiento."
    ama "Los AFV son ocho. Son como un IFV, pero con ruedas en vez de cadenas. En algunos sitios se les llama igual."
    mc "¿Todo esto cabe aquí?"
    call BlinkXS4("c31s006_600") from _call_BlinkXS4_1775
    ama "Este es el hangar principal de la base. Hay otro más grande en las instalaciones de entrenamiento." id c31s006_baseArrival_314abfa6
    mc "¿Y los aviones y helicópteros?"
    ama "En el aeropuerto o en las instalaciones de entrenamiento. Están un poco alejados de la base."
    mc "¿A cuánto están?"
    call BlinkXS4("c31s006_605") from _call_BlinkXS4_1776
    ama "A unos tres kilómetros. Allí está el campo de entrenamiento, los almacenes de armamento, la pista de aterrizaje, el hangar de aeronaves y el otro hangar de vehículos." id c31s006_baseArrival_b637b71b
    mc "¿Por qué separado?"
    ama "Seguridad y logística. Si algo falla en un punto, no compromete el otro."
    mc "¿Lo veremos hoy?"
    call BlinkXS4("c31s006_610") from _call_BlinkXS4_1777
    ama "No tenemos tiempo antes de la reunión. Te lo agendo para mañana si quieres."
    mc "Sí. Quiero verlo todo."
    ama "Lo suponía."
    call BlinkXS4("c31s006_615") from _call_BlinkXS4_1778
    mc "Oye."
    ama "¿Sí?"
    mc "Esto es muy grande."
    ama "Lo sé."
    mc "No lo digo en sentido logístico ni me refiero a la base. Lo digo en el sentido de... es mucha responsabilidad."
    mc "Mientras estábamos en casa todo era muy abstracto. Ahora estoy viendo que es... real."
    call BlinkXS4("c31s006_620") from _call_BlinkXS4_1779
    ama "También lo sé."
    mc "¿Y tú crees que puedo con esto?"
    ama "No te habría apoyado si no lo creyera."
    mc "Eso no responde exactamente a mi pregunta."
    call BlinkXS4("c31s006_625") from _call_BlinkXS4_1780
    ama "*Risa* Sí la responde. Solo hay que escuchar bien la respuesta."
    mc "Eres muy directa cuando quieres."
    ama "*Risa* Soy directa siempre. Lo que pasa es que este sitio..."
    mc "¿Te está afectando volver?"
    call BlinkXS4("c31s006_630") from _call_BlinkXS4_1781
    ama "Un poco. Esta empresa necesitaba un cambio real, no cosmético."
    ama "Lo que has planeado para hoy, la reunión de dentro de un rato..." id c31s006_baseArrival_7bf6aaa2
    ama "Eso no es lo que hacía el anterior CEO. En absoluto."
    mc "El listón no estaba muy alto."
    call BlinkXS4("c31s006_635") from _call_BlinkXS4_1782
    ama "No. Pero tú lo has subido de todas formas. Eso importa. Y aún no has empezado a trabajar..."
    mc "Gracias, Amanda."
    ama "No me las des todavía. Queda mucho trabajo."
    mc "Lo sé."
    call BlinkXS4("c31s006_640") from _call_BlinkXS4_1783
    ama "Nos quedan veinte minutos para la reunión. ¿Tienes alguna pregunta antes de entrar?"
    mc "Varias. Pero pueden esperar."
    ama "Bien. Ah, y una cosa más."
    mc "¿Qué?"
    call BlinkXS4("c31s006_645") from _call_BlinkXS4_1784
    ama "Si preguntan algo que no sepas responder, no finjas que lo sabes."
    "Parece que la conversación sobre el no-tanque que tiene justo detrás le ha abierto los ojos a que eres novato en esto."
    mc "¿Eso pasa mucho en estas reuniones?"
    ama "Con los jefes de departamento, siempre."
    mc "Consejo anotado."
    call BlinkXS4("c31s006_650") from _call_BlinkXS4_1785
    ama "Son buenos en lo suyo, pero llevan años sin rendirle demasiadas cuentas a nadie."
    mc "¿Eso es una advertencia?"
    ama "Es contexto. La advertencia es que algunos van a intentar marearte con tecnicismos."
    mc "¿Y qué hago?"
    call BlinkXS4("c31s006_655") from _call_BlinkXS4_1786
    ama "Escuchar. Preguntar. Y no firmar nada que no entiendas."
    mc "¿Ha pasado eso antes?"
    ama "Con Daniels, sí. Varias veces. Les dejaba hacer siempre y cuando cumplieran con los objetivos." id c31s006_baseArrival_b2952f57
    mc "¿Y cómo acabó?"
    call BlinkXS4("c31s006_660") from _call_BlinkXS4_1787
    ama "Ya sabes cómo acabó. Mal. Por eso te lo digo ahora."
    mc "¿Vas a estar tú en la reunión?"
    ama "A tu lado. Todo el rato. No voy a dejarte solo entre tiburones." id c31s006_baseArrival_0051c6a3
    mc "Bien."
    scene c31s006_665a with fade
    call BlinkXS4("c31s006_665") from _call_BlinkXS4_1788
    "En la puerta de la sala de reuniones, unos minutos después..."
    ama "¿Algo más antes de que entremos?"
    mc "Sí. Una cosa."
    ama "Dime."
    mc "Quiero reunirme con los clones. Con los operativos."
    call BlinkXS4("c31s006_670") from _call_BlinkXS4_1789
    ama "¿Cuándo? ¿Hoy?" id c31s006_baseArrival_63f13e2e
    mc "Después de la reunión de jefes de departamento. Si es posible."
    call BlinkXS4("c31s006_675") from _call_BlinkXS4_1790
    ama "[aar] me comentó que han formado un comité. Para hablar contigo de forma organizada."
    mc "Perfecto. Eso es exactamente lo que quiero."
    ama "¿Cuándo propones?"
    mc "Una hora después de que acabemos con los jefes de departamento. ¿Es viable?"
    mc "Tengo que hablar con [car] y con Soporte informático. Puedo reunirme con los clones entre las dos cosas."
    call BlinkXS4("c31s006_680") from _call_BlinkXS4_1791
    ama "Puedo organizarlo. Dame un segundo para que les avise para que estén preparados dentro de un par de horas."
    mc "Bien. No quiero que parezca una imposición. Quiero que sepan que lo estoy pidiendo yo."
    ama "Se lo haré saber."
    mc "Gracias."
    call BlinkXS4("c31s006_685") from _call_BlinkXS4_1792
    ama "¿Sabes qué les vas a decir?"
    mc "Aún no. Pero sé que voy a escucharles."
    ama "Con eso es suficiente para empezar."
    mc "¿Crees que van a fiarse de mí?"
    call BlinkXS4("c31s006_690") from _call_BlinkXS4_1793
    ama "Algunos sí. Otros necesitarán tiempo. Es normal."
    mc "¿Y tú te fías de mí?"
    ama "Ya te lo he dicho antes. No hay nadie de quien me fíe más que de ti en cuanto a esto."
    mc "Lo sé, pero me gusta escucharlo."
    call BlinkXS4("c31s006_695") from _call_BlinkXS4_1794
    ama "*Risa* No lo voy a volver a repetir o se te acabará subiendo a la cabeza."
    mc "*Risa* Está bien. Tenía que intentarlo."
    ama "Venga. La reunión nos espera."
    mc "Vamos."
    scene black with dissolve
    "[ama] envía un par de mensajes de texto antes de entrar."
    stop music fadeout (1.5)
    "Un escalofrío te recorre la columna vertebral."
    return
label c31s006_DanielsFate:
    if _in_replay:
        call mrS3_Daniels from _call_mrS3_Daniels
    scene c31s006_800a with fade
    play music ("music/CinematicFairyTaleStory.ogg")
    "El resto del día pasa volando."
    "Si la sala de reuniones era opresiva, tu despacho no es mucho mejor. Parece sacado de una película de los 70."
    "[car] te da el Manual del Empleado. Es un libro enorme con un montón de conceptos obsoletos."
    "No hay ni una sola mención a los clones en él. Está pensado para el personal de los departamentos que no se dedican a las operaciones."
    "Lo dejas en un lugar prominente de tu escritorio. Otra cosa para tu lista de tareas pendientes."
    scene c31s006_800b with fade
    "Tienes una reunión con el jefe del departamento de informática, [geo]."
    "Parece un buen tipo, aunque tiene un sentido del humor un poco raro, especialmente en cuanto a elección de vestuario."
    "La aplicación de gestión de la empresa parece bastante operativa, aunque ves posibles áreas de mejora."
    "Crees que, más adelante, pondrás a [geo] en contacto con Jamaal."
    "Si tu informático favorito fue capaz de hackear la base de datos de NTR, se debería incrementar la seguridad."
    "Deja una carpeta con el manual de los sistemas informáticos encima de tu mesa. También te manda la versión electrónica por email."
    scene c31s006_800c with fade
    scene c31s006_800An with dissolve
    "Recibes tres visitas de [vin] a lo largo del día."
    "Quiere detalles minuciosos de los informes que le has pedido."
    "La única pregunta de interés para ti es si quieres los informes sobre la 'Contabilidad Real' o sobre la 'Contabilidad Creativa'."
    "Crees que vas a odiar a [vin] y sus diminutas manos."
    "Después de su última visita, no sabes cuántos cafés te ha traído [car]."
    stop music fadeout (1.5)
    scene c31s006_805a with fade
    call BlinkXS4("c31s006_805") from _call_BlinkXS4_1795
    "Al final de la tarde, [aar] se presenta en tu despacho. No has salido de él desde la hora de comer."
    play music ("music/Smoking Gun.ogg")
    mc "¿Puedo ayudarte en algo, [aar]?"
    aar "Venía a hablar de Daniels."
    mc "Dime."
    scene c31s006_810a with fade
    call BlinkXS4("c31s006_810") from _call_BlinkXS4_1796
    if mc._var("Daniels"):
        aar "Dijiste que querías formar parte de la decisión que se tomara."
    else:
        aar "Sé que dijiste que dejabas la decisión que se tomara en nuestras manos."
    mc "¿Es necesario hacer esto en mi primer día aquí, [aar]? Aún me estoy poniendo al día con mil cosas..."
    call BlinkXS4("c31s006_815") from _call_BlinkXS4_1797
    aar "Creo que será mejor actuar lo antes posible... No he conseguido saber si aún tiene partidarios en la empresa y..."
    mc "Y yo pienso que no podemos hacer nada hasta que [eva] esté aquí."
    mc "No es algo que se pueda hacer por videoconferencia con alguien como ella."
    call BlinkXS4("c31s006_820") from _call_BlinkXS4_1798
    aar "¿Qué quieres decir con 'alguien como ella'?"
    mc "[eva] es impulsiva y emocional. Va a querer estar aquí cuando se tome la decisión."
    call BlinkXS4("c31s006_825") from _call_BlinkXS4_1799
    aar "¡Uff! Por un momento me habías asustado."
    aar "Empezaba a pensar que habíais cambiado a [eva] tanto como a [ama]."
    mc "Quizás un poco más que a ella."
    mc "¿La has notado muy cambiada?"
    call BlinkXS4("c31s006_830") from _call_BlinkXS4_1800
    aar "Lo de ayer en el hangar... Fue una sorpresa."
    aar "Pero hoy he tenido una reunión larguísima con ella y... Es diferente."
    mc "¿En qué lo has notado?"
    call BlinkXS4("c31s006_835") from _call_BlinkXS4_1801
    aar "Es más... asertiva. Más segura de sí misma."
    aar "Antes de dejarla con tu familia hubiera aceptado mis órdenes sin rechistar. Ahora..."
    "No vas a corregirle para decirle que ahora también es la familia de [ama]."
    mc "*Risa* ¿Has intentado darle órdenes? Eres valiente."
    mc "Ya no está bajo tu mando. Tú eres el jefe del Departamento de Operaciones. Ella es la jefa de Seguridad."
    call BlinkXS4("c31s006_840") from _call_BlinkXS4_1802
    aar "Lo sé, lo sé. Pero esperaba... No sé... Supongo que son viejas costumbres."
    mc "Todo el mundo cambia, [aar]. Algunos más rápidos que otros."
    mc "Y volviendo al tema de Daniels... ¿Dónde está ahora mismo?"
    call BlinkXS4("c31s006_845") from _call_BlinkXS4_1803
    aar "En una celda, aislado. Vigilado por dos operativos en todo momento."
    mc "¿Son de fiar?"
    aar "Hacen turnos de 8 horas, con lo que son seis operativos implicados en su vigilancia."
    aar "Creo que sí, que son de fiar. Pero..."
    mc "Tenemos que confiar en nuestros propios hombres, [aar]."
    mc "Si crees que podemos confiar en ellos, podemos aplazar la decisión hasta que [eva] llegue."
    call BlinkXS4("c31s006_850") from _call_BlinkXS4_1804
    aar "Me sorprendes... Los... 'normales' no soléis confiar tanto en los clones."
    if persistent.family:
        mc "He vivido con [ama] y [eva] durante tres semanas."
    else:
        mc "He vivido con [eri], [emm] y [dap] toda mi vida."
    mc "Les confiaría mi vida sin dudarlo. Me da lo mismo si son clones o... 'normales'."
    mc "Creo que voy a odiar esa palabra."
    mc "Son igual de personas que yo o que [mael]. Se confía en las personas por cómo son. No por cómo nacieron."
    call BlinkXS4("c31s006_855") from _call_BlinkXS4_1805
    aar "Lo vuelvo a repetir. Me sorprendes."
    stop music fadeout (1.5)
    mc "Prepárate para más sorpresas con los Marks, [aar]."
    call BlinkXS4("c31s006_860") from _call_BlinkXS4_1806
    play music ("music/LifeOfAWanderingWizard.ogg")
    aar "Sobre eso..."
    mc "¿Qué pasa?"
    aar "¿Podrías decirle a [bet] que dejara de abrazarme cada vez que me ve?"
    mc "*Risa* Eres un iluso si crees que vas a conseguir eso."
    mc "Ha encontrado un nuevo sobrino-nieto. Buena suerte con que deje de abrazarte."
    scene c31s006_865a
    aar "Tenía que intentarlo..."
    mc "Es una batalla perdida, [aar]. Pero puedes intentar decírselo tú mismo."
    call BlinkXS4("c31s006_870") from _call_BlinkXS4_1807
    aar "¿Qué? ¡No! ¡Esa mujer me da miedo! Estoy seguro de que me trataría como a un niño que dice una tontería si lo intento."
    mc "*Risa* Seguramente es lo que haría."
    mc "Pero tienes razón. Debajo de ese aspecto de anciana afable, Tía [bet] es muy dura y puede dar miedo."
    mc "Y tiene un sexto sentido para detectar cosas."
    call BlinkXS4("c31s006_875") from _call_BlinkXS4_1808
    aar "¿En plan 'en ocasiones veo muertos'?"
    mc "*Risa* No, pero detecta cuando alguien guarda un secreto."
    mc "Si descubre que le tienes miedo, estás perdido."
    call BlinkXS4("c31s006_880") from _call_BlinkXS4_1809
    aar "*Risa* Mi nivel de miedo se ha incrementado un par de niveles ahora mismo."
    aar "¿Te veo mañana?"
    mc "Sí, por supuesto."
    stop music fadeout (1.5)
    scene c31s006_885d with fade
    play music ("music/Clear-Air.ogg")
    "Media hora después de que [aar] se haya ido..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    car "*A través de la puerta* ¿Puedo pasar, Señor?"
    mc "Adelante, [car]."
    call BlinkXS4("c31s006_885") from _call_BlinkXS4_1810
    car "Venía a decirle que me voy a casa."
    mc "Perfecto, [car], y gracias. Nos vemos el lunes."
    call BlinkXS4("c31s006_890") from _call_BlinkXS4_1811
    car "¿El lunes? ¿No va a venir mañana?"
    mc "Es sábado... ¿Trabajas los sábados?"
    call BlinkXS4("c31s006_895") from _call_BlinkXS4_1812
    car "Casi todo el personal trabaja los sábados, Señor. La Compañía está abierta los 365 días del año."
    mc "¿Cuántos días libres tienes a la semana?"
    car "Los domingos y los lunes. El domingo conocerá a [lar], la chica que me sustituye cuando tengo el día libre."
    car "Bueno, eso si usted viene a trabajar el domingo... Era el día libre del Sr. Daniels."
    mc "Sí, vendré. Al menos este domingo. Es la operación de [gav] y quiero estar aquí."
    call BlinkXS4("c31s006_900") from _call_BlinkXS4_1813
    car "Es usted... diferente."
    mc "Si te refieres a diferente de Daniels, me lo tomaré como un cumplido."
    scene c31s006_900e
    car "La Srta. [ama] me ha dicho que le está esperando en el aparcamiento."
    scene c31s006_885d with fade
    stop music fadeout (1.5)
    "Tras eso, desaparece sin decirte nada más."
    scene c31s006_900d with fade
    play music ("music/Looking-Forward.ogg")
    "Al llegar a casa, cenas con [bet] y [ama]."
    "Alguien se ha ocupado de enviar cátering a la casa, que llega 20 minutos después que vosotros."
    "Son un acierto con vuestros platos favoritos, aunque [bet] se queja del tamaño de la pizza."
    "Nadie se queja porque los postres sean demasiado abundantes."
    "Le tienes que dar las gracias a [car]."
    "Os explicáis cómo ha ido vuestro primer y agotador día en NTR."
    "Hay risas y comentarios sorprendidos. Ha sido menos duro para [ama] de lo que ella creía."
    scene c31s005_285f with fade
    "Vuelves a caer agotado en la cama."
    stop music fadeout (1.5)
    "[ama] vuelve a dormir en tu cama. Para ella también ha sido un día largo."
    return
label c31s007_AmaTour:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_23
    scene black with dissolve
    centered "{size=+20}{b}DÍA 40 – SÁBADO{/b}{/size}"
    scene c31s007_005An with dissolve
    play music ("music/Clear-Air.ogg")
    "Tu segunda mañana como CEO sigue el mismo patrón que la tarde del primero."
    "Alguna visita que deja alguna carpeta sobre tu mesa."
    "Si no hay visitas, es [car] quién te entrega alguna carpeta nueva."
    call BlinkXS4("c31s007_010") from _call_BlinkXS4_1814
    "Después de la última carpeta antes de la hora de la comida..."
    mc "[car], un momento, por favor."
    car "¿Sí, Señor?"
    mc "¿Hay alguna razón por la que me estáis trayendo toda la documentación en papel?"
    mc "El único email que he recibido con documentación ha sido de [geo]."
    call BlinkXS4("c31s007_015") from _call_BlinkXS4_1815
    car "Al Sr. Daniels le gustaba la documentación en papel. Por eso tiene tantos archivadores aquí."
    mc "Yo me siento... enterrado bajo todas estas carpetas y dosieres."
    call BlinkXS4("c31s007_020") from _call_BlinkXS4_1816
    car "Entonces... ¿no hace falta que le imprima los emails ni los documentos adjuntos?"
    mc "Creo que puedes reenviarme directamente lo que pienses que debo leer."
    mc "Y ¿imprimir un email? Nunca, por favor. Me será más fácil encontrarlos en el portátil que en los archivadores."
    call BlinkXS4("c31s007_025") from _call_BlinkXS4_1817
    car "De acuerdo, Señor."
    mc "[mc]."
    car "A este paso no iba a poder verle por encima de las carpetas."
    car "Le haré saber a [lar] que no debe imprimirle los mensajes."
    mc "Gracias, [car]."
    stop music fadeout (1.5)
    scene c31s007_030a with fade
    call BlinkXS4("c31s007_030") from _call_BlinkXS4_1818
    "Unos minutos después, [ama] entra sin llamar con una bolsa en la mano."
    play music ("music/Southern Gothic.ogg")
    ama "Necesito salir de aquí."
    mc "¿Qué pasa? Me habías dicho que me enseñarías las instalaciones de entrenamiento hoy."
    mc "Pero he tenido un día... complicado."
    call BlinkXS4("c31s007_035") from _call_BlinkXS4_1819
    ama "Hoy va a ser imposible."
    ama "Se corrió la voz de que íbamos a crear un equipo de vigilancia para Newport."
    ama "Tengo más de 90 solicitudes para unirse. ¡Y tengo que entrevistarlos a todos!"
    mc "No sé cómo se ha podido filtrar. No lo hemos hecho público aún."
    call BlinkXS4("c31s007_040") from _call_BlinkXS4_1820
    ama "[dam]. Su solicitud estaba la primera. Te dije que tendríamos que atropellarlo."
    mc "*Risa* Ayer tuve ganas de hacerlo. Coger el No-Tanque y pasarle por encima."
    call BlinkXS4("c31s007_045") from _call_BlinkXS4_1821
    ama "*Risa* IFV. Si vas a dirigir esto, tienes que aprender los nombres de los vehículos y de los dispositivos."
    mc "En algún sitio entre estas carpetas hay un inventario de todo lo que tenemos. Con fotos para tontos como yo."
    mc "Alguien ha pensado que era buena idea enviármelo."
    call BlinkXS4("c31s007_050") from _call_BlinkXS4_1822
    ama "*Risa* [aar]. Y a él no lo puedes atropellar."
    mc "*Risa* Es lo malo de que también sea accionista."
    mc "Pero me has dicho que querías salir de aquí. ¿Has acabado las entrevistas?"
    call BlinkXS4("c31s007_055") from _call_BlinkXS4_1823
    ama "No, pero tengo una hora y media libre para comer. Quiero enseñarte algo en el campo de entrenamiento."
    ama "No va a ser la visita turística, pero hay algo que quiero que veas."
    mc "¿Por eso vas así vestida en vez de con traje?"
    call BlinkXS4("c31s007_060") from _call_BlinkXS4_1824
    ama "Sí, y en la bolsa tienes ropa para que te cambies tú también."
    mc "Voy. ¿Vas avisando a [car] de que voy a salir durante una hora y media?"
    mc "No tengo nada en la agenda, pero..."
    ama "Voy. No tardes."
    mc "Cinco minutos. Cinco minutos reales."
    scene c31s007_065a with fade
    call BlinkXS4("c31s007_065") from _call_BlinkXS4_1825
    "Tardas cuatro minutos. Y cuatro minutos después, estáis en un todoterreno militar camino al campo de entrenamiento."
    mc "¿Qué me quieres enseñar?"
    ama "¿Te acuerdas del día que se rompió tu cama?"
    mc "Sí, el día que Zeus rompió mi cama."
    call BlinkXS4("c31s007_070") from _call_BlinkXS4_1826
    ama "Te dije que te enseñaría mi posesión más preciada. No puedo esperar más a enseñártela."
    mc "También me dijiste que esperabas que no te considerara una psicópata."
    call BlinkXS4("c31s007_075") from _call_BlinkXS4_1827
    ama "Bueno, mi posesión más preciada está junto a... otras cosas."
    if ama._var("route"):
        mc "Veamos qué oscuros secretos esconde mi esposa. No voy a dejar de quererte por ello."
    else:
        mc "Veamos qué oscuros secretos escondes. No voy a dejar de quererte por ello."
    call BlinkXS4("c31s007_080") from _call_BlinkXS4_1828
    ama "*Risa* Eso espero. Tampoco esperes que guarde las orejas cortadas de todas las personas que he matado."
    "La naturalidad con la que lo dice, ente risas, hace que un escalofrío te recorra la espalda."
    "Nunca podrás llegar a entender del todo a la rubia mercenaria ni a su hermana pelirroja. Eso te produce cierta tristeza."
    "Decides seguir la conversación como si ella estuviera bromeando."
    mc "*Risa fingida* ¿Al menos unos cuantos dientes?"
    call BlinkXS4("c31s007_085") from _call_BlinkXS4_1829 #2600
    ama "En eso las películas mienten. Es más difícil de lo que parece sacar un diente. Y lleva tiempo que por norma no tenemos."
    ama "Además, sería bastante asqueroso tener una colección de dientes."
    mc "Estoy totalmente de acuerdo."
    "Supones que, si sabe cuánto tiempo lleva sacar un diente... Prefieres no preguntar."
    scene c31s007_085d with fade
    "Seguís vuestro camino unos minutos más antes de que [ama] pare el todoterreno."
    "No seguís ningún camino o carretera que puedas ver, pero [ama] parece muy segura de hacia dónde conduce."
    scene c31s007_090a with fade
    call BlinkXS4("c31s007_090") from _call_BlinkXS4_1830
    "Paráis al lado de una valla de alambre de espino."
    ama "Aquí estamos. Ya puedes bajar del coche."
    mc "Esto no es el campo de entrenamiento."
    call BlinkXS4("c31s007_095") from _call_BlinkXS4_1831
    ama "*Risa* ¿Quieres un premio por tus dotes de observación?"
    ama "El campo de entrenamiento empieza al otro lado de la valla."
    mc "¿Podemos saltarla?"
    scene c31s007_095d with dissolve
    ama "No hará falta. Pasaremos por debajo."
    mc "Te sigo."
    scene c31s007_095e with fade
    "Camináis unos ciento cincuenta pasos entre pequeños barrancos creados por cursos de agua de lluvia."
    "Usáis uno de esos barrancos para pasar por debajo de la verja."
    "Tan solo necesitáis agacharos. Nada de reptar. Tomas nota mental de que hay que hacer algo con los barrancos."
    "Camináis unos cincuenta pasos más después de atravesar la verja."
    scene c31s007_100a with fade
    call BlinkXS4("c31s007_100") from _call_BlinkXS4_1832
    ama "Es aquí."
    mc "¿Aquí? No hay nada."
    mc "Es exactamente igual que lo que había treinta metros atrás. Me parece que he visto esa roca tres veces hoy."
    scene c31s007_100d with dissolve
    "[ama] te sorprende tirándose al suelo."
    ama "Excepto por esta madriguera... Un momento... Casi lo tengo."
    ama "Ha llovido bastante desde la última vez que estuve aquí y hay más tierra del que esperaba."
    scene c31s007_100e with fade
    stop music fadeout (1.5)
    "Al cabo de un rato, [ama] saca una bolsa impermeable bastante sucia."
    play music ("music/Hidden Past.ogg")
    "La intenta limpiar con la mano, sin mucho éxito."
    mc "¿Qué hay ahí dentro? No es muy grande."
    call BlinkXS4("c31s007_105") from _call_BlinkXS4_1833
    ama "Mis posesiones más preciadas. Ya te lo he dicho. Siéntate."
    "La tristeza en sus ojos es suficiente como para que te sientes sin abrir la boca."
    "La bolsa es pequeña. Esperas algo con valor sentimental, pero no puedes imaginar qué es."
    if persistent.family:
        scene c31s007_105d with fade
    else:
        scene c31s007_105e with fade
    "[ama] saca una polaroid de la bolsa. Se ve a una niña con un equipamiento militar que parece demasiado grande para ella."
    ama "Te presento a Fiona. Es la única foto que existe de ella."
    ama "Es de un entrenamiento una semana antes de que muriera."
    if persistent.family:
        mc "Me recuerda a [eri] más que a [dap]."
    else:
        mc "Por alguna razón, me imaginaba una [eva] en miniatura. Supongo que por el nombre que le puso a la muñeca."
        mc "Pero me recuerda más a [eri] que a [eva]."
    call BlinkXS4("c31s007_110") from _call_BlinkXS4_1834
    ama "Me parece que le hubiera gustado escuchar eso. Era la más empática de todas nosotras."
    ama "Creo que sí, que se hubiera parecido a [eri] si hubiera tenido la oportunidad."
    mc "Lo siento, [ama]. Siento todo lo que tuvisteis que pasar."
    mc "Siento lo de Fiona. Pero también lo de Clarice, Beatrice o Diana."
    mc "Siento no haber tenido la oportunidad de conocerlas."
    scene c31s007_110d with dissolve
    if ama._var("route"):
        "Pasáis un rato mirando la foto. Te gustaría abrazar a la mujer que adoras, pero sabes que está enfrascada en sus pensamientos."
    else:
        "Pasáis un rato mirando la foto. Te gustaría abrazar a la triste mercenaria, pero sabes que está enfrascada en sus pensamientos."
    "Odias a Daniels por haberte privado de la oportunidad de haber conocido a Diana, Beatrice y Clarice."
    "Odias a Richards, el CEO anterior, porque la muerte de Fiona pasó bajo su mandato."
    "Pero, sobre todo, compadeces a las chicas. A las vivas y a las muertas. Por lo que pasaron. Por lo que sufrieron."
    if persistent.family:
        "También al resto de los clones. Ellos pasaron por lo mismo."
    else:
        "También a los clones. Ellos pasaron por lo mismo."
    "Ninguno lo merecía."
    call BlinkXS4("c31s007_115") from _call_BlinkXS4_1835
    mc "¿Estás bien?"
    ama "No. Pero tenía ganas de que las conocieras."
    mc "¿Has dicho 'las'?"
    if persistent.family:
        scene c31s007_115d with fade
    else:
        scene c31s007_115e with fade
    ama "Estas son las otras chicas. Bueno, somos..."
    ama "Diana, yo, Beatrice, [eva], y Clarice."
    mc "Sois tan diferentes entre vosotras... Y se me hace raro verte castaña."
    if persistent.family:
        ama "Intentábamos mantener la individualidad tiñéndonos el pelo y con diferentes maquillajes."
        ama "Nosotras lo teníamos permitido, al contrario que el resto de los clones."
    ama "Diana era la más guapa de nosotras. Sus especialidades eran... la seducción y el asesinato."
    ama "A Beatrice siempre le gustó ser la más fuerte. Se especializó en armamento pesado y en logística."
    ama "Clarice era la más frágil de todas. Estuvo enferma cuando éramos niñas y... Bueno, era la más pequeña junto con Fiona."
    ama "Era la especialista en comunicaciones. Pero hubiera machacado a cualquiera en un combate."
    ama "Y a [eva] y a mí, ya nos conoces."
    mc "¿Cuál era vuestra especialidad?"
    call BlinkXS4("c31s007_120") from _call_BlinkXS4_1836
    ama "La mía era la vigilancia, interrogatorio y espionaje. Me rompí una pierna a los seis años y estuve un mes pegada a los monitores."
    ama "La especialidad de [eva] era... es la infiltración y eliminación."
    ama "Fiona hubiera sido nuestra francotiradora."
    ama "Pero no me malinterpretes. Cualquiera de nosotras podía hacer de todo."
    call BlinkXS4("c31s007_125") from _call_BlinkXS4_1837
    ama "Bueno... quizás de todo menos la parte de la seducción. Eso sólo lo hicieron Diana y Clarice."
    mc "Me lo contaste."
    call BlinkXS4("c31s007_130") from _call_BlinkXS4_1838
    ama "Pero sobre el resto, cualquiera de nosotras podía usar un lanzagranadas o equipo de comunicaciones."
    ama "Y, obviamente, todas podíamos darle una paliza en el campo de tiro con un M4A1 o con una Glock a cualquiera de la base."
    ama "Y en combate cuerpo a cuerpo podíamos competir con cualquiera."
    mc "Me suena muy extraño... Especialistas, pero a la vez generalistas."
    call BlinkXS4("c31s007_135") from _call_BlinkXS4_1839
    ama "Nunca sabes lo que te vas a encontrar en una misión. Todas teníamos que saber hacer de todo."
    ama "Algunos de los otros operativos están más especializados. Los D son muy buenos con las armas pesadas. Son tipos grandes."
    ama "Pero nunca serán tan buenos como lo era Beatrice."
    mc "Lo entiendo."
    mc "Has dicho que esa era la única foto de Fiona. Es extraño, ¿no?"
    mc "Supongo que tampoco hay muchas fotos de todas vosotras juntas."
    if persistent.family:
        scene c31s007_115d with fade
    else:
        scene c31s007_115e with fade
    ama "Esta es la única que hay, que yo sepa."
    ama "Las fotos están prohibidas en la base, excepto cuando quieren hacer un cartel publicitario. Y entonces llevamos máscaras."
    ama "Nadie quiere una foto con 10 clones de la serie G circulando por internet. Ni una foto de seis niñas de 6 años entrenando."
    mc "Lo pillo. Tanto secretismo..."
    mc "Me alegra que me hayas enseñado estas fotos. Me alegra y me pone triste a la vez."
    call BlinkXS4("c31s007_140") from _call_BlinkXS4_1840
    ama "La foto de Fiona la hizo Arnau, uno de los hermanos de [aar], con una cámara que entró de contrabando."
    ama "La nuestra la hizo [aar]. Descubrieron la cámara y se la quitaron."
    ama "Por eso las guardaba aquí. Era mi escondite secreto. Aquí nadie me las quitaría."
    call BlinkXS4("c31s007_145") from _call_BlinkXS4_1841
    ama "La última vez que estuve aquí no sabía que no volvería a ver a mis hermanas con vida."
    ama "Me hubiera gustado que las hubierais conocido. Y que ellas os hubieran conocido a vosotros."
    "Sabes que está intentando hacerse la fuerte. La [ama] de casa seguramente ya estaría llorando. La vuelta a Aruba la está cambiando."
    mc "No hace falta que vuelvas a esconderlas. Nadie te va a quitar esas fotos nunca."
    mc "Me ocuparé de ello si alguien lo intenta."
    call BlinkXS4("c31s007_150") from _call_BlinkXS4_1842
    ama "Gracias, [mc]. Aunque supongo que, ahora que soy propietaria de parte de la empresa, nadie se atrevería a hacerlo."
    mc "Supongo que no."
    mc "Pero no veo nada por lo que pueda llamarte psicópata. Tener fotos de tus hermanas no lo es."
    call BlinkXS4("c31s007_155") from _call_BlinkXS4_1843
    ama "Hay algo más en la bolsa."
    scene c31s007_155d with dissolve
    "[ama] saca un trozo de metal de la bolsa y lo deja sobre su rodilla. No entiendes qué puede ser."
    ama "Es una esquirla del artefacto que mató a Fiona."
    ama "Cada una de nosotras se quedó un trozo. Yo escondí el mío aquí y no pude recuperarlo cuando tuvimos que irnos."
    mc "¿Qué tiene eso de malo?"
    call BlinkXS4("c31s007_160") from _call_BlinkXS4_1844
    ama "¿No consideras raro que nos quedáramos un trozo de lo que mató a nuestra hermana?"
    mc "No es usual, pero he visto madres que llevan un mechón de pelo de su hijo muerto colgado al cuello y..."
    mc "Espera... Enséñame la foto donde estáis las cinco otra vez."
    if persistent.family:
        scene c31s007_115f with fade
    else:
        scene c31s007_115g with fade
    mc "El corazón que lleva [eva] al cuello siempre... ¿Es su trozo del explosivo?"
    call BlinkXS4("c31s007_165") from _call_BlinkXS4_1845
    ama "Sí. Es el trozo más grande. El que la mató. Le dio forma de corazón y se hizo un colgante."
    ama "Por eso lo lleva siempre consigo. Es su forma de que Fiona... vea el mundo que se perdió."
    ama "Sé que puede sonar retorcido para cualquiera que no seamos sus hermanas, pero..."
    mc "No es retorcido, [ama]. Es un gesto muy bonito por parte de [eva]."
    call BlinkXS4("c31s007_170") from _call_BlinkXS4_1846
    ama "No le digas que te lo he dicho yo. Ni siquiera que lo has deducido tú."
    ama "Seguramente me mataría y después se sentiría muy sola por ser la única viva de las seis."
    mc "Eso sería muy típico de [eva]. No te preocupes, no le diré nada."
    mc "Le pregunté por el corazón y me dijo que me lo contaría algún día. Tengo que darle la oportunidad de hacerlo cuando esté preparada."
    scene c31s007_175a with fade
    call BlinkXS4("c31s007_175") from _call_BlinkXS4_1847
    "[ama] se levanta después de meter las fotos y el fragmento en la bolsa de nuevo."
    "No la devuelve a la madriguera, sino que la mete en uno de los bolsillos de sus pantalones."
    ama "Y ahora deberíamos irnos. Nuestra hora y media casi ha pasado ya. Aún tengo que entrevistar a varios operativos hoy."
    ama "Y a [car] no le va a gustar si llegas tarde."
    mc "¿Tenemos tiempo para hacer una cosa?"
    ama "Depende. ¿Qué quieres hacer?"
    scene c31s007_175d with dissolve
    "Te levantas y la abrazas. No tienes palabras para expresar lo que sientes. Tus brazos alrededor de su cuerpo tendrán que transmitir el mensaje."
    scene c31s007_175e with dissolve
    "Por primera vez desde que ha sacado la bolsa de la madriguera, [ama] deja sus sentimientos fluir."
    "Odias hacerla llorar, pero estas lágrimas también forman parte de su proceso de curación."
    "A ninguno de los dos os importa llegar un poco tarde a la siguiente cita de vuestra agenda."
    stop music fadeout (1.5)
    return
label c31s007_surgery:
    scene c31s007_180a with fade
    "El resto del día transcurre con lo que parece que es la nueva normalidad."
    play music ("music/Looking-Forward.ogg")
    "Al menos, las carpetas dejan de acumularse encima de tu mesa."
    scene c31s007_180b with fade
    "Al volver a la Casa del CEO, y tras ducharos, cenáis el cátering que [car] ha encargado."
    "Otra vez ha vuelto a acertar con platos que os gustan. Tienes que enterarte de cómo lo hace."
    "[bet] está un poco nerviosa con la operación del día siguiente."
    "Se ha pasado los dos días reunida con cirujanos e ingenieros, y ensayando la operación."
    "Cree que saldrá bien, pero es una operación que no se ha hecho nunca. Hay demasiadas cosas que podrían salir mal."
    scene c31s007_180c with fade
    "Esta vez, las dos mujeres deciden dormir contigo."
    "Os acostáis pronto. La cirugía de [gav] está planificada para las 10 AM."
    "La cama es lo suficientemente grande para los tres."
    stop music fadeout (1.5)
    scene black with dissolve
    centered "{size=+20}{b}DÍA 41 – DOMINGO{/b}{/size}"
    scene c31s007_180d with dissolve
    play music ("music/LostVoices.ogg")
    "Por la mañana, [bet] apenas toca los croissants recién hechos que [car] envía cada mañana."
    "Si necesitabas alguna muestra de lo nerviosa que está, eso es más que suficiente."
    scene c31s006_800a with fade
    "Llegas a tu despacho un poco antes de las 8. Se te hace raro no ver a [car] al llegar."
    "Las carpetas han desaparecido de tu mesa y un montón de emails han aparecido en tu bandeja de entrada."
    "Hay un café esperándote, con lo que [lar] seguramente ya está en el edificio."
    stop music fadeout (1.5)
    "Crees que vas a adorar la eficiencia de [car]."
    scene c31s007_185a with fade
    call BlinkXS4("c31s007_185") from _call_BlinkXS4_1848
    play music ("music/Majestica.ogg")
    "Cuando llevas unos minutos leyendo correos electrónicos..."
    lar "¡Oops! No sabía que había llegado ya."
    mc "Buenos días. Supongo que eres [lar]. Soy [mc]. Encantado de conocerte."
    call BlinkXS4("c31s007_190") from _call_BlinkXS4_1849
    lar "Buenos días, Sr. Marks. Sí, soy [lar], su asistente los domingos y los lunes."
    mc "Encantado de conocerte, [lar]."
    call BlinkXS4("c31s007_195") from _call_BlinkXS4_1850
    lar "He archivado todas las carpetas que [car] me indicó. Si las quiere consultar, las tiene en..."
    mc "No hace falta. He visto que [car] me envió correos con la documentación. Dudo que necesite las carpetas."
    lar "Perfecto, Señor."
    call BlinkXS4("c31s007_200a") from _call_BlinkXS4_1851
    lar "Si me necesita estaré ahí fuera."
    mc "Gracias, [lar]."
    scene c31s007_200ba with fade
    call BlinkXS4("c31s007_200b") from _call_BlinkXS4_1852
    "Cuando se acerca la hora de la operación..."
    mc "[lar], voy a ir a las instalaciones médicas. Si sale algo {b}urgente{/b}, avísame, por favor."
    lar "Entiendo, Señor. Solo lo verdaderamente urgente."
    mc "Hoy, lo urgente es la cirugía de [gav]. El resto puede esperar a menos que se caiga el cielo sobre nuestras cabezas."
    stop music fadeout (1.5)
    scene c31s007_205a with fade
    "[aar] ya está allí, junto a un G que no conoces."
    play music ("music/SCP-x6x.ogg")
    mc "Buenos días, [aar]. Buenos días..."
    gid "[gid], Señor. Buenos días."
    aar "Buenos días, [mc]."
    mc "¿Vamos según lo previsto?"
    scene c31s007_205b with dissolve
    aar "De momento sí. [bet] aún no ha entrado en el quirófano."
    mc "Me lo imaginaba como en las series de TV."
    mc "Creía que podríamos ver cómo se hace la operación en directo, desde un balcón o algo por el estilo."
    aar "Nunca hemos necesitado ese tipo de instalación. En ese quirófano se suelen tratar heridas de combate."
    mc "Lo entiendo."
    aar "Uno de los asistentes de [bet] nos traerá noticias de vez en cuando. Si hay algo interesante que contar."
    gid "Con su permiso, voy a retirarme. Mi turno empieza en unos minutos."
    mc "Por supuesto, [gid]." (multiple=2)
    aar "Adelante, [gid]." (multiple=2)
    "Ninguno de los dos sabéis a quién se dirigía. No importa."
    call BlinkXS4("c31s007_210") from _call_BlinkXS4_1853
    aar "¿Cómo está [bet]?"
    mc "Nerviosa. Supongo que es lo que tiene hacer una cirugía única."
    mc "Yo no sé si podría estar concentrado todo el tiempo en una operación que durara seis horas."
    aar "Los cirujanos están hechos de otra pasta. Saben lo que un despiste puede representar para sus pacientes."
    scene c31s007_215d with dissolve
    "Para tu sorpresa, [car] aparece en la sala de espera. Se queda en un rincón."
    call BlinkXS4("c31s007_210") from _call_BlinkXS4_1854
    mc "[aar], voy a dejarte un momento. quiero hablar con [car]."
    aar "No hay problema."
    call BlinkXS4("c31s007_215") from _call_BlinkXS4_1855
    mc "Buenos días, [car]. No esperaba verte aquí."
    car "He conocido a [gav]... a todos estos chicos... desde que nacieron."
    car "Creo que no podría quedarme en casa durante la operación sin subirme por las paredes."
    car "Yo tampoco esperaba verle aquí, Señor."
    mc "Te dije que vendría hoy."
    call BlinkXS4("c31s007_220") from _call_BlinkXS4_1856
    car "Lo sé. Pero creía que esperaría los resultados en su despacho. Los señores Richards y Daniels..."
    mc "No soy ni Richards ni Daniels, [car]. Quizás mi forma de hacer las cosas no sea tan eficiente, pero..."
    mc "La cirugía de [gav] me importa."
    call BlinkXS4("c31s007_225") from _call_BlinkXS4_1857
    car "Ya le dije que era usted diferente, Señor."
    mc "Y yo te dije que me lo tomaba como un cumplido."
    car "En este caso, lo es."
    scene c31s007_230a with fade
    "[ama] llega junto con [cal] unos minutos antes de que empiece la cirugía."
    scene c31s007_230b with fade
    "El tiempo, más que pasar, repta en los relojes en el momento en que la operación empieza."
    "Las conversaciones decaen al mismo ritmo."
    scene c31s007_230c with fade
    "No hay nada que ver en esta sala. Y la puerta por la que debería aparecer el asistente que tiene que traer noticias no se abre."
    scene c31s007_230d with fade
    "Te lo tomas como una buena señal. Tienes confianza ciega en [bet] como cirujana."
    scene c31s007_230e with fade
    "Algunos clones aparecen de vez en cuando. Echan una ojeada a la sala antes de volver a irse."
    scene c31s007_230f with fade
    "Cada vez que uno de ellos aparece, te da la impresión de ser observado."
    scene c31s007_230g with fade
    "Como si quisieran asegurarse de que el nuevo CEO está en la sala, preocupándose por cómo va la cirugía de uno de los suyos."
    scene c31s007_230h with fade
    "[mael] aparece hacia el final de la operación. Él también está interesado en saber cómo va todo."
    "Aunque quizás sus razones son diferentes de las tuyas."
    scene c31s007_230i with fade
    "Las seis horas llegan y pasan. El maldito asistente no aparece para dar ninguna explicación."
    scene c31s007_230j with fade
    "Cuando la séptima hora de la cirugía se está acercando, por fin se abre la puerta que todos lleváis una hora mirando."
    ass "La operación ha sido un éxito. Todo ha salido como esperábamos. El paciente está en observación."
    scene c31s007_235An with dissolve
    "Puedes ver las emociones reflejadas en las caras de los presentes."
    "Hay alivio, alegría, e incluso alguna mirada calculadora."
    "Incluso hay unos ojos inquisitivos que estudian tu reacción."
    scene c31s007_230k with fade
    "Todo el mundo va desapareciendo de la sala, dejándote solo con [ama]."
    call BlinkXS4("c31s007_240") from _call_BlinkXS4_1858
    ama "¿Vas a quedarte aquí?"
    mc "Sí. Quiero hablar con Tía [bet] y que me explique cómo ha ido todo. Sé que no voy a entender ni la mitad de lo que me diga, pero..."
    ama "Lo entiendo. Yo tengo que ir un momento a mi despacho y volveré en cuanto pueda."
    mc "¿Más entrevistas?"
    call BlinkXS4("c31s007_245") from _call_BlinkXS4_1859
    ama "No. Nadie quería hacer una entrevista hoy. Todos estarían pensando en la cirugía."
    ama "La mayoría de la gente aprecia a [gav]."
    ama "Tengo que comprobar el cambio de turnos de guardia tan solo."
    mc "Lo entiendo. Te veo luego."
    scene c31s007_245d with fade
    "Te quedas solo en la sala de espera. No hay nada que ver ni ninguna nueva noticia que recibir."
    "Tan solo esperar a Tía [bet]. Pasas unos minutos mirando la puerta."
    stop music fadeout (1.5)
    scene c31s007_250a with fade
    call BlinkXS4("c31s007_250") from _call_BlinkXS4_1860
    "Ella aparece quince minutos después. El tiempo ha vuelto a moverse a su velocidad habitual."
    play music ("music/Separation.ogg")
    bet "No esperaba que quedara nadie aquí. Venía a por un café."
    mc "¿Todo bien en la cirugía?"
    call BlinkXS4("c31s007_255") from _call_BlinkXS4_1861
    bet "Todo perfecto. Incluso mejor que perfecto. El resto de los cirujanos son muy buenos en lo suyo."
    bet "El chico se va a recuperar de la operación antes de lo que esperaba."
    mc "Eso es bueno. ¿Cómo ha ido todo? ¿Cuál será el siguiente paso?"
    call BlinkXS4("c31s007_260") from _call_BlinkXS4_1862
    "Ella te explica cómo ha ido la cirugía. Como imaginabas, no entiendes ni una cuarta parte de lo que te explica."
    bet "Tendremos a [gav] en observación durante unos días. No queremos que se infecte la herida."
    bet "Con un poco de suerte, podremos encender el brazo en una semana y ver cómo reacciona."
    mc "¿Podré estar cuando lo hagáis?"
    call BlinkXS4("c31s007_265") from _call_BlinkXS4_1863
    bet "No lo había pensado, pero me parece que es una buena idea que estés cuando lo hagamos."
    bet "Que seas el último que queda aquí demuestra lo que te importa esto."
    bet "Seguramente alguien está hablando de ello ahora mismo en la base."
    mc "Eso no me importa demasiado ahora mismo."
    mc "¿Tú cómo estás?"
    call BlinkXS4("c31s007_270") from _call_BlinkXS4_1864
    bet "Agotada. Pero muy contenta. Ha habido un momento en que creía que no lo lograríamos."
    bet "Pero todo ha salido bien al final."
    bet "Ahora tengo ganas de darme una ducha. Aún puedo notar el sudor corriéndome por la espalda."
    mc "Entonces no te entretengo más. Te veo luego para ir a casa."
    call BlinkXS4("c31s007_275") from _call_BlinkXS4_1865
    bet "No voy a ir a casa. Quiero quedarme aquí a pasar la noche por si hay alguna complicación."
    mc "Pero estás agotada..."
    bet "El resto de los cirujanos están igual de agotados que yo. Pero es mi operación."
    scene c31s007_270d with dissolve
    mc "Gracias por todo, Tía [bet]."
    bet "Gracias a ti por darme la oportunidad de ayudar al chico."
    scene c31s007_270e with fade
    "Vuelves a tu despacho y le das las noticias a [lar]. Obviamente, ya las sabía."
    scene c31s006_800a with fade
    "Te sientas tras tu escritorio y miras al vacío durante un rato."
    stop music fadeout (1.5)
    "Ahora empieza la espera."
    return
label c31s007_ama:
    scene c31s007_300a with fade
    call BlinkXS4("c31s007_300") from _call_BlinkXS4_1866
    play music ("music/What-Ive-Found.ogg")
    "Al cabo de unos 40 minutos..."
    ama "Acabo de hablar con Tía [bet]. Me ha explicado todo lo de la operación."
    ama "Es genial que todo haya ido tan bien."
    mc "Desde luego que sí. [gav] se lo merece, y [eva] no merece tener que cargar con esa culpa."
    ama "[eva] se va a poner muy contenta."
    if ama._var("route"):
        call BlinkXS4("c31s007_305") from _call_BlinkXS4_1867
        ama "Tía [bet] me ha dicho que va a pasar la noche aquí..."
        ama "¿Te apetece que salgamos a cenar a Oranjestad? Aún no has tenido oportunidad de visitarla..."
        mc "Me encantaría. Y si no es en la ciudad, me da lo mismo si es en la playa, mientras sea contigo."
        scene c31s007_305d with hpunch
        ama "¡Genial! Dile a [aar] que te lleve a casa. Yo me voy ya. ¡Tengo unas cosas que hacer!"
        scene c31s007_305e with hpunch
        play sound ("music/Portazo.ogg")
        "*Blam*"
        mcp "(Me lo tomaré como que va a ser nuestra primera cita real.)"
        ama "*A través de la puerta* [lar], ¿sabes si hay una plancha en la casa del CEO?"
        scene c31s007_305f with fade
        stop music fadeout (1.5)
        "Al llegar a casa..."
        play music ("music/Life of Riley.ogg")
        mc "¿[ama]?"
        ama "*Desde la planta inferior* Estoy acabando de arreglarme. Ve duchándote si quieres."
        scene c31s007_305g with fade
        "Después de la ducha vuelves a la cocina y la sigues encontrando vacía."
        "Tan vacía como que no hay cátering hoy. Supones que [ama] ha avisado a [lar]."
        mc "¿[ama]?"
        ama "Estoy en la terraza."
        scene c31s007_310d with dissolve:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (4.8)
        call BlinkXS4("c31s007_310") from _call_BlinkXS4_1868
        ama "Nos podemos ir cuando quieras. Hoy conduces tú."
        stop music fadeout (1.5)
        mc "Estás increíblemente preciosa."
    else:
        call BlinkXS4("c31s007_315") from _call_BlinkXS4_1869
        ama "Bueno, te veo en un rato para ir a casa."
        stop music fadeout (1.5)
        mc "Perfecto, [ama]."
    return

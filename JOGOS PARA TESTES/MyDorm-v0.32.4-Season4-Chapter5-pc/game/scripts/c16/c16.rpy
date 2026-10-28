label c16:
    $ oma._var("altura", "179cm - 5'10\"")
    $ ama._var("altura", "181cm - 5'11\"")
    $ bet._var("altura", "176cm - 5'9\"")
    $ cri._var("altura", "162cm - 5'4\"")
    $ dap._var("altura", "174cm - 5'9\"")
    $ deb._var("altura", "191cm - 6'3\"")
    $ eil._var("altura", "180cm - 5'11\"")
    $ emm._var("altura", "181cm - 5'11\"")
    $ eri._var("altura", "174cm - 5'9\"")
    $ eva._var("altura", "174cm - 5'9\"")
    $ hai._var("altura", "159cm - 5'3\"")
    $ kal._var("altura", "171cm - 5'7\"")
    $ kat._var("altura", "171cm - 5'7\"")
    $ kia._var("altura", "168cm - 5'6\"")
    $ kim._var("altura", "180cm - 5'11\"")
    $ lis._var("altura", "175cm - 5'9\"")
    $ mad._var("altura", "181cm - 5'11\"")
    $ mar._var("altura", "180cm - 5'11\"")
    $ meg._var("altura", "177cm - 5'10\"")
    $ nia._var("altura", "176cm - 5'9\"")
    $ nor._var("altura", "180cm - 5'11\"")
    $ mee._var("altura", "166cm - 5'5\"")
    $ pat._var("altura", "177cm - 5'10\"")
    $ sai._var("altura", "179cm - 5'10\"")
    $ sam._var("altura", "171cm - 5'7\"")
    $ sca._var("altura", "181cm - 5'11\"")
    $ sim._var("altura", "180cm - 5'11\"")
    $ zoe._var("altura", "174cm - 5'9\"")
    $ emm._var("birthday", "2021-07-23", "set")
    $ dap._var("birthday", "2021-07-26", "set")
    $ eri._var("birthday", "2021-07-26", "set")
    $ oma._var("birthday", "2021-06-22", "set")
    $ ama._var("birthday", "2021-06-15", "set")
    $ eva._var("birthday", "2021-06-17", "set")
    $ eva._var("age", 19, "set")
    $ ama._var("age", 19, "set")
    #$ emm._var("traits, physical", "a ella le gusta la rosa", "del")
    #$ emm._var("traits, mental", _("a ella le gusta el rosa"), "add")
    $ sam._var("job", _("enfermera"), "add")
    $ kim._var("traits, physical", "vitiligo", "add")
    if mar._var("pregnant"):
        $ mar._var("pregnancyDiscovered", True)
    if mar._var("route") and emm._var("route"):
        $ Whatif = False
        call c16s001_EmmaLessons from _call_c16s001_EmmaLessons #lewd
    else:
        call c16s001_Whatif from _call_c16s001_Whatif
    #Friday
    call c16s002_TakeMeemawDoc from _call_c16s002_TakeMeemawDoc #lewd
    call c16s002_RunWithDebbie from _call_c16s002_RunWithDebbie
    call c16s003_ShootingLessons from _call_c16s003_ShootingLessons
    call c16s003_LunchWithEva from _call_c16s003_LunchWithEva
    if mad._var("route"):
        call c16s004_DateWithMaddie from _call_c16s004_DateWithMaddie
    call c16s004_ConvoSairaAboutMegan from _call_c16s004_ConvoSairaAboutMegan
    call c16s005_PickUpMegan from _call_c16s005_PickUpMegan
    if mar._var("route"):
        call c16s006_MarPregnant from _call_c16s006_MarPregnant
    if nor._var("route"):
        call c16s007_NorPregnant from _call_c16s007_NorPregnant
    call c16s008_DinnerWithAmanda from _call_c16s008_DinnerWithAmanda
    return
label c16s001_Whatif:
    scene itchio with dissolve
    "No estás en ruta con [emm] y [mar] a la vez y hay una escena interesante que necesita las dos rutas abiertas. ¿Quieres verla?"
    menu:
        "Si":
            $ Whatif = True
            call c15s007_Night from _call_c15s007_Night_1
            call c16s001_EmmaLessons from _call_c16s001_EmmaLessons_1
            $ Whatif = False
        "No":
            pass
    return
label c16s001_EmmaLessons:
    if _in_replay:
        $ AuxReplay = False
        call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_3
        call mrS3_nor_route from _call_mrS3_nor_route_24
        call mrS3_eri_route from _call_mrS3_eri_route_27
        if not nor._var("route") and not eri._var("route"):
            menu:
                "¿Estás en una relación con alguien más aparte de [mar] y [emm]?"
                "Sí":
                    $ mc._var("relationships", 3, intention = "set")
                "No":
                    $ mc._var("relationships", 2, intention = "set")
        else:
            $ mc._var("relationships", 3, intention = "set")
        call BlinkXP ("c15s007_415" , "d") from _call_BlinkXP_3387
    if mar._var("pregnant"):
        $ mar._var("pregnancyDiscovered", True)
    play music ("music/ABCSong.ogg")
    mc "¿Pero qué estás diciendo, [mar.mc!t]?"
    mc "¿Cómo voy a enseñar a [emm] a besar contigo aquí?"
    call BlinkXP ("c16s001_005", "d") from _call_BlinkXP_1471
    mom "Bueno, yo preferiría estar para poder corregir lo que vea que hace mal. Pero si creéis que si me quedo aquí os cohibiría..."
    scene c16s001_010AnBlink #d-e Emm guiña un ojo a MC y Blink - mira a Mar tímidamente
    emm "No, Mamá, yo preferiría que estuvieras."
    emm "Si te vas, ¿cómo voy a saber si lo hago bien o no?"
    call BlinkXP ("c16s001_015", "d") from _call_BlinkXP_1472
    mom "No sé... supongo que [mc] te lo podría decir, aunque ver a mis hijos besándose... podría ser raro, ¿no?"
    if not persistent.family:
        mcp "(A partir de mañana, una vez le cuentes la verdad a [emm], ya no vas a poder decir eso. Realmente no te envidio teniendo que tener esa conversación.)"
    mcp "(No sé a lo que está jugando [emm], pero voy a seguirle el juego.)"
    mc "Si [emm] se va a sentir más cómoda contigo aquí, por mí no hay ningún problema en que te quedes."
    mc "Lo que me sorprende es que quieras que le enseñe a besar yo. ¿Eso no lo hacéis entre chicas?"
    call BlinkXP ("c16s001_020", "d") from _call_BlinkXP_1473
    mom "Bueno, sí, pero normalmente cuando somos más jóvenes que [emm]. A esta edad... pueden pasar cosas..."
    mom "[emm] es una flor tardía. 18 años y aún no ha besado a ningún chico... al menos un beso de verdad."
    call BlinkXP ("c16s001_025", "d") from _call_BlinkXP_1474
    emm "Si no fuera porque esto ha sido idea tuya, casi me enfadaría por lo que acabas de decir, Mamá."
    mc "[emm], ser una flor tardía no es nada malo. Imagínate que eres una rosa."
    call BlinkXP ("c16s001_030", "d") from _call_BlinkXP_1475
    emm "¿Puedo ser una rosa de color rosa?"
    mcp "(Me está costando horrores aguantarme la risa. [emm] está sobreactuando comportándose como una niña pequeña.)"
    mc "Sí, [emm], puedes ser una rosa rosa."
    call BlinkXP ("c16s001_035", "d") from _call_BlinkXP_1476
    emm "Entonces, ¿te quedas, Mamá? Ya sabes... para darme consejos sobre lo que hago mal."
    mc "A mí no me importa que te quedes, ya te lo he dicho. Parece que [emm] necesita tu apoyo."
    call BlinkXP ("c16s001_040", "d") from _call_BlinkXP_1477
    mom "OK. Os miraré desde el sofá y le daré las indicaciones necesarias."
    mc "¿Me dais un momento para que me quite esta ropa? Yo iba a dormir, pero creo que estas lecciones pueden ser divertidas."
    call BlinkXP ("c16s001_045", "d") from _call_BlinkXP_1478
    mom "Vale, ¿salimos de la habitación?"
    mc "¿Para qué? Las dos me visteis dormir desnudo la última vez. No vais a ver nada que no hayáis visto."
    scene c16s001_045d with dissolve
    emm "¿Te vas a desnudar? Pero yo... yo..."
    mom "No me parece correcto, [mc]. Si [emm] lo hace bien y Mjolnir empieza a crecer... no creo que haya visto ninguna... erección nunca..."
    mc "¿Ni siquiera en el porno?"
    call BlinkXP ("c16s001_050", "d") from _call_BlinkXP_1479
    emm "¿Por quién me has tomado, [mc]? ¿Por una pervertida que ve porno?"
    mcp "(No te pases, [emm]. Si yo sé que ves porno, lo más probable es que [mar.mc!t] también lo sepa.)"
    mc "Como ya os he dicho, me voy a desnudar. Mi habitación, mis normas. Dadme un segundo."
    scene c16s001_050d with fade
    mc "Ya está. ¿Cómo quieres hacerlo, Mamá?"
    mom "Pues creo que... ahí, de pie... sería lo mejor... cuando [emm] bese a su novio... los primeros besos serán... de pie, ¿no?"
    emm "A mí me parece... buena idea... así puedes... corregirme... si hago algo mal..."
    mc "Me parece bien. [emm], ven aquí."
    scene c16s001_055a with dissolve
    emm "¿Preparado para el mejor beso del mundo?"
    stop music fadeout (1.5)
    mc "Seguro que lo es, [emm]."
    play music ("music/Sexy-Background-Music.ogg")
    scene c16s001_060AnBlink with dissolve # 055a (sonrisa) d (guiño) - f beso cutre - abc sonrisa timida (Blink) mar sentada en el sofa
    "Tras guiñarte un ojo, [emm] te da posiblemente el peor beso de tu vida. Solo comparable al de [sca] en el Twins."
    emm "¿Qué tal lo he hecho?"
    mc "La abuela me besa con más pasión, [emm]."
    call BlinkXP ("c16s001_065" , "d") from _call_BlinkXP_1480
    mom "¡Por Dios, [emm]! ¡Eso se parece más a los besos que me dabas a mí cuando eras una niña que a cómo deberías besar a un chico!"
    mc "Bueno, para eso estamos aquí, ¿no? ¿Por qué no le explicas lo que ha hecho mal? Tú tenías mejor visión."
    scene c16s001_065d with dissolve
    "[mar] se enzarza en una serie de explicaciones sobre cómo poner los labios, qué hacer con la boca, cuál debe ser la actitud..."
    mom "... y ahora me voy a poner aquí. Desde el sofá no he tenido una buena visión. Aquí podré ver qué haces mal."
    scene c16s001_070AnBlink with dissolve # a (sonrisa) d (guiño) - e beso cutre - abc sonrisa timida (Blink) Con Mar detras
    "Se vuelve a repetir la secuencia y [emm] vuelve besarte mal. Aún no sabes a qué está jugando."
    emm "¿Mejor ahora?"
    call BlinkXP ("c16s001_075" , "d") from _call_BlinkXP_1481
    mc "Algo mejor... ¿no?"
    mom "Si, algo mejor, pero va a necesitar mucha práctica. A esto me refería con que no podía besar a su chico así."
    call BlinkXP ("c16s001_080" , "d") from _call_BlinkXP_1482
    emm "¿Y si lo besas tú para que yo pueda verlo?"
    mcp "(Así que es a eso a lo que estaba jugando, ¿no? [mar.mc!t] no se puede estar tragando eso, ¿verdad?)"
    call BlinkXP ("c16s001_085" , "h") from _call_BlinkXP_1483
    mom "{b}¿Estás loca?{/b} ¿Cómo voy a besarlo? ¡Es mi hijo!"
    if not persistent.family:
        mcp "(A ver cómo le explicas mañana que no lo soy y que te has negado a besarme con una excusa falsa.)"
        mcp "(Además, como si eso te importara mucho. *Risa mental*)"
    else:
        mcp "(Como si eso te importara mucho. *Risa mental*)"
    call BlinkXP ("c16s001_090" , "d") from _call_BlinkXP_1484
    emm "Porfi, porfi, porfi..." #Pretty please with sugar on top.
    mc "[emm], si le incomoda hacerlo, no la fuerces. Tiene que ser complicado para ella..."
    call BlinkXP ("c16s001_095" , "d") from _call_BlinkXP_1485
    mom "No es que me incomode o que sea complicado... es que viendo cómo te beso no va a aprender más que viendo un beso en una película."
    mc "En eso tienes razón."
    call BlinkXP ("c16s001_100" , "d") from _call_BlinkXP_1486
    emm "¿Creéis que me fijo en cómo se besan en una película? No es que me haya interesado nunca... son actores..."
    emm "Porfi, Mamá... ahora me fijaré bien en cómo lo haces tú..."
    call BlinkXP ("c16s001_105" , "d") from _call_BlinkXP_1487
    mom "¿No te importa?"
    mc "No, no me importa, Mamá. Si es por enseñar a [emm]..."
    mcp "(Si descubre que ya es una experta besando... besándome... nos va a matar a los dos.)"
    scene c16s001_115d with dissolve
    mom "Observa bien, [emm]. No lo vamos a repetir."
    emm "Entonces necesitaré que sea un beso largo, para poder verlo desde todos los ángulos."
    scene c16s001_115AnBlink with dissolve #e-sonrisa (emm detras) - fghij beso, emm en distintas posiciones - a-sin aliento - Blink
    "El beso con [mar] empieza con cierta timidez, pero va ganando en pasión tal como pasan los segundos y [emm] va dando vueltas alrededor vuestro como si estuviera tomando notas."
    mom "*Susurrando* ¡Ufff! ¡Cómo echaba de menos esto! Me has puesto cachonda con un solo beso..."
    mc "*Susurrando* Tú a mí también."
    if itchio:
        scene itchio
        "Después de eso se pasan la noche jugando al ajedrez. Sí, ajedrez para tres. Cosas más ridículas se han visto, como un gato en con el logo del desarrollador."
        mcp "(Yo no recuerdo esto así, creo que hicimos algo diferente. Seguro que si pregunto en Discord alguien me lo recuerda. Me estoy cansando de jugar tanto al ajedrez.)"
        return
    scene c16s001_115k with vpunch #polla trempada
    emm "Mamá, tienes que ser una fiera besando. Fíjate cómo se ha puesto [mc] con un solo beso."
    mc "Besa muy bien, no podrías tener una mejor maestra."
    mom "¡No mires! Aunque eso es lo que les pasa a los chicos cuando se les besa bien."
    mc "Ya la ha visto..."
    mom "Bueno, sí, pero no tiene por qué recrearse mirando."
    call BlinkXP ("c16s001_120" , "d") from _call_BlinkXP_1488
    emm "¡Ahora creo que lo haré mejor! Ya he visto cómo lo hacías y creo que ya sé lo que yo hacía mal."
    mc "[emm], mis ojos están aquí..."
    call BlinkXP ("c16s001_120b" , "d") from _call_BlinkXP_1489
    emm "Perdón... ¿probamos?"
    mc "Perfecto."
    scene c16s001_070An2Blink with dissolve #d (guiño) - e beso normal - abc sonrisa timida (Blink) Con Mar detras
    if persistent.lesbian:
        "El beso de [emm] es mucho mejor que los anteriores, pero muy lejos de sus besos habituales o de cómo te ha besado [mar]."
    else:
        "El beso de [emm] es mucho mejor que los anteriores, demostrándole a [mar] que ha aprendido la lección. Una lección que no necesitaba."
    emm "¡Ahora sí que ha ido bien! Ya he entendido qué hacía mal. Gracias, Mamá."
    mc "Mucho mejor, desde luego."
    if persistent.lesbian:
        call BlinkXP ("c16s001_125" , "d") from _call_BlinkXP_1490
        mom "Ha estado mucho mejor, pero han faltado cosas. Desde aquí parecía que no movías tu lengua dentro de la boca de [mc]. ¿Me equivoco?"
        mc "Bueno, la ha dejado bastante quieta..."
        call BlinkXP ("c16s001_125b" , "d") from _call_BlinkXP_1491
        mom "A eso es a lo que me refiero, tiene que aprender ella. No puede hacerlo mal con su chico ni esperar que sea él quien lleve la iniciativa."
        call BlinkXP ("c16s001_130" , "d") from _call_BlinkXP_1492
        emm "En vuestro beso no podía ver qué hacíais con la lengua. Y en los dibujos japoneses tienen la lengua fuera de la boca cuando se besan, pero vosotros lo habéis hecho diferente."
        scene c16s001_135a with dissolve
        emm "Se me ocurre una idea... ¿por qué no me enseñas tú lo que tengo que hacer con la lengua, Mamá?"
        scene c16s001_135b with hpunch
        mom "{b}¿Qué?{/b} ¿Quieres que {b}yo{/b} te enseñe a besar?"
        call BlinkXP ("c16s001_130b" , "d") from _call_BlinkXP_1493
        emm "Así sabría lo que tiene que hacer una chica. [mc] me podría enseñar sólo a besar como un chico..."
        mcp "(Cada vez es más difícil contenerse la risa. Creo que desde que sabe que [mar.mc!t] y yo estamos juntos ha estado buscando algo así.)"
        mc "Aunque no creyera que iba a decir esto nunca, la lógica de [emm] es correcta en este caso. *Risa*"
        call BlinkXP ("c16s001_140" , "d") from _call_BlinkXP_1494
        mom "Tienes razón. Por una vez la lógica de [emm] no tiene fallos."
        scene c16s001_135c with dissolve
        emm "¡Mamaaaa!"
        call BlinkXP ("c16s001_145" , "d") from _call_BlinkXP_1495
        mom "Sé que me voy a arrepentir de esto, pero ven aquí."
        mom "Sigue los movimientos que haga yo. Que tu lengua no pierda contacto con la mía. Pero no hagas nada brusco..."
        mom "¿Te acuerdas cuando te enseñé a amasar? Pues algo así, suave pero continuo. No se me ocurre otra forma de describirlo. Mejor te lo demuestro."
        scene c16s001_150a with dissolve
        "El beso empieza como algo tierno."
        scene c16s001_150b with dissolve
        "Pero parece que [emm] le va pillando el truco... aunque sabes que ya lo domina. Al final, casi te ha hecho pensar que necesitaba las clases."
        scene c16s001_150c with dissolve
        "Poco a poco va haciéndose más apasionado y las manos de ambas empiezan a explorar el cuerpo de la otra."
        scene c16s001_150d with dissolve
        "Nunca hubieras imaginado que pudiera ser tan tórrido verlas gemir en la boca de la otra."
        if nor._var("route") and eri._var("route"):
            "Aunque después de lo que pasó hace un par de días en la piscina, deberías haber aprendido como pueden ser las cosas."
        call BlinkXP ("c16s001_155" , "d") from _call_BlinkXP_1496
        mom "*Jadeando* Creo que ya está... ya ha aprendido lo que había que aprender..."
        mom "Ahora que repita el beso contigo aplicando lo que hemos hecho juntas..."
        scene c16s001_160An with dissolve #d (sonrisa) e (guiño) - f beso normal.  mar con la mano entre las piernas
        "Esta vez [emm] te besa como sabe hacerlo. Después de ver el espectáculo que ambas han dado notas como tu polla podría reventar en cualquier momento."
        "Si a eso le sumas que puedes notar el calor que emana de la entrepierna de [emm] a través de la fina tela de su pijama, y que parece que [mar] también se está poniendo cachonda..."
        call BlinkXP ("c16s001_160" , "d") from _call_BlinkXP_1497
        emm "¡Wow! Ahora lo entiendo todo. Mamá es una maestra genial. ¿Lo he hecho bien?"
        mc "Lo has hecho genial ahora, [emm]."
    call BlinkXP ("c16s001_165" , "d") from _call_BlinkXP_1498 #emm se gira, mar con una mano entre las piernas
    emm "¿Lo he hecho bien, Mami?"
    mom "Sí, muy bien, cielo. Ha sido... muy bonito veros besaros..."
    emm "¿Tu conejito también tiene calor, Mamá?"
    call BlinkXP ("c16s001_170" , "h") from _call_BlinkXP_1499
    mom "{b}¿Qué?{/b}"
    if persistent.lesbian:
        emm "Hace calor en esta habitación. Después de nuestro beso he empezado a notar que mi conejito se ponía caliente y a sudar..."
        emm "Y ahora, con el beso con [mc]... parece que tenga fiebre..."
    else:
        emm "Hace calor en esta habitación. Durante el beso he empezado a notar que mi conejito se ponía caliente y a sudar..."
    emm "Veo que el tuyo también está pasando calor, Mamá. Te lo estás tocando..."
    mc "*Risa* Es cierto que hace calor en esta habitación. Por eso duermo desnudo."
    scene c16s001_175AnBlink with dissolve #d-e-se mira la mano - Mira a MC y la retira Blink con H
    mom "¿Qué? ¡No!... Digo... Sí... hace calor en esta habitación... al estar debajo del tejado es la habitación más... caliente... de la casa. ¿Verdad, [mc]?"
    call BlinkXP ("c16s001_180" , "h") from _call_BlinkXP_1500
    mom "¿Qué estás haciendo, [emm]?"
    scene c16s001_185An with dissolve #abc
    emm "Desnudarme yo también. Ya has oído a [mc] y lo acabas de reconocer. Hace calor aquí y mi conejito está ardiendo y sudando."
    mc "*Risa* No me refería a que os tuvierais que desnudar vosotras, [emm]."
    call BlinkXP ("c16s001_190" , "d") from _call_BlinkXP_1501 #Mjolnir con líquido preseminal
    emm "Y tu zanahoria también está sudando... No sabía que las zanahorias sudaran..."
    mc "*Risa* No es sudor, [emm]..."
    mcp "(Me siento ridículo explicándole cosas que sabe perfectamente, pero quiero ver a dónde quiere llegar con este juego.)"
    mc "Eso es lo que pasa cuando a un chico le besan muy bien."
    call BlinkXP ("c16s001_195" , "d") from _call_BlinkXP_1502
    mom "*Mascullando para sí misma* Esto se me está yendo de las manos... no es lo que había pensado..."
    mom "Bueno, creo que con esto hemos llegado al final de la clase de hoy. Está claro que ya has aprendido a besar. ¡Vístete, [emm]! Nos vamos."
    scene c16s001_190bAn with dissolve #c-b-a-d-repeat polla arriba, b, polla en medio, a polla abajo
    emm "¿Es normal que se ponga tan duro? Parece que tienes una rampa..."
    mc "Sí, es normal. Ya te digo que cuando a un chico le besan tan bien pasan estas cosas."
    emm "Y ¿duele?"
    mc "No, ahora mismo no, pero si se pasa así mucho tiempo sin... bueno... si se pasa así mucho tiempo, puede doler un poco, pero más bien lo que duelen los..."
    emm "¿Los champiñones?"
    call BlinkXP ("c16s001_200" , "h") from _call_BlinkXP_1503
    mom "{b}¡[emm]!{/b} ¡Deja de tocarle la polla a tu hermano! Vamos a irnos y a dejarle... arreglarlo por él mismo..."
    call BlinkXP ("c16s001_205" , "d") from _call_BlinkXP_1504
    mom "*Susurrando* Lo siento..."
    call BlinkXP ("c16s001_210" , "d") from _call_BlinkXP_1505 #de rodillas con la polla en la mano
    emm "Pero Mamá, no podemos irnos y dejar a su zanahoria así y que después le duelan los champiñones."
    emm "¿Hay algo que pueda hacer para solucionarlo? Ya que lo he provocado yo..."
    call BlinkXP ("c16s001_200b" , "h") from _call_BlinkXP_1506
    mom "{b}¡[emm]! ¿Qué crees que estás haciendo?{/b}"
    scene c16s001_210d with dissolve
    emm "Quizás dándole un besito..."
    call BlinkXP ("c16s001_200b" , "h") from _call_BlinkXP_1507
    mom "{b}¡[emm]!{/b}"
    call BlinkXP ("c16s001_210" , "d") from _call_BlinkXP_1508
    emm "¿Qué? Parece que le ha gustado. Ha saltado de alegría en mi mano cuando le he dado un besito... Además se está poniendo más duro aún."
    mc "*Risa* Sí, le ha gustado. Y lo de ponerse más duro es normal cuando le besa una preciosa chica desnuda."
    emm "¿No podemos hacer nada para ayudarle, Mamá?"
    call BlinkXP ("c16s001_215" , "d") from _call_BlinkXP_1509
    mom "*Susurrando* ¿Qué quieres hacer?"
    mc "*Encogiéndose de hombros* Tú misma, tú has empezado esto de las lecciones..."
    mom "Vale, quédate donde estás... *Entre dientes* Se me ha ido totalmente de las manos..."
    scene c16s001_220a with dissolve
    mom "Escúchame, [emm]. Tienes que cogerle la... mira, me niego a llamarle zanahoria... tienes que cogerle la polla rodeándola con los dedos."
    emm "¿Y con eso dejará de dolerle?"
    mom "No, tienes que subir y bajar la mano, desde la base hasta la punta... creo que con eso habrá suficiente..."
    scene c16s001_225pv with dissolve
    show c16s001_225v with dissolve
    emm "¿Así, Mamá?"
    mom "Exactamente así, [emm]. [mc] te indicará si quiere que hagas más presión o no."
    emm "¿Te gusta así, [mc]?"
    mc "Sí, me está gustando mucho, pero puedes hacer un poco más de presión."
    scene c16s001_230pv with dissolve
    hide c16s001_225v with dissolve
    show c16s001_230v with dissolve
    emm "Mamá, ¿tu conejito te está dando calor todavía? Como has vuelto a tocártelo..."
    mom "A mi conejito le gusta ver como uno de mis hijos le da placer al otro..."
    if not persistent.family:
        mcp "(Cada vez te entiendo más. Me da lo mismo que unos papeles digan que no eres mi madre y que [emm] no es mi hermana.)"
    emm "Y si tocarte te ayuda... [mc], ¿dejarías que Mamá se desnudara en tu habitación?"
    mc "Solo si ella quiere."
    emm "¿Yo también puedo tocarme el conejito? Cada vez está sudando más... y tengo una mano libre..."
    scene c16s001_235a with dissolve
    hide c16s001_230v with dissolve
    mom "Entonces vamos a la siguiente lección para que tengas las dos manos ocupadas..."
    mc "¿Siguiente lección? ¿No crees que vas un poco rápido?"
    scene c16s001_235b with hpunch
    emm "¡Tú calla, [mc]! No soy [dap], pero me gusta aprender. Estas lecciones están siendo mucho más divertidas que las que me van a enseñar en la Universidad."
    mom "Siéntate, [mc]."
    scene c16s001_235c with fade
    emm "¿Qué quieres que haga ahora, Mamá?"
    mom "Ahora te vas a poner entre sus piernas y vas a rodear su polla con tus tetas. Pondrás una mano a cada lado y así podrás controlar la presión."
    mom "Y entonces haces los mismos movimientos que hacías con la mano, arriba y abajo, pero acompañando con todo el cuerpo."
    emm "Eso suena divertido."
    scene c16s001_240pv with dissolve
    show c16s001_240v with dissolve
    "[emm] empieza a hacer lo que [mar] le ha pedido, pero no lo hace muy bien."
    "Por primera vez en la noche, no sabes si es que no sabe hacerlo o está fingiendo. Es la primera vez que hace una cubana."
    emm "¿Así va bien, Mamá?"
    mom "No demasiado, creo que no estás ejerciendo la presión correcta. Aprieta un poco más..."
    emm "¿Por qué no me enseñas tú? Como antes con el beso... ha ido muy bien... Ya sabes que yo aprendo mejor si lo veo que si me lo explican..."
    mc "Pero para eso deberías desnudarte... al menos quitarte la parte de arriba..."
    scene c16s001_245An #cba mira a emm y a MC
    hide c16s001_240v with dissolve
    mom "Sabéis que sois imposibles, ¿verdad? Esto está yendo mucho más lejos de lo que yo había planeado para la primera lección."
    mc "¿La primera? ¿Tenías pensado que hubiera más lecciones?"
    scene c16s001_250AnBlink with dissolve #def se desnuda de cintura para arriba - Blink
    mom "Sí, había pensado que tal como fuerais... como [emm] y su novio fueran avanzando, ir explicándole más cosas."
    mcp "(¿Fuerais? ¡Sabe que [emm] y yo estamos juntos! ¿Cómo? ¿Desde cuándo?)"
    mom "Pero tampoco está tan mal hacer esto para que sepa algo más ¿no?"
    mc "Desde luego que no..."
    mom "*Susurrando para sí misma* Tan solo espero que no quieras llegar hasta el final con ella."
    call BlinkXP ("c16s001_255" , "d") from _call_BlinkXP_1510
    mom "A ver, [emm], déjame un hueco y te lo enseño."
    scene c16s001_260pv with dissolve
    show c16s001_260v with dissolve
    mom "¿Ves, cielo? Así es como tienes que hacerlo. Con la presión suficiente para que él note como tus tetas se deslizan por toda la longitud de su polla."
    emm "Interesante... ¿sabéis que estáis muy sexys haciendo esto juntos?"
    mom "Lo sé, cielo. Vosotros también lo estabais... Ahora te toca a ti. Diría que le falta poco para llegar."
    mc "Aún me queda un poco, pero me estoy acercando. Las dos estáis muy sexys así."
    if persistent.lesbian:
        scene c16s001_265a with dissolve
        hide c16s001_260v with dissolve
        emm "¿Por qué no haces tú la presión en mis tetas, Mamá? Las tuyas son mucho más grandes..."
        mom "¿Eso te gustaría, [mc]?"
        mc "Seguro que sería muy caliente. Y tú sabes cuánta presión ejercer mejor que ella..."
        scene c16s001_265b with dissolve
        mom "Ponte en posición, [emm]. Vamos a darle un... otro espectáculo a tu hermano."
        emm "A los chicos le gusta que las chicas jueguen entre ellas, ¿verdad?"
        mc "Por supuesto, pero solo cuando podemos participar."
        emm "Entonces tengo una idea para luego..."
        scene c16s001_270pv with fade
        mom "¿Ves? Te pones así, y esta es la presión que tienes que hacer. Ahora ve moviéndote poco a poco, arriba y abajo, como he hecho yo."
        show c16s001_270v with dissolve
        mom "No te olvides de mirarle a los ojos."
        mom "A los chicos les gusta el contacto visual mientras les haces esto."
        mc "Nos encanta. Y estáis increíbles las dos así."
        emm "¿Ahora puedo jugar con mi conejito? Ha empezado a picarme, y sigue caliente... y cada vez suda más"
        mc "Sí... eso hará más impresionantes las vistas..." (multiple=2)
        mom "¡No! Bueno... si a tu hermano le gusta... hazlo..." (multiple=2)
        scene c16s001_265c with hpunch
        hide c16s001_270v with dissolve
        mom "*Suspiro de sorpresa* ¿Qué haces [emm]? *Gemido*"
        emm "Si mi conejito está así, suponía que el tuyo también. Y no me equivocaba... está tan caliente como el mío, y tienes el pijama empapado..."
        mc "¡Dios mío, [emm]! Eso ha sido increíble... Aunque Mamá te diga que pares no lo hagas."
        scene c16s001_275pv with dissolve
        show c16s001_275v with dissolve
        emm "No pensaba hacerlo... *Gemido* su conejito está sudando igual que el mío... y al mío le está yendo muy bien..."
        mom "*Gemido* Yo tampoco te iba a pedir que parases... *Jadeo* Hemos dicho que le daríamos *Gemido* un espectáculo a [mc]..."
        mc "Y lo estáis consiguiendo. El mejor espectáculo de la historia... estoy a punto de correrme..."
        mom "*Gemido* A mí aún me queda un poco..."
        emm "*Jadeo* A mí me están entrando ganas de ir a hacer pipí... *Gemido* pero estando entre los dos... no puedo..."
        mom "*Gemido* No es pipí, mi amor. Vas a tener un orgasmo..."
        "Por mucho que lo sientas, te gustaría alargar la escena hasta que las dos se corrieran, no puedes aguantar más. Estás a punto de explotar."
    else:
        emm "Entonces ¿continúo yo?"
        scene c16s001_265b with dissolve
        hide c16s001_260v with dissolve
        mom "Ponte en posición, [emm]. Vas a darle un placer increíble a tu hermano."
        scene c16s001_280pv with fade
        show c16s001_280v with dissolve
        mom "No te olvides de mirarle a los ojos."
        mom "A los chicos les gusta el contacto visual mientras les haces esto."
        mc "Nos encanta. Y estáis increíbles las dos así."
        emm "Pone caras divertidas... *Gemido* ¡Oops! Se me ha escapado ese gemidito..."
        mom "Es normal, cielo. *Gemido* Los pechos son un lugar muy sensible..."
        emm "¿Tú también gimes? *Jadeo* Pero tú ya no estás haciendo esto..."
        mc "Ella está jugando con su conejito mientras tú lo haces, [emm]."
        mom "No puedo evitarlo... *Gemido* estáis tan sexys..."
        emm "Es injusto... *Gemido* Yo quiero que alguien juegue con el mío..."
        "Por mucho que lo sientas, te gustaría alargar la escena hasta que se corriera, no puedes aguantar más. Tendrás que usar otros métodos para que lo haga. Y [emm] también."
        "La pregunta que asalta tu cerebro es si te dejarán hacerlo."
        mc "Chicas, es el mejor espectáculo de la historia... pero estoy a punto de correrme..."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        if persistent.lesbian:
            $ wt2 = _("Posible beso blanco.")
        else:
            $ wt2 = _("Posible beso blanco sin contenido lésbico.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte en el pecho de [emm]." (wt = wt1):
            $ Aux = 1
            call c16s001_CumOnEmmChest from _call_c16s001_CumOnEmmChest
        "Correrte en la cara de las dos." (wt = wt1):
            $ Aux = 2
            call c16s001_CumOnBothFaces from _call_c16s001_CumOnBothFaces
        "Correrte en la boca de [mar]." (wt = wt2):
            call c16s001_CumInMarMouth from _call_c16s001_CumInMarMouth
    $ resetWalkthrough ()
    scene c16s001_315a with fade
    emm "Pues ya han acabado las lecciones por hoy, ¿no?"
    mom "Sí, creo que no hay nada más que hacer por esta noche..."
    mc "Yo creo que sí. Hay un par de conejitos que lo estaban pasando mal. Vosotras me habéis dado mucho placer y creo que me toca a mí dároslo a vosotras."
    scene c16s001_315b with hpunch
    emm "¡Sí!"
    mom "¿Estás seguro? Quieres hacerle a [emm] lo que te ha hecho ella."
    mc "Bueno, yo no tengo tetas, pero sí. Y no solo a [emm], el tuyo también estaba... sudando, ¿no? *Risa*"
    mom "No sé si es buena idea..."
    scene c16s001_315c with dissolve
    emm "¡Venga, Mamá! No seas aguafiestas..."
    mom "Bueno... puedes empezar con [emm] si quieres... así también aprende como un hombre puede darle placer."
    mc "[emm], ponte aquí, tumbada."
    call BlinkXP ("c16s001_320" , "f") from _call_BlinkXP_1511
    emm "¿Así?"
    mc "Perfecta..."
    scene c16s001_325pv with dissolve
    show c16s001_325v with dissolve #mar de espaldas viendo como mc come el coño a emm
    emm "*Gemido* ¡Ufff!"
    mom "¿Te gusta, cielo?"
    emm "*Gemido* Es alucinante... *Jadeo* ¿Por qué no te quitas los pantalones y te tumbas con nosotros?"
    mom "No sé si..."
    emm "*Jadeo* Hazlo, Mamá... tú has empezado esto y *Gemido* está siendo de las mejores noches de mi vida..."
    scene c16s001_330An with dissolve #abcd se desnuda y se tumba
    hide c16s001_325v with dissolve
    mom "Vale... realmente me estoy poniendo cach... mi conejito se está poniendo aún más caliente viéndoos."
    emm "*Gemido* Pues acarícialo... seguro que se calma..."
    scene c16s001_335pv with dissolve
    show c16s001_335v with dissolve #Angulo con [mar] masturbándose mientras [mc] come coño
    emm "*Gemido* Estás super sexy así, Mamá... *Jadeo* No me extraña que los hombres pierdan la cabeza por ti..."
    mom "*Jadeo* Tú también estás guapísima mientras tu hermano te da placer... *Gemido* Hacéis una pareja perfecta..."
    emm "*Gemido* Lo que [mc] le está haciendo a mi conejito es alucinante... *Jadeo* Creo que me voy a hacer pipí, Mamá..."
    mom "*Jadeo* Eso es bueno, cielo... se llama correrse y es el objetivo de lo que te está haciendo... "
    mom "*Gemido* Déjame ver cómo te corres, cielo... *Jadeo* quiero ver como disfrutas..."
    call OrgasmX ("c16s001_340") from _call_OrgasmX_28
    emm "¡Oh, sí! *GEMIDO* ¡JODER! *JADEO* ¡No pares!"
    "El cuerpo de [emm] explota en tus manos, en tu boca, ante tus ojos."
    emm "¡Sigue así, mi amor! *JADEO* ¡No puedo parar de correrme!"
    scene c16s001_345a with dissolve
    if persistent.family:
        "[mar] abandona su propio placer para tomar a su hija entre sus brazos mientras oleada tras oleada de sus orgasmos recorren su cuerpo."
    else:
        "[mar] abandona su propio placer para tomar a la niña que ha criado como una hija entre sus brazos, mientras oleada tras oleada de sus orgasmos recorren su cuerpo."
    mom "Disfruta el momento, mi niña, nunca olvides que te queremos."
    emm "*Susurrando* Te has quedado sin tu orgasmo..."
    mom "No importa, cariño. Lo que importa es que tú has disfrutado."
    scene c16s001_345b with dissolve
    emm "Dile a [mc] que te haga lo mismo que me ha hecho a mí. Te has quedado a medias..."
    mom "No hace falta, [mc], en serio... déjame disfrutar de este momento con mi niña..."
    scene c16s001_345c with dissolve
    emm "No me importa, de verdad. *Susurro* Sé que estáis juntos."
    mom "*Susurro* Yo también sé que lo estáis vosotros."
    scene c16s001_350a with hpunch
    emm "{b}¿Qué?{/b}"
    mom "Hace más de diez años que no decías conejito. No creerías que me ibas a engañar. Soy tu madre. Vuestra madre."
    if not persistent.family:
        mom "*Entre dientes* Le pese a quien le pese y digan lo que digan."
    mom "Llevo días viendo como os miráis. Te mira cómo me mira a mí. Cualquiera con ojos puede ver que está enamorado de ti."
    mc "Mamá..."
    scene c16s001_350b with dissolve
    mom "No pasa nada, cielo... he disfrutado muchísimo viendo a mis hijos juntos por primera vez."
    emm "Y me vas a negar ese mismo placer, el de ver a mi madre y a mi hermano juntos por primera vez, ¿verdad?"
    scene c16s001_350c with dissolve
    mom "¿Realmente quieres ver eso, [emm]?"
    emm "¿Por qué crees que he estado fingiendo todo este rato? Hace casi una semana que sé lo vuestro. Llevo cuatro días planeando algo como esto."
    emm "No sabía ni por dónde empezar hasta que has venido con la idea de las lecciones de besos."
    emm "Y ahora quiero ver como mi hermano le hace a mi madre lo que me acaba de hacer a mí."
    scene c16s001_350d with dissolve
    emm "¿Lo harías por mí, [mc]? ¿Por nosotras?"
    mc "Por supuesto, no podemos dejar a Mamá a medias, ¿verdad?"
    mom "Pero a mí se me ha bajado un poco el calentón..."
    scene c16s001_350e with dissolve
    emm "Pues empieza otra vez desde el principio, con los besos."
    mom "No sé..."
    mc "Ven aquí, mi amor."
    scene c16s001_350f with dissolve
    mom "¿Yo?" (multiple=2)
    emm "¿Mamá o yo?" (multiple=2)
    scene c16s001_350g with dissolve
    mom "*Risa*" (multiple=2)
    emm "*Risa* Creo que es ella." (multiple=2)
    mc "*Risa* Mamá..."
    scene c16s001_355An with dissolve #a-d-b-c
    "[mar] se lanza a tus brazos, a tus labios. Está ansiosa por recibir besos, cariños, caricias."
    "Tú estás ansioso por dárselos."
    "El calor que puedes notar irradiando de su entrepierna niega su mentira de que se le ha pasado el calentón."
    "Al acabar el primer beso, Mjolnir está totalmente despierto."
    call BlinkXP ("c16s001_360" , "d") from _call_BlinkXP_1512
    mom "Hazme el amor con ternura, mi vida."
    mc "Creía que..."
    mom "Necesito que me hagas el amor."
    "La voz con la que te lo dice te parte el alma. Es una voz llena de miedo, tristeza y pérdida. La charla de mañana con [emm] la tiene que tener asustada."
    "Comprendes entonces por qué ésto está pasando esta noche. Por qué hoy, el día en que habéis decidido que hay que contarles el secreto a las chicas."
    if not persistent.family:
        "[emm] dejará de ser su hija mañana."
    scene c16s001_365pv with dissolve
    show c16s001_365v
    "[mar] se tumba en la cama, en la posición que descubrió que era su favorita días atrás."
    "La penetras suavemente, con gentileza, con ternura tal como ella te ha pedido. Pero también con energía."
    mom "Así, suavemente... te quiero, mi amor. Os quiero a los dos..."
    mc "Y nosotros a ti, [mar.name.lewd!t]."
    "En el borde de tu campo de visión, puedes ver como [emm] cambia de posición a una en la que tenga una mejor visión."
    scene c16s001_370pv with dissolve
    hide c16s001_365v
    show c16s001_370v
    emm "Estáis increíbles así... *Gemido* Es lo más sexy que he visto nunca..."
    "No puedes saber si [emm] es consciente que ha empezado a masturbarse, pero es increíblemente bonito hacerle el amor a [mar] mientras [emm] mira."
    "La noche antes de que, posiblemente, todo cambie para no volver a ser nunca lo mismo."
    mom "*Gemido* Sigue así... lento... *Jadeo* profundo... con cariño..."
    mom "*Jadeo* Quiero que esta noche *Gemido* dure para siempre..."
    "Notas como, a cada embestida, la vagina de [mar] se estrecha más. Como se cierra sobre tu astil con fuerza cada vez que retrocedes, como si no quisiera dejarte ir."
    "Es una sensación maravillosa."
    emm "Me estoy poniendo super cachonda de veros. *Jadeo*"
    mom "Dame la mano, mi vida..."
    emm "¿Yo?" (multiple=2)
    mc "¿Yo?" (multiple=2)
    emm "*Risa* Vale, soy yo." (multiple=2)
    mc "Eres tú, [emm]. *Risa*" (multiple=2)
    scene c16s001_375pv with dissolve
    hide c16s001_370v
    show c16s001_375v
    "Las dos mujeres entrelazan sus manos mientras tú sigues bombeando. Es una escena preciosa que no olvidarás nunca."
    mom "*Gemido* Estoy a punto de llegar, cielo."
    emm "*Jadeo* Yo también... esto es demasiado caliente..."
    mc "Yo tampoco voy a poder aguantar mucho más..."
    emm "*Gemido* Corrámonos los tres juntos. *Jadeo* Sería increíble. *Gemido* La familia corriéndose a la vez."
    "Cuando [emm] ha pronunciado la palabra familia el coño de [mar] se ha contraído con fuerza. En otras circunstancias estarías seguro de que ha sido un pequeño orgasmo."
    mom "*Gemido* Córrete dentro de mí, [mc], por favor."
    call OrgasmX ("c16s001_380") from _call_OrgasmX_29
    "En ese momento llega el orgasmo de [emm]."
    emm "¡Oh, sí! *JADEO* ¡Es la mejor paja que me he hecho nunca! *Gemido* ¡JODER!"
    "Ya te has acostumbrado a sus orgasmos explosivos y no te sorprende el borbotón de líquido que sale de dentro de tu hermana."
    if not persistent.family:
        "Siempre lo será, pase lo que pase mañana."
    call OrgasmX ("c16s001_385") from _call_OrgasmX_30
    if persistent.family:
        mom "¡Llena a tu madre con tu semilla! *JADEO* ¡Me corroooo!"
    else:
        mom "¡Lléname con tu semilla! *JADEO* ¡Me corroooo!"
    "En seguida llega el de [mar] que te arrastra al tuyo con sus contracciones, sin darte tiempo de pensar en dónde correrte."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("[mar] embarazada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt = wt1):
            pass
        "Correrte dentro. Ir a por el bebé" (wt = wt2) if persistent.pregnancy and not mar._var("pregnant"):
            if not Whatif:
                $ mar._var("pregnant", True)
            play sound ("music/OldMusicBox5.ogg")
    $ resetWalkthrough ()
    call OrgasmX ("c16s001_390") from _call_OrgasmX_31
    mc "¡Mpfft!"
    "Explotas en dentro de [mar], inundando su vagina con tu semen, en uno de los mejores orgasmos que has tenido."
    mom "¡Lléname!"
    emm "¡Déjala embarazada! ¡Dame un hermanito!"
    "Tu descarga es enorme, aún más teniendo en cuenta que es tu segundo orgasmo de la noche. Cuando la última oleada de [mar] finaliza, sales de su interior y te las quedas mirando."
    scene c16s001_395d with dissolve
    "Unas vistas preciosas."
    mc "Ha sido increíble. Veros a las dos disfrutando a la vez... indescriptible..."
    mom "Ha sido precioso."
    emm "Y super sexy. Tenemos que repetirlo."
    emm "Pero ahora hay algo que quiero hacer..."
    mc "¡Sorpréndenos! *Risa*"
    call BlinkXP ("c16s001_395" , "d") from _call_BlinkXP_1513 #entre las piernas del MC con la polla en la mano
    emm "Mamá siempre dice que no hay que desperdiciar comida y que hay que dejarlo todo limpio, ¿no? *Risita*"
    scene c16s001_395e with dissolve #engulle la polla
    mom "Esta niña entiende lo que quiere. *Risa*"
    mc "A mí la verdad es que no me desagrada la limpieza que está haciendo. Es más, me encanta."
    emm "*Sonidos afirmativos*"
    scene c16s001_400 with dissolve
    emm "Vuestras corridas combinadas tienen un sabor extraño, pero muy agradable."
    if persistent.lesbian:
        emm "¿Puedo limpiarte también a ti, Mamá?"
        call BlinkXP ("c16s001_405" , "h") from _call_BlinkXP_1514
        mom "¿Qué? ¿Te ponen esas cosas?"
        mc "Bueno, creo que está en modo limpieza. *Risa* Le ha pillado el gusto a limpiar en mi habitación."
        scene c16s001_410AnBlink with dissolve #d- parpadea
        emm "De eso ya hablaremos..."
        emm "Si te refieres a si me van las chicas. No, para nada. Pero tú no eres una chica. Tú eres mi madre y... la experiencia de hoy... "
        menu:
            "Límpiala, [emm].":
                mc "Estoy seguro de que le va a gustar."
                call BlinkXP ("c16s001_415" , "d") from _call_BlinkXP_1515
                call c16s001_MyGirl from _call_c16s001_MyGirl
                scene c16s001_420An with dissolve #ab
                emm "Eso es un sí, ¿no?"
                mc "*Risa* ¡Así me gusta, [emm]! No hace falta que esperes respuesta, no vaya a ser que te digan lo que no quieres oír."
                scene c16s001_420An2 with dissolve
                mom "*Gemido* ¡Uff, [emm]!"
                emm "*Slurp-Slurp*"
                mc "Ya te he dicho que te iba a gustar."
                scene c16s001_420d with dissolve
                emm "Limpieza hecha."
            "No creo que le guste, [emm].":
                call BlinkXP ("c16s001_415" , "d") from _call_BlinkXP_1516
                mom "Por mucho que me guste estrechar lazos con mis hijos, todavía hay unos límites que no estoy preparada para cruzar."
                call c16s001_MyGirl from _call_c16s001_MyGirl_1
                mom "Aún así... mejor no."
                scene c16s001_410a with dissolve
                emm "Es una lástima, porque se ve super apetitoso. Pero otra vez será."
    emm "Voy a coger tu albornoz, [mc]. Tengo que ir un momento al lavabo y no quiero ponerme el pijama."
    emm "Y antes de que preguntes, Mamá, sí, me voy a quedar a dormir. Y sí, voy a dormir desnuda."
    call BlinkXP ("c16s001_425" , "d") from _call_BlinkXP_1517
    mom "No pensaba preguntarlo, sino proponerlo. *Risita*"
    mc "Va, [emm]. Te esperamos aquí."
    call BlinkXP ("c16s001_430" , "d") from _call_BlinkXP_1518
    emm "Ahora vuelvo. No empecéis la segunda ronda sin mí. *Risita*"
    stop music fadeout (1.5)
    mc "Creo que Mamá necesita más cariño que sexo ahora mismo. La segunda ronda la podemos dejar para otra ocasión."
    play music ("music/Emotional-Piano-Sad.ogg")
    call BlinkXP ("c16s001_435" , "f") from _call_BlinkXP_1519
    "Una vez [emm] se ha ido..."
    mc "¿Cómo estás, [mar.mc!t]?"
    mom "En una nube... ha sido increíble."
    mc "No me refiero a eso, sé por qué has hecho esto específicamente hoy. Repito la pregunta ¿Cómo estás?"
    call BlinkXP ("c16s001_440" , "d") from _call_BlinkXP_1520
    mom "Me siento rara... sé que hoy hemos estrechado lazos los tres de una forma que no habíamos hecho antes... pero... mañana todo puede cambiar."
    mom "Ya conoces a [emm], se puede enfadar... mucho... cuando descubra que le hemos ocultado cosas toda su vida..."
    if not persistent.family:
        mom "Que le hemos ocultado que no soy su madre, que tú no eres su hermano..."
    scene c16s001_440d with dissolve
    mc "[emm] ya es una adulta, y en los últimos días ha cambiado mucho. Ya no se enfada {b}tanto{/b} como antes."
    call BlinkXP ("c16s001_445" , "d") from _call_BlinkXP_1521
    mom "*Risa* El poder sanador de Mjolnir, supongo."
    mc "*Risa* Supongo..."
    mc "Pero tengo una pregunta... al principio parecías reluctante a quedarte, pero tu plan era quedarte desde el principio, ¿no?"
    call BlinkXP ("c16s001_450" , "d") from _call_BlinkXP_1522
    mom "Claro, pero no me podía imponer. Sabía que estabais juntos, pero no hasta dónde habíais llegado."
    mom "Si me hubiera impuesto, tú habrías sospechado algo. Incluso [emm] podría haber sospechado. Por eso estaba jugando el papel de \"debería quedarme, pero sería raro\"."
    mc "*Risa* Eres taimada."
    call BlinkXP ("c16s001_455" , "d") from _call_BlinkXP_1523
    mom "Tenía que serlo. Tenía que pasar hoy. Es posible que [emm] no nos dirija la palabra a ninguno a partir de mañana..."
    mc "Lo hará. Tiene que comer y le tienes que dar la semanada. *Risa*"
    mom "Estoy hablando en serio, [mc]."
    mom "En el momento en que [emm] ha empezado a actuar como una niña pequeña e inocente, sabía que tenía ganada la partida. Y que habíais llegado más lejos de lo que pensaba."
    mc "Nunca ganará un Oscar, ¿verdad?"
    call BlinkXP ("c16s001_445" , "d") from _call_BlinkXP_1524
    mom "*Risa* Desde luego que no."
    call BlinkXP ("c16s001_460" , "d") from _call_BlinkXP_1525
    mom "Pero me ha sorprendido lo natural que ha salido todo... y como ha actuado [emm]."
    if persistent.lesbian:
        mom "Que empezara a masturbarme mientras te hacíamos la cubana ha sido sorprendente. Que quisiera limpiarme tu corrida casi hace que me explote la cabeza."
    mom "Ella también tenía sus planes... aunque ya conocemos cómo suelen funcionar los planes de [emm]."
    mc "Cómo suelen {b}NO{/b} funcionar. *Risa*"
    mom "Yo tampoco ganaré un premio a los mejores planes. Mi plan no incluía que mi hijo acabara follándome delante de mi hija."
    call BlinkXP ("c16s001_465" , "d") from _call_BlinkXP_1526
    mom "¿Puedo pedirte un favor?"
    mc "Lo que quieras."
    mom "¿Puedo dormir en medio hoy?"
    mc "¿Quieres ser como una gallina con sus polluelos bajo las alas?"
    mom "En cierto modo..."
    mc "No hay ningún problema. Entiendo que lo necesites."
    call BlinkXP ("c16s001_470" , "f") from _call_BlinkXP_1527
    emm "¿Qué pasa? ¿Me toca dormir en el rincón?"
    mc "¿Dónde querías dormir?"
    emm "Abrazada a ti, como la otra vez."
    mc "Eso seguía siendo el rincón, [emm]. Esta vez te toca dormir abrazada a Mamá."
    call BlinkXP ("c16s001_475" , "d") from _call_BlinkXP_1528
    emm "También me sirve. Hacedme un hueco."
    if persistent.lesbian:
        scene c16s001_480An1 with dissolve #a (emm-MC) b (emm-mar) c (MC-mar) d abrazados
    else:
        scene c16s001_480An2 with dissolve #a (emm-MC) e (emm-mar mejilla) c (MC-mar) d abrazados
    "Después de los besos de buenas noches os quedáis los tres abrazados."
    mom "Buenas noches, hijos. Os quiero."
    emm "Y nosotros a ti." (multiple=2)
    mc "Nosotros también te queremos." (multiple=2)
    emm "¿Repetimos mañana? ¿Todas las noches?"
    mom "Mañana va a ser un día largo... hay que hacer muchas cosas..."
    mc "No planeemos nada. Ya veremos."
    scene black with dissolve
    "Apagáis la luz y os quedáis dormidos en seguida."
    "Ha sido la primera noche de muchas que pasarán en los años venideros."
    if mc._var("relationships") > 2:
        "A veces se unirá alguna otra chica, pero las noches a solas con [emm] y [mar] siempre serán memorables."
    "Una madre con sus dos hijos, haciéndose felices entre todos."
    if not persistent.family:
        "Sin que importe lo que la sangre tenga que decir sobre lo que sois."
    emm "*Susurrando* ¡El mejor regalo de cumpleaños de la historia!"
    stop music fadeout (1.5)
    return
label c16s001_CumOnEmmChest:
    if persistent.lesbian:
        call OrgasmX ("c16s001_285a") from _call_OrgasmX_32
        mc "¡Mpfft!"
        "Explotas entre las tetas de [emm], dibujando un hermoso cuadro que salpica las manos de [mar]."
        emm "¡Cuánta leche!"
        mom "¡Y qué caliente!"
        scene c16s001_280a with dissolve
        call c16s001_Text1 from _call_c16s001_Text1
        emm "Pero casi no te queda..."
        scene c16s001_285An1 with dissolve #mar chupa teta de emm a-j
    else:
        call OrgasmX ("c16s001_285b") from _call_OrgasmX_33
        mc "¡Mpfft!"
        "Explotas entre las tetas de [emm], dibujando un hermoso cuadro que empieza a resbalar por las curvas de su pecho."
        emm "¡Cuánta leche!"
        mom "¿Está caliente cielo?"
        emm "Mucho..."
        scene c16s001_280b with dissolve
        call c16s001_Text1 from _call_c16s001_Text1_1
        emm "Pero a ti no te ha manchado..."
        scene c16s001_285An2 with dissolve #mar coge con el dedo semen del pecho de [emm] y se lo lleva a la boca (280d) b-c-d
    call c16s001_Text2 from _call_c16s001_Text2
    return
label c16s001_CumOnBothFaces:
    mc "Poneos juntas... quiero pintaros la cara..."
    call OrgasmX ("c16s001_285c") from _call_OrgasmX_34
    mc "¡Mpfft!"
    "Explotas dividiendo tu corrida entre las caras de tus amantes, dibujando un nuevo tipo de maquillaje que sabes que nunca se pondrá de moda."
    emm "¡Cuánta leche!"
    mom "¡Y qué caliente!"
    scene c16s001_280c with dissolve
    call c16s001_Text1 from _call_c16s001_Text1_2
    emm "Pero a ti te ha manchado menos..."
    if persistent.lesbian:
        scene c16s001_285An3 with dissolve #mar chupa cara de emm e-i
    else:
        scene c16s001_285An4 with dissolve #mar coge con el dedo semen del cara de [emm] y se lo lleva a la boca (280g) f-g-h
    call c16s001_Text2 from _call_c16s001_Text2_1
    return
label c16s001_CumInMarMouth:
    mc "Mamá, voy a correrme... y lo voy a manchar todo..."
    call OrgasmX ("c16s001_285d") from _call_OrgasmX_35
    "[mar] entiende lo que quieres decir y aparta a [emm]. Se mete tu capullo en la boca justo a tiempo de recibir tu descarga."
    mc "¡Mpfft!"
    emm "¡Wow! Eso ha sido increíble Mamá... ¿Qué vas a hacer con eso? ¿Te lo vas a tragar?"
    scene c16s001_295a with dissolve #TIENE un poco en la comisura de los labios
    "[mar] te mira inquisitivamente, preguntando qué quieres que haga. Es increíble como os podéis entender con una simple mirada."
    if persistent.walkthrough:
        $ wt1 = _("")
        if persistent.lesbian:
            $ wt2 = _("Beso blanco.")
        else:
            $ wt2 = _("Beso blanco sin contenido lésbico.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Trágatelo, Mamá." (wt = wt1):
            scene c16s001_295An with dissolve #bcd
            "[mar] cumple con tu solicitud enseñándote después la boca vacía."
            emm "¡Wow! Si lo de antes ha sido increíble... ¡Esto ha sido impresionante!"
            if persistent.lesbian:
                scene c16s001_300An1 with dissolve #a-e with dissolve
            else:
                scene c16s001_300An2 with dissolve #cde emm coge con el dedo semen de la comisura del labio y se la lleva a la boca
            emm "Te has dejado un poco aquí..."
        "Dáselo a probar a [emm], Mamá" (wt = wt2):
            if persistent.lesbian:
                scene c16s001_305An1 with dissolve #a-b-c beso, se tiene que ver el semen. mar con la boca vacía y emm con la boca llena. Acaba con mar mirando a [emm]
            else:
                scene c16s001_305An2 with dissolve #d-e-f mar deja caer el semen en la boca de emm. mar con la boca vacía y emm con la boca llena. Acaba con mar mirando a [emm]
            "[mar] cumple con tu solicitud enseñándote después la boca vacía. La forma que tiene esta mujer de hacer las cosas es increíble."
            mc "Sé que cuesta creerlo, pero me he quedado sin palabras."
            mom "[emm], ahora te lo tienes que tragar. Y no te olvides de enseñarle la boca vacía."
            scene c16s001_310An with dissolve #abcd
    $ resetWalkthrough ()
    emm "Está salado, pero tiene un regusto dulce al final..."
    scene c16s001_315d with dissolve
    mom "¿Tienes pañuelos de papel por aquí?"
    mc "Sí, en el cajón..."
    return
label c16s001_MyGirl:
    mom "No sé... es mi niña..."
    mc "Mamá... es tu niña que se está ofreciendo a limpiar la corrida que tu niño acaba de dejar dentro de ti. *Risa*"
    return
label c16s001_Text1:
    mom "Esto se llama corrida, y es lo que... expulsan los chicos cuando les das mucho placer. ¿Quieres probarlo? Es un poco salado."
    emm "¡Sí!"
    if Aux == 1:
        if persistent.lesbian:
            scene c16s001_280An1 with dissolve #mar da a probar de su mano a [emm] efk
        else:
            scene c16s001_280An2 with dissolve #mar coge semen del pecho de [emm] y se lo da a probar defk
    else:
        scene c16s001_280An3 with dissolve #mar coge semen de la cara de [emm] y se lo da a probar ghij
    emm "Está salado, pero tiene un regusto dulce al final..."
    mom "Ahora me toca probarlo a mí."
    return
label c16s001_Text2:
    mom "Pero tú estás cubierta... Mmmm... Delicioso..."
    mc "¡Wow, Mamá! Eso ha sido increíble... casi me acabas de provocar otra erección..."
    if Aux == 1:
        scene c16s001_290a with dissolve
    else:
        scene c16s001_290b with dissolve
    mom "¿Tienes pañuelos de papel por aquí? Hay que limpiar todo esto."
    mc "Sí, en el cajón..."
    return
label c16s002_TakeMeemawDoc:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_33
        if mar._var("route"):
            call mrS3_emm_route from _call_mrS3_emm_route_35
        else:
            call mrS3_nor_route from _call_mrS3_nor_route_25
            if not nor._var("route"):
                call mrS3_sam_route from _call_mrS3_sam_route_19
                call mrS3_dap_route from _call_mrS3_dap_route_28
                call mrS3_eri_route from _call_mrS3_eri_route_28
                call mrS3_emm_route from _call_mrS3_emm_route_36
        menu:
            "Cuando Tía Betty y [mar!t] estaban hablando en la cocina, ¿te paraste a escuchar a escondidas?"
            "Sí.":
                $ mee._var("mcKnowsSickness", True)
            "No.":
                $ mee._var("mcKnowsSickness", False)
    $ PregnancyTests = True
    $ emm._var("age", 19, "set")
    centered "{size=+20}{b}DÍA 18 – VIERNES{/b}{/size}\nCumpleaños de [emm]"
    $ renpy.notify ("Emma's Birthday")
    scene itchio with dissolve
    "Nota del autor: Cualquier procedimiento médico llevado a cabo durante el juego puede pertenecer a dos categorías: Exageración o completamente inventado."
    "No lleves a cabo estos procedimientos sin supervisión médica... a menos que sea para divertiros ;) ."
    scene black with dissolve
    if mar._var("route") and emm._var("route"):
        "Cuando te despiertas ninguna de las dos está en la habitación. Al final resultará que sí que eres el más dormilón de la familia."
        "Bajas a la cocina a desayunar."
    else:
        "Te despiertas pronto y bajas a desayunar."
    "Tan solo son las 8:00. Te sorprendes de que te hayas despertado tan pronto sin poner el despertador."
    play music ("music/These-Little-Moments.ogg")
    scene c16s002_005 with dissolve
    mc "¡Buenos días, [mar.mc!t]! ¡Buenos días, Meemaw!"
    call KissXP ("c16s002_010", "d") from _call_KissXP_47
    mom "Buenos días, [mc]."
    call BlinkXP ("c16s002_015", "d") from _call_BlinkXP_1529
    mee "Buenos días, [mc]."
    mc "¿Sólo buenos días? ¿No hay beso para mí hoy?"
    call BlinkXP ("c16s002_020", "d") from _call_BlinkXP_1530
    mee "Creía que era voluntario..."
    mc "Y lo es, pero creía que querrías un beso de tu nieto favorito después de lo de ayer. *Risa*"
    call KissXP ("c16s002_025", "d") from _call_KissXP_48
    mee "¿Contento?"
    mc "Sí. *Risa*"
    call BlinkXP ("c16s002_030", "d") from _call_BlinkXP_1531
    mom "Ahora que lo tienes contento, se lo puedes pedir."
    mc "¿El qué? ¿Qué necesitas, Meemaw?"
    call BlinkXP ("c16s002_035", "d") from _call_BlinkXP_1532
    mee "Necesitaría que me llevaras al médico. Me iba a llevar Betty, pero se ha levantado con vómitos. Cenó demasiado anoche."
    mc "*Risa* Al decir lo de los vómitos te iba a preguntar si estaba embarazada. *Risa*"
    mc "¿Cuándo hay que ir al médico?"
    mee "Deberíamos salir en breve."
    mc "¿Hoy? ¿Esta mañana? A mediodía tengo que estar... tengo que ir... tengo una cosa que hacer."
    call BlinkXP ("c16s002_040", "d") from _call_BlinkXP_1533
    mom "Ya le he explicado todo, no te preocupes. Sabe quiénes son Eva y Amanda, y que has quedado con Eva en el lago hoy."
    mom "Por eso no podemos llevarla ni [nor] ni yo. [nor] está un poco nerviosa con preparar la comida para Eva, y la visita al médico es por un chequeo de rutina."
    mc "¿Nos dará tiempo de ir al médico y volver a tiempo de que suba al lago?"
    call BlinkXP ("c16s002_045", "d") from _call_BlinkXP_1534
    mee "La visita al médico debería durar una hora como mucho. A las 10:30 o las 11 deberíamos estar aquí."
    mc "Entonces, déjame comer algo rápido, cambiarme, y nos vamos."
    mee "Perfecto, voy a coger la documentación mientras acabas de desayunar."
    call BlinkXP ("c16s002_050", "f") from _call_BlinkXP_1535
    mom "Ya que la acompañas al médico... a ver si puedes enterarte de cómo está. Creo que nos está ocultando algo sobre su salud."
    mc "Algo... ¿como qué?"
    if mee._var("mcKnowsSickness"):
        mc "¿La galactorrea? ¿O el cáncer?"
        call BlinkXP ("c16s002_055", "h") from _call_BlinkXP_1536
        mom "¿Qué? ¿Cómo sabes eso?"
        mc "Escuché lo del cáncer mientras Betty y tú discutíais. También lo de la galactorrea. Además, el día del secuestro la pillé extrayéndose leche y me lo tuvo que explicar."
        call BlinkXP ("c16s002_060", "d") from _call_BlinkXP_1537
        mom "¿No te enfadas porque no te lo haya contado?"
        mc "No tiene sentido enfadarse. Lo escuché igualmente y Betty te pidió que no se lo contaras a nadie."
    else:
        call BlinkXP ("c16s002_060", "d") from _call_BlinkXP_1538
        mom "No acabo de creerme que sea un chequeo rutinario. Ha dicho que si no podías llevarla tú llamaría a un Under. Y eso ha sido antes de contárselo todo."
    mc "No te preocupes, si me entero de algo, te lo haré saber... a menos que Meemaw me obligue a prometer que guardaré silencio."
    mc "Voy a cambiarme. Te veo luego. Te quiero."
    call KissXP ("c16s002_010", "d") from _call_KissXP_49
    stop music fadeout (1.5)
    mom "Y yo a ti. Conduce con cuidado."
    scene black with dissolve
    if mar._var("route") or nor._var("route") or sam._var("route"):
        "Durante el viaje Meemaw está especialmente callada. No sabes exactamente si es por el médico, los besos, o por tus relaciones. O incluso por otra razón que desconoces."
    else:
        "Durante el viaje Meemaw está especialmente callada. No sabes exactamente si es por el médico o por los besos. O incluso por otra razón que desconoces."
    call BlinkXP ("c16s002_065", "f") from _call_BlinkXP_1539
    play music ("music/Looking-Forward.ogg")
    mee "Bueno, ya hemos llegado. Esta es la consulta. Puerta 64. ¿Dónde me esperas?"
    mc "Dentro. Te voy a acompañar."
    call BlinkXP ("c16s002_070", "d") from _call_BlinkXP_1540
    mee "No hace falta, [mc]. Gracias, pero no es necesario."
    mc "No es necesario, pero lo voy a hacer. ¿Es algún chequeo por la galactorrea?"
    call BlinkXP ("c16s002_075", "d") from _call_BlinkXP_1541
    mee "Sí... pero te vas a quedar aquí, en la sala de espera."
    mc "De acuerdo, aunque preferiría entrar a la consulta contigo, por si hay algunas instrucciones que seguir."
    mee "Soy vieja, pero todavía soy capaz de entender unas instrucciones médicas."
    mcp "(Definitivamente está enfadada por algo.)"
    scene c16s002_080a with fade
    "Tras unos minutos en la sala de espera, aparece una médico."
    python:
        if "doc" not in globals () or not isinstance (doc, TGCharacter):
            doc = TGCharacter (_("Doctora"), color = "#ffffff")
    doc "¿Olivia Pitt? Sígame por favor."
    scene c16s002_080b with dissolve
    "Decides seguir a Olivia y a la médico discretamente."
    "Obviamente, te descubre, aunque ya contabas con ello."
    call BlinkXP ("c16s002_085", "h") from _call_BlinkXP_1542
    mee "*Susurrando* Te he dicho que te quedes en la sala de espera."
    mc "*Susurrando* Voy a entrar para darte apoyo emocional si lo necesitas. No creo que quieras montar un espectáculo delante de una médico que no conoces."
    mee "*Susurrando* Vale, entra, pero ya hablaremos luego."
    scene c16s002_080c with fade
    doc "Buenos días, soy la Doctora Harley Milk y me voy a encargar de su caso. ¿Cómo se encuentra, señora Pitt?"
    mcp "(No me jodas que la especialista en tetas se llama Harley Milk. *Risa Mental*)"
    python:
        if "hm" not in globals () or not isinstance (hm, TGCharacter):
            hm = TGCharacter (_("Dra. Milk"), color = "#ffffff")
    call BlinkXP ("c16s002_090", "d") from _call_BlinkXP_1543
    mee "Bien, no he venido por encontrarme mal, sino para ver si ya podemos empezar con el tratamiento."
    scene c16s002_080d with dissolve
    hm "Por lo que veo aquí, en el informe de su oncólogo, dejó la quimioterapia hace dos semanas. Eso significa que dentro de dos semanas podría empezar el tratamiento para la galactorrea."
    if mee._var("mcKnowsSickness"):
        mcp "(Y se descubrió el pastel de la quimio.)"
    else:
        mcp "(¿Qué? ¿Quimio? ¿Meemaw tiene cáncer?)"
    call BlinkXP ("c16s002_095", "d") from _call_BlinkXP_1544
    mee "¡Pero me dijeron que le visitara dos semanas después de dejar la quimio!"
    if mee._var("mcKnowsSickness"):
        mcp "(Está tan enfadada que no se está dando cuenta que la palabra quimio ya ha sido pronunciada dos veces.)"
    else:
        mcp "(Está tan enfadada que se ha olvidado que estoy aquí. Vamos a tener que hablar sobre esto.)"
    scene c16s002_080e with dissolve
    hm "Sí, exacto. Para preparar el tratamiento tenemos que hacerle una serie de pruebas y análisis. Eso requiere tiempo. Hoy tomaré una muestra de la secreción para analizarla."
    hm "Pase a detrás de esa mampara y desnúdese, por favor."
    scene c16s002_080f with fade
    mee "¿De cintura para arriba, Doctora?"
    scene c16s002_080g with dissolve
    hm "Sí, de momento. Más tarde vendrá una colega, la Doctora Krebs, que la examinará también respecto a la histerectomía. Entonces la haremos desnudar del todo."
    if not mee._var("mcKnowsSickness"):
        mcp "(¿Histerectomía? ¿Qué es eso?)"
        "Tras una rápida búsqueda en internet..."
        mcp "(¿Le han quitado el útero a Meemaw? ¿Cáncer de útero? ¿Y no nos ha dicho nada?)"
    scene c16s002_080f with dissolve
    mee "Ya estoy desnuda."
    scene c16s002_080f with fade
    hm "Bueno, esto tiene bastante buena pinta. Secreción de color correcto. Buena cantidad de fluido. Hoy no ha utilizado la bomba, ¿verdad?"
    mee "No, me dijeron que no la usara 12 horas antes de venir. Noto los pechos muy pesados ahora mismo."
    hm "Es normal. Mmmmm... ¿Se hace los masajes que le indicaron?"
    mee "Sí, Doctora. Me los hace mi hermana, porque yo no puedo hacerlo correctamente."
    hm "Pues no los está haciendo bien. ¿Nota esto aquí? Esto no debería estar aquí."
    mee "Sí, lo noto... pero ella es médico también. Cirujana."
    hm "Eso no tiene nada que ver. Yo soy mastóloga y no sabría cómo operar un cerebro. Hay algo que no está haciendo bien. Mire, le enseño como tiene que hacerlo."
    mee "No puedo ver donde tiene la mano."
    hm "Pues tendrá que venir su hermana para que le explique cómo hacerlo. O puedo explicárselo a... ¿es su hijo?"
    mee "¡Es mi nieto!"
    hm "Siento la equivocación ¿Le importa si le hago pasar?"
    mee "Puedo venir con mi hermana mañana..."
    hm "Mañana es sábado, no paso consulta de nuevo hasta el martes. Si puede venir el martes con su hermana, no hay ningún problema, excepto que no vamos a hacer pruebas hasta que esto no desaparezca."
    mee "*Resignada* Entonces, explíqueselo a mi nieto y que él se lo explique a mi hermana."
    mee "Espera un momento, [mc]. *Susurrando* Doctora, ¿puedo vestirme? No quiero que mi nieto me vea así."
    hm "Le tengo que enseñar a su nieto a hacer los masajes. No puedo hacerlo si está vestida."
    mee "*Resignada* Pasa, [mc]."
    if persistent.lactation and not itchio:
        scene c16s002_100aa with fade
    elif not itchio:
        scene c16s002_100ab with fade
    else:
        scene itchio
    hm "Mire, tiene que palpar en este lateral con el pulgar izquierdo y descubrirá una zona con una textura diferente. Más dura."
    mcp "(Meemaw está claramente avergonzada, no se atreve a hacer contacto visual conmigo.)"
    if persistent.lactation and not itchio:
        scene c16s002_100ba with dissolve
    elif not itchio:
        scene c16s002_100bb with dissolve
    else:
        scene itchio
    mc "Vale, sí, la noto."
    hm "Perfecto. Mantenga la presión ahí, y con dos dedos en la parte inferior del pecho. Como estoy haciendo yo."
    if persistent.lactation and not itchio:
        scene c16s002_100ca with dissolve
    elif not itchio:
        scene c16s002_100cb with dissolve
    else:
        scene itchio
    hm "Ahora tiene que hacer presión con la otra mano en la parte superior del seno e ir dirigiendo esa presión hacia el pezón, como un movimiento ondulante, sin mover la mano."
    hm "Con el pulgar que estaba apretando el nódulo, haga recorridos cortos hacia la parte delantera al mismo ritmo que hace el movimiento ondulante."
    hm "Con los dos dedos de la parte inferior apriete suavemente el pecho cuando todos los movimientos estén más cerca del pezón y después suelte suavemente."
    mc "Me parece que lo estoy pillando. Es complicado coordinar todos los movimientos a la vez al principio."
    scene c16s002_105a with dissolve
    hm "Especialmente en esta postura y con nuestras cuatro manos molestándose. Una vez le pille el truco, lo puede hacer desde atrás, es mucho más cómodo."
    mc "Yo creía que iba a salir más leche con estos masajes."
    hm "Durante el examen he extraído casi todo el líquido. Siempre se tienen que hacer estos masajes una vez extraída la secreción."
    hm "De esta forma se evitan accidentes incómodos, ya que tiene que producir nueva antes de que pueda expulsar más. Tardará unas horas a menos que haya excitación sexual."
    call BlinkXP ("c16s002_110", "h") from _call_BlinkXP_1545
    mee "*Avergonzada* No creo que hablar de mi excitación sexual delante de mi nieto sea correcto, Doctora."
    mc "No pasa nada, Meemaw. Es un término médico como otro cualquiera."
    scene c16s002_105b with dissolve
    hm "Si su nieto va a darle los masajes, debe saber lo que puede pasar. O informar a su hermana si sigue dándoselos ella."
    if persistent.walkthrough:
        $ wt1 = _("Ruta con Meemaw abierta más tarde.")
        $ wt2 = _("Ruta con Meemaw cerrada.\n{color=#ff0000}{b}No habrá más oportunidades de abrir la ruta{/b}{/color}")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "¿Me puede enseñar a dar los masajes desde atrás?" (wt = wt1):
            $ mee._var("route", True) #RIAM, please track this one
            $ mc._var("relationships", 1, "add")
            if not itchio:
                call c16s002_MeemawMassage from _call_c16s002_MeemawMassage
            else:
                scene itchio
                "La doctora te indica como tienes que dar los masajes desde atrás."
                mcp "(Hubiera sido más divertido verlo, pero este gato no se va de aquí. A lo mejor en Discord puedo preguntar cómo librarme de él.)"
        "Con esto tengo suficiente para explicárselo a mi tía." (wt = wt2):
            call c16s002_NoMeemawMassage from _call_c16s002_NoMeemawMassage
    $ resetWalkthrough ()
    scene black with dissolve
    if mee._var("mcKnowsSickness"):
        "Sales a la sala de espera y aprovechas para refrescar lo que has leído sobre histerectomías."
    else:
        "Sales a la sala de espera y aprovechas para leer sobre histerectomías."
    "Cuando Olivia sale, 15 minutos después, hacéis el camino hasta el coche en silencio, casi esperáis que sea el otro el primero que hable."
    stop music fadeout (1.5)
    "Cuando estáis llegando al aparcamiento, no puedes aguantar más y explotas."
    play music ("music/In-The-Rain.ogg")
    call BlinkXP ("c16s002_190", "d") from _call_BlinkXP_1546
    mc "¿Me vas a explicar qué ha sido eso de ahí dentro?"
    mee "Ya sabías que tenía galactorrea. No es que esté enferma... es un desorden hormonal..."
    mc "No me refiero a eso. Quimio. Histerectomía. ¿Tienes cáncer? ¿Cómo te encuentras? ¿Te vas a poner bien?"
    call BlinkXP ("c16s002_195", "d") from _call_BlinkXP_1547
    mee "He tenido cáncer. Estoy bien... o al menos lo que queda de mí. El cáncer desapareció cuando me extirparon... el..."
    mc "He leído lo que es una histerectomía. ¿Cómo estás?"
    mee "Ya te he dicho que no hay rastro del cáncer..."
    mc "Me refiero a cómo estás tú. A cómo te sientes. Sabes que puedes contar conmigo para lo que necesites, ¿verdad? Con todos nosotros... No nos tienes que ocultar cosas así..."
    call BlinkXP ("c16s002_200", "d") from _call_BlinkXP_1548
    mee "Lo sé... pero... es difícil cuando empiezas a ocultar cosas..."
    if persistent.family:
        mee "¿Cómo les digo a mis hijas lo que ha pasado cuando llevo más de un año ocultándoselo y diciéndoles que estoy bien cada vez que llaman? ¿O a las niñas?"
    else:
        mee "¿Cómo le digo a mi hija lo que ha pasado cuando llevo más de un año ocultándoselo y diciéndole que estoy bien cada vez que llama? ¿O a [mar] y a las niñas?"
    mc "Decir la verdad a veces es complicado, pero resulta liberador y evita problemas."
    if mar._var("route") or nor._var("route"):
        call BlinkXP ("c16s002_205", "d") from _call_BlinkXP_1549
        mee "¿Como lo tuyo de ayer en la cocina?"
        mc "No estamos hablando de mí, Meemaw. Creo que es mucho más importante lo que te está pasando que con quién esté yo."
    mc "Yo ahora se lo tuyo y puedo apoyarte en lo que necesites. Si necesitas guardar el secreto, te ayudaré aunque no me parezca bien."
    call BlinkXP ("c16s002_210", "h") from _call_BlinkXP_1550
    mee "Lo sé... sé que puedo confiar en ti, aunque no te haya dicho la verdad... Betty ha sido mi apoyo en esto... y ahora tú."
    mc "Y el resto de la familia lo sería si se lo contaras."
    call BlinkXP ("c16s002_215", "d") from _call_BlinkXP_1551
    mee "Pero es muy difícil. Es complicado explicaros como me siento."
    mc "Prueba a hacerlo conmigo, si quieres."
    mee "Has leído lo que es una histerectomía y sabes que no tengo útero, ¿no?"
    mc "Sí..."
    call BlinkXP ("c16s002_220", "d") from _call_BlinkXP_1552
    mee "Por hablar de un tema más conocido... ¿Qué sabes del cáncer de mama? ¿De las mujeres que se someten a una mastectomía? ¿Cómo se sienten?"
    mc "Sé que se sienten menos femeninas... menos mujeres. Pero lo considero una estupidez."
    call BlinkXP ("c16s002_225", "d") from _call_BlinkXP_1553
    mee "No es una estupidez, [mc]. Cuando te quitan algo que te ha definido como mujer durante toda tu vida, es normal sentirse así..."
    mee "En mi generación, la maternidad era una de las cosas que nos definía como mujeres... no la única, pero una parte importante."
    if persistent.family:
        mee "He tenido tres hijos que han crecido en una parte de mí que ya no existe."
    else:
        mee "He tenido una hija que ha crecido en una parte de mí que ya no existe."
    mee "Es difícil seguir sintiéndose una mujer cuando ya no puedes..."
    mc "{b}¿Estabas pensando en tener más hijos?{/b}"
    call BlinkXP ("c16s002_230", "d") from _call_BlinkXP_1554
    mee "*Risa* No, tonto. Pero ya no puedo tenerlos aunque lo quisiera pensar. Y no me digas ahora que a mi edad no iba a poder tenerlos. *Risa*"
    mc "Nota mental. Decir tonterías hace reír a Meemaw incluso ahora. Seguimos con el experimento."
    mee "*Risa* Estoy hablando en serio, [mc]."
    mc "Que digas eso mientras te estás riendo, le quita un poco de fuerza a la frase."
    call BlinkXP ("c16s002_235", "d") from _call_BlinkXP_1555
    mee "Para ya con las tonterías entonces."
    mee "A lo que me refiero es a que si una mujer con una mastectomía... aunque le reconstruyan el pecho... se siente menos mujer... imagínate como me siento yo."
    mc "¿Te sientes poco femenina? ¿Poco mujer? ¿Poco atractiva?"
    call BlinkXP ("c16s002_240", "d") from _call_BlinkXP_1556
    mee "Sí..."
    if mee._var("route"):
        stop music fadeout (1.5)
        mc "¿Incluso con lo que ha pasado ahí dentro? Sé que has notado mi erección..."
        play music ("music/Inspire.ogg")
        call BlinkXP ("c16s002_245", "v") from _call_BlinkXP_1557 #se aparta
        mee "Eso es diferente... a tu edad tienes las hormonas saltando de alegría... y me estabas tocando... ya sabes..."
        mc "Meemaw, tengo sexo regular desde hace años. No voy a tener una erección simplemente por tocar una teta."
        call BlinkXP ("c16s002_250", "d") from _call_BlinkXP_1558
        mee "Pero..."
        mc "Y además, si estuviéramos hablando sobre otras personas, una hermosa abuela y su nieto, y lo viera desde fuera, casi podría asegurar que la abuela ha disfrutado."
        mc "Que los dos han disfrutado..."
        call BlinkXP ("c16s002_255", "h") from _call_BlinkXP_1559
        mee "{b}¿Qué? ¿Tú también?{/b} ¿También has tenido un... un...?"
        mc "¿Orgasmo?"
        call BlinkXP ("c16s002_260", "d") from _call_BlinkXP_1560
        mee "Sí..."
        mc "No, no lo he tenido, pero tu \"también\" me ha confirmado lo que pensaba. Tenía dudas sobre si tú lo habías tenido."
        call BlinkXP ("c16s002_245", "h") from _call_BlinkXP_1561
        mee "{b}¿Qué? ¡No!{/b}"
        mc "Meemaw, ¿que acabamos de decir sobre mentir y ocultar cosas?"
        call BlinkXP ("c16s002_260b", "d") from _call_BlinkXP_1562
        mee "Tienes razón... sí... he tenido un orgasmo... Estoy muy avergonzada... tener un orgasmo mientras mi nieto me toca... no está bien. Y nunca me había pasado..."
        mc "Meemaw, no hay nada malo en ello. No había nada sexual en lo que estábamos haciendo, y por lo que he leído, tú sí que tienes que tener las hormonas saltando."
        call BlinkXP ("c16s002_265", "d") from _call_BlinkXP_1563
        mee "Si no había nada sexual, explícame por qué has tenido esa erección... todo es culpa tuya. Hasta que he notado como me presionabas por detrás, todo iba bien."
        mc "Si me vas a echar la culpa a mí, mejor no te lo explico. Ha sido una idea estúpida."
        call BlinkXP ("c16s002_270", "d") from _call_BlinkXP_1564
        mee "[mc], ¿que acabamos de decir sobre mentir y ocultar cosas?"
        mc "*Risa* Vale, me has pillado."
        mc "Con lo que ha dicho la Doctora Milk... se las trae el nombre para una especialista en tetas, ¿no?"
        call BlinkXP ("c16s002_275", "d") from _call_BlinkXP_1565
        mee "*Risa* Yo también lo he pensado, los médicos en este hospital tienen nombres raros. Pero estabas diciendo algo sobre lo que ha dicho la Doctora."
        mc "Sí, con lo que ha dicho sobre la leche, he pensado que para hacer esto en casa, lo mejor sería en la ducha, para no manchar..."
        mc "Y nos he imaginado a los dos en la ducha... era muy sexy. Y mi amigo no sabe distinguir entre realidad e imaginación y se ha despertado."
        call BlinkXP ("c16s002_280", "d") from _call_BlinkXP_1566
        mee "¿Sexy? ¿Yo?"
        mc "Sí y no. Eres sexy, pero lo que era de verdad sexy era la imagen de tú y yo juntos en la ducha... desnudos... mientras te hacía el masaje."
        call BlinkXP ("c16s002_285", "d") from _call_BlinkXP_1567
        mee "¿Nos estabas imaginando desnudos a los dos?"
        mc "Claro... consistía en no manchar, ¿no? *Risa* Y visto el resultado, casi hubiera sido lo mejor, ¿no?"
        call BlinkXP ("c16s002_290", "d") from _call_BlinkXP_1568
        mee "¿E imaginarme desnuda te ha provocado una erección? ¿Ves como tu idea sobre la desnudez no era buena?"
        mc "No. Ha sido imaginarnos a los dos desnudos, en una actitud... cariñosa..."
        mee "¿Cariñosa?"
        mc "No creerás que le hago masajes en las tetas a todas las mujeres que me lo piden, ¿verdad?"
        mc "Si hago esto es porque te quiero, Meemaw."
        call BlinkXP ("c16s002_295", "d") from _call_BlinkXP_1569
        if mar._var("route"):
            if persistent.family:
                mee "Pues no tengas ideas raras. No soy como tu madre y no voy a empezar una relación contigo. Al menos nada sexual."
            else:
                mee "Pues no tengas ideas raras. No soy como [mar] y no voy a empezar una relación contigo. Al menos nada sexual."
        elif nor._var("route"):
            mee "Pues no tengas ideas raras. No soy como [nor] y no voy a empezar una relación contigo. Al menos nada sexual."
        else:
            if persistent.family:
                mee "Pues no tengas ideas raras. Soy tu abuela y eso no va a pasar. Al menos nada sexual."
            else:
                mee "Pues no tengas ideas raras. Soy prácticamente tu abuela y eso no va a pasar. Al menos nada sexual."
        mc "Eso me lo repites si la próxima vez no tienes un orgasmo. *Risa* Y antes de que me pegues, estoy bromeando."
        call BlinkXP ("c16s002_255", "h") from _call_BlinkXP_1570
        mee "¿Qué? ¿Quieres seguir haciéndolo? Si no quieres... no es necesario... le puedes explicar a Betty como hacerlo..."
        mc "Si Betty no puede hacerlo, o si prefieres que lo haga yo, no tengo ningún problema en repetir lo de hoy. Parece que ha ido bien."
        mc "A nivel médico, me refiero..."
        call BlinkXP ("c16s002_300", "d") from _call_BlinkXP_1571
        mee "Bueno, ya veremos. De momento se lo vas a tener que explicar a Betty."
        mee "Pero sin desnudos ni duchas... *Risa*"
        mc "De acuerdo, *Risa* ¿nos vamos?"
    else:
        mc "Meemaw, mírame. Eres una mujer muy atractiva y que tiene mucho que ofrecer. Si encontraras a alguien, ese hombre no pensaría en tener hijos con una mujer de tu edad."
        mc "Con lo que no va a tener ninguna importancia para él que no puedas tenerlos porque te falta una pieza del equipo necesario."
        call BlinkXP ("c16s002_275", "d") from _call_BlinkXP_1572
        mee "¿Una pieza del equipo necesario? *Risa* Hay muchas formas de llamarlo, pero esa..."
        mc "Esa es la forma de llamarlo para que te rías y te olvides de esas tonterías."
        mc "¿Nos vamos?"
    call BlinkXP ("c16s002_290", "d") from _call_BlinkXP_1573
    mee "Sí, tienes que ir al lago para tus clases con... ¿con quién era? ¿Amanda o Eva?"
    mc "Eva. Es como [dap] con pistolas. *Risa*"
    stop music fadeout (1.5)
    scene black with dissolve
    "Volvéis al coche y a casa. La conversación es animada. Parece que Meemaw se ha quitado un peso de encima."
    "Te pide un poco de tiempo para preparar el discurso que le va a dar a la familia sobre su enfermedad. Te promete que la próxima semana lo hará."
    return
label c16s002_MeemawMassage:
    mc "De esa forma se lo puedo explicar a mi tía también."
    call BlinkXP ("c16s002_125", "d") from _call_BlinkXP_1574
    mee "No es necesario, [mc]. Betty lo hace por delante."
    mc "Pero parece ser que no lo hace correctamente. Si la Dra. Milk dice que es más cómodo y fácil desde atrás, a lo mejor a ella también le va mejor."
    call BlinkXP ("c16s002_130", "d") from _call_BlinkXP_1575
    stop music fadeout (1.5)
    mee "Bueeeeno... vale"
    play music ("music/Rumba.ogg")
    scene c16s002_105c with dissolve
    hm "Perfecto entonces. Póngase de pie, Sra. Pitt. Y usted sitúese detrás de su abuela. Ahora, Olivia, levante los brazos por encima de la cabeza..."
    "Siguen unas cuantas explicaciones más para corregir la postura."
    hm "Ahora ya puede empezar con el masaje. Recuerde, desde el esternón al pezón. Ahora puede masajear el nódulo con los dos pulgares y hacer la presión inferior con el meñique y el anular."
    if persistent.lactation:
        scene c16s002_135aa with dissolve
    else:
        scene c16s002_135ab with dissolve
    mc "Así es mucho más fácil de hacer el masaje."
    mcp "(Y también mucho más sexy, es como si estuviera abrazando a una amante por detrás...)"
    if persistent.lactation:
        scene c16s002_140pva with dissolve
        show c16s002_140va
    else:
        scene c16s002_140pvb with dissolve
        show c16s002_140vb
    mcp "(¿Estás loco? ¡Es Meemaw! Nunca aceptaría... *Risa mental* Si ya le ha costado aceptar los besos...)"
    mcp "(Pero ¿qué haría yo si ella lo quisiera? Realmente es una mujer muy sexy para su edad...)"
    mcp "(O incluso para cualquier edad. Muchas mujeres más jóvenes quisieran tener un cuerpo como el suyo...)"
    mcp "(Pero, ¿la podría hacer feliz? ¿sería feliz conmigo?)"
    if persistent.family:
        if mar._var("route") or nor._var("route") or emm._var("route") or dap._var("route") or eri._var("route"):
            mcp "(Tampoco sería la primera de la familia con la que tuviera algo. No podría poner eso como excusa para rechazarla.)"
        else:
            mcp "(Sería la primera de la familia con la que tuviera algo. Podría poner eso como excusa para rechazarla.)"
    else:
        mcp "(No somos familia de sangre, con lo que no podría poner eso como excusa para rechazarla.)"
    mcp "(¿Rechazarla? *Risa mental* Ni que ella quisiera algo así conmigo.)"
    if persistent.lactation:
        scene c16s002_135ba with dissolve
        hide c16s002_140va
    else:
        scene c16s002_135bb with dissolve
        hide c16s002_140vb
    mcp "(Aunque realmente me puedo imaginar haciendo esto en la ducha con ella... los dos desnudos...)"
    mcp "(Y ahora es cuando me he vuelto totalmente loco. *Risa mental*)"
    scene c16s002_145a with dissolve
    mcp "(Y cuando me estoy empezando a poner cachondo.)"
    scene c16s002_145b with hpunch
    mee "*Suspiro de sorpresa*"
    if persistent.lactation:
        scene c16s002_145ca with dissolve
    else:
        scene c16s002_145cb with dissolve
    hm "Exacto, siga así. ¿Puede notar como los pezones se están poniendo más duros? Esa es una buena señal."
    if persistent.lactation:
        call BlinkXP ("c16s002_150a", "d") from _call_BlinkXP_1576
    else:
        call BlinkXP ("c16s002_150b", "d") from _call_BlinkXP_1577
    mee "*Gemido* ¿No lo podríamos dejar por hoy, Doctora? Creo que ya ha descubierto como hacerlo."
    mcp "(¿Eso ha sido un gemido?)"
    hm "Creo que sería bueno que siguiera un poco más. Recuerde que hay que hacer esto todos los días."
    if persistent.lactation:
        scene c16s002_155pva with dissolve
        show c16s002_155va
    else:
        scene c16s002_155pvb with dissolve
        show c16s002_155vb
    mee "*Gemido* Bueno... si es porque el chico aprenda... la verdad es que lo hace mejor que mi hermana..."
    mcp "(¡Desde luego que ha gemido! ¿Se está poniendo cachonda? ¿Deberíamos parar?)"
    mee "{i}(¿Qué me está pasando? Cuando lo hace Betty no se parece en nada a esto...){/i}"
    mee "*Jadeo* Mi hermana es mucho más brusca... haciendo esto..."
    mee "{i}(Claro que Betty no me está presionando el culo como lo hace [mc]...){/i}"
    mc "Intento ir con cuidado, Meemaw... no sé cuánta presión puedo hacer sin hacerte daño."
    mcp "(Eso se podría interpretar como presión en sus tetas o en su culo. *Risa mental*)"
    mee "*Gemido* ¡Mas fuerte!... Me refiero que puedes apretar un poco más... si quieres..."
    mee "{i}(¿Me estoy poniendo como una perra en celo? Esto tiene... que parar...){/i}"
    mee "*GEMIDO* ¡Para ya!... O..."
    if persistent.lactation:
        scene c16s002_160An1 with hpunch #cdba
        hide c16s002_155va
    else:
        scene c16s002_160An2 with hpunch #edf
        hide c16s002_155vb
    "Sin darle tiempo a acabar la frase, notas como un gran borbotón de leche se te escapa entre los dedos, mientras el otro pezón entra en erupción como un volcán."
    mee "*GEMIDO*"
    "Meemaw se aprieta contra ti mientras su cuerpo tiembla por un momento."
    mcp "(Eso no puede haber sido un orgasmo, ¿verdad?)"
    call BlinkXP ("c16s002_165", "h") from _call_BlinkXP_1578
    mee "¡Ya está! Creo que lo has pillado. No es necesario que practiques más."
    mee "{i}(No puede ser... esto no puede haber pasado...){/i}"
    scene c16s002_165d with dissolve
    hm "Vaya, yo creía que había extraído toda la secreción. He debido cometer un error y haber dejado algo... un montón... por extraer."
    hm "Tanto volumen, incluso en el pecho no masajeado, solo debería pasar si no se ha extraído en horas o si ha habido excitación sexual."
    mcp "(Definitivamente ha habido excitación sexual, al menos por mi parte. Y podría jurar que lo de Meemaw ha sido un orgasmo.)"
    mcp "(Se la ve tan avergonzada ahora mismo...)"
    if persistent.lactation:
        call BlinkXP ("c16s002_170a", "h") from _call_BlinkXP_1579
    else:
        call BlinkXP ("c16s002_170b", "h") from _call_BlinkXP_1580
    mee "{b}¿Está loca?{/b} ¿Cómo puede pensar que he sentido excitación sexual con mi nieto?"
    mcp "(Y ya vuelve a ser la Meemaw de siempre. *Risa mental* A lo mejor estoy equivocado y no ha sido un orgasmo...)"
    mee "{i}(¡La loca soy yo! He podido notar como iba subiendo y no lo he parado a tiempo... tantos años sin un orgasmo...){/i}"
    scene c16s002_165e with dissolve
    hm "No quería decir eso, Sra. Pitt. Me refería a que era una de las posibilidades, pero debo haberme equivocado al extraer la secreción."
    mcp "(Definitivamente, ha vuelto a ser ella misma. Ya ha acojonado a la médico.)"
    if persistent.lactation:
        call BlinkXP ("c16s002_175a", "h") from _call_BlinkXP_1581
    else:
        call BlinkXP ("c16s002_175b", "h") from _call_BlinkXP_1582
    mee "Y tú... tú ya puedes esperar fuera. Y no me refiero al otro lado de la mampara. Espérame en los bancos del pasillo."
    mcp "(Está en modo \"No me lleves la contraria si no quieres morir\". Debe estar muy avergonzada por lo que ha pasado... pero yo ya sabía lo que podía pasar, con lo que...)"
    mcp "(Definitivamente orgasmo... ¡Mi Meemaw ha tenido un orgasmo mientras le masajeaba las tetas!  *Risa mental* ¡Eso sí que no me lo esperaba!)"
    mc "*Risa* Vale, Meemaw, voy a lavarme las manos y te espero fuera."
    if persistent.lactation:
        menu:
            "Lamer la leche de tus dedos.":
                scene c16s002_175d with dissolve
                mc "Pero antes..."
                "Te llevas un dedo a la boca y lo lames."
                mcp "(Tiene un sabor... diferente...)"
                call BlinkXP ("c16s002_180", "h") from _call_BlinkXP_1583
                mee "¿Qué crees que estás haciendo?"
                mc "No querrás que deje un rastro de leche por el pasillo hasta el lavabo, ¿no? Imagínate si se me empiezan a caer gotas..."
                call BlinkXP ("c16s002_185", "d") from _call_BlinkXP_1584
                mee "Vale... lo entiendo... espérame fuera, por favor."
                mc "De acuerdo, hasta ahora."
            "No hacerlo.":
                mc "Hasta ahora, Meemaw."
    mc "Hasta otra, Dra. Milk."
    scene c16s002_185d with dissolve
    hm "Hasta luego, Sr. Pitt."
    mc "Marks. [mc] Marks."
    mcp "(Y me gusta el Martini mezclado, no agitado. *Risa mental*)" #Shaken, not stirred
    scene c16s002_120b with dissolve
    "Justo cuando vuelves al despacho, entra otra médico."
    call c16s002_Krebs from _call_c16s002_Krebs
    return
label c16s002_NoMeemawMassage:
    mc "Si los masajes te los va a continuar dando Tía Betty, creo que ya le puedo dar lecciones."
    call BlinkXP ("c16s002_115", "d") from _call_BlinkXP_1585
    mee "*Suspiro* Entonces, ¿puedes esperar fuera a que acabemos el examen?"
    mc "Sí, Meemaw, te espero al otro lado de la mampara."
    mee "Me refería a..."
    scene c16s002_120a with dissolve
    mc "Al otro lado de la mampara."
    scene c16s002_080f with fade
    "Te sientas en el despacho de la doctora mientras escuchas preguntas rutinarias sobre los hábitos alimenticios de Meemaw, cuánto ejercicio hace, etc."
    scene c16s002_120b with dissolve
    "Al cabo de un rato aparece otra médico."
    call c16s002_Krebs from _call_c16s002_Krebs_1
    scene c16s002_120d with dissolve
    krb "¿Puede esperar fuera, señor...?"
    mc "Marks. [mc] Marks."
    mcp "(Y me gusta el Martini mezclado, no agitado. *Risa mental*)" #Shaken, not stirred
    mc "Es mi abuela, y me gustaría estar por si puedo ayudarla en algo."
    krb "Voy a hacerle a su abuela unas preguntas que suelen tener respuestas más sinceras si no hay ningún familiar delante."
    mee "*Desde la sala de examen* No pasa nada, cielo. Espérame fuera."
    return
label c16s002_Krebs:
    python:
        if "krb" not in globals () or not isinstance (krb, TGCharacter):
            krb = TGCharacter (_("Dra. Krebs"), color = "#ffffff")
    krb "Me parece que me he equivocado de puerta. Usted no es Olivia Pitt."
    scene c16s002_080f with dissolve
    hm "*Desde la sala de examen* Pasa, Krebs, estoy con la Sra. Pitt aquí dentro."
    scene c16s002_120c with dissolve
    krb "Buenos días, Sra. Pitt. Voy a hacerle unas preguntas."
    return
label c16s002_GiveMeAMinute:
    deb "¡Dame un minuto!"
    scene c16s002_360AnBlink with dissolve #d (se va) - e (se para y levanta un dedo) - f (vuelve) - a- g (besa-H) - Blink
    deb "Por cierto, buenos días, [mc]."
    mc "Buenos días, Debbie."
    scene c16s002_360d with dissolve
    deb "Ahora vuelvo."
    return
label c16s002_RunWithDebbie:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Debbie?"
            "Mas de 0":
                $ deb._var("relationshipPoints", 5, intention = "set")
            "Menos de 0":
                $ deb._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Intentaste besar a Debbie en el Verdad o Reto en la playa?"
            "Sí":
                $ deb._var("kissedBeach" , True)
                menu:
                    "¿Te rechazó?"
                    "Sí":
                        $ deb._var("kissRejected" , True)
                    "No":
                        $ deb._var("kissRejected" , False)
            "No":
                $ deb._var("kissedBeach" , False)
        call mrS3_dap_route from _call_mrS3_dap_route_29
        menu:
            "¿Cuántas relaciones tienes?"
            "Una":
                $ mc._var("relationships", 1, intention = "set")
            "Más de una":
                $ mc._var("relationships", 2, intention = "set")
            "Ninguna" if mc._var("relationships")<1:
                $ mc._var("relationships", 0, intention = "set")
    $ RunWithDebbie = True #RIAM Don't track this one
    if deb.rps > 0:
        $ Aux = True
        "Al llegar a casa, subes a tu habitación a cambiarte y vas a buscar a Debbie. Ya está vestida y preparada pese a que os va a sobrar mucho tiempo."
        call BlinkXP ("c16s002_350" , "d") from _call_BlinkXP_1586
        mc "Hola, Debbie. ¿Hoy no llevas mochila? ¿No vas a bañarte en el lago?"
        deb "No sé si habrá tiempo. Dices que tenías una cita a mediodía."
        mc "Yo creo que, si salimos ahora, media hora para bañarnos seguro que tenemos, si quieres."
        mc "Yo llevo mi mochila y los shorts."
        call BlinkXP ("c16s002_355" , "d") from _call_BlinkXP_1587
        deb "¡Esperaba que dijeras algo así! Llevo el bikini debajo. *Risita*"
        mc "¿Toalla?"
        call c16s002_GiveMeAMinute from _call_c16s002_GiveMeAMinute
    else:
        $ Aux = False
        call BlinkXP ("c16s002_350" , "d") from _call_BlinkXP_1588
        "Al llegar a casa, vas a cambiarte y, al bajar, ves a Debbie sentada en los sofás de su planta."
        mc "Buenos días, Debbie. ¿Vas a salir a correr? ¿O has estado haciendo yoga con las chicas?"
        deb "Las dos cosas. He hecho yoga, y Kim y yo íbamos a ir a correr, pero al final no le ha apetecido."
        if persistent.walkthrough:
            $ wt1 = _("Debbie + 5")
            $ wt2 = _("No podrás abrir la ruta con Debbie.\n{color=#ff0000}{b}No habrá más oportunidades de abrir la ruta{/b}{/color}")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Yo voy a subir al lago." (wt = wt1):
                $ deb.rp (5)
                mc "Si quieres venir, eres bienvenida. Pero tendrías que volver sola."
                call BlinkXP ("c16s002_365a" , "d") from _call_BlinkXP_1589
                deb "¿Volver sola?"
                mc "Tengo que encontrarme con alguien allí a mediodía. Si salimos ahora, aún tendríamos un rato para bañarnos en el lago."
                call BlinkXP ("c16s002_355" , "d") from _call_BlinkXP_1590
                deb "Llevo el bikini debajo. *Risita* Kim y yo nos íbamos a bañar otra vez."
                mc "¿Toalla?"
                if deb.rps > 0:
                    call c16s002_GiveMeAMinute from _call_c16s002_GiveMeAMinute_1
                else:
                    scene c16s002_360d with dissolve
                    deb "¡Dame un minuto!"
                mc "Voy a coger una yo también. Nos vemos aquí en un minuto."
            "Es una lástima. Otro día tenemos que subir al lago." (wt = wt2):
                mc "Hoy he quedado con alguien, pero otro día, si quieres, subimos juntos."
                call BlinkXP ("c16s002_365b" , "d") from _call_BlinkXP_1591
                deb "Seguro. Pásatelo bien."
                $ RunWithDebbie = False #RIAM Don't track this one
                return
        $ resetWalkthrough ()
    scene c16s002_370d with fade
    "Unos minutos después, ya en el bosque..."
    play music ("music/m0450.ogg")
    if Aux:
        mc "Bueno, ayer dijiste que querías hablar de algo. ¿Hay algo que te preocupe?"
    else:
        mc "Te veo muy concentrada, Debbie. ¿Hay algo que te preocupe?"
    call BlinkXP ("c16s002_370" , "d") from _call_BlinkXP_1592
    deb "Me desconciertas, [mc]."
    mc "¿Yo? ¿Por qué? ¿Qué he hecho ahora?"
    call BlinkXP ("c16s002_375a" , "d") from _call_BlinkXP_1593
    if deb._var("kissedBeach"):
        deb "Ahora nada... pero anteayer en la playa..."
        if not deb._var("kissRejected"):
            deb "Nos besamos un par de veces... después ayer otra vez... y me invitaste a correr..."
        else:
            deb "Intentaste besarme... y hoy me invitas a correr..."
        if dap._var("route"):
            deb "Delante de tu novia... que además es tu prima..."
    elif Aux:
        deb "Ahora nada... pero anteayer en la playa..."
        deb "Me aceptaste un beso... pero tú no intentaste besarme..."
        if dap._var("route"):
            deb "Lo entiendo, tu novia estaba allí... y además es tu prima..."
        deb "Y ayer me volviste a aceptar otro beso..."
    else:
        deb "Me invitas a correr y a nadar... como si te gustara pasar tiempo conmigo."
        deb "Pero no intentaste besarme en la playa..."
        if dap._var("route"):
            deb "Lo entiendo, tu novia estaba allí... y además es tu prima..."
    call BlinkXP ("c16s002_375b" , "d") from _call_BlinkXP_1594
    deb "No sé cómo sentirme cuando estás alrededor... no sé de qué va todo esto..."
    mc "No va de nada, Debbie. Me gusta pasar tiempo contigo. Me gusta salir a correr contigo."
    if deb._var("kissedBeach"):
        mc "Si quise besarte es porque Kate dijo que besáramos a quien nos atrajera. Y tú me atraes. Nunca miento, ni siquiera en un juego. Y si estamos aquí es porque me gusta pasar tiempo contigo."
    elif Aux:
        mc "No podía, y no quería, rechazarte el beso, pero aún no estoy seguro de cuánto me atraes. Nunca miento, ni siquiera en un juego. Y si estamos aquí es porque me gusta pasar tiempo contigo."
    else:
        mc "Ninguno de los dos intentó besar al otro. Y los dos estamos aquí, pasando tiempo juntos. Supongo que es porque nos gusta."
    call BlinkXP ("c16s002_380" , "d") from _call_BlinkXP_1595
    if dap._var("route") and Aux:
        deb "Pero... ¿Y [dap]? También la besaste a ella... lo cual es lógico, claro..."
    elif dap._var("route"):
        deb "Pero... ¿Y [dap]? A ella la besaste... lo cual es lógico, claro..."
    if dap._var("route"):
        if mc._var("relationships") > 1:
            mc "[dap] y yo tenemos una relación especial. Ella acepta que yo salga con otras chicas."
            call BlinkXP ("c16s002_385" , "d") from _call_BlinkXP_1596
            deb "¿Qué? ¿Sales con más chicas?"
            mc "Sí, y antes de que me juzgues, debo decirte que todas lo aceptan."
        else:
            mc "[dap] y yo tenemos una relación especial. Ella aceptaría que yo saliera con otras chicas."
            deb "¿No sales con nadie más? Después de lo que dijo [sai] ayer..."
            mc "No, al menos por ahora. Y antes de que me juzgues, debo decirte que, si lo hiciera, todas estarían informadas."
    else:
        deb "Eso es lo que me extraña. Que quieras pasar tiempo conmigo en vez de... ¿con tu novia?"
        mc "¿Me estás preguntando si salgo con alguien? *Risa*"
        if mc._var("relationships") == 1:
            mc "Salgo con alguien, y no le importa que pase tiempo con otras chicas. No es celosa... o no demasiado."
        elif mc._var("relationships") > 1:
            mc "Salgo con alguien, con más de una chica, y no les importa que pase tiempo con otras chicas. No son celosas... o no demasiado."
            call BlinkXP ("c16s002_385" , "d") from _call_BlinkXP_1597
            deb "¿Qué? ¿Sales con más de una chica?"
            mc "Sí, y antes de que me juzgues, debo decirte que todas lo aceptan."
        else:
            mc "No salgo con nadie ahora mismo. Y aunque lo hiciera, eso no impediría que pasara tiempo con quien quisiera."
    call BlinkXP ("c16s002_390" , "d") from _call_BlinkXP_1598
    deb "¿Ves? A eso me refiero... eres desconcertante... ningún chico ha querido pasar tiempo conmigo..."
    if Aux or deb._var("kissedBeach"):
        deb "Por no hablar de besarme..."
    mc "Es posible que los chicos que has encontrado hasta ahora fueran idiotas. No puedo saberlo."
    call BlinkXP ("c16s002_395" , "d") from _call_BlinkXP_1599
    stop music fadeout (1.5)
    deb "*Risita* También es posible que yo esté viendo cosas donde no las hay."
    play music ("music/Africa.ogg")
    "Justo en ese momento, un remolino de aire llega donde estáis y rodea a Debbie de un tornado de pétalos de flores."
    scene c16s002_400pv with dissolve
    show c16s002_400v with dissolve
    deb "¡Qué bonito! *Risa* ¡Es como estar en una película de Disseny!"
    "Ver así a Debbie, con la cara ilusionada intentando cazar unos pétalos que se le escapan entre los dedos cada vez, es un contraste increíble."
    "Es como ver una niña en el cuerpo de una mujer. Una mujer enorme, pero con la ilusión de una niña."
    mc "Ahora mismo eres como una Princesa Disseny. *Risa*"
    deb "Solo me falta pillar un pétalo, o mejor una flor, y ponérmela en el pelo. *Risa*"
    "Se te ocurre una idea, quizás sea un poco osada..."
    if persistent.walkthrough:
        $ wt1 = "Debbie + 10"
        if deb.rps < -5:
            $ wt2 = _("Tus decisiones anteriores evitan que abras la ruta con Debbie hagas lo que hagas.")
        elif deb.rps < 5:
            $ wt2 = _("Tus decisiones anteriores evitarán que abras la ruta con Debbie si no lo haces.")
        else:
            $ wt2 = ""
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Ponerle una flor en el pelo."  (wt = wt1):
            $ deb.rp (10)
            $ deb._var("flower", True)
            scene c16s002_405An1 with dissolve #ab
            "Una margarita pasa volando por delante tuyo y la cazas al vuelo."
            mc "¿Una como esta?"
            "El remolino sigue su camino, llevándose los pétalos y las flores."
            deb "Exactamente como esa. Además, justo a tiempo. *Risita*"
            call BlinkXP ("c16s002_410" , "d") from _call_BlinkXP_1600
            mc "¿Me permites?"
            deb "Por supuesto... tú la has cazado... para mí... gracias..."
            call BlinkXP ("c16s002_415" , "d") from _call_BlinkXP_1601
        "Mejor no hacerlo."  (wt = wt2):
            scene c16s002_405An2 with dissolve #cd
            "Una margarita pasa volando por delante suyo y Debbie la caza al vuelo."
            mc "¿Una como esa?"
            "El remolino sigue su camino, llevándose los pétalos y las flores."
            deb "Exactamente como esta. Además, justo a tiempo. *Risita*"
            call BlinkXP ("c16s002_420" , "d") from _call_BlinkXP_1602
    mc "Te queda muy bien. Ahora eres una auténtica Princesa Disseny."
    deb "Aunque los pétalos ya se han ido."
    mc "Ahora solo falta que cantes y que se te pose un pajarillo en el dedo."
    call BlinkXP ("c16s002_425" , "d") from _call_BlinkXP_1603
    deb "*Risa* Mejor no, creo que habría una migración de aves en California si me pongo a cantar. En dirección contraria a mi dedo."
    mc "No me lo creo. *Risa* ¿Seguimos?"
    deb "Sí, sigamos hasta el lago. Tengo ganas de bañarme."
    stop music fadeout (1.5)
    scene black with dissolve
    "El remolino de pétalos ha sido una experiencia bonita, pero ha interrumpido la conversación que estabais teniendo sobre como desconciertas a Debbie."
    "Con lo tímida que es, va a ser difícil volver a hablar del tema."
    call BlinkXP ("c16s002_430" , "f") from _call_BlinkXP_1604
    play music ("music/From-Above.ogg")
    "Unos minutos después, en el lago, una vez os habéis cambiado de ropa cada cual en su arbusto habitual..."
    mc "¿Nos bañamos?"
    if deb._var("flower") and deb.rps > 4:
        deb "Dame un segundo. Quiero guardar la flor."
        scene c16s002_435AnBlink with dissolve # d-e-Blink
        deb "Ya está. Así se secará y durará por siempre."
        mc "¿Llevas un libro cuando sales a correr?"
        deb "Estudio Literatura, [mc], y tengo que volver sola. Si encuentro un sitio bonito donde quedarme a leer..."
        mc "Pero es una flor corriente..."
        call BlinkXP ("c16s002_440" , "d") from _call_BlinkXP_1605
        deb "Puede que la flor sea corriente, pero la has cazado tú para mí."
        deb "Verla me recordará siempre el remolino de pétalos y como me pusiste la flor en el pelo."
        mc "Eso es muy bonito, Debbie."
    deb "¡Vamos!"
    scene c16s002_435An with dissolve # fg
    deb "¡No te quedes atrás! *Risa* ¡Sólo tenemos media hora!"
    "Otra vez aparece la niña adorable para sustituir a la tímida mujer."
    play sound ("music/Splash.ogg")
    if deb._var("flower") and deb.rps > 4:
        call BlinkXP ("c16s002_445a" , "f") from _call_BlinkXP_1606
    else:
        call BlinkXP ("c16s002_445b" , "f") from _call_BlinkXP_1607
    deb "El agua está a la temperatura perfecta hoy. Ni muy fría ni muy caliente. Y es tan transparente..."
    mc "Este lago siempre ha estado muy limpio. Casi nadie sube aquí nunca y los arroyos que lo alimentan bajan muy limpios."
    mc "Solo está turbio los días después de llover. La lluvia arrastra barro de las laderas, pero en un par de días vuelve a estar transparente."
    call BlinkXP ("c16s002_445a" , "d") from _call_BlinkXP_1608
    deb "Eso me da una idea... ¿has jugado alguna vez a buscar tesoros en este lago? Lisa y yo jugábamos en la playa."
    mc "¿Buscar tesoros? No creo que haya nada interesante..."
    call BlinkXP ("c16s002_450" , "d") from _call_BlinkXP_1609
    deb "Bueno, no consiste en encontrar doblones españoles. *Risa*"
    deb "Consiste en hacer una inmersión buscando cosas en el fondo. El que consiga encontrar la cosa más bonita, valiosa, o rara, gana la ronda."
    mc "Suena interesante. Nunca he buscado nada aquí. ¡Hagámoslo!"
    mc "Pero ¿hay premio para el que gane?"
    call BlinkXP ("c16s002_455" , "d") from _call_BlinkXP_1610
    deb "Nunca he jugado por un premio. Siempre he jugado por diversión..."
    mc "Si estuviera Kate aquí seguro que decía que el que pierde paga prenda. *Risa*"
    call BlinkXP ("c16s002_460" , "d") from _call_BlinkXP_1611
    if deb.rps > 4:
        deb "Pero no lo vamos a hacer, ¿verdad? ¿Qué te parece un beso?"
        mc "¿Cómo funcionaría? Un beso es mutuo..."
        deb "Si tú encuentras el mejor tesoro, te beso yo... si lo encuentro yo, me besas tú..."
        mc "Es decir, que habrá beso después de cada ronda, ¿no?"
        call BlinkXP ("c16s002_465" , "d") from _call_BlinkXP_1612
        deb "A menos que haya empate... *Risita*"
        mc "*Risa* A menos que haya empate."
        if persistent.walkthrough:
            $ wt1 = _("Ruta con Debbie abierta.")
            $ wt2 = _("Ruta con Debbie cerrada. \n{color=#ff0000}{b}No habrá más oportunidades de abrir la ruta.{/b}{/color}")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Me parece un premio genial."  (wt = wt1):
                $ deb._var("route", True)
                $ mc._var("relationships", 1, "add")
                mc "No sé si me apetece ganar o perder. Pero seguro que no quiero empatar."
                call BlinkXP ("c16s002_470b" , "d") from _call_BlinkXP_1613
                deb "Te aseguro que estoy en la misma situación. *Risita*"
                mc "¿Empezamos a jugar? Al mejor de tres."
            "Creo que deberíamos jugar sin premios." (wt = wt2):
                mcp "(Me duele hacerte esto, Debbie, pero no puedo dejar que te ilusiones viendo cosas donde no las hay.)"
                mc "No me malinterpretes, me gustas, pero creo que esto podría llevar a algo que no deberíamos hacer."
                mc "Me gustas, pero no de ese modo, Debbie, lo siento."
                call BlinkXP ("c16s002_470a" , "d") from _call_BlinkXP_1614
                deb "Pero... pero... creo que... tú también me has malinterpretado..."
                deb "No es que... quiera salir contigo... No. Nada de eso... es solo que... besarte es divertido..."
                mc "¿Te parece bien si dejamos los besos sólo como buenos días y buenas noches?"
                call BlinkXP ("c16s002_475" , "d") from _call_BlinkXP_1615
                deb "Ermmm... sí, vale. Así evitaremos... malentendidos..."
                deb "Podríamos jugar por... no sé... El que gane menos rondas le paga una cerveza al otro."
                mc "Me parece genial. Al mejor de tres ¿Empezamos a jugar?"
    else:
        deb "Pero no lo vamos a hacer, ¿verdad? ¿Qué te parece una cerveza? El que gane menos rondas le paga una cerveza al otro."
        mc "Me parece genial. ¿Empezamos a jugar? Al mejor de tres."
    scene c16s002_480a with fade
    "Te sumerges y buscas por el fondo del lago y solo encuentras una piedra con una forma especial antes de que tus pulmones empiecen a pedirte aire."
    scene c16s002_480b with fade
    "Cuando sacas la cabeza del agua Debbie todavía está sumergida. Como dijo Kim, es como una sirenita. ¿O lo dijiste tú?"
    scene c16s002_480c with dissolve
    play sound ("music/Splash.ogg")
    "Aparece de pronto, como surgida de la nada, esparciendo agua a su alrededor."
    call BlinkXP ("c16s002_485" , "d") from _call_BlinkXP_1616
    deb "¿Qué has encontrado? Tenías razón sobre que estaba muy limpio, es difícil encontrar nada."
    mc "¿Lo enseñamos a la vez?"
    deb "¡Venga!"
    scene c16s002_480d with dissolve #manos
    deb "Una taza oxidada. *Risa*" (multiple=2)
    mc "Una piedra. *Risa* Pero tiene una forma especial." (multiple=2)
    mc "Mal empezamos si lo primero que encuentras es una lata. Te acabo de hacer publicidad de que el lago estaba muy limpio. *Risa*"
    deb "¿Has encontrado una piedra que parece un corazón? Está claro que esta ronda la ganas tú. 1-0."
    if deb._var("route"):
        call BlinkXP ("c16s002_485b" , "d") from _call_BlinkXP_1617
        deb "Es el momento de que te pague, ¿no?"
        mc "Por supuesto. ¡Quiero mi pago!"
        scene c16s002_480e with dissolve
        "El beso de Debbie es muy tierno, como todas las veces que te ha besado hasta ahora. Pero hay algo más, una seguridad que no habías notado anteriormente."
        mcp "(Aceptar besos como pago la ha hecho sentirse más segura de sí misma. Es una buena señal.)"
        "El beso acaba abruptamente, como si a Debbie se le hubiera ocurrido una idea de repente."
        call BlinkXP ("c16s002_490" , "d") from _call_BlinkXP_1618
        deb "¿Puedo pedirte un favor?"
        mc "Lo que quieras."
        deb "¿Me regalas la Piedra Corazón?"
        mc "Lo que quieras menos eso. No puedo, Debbie, es muy valiosa."
        call BlinkXP ("c16s002_495" , "d") from _call_BlinkXP_1619
        deb "Pero si solo es una piedra..."
        mc "Pero encontrarla me ha hecho ganar un beso de una chica preciosa. Tiene que ser una piedra increíble."
        mc "Te la podría vender... por otro beso..."
        call BlinkXP ("c16s002_500" , "d") from _call_BlinkXP_1620
        deb "No puedo aceptar. *Risita* Si es tan valiosa... sentiría que te estoy timando."
        mc "Mmmmm... ¿qué propones, entonces?"
        deb "¿Qué te parecería un pago a plazos?"
        mc "¿Cómo funcionaría eso? ¿Tengo que llamar a mi abogado?"
        deb "Un beso ahora y puedes venir a por más cuando quieras. *Risita*"
        mc "Me parece un trato que no voy a poder rechazar. Creo que podemos dejar a los abogados en sus despachos."
        deb "Pues aquí va el primer pago..."
        scene c16s002_480e with dissolve
        mcp "(Cada vez es más segura besando, también más ansiosa. Demostrarle que yo también quiero estos besos lo está cambiando todo para ella.)"
        call BlinkXP ("c16s002_505" , "d") from _call_BlinkXP_1621
        deb "¡Wow! Lo de dejarme sin aliento, ¿es alguna táctica para que tenga menos tiempo para buscar algo en la siguiente ronda?"
        mc "El premio es tan sabroso que tengo que utilizar todos los trucos sucios a mi alcance. *Risa*"
        scene c16s002_480f with dissolve #deb corriendo hacia la mochila
        deb "Dame un segundo que voy a guardar mi Piedra Corazón en la mochila. No quiero perderla."
        mc "Es tuya, mientras sigas pagando los plazos. *Risa*"
    call BlinkXP ("c16s002_510" , "d") from _call_BlinkXP_1622
    mc "¿Segunda ronda?"
    deb "Vamos. Esta vez tengo que encontrar algo que te supere o habrás ganado la partida."
    scene c16s002_515a with dissolve
    if deb._var("route"):
        "Debbie ha dejado su taza al lado de su mochila. Ya la recogeréis cuando acabe la partida."
    else:
        "Lanzáis la taza y la piedra fuera del lago, ya las recogeréis cuando acabe la partida."
    "Os volvéis a sumergir y a rebuscar en el fondo del lago. No está tan limpio cómo creías, con varias botellas y latas repartidas por el fondo."
    "Supones que algún excursionista las dejaría en el bosque y serían arrastradas por la lluvia."
    "Los pulmones no aguantan más antes de que tengas que salir con una lata en la mano."
    call BlinkXP ("c16s002_520" , "d") from _call_BlinkXP_1623
    deb "Creía que tendría que ir a buscarte... *Risa* O que te habías ahogado."
    mc "No había piedras bonitas esta vez. *Risa* ¿Qué has encontrado?"
    scene c16s002_515b with dissolve
    deb "*Risa* ¡Una lata!" (multiple=2)
    mc "*Risa* ¡Una lata esta vez!" (multiple=2)
    deb "*Risa*" (multiple=2)
    mc "*Risa*" (multiple=2)
    deb "Eso significa empate, ¿no?"
    call BlinkXP ("c16s002_525" , "d") from _call_BlinkXP_1624
    mc "Bueno, creo que tu lata está en bastante mejor estado que la mía, aún tiene la anilla, con lo que yo te daría por ganadora de esta ronda."
    if deb._var("route"):
        mc "Además, con un empate me quedo sin beso y tendría que empezar a cobrar los de la Piedra Corazón. *Risa*"
        deb "¿Prefieres perder tú a quedarte con el empate? *Risita*"
        mc "Es imposible que besarte signifique perder, Debbie."
        call BlinkXP ("c16s002_530" , "d") from _call_BlinkXP_1625
        deb "¡Ufff! ¿Sabes que me podría acostumbrar a oír esas cosas?"
        mc "Y yo me podría acostumbrar a decírtelas. Y ahora tengo que pagar."
        scene c16s002_535An1 with dissolve #ab(lengua)c(sorpresa) beso abriendo boca y se tiene que ver la lengua
        mcp "(Veamos qué pasa si ponemos un poco de lengua en el beso)"
        deb "*Jadeo de sorpresa*"
        scene c16s002_535An2 with dissolve #dba repeat
        "Después de la sorpresa inicial, Debbie entiende lo que tiene que hacer y, sorprendentemente, su lengua sigue la tuya con mucha agilidad."
        "Poco a poco el beso va subiendo la velocidad y la pasión."
        call BlinkXP ("c16s002_540" , "d") from _call_BlinkXP_1626
        deb "¡Ufff! Eso ha sido alucinante. Y otra vez me falta la respiración."
        mc "Ha sido nuestro primer beso... \"de verdad\". Si quieres vendrán más."
        call BlinkXP ("c16s002_545" , "d") from _call_BlinkXP_1627
        deb "¿Si quiero? ¿Puedo elegir?"
        deb "Los besos de antes me ponían la carne de gallina. Este ha convertido mis piernas de gelatina."
        mc "¿Y cuáles prefieres?"
        call BlinkXP ("c16s002_550" , "d") from _call_BlinkXP_1628
        deb "¿Por qué no ambos? Creo que debe haber uno para cada circunstancia, ¿no?"
        mc "Bien pensado. ¿Última ronda?"
    else:
        deb "Me parece bien, eso nos deja la última ronda para decidir quién gana."
        mc "¿Vamos a por ella?"
    scene c16s002_555An with dissolve #550a-a deb salta al agua
    deb "¡Vamos!"
    scene c16s002_555b with dissolve
    "Te diriges a la otra orilla antes de sumergirte. No queda nada interesante donde has estado buscando hasta ahora."
    scene c16s002_555c with dissolve
    "Sigues buscando por el fondo del lago sin ver nada que te llame la atención. Puedes ver que Debbie está en la misma situación a través de la cristalina agua del lago."
    scene c16s002_555d with dissolve
    "Encuentras una piedra redondeada y pulida. No es la Piedra Corazón, pero es mejor que otra lata. Subes a la superficie antes de quedarte sin aire."
    call BlinkXP ("c16s002_560" , "d") from _call_BlinkXP_1629
    "Debbie ya está allí, esperándote con las manos en la espalda. Mala señal para tu sencilla piedra."
    deb "¿Qué has encontrado esta vez?"
    mc "Vamos a mostrarlo a la vez. Esta ronda designa el ganador."
    if deb._var("route"):
        scene c16s002_565e with dissolve
        mc "Otra piedra. Pero más simple."
        call BlinkXP ("c16s002_575" , "d") from _call_BlinkXP_1630 #contenta
        mc "¿Debbie? ¿Qué has encontrado?"
        scene c16s002_565An #e-f (D coge la mano de M por debajo) - g (D coge la mano de M por encima)
        deb "Esto. Y no voy a aceptar que me digas que no he ganado la ronda."
        call BlinkXP ("c16s002_565" , "d") from _call_BlinkXP_1631
        deb "A ti."
        mc "¡Wow, Debbie! Me siento super halagado ahora mismo..."
        call BlinkXP ("c16s002_580" , "d") from _call_BlinkXP_1632
        deb "¿Pero...?"
        mc "¿Qué? ¡No! No hay ningún pero. Me ha sorprendido como lo has dicho."
        call BlinkXP ("c16s002_585" , "d") from _call_BlinkXP_1633
        deb "¿Puedo serte sincera?"
        mc "Siempre."
        deb "No sé qué está pasando."
        deb "Me gustas. Mucho. Y me gusta que nos besemos. Pero no sé qué somos... o si somos algo. No hemos hablado de nada. Tan solo hemos empezado a besarnos como..."
        mc "¿Como si fuera lo más natural del mundo?"
        call BlinkXP ("c16s002_590" , "d") from _call_BlinkXP_1634
        deb "Exacto. No sé cómo funciona esto. No sé si tenemos que decidir... o decir si eres mi novio o no. O si solo soy una amiga con derecho a besos. No sé nada..."
        mc "No hace falta decir o decidir nada. Tú también me gustas mucho..."
        if mc._var("relationships")>0:
            mc "Pero ya sabes que hay alguien más."
            if dap._var("route"):
                call BlinkXP ("c16s002_595" , "d") from _call_BlinkXP_1635
                deb "Sí, [dap]. Y no sé si está bien que le haga esto."
                mc "No le estás haciendo nada. Ella sabe, y acepta, que puedo salir con otras chicas."
            call BlinkXP ("c16s002_600" , "d") from _call_BlinkXP_1636
            deb "Eso me sorprende aún más. Saliendo con alguien quieres pasar tiempo conmigo... besarme... y..."
        else:
            mc "Y ya te he dicho que no salgo con nadie ahora mismo."
            call BlinkXP ("c16s002_600" , "d") from _call_BlinkXP_1637
            deb "Eso me desconcierta aún más. Pudiendo salir con quien quisieras, quieres pasar tiempo conmigo... besarme... y..."
        mc "De momento dejémoslo ahí. No sigas con ese \"y\"."
        mc "Me gusta pasar tiempo contigo. Me gusta besarte. Y el día que quieras, continuaremos con ese \"y\", pero no ahora."
        call BlinkXP ("c16s002_605" , "d") from _call_BlinkXP_1638
        deb "¿Me estás diciendo que soy tu novia? ¿O una amiga con derecho a roce como era [sai]? ¿O alguien con quien pasar el rato si no hay otra chica disponible?"
        mc "No me gustan las etiquetas, pero desde luego no eres con quien pasar el rato. Ahora soy yo el que tiene una pregunta."
        mc "¿Qué quieres que seamos?"
        call BlinkXP ("c16s002_610" , "d") from _call_BlinkXP_1639
        deb "¿Qué? ¿Tengo que decidirlo yo?"
        mc "Tú tienes que decidir qué quieres que seamos. Lo que tú quieres es algo que no puedo decidir yo."
        call BlinkXP ("c16s002_615" , "d") from _call_BlinkXP_1640
        if deb._var("flower"):
            deb "No tengo ni idea... hace un rato, cuando me has puesto la flor en el pelo, te hubiera dicho que preferiría ser tu novia. Y no nos habíamos besado... de verdad."
        else:
            deb "No tengo ni idea... hace un rato, cuando hemos salido de casa, te hubiera dicho que preferiría ser tu novia. Y no nos habíamos besado... de verdad."
        deb "Pero creo que tienes razón. Quizás sea pronto para poner etiquetas todavía, ¿no?"
        mc "Me parece bien. Cuando lo tengamos más claro, podemos poner las etiquetas que queramos, o inventarnos una que sólo nos defina a nosotros."
        call BlinkXP ("c16s002_620" , "d") from _call_BlinkXP_1641
        deb "Pero lo que no te voy a perdonar es mi premio... si quieres dármelo."
        mc "Un Marks siempre paga sus deudas. *Risa*"
        scene c16s002_535An3 with dissolve #ab(lengua)db beso abriendo boca y se tiene que ver la lengua repeat!!!!
        "Esta vez el beso tiene una pasión desatada que no ha tenido ninguno de los anteriores."
        "Tienes que luchar con tus manos para que no empiecen a recorrer el cuerpo de Debbie, empezar a seguir los picos y valles de su musculatura."
        call BlinkXP ("c16s002_625" , "d") from _call_BlinkXP_1642
        deb "¡Ufff! Me ha costado tener las manos quietas, [mc]."
        mc "A mí me ha pasado lo mismo. Pero puedes usarlas si quieres."
        deb "Pero me has dicho que no continuara con el \"y\"..."
        mc "¿Te referías a eso? ¡Oops! Te malentendí, culpa mía."
        call BlinkXP ("c16s002_630" , "d") from _call_BlinkXP_1643
        deb "¿Qué habías entendido?"
        mc "..."
        call BlinkXP ("c16s002_635" , "h") from _call_BlinkXP_1644
        deb "¡Oh! ¡No! ¡Qué idiota soy! Para ti unos besos están más que superados... tú ya estabas pensando en... eso..."
        mc "No, Debbie, no estaba pensando en \"eso\". Hay muchos pasos intermedios entre los besos y \"eso\". Y quiero que los demos juntos."
        call BlinkXP ("c16s002_640" , "d") from _call_BlinkXP_1645
        deb "Ahora mismo te debo parecer una niña tonta para la que unos besos son un tesoro..."
        mc "Para nada, cielo. Tus besos son un tesoro, y cada paso que demos hacia \"eso\" lo será también, pero los daremos cuando llegue el momento y cuando estés cómoda con ello."
        eva "¡Ejem!"
        scene c16s002_645AnBlink with dissolve #d (eva) - Blink Debbie sorprendida
        deb "¡Oh, [dap]! ¡Esto no es lo que parece!"
    else:
        scene c16s002_565d with dissolve
        deb "Una herradura." (multiple=2)
        mc "Otra piedra. Pero más simple." (multiple=2)
        call BlinkXP ("c16s002_570" , "d") from _call_BlinkXP_1646
        deb "¡Sí! Definitivamente esta vez he ganado yo."
        mc "Desde luego. Esa herradura debe llevar décadas ahí. Te debo una cerveza."
        call BlinkXP ("c16s002_575b" , "d") from _call_BlinkXP_1647
        deb "Un día que vayamos a la ciudad me la pagas. Ahora me debería ir yendo a secar y a vestir. Quiero llegar a casa y ducharme."
        mc "Perfecto. En unos minutos llegará mi cita."
        eva "¡Ejem!"
        scene c16s002_645AnBlink with dissolve #d (eva) - Blink Debbie sorprendida
        deb "¡Oh, [dap]! ¿Qué haces aquí?"
    mc "Hola, Eva. No es [dap], Debbie. Ven, os presento. Tengo que explicarte algo."
    scene black with dissolve
    "Después de las presentaciones y de que Debbie se cambie, Eva os deja un poco de espacio para que puedas tener La Conversación con Debbie."
    call BlinkXP ("c16s002_650" , "d") from _call_BlinkXP_1648
    deb "Es alucinante. Si no tuviera a Eva delante de mis ojos, te diría que me estás tomando el pelo."
    if persistent.family:
        deb "Solo pensar que es un clon de [dap]... o de [eri]... No me lo puedo creer..."
    else:
        deb "Solo pensar que [dap] y [eri] son clones suyos... No me lo puedo creer..."
    deb "No podía imaginar que estas cosas pasaran..."
    mc "Hoy os lo iban a contar [mar] y [nor], después de contárselo a [emm], [eri], y [dap]."
    mc "Como has venido a correr conmigo no han tenido la oportunidad de hacerlo contigo."
    call BlinkXP ("c16s002_655" , "d") from _call_BlinkXP_1649
    deb "Gracias por confiar en nosotras con un secreto tan grande."
    mc "No creo que vayáis a hacer nada que perjudique a las chicas, y de todas formas, Eva va a venir a comer hoy a casa, con lo que lo descubriríais igualmente."
    deb "Nunca haría nada que pudiera hacer daño a [emm], [eri], o [dap]. Lisa tampoco. Y pondría la mano en el fuego por el resto."
    deb "Pero ahora os voy a dejar con vuestras cosas. Voy a volver a casa para ver si puedo ayudar en algo."
    if deb._var("route"):
        call KissXP ("c16s002_660" , "d") from _call_KissXP_50
        "Es un beso tierno, no sensual. Es un beso que dice \"te veré luego y continuaremos\"."
        deb "Hasta luego, guapo. Recuerda que me llevo la Piedra Corazón y que puedes cobrar tus besos cuando quieras."
        mc "Hasta luego, preciosa. Lo haré."
    else:
        deb "Hasta luego, [mc]."
        mc "Nos vemos en casa, Debbie."
    scene c16s002_660c with dissolve
    deb "Hasta dentro de un rato, Eva."
    stop music fadeout (1.5)
    eva "Te veo en casa, Debbie."
    return
label c16s003_ShootingLessons:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_30
        call mrS3_sca_route from _call_mrS3_sca_route_23
        call mrS3_oma_route from _call_mrS3_oma_route_15
        call mrS3_meg_route from _call_mrS3_meg_route_6
        call mrS3_mar_route from _call_mrS3_mar_route_34
        call mrS3_nor_route from _call_mrS3_nor_route_26
        call mrS3_emm_route from _call_mrS3_emm_route_37
        call mrS3_eri_route from _call_mrS3_eri_route_29
        call mrS3_eil_route from _call_mrS3_eil_route_21
        call mrS3_sam_route from _call_mrS3_sam_route_20
        call mrS3_sim_route from _call_mrS3_sim_route_19
        call mrS3_sai_route from _call_mrS3_sai_route_17
        call mrS3_deb_route from _call_mrS3_deb_route_22
        menu:
            "¿Has pre-abierto la relación con Meemaw?"
            "Sí":
                $ mee._var("route" , True)
            "No":
                $ mee._var("route" , False)
        menu:
            "¿Fuiste a correr con Debbie?"
            "Sí":
                $ RunWithDebbie = True
            "No":
                $ RunWithDebbie = False
        menu:
            "¿Amanda y Eva te dieron los test de embarazo?"
            "Sí":
                $ KnownToAmandaEva = 1
            "No":
                $ KnownToAmandaEva = 0
        call mrS3_edmund_story from _call_mrS3_edmund_story_9
    play music ("music/Throne-King.ogg")
    call BlinkXP("c16s003_005" , "f") from _call_BlinkXP_1650
    if RunWithDebbie:
        eva "Llegas tarde."
        mc "No, llevo aquí media hora."
        eva "36 minutos. Con lo que empezamos 6 minutos tarde."
        mc "¿Has estado aquí todo este tiempo? ¿Por qué no nos has avisado?"
        call BlinkXP("c16s003_010" , "d") from _call_BlinkXP_1651
        eva "Porque habíamos quedado a las 12. Yo he venido antes para prepararlo todo. Y no quería interrumpir vuestro... juego."
        eva "Pero a las 12 eres mío. Tú pediste que te enseñara y lo voy a hacer, pero pido puntualidad."
    else:
        "Cuando llegas al lago, Eva ya te está esperando, con cara de evidente enfado."
        eva "Llegas tarde."
        mc "Lo siento, he tenido que llevar a Meemaw al médico para un chequeo."
        call BlinkXP ("c16s003_005b" , "d") from _call_BlinkXP_1729
        eva "¿Está bien?"
        mc "Sí, era sólo un chequeo por sus enfermedades. Nada importante."
        call BlinkXP("c16s003_005" , "d") from _call_BlinkXP_1730
        eva "Con lo que empezamos 6 minutos tarde por algo que no era importante. Dijimos que a las 12 eras mío."
        eva "Tú pediste que te enseñara y lo voy a hacer, pero pido puntualidad."
    mc "De acuerdo, disculpa. No sabía que 6 minutos fueran tan importantes."
    call BlinkXP("c16s003_015" , "d") from _call_BlinkXP_1652
    eva "Vamos a tratar con armas de verdad, [mc], todo es importante. ¿Vamos?"
    mc "¿Dónde?"
    eva "Ahí detrás de ese repecho. Más tranquilos que en el lago. Menos animales... y menos personas."
    mc "Perfecto. Te sigo."
    if meg._var("route"):
        $ Aux = 1
    else:
        $ Aux = 0
    if mad._var("route"):
        $ Aux = Aux + 1
    if mee._var("route"):
        $ Aux = Aux + 1
    if deb._var("route"):
        call BlinkXP("c16s003_020" , "d") from _call_BlinkXP_1653
        $ Aux = Aux + 1
        if mc._var("relationships")>1:
            eva "¿Así que otra más para el harén? No sabía que te gustaban musculosas."
        elif mc._var("relationsips")==Aux:
            eva "No sabía que te gustaban musculosas."
        mc "Sin querer parecer maleducado, no creo que..."
        call BlinkXP("c16s003_025" , "d") from _call_BlinkXP_1654
        eva "¿Que sea asunto mío? ¡Oh! No lo es, solo hacía una observación."
        eva "*Susurrando para sí misma* Pero si no llego a interrumpiros te hubieras podido acostar con ella."
        mc "Sabes que te he oído, ¿verdad?"
        mc "Debbie y yo aún no estamos ahí."
        call BlinkXP("c16s003_030" , "d") from _call_BlinkXP_1655
        eva "¡Oops! No pretendía que me escucharas."
        eva "Me refería a que, está claro lo que la chica siente por ti..."
        mc "Bueno, hoy hemos dado un paso, pero sigo pensando que es algo que no te debería importar."
    if mc._var("relationships")>0:
        call BlinkXP("c16s003_035" , "d") from _call_BlinkXP_1656
        mc "Tengo una pregunta..."
        if deb._var("route"):
            mc "Con todo el tema de las cámaras y el espionaje... ¿sabéis con quién más salgo? ¿Y cuánto habéis visto?"
        else:
            mc "Con todo el tema de las cámaras y el espionaje... ¿sabéis con quién salgo?"
        if mc._var("relationships") == Aux:
            call BlinkXP("c16s003_040" , "d") from _call_BlinkXP_1657
            eva "¿Sales con alguien? No teníamos ni idea..."
            mc "Es bueno que no lo sepáis todo."
        else:
            call BlinkXP("c16s003_045" , "d") from _call_BlinkXP_1658
            if mar._var("route"):
                eva "[mar]. Os vimos al volver de vuestra cita."
                if emm._var("route"):
                    eva "Y sí, vimos lo de anoche. Fue bonito y sexy a partes iguales."
            if nor._var("route"):
                eva "[nor]. Os hemos visto un par de veces."
            if emm._var("route"):
                eva "[emm]. Solo una vez contigo en solitario."
                mc "¿A qué te refieres a una vez \"conmigo\"?"
                eva "No te voy a contar lo que hacen las chicas cuando están solas en su habitación o en la ducha."
                eva "Pregúntales a ellas... si te atreves."
            if dap._var("route"):
                eva "[dap]. Suponemos lo que pasó hace un par de noches, pero no sabemos dónde estabais. Pero hemos visto las lecciones."
            if eri._var("route"):
                eva "[eri]. Sabemos lo que pasó en la playa, pero no lo vimos. ¡Deberías de dejar de moverte tanto, es difícil seguirte!"
            if sca._var("route"):
                eva "Obviamente vimos lo de [sca]. Las lecciones y lo que pasó en vuestra cita. Aunque nos perdimos tu primera visita a su casa."
                mc "¿Por qué pusisteis cámaras en su casa?"
                call BlinkXP("c16s003_050" , "d") from _call_BlinkXP_1659
                eva "Bueno... [dap] pasaba bastante tiempo allí..."
                mc "Pero no las pusisteis en meses, hasta que llegué yo. Hasta que yo fui de visita."
                eva "Bueno... en ese momento ya erais dos los que visitabais la casa... tenía sentido... ¿no?"
                mc "*Risa* No, pero sigue."
                eva "Vale, oímos como [sca] le explicaba a [dap] sus problemas con Kevin. Creímos que podía ayudar... No nos gustan los violadores ni los acosadores."
                mc "Gracias. Ayudó. No como pensábamos, pero ayudó."
                call BlinkXP("c16s003_045" , "d") from _call_BlinkXP_1660
            if eil._var("route"):
                if not oma._var("route"):
                    eva "Sabemos que estás con [eil]. Es fácil saberlo, sabiendo que le has dado uno de los tests."
                else:
                    eva "Con [eil] te vimos aquí durante el trío con Alexia. Sexy. Eres insaciable. *Risa*"
            if oma._var("route") and not eil._var("route"):
                eva "Alexia. Lo descubrimos cuando te encontraste en el lago con ella y con [eil]. No sabemos cuándo empezasteis."
            if sai._var("route"):
                eva "Sabemos que estás con [sai], por la conversación que tuvisteis el otro día en tu habitación, pero no os hemos visto hacer nada."
            else:
                eva "Sabemos que no estás con [sai], por la conversación que tuvisteis el otro día en tu habitación."
                eva "Sé que presentarse así, sin avisarte, estuvo mal, pero deberías perdonarla. Ha cambiado toda su vida por ti."
            eva "Esperábamos un reencuentro más fogoso. Me hiciste perder una apuesta. *Risita*"
            if sam._var("route") and sim._var("route"):
                eva "Y lo de [sam] y [sim] lo descubrimos en la playa. Suponemos que por eso visitas tanto su casa."
            elif sam._var("route"):
                eva "Y lo de [sam] lo descubrimos en la playa. Suponemos que por eso visitas tanto su casa."
            elif sim._var("route"):
                eva "Y lo de [sim] lo descubrimos en la playa. Suponemos que por eso visitas tanto su casa."
            if sam._var("route") or sim._var("route"):
                mc "Que no tiene y no va a tener cámaras, ¿verdad?"
                eva "No hemos tenido tiempo de ponerlas, y no las pondremos si no quieres."
                mc "No, no quiero."
                eva "Vaaale..."
    if meg._var("route") and mad._var("route"):
        mcp "(Vale, no saben nada de Maddie ni [meg].)"
    elif meg._var("route"):
        mcp "(Vale, no saben nada de [meg].)"
    elif mad._var("route"):
        mcp "(Vale, no saben nada de Maddie.)"
    if mad._var("route"):
        mcp "(¡Oh, mierda! Tenía que ir a buscar a Maddie a la tienda hoy, pero Amanda va a cenar en casa y debería estar con ella. Luego la llamaré.)"
        if mar._var("route") or nor._var("route"):
            mcp "(Y, además, las 24 horas del test también coinciden... mierda.)"
    mc "¿Vais a dejar de espiarme?"
    call BlinkXP("c16s003_055" , "d") from _call_BlinkXP_1661
    eva "En las habitaciones y en los baños sí. Hoy quitaré las cámaras. Tal como habíamos quedado."
    mc "¿Y lo de seguirme a todos lados?"
    eva "No te hemos seguido a casi ningún sitio. Especialmente cuando ibas solo. Si lo hubiéramos hecho, seguramente le hubiera pegado un tiro a Jack cuando te atacó con el cuchillo."
    call BlinkXP("c16s003_060" , "d") from _call_BlinkXP_1662
    eva "Pero yo estaba ocupada..."
    mc "Pero sabéis lo que pasó..."
    call BlinkXP("c16s003_065" , "d") from _call_BlinkXP_1663
    eva "Cámaras en el café. Las pusimos cuando [eri] empezó a trabajar allí."
    mc "Vale. Esas las podéis mantener si queréis."
    call BlinkXP("c16s003_070" , "d") from _call_BlinkXP_1664
    if KnownToAmandaEva > 0:
        $ PregnancyTests = True
        eva "¿Ya has repartido muchos tests?"
        mc "Bueno, supongo que ya sabéis cuantos, ¿no?"
        call BlinkXP("c16s003_075" , "d") from _call_BlinkXP_1665
        if mar._var("route") and emm._var("route"):
            eva "Aparte de lo de anoche no he mirado los videos. Amanda se ocupa de eso."
            mc "Me acabas de hacer sentir como un espectáculo porno andante. *Risa*"
            call BlinkXP("c16s003_080" , "d") from _call_BlinkXP_1666
            eva "Podrías ganarte la vida con el porno, desde luego. *Risa*"
    elif deb._var("route"):
        $ PregnancyTests = False
        eva "Volviendo a Debbie. Tengo que suponer que te acabarás acostando con ella."
        mc "Otra vez, no es algo de lo que quiera hablar ahora mismo. Pero supongo que, si la cosa avanza, sí, acabará pasando."
    else:
        $ PregnancyTests = False
        eva "Volviendo al tema de tus relaciones..."
        mc "No sé si es algo de lo que tengamos que hablar."
    if deb._var("route") and not KnownToAmandaEva > 0:
        call BlinkXP("c16s003_075" , "d") from _call_BlinkXP_1667
        eva "No te lo decía por eso."
        eva "NTR fabrica tests de embarazo ultra rápidos. 72 horas después del sexo se puede saber si una mujer está embarazada."
        mc "Me podría interesar cuando llegue el momento..."
    if deb._var("route"):
        $ KnownToAmandaEva = KnownToAmandaEva + 1
    if mc._var("edmundsStory"):
        mc "Espera... hacéis cosas de medicina avanzada. ¿Tenéis... tenemos tests de ADN?"
        call BlinkXP("c16s003_080" , "d") from _call_BlinkXP_1668
        eva "*Risa* ¿Quieres comprobar si tienes un hijo perdido?"
        mc "Más bien una hermana..."
        scene c16s003_085AnBlink with hpunch #d sorpresa - c16s003_085AnBlink2
        eva "¿Qué?"
        eva "Amanda, ¿has escuchado? ¿Sabes algo?"
        ama "*En la radio* Hola, [mc]. No, Eva, no sabía nada. ¿Qué pasa, [mc]?"
        if persistent.family:
            ama "*En la radio* ¿Piensas que [emm] puede no ser tu hermana?... Eso significaría que yo no... estoy genéticamente emparentada contigo..."
        else:
            ama "*En la radio* Ya sabes que [emm] no es tu hermana, [mc]."
        mc "No es para [emm]. Y me gusta saber cosas que vosotras ignoráis por una vez. *Risa*"
        call BlinkXP("c16s003_090" , "d") from _call_BlinkXP_1669
        eva "No se lo tengas en cuenta, Am. Hoy está haciéndose el difícil."
        ama "*En la radio* Déjame mirar en el ordenador un momento, [mc]."
        "..."
        ama "*En la radio* Sí, NTR fabrica tests de ADN, pero son bastante similares a los del mercado. Nada tan revolucionario como los tests de embarazo."
        ama "*En la radio* Estoy viendo que los de mercado son muy rápidos de por sí. Si quieres, puedo comprar uno y llevártelo esta noche."
        ama "*En la radio* Hay un laboratorio en Atascadero. El martes podrías tener el resultado."
        mc "Gracias, Amanda. Me iría muy bien algo así. No sabía ni por dónde empezar con esto."
        ama "*En la radio* Ningún problema. Luego te lo llevo."
    else:
        scene c16s003_085AnBlink2 with dissolve #e se quita un auricular- f le da un auricular a MC - Blink mientras se toca el oído
        eva "Un momento, [mc]. Amanda quiere saludarte."
        ama "*En la radio* Tan solo quería darte las gracias de nuevo por lo de ayer. Y por darnos la oportunidad de comer con vosotros hoy."
        ama "*En la radio* Eva no te lo va a agradecer, pero va también de su parte."
        call BlinkXP("c16s003_095" , "d") from _call_BlinkXP_1670
        eva "¡Amanda!"
        mc "*Risa* Gracias, pero no hace falta. Fue cosa de [mar] y [nor]. No tuve nada que ver."
    call BlinkXP("c16s003_100" , "d") from _call_BlinkXP_1671
    eva "¿Me lo puedo llevar ya? ¡No me va a dar tiempo de enseñarle nada!"
    ama "*En la radio* *Risa* Sí, llévatelo. Y piensa que, si no acabáis hoy, habrá más lecciones..."
    call BlinkXP("c16s003_105" , "d") from _call_BlinkXP_1672
    eva "¿Y...?"
    if dap._var("route") or sca._var("route"):
        ama "*En la radio* Que ya sabes como acaban las lecciones con [mc]. *Risa*"
    else:
        ama "*En la radio* *Risa* Más oportunidades para conoceros durante las lecciones..."
    mc "Amanda, ¿eres consciente de que aún no le he devuelto el auricular a Eva?"
    ama "*En la radio* ¡Oh, mierda! Devuélveselo ya... Hasta la cena, [mc]."
    mc "Hasta la cena, Amanda."
    call BlinkXP("c16s003_110" , "d") from _call_BlinkXP_1673
    eva "Amanda estaba bromeando..."
    mc "Sí, ya me lo imagino. Como tú el día que te disfrazaste de [eri]..."
    call BlinkXP("c16s003_115" , "d") from _call_BlinkXP_1674
    eva "Sobre eso..."
    mc "¿Por qué no hablamos sobre eso cuando bajemos? Se nos va a hacer tarde para aprender a disparar."
    mc "Aunque no me importará si tenemos que hacer varias lecciones. Y no {b}solo{/b} por lo que ha dicho Amanda."
    call BlinkXP("c16s003_120" , "d") from _call_BlinkXP_1675
    eva "¡Me parece genial! ¡Vamos! Ya estamos llegando."
    mc "Las damas primero."
    call BlinkXP("c16s003_125" , "f") from _call_BlinkXP_1676
    "Llegáis al \"campo de tiro\" y Eva te lo muestra orgullosa."
    eva "He traído unas latas y unos botes. No me gustan las botellas, si llegas a darles no son reutilizables. Además, algún animal se podría cortar con los cristales."
    mc "Me gusta descubrir esa faceta de ti, Eva. No me imaginaba que te preocuparan los animales del bosque."
    call BlinkXP("c16s003_130a" , "d") from _call_BlinkXP_1677
    eva "¿Preocupada por los animales? ¿Yo?"
    eva "Es que... si algún animal se hiriese en una pata... mmmm.... dejaría un rastro de sangre... sí, exactamente eso..."
    eva "Y podría ponérmelo más difícil si alguna vez... no sé... tengo que seguir la pista a uno de mis objetivos a los que haya herido... Sí. Es por eso."
    call BlinkXP("c16s003_130b" , "d") from _call_BlinkXP_1678
    eva "*Mascullando* Como que uno de mis objetivos iba a poder andar si le disparo..."
    mc "Vale. Fingiré que te creo. *Risa*"
    mc "¿Empezamos a disparar?"
    call BlinkXP("c16s003_135" , "d") from _call_BlinkXP_1679
    eva "¡No! Primero la clase teórica. Tienes que aprenderte las cinco leyes de las armas de fuego."
    mc "¿Una clase sobre leyes?"
    call BlinkXP("c16s003_140" , "d") from _call_BlinkXP_1680
    eva "No, idiota. *Risa* Es sobre cómo usar un arma y lo que nunca debes hacer con ella."
    mc "Ah, vale. ¿Tipo \"nunca mires por el cañón de un arma\" y cosas así?"
    eva "Esa es solo para idiotas. Para ti van a ser las cinco leyes básicas. *Risa* Bueno seis."
    mc "Adelante. Soy todo oídos."
    scene c16s003_145An with dissolve #abcdef paseándose con repeat!
    eva "Uno. Nunca apuntes tu arma a algo a lo que no tengas intención de dispararle."
    mc "O lo que es lo mismo, no juegues con ella."
    eva "Exacto. Te sorprendería la cantidad de civiles que os matáis en accidentes idiotas."
    eva "Dos. No acerques tu dedo al gatillo hasta que estés listo para disparar."
    mc "Una buena forma de evitar accidentes."
    call BlinkXP("c16s003_150" , "d") from _call_BlinkXP_1681
    eva "Las leyes para ti acaban de convertirse en siete."
    scene c16s003_145An with dissolve #abcdef paseándose
    eva "Tres. Sé consciente de tu objetivo y de lo que hay más allá."
    mc "No te entiendo."
    call BlinkXP("c16s003_155" , "d") from _call_BlinkXP_1682
    eva "Una bala va en línea recta. Realmente no, pero para el ejemplo piensa que sí. Tienes que saber dónde está tu objetivo, pero también que pasa más allá de él."
    eva "No quieres que, si fallas o la bala atraviesa el objetivo, haya una niña pequeña detrás a la que puedas matar, ¿verdad? O a [dap]. O a mí."
    mc "Tienes razón, no se me habría ocurrido nunca. Sigue, por favor."
    scene c16s003_145An with dissolve #abcdef paseándose
    eva "Cuatro. Nunca bebas alcohol o consumas drogas antes de disparar o mientras lo haces."
    mc "Esa tiene lógica."
    eva "Cinco. Manipula cualquier arma como si estuviera cargada."
    mc "También es lógica."
    call BlinkXP("c16s003_160" , "d") from _call_BlinkXP_1683
    eva "Ahora llegan las específicas para ti."
    mc "¿Algo sobre cómo disparar desde la terraza o algo así?"
    eva "Seis: Siempre sé puntual cuando quedes con alguien. Especialmente si lo has pedido tú."
    eva "Y más especialmente todavía cuando ese alguien esté armado."
    mc "Eva, lo siento..."
    call BlinkXP("c16s003_165a" , "d") from _call_BlinkXP_1684
    eva "¡Hush!"
    eva "Siete: Cuando te esté instruyendo puedes hacer preguntas, pero te puedes ahorrar los comentarios obvios."
    scene c16s003_170An with dissolve #abac repeat
    eva "Ini bini firmi di ivitir iccidintis..."
    call BlinkXP("c16s003_165b" , "d") from _call_BlinkXP_1685
    eva "Eso sobra. Claro que es por eso. Por eso te estoy enseñando. Pero no puedes estar callado un segundo."
    mc "Lo siento, Eva. No quería interrumpirte. Tan solo quería saber la lógica detrás de cada ley."
    call BlinkXP("c16s003_175" , "d") from _call_BlinkXP_1686
    eva "Vale. Si tienes dudas, pregunta. No hagas comentarios."
    mc "¡A sus órdenes! *Risa*"
    call BlinkXP("c16s003_180" , "d") from _call_BlinkXP_1687
    eva "*Risa* ¡Y déjate de payasadas! No soy tu superior en rango."
    eva "Vamos a por las armas. Hoy dispararás con pistola y con balas de práctica. Tienen menos potencia y no expulsa el casquillo automáticamente."
    eva "Depende de como te vaya, el próximo día puede que te permita disparar con balas de verdad."
    mc "¡Vamos!"
    scene c16s003_185a with dissolve
    eva "Esto es una pistola y..."
    "Eva empieza a darte explicaciones sobre como cogerla, el seguro, la introducción del cargador, y un montón de cosas más."
    "Siempre con la recámara vacía y el cargador extraído. Eva pone mucho énfasis en la seguridad y te va repitiendo las leyes hasta que puedes recitarlas de memoria."
    call BlinkXP("c16s003_190" , "d") from _call_BlinkXP_1688
    eva "Vale, eso es lo más básico. Otro día te enseñaré a desmontar y limpiar tu arma. Vamos a lo divertido. Casi estás listo para tu primer disparo."
    mc "Eso, desde luego, suena más divertido que la teoría."
    eva "Ponte en posición para disparar. Coge el arma con las dos manos y apunta a una lata. Dedo fuera del gatillo."
    scene c16s003_185b with dissolve
    "Te pones en tu mejor imitación de las poses que usan los actores en las películas."
    "Pies separados y las rodillas un poco flexionadas. Lo has visto tantas veces en las películas que casi parece una postura natural."
    call BlinkXP("c16s003_195" , "d") from _call_BlinkXP_1689
    eva "Casi bien. Para un civil. Énfasis en casi. En esa postura no le darás ni a un elefante. No es que el elefante tenga la culpa, claro."
    mc "¿Qué estoy haciendo mal?"
    scene c16s003_185An with vpunch #c- empuja el arma. d- pies en el suelo. e- punteras levantadas. f-paso atrás
    eva "Esto. Los pies."
    "Eva da un golpe seco en el cañón del arma descargada que te desequilibra."
    call BlinkXP("c16s003_200" , "d") from _call_BlinkXP_1690
    eva "Tal como tienes los pies, paralelos al arma y entre sí, el retroceso hará que pierdas el equilibrio."
    eva "Solo ha sido un pequeño empujón, menor que el que te dará la munición de práctica. El arma te dará una pequeña coz cuando uses munición de verdad."
    eva "Y esta es solo una 9mm. Si disparas con una .45 será peor. Te caerías de culo encima de esa roca."
    eva "Vuelve a ponerte en la misma posición."
    scene c16s003_205a with dissolve
    eva "¿Ves? Este pie lo tienes bien. Apuntando al objetivo."
    scene c16s003_205b with dissolve
    eva "Este muévelo un poco hacia atrás y gíralo. 45 o 60° respecto al otro, lo que te sea más cómodo."
    scene c16s003_205c with dissolve
    eva "Así mucho mejor. Ahora que sabes la teoría busca una posición cómoda para ti."
    scene c16s003_210An with vpunch #185c. 210a pies en el suelo.
    eva "¿Ves? Mucho más firme y equilibrado."
    mc "Sí, tienes razón. Pero he visto en muchas películas que se ponen así."
    call BlinkXP("c16s003_215" , "d") from _call_BlinkXP_1691
    eva "Nunca te fíes de lo que ves en las películas. Y menos aún en lo referido a las armas."
    eva "Yo crecí pensando que todo el mundo tenía armas y vivía en casas enormes en Estados Unidos. Y que las calles estarían llenas de Brad Pits y Charlize Terons."
    mc "Y la realidad te debió decepcionar un poco. Por cierto, Charlize es sudafricana."
    call BlinkXP("c16s003_220" , "d") from _call_BlinkXP_1692
    eva "Lo sé, pero no lo sabía entonces. Hasta que no estudiamos acentos y dialectos no lo supe."
    mc "¿Acentos y dialectos?"
    call BlinkXP("c16s003_225" , "d") from _call_BlinkXP_1693
    eva "Soy capaz de hablar 17 idiomas, y usar localismos en varios de ellos. Mientras tu jugabas a la Play, nuestros juegos eran hablar en Árabe, con acento de Libia o de Yemen."
    mc "Tiene que haber sido difícil."
    call BlinkXP("c16s003_230" , "d") from _call_BlinkXP_1694
    eva "No lo era. No conocíamos nada más, para nosotras era normal. Lo echábamos de menos tanto como echas tú de menos ser Spiderman."
    eva "Lo que veíamos en la TV no existía. Era ciencia ficción para nosotras. Las niñas no disparaban y no morían en la TV."
    call BlinkXP("c16s003_235" , "h") from _call_BlinkXP_1695
    eva "Pero dejemos de hablar de nosotras. Carga el arma y mete una bala en la recámara."
    eva "Dedo lejos del gatillo. Sin apuntar en mi dirección o en la de tus pies."
    mc "¡A sus órdenes!"
    call BlinkXP("c16s003_240" , "d") from _call_BlinkXP_1696
    eva "Ahora apunta con una mano y dispara a la lata que menos te guste."
    eva "Recuerda. Vas a disparar con munición de práctica. No expulsa el casquillo y no recarga automáticamente. Tienes que amartillarla manualmente."
    mc "Será mejor que te apartes, ¿no?"
    eva "No te preocupes. No me puedes dar aquí. Mi instructor se pondría detrás tuyo, con su arma apuntando a tu cabeza, pero yo prefiero estar aquí. Dispara tres veces."
    scene c16s003_245An1 with dissolve #a-b-c
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "No tienes ni idea de dónde va el primer disparo. La pequeña coz de la que ha hablado Eva es más fuerte de lo que esperabas y el retroceso ha hecho que el cañón se levante."
    eva "Ningún pato muerto de momento. Las latas están mucho más abajo. *Risa* Otra vez."
    eva "Por cierto, pareces salido del Doomfenstein cogiendo la pistola así. *Risa*"
    scene c16s003_245p with dissolve
    mcp "(No me importaría disparar a Eric en un videojuego.)"
    scene c16s003_245An2 with dissolve #a-d-c
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Esta vez el retroceso no te sorprende y eres capaz de controlarlo. Esta vez sí que ves donde impacta la bala. En el árbol que hay detras del bote al que apuntabas."
    eva "Nos vamos acercando. Si el bote devolviera el fuego, ya estarías muerto. Porque estás apuntando al bote, ¿verdad? *Risa* Al menos no has matado ninguna ardilla."
    scene c16s003_245An3 with dissolve # a-e-c
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Intentas compensar más todavía el retroceso. Esta vez levantas un poco de polvo delante de la lata. Lo has compensado en exceso, pero la dirección era buena."
    eva "¡Ese ha sido casi bueno! Hay un topo teniendo un ataque de ansiedad ahora mismo. *Risa* Pero ha sido el mejor disparo."
    call BlinkXP("c16s003_250" , "d") from _call_BlinkXP_1697
    eva "Saca la bala de la recámara, ponle el seguro, saca el cargador, y dame el arma."
    mc "Es más difícil de lo que parece. En las películas lo pillan en seguida."
    eva "¿Qué te he dicho sobre Spiderman hace un rato? No te creas nada de lo que veas en una película."
    eva "Si esto fuera una película habrías acertado a la primera y estaríamos follando contra un árbol."
    mc "*Risa* Antes me vas a tener que invitar a cenar. *Risa*"
    scene c16s003_255a with dissolve #pistola
    eva "Tú crees que eres gracioso, ¿verdad? No hace falta que contestes."
    eva "Tu problema es que tiras del gatillo."
    mc "Eso es lo que hay que hacer, ¿no? Si no, no dispara."
    eva "No, si tiras del gatillo estás desequilibrando el arma. Hacia abajo, como ahora. Eso si eres capaz de controlar el retroceso, que lo estás empezando a hacer bien."
    eva "Lo que tienes que hacer es estrujar con toda la mano. Empuñadura y gatillo. Como si fuera una pelota antiestrés. ¿Ves?"
    mc "Vale, lo veo. Déjame probar otra vez"
    scene c16s003_245An3 with dissolve #a-e-c
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "La teoría de estrujar empuñadura y gatillo a la vez es fácil. La práctica no."
    eva "Casi. El topo acaba de reservar unas vacaciones en Florida. *Risa* Prefiere los caimanes. Controla un poco más como estrujas el conjunto y casi lo tendrás."
    scene c16s003_245An4 with dissolve #a-f-g
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "Esta vez sí que impactas en el bote. La sensación de alegría es inmensa."
    mc "¡Sí!"
    eva "¡Muy bien, [mc]! Un último disparo para comprobar que no ha sido casualidad."
    scene c16s003_245An5 with dissolve #h-i-j
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "La lata salta por los aires. ¡Estás aprendiendo a disparar!"
    eva "¡Genial!"
    eva "Te quedan 11 balas y cuatro objetivos. A ver cuántos puedes derribar."
    scene c16s003_245m with vpunch
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang* *Bang* *Bang*"
    "Disparas tres veces a la botella de gel de manos. No hay suerte. Dirías que le has dado, pero no ha saltado por los aires. Ocho balas. Cuatro objetivos todavía."
    eva "Esa botella no quiere morir. *Risa*"
    scene c16s003_245k with vpunch
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang* *Bang*"
    "La siguiente lata salta volando al segundo disparo. Seis balas. Tres objetivos."
    eva "¡Muy bien!"
    scene c16s003_245l with vpunch
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang*"
    "La siguiente al primero. Cinco balas. Dos objetivos."
    eva "¡Alucinante!"
    "Cambias de objetivo."
    scene c16s003_245n with vpunch
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang* *Bang* *Bang*"
    "Te cuesta tres balas acabar con la siguiente lata. Últimas dos balas. Solo queda la botella de gel de manos." #hand sanitizer
    eva "Esa se ha resistido, pero bien. A por la última."
    scene c16s003_245m2 with vpunch
    play sound ("music/Desert-Eagle-Gunshot.ogg")
    "*Bang* *Bang*"
    "Vuelves a la botella. Disparas. Volverías a jurar que le has dado, pero la botella sigue ahí. No has fallado porque sea transparente, ¿verdad?"
    call BlinkXP("c16s003_260" , "d") from _call_BlinkXP_1698
    eva "Muy bien, [mc]."
    mc "Muy bien no. La botella se ha resistido."
    eva "¿Estás seguro? Ve a verla."
    scene c16s003_245o with fade
    mc "¿Has clavado la botella al suelo? *Risa*"
    call BlinkXP("c16s003_265" , "d") from _call_BlinkXP_1699
    eva "*Risa* ¡Sí! Ha sido divertido ver cómo te frustrabas. Se me saltan las lágrimas."
    mc "Muy graciosa... *Risa*"
    mc "Pero no sé cuántas veces le he dado. No sé ni cuántas le he disparado..."
    call BlinkXP("c16s003_270" , "d") from _call_BlinkXP_1700
    eva "Le has disparado cinco veces y le has dado dos. No está nada mal para tu primera vez. 17 balas y siete aciertos."
    eva "Mi primera vez fue bastante peor. Y fui la mejor de todas."
    call BlinkXP("c16s003_275" , "d") from _call_BlinkXP_1701
    stop music fadeout (1.5)
    eva "Sí, lo sé Amanda, conseguí la misma puntuación que tú, pero más dieces."
    play music ("music/Majestica.ogg")
    mc "¿Qué edad tenías?"
    call BlinkXP("c16s003_280" , "d") from _call_BlinkXP_1702
    eva "6 años. Aquellas pistolas fueron nuestro regalo de cumpleaños."
    mc "Eso es muy triste. ¿Ni una muñeca? ¿Ni un juguete?"
    call BlinkXP("c16s003_285" , "d") from _call_BlinkXP_1703
    eva "Es tan triste como que a ti nunca te regalaran un sable laser que funcionara."
    mc "No existen, Eva."
    call BlinkXP("c16s003_290" , "d") from _call_BlinkXP_1704
    eva "Igual que en nuestro mundo no existían juguetes o muñecas."
    eva "Nuestros juguetes eran armas y dispositivos de vigilancia. Era lo normal. Y espiarnos entre nosotras era divertido."
    eva "Con el tiempo, los A nos empezaron a traer cosas de sus misiones. Bolas de nieve y cosas así."
    eva "Era casi como sentirse en una película. Eran casi como nuestros tíos favoritos."
    mc "Joder, Eva. ¿Puedo abrazarte?"
    call BlinkXP("c16s003_295" , "h") from _call_BlinkXP_1705
    eva "{b}¿Qué? ¿A mí? ¿Por qué?{/b}"
    mc "*Risa* Costumbre familiar. Cuando alguien explica algo triste, nos abrazamos. Nos consolamos."
    call BlinkXP("c16s003_300" , "h") from _call_BlinkXP_1706
    eva "¿Te ha puesto triste?"
    mc "Me pone triste que no hayas tenido una infancia normal."
    eva "No tienes que ponerte triste por eso. Para mí... para nosotras, era normal. No echábamos nada de menos."
    mc "¿Estás intentando consolarme? ¿Tú a mí?"
    call BlinkXP("c16s003_305" , "d") from _call_BlinkXP_1707
    eva "En eso consiste, ¿no? Has dicho que cuando algo os pone tristes, os consoláis. ¿O lo he entendido mal?"
    mc "No, lo has entendido perfectamente."
    call BlinkXP("c16s003_300b" , "d") from _call_BlinkXP_1708
    "Vuelves a abrazarla. Ya no sabes si para consolarla a ella o a ti mismo. Ella parece no necesitar consuelo, pero ayer demostró que necesita cariño."
    mcp "(¡Qué difícil va a ser esto! Ni siquiera entiende lo triste que es su situación.)"
    eva "Si este es el premio por ponerte triste, tengo un montón de historias para contar."
    mc "Las quiero oír todas, Eva."
    mc "Y en casa también querrán hacerlo. Prepárate para muchos abrazos."
    call BlinkXP("c16s003_310" , "d") from _call_BlinkXP_1709
    eva "¡Oh, mierda! ¿Qué hora es? ¿A qué hora me esperan para comer?"
    mc "A la una y media. No sé qué hora es. Tengo el móvil en la mochila."
    call BlinkXP("c16s003_315" , "d") from _call_BlinkXP_1710
    eva "Por eso llegas tarde a los sitios. *Risa* Vamos a recoger las latas y empecemos a bajar. A mí no me gusta llegar tarde."
    mc "¿Cuánto tiempo me lo vas a echar en cara?"
    eva "Hasta que llegues puntual. *Risita*"
    stop music fadeout (1.5)
    scene black with dissolve
    "Recogéis el campo de tiro. Eva hace hincapié en no dejaros ningún casquillo. Las balas son irrecuperables en su mayoría."
    "Se hace una cola y empezáis a bajar hacia casa. Ella es mucho más rápida y ágil que tú. También tiene más prisa. Ni una gota de sudor perla su frente."
    call BlinkXP("c16s003_320" , "d") from _call_BlinkXP_1711
    play music ("music/Rise-Up.ogg")
    eva "Venga, tortuguilla. Vamos a llegar tarde por tu culpa."
    mc "Hay tiempo de sobra, Eva."
    eva "No tanto. Me tengo que cambiar de ropa. No quiero que la primera impresión que tenga la familia de mí sea vestida así."
    mc "¿Por eso te has hecho la coleta?"
    call BlinkXP("c16s003_320b" , "d") from _call_BlinkXP_1712
    eva "Tengo más pinta de buena chica con ella, ¿no? *Risita*"
    mc "Eva, la primera impresión que se van a llevar es que eres una buena chica. Porque lo eres."
    mc "Ahora vas a decirme que llevas un vestido en la mochila."
    call BlinkXP("c16s003_325" , "d") from _call_BlinkXP_1713
    eva "¿Un vestido? ¿Qué tiene de malo un vestido? ¿No sería apropiado?"
    mc "Puedes ponerte lo que quieras, pero apuesto a que [dap] y [emm] van a ir con shorts. Ya las habéis visto. Ante todo, quieren estar cómodas en casa."
    eva "¿Shorts? Perfecto. También llevo."
    mcp "(¿Está tan nerviosa que se ha traído todo su guardarropa?)"
    mc "El vestido iría mejor para una cena. O para la comida del domingo."
    scene c16s003_330a with dissolve
    eva "El domingo también me toca ir a comer a mí, ¿no?"
    mc "Claro. Hoy y el domingo vienes a comer. Mañana a cenar."
    call BlinkXP("c16s003_335" , "d") from _call_BlinkXP_1714
    eva "Lo digo porque vais a celebrar el cumpleaños de las chicas. A lo mejor queréis que sea algo familiar."
    mc "Será familiar. Te lo dije en la playa. De alguna forma formáis parte de esta familia. Hoy lo terminarás de descubrir."
    mc "Amanda. El domingo ven tú también a comer. Y antes de que preguntes quién va a vigilar, la respuesta es vosotras mientas coméis."
    call BlinkXP("c16s003_340" , "d") from _call_BlinkXP_1715
    eva "Dice que OK."
    eva "Sois raros. Celebráis los tres cumpleaños juntos. Hoy es el de [emm], el lunes el de [dap] y [eri]... y lo celebráis el domingo... raros."
    if persistent.family:
        mc "Se llevan tres días de diferencia."
    else:
        mc "Se llevan tres días de diferencia. Al menos por lo que sabemos."
    mc "Celebrar el cumpleaños de [emm] y tres días después los otros dos hubiera sido agotador. [nor] y [mar] las educaron para que la celebración fuera el domingo más cercano."
    call BlinkXP("c16s003_345" , "d") from _call_BlinkXP_1716
    eva "No parece algo que [emm] aceptara de buen grado."
    mc "Para cuando fue consciente de su cumpleaños estaba acostumbrada a hacerlo así. Nunca supuso un problema. Hoy recibe los besos y abrazos. El domingo los regalos."
    call BlinkXP("c16s003_350" , "d") from _call_BlinkXP_1717
    eva "¿Ves, Amanda? Te lo dije. No hacía falta que trajéramos nada hoy."
    mc "Bueno, vosotras vais a ser un regalo especial para ella. Seguro. También para [dap] y [eri]."
    mc "Hablando de [eri]... tenemos una conversación pendiente sobre el día que te disfrazaste."
    call BlinkXP("c16s003_355" , "d") from _call_BlinkXP_1718
    eva "Amanda, corto la comunicación."
    eva "¿Qué quieres saber?"
    mc "¿Por qué lo hiciste? ¿Qué querías?"
    call BlinkXP("c16s003_360" , "d") from _call_BlinkXP_1719
    eva "Ahora te va a parecer ridículo. A mí también me lo parece. Anoche le estuve dando vueltas. Sabía que querrías tener esta conversación."
    mc "Prueba a explicármelo y después decidimos si es ridículo."
    eva "Piensa que no entraba en nuestros planes que llegáramos a conocerte nunca."
    eva "Me quedé atrapada en la habitación de [sai] mientras ponía las cámaras. Me empecé a disfrazar de [eri] para matar el rato mientras os dormíais todos."
    eva "Mi disfraz de [eri] estaba allí, era una habitación que no se iba a usar durante un tiempo. Y se me ocurrió una idea."
    mc "Me das miedo."
    call BlinkXP("c16s003_365" , "d") from _call_BlinkXP_1720
    eva "Mira... estás bueno, ¿vale?"
    mc "Ermmm... gracias, supongo..."
    call BlinkXP("c16s003_370" , "d") from _call_BlinkXP_1721
    if eri._var("route"):
        eva "Después de lo de la sauna, tarde o temprano ibas a tener sexo con [eri], y parecía que necesitabas un empujón con todo eso de \"cuando estés lista\"."
        eva "Y pensé... ¿por qué no catarlo yo antes y a la vez darte ese empujón? Ya lo sé, estúpido y ridículo."
        mc "Aparte de todo lo que hay de malo en ese plan, no se te ocurrió pensar que, cuando tuviéramos sexo por primera vez, yo me sorprendería de que siguiera siendo virgen, ¿verdad?"
    else:
        eva "Después de lo de la sauna, creí que necesitabas un empujón en la dirección de [eri]."
        eva "A la chica le gustas mucho."
        eva "Y pensé... que si podía llevarme una alegría mientras ayudaba un poco a [eri], ¿por qué no? Ya lo sé, estúpido y ridículo."
        mc "Aparte de todo lo que hay de malo en ese plan, no se te ocurrió que, si hubiera funcionado, yo me hubiera sorprendido de que siguiera siendo virgen, ¿verdad?"
    mc "Podrías haber arruinado nuestra relación con ese plan tuyo. Nuestra primera vez juntos no hubiera significado lo mismo."
    call BlinkXP("c16s003_375" , "d") from _call_BlinkXP_1722
    eva "Ya te he dicho que fue estúpido. Parece uno de los planes de [emm]. A veces me parezco más a [emm] que a [dap] o a [eri]."
    eva "Espero que no me odies por ello. Me arrepiento mucho de haberlo intentado."
    mc "No, Eva. Ayer me sentí estúpido cuando até cabos. Pero no te odio."
    mc "Es algo que yo no hubiera hecho nunca... Y sí. Es ridículo. Quiero que me prometas que no se volverá a repetir."
    call BlinkXP("c16s003_380" , "d") from _call_BlinkXP_1723
    eva "Ahora no tiene sentido que se repita. Ahora me caes bien y no creo que tu relación con [eri] vaya a cambiar mucho. O con [dap]."
    mc "¿Ahora te caigo bien? ¿Antes no?"
    call BlinkXP("c16s003_385" , "d") from _call_BlinkXP_1724
    eva "¡Oops! ¿Ves como me parezco a [emm]? No sé tener la boca cerrada."
    eva "La verdad es que con lo que veía cuando llegaste... me parecías un poco manipulador."
    call BlinkXP("c16s003_390" , "d") from _call_BlinkXP_1725
    eva "Tienes que entenderlo. Llevábamos dos meses vigilando a tu familia. Son bastante adorables y nos salió el instinto protector."
    eva "Llegas tú y todo empezó a cambiar. Empiezaron a haber secretos y... No, no me caías bien... pero estabas bueno."
    mc "Puedo entenderlo. Y me alegra que no se vaya a repetir. Y de que tengas ese instinto hacia las chicas."
    mc "Bueno, estamos a cinco minutos de casa. ¿Quieres pasar por mi casa a cambiarte de ropa? La comida será en casa de [nor]."
    call BlinkXP("c16s003_395" , "d") from _call_BlinkXP_1726
    eva "No hace falta. Puedo cambiarme aquí mismo. Ya me has visto en bragas..."
    mc "Voy a girarme para darte un poco de privacidad."
    eva "Como quieras."
    scene c16s003_400a with dissolve
    mc "Avísame cuando acabes."
    eva "¿Top rosa o blanco? Rosa es el color de [emm] y blanco el de [dap]. No quiero mostrar preferencias."
    mc "No creo que tomen los colores que vistes como una preferencia."
    eva "¡Qué poco conoces a tu propia familia! *Risa*"
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
    menu:
        "Echar un vistazo." (wt = wt1):
            if not itchio:
                scene c16s003_405d with dissolve:
                    yalign 1.0
                    linear 5.0 yalign 0.0
                pause (5.0)
            else:
                scene itchio
                mcp "(¿Otra vez este gato?)"
            call BlinkXP("c16s003_405" , "d") from _call_BlinkXP_1727
            eva "Sabía que no podrías resistirte a mirar. *Risa*"
            mc "¡Lo siento, Eva!"
            eva "Ya te he dicho que no hacía falta que te giraras. No ibas a ver nada que no hayas visto."
            eva "Y toda mi vida me he cambiado delante de otros hombres. Solo éramos seis chicas en la base. No había vestuarios exclusivos para nosotras."
            mc "Voy a volver a girarme mientras acabas de cambiarte."
            scene c16s003_400a with dissolve
        "Le he prometido privacidad." (wt = wt1):
            pass
    $ resetWalkthrough ()
    "Un minuto después..."
    eva "Ya estoy. Ya podemos irnos."
    scene c16s003_410d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP("c16s003_410" , "d") from _call_BlinkXP_1728
    mc "¡Wow! Estás preciosa."
    eva "Gr-gracias... supongo..."
    eva "¿N-nos podemos ir? N-no quiero llegar tarde."
    mcp "(No hace falta preguntarle si está nerviosa. Salta a la vista. La chica dura capaz de disparar a alguien en la cocina de [nor] está histérica por conocer a la familia.)"
    mc "Vamos, sígueme."
    return
label c16s003_LunchWithEva:
    if _in_replay:
        call mrS3_dap_route from _call_mrS3_dap_route_31
        call mrS3_sca_route from _call_mrS3_sca_route_24
        call mrS3_mar_route from _call_mrS3_mar_route_35
        call mrS3_nor_route from _call_mrS3_nor_route_27
        call mrS3_emm_route from _call_mrS3_emm_route_38
        call mrS3_eri_route from _call_mrS3_eri_route_30
        menu:
            "¿Tienes Puntos de Relación positivos con Kate?"
            "Si":
                $ kat._var("relationshipPoints", 5, intention = "set")
            "No":
                $ kat._var("relationshipPoints", -5, intention = "set")
        call mrS3_edmund_story from _call_mrS3_edmund_story_10
    call BlinkXP("c16s003_430" , "f") from _call_BlinkXP_1731
    mc "¿Preparada para un montón de abrazos?"
    eva "No me asustes... creo que en estos últimos dos días he dado y recibido más abrazos que en los últimos dos años."
    mc "Pues ve haciéndote a la idea de que no ha sido nada comparado con lo que te espera."
    call BlinkXP("c16s003_435" , "d") from _call_BlinkXP_1732
    eva "No me vas a dejar sola con... ellas, ¿verdad?"
    mc "Creo que sí. Todo el mundo va a querer conocerte, hablar contigo. Van a decir que yo te he tenido para mí solo durante una hora y media y que quieren su ración de Eva."
    call BlinkXP("c16s003_440" , "d") from _call_BlinkXP_1733
    eva "Tal como lo has dicho, parece que me vayan a descuartizar. *Risita*"
    mc "No era mi intención que sonara así, pero si te ha sacado una sonrisa, ha valido la pena."
    eva "No te vayas muy lejos. No tengo ningún plan de extracción excepto tú. *Risa*"
    mc "Vamos dentro, creo que llegamos unos minutos antes de la hora."
    scene c16s003_445a with fade
    mc "Ven, Eva, te voy a presentar a parte de la familia."
    eva "*Susurrando* ¡Joder! Parecen un pelotón de fusilamiento."
    scene c16s003_445b with dissolve
    mc "Ya conoces a [mar] y a [nor]."
    scene c16s003_445c with dissolve
    nor "Bienvenida a casa de nuevo, Eva." (multiple=2)
    mom "Me alegra volver a verte." (multiple=2)
    eva "Gracias, estoy ansiosa de conocer a todo el mundo... en persona."
    call BlinkXP("c16s003_450" , "d") from _call_BlinkXP_1734
    mc "[eri]."
    scene c16s003_455a with dissolve
    eri "Encantada de conocerte, Eva. Bienvenida a la familia."
    eva "Ermmm... gracias... igualmente..."
    call BlinkXP("c16s003_465a" , "d") from _call_BlinkXP_1735
    mc "[emm]."
    emm "..."
    mc "[emm]..."
    call BlinkXP("c16s003_465b" , "d") from _call_BlinkXP_1736
    emm "*Susurrando* Tú y yo tenemos que hablar..."
    scene c16s003_455c with hpunch
    if persistent.family:
        emm "Bienvenida a la familia, Eva, conocerte es uno de los mejores regalos de cumpleaños que podía recibir hoy, aunque mi hermano te haya tenido escondida."
    else:
        emm "Bienvenida a la familia, Eva, conocerte es uno de los mejores regalos de cumpleaños que podía recibir hoy, aunque mi {b}\"hermano\"{/b} te haya tenido escondida."
    eva "Gracias, [emm]. Me alegra mucho conocerte. Mi... hermana... dice que nos parecemos mucho."
    if not persistent.family:
        eva "*Susurrando* Y [mc] es tu hermano quieras o no quieras. No sabes la suerte que tienes..."
    mc "No la he tenido escondida, [emm]. Su trabajo..."
    call BlinkXP("c16s003_470" , "h") from _call_BlinkXP_1737
    emm "¡Hush! ¡Estoy hablando con Eva!"
    eva "[emm]..."
    call BlinkXP("c16s003_460" , "d") from _call_BlinkXP_1738
    mc "[dap]."
    scene c16s003_455b with dissolve
    dap "Bienvenida a casa. Tenemos que hablar de mil cosas. Quiero saberlo todo de ti."
    eva "Gracias, [dap]... no hay mucho que explicar... pero gracias..."
    call BlinkXP("c16s003_485" , "d") from _call_BlinkXP_1739
    mc "[sca]."
    sca "No soy oficialmente de la familia, pero... ¿puedo?"
    mc "*Risa* No vas a ser la primera en no abrazarla, ¿verdad?"
    eva "*Susurrando* Capullo."
    scene c16s003_455d with dissolve
    sca "Bienvenida a casa. Espero que les des la oportunidad de mostrarte lo maravillosos que son."
    eva "Me hago una idea. *Susurrando* ¿Cómo estás tú?"
    sca "Genial, gracias a vosotras dos, a [mc], y a esta familia."
    call BlinkXP("c16s003_475" , "d") from _call_BlinkXP_1740
    mc "Tía Betty."
    bet "¿Puedo abrazarte también?"
    mc "Estoy seguro que lo agradecerá, Tía Betty."
    eva "*Susurrando* Sabes que me las vas a pagar, ¿verdad?"
    scene c16s003_455e with dissolve
    bet "Encantada de conocerte, cariño. Por lo que he oído de ti vamos a ser buenas amigas."
    eva "Pero yo sigo una dieta equilibrada..."
    call BlinkXP("c16s003_480a" , "h") from _call_BlinkXP_1741
    eva "¡Oops! Eso no ha sido muy educado, ¿verdad?"
    bet "No pasa nada, cariño. Me invitas a cenar una pizza y todo queda perdonado. *Risa* Tú puedes comer una ensalada, si quieres."
    call BlinkXP("c16s003_480b" , "d") from _call_BlinkXP_1742
    eva "Ningún problema, tienes que cuidar ese brazo de batear. *Risita*"
    eva "*Susurrando* Y me encanta que me lleven a cenar, aunque tenga que pagar yo."
    call BlinkXP("c16s003_480c" , "d") from _call_BlinkXP_1743
    mc "Y por último, Olivia, mi Meemaw."
    mee "Yo no voy a pedir permiso para abrazarte, lo siento."
    if persistent.family:
        mee "Llevas mis genes, con lo que eres mi nieta de alguna forma."
    scene c16s003_455f with dissolve
    mee "Además, no tuve la oportunidad de darte las gracias por todo lo que hicisteis durante el secuestro."
    eva "Era trabajo, pero fue un placer. Cuando unes trabajo y placer..."
    mc "Bueno, creo que ya está, ¿no?"
    scene c16s003_455g with dissolve
    nor "A mí me ha sabido a poco ese abrazo triple, ¿a tí no?"
    mom "Sí, pero ¿no crees que ya ha tenido suficientes abrazos por ahora?"
    call BlinkXP("c16s003_455h" , "h") from _call_BlinkXP_1744
    nor "¡Nunca!"
    eva "Gracias por esta recepción, [nor]."
    nor "Es un placer tenerte en casa otra vez."
    call BlinkXP("c16s003_455i" , "d") from _call_BlinkXP_1745
    mom "No dejes que te agobiemos demasiado con los abrazos."
    eva "No te preocupes, [mar]. Creo que acabaré acostumbrándome."
    scene c16s003_455j with dissolve
    nor "Hemos preparado una comida de pie. Todas querían sentarse a tu lado y acapararte."
    nor "¿Te va bien así? Si quieres puedes coger un taburete si estás cansada, o sentarte a la mesa..."
    eva "No te preocupes, [nor], de verdad. Estaré bien de pie."
    call BlinkXP("c16s003_495a" , "d") from _call_BlinkXP_1746
    mom "Le va a explotar la cabeza a la pobre chica. ¿Cómo ha ido?"
    mc "Muy bien. Me ha enseñado a disparar... un poco. Y hemos estado charlando. Ya te contaré. Ha tenido una infancia... diferente."
    call BlinkXP("c16s003_495b" , "d") from _call_BlinkXP_1747
    mom "¿Por qué no te vas a cambiar? No vas a comer con la ropa de correr, ¿verdad?"
    mc "¿Quieres que la deje sola con vosotras? Piensa que yo tengo que subir más días al lago con ella y su venganza puede ser cruél. *Risa*"
    call BlinkXP("c16s003_500" , "d") from _call_BlinkXP_1748
    mom "No somos tan malas. *Risa* Abrumadoras sí, pero malas no. Además, apestas un poco."
    mc "Vale, voy a darme una ducha rápida y ahora vuelvo. *Risa*"
    if mar._var("route"):
        call BlinkXP("c16s003_500b" , "d") from _call_BlinkXP_1749
        mom "*Susurrando* Por cierto, he dejado mi... *Susurrando más aún* prueba de embarazo... en tu habitación, en el armario grande. Ahí estará más segura."
        if nor._var("route"):
            mom "*Susurrando* [nor] me ha dicho que [dap] casi la encuentra esta mañana mientras buscaba un top que ponerse. ¡Como que [dap] iba a llenar un top de [nor]!"
        else:
            mom "*Susurrando* [emm] casi la encuentra esta mañana mientras buscaba algo que ponerse en mi armario."
        mc "*Susurrando* Perfecto, [mar.mc!t]. En mi armario nadie va a buscar nada. Cuando llegue la hora sube y lo comprobamos."
        mc "Voy a darme esa ducha antes de que me dejen sin comida. *Risa* Voy a decírselo a Eva."
    scene c16s003_455k with dissolve
    mc "Eva, ¿puedo hablar un momento contigo?"
    emm "¡No puedes llevártela ahora! ¡Acaba de llegar!"
    eri "Ha dicho que es un momento, [emm]."
    dap "Nos la devuelves en seguida, ¿verdad?"
    eva "Ahora vuelvo, chicas. No voy a dejar que me secuestre. *Risita*"
    call BlinkXP("c16s003_505" , "d") from _call_BlinkXP_1750
    eva "Dime."
    mc "¿Cómo lo llevas? ¿Te estamos agobiando mucho?"
    eva "Más que agobiando, abrumando un poco. Pero todo está bien. Raro, pero bien."
    mc "Voy a dejarte un momento en sus manos. Me acaban de decir que apesto un poco y voy a darme una ducha y a cambiarme."
    call BlinkXP("c16s003_510" , "d") from _call_BlinkXP_1751
    eva "¿No vas a quedarte a comer?"
    mc "Sí, va a ser una ducha rápida y vuelvo en un momento. ¿Estarás bien?"
    call BlinkXP("c16s003_515" , "d") from _call_BlinkXP_1752
    eva "C-creo que sí... creo que estaba más preocupada de lo necesario."
    mc "Si necesitas algún plan de extracción, habla con [mar] o [nor]. Ellas te ayudarán."
    call BlinkXP("c16s003_520a" , "h") from _call_BlinkXP_1753
    eva "¡Gracias!"
    mc "¡Hey! ¿A qué viene ese abrazo?"
    call BlinkXP("c16s003_520b" , "d") from _call_BlinkXP_1754
    eva "Costumbres familiares, dijiste. Me pone triste haber sido tan tonta. Haberte prejuzgado..."
    eva "No eres manipulador, solo un idiota que no sabe que no debe preocuparse tanto por las chicas de la familia. Sabemos... saben cuidarse solas."
    mc "¿Acabas de decir \"sabemos\"? *Risa*"
    call BlinkXP("c16s003_525" , "d") from _call_BlinkXP_1755
    eva "¡Joder! Hacéis muy difícil no sentirse aceptada. Me han dicho \"bienvenida a la familia\" quince veces en cinco minutos."
    mc "Ya te lo dije. Ahora solo hace falta que te lo termines de creer."
    call BlinkXP("c16s003_530" , "d") from _call_BlinkXP_1756
    "Eva te abraza un poco más fuerte durante un segundo, apoyando su cabeza contra tu cuello."
    eva "Bueno, vete ya. Al final tu peste se me va a pegar a la ropa."
    mc "Bonita forma de decir que prefieres estar con las chicas a estar conmigo. *Risa*"
    mc "Vuelvo en un rato. No dejes que te agobien demasiado."
    scene c16s003_535a with fade
    mc "Hola, [sai]. Hola, Kate. ¿Habéis comido ya?"
    sai "Sí, Lisa y Kim tenían clase esta tarde y hemos comido todas juntas antes de que se fueran."
    kat "Después de tener La Conversación. Por cierto, una oportunidad perdida de llamarla... *Voz profunda* \"La Clonversación\". *Risa*"
    mc "*Risa* No se me había ocurrido"
    mc "¿No vais a ir a la comida con Eva?"
    scene c16s003_535b with dissolve
    kat "[mar] nos ha dicho que fuéramos, pero hemos pensado que era mejor dejaros un rato en familia. Pasaremos luego a conocerla."
    sai "Y tú deberías estar allí, ¿no?"
    mc "Voy a ducharme y a cambiarme."
    call KissXP("c16s003_540" , "d") from _call_KissXP_51
    sai "No te entretenemos más entonces. Por cierto, buenos días."
    mc "Buenos días, [sai]. *Risa*"
    mc "Luego tengo que hablar contigo."
    sai "OK."
    if kat.rps > 0:
        call KissXP("c16s003_545" , "d") from _call_KissXP_52
        kat "Buenos días, [mc]."
        mc "Buenos días, Kate."
    scene c16s003_535c with dissolve
    kat "Vete a duchar antes de que nos aromatizes la planta con Eau de Sobac. *Risa* ¡Apestas!"
    sai "¡Es verdad! *Risa* Yo notaba un olor conocido y no lo localizaba."
    mc "A lo mejor es por la costumbre de Kate de ir descalza. *Risa* Eau de Rochefort."
    mc "Me voy antes de que empecéis a deprimirme. *Risa*"
    scene c16s003_550a with fade
    "Vuelves a la cocina de [nor] después de ducharte y, tal como te imaginabas, Eva es el centro de atención de las chicas. Las mujeres se mantienen apartadas, hablando entre ellas."
    eva "... y entonces Amanda me avisó por radio y..."
    scene c16s003_550b with dissolve
    eva "Ya ha vuelto la mofeta. *Risa*"
    todas "*Risa*"
    mc "Parece que ya te estás integrando en la familia. *Risa* El deporte familiar es reírse de mí."
    emm "Porque te lo mereces. Siempre haces algo para que nos riamos contigo y de ti."
    eri "No como tú, ¿verdad, [emm]? *Risa*"
    dap "Al menos él lo suele hacer a propósito. *Risa*"
    sca "*Risa* Y nadie le suele prohibir ningún color."
    call BlinkXP("c16s003_555" , "d") from _call_BlinkXP_1757
    emm "Ni siquiera en mi cumpleaños me vais a dejar tranquila, ¿verdad?"
    mc "Elige. No nos reímos de ti hoy o el domingo."
    emm "*Gruñido* El domingo. Es el cumpleaños de verdad."
    todas "*Risa*"
    call BlinkXP("c16s003_560" , "d") from _call_BlinkXP_1758
    mom "Ve a comer algo. Es tarde y todo el mundo estaba hambriento. Si [nor] y yo no llegamos a intervenir no te hubieran dejado nada."
    mc "Gracias, [mar.mc!t]."
    mom "Te he dejado un plato con pato, salmon, rollitos, carne con gambas, y falafel al lado del fregadero. No sabíamos que le gustaría a Eva."
    scene c16s003_550c with dissolve
    "Ver esta reunión y cómo Eva se siente más cómoda de lo que nunca hubiera pensado te llena de alegría de alguna forma."
    "Después de lo que ha contado sobre su infancia... sí, como diría ella, te sientes como un idiota con ganas de protegerla."
    scene c16s003_550d with dissolve #plato de comida
    stop music fadeout (1.5)
    "Proteger. A Eva. La protectora. Quizás la tengas que proteger de cosas que ni siquiera sabe que existen. De las amenazas de una vida normal."
    play music ("music/Sad-Cinematic.ogg")
    eri "Es especial, ¿verdad?"
    call BlinkXP("c16s003_565" , "d") from _call_BlinkXP_1759
    mc "¡Oh, [eri]! No te había visto. Estaba inmerso en mis pensamientos."
    mc "Sí, lo es. Ha tenido una vida tan diferente de lo que estamos acostumbrados que llamarla especial es quedarse corto."
    eri "Cuando te has ido parecía un animalillo acorralado. Hasta que mi madre le ha dado un abrazo y..."
    call BlinkXP("c16s003_570" , "d") from _call_BlinkXP_1760
    if persistent.family:
        eri "Hasta cierto punto también es su madre, ¿no?"
    else:
        eri "Mi madre..."
    mc "¿Cómo ha ido La Conversación?"
    call BlinkXP("c16s003_575a" , "d") from _call_BlinkXP_1761
    eri "Aún la estoy asimilando. No sé como sentirme..."
    if persistent.family:
        eri "Saber que tengo una segunda gemela... y que perdí dos por el camino a quien nunca conoceré... es raro... y duro..."
        eri "El mismo día que gano una hermana me entero que he perdido a dos."
        call BlinkXP("c16s003_575b" , "d") from _call_BlinkXP_1762
        eri "Pero he ganado una hermana y ganaré una prima esta noche. No me puedo quejar demasiado... ¿verdad?"
    else:
        eri "Saber que mi madre no es mi madre biológica... que no tengo madre biológica... es raro... y duro..."
        eri "Mi madre siempre será mi madre. No importa que no lleve sus genes... pero es difícil de asimilar."
        call BlinkXP("c16s003_575b" , "d") from _call_BlinkXP_1763
        eri "Pero he ganado una hermana y no pienso perder a mi madre, con lo que, en el fondo, no me puedo quejar demasiado... ¿verdad?"
    mc "¿Un abrazo?"
    eri "Sí, por favor..."
    call BlinkXP("c16s003_580" , "d") from _call_BlinkXP_1764
    "Os abrazáis en silencio durante unos minutos. Conoces lo suficientemente bien a [eri] como para saber que solo necesita el abrazo. No necesita, no quiere, que hables en ese momento."
    call BlinkXP("c16s003_585" , "d") from _call_BlinkXP_1765
    eri "Ya está, gracias..."
    mc "Ya sabes que me encanta abrazarte. No deberías dar las gracias por ello."
    if eri._var("route"):
        call BlinkXP("c16s003_590" , "d") from _call_BlinkXP_1766
        eri "El día que no le de las gracias a mi novio por un abrazo..."
        eri "Hablando de novios... mi madre me ha hablado de las pruebas de embarazo. Me gustaría hacérmela."
        mc "Las tengo en mi habitación. Después de comer si quieres vamos a hacerla, y mañana sabremos el resultado."
        mc "¿Has notado algún síntoma?"
        call BlinkXP("c16s003_595" , "d") from _call_BlinkXP_1767
        eri "No, pero me gustaría saber si mi novio me ha dejado embarazada el mismo día que me desvirgó. *Risita*"
        mc "A mí también me gustaría. Eso sería casi un record, ¿no?"
        eri "Entonces, cuando acabe la comida te secuestro y vamos a tu habitación. A solas."
        eri "Ahora voy ir al lavabo y a volver con Eva antes de que [emm] le pregunte a cuanta gente ha matado. Hasta ahora, cielo."
        mc "Hasta ahora, mi amor."
    else:
        call BlinkXP("c16s003_590" , "d") from _call_BlinkXP_1768
        eri "Debería ir al lavabo y volver con Eva antes de que [emm] le pregunte a cuanta gente ha matado."
        mc "Hasta ahora, [eri]."
    stop music fadeout (1.5)
    scene c16s003_550e with dissolve #reunión sin daphne
    "Continúas comiendo mientras observas como se va desarrollando la reunión. Al cabo de un rato, [dap] y [sca] se dirigen hacia ti."
    play music ("music/Between-Heaven-And-Earth.ogg")
    scene c16s003_600a with dissolve
    mc "¿Qué tal, chicas?"
    dap "Bien, Eva es fantástica."
    sca "Es muy divertida. Y tiene fijación en hacer bromas sobre ti."
    dap "Nos ha explicado tu cacería del topo en las lecciones de hoy. *Risa*"
    mc "Y, aparte de eso..."
    call BlinkXP("c16s003_605" , "d") from _call_BlinkXP_1769
    dap "Aparte de eso... quiero ir a Aruba."
    mc "¿Qué? ¿Por qué?"
    dap "Bueno, ahora soy accionista de una empresa de tecnología punta. Quiero aprender todo lo posible sobre como funciona."
    dap "Incluso trabajar en NTR cuando acabe la carrera."
    call BlinkXP("c16s003_610" , "d") from _call_BlinkXP_1770
    sca "A mí tampoco me importaría trabajar allí. Me encanta la medicina, pero no sé si estoy hecha para tratar con pacientes."
    sca "Espero que me contratéis para hacer investigación médica."
    mc "Chicas, esperad. Acabáis de enteraros que NTR existe y ya estáis pensando en cambiar vuestros planes de futuro."
    scene c16s003_600b with dissolve
    dap "Es lógico hacerlo. Las circunstancias han cambiado y es una oportunidad increíble."
    sca "No es cambiar los planes, sino adaptarlos a la nueva realidad. Clonación, nuevos dispositivos médicos... es el sueño de cualquier investigador."
    dap "Y una legislación que no pone demasiados impedimentos." (multiple=2)
    sca "En un pais donde todo eso es legal." (multiple=2)
    mc "Por suerte os quedan años para acabar vuestras carreras... aún os quedan meses para empezarla..."
    mc "Aparte de eso, ¿como ha ido La Conversación?"
    call BlinkXP("c16s003_630a" , "d") from _call_BlinkXP_1771
    dap "Ha sido extraño. Saber que mi madre... y el resto... nos habéis ocultado algo tan importante como esto..."
    call BlinkXP("c16s003_630b" , "d") from _call_BlinkXP_1772
    if persistent.family:
        dap "Una empresa de tecnología punta, clonación, espionaje, secuestros... ¡Me encanta! Pero me hubiera gustado saberlo antes."
    else:
        dap "Creía que [eri] y yo éramos adoptadas. Ahora resulta que somos clones de Eva. ¡Mola mucho más!"
    dap "Y tener a Eva delante es como mirarse en un espejo. Un espejo más musculoso de lo que yo nunca seré, pero un espejo."
    call BlinkXP("c16s003_630c" , "d") from _call_BlinkXP_1773
    dap "Sé que los genes no tienen nada que ver en cómo somos, aparte de físicamente, pero llevo toda la comida estudiándola esperando que reaccione de una forma... o ponga una expresión..."
    dap "Y la mayoría de veces actúa de una forma distinta de como lo haría yo."
    call BlinkXP("c16s003_635" , "d") from _call_BlinkXP_1774
    sca "Es raro ver como crece la familia. Y más aún creciendo de esta forma."
    sca "No todos los días te enteras de que la clonación humana existe, ni de que tu mejor amiga es accionista de una empresa que la lleva a cabo."
    mc "Últimamente están pasando muchas cosas, y aún pueden pasar muchas cosas con la empresa."
    if dap._var("route"):
        call BlinkXP("c16s003_615" , "d") from _call_BlinkXP_1775
        dap "Hablando de la empresa... Mi madre me ha dicho que tienes unos test de embarazo especiales, por si alguna vez los necesito... desde la semana pasada sabe que tengo novio..."
        mc "Sí, los tengo, pero aún no los puedes usar. Tienen que pasar 48 horas, con lo que hasta esta noche o mañana no van a servir."
        dap "Mejor mañana entonces. Así aseguramos el resultado si me dejaste embarazada al segundo intento."
        if sca._var("route"):
            call BlinkXP("c16s003_620" , "d") from _call_BlinkXP_1776
            sca "¿Dos? ¿La misma noche? Yo no tuve tanta suerte..."
            mc "Tú no me dejaste quedarme a dormir. *Risa* ¿Tú también quieres hacerte la prueba?"
            call BlinkXP("c16s003_625" , "d") from _call_BlinkXP_1777
            sca "Sí. Puedo esperar a hacerla mañana con [dap]."
            mc "Perfecto entonces. Mañana llevo un par de pruebas a vuestra habitación."
            scene c16s003_600c with dissolve
            dap "¿Te imaginas que nos quedáramos embarazadas a la vez? Por cierto, me he pedido Maeve si es niña. *Risita*"
            sca "Yo aún no he pensado en nombres... la próxima vez que esté a solas con mi novio lo hablaremos. *Risita*"
        else:
            scene c16s003_600c with dissolve
            sca "¿Te imaginas que te quedaras embarazada en tu primera cita? *Risita* "
            dap "Si es de [mc] me da lo mismo que sea en la primera o en la tercera. *Risita*"
    elif sca._var("route"):
        mc "Hablando de pasar cosas... [sca], tenemos unas pruebas de embarazo especiales, por si quieres hacerte la prueba."
        call BlinkXP("c16s003_640" , "d") from _call_BlinkXP_1778
        sca "Pero se necesitan 15 días o así para que sean efectivas, ¿no?"
        mc "No con estas. 48 horas después del sexo. Con lo que ya te las podrías hacer y tener el resultado mañana. Si quieres."
        call BlinkXP("c16s003_645" , "d") from _call_BlinkXP_1779
        sca "Si, quiero. *Risita* Ahora parece que me hayas pedido matrimonio. ¿Te va bien que lo hagamos mañana por la mañana? Hoy estás muy ocupado..."
        mc "Perfecto. Mañana te llevo el test a vuestra habitación."
        scene c16s003_600c with dissolve
        dap "¿Te imaginas que te quedaras embarazada en tu primera cita? *Risita* "
        sca "Si es de [mc] me da lo mismo que sea en la primera o en la tercera. *Risita*"
    if mc._var("edmundsStory"):
        mc "[dap], ¿puedo hablar un momento a solas con [sca]?"
        scene c16s003_600d with dissolve
        dap "Por supuesto, yo debo volver a mirarme en los ojos de Eva."
        call BlinkXP("c16s003_650" , "d") from _call_BlinkXP_1780
        sca "¿Pasa algo, [mc]?"
        mc "Le he preguntado a Amanda y a Eva por los tests de ADN, sin decirle para quien era, y Amanda me traerá uno esta noche. Por si quieres que lo hagamos."
        call BlinkXP("c16s003_655" , "d") from _call_BlinkXP_1781
        sca "¡Sí! ¿Cuándo podríamos tener los resultados?"
        mc "Por lo que me ha dicho, el martes. No son de NTR, sino de un laboratorio de Atascadero."
        sca "¡Genial! Tengo muchas ganas de saber si lo que sospechamos es cierto. Y de poder contárselo a la familia."
        mc "A lo mejor no hay nada que contar."
        call BlinkXP("c16s003_660" , "d") from _call_BlinkXP_1782
        sca "Salga lo que salga... al menos saldremos de dudas."
        if sca._var("route"):
            sca "Lo podemos hacer mañana cuando hagamos el test de embarazo."
        else:
            sca "Lo podemos hacer mañana por la mañana. Hoy va a haber mucho movimiento en casa. ¿Lo hacemos en mi habitación?"
        mc "¿Con [dap]? ¿Qué le vamos a contar?"
        call BlinkXP("c16s003_665a" , "d") from _call_BlinkXP_1783
        sca "Es posible... que se me escapara el otro día... sabe que existe la posibilidad de que haya encontrado a mi padre."
        mc "[sca], dijimos de guardarlo en secreto hasta no tener confirmación."
        sca "Lo sé, pero estaba muy emocionada, y [dap] me conoce demasiado bien. Preguntó y no quería mentirle. Pero no le he dicho quién podría ser."
        mc "Te entiendo. Cada vez odio más los secretos. Entonces, mañana en tu habitación."
        call BlinkXP("c16s003_665b" , "d") from _call_BlinkXP_1784
        sca "Sí, mañana en mi habitación. Te voy a dejar y a volver con Eva. No te gires, pero [emm] lleva un rato mirando en esta dirección, como si quisiera hablar contigo."
        sca "Creo que necesitáis hablar. No gritéis mucho. No se ha tomado muy bien las noticias."
    else:
        sca "No te gires, pero [emm] lleva un rato mirando en esta dirección, como si quisiera hablar contigo."
        dap "Creo que os vamos a dejar para que habléis. No gritéis mucho. No se ha tomado muy bien las noticias."
    mc "OK. Me da un poco de miedo. Esconde los cuchillos."
    stop music fadeout 1.5
    sca "Acaban de llegar Kate, Debbie, y [sai]... Es una buena oportunidad para presentarles a Eva."
    call BlinkXP("c16s003_670" , "f") from _call_BlinkXP_1785
    play music ("music/Tribal.ogg")
    emm "Sabes que hoy te odio, ¿verdad?"
    mc "Me lo imagino. Pero yo no tengo la culpa, [emm]."
    emm "Tú tienes la culpa de no habérmelo explicado antes."
    mc "No podía hacerlo, [emm]. Tenía que ser Mamá."
    if emm._var("route") and mar._var("route"):
        call BlinkXP("c16s003_675" , "d") from _call_BlinkXP_1786
        emm "No puedo creer que, sabiendo lo que sabíais anoche, no me lo dijeráis."
        if persistent.family:
            emm "¡Joder! Yo creía que eramos una familia y que no tenía que haber secretos."
        else:
            emm "*Susurrando* Yo pensando que estaba teniendo una sesión de sexo con mi hermano y mi madre y resulta que son dos desconocidos. Y todo por guardar secretos."
            call c16s003_Text2 from _call_c16s003_Text2
        mc "Hemos tenido secretos desde que estamos juntos. Tú guardaste en secreto que sabías lo mío con Mamá. ¿Sólo importan los secretos cuando eres tú quien no los sabe?"
        mc "Y Mamá quería tener una conversación a solas contigo hoy. Ayer estaba muy afectada por todo esto. ¿Por qué crees que pasó ayer precisamente?"
    elif emm._var("route"):
        call BlinkXP("c16s003_675" , "d") from _call_BlinkXP_1787
        emm "No puedo creer que, sabiendo lo que sabías, no me lo dijeráis."
        if persistent.family:
            emm "¡Joder! Yo creía que eramos una familia y que no tenía que haber secretos. *Susurrando* ¡Y eres mi novio!"
        else:
            emm "Yo pensando que me estaba acostando con mi hermano y resulta que era un desconocido. Y todo por guardar secretos."
            call c16s003_Text2 from _call_c16s003_Text2_1
        mc "Hemos tenido secretos desde que estamos juntos. ¿O le has contado lo nuestro a alguien sin que se te escapara? ¿Sólo importan los secretos cuando eres tú quien no los sabe?"
        mc "Y Mamá quería tener una conversación a solas contigo hoy. Ayer estaba muy afectada por todo esto."
    else:
        call BlinkXP("c16s003_675" , "d") from _call_BlinkXP_1788
        emm "No puedo creer que, sabiendo lo que sabías, no me lo dijeráis."
        if persistent.family:
            emm "¡Joder! Yo creía que eramos una familia y que no tenía que haber secretos."
        else:
            emm "Yo pensando que me tenía una familia y resulta que eran unos desconocidos. Y todo por guardar secretos."
            call c16s003_Text2 from _call_c16s003_Text2_2
        mc "Hemos tenido secretos desde siempre. ¿O le has contado a alguien que me besaste al volver del Twins? ¿Sólo importan los secretos cuando eres tú quien no los sabe?"
        mc "Y Mamá quería tener una conversación a solas contigo hoy. Ayer estaba muy afectada por todo esto."
    call BlinkXP("c16s003_680" , "d") from _call_BlinkXP_1789
    emm "¿Afectada por qué? ¿Porque su secreto se iba a la mierda?"
    mc "No, [emm]. Porque sabía lo que te podía afectar La Conversación. Porque sabía que te podías enfadar. Yo intenté convencerla de que has madurado, de que ya eres adulta."
    mc "Pero veo que me equivoqué."
    call BlinkXP("c16s003_685" , "d") from _call_BlinkXP_1790
    if emm._var("route"):
        emm "¡Ahora resulta que no soy adulta! Sois vosotros los que vais con secretos y la que no es adulta soy yo. *Susurrando* Para follar contigo soy adulta, pero para saber esto no."
    else:
        emm "¡Ahora resulta que no soy adulta! Sois vosotros los que vais con secretos y la que no es adulta soy yo."
    mc "[emm], yo siempre te he considerado una adulta desde que volví. Te lo he demostrado. *Susurrando* Y el sexo no tiene nada que ver."
    if persistent.family:
        mc "Vale, sí. Hay una empresa y hay un clon tuyo por ahí. ¿Qué ibas a hacer con esa información? Imágína que te lo hubiéramos dicho hace cuatro años."
        call c16s003_Text1 from _call_c16s003_Text1
        mc "Y por eso te lo ha contado ahora. Por entonces ni siquiera sabíamos que Amanda existía. Solo que Mamá y Tía [nor] tenían acciones de la empresa que fundaron nuestros tíos."
    else:
        mc "Vale, sí. Hay una empresa y eres el clon de Amanda. ¿Qué ibas a hacer con esa información? Imágína que te lo hubiéramos dicho hace cuatro años."
        call c16s003_Text1 from _call_c16s003_Text1_1
        mc "Y por eso te lo ha contado ahora. Por entonces ni siquiera sabíamos que Amanda existía. Sabíamos que eras un clon, pero no de quién."
    call BlinkXP("c16s003_695" , "d") from _call_BlinkXP_1791
    emm "¡Pero hace casi una semana que sabéis lo de Amanda y Eva!"
    mc "Cuatro días. Y no estábamos seguros del todo. Mamá vió a Amanda ayer por primera vez. Y te lo ha contado hoy. No le puedes pedir más."
    call BlinkXP("c16s003_700" , "d") from _call_BlinkXP_1792
    emm "No crees que estoy exagerando, ¿verdad?"
    mc "Sabía que te ibas a enfadar, pero creo que sí, que lo estás exagerando."
    if persistent.family:
        mc "Yo tambén descubrí ayer que es posible que nuestros tíos fueran asesinados..."
    else:
        mc "Tú has descubierto que eras un clon. Yo descubrí ayer que es posible que a mi madre biológica la asesinaran..."
    call BlinkXP("c16s003_705" , "v") from _call_BlinkXP_1793
    emm "¿Qué?"
    mc "Si Mamá no te lo ha dicho es porque no hay pruebas, pero Aaron, Amanda, y Eva piensan que el accidente de avión pudo ser un sabotaje."
    emm "¡Eso es muy jodido! Yo estaba histérica porque pensaba que alguien nos quisiera matar. Con el accidente de avión lo consiguieron..."
    stop music fadeout (1.5)
    mc "Ellos no tenían a Eva y a Amanda para protegerlos. Nosotros sí."
    call BlinkXP("c16s003_710" , "d") from _call_BlinkXP_1794
    play music ("music/What-Ive-Found.ogg")
    emm "Es diferente de lo que me había imaginado... Me imaginaba una [dap]... por alguna razón no me imaginaba que se pareciera a [eri]."
    emm "Pero cuanto más hablo con ella, más me recuerda a alguien, y no sé a quien. Pero no es a [dap] ni a [eri]."
    mc "Yo sé a quién te recuerda. Si en un par de días no lo has descubierto, te lo diré."
    call BlinkXP("c16s003_715" , "d") from _call_BlinkXP_1795
    emm "Pero me cae muy bien. Creo que podríamos ser amigas. Además tiene muy buen gusto, el top es precioso, aunque sea blanco."
    mc "Me ha preguntado si se ponía uno rosa para gustarte más. Estaba muy nerviosa por conoceros. Piensa que para ella también tiene que ser difícil."
    call BlinkXP("c16s003_720" , "d") from _call_BlinkXP_1796
    emm "Me lo imagino. No ha querido contar mucho de ella misma, pero por lo que me ha contado Mamá..."
    if not persistent.family:
        mcp "(Vuelve a ser Mamá...)"
    mc "Ha tenido una vida que ninguno de nosotros desearíamos."
    call BlinkXP("c16s003_725" , "d") from _call_BlinkXP_1797
    emm "Pero ahora que somos sus jefes, podemos dejarle hacer lo que quiera, ¿no? Que deje de ser una mercenaria, que tenga una vida más normal."
    mc "Si quiere, supongo que sí."
    emm "Claro, si quiere."
    call BlinkXP("c16s003_730" , "d") from _call_BlinkXP_1798
    emm "Y ahora que somos ricos, ¿puedo comprarme un Ferarri rosa?"
    mc "*Risa* Aún no somos ricos, [emm]. Hay que decidir qué hacer con la empresa. Pero dejémoslo para otro día."
    call BlinkXP("c16s003_735" , "d") from _call_BlinkXP_1799
    emm "Mira, nuestra invitada se acerca. Puede que nos haya oído hablar de ella."
    call BlinkXP("c16s003_740" , "d") from _call_BlinkXP_1800
    eva "[emm], perdona si te interrumpo. ¿Puedo hablar con [mc] a solas un momento?"
    call BlinkXP("c16s003_735b" , "d") from _call_BlinkXP_1801
    emm "Por supuesto. Tengo que ir a... disculparme con mi madre."
    stop music fadeout (1.5)
    call BlinkXP("c16s003_745" , "f") from _call_BlinkXP_1802
    eva "¿Me puedes sacar de aquí?"
    play music ("music/Rise-Up.ogg")
    mc "¿Ya te han aburrido?"
    call BlinkXP("c16s003_750" , "d") from _call_BlinkXP_1803
    eva "No, para nada. Pero se están portando todas tan bien conmigo... "
    eva "Necesito aire fresco. Creo que [nor] ha cortado muchas cebollas hoy en esta cocina."
    mc "¿Cuánto tiempo te va a llevar retirar las cámaras?"
    call BlinkXP("c16s003_755" , "d") from _call_BlinkXP_1804
    eva "Un par de horas, ¿por qué?"
    mc "Ahí tienes tu excusa. Un par de horas para las cámaras, volver a la base para relevar a Amanda... Si no empiezas ahora no te va a dar tiempo de todo."
    eva "Tengo tiempo de sobras."
    mc "Pero yo no lo sabía hasta ahora mismo y nadie lo sabe. No sabemos donde está la base. Y, de momento, no sé si quieres que lo sepamos."
    call BlinkXP("c16s003_760" , "d") from _call_BlinkXP_1805
    eva "¡Jodido manipulador! *Risa*"
    mc "Tú misma lo has dicho. No soy manipulador, protejo a mis chicas... de mis otras chicas. *Risa*"
    call BlinkXP("c16s003_765" , "d") from _call_BlinkXP_1806
    eva "{b}¿Qué?{/b} ¿Tus chicas? {b}¿Me consideras una de tus chicas?{/b}"
    mc "Sí, Eva. Tú y Amanda sois unas de mis chicas... de nuestras chicas. No lo voy a volver a repetir más. Sois parte de esta familia."
    call BlinkXP("c16s003_770" , "d") from _call_BlinkXP_1807 #sonrisa pícara
    eva "Mmmm... vaaale..."
    eva "¿Por dónde quieres que empiece a retirar las cámaras?"
    mc "Puedes empezar por mi casa. Ahora mismo está vacía."
    scene c16s003_775a with dissolve #Deb, Kat, Sai, Emm, Eri, Dap, Sca, Mar, Nor, Mee, Bet, Eva
    "Eva se despide de todo el mundo, prometiendo pasar de nuevo por la cocina antes de irse para despedirse de verdad."
    "Nadie quiere que Eva se vaya, pero nadie quiere tener cámaras en su habitación. Difícil disyuntiva. A regañadientes, dejan que te lleves a Eva."
    if eri._var("route"):
        "Quedas con [eri] en 10 minutos en tu habitación para hacer el test."
    call BlinkXP("c16s003_780" , "f") from _call_BlinkXP_1808
    eva "¡Phew! Ha sido intenso."
    mc "¿Peor de lo que creías?"
    call BlinkXP("c16s003_785" , "d") from _call_BlinkXP_1809
    eva "¡Mucho mejor! Pero demasiado intenso."
    mc "Me alegra que te lo hayas pasado bien."
    call BlinkXP("c16s003_790" , "d") from _call_BlinkXP_1810
    eva "Tengo una pregunta..."
    mc "Dime."
    eva "Has dicho que formamos parte de esta familia..."
    mc "Sí."
    eva "¿Para todo?"
    mc "Claro."
    call KissXP("c16s003_795" , "h") from _call_KissXP_53
    eva "Buenos días, [mc]... o buenas tardes ya."
    mc "¡Wow, Eva! ¿Lo decías por eso?"
    call BlinkXP("c16s003_800" , "d") from _call_BlinkXP_1811
    eva "Si ellas pueden besar a mi primo cañón, o lo que seas, yo también."
    mc "*Risa* Vamos a quitar las cámaras."
    stop music fadeout (1.5)
    scene black with dissolve
    "Acompañas a Eva a tu habitación, de donde saca un par de cámaras y un micrófono. Ella seguirá en solitario por la casa"
    if eri._var("route"):
        "[eri] llega unos minutos después y hacéis el test. Ahora solo queda esperar 24 horas para saber el resultado. Empiezas a estar ansioso."
    return
label c16s003_Text1:
    mc "¿Me puedes asegurar que la [emm] de hace cuatro años no iba a fanfarronear sobre ello? ¿Con lo que te gustaba ser el centro de atención?"
    call BlinkXP("c16s003_690" , "d") from _call_BlinkXP_1812
    emm "Seguramente lo hubiera hecho... pero ya no soy así."
    return
label c16s003_Text2:
    emm "Y deja de llamarla Mamá. Es tan tu madre como la mía."
    mc "[emm], Mamá sigue siendo Mamá, y tú sigues siendo mi hermana. Me da lo mismo no llevar los mismos genes que vosotras."
    return
label c16s004_DateWithMaddie:
    if _in_replay:
        call mrS3_mad_type from _call_mrS3_mad_type_1
    "Decides llamar a Maddie para retrasar la cita. No vas a poder llegar antes de que acabe la cena con Amanda."
    play music ("music/AmbientPianoStrings.ogg")
    scene c16s004_005 with dissolve
    mc "Hola, Maddie. Tengo malas noticias."
    if mad._var("romance"):
        call BlinkXP ("c16s004_010" , "d") from _call_BlinkXP_1813
        mad "Hola, guapo. Al final tienes que recoger a aquella chica, ¿verdad?"
        mc "Sí, y además después hay una cena en mi casa a la que no puedo faltar."
        call BlinkXP ("c16s004_015" , "d") from _call_BlinkXP_1814
        mad "Con lo que tendremos que pasar nuestra película a otro día... o anularla..."
        mc "Había pensado en pasarme al acabar la cena, si quieres."
        call BlinkXP ("c16s004_020" , "d") from _call_BlinkXP_1815
        mad "¡Me parece genial! Tengo una sorpresa para ti en mis manos ahora mismo."
        mc "Espero que sea lo que pienso. *Risa*"
        call BlinkXP ("c16s004_025" , "d") from _call_BlinkXP_1816
        mad "¡Picarón! Es algo que me he probado para esta noche. Creo que te va a gustar."
        mc "Estoy deseando verlo. Cuando salga de casa, ¿te llamo para decirte que voy en camino?"
        call BlinkXP ("c16s004_030" , "d") from _call_BlinkXP_1817
        mad "Lo estoy deseando. Te veo luego."
        mc "Hasta luego, preciosa."
    elif mad._var("sub"):
        call BlinkXP ("c16s004_035" , "d") from _call_BlinkXP_1818
        mad "Hola, [mc]. No vas a poder venir, ¿verdad? Tienes que recoger a aquella chica..."
        mc "La tengo que recoger, y después hay una cena en mi casa a la que no puedo faltar."
        call BlinkXP ("c16s004_040" , "d") from _call_BlinkXP_1819
        mad "Entonces... ¿quieres retrasar nuestra... cita... a otro día?"
        mc "No, me pasaré al acabar la cena por tu casa."
        call BlinkXP ("c16s004_045" , "d") from _call_BlinkXP_1820
        mad "¡Sí!... si es lo que quieres... Precisamente tengo en las manos algo para ti ahora mismo."
        mc "Toda tú eres para mí, Maddie. *Risa*"
        call BlinkXP ("c16s004_050" , "d") from _call_BlinkXP_1821
        mad "No me refería a eso, es algo que me he comprado para ti. Creo que te va a gustar."
        mc "Estoy deseando verlo. Te llamo cuando salga de casa para decirte que voy en camino."
        call BlinkXP ("c16s004_055" , "d") from _call_BlinkXP_1822
        mad "Lo estoy deseando. Te veo luego."
        mc "Hasta luego, preciosa."
    else:
        call BlinkXP ("c16s004_060" , "d") from _call_BlinkXP_1823
        mad "Hola, guapo. Al final quieres anteponer a aquella chica a mí, ¿verdad?"
        mc "No es eso. La tengo que recoger, sí, y después hay una cena en mi casa a la que no puedo faltar."
        call BlinkXP ("c16s004_065" , "d") from _call_BlinkXP_1824
        mad "¿Me estás pidiendo permiso para cambiar nuestra cita a otro día?"
        mc "Había pensado en pasarme al acabar la cena, si me lo permites."
        call BlinkXP ("c16s004_070" , "d") from _call_BlinkXP_1825
        mad "No es mala idea. Además demuestras iniciativa. Sólo por eso, tengo un premio para ti en mis manos ahora mismo."
        mc "Estoy deseando verlo."
        call BlinkXP ("c16s004_075" , "d") from _call_BlinkXP_1826
        mad "No es lo que crees. Es algo que me he probado para esta tarde... noche. Creo que va a darle un tono diferente a la noche."
        mc "Estoy deseando verlo. Cuando salga de casa, ¿quieres que te llame para decirte que voy en camino?"
        call BlinkXP ("c16s004_080" , "d") from _call_BlinkXP_1827
        mad "Sí, hazlo. Te veo luego."
        mc "Hasta luego, Maddie."
    stop music fadeout (1.5)
    return
label c16s004_ConvoSairaAboutMegan:
    if _in_replay:
        call mrS3_sai_route from _call_mrS3_sai_route_18
        if not sai._var("route"):
            call mrS3_sca_route from _call_mrS3_sca_route_25
            call mrS3_eil_route from _call_mrS3_eil_route_22
        call mrS3_deb_route from _call_mrS3_deb_route_23
        menu:
            "¿Cuántos Puntos de Relación tienes con Debbie?"
            "5 o más":
                $ deb._var("relationshipPoints", 5, intention = "set")
            "Menos de 5":
                $ deb._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Lisa?"
            "5 o más":
                $ lis._var("relationshipPoints", 5, intention = "set")
            "Menos de 5":
                $ lis._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Kim?"
            "5 o más":
                $ kim._var("relationshipPoints", 5, intention = "set")
            "Menos de 5":
                $ kim._var("relationshipPoints", -5, intention = "set")
        menu:
            "¿Cuántos Puntos de Relación tienes con Kate?"
            "5 o más":
                $ kat._var("relationshipPoints", 5, intention = "set")
            "Menos de 5":
                $ kat._var("relationshipPoints", -5, intention = "set")
    scene black with dissolve
    "Llega el momento de ir a buscar a [meg] a la estación. Está siendo un día muy ocupado."
    "Se te ha ocurrido una idea para no tener que cederle tu cama, pero tienes que hablar con [sai]."
    scene c16s004_100c with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Soy yo."
    play music ("music/RayOfHope.ogg")
    sai "*A través de la puerta* Pasa."
    if sai._var("route"):
        call KissXP ("c16s004_100" , "d") from _call_KissXP_54
        sai "Hola, mi amor. Me cuesta mucho no besarte de verdad delante de todas..."
        mc "A mí también."
        call BlinkXP ("c16s004_105" , "d") from _call_BlinkXP_1828
        sai "Te va a parecer gracioso, pero ahora soy yo la que está dudando si deberíamos hacerlo público."
        call c16s004_ConvoSairaAboutGirls from _call_c16s004_ConvoSairaAboutGirls
        call BlinkXP ("c16s004_115" , "d") from _call_BlinkXP_1829
        sai "[eil] y [sca] ya lo saben. Creo que, de momento, es suficiente. Déjame establecerme un poco en la casa antes de hacerlo público."
        mc "Sí, me parece bien. Quiero que te sientas a gusto en casa, y si crees que esto te va a ayudar..."
        mc "Hablando de ayuda, venía a pedirte un favor..."
        call BlinkXP ("c16s004_120" , "d") from _call_BlinkXP_1830
    else:
        call BlinkXP ("c16s004_110" , "d") from _call_BlinkXP_1831
        sai "Hola, [mc]. ¿Vienes a hablar o te puedo ayudar en algo?"
        mc "Las dos cosas."
        call BlinkXP ("c16s004_115" , "d") from _call_BlinkXP_1832
        sai "Te ayudaré en lo que necesites, pero me gustaría hablar de nosotros primero."
        mc "Hablemos..."
        call BlinkXP ("c16s004_120" , "d") from _call_BlinkXP_1833
        sai "He estado pensando, y he decidido que sí, que podría aceptar una relación abierta contigo otra vez."
        sai "Pero con unas diferencias sobre lo que teníamos en Portland."
        mc "Dime."
        call BlinkXP ("c16s004_125" , "d") from _call_BlinkXP_1834
        sai "La principal es que, de momento, no quiero que nadie sepa que estamos juntos."
        call c16s004_ConvoSairaAboutGirls from _call_c16s004_ConvoSairaAboutGirls_1
        if eil._var("route"):
            call BlinkXP ("c16s004_130" , "d") from _call_BlinkXP_1835
            sai "Además, estás con [eil], y no quiero que me pueda ver como una amenaza. Creo que realmente puede convertirse en mi mejor amiga. ¡Vaya sorpresa!"
            mc "Es una mujer fantástica."
        if sca._var("route"):
            call BlinkXP ("c16s004_135" , "d") from _call_BlinkXP_1836
            sai "[sca] lo ha pasado muy mal y está encontrando estabilidad en casa y contigo. No quiero ser un elemento que la ponga nerviosa."
            mc "[sca] es más fuerte de lo que parece, te lo aseguro."
        call BlinkXP ("c16s004_140" , "d") from _call_BlinkXP_1837
        sai "Y tu familia... no sé cómo aceptaría que volviéramos a estar juntos. He visto algunas miradas que no he sabido como interpretar."
        mc "Supongo que es porque, como yo, no entienden por qué te mudaste sin avisarme. Yo puedo entenderlo ahora, pero a ellas no se lo ha explicado nadie y las desconciertas."
        mc "¿Y el resto de diferencias?"
        call BlinkXP ("c16s004_145" , "d") from _call_BlinkXP_1838
        sai "No quiero una relación abierta como teníamos en Portland. Nunca me acosté con nadie que no fueras tú."
        sai "Si tengo que aceptar que tú puedas salir con otras, lo haré. Es lo que teníamos allí. Pero en mi lado de la relación va a ser cerrada."
        sai "No quiero tener la opción de salir con otros tíos. Nunca la voy a utilizar de todas formas."
        mc "¡Wow, [sai]! Me pones en una encrucijada."
        if persistent.walkthrough:
            $ wt1 = _("Ruta con [sai] abierta.")
            $ wt2 = _("Ruta con [sai] cerrada.\n{color=#ff0000}{b}No habrá más oportunidades de abrir la ruta{/b}{/color}")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Acepto." (wt = wt1):
                $ sai._var("route", True)
                $ mc._var("relationships", 1, "add")
                $ sai._var("routeSecondChance", True)
                call c16s004_SairaPath from _call_c16s004_SairaPath
            "No puedo aceptar." (wt = wt2):
                call c16s004_NoSairaPath from _call_c16s004_NoSairaPath
        $ resetWalkthrough ()
    call c16s004_SleepingArrangements from _call_c16s004_SleepingArrangements
    if sai._var("route"):
        call KissXP ("c16s004_100" , "d") from _call_KissXP_55
        sai "Te quiero. Conduce con cuidado. Te veo luego."
    else:
        call BlinkXP ("c16s004_200" , "d") from _call_BlinkXP_1839 #abrazo
        sai "Conduce con cuidado. Te veo luego."
    mc "Hasta luego, preciosa."
    mc "Por cierto, me gusta el nuevo peinado."
    stop music fadeout (1.5)
    return
label c16s004_ConvoSairaAboutGirls:
    mc "Me acabas de sorprender mucho."
    call BlinkXP ("c16s004_150" , "d") from _call_BlinkXP_1840
    sai "Sabes que no tenía muchas amigas en Portland..."
    mc "Si tu definición de no tener muchas amigas es no tener ninguna, sí. Tenías conocidas y chicas con las que te llevabas bien, pero ¿amigas de verdad?... no creo que tuvieras ninguna."
    call BlinkXP ("c16s004_155" , "d") from _call_BlinkXP_1841
    sai "Bueno, sí, eso..."
    sai "No voy a decir que la culpa fuera tuya, claro..."
    mc "¿Mía? ¿Por qué?"
    call BlinkXP ("c16s004_160" , "d") from _call_BlinkXP_1842
    sai "Porque salía contigo. O teníamos la falsa relación abierta que teníamos, para ser más exactos."
    sai "Muchas de las chicas que se me acercaban era porque querían saber si me importaría que intentaran algo contigo."
    sai "Pese a que les decía que podían intentarlo, creo que se me debía notar en la cara que mentía. Es difícil que quisieran ser mis amigas después de eso."
    mc "No me lo habías dicho nunca."
    call BlinkXP ("c16s004_165" , "d") from _call_BlinkXP_1843
    sai "Una cosa es que tuvieras libertad para salir con quien quisieras, y otra diferente que te las buscara yo, ¿no?"
    mc "Entiendo, pero ¿qué tiene que ver con esto?"
    call BlinkXP ("c16s004_170" , "d") from _call_BlinkXP_1844
    sai "Que no quiero que se repita lo mismo aquí. Anoche estuvimos hablando mucho sobre ti. Me bombardearon a preguntas."
    sai "No fuiste el único tema de conversación, pero la mayoría de la conversación giró en torno a ti cuando supieron lo que teníamos en Portland."
    $ Aux = 0
    if deb.rps > 4:
        $ Aux = Aux + 1
        call BlinkXP ("c16s004_175" , "d") from _call_BlinkXP_1845
        sai "A Debbie le gustas. No es que me haya dicho nada, pero se le nota."
        if deb._var("route"):
            mc "Creo que es muy tímida como para hablar de eso con nadie que no sea su hermana."
        else:
            mc "No sé si le gusto de esa forma."
    if kim.rps > 4:
        $ Aux = Aux + 1
        call BlinkXP ("c16s004_180" , "d") from _call_BlinkXP_1846
        sai "Kim está deseando echarte el lazo. Anoche no hacía más que preguntar por ti y por nuestra relación."
        sai "No me extrañaría que te tirase los trastos en breve."
        mc "Creo que le caigo bien, pero no sé si llegará a eso."
    if lis.rps > 4:
        $ Aux = Aux + 1
        call BlinkXP ("c16s004_185" , "d") from _call_BlinkXP_1847
        sai "Lisa aún no ha decidido si le gustas o no. Al menos de esa forma. Anoche parecía que estaba luchando consigo misma cada vez que hacía una pregunta sobre ti."
        sai "Creo que ha dejado al tal Anthony, si es que alguna vez han estado juntos, por ti."
        mc "¿Lisa? Creo que te equivocas. Anthony no ha resultado ser lo que ella esperaba."
    if kat.rps > 4:
        $ Aux = Aux + 1
        call BlinkXP ("c16s004_190" , "d") from _call_BlinkXP_1848
        sai "Diría que Kate siente curiosidad hacia ti. No sé si en plan romántico o es que no sabe dónde encajarte en su idea del mundo."
        mc "Creo que te equivocas respecto a Kate."
        sai "¿Por qué? ¿Porque dice que es lesbiana? No te dejes engañar. Es bisexual. Le gustan chicos y chicas. Nos contó algo que... que tiene que quedar entre las chicas."
        sai "Pero hazme caso. No es una lesbiana de esas que piensan que todos los hombres son el diablo. Al menos ya no."
    mc "Pero sigo sin entender qué tiene que ver eso con hacerlo público."
    call BlinkXP ("c16s004_195" , "d") from _call_BlinkXP_1849
    sai "A veces te cuesta entender las cosas..."
    if Aux == 1:
        sai "Me estoy empezando a llevar bien con el resto de las chicas, y no querría que ella me empezara a mirar de otra forma si se enteran que hemos reanudado lo nuestro."
        sai "Además, creo que si se enterara de que estamos juntos, no intentaría nada contigo. Y no te puedo negar eso si acepto esta relación."
    else:
        if Aux > 1:
            sai "Me estoy empezando a llevar bien con el resto de las chicas, y no querría que ninguna me empezara a mirar de otra forma si se enteran que hemos reanudado lo nuestro."
        else:
            sai "Me estoy empezando a llevar bien con el resto de las chicas. No sé si le gustas a alguna de ellas, pero si lo hacemos público empezarían a mirarme de otra forma."
        sai "Además, creo que si se enteraran de que estamos juntos, no intentarían nada contigo. Y no te puedo negar eso si acepto esta relación."
    mc "Vale, lo entiendo. No me gustan los secretos, pero te entiendo."
    return
label c16s004_SairaPath:
    mc "Hubiera aceptado con cualquier condición que hubieras puesto. Has expuesto tus razones de una forma que las hacen irrechazables."
    call KissXP ("c16s004_100" , "d") from _call_KissXP_56
    sai "¡Me alegra tanto haberlo aclarado!"
    mc "Es muy difícil rechazar esos ojos."
    call BlinkXP ("c16s004_200" , "d") from _call_BlinkXP_1850 #abrazo
    sai "Siempre sabes qué decir para hacerme sentir bien."
    sai "Ahora me tienes que explicar cuál era la ayuda que necesitabas de mí, y después podemos empezar a desnudarnos."
    mc "Sobre eso... no va a poder ser y lo entenderás en cuanto te pida el favor."
    return
label c16s004_NoSairaPath:
    stop music fadeout (1.5)
    mc "[sai], te querré siempre, pero no estoy enamorado de ti. Lo estuve, pero me alejaste."
    play music ("music/1000lichter.ogg")
    call BlinkXP ("c16s004_205" , "d") from _call_BlinkXP_1851 #triste
    mc "No puedo atarte a una relación en la que no se te va a amar como te mereces."
    sai "Pero me dijiste que..."
    mc "Que teníamos que hablar. Y lo hemos hecho. Tu estás dispuesta a dar mucho más que yo, y eso sería injusto."
    call BlinkXP ("c16s004_210" , "d") from _call_BlinkXP_1852
    sai "No te preocupes, después del semestre de otoño, volveré a Portland a acabar la carrera. No quiero ser una molestia."
    mc "No quiero que te vayas, [sai]. Quédate y acaba la carrera aquí. Sé parte de esta familia. Y después decide qué quieres hacer."
    mc "Tú misma lo has dicho, empiezas a llevarte bien con las chicas, y con el resto de la familia no vas a tardar en hacerlo."
    mc "Quédate, por favor. Quiero que formes parte de mi vida, aunque no como te gustaría a ti."
    call BlinkXP ("c16s004_200" , "d") from _call_BlinkXP_1853 #abrazo
    sai "¡Joder, [mc]! Eres capaz de hacer sentir bien a una chica a la que acabas de rechazar."
    sai "No lo haces sólo porque ahora me vayas a pedir un favor, ¿verdad?"
    mc "*Risa* Sobre eso..."
    return
label c16s004_SleepingArrangements:
    call BlinkXP ("c16s004_250" , "d") from _call_BlinkXP_1854
    mc "¿Te acuerdas de [meg] Peel? ¿De Portland?"
    sai "¿La cantante? Sí, claro. Nunca fuimos buenas amigas, pero nos caíamos bien. ¿Por qué?"
    call BlinkXP ("c16s004_255" , "d") from _call_BlinkXP_1855
    mc "Vive en Westport, al norte. Canta en un club de Jazz, aquí en Newport, los fines de semana."
    sai "Oh, eso está genial. Tenía una voz preciosa, podríamos ir a escucharla un día. Pero ¿qué tiene que ver conmigo?"
    mc "Va a pasar este fin de semana en casa. Tiene el coche averiado."
    call BlinkXP ("c16s004_260" , "d") from _call_BlinkXP_1856
    sai "¿Dónde va a dormir? Tenéis la casa llena."
    mc "Ese es el favor que te quería pedir. ¿Te importaría compartir habitación con ella?"
    mc "Si no te parece bien le puedo ceder mi habitación y buscarme algún sitio donde dormir."
    if sai._var("route"):
        call BlinkXP ("c16s004_265" , "d") from _call_BlinkXP_1857
        sai "Cédele tu habitación y duerme aquí todo el fin de semana. O mejor aún, pasa aquí todo el fin de semana sin dormir. *Risa*"
        mc "Perfecto. Te pasarás todo el fin de semana gimiendo y tu secreto se esfumará. Las chicas no te hablarán y mi madre te echará laxante en el desayuno. *Risa*"
    else:
        call BlinkXP ("c16s004_270" , "d") from _call_BlinkXP_1858
        sai "No hay ningún problema. [meg] me gustaba y podemos aprovechar para ponernos al día."
        mc "Genial, no os paséis hablando hasta muy tarde cuando vuelva del trabajo, o molestaréis a todo el mundo. Las chicas no te hablarán y mi madre te echará laxante en el desayuno. *Risa*"
    call BlinkXP ("c16s004_275" , "d") from _call_BlinkXP_1859
    sai "[eil] me defendería de las chicas y me traería pañales. *Risa*"
    mc "De querer sacarle los ojos a ser las mejores amigas."
    call BlinkXP ("c16s004_280" , "d") from _call_BlinkXP_1860
    sai "Estaba totalmente equivocada con ella. Se ha portado muy bien conmigo."
    mc "Es normal que estuvieras equivocada. *Risa* No la conocías y para ti ya era La Bruja Pelirroja."
    call BlinkXP ("c16s004_285" , "d") from _call_BlinkXP_1861
    sai "No me lo recuerdes..."
    mc "Bueno, yo me voy a ir a buscar a [meg]. No sé si tienes que ordenar algo o hacerle hueco en el armario."
    call BlinkXP ("c16s004_290" , "d") from _call_BlinkXP_1862
    sai "Sí, recogeré las bragas de debajo de la cama y guardaré los consoladores bajo llave. *Risa* ¡Soy una chica ordenada, [mc]! ¡No tengo bragas bajo la cama!"
    mc "¡No lo decía por eso! *Risa* Pero no has dicho que no tengas consoladores."
    sai "¡Vete antes de que te pegue con uno en la frente!"
    return
label c16s005_PickUpMegan:
    if _in_replay:
        menu:
            "¿Amanda y Eva te dieron los test de embarazo?"
            "Sí":
                $ KnownToAmandaEva = 1
                $ PregnancyTests = True
            "No":
                $ KnownToAmandaEva = 0
                $ PregnancyTests = False
        call mrS3_meg_route from _call_mrS3_meg_route_7
        if meg._var("route"):
            call mrS3_mar_route from _call_mrS3_mar_route_36
    scene c16s005_005c with fade
    "Cuando llegas a la parada de autobús, [meg] interrumpe su conversación con una anciana para saludarte. La anciana te mira con una sonrisa."
    play music ("music/Gypsy-Jazz.ogg")
    call BlinkXP ("c16s005_010" , "f") from _call_BlinkXP_1863 #abrazo
    mc "Hola, preciosa. ¡Cuánta efusividad! ¿Qué le estabas contando a la anciana? Me ha mirado como si me conociera."
    if meg._var("route"):
        call KissXP ("c16s005_005" , "d") from _call_KissXP_57
        meg "Hola, guapísimo. Le he dicho que mi novio venía a buscarme y ha empezado a cotillear. *Risa*"
    else:
        meg "Hola, [mc]. Le he dicho que un amigo venía a buscarme y ha empezado a cotillear y a hacer preguntas incómodas. *Risa*"
        meg "Ahora puede pensar lo que quiera. *Risa*"
    call BlinkXP ("c16s005_015" , "d") from _call_BlinkXP_1864
    mc "¿Hace mucho que has llegado? ¿A qué hora tienes que estar en el club?"
    meg "Diez minutos, pero se me han hecho eternos con las preguntas de la abuela. *Risa*"
    meg "Entro a trabajar a las 9. ¿Por qué lo preguntas?"
    mc "Déjame coger tu maleta. ¿Te dará tiempo de cenar en casa? "
    call BlinkXP ("c16s005_020" , "d") from _call_BlinkXP_1865
    meg "No puedo, los viernes vamos a cenar todo el personal antes de abrir el Jazz Corner. Es una costumbre. Pero mañana seguro que puedo cenar con vosotros."
    if meg._var("route") and mar._var("route"):
        meg "Si tu madre no me echa de casa cuando le diga que las dos estamos contigo, claro."
        mc "Estoy seguro de que te vas a llevar una sorpresa con mi madre. Por no hablar de la que te vas a llevar en la comida de mañana."
    else:
        mc "Entonces la sorpresa te la llevarás mañana durante la comida de mañana."
    call BlinkXP ("c16s005_025" , "d") from _call_BlinkXP_1866
    meg "¿A qué te refieres? ¿Qué sorpresa tienes preparada?"
    mc "Es el momento de que tengamos La Clonversación. Te lo explico en el coche."
    call BlinkXP ("c16s005_030" , "f") from _call_BlinkXP_1867
    $renpy.sound.play("music/Motor.ogg", loop=True)
    "Para cuando acabas La Conversación, ya estáis tan solo a unos minutos de casa. [meg] ha tenido la boca abierta con un gesto de sorpresa los últimos minutos."
    meg "¡Alucinante! ¿Me estás diciendo que habéis estado en peligro de que os asesinaran?"
    if persistent.family:
        meg "¿Que es posible que asesinaran a tus tíos en el accidente de avión?"
        meg "¿Que tienes clones como guardaespaldas? ¿Y que son clones de tu hermana y tus primas?"
    else:
        meg "¿Que es posible que asesinaran a tu madre en el accidente de avión?"
        meg "¿Que tu hermana y tus primas son clones de vuestros guardaespaldas?"
    meg "¿Que eres propietario de una empresa de clonación y que tienes un ejército privado... de clones?"
    mc "Más o menos. En resumen es eso. Aunque ni el ejército ni la empresa son míos. Son de la familia, y aún no sabemos qué vamos a hacer con ello."
    call BlinkXP ("c16s005_035" , "d") from _call_BlinkXP_1868
    meg "¡Creía que esas cosas no existían hasta hace diez minutos! Me da lo mismo de quien sean. ¡Es una mezcla de James Bind y la segunda trilogía de Galaxy Wars!"
    mc "Esa frase me la esperaría de [dap]. Te va a caer bien."
    call BlinkXP ("c16s005_040" , "d") from _call_BlinkXP_1869
    meg "Estoy flipando. Parece que te lo tomas como lo más normal del mundo."
    mc "He tenido La Clonversación cinco veces en las últimas 24 horas. He oído todo tipo de reacciones. Cuánto más la repito, más normal me parece todo."
    mc "Y cuando conozcas a las chicas, verás que son personas normales."
    call BlinkXP ("c16s005_045" , "d") from _call_BlinkXP_1870
    meg "No lo dudo. Seguro que son fantásticas. No quería que sonara así."
    mc "Ya te he dicho que he tenido la conversación varias veces. Conozco las reacciones. Yo estaría igual de flipado que tú."
    mc "Pero volviendo al tema de la cena, ¿quieres que te lleve a la cena del Jazz Corner?"
    call BlinkXP ("c16s005_050" , "d") from _call_BlinkXP_1871
    meg "No hace falta. Parece que tienes un día muy ocupado hoy. Pediré un Under para ir, y otro para volver cuando cerremos."
    meg "No quiero despertar a nadie al volver, ni que tengas que quedarte despierto hasta tarde para recogerme."
    mc "Bueno... sobre lo de despertar a alguien..."
    mc "Ha habido un pequeño problema logístico con las camas. Puedes dormir en mi habitación o en la de [sai]."
    call BlinkXP ("c16s005_055" , "d") from _call_BlinkXP_1872
    meg "¿[sai]? ¿Tu [sai] de Portland?"
    mc "Claro, tú no lo sabes. Sí, está haciendo un curso de verano aquí."
    if meg._var("route"):
        call BlinkXP ("c16s005_060" , "d") from _call_BlinkXP_1873
        meg "¿[sai] está aquí? ¿volvéis a estar juntos? ¿Cómo nos deja eso a nosotros?"
        mc "[meg], que esté o no con [sai] no afecta a cómo estemos tú y yo. Yo estoy contigo y ninguna otra mujer va a cambiar eso. Sea quién sea."
        call BlinkXP ("c16s005_065" , "d") from _call_BlinkXP_1874
        meg "Me quitas un peso de encima. Por un momento he pensado que... no sé..."
        if mar._var("route"):
            meg "Si a eso le sumas lo de tu madre... ¿Cuándo crees que sería un buen momento para hablar con tu madre? Ya sabes... sobre nosotros... y vosotros..."
            mc "Seguramente mañana. Hoy tú vas justa de tiempo y ella estará ocupada preparando la cena para Amanda. Es la primera vez que viene a cenar."
            call BlinkXP ("c16s005_070" , "d") from _call_BlinkXP_1875
            meg "Creo que es lógico. Amanda es la que es igual que tu hermana, ¿no? Tiene que ser difícil para tu madre. Y emotivo."
            mc "Lo es. Más emotivo que difícil. Para ella es como conocer a una hija con la que no ha tenido contacto nunca."
            call BlinkXP ("c16s005_075" , "d") from _call_BlinkXP_1876
            meg "Sobre lo de la habitación, creo que será mejor que no duerma contigo en su casa hasta que no hable con ella. Me quedaré con [sai] si a ella no le importa."
            mc "*Risa* No le importa, ya se lo he preguntado. Siempre le caíste bien. Y en mi habitación ibas a estar sola. Yo iba a dormir en algún sofá."
            mc "Creo que tenéis que hablar antes de que tú y yo podamos dormir juntos en casa."
        else:
            mc "No te preocupes, me gustas mucho y eso no va a cambiar."
            call BlinkXP ("c16s005_075" , "d") from _call_BlinkXP_1877
            meg "Creo que será mejor que no duerma contigo hasta que no hable con ella. Me quedaré con [sai] si a ella no le importa."
            mc "*Risa* No le importa, ya se lo he preguntado. Siempre le caíste bien. Y en mi habitación ibas a estar sola. Yo iba a dormir en algún sofá."
            mc "Creo que será bueno que os pongáis al día."
        if PregnancyTests:
            mc "Hay otro tema del que te quería hablar. ¿Has sentido algún tipo de molestias últimamente?"
            call BlinkXP ("c16s005_080" , "d") from _call_BlinkXP_1878
            meg "¿Qué tipo de molestias? No me digas que tienes herpes o alguna cosa así."
            mc "No, me refería a si... habías tenido algún síntoma de malestar, vómitos, pezones sensibles... esas cosas."
            call BlinkXP ("c16s005_085" , "d") from _call_BlinkXP_1879
            meg "¿Te preocupa haberme dejado embarazada?"
            mc "No, no me preocupa. Si estoy contigo y llega un crío no voy a tener ningún problema con ello. Pero..."
            "Le explicas a [meg] lo de los tests de embarazo. Su cara de sorpresa cuando acabas lo dice todo."
            call BlinkXP ("c16s005_090" , "d") from _call_BlinkXP_1880
            meg "Primero clones y ahora tests de embarazo sacados de una novela de ciencia ficción. ¿Estás seguro de que no me estás tomando el pelo?"
            mc "Segurísimo. Los tengo en mi habitación, por si quieres hacerlo."
            call BlinkXP ("c16s005_095" , "d") from _call_BlinkXP_1881
            meg "Lo haré. Ayer me levanté con el estómago revuelto, pero no vomité y hoy estaba bien. No tengo ningún otro síntoma, con lo que podría ser cualquier cosa que me sentara mal."
            meg "Pero ahora que has sacado el tema... es mejor asegurarnos, ¿no?"
            mc "Yo pienso lo mismo. Podemos hacerlo cuando lleguemos, así tendremos el resultado mañana."
        call BlinkXP ("c16s005_100" , "d") from _call_BlinkXP_1882
        meg "Genial. ¿Queda mucho para llegar a tu casa?"
        mc "Un par de minutos tan solo."
        meg "¿Puedes parar aquí un momento?"
        mc "¿Aquí?"
        meg "Sí. Y baja del coche."
        stop sound fadeout (1.5)
        call BlinkXP ("c16s005_105" , "f") from _call_BlinkXP_1883
        meg "Quiero besarte antes de llegar a tu casa."
        if mar._var("route"):
            meg "Creo que sería una falta de respeto hacerlo allí antes de hablar con tu madre."
        else:
            meg "Creo que sería una falta de respeto hacerlo allí antes de hablar con [sai]."
        mc "Nunca voy a rechazar un beso tuyo. Ven aquí"
        scene c16s005_110d with fade
        "Hace muchos días que no os habéis visto y las ganas de besaros se notan. El beso de la parada de autobús no ha sido suficiente para saciar el hambre que sentís el uno por el otro."
        call BlinkXP ("c16s005_110" , "d") from _call_BlinkXP_1884
        meg "Voy a echar de menos besarte."
        mc "Sobre eso... hay una costumbre especial en mi casa. *Risa* Todo el mundo me besa como saludo."
        call BlinkXP ("c16s005_115" , "d") from _call_BlinkXP_1885
        meg "¿Qué? ¿Incluso tu abuela?"
        mc "Bueno, todo empezó porque mi tía abuela quería tocarle los huevos a mi abuela. Al final todo el mundo que quiere me besa los buenos días y las buenas noches."
        mc "Nada que ver con como nos acabamos de besar, pero te lo digo para que no te sorprendas."
        call BlinkXP ("c16s005_120" , "d") from _call_BlinkXP_1886
        meg "Creo que voy a tardar en acostumbrarme a tu familia. *Risa* Sois muy raros..."
        mc "Yo prefiero decir especiales. ¿Vamos?"
    else:
        call BlinkXP ("c16s005_075" , "d") from _call_BlinkXP_1887
        meg "Creo que será mejor que no duerma contigo. Me quedaré con [sai] si a ella no le importa."
        mc "*Risa* No le importa, ya se lo he preguntado. Siempre le caíste bien. Y en mi habitación ibas a estar sola. Yo iba a dormir en algún sofá."
        mc "Lo de dormir en mi habitación no era ninguna proposición. *Risa*"
        call BlinkXP ("c16s005_100" , "d") from _call_BlinkXP_1888
        meg "Genial. ¿Queda mucho para llegar a tu casa?"
        mc "Un par de minutos tan solo."
    scene black with dissolve
    "Llegáis a casa y haces las presentaciones. Cuando [emm] se entera de que [meg] es cantante profesional, no puede evitar pedirle una canción."
    "Un minuto después ya está planeando una visita al Jazz Corner."
    if meg._var("route"):
        "Después de dejar su maleta en la habitación de [sai], subes con [meg] a tu habitación con la excusa de enseñarle la casa. Aprovecháis para extraer una gota de sangre y ponerla en el test de embarazo."
    "Poco rato después [meg] tiene que irse al Jazz Corner para la cena con sus compañeros."
    stop music fadeout (1.5)
    "Eva ya se ha ido después de quitar todas las cámaras de las habitaciones. Se ha despedido de todo el mundo antes de irse. ¿Le estará pillando el gusto a los abrazos?"
    return
label c16s006_MarPregnant:
    if _in_replay:
        call mrS3_nor_route from _call_mrS3_nor_route_28
        call mrS3_mar_pregnant from _call_mrS3_mar_pregnant_4
        menu:
            "¿Está [mar] embarazada?"
            "Sí":
                $ mar._var("pregnancyDiscovered" , True)
            "No":
                $ mar._var("pregnancyDiscovered" , False)
    play music ("music/Wonder.ogg")
    "Al poco rato, escuchas un zumbido en el armario donde tienes guardada la prueba de embarazo de [mar]. Debe significar que ya esta, ¿no? Pero aún faltan 28 minutos."
    "No te atreves a abrir el armario. Si ha acabado y las luces están encendidas sabrías el resultado. Quieres estar con [mar] cuando lo sepas."
    "Decides ir a buscarla. Es mejor esperar los 28 minutos con ella."
    "27 minutos."
    scene c16s006_005An with dissolve #abcdef Caminando por el rellano
    "La encuentras en la planta de las estudiantes, paseando de un lado a otro, visíblemente nerviosa."
    mc "¿Qué haces aquí, [mar.mc!t]?"
    call BlinkXP ("c16s006_010" , "d") from _call_BlinkXP_1889
    mom "Haciendo tiempo para que llegue la hora. No me puedo concentrar en la cocina. Por suerte, casi todo lo que necesito para la cena de Amanda ya está hecho o acabándose de hacer."
    mom "No quería subir a tu habitación para no contagiarte los nervios..."
    mc "Yo bajaba a buscarte... Acaba de zumbar el aparato."
    call BlinkXP ("c16s006_015" , "d") from _call_BlinkXP_1890
    mom "Pero aún faltan... 25 minutos..."
    mc "A lo mejor las 24 horas no son exactas. Sería raro que algo así tardara 24 horas justas."
    mc "¿Subimos a comprobarlo? Si aún no está, podemos esperar juntos."
    call BlinkXP ("c16s006_020" , "d") from _call_BlinkXP_1891
    mom "Sí, por favor. Los nervios me están consumiendo."
    scene black with dissolve
    "24 minutos."
    call BlinkXP ("c16s006_025" , "d") from _call_BlinkXP_1892
    mc "¿Preparada?"
    mom "¡Abre esa puñetera puerta de una vez!"
    scene c16s006_030c with dissolve
    "Abrir la puerta te cuesta un mundo. Cada centímetro es un paso más hacia la confirmación o la negación de que vas a ser padre. De que [mar] lleva un hijo tuyo dentro."
    stop music fadeout (1.5)
    if mar._var("pregnancyDiscovered"):
        $ mar._var("firstPregnancy", True) #RIAM don't track this variable
        scene c16s006_030a with vpunch
        play music ("music/Inspiring-Upbeat-Ambient.ogg")
        "Cada uno de esos centímetros ha valido la pena. La luz está verde."
        call BlinkXP ("c16s006_035" , "d") from _call_BlinkXP_1893
        mom "¡Sí! ¿Eso significa que...?"
        mc "¡Sí! ¡Estamos embarazados!"
        call BlinkXP ("c16s006_040" , "h") from _call_BlinkXP_1894 #abrazo
        mom "¡Sí! {b}¡Sí! ¡Genial!{/b}"
        mc "¿Contenta? ¡Yo no lo puedo estar más!"
        call BlinkXP ("c16s006_045" , "d") from _call_BlinkXP_1895
        mom "No te puedes imaginar cuánto."
        if persistent.family:
            mom "¡[emm] y tú vais a tener un hermano! Voy a ser la madre de los hijos del hombre más maravilloso del mundo."
            mc "*Risa* No le podré decir que falta el respeto a su padre si me llama Bro."
        else:
            mom "¡Por fin voy a ser madre! Y voy a ser la madre de los hijos del hombre más maravilloso del mundo."
            mc "Y si te sigo llamando Mamá... *Risa* No le podré decir que falta el respeto a su padre si me llama Bro."
            call BlinkXP ("c16s006_050" , "d") from _call_BlinkXP_1896
            mom "Nunca dejes de llamarme Mamá, por favor."
            mc "No pensaba hacerlo, Mamá. Además, ahora vas a serlo."
        call BlinkXP ("c16s006_055" , "d") from _call_BlinkXP_1897
        mom "Esa cosa no dice el género del niño, ¿verdad?"
        mc "No, creo que para eso aún quedan unas cuantas semanas. ¿Ya quieres pensar en nombres?"
        call BlinkXP ("c16s006_060" , "d") from _call_BlinkXP_1898
        if mc.name.name == "Luke":
            $ MarSon = "Lucas"
        else:
            $ MarSon = "Luke"
        mom "No, tan solo quiero saber si es Sharon o [MarSon]. *Risita*"
        mc "¿Sharon o [MarSon]? ¿Ya tienes escogidos los nombres?"
        mom "Hace tiempo que los tengo pensados. Solo espero que te gusten."
        mc "Prefiero Sharon a [MarSon]. Pero si sale niño, no le pienso llamar Sharon. *Risa*"
        call BlinkXP ("c16s006_065" , "d") from _call_BlinkXP_1899
        mom "Sabes que vas a ser un padre fantástico, ¿verdad?"
        mc "¿Los padres fantásticos están acojonados a la vez que contentos?"
        mom "Lo estan..."
        scene c16s006_070 with dissolve #arrodillado en la barriga
        mc "Hola Sharon o [MarSon]. ¡Yo soy tu padre! Siempre he querido decir esa frase. *Risa*"
        mom "¡Estás loco, [mc]! *Risa*"
        if persistent.family:
            mc "No hagas caso a Mamá. Ni a la tuya y a la mía. Es maravillosa, pero no tiene sentido del humor friki. Te tendré que educar yo en eso."
        else:
            mc "No hagas caso a Mamá. Es maravillosa, pero no tiene sentido del humor friki. Te tendré que educar yo en eso."
        mom "Vuelve aquí arriba. Quiero seguir abrazando al padre."
        call BlinkXP ("c16s006_040b" , "d") from _call_BlinkXP_1900 #abrazo
        "Os abrazáis durante un rato. Abrumados. Felices."
        "La mayoría del tiempo en silencio solo interrumpido por risas y besos. No hacen falta palabras para compartir cómo os sentís."
        "Hacéis planes sobre cuándo contárselo a la familia. Decidís dejar pasar los cumpleaños. Las chicas deben ser las protagonistas, no vuestro embarazo."
        if nor._var("route"):
            mc "Debería ir a ver a [nor]. Su test debe estar listo también."
            call BlinkXP ("c16s006_075" , "d") from _call_BlinkXP_1901
            mom "¡Oh, mierda! Me había olvidado de ella. Solo puedo pensar en Sharon ahora mismo."
            mc "¿Ya no es [MarSon]?"
            call BlinkXP ("c16s006_080" , "d") from _call_BlinkXP_1902
            mom "Prefiero una niña. Si [MarSon] llega no voy a tener ningún problema, pero prefiero que llegue Sharon."
            mom "Pero vete. [nor] tiene que estar tan nerviosa como estaba yo."
            call c16s006_FarewellMar from _call_c16s006_FarewellMar
            stop music fadeout (1.5)
        else:
            play sound ("music/RingtoneMC.ogg")
            "Al cabo de mucho rato de estar abrazados suena tu teléfono."
            stop sound
            stop music fadeout (1.5)
    else:
        scene c16s006_030b with vpunch
        play music ("music/Sad-Piano.ogg")
        "Cada uno de esos centímetros acaba en una pequeña decepción. La luz está roja."
        call BlinkXP ("c16s006_085" , "d") from _call_BlinkXP_1903
        mom "¡Oh, no! ¿Eso significa que...?"
        mc "Exacto, no estamos embarazados."
        call BlinkXP ("c16s006_090" , "h") from _call_BlinkXP_1904 #abrazo
        mom "Lo siento, [mc]."
        mc "¿Sentirlo? ¡No es culpa tuya!"
        call BlinkXP ("c16s006_095" , "d") from _call_BlinkXP_1905
        mom "No te puedes imaginar cuánto deseaba que saliera verde."
        if persistent.family:
            mom "Quería que [emm] y tú tuvierais un hermano! Quería ser la madre de los hijos del hombre más maravilloso del mundo."
        else:
            mom "Quería ser madre finalmente. Quería ser la madre de los hijos del hombre más maravilloso del mundo."
        mc "No pasa nada, mi amor. Lo seguiremos intentando."
        if emm._var("route"):
            mc "Además, este test sólo nos dice que no te quedaste embarazada la semana pasada. A lo mejor anoche lo conseguimos."
            call BlinkXP ("c16s006_055" , "d") from _call_BlinkXP_1906
            mom "¿Te imaginas que me hubieras dejado embarazada delante de [emm]?"
            mc "Ella lo pidió. *Risa* \"Déjala embarazada\" estuvo gritando al final."
        call BlinkXP ("c16s006_100" , "d") from _call_BlinkXP_1907
        mc "¿Habías pensado en algún nombre?"
        if mc.name.name == "Luke":
            $ MarSon = "Lucas"
        else:
            $ MarSon = "Luke"
        mom "Sí, Sharon si era niña o [MarSon] si era niño."
        mc "Me gustan. Prefiero que sea niña, pero si es niño, es tentador..."
        mc "\"Hola [MarSon]. ¡Yo soy tu padre!\" Siempre he querido decir esa frase. *Risa*"
        call BlinkXP ("c16s006_105" , "d") from _call_BlinkXP_1908
        mom "Sabes que vas a ser un padre fantástico, ¿verdad?"
        mc "Para eso tenemos que hacer más intentos."
        mom "Maravillosos intentos. No hay ninguna prisa. Sería mucha suerte que me hubieras dejado embarazada al primero."
        mom "Abrázame."
        call BlinkXP ("c16s006_090" , "d") from _call_BlinkXP_1909 #abrazo
        "Os abrazáis durante un rato. Tristes pero esperanzados. Decepcionados."
        "La mayoría del tiempo en silencio solo interrumpido por besos. No hacen falta palabras para compartir cómo os sentís."
        if nor._var("route"):
            mc "Debería ir a ver a [nor]. Su test debe estar listo también."
            call BlinkXP ("c16s006_075" , "d") from _call_BlinkXP_1910
            mom "¡Oh, mierda! Me había olvidado de ella. Soy una egoísta."
            mc "¿Egoísta? No. Nos hemos llevado una decepción, pero habrá más oportunidades."
            mc "¿Estás bien para quedarte sola? ¿Quieres venir?"
            call BlinkXP ("c16s006_080" , "d") from _call_BlinkXP_1911
            mom "Vete. [nor] tiene que estar tan nerviosa como estaba yo, y es algo que tenéis que hacer juntos y solos."
            mom "Ya lo celebraremos juntas si sale positivo, o planearemos un calendario para no dejarte descansar si sale negativo."
            call c16s006_FarewellMar from _call_c16s006_FarewellMar_1
            stop music fadeout (1.5)
        else:
            play sound ("music/RingtoneMC.ogg")
            "Al cabo de mucho rato de estar abrazados suena tu teléfono."
            stop music fadeout (1.5)
            stop sound
    return
label c16s006_FarewellMar:
    call KissXP ("c16s006_110" , "d") from _call_KissXP_58
    mc "Te veo luego. Te quiero."
    mom "Y yo te quiero a ti."
    return
label c16s007_NorPregnant:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_37
        if mar._var("route"):
            menu:
                "¿Está embarazada?"
                "Sí":
                    $ mar._var("pregnancyDiscovered" , True)
                "No":
                    $ mar._var("pregnancyDiscovered" , False)
        else:
            $ mar._var("pregnancyDiscovered" , False)
        call mrS3_nor_pregnant from _call_mrS3_nor_pregnant_4
    scene c16s007_005d with fade
    play music ("music/Wonder.ogg")
    "Llegas a la habitación de [nor] con los nervios a flor de piel. Aún quedan unos minutos para que se cumplan las 24 horas."
    if mar._var("route"):
        if mar._var("pregnancyDiscovered"):
            "Después de la alegría del test de [mar], tienes muchas ganas de saber el resultado del de [nor]."
        else:
            "Después de la decepción del test de [mar], tienes miedo de saber el resultado del de [nor]."
            "Te ha partido el alma ver cómo ha reaccionado ella. No quieres que [nor] pase por lo mismo. Maldito test..."
    "Hay que llamar a esa puerta. Subes la mano, nervioso."
    call BlinkXP ("c16s007_005" , "h") from _call_BlinkXP_1912
    "La puerta se abre antes de que llegues a tocarla. Una sorprendida [nor] está detrás."
    nor "Iba a buscarte. Esto acaba de pitar."
    mc "¿Te ibas a pasear por las dos casas con una caja en la que pone PregnaTron 2?"
    mc "Creía que lo ibas a mantener en secreto unos días al menos..."
    scene c16s007_010d with dissolve
    pause (0.5)
    call BlinkXP ("c16s007_010" , "d") from _call_BlinkXP_1943
    #scene c16s007_010AnBlink with dissolve #d-blink
    nor "¡Joder! ¡Ni lo he pensado! Ha pitado y lo he cogido para ir a buscarte... Aún quedan unos minutos para las 24 horas. Pasa..."
    if mar._var("route"):
        mc "El de [mar.mc!t] también ha pitado antes."
        call BlinkXP ("c16s007_015" , "d") from _call_BlinkXP_1913
        nor "¿Lo habéis mirado? ¿Qué ha salido? Las dos estábamos muy nerviosas..."
        if mar._var("pregnancyDiscovered"):
            mc "¡Positivo! ¡Vas a ser tía abuela!"
            call BlinkXP ("c16s007_020" , "d") from _call_BlinkXP_1914 #abrazo
            if persistent.family:
                nor "¡Felicidades! Me acabas de hacer sentir vieja, pero felicidades, mi amor. Luego hablaré con [mar]. También voy a ser tía."
            else:
                nor "¡Felicidades! Al menos no lo seré legalmente, si no, me hubieras hecho sentir muy vieja. *Risa* Pero felicidades, mi amor. Luego hablaré con [mar]."
            mc "Gracias, mi vida. Vamos a ver el tuyo, a ver si repetimos resultado."
        else:
            mc "Negativo... [mar] estaba muy decepcionada."
            call BlinkXP ("c16s007_025" , "d") from _call_BlinkXP_1915 #abrazo
            nor "Lo siento mucho, mi amor. Sé que tanto ella como tú estabais muy ilusionados."
            mc "Sí, pero no todo puede salir bien a la primera. Habrá más oportunidades."
            mc "Vamos a ver el tuyo, a ver si tenemos más suerte."
    else:
        mc "He venido antes porque no me aguantaba los nervios. Prefería esperar aquí contigo."
    call BlinkXP ("c16s007_030" , "d") from _call_BlinkXP_1916
    nor "¿Lo quieres abrir tú o lo abro yo? Tenía que haber tirado la caja. Ahora ya sabríamos lo que es."
    mc "Y lo hubieras sabido sin mí, en el momento en que ha pitado."
    call BlinkXP ("c16s007_035" , "d") from _call_BlinkXP_1917
    nor "Tienes razón... ¿lo abro?"
    mc "Ábrelo. Me estoy empezando a poner nervioso..."
    call BlinkXP ("c16s007_040" , "d") from _call_BlinkXP_1918
    if mar._var("route") and not mar._var("pregnancyDiscovered"):
        nor "Después del resultado de [mar], tengo aún más miedo. ¿Y si el nuestro sale negativo también?"
    elif mar._var("pregnancyDiscovered"):
        nor "Después del resultado de [mar], tengo aún más miedo. ¿Y si el nuestro sale negativo?"
    else:
        nor "Tengo miedo. ¿Y si sale negativo?"
    mc "Habrá más oportunidades. No creerás que voy a dejar de hacerte el amor porque salga negativo el primer test que hacemos que nos puede dar una respuesta fiable, ¿no?"
    call BlinkXP ("c16s007_045" , "d") from _call_BlinkXP_1919
    nor "Espero que no dejes de hacerme el amor nunca, mi vida. Salga positivo o negativo."
    stop music fadeout (1.5)
    mc "No lo hare, mi amor. Pero, por lo que más quieras, ¡ábrelo ya!"
    if nor._var("pregnant"):
        play music ("music/Inspiring-Upbeat-Ambient.ogg")
        $ nor._var("pregnancyDiscovered", True)
        scene c16s007_050a with dissolve
        nor "¡Verde! ¿Eso es un sí? ¿Estoy embarazada?"
        mc "Sí, mi amor. ¡Estamos embarazados!"
        scene c16s007_055d with hpunch
        "[nor] se lanza encima tuyo y te da un beso lleno de alegría y alivio a partes iguales."
        call BlinkXP ("c16s007_055" , "d") from _call_BlinkXP_1920
        nor "¡Felicidades, Papá!"
        mc "¡Felicidades, Mamá! ¿Contenta?"
        call BlinkXP ("c16s007_060" , "d") from _call_BlinkXP_1921
        nor "Contenta, feliz, aliviada, entusiasmada, ilusionada... ¿Y tú?"
        mc "Lo mismo y un poco más. *Risa*"
        if persistent.family:
            call BlinkXP ("c16s007_065" , "d") from _call_BlinkXP_1922
            nor "No quiero sonar como una mala madre, pero las gemelas llegaron... por accidente. Ni Mike ni yo queríamos tener hijos en ese momento."
            call c16s007_Twins from _call_c16s007_Twins
            call BlinkXP ("c16s007_070" , "d") from _call_BlinkXP_1923
            nor "Cuando aquel test salió positivo fue algo inesperado. Este positivo ha sido deseado. Muy deseado. Estoy muy feliz ahora mismo."
            nor "A mi edad no pensaba que fuera a volverme a pasar suceder nunca..."
        else:
            call BlinkXP ("c16s007_065" , "d") from _call_BlinkXP_1924
            nor "No quiero sonar como una mala madre, pero las gemelas llegaron... de una forma diferente."
            call c16s007_Twins from _call_c16s007_Twins_1
            call BlinkXP ("c16s007_070" , "d") from _call_BlinkXP_1925
            nor "Cuando llegaron a mi vida me enamoré de ellas inmediatamente. Pero con este test... me ha pasado lo mismo. ¡Voy a ser madre! ¡Estoy embarazada!"
            mc "Ya eres madre, mi amor. Ahora tan solo vas a tener que pasar por el embarazo."
            call BlinkXP ("c16s007_075" , "d") from _call_BlinkXP_1926
            nor "Ya sabes a lo que me refiero. A mi edad no pensaba que fuera a suceder nunca..."
        mc "Pues ha pasado. Ahora solo hay que cuidarte y mimarte. Espero no volver a verte acarrear dos neveras de camping nunca más. Pide ayuda."
        call BlinkXP ("c16s007_080" , "d") from _call_BlinkXP_1927
        nor "No lo volveré a hacer, no te preocupes. El problema va a ser el vino... con mi madre y Betty aquí..."
        mc "¿El vino? ¿Necesitas vino para estar con ellas? Se están portando... relativamente bien."
        call BlinkXP ("c16s007_085" , "d") from _call_BlinkXP_1928
        nor "¡No! ¡No me refiero a eso! *Risa* Ahora que sé que estoy embarazada, no voy a beber vino, y van a sospechar. Especialmente Betty."
        nor "El otro día en la playa se sorprendieron del cava sin alcohol. Pero tenía la excusa de que así las chicas podían brindar. Si compramos también vino sin alcohol..."
        mc "Puedes decir que el alcohol te está haciendo ganar un poco de peso. Realmente vas a ganar peso. *Risa*"
        call BlinkXP ("c16s007_090a" , "d") from _call_BlinkXP_1929
        nor "¿Te voy a tener que llamar Mr. Alcohol? *Risa* Puedes resultar igual de adictivo."
        mc "Puedes llamarme como quieras, mi amor."
        call BlinkXP ("c16s007_090b" , "d") from _call_BlinkXP_1930
    else:
        scene c16s007_050b with dissolve
        play music "music/Sad-Piano.ogg"
        nor "¡Rojo! Eso es un no, ¿verdad?"
        mc "Sí, mi amor. No hemos tenido suerte."
        call BlinkXP ("c16s007_095" , "d") from _call_BlinkXP_1931
        nor "Bueno, me lo imaginaba... a mi edad no es fácil quedarse embarazada..."
        mc "¿A tu edad? [nor], aún eres joven, creo que tan solo tenemos que intentarlo más."
        call BlinkXP ("c16s007_100" , "d") from _call_BlinkXP_1932
        nor "No, [mc], a mi edad se considera difícil, y aunque me quedara embarazada sería un embarazo de riesgo."
        nor "Estaba muy ilusionada con este test, pero..."
        if persistent.family:
            nor "No quiero sonar como una mala madre, pero las gemelas llegaron... por accidente. Ni Mike ni yo queríamos tener hijos en ese momento."
            call c16s007_Twins2 from _call_c16s007_Twins2
            call BlinkXP ("c16s007_105" , "d") from _call_BlinkXP_1933
            nor "Cuando aquel test salió positivo fue algo inesperado. Pero deseaba que este también saliera positivo... lo deseaba mucho. Un bebe tuyo y mío."
            nor "A mi edad estaba segura de que no iba a volver a pasarme... y no me he equivocado."
        else:
            nor "No quiero sonar como una mala madre, pero las gemelas llegaron... de una forma diferente."
            call c16s007_Twins2 from _call_c16s007_Twins2_1
            call BlinkXP ("c16s007_105" , "d") from _call_BlinkXP_1934
            nor "Cuando llegaron a mi vida me enamoré de ellas inmediatamente. Pero deseaba que este saliera positivo... deseaba volver a enamorarme de un bebé. De un bebe tuyo y mío. Ser madre."
            mc "Ya eres madre, mi amor. Ahora tan solo tenemos que seguir intentándolo para que tengas que pasar por el embarazo."
            call BlinkXP ("c16s007_110" , "d") from _call_BlinkXP_1935
            nor "Ya sabes a lo que me refiero. A mi edad no pensaba que fuera a suceder nunca... y no me he equivocado."
        mc "De momento no te has equivocado, pero voy a hacer todo lo posible para que te equivoques."
        call BlinkXP ("c16s007_115" , "d") from _call_BlinkXP_1936
    nor "¿Puedes abrazarme?"
    mc "Por supuesto. Ven aquí."
    if nor._var("pregnancyDiscovered"):
        call BlinkXP ("c16s007_120a" , "d") from _call_BlinkXP_1937 #contenta
    else:
        call BlinkXP ("c16s007_120b" , "d") from _call_BlinkXP_1938 #triste
    "Os abrazáis unos momentos en silencio. No hace falta decir nada. Las emociones son compartidas en ese instante."
    if not nor._var("pregnancyDiscovered"):
        call BlinkXP ("c16s007_125" , "d") from _call_BlinkXP_1939
        nor "Me acabo de dar cuenta de que soy una egoísta."
        mc "¿Qué? ¿Por qué?"
        nor "Te he explicado cómo me ha hecho sentir que salga negativo... pero no he tenido la decencia de preguntarte cómo te sientes tú."
        mc "Un poco decepcionado. Y triste."
        mc "Pero no por mí. Sino por cómo estás tú. No me gusta verte triste. Y antes de que lo intentes, aún me gustaría menos que fingieras no estarlo."
        mc "Prefiero compartir tu tristeza a no saber de ella."
        call BlinkXP ("c16s007_130" , "d") from _call_BlinkXP_1940
        nor "¿Entiendes ahora por qué me he enamorado de ti?"
    play sound ("music/RingtoneMC.ogg")
    "En ese momento suena tu teléfono. Ni siquiera un momento de tranquilidad en esta familia."
    stop music fadeout (1.5)
    stop sound
    return
label c16s007_Twins:
    nor "Me alegra muchísimo de que pasara. Son lo mejor que me ha sucedido en mi vida. No te ofendas..."
    if mar._var("pregnancyDiscovered"):
        mc "No me ofendo. Ahora que tengo dos hijos en camino, entiendo perfectamente a lo que te refieres."
    else:
        mc "No me ofendo. Ahora que tengo un hijo en camino, entiendo perfectamente a lo que te refieres."
    return
label c16s007_Twins2:
    nor "Me alegra muchísimo de que pasara. Son lo mejor que me ha sucedido en mi vida. No te ofendas..."
    mc "No me ofendo. Sabiendo lo que sentía al pensar en ese test, entiendo perfectamente a lo que te refieres."
    return
label c16s008_DinnerWithAmanda:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_38
        call mrS3_nor_route from _call_mrS3_nor_route_29
    if nor._var("route"):
        scene c16s008_005a with dissolve
    elif mar._var("route"):
        scene c16s008_005b with dissolve
    else:
        scene c16s008_005c with dissolve
    mc "Dime, Amanda."
    ama "Siento molestarte, pero necesito tu ayuda."
    mc "¿Qué puedo hacer por ti?"
    ama "He pinchado una rueda de la furgoneta y vestida así no puedo conducir la moto de Eva. ¿Puedes venir a buscarme?"
    mc "Ningún problema ¿Dónde estás? Voy a buscarte."
    ama "Te mando las coordenadas GPS..."
    mc "¿Amanda?"
    ama "Gracias, [mc]."
    if nor._var("route"):
        call KissXP ("c16s008_010" , "d") from _call_KissXP_59
        mc "Amanda ha tenido una avería y tengo que ir a buscarla."
        nor "Ve a por ella. No podemos tener una cena sin nuestra invitada."
        mc "Te quiero. Te veo luego."
        nor "Yo también te quiero."
    elif mar._var("route"):
        call BlinkXP ("c16s008_015" , "d") from _call_BlinkXP_1941
        mc "Amanda ha tenido una avería y tengo que ir a buscarla."
        mom "Ve a por ella. No podemos tener una cena sin nuestra invitada."
        call c16s006_FarewellMar from _call_c16s006_FarewellMar_2
    scene black with dissolve
    $renpy.sound.play("music/Motor.ogg", loop=True)
    "Antes de sacar el coche del garaje piensas que si el dormitorio y NTR no funcionan, te podrías ganar la vida como taxista."
    "Conduces hasta las coordenadas que te ha proporcionado Amanda. Tienes que conducir por un camino sin asfaltar que se interna en el bosque entre tu casa y la ciudad."
    mcp "(Parece que por fin voy a saber dónde está la base secreta.)"
    mcp "(Eso acaba de sonar a película de espías. [meg] tenía razón.)"
    scene c16s008_020e with dissolve
    "Por fin llegas a las coordenadas. Puedes ver la furgoneta y la vieja hacienda abandonada."
    "De crío venías aquí a jugar muchas veces. Estaba abandonada. Era como la casa encantada del bosque."
    stop sound fadeout (1.5)
    "Sigue pareciendo abandonada, pero ahora sabes que no lo está."
    scene c16s008_020f with dissolve
    play sound ("music/Car-Horn.ogg")
    "Bajas del coche tras tocar el claxon."
    mc "*Gritando* ¡Amanda! Ya estoy aquí."
    scene c16s008_020d with dissolve:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP("c16s008_020" , "d") from _call_BlinkXP_1942
    ama "Lo sé. Gracias por venir a buscarme."
    return

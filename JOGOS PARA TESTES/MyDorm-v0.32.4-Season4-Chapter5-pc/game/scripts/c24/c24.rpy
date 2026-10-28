label c24:
    call c23s000_DiscoveredPregnancies from _call_c23s000_DiscoveredPregnancies_4
    if bet._var("route"):
        call c24s001_Bet from _call_c24s001_Bet
        call c24s002_Breakfast from _call_c24s002_Breakfast
    else:
        call c24s001_NoBetSex from _call_c24s001_NoBetSex
    call c24s002_Meanwhile_Kim_Mar_Kat from _call_c24s002_Meanwhile_Kim_Mar_Kat
    call c24s002_BetNoNun from _call_c24s002_BetNoNun
    call c24s003_Mar from _call_c24s003_Mar
    if kia._var("route"):
        call c24s003_KiaDate from _call_c24s003_KiaDate
        call c24s004_Eri_Dap_Kat_Nor from _call_c24s004_Eri_Dap_Kat_Nor
        call c24s003_KiaSex from _call_c24s003_KiaSex
    else:
        call c24s003_NoKia from _call_c24s003_NoKia
        call c24s004_Eri_Dap_Kat_Nor from _call_c24s004_Eri_Dap_Kat_Nor_1
    #Day Change
    call c24s004_Deb_Sim from _call_c24s004_Deb_Sim
    call c24s004_Mad_Lis_Emm from _call_c24s004_Mad_Lis_Emm
    call c24s004_Kim_Mee_Meg from _call_c24s004_Kim_Mee_Meg
    call c24s005_Ama from _call_c24s005_Ama
    call c24s005_Eva from _call_c24s005_Eva
    return
    call eoc from _call_eoc23
    jump c24


label c24s001_Bet:
    if _in_replay:
        call mrS3_sca_route from _call_mrS3_sca_route_5
        call mrS3_oma_route from _call_mrS3_oma_route_3
        call mrS3_mee_route from _call_mrS3_mee_route_3
        call c23s007_End from _call_c23s007_End_1
    call BlinkXPS3 ("c23s007_190" , "d") from _call_BlinkXPS3_1539
    play music ("music/OneLastChance.ogg")
    mc "Pues sí, creo que nos ha oído."
    mc "¿Vas a dormir con eso?"
    call BlinkXPS3 ("c24s001_005" , "d") from _call_BlinkXPS3_1540
    bet "No he dormido con un sujetador en mi vida... Esto tiene que ser super incómodo."
    mc "Te puedo dejar la camiseta que me iba a poner mañana, si quieres."
    call BlinkXPS3 ("c24s001_010" , "d") from _call_BlinkXPS3_1541
    bet "Sí, por favor..."
    mc "Aunque también podrías dormir sin el sujetador. No voy a ver nada que no haya visto en la piscina..."
    mc "O en la cocina, durante la partida de DnD."
    call BlinkXPS3 ("c24s001_015" , "d") from _call_BlinkXPS3_1542
    bet "¡[mc]! ¡Es diferente!"
    bet "No íbamos a compartir cama y no habíamos tenido la conversación que hemos tenido esta mañana en el coche."
    mc "No te preocupes, te presto mi camiseta."
    mc "De todas formas, no iba a pasar nada. Te dije que podríamos tener una oportunidad de estar juntos si no eras monja. Y aún lo eres."
    call BlinkXPS3 ("c24s001_020" , "d") from _call_BlinkXPS3_1543
    bet "Lo sé..."
    bet "Dame esa camiseta, por favor."
    mc "Se la presté a [eil] el día que llegó a casa y me parece que ha dado el cuello de sí un poco..."
    scene c23s007_185b with fade
    bet "*Desde el lavabo* ¿En serio? ¿No tenías otra camiseta?"
    mc "*Risa* Lo sé, casi parece hecho a propósito."
    bet "*Desde el lavabo* ¿Estás seguro de que esto no es un plan tuyo y de [emm]?"
    mc "*Risa* No podía haber planeado algo así antes de la conversación de esta mañana."
    mc "[emm] ha tenido tiempo de planearlo si ha fingido estar dormida, pero lo de la camiseta es casualidad. *Risa* Me la regaló Jam hace años."
    mc "Y antes de que preguntes, me gustaría recuperarla. Es un préstamo."
    scene c24s001_025d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c24s001_025" , "d") from _call_BlinkXPS3_1544
    bet "Al menos es grande. No creo que entrase en una camiseta tuya de ahora. Pero es cortísima..."
    mc "No voy a ver nada que no haya visto hace cinco minutos. *Risa* Porque sigues llevando las bragas, ¿verdad?"
    call BlinkXPS3 ("c24s001_030" , "d") from _call_BlinkXPS3_1545
    bet "¡Claro que sigo llevándolas!"
    mc "Sólo bromeaba, Tía [bet]. Vamos a la cama; se está haciendo tarde."
    scene c24s001_030d with fade
    "Tras apagar las luces..."
    mc "Buenas noches, Tía [bet]."
    bet "Buenas noches, [mc]."
    if sca._var("route"):
        "Intentas dormir sin éxito. Te preocupa moverte en sueños y que tu mano acabe en el mismo sitio que acabó con [sca]. Salvando las diferencias de tamaño."
    else:
        "Intentas dormir sin éxito. Te preocupa moverte en sueños y hacer algo que incomode a Tía [bet]."
    "Al cabo de un rato..."
    bet "*Susurrando* ¿Estás dormido?"
    mc "No, no puedo dormir. ¿Tú tampoco?"
    call BlinkXPS3 ("c24s001_035" , "d") from _call_BlinkXPS3_1546
    bet "No, estaba pensando en todo lo que ha pasado hoy..."
    mc "¿Quieres hablarlo?"
    bet "No, no quiero que pierdas horas de sueño. Intenta dormir."
    mc "No voy a poder. Voy a encender la luz."
    call BlinkXPS3 ("c24s001_040" , "f") from _call_BlinkXPS3_1547
    mc "Sé que es tontería preguntarte qué te preocupa, pero no tienes que tomar la decisión hoy. Tienes dos meses para pensarlo."
    bet "Esa decisión ya la he tomado. No voy a entrar en un convento de clausura ni me voy a ir a Latinoamérica."
    bet "Las dos cosas significarían perder a la familia, y no estoy dispuesta a ello."
    mc "Bueno, volver a África, que era tu plan inicial, también hubiera significado que no nos verías..."
    call BlinkXPS3 ("c24s001_045" , "d") from _call_BlinkXPS3_1548
    bet "Es diferente. De allí podría volver una o dos veces al año para veros. De un convento en Perú, no."
    mc "Tienes razón, no lo había pensado así. Para mí sería casi igual de duro que te fueras a Perú que a... no sé... un país de África que no fuera Tanzania."
    mc "Me he acostumbrado a verte todos los días, y sería difícil si te tuvieras que ir."
    call BlinkXPS3 ("c24s001_050" , "d") from _call_BlinkXPS3_1549
    bet "Por eso te digo que la decisión está tomada. Por lo que a mí respecta, he dejado de ser monja hace horas, aunque deje de serlo oficialmente en unos meses."
    mc "Si tienes la decisión tomada, ¿por qué no hacerlo oficial mañana cuando vayas a por la documentación de los conventos?"
    mc "Supongo que la iglesia pensará que tomarás la decisión entre las dos opciones que te han propuesto, no una tercera opción."
    mc "No sé si tendrán que preparar algún papel para que te des de baja, o como se diga."
    call BlinkXPS3 ("c24s001_055" , "d") from _call_BlinkXPS3_1550
    bet "Tienes razón... sería una forma de cerrar todo este asunto, al menos hasta que firme los papeles que seguro que me harán firmar."
    mc "Genial. Un tema resuelto. Supongo que lo otro a lo que le estabas dando vueltas era a lo de la certificación, pero eso ya ha quedado resuelto."
    call BlinkXPS3 ("c24s001_060" , "d") from _call_BlinkXPS3_1551
    bet "Me preocupa ponerme a estudiar a mi edad, y empezar a buscar trabajo... Soy una anciana a punto de retirarse, al fin y al cabo."
    mc "Eres una mujer con un montón de experiencia. Creo que eso también lo valorarán. ¿Alguna cosa más que te preocupe?"
    stop music fadeout (1.5)
    call BlinkXPS3 ("c24s001_065a" , "d") from _call_BlinkXPS3_1552
    bet "Lo que has dicho antes."
    mc "¿Qué he dicho?"
    play music ("music/SensualJazzMedium2.ogg")
    call BlinkXPS3 ("c24s001_065b" , "d") from _call_BlinkXPS3_1553
    bet "Lo de que podríamos tener una oportunidad de estar juntos si no era monja. Y que aún lo era. Aunque solo sea oficialmente..."
    mc "¿Y qué te preocupa sobre eso?"
    call BlinkXPS3 ("c24s001_070" , "d") from _call_BlinkXPS3_1554
    bet "Hace 40 años que no estoy con nadie... Ya no sé qué hacer o cómo hacerlo. Y no me refiero al sexo... me refiero... a esa oportunidad de la que hablabas."
    mc "Eso es muy fácil. Se habla todo. Cualquier duda que tengas sobre lo que debes o no debes hacer, solo tienes que hablarlo conmigo."
    scene c24s001_075An with dissolve
    mc "Por ejemplo, yo podría preguntar si puedo hacer esto ahora que sólo eres monja oficialmente pero ya no te consideras una."
    mc "Y tú podrías contestar sí o no, o no contestar y dejarme seguir."
    bet "O podría preguntar qué pretendes con eso..."
    mc "Podrías, pero... ¿lo estás preguntando?"
    call BlinkXPS3 ("c24s001_080" , "d") from _call_BlinkXPS3_1555
    bet "No..."
    mc "Yo tampoco he preguntado si puedo..."
    bet "Pero puedes..."
    mc "Y si te dijera que quiero recuperar mi camiseta, ¿cuál sería tu respuesta?"
    call BlinkXPS3 ("c24s001_085" , "d") from _call_BlinkXPS3_1556
    bet "*Risa* Que te la tendré que devolver porque me la has prestado mientras aún era monja..."
    if sca._var("route"):
        bet "[sca] te enseño cómo funciona esto cuando le prestas ropa a tu pareja, ¿no? Eso no ha cambiado desde mi época."
    else:
        bet "Ya sabes cómo funciona esto cuando le prestas ropa a tu pareja, ¿no? Eso no ha cambiado desde mi época."
    mc "*Risa* Creo que gastaré mucho en ropa entonces. Pero de momento, quiero mi camiseta."
    call BlinkXPS3 ("c24s001_090" , "d") from _call_BlinkXPS3_1557
    if persistent.family:
        bet "*Conteniendo la risa mientras finge sorpresa* ¡[mc]! ¿Quieres verle las tetas a tu Tía Abuela?"
    else:
        bet "*Conteniendo la risa mientras finge sorpresa* ¡[mc]! ¿Quieres verle las tetas a una anciana exmonja?"
    mc "No solo verlas. Aunque no me canse de verlas, hoy quiero hacer más que solo mirarlas."
    scene c24s001_095AnBlink with dissolve
    bet "¿Mejor así, entonces?"
    mc "Mucho mejor... pero antes de continuar quiero preguntarte si estás realmente segura de esto."
    mc "Aún eres oficialmente una monja y no me gustaría que por la mañana te sintieras mal por lo que pase ahora."
    call BlinkXPS3 ("c24s001_100" , "d") from _call_BlinkXPS3_1558
    bet "Estoy segurísima, no te preocupes. No me voy a volver a poner el hábito nunca más."
    mc "En ese caso, creo que necesito acariciarte. *Risa* Y eliminar la camiseta de la ecuación."
    bet "En ese caso, creo que estoy de acuerdo en devolverte la camiseta. Por esta vez."
    call BlinkXPS3 ("c24s001_105" , "f") from _call_BlinkXPS3_1559
    bet "¿Así o quieres que me desnude del todo?"
    mc "Querré, pero todo a su tiempo. Ahora es el momento de entregar las caricias prometidas."
    mc "Túmbate, por favor, quiero disfrutar de ese cuerpo como es debido."
    call BlinkXPS3 ("c24s001_110" , "f") from _call_BlinkXPS3_1560
    bet "¿Así va bien?"
    mc "Así estás perfecta. Y super sexy."
    bet "Que me llames sexy a mi edad..."
    mc "Eres muy sexy, [bet]."
    scene c24s001_115An with dissolve
    "Empiezas a besar la parte interior de su brazo, esperando que no tenga cosquillas."
    bet "¿Ya no soy Tía [bet]?"
    mc "*Smooch* A menos que tengas un fetiche con el incesto, prefiero llamarte solo [bet]."
    mc "*Smooch* Pero como tú quieras."
    bet "[bet] está bien... *Gemido* Ya tendremos tiempo de hablar de fetiches..."
    scene c24s001_120An with dissolve
    "Saltas de su brazo a su pecho, evitando que tus labios toquen su pezón. Quieres que la excitación debida a la anticipación vaya creciendo en ella."
    bet "Me encanta lo que me haces con la barba en el pezón... *Gemido* Son como mil dedos tocándolo a la vez."
    "Al esquivar su pezón, lo has rozado suavemente con tu barbilla. Ahora no puedes dejar de hacerlo."
    mc "*Smooch* Cualquier cosa por mi exmonja favorita."
    scene c24s001_125An with dissolve
    "Tus labios empiezan a bajar por su estómago, más firme de lo que parece a simple vista, repartiendo besos por el camino."
    bet "*Gemido* Sabes que no hace falta que me pongas cachonda, ¿verdad?"
    mc "*Smooch* No es solo por eso. Nunca más vamos a tener nuestra primera vez juntos, y quiero disfrutarla."
    "Y quieres ponerla cachonda."
    scene c24s001_130 with dissolve
    mc "Tengo mucha [bet] que disfrutar y me faltan manos y labios para hacerlo todo a la vez."
    bet "*Gemido* Eres malvado... cada vez que parece que vas a atacar un pezón, lo rodeas..."
    scene c24s001_135An with dissolve
    "Crees que ya ha llegado el momento de asaltar el primero de sus tesoros."
    mc "*Smooch* ¿Malvado yo? Lo estaba reservando para este momento."
    bet "*Jadeo* Están muy sensibles. Me has puesto muy cachonda. Más de lo que he estado en años..."
    call BlinkXPS3 ("c24s001_140" , "d") from _call_BlinkXPS3_1561
    mc "¿Preparada para que siga bajando?"
    bet "Preparada y ansiosa..."
    scene c24s001_145An with dissolve
    "Empiezas a descender por su costado hasta sus piernas, aumentando aún más su excitación."
    "Por una vez dejas las manos quietas. Quieres que se centre en tus labios."
    bet "*Gemido* Me encantan esos besos..."
    call BlinkXPS3 ("c24s001_150" , "d") from _call_BlinkXPS3_1562
    "Por fin te sitúas encima de sus piernas. Llega el momento de la verdad."
    mc "Última oportunidad para echarte atrás, [bet]."
    bet "No te preocupes; no pienso hacerlo. Sólo queda pendiente nuestra ropa interior, y la mía casi me está quemando."
    mc "Eso no lo podemos consentir, ¿no?"
    scene c24s001_155An with dissolve
    call addProfileImageS3 (8, "betty_8", bet, _(": 15 - Especial"), "") from _call_addProfileImageS3_6
    "Retiras sus bragas en un movimiento suave mientras el olor que revela cuan cachonda está asalta tus fosas nasales."
    mc "Alguien esperaba visita. Me lo imaginaba salvaje y natural."
    if oma._var("route"):
        bet "*Risa* Hace años que lo llevo así. Los 70 quedaron atrás y es más cómodo así. Ya tuve mi época [oma]."
    else:
        bet "*Risa* Hace años que lo llevo así. Los 70 quedaron atrás y es más cómodo así."
    mc "Dame un momento para quitarme los boxers,"
    call BlinkXPS3 ("c24s001_160" , "d") from _call_BlinkXPS3_1563
    bet "¿No me vas a dejar verlo? ¿O es una sorpresa?"
    mc "No tengo nada que esconder."
    scene c24s001_160d with dissolve
    bet "¡Ni nada de lo que avergonzarte! ¡Es enorme!"
    if oma._var("route"):
        bet "(No parecía tan grande en el jacuzzi cuando estaba con [oma]. La distancia debió engañarme.)"
    mc "No es el tamaño lo que importa, [bet]."
    bet "Eso lo suelen decir los que la tienen pequeña. *Risa* No les falta razón, pero se hace extraño que lo digas tú con eso entre las piernas."
    scene c24s001_165a with dissolve
    mc "Hablando de piernas, creo que es hora de que pruebe lo que hay entre las tuyas."
    bet "Creía que me iba a morir de anticipación antes de que llegaras ahí."
    scene c24s001_165An with dissolve
    "Cuando hundes tu lengua en su coño puedes notar su intenso sabor."
    bet "*GEMIDO* ¡Joder! *JADEO*"
    "La reacción de [bet] te toma por sorpresa, aprisionándote entre sus piernas. Vas a necesitar un cuello de recambio."
    bet "¡No pares ahora!"
    scene c24s001_175pv with dissolve
    show c24s001_170v
    "Empiezas a jugar con tu lengua en sus labios. Su coño está prácticamente tan húmedo como tu lengua."
    bet "*Gemido* ¡Por el amor de Dios, [mc]! *Jadeo*"
    "Su duro clítoris se muestra sensible a cada una de tus caricias, produciendo un escalofrío en todo su cuerpo."
    bet "*Jadeo* ¿Dónde has aprendido a hacer eso? *Gemido*"
    "Casi se te escapa la risa. Vas aprendiendo poco a poco, tal como su cuerpo te va diciendo qué es lo que le gusta."
    scene c24s001_170pv with dissolve
    show c24s001_175v
    hide c24s001_170v
    "Y le gusta casi todo lo que haces."
    bet "*Gemido* Si sigues así, me voy a correr en seguida. *Jadeo*"
    "Casi es música para tus oídos escucharla decir eso."
    mcp "(Ese era el plan, ¿no? *Risa mental*)"
    "Pero [bet] tiene otros planes."
    call BlinkXPS3 ("c24s001_180" , "d") from _call_BlinkXPS3_1564
    bet "*Jadeo* Para por favor, [mc]."
    mc "¿Hay algo que no te esté gustando?"
    bet "Justo lo contrario. Pero no quiero correrme así. Ni aún."
    bet "Necesito un momento de descanso."
    mc "Ningún problema. Ponte de costado."
    scene c24s001_180d with dissolve
    bet "¿Así? ¿Qué vas a hacer?"
    mc "Darte un momento de descanso. Pero sigue habiendo mucha [bet] que recorrer y estudiar."
    scene c24s001_185An with dissolve
    "Empiezas a darle besos en la espalda, tal como has hecho anteriormente por su parte de delante."
    bet "*Gemido* Eso no me va a dar ningún descanso, [mc]. *Jadeo*"
    mc "*Smooch* Pero ¿te gusta?"
    bet "*Jadeo* Me encanta. *Gemido*"
    scene c24s001_190An with dissolve
    "Empiezas a bajar por su espalda hasta el lugar donde pierde su nombre."
    bet "*Gemido* ¿Eres hombre de culos o de tetas? *Jadeo*"
    "Pregunta curiosa cuando es una mujer que va tan bien surtida de ambas cosas."
    mc "¿Por qué no los dos?"
    scene c24s001_190d with hpunch
    "No puedes resistirte a darle un mordisco en su enorme cachete."
    bet "*Jadeo* ¡Ouch!"
    mc "¿Te he hecho daño?"
    bet "No, pero eso ha hecho que acabe el descanso. Te necesito dentro de mí."
    stop music fadeout (1.5)
    scene c24s001_195 with dissolve
    "Te acoplas a su espalda, introduciendo a Mjolnir entre sus piernas. Quieres que se acostumbre a sentirlo antes de penetrarla."
    play music ("music/Sexy-Background-Music.ogg")
    bet "Se veía grande, pero se siente enorme."
    mc "Podemos esperar todo lo que quieras, [bet]."
    call BlinkXPS3 ("c24s001_200" , "d") from _call_BlinkXPS3_1565
    bet "Creo que he esperado mucho ya. 40 años. Va a ser casi como si volviera a perder la virginidad."
    mc "*Risa* Dicen que es como montar en bicicleta. Que nunca se olvida."
    bet "Habrá que comprobarlo. *Risa* Lo que noto entre las piernas no es una herramienta para principiantes."
    mc "Si no fuera así, con tu culo en medio, dudo que pudiera llegar. *Risa*"
    call BlinkXPS3 ("c24s001_205" , "d") from _call_BlinkXPS3_1566
    bet "¿Acabas de decir que tengo el culo gordo?"
    mc "*Risa* No. Acabo de decir que tienes un precioso y enorme culo."
    mc "Un culo que me encanta."
    call BlinkXPS3 ("c24s001_210" , "d") from _call_BlinkXPS3_1567
    "La antigua monja abre un poco sus piernas para dejarte vía libre."
    bet "Cuidado con las telarañas. Hace mucho que no se usa."
    scene c24s001_215pv
    show c24s001_215va
    hide c24s001_175v
    pause (1.3)
    scene c24s001_215mv
    if persistent.family:
        "Penetras a tu tía abuela suavemente, justo lo suficiente como para que entre tu glande. Es muy estrecha."
    else:
        "Penetras a [bet] suavemente, justo lo suficiente como para que entre tu glande. Es muy estrecha."
    bet "*GEMIDO* ¡Oof! *JADEO* Solo ha sido la punta, ¿verdad?"
    mc "Sí, preciosa. Podemos esperar a que te acostumbres."
    bet "No es necesario. He dicho que sería CASI como volver a perder la virginidad."
    bet "Puedes seguir cuando quieras."
    show c24s001_215vb
    hide c24s001_215va
    pause (1.2)
    scene c24s001_215dv
    "Introduces la mitad de Mjolnir en su coño. Cuanto más la penetras, más estrecha se siente."
    bet "*JADEO* ¡OOF! *GEMIDO*"
    "Su coño estrechísimo ha opuesto más resistencia de la que esperabas."
    mc "¿Estás bien? No olvides relajarte."
    call BlinkXPS3 ("c24s001_220" , "d") from _call_BlinkXPS3_1568
    bet "Creo que no voy a volver a comer pavo relleno nunca. *Risa* Ahora mismo les compadezco."
    bet "Pero estoy bien. No te preocupes, estaba relajada. Creo que has limpiado las telarañas de todos los rincones."
    mc "¿Quieres que espere?"
    bet "No hace falta, cielo. Espero que lo que has dicho de la bicicleta sea cierto."
    scene c24s001_900pv
    show c24s001_900v
    hide c24s001_215va
    "Empiezas a bombear con tus caderas antes de que pueda cambiar de opinión."
    bet "*Gemido* ¡Oh, Dios mío! *Jadeo* Sigue así, cielo. *Gemido*"
    "Su voz maternal resulta chocante en esta situación, mientras golpeas las puertas de su útero."
    bet "*Jadeo* ¡Cuanta energía! *Gemido* ¡Me encanta! *Jadeo* ¡Estás moviendo toda la cama!"
    "Te fijas en ese momento en que las lámparas están moviéndose con cada una de tus embestidas. Ya no construyen los moteles como antes."
    scene c24s001_905pv
    show c24s001_905v
    hide c24s001_900v
    "Bajas un poco la intensidad de tus embestidas, centrándote en reaccionar a los gemidos de [bet], maximizando su placer."
    bet "*GEMIDO* ¡Si sigues así me voy a correr en seguida! *JADEO*"
    "Te sorprende que esté a punto de llegar tan rápido, pero después de todos los preliminares, no te extraña."
    bet "*JADEO* ¡JODER, JODER, JODER! *GEMIDO*"
    "Su estrechísimo coño hace que las sensaciones para ambos sean mucho más intensas de lo normal."
    call OrgasmXS3 ("c24s001_225") from _call_OrgasmXS3_40
    bet "*GEMIDO* ¡POR EL AMOR DE DIOS! *JADEO* ¡ME CORRO! *GEMIDO*"
    if persistent.family:
        "El cuerpo de tu tía abuela se tensa por un momento, pareciendo a punto de romperse, antes de liberar toda la tensión de golpe."
    else:
        "El cuerpo de [bet] se tensa por un momento, pareciendo a punto de romperse, antes de liberar toda la tensión de golpe."
    "El coño de la monja (o exmonja) se estrecha aún más, abrazando toda la longitud de tu polla en cada embestida."
    scene c24s001_910pv
    show c24s001_910v
    hide c24s001_905v
    "Las fuerzas parecen abandonarle y tan solo reacciona a la entrada y salida de Mjolnir en su coño. Reacciona para aprisionarlo con fiereza."
    bet "*GEMIDO* DIOS... *JADEO* BUENO... *GEMIDO* INCREÍBLE... *JADEO* SOBRINO... *GEMIDO*"
    "Ni siquiera intentas entender qué está diciendo. Te tienes que concentrar en no correrte en cada embestida. Quieres que dure más."
    bet "*JADEO* DENTRO... *GEMIDO* CORRERTE... *JADEO* DENTRO... *GEMIDO*"
    "Casi estás tentado de contradecirle. Ver tu semen pintando su estómago es tentador, pero no puedes hacerle eso después de 40 años de abstinencia."
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[bet] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ bet._var("pregnant", True)
                $ bet._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c24s001_230") from _call_OrgasmXS3_41
    hide c24s001_910v
    mc "¡Mpfft!"
    if persistent.walkthrough:
        "No puedes aguantar más y descargas una gran cantidad de semen en el coño de tu tía abuela."
    else:
        "No puedes aguantar más y descargas una gran cantidad de semen en el coño de [bet]."
    "Justo cuando recuerdas la conversación que tuviste con ella sobre lo fértiles que son las mujeres de tu familia incluso a su edad."
    bet "*GEMIDO* ¡OH, SÍ! *JADEO* ¡LLÉNAME! *GEMIDO*"
    "Tu orgasmo es muy intenso. Puedes notar los dedos de la monja sobre tu polla mientras aprieta su clítoris para alargar su placer."
    call BlinkXPS3 ("c24s001_235" , "f") from _call_BlinkXPS3_1569
    stop music fadeout (1.5)
    "Os derrumbáis sobre la cama, todavía abrazándola"
    play music ("music/Wonder.ogg")
    bet "Ha sido increíble, cielo. Pero que no te engañen. Puede que sea como montar en bicicleta, pero tú eres una moto de carreras."
    mc "*Risa* Me lo tomaré como que te ha gustado."
    call BlinkXPS3 ("c24s001_240" , "d") from _call_BlinkXPS3_1570
    bet "¡Me ha encantado! Realmente no lo recordaba tan bueno."
    mc "Supongo que han pasado años..."
    bet "Y que, definitivamente, es diferente el sexo con desconocidos a tener sexo con alguien a quien quieres. Es mucho mejor contigo."
    call BlinkXPS3 ("c24s001_245" , "d") from _call_BlinkXPS3_1571
    bet "¡Oh! Me acabo de dar cuenta."
    mc "¿De qué?"
    call BlinkXPS3 ("c24s001_250" , "f") from _call_BlinkXPS3_1572
    bet "¡No nos hemos besado ni una sola vez! Y no me refiero a los besos como saludo."
    bet "No me has besado hoy."
    mc "Eso es mentira. *Risa* He besado muchas partes de ti."
    call BlinkXPS3 ("c24s001_255" , "d") from _call_BlinkXPS3_1573
    bet "*Risa* En eso tienes razón, pero esperaba algo más romántico, con más besos."
    mc "No me culpes a mí. *Risa* Has sido tú la que has querido que entrara cuando aún estaba a mitad de los preliminares."
    call BlinkXPS3 ("c24s001_260" , "d") from _call_BlinkXPS3_1574
    bet "¡No quieras culparme a mí como si fuera una exmonja hambrienta de sexo!"
    mc "*Risa* ¿Vamos a discutir ahora sobre quién es el culpable de que no nos hayamos besado?"
    call BlinkXPS3 ("c24s001_265" , "d") from _call_BlinkXPS3_1575
    stop music fadeout (1.5)
    bet "O discutimos o le ponemos solución, aunque sea con retraso."
    play music ("music/You-Know-Instrumental.ogg")
    mc "Me parece la mejor idea. *Risa*"
    scene c24s001_270a with hpunch
    "La tumbas boca arriba y la besas apasionadamente mientras notas como una de sus tetas, sorprendentemente dura pese a su edad, presiona tu pecho."
    "No tiene nada que ver con los besos de buenos días que os habíais dado hasta ahora."
    call BlinkXPS3 ("c24s001_275" , "d") from _call_BlinkXPS3_1576
    mc "¿Contenta?"
    bet "Un poco más contenta, pero esos labios tuyos son adictivos, podría pasarme horas besándote."
    mc "¿Tienes algún lugar mejor en el que estar durante esas horas?"
    scene c24s001_270An with dissolve
    "Sin contestarte, levanta su cabeza y te besa apasionadamente."
    "Pasáis un rato besándoos, disfrutando de vuestros labios y del juego que solo dos lenguas que se buscan con ansia pueden jugar."
    "Un beso lleva a otro, en una lucha que hace que vayáis cambiando de posiciones para que vuestras manos puedan explorar el cuerpo ajeno."
    "No podrías decir si el beso ha durado minutos, horas, toda la noche, o tan solo unos segundos."
    "El tiempo ha perdido toda importancia mientras jugabais con vuestras lenguas, con vuestros labios, con vuestros alientos."
    call BlinkXPS3 ("c24s001_280" , "f") from _call_BlinkXPS3_1577
    bet "¿Alguna vez te han dicho que besas muy bien?"
    mc "Alguna vez. *Risa* ¿Y a ti?"
    bet "Alguna vez..."
    scene c24s001_280d with fade
    bet "Pero en vez de palabras, siempre he preferido hechos. Como el hecho de sentir tu dura polla contra mi hombro."
    mc "*Risa* Eso es lo que pasa cuando se tiene una mujer sexy entre los brazos que te ha dejado sin aliento con una sesión de besos increíble."
    call BlinkXPS3 ("c24s001_290" , "d") from _call_BlinkXPS3_1578
    bet "Y también pasa cuando tienes 21 años. *Risa* A mi edad..."
    mc "A tu edad me vas a mentir y me vas a decir que no estas mojada después de los besos, ¿verdad?"
    call BlinkXPS3 ("c24s001_295" , "d") from _call_BlinkXPS3_1579
    bet "¿Mojada? Empapada como si me hubieran sacado de un lago."
    mc "Entonces ¿a qué viene lo de la edad?"
    call BlinkXPS3 ("c24s001_285" , "d") from _call_BlinkXPS3_1580
    bet "A que no creo que pueda seguir tu ritmo en un segundo asalto."
    mc "¿Solo segundo asalto? *Risa* ¿Qué hay del tercero y del cuarto?"
    call BlinkXPS3 ("c24s001_290" , "d") from _call_BlinkXPS3_1581
    bet "*Risa* Te he dicho que hace 40 años que no hago esto. Me pillas desentrenada."
    mc "Entonces habrá que ponerte en forma lo antes posible. *Risa* Tienes mucho tiempo que recuperar."
    scene c24s001_300a with dissolve
    "Se revuelve en la cama hasta que consigue que te dejes tumbar de espalda. Se sienta a horcajadas sobre tu pierna."
    "Puedes notar el calor que emana de su coño en tu muslo."
    bet "¿Me estás retando?"
    mc "¿Retándote? ¿Yo? *Risa* Si te lo quieres tomar como un reto y demostrar que estoy equivocado, adelante."
    scene c24s001_300b with dissolve
    "Vuelve a besarte apasionadamente. Parece que los retos encienden algún interruptor en su mente."
    stop music fadeout (1.5)
    scene c24s001_300c with dissolve
    mc "Parece que Mjolnir ha encontrado un nuevo hogar. *Risa*"
    play music ("music/TheMatador.ogg")
    bet "No, cielo. Si me tengo que poner en forma... no va a ser con mis tetas. Al menos no hoy."
    mc "Entonces, ¿qué vas a hacer?"
    scene c24s001_305An with dissolve
    "La monja se incorpora sobre tu polla y se empala en un solo movimiento."
    bet "*Gemido* ¡Oof! *Jadeo*"
    mc "¿Estás bien?"
    bet "*Jadeo* No me dejes aceptar retos nunca. *Gemido* Me acabo de romper. *Jadeo*"
    mc "Ya te he dicho que había que ponerte en forma, pero..."
    scene c24s001_920pv with dissolve
    show c24s001_920v
    "Sin dejarte finalizar la frase, [bet] empieza a cabalgarte. Puede que no sea como montar en bicicleta, pero sabe lo que hace."
    bet "*Gemido* ¿Te parece bien para alguien que no está en forma? *Risa*"
    "Esa risa al final muestra que ha perdido toda inhibición. Esta es la [bet] que adoras."
    mc "*Risa* Me parece impresionante para alguien desentrenado."
    if persistent.family:
        "Te cuesta hacer bromas. Pese al polvo anterior, el coño de tu tía abuela sigue igual de estrecho, produciéndote unas sensaciones increíbles."
    else:
        "Te cuesta hacer bromas. Pese al polvo anterior, el coño de tu [bet] sigue igual de estrecho, produciéndote unas sensaciones increíbles."
    scene c24s001_935pv with dissolve
    show c24s001_935v
    hide c24s001_920v
    "A simple vista, [bet] es una mujer en baja forma, pero hay un montón de músculos escondidos ahí. Los está usando todos para mantener un ritmo endiablado."
    bet "*Jadeo* ¿Te gusta así, cielo? *Gemido* ¿O prefieres más rápido? *Jadeo* ¿O más lento?"
    "Dudas que pueda acelerar más sin que empiece a faltarle el aire."
    mc "Así está genial, es un ritmo perfecto."
    "No mientes. Ver su coño empalándose en tu polla a ese ritmo es casi hipnótico. Placer visual y placer físico a la vez."
    scene c24s001_925pv with dissolve
    show c24s001_925v
    hide c24s001_935v
    "Sus enormes tetas suben y bajan en cada uno de sus recorridos, en un baile que las junta y las separa al ritmo de sus movimientos."
    bet "*Gemido* Mejor. *Jadeo* No creo que pudiera acelerar mucho más. *Gemido*"
    "Tantas sensaciones visuales mientras su estrecho coño aprisiona tu polla están a punto de llevarte más allá de tu punto de no retorno."
    mc "No es necesario... Estoy a punto de correrme otra vez."
    "Su coño se tensa alrededor de tu astil como respuesta a tu frase."
    scene c24s001_930pv with dissolve
    show c24s001_930v
    hide c24s001_925v
    "Sacando fuerzas de donde no las hay, acelera un poco el ritmo para llevarte a la tierra prometida."
    bet "*GEMIDO* ¡Corrámonos juntos! *JADEO*"
    "Puedes notar como su gigantesco culo choca con fuerza contra tus piernas cada vez que el movimiento finaliza."
    bet "*JADEO* ¡VUELVE A LLENARME! *JADEO*"
    "En esta posición no puedes hacer mucho para evitar cumplir con su petición."
    mc "¡Me corro, [bet]!"
    call OrgasmXS3 ("c24s001_310") from _call_OrgasmXS3_42
    hide c24s001_930v
    bet "*GEMIDO* ¡YO TAMBIÉN! *JADEO* ¡POR DIOS! *GEMIDO*"
    if persistent.family:
        "Cuando estás a punto de correrte, llega el orgasmo de tu tía abuela."
    else:
        "Cuando estás a punto de correrte, llega el orgasmo de [bet]."
    "Las contracciones en el coño de la monja te llevan más allá de tu límite."
    if persistent.pregnancy and not bet._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[bet] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ bet._var("pregnant", True)
                $ bet._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c24s001_315") from _call_OrgasmXS3_43
    mc "¡Mpfft!"
    "Otra vez descargas lo que parecen litros de semen en el interior de la hermosa mujer."
    bet "*JADEO* ¡SÍ! *GEMIDO*"
    "Aprieta con tanta fuerza alrededor de tu astil que puedes notar como parte de tu semilla empieza a salir de su interior, bajando por tu polla."
    call BlinkXPS3 ("c24s001_320" , "f") from _call_BlinkXPS3_1582
    stop music fadeout (1.5)
    "Unos momentos después, las fuerzas agotadas de nuevo, [bet] se derrumba encima de tu pecho, con tu polla todavía dentro de ella."
    play music ("music/Wonder.ogg")
    bet "*Jadeo* Es agotador, pero es maravilloso. *Jadeo*"
    mc "Espero que tengas fuerzas para el tercer y el cuarto round. *Risa*"
    call BlinkXPS3 ("c24s001_325" , "d") from _call_BlinkXPS3_1583
    bet "¿Lo estás diciendo en serio?"
    mc "Sabía que no podrías con otro round."
    bet "Lo de retarme antes te ha funcionado. No creo que te vaya a volver a funcionar esta noche."
    call BlinkXPS3 ("c24s001_330" , "d") from _call_BlinkXPS3_1584
    bet "*Risa* Al menos sin invitarme a pizza para recargar energía."
    mc "*Risa* Voy a buscar si hay algún sitio abierto a esta hora."
    bet "*Risa* Lo decía en broma, cielo."
    call BlinkXPS3 ("c24s001_335" , "d") from _call_BlinkXPS3_1585
    bet "Y antes de que tengas más ideas divertidas, voy a darme una ducha."
    mc "¿Ducha después del sexo?"
    bet "Siempre antes y después."
    scene c24s001_335d with dissolve
    bet "*Desde el lavabo* Podríamos haber usado el jacuzzi y matar dos pájaros de un tiro."
    if oma._var("route"):
        bet "{i}(Desde que te vi con [oma], jacuzzi y sexo se funden en mi mente.)"
    mc "O la ducha."
    if mee._var("route"):
        bet "{i}(Después de verte con [mee]. no estoy segura de que fuera una buena idea para nuestra primera vez.)"
    "Escuchas llegar el Ferrarini de [emm] en el parking del motel. A estas alturas no vale la pena ir a por la ropa de [bet]."
    "Irás por la mañana, no crees que sea correcto que vaya con tu camiseta a la iglesia. Y quieres recuperar tu camiseta."
    bet "*Desde el lavabo* La ducha no es muy grande, no sé si sería muy cómodo."
    "Decides levantarte de la cama."
    call BlinkXPS3 ("c24s001_340" , "f") from _call_BlinkXPS3_1586
    mc "Yo veo mucho espacio ahí para los dos."
    bet "¡[mc]! ¿Qué haces?"
    mc "Venir a ver la ducha. Y creo que lo estabas esperando. No has abierto el agua aún."
    scene c24s001_345d with dissolve
    pause (0.8)
    call BlinkXPS3 ("c24s001_345" , "d") from _call_BlinkXPS3_1587
    bet "Si quieres ducharte conmigo no voy a poner ningún inconveniente, pero no tengas ideas malvadas."
    mc "¿Malvadas? No creo que haya nada malvado en querer entrar en la ducha contigo."
    call BlinkXPS3 ("c24s001_350" , "d") from _call_BlinkXPS3_1588
    mc "Solo por estar limpios, y esas cosas."
    bet "*Risa* Sí, sí, solo por la limpieza."
    mc "*Risa* Lo dices como si creyeras que tengo otras intenciones."
    scene c24s001_350d with dissolve
    bet "*Risa* No lo creería si tu amigo no quisiera también atención."
    mc "Mi amigo se pone así cuando hay una mujer sexy y desnuda cerca."
    call BlinkXPS3 ("c24s001_355" , "d") from _call_BlinkXPS3_1589
    bet "[mc], no hace falta que mientas."
    mc "No miento, [bet]. Nunca miento."
    call BlinkXPS3 ("c24s001_360" , "d") from _call_BlinkXPS3_1590
    bet "¿De verdad me consideras sexy? ¿No lo estás diciendo solo para que me sienta bien?"
    mc "¿De verdad crees que podría fingir una erección si no te considerara sexy?"
    mc "¿Crees que podría haber hecho el amor dos veces contigo hoy solo para hacerte sentir bien?"
    call BlinkXPS3 ("c24s001_365" , "d") from _call_BlinkXPS3_1591
    bet "Visto así..."
    mc "Podría decir muchos clichés ahora mismo."
    mc "La inteligencia es sexy. No hay nadie más sexy que la persona a quien quieres. La curva más sexy de una mujer es su sonrisa."
    mc "Podría decirte muchas frases manidas, pero si te fijas en cómo te miro, en lo cachondo que me pones, ya deberías saberlo todo."
    call BlinkXPS3 ("c24s001_370" , "d") from _call_BlinkXPS3_1592
    bet "*Risa* Me acabas de mojar, y sin necesidad de abrir el agua de la ducha."
    mc "*Risa* [bet], esto no va solo de sexo. Si estamos juntos no va a ser sexo todo el día."
    call BlinkXPS3 ("c24s001_375" , "d") from _call_BlinkXPS3_1593
    bet "¿No? *Risa* ¡Qué decepción!"
    mc "*Risa* Estoy hablando en serio. Eres una mujer muy sexy y me ha encantado hacer el amor contigo. Dos veces."
    mc "Pero estar juntos también implica besos, abrazos, pasar el tiempo juntos."
    call BlinkXPS3 ("c24s001_380" , "d") from _call_BlinkXPS3_1594
    bet "Bueno, ha habido muchos besos. No voy a decir que han sido mi parte favorita, pero casi."
    mc "Y puede haber muchos más. No todo es sexo, pese a lo divertido que es."
    stop music fadeout (1.5)
    "No hace falta que digáis nada. Vuestros ojos lo dicen todo."
    scene c24s001_385An with dissolve
    "Y vuestros labios toman el relevo de la conversación."
    play music ("music/SensualJazzMedium2.ogg")
    "Labios, manos, lenguas, bocas. Todos quieren tener su parte de diálogo. Un diálogo sin palabras que va subiendo de temperatura tal como pasan los segundos."
    "Volvéis a perder la noción del tiempo, sin saber si es de día o de noche. No importa mientras acompañas a la monja en un nuevo viaje al paraíso."
    call BlinkXPS3 ("c24s001_390" , "d") from _call_BlinkXPS3_1595
    bet "¡Wow!"
    mc "¡Wow!"
    bet "Podría pasarme horas haciendo esto."
    mc "Creo que nos las hemos pasado. *Risa*"
    call BlinkXPS3 ("c24s001_395" , "d") from _call_BlinkXPS3_1596
    bet "Te apetece que..."
    mc "Me apetece hacer lo que te apetezca a ti."
    scene c24s001_395d with dissolve
    bet "Tu amigo parece a punto de explotar."
    mc "¿Te parece extraño? Antes te he dicho que besabas muy bien."
    mc "Sigo pensándolo. Y él también."
    call BlinkXPS3 ("c24s001_400" , "f") from _call_BlinkXPS3_1597
    bet "Entonces, si no te importa, voy a comerme el postre."
    bet "Los mejores postres son los que te comes a escondidas a medianoche. *Risa*"
    mc "¿No quieres que...?"
    call BlinkXPS3 ("c24s001_405" , "d") from _call_BlinkXPS3_1598
    bet "Estoy mojadísima, pero tengo el coño ardiendo de antes. No sé si podría."
    bet "Tú me has comido antes y ahora es mi turno. Aún no te he probado."
    mc "Nunca voy a decir que no a algo así."
    scene c24s001_950pv with dissolve
    show c24s001_950v
    if persistent.family:
        "Tu tía abuela se introduce tu polla entre sus carnosos labios y empieza una mamada antológica."
    else:
        "[bet] se introduce tu polla entre sus carnosos labios y empieza una mamada antológica."
    mc "¡Wow!"
    "Su técnica te deja sin palabras. Deberías recordar que no es su primer rodeo pese a los años de actividad."
    bet "*Slurp inquisitivo*"
    "Su lengua juega con tu glande como si de una piruleta se tratara. Casi se te escapa la risa al pensar en [bet] comiendo y en ti siendo su postre."
    mc "Sí, perfecto."
    scene c24s001_955pv with dissolve
    show c24s001_955v
    hide c24s001_950v
    "No hay por qué decir más. Tampoco tienes palabras con lo que estás sintiendo. Y las vistas son muy buenas, además."
    mc "Nunca creía que una monja tuviera una boca tan pecaminosa."
    "Sabes que ya no es monja para ninguno de los dos, pero sí para el resto del mundo. Te da lo mismo el resto del mundo."
    bet "*Slurp divertido*"
    "A ella también. Ahora mismo solo existís los dos, tu polla, y su boca."
    scene c24s001_945pv with dissolve
    show c24s001_945v
    hide c24s001_955v
    "Su salvaje mamada está llevándote al límite a una velocidad exagerada. Más aún teniendo en cuenta tus dos corridas previas."
    bet "*Slurp inquisitivo*"
    "Ella lo puede notar en tus movimientos, en cómo tu polla reacciona a cada uno de los lametones de su lengua."
    mc "Sí, me estoy acercando. No voy a durar mucho más."
    mc "Lástima que no quieras un tercer round."
    call BlinkXPS3 ("c24s001_410" , "d") from _call_BlinkXPS3_1599
    "La monja separa la boca de tu polla inmediatamente y te mira directamente a los ojos."
    bet "No es que no quiera, es que... estoy muy sensible..."
    mc "Quizás eso te ayude a disfrutarlo aún más, ¿no?"
    call BlinkXPS3 ("c24s001_415" , "d") from _call_BlinkXPS3_1600
    bet "*Risa* ¿Aún más? No creo que sea posible."
    mc "Solo hay una forma de comprobarlo. Pero solo si quieres."
    call BlinkXPS3 ("c24s001_420" , "d") from _call_BlinkXPS3_1601
    if persistent.family:
        "Tu tía abuela se levanta y apoya las manos contra el cristal de la mampara, presentándote su increíble culo."
    else:
        "[bet] se levanta y apoya las manos contra el cristal de la mampara, presentándote su increíble culo."
    bet "Quiero. Mi coño te echa de menos."
    mc "Pues no le hagamos esperar."
    bet "¿Crees que cabrás ahí detrás?"
    mc "*Risa* Ya no estoy gordo, con lo que creo que sí."
    scene c24s001_425An with dissolve
    "Vuelves a penetrar su coño chorreante. Te sorprende que siga igual de estrecha en el tercer polvo de la noche."
    bet "*GEMIDO*"
    bet "Joder, [mc]. Casi me vuelvo a correr."
    mc "Cuidado con lo que sale de esa boca, señorita."
    call BlinkXPS3 ("c24s001_430" , "d") from _call_BlinkXPS3_1602
    bet "*Risa* Hace un momento ha salido tu polla de esta boca, no creo que por un taco pase nada."
    mc "*Risa* Tienes razón."
    "Te encanta que el sexo se entremezcle con las risas. Hace que sea todavía más íntimo."
    "Solo puedes reír mientras follas con alguien con quien tienes mucha confianza."
    mc "*Risa* Perdonaremos a esa boca por el maravilloso trabajo que ha hecho."
    call BlinkXPS3 ("c24s001_435" , "d") from _call_BlinkXPS3_1603
    mc "Y pensar que solo la has utilizado para comer durante todos estos años. *Risa* ¡Qué desperdicio de habilidades!"
    bet "*Risa* O empiezas a follarme o vuelvo a usar la boca."
    scene c24s001_970pv with dissolve
    show c24s001_970v
    hide c24s001_945v
    "¿Por qué no? Empiezas a bombear con Mjolnir su húmeda raja y los gemidos no tardan en aparecer. Estaba cachondísima antes de que la penetraras."
    bet "*Gemido* Creo que me vas a poner en forma en seguida. *Jadeo*"
    "Si cada día folláis tres veces, desde luego vais a recuperar sus 40 años de abstinencia bastante rápido."
    bet "*Jadeo* Necesitaré mucha pizza para recuperar la energía. *Gemido*"
    "Ni siquiera con tu polla dentro de ella puede dejar de pensar en pizza. Si no fuera un regalo de Jamaal, le permitirías quedarse con la camiseta."
    scene c24s001_975pv with dissolve
    show c24s001_975v
    hide c24s001_970v
    "Ver cómo su culo rebota contra tu estómago a cada embestida de Mjolnir en su coño es fascinante."
    bet "*GEMIDO* Comerte la polla me ha puesto cachondísima. *JADEO*"
    "Puedes notar cómo sus paredes interiores empiezan a apretar tu polla con cada movimiento, revelando que su orgasmo se está preparando."
    bet "*JADEO* ¡Corrámonos juntos otra vez! *GEMIDO*"
    "A ti te queda bastante todavía, con lo que no va a poder ser esta vez."
    call OrgasmXS3 ("c24s001_440") from _call_OrgasmXS3_44
    bet "*GEMIDO* ¡POR EL AMOR DE DIOS! *JADEO* ¡ES MEJOR QUE LOS DE ANTES! *GEMIDO*"
    "Su vagina se cierra sobre tu polla como una trampa para osos. Una trampa húmeda, caliente, y muy confortable."
    bet "*JADEO* ¡NO PARES! *GEMIDO*"
    scene c24s001_965pv with dissolve
    show c24s001_965v
    hide c24s001_975v
    "Las dos veces anteriores, en la cama, tan solo ha tenido un gigantesco orgasmo seguido de una serie de micro orgasmos de continuación."
    bet "*GEMIDO* ¡ME ENCANTA! *JADEO*"
    "Algo en su lenguale corporal, en cómo aprisiona a Mjolnir, te dice que esta vez va a ser diferente."
    bet "*GEMIDO* ¡SIGUE FOLLÁNDOTE A ESTA PECAMINOSA MONJA! *GEMIDO*"
    "En su mente, nublada por los orgasmos, se ha olvidado de que ha decidido que ya no es monja."
    "Le da lo mismo."
    "A ti también."
    scene c24s001_980pv with dissolve
    show c24s001_980v
    hide c24s001_965v
    "Tu percepción era correcta y sus orgasmos se suceden uno tras otro, estrujando tu astil en cada movimiento."
    bet "*JADEO* ¡ME CORROOOO! *GEMIDO* ¡NO PUEDO PARAR DE CORRERME! *JADEO*"
    "Cada penetración te acerca a tu límite a pasos agigantados. Si sigue corriéndose así, os vais a correr a la vez."
    "Tu tercero de la noche y su número 20... o más."
    mc "¡Estoy a punto, [bet]!"
    "Sus piernas casi no sujetan su peso y cada vez está más sin aliento."
    if persistent.family:
        bet "*JADEO* ¡Córrete para tu tía abuela! *JADEO* ¡CÓRRETE PARA ESTA MONJA! *JADEO*"
    else:
        bet "*JADEO* ¡Córrete para mí! *JADEO* ¡CÓRRETE PARA ESTA MONJA! *JADEO*"
    if persistent.walkthrough:
        $ wt1 = _("[bet] embarazada.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro. Ir a por el bebé." (wt = wt1) if persistent.pregnancy and not bet._var("pregnant"):
            $ bet._var("pregnant", True)
            $ bet._var("undiscoveredPregnancy", True)
            play sound ("music/OldMusicBox5.ogg")
            call c24s001_Creampie from _call_c24s001_Creampie
            $ Espalda = False
        "Correrte dentro." (wt = wt2):
            call c24s001_Creampie from _call_c24s001_Creampie_1
            $ Espalda = False
        "Pintar su culo y su espalda." (wt = wt2):
            call c24s001_Paint from _call_c24s001_Paint
            $ Espalda = True
    $ resetWalkthrough ()
    call BlinkXPS3 ("c24s001_480" , "d") from _call_BlinkXPS3_1604
    bet "Ahora lo que necesito es una ducha y dormir."
    mc "*Risa* ¿Nos despedimos del cuarto asalto?"
    call BlinkXPS3 ("c24s001_485" , "d") from _call_BlinkXPS3_1605
    bet "*Risa* Y eres tú quien me llama avariciosa a mí. No podría aguantar el cuarto asalto aunque me ganara el cielo con ello."
    bet "¿Quieres que nos duchemos juntos?"
    mc "Si nos duchamos juntos, no sé si podré asegurarte de que no haya un cuarto asalto."
    call BlinkXPS3 ("c24s001_490" , "d") from _call_BlinkXPS3_1606
    bet "Entonces dame cinco minutos para ducharme y te dejo la ducha para ti."
    mc "Perfecto. Te espero en la cama."
    call BlinkXPS3 ("c24s001_495" , "f") from _call_BlinkXPS3_1607
    "Cinco minutos después..."
    bet "Ya tienes la ducha para ti. Es mi turno de esperarte en la cama."
    mc "¿No te vas a secar?"
    bet "Mientras te duchas. Es tarde y no quería acaparar el lavabo."
    mc "Entonces ahora vuelvo."
    scene c24s001_495d with dissolve
    "Os besáis apasionadamente antes de que entres en el lavabo."
    "Su aliento fresco te indica que ha usado colutorio después de la ducha."
    scene c24s001_495e with fade
    if persistent.family:
        "Al salir de la ducha te das cuenta de que tu tía abuela se ha quedado dormida mientras te esperaba, con el pelo todavía húmedo."
    else:
        "Al salir de la ducha te das cuenta de que [bet] se ha quedado dormida mientras te esperaba, con el pelo todavía húmedo."
    scene c24s001_495f with fade
    "Te acuestas al lado de la mujer que dejará de ser monja mañana, abrazándola por detrás, antes de apagar las luces."
    "No reacciona a tu abrazo y sigue durmiendo, agotada."
    scene black with dissolve
    "Te quedas dormido en seguida."
    centered "{size=+20}{b}DÍA 25 – VIERNES{/b}{/size}"
    "Te despiertas cuando está amaneciendo, notando una sensación extraña."
    scene c24s001_495g with fade
    "De alguna forma, Mjolnir ha encontrado el camino a su nuevo hogar."
    scene black with dissolve
    "Te quedas dormido tras un par de pensamientos traviesos."
    stop music fadeout (1.5)
    "No tienes la energía para llevarlos a cabo."
    return
label c24s001_Creampie:
    call OrgasmXS3 ("c24s001_445") from _call_OrgasmXS3_45
    mc "¡Mpfft!"
    "Vuelves a descargar otra cantidad enorme de semen dentro de la hermosa mujer mientras otro enorme orgasmo recorre su cuerpo."
    bet "*JADEO* ¡SÍ! *GEMIDO* ¡DÁMELA TODA! *JADEO*"
    "Tu corrida provoca que su orgasmo se prolongue en el tiempo, robándole las últimas fuerzas."
    call BlinkXPS3 ("c24s001_450" , "f") from _call_BlinkXPS3_1608
    stop music fadeout (1.5)
    "Se derrumba en el suelo, mientras la sujetas para que el aterrizaje sea más suave, con tu semen aún saliendo de su raja."
    play music ("music/Wonder.ogg")
    bet "*Jadeo* Ha sido alucinante. *Jadeo* No sabía que me podía correr así... *Jadeo*"
    mc "Ha sido increíble y has aguantado como una campeona."
    mc "Quizás teniendo tu culo rebotando contra mi estómago haya influido."
    call BlinkXPS3 ("c24s001_455" , "d") from _call_BlinkXPS3_1609
    bet "*Jadeo* Desde luego que sí... *Jadeo* Notar cómo chocabas contra mi culo ha sido... tórrido. *Jadeo*"
    bet "Si quieres, la próxima vez..."
    mc "*Risa* No seas avariciosa. No te quedan fuerzas y ya estás pensando en la próxima vez."
    scene c24s001_460AnBlink1 with dissolve
    bet "Bueno... esto tiene mucha energía. *Risa*"
    mc "*Risa* Necesitarás mucho más que eso para recuperar la energía que has gastado hoy."
    return
label c24s001_Paint:
    call OrgasmXS3 ("c24s001_465") from _call_OrgasmXS3_46
    mc "¡Mpfft!"
    "Sales del interior de la hermosa mujer pintando un cuadro abstracto sobre su culo y su espalda."
    bet "*JADEO* ¡SÍ! *GEMIDO* ¡DÁMELA TODA! *JADEO*"
    "Tu corrida coincide con un último orgasmo que le roba las últimas fuerzas."
    call BlinkXPS3 ("c24s001_470" , "f") from _call_BlinkXPS3_1610
    stop music fadeout (1.5)
    "Se derrumba en el suelo, mientras la sujetas para que el aterrizaje sea más suave, con tu semen recorriendo su espalda."
    play music ("music/Wonder.ogg")
    bet "*Jadeo* Ha sido alucinante. *Jadeo* No sabía que me podía correr así... *Jadeo*"
    mc "Ha sido increíble y has aguantado como una campeona."
    mc "Quizás teniendo tu culo rebotando contra mi estómago haya influido."
    call BlinkXPS3 ("c24s001_455" , "d") from _call_BlinkXPS3_1611
    bet "*Jadeo* Desde luego que sí... *Jadeo* Notar cómo chocabas contra mi culo ha sido... tórrido. *Jadeo*"
    bet "Si quieres, la próxima vez..."
    mc "*Risa* No seas avariciosa. No te quedan fuerzas y ya estás pensando en la próxima vez."
    scene c24s001_460AnBlink2 with dissolve
    bet "Bueno... esto tiene mucha energía. *Risa*"
    mc "*Risa* Necesitarás mucho más que eso para recuperar la energía que has gastado hoy."
    return
label c24s001_NoBetSex:
    scene c24s001_500 with fade
    play music ("music/Wonder.ogg")
    "Vas a tu habitación y juegas un rato a My Residence."
    "La escena de hoy muestra una traición de Irma, la hermana del MC que acaba con Vilma, la suma sacerdotisa del culto alien, en la cama con tu personaje."
    "Poco después de jugar te echas a dormir."
    scene black with dissolve
    centered "{size=+20}{b}DÍA 25 – VIERNES{/b}{/size}"
    "Por la mañana, te reúnes con las chicas para desayunar y planear el día."
    stop music fadeout (1.5)
    "Después de desayunar, vais a devolver el coche de [emm] antes de ir a la iglesia."
    return
label c24s002_Breakfast:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_10
    scene c24s002_005a with fade
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/LifeOfAWanderingWizard.ogg")
    emm "*A través de la puerta* ¿Estáis dormidos aún? ¿Puedo pasar?"
    mc "Dame un momento."
    call BlinkXPS3 ("c24s002_010" , "h") from _call_BlinkXPS3_1612
    "Te levantas para ponerte los calzoncillos."
    bet "*Susurrando* ¡[mc]! ¿Qué va a pensar?"
    mc "*Susurrando* Va a pensar que hemos follado toda la noche y que su plan ha salido bien."
    mc "*Susurrando* Ya verás..."
    call BlinkXPS3 ("c24s002_015" , "f") from _call_BlinkXPS3_1613
    emm "Traigo la ropa de Tía [bet]. Por alguna razón acabó en una de mis maletas."
    mc "[emm], estuvo muy mal lo que hiciste anoche. ¿Qué crees que iba a pasar?"
    emm "Lo que supongo que ha pasado. Que la viste en lencería y no pudiste resistirte."
    emm "Después os habéis pasado la noche follando."
    emm "Soy un genio."
    call BlinkXPS3 ("c24s002_020" , "h") from _call_BlinkXPS3_1614
    bet "¡[emm]!"
    mc "Espera, [bet]. Que nos explique por qué piensa eso."
    call BlinkXPS3 ("c24s002_025" , "d") from _call_BlinkXPS3_1615
    emm "Es muy fácil. Si necesitabas un momento para abrirme la puerta es porque estabas durmiendo desnudo."
    emm "Tía [bet] lleva el pelo revuelto, como si se hubiera acostado con el pelo húmedo, pero se duchó antes de ir a cenar."
    emm "Le prestaste una camiseta para dormir, pero se nota que no lleva bragas, con lo que acabó sin camiseta y sin la lencería que le compré."
    emm "Y cuando follasteis en la ducha os podía oír desde mi habitación. *Risa*"
    mc "*Risa* Buena deducción, pero con la pista de la ducha..."
    call BlinkXPS3 ("c24s002_030" , "d") from _call_BlinkXPS3_1616
    emm "¡Hey! ¡Lo hubiera deducido igualmente! He descubierto todo eso con una sola mirada."
    mc "No lo pongo en duda. Mi hermana es muy lista."
    call BlinkXPS3 ("c24s002_035" , "d") from _call_BlinkXPS3_1617
    emm "Espero que no te enfadaras por lo de la ropa, Tía [bet]."
    call BlinkXPS3 ("c24s002_040" , "d") from _call_BlinkXPS3_1618
    bet "Al principio me enfadé un poco, pero luego..."
    bet "Digamos que te perdono. *Risa*"
    call BlinkXPS3 ("c24s002_045" , "d") from _call_BlinkXPS3_1619
    emm "Entonces vestíos y vamos a desayunar. A menos que queráis un segundo round matutino."
    mc "No, [emm]. Vamos a vestirnos y a desayunar."
    call BlinkXPS3 ("c24s002_050" , "d") from _call_BlinkXPS3_1620
    bet "¿Segundo round? Ilusa..."
    call BlinkXPS3 ("c24s002_055" , "h") from _call_BlinkXPS3_1621
    emm "¿Qué? ¿Follasteis dos veces en vuestra primera vez?"
    if emm._var("route"):
        emm "Conmigo solo fue una vez..."
        mc "Tu eras virgen, [emm]. Te pasaste dos días andando como si hubieras dejado el caballo en la puerta del saloon."
        call BlinkXPS3 ("c24s002_060" , "h") from _call_BlinkXPS3_1622
        emm "¿Qué? ¿Tía [bet] no era virgen? Creía que las monjas..."
    call BlinkXPS3 ("c24s002_065" , "d") from _call_BlinkXPS3_1623
    bet "*Risa* Algún día te lo explicaré. De momento me voy a vestir y vamos a desayunar."
    bet "¡Estoy hambrienta!"
    stop music fadeout (1.5)
    scene black with dissolve
    "Después de desayunar, vais a devolver el coche de [emm] antes de ir a la iglesia."
    return
label c24s002_Meanwhile_Kim_Mar_Kat:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_emm_route from _call_mrS3_emm_route_11
        call mrS3_mar_route from _call_mrS3_mar_route_6
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_7
    scene black with dissolve
    "Mientras tanto, en casa..."
    play music ("music/RhythmPlay.ogg")
    call BlinkXPS3 ("c24s002_070" , "d") from _call_BlinkXPS3_1624
    mom "Buenos días, [kim] y [kat]."
    mom "¿Cómo fue el trabajo, [kim]? No he tenido oportunidad de preguntarte."
    scene c24s002_070d with dissolve
    kat "Buenos días, [mar]. Voy a preparar el café."
    kim "Buenos días, [mar]."
    kim "Fue muy bien. El yate era increíble, y estuve casi todo el rato en el helipuerto, recibiendo a los invitados."
    call BlinkXPS3 ("c24s002_075" , "d") from _call_BlinkXPS3_1625
    mom "¿Un yate con helipuerto? Tenía que ser enorme."
    call BlinkXPS3 ("c24s002_080" , "d") from _call_BlinkXPS3_1626
    kim "Era gigantesco. Hay otro evento mañana en el mismo yate y me han llamado de la agencia porque me vuelven a contratar."
    kim "Estoy muy contenta. Si me siguen llamando de eventos así, no voy a tener problemas económicos por un tiempo."
    kim "Me daba miedo no encontrar demasiados trabajos en el área de Newport."
    call BlinkXPS3 ("c24s002_085" , "d") from _call_BlinkXPS3_1627
    mom "[kim], si en algún momento tuvieras algún tipo de problema de dinero, no te preocupes por pagar la residencia."
    mom "Podemos aplazar los pagos el tiempo que sea necesario."
    call BlinkXPS3 ("c24s002_090" , "d") from _call_BlinkXPS3_1628
    kim "Gracias, [mar], pero no creo que sea necesario. Este tipo de eventos paga muy bien."
    kim "Y si la agencia me ha llamado para otro evento del mismo cliente que paga aún mejor, significa que están contentos conmigo."
    scene c24s002_095d with dissolve
    kat "Aquí tienes tu café, [kim]."
    kim "Gracias, [kat]."
    call BlinkXPS3 ("c24s002_095" , "d") from _call_BlinkXPS3_1629
    kat "¿Tienes algo que hacer ahora mismo, [mar]? ¿Tienes unos minutos libres?"
    call BlinkXPS3 ("c24s002_100" , "d") from _call_BlinkXPS3_1630
    mom "Para vosotras siempre tengo tiempo libre, ¿por qué? ¿Qué necesitáis?"
    call BlinkXPS3 ("c24s002_105" , "d") from _call_BlinkXPS3_1631
    kat "Yo no necesito nada en concreto, pero lo que hizo [deb.nick] el otro día me dio una idea."
    kat "[kim] lleva días queriendo hablar contigo, pero siempre lo retrasa diciendo que estás muy ocupada."
    call BlinkXPS3 ("c24s002_110" , "h") from _call_BlinkXPS3_1632
    kim "¡[kat]!"
    call BlinkXPS3 ("c24s002_115" , "d") from _call_BlinkXPS3_1633
    kat "Y no os voy a encerrar en la cocina para que habléis, pero si ahora tienes un momento para que lo hagáis..."
    kat "Creo que si nadie fuerza un poco la situación, vamos a acabar nuestras carreras antes de que [kim] se atreva a hacerlo."
    call BlinkXPS3 ("c24s002_110" , "h") from _call_BlinkXPS3_1634
    kim "¡[kat]! ¡No hay prisa en hablarlo!"
    call BlinkXPS3 ("c24s002_120" , "d") from _call_BlinkXPS3_1635
    mom "¿Qué pasa [kim]? ¿Hay algo en la casa que no te guste?"
    call BlinkXPS3 ("c24s002_125" , "d") from _call_BlinkXPS3_1636
    kat "*Risa* Más bien al contrario."
    kat "Bueno, yo os dejo y voy a tomarme el café a mi habitación."
    call BlinkXPS3 ("c24s002_130" , "d") from _call_BlinkXPS3_1637
    kim "¡[kat], esta me la apunto!"
    call BlinkXPS3 ("c24s002_135" , "d") from _call_BlinkXPS3_1638
    mom "¿Qué pasa, [kim]?"
    call BlinkXPS3 ("c24s002_140" , "d") from _call_BlinkXPS3_1639
    kim "No es nada, en serio. Es sólo una tontería."
    call BlinkXPS3 ("c24s002_145" , "d") from _call_BlinkXPS3_1640
    mom "Sabes que puedes hablar conmigo de cualquier cosa, ¿verdad?"
    call BlinkXPS3 ("c24s002_150" , "d") from _call_BlinkXPS3_1641
    mom "*Risa* Acabo de sonar como sonaba cuando hablaba con [emm] cuando era más joven."
    mom "Me sale la vena maternal con tantas chicas en casa."
    call BlinkXPS3 ("c24s002_155" , "d") from _call_BlinkXPS3_1642
    kim "Precisamente por eso..."
    call BlinkXPS3 ("c24s002_160" , "d") from _call_BlinkXPS3_1643
    mom "¿Es por lo del otro día cuando estuviste a punto de llamarme Mamá?"
    mom "No te preocupes por eso. A mí no me importa... Es más, me gusta que te sientas tan cómoda conmigo."
    mom "Ven aquí, dame un abrazo."
    call BlinkXPS3 ("c24s002_165" , "f") from _call_BlinkXPS3_1644
    kim "Gracias, [mar]. Pero solo tiene que ver parcialmente con eso."
    kim "Me gusta mucho la relación que estamos desarrollando y no quiero estropearla."
    call BlinkXPS3 ("c24s002_170" , "d") from _call_BlinkXPS3_1645
    mom "¿Por qué ibas a estropearla? Eres una chica fantástica, [kim], y no creo que hayas hecho nada malo desde que has llegado a casa."
    call BlinkXPS3 ("c24s002_175" , "d") from _call_BlinkXPS3_1646
    kim "Al final me vas a emocionar. *Risa* Si me pongo a llorar como una tonta será culpa tuya."
    call BlinkXPS3 ("c24s002_180" , "d") from _call_BlinkXPS3_1647
    mom "Si necesitas llorar como una tonta, hazlo. Si quieres que lloremos juntas, explícame qué te pasa y lloramos juntas."
    scene c24s002_180d with dissolve
    kim "Lo pones tan fácil y tan difícil a la vez..."
    call BlinkXPS3 ("c24s002_185" , "d") from _call_BlinkXPS3_1648
    mom "[kim], dime que te pasa. Va a ser muy difícil ayudarte si no me lo explicas."
    call BlinkXPS3 ("c24s002_190" , "d") from _call_BlinkXPS3_1649
    kim "Es por [mc]."
    call BlinkXPS3 ("c24s002_195" , "d") from _call_BlinkXPS3_1650
    mom "¿Qué pasa con él? ¿Ha hecho algo malo? ¿Te ha dicho algo que no te haya gustado?"
    if kim._var("makeup"):
        mom "Aparte de la tontería que dijo sobre tu maquillaje corporal, claro."
    call BlinkXPS3 ("c24s002_200" , "d") from _call_BlinkXPS3_1651
    kim "No. No ha hecho nada malo. Es justo al revés. Es... demasiado bueno conmigo..."
    call BlinkXPS3 ("c24s002_205" , "d") from _call_BlinkXPS3_1652
    mom "Y crees que estás empezando a desarrollar sentimientos por él, ¿no?"
    call BlinkXPS3 ("c24s002_210" , "h") from _call_BlinkXPS3_1653
    kim "¿Cómo lo sabes?"
    call BlinkXPS3 ("c24s002_215" , "d") from _call_BlinkXPS3_1654
    mom "Sólo hace falta verte cuando está cerca, cielo."
    mom "Cuando empezamos a sentir algo por alguien creemos que nadie se da cuenta, y tan solo no se dan cuenta quienes no nos ven... y [mc]."
    mom "Además, yo pasé por lo mismo, con lo que reconozco los síntomas."
    if not mar._var("route"):
        call BlinkXPS3 ("c24s002_220" , "h") from _call_BlinkXPS3_1655
        kim "¿Qué? ¿Tú?"
        call BlinkXPS3 ("c24s002_225" , "d") from _call_BlinkXPS3_1656
        if persistent.family:
            mom "Sí. Fue unos días antes de que llegarais. Me sentía confundida y creía que me estaba enamorando de mi propio hijo."
        else:
            mom "Sí. Fue unos días antes de que llegarais. Me sentía confundida y creía que me estaba enamorando de [mc]."
        mom "Por suerte, [mc] tiene la costumbre de hablarlo todo y lo aclaramos muy rápido antes de que nadie saliera herido."
        mom "Quizás deberías hacer lo mismo. ¿Lo has hecho ya?"
    else:
        call BlinkXPS3 ("c24s002_230" , "d") from _call_BlinkXPS3_1657
        kim "Por eso es un problema..."
        call BlinkXPS3 ("c24s002_225b" , "d") from _call_BlinkXPS3_1658
        mom "¿Te preocupa compartir a [mc] conmigo?"
        call BlinkXPS3 ("c24s002_240" , "d") from _call_BlinkXPS3_1659
        kim "Me preocupa cómo te vas a sentir tú si intento algo con [mc]. Salís juntos."
        if persistent.family:
            kim "Y es tu hijo."
        call BlinkXPS3 ("c24s002_245" , "d") from _call_BlinkXPS3_1660
        if mc._var("relationships")>1:
            mom "Ya sabes que no tenemos una relación exclusiva y que no soy la única mujer con la que sale."
            mom "No sé por qué me debería importar que una chica tan fantástica como tú se uniera al harén."
        else:
            mom "Salimos juntos, pero nunca hemos hablado de exclusividad."
            mom "Si alguna vez [mc] se plantea tener un harén, me encantaría que tú formaras parte de él, si quieres."
        mom "Pero para eso, primero tienes que hablar con él. ¿Lo has hecho ya?"
    call BlinkXPS3 ("c24s002_250" , "d") from _call_BlinkXPS3_1661
    kim "Lo intenté... o para ser más exactos, lo hablé."
    kim "Se dio cuenta de que me pasaba algo cuando estaba cerca y me preguntó. No pude mentirle."
    call BlinkXPS3 ("c24s002_255" , "d") from _call_BlinkXPS3_1662
    mom "¿Y qué dijo? No estaríamos hablando de esto si no te hubiera dado esperanzas."
    mom "Y si te dio falsas esperanzas se lo haremos pagar juntas."
    call BlinkXPS3 ("c24s002_260" , "d") from _call_BlinkXPS3_1663
    kim "No, se comportó muy bien. Le dije que me preocupaba tu opinión y dijo que no me daría una respuesta... o esperanzas... hasta que no lo hablara contigo."
    call BlinkXPS3 ("c24s002_265" , "d") from _call_BlinkXPS3_1664
    mom "Típico de [mc]. Él ya debería saber lo que yo iba a responder."
    if persistent.family:
        mom "Me encantaría que salieras con mi hijo si los dos queréis."
    else:
        mom "Me encantaría que salieras con [mc] si los dos queréis."
    mom "Pero quería que lo solucionaras en tus propios términos sin importar lo que él quisiera o pensara sobre mi respuesta."
    mom "Y no te dio esperanzas para que, una vez te diera mi respuesta, todo dependiera de ti."
    call BlinkXPS3 ("c24s002_270" , "d") from _call_BlinkXPS3_1665
    kim "Para lo inocente que es a veces, parece un plan muy taimado. *Risita*"
    call BlinkXPS3 ("c24s002_275" , "d") from _call_BlinkXPS3_1666
    mom "Es muy inocente para muchas cosas, y eso me encanta de él, pero creo que está evolucionando mucho."
    mom "Cuando volvió de la universidad, seguramente ni siquiera se hubiera dado cuenta de que te pasaba algo con él."
    call BlinkXPS3 ("c24s002_280" , "d") from _call_BlinkXPS3_1667
    mom "Además, él nunca ha empezado una relación por lo que sé."
    mom "[eil] y [sai] la empezaron ellas."
    if mar._var("route"):
        mom "Yo también."
        if mc._var("relationships")>1:
            mom "Y ya sabes el resto."
    elif mc._var("relationships")>1:
        mom "Y ya sabes el resto."
    call BlinkXPS3 ("c24s002_285" , "d") from _call_BlinkXPS3_1668
    kim "Es una posición muy cómoda por su parte, ¿no? Y un poco egoísta."
    kim "Somos nosotras las que tenemos que descubrir nuestros sentimientos y él aceptarlos o no."
    kim "Nos tenemos que desnudar emocionalmente delante de él..."
    call BlinkXPS3 ("c24s002_290" , "d") from _call_BlinkXPS3_1669
    mom "Los hombres han estado en esa situación durante siglos."
    mom "[mc] le ha dado la vuelta. Solo plantéate una pregunta."
    mom "¿Crees que [mc] está enamorado de ti?"
    call BlinkXPS3 ("c24s002_295" , "d") from _call_BlinkXPS3_1670
    kim "No lo sé... lo dudo."
    kim "Aunque yo tampoco estoy enamorada de él... al menos no hasta las trancas..."
    call BlinkXPS3 ("c24s002_300" , "d") from _call_BlinkXPS3_1671
    mom "No te lo tomes a mal. Yo también lo dudo."
    mom "Pero crees que podría querer salir contigo, ¿no?"
    call BlinkXPS3 ("c24s002_305" , "d") from _call_BlinkXPS3_1672
    kim "Quiero creer que hay una posibilidad."
    kim "Creo que le gusto físicamente."
    call BlinkXPS3 ("c24s002_310" , "d") from _call_BlinkXPS3_1673
    mom "Siguiente pregunta. ¿Por qué iba a salir contigo si no está enamorado de ti?"
    mom "Que le gustes físicamente no es razón suficiente. La mayoría de los hombres follarían con una mujer que les atrae físicamente."
    mom "Pero no necesariamente saldrían con ella."
    call BlinkXPS3 ("c24s002_315" , "d") from _call_BlinkXPS3_1674
    kim "No lo sé... ¿quieres decir que sólo va a querer tener sexo conmigo?"
    call BlinkXPS3 ("c24s002_320" , "d") from _call_BlinkXPS3_1675
    mom "No, [kim]. [mc] no es así. Si tiene algo contigo será una relación completa, aunque no esté enamorado de ti."
    mom "Al menos aún. Hace dos semanas que os conocéis. No ha tenido tiempo de enamorarse de ti."
    call BlinkXPS3 ("c24s002_325" , "d") from _call_BlinkXPS3_1676
    kim "Eso es relativo... yo..."
    kim "Pero entonces... ¿por qué iba a querer salir conmigo?"
    kim "Cada vez lo entiendo menos."
    call BlinkXPS3 ("c24s002_330" , "d") from _call_BlinkXPS3_1677
    if persistent.family:
        mom "Porque [mc] es especial. Y no lo digo solo porque sea mi hijo."
    else:
        mom "Porque [mc] es especial."
    mom "Si empieza a salir contigo será porque cree que puede funcionar a largo plazo. Porque cree que puede enamorarse de ti."
    mom "Y porque tú sí que estás enamorada de él. Necesitas estar con él."
    call BlinkXPS3 ("c24s002_335" , "d") from _call_BlinkXPS3_1678
    mom "No va a empezar algo contigo solo por sexo. Puede tener todo el sexo que quiera sin hacer daño a nadie."
    mom "[mc] nunca haría daño a nadie a propósito. Y menos a alguien que... ¿cómo lo has dicho?... Se desnuda emocionalmente delante de él."
    call BlinkXPS3 ("c24s002_340" , "d") from _call_BlinkXPS3_1679
    kim "Ahora que lo has dicho tú... he sonado un poco cursi, ¿verdad?"
    call BlinkXPS3 ("c24s002_345" , "d") from _call_BlinkXPS3_1680
    mom "*Risa* ¿Sólo un poco?"
    mom "Dame otro abrazo."
    scene c24s002_345d with dissolve
    kim "Entonces, ¿no te importa que lo intente con él?"
    mom "No, cielo. No me importa. Nunca nadie me lo ha preguntado y no tengo ningún derecho a que me importe."
    kim "Quizás no te lo han preguntado porque no te veían como una figura materna."
    if emm._var("route"):
        mom "*Risa* ¿Ni siquiera [emm]?"
        mom "Sobre el resto, es posible, mi niña."
    else:
        mom "Es posible, mi niña."
    kim "¿Tienes algo que hacer ahora mismo?"
    mom "No, ¿por qué?"
    kim "¿Podemos quedarnos así un rato?"
    stop music fadeout (1.5)
    mom "Todo el tiempo que necesites."
    return
label c24s002_BetNoNun:
    if _in_replay:
        call mrS3_bet_route from _call_mrS3_bet_route
    scene black with dissolve
    "Después de dejar el coche de [emm] vais al edificio administrativo de la iglesia."
    "[bet] te pide que la acompañes."
    play music ("music/Tribal.ogg")
    "[emm] también quiere entrar, pero después de una par de amenazas veladas, decidís que será mejor que os espere en la heladería de ayer."
    scene c24s002_350a with dissolve
    bet "Buenos días, Hermana. Tengo una cita con el Padre Segismund."
    "Monja" "Lo siento, pero hoy solo tiene una cita..."
    bet "¿Con la Hermana Beatrix?"
    "Monja" "Sí..."
    scene c24s002_350b with hpunch
    "Monja" "¡Oh!"
    bet "Exacto. ¡Oh! Estuve ayer aquí."
    scene c24s002_350c with dissolve
    "Monja" "Debería haber venido con el hábito, Hermana."
    bet "No es necesario para lo que vengo a hacer, Hermana."
    bet "¿Puedo pasar al despacho del Padre Segismund?"
    scene c24s002_350d with dissolve
    "Monja" "Ya la acompaño..."
    bet "No es necesario, gracias. Conozco el camino. [mc], vamos."
    scene c24s002_355a with fade
    bet "Buenos días, Padre Segismund. Siéntate, [mc]."
    "Segismund" "¡Hermana! ¿Qué hace vestida así? ¿Dónde está su hábito?"
    call BlinkXPS3 ("c24s002_360" , "d") from _call_BlinkXPS3_1681
    bet "En mi maleta. Nos vamos hoy de Monterey."
    scene c24s002_355b with dissolve
    "Segismund" "Esto es una instalación de la Iglesia. Debería haber venido vestida correctamente."
    "Segismund" "No... así. En ninguno de los conventos que le proponemos la van a dejar vestir así."
    "Segismund" "No es... decoroso."
    call BlinkXPS3 ("c24s002_365" , "d") from _call_BlinkXPS3_1682
    bet "Bueno, sobre eso es sobre lo que iba esta reunión, ¿no? Sobre esos conventos."
    scene c24s002_355c with dissolve
    "Segismund" "Le he preparado la información que le prometí sobre los conventos disponibles."
    call BlinkXPS3 ("c24s002_370" , "d") from _call_BlinkXPS3_1683
    bet "No hace falta que me la de. No voy a aceptar ninguno de ellos."
    scene c24s002_355d with dissolve
    "Segismund" "¿Qué? ¿Por qué?"
    "Segismund" "Eso significará la expulsión de la Iglesia. El obispo lo dejó muy claro."
    mc "*Risa*"
    mc "¡Uy, perdón!"
    scene c24s002_355e with dissolve
    "Segismund" "¿De qué se ríe, muchacho?"
    mc "Una idea que me ha cruzado por la mente me ha parecido graciosa."
    mc "No sé cómo funciona esto, pero si la despiden, la expulsan, o como se llame, ¿recibirá algún tipo de indemnización?"
    scene c24s002_355f with dissolve
    "Segismund" "No, por supuesto. La expulsión se debe a desobedecer órdenes del obispo."
    mc "Órdenes que, para cualquier persona que no pertenezca a la Iglesia, serían como una condena de cárcel o el exilio, ¿no?"
    scene c24s002_355g with dissolve
    "Segismund" "No, Señor..."
    mc "Marks. Soy el sobrino nieto de [bet]."
    "Segismund" "Como decía, está usted equivocado. Le estamos dando a su tía una oportunidad de seguir sirviendo a la iglesia y la está rechazando."
    "Segismund" "Todo es legal. La Iglesia siempre actúa de buena fe."
    mc "Entonces, no le importaría si yo fuera a la prensa y explicara la situación, ¿verdad?"
    mc "Si todo es legal y hecho de buena fe, no debería haber ningún problema."
    mc "Tampoco en explicar lo que pasó en Tanzania, que es lo que nos ha traído a esta situación."
    scene c24s002_355h with dissolve
    "Segismund" "¡No puede hacer eso! Ayer acordamos con su tía que si hablaba con la prensa retiraríamos la oferta."
    mc "Y la expulsarían, ¿no?"
    mc "Si no acepta los conventos también la expulsarán, con lo que nada evita que vayamos a la prensa."
    call BlinkXPS3 ("c24s002_375" , "d") from _call_BlinkXPS3_1684
    bet "[mc], déjalo. La decisión ya estaba tomada."
    mc "Déjame un momento, por favor."
    scene c24s002_355i with dissolve
    mc "Entonces, una pequeña indemnización por los años de servicio sería lo idóneo y lo justo, ¿no?"
    "Segismund" "Eso no se ha hecho nunca. Sentaría un precedente."
    mc "Mire, no le estoy diciendo que compre nuestro silencio. Eso sería chantaje. Solo le estoy pidiendo lo que es justo para mi tía."
    mc "Ustedes la expulsan y ella tiene que empezar una vida nueva después de 40 años de servicio sin tener un dólar ahorrado."
    mc "No es justo, ¿no?"
    scene c24s002_355j with dissolve
    "Segismund" "No... pero... es legal."
    mc "También es legal ir a la prensa a explicar la situación."
    mc "Podrán comprobar como descienden las donaciones cuando se descubra cómo trata esta diócesis a personas que han trabajado 40 años para la Iglesia."
    call BlinkXPS3 ("c24s002_380" , "d") from _call_BlinkXPS3_1685
    bet "¿Qué haces, [mc]?"
    mc "Tratar a la Iglesia como te ha intentado tratar a ti."
    mc "Si ellos pueden usar sus armas, nosotros podemos usar las nuestras."
    mc "Supongo que no habían pensado que pudieras tener un sobrino abogado laboralista."
    scene c24s002_355k with dissolve
    "Segismund" "¿Abogado laboralista? Entonces, ¿qué propone?"
    mc "Una pequeña indemnización por cada año trabajado."
    mc "No le estoy pidiendo que lo haga teniendo en cuenta el sueldo de un cirujano con los años de experiencia de mi tía."
    mc "Puede usar su sueldo actual como referencia. Nos conformamos con 30 días de indemnización por año trabajado."
    mc "No sé si, en alguno de los países en los que ha trabajado, la indemnización puede llegar a los 40 días por año trabajado. Lo tendría que mirar."
    scene c24s002_355l with dissolve
    "Segismund" "¡Eso sería mucho dinero! La Iglesia..."
    mc "La Iglesia va a perder mucho más en donaciones si esto sale en la prensa."
    mc "Son poco más de tres años de sueldo de una monja. Lo acabo de calcular."
    scene c24s002_355m with dissolve
    "Segismund" "No puedo autorizar eso. No tengo poder para ello."
    "Segismund" "¿Podrían volver en un mes y les hacemos una propuesta?"
    mc "No."
    call BlinkXPS3 ("c24s002_385" , "d") from _call_BlinkXPS3_1686
    bet "¿No?"
    mc "No, Tía [bet]. En un mes estaré fuera del país, y no quiero que te intenten estafar."
    scene c24s002_355n with dissolve
    mc "Dice que no tiene poder para tomar esa decisión. Consúltelo con quién lo tenga que consultar y volveremos en tres horas."
    "Segismund" "¿Tres horas? No sé si tendré tiempo de..."
    mc "Si en tres horas no tiene una propuesta, en tres días aparecerá en prensa nuestra versión de los hechos."
    mc "Para que no puedan adelantarse y mentir, publicaré ahora mismo un twirp indicando el inicio de la historia."
    mc "Deme un segundo."
    scene c24s002_355o with dissolve
    "Después de publicar el twirp..."
    mc "Ya está hecho. La historia de una monja maltratada y chantajeada por la iglesia. En tres días sabrán toda la verdad."
    mc "Nos vemos en tres horas. Tic-tac."
    call BlinkXPS3 ("c24s002_390" , "d") from _call_BlinkXPS3_1687
    mc "¿Nos vamos, Tía [bet]?"
    bet "Sí, vámonos. Creo que el Padre Segismund tiene unas llamadas que hacer."
    call BlinkXPS3 ("c24s002_395" , "f") from _call_BlinkXPS3_1688
    stop music fadeout (1.5)
    "Al salir del edificio de la Iglesia..."
    play music ("music/These-Little-Moments.ogg")
    bet "¿Qué has hecho? Ya habíamos hablado de que venía a informarles de que dejaba de ser monja."
    mc "Vas a dejar de ser monja igualmente, no te van a permitir seguir en la Iglesia y moverte libremente. Pero te irás con los bolsillos llenos."
    mc "Podrás pagar la certificación y ayudar a Meemaw con su nueva casa, tal como queréis las dos."
    call BlinkXPS3 ("c24s002_400" , "d") from _call_BlinkXPS3_1689
    bet "*Risa* Tienes razón. No se me hubiera ocurrido nunca."
    mc "*Risa* Para eso me tienes a mí."
    call BlinkXPS3 ("c24s002_405" , "d") from _call_BlinkXPS3_1690
    bet "Por cierto, creía que no mentías nunca."
    mc "Y no he mentido."
    bet "¿Abogado laboralista? ¿Desde cuándo eres abogado?"
    mc "Yo no he dicho que lo fuera. He dicho que ellos no podían imaginar que tuvieras un sobrino que lo fuera."
    mc "Yo tampoco. *Risa* Porque no lo tienes."
    call BlinkXPS3 ("c24s002_410" , "d") from _call_BlinkXPS3_1691
    bet "¿Y lo de las indemnizaciones de 40 días en los países en los que he trabajado?"
    mc "He dicho que no sabía si alguno de esos países tenía 40 días de indemnización. *Risa*"
    mc "He pedido 30 días esperando que nos den 15. Lo de los 40 días de indemnización lo he dicho para ponerlo nervioso."
    mc "Tanto él como tú habéis entendido lo que habéis creído oír, pero que yo no he dicho. *Risa* No hay una sola mentira en lo que he dicho."
    call BlinkXPS3 ("c24s002_415" , "d") from _call_BlinkXPS3_1692
    bet "*Risa* A partir de ahora tendré que analizar todo lo que digas."
    mc "No hace falta. Esos trucos solo los uso con gente de fuera de la familia."
    mc "Con la familia tendrían un recorrido muy corto."
    mc "¿Vamos a buscar a [emm]? Tenemos tres horas para hacer turismo antes de tener que volver."
    call BlinkXPS3 ("c24s002_420" , "d") from _call_BlinkXPS3_1693
    bet "Eso es otra cosa que no he entendido. ¿Por qué tres horas y no dos o cinco?"
    mc "Sonaba bien lo de tres horas para arreglarlo o tres días para publicarlo."
    mc "Hoy es viernes, con el fin de semana por en medio, se publicaría el lunes. No tenían mucho tiempo para reaccionar."
    mc "Además, a ese pobre hombre se le veía muy agobiado, como si no supiera de dónde le venían los golpes."
    mc "Y lo del twirp ha sido lo que ha acabado de descolocarlo. Por suerte solo me sigue Jamaal en Twirper."
    call BlinkXPS3 ("c24s002_425" , "d") from _call_BlinkXPS3_1694
    bet "*Risa* ¿Y todo eso lo has pensado en un minuto?"
    mc "No, ayer estuve pensando en diferentes escenarios, pero hasta que no ha dicho lo de la expulsión no he atado cabos."
    mc "En mi mente expulsión y despido venía a ser lo mismo, y he ido planeando cosas mientras hablaba."
    call BlinkXPS3 ("c24s002_430" , "d") from _call_BlinkXPS3_1695
    bet "Pero les estás haciendo chantaje con lo de ir a la prensa. Podríamos acabar en la cárcel."
    mc "No, no les estoy chantajeando. Son ellos los que intentaron chantajearte a ti diciendo que si ibas a la prensa retiraban su oferta."
    mc "Yo tan solo les he dicho que pueden retirar la oferta porque vamos a ir a la prensa igualmente."
    mc "Si no quieren prensa, queremos un trato justo. Tan solo estamos rechazando su chantaje."
    call BlinkXPS3 ("c24s002_435" , "d") from _call_BlinkXPS3_1696
    bet "Y si intentaran denunciarnos, tendrían que reconocer que estaban intentando chantajearme."
    mc "Exacto. No soy abogado, pero el cura tampoco lo es. El sentido común es lo que me dice, y supongo que a él también."
    mc "Por eso le he dado poco tiempo para decidir. No va a poder consultar con mucha gente."
    call BlinkXPS3 ("c24s002_440" , "d") from _call_BlinkXPS3_1697
    bet "*Risa* Espero no tenerte nunca de enemigo."
    mc "No deberías temerme a mí. *Risa* [ama] y [eva] te deberían preocupar más. Especialmente si no tienes un rodillo a mano."
    mc "Vamos a buscar a [emm] y a hacer un poco de turismo. Solo tenemos tres horas."
    call BlinkXPS3 ("c24s002_445" , "f") from _call_BlinkXPS3_1698
    "Pasáis a buscar a [emm] por la heladería y le explicáis el resultado de la reunión."
    emm "Menos mal que no he ido."
    mc "¿Por qué?"
    emm "Lo primero que le hubiera dicho al cura hubiese sido 'Mi tía os abandona, gilipollas. Vosotros os lo perdéis.'"
    emm "Y no hubiera habido indemnización. *Risa* Además, no se me hubiera ocurrido nunca."
    call BlinkXPS3 ("c24s002_450" , "d") from _call_BlinkXPS3_1699
    bet "A mí tampoco. Pero [mc] ha pensado muy rápido y no ha dejado un segundo para que el Padre Segismund pudiera pararse a pensar."
    mc "Bueno, es una de las técnicas de negociación que me enseñaron en la universidad."
    mc "No la recomiendan por ser demasiado agresiva, y normalmente la gente tiene tiempo para pensar después, con lo que se dan cuenta de los fallos que haya cometido."
    call BlinkXPS3 ("c24s002_455" , "d") from _call_BlinkXPS3_1700
    emm "Lo importante es que está resuelto... a medias."
    emm "¿Preparados para que os haga de guía turístico de Monterey?"
    mc "No sabía que habías estado aquí antes."
    call BlinkXPS3 ("c24s002_460" , "d") from _call_BlinkXPS3_1701
    emm "No he estado nunca, pero he tenido tiempo de mirarme unas guías por internet mientras esperaba."
    if bet._var("route"):
        emm "Y anoche, mientras alguien hacía otras cosas más divertidas."
    mc "*Risa* Es un buen entrenamiento para ti. Querías ser fotógrafa de guías de viaje."
    call BlinkXPS3 ("c24s002_465" , "d") from _call_BlinkXPS3_1702
    bet "Nunca me has dicho como [eri] y tú decidisteis que vuestro sueño era algo tan específico y que coincidieseis en lo que queríais ser."
    call BlinkXPS3 ("c24s002_470" , "d") from _call_BlinkXPS3_1703
    emm "Encontramos unas guías de Europa en la biblioteca del instituto, de esas viejas, en papel."
    emm "Venecia, París, Roma, Barcelona, Atenas..."
    emm "Decidimos que queríamos conocer todas esas ciudades. *Risa* Y que no había mejor forma de hacerlo que si nos pagaban."
    mc "El plan se le ocurrió a [eri], ¿no?"
    call BlinkXPS3 ("c24s002_475" , "h") from _call_BlinkXPS3_1704
    emm "¿Qué insinúas con eso? ¿Que mis planes no son realistas?"
    if bet._var("route"):
        emm "El de anoche funcionó."
    mc "Pero se le ocurrió a [eri], ¿verdad?"
    call BlinkXPS3 ("c24s002_480" , "d") from _call_BlinkXPS3_1705
    emm "Sí. *Risa* Y vámonos a visitar Monterey o al final no podré enseñaros los sitios que he descubierto."
    mc "Vamos. Tenemos menos de tres horas."
    scene c24s002_485An with dissolve
    "[emm] os lleva por algunos de los sitios más emblemáticos de Monterey, aprovechando para sacar fotografías en cada uno de ellos."
    "Os da explicaciones sorprendentemente detalladas sobre cada uno de los lugares que visitáis."
    "Pero esas tres horas se hacen muy cortas y tenéis que dejar muchas cosas en el tintero, para otra visita."
    "La última parada es la Catedral de Monterey, muy cerca del edificio donde os habéis reunido con el Padre Segismund."
    emm "Y esta es la catedral más pequeña de los Estados Unidos. Se fundó como la capilla de un presidio español."
    emm "Era como llamaban a sus fuertes."
    bet "Muy interesante la visita, [emm]. Nos has dado un montón de información para haber estudiado la ciudad solo unas horas."
    mc "Si lo de hacerte fotógrafa no funciona, tienes futuro como guía turística."
    scene c24s002_485f with dissolve
    emm "Iros antes de que me hagáis ruborizar. No estoy acostumbrada a los elogios."
    emm "Me llevo la camioneta a la heladería y os espero allí. Ya me estoy haciendo amiga de Margaret, la camarera."
    bet "Déjame un poco de helado. El dónut de antes me ha dejado con hambre."
    stop music fadeout (1.5)
    mc "Te vemos en un rato."
    scene c24s002_350e with dissolve
    play music ("music/Throne-King.ogg")
    bet "Hola de nuevo, Hermana. Venimos a ver al Padre Segismund de nuevo."
    "Monja" "Les está esperando. Pasen."
    scene c24s002_355p with dissolve
    "Segismund" "Hola de nuevo. Tengo noticias para ustedes. Siéntense, por favor."
    "Segismund" "He hablado con mis superiores y, por desgracia, no han aceptado lo de los 30 días de indemnización por año trabajado."
    mc "Bueno, entonces no nos deja más opciones que ir a la prensa."
    scene c24s002_355q with dissolve
    "Segismund" "No, espere. Me han autorizado a pagarle a la Hermana Beatrix tan solo 20 días de indemnización."
    "Segismund" "Usted tenía razón en que hay países en los que ha trabajado con indemnizaciones de hasta 45, pero otros tienen menos."
    "Segismund" "Sé que no era lo que esperaban, pero..."
    mc "Entonces eso sería... algo más de dos años de sueldo."
    scene c24s002_355r with dissolve
    "Segismund" "Algo más. He pedido que, al no cumplir con sus peticiones, añadieran algo más por algunos complementos para su tía."
    "Segismund" "Al final, serán 2.64 años de sueldo. Lo siento pero no he podido conseguir más." id c24s002_BetNoNun_61103e94
    "Segismund" "Obviamente tendrá que firmar un acuerdo de confidencialidad sobre todo este asunto."
    mc "2.64 años y acuerdo de confidencialidad. ¿Cómo lo ves, Tía [bet]?" id c24s002_BetNoNun_d093d5c0
    call BlinkXPS3 ("c24s002_490" , "d") from _call_BlinkXPS3_1706
    bet "Me parece bien..."
    scene c24s002_355s with dissolve
    mc "¿Hay oferta por escrito de todo esto?"
    "Segismund" "Sí, también tengo el acuerdo de confidencialidad. Ha llegado todo hace unos minutos. Tres horas era muy poco tiempo."
    "Segismund" "La oferta indica que dejará la Iglesia a final de mes, que es cuando se les entregará el dinero. Pero el acuerdo de confidencialidad entra en vigor hoy."
    mc "Me parece bien. ¿Firmamos?"
    call BlinkXPS3 ("c24s002_495" , "d") from _call_BlinkXPS3_1707
    "Después de firmar todos los papeles..."
    mc "Bueno, Tía [bet], en unos días dejarás de ser monja y tendrás una buena cantidad de dinero en tu cuenta."
    bet "Sí. Creo que es lo mejor para todos. Para la Iglesia y para mí."
    mc "Creo que, ahora que todo está firmado, le puedes decir al Padre Segismund cuál era tu intención al entrar por esa puerta esta mañana."
    call BlinkXPS3 ("c24s002_500" , "d") from _call_BlinkXPS3_1708
    bet "¿Qué? ¿Crees que es necesario?"
    mc "Creo que vas a disfrutar cada segundo."
    call BlinkXPS3 ("c24s002_505" , "d") from _call_BlinkXPS3_1709
    bet "Padre Segismund, primero quiero darle las gracias por hacer las gestiones tan rápido."
    scene c24s002_355t with dissolve
    "Segismund" "Supongo que hay algún pero por lo que ha dicho su sobrino."
    call BlinkXPS3 ("c24s002_510" , "d") from _call_BlinkXPS3_1710
    bet "Sí. Pero mi intención al venir hoy era abandonar la Iglesia. Nunca pensé en una indemnización ya que era yo la que me iba."
    bet "Gracias por 2.64 años de mi sueldo." id c24s002_BetNoNun_492795a5
    scene c24s002_355u with hpunch
    "Segismund" "¿Qué?"
    mc "*Risa* Por suerte, todo está firmado y mi tía ya no se puede echar atrás."
    mc "Gracias por todo, Padre Segismund."
    "Abandonáis el edificio de la Iglesia con la cara de sorpresa del Padre Segismund grabada en vuestras retinas."
    call BlinkXPS3 ("c24s002_515" , "d") from _call_BlinkXPS3_1711
    stop music fadeout (1.5)
    "Una vez en el exterior..."
    play music ("music/These-Little-Moments.ogg")
    bet "Gracias por todo, [mc]. Si no hubiera sido por ti..."
    mc "No tienes por qué darlas. He visto una oportunidad y la he aprovechado. Esperaba 15 días y nos han dado 20. No está mal."
    mc "Ahora tienes dinero suficiente para la recertificación, supongo."
    if bet._var("route"):
        call BlinkXPS3 ("c24s002_520" , "d") from _call_BlinkXPS3_1712
        bet "Lo que más me jode de no haber dejado de ser monja hoy es que no te puedo besar ahora mismo aquí delante."
        bet "Serían capaces de excomulgarme para ahorrarse el dinero. *Risa*"
        mc "*Risa* Habrá mucho tiempo para eso. No te preocupes."
    mc "Vamos a buscar a [emm]. Se tiene que estar mordiendo las uñas del nerviosismo."
    call BlinkXPS3 ("c24s002_525" , "f") from _call_BlinkXPS3_1713
    "Después de recoger a [emm] y explicárselo todo..."
    if bet._var("route"):
        emm "Si queréis puedo conducir yo de vuelta a casa. Por si estáis cansados después de la noche de ayer. *Risita*"
        mc "Me parece una buena idea. Así podemos echar una siesta mientras tú conduces."
        mc "Tu dormiste en el viaje de ida y nosotros en el de vuelta."
    else:
        emm "Vuelvo a pedirme el asiento de atrás. He dormido poco con los ronquidos de Tía [bet]."
    emm "¡De vuelta a casa!"
    scene black with dissolve
    "Durante el viaje a casa, Tía [bet] manda varios mensajes al grupo de WhatsUp para informar de cómo ha ido todo."
    stop music fadeout (1.5)
    "Se queda profundamente dormida después de contestar todos los mensajes del resto de las chicas."
    return
label c24s003_Mar:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_bet_route from _call_mrS3_bet_route_1
        call mrS3_mar_route from _call_mrS3_mar_route_7
        call mrS3_kia_route from _call_mrS3_kia_route_4
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_8
    scene black with dissolve
    "Paráis a comer en King City. Pizza para todos. Idea de [bet]."
    "Después de charlar un rato y reposar la comida, seguís camino a casa."
    if bet._var("route"):
        "Conduces tú después de comer. [emm] ha querido competir con [bet] comiendo pizza y se siente pesada."
    call BlinkXPS3 ("c24s003_005" , "d") from _call_BlinkXPS3_1714
    play music ("music/Sunny-Skies.ogg")
    "En cuanto abres la puerta del garaje, aparece [mar] en la puerta de casa. Parece que os ha estado esperando."
    call BlinkXPS3 ("c24s003_010" , "d") from _call_BlinkXPS3_1715
    mom "Hola, [emm]. ¿Te lo has pasado bien con el coche?"
    emm "Ha sido fantástico. Incluso hemos tenido un poco de tiempo para hacer turismo en Monterey."
    emm "¿Todo bien por aquí?"
    mom "Sí, cielo. Os he echado de menos. Déjame abrazar a Tía [bet]."
    call BlinkXPS3 ("c24s003_015" , "d") from _call_BlinkXPS3_1716
    mom "Felicidades por haberlo resuelto todo, Tía."
    if bet._var("route"):
        if mar._var("route"):
            mom "Y bienvenida al harén."
        elif mc._var("relationships")>1:
            mom "Y por entrar en el harén de [mc]."
        else:
            mom "Y por lo tuyo con [mc]."
    bet "Gracias, cielo. Ha sido un viaje muy intenso."
    bet "Ve a abrazar a [mc]. Te veo ansiosa. [emm] y yo vamos a meter las maletas dentro."
    call BlinkXPS3 ("c24s003_020" , "h") from _call_BlinkXPS3_1717
    emm "¿No nos va a ayudar [mc]? ¡Yo tengo tres maletas!"
    scene c24s003_025 with dissolve
    bet "Él las ha bajado de la camioneta."
    bet "Si quieres trabajar viajando tendrás que aprender a llevar menos equipaje. Esta es tu primera lección."
    bet "Yo subo una y tú otra. Después subes la tercera mientras yo recojo la mía."
    call BlinkXPS3 ("c24s003_030" , "d") from _call_BlinkXPS3_1718
    "[mar] te da un abrazo que sería la envidia de cualquier mamá oso."
    mom "Se me ha hecho muy largo no teneros por aquí."
    mc "Sólo ha sido un día. Pero me alegro de volver, y más con este recibimiento."
    if mar._var("route"):
        scene c24s003_030d with dissolve
        if persistent.family:
            "Tu madre te da un apasionado beso que te deja sin aliento."
        else:
            "[mar] te da un apasionado beso que te deja sin aliento."
        call BlinkXPS3 ("c24s003_030" , "d") from _call_BlinkXPS3_1719
    mom "Ahora todo está mejor. Ya estáis en casa."
    if kia._var("route"):
        call BlinkXPS3 ("c24s003_035" , "d") from _call_BlinkXPS3_1720
        "Después de un largo abrazo..."
        mom "Hoy tienes tu primera cita con [kia], no lo olvides."
        mc "*Risa* No lo puedo olvidar, aunque para nosotros es la tercera. Salimos a comer y dimos un paseo."
        mom "¿Dónde vais a ir?"
        mc "No tengo ni idea. Me dijo que lo organizaba ella, con lo que es una sorpresa también para mí."
        call BlinkXPS3 ("c24s003_040" , "d") from _call_BlinkXPS3_1721
        mom "Ah, por eso me estuvo preguntando por restaurantes bonitos. ¡Seré tonta!"
        mom "El único que conozco es el de la cueva al que me llevaste. Parece que hace mil años."
        if mar._var("route"):
            mom "Pero ese no se lo voy a recomendar a nadie. Ese es nuestro. Nuestra primera cita, aunque no saliéramos juntos aún."
        mc "Un día tenemos que volver a ese sitio. Fue una noche fantástica."
        call BlinkXPS3 ("c24s003_045" , "d") from _call_BlinkXPS3_1722
        mom "Estoy segura de que, te lleve donde te lleve [kia] también os lo vais a pasar muy bien."
        mom "Ayer estaba nerviosa por la cita."
        mc "A lo mejor debería hablar con ella antes..."
        call BlinkXPS3 ("c24s003_050" , "d") from _call_BlinkXPS3_1723
        mom "No creo que tengas mucho tiempo para eso. Está trabajando y supongo que, cuando vuelva a casa, se querrá poner guapa para ti."
        mom "Los nervios se le pasarán en cuanto la recojas."
        mc "*Risa* Espero que también se me pasen a mí."
        call BlinkXPS3 ("c24s003_055" , "d") from _call_BlinkXPS3_1724
        mom "*Risa* Bueno, ve a descansar un rato antes de esa cita."
    else:
        mom "Será mejor que vayas a descansar un rato antes de la cena."
    mom "Dame la mochila. Bajaré a dejar la ropa en la lavadora."
    mom "Veo que al final te has puesto la camisa azul. *Risa*"
    stop music fadeout (1.5)
    mc "*Risa* Si, te veo luego."
    scene black with dissolve
    return
label c24s003_NoKia:
    scene c24s003_060a with dissolve
    play music ("music/SaveMe.ogg")
    "Subes a tu habitación a dejar tus cosas y aprovechas para jugar un rato a My Residence."
    "Hoy toca cita con Claire, la preciosa irlandesa que es la madre de la exnovia del protagonista."
    "Hay una tórrida escena en la ducha que crees que rejugarás varias veces en la galería."
    scene black with dissolve
    "Después de cenar, te retiras a tu habitación, donde lees unos documentos que [ama] te ha enviado sobre Iron Fist."
    "Tienes que estar preparado para la reunión de mañana en el yate."
    "Es información muy aburrida y te quedas dormido mientras la lees."
    centered "{size=+20}{b}DÍA 26 – SÁBADO{/b}{/size}"
    stop music fadeout (1.5)
    "Te levantas muy tarde, casi a mediodía. Debías estar más cansado de lo que creías."
    return
label c24s003_KiaDate:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_mar_route from _call_mrS3_mar_route_8
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_9
    scene black with dissolve
    "Subes a tu habitación a dejar tus cosas y lees unos documentos que [ama] te ha enviado sobre Iron Fist."
    "Tienes que estar preparado para la reunión de mañana en el yate."
    "Cuando se acerca la hora de tu cita, te das una ducha y te cambias. No sabes dónde vais a ir, con lo que eliges algo que pueda ir bien en casi cualquier sitio."
    scene c24s003_060b with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    kia "*A través de la puerta* Soy yo, ¿puedo pasar?"
    play music ("music/In-The-Rain.ogg")
    mc "Sí, pasa."
    scene c24s003_065d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c24s003_065" , "d") from _call_BlinkXPS3_1725
    mc "¡Wow, [kia]! ¡Estás preciosa!"
    kia "Gracias, [mc]. Tú también estás muy guapo."
    kia "¿Estás preparado para irnos?"
    mc "Cuando tú quieras. ¿Dónde vamos a ir? ¿Voy bien así?"
    call BlinkXPS3 ("c24s003_070" , "d") from _call_BlinkXPS3_1726
    kia "Estás perfecto."
    kia "Voy a ser la envidia de todas las mujeres."
    mc "Y a mí me van a envidiar todos los hombres vayamos donde vayamos."
    call BlinkXPS3 ("c24s003_075" , "d") from _call_BlinkXPS3_1727
    kia "*Risa* Van a pensar que sales a cenar con tu madre. Nada envidiable."
    if mar._var("route"):
        call BlinkXPS3 ("c24s003_080" , "d") from _call_BlinkXPS3_1728
        kia "¡Oh! No me refería a [mar] y a ti. Hacéis una pareja perfecta."
        mc "Ya lo sé. Entiendo a lo que te refieres y, aunque no seas mi madre, te aseguro que cualquier hombre querría estar en mi posición hoy."
    mc "Si piensan que eres mi madre y que además estamos saliendo juntos, más hombres aún me van a envidiar. Ya sabes, fetiche con el incesto..." id c24s003_KiaDate_b8ec88c3
    mc "La mitad de los hombres del mundo darían lo que fuera por tener una madre como tú y poder hacer esto con ella."
    scene c24s003_075d with dissolve
    "Sin dejarle reaccionar, la coges entre tus brazos y dejas que tus labios recorran los suyos."
    "Tras un segundo de sorpresa, la hermosa pelirroja entreabre su boca y deja que su lengua empiece a jugar con la tuya."
    call BlinkXPS3 ("c24s003_085" , "d") from _call_BlinkXPS3_1729
    kia "¡Hey! ¡Para! Tenemos una reserva para cenar, y quiero una cena tranquila."
    mc "*Risa* ¿Te pones nerviosa cenando?"
    call BlinkXPS3 ("c24s003_090" , "d") from _call_BlinkXPS3_1730
    kia "*Risa* No, idiota. Pero si empiezas así antes de que nos vayamos, no voy a poder pensar en otra cosa mientras cenamos."
    mc "Eres consciente de que, aunque estemos en un restaurante, podemos besarnos, ¿verdad?"
    call BlinkXPS3 ("c24s003_095" , "d") from _call_BlinkXPS3_1731
    kia "Sí, lo sé. Y seguramente te besaré. Pero no serán besos así."
    kia "Nunca me han gustado las parejas que se enrollan en público. Son cosas que se tienen que hacer en la intimidad."
    mc "Me parece bien. A mí nunca me han importado, pero si a ti no te gusta esperaré a disfrutar de tus labios."
    call BlinkXPS3 ("c24s003_100" , "d") from _call_BlinkXPS3_1732
    kia "Tengo pensado pedir una ensalada de aguacate, con lo que espero que te siga gustando la combinación con mi pintalabios."
    mc "Me gustaría aunque no llevaras pintalabios. Aunque no comieras aguacate."
    call BlinkXPS3 ("c24s003_105" , "d") from _call_BlinkXPS3_1733
    kia "Entonces vámonos antes de que te tenga que volver a besar."
    mc "Me tendrás que decir dónde vamos si tengo que conducir hasta allí. ¿O vamos a coger un Under?"
    call BlinkXPS3 ("c24s003_110" , "d") from _call_BlinkXPS3_1734
    kia "Conduzco yo. Le he pedido el coche a [mar]. Vamos a un par de sitios donde coger un Under sería complicado."
    mc "¡Oh! Eso quiere decir que no quieres revelar la sorpresa."
    scene c24s003_110d with dissolve
    kia "Exacto. Ya he dejado la bolsa y el bolso en el coche."
    mc "¿Bolsa? ¿Para qué necesitas una bolsa?"
    kia "Esa es la segunda sorpresa de esta noche."
    scene black with dissolve
    "[kia] conduce durante 20 minutos antes de aparcar el coche en lo que parece una viejo edificio."
    "Por alguna razón, acabas cargando con su bolso."
    call BlinkXPS3 ("c24s003_115" , "d") from _call_BlinkXPS3_1735
    "Cuando entráis al restaurante está totalmente vacío. Es muy pronto para cenar."
    kia "Ya hemos llegado. Creo que no debes conocer este sitio. Lo abrieron mientras estabas en Portland."
    kia "Y ninguna de las chicas lo conocía, con lo que seguramente no habrás venido nunca."
    mc "No, no he venido nunca. No sabía ni que habían hecho un restaurante en este viejo almacén."
    call BlinkXPS3 ("c24s003_120" , "d") from _call_BlinkXPS3_1736
    kia "Las fotos de internet parecían muy bonitas y le hacen justicia. Espero que te guste."
    mc "Me gustaría aunque fuera tu carrito de perritos calientes favorito."
    mc "Me importa estar aquí contigo. Me da lo mismo dónde sea 'aquí'."
    mc "Pero es pronto para cenar, ¿no?"
    call BlinkXPS3 ("c24s003_125" , "d") from _call_BlinkXPS3_1737
    kia "Quiero acabar de cenar pronto para llevarte a un sitio."
    mc "Eso suena interesante. ¿Es para ese sitio la bolsa?"
    kia "Sí, y no preguntes qué hay dentro."
    mc "*Risa* Estoy empezando a ponerme nervioso por esa sorpresa."
    call BlinkXPS3 ("c24s003_130" , "d") from _call_BlinkXPS3_1738
    kia "No hace falta que te pongas nervioso. Es uno de mis lugares favoritos de Newport. E ir esta noche contigo me apetece mucho."
    mc "Entonces vamos a cenar. Casi tengo ganas de ir a ver tu sitio favorito."
    scene c24s003_135a with fade
    $ wai = Character (_("Camarera"))
    wai "Buenas noches, perdón por la espera. ¿Tenían reserva?"
    kia "Sí, a nombre de [kia] Wellesley."
    wai "Sí, acompáñeme, por favor."
    call BlinkXPS3 ("c24s003_140" , "d") from _call_BlinkXPS3_1739
    "La camarera os acompaña a la mesa y os entrega los menús."
    mc "¿Wellesley?"
    kia "Sí. No pienso usar nunca más el apellido Lamb, si puedo evitarlo. Quiero recuperar mi apellido de soltera."
    mc "Me parece una gran idea. Creo que brindaré por ello en cuanto nos traigan el vino."
    call BlinkXPS3 ("c24s003_145" , "d") from _call_BlinkXPS3_1740
    kia "No voy a beber vino, [mc]. Hoy conduzco yo, y no quiero que la noche acabe con el coche de [mar] en la cuneta o nosotros detenidos."
    kia "Pero tú puedes beber si quieres."
    mc "No me apetece beber si no lo haces tú pero, si quieres, podemos pedir mosto. Veo que tienen en la carta. No es lo mismo, pero..."
    call BlinkXPS3 ("c24s003_150" , "d") from _call_BlinkXPS3_1741
    kia "Nunca lo he probado. ¿Sabe a vino?"
    mc "No. *Risa* Es mucho más dulce. Básicamente es zumo de uva."
    kia "*Risa* Entonces sí que lo he probado. Bebía mucho zumo de uva cuando era niña. Me gustaba. Y voy a cambiar la ensalada por filete."
    mc "Entonces no se hable más. Zumo de uva y filete para la señora. Echaré de menos el aguacate."
    "Miras la carta durante un momento."
    mc "Y zumo de uva y pollo para mí."
    call BlinkXPS3 ("c24s003_155" , "d") from _call_BlinkXPS3_1742
    "Después de que la camarera os tome nota..."
    kia "Llevo desde el día que comimos juntos queriendo salir a cenar contigo."
    mc "Han sido unos días muy ocupados. Siento que no haya podido ser antes."
    mc "¿Le has dicho a Geneviève que salimos a cenar? ¿Sigue pensando que me quiero aprovechar de ti?"
    call BlinkXPS3 ("c24s003_160" , "d") from _call_BlinkXPS3_1743
    kia "No, al menos no me ha dicho nada más. Cuando te fuiste se disculpó por meterse donde no le llamaban."
    kia "Pero no hemos vuelto a hablar de ti."
    mc "Cuando me fui pensé que quizás había sido un poco duro con ella. Solo estaba intentando cuidar de ti. Protegerte."
    call BlinkXPS3 ("c24s003_165" , "d") from _call_BlinkXPS3_1744
    kia "Sus intenciones eran buenas, [mc], pero la forma de hacerlo no."
    kia "No debería juzgarte sin conocerte. Y si te conociera..."
    call BlinkXPS3 ("c24s003_170" , "d") from _call_BlinkXPS3_1745
    if mc._var("relationships")>1:
        kia "*Risa* Si no estuviera recién casada y enamorada de su marido, habría que hacerle un hueco en el harén."
    else:
        kia "*Risa* Si no estuviera recién casada y enamorada de su marido, seguramente me pediría compartirte."
    kia "*Risa* Con lo que prefiero que no te conozca a fondo. Nos pasaríamos el día hablando de ti en la biblioteca."
    mc "*Risa* Lo dices como si las mujeres cayeran a mis pies a los cinco minutos de conocerme."
    call BlinkXPS3 ("c24s003_175" , "d") from _call_BlinkXPS3_1746
    kia "*Risa* Bueno, yo tardé cinco días viviendo en la misma casa. O en la de [nor] para ser más exactos."
    mc "Tú me conocías de antes. Sabías cómo era."
    call BlinkXPS3 ("c24s003_180" , "f") from _call_BlinkXPS3_1747
    "La camarera interrumpe vuestra conversación trayendo vuestro pedido. Continuáis en cuanto se va."
    kia "Aunque te conociera de antes, nunca me hubiera planteado estar aquí contigo."
    kia "No, [mc]. No eres el mismo chico que conocí. Hay que ver el hombre en el que te has convertido para entender lo que siento."
    mc "Gracias."
    call BlinkXPS3 ("c24s003_185" , "d") from _call_BlinkXPS3_1748
    kia "Y no solo me refiero a cómo eres conmigo o a las dos veces que te enfrentaste a Solomon."
    kia "Cómo trataste al Decano para defender a [mar]. Cómo solucionaste el tema con el antiguo novio de [eri]."
    kia "Cómo actuaste con el novio de la madre de [sca]. O cómo has solucionado lo de [bet]."
    call BlinkXPS3 ("c24s003_190" , "d") from _call_BlinkXPS3_1749
    kia "Todo eso no lo hace un chico. Son cosas que hace un hombre que toma las riendas cuando debe."
    mc "*Risa* Me vas a hacer ruborizar."
    mc "No lo he hecho todo solo. [mar] ayudó mucho con el Decano. [eva] y [ama] con Solomon y Kevin..."
    call BlinkXPS3 ("c24s003_195" , "d") from _call_BlinkXPS3_1750
    kia "A eso me refiero. No sólo haces lo que tienes que hacer. Nos das ejemplo a las demás y nos inspiras para que nosotras hagamos lo que debemos."
    mc "*Risa* ¡Joder, [kia]! Haces que parezca el líder de una secta."
    call BlinkXPS3 ("c24s003_200" , "d") from _call_BlinkXPS3_1751
    kia "Mas o menos. *Risa* Has creado una familia de elección a tu alrededor."
    if mc._var("relationships")>1:
        kia "Y no me refiero solo a las mujeres que estamos contigo. No eres el líder de esa familia. Pero eres el centro."
    else:
        kia "Y aunque no seas el líder de esa familia, pero eres el centro..."
    kia "Eres el factor común para todas nosotras. De [kat] a [mee], pasando por mí o por [mar]."
    mc "¿[kat]? Ella ya iba a venir a casa antes de que yo volviera de la universidad."
    call BlinkXPS3 ("c24s003_205" , "d") from _call_BlinkXPS3_1752
    kia "Sí, pero antes de que llegaran las chicas ya habías creado el ambiente que hay ahora."
    kia "Sólo con la familia cercana, pero suficiente para que fuera fácil que ellas se sumaran. Después nos hemos sumado el resto."
    mc "No hice nada de eso, [kia]. Me encanta que me veas así, pero no me puedo otorgar el mérito."
    mc "Además, estamos hablando mucho de la familia y poco de nosotros."
    call BlinkXPS3 ("c24s003_210" , "d") from _call_BlinkXPS3_1753
    kia "Me da un poco de miedo hablar de nosotros. Hablar de ello lo hace demasiado real."
    mc "¿Es por Solomon? ¿Porque aún sigues casada con él?"
    call BlinkXPS3 ("c24s003_215" , "d") from _call_BlinkXPS3_1754
    kia "En parte sí. Pese a que soy católica, no soy de esas que rechaza el divorcio, pero él sí. Nunca me lo va a dar."
    if mc._var("relationships")>1:
        kia "Y aunque me lo diera, tú y yo no nos vamos a poder casar nunca."
        kia "No sería justo que sólo una de nosotras se pudiera casar contigo, con lo que lo hemos hablado entre nosotras y ninguna va a aceptar casarse contigo."
    else:
        kia "Y eso hace que tú y yo no nos vayamos a casar nunca."
    mc "Se puede vivir una vida muy feliz sin estar casados, [kia]."
    call BlinkXPS3 ("c24s003_220" , "d") from _call_BlinkXPS3_1755
    kia "Lo sé, pero me educaron para casarme con el hombre de mi vida. Creí que era Solomon y resultó no serlo."
    kia "Y si al final lo eres tú, no podremos hacerlo."
    call BlinkXPS3 ("c24s003_225" , "d") from _call_BlinkXPS3_1756
    kia "No voy a decir que me entristezca tener una relación contigo sin estar casados, pero..."
    mc "Te entiendo. Pero tiene difícil solución."
    kia "Lo sé. Pero hablemos de cosas más alegres."
    call BlinkXPS3 ("c24s003_230" , "d") from _call_BlinkXPS3_1757
    kia "[bet] me ha explicado lo que has hecho con la Iglesia en Monterey."
    mc "*Risa* Tenías que haber visto la cara del pobre cura al final."
    kia "Soy católica, pero no me gustan muchas de las cosas que hace la Iglesia."
    "Empiezas a explicarle cómo ha ido la reunión. Ella ya lo sabe porque se lo ha explicado [bet], pero te escucha atentamente."
    "Disfrutando del cambio de conversación."
    scene c24s003_230d with dissolve
    "Cuando estás llegando al final de la explicación entra un grupo de ruidosos chicos, algo mayores que tú."
    "Todos se quedan mirando a [kia], que brilla como una estrella en el casi vacío restaurante."
    call BlinkXPS3 ("c24s003_235" , "d") from _call_BlinkXPS3_1758
    "[kia] se da cuenta de sus miradas y baja la suya."
    mc "Te he dicho que sería la envidia del restaurante."
    kia "No estoy acostumbrada..."
    mc "Estoy seguro de que los chicos del instituto te miran igual en la biblioteca que esos de ahí."
    call BlinkXPS3 ("c24s003_240" , "d") from _call_BlinkXPS3_1759
    kia "¡Qué va! Miran a Gen. Es mucho más joven que yo."
    mc "Puede que sea más joven, pero no te cambiaría por dos Genevièves. Ni siquiera para hacer un trío con ellas dos."
    mc "Ella es mona. Tú eres preciosa."
    call BlinkXPS3 ("c24s003_245" , "d") from _call_BlinkXPS3_1760
    kia "Ellos no deben pensar lo mismo. Nunca me han mirado, y no es que me importe. Casi lo prefiero."
    mc "Geneviève va maquillada al trabajo. Cada vez que te he visto ir a la biblioteca, excepto el día que quedamos para comer, ibas sin maquillaje."
    mc "Y no quiero decir que lo necesites para estar preciosa. Pero en igualdad de condiciones, estoy seguro de que nadie miraría a Geneviève."
    call BlinkXPS3 ("c24s003_250b" , "d") from _call_BlinkXPS3_1761
    kia "*Risita* Ahora voy maquillada todos los días. Por si decides pasarte por la biblioteca. Sé que te gusta." id c24s003_KiaDate_4db88899
    mc "Tendré que hacerlo más a menudo. Aunque solo sea para hacer esto."
    scene c24s003_250a with dissolve
    pause (1.0)
    scene c24s003_250b with dissolve
    "La besas sin avisarla. Lo que empieza como un dulce beso, acaba como el beso que os habéis dado en la habitación."
    "No puedes evitar desear abrir los ojos para ver la cara de los ruidosos chicos cuando oyes sus sonidos de sorpresa."
    "Pero después del primer segundo, no existen para ti. Tan solo existen vuestros labios y vuestras lenguas rozándose y jugando."
    "Escribiendo con saliva una carta de amor."
    call BlinkXPS3 ("c24s003_255" , "d") from _call_BlinkXPS3_1762
    mc "Creía que no te gustaban las parejas que se enrollan en público."
    kia "Y no me gustan, pero no sé si has oído al grupo de chicos. Se han sorprendido cuando me has besado."
    mc "Sí..."
    call BlinkXPS3 ("c24s003_265" , "d") from _call_BlinkXPS3_1763
    kia "Pues me ha encantado ese sonido."
    mc "*Risa* Por mí pueden sorprenderse todo lo que quieran. Soy el tío más afortunado en el restaurante."
    mc "En el mundo."
    call BlinkXPS3 ("c24s003_260" , "d") from _call_BlinkXPS3_1764
    kia "Además de eso..."
    mc "¿Qué?"
    kia "Hoy he entendido por primera vez a esas parejas. Me daba lo mismo que estuviéramos en público. Era como si sólo existiéramos tú y yo."
    mc "Es que solo existimos tú y yo, cielo."
    scene c24s003_250c with dissolve
    "Vuelves a besarla para demostrárselo."
    "Vuelve a besarte para decirte que está de acuerdo."
    "Esta vez no escucháis sonidos de sorpresa. No hay nadie para emitirlos."
    call BlinkXPS3 ("c24s003_270" , "d") from _call_BlinkXPS3_1765
    kia "Necesito beber algo... y recuperar el aliento."
    mc "La combinación del filete con tu pintalabios también está deliciosa."
    mc "Ahora me gustaría probarla con el mosto."
    scene c24s003_270d with dissolve
    "[kia] bebe un largo sorbo de mosto mientras aparta la mirada. Esperas que acabe para volver a besarla."
    call BlinkXPS3 ("c24s003_275" , "d") from _call_BlinkXPS3_1766
    kia "Creo que deberíamos dejar los besos para después. O se nos va a hacer tarde para ir donde te quiero llevar."
    kia "Allí podremos besarnos todo lo que quieras. No hay nadie nunca."
    mc "¿Pido la cuenta entonces?"
    call BlinkXPS3 ("c24s003_280" , "d") from _call_BlinkXPS3_1767
    kia "*Risa* ¿Tan ansioso estás? ¿No quieres postre?"
    mc "Voy a sonar cursi, pero acabo de besar los labios más dulces. Cualquier postre me sabrá soso."
    call BlinkXPS3 ("c24s003_285" , "d") from _call_BlinkXPS3_1768
    kia "*Risa* Pues sí, has sonado cursi. Pero me encanta."
    kia "Pide la cuenta mientras voy al lavabo. Seguro que me tengo que retocar el pintalabios."
    call BlinkXPS3 ("c24s003_290" , "d") from _call_BlinkXPS3_1769
    kia "No pagues. Hoy me toca a mí."
    mc "Pero..."
    scene c24s003_290d with dissolve
    "La preciosa bibliotecaria te da un suave beso indicando que no empieces una discusión que no vas a ganar."
    scene c24s003_290e with dissolve
    "Pides la cuenta y te das cuenta de que el restaurante sigue medio vacío. Aunque hayáis acabado de cenar, sigue siendo pronto."
    "Siempre te ha gustado hacer figuritas con la capa de estaño que protege el corcho."
    "Empiezas a juguetear con la cápsula del mosto mientras tu mente divaga, pensando en la conversación que habéis tenido."
    "La camarera trae la cuenta al mismo tiempo que [kia] vuelve del lavabo."
    scene c24s003_135b with fade
    "Cuando vuelve [kia]..."
    wai "¿Estaba todo a su gusto?"
    mc "Sí, todo perfecto."
    kia "Un sitio muy bonito y con una calidad excelente. Volveremos."
    call BlinkXPS3 ("c24s003_295" , "f") from _call_BlinkXPS3_1770
    "Después de que [kia] pague la cuenta, una vez en el coche..."
    mc "¿Siguiente parada?"
    kia "Ahí es donde está la sorpresa."
    mc "Tenía que intentarlo."
    call BlinkXPS3 ("c24s003_300" , "d") from _call_BlinkXPS3_1771
    kia "Aunque me gustaría explicártelo, no lo podrías entender hasta que lo vieras, con lo que prefiero llevarte allí."
    mc "Cada vez estás más misteriosa. *Risa*"
    kia "Allí te explicaré por qué me gusta ese sitio. Pero nos tenemos que ir ya o no llegaremos a tiempo."
    stop music fadeout (1.5)
    mc "Entonces vamos. Quiero saberlo todo de ti."
    if not _in_replay:
        call c24s003_KiaBeach from _call_c24s003_KiaBeach
    return
label c24s003_KiaBeach:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_rels from _call_mrS3_rels_10
    call BlinkXPS3 ("c24s003_305" , "f") from _call_BlinkXPS3_1772
    play music ("music/romantic-day.ogg")
    "[kia] conduce diez minutos por una carretera estrecha hasta llegar a un camino sin asfaltar cerca del mar, donde aparca el coche."
    "Ella coge su bolso y te toca cargar con la bolsa del maletero."
    mc "¿Aquí? ¿En medio de la nada?"
    kia "*Risa* No, tenemos que caminar un par de minutos."
    mc "Déjame llevar la bolsa."
    kia "Vale, pero no la abras."
    "Más misterios."
    scene c24s003_305d with fade
    "Tras dos minutos andando por el camino de tierra, puedes ver el que supones que es el lugar al que [kia] se refería."
    "Con el tiempo perfectamente medido, llegáis cuando el cielo empieza a teñirse de naranja con la puesta de sol."
    call BlinkXPS3 ("c24s003_310" , "d") from _call_BlinkXPS3_1773
    mc "¡Es precioso! No había estado nunca aquí."
    kia "Está escondido. Lo descubrí un día mirando mapas en internet. Marcaba que había un mirador y decidí venir a verlo."
    kia "Me gustó el sitio el primer día que vine. Me enamoré de él la primera vez que vine a ver la puesta de sol."
    kia "Hoy la marea está baja y es menos espectacular, pero sigue siendo muy bonito."
    kia "Vamos a aquella punta y déjame sacar una cosa de la bolsa."
    call BlinkXPS3 ("c24s003_315" , "f") from _call_BlinkXPS3_1774
    "Siendo una mujer previsora, ha traído una manta de picnic, en la que se sienta tras extenderla."
    mc "Hay un banco justo ahí detrás..."
    kia "*Risa* Siempre está lleno de cacas de gaviota. Por eso vengo con la manta."
    mc "*Risa* Ni me había fijado. Me hubiera llevado un montón de cacas a casa pegadas en los pantalones."
    call BlinkXPS3 ("c24s003_320" , "d") from _call_BlinkXPS3_1775
    "Te tumbas a su lado. Mirarla desde abajo, por una vez, te da una perspectiva diferente de su belleza."
    kia "*Risa* Por suerte vienes con una mujer previsora."
    mc "Una mujer que me tiene que explicar la historia de este sitio para ella, aparte de encontrarlo en un mapa por casualidad."
    call BlinkXPS3 ("c24s003_325" , "d") from _call_BlinkXPS3_1776
    kia "No es una historia alegre..."
    mc "Pero es tu historia. Quiero escucharla."
    call BlinkXPS3 ("c24s003_330" , "d") from _call_BlinkXPS3_1777
    kia "Lo descubrí el verano de hace seis años. Unos meses antes de que [eil.nick] y tú empezarais a salir."
    kia "Ella se fue dos semanas a un campamento de animadoras y estaba en casa sola con Solomon."
    kia "Por entonces Solomon bebía y estaba agresivo. No tanto como se puso después."
    mc "Recuerdo como empeoró durante el año siguiente..."
    call BlinkXPS3 ("c24s003_335" , "d") from _call_BlinkXPS3_1778
    kia "Exacto. Él trabajaba en el turno de tarde en la fábrica aquel verano, con lo que yo estaba sola en casa casi todo el día."
    kia "Por la mañana él dormía, se levantaba, iba a trabajar, volvía de noche y bebía hasta caer dormido."
    kia "En los días buenos."
    mc "Una vida de mierda que eligió él."
    kia "Sí, y que nos hacía pagar a [eil.nick] y a mí."
    call BlinkXPS3 ("c24s003_340" , "d") from _call_BlinkXPS3_1779
    kia "Pero a lo que iba... Cuando se iba a trabajar, no quería estar sola en casa. Me parecía opresiva."
    kia "Empecé a conducir sin rumbo fijo. Después de un par de días, empecé a buscar en internet sitios cerca de Newport donde no hubiera estado nunca."
    mc "Lo entiendo..."
    call BlinkXPS3 ("c24s003_345" , "d") from _call_BlinkXPS3_1780
    kia "Descubrí algunos sitios bonitos, pero ninguno como este. Se convirtió en mi lugar favorito."
    kia "Me daba... paz."
    kia "Aquí me sentía segura. Sola pero segura."
    call BlinkXPS3 ("c24s003_350a" , "d") from _call_BlinkXPS3_1781
    kia "Aquí nadie me decía que era una inútil ni me agarraba del pelo, llevándome por la casa para enseñarme lo que había hecho mal."
    call BlinkXPS3 ("c24s003_350b" , "d") from _call_BlinkXPS3_1782
    kia "Me podía imaginar navegando hacia la puesta de sol en un barco con [eil.nick]. Para no volver nunca."
    call BlinkXPS3 ("c24s003_355" , "d") from _call_BlinkXPS3_1783
    kia "Sé que es una tontería. El sueño de un ama de casa infeliz."
    kia "Pero me daba tranquilidad."
    mc "Lo entiendo, pero ¿por qué volver ahora que has dejado eso atrás?"
    call BlinkXPS3 ("c24s003_360" , "d") from _call_BlinkXPS3_1784
    kia "Porque, aunque sea un sitio que evoca recuerdos oscuros, hace que los recuerdos felices que estamos creando se vean más brillantes."
    kia "Y porque es un lugar precioso que quería compartir contigo."
    mc "Entonces deberíamos empezar a crear recuerdos felices aquí, ¿no?"
    call BlinkXPS3 ("c24s003_365" , "d") from _call_BlinkXPS3_1785
    kia "Estar aquí hoy, contigo, ya es un recuerdo feliz, aunque lo esté viviendo ahora mismo."
    mc "Pienso lo mismo. Pero me has prometido que habría besos aquí."
    call BlinkXPS3 ("c24s003_370" , "d") from _call_BlinkXPS3_1786
    kia "*Risa* Si empezamos a besarnos, nos perderemos la puesta de sol."
    mc "Prefiero mirarte a ti que a la puesta de sol. Además, aún queda mucho."
    call BlinkXPS3 ("c24s003_375" , "d") from _call_BlinkXPS3_1787
    kia "A mí me puedes mirar cuando quieras. La puesta de sol sólo dura un segundo."
    mc "Entonces déjame hacer algo antes de que se ponga el sol. Sé que puede parecerte una tontería."
    call BlinkXPS3 ("c24s003_380a" , "d") from _call_BlinkXPS3_1788
    kia "Ahora soy yo la que tiene curiosidad por lo que vas a hacer."
    mc "Antes has dicho que tú y yo no nos podríamos casar nunca. Porque Solomon nunca te dará el divorcio."
    call BlinkXPS3 ("c24s003_380b" , "d") from _call_BlinkXPS3_1789
    if mc._var("relationships")>1:
        mc "Y porque, aunque te lo diera, sería injusto que solo me casara contigo."
    else:
        mc "Y, aunque te lo diera, pasarían meses antes de que pudiéramos hacer algo así."
    kia "Sí. Pero lo entiendo, aunque me hubiera gustado si todo esto hubiera pasado en otras circunstancias."
    call BlinkXPS3 ("c24s003_385" , "d") from _call_BlinkXPS3_1790
    mc "Podemos crear nuestras propias circunstancias."
    kia "¿A qué te refieres?"
    scene c24s003_385d with hpunch
    mc "[kia] Wellesley, ¿quieres casarte conmigo aunque nunca lo legalicemos?"
    mc "Estaremos casados a nuestros ojos, aunque no lo estemos a los ojos del mundo."
    kia "¿QUÉ?"
    kia "¿De dónde has sacado un anillo?"
    mc "Del bolsillo..."
    call BlinkXPS3 ("c24s003_390" , "d") from _call_BlinkXPS3_1791
    kia "Me refiero... ¿Tenías esto planeado? ¿Has llevado un anillo todo este tiempo?"
    mc "No, cielo. Sé que es un muy cutre, pero lo he hecho con el estaño del tapón del mosto cuando has ido al lavabo."
    scene c24s003_390f with dissolve
    pause (1.0)
    call BlinkXPS3 ("c24s003_390" , "d") from _call_BlinkXPS3_1792
    mc "Mis dedos han empezado a jugar con el metal y ha salido un anillo. Mi subconsciente me ha dicho que tenía que pedirte que te casaras conmigo."
    scene c24s003_390d with hpunch
    kia "¡Sí quiero!"
    mc "Te prometo cambiarlo por uno de verdad en cuanto pueda."
    scene c24s003_390e with hpunch
    "Tu prometida se lanza a tus labios con una pasión desconocida hasta ese momento."
    call BlinkXPS3 ("c24s003_395" , "d") from _call_BlinkXPS3_1793
    kia "Sí quiero. No te puedes imaginar lo bonito que es lo que acabas de hacer."
    mc "Sólo es un anillo hecho con el estaño de una botella..."
    kia "No es el anillo. Es el hecho. Sabías que era importante para mí y lo has hecho."
    if mc._var("relationships")>1:
        call BlinkXPS3 ("c24s003_400" , "d") from _call_BlinkXPS3_1794
        kia "Pero tengo que poner una condición."
        mc "¿Cuál?"
        kia "Que yo no sea la única a quién se lo pidas."
        mc "Me parece una condición que puedo cumplir."
        mc "Y vuelve a demostrar lo maravillosa que eres."
        call BlinkXPS3 ("c24s003_405" , "d") from _call_BlinkXPS3_1795
        kia "¿Por qué?"
        mc "Porque en un momento importante para ti, lo que haces es pensar en otras personas."
        kia "Es lo lógico, ¿no? Somos una familia..."
        mc "Sí, es lo lógico. Pero no todo el mundo lo haría en tus circunstancias."
    else:
        mc "Lo que es importante para ti, es importante para mí."
    call BlinkXPS3 ("c24s003_410" , "d") from _call_BlinkXPS3_1796
    kia "¿Puedo volver a besar a mi prometido?"
    mc "Por supuesto, pero... ¿y la puesta de sol?"
    kia "Ya la veremos otro día."
    scene c24s003_415An with dissolve
    "Os empezáis a besar como si no hubiera un mañana, como si el tiempo se hubiera paralizado y el sol no se fuera a poner nunca."
    "No eres capaz de saber cómo es posible que acabarais ese beso con la misma ropa que lo empezasteis."
    "Tan solo recuerdas que fue uno de los besos más maravillosos de tu vida. Tu primer beso como prometido de alguien."
    "Y el sol se puso sin que os dierais cuenta."
    stop music fadeout (1.5)
    "Os da lo mismo."
    return
label c24s004_Eri_Dap_Kat_Nor:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_nor_route from _call_mrS3_nor_route_3
        call mrS3_rels from _call_mrS3_rels_11
        call mrS3_kat_rps (1, 5, 10) from _call_mrS3_kat_rps
        if not persistent.lesbian:
            call mrS3_kat_lesbian from _call_mrS3_kat_lesbian
    scene c24s004_005a with dissolve
    "Después de cenar, en la cocina de [nor]..."
    play music ("music/RhythmPlay.ogg")
    nor "Estoy muy contenta por Tía [bet]. Era injusto..."
    eri "Estoy de acuerdo. Querían aprovecharse de lo que creían que era un momento de vulnerabilidad de la tía."
    dap "Pero no contaban con [mc]. *Risita*"
    call BlinkXPS3 ("c24s004_010" , "d") from _call_BlinkXPS3_1797
    nor "¿Tenéis algún plan para el fin de semana?"
    call BlinkXPS3 ("c24s004_015" , "d") from _call_BlinkXPS3_1798
    dap "He quedado con [eva] para que me enseñe a disparar el domingo por la tarde. También vienen varias de las chicas."
    call BlinkXPS3 ("c24s004_020" , "d") from _call_BlinkXPS3_1799
    nor "¿Vas a ir tú también, [eri]?"
    call BlinkXPS3 ("c24s004_025" , "d") from _call_BlinkXPS3_1800
    eri "Me hubiera gustado ir. Ha alquilado un campo de tiro y podría haber estado bien, pero trabajo, con lo que quedaremos otro día."
    eri "Iremos al bosque, donde le enseñó a disparar a [mc]."
    call BlinkXPS3 ("c24s004_030" , "d") from _call_BlinkXPS3_1801
    nor "Ir con cuidado con las armas... No son juguetes."
    call BlinkXPS3 ("c24s004_035" , "d") from _call_BlinkXPS3_1802
    dap "Lo sabemos, Mamá. Creo que tú también deberías aprender a disparar."
    dap "Nunca puedes saber cuándo se repetirá otro secuestro, y creo que deberíamos tener armas en casa."
    call BlinkXPS3 ("c24s004_040" , "d") from _call_BlinkXPS3_1803
    eri "Yo creo que no son necesarias, pese a lo bien que fue que [eva] tuviera una pistola escondida cuando pasó lo de Solomon."
    call BlinkXPS3 ("c24s004_045" , "d") from _call_BlinkXPS3_1804
    nor "Yo pienso lo mismo. Yo ya sé disparar pero, si hubiera intentado hacer lo que hizo [eva], lo más probable es que le hubiera dado en la mano a Solomon."
    nor "O incluso sería más probable que hubiera matado a una ardilla en el bosque al otro lado de la calle. *Risa*"
    call BlinkXPS3 ("c24s004_050" , "d") from _call_BlinkXPS3_1805
    nor "[eva] y [ama] no van a ir a ningún sitio, con lo que creo que es mejor si son ellas las que se ocupan de las armas."
    nor "Es bueno que aprendáis, pero no me gustaría tener armas en casa."
    scene c24s004_005b with dissolve
    eri "Aparte de las que tiene [eva] escondidas, ¿no? *Risa*"
    nor "*Risa* Exacto. Aparte de esas."
    dap "Bueno, una vez nos enseñe a disparar, nos podría decir dónde están..."
    nor "*Risa* Entonces dejarían de estar escondidas. ¿Te imaginas a [emm] sabiendo dónde están las armas?"
    call BlinkXPS3 ("c24s004_055" , "d") from _call_BlinkXPS3_1806
    kat "Hola, chicas. ¿De qué habláis?"
    scene c24s004_005c with dissolve
    "Todas" "De armas."
    call BlinkXPS3 ("c24s004_060" , "d") from _call_BlinkXPS3_1807
    kat "¿Ah, de lo de [eva] el domingo? Va a ser divertido."
    kat "Al final [kim] también vendrá."
    call BlinkXPS3 ("c24s004_065" , "d") from _call_BlinkXPS3_1808
    dap "*Risa* Yo que tú iría con cuidado si [kim] está armada cerca de ti."
    call BlinkXPS3 ("c24s004_070" , "d") from _call_BlinkXPS3_1809
    kat "¿Por qué? Le he hecho un favor..."
    call BlinkXPS3 ("c24s004_075" , "d") from _call_BlinkXPS3_1810
    eri "Sí, probablemente, pero las formas no han sido las correctas y lo sabes, [kat]."
    eri "La podías haber puesto en una situación desagradable cuando no estaba preparada."
    call BlinkXPS3 ("c24s004_080" , "d") from _call_BlinkXPS3_1811
    kat "Si no lo hubiera hecho, le hubiera estado dando vueltas al mismo tema durante meses..."
    scene c24s004_085 with dissolve
    nor "Chicas, ¿me podéis dejar a solas con [kat] un momento?"
    scene c24s004_005d with dissolve
    dap "Sí, quiero acostarme pronto hoy."
    eri "No seas muy dura con ella, Mamá."
    call BlinkXPS3 ("c24s004_090" , "d") from _call_BlinkXPS3_1812
    kat "¿Tan malo ha sido lo que he hecho?"
    call BlinkXPS3 ("c24s004_095" , "d") from _call_BlinkXPS3_1813
    nor "Solo ha sido malo que lo hicieras sin consultarle a [kim] previamente."
    if nor._var("route"):
        if mc._var("relationships")>1:
            nor "Cuando ha venido a preguntarme si me importaría que entrara en el harén estaba muy enfadada."
        else:
            nor "Cuando ha venido a preguntarme si me importaría que intentara algo con [mc] estaba muy enfadada."
    else:
        nor "Cuando me ha contado lo que has hecho estaba muy enfadada."
    call BlinkXPS3 ("c24s004_100" , "d") from _call_BlinkXPS3_1814
    kat "Lo siento, supongo que debería disculparme..."
    call BlinkXPS3 ("c24s004_105" , "d") from _call_BlinkXPS3_1815
    nor "Como ha dicho [eri], el problema han sido las formas."
    nor "Imagínate que yo hago lo mismo contigo."
    call BlinkXPS3 ("c24s004_110" , "d") from _call_BlinkXPS3_1816
    kat "No es lo mismo, [nor]..."
    call BlinkXPS3 ("c24s004_115" , "d") from _call_BlinkXPS3_1817
    nor "¿Cuál es la diferencia? Tú también vas a darle vueltas al tema durante mucho tiempo, por lo que parece."
    nor "Y no me digas que es más complicado."
    call BlinkXPS3 ("c24s004_110" , "d") from _call_BlinkXPS3_1818
    kat "Es que es más complicado..."
    call BlinkXPS3 ("c24s004_120" , "d") from _call_BlinkXPS3_1819
    nor "¿Por qué? ¿Porque incluye a [kim] y a [mc] en tu caso?"
    nor "¿Te encierro con los dos en una habitación mañana? ¿O espero a saber si acaban juntos?"
    call BlinkXPS3 ("c24s004_125" , "d") from _call_BlinkXPS3_1820
    kat "Me moriría de vergüenza..."
    call BlinkXPS3 ("c24s004_130" , "d") from _call_BlinkXPS3_1821
    nor "Eso es lo que le ha pasado a [kim] esta mañana."
    nor "[deb.nick] lo podía hacer con [lis] porque son hermanas. Sabía cómo iba a reaccionar ella saliera lo que saliera de ese encierro."
    call BlinkXPS3 ("c24s004_135" , "d") from _call_BlinkXPS3_1822
    nor "No la has encerrado con [mc], pero sí con [mar], que es casi más importante para ella."
    nor "Y tú te podías imaginar la respuesta que iba a dar [mar], pero pese a todo has forzado una situación que no tenías derecho a forzar."
    call BlinkXPS3 ("c24s004_140" , "d") from _call_BlinkXPS3_1823
    kat "Pero es que... necesitaba forzarla..."
    call BlinkXPS3 ("c24s004_145" , "d") from _call_BlinkXPS3_1824
    nor "¿Por qué? ¿Crees que, si [kim] y [mc] acaban juntos, te vas a quitar a los dos de la cabeza?"
    call BlinkXPS3 ("c24s004_150" , "d") from _call_BlinkXPS3_1825
    kat "Sí, esa es la idea. Matar dos pájaros de un tiro..."
    kat "*Susurrando para sí misma* O dos esperanzas a la vez..."
    call BlinkXPS3 ("c24s004_155" , "d") from _call_BlinkXPS3_1826
    nor "Eso no va a funcionar, [kat]."
    nor "Si acaban juntos te empezarás a imaginar las posibilidades."
    nor "Y si no acaban juntos, seguirás como estás ahora mismo, pero habrás conseguido enfadar a [kim]."
    call BlinkXPS3 ("c24s004_160" , "d") from _call_BlinkXPS3_1827
    kat "Pero es que no sabes lo difícil que es compartir habitación con una de las mujeres más bonitas que he visto nunca."
    kat "Reír juntas, hacernos amigas... verla desnuda cada día..."
    call BlinkXPS3 ("c24s004_165" , "d") from _call_BlinkXPS3_1828
    nor "¿Y con [mc]? ¿Qué esperas conseguir con él? ¿Ya has conseguido aclararte?"
    call BlinkXPS3 ("c24s004_170" , "d") from _call_BlinkXPS3_1829
    kat "Ahí está el problema... yo era feliz mientras sólo me gustaban las mujeres..."
    if kat.rps>0:
        kat "Entonces llega [mc] y me empieza a tratar como una persona normal, y eso me desconcierta."
    else:
        kat "Entonces llega [mc] y, pese a que se ha comportado como un capullo muchas veces, me desconcierta."
    call BlinkXPS3 ("c24s004_175" , "d") from _call_BlinkXPS3_1830
    kat "Aún no sé si siento algo por él, o si tan solo estoy tan desconcertada con él que tengo la cabeza hecha un lío."
    kat "Pero si [kim] y él acaban juntos, en el fondo les habré hecho un favor... ¿no?"
    call BlinkXPS3 ("c24s004_180" , "d") from _call_BlinkXPS3_1831
    nor "Mi niña, las cosas no funcionan así."
    nor "Respóndeme a esta pregunta sin pensarlo. Si tuvieras que elegir entre estar con [kim] o estar con [mc], ¿qué escogerías?"
    call BlinkXPS3 ("c24s004_185" , "d") from _call_BlinkXPS3_1832
    "[kat] responde automáticamente, sin pensar."
    if kat.rps>0:
        if kat._var("lesbianContent") or persistent.lesbian:
            kat "Con los dos."
        else:
            kat "Con [mc]."
    else:
        kat "Con [kim]."
        kat "Y si [mc] fuera menos capullo, con los dos."
    call BlinkXPS3 ("c24s004_190" , "d") from _call_BlinkXPS3_1833
    nor "Ahí tienes la respuesta a tus dilemas. A veces, no pensar las cosas es la mejor forma de descubrir la respuesta adecuada."
    call BlinkXPS3 ("c24s004_195" , "h") from _call_BlinkXPS3_1834
    kat "¡Joder! ¿Así de fácil?"
    call BlinkXPS3 ("c24s004_200" , "d") from _call_BlinkXPS3_1835
    nor "Así de fácil. Dame un abrazo."
    if kat.rps>0 and nor._var("route"):
        nor "Aunque no lo necesites, tienes que saber que me alegrará si te unes al harén."
    scene c24s004_205a with dissolve
    kat "Gracias, [nor]."
    kat "¿Puedes hacer el mismo truco en mis exámenes y preguntarme cosas sobre las belugas? *Risa*"
    nor "*Risa* Creo que no funcionaría."
    scene c24s004_205b with dissolve
    nor "*Risa* Y creo que deberías sacar tu nariz de entre mis tetas."
    kat "*Risa* Yo también lo creo, pero... ¡Por el amor de Dios, [nor]!"
    scene c24s004_205a with dissolve
    "Ambas" "*Risa*"
    "Las dos mujeres pasan un rato abrazadas, entre silencios y risas."
    "[kat] por fin ha decidido qué es lo que quiere. Ahora solo necesita un plan para conseguirlo."
    stop music fadeout (1.5)
    return
label c24s003_KiaSex:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_rels from _call_mrS3_rels_12
    call BlinkXPS3 ("c24s003_425" , "d") from _call_BlinkXPS3_1836
    "De vuelta en la playa..."
    play music ("music/romantic-day.ogg")
    kia "¡Wow!"
    mc "¡Wow! *Risa*"
    call BlinkXPS3 ("c24s003_430" , "d") from _call_BlinkXPS3_1837
    kia "Creo que deberíamos irnos o va a empezar a hacer frío."
    mc "Estoy de acuerdo. Está refrescando."
    mc "Además llevo una hora clavándome una piedra en la espalda. *Risa*"
    call BlinkXPS3 ("c24s003_435" , "d") from _call_BlinkXPS3_1838
    kia "¿Por qué no has dicho nada? Podíamos habernos ido antes..."
    mc "Porque tenía la boca ocupada. *Risa* Y una piedra no iba a hacerme interrumpir ese beso."
    call BlinkXPS3 ("c24s003_440" , "f") from _call_BlinkXPS3_1839
    kia "Entonces vámonos ya."
    mc "¿A casa? ¿Quieres dormir en mi habitación esta noche?"
    call BlinkXPS3 ("c24s003_445" , "d") from _call_BlinkXPS3_1840
    kia "No. No vamos a casa. La última sorpresa de la noche es que tengo una habitación reservada para nosotros."
    mc "Me gustan tus sorpresas. *Risa* Aunque espero que no sea la última sorpresa. Vámonos."
    scene black with dissolve
    "Recogéis la manta y [kia] conduce durante 20 minutos hacia San Luis Obispo."
    "Llegáis a un bonito y pequeño hotel donde [kia] se vuelve a identificar con el apellido Wellesley."
    call BlinkXPS3 ("c24s003_450" , "d") from _call_BlinkXPS3_1841
    kia "Pues esta es la habitación. Puedes dejar la bolsa ahí. Tengo que ir a cambiarme al baño."
    mc "Pero habrá un beso antes de que te vayas, ¿no?"
    call BlinkXPS3 ("c24s003_455" , "d") from _call_BlinkXPS3_1842
    kia "No. *Risa* Me ha costado mantenerme vestida en la playa, y conociendo cómo besas, te quedarías sin ver lo que hay en la bolsa."
    mc "Creo que ahora mismo me acabas de plantear un dilema. ¿Besarte o ver lo que hay en la bolsa?"
    call BlinkXPS3 ("c24s003_460" , "d") from _call_BlinkXPS3_1843
    kia "*Risa* No te estaba dando a elegir. Si me prometes un beso corto, me arriesgaré a besarte antes de irme."
    mc "*Risa* Lo único que te puedo prometer es intentar que no sea un beso que empiece aquí y acabe en la cama."
    stop music fadeout (1.5)
    kia "*Risa* Me sirve si lo intentamos los dos."
    play music ("music/CCFunk.ogg")
    scene c24s003_465An with dissolve
    "Pese a la promesa, es imposible que vuestras manos no empiecen a recorrer vuestros cuerpos durante el beso."
    "De alguna forma, la diminuta [kia] te guía hasta la cama, donde se sienta a horcajadas encima tuyo para después tumbarte."
    "Tus manos empiezan a juguetear con su vestido durante el beso, desnudando su pecho, y esa es la señal de alarma para la preciosa pelirroja."
    call BlinkXPS3 ("c24s003_470" , "d") from _call_BlinkXPS3_1844
    kia "*Risa* Has incumplido tu promesa. Sabía que no podrías mantenerla."
    mc "*Risa* Yo solo he prometido intentarlo, no conseguirlo. Además, has sido tú quien me ha tumbado en la cama."
    scene c24s003_475AnBlink with dissolve
    kia "¿Una mujer tan pequeña como yo ha tumbado a un hombre como tú? *Risa* ¿Piensas que alguien te creería?"
    kia "Pues ahora te toca esperar. *Risa* Ponte cómodo y estaré de vuelta en dos minutos."
    scene c24s003_475An2 with dissolve
    kia "Ni se te ocurra seguirme."
    stop music fadeout (1.5)
    mc "*Risa* Van a ser dos minutos más largos que si mirara como gira la taza de leche en el microondas."
    scene c24s003_475i with dissolve
    play music ("music/CelticFlute.ogg")
    kia "*Desde el lavabo* *Risa* No lo van a ser. Supongo que vas a usar esos dos minutos para desnudarte."
    mc "*Risa* Me han sobrado un minuto y cuarenta segundos. Estoy tentado de ir a buscarte."
    kia "*Desde el lavabo* ¡Ni se te ocurra! Deja que una chica se arregle para ti. No tengas tanta prisa." id c24s003_KiaSex_d2a65dd5
    kia "*Desde el lavabo* ¡Mierda!"
    mc "¿Qué pasa?"
    kia "*Desde el lavabo* El anillo. Se ha enganchado y se ha abierto."
    mc "¿Quieres que vaya y lo arregle?"
    kia "*Desde el lavabo* ¡No! ¡Estoy a medio vestir todavía!"
    mc "¿Sólo medio? Déjate al menos el resto de la joyería. *Risa* Ahorraremos unos segundos. Esto se está haciendo muy largo."
    kia "*Desde el lavabo* ¡Estoy yendo lo más rápido que puedo, pero esto es incomodísimo de poner!"
    mc "*Risa* Espero que sea más fácil de quitar después."
    kia "*Desde el lavabo* *Risa* Supongo que lo será. Es casi como un puzzle. ¿Listo?"
    stop music fadeout (1.5)
    mc "*Risa* Llevo listo dos horas, no dos minutos."
    scene c24s003_420d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c24s003_420" , "d") from _call_BlinkXPS3_1845
    play music ("music/KindofGirl.ogg")
    kia "Me ha parecido oír que hay un hombre impaciente por aquí."
    mc "..."
    kia "¿Nada que decir?"
    mc "Me he quedado sin palabras. Estás increíblemente preciosa. Y sexy a rabiar."
    mc "Me encanta la lencería..."
    call BlinkXPS3 ("c24s003_480" , "d") from _call_BlinkXPS3_1846
    kia "Seguramente te gustará más cuando esté en el suelo, ¿no?"
    mc "*Risa* Me da lo mismo si es en el suelo o encima de la mesa."
    mc "Creo que voy a..."
    call BlinkXPS3 ("c24s003_485" , "d") from _call_BlinkXPS3_1847
    kia "*Jadeo* ¡Por el amor de Dios!"
    mc "¿Qué? ¿Qué pasa, [kia]?"
    kia "¡Eso! ¿Es real?"
    scene c24s003_485d with dissolve
    pause (1.0)
    mc "¿Mjolnir? Sí."
    call BlinkXPS3 ("c24s003_485" , "d") from _call_BlinkXPS3_1848
    mc "Se pone así cuando hay una mujer tan sexy como tú cerca."
    call BlinkXPS3 ("c24s003_490" , "d") from _call_BlinkXPS3_1849
    kia "Nunca he visto algo tan grande fuera de una porno..."
    mc "Mi católica prometida viendo porno... *Risa* ¡Qué traviesa!"
    call BlinkXPS3 ("c24s003_495" , "d") from _call_BlinkXPS3_1850
    kia "*Risita* Y puedo ser aún más traviesa si me dejas..."
    "La risa hace que se olvide del tamaño de Mjolnir y vuelva a aparecer la bibliotecaria sexy."
    mc "*Risa* ¿Significa eso que voy a tener que mantener las manos lejos de ti? No sé si compensa..."
    call BlinkXPS3 ("c24s003_500" , "d") from _call_BlinkXPS3_1851
    kia "Significa que te vas a quedar ahí sentadito como un buen chico. Te prometo que te compensará."
    mc "Si te vas a poner en plan bibliotecaria estricta, no deberías haberte quitado las gafas. *Risa*"
    scene c24s003_500An with dissolve
    kia "¡Oops! ¡Ahora vengo!"
    mc "¡No te vayas otra vez!"
    call BlinkXPS3 ("c24s003_510" , "f") from _call_BlinkXPS3_1852
    kia "¡Hush! En la biblioteca no se grita."
    mc "Como desees... ¿Pero puedo babear?"
    call BlinkXPS3 ("c24s003_510d" , "d") from _call_BlinkXPS3_1853
    kia "Siempre y cuando no lo hagas encima de los libros..."
    mc "Por suerte no hay libros por aquí, si no, no podría prometerte nada."
    call BlinkXPS3 ("c24s003_510e" , "d") from _call_BlinkXPS3_1854
    kia "Y por suerte, solo soy estricta con los malos estudiantes. Con los buenos chicos puedo ser muy buena."
    kia "¿Has sido un buen chico, [mc]?"
    mc "Creo que sí, pero a lo mejor soy parcial. Mi prometida podría darte una respuesta más objetiva."
    call BlinkXPS3 ("c24s003_510f" , "d") from _call_BlinkXPS3_1855
    kia "La he visto antes, en el lavabo. Me ha dicho que has sido MUY buen chico hoy."
    mc "¿Y eso merece algún premio? *Risa* ¿Me van a perdonar las multas por devolver libros tarde?"
    scene c24s003_510g with dissolve
    kia "No tienes ninguna multa pendiente, aunque te deberían multar por traer armas a la biblioteca."
    scene c24s003_510h with dissolve
    kia "Esta vez haré una excepción. También pasaré por alto que tu arma esté babeando porque no hay libros."
    mc "¿Cómo no va a babear teniendo delante la bibliotecaria más sexy de la historia?"
    scene c24s003_510i with dissolve
    "[kia] recoge un poco de líquido preseminal de la punta de tu polla y se lo lleva a la boca."
    call BlinkXPS3 ("c24s003_505" , "d") from _call_BlinkXPS3_1856
    kia "Sabroso."
    mc "Tenías razón en que podías ser más traviesa. Pero creo que ese no es el uniforme adecuado para una biblioteca."
    call BlinkXPS3 ("c24s003_510j" , "d") from _call_BlinkXPS3_1857
    "[kia] cada vez está más metida en el juego de roles y se lo está pasando muy bien."
    kia "¿Qué debería hacer, entonces? ¿Me lo quito? ¿O me pongo otra cosa más adecuada para el trabajo de bibliotecaria?"
    kia "Es un gran dilema."
    call BlinkXPS3 ("c24s003_510k" , "d") from _call_BlinkXPS3_1858
    kia "No me gustaría que me despidieran por no llevar la vestimenta adecuada..."
    mc "Entonces creo que te la deberías quitar. Después ya decidiremos."
    call BlinkXPS3 ("c24s003_510l" , "d") from _call_BlinkXPS3_1859
    kia "Pero puedo ver que uno de los chicos, el más guapo de la biblioteca, me está mirando libidinosamente."
    mc "Este chico te miraría así aunque llevaras un saco de patatas en vez de esa hermosa lencería."
    scene c24s003_510mAn with dissolve
    kia "¿Cómo me mirará ahora que parte de la lencería ha desaparecido?"
    mc "Asegurándose de que no hay ningún libro cerca, no le gustaría empezar a babear encima de uno y que la bibliotecaria se enfadara."
    call BlinkXPS3 ("c24s003_515a" , "d") from _call_BlinkXPS3_1860
    kia "¿Por qué tendría que enfadarse en vez de sentirse halagada?"
    kia "Hay muchos libros, pero la cara que tiene el chico ahora mismo es única."
    mc "Lo que es único es lo que el chico tiene delante ahora mismo."
    mc "Y creo que por decir esa frase te podrían expulsar del gremio de bibliotecarias. *Risa*"
    call BlinkXPS3 ("c24s003_515b" , "d") from _call_BlinkXPS3_1861
    kia "Bueno, entonces tendría que acudir a mi prometido. Es un experto en gestionar expulsiones."
    kia "Si ha podido vencer a la Iglesia, seguro que puede vencer a unas pobres bibliotecarias."
    mc "Si la sangre le llegara al cerebro en vez de tenerla concentrada en otro sitio..."
    scene c24s003_515cd with dissolve
    pause (1.0)
    call BlinkXPS3 ("c24s003_515c" , "d") from _call_BlinkXPS3_1862
    kia "Pobrecito. ¿Esta bibliotecaria te está haciendo sufrir mucho?"
    mc "¿Sufrir? ¡Es el mejor espectáculo que he visto nunca!"
    mc "Me estás matando de anticipación, pero ¿hacerme sufrir? ¡Ni en broma!"
    call BlinkXPS3 ("c24s003_515d" , "d") from _call_BlinkXPS3_1863
    kia "¿Quieres que lo acabe entonces?"
    mc "Aunque estoy deseando lo que viene después, estoy disfrutando cada segundo."
    mc "Continúa con lo que tenías pensado."
    call BlinkXPS3 ("c24s003_515e" , "d") from _call_BlinkXPS3_1864
    kia "*Risa* ¿Pensado? ¡Voy improvisando sobre la marcha!"
    mc "*Risa* Pues es la improvisación más sexy que he visto nunca."
    scene c24s003_515fa with dissolve
    kia "¿Te puedo contar un secreto?"
    mc "Todos los que quieras. Todos los que tengas" id c24s003_KiaSex_20eed5ce
    scene c24s003_515fb with dissolve
    pause (0.8)
    scene c24s003_515fc with dissolve
    kia "Yo también estoy deseando lo que viene después."
    mc "¡Wow!"
    call BlinkXPS3 ("c24s003_515g" , "d") from _call_BlinkXPS3_1865
    kia "¿Tanto te gusta mi culo? ¿No quieres que me gire por completo?"
    mc "Me encanta, pero estoy deseando verte desnuda."
    kia "*Risa* Ya estoy desnuda, cielo."
    mc "*Risa* Sin sangre en el cerebro no sé explicarme correctamente, pero sabes lo que quiero decir."
    scene c24s003_520d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c24s003_520" , "d") from _call_BlinkXPS3_1866
    kia "Lo sé, cielo."
    call addProfileImageS3 (8, "kiara_8", kia, _(": 15 - Especial"), "") from _call_addProfileImageS3_7
    mc "¡Wow!"
    kia "*Risa* No sé qué reacción esperaba, pero esa me sirve."
    mc "Estoy sin palabras... No sé dónde mirar. Me encanta todo..."
    scene c24s003_525AnBlink with dissolve
    kia "Eso tiene fácil solución. Observa bien."
    mc "Tendría que haberlo grabado en video. *Risa* Sigo sin saber dónde mirar."
    kia "Te lo tendré que repetir muchas veces entonces. Tendremos muchas noches para hacerlo."
    mc "Y nunca me cansaré de no saber dónde mirar."
    call BlinkXPS3 ("c24s003_530" , "d") from _call_BlinkXPS3_1867
    kia "Déjame quitarme los zapatos y estoy contigo."
    mc "¡Noooo! *Risa* ¡Los zapatos noooo!"
    kia "*Risa* Había oído que tenías un fetiche con los zapatos de tacón, pero no creía que fuera para tanto."
    mc "No es un fetiche, pero me encanta cómo te quedan y me gustaría que los continuaras llevando toda la noche."
    scene c24s003_535AnBlink with dissolve
    kia "*Risa* Esa es la definición de fetiche."
    mc "¿Las gafas también? ¿Ya ha desaparecido mi bibliotecaria?"
    call BlinkXPS3 ("c24s003_540" , "d") from _call_BlinkXPS3_1868
    kia "Sí, ahora solo quedo yo. Y las gafas van a estar más seguras encima de la mesa."
    mc "*Risa* ¿Tan salvaje va a ser el sexo?"
    call BlinkXPS3 ("c24s003_545" , "d") from _call_BlinkXPS3_1869
    "[kia] se sienta a horcajadas en tus piernas con la sonrisa más maravillosa del mundo dibujada en sus labios."
    kia "*Risa* Nunca se sabe. Y parece que te gusto con gafas, con lo que prefiero que no se rompan."
    mc "Cielo, me gustas con gafas y sin gafas, con ropa y sin ropa. Me gustas tú. Punto."
    scene c24s003_550An with dissolve
    "[kia] baja su cabeza para capturar tus labios entre los suyos."
    "El tiempo pasa volando, pero los segundos se detienen con cada uno de los roces de vuestras lenguas."
    "Vuestros labios juegan uno de los más bonitos juegos que cuatro labios pueden jugar."
    "Se hablan en silencio. Se rozan con ansia. Se aman con pasión."
    "El pintalabios de tu prometida sigue sabiendo increíblemente bien."
    call BlinkXPS3 ("c24s003_555" , "d") from _call_BlinkXPS3_1870
    kia "Creo que ha llegado el momento, ¿no?"
    mc "Solo si tú quieres. Me podría pasar la noche besándote y no echar de menos nada."
    call BlinkXPS3 ("c24s003_560" , "d") from _call_BlinkXPS3_1871
    kia "No te preocupes, cariño. Quiero."
    kia "Y tener a... ¿Mjolnir?... apretado entre nuestros estómagos, pulsando, me dice que tú también quieres que pase."
    stop music fadeout (1.5)
    mc "¿Cómo quieres hacerlo? No me has dicho qué posturas prefieres..."
    scene c24s003_565An with dissolve
    play music ("music/Sexy-Background-Music.ogg")
    kia "*GEMIDO* ¡OOOF! *JADEO*"
    "La preciosa MILF pelirroja se empala en tu polla en un movimiento inesperado. Notas cómo su vagina rodea tu astil en un abrazo apretado y húmedo."
    "Muy húmedo."
    call BlinkXPS3 ("c24s003_570" , "d") from _call_BlinkXPS3_1872
    kia "*Respiración entrecortada* Así. Quiero así."
    mc "Eso ha sido una sorpresa."
    call BlinkXPS3 ("c24s003_575" , "d") from _call_BlinkXPS3_1873
    kia "*Respiración entrecortada* Hacerte el striptease, los besos... notar cómo me miras... Me ha puesto muy cachonda."
    kia "*Respiración entrecortada* No podía esperar más..."
    mc "Si te soy sincero... yo hace rato que no podía esperar más. *Risa* Pero he disfrutado cada segundo de la espera."
    call BlinkXPS3 ("c24s003_580" , "d") from _call_BlinkXPS3_1874
    kia "*Risa* ¡No te rías! *Gemido* ¡Mjolnir se mueve cuando te ríes!"
    mc "*Risa* Pues se va a mover más aún."
    kia "*Risa* Ya lo sé, idiota. Sólo esperaba poder acostumbrarme antes de que lo hiciese."
    mc "Si necesitas tiempo, tómatelo. No tenemos ninguna prisa."
    scene c24s003_900pv with dissolve
    show c24s003_900v
    "La bibliotecaria empieza a mover sus caderas a un ritmo lento. Calmado. Impresionante."
    kia "*Gemido* No tienes prisa tú. *Jadeo* Yo estoy a punto de correrme sólo por tenerte dentro. *Gemido*"
    "Parece que cada uno de sus empalamientos está a punto de llevarte al orgasmo. Pero son demasiado lentos para eso."
    kia "*Jadeo* Me encanta... *Gemido* Te quiero... *Jadeo*"
    "Es la primera vez que dice que te quiere. La última barrera, aunque siempre la has considerado estúpida, se ha derribado."
    scene c24s003_910pv with dissolve
    hide c24s003_900v
    show c24s003_910v
    mc "Yo también te quiero, cielo."
    "Sus paredes interiores se cierran en un espasmo sobre tu astil al escucharlo. También es la primera vez que se lo dices."
    kia "*Gemido* Lo sé. *Jadeo*"
    "No se lo habías dicho, pero se lo habías demostrado. Un anillo roto en el baño es la muestra menos importante de ello."
    kia "*Jadeo* Me voy a casar contigo. *Gemido* Así que lo sé. *Jadeo*"
    "Otro espasmo la recorre. Se pone cada vez más húmeda. Su cuerpo empieza a tensarse."
    scene c24s003_915pv with dissolve
    hide c24s003_910v
    show c24s003_915v
    "Su vello pelirrojo, rozando suavemente tu estómago con cada uno de los movimientos de sus caderas, es una visión preciosa."
    kia "*Gemido* Estoy a punto de correrme. *Jadeo* No voy a poder aguantarlo más. *Gemido*"
    "El lento movimiento de sus caderas te acerca paso a paso a tu clímax, pero puedes notar que el suyo se acerca galopando."
    kia "*Gemido* ¡Corrámonos juntos! *Jadeo*"
    "Su cuerpo se tensa más todavía, sin perder el ritmo por ello."
    call OrgasmXS3 ("c24s003_585") from _call_OrgasmXS3_47
    kia "*GEMIDO* ¡SÍ! *JADEO* ¡POR EL AMOR DE DIOS! *GEMIDO*"
    "La MILF pelirroja parece romperse con un latigazo que recorre todo su cuerpo mientras su coño estruja tu polla."
    kia "*JADEO* ¡OH, DIOS MÍO! *GEMIDO* ¡ESTO ES INCREÍBLE! *JADEO*"
    "Sus movimientos se paran durante unos segundos mientras recupera la respiración."
    scene c24s003_905pv with dissolve
    hide c24s003_915v
    show c24s003_905v
    "Cuando los reanuda, siguen siendo igual de precisos, incluso más placenteros que antes. Sus paredes internas masajean tu polla con cada oleada de su clímax."
    kia "*GEMIDO* ¡ES EL MEJOR ORGASMO DE MI VIDA! *JADEO*"
    "No puedes saber cómo han sido los anteriores, pero te vas a asegurar de estar presente en cada uno de los que tenga a partir de ahora."
    "Puedes notar en tu astil que este es muy intenso. Esperas que este sea el peor de los que disfrute contigo."
    mc "Estoy a punto de correrme..."
    kia "*JADEO* ¡CÓRRETE DENTRO! *GEMIDO*"
    "No puedes evitar seguir sus órdenes. No quieres evitar seguirlas."
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("[kia] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ kia._var("pregnant", True)
                $ kia._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c24s003_590") from _call_OrgasmXS3_48
    hide c24s003_905v
    mc "¡Mpfft!"
    "Explotas en el interior de tu prometida, llenándola con tu semilla, en un orgasmo más intenso que cualquiera puedas recordar."
    kia "*GEMIDO* ¡DIOS! ¡DIOS! ¡DIOS! *JADEO* ¡HAY MUCHÍSIMA!"
    call BlinkXPS3 ("c24s003_595" , "f") from _call_BlinkXPS3_1875
    stop music fadeout (1.5)
    "Tu clímax es seguido unos segundos después por el final del de [kia], que se derrumba sin fuerzas sobre tu pecho."
    play music ("music/thinking-of-you.ogg")
    kia "*Respiración entrecortada* No me lo puedo creer... ha sido alucinante..."
    mc "Ha sido perfecto para nuestra primera vez."
    call BlinkXPS3 ("c24s003_600" , "d") from _call_BlinkXPS3_1876
    kia "*Risa* Tendremos que probar otro día si la segunda vez es igual de buena."
    mc "*Risa* ¿Otro día? ¿No va a haber segundo asalto?"
    call BlinkXPS3 ("c24s003_605" , "d") from _call_BlinkXPS3_1877
    kia "*Risa* No te rías de mí y de mi inexperiencia. Eso solo pasa en las novelas eróticas. Ni siquiera en el porno."
    kia "Los hombres necesitáis descansar. Por muy joven que seas, necesitas descansar igual."
    mc "Sí. Cinco minutos. Diez o quince si estoy muy cansado."
    kia "*Risa* Te he dicho que no te rías de mí..."
    call BlinkXPS3 ("c24s003_610" , "d") from _call_BlinkXPS3_1878
    kia "¡Lo estás diciendo en serio! ¡No está flácida!"
    mc "*Risa* Mjolnir no quiere perderse ni un momento de ti. No creo que baje en un buen rato."
    kia "¿¡¿Quieres hacerlo una segunda vez?!?"
    mc "Y una tercera y..."
    call BlinkXPS3 ("c24s003_615" , "d") from _call_BlinkXPS3_1879
    kia "Paso a paso, semental. Que yo tengo que trabajar mañana... y ni siquiera podría cabalgarte una segunda vez."
    mc "Para eso hay soluciones muy fáciles."
    call BlinkXPS3 ("c24s003_620" , "d") from _call_BlinkXPS3_1880
    kia "¿Cuáles?"
    mc "Que sea yo quien te monte. *Risa*"
    call BlinkXPS3 ("c24s003_625" , "h") from _call_BlinkXPS3_1881
    "Te retuerces mientras la levantas y, sin salir de dentro de la preciosa católica, la tumbas sobre su espalda."
    kia "¡Hey! ¡No soy una muñeca para que me muevas así!"
    mc "*Risa* Pero te ha gustado que lo haga, ¿verdad?"
    call BlinkXPS3 ("c24s003_630" , "d") from _call_BlinkXPS3_1882
    kia "*Risita* Me ha encantado."
    kia "Ahora solo falta que demuestres que no fanfarroneabas con lo del segundo asalto."
    mc "¿No puede un pobre hombre descansar un poco?"
    stop music fadeout (1.5)
    kia "*Risita* Sabía que era una fanfarronada..."
    scene c24s003_635An with dissolve
    play music ("music/Sexy-Background-Music.ogg")
    "Coges a [kia] de los tobillos haciendo que su agujero se alinee mejor con tu polla y, con un movimiento de cadera, acabas de meter a Mjolnir hasta el fondo." id c24s003_KiaSex_4bb63023
    kia "*GEMIDO* ¡OOOF! *JADEO*"
    mc "*Risa* ¿Fanfarronada?"
    call BlinkXPS3 ("c24s003_640" , "d") from _call_BlinkXPS3_1883
    kia "*Respiración entrecortada* ¿Eso es... un segundo asalto... para ti? *Risita* ¡Vaya... decepción! *Gemido*"
    mc "*Risa* Si no fuera por el gemido al final, casi me lo hubiera creído."
    kia "*Respiración entrecortada* Es imposible... contenerlos... teniéndote dentro... *Jadeo*"
    mc "Voy a empezar a moverme."
    scene c24s003_920pv with dissolve
    hide c24s003_915v
    show c24s003_920v
    "Empiezas a bombear con tus caderas mientras aguantas casi todo el peso de [kia] por sus tobillos. Su cuerpo solo apoyado en la cama por la parte superior de su espalda."
    mc "¿Mejor así?"
    kia "*Gemido* ¡Fantástico! *Jadeo* ¡Te noto en la boca del útero! *Gemido*"
    "No sabías si la posición le resultaría cómoda, pero para ti es increíble. El ángulo de entrada de tu polla hace que tu capullo golpee en zonas donde no lo hacía antes."
    kia "*Jadeo* ¡No me lo puedo creer! *Gemido* Me he prometido a un semental. *Jadeo*"
    "Si piensa así en el segundo asalto, estás deseando que descubra que el tercero también existe."
    scene c24s003_925pv with dissolve
    hide c24s003_920v
    show c24s003_925v
    "Mjolnir ha encontrado un nuevo y cómodo hogar. Húmedo. Muy húmedo. Pero hecho a medida para él."
    kia "*GEMIDO* ¡Ese ángulo me encanta! *JADEO* ¡Dios mío! *GEMIDO*"
    "Sus gemidos son más fuertes que antes, estando sensible de la posición y el orgasmo anterior. No es diferente para ti. Casi puedes contar con tu glande cada uno de sus pliegues."
    kia "*JADEO* ¡No quiero que acabe! *JADEO*"
    "¿Significa eso que está a punto de correrse? Porque, estando tan sensible como estás, no vas a durar mucho más."
    "No has salido de ella desde que se ha empalado en Mjolnir, y estás empezando a notar los efectos."
    scene c24s003_930pv with dissolve
    hide c24s003_925v
    show c24s003_930v
    "Su coño empieza a abrazarte con fuerza, como hizo antes, anunciando que su clímax se está acercando."
    kia "*GEMIDO*"
    "Sin fuerzas para hablar, por su rostro van pasando todas las sensaciones que experimenta. Todas las sensaciones compartidas."
    kia "*JADEO*"
    "Su túnel se cierra más todavía. Te acerca a tu orgasmo inexorablemente. Tú tampoco quieres que acabe, pero no vas a poder evitarlo."
    kia "*GEMIDO* ¡ME CORROOOO! *JADEO*"
    "Su coño se cierra como un puño alrededor de tu astil. Una maravillosa presión en toda la longitud de tu polla que se mueve en oleadas hasta tu glande."
    if persistent.pregnancy and not kia._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[kia] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ kia._var("pregnant", True)
                $ kia._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c24s003_645") from _call_OrgasmXS3_49
    mc "¡Mpfft!"
    "Vuestros orgasmos llegan prácticamente a la vez. El suyo provocando el tuyo. El tuyo potenciando el de ella."
    kia "*GEMIDO* ¡SÍ! *JADEO* ¡DIOS MÍO! *GEMIDO* ¡MÁS!"
    "No sabes si se refiere a que continúes o a que quiere más de tu semilla. Te decides por lo primero, mientras queden fuerzas."
    scene c24s003_930pv with dissolve
    show c24s003_930v
    "Continúas bombeando, cada vez más sensible, notando cómo la humedad de [kia] se mezcla con tu semen dentro de ella."
    kia "*GEMIDO* ¡NO TENGO FUERZAS...! *JADEO* ¡...PARA EL TERCER ASALTO! *GEMIDO*"
    "Desgraciadamente, no es el tercer asalto sino los últimos coletazos del segundo. Vas a necesitar un poco de descanso antes de un posible tercero."
    scene c24s003_645An with fade
    hide c24s003_930v
    "Sales del interior de [kia] y observas hipnotizado tu obra. Te sorprende el poco semen que sale de su coño después de haber recibido dos corridas."
    kia "*Respiración entrecortada* ¿Siempre es así?"
    stop music fadeout (1.5)
    call BlinkXPS3 ("c24s003_650" , "f") from _call_BlinkXPS3_1884
    "Te tumbas al lado de la preciosa mujer. Ella arquea la espalda, disfrutando de los últimos espasmos de su orgasmo mientras realza sus hermosas tetas."
    play music ("music/thinking-of-you.ogg")
    mc "Bueno, a veces me corro más y a veces menos..."
    kia "*Respiración entrecortada* Me refiero a si siempre es tan bueno contigo. Es la primera vez en mi vida que tengo dos orgasmos."
    kia "*Respiración entrecortada* Y ni siquiera sabía que era posible un segundo asalto... y menos aún tan seguidos."
    mc "La mayoría de las veces tengo que descansar un poco más que hoy."
    call BlinkXPS3 ("c24s003_655" , "d") from _call_BlinkXPS3_1885
    kia "*Risa* Debe ser el poder del anillo."
    mc "*Risa* Es posible. Es la primera vez que hago el amor estando prometido."
    kia "Ahora habrá que buscar un anillo para ti. Quiero que todo el mundo sepa que eres mío. Y que yo soy tuya."
    if mc._var("relationships")>1:
        call BlinkXPS3 ("c24s003_660" , "v") from _call_BlinkXPS3_1886
        kia "¡Oh! ¡Me acabo de dar cuenta!"
        mc "¿De qué?"
        kia "Si cada una te damos un anillo... vas a ser el Señor de los Anillos."
        mc "*Risa* Por suerte no son pendientes o me podrían confundir con el tipo malo del libro ese de Frodu y Gandalfo."
        call BlinkXPS3 ("c24s003_655" , "d") from _call_BlinkXPS3_1887
        kia "*Risa* Tienes razón. Y podrían venir a denunciarte por infracción de copyright."
    mc "Cuando vayamos a sustituir tu anillo de estaño, podemos comprar uno a juego para mí."
    kia "Me parece una idea fabulosa. Aunque conservaré el anillo que me has dado."
    call BlinkXPS3 ("c24s003_665" , "d") from _call_BlinkXPS3_1888
    kia "No sé si te has dado cuenta de una cosa..."
    mc "¿De qué?"
    kia "Nos hemos dicho que nos queríamos por primera vez mientras hacíamos el amor..."
    mc "¿Te molesta que haya sido así la primera vez que nos lo hemos dicho?"
    call BlinkXPS3 ("c24s003_670" , "d") from _call_BlinkXPS3_1889
    kia "No. Ha sido una noche maravillosa. Mucho mejor de lo que hubiera podido imaginar. Y el sexo no tiene nada que ver con ello."
    kia "Ya era la mejor noche de mi vida antes de entrar en la habitación."
    kia "Lo decía por si te había molestado a ti... No sé a lo que estás acostumbrado."
    mc "No, cielo. Me ha parecido muy bonito. En ese momento solo se puede ser sincero."
    mc "Es un poco raro que nos lo hayamos dicho la primera vez así, pero no por ello ha sido menos bonito."
    mc "Nunca he entendido por qué la gente le da tanta importancia a la frase en vez de a los hechos."
    call BlinkXPS3 ("c24s003_675" , "d") from _call_BlinkXPS3_1890
    kia "Estoy de acuerdo. Me gusta pensar que nos lo hemos estado diciendo durante toda la noche. Con las miradas, con las caricias, con los besos..."
    kia "Tan solo lo hemos verbalizado."
    mc "Es una forma muy romántica de verlo. Y pienso que tienes razón. A veces no hace falta decir las palabras para leer los sentimientos."
    mc "Pero después de lo que acabas de decir, no me vuelvas a llamar cursi nunca. *Risa*"
    call BlinkXPS3 ("c24s003_680" , "d") from _call_BlinkXPS3_1891
    kia "*Risa* ¡Idiota! ¿Me estás llamando cursi después de lo bonito que me ha quedado?"
    mc "*Risa* Sí, mi preciosa bibliotecaria cursi."
    kia "*Risa* Pero te ha gustado que me ponga cursi tanto como me gusta a mí cuando lo haces tú, ¿verdad?"
    mc "*Risa* Exactamente lo mismo. Ha sido precioso. ¡Vaya par de cursis somos!"
    scene c24s003_680d with dissolve
    "Tu preciosa prometida te vuelve a decir 'Te quiero' otra vez sin palabras. Solo labios. Lenguas. Alientos compartidos."
    "Pasará mucho tiempo hasta que volváis a verbalizarlo. No es necesario."
    call BlinkXPS3 ("c24s003_685" , "f") from _call_BlinkXPS3_1892
    kia "Voy a darme una ducha rápida... Huelo a sexo..."
    mc "No sabía que fuera un olor desagradable."
    kia "No lo es, pero quiero oler a limpio cuando durmamos juntos la primera vez."
    mc "Vale. Te espero aquí."
    stop music fadeout (1.5)
    if not _in_replay:
        call c24s003_KiaSex2 from _call_c24s003_KiaSex2
    return
label c24s003_KiaSex2:
    scene c24s003_685d with fade
    "Al poco tiempo escuchas cómo se abre el agua de la ducha. Pasas un rato mirando la chimenea."
    "Al cabo de tres o cuatro minutos..."
    play music ("music/KindofGirl.ogg")
    kia "*Desde el baño* [mc], ¿puedes venir un momento?"
    mc "¡Voy!"
    call BlinkXPS3 ("c24s003_690" , "f") from _call_BlinkXPS3_1893
    "Vas hacia el baño, donde observas por unos segundos a [kia], que no se ha dado cuenta de tu presencia."
    "Su piel y cabello mojado le proporcionan una belleza diferente, no por ello menos hermosa."
    call BlinkXPS3 ("c24s003_695" , "d") from _call_BlinkXPS3_1894
    "Decides entrar antes de que te vea allí, observándola, y piense que eres un pervertido. Porque no lo eres, ¿verdad?"
    kia "Te has tomado tu tiempo..."
    mc "Estaba..."
    kia "Mirándome."
    mc "Sí."
    kia "Tan solo te llamaba por si querías compartir la ducha, pero si necesito convencerte..."
    call BlinkXPS3 ("c24s003_700" , "d") from _call_BlinkXPS3_1895
    kia "¿Me acerco más? ¿Así, apretada contra la mampara?"
    mc "¿Estás intentando seducirme?"
    kia "¿Necesito hacerlo?"
    mc "No."
    call BlinkXPS3 ("c24s003_705" , "d") from _call_BlinkXPS3_1896
    kia "¿O así? Ya que antes no sabías dónde mirar..."
    mc "Sigo sin decidirme."
    kia "Yo preferiría que no hubiera un cristal entre nosotros."
    mc "Entonces, déjame entrar en la ducha."
    scene c24s003_705d with fade
    "Nada más entrar en la ducha, [kia] se lanza hacia tus labios, en un apasionado beso."
    "Hace tan solo cinco minutos que ha abandonado la habitación, pero vuestros labios ya se echan de menos."
    "El agua continúa cayendo de la ducha, humedeciendo vuestros cuerpos, mientras vuestras húmedas lenguas vuelven a jugar."
    call BlinkXPS3 ("c24s003_710" , "d") from _call_BlinkXPS3_1897
    mc "Creo que ya he decidido dónde prefiero mirar."
    kia "¿Dónde?"
    mc "A tu ojos, cuando me miras así."
    mc "Cursi, lo sé."
    kia "Y precioso."
    call BlinkXPS3 ("c24s003_715" , "d") from _call_BlinkXPS3_1898
    kia "Como has dicho antes, somos un par de cursis, pero me encanta serlo contigo, y que tú lo seas conmigo."
    mc "Ahora mismo no me apetece ser cursi con nadie más, aunque la bibliotecaria de antes era más una come hombres que alguien cursi."
    call BlinkXPS3 ("c24s003_720" , "d") from _call_BlinkXPS3_1899
    kia "¿Puedo decirte una cosa?"
    mc "Siempre podrás decirme lo que quieras, cielo."
    kia "Estaba aterrada cuando he empezado a actuar así... Nunca había hecho algo así... No quería parecer ridícula."
    mc "¿Por qué lo has hecho, entonces?"
    call BlinkXPS3 ("c24s003_725" , "d") from _call_BlinkXPS3_1900
    kia "[eil]. Dijo que te gustaría algo así... Bueno, no exactamente así... Me dijo que jugara el rol de bibliotecaria estricta."
    kia "La lencería también ha sido idea suya, una que me pudiera quitar por piezas. Le pedí a [emm] que comprara algo en Monterey si encontraba algo que creyera que te iba a gustar" id c24s003_KiaSex2_2c68b303
    mc "*Risa* Me conocen muy bien. Me ha encantado todo. La actuación y la lencería." id c24s003_KiaSex2_66dc35c9
    mc "Pero se te veía muy metida en el papel. No me puedo creer que no lo hayas disfrutado."
    call BlinkXPS3 ("c24s003_730" , "d") from _call_BlinkXPS3_1901
    kia "*Risa* Ha sido divertidísimo. Sexy y divertido. Tal como me iba metiendo en el papel me iba gustando más."
    kia "He descubierto una faceta de mí misma que no conocía. He pasado de estar asustada a confiada. Y me ha encantado."
    call BlinkXPS3 ("c24s003_735" , "d") from _call_BlinkXPS3_1902
    kia "Tus miradas han ayudado mucho. Poder leer en tus ojos cómo me deseabas ha sido... tórrido."
    mc "La felina come hombres era muy sexy, pero la gatita cursi también lo es."
    mc "Por suerte, no tengo que elegir. Puedo tenerlas a las dos en la misma persona."
    call BlinkXPS3 ("c24s003_740" , "d") from _call_BlinkXPS3_1903
    kia "Puedo ser quien quieras que sea."
    mc "Solo hay una persona que quiero que seas. Tú misma. Quién tú quieras ser en cada momento."
    scene c24s003_740An with hpunch
    "[kia] salta a tus brazos, rodeándote con las piernas mientras vuelve a besarte apasionadamente. Giras sobre ti mismo para apoyar su espalda contra la mampara."
    "Es una mujer maravillosa que tan solo necesitaba que alguien le dijera que es lo suficientemente buena siendo quién es. No necesita nada más."
    "Te alegras de ser tú quien se lo haya dicho."
    call BlinkXPS3 ("c24s003_745" , "d") from _call_BlinkXPS3_1904
    kia "No puedes llegar a imaginar lo que significa eso para mí. Que alguien quiera que sea... como soy."
    mc "No estaríamos aquí si no quisiera que siguieras siendo como eres. No quiero cambiar nada de ti."
    mc "Soy un hombre simple. Te he pedido que te cases conmigo esperando que no cambies nunca."
    call BlinkXPS3 ("c24s003_750" , "d") from _call_BlinkXPS3_1905
    kia "*Risa* Sabes que las mujeres nos casamos esperando cambiar... o pulir... al hombre con el que nos casamos, ¿verdad?"
    mc "*Risa* Y sabes que nunca lo conseguís, ¿verdad?"
    call BlinkXPS3 ("c24s003_755" , "d") from _call_BlinkXPS3_1906
    kia "No te preocupes. Yo tampoco quiero cambiar nada de ti."
    mc "*Risa* Te acabas de ahorrar un montón de frustración."
    call BlinkXPS3 ("c24s003_760" , "d") from _call_BlinkXPS3_1907
    kia "Y una de las cosas que no quiero cambiar es que nuestros besos te dejen así."
    mc "¿Así cómo?"
    scene c24s003_770pv with dissolve
    kia "Así."
    mc "Llevo así casi desde que he estado observándote ahí fuera."
    call BlinkXPS3 ("c24s003_760" , "d") from _call_BlinkXPS3_1908
    kia "Parece que no eres el único que mira a los ojos... Ni me había dado cuenta."
    mc "Eso quiere decir que ahora estoy con la gatita cursi. Me encanta."
    mc "Y me encantaría hacerle el amor."
    call BlinkXPS3 ("c24s003_765" , "d") from _call_BlinkXPS3_1909
    kia "Ya se lo has hecho a la bibliotecaria come hombres y al ama de casa sin experiencia. Creo que es justo que la gatita reciba su ración."
    mc "¿Tienes tantas ganas como yo? No sabías que el segundo round fuera posible, y ahora estamos a punto del tercero."
    stop music fadeout (1.5)
    kia "Sí. No sé cuántas ganas tienes tú, pero no se pueden tener más ganas de las que tengo yo ahora mismo."
    play music ("music/SexyLoungeMusic.ogg")
    scene c24s003_770pv
    show c24s003_770v
    pause (0.5)
    scene c24s003_770dv
    hide c24s003_770v
    "Vuelves a penetrar, por tercera vez en la noche, a la hermosa gatita cursi."
    "La humedad de la ducha no es nada comparada con la que recibe a Mjolnir en su nuevo hogar."
    kia "*JADEO* ¡OOOF! *JADEO* ¡No creo que me acostumbre nunca a esto! *GEMIDO*"
    call BlinkXPS3 ("c24s003_775" , "d") from _call_BlinkXPS3_1910
    mc "¿Estás bien?"
    kia "*Jadeo* Mejor que bien... pero cada vez que me empalas me parece que me voy a romper por un segundo... *Jadeo*"
    kia "Soy tan pequeñita en comparación a tu tamaño..."
    mc "*Risa* El tamaño no importa."
    scene c24s003_940pv
    show c24s003_940v
    "Empiezas un lento bombeo mientras sujetas a la hermosa bibliotecaria contra el cristal de la mampara."
    kia "*Gemido* ¡Aún no estaba preparada! *Jadeo* ¡No me dejes estarlo nunca! *Gemido*"
    "Los sonidos del agua de la ducha se mezclan con sus gemidos y con el ruido que hacen vuestros húmedos cuerpos al chocar."
    kia "*Jadeo* ¡Oh, Dios mío! *Gemido* ¡Sigue así! *Jadeo*"
    "No puedes saber si [kia] está más húmeda por fuera o por dentro."
    scene c24s003_935pv
    hide c24s003_940v
    show c24s003_935v
    "Sus jugos se mezclan con el agua de la ducha, resbalando por tu astil. No sabrías decir si las gotas que recorren tus piernas son suyas o de la ducha."
    kia "GEMIDO* ¡Me voy a volver a correr! *JADEO* ¡NO ME LO PUEDO CREER! *GEMIDO*"
    "Ya no te sorprende nada de esta mujer, ni siquiera la velocidad a la que está a punto de llegar a su tercer orgasmo de la noche."
    kia "*JADEO* ¡AGUANTAME FUERTE! *GEMIDO* ¡ME CORROOOO! *JADEO*"
    "A ti te queda mucho todavía. Va a ser una nueva experiencia saber hasta dónde vas a poder llevarla esta vez."
    call OrgasmXS3 ("c24s003_780") from _call_OrgasmXS3_50
    kia "*GEMIDO* ¡POR EL AMOR DE DIOS! *JADEO* ¡SÍ! *GEMIDO*"
    "Sus músculos se tensan a tu alrededor. Alrededor de tu cuello. Alrededor de tu culo. Alrededor de tu polla."
    "Te sientes aprisionado en un abrazo múltiple y simultáneo que te estruja por todas partes."
    "¿Abrazos de oso? ¡Son unos animalitos novatos y angelicales cuando se trata de dar abrazos si se comparan con [kia]!"
    scene c24s003_945pv
    hide c24s003_935v
    show c24s003_945v
    "Continúas bombeando en cuanto la madre de [eil] libera la presión sobre tus caderas, sus piernas colgando flácidas."
    kia "*JADEO* ¡NO PUEDO AGUANTAR MÁS AQUÍ ARRIBA! *GEMIDO*"
    "Notas como la presión de su brazo en tu cuello va desapareciendo, sus fuerzas agotadas por el orgasmo."
    kia "*GEMIDO* ¡Bájame al suelo, por favor! *JADEO* ¡Me voy a caer! *GEMIDO*"
    "Casi se aguanta en exclusiva por la presión del cristal en su espalda y de Mjolnir en su coño. Decides hacerle caso."
    scene c24s003_950pv with fade
    hide c24s003_945v
    show c24s003_950v
    "Pero no por ello dejas de bombear cuando sus pies tocan el suelo. Ahora que no tienes que aguantar su peso, puedes acelerar tus movimientos."
    kia "*JADEO* ¡ESTO ES DIFERENTE! *GEMIDO* ¡ES INCLUSO MEJOR! *JADEO*"
    "Agarrada a tus caderas para notar mejor el ritmo, lo único que tiene que hacer es disfrutar del placer que Mjolnir le provoca."
    kia "GEMIDO* ¡VOY A VOLVER A CORRERME! *JADEO* ¡NO ME LO PUEDO CREER! *GEMIDO*"
    "¿También va a descubrir hoy que se puede tener más de un orgasmo en una sola relación?"
    scene c24s003_960pv
    hide c24s003_950v
    show c24s003_960v
    "Aceleras un poco más todavía, intentando llevarla a su segundo orgasmo y acercarte al tuyo."
    kia "*GEMIDO* ¡JODER! *JADEO* ¡EXISTE! *GEMIDO* ¡JODER, JODER, JODER! *JADEO*"
    "Ella descubre que existe la multiorgasmia y tú descubres lo alto que puede jurar y soltar tacos. O incluso que sabe usarlos."
    kia "*JADEO* ¡TENGO LAS PIERNAS DE GELATINA! *GEMIDO*"
    "Sus piernas son de gelatina, sus paredes interiores son de acero que estrujan tu polla en cada embestida, queriendo mantenerte dentro de su coño."
    scene c24s003_955pv
    hide c24s003_960v
    show c24s003_955v
    "Empotrada entre el cristal y Mjolnir, sigue siendo recorrida por el segundo orgasmo. Tú te acercas al tuyo."
    kia "*GEMIDO* ¡FÓLLAME SALVAJEMENTE! *JADEO* ¡NO DEJES QUE ESTO ACABE! *GEMIDO*"
    "Cada vez más confiada, se deja ir completamente, descubriendo una faceta suya que no sabías que existía."
    mc "[kia], estoy a punto de correrme..."
    kia "*GEMIDO* ¡LLÉNAME HASTA EL BORDE! *JADEO* ¡DAME TODA TU LECHE! *GEMIDO*"
    "Suenan golpes en la pared, parece que los gritos de [kia] están empezando a molestar a los inquilinos de la habitación contigua."
    "Los ignoráis."
    "Tu orgasmo llega al tercer golpe."
    if persistent.pregnancy and not kia._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[kia] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ kia._var("pregnant", True)
                $ kia._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c24s003_785") from _call_OrgasmXS3_51
    hide c24s003_955v
    mc "¡Mpfft!"
    "Vuelves a llenar su útero con tu semilla una vez más. Ella aprieta su coño alrededor de Mjolnir como si tuviera un nuevo orgasmo."
    kia "*JADEO* ¡TRES! *GEMIDO* ¡JODER, POR EL AMOR DE DIOS! *JADEO* BUÍOCHAS LE DIA! *GEMIDO*"
    "En sucesivos encuentros, descubrirás que [kia] solo úsa gaélico en los momentos de máximo placer."
    "Ella vuelve a estrujar tu polla con el nuevo orgasmo producido al recibir tu descarga. Una sensación maravillosa que incrementa tu propio placer."
    scene c24s003_785d with fade
    stop music fadeout (1.5)
    "Cuando vuestros orgasmos finalizan, os quedáis inmóviles durante un rato, intentando recuperar la respiración. Mjolnir no abandona su húmeda y caliente posición."
    play music ("music/thinking-of-you.ogg")
    kia "*Respiración entrecortada* Ha sido... increíble... ¡He tenido tres orgasmos!"
    kia "*Respiración entrecortada* ¡Cinco en la misma noche!"
    mc "*Risa* Y la noche no ha acabado."
    call BlinkXPS3 ("c24s003_790" , "d") from _call_BlinkXPS3_1911
    kia "*Risa* Me estás vacilando, ¿verdad?"
    mc "*Risa* Un poco. Pero SOLO un poco."
    call BlinkXPS3 ("c24s003_795" , "d") from _call_BlinkXPS3_1912
    kia "*Risa* Hacía más de quince años que no tenía un orgasmo que no fuera con estos..."
    kia "Y en una sola noche he descubierto que el segundo asalto existe..."
    mc "Y el tercero..."
    call BlinkXPS3 ("c24s003_800" , "d") from _call_BlinkXPS3_1913
    kia "*Risa* Sí, y el tercero. Y que puedo tener más de un orgasmo en un solo asalto. Y que me gustan los juegos de roles..."
    kia "Me estás haciendo descubrir un mundo nuevo... No sé qué más descubriré contigo..."
    mc "*Risa* El poder del anillo."
    call BlinkXPS3 ("c24s003_805" , "d") from _call_BlinkXPS3_1914
    kia "Y además eso. La noche más romántica de la historia acabada con el mejor sexo de mi vida."
    mc "Ya sabes lo que dicen, hoy es el primer día del resto de nuestras vidas."
    mc "Pero ahora te voy a abandonar."
    call BlinkXPS3 ("c24s003_810" , "d") from _call_BlinkXPS3_1915
    kia "¿Vuelves a la cama?"
    mc "Sí, te espero allí. Pero antes tengo que ir a mear."
    call BlinkXPS3 ("c24s003_815" , "d") from _call_BlinkXPS3_1916
    stop music fadeout (1.5)
    kia "[mc]..."
    play music ("music/KindofGirl.ogg")
    mc "Dime."
    kia "Puedes hacerlo aquí si quieres..."
    mc "¿Quieres que mee en la ducha? Me sorprendes, [kia]."
    call BlinkXPS3 ("c24s003_820" , "d") from _call_BlinkXPS3_1917
    kia "Sabes que he visto mucho porno... de todos tipos... Siempre ha habido cosas que he querido probar..."
    kia "Hoy es una noche de descubrimientos para mí y... No me gustaría que me juzgaras, pero..."
    kia "No hace falta que lo hagas sobre mí si no quieres... ni siquiera que lo hagas en la ducha si... te da asco..."
    if persistent.walkthrough:
        $ wt1 = _("Fetiche de Orina activado con [kia].\n Meas en su pecho.")
        $ wt2 = _("Fetiche de Orina activado con [kia].\n Meas en el suelo.")
        $ wt3 = _("Fetiche de Orina desactivado con [kia].")
    else:
        $ wt1 = ""
        $ wt2 = ""
        $ wt3 = ""
    menu:
        "¿Mear encima tuyo? No lo he probado nunca." (wt = wt1):
            $ kia._var("urination", True)
            call c24s003_peeOnKia from _call_c24s003_peeOnKia
        "No lo he hecho nunca. Podemos probar poco a poco." (wt = wt2):
            $ kia._var("urination", True)
            call c24s003_peeOnFloor from _call_c24s003_peeOnFloor
        "No es algo que me guste hacer." (wt = wt3):
            call c24s003_peeInWC from _call_c24s003_peeInWC
            $ kia._var("urination", False)
    $ resetWalkthrough ()
    stop music fadeout (1.5)
    "Te llevas el anillo roto para repararlo mientras esperas."
    play music ("music/SensualJazzMedium2.ogg")
    "Casi tienes un déjà vu. Estabas en esta misma posición tan solo hace... no sabes cuánto tiempo ha pasado desde que [kia] te ha llamado desde el baño."
    call BlinkXPS3 ("c24s003_860a" , "f") from _call_BlinkXPS3_1918
    "Al cabo de unos minutos vuelve a aparecer la hermosa [kia], con el pelo aún mojado."
    kia "¿Sabes qué he oído?"
    mc "Dime."
    kia "Que hay algunas parejas que pueden llegar al cuarto asalto. *Risita* Pero no me lo creo."
    mc "*Risa* No soy nadie para decirte lo que debes o no debes creer."
    call BlinkXPS3 ("c24s003_860b" , "d") from _call_BlinkXPS3_1919
    kia "¿Qué? ¡Esperaba que dijeras algo como 'ven aquí y te demuestro que estás equivocada'!"
    mc "*Risa* Lo sé. Pero en una noche de descubrimientos, acabas de descubrir que también te puedo tomar el pelo."
    call BlinkXPS3 ("c24s003_860c" , "d") from _call_BlinkXPS3_1920
    kia "Prefiero descubrir hasta qué asalto podemos llegar antes de caer agotados."
    mc "Me parece una de las mejores ideas de la historia de las buenas ideas." id c24s003_KiaSex2_1d427aed
    scene c24s003_865a with fade
    "Y hay un cuarto asalto."
    scene c24s003_865b with fade
    "Y un quinto también. Empezáis a recorrer la habitación, probando sitios nuevos."
    scene c24s003_865c with fade
    "Consigues convencer a [kia] para que se ponga las gafas en el sexto."
    "No se las vuelve a quitar."
    scene c24s003_865d with fade
    "El séptimo es el último que contáis."
    "Al fin y al cabo, ¿a quién le importa un simple número?"
    scene c24s003_865An with fade
    "Probáis cada mueble, cada parte de la habitación, en la noche de sexo más salvaje y romántica que ninguno de los dos ha experimentado."
    "Sí, salvaje y romántico pueden ir de la mano en la misma noche."
    "Hay muchas palabras de amor entre asalto y asalto. Durante los asaltos."
    "No os decís 'Te quiero' ni una sola vez. Al menos no con palabras."
    "No es necesario."
    stop music fadeout (1.5)
    scene black with dissolve
    "En algún momento de la noche..."
    centered "{size=+20}{b}DÍA 26 – SÁBADO{/b}{/size}"
    scene c24s003_865i with fade
    play sound ("music/notification.ogg")
    "Una alarma suena en el móvil de [kia] justo después de un asalto sin número, durante el tiempo de los abrazos."
    play music ("music/On-The-Rise.ogg")
    kia "¿Qué? ¿Ya son las 8?"
    mc "Supongo que sí. Empiezas a trabajar en una hora y media, ¿no?"
    call BlinkXPS3 ("c24s003_870" , "d") from _call_BlinkXPS3_1921
    kia "Sí. ¿Puedes pedir algo para desayunar al servicio de habitaciones mientras me doy una ducha? ¡Estoy hambrienta!"
    mc "*Risa* ¿No soy bienvenido en esa ducha?"
    scene c24s003_870d with dissolve
    kia "Sabemos cómo va a acabar si vienes a la ducha, y no vamos a tener tiempo para desayunar. No hay tiempo para las dos cosas."
    kia "Y yo necesito recuperar energía."
    mc "OK. Pido el desayuno. ¿Algo especial?"
    scene black with dissolve
    "Desayunáis desnudos en la habitación y te duchas mientras [kia] se viste. Hay otro vestido en la bolsa de las sorpresas."
    "Se vuelve a poner el anillo de estaño."
    "Poco después abandonáis, con un poco de tristeza, la habitación en las que tantas cosas buenas han pasado."
    "Llegáis a su trabajo unos minutos antes de su hora de entrada."
    scene c24s003_870e with dissolve
    "Os despedís con un largo beso en la puerta de la biblioteca. Puedes notar la mirada de Geneviève clavada en vosotros durante todo el beso."
    "Ninguno de los dos le prestáis la más mínima atención."
    scene c24s003_870f with fade
    "Antes de volver al coche, ves como [kia] entra a la biblioteca y lo primero que hace es mostrarle el anillo a su jefa."
    "Para tu sorpresa, la bibliotecaria jefe parece alegrarse."
    "Te encantaría escuchar esa conversación."
    scene black with dissolve
    "Conduces hasta casa y subes a tu habitación. Por suerte, no te cruzas con nadie. No podrías mantener una conversación coherente en esos momentos."
    "En el momento en que has dejado a [kia] en la biblioteca, el último rastro de energía ha desaparecido de tus músculos y de tu cerebro."
    stop music fadeout (1.5)
    "Duermes hasta la hora de comer."
    return
label c24s003_peeOnKia:
    mc "Y no te preocupes, nunca te juzgaría por querer probar cosas nuevas."
    mc "Pero si quieres probar, estoy dispuesto a descubrir yo también cosas nuevas esta noche."
    call BlinkXPS3 ("c24s003_825" , "f") from _call_BlinkXPS3_1922
    "La preciosa bibliotecaria se arrodilla a tus pies, tomando la iniciativa. Crees que sabe más de esto que tú."
    kia "¿Aquí estoy bien?"
    "Es algo que alguna vez te ha llamado la atención, pero nunca has pensado en proponérselo a ninguna de las chicas con las que has estado."
    mc "Supongo que sí..."
    "Esta vez te lo ha propuesto la persona de la que menos hubieras sospechado que quisiera hacerlo. Es una caja de sorpresas."
    call BlinkXPS3 ("c24s003_830" , "d") from _call_BlinkXPS3_1923
    kia "Puedes empezar cuando quieras."
    mc "¿Dónde debo apuntar?"
    kia "Donde tú quieras. Soy tan novata como tú en esto."
    mc "Empecemos poco a poco..."
    kia "Apunta a mi pecho, entonces..."
    scene c24s003_835a with dissolve
    "Empiezas a soltar un chorro de pis que impacta en el pecho de [kia], mientras te mira sorprendida."
    "Es algo que no has hecho nunca. Aún no sabes si te gusta. Parece que ella tampoco sabe si le va a gustar."
    "Tu orina es lavada por el agua de la ducha en el mismo momento en que impacta en el cuerpo de [kia]."
    scene c24s003_835b with dissolve
    kia "¡Está muy caliente!"
    "Su radiante sonrisa te indica que realmente le gusta. Solo por ver esa sonrisa empieza a gustarte a ti también."
    scene c24s003_835c with dissolve
    "Has visto que, en el porno, muchas veces se usa este fetiche como una muestra de poder, de humillación."
    "No existe ese componente en la relación que tienes con [kia]."
    kia "¡Me encanta!"
    "Tal como pasan los segundos, te va gustando más a ti también."
    "Pero puedes notar cómo tu vejiga se va vaciando. No queda mucho pis que expulsar."
    scene c24s003_835d with dissolve
    kia "¿Quieres apuntar más arriba?"
    "La propuesta te vuelve a sorprender. La caja de sorpresas tiene una menos en su interior."
    menu:
        "¿Mear en tu cara? ¿Estás segura?" (wt = ""):
            kia "Segurísima. Si estamos probando cosas..."
            scene c24s003_835e with dissolve
            "Apuntas más arriba, salpicando la cara de [kia] con el último chorro de tu orina, que es lavada por la ducha en el mismo momento del impacto."
            kia "¡Sí! ¡Me gusta!"
            "A ti también. Tal como van pasando los segundos lo vas disfrutando más."
            "Descubrir junto a la hermosa pelirroja una nueva experiencia compartida es increíble."
            "Pero tu vejiga se vacía por completo antes de que te des cuenta."
            scene c24s003_835f with dissolve
            kia "¿Ya se ha acabado? ¡Se me ha hecho cortísimo! Pero me ha gustado."
        "Creo que voy a pasar." (wt = ""):
            mc "Es demasiado para mí y, además, ya se está acabando."
            scene c24s003_835f with dissolve
            kia "¿Ya se ha acabado? ¡Se me ha hecho cortísimo! Pero me ha gustado."
            kia "Quizás lo de apuntar a mi cara era demasiado para la primera vez. Perdona por habértelo pedido."
            mc "No tienes que pedir perdón por eso, ni por nada que quieras probar."
    mc "A mí también me ha gustado. Verte disfrutar ha sido increíblemente caliente."
    mc "Nunca temas preguntar cualquier cosa que quieras probar. Puede ser tan caliente como esto..."
    call BlinkXPS3 ("c24s003_840" , "d") from _call_BlinkXPS3_1924
    call c24s004_kiaPee from _call_c24s004_kiaPee
    return
label c24s003_peeOnFloor:
    mc "Y no te preocupes, nunca te juzgaría por querer probar cosas nuevas."
    mc "Pero si quieres que mee en la ducha, estoy dispuesto a descubrir yo también cosas nuevas esta noche. Nunca lo he hecho delante de nadie."
    call BlinkXPS3 ("c24s003_845a" , "d") from _call_BlinkXPS3_1925
    kia "*Risa* ¡Eso significa que has meado en la ducha con anterioridad!"
    mc "*Risa* Quien diga que no lo ha hecho nunca miente. ¿O acaso no lo has hecho nunca?"
    call BlinkXPS3 ("c24s003_845b" , "d") from _call_BlinkXPS3_1926
    kia "*Risa* ¡Por supuesto!"
    mc "*Risa* ¿Quieres que apunte a algún lugar concreto?"
    scene c24s003_850a with dissolve
    "La preciosa pelirroja coge tu polla en su mano mientras la mira hipnotizada."
    kia "Si no te importa, prefiero apuntar yo."
    mc "No me importa. Es tu petición, con lo que adelante. Voy a empezar."
    scene c24s003_850b with dissolve
    "Un caliente chorro de orina sale de tu polla, estrellándose contra el suelo. Hace un charco que el agua de la ducha lucha por eliminar en el momento en que se forma."
    kia "Puedo notar cómo recorre tu polla en mi mano..."
    mc "¿Te gusta la sensación? A mí me está pareciendo muy tórrida..."
    scene c24s003_850An with dissolve
    "[kia] empieza a jugar con tu polla a la vez que redirige el chorro de orina."
    kia "¡Me encanta!"
    mc "Podemos repetir esto en casa si quieres, cada vez que vaya al lavabo..."
    call BlinkXPS3 ("c24s003_855a" , "d") from _call_BlinkXPS3_1927
    kia "No me tientes..."
    "Tu meada acaba mientras vuestros ojos están prendidos en los del otro."
    call BlinkXPS3 ("c24s003_855b" , "d") from _call_BlinkXPS3_1928
    kia "¿Ya está? ¡Ha durado menos de lo que esperaba!"
    mc "Me parece que sí. No queda más."
    call BlinkXPS3 ("c24s003_855c" , "d") from _call_BlinkXPS3_1929
    kia "Me ha gustado más de lo que pensaba."
    mc "A mí también. No esperaba tener ese fetiche."
    call BlinkXPS3 ("c24s003_855d" , "d") from _call_BlinkXPS3_1930
    kia "No sabía si atreverme a pedírtelo. Es algo muy específico... y no creo que a todo el mundo le guste."
    mc "Nunca temas preguntar cualquier cosa que quieras probar. Puede ser tan caliente como esto..."
    call BlinkXPS3 ("c24s003_855e" , "d") from _call_BlinkXPS3_1931
    call c24s004_kiaPee from _call_c24s004_kiaPee_1
    return
label c24s003_peeInWC:
    mc "Y no te preocupes, nunca te juzgaría por querer probar cosas nuevas."
    mc "Pero esto no es algo que me haya llamado nunca la atención."
    call BlinkXPS3 ("c24s003_855d" , "d") from _call_BlinkXPS3_1932
    kia "No sabía si atreverme a pedírtelo. Es algo muy específico... y no creo que a todo el mundo le guste."
    mc "Nunca temas preguntar cualquier cosa que quieras probar. Puede ser que nos guste a los dos..."
    mc "Y ahora voy a mear antes de hacérmelo encima. *Risa* ¿Te quedas acabando de ducharte?"
    kia "Sí, espérame en la habitación."
    scene c24s003_685d with fade
    "Vuelves a la habitación después de mear y secarte. Esperas que [kia] termine la ducha mirando la chimenea."
    return
label c24s004_kiaPee:
    kia "Si puedo preguntar cualquier cosa... ¿te importaría si yo meo en la ducha?"
    if persistent.walkthrough:
        $ wt1 = _("[kia] mea sobre ti.")
        $ wt2 = _("Verás a [kia] meando en la ducha.")
        $ wt3 = _("Te irás a la habitación sin ver nada.")
    else:
        $ wt1 = ""
        $ wt2 = ""
        $ wt3 = ""
    menu:
        "Incluso puedes hacerlo encima mío si quieres." (wt = wt1):
            call c24s004_kiaOnMC from _call_c24s004_kiaOnMC
        "No me importa, si no te importa que mire." (wt = wt2):
            call c24s004_kiaOnFloor from _call_c24s004_kiaOnFloor
        "No me importa. Te espero en la habitación" (wt = wt3):
            kia "Ningún problema. Espérame allí y ahora voy."
            scene c24s003_685d with fade
            "Vuelves a la habitación después secarte. Esperas que [kia] termine la ducha mirando la chimenea." id c24s004_kiaPee_5ff4afd8
    $ resetWalkthrough ()
    return
label c24s004_kiaOnMC:
    scene c24s004_500a with fade
    "Te tumbas en el suelo mientras la bellísima pelirroja pone un pie a cada lado de tu cuerpo."
    kia "¿Preparado?"
    mc "*Risa* No muy convencido, pero preparado."
    call BlinkXPS3 ("c24s004_505a" , "d") from _call_BlinkXPS3_1933
    kia "Si quieres lo podemos dejar, si no estás muy seguro."
    mc "No te preocupes. Quiero probarlo. Hoy es día de descubrimientos."
    kia "Voy entonces..."
    scene c24s004_500b with dissolve
    "La bibliotecaria deja caer un chorro que impacta en tu pecho. Se siente muy caliente mientras el agua de la ducha elimina la orina nada más tocarte."
    mc "Está muy caliente."
    kia "¿Te gusta?"
    scene c24s004_500c with dissolve
    mc "Me gusta, es un descubrimiento interesante. Y tórrido. ¿Qué tal por ahí arriba?"
    kia "Es una sensación... de poder. Me gusta."
    kia "Sin embargo, al haberlo pedido tú, no me siento como si te estuviera humillando. Eso me gusta aún más."
    scene c24s004_500d with dissolve
    mc "Te estás poniendo cachonda, ¿verdad?"
    kia "No te puedes imaginar cuánto."
    kia "Lo malo es que no dura mucho..."
    mc "Lo podremos repetir en otro momento, si quieres."
    call BlinkXPS3 ("c24s004_505b" , "d") from _call_BlinkXPS3_1934
    "El chorro acaba inesperadamente. Casi lo echas de menos."
    kia "Me parece una idea excelente. Ya me estoy imaginando escenarios..."
    mc "*Risa* Voy a acabar de limpiarme y te espero en la habitación. Me tienes que contar esos escenarios."
    scene c24s003_685d with fade
    "Vuelves a la habitación después de limpiarte y secarte. Esperas que [kia] termine la ducha mirando la chimenea."
    return
label c24s004_kiaOnFloor:
    call BlinkXPS3 ("c24s004_510" , "d") from _call_BlinkXPS3_1935
    kia "¿Cómo va a importarme que mires? Eso era lo más interesante de mi petición..."
    mc "Eres mucho más traviesa de lo que imaginaba. Me encanta..."
    call BlinkXPS3 ("c24s004_515" , "d") from _call_BlinkXPS3_1936
    kia "¿Vas a mirar desde ahí arriba?"
    mc "Voy a mirar desde todos los ángulos. No es algo que quiera perderme."
    kia "Ahí voy, entonces."
    scene c24s004_520a with dissolve
    "Un potente chorro amarillento hace su aparición en un momento. Es hipnótico."
    kia "Me está poniendo cómo me miras..."
    mc "A mí me está poniendo mirarte..."
    scene c24s004_520b with dissolve
    "Se forma un pequeño charco en el suelo que lucha por no ser lavado por el agua de la ducha."
    kia "¿Te pongo yo o verme mear?"
    mc "Las dos cosas... que seas tú quién mee. Que seas tú quién lo ha propuesto."
    scene c24s004_520c with dissolve
    "Cambias de ángulo, no queriendo perderte nada del espectáculo. [kia] cambia de posición para darte una mejor visión."
    kia "Ya se está acabando..."
    mc "Habrá que disfrutar las vistas hasta el último momento, entonces."
    scene c24s004_520d with dissolve
    "El chorro desaparece casi de golpe y el charco un par de segundos después."
    mc "Ha durado menos de lo que esperaba... pero ha valido la pena."
    kia "Una experiencia nueva para los dos."
    call BlinkXPS3 ("c24s004_525" , "d") from _call_BlinkXPS3_1937
    kia "Ahora mismo estoy cachondísima. Hacer esto delante tuyo ha sido super caliente."
    kia "Y veo que a ti también te ha puesto igual de cachondo. Mjolnir vuelve a estar enorme."
    mc "*Risa* ¿Quieres el cuarto asalto? Te estás volviendo avariciosa..."
    call BlinkXPS3 ("c24s004_530" , "d") from _call_BlinkXPS3_1938
    kia "No creo que pudiera. Ahora quiero acabar de ducharme e ir a la cama a darnos abrazos antes de dormir."
    mc "Me parece una idea estupenda. Déjame aclararme y te espero en la cama mientras acabas de ducharte."
    scene c24s003_685d with fade
    "Vuelves a la habitación después de aclararte y secarte. Esperas que [kia] termine la ducha mirando la chimenea."
    return
label c24s004_Deb_Sim:
    if _in_replay:
        call mrS3_deb_route from _call_mrS3_deb_route_7
        call mrS3_sim_route from _call_mrS3_sim_route_3
    scene black with dissolve
    play music ("music/Morning-Sun.ogg")
    "Después de comer, algunas de las chicas te preguntan si te vas a unir a ellas en la piscina."
    "Subes a tu habitación a ponerte el bañador. Quieres relajarte un rato antes de la reunión con Iron Fist de la noche."
    scene c24s004_210a with dissolve
    "Cuando bajas a la piscina, encuentras a [deb.nick] y a [sim] charlando animadamente en el agua."
    scene c24s004_210b with dissolve
    mc "¿Qué tal, chicas? ¿Cómo están las dos sirenas?"
    sim "Genial. Después de ver a un montón de niños nadando esta mañana, tenía ganas de nadar un rato. Y no hay nadie mejor que [deb.nick] para hacerlo."
    deb "No exageres, [sim]."
    mc "¿Hacéis carreras entre vosotras?"
    call BlinkXPS3 ("c24s004_215" , "d") from _call_BlinkXPS3_1939
    sim "*Risa* ¡Qué va! [deb.nick] es demasiado buena para mí."
    sim "Hicimos una amistosa y no tuvo que esforzarse para darme una paliza."
    call BlinkXPS3 ("c24s004_220" , "d") from _call_BlinkXPS3_1940
    deb "No le hagas caso. Está exagerando y está desentrenada."
    mc "Bueno, lleva tiempo sin nadar. Es lógico."
    call BlinkXPS3 ("c24s004_225" , "d") from _call_BlinkXPS3_1941
    sim "Llevo un año sin nadar en una competición y ni siquiera entonces llegué a los campeonatos nacionales."
    sim "Ella llegó y los ganó. Creo que la diferencia está clara, ¿no?"
    call BlinkXPS3 ("c24s004_230" , "d") from _call_BlinkXPS3_1942
    deb "Ya sabes por qué fue. No tienes el cuerpo adecuado para ser nadadora competitiva."
    deb "Te desarrollaste donde no me desarrollé yo, y eso te quita centésimas en cada brazada."
    call BlinkXPS3 ("c24s004_235" , "d") from _call_BlinkXPS3_1943
    sim "A veces odio estas tetas..."
    if sim._var("route"):
        mc "A mí me encantan..."
        if deb._var("route"):
            call BlinkXPS3 ("c24s004_240" , "d") from _call_BlinkXPS3_1944
            sim "También te encantan las de [deb.nick]. *Risa* Tu opinión es bienvenida, pero eres poco quisquilloso en cuanto a tetas."
            mc "Tienes razón, ¿para qué negarlo? *Risa*"
    mc "Todos tenemos que aceptar el cuerpo que nos toca, [sim]."
    if sim._var("route") and deb._var("route"):
        mc "Y a mí me gustan los vuestros. Los de las dos."
    scene c24s004_210An with dissolve
    deb "¿Sí?" (multiple=2)
    sim "¡Sí!" (multiple=2)
    mc "Sí, ¿sobre qué?"
    scene c24s004_210An2 with dissolve
    play sound ("music/splash.ogg")
    sim "¡Ahora!"
    mc "¿QUÉ?"
    scene c24s004_210k with fade
    mc "*Risa* ¿A qué ha venido eso?"
    sim "*Risa* Me estaba entrando tortícolis de mirar tan arriba."
    deb "*Risa* Y a ti te ha tocado un cuerpo poco ágil que no ha podido esquivar nuestros ataques."
    if sim._var("route"):
        call KissXPS3 ("c24s004_245" , "d") from _call_KissXPS3_35
        sim "Además, tenía ganas de hacer esto."
        mc "Entonces no me voy a quejar del ataque a traición."
        if deb._var("route"):
            call KissXPS3 ("c24s004_250" , "d") from _call_KissXPS3_36
            deb "Yo también tenía ganas de besarte."
            mc "*Risa* Podéis atacarme cuando queráis si la recompensa es esta."
    elif deb._var("route"):
        call KissXPS3 ("c24s004_250" , "d") from _call_KissXPS3_37
        deb "Además, tenía ganas de besarte."
        mc "*Risa* Podéis atacarme cuando queráis si la recompensa es esta."
    scene c24s004_210j with dissolve
    mc "Y, aparte de atacar a pobres hombres que pasaban por aquí, ¿de qué estabais hablando?"
    call BlinkXPS3 ("c24s004_255" , "d") from _call_BlinkXPS3_1945
    deb "Precisamente estábamos hablando de nadar."
    deb "Le estaba diciendo a [sim] que quizás pudiera convencer al entrenador de la universidad para que la dejara entrenar algunos días con nosotras."
    mc "¿Puedes hacer eso?"
    call BlinkXPS3 ("c24s004_260" , "d") from _call_BlinkXPS3_1946
    sim "¡Claro que puede! ¡Es la estrella de la universidad! Seguro que no le niegan nada."
    call BlinkXPS3 ("c24s004_260b" , "d") from _call_BlinkXPS3_1947
    sim "Pero prefiero que no lo haga. Sería como... no sé... probar cómo hubiera sido mi vida en otras circunstancias pero no poder vivirla del todo."
    call BlinkXPS3 ("c24s004_265" , "d") from _call_BlinkXPS3_1948
    deb "¡Es tan cabezota como su hermano!"
    deb "Aprendería técnicas nuevas y cómo se entrena en la universidad. Sólo por eso ya valdría la pena."
    mc "Creo que tienes razón, pero también comprendo a [sim]."
    call BlinkXPS3 ("c24s004_270" , "d") from _call_BlinkXPS3_1949
    sim "¿Ves? ¡El me entiende!"
    mc "Te entiendo, pero no comparto tu decisión."
    call BlinkXPS3 ("c24s004_275" , "h") from _call_BlinkXPS3_1950
    sim "¿Qué?"
    mc "Siempre te ha gustado nadar y ahora tienes que ver cómo otros lo hacen y esperar a que se ahoguen para salvarlos."
    call BlinkXPS3 ("c24s004_280" , "d") from _call_BlinkXPS3_1951
    sim "*Risa* ¡No se ahoga nadie en mi guardia!"
    mc "[sim], hablo en serio. Entiendo cómo te sientes, pero creo que deberías aceptar la oferta de [deb.nick]."
    mc "Entrenarías con las mejores de la ciudad y, aunque no vuelvas a competir, aprenderás muchísimo."
    call BlinkXPS3 ("c24s004_285" , "d") from _call_BlinkXPS3_1952
    deb "Es lo que le he dicho. Además, nuestro entrenador es muy bueno y aprenderá cómo entrenar a otros."
    call BlinkXPS3 ("c24s004_285b" , "d") from _call_BlinkXPS3_1953
    deb "Es lo que querías estudiar, ¿no?"
    call BlinkXPS3 ("c24s004_290" , "d") from _call_BlinkXPS3_1954
    sim "Sí, pero sin la beca, no voy a ir nunca a la universidad. Dudo que nunca sea entrenadora."
    sim "Y con mis récords, nunca voy a conseguir una beca."
    mc "Pero aprenderás mucho igualmente. Y seguirás nadando, que es lo que importa."
    call BlinkXPS3 ("c24s004_295" , "d") from _call_BlinkXPS3_1955
    deb "Creo que no la vas a convencer. Como he dicho, es casi peor que intentar convencer a Jamaal para que suelte un plato de comida."
    mc "Siempre he dicho que se parecen mucho. No sé cuál de los dos es más terco."
    call BlinkXPS3 ("c24s004_300" , "h") from _call_BlinkXPS3_1956
    sim "¡Hey! Estoy aquí, ¿sabéis?"
    "[deb.nick] y tú la ignoráis. Habéis encontrado su punto débil."
    call BlinkXPS3 ("c24s004_305" , "d") from _call_BlinkXPS3_1957
    deb "No creas que no la entiendo. Con esos dos flotadores tiene que ser incómodo nadar. En eso se diferencia de Jamaal."
    mc "*Risa* Sí, creo que Jamaal tiene poca flotabilidad con la silla de ruedas."
    mc "Pero, ¿sabes en lo que sí que se parecen? A los dos les cuesta aceptar retos."
    mc "Jamaal tardó tiempo en descubrir que, aunque tuviera que vivir una vida diferente, podía hacer lo que le gustaba."
    call BlinkXPS3 ("c24s004_310" , "h") from _call_BlinkXPS3_1958
    sim "¡Tenía once años! ¡Era un niño!"
    "Seguís ignorándola."
    call BlinkXPS3 ("c24s004_315" , "d") from _call_BlinkXPS3_1959
    deb "Y es una lástima que [sim] se comporte como una niña de once años, ¿verdad?"
    mc "Sí, una verdadera lástima. Va a dejar de hacer lo que le gusta porque no puede hacerlo al nivel que le gustaría."
    deb "*Risa* Justo como su hermano." (multiple=2)
    mc "*Risa* Justo como Jamaal." (multiple=2)
    mc "¿Sabes que Jam estuvo a punto de no ir al baile de graduación?"
    call BlinkXPS3 ("c24s004_320" , "h") from _call_BlinkXPS3_1960
    sim "¡Porque le dejó su novio dos semanas antes del baile!"
    call BlinkXPS3 ("c24s004_325" , "d") from _call_BlinkXPS3_1961
    "[deb.nick] continúa como si no hubiera escuchado nada."
    deb "¿Porque no podía bailar?"
    mc "No, le encanta bailar y hace unas cosas tremendas con las ruedas. Pero no quería porque no podía bailar con quién él hubiera querido bailar."
    mc "Es como su hermana. Ella no quiere nadar porque no puede nadar en competiciones."
    mc "Yo convencí a Jam, pero te tocará a ti convencer a [sim]."
    call BlinkXPS3 ("c24s004_330" , "h") from _call_BlinkXPS3_1962
    sim "¡Parad! ¡Vale! ¡Habla con ese entrenador a ver si puedo entrenar con vosotras alguna tarde este verano!"
    mc "¡Oh, [sim]! ¿Estabas aquí?"
    sim "*Grrrr*"
    call BlinkXPS3 ("c24s004_335" , "d") from _call_BlinkXPS3_1963
    deb "*Risa* Si lo hubiéramos planeado no hubiera podido salir mejor."
    mc "*Risa* Pero es una táctica que siempre funciona con los Washington. Comparar a [sim] y a Jamaal."
    call BlinkXPS3 ("c24s004_340" , "d") from _call_BlinkXPS3_1964
    sim "Pues ahora te vamos a expulsar de la piscina."
    mc "¿Por qué a mí? ¡Lo hemos hecho [deb.nick] y yo!"
    call BlinkXPS3 ("c24s004_345" , "d") from _call_BlinkXPS3_1965
    sim "Puedes ir a la otra zona. Esto se acaba de convertir en Zona de Entrenamiento [sim]. Vamos a ponernos bañadores para entrenar. ¡No se puede entrenar en bikini!"
    sim "No puedo hacer el ridículo cuando vaya a esos entrenamientos. Y [deb.nick] lo va a pagar ayudándome a entrenar. *Risa* Se le acabó hacer top-less."
    mc "Vale, vale. Ya me voy. Puedes pedirle un bañador a mi madre."
    if sim._var("route"):
        call KissXPS3 ("c24s004_245" , "d") from _call_KissXPS3_38
        sim "Aunque te bese, me las pagarás por lo que acabas de hacer."
    else:
        call BlinkXPS3 ("c24s004_350" , "d") from _call_BlinkXPS3_1966
        sim "Aunque te abrace, me las pagarás por lo que acabas de hacer."
    mc "Creo que más que pagártelas, me lo acabarás agradeciendo."
    if deb._var("route"):
        call KissXPS3 ("c24s004_250" , "d") from _call_KissXPS3_39
    else:
        call BlinkXPS3 ("c24s004_355" , "d") from _call_BlinkXPS3_1967
    deb "Yo también lo creo. Nos lo acabará agradeciendo, pero ahora debes marcharte, antes de que cambie de opinión."
    stop sound fadeout (1.5)
    stop music fadeout (1.5)
    mc "Os dejo que vayáis a poneros los bañadores. Voy a ver qué están haciendo las otras chicas."
    return
label c24s004_Mad_Lis_Emm:
    if _in_replay:
        call mrS3_emm_route from _call_mrS3_emm_route_12
        call mrS3_lis_route from _call_mrS3_lis_route_2
        call mrS3_mad_route from _call_mrS3_mad_route_2
        call mrS3_deb_route from _call_mrS3_deb_route_8
    scene c24s004_550a with fade
    play music ("music/RhythmPlay.ogg")
    "Orgulloso de cómo las chicas se están ayudando entre ellas, sales de la piscina y te secas."
    "Te acercas a [lis], [emm], y [mad.nick], que parecen ocupadas alrededor de unos papeles."
    mc "¿Qué tal, chicas?"
    scene c24s004_550b with dissolve
    emm "¡Hola,  [mc]!"
    lis "Estamos ayudando a [mad.nick] con sus diseños. A ver si podemos acabar hoy y así puede empezar con la costura."
    mad "Hay un montón de cosas en las que no había pensado."
    mc "Es genial que os estéis ayudando tanto."
    if lis._var("route") or emm._var("route") or mad._var("route"):
        mc "¿No hay besos para mí, hoy?"
        if emm._var("route"):
            scene c24s004_550c with dissolve
            if persistent.family:
                "Tu hermana se lanza a tus brazos para darte un largo beso. Prácticamente no habéis hablado desde que volvisteis de Monterey."
            else:
                "[emm] se lanza a tus brazos para darte un largo beso. Prácticamente no habéis hablado desde que volvisteis de Monterey."
            call BlinkXPS3 ("c24s004_555" , "d") from _call_BlinkXPS3_1968
            emm "Te aseguro que no voy a dejar de darte besos por unos vestidos, por bonitos que sean."
        if mad._var("route"):
            scene c24s004_550d with dissolve
            "La preciosa asiática te da un apasionado beso."
            call BlinkXPS3 ("c24s004_560" , "d") from _call_BlinkXPS3_1969
            mad "Por mucho que me gusten mis diseños, me gusta más esto."
        if lis._var("route"):
            scene c24s004_550e with dissolve
            "[lis] se acerca tímidamente y se dirige a darte un beso en la mejilla. Giras un poco la cara para rozar sus labios. No se aparta."
            "Es la primera vez que tiene la oportunidad de demostrar en público que estáis juntos."
            call BlinkXPS3 ("c24s004_565" , "d") from _call_BlinkXPS3_1970
            emm "¡Eso no es un beso, [lis]! Estoy segura de que lo puedes hacer mejor."
            scene c24s004_550f with dissolve
            "Tu pequeña princesa parece olvidarse de que las otras dos chicas están alrededor y aumenta la pasión del beso. Un largo beso."
            call BlinkXPS3 ("c24s004_570" , "d") from _call_BlinkXPS3_1971
            emm "*Risa* ¡Eso está mejor! Pero, o volvemos a los vestidos, u os buscáis una habitación."
            call BlinkXPS3 ("c24s004_575" , "d") from _call_BlinkXPS3_1972
            lis "*Risa* Si nos buscamos una habitación, seguro que convences a [mad.nick] para que haga todos los vestidos rosas."
            call BlinkXPS3 ("c24s004_580" , "d") from _call_BlinkXPS3_1973
            mad "¡Ni en broma! *Risa* Van a ser blancos. Le van a quedar genial a [kim]."
            call BlinkXPS3 ("c24s004_585a" , "d") from _call_BlinkXPS3_1974
    else:
        call BlinkXPS3 ("c24s004_585b" , "d") from _call_BlinkXPS3_1975
        mad "Y falta [kim], que es quién va a ser la modelo."
    mad "Está probándose el uniforme que le han mandado para el trabajo de esta noche."
    mc "¿Puedo ayudaros con el tema de los vestidos? No es que sea un experto, pero..."
    mc "Sé lo que queda sexy en una mujer."
    call addProfileImageS3 (2, "maddie_2", mad, _(": 15 - Especial"), "") from _call_addProfileImageS3_8
    call BlinkXPS3 ("c24s004_590" , "d") from _call_BlinkXPS3_1976
    emm "*Risa* Si tuvieras que elegir lo que queda sexy en [kim], seguro que acababa sólo con un tanga."
    mc "Y estoy seguro de que estaría super sexy, pero no creo que sea el estilo que [mad.nick] quiere para sus vestidos."
    mc "¿Es para otro concurso?"
    call BlinkXPS3 ("c24s004_595" , "d") from _call_BlinkXPS3_1977
    mad "No, esta vez estamos refinando mi portfolio de diseños. Voy a coser los vestidos para [kim], de tal forma que [emm] pueda hacer las fotos."
    if not lis._var("route"):
        mc "Me parece una idea estupenda. Y supongo que [lis] está para evitar que [emm] te convenza para que los hagas rosas."
    else:
        mc "Me parece una idea estupenda. Y, aparte de evitar que [emm] te convenza para que los hagas rosas, ¿cuál es la función de [lis]?"
    call BlinkXPS3 ("c24s004_600" , "d") from _call_BlinkXPS3_1978
    lis "*Risa* Hay un par de vestidos que están pensados para cenas de gala y eventos sociales."
    lis "Esos los va a hacer [mad.nick] también en mi talla y la de [deb.nick], así podemos usarlos cuando vayamos a alguna fiesta con famosos y hacerle un poco de publicidad."
    mc "Empezáis a dar un poco de miedo. Parece que habéis encontrado una forma en que todas aportáis algo y todas ganáis algo."
    mc "Experiencia, publicidad, portfolio, o vestidos."
    call BlinkXPS3 ("c24s004_605" , "d") from _call_BlinkXPS3_1979
    lis "*Risa* Lo dices como si fuera una transacción comercial, y lo estamos haciendo por ayudar a [mad.nick] con sus diseños y a [kim] con su portfolio."
    lis "Y para que [emm] pueda hacer su primer trabajo semiprofesional... *Risa* Vale, sí. Experiencia, publicidad, portfolio, y vestidos."
    mc "*Risa* Aunque vuestras acciones sean altruistas, todas ganáis algo. Es la mejor forma de hacerlo."
    call BlinkXPS3 ("c24s004_610" , "d") from _call_BlinkXPS3_1980
    mad "Sólo nos falta convencer a [deb.nick] para que pose con los vestidos que le voy a hacer."
    mad "Siendo tan alta, las fotos quedarían geniales."
    mcp "(Y le ayudaríais a entender que ser alta puede tener muchas ventajas.)"
    if deb._var("route"):
        mcp "(Y que no me gusta sólo a mí que sea así.)"
    mc "Supongo que diferentes vestidos quedarán mejor o peor en diferentes modelos."
    call BlinkXPS3 ("c24s004_615" , "d") from _call_BlinkXPS3_1981
    emm "*Risa* Y si haces un vestido rosa, yo me presto voluntaria para posar con él."
    emm "Cuantas más modelos diferentes tengas, más profesional quedará tu portfolio."
    mc "¿Quién sacará las fotos si tú estás posando?"
    call BlinkXPS3 ("c24s004_620" , "d") from _call_BlinkXPS3_1982
    lis "Las puedo sacar yo. No soy tan buena como [emm], pero sé algo de fotografía."
    mc "Genial ¿Vais a hacer las fotos en la piscina? Podrían quedar muy chulas."
    call BlinkXPS3 ("c24s004_625" , "d") from _call_BlinkXPS3_1983
    mad "Haremos algunas aquí y otras en el bosque, quizás algunas en la playa, incluso. Pero, para el portfolio, quedarían mejor en un estudio."
    call BlinkXPS3 ("c24s004_630" , "d") from _call_BlinkXPS3_1984
    emm "Quiero convencer a Mamá para que me deje usar parte del sótano para montar un estudio de fotografía. No necesito mucha inversión y hay un montón de espacio sin usar."
    emm "¿Crees que me dejará hacerlo?"
    mc "No creo que ponga ningún impedimento. Siempre dice que deberíamos darle alguna utilidad al sótano."
    call BlinkXPS3 ("c24s004_635" , "d") from _call_BlinkXPS3_1985
    mad "Para alguna de las fotos que tengo pensadas... ¿te importaría posar con [kim]?"
    mad "Hay algunos vestidos que quedarían genial en poses románticas con un chico."
    mc "*Risa* ¿Quieres que haga de modelo para ti? Por mí no hay ningún problema."
    call BlinkXPS3 ("c24s004_640" , "d") from _call_BlinkXPS3_1986
    emm "*Risa* Podrías hacer del madurito cuarentón seduciendo a una jovencita. Ya sabes que aparentas más edad de la que tienes."
    if emm._var("route"):
        mc "*Risa* Contigo funcionó, aunque no tuviera que hacer nada para seducirte."
    else:
        mc "*Risa* Podría ser divertido."
    mc "¿También hay trajes para mí?"
    call BlinkXPS3 ("c24s004_645" , "d") from _call_BlinkXPS3_1987
    lis "No, [mad.nick] no hace ropa para hombre, al menos aún."
    lis "Pero estarías muy bien con el traje que llevaste al Jazz Corner."
    call BlinkXPS3 ("c24s004_650" , "d") from _call_BlinkXPS3_1988
    mad "*Risa* Sabéis que os odio a veces, ¿verdad?"
    mc "¿Por qué?"
    call BlinkXPS3 ("c24s004_655" , "d") from _call_BlinkXPS3_1989
    mad "Es una tontería pero, excepto el cumpleaños de las chicas, me he perdido todas las actividades familiares."
    mad "La fiesta en la playa, la noche en el club de Jazz... A veces os ponéis a hablar de esas cosas y estoy un poco fuera de lugar."
    mad "Me hubiera gustado estar, pero hasta la partida de DnD no me sentía parte de esto..."
    call BlinkXPS3 ("c24s004_660" , "d") from _call_BlinkXPS3_1990
    emm "No te preocupes, [mad.nick]. A partir de ahora vendrás siempre que hagamos algo especial."
    emm "Estoy pensando que, si tú te sientes así, ¿cómo se van a sentir las chicas que llegan en Septiembre?"
    mc "Bueno, falta por ver si se integran en la familia tan rápido como..."
    call BlinkXPS3 ("c24s004_665" , "d") from _call_BlinkXPS3_1991
    lis "¿Como nosotras? Estoy segura de que lo harán. [sca] me dijo que una de ellas era amiga suya y de [dap] hace años, que vivía en Newport."
    lis "Integrarla a ella en la familia será fácil, y a la prima de [sai] también."
    mc "¿Quién es la amiga de [dap] y [sca]?"
    call BlinkXPS3 ("c24s004_670" , "d") from _call_BlinkXPS3_1992
    emm "Patty. No sé si la recuerdas, morena, ojos grandes... era un par de días mayor que [sca]. No era muy amiga mía, pero nos llevábamos bien."
    emm "Su madre encontró trabajo en Dallas, y se marcharon un año antes de que tú te graduaras."
    mc "Me suena el nombre, pero no le puedo poner cara."
    emm "Deberías mirar los expedientes de las chicas nuevas y..."
    scene c24s004_675An1 with dissolve
    kim "[mad.nick], ¿me puedes ayudar a...?"
    scene c24s004_675d with hpunch
    kim "¡Oops! Veo que estáis ocupadas. No os preocupéis."
    scene c24s004_675An2 with dissolve
    kim "Voy a pedirle ayuda a la Abuela..."
    scene c24s004_550g with dissolve
    mc "¿Qué le pasa?"
    emm "¿No la has oído? Ha visto que [mad.nick] está ocupada y..."
    mad "... Y no ha querido entretenerme por si..."
    lis "... Por si estaba haciendo algo importante... supongo..."
    mc "¿Qué me estáis ocultando, chicas?"
    scene c24s004_550h with dissolve
    lis "¿Nosotras?"
    emm "¿Qué íbamos a querer ocultarte?"
    mad "Si es algo en lo que puede ayudarle [mee]..." id c24s004_Mad_Lis_Emm_c88f9707
    mc "Vale, no os voy a sacar nada, ¿verdad?"
    scene c24s004_550i with dissolve
    "Todas" "Nope."
    lis "Además, lo dices como si... en el caso de que le pasara algo a [kim]... nosotras supiéramos qué es."
    emm "Y no estamos diciendo que le pase nada..."
    mad "Ni que sepamos qué le pasa... si es que le pasa algo. O que te lo fuéramos a decir si lo supiéramos."
    mc "*Risa* Vale, vale. Pero... ¿ha llamado 'Abuela' a Meemaw?"
    scene c24s004_550j with dissolve
    emm "*Risa* Sí. [kim] está llevando lo de integrarse en la familia a un nuevo nivel. Pero aún no se atreve a llamárselo a ella."
    lis "*Risa* El día menos pensado nos empieza a llamar hermanas a todas."
    mad "*Risa* No dejaría de ser divertido que tantas chicas de razas diferentes nos empezásemos a considerar hermanas algún día."
    "En ese momento oís una furgoneta y cómo se abre la verja de entrada."
    call BlinkXPS3 ("c24s004_680" , "d") from _call_BlinkXPS3_1993
    play sound ("music/motor.ogg")
    emm "Creo que esa es [ama]. Debe venir a buscarte para lo de esta noche."
    mc "Pero es muy pronto para que venga el helicóptero."
    emm "A lo mejor quiere repasar algunos datos."
    mc "Voy a ver..."
    stop sound
    if emm._var("route"):
        scene c24s004_550c with dissolve
        pause (1.0)
    if lis._var("route"):
        scene c24s004_550f with dissolve
        pause (1.0)
    if mad._var("route"):
        scene c24s004_550d with dissolve
    "Te despides de las chicas y te diriges a la furgoneta."
    scene c24s004_685a with dissolve
    "[ama] está sentada dentro, parece que está escribiendo algo."
    scene c24s004_685b with dissolve
    "Te acercas a la furgoneta, dispuesto a golpear en la ventanilla."
    ama "Un momento, [mc], por favor."
    stop music fadeout (1.5)
    "Esperas."
    return
label c24s004_Kim_Mee_Meg:
    scene c24s004_750a with fade
    "Unos minutos antes, en la cocina de [nor]..."
    play music ("music/Gypsy-Jazz.ogg")
    mee "Un día tengo que ir a oírte cantar. Siempre me ha gustado el jazz."
    meg "Aunque el sitio se llame Jazz Corner, no solo canto jazz. Tenemos un repertorio muy variado."
    call BlinkXPS3 ("c24s004_755" , "d") from _call_BlinkXPS3_1994
    mee "Bueno, igualmente me gustaría ir. Hace años que no voy a ningún sitio con música en directo."
    call BlinkXPS3 ("c24s004_760" , "d") from _call_BlinkXPS3_1995
    meg "¿Ibas mucho cuando...?"
    call BlinkXPS3 ("c24s004_765" , "d") from _call_BlinkXPS3_1996
    mee "*Risa* ¿Cuando era joven?"
    mee "Sí, a John y a mí nos gustaba mucho ir, especialmente antes de casarnos, cuando él aún vivía en San Francisco."
    call BlinkXPS3 ("c24s004_770" , "d") from _call_BlinkXPS3_1997
    meg "San Francisco siempre ha tenido buenos clubes de jazz. ¿Teníais algún favorito?"
    call BlinkXPS3 ("c24s004_775" , "d") from _call_BlinkXPS3_1998
    mee "Sí, el Keystone Korner. Un clásico. Incluso estuvimos allí en un par de ocasiones cuando hicieron grabaciones de directos."
    mee "Todavía tengo los vinilos de esas grabaciones."
    call BlinkXPS3 ("c24s004_780" , "d") from _call_BlinkXPS3_1999
    meg "¡Oh! ¡Eso es increíble! ¿De quién son los discos?"
    call BlinkXPS3 ("c24s004_785" , "d") from _call_BlinkXPS3_2000
    mee "Uno es de Tete Montoliu y otro de Jaki Byard, los dos en el '79 o el '80. Son fantásticos."
    call BlinkXPS3 ("c24s004_790" , "d") from _call_BlinkXPS3_2001
    meg "¡Me tienes que dejar escucharlos!"
    meg "Me das mucha envidia. ¡Estuviste ahí cuando se escribía historia de la música!"
    call BlinkXPS3 ("c24s004_795" , "d") from _call_BlinkXPS3_2002
    mee "Bueno, eran otros tiempos. Todo era más artesanal."
    mee "Los tengo en la casa de Florida. Te los traeré cuando vaya la semana que viene a poner la casa en venta."
    call BlinkXPS3 ("c24s004_800" , "d") from _call_BlinkXPS3_2003
    meg "Explícame cosas de aquella época, por favor. Es una de mis épocas favoritas de la música."
    scene c24s004_750a with dissolve
    "Las dos mujeres se enzarzan en una conversación sobre una época pasada de clubs de música donde pasaban cosas importantes."
    stop music fadeout (1.5)
    "Un tiempo en el que podías coincidir con músicos famosos en clubs que no estaban abarrotados."
    play music ("music/Memories-Instrumental.ogg")
    call BlinkXPS3 ("c24s004_805" , "f") from _call_BlinkXPS3_2004
    kim "Hola, [mee]. ¿Qué hay, [meg]?"
    kim "¿Puedo pedirte un favor, [mee]?"
    scene c24s004_750b with dissolve
    mee "Lo que quieras, cielo."
    meg "¿Qué pasa, [kim]?"
    call BlinkXPS3("c24s004_810" , "d") from _call_BlinkXPS3_2005
    kim "Al ponerme el uniforme para esta noche lo he roto. Me va un poco apretado..."
    kim "He intentado coserlo, pero... estoy muy nerviosa y soy incapaz de enhebrar la aguja."
    call BlinkXPS3("c24s004_815" , "d") from _call_BlinkXPS3_2006
    mee "Dame ese uniforme. Deja que la abuela haga su magia con la aguja."
    mee "¿Hay hilo y aguja en esa bolsa? Siéntate mientras lo coso."
    call BlinkXPS3("c24s004_820" , "f") from _call_BlinkXPS3_2007
    "Unos minutos después..."
    mee "Ya está cosido. He reforzado alguna de las costuras que parecían más débiles."
    mee "Ese uniforme estaba muy mal cosido."
    call BlinkXPS3("c24s004_825" , "d") from _call_BlinkXPS3_2008
    kim "Gracias, [mee]. No sé qué habría hecho sin ti. Voy a probármelo a ver si no rompo nada esta vez."
    call BlinkXPS3("c24s004_830" , "d") from _call_BlinkXPS3_2009
    meg "Pruébatelo en el baño si quieres y así te lo vemos puesto."
    meg "Y [mee] puede repararlo si se rompe alguna otra costura."
    call BlinkXPS3("c24s004_835" , "d") from _call_BlinkXPS3_2010
    mee "O puedes subir a mi habitación si quieres. O incluso cambiarte aquí."
    mee "*Risa* Esta cocina ya ha visto a mucha gente desnuda últimamente."
    call BlinkXPS3("c24s004_840a" , "d") from _call_BlinkXPS3_2011
    meg "¿A quién? Creía que la zona nudista era solo en el jacuzzi."
    call BlinkXPS3("c24s004_845a" , "d") from _call_BlinkXPS3_2012
    kim "Oí que [mc] se había desnudado aquí para poner fin a una discusión sobre la desnudez el día del secuestro."
    kim "A veces tiene unos métodos... extraños..."
    kim "Dame la bolsa. [mc] está ocupado en la piscina y el resto somos todas chicas. Voy a cambiarme en ese rincón."
    call BlinkXPS3("c24s004_840b" , "d") from _call_BlinkXPS3_2013
    meg "¿Es eso cierto? ¿[mc] se desnudó durante el secuestro?"
    call BlinkXPS3("c24s004_845b" , "d") from _call_BlinkXPS3_2014
    mee "*Risa* No, [mc] lo hizo después del secuestro. Me estaba comportando como una idiota y me puso en mi sitio."
    mee "*Risa* La que se desnudó durante el secuestro fui yo. O más bien, ya estaba desnuda pero dejé caer la toalla."
    call BlinkXPS3("c24s004_850" , "d") from _call_BlinkXPS3_2015
    kim "Tía [bet] me lo contó. Fuiste muy valiente y sirvió para que los secuestradores se despistaran y [eva] pudiera entrar."
    call BlinkXPS3("c24s004_855" , "d") from _call_BlinkXPS3_2016
    meg "¡Esperad! Había oído lo del secuestro, pero no me había enterado de nada de eso..."
    meg "¡Me lo tenéis que explicar todo!"
    scene c24s004_860An with dissolve
    "Mientras [mee] pone en antecedentes a [meg], [kim] se prueba el uniforme para el evento de la noche."
    call addProfileImageS3 (8, "kim_8", kim, _(": 15 - Especial"), "") from _call_addProfileImageS3_9
    call BlinkXPS3("c24s004_865" , "d") from _call_BlinkXPS3_2017
    kim "¡Ha quedado genial, [mee]! ¡Muchas gracias!"
    scene c24s004_750c with dissolve
    meg "¡Estás monísima con ese uniforme!"
    mee "Es super gracioso. Pareces salida de una película de Corea o Vietnam, cuando las actrices y cantantes se vestían de militares para apoyar a las tropas."
    call BlinkXPS3("c24s004_870" , "d") from _call_BlinkXPS3_2018
    kim "La verdad es que es muy chulo. Tengo ganas de hacer este evento. El yate es increíble."
    call addProfileImageS3 (5, "kim_5", kim, _(": 15 - Especial"), "") from _call_addProfileImageS3_10
    kim "Ahora solo necesito llamar a un Under para que me lleve a Westport."
    call BlinkXPS3("c24s004_875" , "d") from _call_BlinkXPS3_2019
    meg "¿Dónde de Westport tienes que ir y a qué hora tienes que estar?"
    meg "Te podría llevar yo antes de ir al club."
    scene c24s004_750d with dissolve
    "Las tres mujeres pasan un rato hablando sobre el trabajo de [kim] y geografía de Westport."
    "También hablan de la familia y de los planes que tiene cada una de ellas."
    "[kim] llama 'Abuela' un par de veces a [mee]."
    stop music fadeout (1.5)
    "Ninguna de ellas se da cuenta."
    return
label c24s005_Ama:
    if _in_replay:
        call mrS3_ama_route from _call_mrS3_ama_route_6
        call mrS3_eva_route from _call_mrS3_eva_route_4
    scene c24s004_685b with fade
    play music ("music/i-feel-alive.ogg")
    "De vuelta en la furgoneta..."
    call BlinkXPS3 ("c24s005_010" , "d") from _call_BlinkXPS3_2020
    ama "Disculpa, tenía que acabar de escribir algo que tienes que firmar."
    mc "¿Qué es?"
    call BlinkXPS3 ("c24s005_015" , "d") from _call_BlinkXPS3_2021
    ama "Aquí no. Te lo explico en tu habitación."
    mc "¡Qué misteriosa! Pero es muy pronto para que venga el helicóptero ¿no?"
    call BlinkXPS3 ("c24s005_020" , "d") from _call_BlinkXPS3_2022
    ama "No va a venir aquí. No quieres que Iron Fist sepa dónde vives, ¿verdad?"
    mc "Si tienen mi teléfono, supongo que también tienen mi dirección."
    call BlinkXPS3 ("c24s005_025" , "d") from _call_BlinkXPS3_2023
    ama "En tu ficha de empleado de NTR figura tu teléfono, pero tu dirección es de San Luis Obispo."
    ama "*Risa* Vives en el campo de beisbol de la universidad. Por si teníamos algún topo."
    mc "*Risa* Espero que sea debajo de las gradas o me mojaré cuando llueva."
    mc "¿Dónde va a ir a buscarnos el helicóptero, entonces?"
    call BlinkXPS3 ("c24s005_030" , "d") from _call_BlinkXPS3_2024
    ama "Hemos alquilado un campo de tiro todo el fin de semana. Mañana por la tarde [eva] enseñará a disparar a algunas chicas."
    ama "El helicóptero nos recogerá allí en cuatro horas."
    mc "OK. Voy a ducharme."
    scene c24s005_030d with dissolve
    ama "Voy a saludar a [mar] y te veo en 15 minutos en tu habitación."
    mc "¿15 minutos? Acabo de decir que me tenía que duchar. ¡Tenemos cuatro horas!"
    ama "*Risa* La última vez que te espié duchándote, no eras tan lento como [emm]. ¿Te tienes que maquillar y depilar las piernas?"
    mc "*Risa* Vale, 15 minutos ¿Qué llevas en esa bolsa?"
    ama "Lo que vas a firmar y lo que te vas a poner."
    call BlinkXPS3 ("c24s005_035" , "f") from _call_BlinkXPS3_2025
    "15 minutos después..."
    mc "Ya estoy aquí. ¿Qué querías que firmara? ¿Y por qué tanta prisa?"
    if ama._var("route"):
        scene c24s005_035d with dissolve
        "[ama] se levanta y te da un tierno beso."
        call BlinkXPS3 ("c24s005_040" , "d") from _call_BlinkXPS3_2026
        ama "Primero, mis labios..."
        mc "Me parece la forma ideal de empezar una reunión de trabajo."
        call BlinkXPS3 ("c24s005_045" , "d") from _call_BlinkXPS3_2027
        ama "*Risa* Espero que no hagas lo mismo con Ichigo esta noche."
        mc "No, eso solo lo hago con mercenarias rubias."
        ama "*Risa* Que no te oiga [eva]."
        scene c24s005_050d with dissolve
        "[ama] se gira para sacar algo de la bolsa de viaje que ha traído."
        "Las vistas son excelentes."
        call BlinkXPS3 ("c24s005_050" , "f") from _call_BlinkXPS3_2028
        ama "Lo siguiente que tienes que firmar es esto. Hoy es tu primer día como CEO y el primer documento que vas a firmar."
    else:
        scene c24s005_050d with dissolve
        ama "Dame un segundo."
        "[ama] se agacha para sacar algo de la bolsa de viaje que ha traído."
        call BlinkXPS3 ("c24s005_050" , "f") from _call_BlinkXPS3_2029
        ama "Tienes que firmar es esto. Hoy es tu primer día como CEO y el primer documento que vas a firmar."
    scene c24s005_050e with dissolve
    "[ama] te entrega un papel escrito a mano, con varios tachones."
    if persistent.pregnancy:
        if persistent.walkthrough:
            $ wt1 = _("Sin consecuencias.")
            $ wt2 = _("Sin consecuencias. [mc] lo leerá y sabrá lo que pone")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Leer el documento." (wt = wt1):
                "Carta de autorización"
                "Como CEO de NTR, por la presente autorizo a la Srta. Gilford a realizar un estudio exhaustivo de las necesidades"
                "y requisitos pertinentes para establecer la Beca NTR para el próximo año académico."
                "Esta beca {s}del programa{/s} tiene como objetivo apoyar a los nadadores de Newport que han decidido abandonar la natación de competición"
                "y {s}desean{/s} aspiran a convertirse en entrenadores de natación."
                "A la Srta. Gilford se le confían las siguientes responsabilidades:"
                "*Realizar una evaluación exhaustiva para determinar los criterios y requisitos específicos para {s}la{/s} esta nueva beca."
                "*Interactuar con posibles {s}estudiantes{/s} candidatos para comprender sus motivaciones, desafíos y aspiraciones en la transición de nadadores a entrenadores."
                "*Colaborar con clubes de natación locales, instituciones educativas y partes interesadas relevantes para desarrollar un marco de becas sólido."
                "*Asegurarse de que la beca proporcione el apoyo financiero, los recursos y las oportunidades de desarrollo profesional adecuados para los candidatos seleccionados."
                "Se espera que la Srta. Gilford presente sus conclusiones y recomendaciones en los próximos tres días,"
                "tras lo cual se desarrollará la estructura final y el plan de implementación de la Beca NTR."
                "Esta autorización entra en vigor inmediatamente y permanecerá vigente hasta la finalización del proyecto."
                "Firmado:"
                "[mc] Marks"
                "CEO de NTR"
            "No leer el documento." (wt = wt2):
                pass
    $ resetWalkthrough ()
    mc "Esto es la creación de una beca hecha a medida para [sim]. 'Nadadores de Newport que han decidido abandonar la natación de competición y aspiran a convertirse en entrenadores'."
    ama "He oído vuestra conversación en la piscina y he creído que, con todo el mal que ha hecho NTR, es hora de que haga algo bueno."
    mc "Pero puedes hacer esto sin mi autorización. Tú también eres accionista."
    call BlinkXPS3 ("c24s005_055" , "d") from _call_BlinkXPS3_2030
    ama "Todavía no tengo un cargo oficial en NTR, con lo que no puedo hacerlo. Tiene que ser todo legal si queremos que la empresa evolucione, [mc]."
    ama "La estaba acabando de escribir en la furgoneta. De ahí los tachones."
    mc "*Risa* Le quitan un punto de oficialidad, pero supongo que es igual de legal."
    mc "Y tú vuelves a demostrar que eres una mujer increíble."
    "Firmas el documento."
    call BlinkXPS3 ("c24s005_060" , "d") from _call_BlinkXPS3_2031
    ama "Gracias, pero no hay nada que no estuviera dispuesta a hacer por esta familia."
    ama "Haga lo que haga, nunca os podré devolver lo que me estáis dando vosotros."
    mc "La familia no es un negocio, [ama]. No hay que pesar lo que se da o se recibe. Pero tú estás dando mucho."
    stop music fadeout (1.5)
    call BlinkXPS3 ("c24s005_065" , "d") from _call_BlinkXPS3_2032
    play music ("music/Acoustic-Inspirational.ogg")
    ama "Y lo siguiente es lo que te vas a poner esta tarde."
    mcp "(Como siempre, cambiando de tema en el momento en que alguien la alaba. Al menos esta vez sonríe.)"
    mc "¿Mis trajes no son adecuados para la reunión con Iron Fist?"
    call BlinkXPS3 ("c24s005_070" , "d") from _call_BlinkXPS3_2033
    ama "Sí, y ahora me darás uno. El que te pondrás esta noche."
    mc "No lo entiendo. ¿Me traes un traje para la tarde y yo te doy uno para la noche? ¿Me voy a cambiar en el yate?"
    call BlinkXPS3 ("c24s005_075" , "d") from _call_BlinkXPS3_2034
    ama "¿No has hablado con [eva]?"
    mc "Hoy no. ¿Por qué?"
    ama "Te tenía que haber llamado esta mañana."
    mc "He dormido hasta tarde y me quedé sin batería anoche. Lo he puesto a cargar cuando me he levantado. Ni siquiera lo he encendido aún."
    call BlinkXPS3 ("c24s005_080" , "d") from _call_BlinkXPS3_2035
    ama "Eso lo explica todo."
    ama "Vas a hacer prácticas de tiro con [eva] antes de ir a la reunión. Dice que no has practicado más después del primer día en el bosque."
    mc "¿Por eso habéis alquilado el campo de tiro?"
    call BlinkXPS3 ("c24s005_085" , "d") from _call_BlinkXPS3_2036
    ama "Por eso, para enseñar a las chicas a disparar, y para que venga el helicóptero a buscarnos."
    if eva._var("route"):
        call BlinkXPS3 ("c24s005_090" , "d") from _call_BlinkXPS3_2037
        ama "[eva] quería pasar un rato a solas contigo. Ella no lo llama cita sino entrenamiento."
        ama "Pero no lo dudes. Es una cita. Con armas en vez de con comida o vino."
        mc "¿No crees que me lo debería haber preguntado antes a mí?"
        call BlinkXPS3 ("c24s005_095" , "d") from _call_BlinkXPS3_2038
        ama "*Risa* Si no te hubieras quedado sin batería o lo hubieras encendido..."
        mc "*Risa* Touché."
        mc "¿Qué tengo que ponerme para la cita?"
        call BlinkXPS3 ("c24s005_100" , "d") from _call_BlinkXPS3_2039
        ama "Lo que hay en la bolsa. Te espero fuera mientras te cambias."
        if ama._var("route"):
            mc "Sabes que no es necesario, ¿verdad?"
            scene c24s005_100d with dissolve
            ama "*Risa* Si te desnudas delante mío, es posible que no llegues a la cita con [eva]."
            ama "*Risa* Y seguramente me lo haría pagar. De forma dolorosa. Mientras duermo."
        else:
            mc "OK. En dos minutos estaré vestido."
            scene c24s005_100d with dissolve
    else:
        call BlinkXPS3 ("c24s005_100" , "d") from _call_BlinkXPS3_2040
        ama "Ponte lo que hay en la bolsa. Te espero fuera mientras te cambias."
        if ama._var("route"):
            mc "Sabes que no es necesario, ¿verdad?"
            scene c24s005_100d with dissolve
            ama "*Risa* Si te desnudas delante mío, es posible que no llegues a la clase de tiro con [eva]."
            ama "*Risa* Y seguramente me lo haría pagar. De forma dolorosa. Mientras duermo."
        else:
            mc "OK. En dos minutos estaré vestido."
            scene c24s005_100d with dissolve
    ama "Saca el traje que te vas a poner para el yate."
    scene c24s005_100e with fade
    "Dos minutos después..."
    mc "[ama], ya estoy vestido. Aunque no entiendo para qué necesito esto..."
    call BlinkXPS3 ("c24s005_105" , "f") from _call_BlinkXPS3_2041
    ama "*Risa* ¡Estás ridículo!"
    mc "*Risa* Lo sé. Más que a practicar tiro, parece que voy a hacer una carrera en Laguna Seca."
    call BlinkXPS3 ("c24s005_110" , "d") from _call_BlinkXPS3_2042
    if eva._var("route"):
        ama "*Risa* Bueno, esa es la otra parte de la cita con [eva]."
    ama "¿Has montado en moto alguna vez?"
    mc "No..."
    call BlinkXPS3 ("c24s005_115" , "d") from _call_BlinkXPS3_2043
    ama "Pues hoy va a ser tu primera vez. [eva] quería que fueras seguro. El traje lo ha elegido ella."
    ama "Es uno de los trajes de skydiving de NTR. Era lo más adecuado que teníamos para ti."
    mc "¿No vamos a ir en la furgoneta al campo de tiro?"
    call BlinkXPS3 ("c24s005_120" , "d") from _call_BlinkXPS3_2044
    ama "No, te lleva [eva]. Yo me quedaré con [mar] y [nor], pasando la tarde hasta que se acerque la hora de que llegue el helicóptero."
    mc "*Risa* Es decir, motos y armas. ¿Alguna cosa peligrosa más?"
    call BlinkXPS3 ("c24s005_125" , "d") from _call_BlinkXPS3_2045
    ama "*Risa* [eva]."
    mc "*Risa* No me da miedo. Seguramente porque no soy capaz de imaginar la mitad de las cosas que puede hacerme."
    mc "Bueno, las armas tampoco después del primer entrenamiento. Y las motos..."
    call BlinkXPS3 ("c24s005_130" , "d") from _call_BlinkXPS3_2046
    play sound ("music/motorbike.ogg")
    "Suena una moto a toda velocidad por la carretera, todavía lejos."
    ama "Creo que la tuya está llegando."
    mc "Te veo luego, entonces."
    ama "Sí, cuando falten 20 minutos para que llegue el helicóptero, iré al campo de tiro. Así tienes tiempo de cambiarte."
    if ama._var("route"):
        scene c24s005_035e with dissolve
        "[ama] se despide de ti con otro tierno beso."
    ama "Te veo luego."
    scene black with dissolve
    stop music fadeout (1.5)
    "Mientras bajas las escaleras, enciendes el móvil. Tienes 32 llamadas perdidas de [eva]. Y 24 mensajes de texto."
    return
label c24s005_Eva:
    if _in_replay:
        call mrS3_eva_route from _call_mrS3_eva_route_5
    call BlinkXPS3 ("c24s005_150" , "f") from _call_BlinkXPS3_2047
    play music ("music/I-Can-Feel-it-Coming.ogg")
    "Al salir a la calle, [eva] ya te está esperando."
    mc "Hola, [eva]."
    if eva._var("route"):
        scene c24s005_155a with dissolve
        "[eva] salta a tus brazos buscando tus labios. Hace días que no os habéis besado."
    call BlinkXPS3 ("c24s005_160" , "d") from _call_BlinkXPS3_2048
    eva "Hola, [mc]. ¿Preparado para el entrenamiento?"
    mc "*Risa* Para el entrenamiento sí. Para la moto no tanto."
    play sound ("music/punch.ogg")
    scene c24s005_155b with hpunch
    "[eva] te pega un puñetazo en el hombro. No es un puñetazo suave. Los matones del colegio te pegaban más flojo."
    mc "¡Ouch! ¿A qué ha venido eso?"
    eva "A que así aprenderás a responder a mis llamadas."
    mc "¡Me quedé sin batería y no me he acordado de encenderlo hasta hace un momento!"
    call BlinkXPS3 ("c24s005_165" , "d") from _call_BlinkXPS3_2049
    eva "Seguro que no se te vuelve a olvidar."
    call BlinkXPS3 ("c24s005_170" , "d") from _call_BlinkXPS3_2050
    eva "¿Has montado alguna vez en moto?"
    mc "No... ¿Hay algo que deba saber?"
    eva "Tan solo agárrate fuerte a mí e intenta no moverte demasiado. Actúa como si fueras mi mochila."
    call BlinkXPS3 ("c24s005_175" , "d") from _call_BlinkXPS3_2051
    eva "*Risa* Y no grites ni llores en las curvas."
    mc "*Risa* Lo intentaré, pero no prometo nada."
    mc "*Risa* ¿En las rectas puedo llorar?"
    scene c24s005_180An with dissolve
    eva "*Risa* Puedes hacerlo, pero no te voy a oír ni voy a parar."
    scene c24s005_180f with dissolve
    stop music fadeout (1.5)
    eva "¡Sube en la moto!"
    play sound ("music/motorbike.ogg")
    scene c24s005_185pv with fade
    show c24s005_185v
    pause (7.4)
    scene c24s005_185dv
    if eva._var("route"):
        "[eva] arranca para llevarte a la cita más extraña de tu vida."
    else:
        "[eva] arranca para llevarte al entrenamiento más extraño de tu vida."
    "Consigues no gritar en la primera curva pese al frenazo de [eva]. Te comportas como una buena mochila."
    return

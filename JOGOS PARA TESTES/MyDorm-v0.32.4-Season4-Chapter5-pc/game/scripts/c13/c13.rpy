label c13:
    call c13s001_KiaraEileen from _call_c13s001_KiaraEileen
    call c13s001_SleepingInTheCouch from _call_c13s001_SleepingInTheCouch
    call c13s002_TalkToTheFamily from _call_c13s002_TalkToTheFamily
    call c13s002_TheHospital from _call_c13s002_TheHospital
    call c13s003_ScarlettHouse from _call_c13s003_ScarlettHouse
    call c13s004_KiaraAndScarlett from _call_c13s004_KiaraAndScarlett
    call c13s004_GetSaira from _call_c13s004_GetSaira
    call c13s005_SamanthaHouse from _call_c13s005_SamanthaHouse
    return
label c13s001_KiaraEileen:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        call mrS3_eil_route from _call_mrS3_eil_route_11
        if eil._var("route"):
            call mrS3_eri_route from _call_mrS3_eri_route_15
            call mrS3_oma_route from _call_mrS3_oma_route_9
            if mc._var("relationships")<2:
                call mrS3_rels from _call_mrS3_rels_32
    call BlinkXP ("c13s001_005" , "d") from _call_BlinkXP
    $renpy.sound.play("music/Motor.ogg", loop=True)
    mc "¿Qué ha pasado, [eil]?"
    eil "Lo de siempre. Mi padre bebió demasiado y empezó a gritarle a mi madre por alguna tontería."
    eil "Esta vez la agarró del brazo y empezó a arrastrarla por la casa. En ese momento llegué yo."
    call BlinkXP ("c13s001_010" , "d") from _call_BlinkXP_1
    mc "¿Estás bien, Kiara?"
    kia "Sí, no ha sido tanto como [eil] dice. Me ha hecho un poco de daño y..."
    kia "¿Podemos esperar a llegar a tu casa para seguir hablando de esto? Es raro hablar con dos cogotes..."
    mc "Ningún problema, Kiara."
    call BlinkXP ("c13s001_015" , "d") from _call_BlinkXP_2
    mc "Hoy dormiréis en mi habitación. Todo el mundo está durmiendo ahora mismo y sería complicado habilitaros otra habitación."
    eil "¿Dónde vas a dormir tú?"
    mc "Con vosotras, por supuesto. Es mi habitación."
    call BlinkXP ("c13s001_020" , "v") from _call_BlinkXP_3
    eil "¡[mc]! No puedo dejar que duermas con mi madre..."
    mc "Eile, es broma. Buscaré algún sitio donde dormir sin molestar a nadie."
    call BlinkXP ("c13s001_025" , "d") from _call_BlinkXP_4
    eil "Lo siento, no tengo el ánimo para bromas ahora mismo."
    mc "No te preocupes. Quizás no era el momento más adecuado para bromas."
    scene c13s001_030 with dissolve
    "Continúas conduciendo hacia casa. Ahora en silencio. El camino parece eterno una vez la adrenalina que te ha traído aquí volando desaparece."
    stop sound fadeout (1.5)
    scene c13s001_035 with fade
    mc "Pues esta es mi habitación, Kiara. Hay un baño con ducha justo pasar el gimnasio. [eil] conoce la casa, con lo que cualquier duda se la puedes preguntar."
    play music "music/LostVoices.ogg"
    mc "Si necesitáis cualquier cosa, estaré durmiendo en los sofás que acabamos de pasar en la planta debajo de esta."
    kia "Gracias, [mc], me sabe mal que tengas que dormir en un sofá por nuestra culpa."
    eil "Podrías dormir en este sofá si quieres. No queremos echarte de tu habitación."
    call BlinkXP ("c13s001_040" , "d") from _call_BlinkXP_5
    kia "O mejor aún, dormimos nosotras en esos sofás y tu duermes en tu cama como debería ser."
    mc "Eso no puedo permitirlo. Sois mis invitadas y vais a dormir en una cama."
    call BlinkXP ("c13s001_045" , "d") from _call_BlinkXP_6
    eil "Mamá... ¿no has metido pijamas en la bolsa?"
    call BlinkXP ("c13s001_050" , "d") from _call_BlinkXP_7
    kia "¡Oops! No. Me he despistado. Con las prisas he pensado en ropa, artículos de higiene... pero no en los pijamas."
    mc "No os preocupéis. Podéis coger camisetas o pijamas míos para dormir. [eil] sabe donde están."
    call BlinkXP ("c13s001_055" , "d") from _call_BlinkXP_8
    kia "Se me hace raro que [eil] sepa más de una casa que yo. *Risa* Pero después de tantos años juntos es normal."
    kia "Es una lástima que lo dejáseis cuando estabas en Portland. Pensaba que volveriais a estar juntos cuando volvieras de la universidad."
    mc "Bueno, no funcionaba a distancia."
    if eil._var("route"):
        call BlinkXP ("c13s001_060" , "d") from _call_BlinkXP_9
        "[eil] te mira interrogativamente, como si te pidiera permiso para desvelar la noticia a su madre."
        "Asientes."
        call BlinkXP ("c13s001_065" , "d") from _call_BlinkXP_10
        eil "Mamá, volvemos a estar juntos."
        if mc._var("relationships") > 1:
            eil "No de la misma forma que antes, pero volvemos a estarlo."
        call BlinkXP ("c13s001_070" , "h") from _call_BlinkXP_11
        kia "¡Eso es fantástico! Me alegro mucho por vosotros."
        mc "Gracias, Kiara."
    else:
        call BlinkXP ("c13s001_065" , "d") from _call_BlinkXP_12
        eil "Además, ahora somos buenos amigos. Lo importante es que no hemos perdido la relación."
    scene c13s001_075 with dissolve
    mc "Voy a dejar que os cambiéis y os acostéis. Mañana hablaremos de cómo nos organizamos y de lo que ha pasado esta noche."
    kia "Gracias, [mc]."
    eil "Gracias. Por todo."
    scene c13s001_080 with fade
    "Bajas a la planta de las estudiantes. Parece mentira que Kim te despertara en este mismo sofá hace menos de 24 horas."
    mcp "{i}(Soy idiota. Les he dicho que cogieran mis pijamas y no he cogido uno para mí. Ni siquiera unos shorts.){/i}"
    mcp "{i}(*Risa mental* Dormir en pelotas en el sofá no sería muy adecuado si alguna de las estudiantes se despierta antes que yo.){/i}"
    "Vuelves a tu habitación."
    scene c13s001_085 with fade
    play sound "music/knock.ogg"
    "*Knock-Knock*"
    mc "¿Puedo entrar? No he cogido nada para mí, para dormir."
    eil "*A través de la puerta* Espera un segundo, por favor."
    "Al cabo de unos segundos..."
    kia "*A través de la puerta* Puedes pasar."
    scene c13s001_090 with fade
    mc "Disculpad, pero es que no he cogido mi propio pijama."
    mc "Aunque viendo que a vosotras os queda mejor mi ropa que a mí..."
    call BlinkXP ("c13s001_095" , "d") from _call_BlinkXP_13
    eil "*Risa* ¿Ya estás diciendo payasadas? ¿Tú no ibas a dormir?"
    mc "¿Payasadas? {b}¿Yo?{/b} ¡Qué va! Tenéis un espejo en ese armario si queréis, en el interior de la puerta."
    mc "Y sobre lo de dormir... demasiados nervios para dormir ahora mismo."
    scene c13s001_100 with dissolve
    mc "¿Eso es lo que te ha hecho Solomon? Parece un hematoma importante, deberíamos ir al hospital a mirarlo."
    scene c13s001_105AnBlink with dissolve
    kia "No hace falta, tan solo es un morado. No es la primera vez..."
    mc "Espero que sea la última."
    mc "Pero de todas formas, habría que mirarlo. Sin dejar pasar muchos días."
    mc "¿Quieres hablar sobre lo que ha pasado?"
    call BlinkXP ("c13s001_110" , "d") from _call_BlinkXP_14
    kia "Nosotras tampoco vamos a poder dormir, si quieres te lo explico ahora antes de que se nos olviden los detalles."
    kia "Es lo menos que te debo..."
    mc "Kiara, no me debes nada. Es más, no tienes que explicarme nada de lo que ha pasado."
    mc "Lo decía porque en mi familia acostumbramos a hablarlo todo para quitarnos el peso de encima."
    call BlinkXP ("c13s001_115" , "d") from _call_BlinkXP_15
    eil "Es una buena costumbre, Mamá. Deberíamos aplicarla en casa."
    eil "¿Nos sentamos?"
    mc "Sólo si tu madre quiere."
    call BlinkXP ("c13s001_120" , "d") from _call_BlinkXP_16
    kia "Sí, probemos esa costumbre familiar vuestra. Está claro que las costumbres de mi familia no son las mejores."
    mc "No te machaques ahora. [eil] ha salido muy bien. Y tú también."
    scene c13s001_125 with fade
    mc "¿Por dónde quieres empezar, Kiara?"
    kia "Es difícil decidirlo. ¿Cuánto sabes? ¿Te pongo en antecedentes?"
    eil "Mamá, [mc] sabe lo que pasaba cuando Papá bebía... cuando aún estábamos en el instituto."
    call BlinkXP ("c13s001_130" , "d") from _call_BlinkXP_17
    kia "Entonces... esta noche..."
    kia "Desde que Solomon ha vuelto a beber, no se había puesto violento ninguna vez, esta es la primera."
    mc "Eso es una vez más de las necesarias."
    call BlinkXP ("c13s001_135" , "d") from _call_BlinkXP_18
    kia "Lo sé. Cuando dejó de beber lo hizo, entre otras razones, por que le amenacé con dejarle si me volvía a poner la mano encima."
    kia "Todo fue bien durante dos años, y después volvió a beber."
    mc "Lo sé, [eil] me lo explicó. ¿Sabéis por qué volvió?"
    call BlinkXP ("c13s001_140" , "d") from _call_BlinkXP_19
    eil "No. Ya te dije que empezó a beber una cerveza al salir del trabajo, con los compañeros. Le dijimos que no lo hiciera, pero no nos hizo caso."
    eil "\"Sólo es una cerveza un día a la semana\" decía. Como te dije, de ahí pasó varias cervezas, a un whisky, a varios whiskys..."
    mc "Pero no estaba violento hasta hoy, ¿qué ha pasado hoy?"
    call BlinkXP ("c13s001_145" , "d") from _call_BlinkXP_20
    kia "Cuando he llegado de trabajar estaba muy borracho."
    kia "Se enfadó mucho cuando le dije que tardaría 30 minutos en preparar la cena."
    mc "Acababas de llegar, ¿cuando quería que la preparases?"
    call BlinkXP ("c13s001_150" , "d") from _call_BlinkXP_21
    eil "Cuando está borracho el alcohol sustituye a la lógica."
    eil "Puede quejarse de cualquier cosa, tenga razón o no. Y si le llevas la contraria se enfada más todavía. No se puede razonar con él."
    mc "Tú aún estabas en el trabajo, ¿no?"
    call BlinkXP ("c13s001_155" , "d") from _call_BlinkXP_22
    eil "Sí, ayer... hoy... tenía que cerrar el café y hacer la caja. A los temporales como [eri] no les dejan hacerla."
    eil "Si hubiera estado ahí..."
    mc "No es culpa tuya. Estabas trabajando. Dejaste la universidad para ayudar económicamente en casa porque tu padre perdió el trabajo. No se te puede exigir más."
    eil "Lo sé, pero..."
    call BlinkXP ("c13s001_160" , "d") from _call_BlinkXP_23
    kia "[mc] tiene razón. No es culpa tuya. Ya haces demasiado. Pero mejor que siga..."
    kia "Durante la cena estuvo gruñón, quejándose de la limpieza, de cenar tarde, y de... de otras cosas..."
    mc "No hace falta que me expliques todo si no quieres..."
    call BlinkXP ("c13s001_165" , "d") from _call_BlinkXP_24
    kia "No es eso... es que son temas de pareja..."
    mc "Entonces no me hace falta saberlo."
    kia "Es que... si no te lo explico... no vas a poder entender el resto..."
    mc "Como quieras, pero te puedo asegurar que lo que me digas no va a salir de esta habitación."
    call BlinkXP ("c13s001_170" , "d") from _call_BlinkXP_25
    kia "Se quejaba de que ya no tenemos sexo nunca. ¡Hale, ya lo he dicho! ¡Ufff! Realmente va bien esto de hablar las cosas..."
    kia "Desde que empezó a beber, el no... no funciona bien... no le funciona bien su..."
    mc "Vale, lo entiendo. No tiene erecciones."
    call BlinkXP ("c13s001_175" , "d") from _call_BlinkXP_26
    kia "Sí que las tiene. Pero duran segundos. Y no vuelven a subir. Hace meses que no... que no tenemos relaciones."
    mc "El alcohol puede tener ese efecto."
    call BlinkXP ("c13s001_180" , "d") from _call_BlinkXP_27
    kia "Pues después de cenar dijo que quería sexo. Había estado bebiendo cerveza durante la cena, y mientras esperaba a que la hiciera, añadiendo aún más alcohol al que llevaba cuando llegué."
    kia "No me apetecía nada. En ese momento estaba frustrada y enfadada. Se lo dije."
    mc "Y se puso violento."
    call BlinkXP ("c13s001_185" , "d") from _call_BlinkXP_28
    kia "Levantó la mano para darme una bofetada, pero se paró a tiempo."
    kia "Me entró miedo."
    kia "Le seguí a la habitación."
    call BlinkXP ("c13s001_190" , "d") from _call_BlinkXP_29
    kia "Se desnudó y aquello estaba fláccido. No iba a subir..."
    kia "Y se enfadó aún más."
    kia "Empezó a culparme a mí. Dijo que ya no me vestía sexy para él nunca. Que ya no le excitaba. Que se iba a buscar una más joven que yo."
    mc "*Entre dientes* ¡Capullo!"
    call BlinkXP ("c13s001_195" , "d") from _call_BlinkXP_30
    kia "Me cogió por el brazo y empezó a llevarme de habitación en habitación. Enseñándome todo lo que según él estaba mal."
    kia "Platos por fregar... los de {b}SU{/b} comida y los de la cena..."
    kia "Alguna ventana no estaba del todo limpia... la compra que habían entregado ese día estaba por guardar... había ropa por poner en la lavadora..."
    call BlinkXP ("c13s001_200" , "d") from _call_BlinkXP_31
    eil "Ahí es donde llegué yo... el espectáculo era dantesco. Mi padre en pelotas arrastrando a mi madre, vestida, del brazo por el suelo en la sala de la lavadora..."
    eil "Había ropa para poner una lavadora a lo sumo. Mi ropa de correr de la mañana, una muda de mi madre y ropa de mi padre. Olía a vómito."
    mc "¿Él no tiene manos? ¿No puede poner la lavadora mientras las dos estáis trabajando?"
    call BlinkXP ("c13s001_205" , "d") from _call_BlinkXP_32
    eil "Eso sería muy degradante para él. ¿Cómo quieres que limpie o ponga a lavar la ropa si tiene a dos mujeres en casa?"
    eil "Es mejor estar todo el día en el sofá, viendo la tele y bebiendo, y después quejarse de que no hay nada hecho en casa."
    mc "¿Entonces fue cuando os fuisteis?"
    call BlinkXP ("c13s001_210" , "d") from _call_BlinkXP_33
    eil "Entonces es cuando a él le entraron las arcadas. No solo es un borracho. Es un mal bebedor con poco aguante."
    eil "Salió corriendo hacia el baño para vomitar."
    call BlinkXP ("c13s001_215" , "d") from _call_BlinkXP_34
    kia "Y se quedó dormido encima de la taza del wáter después de hacerlo."
    kia "En ese momento [eil] me convenció para irnos. Cuando se despertara, iba a ser peor."
    call BlinkXP ("c13s001_220" , "d") from _call_BlinkXP_35
    kia "Metí algo de ropa en la bolsa de viaje, los cepillos de dientes y nos fuimos."
    kia "[eil] llamó a su amiga, la policía..."
    call BlinkXP ("c13s001_225" , "d") from _call_BlinkXP_36
    kia "Aunque le dije que no quería poner una denuncia..."
    call BlinkXP ("c13s001_230" , "d") from _call_BlinkXP_37
    eil "La llamaba para saber si podíamos quedarnos en su casa, no para poner una denuncia. Su abuelo se iba hoy y sabía que tendría una habitación libre."
    eil "Pero está en San Diego con sus padres. No le he dicho por qué la llamaba, no quería preocuparla."
    eil "Y entonces te he llamado a ti. No es que fueras la segunda opción, pero creía que..."
    mc "Que si tu madre hablaba con una policía, Alexia la convencería para poner la denuncia."
    call BlinkXP ("c13s001_235" , "d") from _call_BlinkXP_38
    eil "Al menos la haría entrar en razón. En ese momento mi madre estaba diciendo que buscásemos algún sitio donde pasar esta noche."
    eil "Sólo esta noche..."
    call BlinkXP ("c13s001_240" , "d") from _call_BlinkXP_39
    kia "¿Qué querías que hiciera? ¿Que abandonase a mi marido y mi casa? Todos los matrimonios tienen problemas..."
    mc "Creo que es lo mejor, al menos por unos días. Que le vea las orejas al lobo."
    mc "A lo mejor reacciona y vuelve a dejar la bebida..."
    call BlinkXP ("c13s001_245" , "d") from _call_BlinkXP_40
    eil "Es lo que le he dicho. Una semana como mínimo. Al final ha aceptado. Mañana buscaremos un hotel."
    mc "No hace falta. Tenéis esta habitación para vosotras todo el tiempo que queráis."
    call BlinkXP ("c13s001_250" , "d") from _call_BlinkXP_41
    kia "No podemos hacerte eso. No podemos echarte de tu habitación durante una semana. Mañana buscamos un hotel o algo donde quedarnos unos días."
    mc "Entonces, en casa de [nor] hay una habitación vacía. Es para las estudiantes que llegan en otoño. Al menos hasta entonces la podéis usar."
    mc "A [nor] no le va a importar en el momento en que sepa vuestra situación, os lo aseguro. Al menos la situación que queráis explicarle."
    call BlinkXP ("c13s001_255" , "d") from _call_BlinkXP_42
    eil "¿De verdad crees que nos va a dejar dormir en su casa?"
    mc "Eile, a [nor] siempre le has gustado. No va a tener ningún problema con ello. ¿Cuánto hace que no la ves?"
    call BlinkXP ("c13s001_260" , "d") from _call_BlinkXP_43
    eil "Mucho. No tengo ni idea de cuanto... ¿un año? ¿dos? Al contrario que tú, cuando ella lleva a [eri] al trabajo, no entra a tomarse ni siquiera un café."
    mc "Entonces no te diré nada. Por la mañana te llevarás una pequeña sorpresa."
    mc "Creo que con esto está todo arreglado, al menos el alojamiento. ¿Necesitáis algo más?"
    call BlinkXP ("c13s001_265" , "d") from _call_BlinkXP_44
    kia "Si nos vamos a quedar una semana, deberíamos pasar por casa a buscar más ropa. Metí ropa para un par de días en la bolsa. Y ni siquiera los pijamas..."
    mc "Yo de vosotras no iría mientras Solomon esté allí, o al menos no solas. Si queréis os acompaño."
    call BlinkXP ("c13s001_270" , "d") from _call_BlinkXP_45
    eil "Yo puedo aguantar dos o tres días perfectamente. Los jueves por la noche mi padre se va de copas con sus amigos y podríamos ir a casa."
    mc "Kiara, ¿tú tienes ropa para aguantar hasta el jueves? Si no, habiendo 11 mujeres en casa, seguro que alguna os puede dejar ropa. O podéis coger mis camisetas; os quedan geniales."
    mc "Además, aunque vivamos en medio de la nada, también tenemos lavadoras. *Risa*"
    call BlinkXP ("c13s001_275" , "d") from _call_BlinkXP_46
    kia "No te preocupes, cogí mi ropa de trabajo y dos uniformes para [eil], eso es lo más importante. El resto se puede comprar o lavar hasta que el jueves podamos volver."
    mc "Ahora que pienso, el miércoles vuelve Alexia, con lo que también nos podría acompañar el jueves si fuera necesario. Tener una policía cerca impone."
    mc "Y, una vez aclarado todo esto, os voy a dejar dormir."
    if eil._var("route"):
        mc "¿Puedo hablar un momento en privado contigo, [eil]?"
        call BlinkXP ("c13s001_280" , "d") from _call_BlinkXP_47
        eil "Sí, vamos fuera. Ahora vuelvo, Mamá."
        call BlinkXP ("c13s001_285" , "d") from _call_BlinkXP_48
        kia "No es necesario. Voy al lavabo y os dejo un poco de privacidad. ¿Cuánto tiempo necesitáis?"
        mc "*Risa* No es eso, Kiara. No vamos a enrollarnos aquí... al menos no hoy. *Risa*"
        kia "*Risa* Vale, pues vuelvo en cinco minutos. ¿Tendrás suficiente?"
        mc "Sí, por supuesto. La primera puerta a la izquierda una vez pases el gimnasio."
        call BlinkXP ("c13s001_290" , "f") from _call_BlinkXP_49
        eil "¿De qué querías hablar que no pudieras hablar delante de mi madre?"
        if mc._var("relationships") > 1:
            if eri._var("route"):
                mc "Ya sabes que estoy con [eri]. Solo me gustaría que Kiara estuviera sobreaviso de que puede ver cosas que le sorprendan, y no quiero que piense que te estoy engañando."
            elif oma._var("route"):
                mc "Ya sabes que estoy con Alexia. Solo me gustaría que Kiara estuviera sobreaviso de que puede ver cosas que le sorprendan, y no quiero que piense que te estoy engañando."
            else:
                mc "Ya sabes que estoy con alguien más. Solo me gustaría que Kiara estuviera sobreaviso de que puede ver cosas que le sorprendan, y no quiero que piense que te estoy engañando."
            call BlinkXP ("c13s001_295" , "d") from _call_BlinkXP_50
            eil "Tienes razón, no había caído en eso. Le diré lo especial de nuestra relación para que no te saque los ojos si te ve en los brazos de otra."
            mc "Además..."
            call KissXP ("c13s001_300" , "d") from _call_KissXP
            mc "Me moría por besarte antes de ir a dormir."
        else:
            call KissXP ("c13s001_300" , "d") from _call_KissXP_1
            mc "Tan solo me moría por besarte antes de ir a dormir."
        eil "No te tienes que esconder de mi madre para besarme. Ni de mi madre ni de nadie. Soy una adulta y puedo besar a quien quiera. Y al único que quiero besar es a ti."
        eil "Si necesitas decirle a alguien que salimos juntos, puedes hacerlo. Yo tampoco me tengo que esconder."
        mc "Entonces no me esconderé. Me voy a ir a mi sofá y os voy a dejar descansar... Un poco más y me olvido de coger la ropa."
        call KissXP ("c13s001_300" , "f") from _call_KissXP_2
        mc "Hasta mañana, mi amor."
        eil "Hasta mañana, mi vida. Te quiero."
        mc "Y yo a ti."
    else:
        call BlinkXP ("c13s001_285" , "d") from _call_BlinkXP_51
        kia "¿Dónde has dicho que estaba el lavabo?"
        mc "La primera puerta a la izquierda una vez pases el gimnasio."
        call BlinkXP ("c13s001_280" , "f") from _call_BlinkXP_52
        eil "Gracias por todo, [mc]. No sé qué hubiéramos hecho sin ti hoy."
        mc "Para eso estamos los amigos. Ya sabes que puedes contar conmigo para lo que necesites."
        call BlinkXP ("c13s001_310" , "d") from _call_BlinkXP_53
        eil "Cuánto te he echado de menos estos tres años. No hay hombres como tú."
        mc "¿Como yo? Espera... ¿cómo me llamabas cuando salíamos juntos? ¿Cabeza hueca?"
        call BlinkXP ("c13s001_315" , "d") from _call_BlinkXP_54
        eil "No, eso era lo que tú llamabas me llamabas a mí cuando empezamos a salir. *Risa*"
        mc "Bueno, te voy a dejar descansar. Tienes que estar agotada después de trabajar y todo el problema que te has encontrado al llegar a casa."
        mc "Hasta mañana, Eile."
        eil "Hasta mañana, [mc]."
    call BlinkXP ("c13s001_320" , "f") from _call_BlinkXP_55
    kia "¿Ya te marchas?"
    mc "Sí, es tarde y tenéis que descansar. Mañana tengo que ir a un par de sitios, pero si te despiertas pronto puedo llevarte al hospital."
    call BlinkXP ("c13s001_325" , "d") from _call_BlinkXP_56
    kia "[mc], ya te he dicho que no quería poner una denuncia..."
    mc "Te dejaré en manos de una enfermera que es buena amiga también. Si no quieres poner denuncia, no te va a obligar, pero al menos verá como está ese hematoma."
    call BlinkXP ("c13s001_330" , "d") from _call_BlinkXP_57
    "Kiara te abraza con fuerza. Es un abrazo que dice a gritos que está herida, más allá de las heridas físicas, que es vulnerable, y que necesita esa curación que dice que tus abrazos ofrecen."
    kia "Gracias, [mc]. Por darnos un techo y por entender mi decisión sobre la denuncia."
    mc "No la comparto ni la comprendo, pero tengo que respetarla. No puedo obligarte a presentar una denuncia si no quieres."
    "Pasáis unos minutos en silencio, disfrutando del abrazo. Kiara se separa de ti reluctantemente."
    call BlinkXP ("c13s001_335" , "d") from _call_BlinkXP_58
    kia "Buenas noches, [mc]. Que descanses bien."
    mc "Buenas noches, Kiara. Duerme todo lo que puedas."
    stop music fadeout (1.5)
    return
label c13s001_SleepingInTheCouch:
    if _in_replay:
        $ kat._var("relationshipPoints", 0, intention = "set")
        call mrS3_kim_makeup from _call_mrS3_kim_makeup_1
        call mrS3_kat_rps (-3, 0, 8) from _call_mrS3_kat_rps_3
    scene c13s001_080 with fade
    "Vuelves a la tercera planta después de cambiarte a algo más cómodo para dormir."
    "Nunca pensaste que echarías de menos a Lisa en ese sofá."
    scene c13s001_400 with dissolve
    "Te tumbas mirando al techo. Sabes que te va a costar dormirte después de los eventos de la noc...zzzz"
    scene black with dissolve
    centered "{size=+20}{b}DIA 15 - MARTES \n 6:13{/b}{/size}"
    "Te despiertan unos pasos y la puerta del baño que se cierra."
    scene c13s001_405 with dissolve
    "Miras el reloj del móvil. Las 6:13. Difícilmente vas a poder volver a dormirte. Ya ha amanecido."
    call BlinkXP ("c13s001_410" , "d") from _call_BlinkXP_59
    play music "music/Stardust.ogg"
    kat "Buenos días, [mc]. ¿Qué haces aquí? ¿Esperando a Lisa?"
    mc "No, hay dos chicas en mi habitación y quería dejarlas dormir tranquilamente."
    call BlinkXP ("c13s001_415" , "h") from _call_BlinkXP_60
    kat "¿Dos chicas en tu habitación? ¡Tenemos un macho en la casa!"
    mc "*Risa* No, no va por ahí. Son dos amigas que necesitaban un sitio donde pasar la noche. Les he prestado mi cama."
    call BlinkXP ("c13s001_420" , "d") from _call_BlinkXP_61
    kat "Entonces no es un macho, es un caballero. Podemos hacer un intercambio. Subo yo a tu habitación y tu duermes en mi cama. *Risa*"
    mc "*Risa* Creo que os lo podríais pasar muy bien juntas, pero creo que no como tú esperarías."
    mc "Una era mi novia en el instituto y la otra es su madre. Casada. Con un hombre."
    call BlinkXP ("c13s001_425" , "d") from _call_BlinkXP_62
    kat "*Risa* Entonces no te cambio la cama. Además, Kim se podría asustar si se despierta y te ve a ti en vez de a mí."
    if not kim._var("makeup"):
        kat "Después de lo que le dijiste ayer del mapa de su piel... creo que la hiciste feliz por todo el día."
        mc "*Risa* Lo más divertido de todo es que no lo dije sobre ella en concreto, sino que lo dije en un hipotético caso. Además sonó muy cursi."
    else:
        kat "Después de lo que le dijiste ayer sobre su piel... creo que aún está enfadada contigo."
        mc "Bueno, no era mi intención enfadarla, tan solo es que... creo que tenía razón si tanto le molesta llamar la atención."
    call BlinkXP ("c13s001_430" , "d") from _call_BlinkXP_63
    kat "¿Te importa que me siente?"
    mc "Por supuesto que no. Soy yo quien ha invadido vuestra planta."
    kat "Y nosotras hemos invadido tu casa. Lo podríamos llamar un empate."
    mc "¿Qué tal la adaptación a la nueva casa y a la nueva universidad?"
    call BlinkXP ("c13s001_435" , "d") from _call_BlinkXP_64
    kat "La universidad está genial. Tiene un muy buen programa de oceanografía y está cerca del mar. Estudiar en Phoenix sobre acuarios no tiene el mismo valor."
    mc "Está bien, es una universidad relativamente pequeña, pero de muy buen nivel."
    mc "¿Y la casa? ¿Algún problema hasta ahora?"
    call BlinkXP ("c13s001_440" , "d") from _call_BlinkXP_65
    kat "La casa es impresionante. Creía que siendo tan pocas podía haber problemas entre nosotras. Ya sabes... ser la primera gallina del corral y esas cosas."
    kat "Además, ya conocía a Lisa y me imaginaba que iba a luchar por esa posición. Pero me está sorprendiendo mucho. Parece una mujer diferente de la de Phoenix."
    mc "Parece incluso una mujer diferente de la que llegó el viernes al aeropuerto."
    call BlinkXP ("c13s001_445" , "d") from _call_BlinkXP_66
    kat "No sé que le dais de comer, pero seguid haciéndolo. Me gusta más esta Lisa."
    mc "A mí también. Hoy llega la última chica. [sai], de India."
    call BlinkXP ("c13s001_450" , "d") from _call_BlinkXP_67
    kat "¡Oh! ¿Una belleza exótica?"
    mc "Sí, lo es. Es una preciosidad. Nos conocemos de Portland."
    kat "¿Otra ex-novia?"
    mc "Sí, ¿por qué lo preguntas?"
    call BlinkXP ("c13s001_455" , "d") from _call_BlinkXP_68
    kat "Tienes a tu ex-novia del instituto durmiendo en tu habitación y vas a tener a tu ex-novia de la universidad durmiendo justo debajo."
    kat "¿Tú has oido la expresión \"Pelea de Gatas\"?"
    mc "Ni [eil] ni [sai] son así."
    call BlinkXP ("c13s001_460" , "d") from _call_BlinkXP_69
    kat "¿[eil]? ¿Pelirroja? ¿Guapísima? ¿Ojos azules? ¿Compañera de trabajo de [eri]?"
    mc "Sí, ¿por qué?"
    call BlinkXP ("c13s001_465" , "d") from _call_BlinkXP_70
    kat "¡Eres mi héroe! Si estando tan gordo como estabas en el instituto conseguiste que esa belleza se fijara en ti, hay esperanzas para el resto de nosotras."
    menu:
        "Podrías conseguir a cualquier chica que quisieras." (wt="{color=#0f0}Kate + 5{/color}"):
            $ Aux = True
        "Sólo fue un golpe de suerte." (wt="{color=#f00}Kate - 3{/color}"):
            $ Aux = False
    if Aux:
        mc "Y no solo a cualquier chica. A cualquier persona. Eres divertida, inteligente, guapa..."
        call BlinkXP ("c13s001_470" , "d") from _call_BlinkXP_71
        kat "[mc], ¿me estás tirando los trastos? *Risa* Por si no lo recuerdas, no me interesan los hombres... desde hace mucho."
        mc "{b}¿Qué? ¡No!{/b} * Risa* Eres de las pocas mujeres a quien le puedo decir que es guapa y que no se lo tomen como que quiero algo con ellas. No te estoy tirando los trastos, pero podría hacerlo."
        call BlinkXP ("c13s001_475" , "d") from _call_BlinkXP_72
        kat "¿A qué te refieres exactamente?"
        mc "Me caes muy bien. Ya te he dicho que eres divertida, inteligente, guapa... podría seguir con que tienes un gran sentido del humor, que no te dejas avasallar, que no tienes complejos..."
        if kat.rps > 5:
            mc "Tienes una personalidad arrolladora y, si te interesaran los hombres, es probable que te tirase los trastos. Creo que yo también te caigo bien."
        elif kat.rps > -5:
            mc "Tienes una personalidad arrolladora y, si te interesaran los hombres, es posible que te tirase los trastos. Aún no estoy seguro de que te caiga bien."
        else:
            mc "Tienes una personalidad arrolladora y, si te interesaran los hombres, existe alguna posibilidad de que te tirase los trastos. Pero dudo que saliera bien. No creo que te caiga bien."
        $ kat.rp (5)
    else:
        mc "Estuve en el lugar correcto en el momento correcto. Dudo que alguien como yo era entonces pudiera conseguir a alguien como [eil] en circunstancias normales."
        call BlinkXP ("c13s001_550" , "d") from _call_BlinkXP_73
        kat "Eso quiere decir que, según tú yo no podría conseguir estar con alguien como Kim o a alguien como tú si me interesaran los hombres, ¿no? Suerte que no me interesan... desde hace mucho."
        mc "Dependería mucho de la otra persona."
        call BlinkXP ("c13s001_475" , "d") from _call_BlinkXP_74
        kat "¿A qué te refieres exactamente?"
        mc "A mí me caes muy bien. Eres divertida, inteligente, guapa, tienes un gran sentido del humor, no te dejas avasallar, no tienes complejos..."
        if kat.rp_score > 5:
            mc "Tienes una personalidad arrolladora y, si te interesaran los hombres, es probable que te tirase los trastos. Creo que yo también te caigo bien."
        elif kat.rp_score > -5:
            mc "Tienes una personalidad arrolladora y, si te interesaran los hombres, es posible que te tirase los trastos. Aún no estoy seguro de que te caiga bien."
        else:
            mc "Tienes una personalidad arrolladora y, si te interesaran los hombres, existe alguna posibilidad de que te tirase los trastos. Pero dudo que saliera bien. No creo que te caiga bien."
        mc "Pero lo tendrías más difícil con personas a las que le interesara más el físico perfecto que la personalidad."
        $ kat.rp (-3)
    call BlinkXP ("c13s001_480" , "d") from _call_BlinkXP_75
    kat "¡Wow! Eso me pasa por preguntar."
    mc "Y ya que yo he respondido, ¿puedo hacer una pregunta?"
    call BlinkXP ("c13s001_485" , "d") from _call_BlinkXP_76
    kat "Sería justo que te dejara hacerla. No puedo asegurar que responda."
    mc "¿Has dicho que no te interesan los hombres desde hace mucho?"
    call BlinkXP ("c13s001_490" , "d") from _call_BlinkXP_77
    kat "*Risa* Uff, creía que sería una pregunta más complicada o comprometedora. Sí, lo he dicho."
    mc "No me refería a eso, la pregunta sería ¿qué pasó para que dejaran de interesarte?"
    call BlinkXP ("c13s001_495" , "d") from _call_BlinkXP_78
    kat "*Risa* Eso sería una segunda pregunta."
    mc "Pero..."
    kat "*Risa* No tengo la culpa de que no prestases atención a lo que decía y hayas gastado tu primera pregunta."
    mc "*Risa* Vale, me estás tomando el pelo, ya lo pillo."
    stop music fadeout (1.5)
    call BlinkXP ("c13s001_500" , "d") from _call_BlinkXP_79
    kat "Por supuesto que te estoy tomando el pelo. Eres divertido y sabes encajarlo. *Risa*"
    mc "Entonces... ¿contestas la pregunta?"
    play music "music/SaveMe.ogg"
    call BlinkXP ("c13s001_505" , "d") from _call_BlinkXP_80
    kat "Es fácil. Solo he tenido una cita con un chico. Yo tenía 15 años y Isaac, el chico más popular de mi curso, me invitó a ir a cenar."
    mc "Y algo salió mal."
    call BlinkXP ("c13s001_510" , "d") from _call_BlinkXP_81
    kat "Sí, que había una voz en off que no me dejaba explicarme. *Risa*"
    mc "Vale, ya me callo. *Risa*"
    call BlinkXP ("c13s001_515" , "d") from _call_BlinkXP_82
    kat "Imagínate, la ballena del instituto saliendo con el chico más popular de mi clase. Era un sueño hecho realidad."
    call BlinkXP ("c13s001_520" , "d") from _call_BlinkXP_83
    kat "Y como te puedes imaginar, yo me emperifollé toda, pedí a mis padres que me compraran un vestido nuevo, llegué al lugar de la cita y allí estaba él, guapísimo."
    call BlinkXP ("c13s001_525" , "d") from _call_BlinkXP_84
    kat "Rodeado de todos sus amigos y amigas... riéndose de mí. Algo sacado de una película mala de instituto donde todos los populares son gilipollas y se ríen de la perdedora."
    mc "Lo siento, Kate."
    call BlinkXP ("c13s001_530" , "d") from _call_BlinkXP_85
    kat "Besó a una de las animadoras, tan solo para demostrar que podía besar a quien quisiera y que no lo iba a hacer conmigo."
    mc "Ese crío era un capullo. Los hay en todos los institutos."
    call BlinkXP ("c13s001_535" , "d") from _call_BlinkXP_86
    kat "Pero como en todas las películas malas, la perdedora acabó ganando. Dos meses después estaba saliendo con esa misma animadora. Jennifer. Fue mi primera novia."
    kat "Ella me enseñó que no necesitaba a un chico para ser feliz, para sentirme querida y especial."
    mc "¿Cómo se lo tomó aquel chico?"
    call BlinkXP ("c13s001_540" , "d") from _call_BlinkXP_87
    kat "No le dió importancia hasta que Jennifer colgó una foto en InstaPic de nosotras dos besándonos."
    kat "El texto decía \"Me ha costado dos meses quitarme el mal sabor de boca de un beso horrible de Isaac. Besa tan mal que me ha vuelto lesbiana.\" Como te puedes imaginar, ella siempre lo había sido."
    mc "¡Bien por Jennifer!"
    call BlinkXP ("c13s001_545" , "d") from _call_BlinkXP_88
    kat "Y esa es la historia de por qué solo salgo con chicas. Sigo apreciando el aspecto de un chico guapo, pero no voy a dejar que me hagan daño otra vez."
    kat "Pero que un chico como tú se planteara tirarme los trastos... me sorprende."
    mc "¿Un chico como yo? Kate, ¿me estás tirando los trastos? *Risa*"
    call BlinkXP ("c13s001_555" , "d") from _call_BlinkXP_89
    kat "*Risa* No solo es guapo y sabe encajar las bromas, también sabe devolverlas."
    mc "¿Dónde estaría lo divertido si sólo recibiera uno?"
    stop music fadeout (1.5)
    "Justo en ese momento escuchas pasos en la escalera."
    call BlinkXP ("c13s001_560" , "d") from _call_BlinkXP_90
    mom "¿Qué hacéis aquí tan temprano? ¿Le has pillado el gusto a dormir en el sofá, [mc]? *Risa* ¿Hoy has cambiado a Lisa por Kate?"
    mc "¿Cómo sabes tú eso?"
    call BlinkXP ("c13s001_565" , "d") from _call_BlinkXP_91
    kat "Ayer Lisa lo comentó varias veces. Por lo visto hablar contigo le ayudó mucho... en algo."
    mc "Ah, vale."
    call BlinkXP ("c13s001_570" , "d") from _call_BlinkXP_92
    kat "Pero no te preocupes, [mar]. Esta vez lo he encontrado yo durmiendo en el sofá."
    call BlinkXP ("c13s001_575" , "d") from _call_BlinkXP_93
    mom "¿Ha pasado algo en tu habitación?"
    mc "Algo. Tenemos que hablar."
    call BlinkXP ("c13s001_580" , "d") from _call_BlinkXP_94
    kat "Yo voy a darme una ducha. Os dejo hablar tranquilos."
    mc "Nosotros vamos a bajar a la sala de abajo, es el sitio más alejado de cualquier habitación."
    return
label c13s002_TalkToTheFamily:
    if _in_replay:
        $ mc._var("relationships", 0, intention = "set")
        menu:
            "¿Estás en una relación con [mar!t]?"
            "Sí":
                $ mar._var("route" , True)
                $ AuxReplay = True
                $ mc._var("relationships", 1)
            "No":
                $ mar._var("route" , False)
                $ AuxReplay = False
        menu:
            "¿Estás en una relación con [nor]?"
            "Sí":
                $ nor._var("route" , True)
                if AuxReplay:
                    $ AuxReplay = True
                else:
                    $ AuxReplay = False
                $ mc._var("relationships", 1)
            "No":
                $ nor._var("route" , False)
        if not AuxReplay:
            menu:
                "¿Tienes más de una relación?"
                "Sí":
                    $ mc._var("relationships", 2, intention = "set")
                "No":
                    $ mc._var("relationships", 0, intention = "set")
    call BlinkXP ("c13s002_005" , "f") from _call_BlinkXP_95
    mom "¿Qué ha pasado?"
    play music "music/IWonderWhatIllDoToday.ogg"
    if mar._var("route"):
        mc "Ahora te lo explico, pero antes quiero un beso."
        call KissXP ("c13s002_010" , "d") from _call_KissXP_3
        mom "Mmmmm... subía a ver si estabas despierto para besarte antes de que todo el mundo se despertara. Verte con Kate ha hecho que me despiste."
        mc "Problema resuelto. *Risa* Sobre lo que ha pasado..."
    mc "[eil] y su madre están durmiendo en mi habitación"
    call BlinkXP ("c13s002_015" , "h") from _call_BlinkXP_96
    mom "{b}¿Qué?{/b} ¿Por qué?"
    if mar._var("route"):
        mom "Tu y ellas..."
        mc "No, no es eso, no te preocupes."
    mc "Solomon se puso violento ayer con Kiara."
    call BlinkXP ("c13s002_020" , "h") from _call_BlinkXP_97
    mom "{b}¿Qué?{/b} ¿Kiara está bien?"
    mc "Tiene un hematoma gigante en el antebrazo. Por el resto parece estar bien... físicamente."
    mc "Cuando se despierte quiero llevarla al hospital a que vea a [sam]."
    call BlinkXP ("c13s002_025" , "d") from _call_BlinkXP_98
    mom "Sí, es lo mejor. Así tendrá un informe para presentar a la policía."
    mc "No quiere presentar denuncia. Ni siquiera quiere ir al hospital."
    mc "Quería volver a casa mañana... la he convencido para que pase unos días en casa. Todavía hay una habitación libre en casa de [nor]. No sé si me he tomado muchas libertades..."
    call BlinkXP ("c13s002_030" , "d") from _call_BlinkXP_99
    mom "No, para nada. Si alguien tiene problemas, debemos que ayudarlo. Tenemos una habitación libre hasta que lleguen las otras estudiantes, no creo que haya mejor forma de usarla."
    mc "De todas formas creo que debería haberlo consultado con [nor], pero era pasada la medianoche cuando hemos llegado a casa."
    call BlinkXP ("c13s002_035" , "d") from _call_BlinkXP_100
    mom "Llámala y dile que venga. Ya debe estar despierta. Yo no he bajado el móvil."
    mc "OK, dáme un segundo."
    scene black with dissolve
    "Unos minutos después, una vez habéis puesto a [nor] al corriente..."
    call BlinkXP ("c13s002_040" , "d") from _call_BlinkXP_101
    mc "Espero no haberme extralimitado diciéndoles que se pueden quedar una semana en tu casa."
    nor "¿Una semana? ¡Se pueden quedar todo el tiempo que quieran! Mientras no lleguen las estudiantes en otoño, esa habitación es suya si la quieren."
    mc "Gracias, [nor]. Entre Meemaw, Tía Betty, y ahora Kiara y [eil], casi es como si tuvieras a las estudiantes."
    call BlinkXP ("c13s002_045" , "d") from _call_BlinkXP_102
    nor "Me servirá de entrenamiento. *Risa* [sca] se queda a dormir la mitad de los días. Cuando coincidan todas tendré cinco huespedes."
    call BlinkXP ("c13s002_050" , "d") from _call_BlinkXP_103
    mom "A mí me llega hoy la quinta. Por cierto, [mc], tienes que ir a buscarla al aeropuerto. Llega a las 2 PM."
    mc "Sí, lo sé. Me lo dijo [nor] ayer. Parece que iba a ser una sorpresa para mí..."
    call BlinkXP ("c13s002_055" , "d") from _call_BlinkXP_104
    mom "¿Sorpresa? ¿Qué sorpresa?"
    mc "¿Te acuerdas de la chica India con la que salía en Portland? Estoy 99\% seguro de que es ella."
    if mar._var("route") and nor._var("route"):
        scene c13s002_060a with dissolve
    elif not mar._var("route") and not nor._var("route"):
        if not eri._var("route"):
            scene c13s002_060b with dissolve
        else:
            scene c13s002_060d with dissolve
    elif mar._var("route") and not nor._var("route"):
        if not eri._var("route"):
            scene c13s002_060c with dissolve
        else:
            scene c13s002_060a with dissolve
    else:
        scene c13s002_060d with dissolve
    mom "¿Te ha seguido desde Portland? ¿Sin decírtelo?"
    nor "Super romántico, ¿verdad? Estoy segura de que quiere volver con él."
    mc "No estoy seguro, pero si no fuera así ¿por qué el secretismo? ¿Por qué se ha transferido a Newport?"
    call BlinkXP ("c13s002_065" , "d") from _call_BlinkXP_105
    mom "¿Tú quieres volver con ella?"
    if mc._var("relationships") > 0:
        mc "Mi situación es diferente de cuando estaba en Portland. Tengo que hablar con ella."
    else:
        mc "Hay muchas cosas que hacer en casa y no tengo demasiado tiempo para empezar o reanudar una relación. Tengo que hablar con ella."
    mc "Pero volviendo al tema del día. Deberiais hablar con [eil] y Kiara. Les dije que os comentaría lo de la habitación y..."
    call BlinkXP ("c13s002_070" , "d") from _call_BlinkXP_106
    nor "No hay nada que comentar. La habitación es suya por el tiempo que quieran."
    mc "Pero eso se les debería decir a ellas, no a mí. Yo ya sabía que no las íbamos a dejar en la estacada."
    call BlinkXP ("c13s002_075" , "d") from _call_BlinkXP_107
    nor "¿Están despiertas?"
    mc "No lo sé, se acostaron tarde... Yo debería entrar para coger ropa y vestirme."
    nor "Probemos entonces..."
    scene c13s002_080a with fade
    play sound "music/knock.ogg"
    "*Knock-Knock*"
    mc "Soy yo."
    kia "Entra, [mc]."
    call BlinkXP ("c13s002_085" , "d") from _call_BlinkXP_108
    mc "Buenos días, Kiara. ¿Habéis dormido bien?"
    kia "Sí, hemos dormido genial. Hacía tiempo que Eile y yo no compartíamos cama. Gracias por dejarnos tu habitación."
    scene c13s002_080b with dissolve
    mc "No se si recuerdas a mi madre y a mi tía."
    mom "Bienvenida a casa, Kiara. ¿Donde está [eil]? Hace siglos que no la veo. Siento mucho lo que te ha pasado. Lo que os ha pasado a las dos."
    nor "Hoy moveremos vuestras cosas a una habitación en mi casa, así [mc] puede recuperar la suya. Estaréis más cómodas allí, hay dos camas. Sentimos no poderos ofrecer más."
    call BlinkXP ("c13s002_090" , "d") from _call_BlinkXP_109
    kia "Gracias por acogernos, [mar] y [nor]. O lo que queda de ti, [nor]. Creo que si te viera por la calle no te reconocería. Nos conformamos con poco, solo serán unos días. No queremos molestar."
    kia "[eil] está en la ducha. Hoy empieza pronto en el trabajo y no cogió su bici. Tendrá que coger el autobús."
    mc "No te preocupes por eso. El café está de camino al hospital y la puedo llevar yo."
    call BlinkXP ("c13s002_095" , "d") from _call_BlinkXP_110
    kia "[mc], ya hablamos de eso anoche. No es necesario ir al hospital."
    mc "No es necesario, pero sí recomendable. ¿Tienes algo mejor que hacer esta mañana? ¿A qué hora entras a trabajar?"
    call BlinkXP ("c13s002_100" , "d") from _call_BlinkXP_111
    kia "A la 1 PM. Voy a tener que mover nuestras cosas a la nueva habitación..."
    mc "Las cosas son una bolsa de viaje tan solo, Kiara. La puedo llevar yo en cuanto [eil] salga de la ducha."
    mc "A las 10 AM tengo que estar en un sitio, a las 2 PM tengo que estar en el aeropuerto, tu trabajo me pilla de camino entre el hospital y el aeropuerto."
    mc "Dejamos a [eil] en el café, vamos al hospital, me acompañas a lo que tengo que hacer a las 10, y te llevo al trabajo. Si tenemos tiempo, te invito a comer."
    call BlinkXP ("c13s002_105" , "d") from _call_BlinkXP_112
    mom "[mc] me ha dicho lo que ha pasado. [sam] Washington es una amiga, no va a hacer nada que tu no quieras hacer."
    mom "Si no quieres presentar la denuncia, no te va a obligar."
    call BlinkXP ("c13s002_110" , "d") from _call_BlinkXP_113
    kia "¿[sam] Washington? ¿La madre del chico en... del chico que estudiaba en el mismo curso que [eil] y [mc]?"
    mc "Sí, la madre de Jamaal."
    kia "Sí, eso, Jamaal. No he hablado más que un par de veces con ella..."
    call BlinkXP ("c13s002_115" , "d") from _call_BlinkXP_114
    nor "Pero es amiga de la familia. Y tú también. Si [mc] le pide algo..."
    mc "Entonces decidido, voy a ducharme y nos vamos cuando queráis."
    call BlinkXP ("c13s002_120" , "d") from _call_BlinkXP_115
    eil "¿[nor]? ¡Estás fantástica!"
    eil "Tu también, [mar]."
    scene c13s002_125a with dissolve
    mom "Bienvenida a casa, [eil]. Sabía que tarde o temprano te mudarías aquí, pero esperaba que fuera en otras circunstancias."
    eil "Gracias, [mar]. Yo también lo esperaba."
    scene c13s002_125b with dissolve
    eil "Me parece increíble que haya pasado tanto tiempo sin veros. Tienes que entrar en el café cuando traigas a [eri] y lucir ese tipito."
    eil "¡Estás increíble! Me tienes que decir como has perdido tanto peso. No me iría mal a mí también."
    nor "Gracias, [eil], pero tú no lo necesitas, a menos que quieras disfrazarte de esqueleto en Halloween. *Risa*"
    call BlinkXP ("c13s002_130" , "d") from _call_BlinkXP_116
    mom "Entonces, ¿vamos a desayunar mientras [mc] se ducha? Parece que va a tener un día ocupado"
    mc "A mí también me gustaría desayunar..."
    call BlinkXP ("c13s002_135" , "d") from _call_BlinkXP_117
    nor "No te preocupes, te dejaremos algo para que desayunes. Ve a ducharte, ya llevaré yo la bolsa de Kiara y [eil] a casa."
    call BlinkXP ("c13s002_140" , "d") from _call_BlinkXP_118
    nor "Si necesitáis algo de ropa, no dudéis en pedírnoslo a nosotras o a cualquiera de las chicas."
    call BlinkXP ("c13s002_145" , "d") from _call_BlinkXP_119
    kia "No te preocupes, podemos aguantar dos o tres días con lo que hemos traído. El jueves mi hija quiere ir a casa a coger más ropa."
    mc "El jueves por la noche no estará Solomon. Y esperamos poder llevar a Alexia... a la Agente Martínez por si se tuercen los planes."
    call BlinkXP ("c13s002_150" , "d") from _call_BlinkXP_120
    mom "Ve a ducharte o llegaréis tarde. Nosotras vamos a seguir charlando en la cocina mientras preparamos el desayuno."
    stop music fadeout (1.5)
    mc "OK, os veo en la cocina."
    return
label c13s002_TheHospital:
    if _in_replay:
        call mrS3_sam_route from _call_mrS3_sam_route_8
    scene black with dissolve
    "Después de desayunar, llevas a [eil] al café y vas al hospital. Aparcas en la zona de visitantes."
    call BlinkXP ("c13s002_200" , "d") from _call_BlinkXP_121
    play music "music/1000lichter.ogg"
    kia "[mc], de verdad que esto no es necesario. Tan solo es un hematoma."
    mc "No hace mucho que yo tuve unos hematomas y me dijeron que podían ser peligrosos si no se trataban correctamente."
    mc "No nos podemos arriesgar a que te pase nada, ¿verdad?"
    call BlinkXP ("c13s002_205" , "d") from _call_BlinkXP_122
    kia "Te conozco desde que tenías 15 años. Casi no reconozco a aquel chico tímido en este hombre que tengo ahora delante."
    mc "Kiara, sigo siendo yo. Tan solo he crecido y he adelgazado."
    call BlinkXP ("c13s002_210" , "d") from _call_BlinkXP_123
    kia "No me refiero a eso, [mc]. No quiero que te ofendas, pero al principio de salir con mi Eile me parecías un pusilánime." #pushover
    kia "No sé dónde tenías escondido a este hombre que toma las riendas de las situaciones."
    mc "Creo que me lo había comido. *Risa*"
    call BlinkXP ("c13s002_215" , "d") from _call_BlinkXP_124
    kia "*Risa* Eso no lo has perdido. Me sigues haciendo reír."
    mc "¿Te parecía tan malo como dices?"
    call BlinkXP ("c13s002_220" , "d") from _call_BlinkXP_125
    kia "Al principio sí. No me gustabas, pero la hacías feliz y por eso nunca me opuse a vuestra relación. Nunca le dije nada a ella."
    mc "Gracias. ¿Y después?"
    call BlinkXP ("c13s002_225" , "d") from _call_BlinkXP_126
    kia "Después evolucionasteis los dos. Ella dejó de querer ser el centro de atención. Maduró gracias a ti."
    kia "Tu dejaste de ser tan pusilánime, no encuentro una palabra mejor, pero sin perder tu esencia. Sacábais lo mejor del otro y hacíais que el otro enterrase lo peor de sí mismo."
    mc "No éramos una pareja para ser los reyes del baile, pero no nos iba mal. Nadie hubiera votado por mí como rey del baile entonces."
    call BlinkXP ("c13s002_230" , "d") from _call_BlinkXP_127
    kia "No necesitabais serlo. Solomon y yo lo fuimos, y ya ves..."
    mc "No te preocupes, Kiara. Si no quieres, no tienes que volver a verlo, y si quieres..."
    call BlinkXP ("c13s002_235" , "d") from _call_BlinkXP_128
    kia "¡No! No voy a denunciarlo. Si no fuera por todo lo que me habéis dicho, no estaría aquí ni siquiera."
    mc "No te iba a decir eso. Es tu decisión y, aunque no la comparta, tengo que respetarlo. Es tu familia."
    mc "Iba a decirte que si querías podías quedarte en casa todo el tiempo que necesitaras."
    mc "Hasta otoño tenéis disponible la habitación que ocuparéis. Y después podéis volver a dormir en mi cama."
    call BlinkXP ("c13s002_240" , "d") from _call_BlinkXP_129
    kia "*Risa* Cualquiera que te oyera pensaría que hoy hemos dormido en tu cama contigo dentro. *Risa*"
    mc "Bueno, en esa cama hemos dormido tres personas confortablemente. *Risa*"
    mc "La entrada está ahí mismo. ¿Preparada?"
    call BlinkXP ("c13s002_245" , "d") from _call_BlinkXP_130
    kia "Sí. ¿Me aseguras que esa enfermera es de confianza? ¿No va a dar parte a la policía?"
    mc "Kiara, [sam] es como una segunda madre para mí. No va a hacer nada que tu no quieras, pero me gustaría que comprobara como está ese brazo."
    mc "Y si hace un informe que puedas usar si cambias de opinión, mejor."
    stop music fadeout (1.5)
    kia "Vamos allá, entonces."
    call BlinkXP ("c13s002_250" , "f") from _call_BlinkXP_131
    play music "music/pianomatic.ogg"
    mc "Buenos días, [sam.nick]. Esta es Kiara, la madre de [eil], no sé si la recuerdas."
    sam "Hola, [mc]. Encantada de volver a verte, Kiara. Hacía años que no coincidíamos. Voy a ser tu enfermera hoy."
    call BlinkXP ("c13s002_255" , "d") from _call_BlinkXP_132
    kia "Hola, [sam]. No es nada grave, de verdad. [mc] está exagerando."
    mc "No exagero, tan solo soy precavido. Y ya has escuchado a [eil], [nor] y [mar]."
    call BlinkXP ("c13s002_260" , "d") from _call_BlinkXP_133
    sam "Un hematoma puede ser algo importante, más de lo que se piensa, no está de más echarle un ojo."
    sam "Acompáñame, Kiara. Tú quédate aquí, [mc]. No eres familia y no puedes pasar. Normas del hospital."
    mc "¿Para cuanto rato tenéis? Tengo que estar en otro sitio a las 10."
    call BlinkXP ("c13s002_265" , "d") from _call_BlinkXP_134
    sam "Déjame echarle una ojeada y salgo a decírtelo."
    mc "Perfecto. Os espero aquí."
    call BlinkXP ("c13s002_270" , "d") from _call_BlinkXP_135
    kia "Una vez más, gracias, [mc]."
    mc "Una vez más, no es necesario. Si me tengo que ir mientras estás con [sam], te escribo o te llamo."
    call BlinkXP ("c13s002_275" , "f") from _call_BlinkXP_136
    "Unos interminables minutos después..."
    sam "El brazo tiene mala pinta y quiero que la vea un doctor y que ordene una radiografía, pero ahora mismo están muy ocupados. Se va a quedar un rato. Calcula un par de horas."
    mc "Vale, entonces voy a ir hacer unas cosas y vuelvo luego a buscarla."
    call BlinkXP ("c13s002_280" , "d") from _call_BlinkXP_137
    sam "Perfecto. Le diré que la has abandonado en un hospital y que no volverás a buscarla. *Risa*"
    if sam._var("route"):
        mc "*Risa* Supongo que no me vas a dejar besarte aquí, ¿verdad?"
        call BlinkXP ("c13s002_285" , "d") from _call_BlinkXP_138
        sam "Supones bien. Aún no estoy preparada para que nadie del trabajo sepa lo nuestro."
    mc "Gracias, [sam.nick]. Trátala bien, por favor. Lo ha pasado mal"
    call BlinkXP ("c13s002_290" , "d") from _call_BlinkXP_139
    sam "Yo siempre trato bien a mis pacientes, [mc]. *Risa* Ya lo sabes."
    mc "Y por cierto, [sam.nick], perdón por el plantón de ayer."
    call BlinkXP ("c13s002_295" , "d") from _call_BlinkXP_140
    sam "No te preocupes. Jamaal lo agradeció, pero aún quedaron pastas si quieres venir esta tarde. Salgo a las 13:00, puedes venir a comer si quieres."
    mc "Imposible, tengo que recoger a la última estudiante en el aeropuerto. Pero intentaré pasar por la tarde."
    call BlinkXP ("c13s002_300" , "d") from _call_BlinkXP_141
    sam "Genial, te esperaré."
    stop music fadeout (1.5)
    mc "Hasta dentro de un rato, [sam.nick]."
    return
label c13s003_ScarlettHouse:
    if _in_replay:
        call mrS3_sca_route from _call_mrS3_sca_route_12
        call mrS3_rels from _call_mrS3_rels_33
    scene black with dissolve
    "Aparcas delante de casa de [sca] y le mandas un mensaje. Has pasado el video a una tablet para que sea más cómodo enseñárselo a su madre."
    "[sca] sale de su casa y entra en la camioneta."
    play music "music/m0450.ogg"
    call BlinkXP ("c13s003_005" , "d") from _call_BlinkXP_142
    if sca._var("route"):
        sca "Hola, cariño, me muero por besarte, pero no puedo aquí. Si mi madre nos ve..."
        mc "Lo entiendo. Te avergüenzas de mí."
        call BlinkXP ("c13s003_010" , "d") from _call_BlinkXP_143
        sca "Estoy castigada un día sin salir por quemar una olla haciendo{b}me{/b} espaguetis. Si mi madre se entera de que los hice para mi novio, estaré una semana."
        sca "Y si descubre que acabamos pidiendo pizza, seguramente me castigue un mes. ¿Has traído el video?"
    else:
        sca "Hola, [mc]. ¿Has traído el video ese?"
    mc "Sí, lo he pasado a una tablet para que le sea más cómodo leer los subtítulos que en el móvil."
    call BlinkXP ("c13s003_015" , "d") from _call_BlinkXP_144
    sca "¿Puedo verlo?"
    mc "Por supuesto. Aquí tienes la tablet."
    call BlinkXP ("c13s003_020" , "d") from _call_BlinkXP_145
    "[sca] permanece en silencio durante todo el video. Tan solo con la boca abierta en una expresión de sorpresa."
    call BlinkXP ("c13s003_025" , "d") from _call_BlinkXP_146
    sca "Hay que enseñárselo a mi madre. Con esto tendrá que creer que todas las veces que le he dicho que Kevin me acosaba era cierto."
    mc "Sí, no hay forma de negarlo. Está claro cuales son sus intenciones."
    sca "Vamos dentro a enseñárselo..."
    call BlinkXP ("c13s003_030" , "d") from _call_BlinkXP_147
    sca "¡Mierda! Hay un problema."
    mc "¿Qué pasa?"
    sca "¿De dónde le decimos que lo hemos sacado?"
    mc "No había pensado en eso... ¿Siempre te ha acosado en tu habitación?"
    call BlinkXP ("c13s003_035" , "d") from _call_BlinkXP_148
    sca "No, en cualquier sitio de casa, pero la mayoría de veces ha sido en mi habitación."
    mc "Puedes decir que me pediste que instalara esa cámara ya que ella no te creía. Así también tienes una razón para que lo haya traído yo en vez de enseñárselo tú ayer."
    call BlinkXP ("c13s003_040" , "d") from _call_BlinkXP_149
    sca "Puede ser una buena idea. Eso le da más plausibilidad. Vamos"
    call BlinkXP ("c13s003_045" , "f") from _call_BlinkXP_150
    "Al bajar de la camioneta [sca] saca el móvil mientras os dirigís a la puerta. Te mira con nerviosismo."
    sca "Truco de sordos. Le mando un mensaje a mi madre por la aplicación del timbre, diciéndole que voy a entrar."
    sca "No puede oír ni el timbre ni la puerta, así está sobreaviso de que hay alguien más en casa."
    if sca._var("route"):
        mc "Compraremos una cosa así si algún día es necesaria."
        call BlinkXP ("c13s003_050" , "d") from _call_BlinkXP_151
        sca "No puedes saber lo que llego a quererte por cosas como estas."
    scene c13s003_055 with fade
    "Entraís en casa y [sca] hace las presentaciones. Te presenta como un amigo."
    "Te imaginabas que iba a ser una conversación a través de lengua de signos, pero la Señora Russell habla perfectamente, con ese deje especial que tienen las personas que no pueden escucharse."
    "[sca] explica la excusa que habéis inventado para tener el video, sin contarle el contenido."
    "A la Señora Russell no le gusta mucho la idea."
    stop music fadeout (1.5)
    call BlinkXP ("c13s003_065" , "d") from _call_BlinkXP_152
    mj "¿Has puesto cámaras en mi casa? ¿Por qué no me has pedido autorización?"
    play music "music/OneLastChance.ogg"
    call BlinkXP ("c13s003_070" , "d") from _call_BlinkXP_153
    sca "Mamá, no estabas. No te podía mandar un mensaje por si lo leía Kevin. Tomé la decisión, es mi habitación al fin y al cabo."
    call BlinkXP ("c13s003_075" , "d") from _call_BlinkXP_154
    mj "Pero está en mi casa. Tendrías que habérmelo dicho."
    call BlinkXP ("c13s003_080" , "d") from _call_BlinkXP_155
    sca "Si te lo hubiera dicho me las hubieras hecho quitar y seguiríamos estando igual."
    mc "Cuanta menos gente sepa estas cosas, suele ser mejor, Señora Russell."
    call BlinkXP ("c13s003_085" , "d") from _call_BlinkXP_156
    mj "¿Qué has dicho?"
    call BlinkXP ("c13s003_090" , "d") from _call_BlinkXP_157
    sca "Mírala de frente cuando hables con ella, [mc]. De esa forma puede leerte los labios."
    call BlinkXP ("c13s003_095" , "d") from _call_BlinkXP_158
    mc "Perdón, Señora Russell, decía que cuanta menos gente sepa estas cosas, suele ser mejor."
    mc "Además, si nadie hace nada inapropiado en la habitación de [sca], no pasa nada, ¿no?"
    mj "Si tú tienes acceso a ese video, podrías ver a mi hija desnuda."
    call BlinkXP ("c13s003_100" , "d") from _call_BlinkXP_159
    sca "Mamá, hay ángulos muertos, yo sé dónde están y la cama no es visible en el video. Nadie va a verme desnuda."
    sca "Compruébalo tu misma mirando el video."
    scene c13s003_105 with dissolve
    "El video comienza con [sca] en su habitación."
    scene c13s003_110 with dissolve
    kev "Hola [sca], ¿Me has echado de menos?"
    scav "¡Kevin! Te he dicho mil veces que no entres en mi habitación sin llamar. ¡Podría estar cambiándome!"
    mj "¿Entró sin llamar?"
    sca "Sí, Mamá, lo hace siempre. Ya le he dicho mil veces que no lo haga."
    scene c13s003_115 with dissolve
    kev "¿No he llamado? ¿Estás segura? Yo diría que sí. Deberías revisar si llevas bien ajustado tu audífono. *Risa*"
    mj "A lo mejor estabas despistada, cariño, y no lo oíste."
    scav "Idiota, era mi oído bueno el que estaba encarado a la puerta."
    scene c13s003_120 with dissolve
    kev "Ya sabes que puedes perder el mundo de vista, cuando te pones a pensar en tus cosas y en ese chico que nunca te hará caso. *Risa cruel*"
    if sca._var("route"):
        scav "Pues que sepas que estamos saliendo. Imbécil."
    else:
        scav "No es asunto tuyo si me hace caso o no. Imbécil."
    mj "Creo que te has pasado insultándole. Lo que ha dicho es verdad, cuando te pones a pensar en ese chico..."
    sca "¡Mamá!"
    kev "Pero aún no me has contestado ¿Me has echado de menos?"
    scene c13s003_125 with dissolve
    scav "Si crees que voy a echar de menos a alguien que entra en mi habitación sin autorización y sin llamar, estás muy equivocado."
    kev "Ya te he dicho que he llamado. A ver si voy a tener que poner cámaras para grabar nuestras conversaciones y cada vez que entro en tu habitación. *Risa*"
    mj "Alguien las puso..."
    scene c13s003_130 with dissolve
    scav "¿Para qué? ¿Para pajearte mientras me cambio?"
    mj "¡[sca]!"
    sca "Espera y lee lo que dice ahora..."
    kev "Mira, niña, sería una buena paja. Y después pensaría en ello mientras tu madre me chupa la polla."
    scene c13s003_135 with dissolve
    mj "Es imposible que haya dicho eso... No habéis manipulado los subtítulos, ¿verdad?"
    mc "No, Señora Russell. Lo que usted lee y lo que oímos nosotros es lo mismo."
    sca "Espera, que ahora viene lo peor..."
    scene c13s003_140 with dissolve
    kev "Y mañana tu madre tiene turno de noche y la he convencido para que te castigue por lo de la olla. No vas a poder fugarte a casa de tu amiguita."
    kev "Eres una inútil que no sirve ni para cocinar unos putos espaguetis."
    kev "Por primera vez en meses vamos a estar solos en casa. A lo mejor puedo darte unas lecciones de como chupar una polla, por si ese chico algún día se decide..."
    scene c13s003_145pv
    show c13s003_145v
    pause (1.77)
    scene c13s003_145dv
    scav "Ni se te ocurra acercarte, cabrón."
    mj "¡[sca]!"
    scene c13s003_150 with dissolve
    kev "Mejor que guardes esa furia para mañana. Me gustará más así."
    scene c13s003_155 with dissolve
    play sound "music/DoorSlam.ogg"
    "*Portazo*"
    call BlinkXP ("c13s003_160" , "d") from _call_BlinkXP_160
    mj "Esto no puede ser real. Sé que lo que decía [sca] coincidía con los subtítulos, puedo leerle los labios en la mayoría del video, pero no me puedo creer que Kevin dijera eso."
    mc "Señora Rusell, es lo que hay en el video, se lo aseguro."
    stop music fadeout (1.5)
    call BlinkXP ("c13s003_165" , "d") from _call_BlinkXP_161
    sca "Mamá, [mc] dice la verdad. Kevin me dijo esas cosas."
    call BlinkXP ("c13s003_170" , "d") from _call_BlinkXP_162
    mj "¿Por qué no me lo dijiste ayer?"
    call BlinkXP ("c13s003_175" , "d") from _call_BlinkXP_163
    play music "music/Groove Grove.ogg"
    sca "Te intenté decir hace unas semanas que se estaba propasando y no me creíste. Esperaba que [mc] viniera con pruebas para poder enseñártelas."
    scene c13s003_180An with dissolve
    "En ese momento la Señora Russell deja de hablar con su voz y pasa a hacerlo con sus manos. Queda claro que quiere que sea una discusión entre madre e hija."
    "[sca] no traduce."
    if mc._var("relationships") > 1:
        "El gesto en la cara de su madre muestra su enfado, tú también lo estarías si una de tus chicas acosara a tu hijo, si alguna vez lo tienes."
    else:
        "El gesto en la cara de su madre muestra su enfado, tú también lo estarías si tu pareja acosara a tu hijo, si alguna vez lo tienes."
    if sca._var("route"):
        "Solo conoces una frase en lenguaje de signos. Esa frase aparece varias veces. Siempre en manos de [sca], nunca de su madre."
    "La conversación acaba abruptamente. Las dos están claramente enfadadas. Supones que con Kevin, pero mejor no preguntar."
    call BlinkXP ("c13s003_185" , "d") from _call_BlinkXP_164
    sca "Ya está. Dice que Kevin va a tardar poco en volver a casa y le preguntará sobre el video."
    mc "¿Le va a dar la oportunidad de negarlo?"
    sca "Sí. Vamos a sentarnos a esperarlo."
    scene c13s003_190 with dissolve
    stop music fadeout (1.5)
    "Está claro que durante la conversación las cosas se han caldeado entre madre e hija y ha acabado en enfado. Está claro que ninguna de las dos va a decir una palabra más."
    "Va a ser un silencio muy incómodo hasta que vuelva Kevin."
    scene c13s003_195AnBlink with dissolve
    "Por suerte, al cabo de unos minutos el móvil de la Señora Russell vibra."
    "Lo mira y su cara se ilumina con una sonrisa."
    "No es buena señal."
    play music "music/I-Can-Feel-it-Coming.ogg"
    call BlinkXP ("c13s003_200" , "d") from _call_BlinkXP_165
    kev "Hola, mi amor. Veo que tenemos visita."
    call BlinkXP ("c13s003_205" , "d") from _call_BlinkXP_166
    kev "Hola, soy Kevin Cameron. La pareja de esta preciosidad. Y prácticamente el padrastro de la otra belleza."
    "No te levantas. No piensas estrechar su mano."
    "Lo que te apetecería hacer sería meter esos dientes perfectos en su estómago de un puñetazo y dejar su cara hecha pulpa por tus puños."
    "Te cuesta retenerte de empezar a hacer zumo con sus ojos. Calma."
    mc "[mc]."
    call BlinkXP ("c13s003_210" , "d") from _call_BlinkXP_167
    kev "¿Ha pasado algo, cariño?"
    call BlinkXP ("c13s003_215" , "d") from _call_BlinkXP_168
    mj "Mira este video, mi amor, por favor. Dime que no es cierto."
    call BlinkXP ("c13s003_220" , "d") from _call_BlinkXP_169
    kev "¿De qué va esto, mi vida?"
    mj "Míralo, por favor."
    "Kevin empieza a mirar el video con una cara de perplejidad."
    call BlinkXP ("c13s003_225" , "d") from _call_BlinkXP_170
    "Su expresión cambia a sorpresa absoluta tal como pasan los segundos."
    call BlinkXP ("c13s003_230" , "d") from _call_BlinkXP_171
    "Casi al final del video la sonrisa vuelve a su cara."
    "No es buena señal."
    call BlinkXP ("c13s003_235" , "d") from _call_BlinkXP_172
    kev "*Risa* Está muy bien hecho, pero como broma es un poco pesada."
    mcp "{i}(¿Que?){/i}"
    kev "Además, este tipo tiene acento de Alabama, y ya sabes que yo soy de Tejas, cariño. No es mi voz."
    "Tu perplejidad no hace más que aumentar. Es cláramente su voz y su acento. Tus ganas de machacarle la cara aumentan. Una bestia empieza a despertarse en tu interior. Calma."
    kev "*Risa* Lo que estos chicos son capaces de hacer con inteligencia artificial..."
    scene c13s003_240 with dissolve
    mj "¿Entonces no es cierto? ¿Me lo juras?"
    kev "Por supuesto que te lo juro."
    call BlinkXP ("c13s003_245" , "h") from _call_BlinkXP_173
    mj "¡Lo sabía! No serías capaz de decir esas cosas."
    kev "Por supuesto que no, cielo. Ya sabes que yo solo tengo ojos para ti."
    scene c13s003_250 with dissolve
    mj "Señor Marks, no sé lo que esperaba conseguir con esta broma, pero no ha tenido ninguna gracia. Por favor, márchese de mi casa."
    mc "Pero Señora Russell, le está mintiendo."
    mj "Cállese y váyase, por favor."
    scene c13s003_255 with dissolve
    mj "Tú y yo vamos a tener una larga conversación, niña."
    mc "*Susurrando* ¿Qué hago?"
    call BlinkXP ("c13s003_260" , "d") from _call_BlinkXP_174
    sca "Vete, [mc]. Ya lo intentaré arreglar... como sea."
    call BlinkXP ("c13s003_265" , "d") from _call_BlinkXP_175
    kev "Ya te acompaño yo a la puerta, muchacho."
    "La palabra \"muchacho\" va cargada de ironía. Te está diciendo que eres un niño que se ha metido en un juego de adultos al que no pertenece."
    "Te cuesta mucho no dejar salir la bestia que está creciendo dentro de ti. Calma."
    scene c13s003_270 with dissolve
    "Desde la puerta puedes ver cómo madre e hija discuten. Lo surrealista de la situación hace que casi sea gracioso ver a dos personas gritándose en silencio."
    kev "Mira, hijo, creía que solo iba a tener una noche a solas con esa putilla. Es demasiado perfecta para que la castiguen a menudo."
    kev "Ahora, gracias a ti, me parece que voy a tener muchas noches a solas con ella. La próxima vez que la veas será toda una mujer."
    "Lisa estaría orgullosa de ti. Una bestia a la que has estado a punto de llevar a la extinción aparece con toda la furia de un animal aprisionado."
    play sound "music/punch.ogg"
    scene c13s003_275An with dissolve
    "Tu puño sale disparado hacia la boca de Kevin. No es un rodillo, pero hace el mismo efecto. No saltan dientes."
    scene c13s003_280An with dissolve
    "[sca] y la Señora Rusell paran la discusión y os miran mientras Kevin cae al suelo."
    mc "[sca], haz las maletas si quieres puedes venir a casa. No voy a dejarte con este cerdo."
    call BlinkXP ("c13s003_285" , "d") from _call_BlinkXP_176
    kev "¡Te voy a denunciar, hijo de puta! ¡Sé tu nombre!"
    scene c13s003_290 with vpunch
    mj "¡Haz tus maletas y vete de mi casa, [sca]!"
    mj "¡No te quiero volver a ver en esta casa!"
    sca "¿Qué?"
    "Nada está saliendo como habías planeado..."
    scene c13s003_295 with hpunch
    mj "¡Lo que has oído! ¡Primero me destrozas la vida!"
    mj "¡Después tu padre deja de mandarme dinero!"
    mj "¡Ahora traes a tu amigo para que apalice a Kevin, con lo bueno que ha sido con nosotras! ¡Fuera de aquí!"
    sca "¿Qué estás diciendo? ¿Has estado recibiendo dinero de mi padre todos estos años?"
    "El tiempo parece haberse detenido para Kevin y para ti. Seguir la pelea hubiera sido lógico. Observar a las dos mujeres gritarse es más interesante."
    scene c13s003_300 with vpunch
    mj "¡Sí! ¡Y me alegra habértelo ocultado! No te mereces nada."
    sca "¡Pues lo buscaré e iré con él! Seguro que estaré mejor con él que contigo. Siempre pensando solo en el dinero y creyendo antes a Kevin que a tu hija."
    scene c13s003_305 with vpunch
    mj "Suerte con eso. Me escribió hace unos días. Como ya tienes 18, no va a mandar más dinero."
    mj "Eso es lo que te quiere y se preocupa por ti, mientras yo he sacrificado mi vida por tenerte."
    play sound "music/doorbell1.ogg"
    "*Ding-Dong*"
    scene c13s003_310 with dissolve
    "El móvil de la Señora Russell vuelve a vibrar. El timbre os paraliza a todos durante unos segundos."
    play sound "music/doorbell1.ogg"
    "*Ding-Dong*"
    play sound "music/doorbell1.ogg"
    "*Ding-Dong*"
    scene c13s003_315 with dissolve
    "La Señora Russell va a abrir la puerta. Esquiva el cuerpo de Kevin en el suelo. Si no fuera por eso, parecería que no ha pasado nada para ella. "
    "La persona más inesperada está fuera."
    call BlinkXP ("c13s003_320" , "h") from _call_BlinkXP_177
    ama "FBI. Apártese, Señora Russell."
    ama "¡[mc] Marks, queda detenido por infracciones contra la Ley de Pivacidad en el Hogar!"
    mcp "{i}(No puede ser. Es igualita que [emm]... si no fuera por el pelo... y por que se la ve mucho más adulta que a [emm]...){/i}"
    mc "Ama..."
    ama "¡Silencio! De rodillas. ¡Las manos detras de la espalda!"
    "Sigues sus instrucciones. No sabes de qué va esto."
    call BlinkXP ("c13s003_325" , "d") from _call_BlinkXP_178
    "Mientras Amanda te esposa..."
    ama "*Susurrando* No te preocupes..."
    kev "También me ha agredido..."
    call BlinkXP ("c13s003_330" , "d") from _call_BlinkXP_179
    ama "Eso se sumará a la lista de cargos. Acompáñeme junto con la Señora Russell, por favor. Tengo que tomarles declaración."
    call BlinkXP ("c13s003_335" , "f") from _call_BlinkXP_180
    "Amanda desaparece con la Señora Russell y Kevin. Ambos están en shock."
    sca "¿Esa era... [emm]?"
    mc "No, pero ahora no te lo puedo explicar. Ayúdame con las esposas."
    call BlinkXP ("c13s003_340" , "d") from _call_BlinkXP_181
    sca "No tengo ni idea de como abrirlas... "
    mc "No te preocupes, Ama... la falsa [emm] va a volver ahora... está de nuestra... de mi parte. Ayúdame a levantarme."
    call BlinkXP ("c13s003_345" , "f") from _call_BlinkXP_182
    ama "[sca], ve a hacer las maletas. Tienes un par de horas. No creo que pueda entretenerlos mucho más antes de que empiecen a sospechar."
    "Su voz transpira autoridad. Pero [sca] ya no es la niña tímida de hace dos semanas. Algo ha cambiado en ella."
    call BlinkXP ("c13s003_350" , "d") from _call_BlinkXP_183
    sca "¿Por qué? ¿Y quién eres? Tienes la cara de [emm], pero ahí acaba el parecido."
    mc "[sca], ya te he dicho que no te lo podía explicar ahora..."
    call BlinkXP ("c13s003_355" , "d") from _call_BlinkXP_184
    if sca._var("route"):
        ama "Será mejor que hagas caso a tu novio, [sca]."
    else:
        ama "Será mejor que hagas caso a [mc], [sca]."
    ama "Si dejo a tu madre y a Kevin mucho rato solos saldrán del estado de shock y empezarán a notar que hay cosas que no cuadran."
    call BlinkXP ("c13s003_360" , "d") from _call_BlinkXP_185
    sca "Tienes razón. Los agentes del FBI siempre van por parejas en las películas, y has dejado a un sospechoso sin vigilancia. Mi madre no es tonta y lo notará."
    sca "Voy a hacer las maletas y ahora vuelvo."
    call BlinkXP ("c13s003_365" , "f") from _call_BlinkXP_186
    "Un minuto después, una vez retiradas las esposas..."
    ama "¡Joder! Cuando te mandamos el video creíamos que ibas a usar a Jamaal para hacerlo viral en MeTube o llevárselo a Alexia. No esto."
    ama "He venido en cuanto he deducido que tu plan no iba a funcionar."
    mc "Creía que esto podía solucionarlo todo... Al menos hoy te ha dado tiempo de quitarte el mono de mecánico..."
    mc "¿Desde cuándo tenéis cámaras en casa de [sca]? ¿Hay otros videos donde se vea la cara de Kevin y la Señora Russell pueda leer sus labios?"
    call BlinkXP ("c13s003_370" , "d") from _call_BlinkXP_187
    ama "No, lo siento. Las pusimos el domingo, cuando [sca] fue a comprar al supermercado..."
    if sca._var("route"):
        mc "Entonces tenéis grabado..."
        ama "Sí, pero destruímos todo lo que no es importante para la misión..."
    else:
        mc "Lástima... pero ¿por qué vigilar la casa de [sca]?"
        ama "Podía ser importante para la misión... y destruimos lo que no es importante."
    ama "{i}(O lo copiamos a discos privados.){/i}"
    mc "Y no me vas a decir cual es esa misión, ¿verdad? ¿Tiene algo que ver con la cláusula NG?"
    call BlinkXP ("c13s003_375" , "v") from _call_BlinkXP_188
    ama "{b}¿Qué?{/b} ¿Dónde has oído eso? "
    mc "Vosotras tenéis vuestros secretos y yo los míos. Cuando quieras intercambiamos información."
    mc "{i}(OK. No tienen acceso a mi ordenador o no son capaces de romper el cifrado de Jamaal.){/i}"
    call BlinkXP ("c13s003_380" , "d") from _call_BlinkXP_189
    ama "Me parece justo. Mañana o pasado nos pondremos en contacto con vosotros para hablar."
    ama "Voy a llevarme a la Señora Russell y a Kevin o van a empezar a sospechar. Les voy a decir que estás detenido, con lo que mejor que no pases por este barrio en unos días."
    mc "Sólo una pregunta más. ¿Por qué me habéis enviado el video? [sca] no tiene nada que ver con NTR o con GILF."
    call BlinkXP ("c13s003_385" , "d") from _call_BlinkXP_190
    ama "Porque pensamos que podía ser importante. Especialmente para ti... y para [dap]... aunque no tenga nada que ver con la misión. Y porque Kevin es un cerdo."
    mc "Gracias."
    call BlinkXP ("c13s003_390" , "d") from _call_BlinkXP_191
    ama "No tienes que darlas. Saca a [sca] de aquí en cuanto puedas."
    ama "No sabía lo del dinero de su padre, pero parece que era una de las razones por la que la Señora Russell no la ha echado antes."
    ama "Nos veremos pronto. Buen puñetazo, por cierto."
    stop music fadeout (1.5)
    scene black with dissolve
    "Haces una llamada a [nor] y, después de confirmar la que pensabas que sería su respuesta, vas a la habitación de [sca]."
    call BlinkXP ("c13s003_395" , "d") from _call_BlinkXP_192
    play music "music/Retrospection.ogg"
    mc "¿Necesitas ayuda?"
    sca "No sé por donde empezar. He cogido la ropa... y... y..."
    mc "Ven aquí."
    call BlinkXP ("c13s003_400" , "d") from _call_BlinkXP_193
    sca "No tengo ni idea de qué voy a hacer... de dónde voy a vivir... estoy sin blanca..."
    mc "No te preocupes por eso. Acabo de hablar con [nor] y con [dap]. Les he explicado lo que ha pasado... al menos parte. He obviado lo del video."
    mc "Puedes vivir en casa de [nor], si no te importa compartir habitacion con [dap]."
    call BlinkXP ("c13s003_405" , "d") from _call_BlinkXP_194
    sca "¿Que has hecho {b}qué{/b}?"
    mc "Sí, [sca]. No tienes que preocuparte de dónde vas a vivir. Casi eres parte de la familia..."
    if sca._var("route"):
        call KissXP ("c13s003_410" , "d") from _call_KissXP_4
        sca "Te quiero. Gracias."
        mc "Y yo a ti. Pasabas la mitad de las noches allí. Ahora serán todas."
    else:
        call KissXP ("c13s003_415" , "d") from _call_KissXP_5
        sca "Gracias, [mc]."
        mc "No tienes por que darlas. Pasabas la mitad de las noches allí. Ahora serán todas."
    mc "Vamos a acabar de recoger tus cosas y las llevamos a la camioneta."
    call BlinkXP ("c13s003_420" , "d") from _call_BlinkXP_195
    sca "Pero ¿qué me llevo? Toda mi vida está en esta habitación..."
    mc "Todo lo que quieras conservar."
    if sca._var("route"):
        mc "Todo lo que quieras llevarte de esta vida a la que vas a empezar en casa."
    scene c13s003_425a with dissolve
    mc "Tus fotos y pósters..."
    scene c13s003_425b with dissolve
    mc "Discos, libros..."
    mc "Cualquier cosa que quieras conservar. La parte de atrás de la camioneta está vacía. Voy a ir llevando el tocadiscos mientras decides que llevar."
    call BlinkXP ("c13s003_430" , "f") from _call_BlinkXP_196
    stop music fadeout (1.5)
    "Una hora después, tras varios viajes a la camioneta y una llamada de teléfono..."
    sca "Ya está todo. Nos podemos ir."
    mc "Despídete de esta casa, [sca]. ¿Lo llevamos todo?"
    call BlinkXP ("c13s003_435" , "d") from _call_BlinkXP_197
    $renpy.sound.play("music/Motor.ogg", loop=True)
    sca "Sí, no queda nada ahí que quiera conservar. Una parte de mí la va a echar de menos. Otra parte mayor... no."
    sca "Saber que mi madre me ha estado ocultando cosas, que ha estado en contacto con mi padre todo este tiempo... que ha creído a Kevin antes que a mí..."
    mc "Sé que es difícil de digerir, pero vas a vivir con nosotros. Te vamos a ayudar entre todos."
    call BlinkXP ("c13s003_440" , "d") from _call_BlinkXP_198
    sca "Gracias, [mc], una vez más."
    mc "No tienes por qué darlas. Pero nos tenemos que ir. Las nuevas inquilinas nos estarán esperando."
    call BlinkXP ("c13s003_445" , "d") from _call_BlinkXP_199
    sca "Es verdad, hoy llegaba la última estudiante del verano."
    mc "Sí, pasamos por el hospital a recoger a Kiara y vamos al aeropuerto a buscarla. Su vuelo llega en una hora."
    call BlinkXP ("c13s003_450" , "d") from _call_BlinkXP_200
    sca "¿Kiara?"
    mc "Ahora la conocerás. Creo que te va a gustar."
    return
label c13s004_KiaraAndScarlett:
    if _in_replay:
        $ AuxReplay = True
        menu:
            "¿Estás en una relación con [sca]?"
            "Sí":
                $ sca._var("route" , True)
                menu:
                    "¿Estás en una relación con [dap]?"
                    "Sí":
                        $ dap._var("route" , True)
                    "No":
                        $ AuxReplay = False
                        $ dap._var("route" , False)
            "No":
                $ AuxReplay = False
                $ sca._var("route" , False)
        if not AuxReplay:
            menu:
                "¿Tienes más de una relación?"
                "Sí":
                    $ mc._var("relationships" , 2, intention = "set")
                "No":
                    $ mc._var("relationships" , 0, intention = "set")
        call mrS3_edmund_story from _call_mrS3_edmund_story_4
    call BlinkXP ("c13s004_005" , "d") from _call_BlinkXP_201
    sca "¿Quién es? ¿La conozco? No me suena el nombre."
    mc "Es la madre de [eil]. Va a vivir unos días con vosotras, en casa de [nor]."
    call BlinkXP ("c13s004_010" , "d") from _call_BlinkXP_202
    sca "¿[eil] también?"
    mc "Sí, ¿por qué lo preguntas?"
    if sca._var("route"):
        call BlinkXP ("c13s004_015" , "d") from _call_BlinkXP_203
        sca "Tan solo por curiosidad. Hace un tiempo me hubiera puesto celosa por saber que [eil] iba a vivir en tu casa... más o menos..."
        if mc._var("relationships") > 1:
            sca "Ahora que sé que estás saliendo con otras chicas, casi me alegraría que [eil] fuera una de ellas... y no, no estoy preguntando si lo es."
            mc "Eso se lo tendrás que preguntar a ella. A ser posible conmigo delante. *Risa* Su cara puede ser muy divertida {b}si{/b} no estoy con ella."
        else:
            sca "Ahora que estás saliendo conmigo, me da lo mismo quien viva contigo... con nosotros..."
            mc "[sca], ahora mismo solo me importas tú. No me importa quién viva en casa."
    else:
        call BlinkXP ("c13s004_020" , "d") from _call_BlinkXP_204
        sca "Tan solo por curiosidad. Tú y yo no vamos a estar juntos nunca, con lo que no debo ponerme celosa por que tu ex viva en tu casa... más o menos..."
        mc "[sca], ya lo hemos hablado. No sería justo para ninguno de los dos, lo único que harías es hacerte daño."
        sca "Lo sé, pero no por ello es más fácil."
    call BlinkXP ("c13s004_025" , "d") from _call_BlinkXP_205
    sca "Si puedo preguntar, ¿por qué se han mudado a casa de [nor]?"
    mc "Por la misma razón que tú. Han tenido problemas en casa, y les hemos ofrecido un sitio donde quedarse. De momento se quedarán una semana."
    sca "Supongo que no vas a entrar en detalles igual que no entrarías si alguien te preguntará por qué me he mudado yo."
    mc "Exacto. Creo que cada una de vosotras tiene derecho a explicar lo que quiera a quién quiera."
    call BlinkXP ("c13s004_030" , "d") from _call_BlinkXP_206
    sca "Y cambiando de tema... ¿quién es la falsa [emm]?"
    mc "Aún no estoy muy seguro. De momento te puedo decir que las dos veces que la he visto ha aparecido para ayudar. Fue ella la que mandó el video."
    mc "Me ha dicho que en uno o dos días se pondrá en contacto con la familia para aclarar las cosas... supongo..."
    call BlinkXP ("c13s004_035" , "d") from _call_BlinkXP_207
    sca "¿Cómo sabía lo que estaba pasando? ¿También hay cámaras en el salón?"
    mc "Creo que la casa de tu madre tiene cámaras por todos lados..."
    if sca._var("route"):
        mcp "{i}(Mejor no decirle que nos grabaron el domingo. Si han destruído el video, no hay de qué preocuparse.){/i}"
    mc "Ya estamos llegando al hospital. Ahora te presento a Kiara y vamos a comer."
    call BlinkXP ("c13s004_040" , "f") from _call_BlinkXP_208
    mc "Hola, Kiara. Sube."
    call BlinkXP ("c13s004_045" , "f") from _call_BlinkXP_209
    mc "¿Cómo ha ido? ¿Qué tal te ha tratado [sam.nick]?"
    kia "Mal y bien. El hematoma es señal de un pequeño desgarro muscular. [sam] ha sido un cielo, me ha dado un ungüento."
    mc "Por cierto, [sca] - Kiara, Kiara - [sca]."
    kia "Encantada, [sca]."
    call BlinkXP ("c13s004_050" , "d") from _call_BlinkXP_210
    sca "Igualmente, Kiara. Me ha dicho [mc] que somos las nuevas inquilinas. Yo también me mudo hoy."
    call BlinkXP ("c13s004_055" , "d") from _call_BlinkXP_211
    kia "¡Oh! ¿Eres la nueva estudiante? Creía que tu vuelo llegaba más tarde..."
    mc "No, [sca] es una amiga de la familia. Se va a mudar a la habitación de [dap]. A la estudiante la irémos a buscar después de dejarte en el trabajo."
    call BlinkXP ("c13s004_060" , "d") from _call_BlinkXP_212
    kia "Genial, me extrañaba que hubiera volado con tantas cajas."
    kia "No me va a dar tiempo de comer con vosotros. Voy a llegar un poco justa."
    mc "Aún nos queda un rato. Conozco un sitio al lado de tu trabajo. O conocía antes de ir a la universidad... no sé si el puesto de perritos seguirá ahí."
    call BlinkXP ("c13s004_065" , "d") from _call_BlinkXP_213
    kia "Sí, sigue ahí. Dejadme invitaros a comer."
    mc "He sido yo quién te ha dicho que te invitaría a comer, con lo que no voy a aceptar que pagues tú."
    mc "[sca], ¿te gustan los perritos?"
    call BlinkXP ("c13s004_070" , "d") from _call_BlinkXP_214
    sca "¡Me encantan!"
    mc "Entonces no se hable más. Perritos para todos."
    stop sound fadeout (1.5)
    call BlinkXP ("c13s004_075" , "f") from _call_BlinkXP_215
    "Unos perritos después..."
    play music "music/Birds.ogg"
    sca "Y esa es mi historia y por qué de me estoy mudando..."
    mcp "{i}(Has hecho bien en omitir lo del video. Habría que dar muchas explicaciones a Kiara y querría hablar con Amanda antes. O con Eva.){/i}"
    call BlinkXP ("c13s004_080" , "d") from _call_BlinkXP_216
    kia "Lo siento mucho, [sca]. Yo creía que lo mío era malo, pero lo tuyo es horrible."
    kia "No sé si es peor lo de Kevin o que te haya ocultado que ha estado en contacto con tu padre."
    mcp "(Es sorprendente lo rápido que han encajado estas dos. Las dos lo han pasado mal y a Kiara le ha salido la vena maternal y protectora en cuanto se han explicado sus historias.)"
    call BlinkXP ("c13s004_085" , "d") from _call_BlinkXP_217
    sca "Lo más peligroso ha sido lo de Kevin. Lo que más me ha dolido ha sido lo de mi padre."
    sca "Ella sabe lo importante que ha sido para mí saber quién es durante todos estos años. Ocultarmelo ha sido... doloroso."
    if mc._var("edmundsStory"):
        mcp "{i}(Si mis sospechas son ciertas, no tendrás que esperar mucho para saberlo, aunque sea un saco de mierda.){/i}"
    call BlinkXP ("c13s004_090" , "d") from _call_BlinkXP_218
    kia "Yo podría hacer algo al respecto si la cosa se pusiera fea, pero tú lo tienes más complicado con lo de Kevin. Sin pruebas..."
    mc "Ahora solo hace falta que quieras hacerlo antes de que se ponga demasiado fea."
    call BlinkXP ("c13s004_095" , "d") from _call_BlinkXP_219
    kia "No insistas, [mc]. No quiero poner la denuncia. Ha sido la primera vez en 3 años, creo que se va a asustar lo suficiente con que nos hayamos marchado como para repetirlo."
    mc "No estoy insistiendo, Kiara. Al menos ahora tienes un informe médico por si cambias de opinión. Espero que no lo hagas demasiado tarde."
    call BlinkXP ("c13s004_100" , "d") from _call_BlinkXP_220
    sca "Creo que te equivocas, [mc]. Si fuera yo, presentaría la denuncia, pero Kiara tiene razón."
    sca "Pero quien pega a una mujer por norma es un cobarde. Kiara y [eil] lo han abandonado, aunque sea temporalmente, y eso le hará recapacitar."
    mc "Espero que tengas razón. Que la tengáis las dos."
    call BlinkXP ("c13s004_105" , "d") from _call_BlinkXP_221
    kia "Yo sé que la tenemos, y lo verás la semana que viene cuando volvamos a casa."
    kia "Ahora debería ir a trabajar si no quiero llegar tarde. Muchas gracias por todo, [mc]."
    mc "¿Quieres que pase a buscarte cuando salgas del trabajo?"
    call BlinkXP ("c13s004_110" , "d") from _call_BlinkXP_222
    kia "No hace falta, cogeré el autobús. Saldré tarde hoy."
    kia "Nos vemos en casa de [nor], [sca]. Hasta luego, [mc]."
    mc "Hasta luego, Kiara."
    call BlinkXP ("c13s004_115" , "d") from _call_BlinkXP_223
    sca "Nos vemos en casa, Kiara."
    mcp "{i}(Enorme diferencia en la misma frase. Para [sca] ya es su casa. Kiara lógicamente se siente como una invitada. No me importaría que se quedaran. Estarían más seguras.){/i}"
    mc "Siguiente parada, el aeropuerto para recoger a [sai]"
    call BlinkXP ("c13s004_120" , "d") from _call_BlinkXP_224
    sca "¿[sai]? ¿No se llamaba así tu novia de Portland? Bueno... novia... la chica con la que tenías una relación abierta..."
    mc "Sí, estoy seguro de que es ella. Solo me falta confirmarlo."
    call BlinkXP ("c13s004_125" , "d") from _call_BlinkXP_225
    sca "¿Querrías que fuera ella?"
    mc "Por una parte no estoy seguro. Por otra, sí, lo querría. Si no fuera ella no la reconocería y me he dejado el cartel con su nombre en casa. *Risa*"
    if sca._var("route"):
        mc "¿Te molestaría que fuera ella?"
        call BlinkXP ("c13s004_130" , "d") from _call_BlinkXP_226
        sca "Por una parte sí. No saber si viene a recuperarte o no... me pondría nerviosa."
        sca "Por otra parte, le debo estar agradecida."
        mc "¿Qué? ¿Por qué?"
        call BlinkXP ("c13s004_135" , "d") from _call_BlinkXP_227
        if mc._var("relationships") > 1:
            sca "Por meterte en esa cabezota tuya la idea de las relaciones abiertas o con más de una chica."
            if dap._var("route"):
                sca "No me gustaría tener que competir con [dap] por la exclusividad."
            else:
                sca "Si solo quisieras estar con una chica yo tendría menos oportunidades de ser la elegida."
        else:
            sca "Por dejarte marchar sin asegurar la relación. Si no fuera por eso, difícilmente estaríamos juntos ahora."
        mc "Tienes razón. La situación sería muy diferente si no fuera por ella."
        mc "Ya que estamos hablando de [sai], ¿cómo quieres que te presente? ¿Amiga? ¿Novia?"
        call BlinkXP ("c13s004_140" , "d") from _call_BlinkXP_228
        sca "¡Novia, por supuesto! Si quieres hacerlo público claro..."
        mc "Entonces será novia."
    call BlinkXP ("c13s004_145" , "d") from _call_BlinkXP_229
    stop music fadeout (1.5)
    sca "¿Vamos? Tengo ganas de conocerla."
    return
label c13s004_GetSaira:
    if _in_replay:
        $ mc._var("relationships" , 0, intention = "set")
        call mrS3_sca_route from _call_mrS3_sca_route_13
        if sca._var("route"):
            call mrS3_dap_route from _call_mrS3_dap_route_16
        call mrS3_eil_route from _call_mrS3_eil_route_12
        if mc._var("relationships") < 2:
            call mrS3_rels from _call_mrS3_rels_34
        call mrS3_edmund_story from _call_mrS3_edmund_story_5
    if mc._var("edmundsStory"):
        play music "music/Morning-Sun.ogg"
        call BlinkXP ("c13s004_200" , "d") from _call_BlinkXP_230
        mc "Vamos a quedarnos sentados aquí un momento, [sca]. Hay un tema que quiero hablar contigo."
        sca "De golpe estás sonando muy serio, [mc]. ¿Pasa algo?"
        mc "Bueno, hay algo que quiero comentarte."
        call BlinkXP ("c13s004_205" , "d") from _call_BlinkXP_231
        sca "Me estás preocupando. ¿He hecho algo malo?"
        mc "¿Tú? ¡No! Quiero hacerte unas preguntas sobre el tema de tu padre."
        call BlinkXP ("c13s004_210" , "d") from _call_BlinkXP_232
        sca "Bueno, después de lo que me ha dicho mi madre esta mañana, dudo que nunca le saque la verdad sobre quién es."
        sca "¿Puedes creerte que ha estado en contacto con él todo este tiempo? ¿Recibiendo dinero de él? ¿Y ocultándomelo?"
        mc "Tu madre me ha parecido un poco... no quiero ser ofensivo ni molestarte, al fin y al cabo es tu madre."
        call BlinkXP ("c13s004_215" , "d") from _call_BlinkXP_233
        sca "Puedes decir lo que quieras. No me voy a ofender aunque la llames despreciable. Ahora mismo es la palabra que me viene a la mente. Estoy muy enfadada con ella."
        mc "Me ha parecido muy fuerte que dijera que le habías destrozado la vida, y que lo siguiente de lo que hablara fuera del dinero de tu padre..."
        call BlinkXP ("c13s004_220" , "d") from _call_BlinkXP_234
        sca "Aunque no tiene disculpa, casi la entiendo. Para ella el dinero es muy importante. Mis abuelos no quisieron ayudarla cuando se quedó embarazada de mí."
        sca "Pasó de estar a punto de ir a Yale con una beca a tener que irse de casa y buscarse la vida trabajando de camarera en un bar cutre, viviendo de las propinas..."
        sca "Mis abuelos cambiaron de opinión cuando nací, pero ella no quiso volver. La relación ya estaba muy dañada entre ellos. Solo veía a mis abuelos en los cumpleaños, Acción de Gracias, Navidad..."
        mc "Pero parece que no vivía solo de las propinas, sino también del dinero que tu padre le enviaba."
        call BlinkXP ("c13s004_225" , "d") from _call_BlinkXP_235
        sca "Sí, eso parece. Una mentira más que sumar a la larga lista de mentiras que ha contado sobre él. Si al menos supiera quién es..."
        mc "Me parece que ha dicho alguna mentira más sobre el tema, como que ha dejado de mandar dinero por que ya tenías 18."
        call BlinkXP ("c13s004_230" , "d") from _call_BlinkXP_236
        sca "¿Por qué dices eso?"
        mc "Si te dijera que es posible que tenga una pista, que podrías encontrar a tu otra familia... ¿querrías seguirla?"
        call BlinkXP ("c13s004_235" , "d") from _call_BlinkXP_237
        sca "{b}¿Qué?{/b} ¡Por supuesto que querría!"
        sca "¿De dónde has sacado la información?"
        mc "Antes de responderte, déjame darte algunos datos. No es tan sencillo."
        call BlinkXP ("c13s004_240" , "d") from _call_BlinkXP_238
        sca "¿Que puede haber de complicado? Una prueba de ADN resolvería las dudas..."
        mc "Lo complicado es que tu posible padre no está disponible para hacer una prueba de ADN. Pero déjame explicarte lo que sé."
        call BlinkXP ("c13s004_245" , "d") from _call_BlinkXP_239
        "Explicas a [sca] la conversación de ayer con tu padre, sin decirle que es tu padre, y las pistas que dejó caer sobre la identidad de tu medio hermana."
        mc "Y eso es todo lo que sé."
        sca "Tengo que ser yo. 18 años, segunda de mi clase, empiezo medicina en la NWU, la matrícula está pagada, y ha enviado dinero a mi madre."
        mc "Ese último dato es el que me ha hecho atar cabos. Estaba bastante seguro de que podías ser tú, pero al decir tu madre lo del dinero casi ha confirmado mis sospechas."
        call BlinkXP ("c13s004_250" , "d") from _call_BlinkXP_240
        sca "Pero hay una cosa que no entiendo. ¿Por qué ese hombre, mi posible padre, te lo contó a ti?"
        call BlinkXP ("c13s004_255" , "d") from _call_BlinkXP_241
        sca "A menos que..."
        call BlinkXP ("c13s004_260" , "d") from _call_BlinkXP_242
        if sca._var("route"):
            sca "No puede ser, ¿verdad? No eres mi medio hermano... no ahora..."
        else:
            sca "No puede ser, ¿verdad? No eres mi medio hermano..."
        mc "Podría ser. Engañó a mi madre y las fechas coinciden, pero deberíamos confirmarlo antes de..."
        call BlinkXP ("c13s004_265", "h") from _call_BlinkXP_243
        sca "¡Eres mi hermano!"
        mc "[sca], no. No lo sabemos todavía. Podría ser una chica de Westport que estudie medicina en la NWU. Tenemos que confirmarlo antes..."
        call BlinkXP ("c13s004_270" , "d") from _call_BlinkXP_244
        sca "Tienes razón. Siempre pensé que quería encontrar a mi padre. Mi madre me dijo que estaba casado, pero ha mentido tanto que nunca pensé en si tendría hermanos."
        mc "O primas... si mis sospechas son ciertas puede que tengas una gran familia."
        if sca._var("route"):
            call BlinkXP ("c13s004_275" , "d") from _call_BlinkXP_245
            sca "Y esto... ¿cómo nos deja a nosotros?"
            mc "Hasta que no tengamos confirmación, igual que estamos. No quiero actuar en base a suposiciones."
            call BlinkXP ("c13s004_280" , "d") from _call_BlinkXP_246
            sca "Pero... ¿Y si somos...?"
            mc "¿Y si no somos...?"
            mc "Acabamos de empezar a salir. No pienso romper contigo porque tengamos sospechas de que eres mi hermana."
            if persistent.family:
                mc "Y aunque lo seas, tampoco pienso hacerlo."
            else:
                mc "Y si lo eres, ya hablaremos de ello."
            call BlinkXP ("c13s004_285" , "d") from _call_BlinkXP_247
            if dap._var("route"):
                sca "Suponía que esas cosas no te importaban... también sales con [dap]."
                mc "Bueno, sobre eso es algo que deberemos hablar [dap] y yo. A ella parece no importarle y..."
                call BlinkXP ("c13s004_290" , "d") from _call_BlinkXP_248
                sca "A mí tampoco me importaría..."
            else:
                call BlinkXP ("c13s004_290" , "d") from _call_BlinkXP_249
                sca "A mí no me importaría..."
            mc "Entonces ya lo hablaremos si tenemos confirmación positiva. Y si es negativa, no habrá nada de lo que hablar. Primero habrá que confirmar si somos familia."
        else:
            call BlinkXP ("c13s004_275" , "d") from _call_BlinkXP_250
            sca "¿Te imaginas que [dap] y yo fueramos primas? Ya casi es como una hermana para mí y..."
        call BlinkXP ("c13s004_295", "h") from _call_BlinkXP_251
        sca "¡[emm] sería mi hermana también!"
        mc "Supongo que debes estar en shock ahora mismo. *Risa* No es típico de ti tardar tanto en darte cuenta de algo."
        call BlinkXP ("c13s004_300" , "d") from _call_BlinkXP_252
        sca "Son muchas cosas que asimilar..."
        mc "Es normal, [sca]. Ayer yo estaba igual que tú ahora mismo."
        mc "Escucha, creo que deberías tomarte un tiempo para pensar. El vuelo de [sai] llega en un rato y deberíamos ir al aeropuerto."
        call BlinkXP ("c13s004_305" , "d") from _call_BlinkXP_253
        sca "Entonces vamos a por ella. Creo que tenemos que hablar de esto sin interrupciones cuando haya tenido tiempo de asimilarlo y..."
        mc "Solo una cosa más, [sca]. De momento no se lo digas a nadie. Nadie sabe que he estado hablando con mi padre ni lo que me ha dicho. Me gustaría explicarlo cuando sea el momento."
        sca "Lo entiendo, aunque me moriré de ganas de decírselo a [dap]."
        stop music fadeout (1.5)
    else:
        mc "Vamos."
    scene black with dissolve
    "Llegáis al aeropuerto justo a tiempo después de pillar un pequeño atasco. Los carteles indican que el vuelo de [sai] ha aterrizado hace unos minutos."
    play music "music/RayOfHope.ogg"
    scene c13s004_310a with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXP ("c13s004_315" , "d") from _call_BlinkXP_254
    "Unos minutos después aparece [sai] y te levantas a recibirla."
    sai "¡Sorpresa! *Risa*"
    mc "*Risa* Casi... la estropeaste al no colgar la video conferencia."
    call BlinkXP ("c13s004_320" , "d") from _call_BlinkXP_255
    sai "Maldición... ¿cuanto oíste?"
    mc "Todo hasta que colgaste."
    call BlinkXP ("c13s004_325" , "d") from _call_BlinkXP_256
    sai "No pienses mal, no pienso todo lo que dije..."
    mc "No te preocupes, sé que puedes ser más ladradora que mordedora."
    call BlinkXP ("c13s004_330" , "d") from _call_BlinkXP_257
    sai "¿No me vas a dar un beso de bienvenida?"
    python:
        wt1 = _("Ruta con [sai] abierta.")
        wt2 = _("Ruta con [sai] cerrada de momento.")
    menu qKissSairaArrival:
        "¿Dónde le das el beso?"
        "En los labios." (wt = wt1):
            $ sai._var("route", True)
            $ mc._var("relationships", 1, "add")
        "En la mejilla." (wt = wt2):
            pass
    $ resetWalkthrough ()
    if sai._var("route"):
        scene c13s004_335a with dissolve
        "Vuestros labios se juntan en un beso que tiene mucha inseguridad detrás. Ninguno de los dos sabe cómo va a reaccionar el otro."
        if mc._var("relationships") > 1:
            "El beso dura un segundo, es tiempo más que suficiente para borrar el mes y medio que habéis estado separados y dejaros donde estábais... casi."
        else:
            "El beso dura un segundo, es tiempo más que suficiente para borrar el mes y medio que habéis estado separados y dejaros donde estábais."
        if sca._var("route"):
            call BlinkXP ("c13s004_340" , "d") from _call_BlinkXP_258
            sca "¡Ejem!"
    else:
        scene c13s004_335b with dissolve
        "No es el beso que [sai] espera y su cuerpo se tensa por un momento. Tienes que hablar con ella antes de pensar en retomar lo vuestro."
        if mc._var("relationships") > 1:
            "Vuestra relación abierta sería mucho más abierta ahora. Tiene que saberlo antes de que piense que vuelves a ser suyo en exclusiva."
        if sca._var("route"):
            call BlinkXP ("c13s004_345" , "d") from _call_BlinkXP_259
            sca "¡Ejem!"
    mc "Ven, [sai], voy a presentarte a..."
    call BlinkXP ("c13s004_350", "h") from _call_BlinkXP_260
    sai "¿Esa es [eil]? Creía que era pelirroja..."
    mc "No, no es [eil]. A [eil] la conocerás hoy. Está viviendo en casa."
    call BlinkXP ("c13s004_355", "h") from _call_BlinkXP_261
    sai "{b}¿QUÉ?{/b}"
    mc "Es largo de contar, ven."
    if sca._var("route") and sai._var("route"):
        call BlinkXP ("c13s004_360" , "d") from _call_BlinkXP_262
    else:
        call BlinkXP ("c13s004_365" , "d") from _call_BlinkXP_263
    if sca._var("route"):
        if mc._var("relationships") > 2 or (mc._var("relationships") > 1 and not sai._var("route")):
            mc "[sai], esta es [sca], una de las chicas con las que salgo."
        elif sai._var("route"):
            mc "[sai], esta es [sca]. Mi otra novia, aparte de ti, si es que quieres volver conmigo, claro."
        else:
            mc "[sai], esta es [sca]. Mi novia."
        mc "Hoy se muda a casa también."
        sca "Encantada, [sai]."
        call BlinkXP ("c13s004_370" , "d") from _call_BlinkXP_264
        sai "¿Qué? ¿Estás saliendo con... con... ella?"
        sai "¿Y [eil]?"
        if eil._var("route"):
            mc "Sí, con [eil] también."
            scene c13s004_375 with hpunch
            sca "¿Qué? ¿Sales con [eil]?" (multiple = 2)
            sai "¿Qué? ¿Ya has vuelto con ella?" (multiple = 2)
            mc "Sí. No te sorprendas tanto, [sca]. Tengo su autorización para hacerlo público."
            mc "[sai], tú y yo teníamos una relación abierta que no lo era en la práctica. Ahora tengo una que lo es."
            call BlinkXP ("c13s004_380" , "d") from _call_BlinkXP_265
            sai "Pero... pero... yo me he transferido por ti..."
            mc "No creo que sea el mejor momento para hablarlo, [sai]. Creo que te lo tengo que explicar en privado."
            mc "No te ofendas, [sca]."
            call BlinkXP ("c13s004_385" , "d") from _call_BlinkXP_266
            sca "No, no me ofendo. Ahora mismo estoy demasiado flipada..."
        else:
            mc "No, [eil] y yo solo somos buenos amigos."
    else:
        mc "[sai], esta es [sca], una amiga. También va a vivir en casa."
        sca "Un placer conocerte, [sai]."
        call BlinkXP ("c13s004_390" , "d") from _call_BlinkXP_267
        sai "Igualmente, [sca]. Por un momento he pensado que eras [eil]."
        sai "Por suerte, [mc] tiene el suficiente tacto como para no venir con su {b}ex{/b}-novia del instituto a buscar a su novia de la universidad."
        if eil._var("route"):
            mc "Bueno, [eil] ya no es una ex-novia."
            scene c13s004_375 with hpunch
            sca "¿Qué? ¿Sales con [eil]?" (multiple = 2)
            sai "¿Qué? ¿Ya has vuelto con ella?" (multiple = 2)
            mc "Sí. No te sorprendas tanto, [sca]. Tengo su autorización para hacerlo público."
            mc "[sai], tú y yo teníamos una relación abierta. Nunca quisiste ser mi novia..."
            call BlinkXP ("c13s004_380" , "d") from _call_BlinkXP_268
            sai "Pero... pero... yo me he transferido por ti..."
            mc "No creo que sea el mejor momento para hablarlo, [sai]. Creo que deberíamos hablarlo en privado."
            mc "No te ofendas, [sca]."
            call BlinkXP ("c13s004_385" , "d") from _call_BlinkXP_269
            sca "No, no me ofendo. Ahora mismo estoy demasiado flipada..."
        else:
            mc "No, [eil] está trabajando ahora mismo, pero tiene ganas de conocerte."
    mc "¿Tienes que recoger maletas, [sai]?"
    call BlinkXP ("c13s004_495" , "d") from _call_BlinkXP_270
    sai "No, va todo en el camión con los muebles y el resto de cosas. Debería haber llegado durante la mañana, salió ayer de Portland."
    mc "Entonces vamos a casa, he salido pronto y no sé si ha llegado."
    mc "Además, tengo que descargar las cosas de [sca] antes de ir a ver a la enfermera."
    call BlinkXP ("c13s004_395" , "d") from _call_BlinkXP_271
    sca "¿La que ha atendido a Kiara?"
    stop music fadeout (1.5)
    mc "Sí, [sam], la madre de Jamaal. Tengo que pasar a verla esta tarde. ¿Vamos?"
    $renpy.sound.play("music/Motor.ogg", loop=True)
    if not eil._var("route"):
        if sca._var("route"):
            if sai._var("route"):
                scene c13s004_400An1 with fade
                "El camino a casa es incómodo, quizás no ha sido una buena idea besar a [sai] delante de [sca] y después presentarla como tu novia."
            else:
                scene c13s004_400An2 with fade
                "De camino a casa [sca] está dicharachera mientras [sai] está silenciosa, quizás esperaba algo más que un beso en la mejilla."
        else:
            if sai._var("route"):
                scene c13s004_400An3 with fade
                "De camino a casa, [sca] y [sai] charlan animadamente. Besar a [sai] ha hecho que sus dudas sobre vuestra relación se disipen."
            else:
                scene c13s004_400An2 with fade
                "De camino a casa [sca] está dicharachera mientras [sai] está silenciosa, quizás esperaba algo más que un beso en la mejilla."
    else:
        if sca._var("route"):
            if sai._var("route"):
                scene c13s004_400An4 with fade
                "El camino a casa es incómodo, quizás no ha sido una buena idea besar a [sai] delante de [sca] y después presentarla como tu novia. Y para colmo decirles que también estás con [eil]."
            else:
                scene c13s004_400An5 with fade
                "El camino a casa es incómodo, quizás no ha sido una buena idea decirles que estás con [eil]. Y seguramente [sai] esperaba más que un beso en la mejilla."
        else:
            if sai._var("route"):
                scene c13s004_400An6 with fade
                "De camino a casa [sca] está dicharachera mientras [sai] parece enfadada, quizás decirle que estás con [eil] justo después de besarla no ha sido buena idea."
            else:
                scene c13s004_400An2 with fade
                "De camino a casa [sca] está dicharachera mientras [sai] está silenciosa, quizás esperaba algo más que un beso en la mejilla."
    stop sound fadeout (1.5)
    "Llegas a casa y entras a presentar a [sai]. [sca] se queda fuera mientras empieza a bajar cajas y maletas."
    play music "music/RayOfHope.ogg"
    call BlinkXP ("c13s004_405", "f") from _call_BlinkXP_272
    if persistent.family:
        mc "[sai], esta es [mar], mi madre. Es una de las administradoras del dormitorio."
    else:
        mc "[sai], esta es [mar], ya te he hablado de ella. Es una de las administradoras del dormitorio."
    mom "Encantada de conocerte, [sai]. [mc] nos ha hablado de ti."
    if emm._var("route"):
        call BlinkXP ("c13s004_415" , "d") from _call_BlinkXP_273
    else:
        call BlinkXP ("c13s004_420" , "d") from _call_BlinkXP_274
    mc "Y esta es [emm], mi hermana. Seguro que os vais a llevar bien."
    emm "Seguro. Bienvenida a casa, [sai]."
    call BlinkXP ("c13s004_425" , "d") from _call_BlinkXP_275
    sai "Encantada de conoceros a las dos. [mc] también me habló mucho de vosotras durante el tiempo que estuvimos juntos en Portland."
    call BlinkXP ("c13s004_430" , "d") from _call_BlinkXP_276
    mom "Voy a acompañarte a tu habitación. Hace 20 minutos que se han ido los de las mudanzas que han traído tus cosas."
    mom "Así también te presento a dos de las chicas que viven en tu misma planta. Las otras dos están en clase."
    call BlinkXP ("c13s004_435" , "d") from _call_BlinkXP_277
    sai "Gracias, [mar]."
    mc "Yo voy a salir a llevar las cosas de [sca] a la habitación de [dap]."
    call BlinkXP ("c13s004_440" , "d") from _call_BlinkXP_278
    mom "¿Cómo está? [nor] me ha explicado lo que ha pasado."
    mc "Ahora está mejor, pero ha sido duro para ella."
    mom "Cuando acabe de enseñarle la casa a [sai] iré a verla. Creo que va a necesitar el cariño de todas."
    if mc._var("edmundsStory"):
        mcp "(Antes de hacer nada con las pruebas de ADN, debería hablar con [mar.mc!t] y explicarle lo que sé.)" id qKissSairaArrival_f7e4136f
    call BlinkXP ("c13s004_445" , "d") from _call_BlinkXP_279
    emm "Yo te acompaño, [mc]. Tengo ganas de darle un abrazo, y así os ayudo a subir cosas."
    mc "Perfecto, vamos. Ahora mismo está descargando ella sola la camioneta."
    stop music fadeout (1.5)
    mc "[sai], te veo luego, cuando estés instalada. [mar.mc!t], cuando acabes, estamos en casa de [nor]."
    play music "music/ChillUkelele.ogg"
    scene c13s004_450 with fade
    "Sales a la calle y te encuentras una tierna imagen con [nor] abrazando a [sca], mientras [dap] se dirige casi volando hacia ellas."
    call BlinkXP ("c13s004_455", "f") from _call_BlinkXP_280
    dap "Vas a estar bien aquí, [sca]. Será como cuando vienes a pasar una noche, pero será para siempre."
    call BlinkXP ("c13s004_460" , "d") from _call_BlinkXP_281
    nor "Solo tienes que pedir lo que necesites. Considéranos tu nueva familia."
    if mc._var("edmundsStory") and persistent.family:
        mcp "(No sabes lo cerca que podrías estar de la verdad, [nor].)"
    call BlinkXP ("c13s004_465" , "d") from _call_BlinkXP_282
    eri "Si te vuelves a teñir de pelirroja y yo vuelvo a mi color, podremos pasar por tres hermanas. O puedes volver tú a tu color y que [dap] se tiña de morena."
    scene c13s004_470 with hpunch
    dap "¡Ni en broma!" (multiple = 2)
    sca "¡Ni por todo el oro del mundo!" (multiple = 2)
    mc "*Risa* Parece que el color del pelo no se toca. Seréis una rubia, una pelirroja y una morena."
    call BlinkXP ("c13s004_475" , "d") from _call_BlinkXP_283
    emm "¿Puedo abrazar a mi nueva prima?"
    if mc._var("edmundsStory") and persistent.family:
        mcp "(O incluso a tu nueva medio hermana, si mis sospechas son correctas.)"
    elif mc._var("edmundsStory"):
        mcp "(O incluso a mi medio hermana, si mis sospechas son correctas.)"
    call BlinkXP ("c13s004_480" , "d") from _call_BlinkXP_284
    sca "Al final me vais a hacer llorar. No esperaba esta recepción..."
    emm "*Susurrando* Si quieres hacerlo, no te cortes, estás en familia."
    call BlinkXP ("c13s004_485" , "d") from _call_BlinkXP_285
    nor "[sca], llevas años viniendo a nuestra casa. Ahora también es la tuya."
    mc "Ahora que ha acabado la ronda de abrazos. ¿Subimos las cosas de [sca] entre todos?"
    scene c13s004_490 with dissolve
    todas "¡Vamos!"
    scene black with dissolve
    "Entre todos subís las cosas de [sca] en pocos viajes. Meemaw y Betty han ido al centro y no están en casa para ayudar."
    "Kate y Debbie se unen a la mudanza en cuanto [mar] les dice las novedades al presentarles a [sai]. Poco después también se unen [mar] y [sai]."
    "Hacéis el trabajo como si de una verdadera familia se tratara. Quizás algún día..."
    stop music fadeout (1.5)
    return
label c13s005_SamanthaHouse:
    if _in_replay:
        $ AuxReplay = True
        call mrS3_sam_route from _call_mrS3_sam_route_9
        call mrS3_sim_route from _call_mrS3_sim_route_9
        call mrS3_sam_blackPanther from _call_mrS3_sam_blackPanther_2
    scene black with dissolve
    "Después de subir las cosas de [sca] a la habitacón de [dap] te despides de todo el mundo y vas a casa de [sam]."
    "Tienes que compensar el plantón de ayer y quieres pasar el máximo de rato con ella y Jamaal."
    if sam._var("route"):
        "Bueno, con Jamaal no tanto como con ella."
    scene c13s005_005 with dissolve
    play sound "music/doorbell1.ogg"
    "*Ding-Dong*"
    jam "*Gritando a través de la puerta* Ya voy yo, Mamá."
    play music "music/SneakySnitch.ogg"
    call BlinkXP ("c13s005_010" , "d") from _call_BlinkXP_286
    jam "¡Hermano! Me ha dicho mi madre que ibas a venir. Esperaba que no nos dieras plantón como ayer."
    mc "Lo siento, Jam. Surgió algo importante."
    call BlinkXP ("c13s005_015" , "d") from _call_BlinkXP_287
    jam "*Gritando* Me dolió mucho en el corazón que nos abandonaras por esa cosa que tenías que hacer."
    jam "*Gritando* Tuve que hacer un esfuerzo y comer más pastitas de las que debía..."
    call BlinkXP ("c13s005_020" , "d") from _call_BlinkXP_288
    jam "*Susurrando* Pero yo te agradecí que no vinieras. Me puse hasta el culo de pastitas."
    mc "*Susurrando* Eres un capullo. *Risa*"
    mc "*Gritando* Si no me hubieras dicho que hacía tres días que no te duchabas, a lo mejor me hubiera atrevido a venir."
    sam "*Desde la cocina* Sabéis que no susurraís demasiado flojo, ¿verdad?"
    call BlinkXP ("c13s005_025" , "d") from _call_BlinkXP_289
    jam "Tío, no sabes ni susurrar. Anda, pasa."
    mc "Apártate primero de en medio. No pienso saltar por encima tuyo. Ya sabes que las carreras de vallas no se me daban bien."
    call BlinkXP ("c13s005_030" , "d") from _call_BlinkXP_290
    sam "Al final has podido venir."
    mc "No podía darte plantón dos días seguidos."
    mc "Por Jamaal no me importa, pero a ti no osaría dejarte plantada por segunda vez."
    call BlinkXP ("c13s005_035" , "d") from _call_BlinkXP_291
    jam "Claro, como el pobre Jamaal ya está plantado en su silla... ¿qué más da dejarlo plantado también cuando se queda con él?"
    mc "Calla y déjame saludar a tu madre como es debido."
    call BlinkXP ("c13s005_040" , "d") from _call_BlinkXP_292
    mc "Estás guapísima, como siempre."
    sam "Y tú eres un adulador, como siempre. Pero puedes seguir haciéndolo, me encanta."
    call BlinkXP ("c13s005_045" , "d") from _call_BlinkXP_293
    sam "Podéis ir a hacer lo que queráis, lo tendré todo preparado en unos minutos."
    mc "¿Necesitas ayuda?"
    sam "No, qué va. Solo me estorbaríais en la cocina."
    mc "Te esperamos aquí sentados. Bueno, Jamaal siempre espera sentado. Es un vago."
    call BlinkXP ("c13s005_050" , "d") from _call_BlinkXP_294
    sam "¡[mc]! Ya sabes que no me gusta que hagas esas bromas."
    mc "Perdón, [sam.nick]. Es la costumbre."
    call BlinkXP ("c13s005_055" , "d") from _call_BlinkXP_295
    jam "¡Hey, a mí me gustan esas bromas! Para una vez que usa el cerebro, déjalo antes de que lo confundan con una endivia."
    mc "Tú te callas, si [sam.nick] no quiere que haga esas bromas, te las haré en privado. Y no, no es una proposición."
    call BlinkXP ("c13s005_060" , "d") from _call_BlinkXP_296
    jam "Tampoco eres mi tipo. *Risa* Y no me puedo desgravar de los impuestos hacer obras de caridad de ese tipo."
    stop music fadeout (1.5)
    jam "Estaremos en mi habitación, Mamá. Avísanos cuando esté todo listo."
    call BlinkXP ("c13s005_065", "f") from _call_BlinkXP_297
    play music "music/CCFunk.ogg"
    jam "¿Te llegó mi correo? ¿Recordabas las contraseñas?"
    mc "Sí, son contraseñas que no olvidaré nunca. *Risa*"
    mc "Gracias por la información, pero recuerda esas dos preguntas estúpidas que acabas de hacer."
    call BlinkXP ("c13s005_070" , "d") from _call_BlinkXP_298
    jam "¿Estúpidas? ¿Por qué?"
    mc "Luego te lo explico. ¿Has conseguido encontrar los nombres de las cinco chicas que te pedí?"
    call BlinkXP ("c13s005_075" , "d") from _call_BlinkXP_299
    jam "Sí, es gracioso. Amanda, Beatrice, aunque a veces aparece como Beatrix, Claire, Diana, y Eva. ABCDE. Todas se apellidan Gilford. GILF-ord."
    mc "Gracias, Jam. ¿Ya has descubierto por qué tus preguntas son estúpidas?"
    call BlinkXP ("c13s005_080" , "d") from _call_BlinkXP_300
    jam "No, sigo sin verlo."
    mc "Has buscado el nombre de cinco chicas que te pedí ayer, ¿verdad?"
    jam "Sí, claro. Me puse a ello en el momento en que recibí tu correo..."
    call BlinkXP ("c13s005_085" , "d") from _call_BlinkXP_301
    jam "Correo que no me hubieras enviado si no hubieras recibido el mío... vale, colega, tu hermano es tonto."
    mc "No, no lo eres."
    jam "Gracias..."
    mc "Me refiero a que no eres mi hermano. Tu tontedad me avergüenza y te repudio. *Risa*"
    call BlinkXP ("c13s005_090" , "d") from _call_BlinkXP_302
    jam "¡Eres un capullo! ¿Dónde ibas a encontrar un hermano tan guapo como yo?"
    mc "En el zoo seguramente. Si me tengo que retener toda la tarde de meterme contigo por lo que ha dicho [sam.nick], tengo que quitarme el mono ahora."
    call BlinkXP ("c13s005_095" , "d") from _call_BlinkXP_303
    if sam._var("route"):
        jam "¿Toda la tarde? ¡Ni lo pienses! No pienso estar con los dos tortolitos fastidiándoos el plan."
        mc "Jam, no hay plan. He venido a veros como he venido toda mi vida. Recuerda que todas esas paranoias tuyas eran hipotéticas."
        call BlinkXP ("c13s005_100" , "d") from _call_BlinkXP_304
        jam "Sí, sí. Una de las razones por las que venías es porque siempre te gustó mi madre. La otra eran los pastelillos. Ahora tienes las dos cosas. *Risa*"
        mc "Bueno, hoy me conformo con los pastelillos."
    else:
        jam "¿Toda la tarde? ¿No te ha dicho mi madre que tenía que irme hoy?"
        mc "No, no me lo ha dicho. Pero bueno, más pastelillos para mí."
        call BlinkXP ("c13s005_100" , "d") from _call_BlinkXP_305
    jam "La próxima vez que me llames glotón, te recordaré esta conversación. *Risa*"
    call BlinkXP ("c13s005_105" , "d") from _call_BlinkXP_306
    jam "Cambiando de tema. ¿Hay algo que me puedas contar sobre la investigación? ¿O tengo que seguir investigando a ciegas?"
    mc "Hoy me he encontrado con alguien. Me ha dicho que en uno o dos días me va a dar más información."
    call BlinkXP ("c13s005_110" , "d") from _call_BlinkXP_307
    jam "¿Nada que puedas contarme ahora?"
    mc "He aprendido más con tu correo de lo que sabía por mí mismo. Sabes lo mismo que yo."
    call BlinkXP ("c13s005_120" , "d") from _call_BlinkXP_308
    jam "No. Yo sé mucho más ahora que ayer. He descubierto de dónde sacan el dinero."
    mc "¿De dónde?"
    call BlinkXP ("c13s005_125" , "d") from _call_BlinkXP_309
    jam "Vas a flipar. NTR se dedica a hacer Operaciones Especiales en las que nuestro gobierno no quiere involucrarse directamente."
    mc "¿Son mercenarios?"
    jam "Más o menos. Pero unos mercenarios especiales. Utilizan niños para las misiones."
    mc "¿Qué?"
    call BlinkXP ("c13s005_130" , "d") from _call_BlinkXP_310
    jam "Sí, yo también he flipado. Te pongo un ejemplo. He encontrado un par de expedientes de misiones en las que han participado clones de la Serie G. Casi todo censurado."
    mcp "(La serie G son los que se colaron ayer en casa. Eric era Serie E y el resto Serie G.)"
    jam "Lo más curioso es que la Serie G se creó hace 13 años. ¡Son pre-adolescentes!"
    mc "¿Qué? ¡Es imposible! Yo..."
    mcp "(Yo los he visto y diría que tienen alrededor de 20 años.)"
    call BlinkXP ("c13s005_135" , "d") from _call_BlinkXP_311
    jam "Tú... ¿qué?"
    mc "Yo lo veo muy raro... ¿sabes cuando se creó la Serie E?"
    jam "E-F-G... Dos años antes. Hace unos 15. ¿Por qué?"
    mc "Creía haber conocido a un tipo de la Serie E, pero es imposible. Debía estar en la mitad de sus 30."
    mcp "(¿Hay otra empresa haciendo lo mismo que NTR pero con años de ventaja? Las fechas no cuadran con las edades que vi.)"
    call BlinkXP ("c13s005_140" , "d") from _call_BlinkXP_312
    jam "¿Has conocido a un clon?"
    if persistent.family:
        mcp "(He estado hablando con una hace unas horas. Fliparías.)"
    else:
        mcp "(Sí, y tú también. Pero no puedo traicionar las identidades de [emm], [dap], y [eri]. Al menos no sin que ellas lo sepan.)"
    mc "Lo que he dicho es que me había parecido conocerlo, pero las edades no cuadran."
    call BlinkXP ("c13s005_141" , "d") from _call_BlinkXP_313
    jam "Aparte de eso tienen actividades médicas. Nada que esté aprobado en los Estados Unidos. Supongo que una cosa es que los usemos para operaciones encubiertas..."
    mc "Y otra diferente que les dejemos vender medicamentos aquí..."
    call BlinkXP ("c13s005_142" , "d") from _call_BlinkXP_314
    jam "Oh, no, no son medicamentos. Son más bien articulos avanzados de farmacia. Maquinaria, tests para enfermedades..."
    sam "*Desde el salón* Ya está todo listo. Dejad los videojuegos antes de que se enfríe el té."
    stop music fadeout (1.5)
    mc "Seguimos luego, y mándame todo lo que tengas por correo. No podemos hacer esperar a tu madre."
    call BlinkXP ("c13s005_145", "f") from _call_BlinkXP_315
    play music "music/SneakySnitch.ogg"
    sam "Hacía días que no te veía, [mc], excepto esta mañana, claro."
    sam "¿Alguna novedad en casa?"
    mc "Bueno, hoy ha llegado la última de las estudiantes. Ya sabes que [eil] y Kiara están viviendo en casa también."
    mc "Y hoy se ha mudado [sca], la amiga de [dap]. Problemas en casa."
    call BlinkXP ("c13s005_150" , "d") from _call_BlinkXP_316
    sam "Es decir, que estás viviendo con... 13 mujeres, ¿no? No me extraña que quieras fugarte y visitarnos. *Risa*"
    mc "No es malo, de verdad. Y son 15. No has contado a mi Meemaw y a Tía Betty. Llegaron el sábado."
    call BlinkXP ("c13s005_155" , "d") from _call_BlinkXP_317
    jam "*Risa* No es malo ahora. Espera a que se les sincronicen los periodos a las 15... aunque tu abuela y Betty no serán un problema en eso, ¿verdad?"
    mc "*Risa* ¡Qué bruto eres!... ¿Me acogeriais una semana en casa si se diera el caso? *Risa*"
    call BlinkXP ("c13s005_165" , "d") from _call_BlinkXP_318
    sam "Si se diera el caso, con lo mal que lo pinta Jamaal, creo que tendrías que huir del país un par de semanas. A alguna isla del Caribe. *Risa*"
    sam "Aunque él no tiene queja cuando se nos sincroniza a [sim] y a mí... {b}Verdad{/b}, ¿hijo?"
    call BlinkXP ("c13s005_160" , "d") from _call_BlinkXP_319
    jam "No hagas caso, [mc]. Cuando se les sincroniza me encierro en mi habitación una semana. Esa semana soy super productivo en el trabajo."
    mc "Jamaal, no sabes donde te estás metiendo..."
    call BlinkXP ("c13s005_170" , "d") from _call_BlinkXP_320
    sam "No pasa nada, ya lo conocemos y sabemos cómo son sus bromas. No nos afectan demasiado."
    mc "¿Y tú qué me cuentas, [sam.nick]? ¿Alguna novedad desde que fuimos a cenar?"
    call BlinkXP ("c13s005_175" , "d") from _call_BlinkXP_321
    sam "Que llevo una vida aburrida. Trabajo y casa. Eso hace que los días parezcan todos iguales y se hagan eternos. Cuando miras atrás a una cosa especial, como nuestra cena, parece que fue ayer."
    mc "Pues habrá que repetirlo..."
    call BlinkXP ("c13s005_180" , "d") from _call_BlinkXP_322
    jam "Vosotros planead vuestra próxima cita, que a mí me está entrando hambre y esas pastitas me están llamando."
    scene c13s005_185AnBlink with dissolve
    play sound "music/Slap.ogg"
    sam "Solo hay un problema... tu ya comiste ayer más de las que te tocaban. Estas son para [mc]."
    jam "¡Mamaaaaa!"
    call BlinkXP ("c13s005_190" , "d") from _call_BlinkXP_323
    sam "¿Qué quieres que te diga? Creo que me está empezando a bajar el periodo... *Risa*"
    mc "*Risa* Nunca te metas con el periodo de la mujer que te prepara la comida, Jam. Yo si que voy a comer alguna pastita, si no te importa, [sam.nick]."
    call BlinkXP ("c13s005_195" , "d") from _call_BlinkXP_324
    sam "Por supuesto que no, cariño. Tú puedes comer."
    mc "Mmmmm... que buenas están estas pastitas, Jamaal. Lástima que tú no puedas comer... están deliciosas..."
    call BlinkXP ("c13s005_200" , "d") from _call_BlinkXP_325
    jam "Eres... eres... eres un capullo glotón."
    mc "No te enfurruñes, Jam, tú te comiste las tuyas ayer. *Risa*"
    call BlinkXP ("c13s005_205" , "d") from _call_BlinkXP_326
    sam "No te preocupes, el enfurruñamiento le durará hasta que le diga que hoy voy a hacer empanadas argentinas para cenar. ¿Quieres quedarte a cenar?"
    mc "Me encantaría, pero con cuatro inquilinas nuevas... creo que debería estar en casa, por si [mar.mc!t] y [nor] me necesitan."
    call BlinkXP ("c13s005_210" , "d") from _call_BlinkXP_327
    jam "Sólo faltaría eso, que también te comieras las empanadas..."
    jam "Sabes que puedes pedirme lo que quieras, pero con mi comida no puedes jugar..."
    mc "Seguro que tu madre haría más empanadas de las necesarias si me quedase yo, no es que fuese a quitarte comida del plato para ponérmela a mí. *Risa*"
    call BlinkXP ("c13s005_215" , "d") from _call_BlinkXP_328
    sam "No me des ideas, que se está poniendo un poco fondón... *Risa*"
    mc "Echará de menos tener un gordo en la familia, y querrá coger él ese rol. *Risa*"
    call BlinkXP ("c13s005_220" , "d") from _call_BlinkXP_329
    jam "¡No tengo por qué aguantar esto! Voy a irme a la calle a tomarme un café y un dónut antes de irme a ese sitio que tengo que ir..."
    mc "No hace falta, Jam, puedes comerte mis pastitas si quieres..."
    call BlinkXP ("c13s005_225" , "d") from _call_BlinkXP_330
    sam "Pues ya que vas a la calle, bája la caja de la pizza que pediste anoche. Ahora te la traigo."
    mc "[sam.nick], de verdad que no es necesario que se vaya, yo no me voy a comer todas las pastas..."
    if sam._var("route"):
        call BlinkXP ("c13s005_230" , "d") from _call_BlinkXP_331
        jam "*Susurrando* Ya te he dicho que no me quedaría haciendo de aguantavelas toda la tarde. Soy un actor de puta madre."
        mc "No vamos a hacer nada, Jam. Aunque te fueras, [sim] puede llegar en cualquier momento... ¿no?"
        call BlinkXP ("c13s005_235" , "d") from _call_BlinkXP_332
        jam "[sim] se ha ido a trabajar hace un par de horas. Hasta las 7 o las 8 no volverá. Tenéis la casa para vosotros solos."
        mc "Aún así, tu madre no va a querer hacer nada, tú podrías volver en 30 minutos por lo que a ella concierne."
        jam "Veo que ya has dejado de esconderte detrás de la palabra \"hipotéticamente\". *Risa*"
    else:
        call BlinkXP ("c13s005_230" , "d") from _call_BlinkXP_333
        jam "Me hubiera gustado quedarme más, pero tengo que hacer un par de cosas en la calle. De verdad que no me voy por las pastas. *Risa*"
        mc "Últimamente te veo poquísimo. Un día que no estés tan ocupado deberíamos quedar a comer."
        if sim._var("route"):
            call BlinkXP ("c13s005_235" , "d") from _call_BlinkXP_334
            jam "Y así me cuentas como te va con mi hermana. *Risa*"
            mc "Solo si, hipotéticamente, estuviera con ella..."
        else:
            call BlinkXP ("c13s005_235" , "d") from _call_BlinkXP_335
            jam "Cuando quieras. Creo que estaré un poco más libre... en un mes apróximadamente."
            mc "Trabajas demasiado..."
    call BlinkXP ("c13s005_240" , "d") from _call_BlinkXP_336
    sam "Aquí tienes la caja. Recuerda que va al contenedor azul."
    if sam._var("route"):
        scene c13s005_245AnBlink with dissolve
        jam "Bueno, os dejo solos... volveré en tres o cuatro horas, Mamá. Más o menos a la misma hora que [sim]."
        call c13s005_SamanthaSex from _call_c13s005_SamanthaSex
    else:
        call BlinkXP ("c13s005_245" , "d") from _call_BlinkXP_337
        jam "Bueno, voy a tirar esto y a acercarme a la papelería. Vuelvo en un rato."
        call c13s005_SamanthaNoSex from _call_c13s005_SamanthaNoSex
    return
label c13s005_SamanthaNoSex:
    if _in_replay and not AuxReplay:
        call mrS3_sim_route from _call_mrS3_sim_route_10
    call BlinkXP ("c13s005_250" , "d") from _call_BlinkXP_338
    sam "Últimamente trabaja mucho y siempre está yendo y viniendo..."
    mc "¿De quién lo habrá aprendido? *Risa*"
    call BlinkXP ("c13s005_255" , "d") from _call_BlinkXP_339
    sam "Pues no lo sé. *Risa* No me estás culpando a mí, ¿verdad?"
    mc "No, por supuesto. Que tu hijo sea un adicto al trabajo no tiene nada que ver con que tú tampoco lo seas. *Risa*"
    sam "Seguramente no. Dáme un segundo. Tengo que comprobar si tengo de todo para hacer las empanadas para mandarle un mensaje a Jamaal y decirle que lo compre cuando vuelva."
    mc "Tómate todo el tiempo que quieras. Voy a inspeccionar la casa."
    scene c13s005_260 with dissolve
    mc "*Gritando* Siempre me ha encantado esta foto."
    sam "*Desde la cocina* ¿Qué foto?"
    mc "*Gritando* La foto en la que estás patinando."
    sam "*Desde la cocina* ¡Ufff! Te gustan jovencitas. *Risa* En esa foto tenía la edad de [sim]. Aún no sabía que estaba embarazada de Jamaal."
    mc "*Gritando* [sam.nick], me gustas en esta foto, me gustabas cuando te conocí diez años después, y me pareces preciosa ahora..."
    call BlinkXP ("c13s005_265" , "d") from _call_BlinkXP_340
    sam "Ya estoy aquí. He escrito a Jamaal. Me falta tomate."
    mc "Me estás poniendo muy difícil irme. Suenan tentadoras esas empanadas."
    call BlinkXP ("c13s005_270" , "d") from _call_BlinkXP_341
    sam "Pero entiendo que te tengas que ir. Además, no te dejaría acercarte a mi cocina ni aunque me pagaras por ello."
    mc "No soy tan desastre en la cocina... algo he aprendido de [mar.mc!t] y de [nor]."
    call BlinkXP ("c13s005_275" , "d") from _call_BlinkXP_342
    sam "No lo suficiente para que me fíe de ti. Voy a tener que empezar a hacer la masa para que fermente bien. Si quieres sientate aquí y seguimos charlando."
    mc "Te conozco cuando cocinas. Vas a dejar de escucharme en cuanto empieces a amasar, con lo que te voy a dejar que cocines tranquila."
    mc "¿Por qué no venís un día los tres a casa a comer?"
    call BlinkXP ("c13s005_280" , "d") from _call_BlinkXP_343
    sam "¡Sería fantástico! Así conozco a las chicas nuevas y saludo a tu abuela y a Betty."
    sam "O podríamos ir toda la familia a la playa. Hace siglos que no vamos. Llamaré a [mar] para atar cabos."
    mc "Me parece genial. A mí también me apetece."
    call BlinkXP ("c13s005_370" , "d") from _call_BlinkXP_344
    sam "Cuídate, [mc]."
    mc "Tú también, [sam.nick]."
    if sim._var("route"):
        call BlinkXP ("c13s005_285", "f") from _call_BlinkXP_345
        "Al salir al rellano te encuentras una sorpresa."
        mc "¡[sim]! Creía que estabas trabajando..."
        sim "¡Hush! Si nos oye mi madre no voy a poder hacer esto..."
        call KissXP ("c13s005_290", "d") from _call_KissXP_6
        "Vuestros labios se juntan en un beso que dice a gritos que se han echado de menos en los días que hace que no os habéis visto."
        sim "No quiero pasar tantos días sin verte. Ya sé que has estado muy ocupado pero..."
        mc "Tendríamos que vernos más a menudo. Le he dicho a tu madre que vengáis un día a comer a casa. Ella ha propuesto playa..."
        call BlinkXP ("c13s005_295", "d") from _call_BlinkXP_346
        sim "Eso será casi peor que no verte. Tenerte cerca y no poder besarte..."
        mc "Eso tiene fácil arreglo si se lo decimos a tu madre..."
        call BlinkXP ("c13s005_300", "d") from _call_BlinkXP_347
        sim "¡Ni en broma! ¿Sabes la charla que me daría si saliera contigo?"
        mc "¿Tan malo soy para ella? Acabamos de pasar un rato agradable tomando pastitas."
        call BlinkXP ("c13s005_305", "d") from _call_BlinkXP_348
        sim "¿Malo tú? ¡La mala sería yo para ti! Empezaría a decirme que tengo que cuidarte, que un chico como tú no se encuentra todos los días..."
        mc "Y es cierto, no se encuentra todos los días..."
        scene c13s005_290An with dissolve
        sim "Lo sé... por eso se me hace tan duro cuando no puedo hacer esto."
        scene c13s005_310AnBlink with vpunch
        sam "¡[mc]! Te has... dejado... el móvil..."
        call BlinkXP ("c13s005_315", "v") from _call_BlinkXP_349
        sim "¡Mamá! Esto no es lo que parece..."
        mc "[sim]..."
        call BlinkXP ("c13s005_320", "d") from _call_BlinkXP_350
        sim "Bueno, sí. Es lo que parece... [mc] y yo estamos saliendo juntos..."
        call BlinkXP ("c13s005_325", "h") from _call_BlinkXP_351
        sam "{b}¿Qué?{/b} ¿Desde cuándo?"
        mc "Hace una semana."
        sam "¿Y ninguno de los dos tenía pensado decirme nada?"
        call BlinkXP ("c13s005_330", "d") from _call_BlinkXP_352
        sim "Sí, Mamá. [mc] me ha insistido en que te lo dijera, pero yo quería dejar pasar un poco de tiempo antes de..."
        mc "Ya sabes... por si la cosa salía mal..."
        call BlinkXP ("c13s005_335", "d") from _call_BlinkXP_353
        sam "[sim], haz caso a [mc]. Se equivoca tanto como cualquier otro, pero al menos no le gusta mentir y guardar secretos."
        sam "Un chico como él no lo vas a encontrar todos los días."
        scene c13s005_340AnBlink with dissolve
        sim "*Risa*"
        mc "*Risa*"
        call BlinkXP ("c13s005_345", "d") from _call_BlinkXP_354
        sam "¿Qué pasa?"
        mc "Nada, [sam]. Hace un momento tu hija decía que dirías esa frase."
        sam "¿Tan previsible soy?"
        mc "Un poco..."
        sam "Pues sabes lo que viene ahora, ¿verdad?"
        mc "¿Decirme que me vaya y que tienes que darle la charla de las abejas y las flores a [sim]?"
        call BlinkXP ("c13s005_350", "d") from _call_BlinkXP_355
        sim "¡Oh, no!"
        call BlinkXP ("c13s005_355", "d") from _call_BlinkXP_356
        sam "¡Oh, si! Parece que soy previsible de verdad."
        sam "Os dejo un par de minutos para que os despidáis y te quiero en la cocina conmigo, [sim]."
        sam "Hasta luego, [mc]. El día que vayamos a comer o a la playa, ya hablaré contigo. Ahora tengo que tener una charla con mi hija."
        call KissXP ("c13s005_360", "d") from _call_KissXP_7
        mc "No ha ido tan mal, ¿no?"
        sim "Para ti no. ¿Sabes lo que voy a tener que aguantar hasta que vuelva Jamaal? ¡Voy a acabar de abejas y flores hasta la coronilla!"
        mc "Siempre le puedes decir que no eres virgen y que todo eso ya lo sabes..."
        call BlinkXP ("c13s005_365", "d") from _call_BlinkXP_357
        sim "Si quieres enviudar antes de casarte conmigo..."
        sam "*Desde casa* Vuestros dos minutos ya han pasado..."
        call KissXP ("c13s005_290", "d") from _call_KissXP_8
        mc "Nos vemos pronto. Te quiero."
        sim "Yo más."
    scene black with dissolve
    stop music fadeout (1.5)
    return
label c13s005_SamanthaSex:
    call BlinkXP ("c13s005_250" , "d") from _call_BlinkXP_358
    sam "Últimamente está más raro de lo normal. ¿Le has dicho algo de nosotros?"
    mc "No, pero tu hijo no es tonto y lo ha deducido. Me ha intentado sonsacar, pero no le he dicho nada."
    call KissXP ("c13s005_400" , "d") from _call_KissXP_9
    sam "Casi me siento culpable por querer que se fuera para poder besarte."
    mc "Tienes que empezar a pensar cuándo se lo quieres decir a [sim] y Jamaal para no tener que escondernos. Jamaal puede ser muy insistente."
    call BlinkXP ("c13s005_255" , "d") from _call_BlinkXP_359
    sam "Se está convirtiendo en un cotilla, creo que es por hacerle ver los culebrones cuando se recuperaba del accidente. *Risa*"
    sam "Dáme un segundo que me ponga algo más cómodo. Vuelvo en un momento, ponte cómodo."
    mc "Tómate todo el tiempo que quieras. Voy a inspeccionar la casa."
    scene c13s005_260 with dissolve
    mc "*Gritando* Siempre me ha encantado esta foto."
    sam "*Desde la habitación* ¿Qué foto?"
    mc "*Gritando* La foto en la que estás patinando. Estás guapísima."
    sam "*Desde la habitación* ¡Ufff! Es de antes de que nacieras. En esa foto tenía la edad de [sim], aún no sabía que estaba embarazada de Jamaal. *Risa* Te gustan jovencitas."
    stop music fadeout (1.5)
    mc "*Gritando* [sam.nick], me gustas en esta foto, me gustabas cuando te conocí diez u once años después, y me pareces preciosa ahora..."
    if itchio:
        scene itchio
        "Cuando [sam] vuelve, pasáis una agradable tarde jugando al ajedrez."
        call c13s005_CaughtBySim from _call_c13s005_CaughtBySim
        return
    play music "music/KindofGirl.ogg"
    if sam._var("naturalPubicHair"):
        scene c13s005_405n:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXP ("c13s005_405" , "x") from _call_BlinkXP_360
    else:
        scene c13s005_405s:
            yalign 1.0
            linear 5.0 yalign 0.0
        pause (5.0)
        call BlinkXP ("c13s005_405" , "x") from _call_BlinkXP_361
    sam "No esperaba otra respuesta. Te hubieras perdido el postre, ya que no te has comido todos los pastelillos..."
    mc "¡[sam.nick], estás increíble! Pero..."
    call BlinkXP ("c13s005_410" , "d") from _call_BlinkXP_362
    sam "Sin peros, ya has oído a Jamaal, [sim] y él volverán en tres o cuatro horas."
    sam "Te tengo para mí todo ese tiempo, a menos que prefieras estar en algún otro sitio..."
    mc "Si alguna vez prefiero estar en otro sitio que no sea contigo, mátame. *Risa* Ahora mismo no hay mujer más bonita que tú."
    call BlinkXP ("c13s005_415" , "d") from _call_BlinkXP_363
    sam "Otra vez, no esperaba otra respuesta. Hay una cama esperándonos."
    sam "Quiero hacer el amor contigo en mi cama. Esta vez no será en la habitación de un hotel, como dos adolescentes escondiéndose."
    mc "A mí me da lo mismo dónde sea, mientras sea contigo."
    if sam._var("naturalPubicHair"):
        scene c13s005_925pva
        show c13s005_925va
        pause (1.86)
        show c13s005_925vc
    else:
        scene c13s005_925pvb
        show c13s005_925vb
        pause (1.86)
        show c13s005_925vc
    sam "Hoy estás dando todas las respuestas correctas. Por un momento estoy tentada de darte un premio."
    python:
        wt1 = _("Anal con [sam] activado.")
        wt2 = _("Anal con [sam] desactivado.")
    menu qSamanthaAnal:
        "Por mí encantado." (wt = wt1):
            $ sam._var("anal", True)
        "No es lo mío, [sam.nick]." (wt = wt2):
            pass
    $ resetWalkthrough ()
    call BlinkXP ("c13s005_420" , "f") from _call_BlinkXP_364
    hide c13s005_925va
    hide c13s005_925vb
    hide c13s005_925vc
    sam "¡Oops! Creo que me has malinterpretado, cariño. Mi culo no está disponible..."
    if sam._var("anal"):
        mc "Aún..."
        call BlinkXP ("c13s005_425" , "d") from _call_BlinkXP_365
        sam "Pervertido. *Risa* Dejémoslo en que ya lo hablaremos otro día."
    else:
        mc "Como ya te he dicho, no es lo mío."
        call BlinkXP ("c13s005_425" , "d") from _call_BlinkXP_366
        sam "Nos ahorramos una discusión, entonces. *Risa*"
    sam "Pero llevas demasiada ropa aún..."
    mc "Eso tiene fácil arreglo."
    call BlinkXP ("c13s005_430" , "d") from _call_BlinkXP_367
    sam "Sí, voy a desnudar a mi hombre en mi habitación, sin tener que temer si llegarán mis hijos."
    sam "Solo de pensarlo me estoy poniendo super cachonda."
    mc "*Risa* Pensaba desnudarme yo, pero si quieres hacerlo tú, no te voy a decir que no."
    scene c13s005_435An with dissolve
    sam "No me lo perdería por nada del mundo. Va a ser la primera vez que pueda desnudarte con calma."
    call BlinkXP ("c13s005_440" , "d") from _call_BlinkXP_368
    sam "Y recorrer tu piel con mis labios..."
    mc "Me encanta notar tus labios sobre mi piel."
    scene c13s005_445An with dissolve
    sam "Puedo verlo..."
    mc "Ya te he dicho que no es que fuera que me gustasen jovencitas. Quien me gusta, quien me pone cachondo, eres tú."
    call BlinkXP ("c13s005_450" , "d") from _call_BlinkXP_369
    sam "El día de las respuestas correctas. Vamos a la cama."
    mc "Detrás tuyo."
    call BlinkXP ("c13s005_455" , "f") from _call_BlinkXP_370
    sam "Túmbate. Tenemos mucho tiempo, hoy quiero hacer las cosas con calma."
    mc "A tus órdenes, mi amor."
    call BlinkXP ("c13s005_460" , "d") from _call_BlinkXP_371
    mc "¿Aquí va bien?"
    sam "Perfecto, mi vida."
    scene c13s005_930pv
    show c13s005_930v
    sam "¿Te gusta así?"
    mc "Me encanta. Y ver tus preciosos ojos verdes mientras lo haces hace que sea más excitante todavía."
    sam "Puedo notar espasmos en todo el astil. ¿Ya estás a punto?"
    mc "Ni de lejos. Los espasmos son porque me tienes muy cachondo, no por que esté a punto. Además, quiero acabar dentro de ti."
    sam "Otra cosa que tiene fácil solución."
    scene c13s005_935pv
    hide c13s005_930v
    show c13s005_935v
    pause (1.93)
    scene c13s005_935dv with dissolve
    mc "No me refería exactamente a eso, pero no me quejaré."
    sam "¡Mmmpfft!"
    mc "[sam], siempre me has dicho que no debo hablar con la boca llena. Deberías aplicártelo ahora."
    sam "*Gruñido*"
    scene c13s005_940pv
    hide c13s005_935v
    show c13s005_940v
    "Ese gruñido, que reverbera en tu glande, marca el inicio de una increíble mamada."
    "La sensación de sus carnosos labios alrededor de tu ástil mientras su lengua recorre toda la longitud de tu polla, recreándose en tu glande cuando lo tiene a su alcance, es increíble."
    $renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    mc "[sam.nick], sigue así. Está siendo impresionante."
    sam "*Gemido*"
    mc "[sam.nick], ¿te estás tocando mientras me comes?"
    scene c13s005_945pv
    hide c13s005_940v
    show c13s005_945v
    sam "*Gemido afirmativo*"
    "El gemido reverbera en tu glande. Puedes notar la vibración originándose en el fondo de su garganta."
    mc "Te pone cachonda chuparle la polla a tu hombre, ¿verdad?"
    sam "*Jadeo afirmativo*"
    mc "Y te pone más cachonda aún que te hable así, ¿verdad?"
    sam "*Gemido afirmativo*"
    scene c13s005_940pv
    hide c13s005_945v
    show c13s005_940v
    mc "Me está encantando descubrir esta faceta de ti, mi amor. No sabía que tenías este fetiche."
    mc "No sabía que te ponía cachonda que tu hombre te hablara sucio mientras tienes su polla en tu boca..."
    sam "*Jadeo*"
    mc "Sube aquí, quiero acabar dentro de ti. A mí también me está poniendo cachondo."
    sam "*Gemido negativo*"
    mc "¿Me quieres hacer correr con tus labios?"
    sam "*JADEO AFIRMATIVO*"
    mc "No sabía que te pusieras aún más cachonda mientras piensas en mi leche regalimando por tus labios... que no quieras subir hasta hacerme correr."
    sam "*GEMIDO AFIRMATIVO*"
    mc "Pero no quiero que te corras tú sola. Quiero hacerte correr yo. ¿Puedes acariciarme los huevos mientras me comes la polla? Con la mano con la que te estás tocando."
    scene c13s005_465 with vpunch
    "La cara de sorpresa en [sam] es genuina. Parece que esa no era su intención. Pero tampoco es la tuya que se corra ella sola."
    "Estás a punto de correrte y quieres disfrutar de ella durante tu tiempo de recuperación."
    mc "No pares ahora, mi amor, estoy a punto de correrme."
    scene c13s005_950pv
    hide c13s005_940v
    show c13s005_950v
    stop sound fadeout (1.5)
    "[sam] lleva su mano a tus huevos. Puedes notar la humedad de sus fluídos empapando sus dedos."
    "Sabiendo que estás a punto de correrte, ella continúa con más ansia todavía. Deseosa de recibir tu corrida."
    "Solo tienes que decidir dónde correrte."
    python:
        wt1 = _("Sin consecuencias.")
        wt2 = _("Sin consecuencias.")
    menu qSamanthaBlowjobC13:
        "¿Dónde quieres correrte?"
        "En su boca." (wt = wt1):
            call c13s005_mouth from _call_c13s005_mouth
        "En sus tetas." (wt = wt2):
            $ Aux = False
            call c13s005_tits from _call_c13s005_tits
    $ resetWalkthrough ()
    scene c13s005_480g with dissolve
    hide c13s005_950v
    "[sam] se levanta y se dirige al lavabo, ofreciéndote una vista increíble de su culo."
    if sam._var("naturalPubicHair"):
        call BlinkXP ("c13s005_495n" , "f") from _call_BlinkXP_372
    else:
        call BlinkXP ("c13s005_495s" , "f") from _call_BlinkXP_373
    "Vuelve al cabo de un minuto, todavía con hambre en su mirada."
    sam "Ya he vuelto. ¿El pequeñín aún no ha levantado cabeza?"
    mc "*Risa* Ha pasado literalmente un minuto, y nunca me ha puesto cachondo mirar las paredes."
    mc "Ahora que estás aquí, no le va a costar mucho volver a presentar sus respetos."
    mc "Mientras tanto, ponte aquí. Creo que tengo un favor que devolverte, si aún estás cachonda."
    call BlinkXP ("c13s005_500" , "d") from _call_BlinkXP_374
    sam "No sabes nada, [mc] Marks. Los hombres sois como tostadoras, os calentáis en un minuto con un dedo, y os enfriáis igual de rápido."
    sam "Las mujeres somos como hornos de fundición, quizás nos cueste más calentarnos, pero una vez calientes no nos vamos a enfriar por ir al lavabo."
    mc "Tengo mucho que aprender de mi mujercita con experiencia."
    if sam._var("naturalPubicHair"):
        call BlinkXP ("c13s005_505n" , "d") from _call_BlinkXP_375
    else:
        call BlinkXP ("c13s005_505s" , "d") from _call_BlinkXP_376
    sam "No mucho, hay cosas en las que ya eres un experto. *Risa* Me encantó lo que hiciste en el hotel. ¿Puedes repetirlo?"
    mc "¡Aguántame la cerveza!"
    if sam._var("naturalPubicHair"):
        scene c13s005_955npv
        show c13s005_955nv
    else:
        scene c13s005_955spv
        show c13s005_955sv
    "Tu lengua se empapa en sus jugos, su coño se empapa en tu saliva. El olor terroso de su feminidad inunda tus fosas nasales."
    $renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    sam "¡Oh, sí! *Gemido* Es justo como lo recordaba..."
    "El tacto de su piel llena cada terminación nerviosa de las yemas de tus dedos. El sonido ronco de sus gemidos suena como la mejor simfonía."
    "¿Y qué decir de las vistas? Son muchas sensaciones asaltando cada uno de tus sentidos simultáneamente."
    if sam._var("naturalPubicHair"):
        scene c13s005_960npv
        hide c13s005_955nv
        show c13s005_960nv
    else:
        scene c13s005_960spv
        hide c13s005_955sv
        show c13s005_960sv
    sam "¡Oh, por Dios! *Jadeo* Justo ahí. Estoy a punto de llegar"
    "Su cuerpo se va tensando poco a poco, anunciando la llegada de su inminente clímax."
    "La excitación durante la mamada ha hecho que no hagan falta más que unos pocos minutos para que su orgasmo llame a las puertas."
    "Quizás sería un buen momento para..."
    python:
        wt1 = _("Beso Negro activado para [sam].")
        wt2 = _("Beso Negro desactivado para [sam].")
    menu qSamanthaRimjob:
        "¿Quieres hacerle un Beso Negro?"
        "¡Sí!" (wt = wt1):
            $ sam._var("rimjob", True)
            call c13s005_rimjob from _call_c13s005_rimjob
        "No, no es lo mío" (wt = wt2):
            call c13s005_notRimjob from _call_c13s005_notRimjob
    $ resetWalkthrough ()
    call BlinkXP ("c13s005_535" , "d") from _call_BlinkXP_377
    sam "Déjame quitarme los tacones. Quiero tumbarme un poco contigo mientras te recuperas."
    mc "¿Quitarte los tacones? ¿Por qué?"
    call BlinkXP ("c13s005_540" , "d") from _call_BlinkXP_378
    sam "Porque no eres tú quien va a tener que lavar las sábanas después. *Risa*"
    sam "¿Tienes un fetiche con los tacones?"
    mc "No es que tenga un fetiche, pero... es sexy."
    call BlinkXP ("c13s005_545" , "d") from _call_BlinkXP_379
    sam "Entonces me compraré unos solo para tener sexo. Esos no mancharán las sábanas. *Risa*"
    mc "Mmmm... ¿Y tú? ¿Tienes un fetiche con ellos?"
    call BlinkXP ("c13s005_550" , "d") from _call_BlinkXP_380
    sam "No, pero si mi hombre cree que estaré sexy con ellos no voy a negarle esa pequeña petición..."
    sam "Ni casi ninguna otra."
    mc "¿Algún fetiche del que tenga que estar informado?"
    call BlinkXP ("c13s005_555" , "d") from _call_BlinkXP_381
    sam "Nada demasiado raro..."
    mc "Me lo puedes explicar, [sam.nick]."
    call BlinkXP ("c13s005_560" , "d") from _call_BlinkXP_382
    sam "Me gustan los espejos... mirarme en ellos mientras... ya sabes..."
    mc "Solo de pensarlo, mi amigo está empezando a despertarse..."
    scene c13s005_560d with dissolve
    sam "¿No te parece raro?"
    mc "No me parece nada de lo que avergonzarse, ahí tienes uno, aunque el ángulo puede ser un poco complicado para ver tu reflejo."
    call BlinkXP ("c13s005_565" , "d") from _call_BlinkXP_383
    sam "No hay nada como probarlo, ¿no? Aprovechemos que {b}nuestro{/b} amigo se está despertando."
    mc "Puedes tocarlo otra vez, [sam.nick]. *Risa*"
    sam "¿Vas a parafrasear frases de película? Además, no hay nada que tocar, ya está despierta del todo."
    if sam._var("naturalPubicHair"):
        scene c13s005_975npv
        show c13s005_975nv
        pause (0.9)
        scene c13s005_975ndv with vpunch
        hide c13s005_975nv
    else:
        scene c13s005_975spv
        show c13s005_975sv
        pause (1.83)
        scene c13s005_975sdv with vpunch
        hide c13s005_975sv
    "[sam] se sienta a horcajadas encima tuyo y en un solo movimiento se empala en tu sable."
    "Su reciente orgasmo hace que entre como en una vaina hecha especialmente para él."
    "La sensibilidad en tu glande debido a tu reciente orgasmo hace que la sensación sea increíble."
    sam "¡Ufff! ¡Me siento como un pavo relleno!"
    mc "¿Qué tal el ángulo?"
    scene c13s005_560e with dissolve
    $renpy.sound.play("music/SamanthaMoan.ogg", loop=True)
    sam "No es el mejor, pero me sirve. Me estoy poniendo cachonda viéndome atravesada por ti... más cachonda aún."
    mc "Pues imáginate cuando empecemos a movernos..."
    "Esa frase le sirve a [sam.nick] como pistoletazo de salida para empezar a subir y bajar sus caderas."
    if sam._var("naturalPubicHair"):
        scene c13s005_900pv with dissolve
        show c13s005_900v
    else:
        scene c13s005_905pv with dissolve
        show c13s005_905v
    sam "¡Oh, sí! *Gemido* ¡Me encanta ser un pavo relleno!"
    mc "*Risa* No me hagas reír ahora. Las vistas son demasiado buenas como para perdérmelas."
    mc "¿Qué tal tus vistas?"
    if sam._var("naturalPubicHair"):
        scene c13s005_915pv with dissolve
        hide c13s005_900pv
        show c13s005_915v
    else:
        scene c13s005_920pv
        hide c13s005_905v
        show c13s005_920v
    sam "¡Increíbles! *Jadeo* Pero lo más increíble es notarte dentro de mí..."
    "Tan solo decirlo su cuerpo se estremece. Parece que una idea le ha venido a la mente y casi la ha llevado al orgasmo. "
    sam "*Gemido* Pero se me está ocurriendo ... otro fetiche que me gustaría probar..."
    mc "Dime, cariño"
    scene c13s005_980pv with dissolve
    hide c13s005_915pv
    hide c13s005_920pv
    show c13s005_980v
    sam "*Respiración entrecortada* Me estoy imaginando... en esta postura... preñada con tus bebés... notando mis tetas enormes... rebotando en mi barriga..."
    sam "*Gemido* Podría correrme solo de pensar en esa imagen..."
    if persistent.pregnancy or mc._var("wantsChildren"):
        mc "Cuando quieras podemos hacer un bebé..."
        sam "*Jadeo* No me digas eso... mientras estoy cabalgándote... o no voy a dejar que des marcha atrás..."
    else:
        mc "Todo se hablará, [sam.nick]..."
        mcp "(La imagen es tentadora, pero no quiero bebés ahora mismo...)"
        sam "*Jadeo* No me digas eso... mientras estoy cabalgándote... o paro ahora mismo para hablarlo... *Risa jadeante*"
    scene c13s005_910pv
    hide c13s005_980v
    show c13s005_910v
    mc "*Risa* No te lo recomendaría, pero tú tienes el poder. Yo tengo las mejores vistas..."
    sam "*Gemido* Lléname con tu leche. Yo estoy llegando ya..."
    python:
        wt1 = _("Sin consecuencias")
        wt2 = _("Sin consecuencias")
        wt3 = _("[sam] embarazada")
    menu qSamanthaCumC13:
        "¿Dónde quieres correrte?"
        "Correrte dentro" (wt = wt1):
            call c13s005_inside from _call_c13s005_inside
        "Correrte en su estómago" (wt = wt2):
            call c13s005_outside from _call_c13s005_outside
        "Correrte dentro. Ir a por el bebé" (wt = wt3) if persistent.pregnancy and not sam._var("pregnant"):
            play sound ("music/OldMusicBox5.ogg")
            $ sam._var("pregnant", True)
            call c13s005_inside from _call_c13s005_inside_1
    $ resetWalkthrough ()
    scene c13s005_480h with dissolve
    "[sam] se levanta y se dirige al lavabo, volvíendote a ofrecer una vista increíble de su culo. No crees que puedas cansarte de esa vista."
    stop music fadeout (1.5)
    scene c13s005_595a with dissolve
    mc "¿Decías en serio lo de quedarte embarazada?"
    play music "music/LePrunierenFleur.ogg"
    sam "*Desde el lavabo* No lo sé... ha sido algo que he dicho en el calor del momento, pero me ha puesto cachonda pensarlo."
    sam "*Desde el lavabo* Soy un poco mayor para tener hijos, ¿no crees?"
    mc "No, no lo eres."
    sam "*Desde el lavabo* Soy enfermera, sería un embarazo de riesgo, pero se podría llevar a cabo. No me refiero solo a mayor físicamente..."
    sam "*Desde el lavabo* Tengo edad para ser abuela, si [sim] encontrara a alguien y Jamaal no lo espantara..."
    mc "Serías la segunda abuela más guapa del mundo. *Risa*"
    sam "*Desde el lavabo* Lo tuyo con tu Meemaw es increíble. *Risa* Llegar a decirle a la mujer con la que acabas de tener sexo que..."
    play sound "music/Notification.ogg"
    "*Ring-Ring*"
    sam "*Desde el lavabo* ¿Ese es tu móvil?"
    mc "Sí, me lo he dejado en el salón. Voy a ver quién es."
    scene c13s005_595b with dissolve
    mc "Es un mensaje de mi madre."
    sam "*Desde el lavabo* ¿Te tienes que ir?"
    mc "No, me ha escrito para que compre harina de vuelta a casa. Con tanta gente en casa, ha hecho corto para el desayuno de mañana."
    call BlinkXP ("c13s005_600" , "d") from _call_BlinkXP_384
    sam "Qué suerte. Ya creía que te ibas a tener que ir y teníamos que cortar la tarde juntos."
    mc "No la voy a acortar por un poco de harina. Aún tenemos tiempo para estar juntos y echar el segundo round."
    mc "Has dicho que nos lo íbamos a tomar con calma, ¿no?"
    call BlinkXP ("c13s005_605" , "d") from _call_BlinkXP_385
    sam "Sí, tenemos toda la tarde para nosotros. Y yo tengo un hombre desnudo en el salón de mi casa."
    sam "Creo que me voy a aprovechar de él."
    mc "Harás bien. ¿Un hombre desnudo en tu salón? Seguro que no tiene buenas intenciones."
    scene c13s005_610An with dissolve
    "Entre besos y abrazos, [sam] te obliga a sentarte en el sofá. Tú te dejas obligar."
    mc "¿Qué le vas a hacer a ese pobre hombre desnudo?"
    sam "Le voy a hacer pagar por la osadía de presentarse desnudo en mi salón."
    mc "¿Cómo le vas a hacer pagar? Va desnudo y no tendrá dinero."
    sam "Puede pagarme en leche. Me gusta la leche de ese hombre. Quiero tenerla dentro de mí."
    mc "Veo que estás insaciable hoy."
    call BlinkXP ("c13s005_620" , "d") from _call_BlinkXP_386
    sam "Mi amor, hacía cinco días que no te tenía en mis brazos. No sé cuando podré volver a tenerte."
    mc "Cuando quieras, mi vida."
    call BlinkXP ("c13s005_625" , "d") from _call_BlinkXP_387
    sam "Cuando no estoy trabajando, están los niños en casa. Lo de hoy es un cúmulo de casualidades que no sé cuándo se repetirá."
    mc "Pues se lo decimos a tus hijos y a mi familia."
    call BlinkXP ("c13s005_630" , "d") from _call_BlinkXP_388
    sam "¡Pero se van a escandalizar! ¡Estoy con un hombre al que le doblo la edad!"
    mc "Si a ti no te importa la diferencia de edad, ellos no tienen absolutamente nada que decir sobre ello. Ya te he dicho que no me avergüenzo de estar contigo."
    mc "Si tú te avergüenzas de estar conmigo ya es otro asunto."
    call BlinkXP ("c13s005_635" , "d") from _call_BlinkXP_389
    sam "No me avergüenzo, pero es complicado... nunca he estado con nadie desde que murió el padre de [sim] y Jamaal. No sé si lo van a entender."
    mc "[sam], Jamaal prácticamente nos ha dado su bendición. Y [sim]... [sim] puede ser más complicada..."
    sam "Sí, puede serlo..."
    mc "Cuando estés preparada, se lo diremos juntos. Cuanto antes se lo digamos, antes podremos estar juntos sin escondernos."
    scene c13s005_640An with dissolve
    sam "Te quiero."
    mc "Y yo a tí."
    call c13s005_CaughtBySim from _call_c13s005_CaughtBySim_1
    return
label c13s005_CaughtBySim:
    scene c13s005_640An2 with dissolve
    sim "¡Mamá, estoy en casa! Han tenido que cerrar la piscina. Un escape de cloro..."
    call BlinkXP ("c13s005_645" , "h") from _call_BlinkXP_390
    sim "¡Mamá! ¡[mc]!"
    call BlinkXP ("c13s005_650" , "h") from _call_BlinkXP_391
    sam "¡[sim]!"
    stop music fadeout (1.5)
    return
label c13s005_inside:
    if sam._var("naturalPubicHair"):
        call OrgasmX ("c13s005_570") from _call_OrgasmX
    else:
        call OrgasmX ("c13s005_590") from _call_OrgasmX_1
    "[sam] y tú llegáis al orgasmo simultáneamente. Tu leche y sus jugos se juntan en su interior en una explosión de placer."
    sam "¡Mpffft!"
    mc "¡Mpffft!"
    scene c13s005_910pv
    show c13s005_910v
    "[sam] sigue cabalgándote para exprimir los últimos momentos de placer mientras te ordeña el miembro con sus espasmos."
    sam "¡Oh, sí! *Gemido* ¡POR DIOS! ¡Descarga toda tu leche en mi interior! ¡Lléname!"
    stop sound fadeout (1.5)
    "Poco a poco sus movimientos van perdiendo velocidad y termina por derrumbarse encima tuyo, todavía con tu polla dentro."
    if sam._var("naturalPubicHair"):
        scene c13s005_575a with dissolve
    else:
        scene c13s005_575b with dissolve
    hide c13s005_910v
    sam "Ha sido increíble. Esto del espejo es una maravilla..."
    mc "Pues recubramos la habitación con espejos. También tengo uno grande en mi habitación, dentro del armario. Si alguna vez quieres probarlo..."
    call BlinkXP ("c13s005_580i" , "d") from _call_BlinkXP_392
    sam "Me daría mucha vergüenza hacer el amor contigo con [mar] en casa... ¿qué pasaría si nos pillara?"
    mc "Depende de si se lo hemos dicho o no..."
    call BlinkXP ("c13s005_585i" , "d") from _call_BlinkXP_393
    sam "¿Qué? ¿Quieres decirle a tu madre que estamos juntos?"
    mc "[sam.nick], no tengo nada de lo que avergonzarme por estar contigo. Yo se lo diría a todo el mundo si de mí dependiera."
    call BlinkXP ("c13s005_590i" , "d") from _call_BlinkXP_394
    sam "Dame un momento que vaya al lavabo antes de poner las sábanas perdidas. Tu leche empieza a salirse."
    mc "Tanto tiempo como quieras."
    return
label c13s005_outside:
    if sam._var("naturalPubicHair"):
        call OrgasmX ("c13s005_570o") from _call_OrgasmX_2
    else:
        call OrgasmX ("c13s005_590s") from _call_OrgasmX_3
    "[sam] llega al orgasmo en cuanto acaba la frase."
    sam "¡Mpffft!"
    "Sus paredes vaginales empiezan a producir espasmos que puedes notar en toda la longitud de tu polla, llevándote a tu propio clímax."
    if sam._var("naturalPubicHair"):
        call OrgasmX ("c13s005_595n") from _call_OrgasmX_4
    else:
        call OrgasmX ("c13s005_595s") from _call_OrgasmX_5
    stop sound fadeout (1.5)
    "Sales de su interior y empiezas a regar con tu leche su estómago, blanco sobre negro, dibujando un precioso cuadro abstracto."
    mc "¡Mpffft!"
    sam "¡Sí! ¡Cubre mi estómago con tu leche!"
    "Cuando tu descarga finaliza, [sam.nick] se derrumba encima tuyo."
    if sam._var("naturalPubicHair"):
        scene c13s005_575c with dissolve
    else:
        scene c13s005_575d with dissolve
    sam "Ha sido increíble. Esto del espejo es una maravilla..."
    mc "Pues recubramos la habitación con espejos. También tengo uno grande en mi habitación, dentro del armario. Si alguna vez quieres probarlo..."
    call BlinkXP ("c13s005_580o" , "d") from _call_BlinkXP_395
    sam "Me daría mucha vergüenza hacer el amor contigo con [mar] en casa... ¿qué pasaría si nos pillara?"
    mc "Depende de si se lo hemos dicho o no..."
    call BlinkXP ("c13s005_585o" , "d") from _call_BlinkXP_396
    sam "¿Qué? ¿Quieres decirle a tu madre que estamos juntos?"
    mc "[sam.nick], no tengo nada de lo que avergonzarme por estar contigo. Yo se lo diría a todo el mundo si de mí dependiera."
    call BlinkXP ("c13s005_590o" , "d") from _call_BlinkXP_397
    sam "Dame un momento que vaya al lavabo antes de poner las sábanas perdidas. Tu leche empieza a resbalarme por el estómago."
    mc "Tanto tiempo como quieras."
    return
label c13s005_mouth:
    mc "[sam.nick], estoy a punto de correrme."
    "A [sam] parece no importarle y sigue mamando como si no hubiera un mañana."
    call OrgasmX ("c13s005_470") from _call_OrgasmX_6
    "Explotas con una abundante corrida que sus labios no pueden mantener en el interior de su boca."
    mc "¡Mffpt!"
    "Un poco de tu semen escapa por las comisuras de sus labios cuando ella sonríe sin dejar de recorrer tu astil con su boca."
    call BlinkXP ("c13s005_475" , "d") from _call_BlinkXP_398
    "Cuando tu corrida por fin termina, te mira interrogativamente."
    mc "¿Me estás preguntando si tragas o escupes?"
    sam "*Gruñido afirmativo*"
    python:
        wt1 = _("Sin consecuencias.")
        wt2 = _("Sin consecuencias.")
    menu qSamanthaBlowjobC13mouth:
        "¿Qué quieres que [sam] haga con tu corrida?"
        "Tragar." (wt = wt1):
            $ Aux = True
        "Escupir." (wt = wt2):
            $ Aux = False
    $ resetWalkthrough ()
    if Aux:
        mc "Trágatelo, si no te importa."
        scene c13s005_480AnBlink with dissolve
        "[sam] se traga tu corrida y te enseña su boca vacía."
        sam "¿Contento?"
        mc "Mucho. ¿Cachonda?"
        sam "Muchísimo. Dame un segundo para que me limpie lo que se me ha escapado y ahora vuelvo. Vaya desperdicio..."
        mc "Todo el tiempo que quieras."
    else:
        mc "Puedes escupirlo si no quieres tragarlo."
    return
label c13s005_tits:
    mc "[sam.nick], estoy a punto de correrme."
    "A [sam] parece no importarle y sigue mamando como si no hubiera un mañana hasta que nota tu primer espasmo."
    call OrgasmX ("c13s005_485") from _call_OrgasmX_7
    "Ella se saca tu polla de la boca justo antes de que empieces a rociar sus tetas con tu leche."
    mc "¡Mffpt!"
    "Es precioso pintar un Kandinski en su pecho mientras ella te sonrie hambrienta."
    call BlinkXP ("c13s005_490" , "d") from _call_BlinkXP_399
    sam "¿Te ha gustado, mi amor?"
    mc "Me ha encantado. Ahora me toca a mí. Supongo que sigues cachonda, ven aquí."
    sam "¿Cachonda? Muchísimo. Dame un segundo para que me limpie esto y ahora vuelvo. Vaya desperdicio..."
    mc "Todo el tiempo que quieras."
    return
label c13s005_rimjob:
    if sam._var("naturalPubicHair"):
        scene c13s005_965npv
        hide c13s005_960nv
        show c13s005_965nv
        pause (0.93)
        scene c13s005_965ndv
    else:
        scene c13s005_965spv
        hide c13s005_960sv
        show c13s005_965sv
        pause (0.93)
        scene c13s005_965sdv
    "Mueves tu lengua a su agujero pequeño, recorriendo el perineo en el camino."
    "[sam] se tensa más todavía."
    call BlinkXP ("c13s005_510" , "h") from _call_BlinkXP_400
    sam "*Jadeo* ¿Qué crees que estás haciendo? Te he dicho que mi culo..."
    scene c13s005_970pv
    hide c13s005_965sv
    hide c13s005_965nv
    show c13s005_970v
    "Ignoras su queja y empiezas a masajear los bordes de su ano con tu lengua"
    sam "*Gemido* ... no estaba..."
    sam "*JADEO* ... disponible..."
    call OrgasmX ("c13s005_515") from _call_OrgasmX_8
    hide c13s005_970v
    "Apenas pronuncia esas palabras cuando su cuerpo explota en un festival de fluidos."
    sam "¡OH, SÍ! *GEMIDO* ¡Oh, Dios mío!"
    "Mantenerla en tensión durante la mamada hace que su orgasmo sea intenso y explosivo."
    call BlinkXP ("c13s005_520" , "d") from _call_BlinkXP_401
    stop sound fadeout (1.5)
    "Cuando las oleadas de placer empiezan a desaparecer, [sam] se derrumba en la cama."
    sam "Eso ha sido intenso... pero te he dicho que mi culo no estaba disponible..."
    mc "Si me juras que no te ha gustado, no volveré a hacerlo."
    if sam._var("naturalPubicHair"):
        call BlinkXP ("c13s005_525n" , "d") from _call_BlinkXP_402
    else:
        call BlinkXP ("c13s005_525s" , "d") from _call_BlinkXP_403
    sam "Una relación se debe basar en la confianza. *Risa* Nunca te mentiría. Es la primera vez que alguien me hace eso... y me ha encantado."
    sam "Es la primera vez que noto mi coño explotar así... "
    if sam._var("anal"):
        mc "*Risa* Iremos avanzando poco a poco en tu descubrimiento de las bondades de incluir tu culo en nuestros juegos."
        sam "*Risa* Ve quitándote eso de la cabeza..."
        sam "{i}(Aunque si es tan intenso como esto... ¿quién sabe?){/i}"
    else:
        mc "*Risa* Hasta aquí introduciremos tu culo en nuestros juegos. No iremos más allá."
        sam "*Risa* Al menos no te tengo que disuadir de ello."
        sam "{i}(Aunque si es tan intenso como esto... ¿quién sabe si he cometido un error quitándotelo de la cabeza?){/i}"
    return
label c13s005_notRimjob:
    "Casi no te da tiempo de descartar el pensamiento antes de que [sam] explote en un festival de fluidos."
    call OrgasmX ("c13s005_530") from _call_OrgasmX_9
    sam "¡OH, SÍ! *GEMIDO* ¡Oh, Dios mío!"
    call BlinkXP ("c13s005_520" , "d") from _call_BlinkXP_404
    stop sound fadeout (1.5)
    "Cuando las oleadas de placer empiezan a desaparecer, [sam] se derrumba en la cama."
    sam "Eso ha sido intenso... ya te he dicho que había cosas en las que eras un maestro."
    mc "Siempre un placer poder servirla, milady."
    if sam._var("naturalPubicHair"):
        call BlinkXP ("c13s005_525n" , "d") from _call_BlinkXP_405
    else:
        call BlinkXP ("c13s005_525s" , "d") from _call_BlinkXP_406
    sam "Creo que vas a tener más oportunidades de servirme así."
    mc "Yo prefiero la servidumbre mutua..."
    sam "También podemos probar algún día."
    mc "*Risa* No me refería a eso, pero también me vale."
    return

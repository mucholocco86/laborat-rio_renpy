label c26:
    if mee._var("route"):
        call c26s001_MeeDate from _call_c26s001_MeeDate
        call c26s001_MeeSex from _call_c26s001_MeeSex
    else:
        call c26s001_NoMee from _call_c26s001_NoMee
    ######MONDAY August 1st
    call c26s002_EriDapSca from _call_c26s002_EriDapSca
    call c26s003_Sai from _call_c26s003_Sai
    call c26s002_Solomon from _call_c26s002_Solomon
    call c26s003_Sai2 from _call_c26s003_Sai2
    if sai._var("route"):
        call c26s003_SaiSex from _call_c26s003_SaiSex #lewd
    else:
        call c26s003_NoSai from _call_c26s003_NoSai #MR
    call c26s004_MarEmm from _call_c26s004_MarEmm
    call c26s004_Cafe from _call_c26s004_Cafe
    call c26s004_SamSim from _call_c26s004_SamSim #En la tienda. Sam da las gracias por convencer a Sim para entrenar. Todavía no saben nada de la beca
    call c26s004_Jamaal from _call_c26s004_Jamaal
    call c26s005_EvaDap from _call_c26s005_EvaDap
    call c26s005_LisDebKat from _call_c26s005_LisDebKat #charla Desayuno Kate. Si en rel con Deb, planean cita para comer. La empieza Lisa
    ##########TUESDAY August 2
    call c26s006_KatBreakfast from _call_c26s006_KatBreakfast #Desayuno con Kate
    call c26s007_Bet from _call_c26s007_Bet #Ya no es monja
    call c26s007_Bed from _call_c26s007_Bed #Llega la cama nueva
    if deb._var("route"):
        call c26s008_DebTeaser from _call_c26s008_DebTeaser
    return
label c26s001_MeeDate:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_bet_route from _call_mrS3_bet_route_2
        call mrS3_nor_route from _call_mrS3_nor_route_7
        if persistent.family:
            call mrS3_mar_route from _call_mrS3_mar_route_12
        call mrS3_emm_route from _call_mrS3_emm_route_13
        if emm._var("route"):
            $ Granddau = 1
        else:
            $ Granddau = 0
        call mrS3_eri_route from _call_mrS3_eri_route_7
        if eri._var("route"):
            $ Granddau = Granddau + 1
        if Granddau < 2:
            call mrS3_dap_route from _call_mrS3_dap_route_6
            if dap._var("route"):
                $ Granddau = Granddau + 1
        if Granddau < 2:
            call mrS3_eva_route from _call_mrS3_eva_route_10
            if eva._var("route"):
                $ Granddau = Granddau + 1
        if Granddau < 2:
            call mrS3_ama_route from _call_mrS3_ama_route_10
            if ama._var("route"):
                $ Granddau = Granddau + 1
        call mrS3_rels from _call_mrS3_rels_14
        call c25s007_MeeDate from _call_c25s007_MeeDate_1
    call BlinkXPS3 ("c26s001_005" , "d") from _call_BlinkXPS3_2455
    play music ("music/Acoustic-Inspirational.ogg")
    mc "¡Estás guapísima!"
    mee "Bueno, una chica tiene que arreglarse para una cita, ¿no? *Risita*"
    mc "Creía que no era una cita. O que decidirías luego si era una cita."
    call BlinkXPS3 ("c26s001_010" , "d") from _call_BlinkXPS3_2456
    mee "Bueno, pues una mujer tiene que arreglarse cuando va a cenar con su nieto."
    mee "Ya decidiremos luego si ha sido una cita o no."
    mc "Sea lo que sea, te aseguro que, en el restaurante, todos los clientes me van a mirar preguntándose cómo puedo ir con una mujer tan guapa."
    call BlinkXPS3 ("c26s001_015" , "d") from _call_BlinkXPS3_2457
    mee "No te va a mirar nadie preguntándose eso mientras cenamos. *Risa*"
    mc "¿Quieres apostar?"
    mee "Vale. ¿Qué quieres apostar?"
    mc "Si me miran al menos cinco clientes... y decides que es una cita... hoy duermes en mi habitación."
    mc "Aunque mi cama ha sufrido un pequeño accidente por culpa de un gato."
    call BlinkXPS3 ("c26s001_020" , "d") from _call_BlinkXPS3_2458
    mee "*Risa* Lo sé, me lo ha contado [nor]."
    mee "La apuesta me parece bien, pero ¿y si no te mira nadie?"
    mc "No sé. Decide tú."
    mee "Si no te mira nadie, tú duermes en la mía. Si decidimos que es una cita, claro. *Risita* Al menos la mía tiene una cama en buen estado."
    mc "Parece un buen plan. *Risa* Sea como sea, hoy dormiremos juntos. Si {b}decides{/b} que es una cita."
    call BlinkXPS3 ("c26s001_025" , "d") from _call_BlinkXPS3_2459
    mee "[mc]..."
    mc "¿Pasa algo, Meemaw?"
    call BlinkXPS3 ("c26s001_030" , "d") from _call_BlinkXPS3_2460
    mee "¿Podemos dejar de fingir que esto no es una cita?"
    mee "Hace días que decidí que lo sería, y me muero por besarte..."
    scene c26s001_030d with dissolve
    "No tienes que responder. Al menos no con palabras. Tus labios besan los de [mee] con dulzura."
    "Su cuerpo tiembla bajo tu tacto hasta que se separa reluctantemente de tus labios."
    call BlinkXPS3 ("c26s001_035" , "d") from _call_BlinkXPS3_2461
    mee "*Respirando pesadamente* Creo que como aperitivo hay suficiente."
    mc "Hay que dejar más besos para después de la cena, ¿no?"
    mc "Por cierto, ¿dónde vamos a ir?"
    scene c26s001_035d with dissolve
    mee "He alquilado un sitio en San Luis."
    mc "¿Alquilado? Querrás decir reservado, ¿no?"
    mee "Lo tendrás que descubrir cuando lleguemos."
    scene drive_afternoon with fade
    "[mee] introduce la dirección en el GPS. Llegaréis en unos 30 minutos."
    "Cuando faltan unos minutos para llegar, hace una llamada, indicando que estáis a menos de cinco minutos."
    "Parece que le dan unas indicaciones con las que te guía hasta una rotonda desde la que salen varios caminos empedrados que se adentran en el bosque."
    scene c26s001_035e with fade
    "Aparcas la camioneta en el lugar que te indica [mee] y camináis unos minutos por uno de los caminos rodeado de árboles."
    scene c26s001_035f with fade
    "Al girar por una de las curvas del camino, aparece una visión de cuento en medio de un claro en el bosque."
    call BlinkXPS3 ("c26s001_040" , "d") from _call_BlinkXPS3_2462
    mc "¡Wow, Meemaw! ¡Es precioso!"
    mee "¿Te gusta? No mucha gente conoce este sitio."
    mc "Es increíble. ¿Cómo es que tú lo conoces?"
    call BlinkXPS3 ("c26s001_045" , "d") from _call_BlinkXPS3_2463
    mee "Vendí estos terrenos unos años antes de que nacieras."
    mee "Iban a construir un hotel también, pero al final no lo hicieron y sólo construyeron el restaurante."
    mc "¿Dónde están los camareros? Si tienen que venir por el camino empedrado más les vale ir en patinete."
    call BlinkXPS3 ("c26s001_050" , "d") from _call_BlinkXPS3_2464
    mee "*Risa* Este sitio no funciona así, cariño. Pedí la comida cuando lo alquilé."
    mee "Lo han preparado todo en el gazebo cuando he llamado."
    mc "Pero..."
    call BlinkXPS3 ("c26s001_055" , "d") from _call_BlinkXPS3_2465
    mee "¿Qué tal si respondo a tus preguntas allí? *Risa* Parecemos dos idiotas en medio del bosque."
    mc "*Risa* Tienes razón. Te sigo."
    call BlinkXPS3 ("c26s001_060" , "f") from _call_BlinkXPS3_2466
    mee "¿Ves? Detrás tuyo tienes los cortes fríos y aquí la comida caliente."
    mc "Incluso tiene un sofá. Es un sitio genial. Muy romántico."
    call BlinkXPS3 ("c26s001_065" , "d") from _call_BlinkXPS3_2467
    mee "Nunca más vamos a tener una primera cita, con lo que quería que fuera especial."
    mc "Lo has conseguido. Es precioso."
    call BlinkXPS3 ("c26s001_070" , "d") from _call_BlinkXPS3_2468
    mee "Y, como puedes ver, ningún cliente te va a mirar preguntándose nada. *Risa*"
    mee "Hoy duermes en mi habitación."
    mc "*Risa* Eso es trampa. Tú sabías que habías ganado la apuesta antes de hacerla."
    call BlinkXPS3 ("c26s001_075" , "d") from _call_BlinkXPS3_2469
    mee "*Risa* Nunca apuestes a ciegas, cielo."
    mee "Además, no quieres que una pobre anciana duerma en un colchón en el suelo."
    mc "*Risa* En este caso, es una apuesta que no me importa perder."
    mee "Coge la comida que quieras. No sabía qué te apetecería y he pedido muchísima comida."
    scene c26s001_075d with dissolve
    "[mee] no miente. Hay comida para alimentar a la mitad de la familia. Especialmente si dentro de esa mitad no está Jamaal."
    call BlinkXPS3 ("c26s001_080" , "f") from _call_BlinkXPS3_2470
    mc "Tenías razón. Has pedido demasiada comida. ¡Pero si hay incluso bacon canadiense!"
    mee "*Risa* Ese es para mí. Ya sé que no te gusta, pero para mí es un placer culpable."
    mc "*Risa* ¿Qué va a ser lo siguiente? ¿Pizza con cosas raras?"
    call BlinkXPS3 ("c26s001_085" , "d") from _call_BlinkXPS3_2471
    mee "*Risa* No, eso se lo dejo a [bet]. Creo que si pones un bisonte entero encima de una base de pizza sería capaz de comérselo."
    mc "*Risa* Me lo creo."
    mc "Pero explícame la historia de este sitio. Parece un sitio muy especial."
    call BlinkXPS3 ("c26s001_090" , "d") from _call_BlinkXPS3_2472
    mee "Lo es. Querían construir un complejo de lujo para famosos que huyeran de L.A. Por eso los gazebos están escondidos, para darles intimidad."
    mee "Siempre pensé que estaba pensado para que pudieran venir aquí para escapar de los paparazzis."
    mc "Tiene lógica."
    call BlinkXPS3 ("c26s001_095" , "d") from _call_BlinkXPS3_2473
    if persistent.family:
        mee "Yo vendí los terrenos y tu abuelo hizo el proyecto del restaurante. Fue uno de sus últimos trabajos."
    else:
        mee "Yo vendí los terrenos y John hizo el proyecto del restaurante. Fue uno de sus últimos trabajos."
    mee "El hotel fue diseñado por un estudio de San Francisco. Una cosa muy lujosa. Y muy fea a mi parecer."
    mee "John no llegó a verlo completado, ni a saber que el hotel no se construiría."
    mc "Creo que no deberíamos haber venido a este sitio, Meemaw. Te debe traer recuerdos dolorosos."
    call BlinkXPS3 ("c26s001_100" , "d") from _call_BlinkXPS3_2474
    mee "Tan dolorosos como cualquier otro de sus edificios. Este no es más especial que otros."
    mee "Además, para mí es un sitio nuevo. No estaba acabado cuando John murió y nunca vine después."
    mc "Pero..."
    call BlinkXPS3 ("c26s001_105" , "d") from _call_BlinkXPS3_2475
    if persistent.family:
        mee "Cuando a tu abuelo le diagnosticaron el cáncer, me obligó a prometerle que reconstruiría mi vida sin él."
    else:
        mee "Cuando a John le diagnosticaron el cáncer, me obligó a prometerle que reconstruiría mi vida sin él."
    mee "He tardado 23 años. Y un sitio que diseñó él me parece un buen lugar para empezar."
    mc "No creo que hayas tardado 23 años. Has vivido una vida plena todos esos años."
    mc "Estar o no en una relación no debería ser la definición de reconstruir una vida."
    call BlinkXPS3 ("c26s001_110" , "d") from _call_BlinkXPS3_2476
    mee "Ah, OK. Entonces ya nos podemos ir. *Risa*"
    mc "Lo estoy diciendo en serio."
    call BlinkXPS3 ("c26s001_115" , "d") from _call_BlinkXPS3_2477
    mee "Yo también, [mc]. Hasta ahora había pensado que estaba viviendo una buena vida, pero estos últimos días..."
    mee "Me han hecho recuperar una ilusión que no recordaba, si es que alguna vez la he tenido."
    if persistent.family:
        mc "Con el abuelo la tendrías, ¿no?"
    else:
        mc "Con John la tendrías, ¿no?"
    call BlinkXPS3 ("c26s001_120" , "d") from _call_BlinkXPS3_2478
    mee "Era diferente. Todo se desarrolló muy rápido..."
    mee "[bet] me dijo que te explicó nuestra historia, con lo que ya lo sabes."
    call BlinkXPS3 ("c26s001_125" , "d") from _call_BlinkXPS3_2479
    mee "No había sentimiento de anticipación después del fin de semana en el que nos conocimos."
    if persistent.family:
        mee "Todo parecía evolucionar de forma natural. Conocernos, casarnos, tener hijos..."
    else:
        mee "Todo parecía evolucionar de forma natural. Conocernos, casarnos, tener a [nor]..."
    mc "Y lo que está pasando ahora es diferente, ¿no?"
    call BlinkXPS3 ("c26s001_130" , "d") from _call_BlinkXPS3_2480
    mee "Lo es. Es muy diferente. No vamos a tener hijos. No creo que los quisiera a mi edad aunque pudiera."
    if persistent.family:
        mee "Te conozco desde que naciste. ¡Mierda, era más mayor cuando naciste que tu madre ahora!"
    else:
        mee "Te conozco desde que naciste. ¡Mierda, era más mayor cuando naciste que [mar] ahora!"
    mc "Tenías la edad de [nor]..."
    call BlinkXPS3 ("c26s001_135" , "d") from _call_BlinkXPS3_2481
    mee "Sí. Exactamente la misma edad que [nor] tiene ahora."
    mee "Y no es... natural... que tú y yo estemos juntos."
    call BlinkXPS3 ("c26s001_140" , "d") from _call_BlinkXPS3_2482
    mee "Aunque no renunciaría a ello por nada ni por nadie. Me da lo mismo lo que puedan pensar los demás."
    mc "Yo tampoco renunciaría a esto."
    call BlinkXPS3 ("c26s001_145" , "d") from _call_BlinkXPS3_2483
    mee "*Risa* ¿Aunque me guste el bacon canadiense?"
    mc "*Risa* Aunque te guste el bacon canadiense."
    call BlinkXPS3 ("c26s001_150" , "d") from _call_BlinkXPS3_2484
    mee "Pero hablando en serio, me encanta lo que ha pasado entre nosotros en los últimos días."
    mee "Me encanta no saber qué va a pasar la siguiente vez que estemos juntos. Me encanta ese sentimiento de anticipación."
    mc "Pasará lo que queramos que pase. No hay nadie poniendo límites."
    call BlinkXPS3 ("c26s001_155" , "d") from _call_BlinkXPS3_2485
    mee "*Risa* Sí que lo hay. Yo. No quiero descubrir todo lo que somos capaces de hacer en nuestra primera noche."
    mee "No quiero que ese sentimiento de anticipación desaparezca."
    mc "No tiene por qué desaparecer. Siempre podemos inventar cosas nuevas que hacer."
    if mee._var("iceCream"):
        mc "Por ejemplo, helado. Estaba bueno."
        call BlinkXPS3 ("c26s001_160" , "d") from _call_BlinkXPS3_2486
        mee "¿Ya lo has probado?"
        mc "Justo antes de ir a buscarte. Era tentador."
        mee "¿Qué te ha parecido? ¿Te ha gustado? Esperaba ser la primera en hacerlo."
        mc "Estaba bueno. No he notado mucha diferencia con el helado normal."
        mc "Pero volviendo al sentimiento de anticipación..."
    call BlinkXPS3 ("c26s001_165" , "d") from _call_BlinkXPS3_2487
    mee "¿Qué crees que pasará esta noche?"
    mc "¡Qué directa! *Risa*"
    mc "Creo que vamos a seguir disfrutando de una bonita cena."
    call BlinkXPS3 ("c26s001_170" , "d") from _call_BlinkXPS3_2488
    mee "¡No me refiero a eso! *Risa* Sabes a lo que me refiero."
    mc "¿Te refieres a cuando me quede a dormir en tu habitación?"
    mc "Pues que tendré que ir a por un pijama a la mía primero."
    call BlinkXPS3 ("c26s001_175" , "d") from _call_BlinkXPS3_2489
    mee "Había oído que dormías desnudo..."
    mc "Por norma sí, pero no sé si querrás que lo haga."
    mee "Por mí no hace falta que duermas con más ropa de la que sueles usar."
    mc "¿Y tú? ¿Cómo duermes?"
    call BlinkXPS3 ("c26s001_180" , "d") from _call_BlinkXPS3_2490
    mee "Por norma con un pijama. Pero hoy... esperaba que me dieras calor suficiente como para no necesitarlo."
    mc "Me siento un hombre objeto usado como si fuera una mera bolsa de agua caliente. *Risa*"
    mc "Pero me parece una buena idea. No vamos a ver nada que no hayamos visto con anterioridad."
    mc "¿Lado derecho o izquierdo de la cama?"
    call BlinkXPS3 ("c26s001_185" , "d") from _call_BlinkXPS3_2491
    mee "Derecho. Y no pienso ceder sobre eso, al menos en mi cama."
    mc "*Risa* No hace falta que cedas. Yo duermo en el centro o en la izquierda."
    mc "Nuestra primera discusión como pareja no va a ser sobre el lado de la cama en el que dormimos."
    call BlinkXPS3 ("c26s001_190" , "d") from _call_BlinkXPS3_2492
    mee "Pero sabes que llegará tarde o temprano, ¿verdad? Un día discutiremos."
    mc "Estoy seguro de que lo hará, pero ese puente habrá que cruzarlo en su momento. No es necesario pensar en ese puente cuando ni siquiera sabemos que río atraviesa."
    if persistent.family:
        mee "Tienes razón. Me preocupo demasiado, pero es que no he estado con nadie desde tu abuelo..."
    else:
        mee "Tienes razón. Me preocupo demasiado, pero es que no he estado con nadie desde John..."
    mc "Si te sirve de algo, Tía [bet] dijo que me parecía mucho a él. A lo mejor las discusiones son parecidas."
    call BlinkXPS3 ("c26s001_195" , "d") from _call_BlinkXPS3_2493
    mee "*Risa* Te pareces a él en algunas cosas, pero hay más diferencias que similitudes."
    mc "¿Por ejemplo?"
    call BlinkXPS3 ("c26s001_200" , "d") from _call_BlinkXPS3_2494
    mee "Tu eres más directo y asertivo cuando quieres algo. Él le daba vueltas y más vueltas hasta que ya no recordabas de quién había sido la idea original."
    mc "Bueno, creo que los rodeos innecesarios son... innecesarios."
    call BlinkXPS3 ("c26s001_205" , "d") from _call_BlinkXPS3_2495
    mee "Después está vuestro concepto de familia. Es muy diferente."
    mc "Tía [bet] me dijo lo contrario, que los dos aceptábamos a todo el mundo en la familia."
    mee "Ahí está la diferencia. Tú aceptas a todo el mundo en la familia."
    mee "El daba la bienvenida a todo el mundo a {b}nuestra{/b} familia. Nosotros siempre íbamos a ser el centro de esa familia extendida."
    mee "Quien quisiera unirse debía adaptarse a nosotros. Tú permites que cada cual siga siendo como es."
    mc "Es que la familia no es mía. Es de todos. Los de siempre y los nuevos."
    call BlinkXPS3 ("c26s001_210" , "d") from _call_BlinkXPS3_2496
    mee "¿Puedes ver la diferencia? Tú no quieres ser el centro de la familia ni imponer normas."
    mee "Para él, la familia era nuestra, suya y mía."
    if persistent.family:
        mee "Y de nuestros hijos más tarde."
    else:
        mee "Y de [nor] más tarde."
    mee "Pero si alguien más quería ser parte de la familia, lo tenía que hacer bajo nuestras condiciones."
    mc "Supongo que son otros tiempos y el concepto de familia ha cambiado. No hay que juzgarle en base a nuestros valores actuales."
    call BlinkXPS3 ("c26s001_215" , "d") from _call_BlinkXPS3_2497
    mee "No le estoy juzgando, [mc]. Sólo digo que es un aspecto importante en el que sois diferentes. Ni mejores ni peores."
    mee "Como has dicho, eran otros tiempos. El poliamor o los harenes eran cosas... raras."
    if mc._var("relationships")>1:
        mc "¿Cómo te sientes al formar parte de un harén? Supongo que no debe de ser fácil para ti."
        call BlinkXPS3 ("c26s001_220" , "d") from _call_BlinkXPS3_2498
        mee "No he pensado mucho en ello. Siempre me había parecido algo... tercermundista... con un macho dominante y unas mujeres sumisas, quizás contra su voluntad."
        mee "Yo también soy de otros tiempos..."
        mee "Pero lo que tú has construido no tiene nada que ver con eso. Se ha creado de una forma natural. Lo has hecho muy bien."
        mc "Gracias, pero supongo que hay un 'pero'."
        if emm._var("route"):
            $ Granddau = 1
        else:
            $ Granddau = 1
        if eri._var("route"):
            $ Granddau = Granddau + 1
        if dap._var("route"):
            $ Granddau = Granddau + 1
        if eva._var("route"):
            $ Granddau = Granddau + 1
        if ama._var("route"):
            $ Granddau = Granddau + 1
        $ GranddauRel = False
        if persistent.family and not nor._var("route") and not mar._var("route"):
            if Granddau > 0:
                $ GranddauRel = True
        elif not persistent.family and not nor._var("route"):
            if Granddau > 0:
                $ GranddauRel = True
        $ ShareFam = False
        call BlinkXPS3 ("c26s001_225" , "d") from _call_BlinkXPS3_2499
        if bet._var("route"):
            $ ShareFam = True
            mee "*Risa* Se me hace extraño compartir hombre con mi hermana."
            if persistent.family:
                if nor._var("route") and mar._var("route"):
                    mee "O con mis hijas..."
                elif nor._var("route") or mar._var("route"):
                    mee "O con una de mis hijas..."
            else:
                if nor._var("route"):
                    mee "O con mi hija..."
            if Granddau > 1:
                mee "O con mis nietas..."
            elif Granddau == 1:
                mee "O con una de mis nietas..."
        elif nor._var("route") or mar._var("route"):
            if persistent.family:
                $ ShareFam = True
                if nor._var("route") and mar._var("route"):
                    mee "*Risa* Se me hace extraño compartir hombre con mis hijas."
                elif nor._var("route") or mar._var("route"):
                    mee "*Risa* Se me hace extraño compartir hombre con una de mis hijas."
                if Granddau > 1:
                    mee "O con mis nietas..."
                elif Granddau == 1:
                    mee "O con una de mis nietas..."
            elif nor._var("route"):
                $ ShareFam = True
                mee "*Risa* Se me hace extraño compartir hombre con mi hija."
                if Granddau > 1:
                    mee "O con mis nietas..."
                elif Granddau == 1:
                    mee "O con una de mis nietas..."
        elif GranddauRel:
            $ ShareFam = True
            if Granddau > 1:
                mee "*Risa* Se me hace extraño compartir hombre con mis nietas."
            else:
                mee "*Risa* Se me hace extraño compartir hombre con una de mis nietas."
        else:
            mee "*Risa* No, no hay ningún 'pero'. Es raro compartirte con otras mujeres, pero estoy contenta de hacerlo."
        if ShareFam:
            mee "Pero estoy contenta de hacerlo."
            mc "*Risa* Creo que te acostumbrarás muy rápido."
        mc "Especialmente en cuanto les comuniques a todas que formas parte del harén."
        call BlinkXPS3 ("c26s001_230" , "d") from _call_BlinkXPS3_2500
        mee "Eso es lo que más me asusta."
    else:
        call BlinkXPS3 ("c26s001_230" , "d") from _call_BlinkXPS3_2501
        mee "Y ahora le tengo que comunicar al resto de chicas que estamos juntos. Eso es lo que más me asusta."
    mc "¿Asustarte? ¿Por qué?"
    call BlinkXPS3 ("c26s001_235" , "d") from _call_BlinkXPS3_2502
    mee "No reaccioné muy bien aquella vez con los besos en la cocina. Voy a parecer una hipócrita si me acuesto contigo."
    mee "No 'si'... Cuando me acueste contigo y se lo diga a todas ellas."
    mc "¿Sabes lo mejor de esta familia? Nadie juzga a nadie. No te tienes que preocupar más allá de que te gasten alguna broma sobre tu cambio de opinión."
    call BlinkXPS3 ("c26s001_240" , "d") from _call_BlinkXPS3_2503
    mee "*Risa* Supongo que tienes razón. Aunque en el grupo de WhatsUp de las chicas hay un montón de mensajes juzgando, aunque disfrazados de broma."
    mee "Es una buena forma de decirle a alguna de las chicas lo que debería pulir sin que nadie se sienta ofendido."
    mc "A veces me alegro de no estar en ese grupo. Lo pasaría mal con las 22 mujeres y Jamaal criticándome, aunque fuera medio en broma."
    call BlinkXPS3 ("c26s001_245" , "d") from _call_BlinkXPS3_2504
    mee "No lo harías. Siempre que alguien ha comentado algo que deberías cambiar, alguna de 'Las Bestias' han salido en tu defensa."
    if mc._var("relationships")>2:
        mee "Alguna te defendía incluso antes de salir contigo."
    mc "*Risa* ¿Las Bestias? ¿Quiénes son? ¿Qué decís que debería cambiar?"
    call BlinkXPS3 ("c26s001_250" , "d") from _call_BlinkXPS3_2505
    mee "No creo que te convenga saberlo. Además, son cosas entre nosotras. Nada serio. Si hay algún problema serio, lo hablamos en persona."
    mee "Tenga que ver contigo o no."
    mc "¿Y tú? ¿Crees que debería cambiar algo de cómo soy?"
    call BlinkXPS3 ("c26s001_255" , "d") from _call_BlinkXPS3_2506
    mee "*Risa* Eso es una pregunta trampa. Si digo que no, pensarás que eres perfecto, y no lo eres."
    mee "Si digo que sí, empezarás a justificar el porqué de hacer las cosas así."
    mee "Si tienes que cambiar algo, ya lo descubrirás por ti mismo."
    stop music fadeout (1.5)
    mc "Eso no resuelve ninguna de mis dudas."
    play sound ("music/thunder.ogg")
    "Suena un trueno a lo lejos."
    call BlinkXPS3 ("c26s001_260" , "d") from _call_BlinkXPS3_2507
    mee "Creo que va a llover. Deberíamos volver a casa."
    mc "Estoy de acuerdo. Además, no has pedido postre."
    mc "Aunque esperaba poder sentarnos en el sofá un rato. Pero entonces nos va a pillar la lluvia."
    call BlinkXPS3 ("c26s001_265" , "d") from _call_BlinkXPS3_2508
    mee "Bueno, sobre el postre... esperaba que lo fueras tú. *Risita*"
    mc "Me parece una idea estupenda. Yo esperaba que lo fueras tú."
    mc "¿Volvemos a casa?"
    mee "Vamos."
    scene c26s001_270An with dissolve
    play sound ("music/thunder.ogg")
    "Antes de abandonar el gazebo, giras a [mee] y le das un apasionado beso. Un aperitivo de lo que está por llegar."
    "Los segundos se convierten en minutos hasta que el tiempo pierde todo el sentido."
    call BlinkXPS3 ("c26s001_275a" , "d") from _call_BlinkXPS3_2509
    mee "Deberíamos irnos antes de que te tenga que tumbar en ese sofá y hacer cosas que no deberíamos hacer en un restaurante."
    mc "*Risa* Bueno, a un restaurante se viene a comer, ¿no? Es tentador 'comerte' en ese sofá."
    call BlinkXPS3 ("c26s001_275b" , "d") from _call_BlinkXPS3_2510
    mee "*Risa* Aunque estén aislados, sigo pensando que no es la mejor idea. No sé si los gemidos se escucharán desde las cocinas. O atraerán a algún jabalí."
    mee "Vámonos antes de que me corrompas más de lo necesario."
    scene drive_night_rain
    play music ("music/heavy-rain.ogg")
    "A medio camino a casa el cielo parece abrirse y deja caer todo su contenido sobre vosotros en forma de una intensa lluvia."
    "Es casi una metáfora de lo que está por venir durante el resto de la noche."
    call BlinkXPS3 ("c26s001_280" , "d") from _call_BlinkXPS3_2511
    "Al llegar a casa sigue lloviendo a cántaros."
    mc "¿Quieres que vaya a por un paraguas?"
    mee "No hace falta. Aparca el coche delante del camino de tablones y solo tendré que correr unas yardas."
    mc "¿Vas a anotar un touchdown?"
    mee "*Risa* No, eso lo harás tú luego."
    scene c26s001_285An with fade
    "Nada más aparcar, [mee] sale corriendo, casi desapareciendo en la intensa lluvia."
    scene c26s001_290An with dissolve
    "La sigues unos segundos después, para encontrártela empapada, refugiada al lado de la puerta."
    call BlinkXPS3 ("c26s001_295" , "d") from _call_BlinkXPS3_2512
    mc "Sólo han sido unas yardas, pero lo suficiente como para que te hayas empapado."
    mee "Correr no sirve de mucho en la lluvia. *Risa* Y correr con tacones no es fácil."
    mee "Tú también te has empapado. Ni siquiera has intentado correr."
    mc "¿Para qué? Con lo que está lloviendo, lo único que podría conseguir es resbalar y caerme."
    mc "Además, así tenemos una excusa para quitarnos la ropa en seguida. *Risa*"
    call BlinkXPS3 ("c26s001_300" , "d") from _call_BlinkXPS3_2513
    mee "*Risa* Me gusta cómo piensas, [mc]. Vamos a mi habitación."
    mc "Después de ti, Meemaw."
    stop music fadeout (1.5)
    return
label c26s001_NoMee:
    scene c26s001_1000 with fade
    "Vas a tu habitación a jugar un rato a My Residence."
    "Tienes una romántica cita con Nana, la matriarca de la familia alien, que es interrumpida por la lluvia."
    "Mientras estás jugando esa escena, suena un trueno a lo lejos y empieza a llover en Newport."
    return
label c26s001_MeeSex:
    if _in_replay:
        $ mc._var("relationships", 1, "set")
        call mrS3_rels from _call_MRS3_rels
        if mc._var("relationships")>1:
            menu:
                "¿Estás en una relación con [mar], [nor], [bet], [eri], [emm], o [dap]?"
                "Sí":
                    $ bet._var("route", True)
                "No":
                    $ bet._var("route", False)
                    $ mar._var("route", False)
                    $ nor._var("route", False)
                    $ eri._var("route", False)
                    $ emm._var("route", False)
                    $ dap._var("route", False)
                    menu:
                        "¿Estás en una relación con [sai], [sca], [eil], [sam], [sim], [oma], [eva], [mad.nick], [meg], o [kia]?"
                        "Sí":
                            $ kia._var("route", True)
                        "No":
                            $ oma._var("route", False)
                            $ eil._var("route", False)
                            $ sai._var("route", False)
                            $ sca._var("route", False)
                            $ sam._var("route", False)
                            $ sim._var("route", False)
                            $ eva._var("route", False)
                            $ mad._var("route", False)
                            $ meg._var("route", False)
                            $ kia._var("route", False)
        else:
            $ bet._var("route", False)
            $ mar._var("route", False)
            $ nor._var("route", False)
            $ eri._var("route", False)
            $ emm._var("route", False)
            $ dap._var("route", False)
            $ oma._var("route", False)
            $ eil._var("route", False)
            $ sai._var("route", False)
            $ sca._var("route", False)
            $ sam._var("route", False)
            $ sim._var("route", False)
            $ eva._var("route", False)
            $ mad._var("route", False)
            $ meg._var("route", False)
            $ kia._var("route", False)
    call BlinkXPS3 ("c26s001_305" , "f") from _call_BlinkXPS3_2514
    "En la habitación de [mee]..."
    play music ("music/Higher-Instrumental.ogg")
    mee "Voy a buscar unas toallas para que te puedas secar. Puedes ir quitándote la ropa mojada si quieres."
    mc "Sí, por favor, trae un par de toallas. Estoy más mojado de lo que creía."
    call BlinkXPS3 ("c26s001_310" , "d") from _call_BlinkXPS3_2515
    mee "Yo también. *Risita* Pero no tiene nada que ver con la lluvia."
    mc "¿Ya?"
    scene c26s001_310d with dissolve
    mee "Desde la cena... Me haces pensar en cosas en las que no debería pensar mientras estoy comiendo."
    mc "*Risa* Aún queda el postre..."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_315wm" , "f") from _call_BlinkXPS3_2516
    else:
        call BlinkXPS3 ("c26s001_315nm" , "f") from _call_BlinkXPS3_2517
    "Unos minutos después..."
    mee "¡Esperaba que estuvieras tapado en la cama! ¡Vas a coger frío!"
    mc "No te preocupes, me he secado bien. Y una lluvia de verano no va a hacerme coger frío. Tu pelo mojado, sin embargo..."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_320wm" , "d") from _call_BlinkXPS3_2518
    else:
        call BlinkXPS3 ("c26s001_320nm" , "d") from _call_BlinkXPS3_2519
    mee "No voy a esperar a que se seque, ni a pasarme media hora en el baño con el secador."
    mee "¡Quiero mi postre!"
    mc "Entonces ven aquí."
    if persistent.lactation:
        scene c26s001_320wmd with dissolve
        mc "Veo que el mío ya está preparado."
        mee "Llevo un rato pensando en lo que vamos a hacer y... ya sabes lo que me pasa..."
        scene c26s001_325awm with dissolve
    else:
        scene c26s001_325anm with dissolve
    stop music fadeout (1.5)
    "[mee] se sienta a horcajadas encima de tus piernas y empieza a besarte con pasión e impaciencia."
    play music ("music/SensualJazzMedium2.ogg")
    if persistent.lactation:
        "Puedes notar el calor que emana de su entrepierna encima de Mjolnir y como sus húmedos pezones rozan sobre tu pecho."
    else:
        "Puedes notar el calor que emana de su entrepierna encima de Mjolnir."
    scene c26s001_325b with dissolve
    "Los besos continúan, en una lucha por saber quién besa más apasionadamente."
    "A ninguno de los dos os importa. Ni siquiera sabéis que estáis luchando por ello."
    scene c26s001_325c with dissolve
    "Cambiáis de posición diversas veces, dejándote guiar por la diminuta mujer."
    "Vuestras manos recorren vuestros cuerpos en caricias que acompañan a los besos."
    scene c26s001_325d with dissolve
    "Mjolnir, en perfecto orden de batalla, queda aprisionado entre vuestros cuerpos, masajeado por vuestros estómagos."
    "La respiración de [mee] se va acelerando más y más con cada nuevo beso y cada cambio de posición."
    call BlinkXPS3 ("c26s001_330" , "d") from _call_BlinkXPS3_2520
    mee "*Respiración entrecortada* Quédate así. Quiero mi postre antes de que no pueda retenerme más."
    mc "Y yo quiero el mío."
    call BlinkXPS3 ("c26s001_335" , "d") from _call_BlinkXPS3_2521
    mee "*Risa* Por suerte, alguien inventó una posición para eso."
    mc "*Risa* Le tenemos que estar agradecidos, aunque fuera un obseso de los números."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_340wm" , "f") from _call_BlinkXPS3_2522
    else:
        call BlinkXPS3 ("c26s001_340nm" , "f") from _call_BlinkXPS3_2523
    mee "Llevo deseando esto desde que hemos salido del restaurante."
    mc "¿Sólo desde entonces? *Risa* Yo llevo deseándolo desde antes de salir de casa."
    if persistent.lactation:
        mc "Y espero que ese reguero que sale de tus pechos se convierta en una catarata en breve."
        mc "Recuerda lo que me decías cuando era pequeño. Un vaso caliente de leche por la noche es bueno. *Risa* Y es mejor sin vaso, directamente del envase."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_345wm" , "d") from _call_BlinkXPS3_2524
    else:
        call BlinkXPS3 ("c26s001_345nm" , "d") from _call_BlinkXPS3_2525
    mee "En ningún momento he dudado sobre que fuera a pasar, pero sigo teniendo ganas de mi postre."
    scene c26s001_900-pv with dissolve
    show c26s001_900v
    "Sin dejarte responder, [mee] se introduce a Mjolnir en su boca y empieza una profunda mamada."
    if persistent.family:
        "No puedes dejar que tu abuela sea la única que disfruta de su postre. Empiezas a saborear el tuyo."
    else:
        "No puedes dejar que la preciosa mujer de pelo gris sea la única que disfruta de su postre. Empiezas a saborear el tuyo."
    mee "*Gemido*"
    "Las habilidades de [mee] con su boca son sorprendentes, pese a haberlas disfrutado con anterioridad."
    "Sus habilidades, la anticipación y los roces durante la sesión de besos hacen que tu orgasmo se acerque rápidamente."
    mee "*Jadeo*"
    scene c26s001_910-b-pv with dissolve
    show c26s001_910v
    hide c26s001_900v
    "Su coño está tan mojado como si una tormenta la hubiera empapado y no le hubieras dado tiempo de secarse."
    mee "*GEMIDO*"
    "Tu orgasmo no es el único que se acerca. Ella también ha estado anticipando este momento durante toda la cena y ahora su cuerpo reacciona a cada uno de tus lametones."
    "Guiándola inexorablemente al que será el primer orgasmo de la noche."
    mee "*JADEO*"
    "Su culo se tensa bajo tus dedos, anunciando que no vas a ser el primero en correrte."
    if persistent.lactation:
        call OrgasmXS3 ("c26s001_350wm") from _call_OrgasmXS3_58
    else:
        call OrgasmXS3 ("c26s001_350nm") from _call_OrgasmXS3_59
    mee "*GEMIDO* ¡SÍ! *JADEO*"
    if persistent.lactation:
        "Una explosión de sabores llena tu boca, mientras notas cómo la leche que brota de sus pechos se vuelve más caliente."
        "No es tanta cantidad como en otras ocasiones, pero lo suficiente como para notar un cambio de temperatura con la llegada de leche nueva."
    else:
        "Una explosión de sabores llena tu boca mientras el cuerpo de la madura mujer se tensa espasmódicamente."
    mee "*JADEO*"
    "Se vuelve a meter tu polla en la boca para continuar su antológica mamada. Esta mujer quiere su postre y no va a parar hasta conseguirlo."
    if persistent.lactation:
        scene c26s001_905-wm-pv with dissolve
        show c26s001_905wmv
        hide c26s001_910v
    else:
        scene c26s001_905-nm-pv with dissolve
        show c26s001_905nmv
        hide c26s001_910v
    "De alguna forma desconocida, consigue que la reverberación de sus gemidos con tu polla en su boca te provoquen aún más placer."
    mee "*GEMIDO*"
    "No vas a poder aguantar mucho más, pero sigues lamiendo pese a todo, buscando alargar el placer de su primer orgasmo mientras el tuyo se acerca irremediablemente."
    mc "*Slurp* Estoy a punto de correrme, Meemaw."
    mee "*JADEO*"
    "Ella continúa con su excelso trabajo bucal como si no te hubiera oído, o como si no le importara recibir en su boca la descarga que preparas."
    "Quiere su postre y no va a dejar escapar ni una gota. O al menos lo va a intentar."
    call OrgasmXS3 ("c26s001_355") from _call_OrgasmXS3_60
    mc "¡Mpfft!"
    "Sin poder contener más tu clímax, liberas en su boca una gran cantidad de semen producida por la larga anticipación."
    mee "*JADEO*"
    "Supones que la pequeña mujer no puede retener todo el líquido en el interior de su pequeña boca."
    if persistent.lactation:
        scene c26s001_355wmd with dissolve
    else:
        scene c26s001_355nmd with dissolve
    "Una vez acaba tu descarga, lo remedia lamiendo cada gota que se le ha escapado."
    "Pasa su lengua por cada insospechado lugar en el que puede provocar una nueva oleada de placer."
    mee "*Gemido* Mmmm... *Slurp* Delicioso postre."
    mc "*Risa* El mío también ha sido increíble."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_360wm" , "f") from _call_BlinkXPS3_2526
        hide c26s001_905wmv
    else:
        call BlinkXPS3 ("c26s001_360nm" , "f") from _call_BlinkXPS3_2527
        hide c26s001_905nmv
    "Se sienta a horcajadas sobre tu estómago, dejándote notar el calor que sigue emanando de su coño."
    mee "Eso ha sido mucho más rápido de lo que esperaba. Tanto por tu parte como por la mía."
    mc "La anticipación está bien, pero tiene estos efectos indeseados."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_365wm" , "d") from _call_BlinkXPS3_2528
    else:
        call BlinkXPS3 ("c26s001_365nm" , "d") from _call_BlinkXPS3_2529
    mee "¿Indeseados? Ha sido todo lo que podía desear para la primera parte de la noche."
    mee "Ahora tan solo tenemos que esperar a que estés listo otra vez."
    "Notas cómo Mjolnir se declara en huelga, pidiendo un descanso tras la intensa corrida."
    mc "No hay por qué esperar. Hay muchas cosas más que podemos hacer. *Risa* No soy solo un hombre a una polla pegado." id c26s001_MeeSex_9d8ca839
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_370wm" , "d") from _call_BlinkXPS3_2530
    else:
        call BlinkXPS3 ("c26s001_370nm" , "d") from _call_BlinkXPS3_2531
    if mc._var("relationships")>1:
        mee "*Risa* ¿Qué me puedes ofrecer en el pack de bienvenida al harén?"
    else:
        mee "*Risa* ¿Qué me puedes ofrecer en el pack de bienvenida a una relación oficial?"
    if persistent.lactation:
        scene c26s001_375a with dissolve
        if persistent.family:
            "Te sientas como si no tuvieras el peso de tu ligera abuela encima de tu estómago, haciendo que resbale hasta tus piernas."
        else:
            "Te sientas como si no tuvieras el peso de la ligera mujer encima de tu estómago, haciendo que resbale hasta tus piernas."
        mc "Esto, por ejemplo."
        scene c26s001_375b with dissolve
        "Un caliente brote de leche llena tu boca en cuanto tus labios rodean el pezón de [mee]. Parece que ese chorro de leche ha esperado a tener un destino antes de salir."
        mee "*Gemido* Parece que la he estado guardando para ti."
        "Nunca has estado tan contento de tener tu ración de leche caliente antes de acostarte."
        mc "*Slurp*"
        "Claro, nunca la has tomado directamente de la productora. Ni siquiera en tu mente puedes pensar en [mee] como en la vaca."
        scene c26s001_375c with dissolve
        if persistent.family:
            "Mientras sigues bebiendo, llevas una mano a la entrepierna de tu abuela, buscando su clítoris."
        else:
            "Mientras sigues bebiendo, llevas una mano a la entrepierna de la pequeña mujer, buscando su clítoris."
        mee "*Jadeo* ¿No me vas a dejar descansar ni un momento?"
        "Si pensaba que iba a ser una noche relajada, no podía estar más equivocada. Ella ha empezado con fuerza y es el momento de que tú continúes."
        mc "*Slurp negativo*"
        "Otro borbotón de leche llena tus labios. Intentas no dejar escapar ni una gota del pezón que tienes aprisionado, aunque no puedes hacer lo mismo con el otro."
        scene c26s001_375d with dissolve
        "[mee] te deja beber el caliente fluido que sale de sus pechos mientras añade gemidos a tus sonidos de succión."
        mee "*Gemido* Chupas más fuerte que [nor], y hay que tener en cuenta que ella era una tragona."
        "Por un momento te imaginas a la [nor] adulta mamando la leche de su madre. Ignoras el pensamiento. Esta leche es sólo tuya ahora."
        mee "*Jadeo* Estoy muy sensible... Si sigues así no voy a poder dejar de correrme..."
        "Suena como un buen plan. Aumentas la presión que tu dedo hace sobre su botón del placer y la velocidad de succión."
        scene c26s001_375e with dissolve
        if persistent.family:
            "Los jadeos de tu abuela suben de volumen mientras su cuerpo se tensa ante tu intensificado ataque a sus zonas más erógenas."
        else:
            "Los jadeos de [mee] suben de volumen mientras su cuerpo se tensa ante tu intensificado ataque a sus zonas más erógenas."
        mee "*GEMIDO*"
        "Otro borbotón de caliente leche llega a tu boca. Una serie de micro orgasmos empieza a recorrer el cuerpo de la hermosa mujer."
        mee "*JADEO*"
        "Ella ya no puede añadir palabras a su lenguaje corporal, pero no es necesario. Sabes que una gran explosión se está preparando."
        call OrgasmXS3 ("c26s001_380") from _call_OrgasmXS3_61
        mee "{size=+25}*GEMIDO*{/size}"
        "Y la explosión llega. Arriba y abajo. Tu boca se llena de sabores. Tus dedos se empapan en sus fluidos."
        mee "{size=+25}*JADEO*{/size}"
        "Su cuerpo se vuelve a tensar hasta casi romperse antes de liberar toda la tensión."
        scene c26s001_375f with dissolve
        "La mujer de pelo gris se derrumba sobre tu hombro un segundo después. El suministro de leche ha desaparecido como por arte de magia."
        mee "*Respiración entrecortada* Esto es adictivo..."
        "Lo sabes. Podrías estar haciendo esto durante horas."
        if persistent.family:
            "Tu abuela tiene un cuerpo que agradece cada caricia llegando al clímax rápidamente."
        else:
            "[mee] tiene un cuerpo que agradece cada caricia llegando al clímax rápidamente."
        mee "*Respiración entrecortada* Y cada vez quiero más..."
        mc "*Risa* Te estás volviendo codiciosa. Daré por hecho que te ha gustado."
        call BlinkXPS3 ("c26s001_385" , "d") from _call_BlinkXPS3_2532
        mee "¿Gustarme? ¡Me ha encantado! Incluso más que las veces anteriores."
        mc "*Risa* La anticipación..."
        call BlinkXPS3 ("c26s001_390" , "d") from _call_BlinkXPS3_2533
        mee "Exacto. Pero ahora no puedo parar. Túmbate. Quiero esa lengua dónde pertenece."
        mc "Como desees."
        mee "Pero antes..."
        scene c26s001_390d with dissolve
        "Te da un apasionado y agresivo beso en el que su lengua recorre el interior de tu boca en vez de sólo buscar la tuya."
        "Es un beso largo, potente."
        "A los pocos segundos, la mujer empieza a jadear en tu boca."
        call BlinkXPS3 ("c26s001_395" , "d") from _call_BlinkXPS3_2534
        mee "Probar mi leche de tus labios me pone cachonda. Aún más cachonda."
        mc "Entonces no dejemos que ese sentimiento se pierda. Me has dicho que me tumbe, ¿no?"
    else:
        mc "Lo que tú quieras. *Risa* Hoy estamos de oferta especial."
        call BlinkXPS3 ("c26s001_400" , "d") from _call_BlinkXPS3_2535
        mee "Entonces quédate en esa posición. Necesito que tu lengua vuelva a donde pertenece."
        mc "Como desees. *Risa* Pero, ¿no te estás volviendo codiciosa?"
        call BlinkXPS3 ("c26s001_405" , "d") from _call_BlinkXPS3_2536
        mee "*Risa* Sí. Es culpa tuya. Y no es codicia. Es adicción."
        mc "*Risa* Si es culpa mía, tendré que ponerle solución."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_410wm" , "d") from _call_BlinkXPS3_2537
        "Tras tumbarte, se sienta sobre tu pecho."
    else:
        call BlinkXPS3 ("c26s001_410nm" , "f") from _call_BlinkXPS3_2538
    mee "No quiero ser egoísta... Si quieres descansar..."
    mc "No necesito descansar, no te preocupes. Si para ti es adictivo, notar tu sabor en mi boca también lo es para mí."
    if persistent.lactation:
        scene c26s001_915-wm-pv
        show c26s001_915wmv
    else:
        scene c26s001_915-nm-pv
        show c26s001_915nmv
    if persistent.family:
        "Tu abuela avanza su pelvis lo justo para que puedas llegar a su chorreante coño."
    else:
        "[mee] avanza su pelvis lo justo para que puedas llegar a su chorreante coño."
    "No dudas ni un instante sobre qué hacer y pones tu lengua a trabajar, percibiendo el acre sabor de orgasmos anteriores."
    mee "*Gemido* ¡Eres increíble! *Jadeo* ¡Esto es lo mejor del mundo! *Gemido*"
    "Esperas que cambie de opinión cuando llegue el plato principal. Empezar por los postres está muy bien, pero no es nada que no hayáis hecho antes."
    mee "*Jadeo* ¡Me encanta! *Gemido* ¡Llegan uno tras otro! *Jadeo*"
    if persistent.lactation:
        "Los micro orgasmos de [mee] aparecen en rápida sucesión, cada uno de ellos aumentando el reguero de leche que baja por sus pechos."
    else:
        "Los micro orgasmos de [mee] aparecen en rápida sucesión."
    if persistent.lactation:
        scene c26s001_920-wm-pv
        show c26s001_920wmv
        hide c26s001_915wmv
    else:
        scene c26s001_920-nm-pv
        show c26s001_920nmv
        hide c26s001_915nmv
    "Su cuerpo es recorrido por espasmos producidos por la catarata de orgasmos, haciendo que sus movimientos sean casi epilépticos."
    mee "*Jadeo* ¡No había tenido tantos orgasmos nunca! *Jadeo*"
    "Dijo lo mismo la última vez, en la ducha. Supones que, ahora que por fin se ha dejado ir, no hay ninguna barrera mental que la retenga."
    mee "*Gemido* No sé si me va a quedar resistencia para cuando te recuperes. *Gemido*"
    "Su comentario te sorprende hasta que te das cuenta de que ha estado de espaldas a Mjolnir desde que ha acabado la maravillosa mamada."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_415wm" , "d") from _call_BlinkXPS3_2539
        hide c26s001_920wmv
    else:
        call BlinkXPS3 ("c26s001_415nm" , "d") from _call_BlinkXPS3_2540
        hide c26s001_920nmv
    mee "*Gemido* ¿Por qué has parado?"
    mc "Meemaw, he estado recuperado desde un minuto después de correrme..."
    mee "¿Qué? ¿Por qué no me lo has dicho?"
    mc "Porque tengo otras formas de hacerte disfrutar sin hacerte el amor. La noche es larga."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_420wm" , "d") from _call_BlinkXPS3_2541
    else:
        call BlinkXPS3 ("c26s001_420nm" , "d") from _call_BlinkXPS3_2542
    mee "..."
    mc "¿Qué pasa, Meemaw?"
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_425wm" , "d") from _call_BlinkXPS3_2543
    else:
        call BlinkXPS3 ("c26s001_425nm" , "d") from _call_BlinkXPS3_2544
    mee "Va a ser la primera vez que haga el amor con mi nueva... Después de la operación..."
    mee "No sé cómo será. Si lo notarás... raro..."
    mc "Solo hay una forma de descubrirlo. Pero sólo si quieres descubrirlo."
    mc "Me puedo pasar la noche usando la lengua y los dedos si no estás decidida."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_430wm" , "f") from _call_BlinkXPS3_2545
    else:
        call BlinkXPS3 ("c26s001_430nm" , "f") from _call_BlinkXPS3_2546
    if persistent.family:
        "Tu abuela se baja de encima de tu pecho y se sienta en el borde de la cama."
    else:
        "[mee] se baja de encima de tu pecho y se sienta en el borde de la cama."
    mee "Llevo toda la noche deseando descubrirlo. Asustada de qué descubriremos."
    mee "No quiero retrasarlo más. Quiero notarte dentro y saber cómo se siente un cuerpo nuevo para un nuevo amor."
    mc "¿Cuál es tu postura favorita?"
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_435wm" , "d") from _call_BlinkXPS3_2547
    else:
        call BlinkXPS3 ("c26s001_435nm" , "d") from _call_BlinkXPS3_2548
    mee "Soy una mujer clásica. Me encantaría que me hicieras el amor mientras te miro a los ojos."
    mc "Me parece una idea perfecta."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_440wm" , "f") from _call_BlinkXPS3_2549
    else:
        call BlinkXPS3 ("c26s001_440nm" , "f") from _call_BlinkXPS3_2550
    if persistent.family:
        "Rodeas la cama y te pones de pie entre sus piernas, dispuesto a asaltar el reconstruido tesoro de tu abuela."
    else:
        "Rodeas la cama y te pones de pie entre sus piernas, dispuesto a asaltar el reconstruido tesoro de la anciana."
    mc "¿Preparada?"
    mee "Casi. Déjame ponértelo más fácil."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_445wm" , "d") from _call_BlinkXPS3_2551
    else:
        call BlinkXPS3 ("c26s001_445nm" , "d") from _call_BlinkXPS3_2552
    "Para tu sorpresa, sube una pierna encima de tu hombro. Puede que haya pasado de los sesenta, pero sigue siendo una mujer flexible."
    mee "*Risa* ¡No pongas esa cara de sorpresa! Así evitaremos que me rompas a la primera embestida."
    mc "Intentaré ser delicado."
    scene c26s001_450An1 with dissolve
    "Introduces la punta de Mjolnir en el coño de [mee]. Aparte de que es más estrecha de lo que imaginabas, no notas ninguna diferencia con otras mujeres."
    mc "¿Estás bien?"
    mee "Un poco distendida, pero bien."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_455wm" , "d") from _call_BlinkXPS3_2553
    else:
        call BlinkXPS3 ("c26s001_455nm" , "d") from _call_BlinkXPS3_2554
    mee "¿Cómo es? ¿Notas algo... raro?"
    mc "Es perfecto. Lo único raro es que haya aguantado tanto tiempo antes de hacer esto."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_460wm" , "d") from _call_BlinkXPS3_2555
    else:
        call BlinkXPS3 ("c26s001_460nm" , "d") from _call_BlinkXPS3_2556
    mee "*Risa* Sabes cómo hacer que una chica se sienta bien. Bueno... 'chica'." id c26s001_MeeSex_989d5079
    mc "Ahora eres mi chica, Meemaw. Y mi trabajo y mi vocación son hacerte sentir bien."
    mee "Entonces puedes seguir. Notarte dentro me hace sentir... muy bien."
    scene c26s001_450An2 with dissolve
    if persistent.family:
        "Penetras a tu abuela un poco más, hasta que notas que llegas al fondo."
    else:
        "Penetras a [mee] un poco más, hasta que notas que llegas al fondo."
    mee "*GEMIDO* ¡Ooof! *JADEO*"
    "Es una sensación diferente, como si fuera un cérvix un poco más duro y a menos profundidad."
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_465wm" , "d") from _call_BlinkXPS3_2557
    else:
        call BlinkXPS3 ("c26s001_465nm" , "d") from _call_BlinkXPS3_2558
    mee "*Respiración entrecortada* Creo que has llegado al final. ¿Cómo es?"
    mc "Igual de perfecto que el principio. Algo más cerca de lo que esperaba, pero igual de perfecto."
    mee "*Respiración entrecortada* Me dijo el cirujano que tardaría un poco en recuperar la flexibilidad."
    mc "Tienes la flexibilidad necesaria. No te preocupes. ¿Cómo te sientes tú?"
    if persistent.lactation:
        call BlinkXPS3 ("c26s001_470wm" , "d") from _call_BlinkXPS3_2559
    else:
        call BlinkXPS3 ("c26s001_470nm" , "d") from _call_BlinkXPS3_2560
    mee "*Respiración entrecortada* Rellena como un pollo. *Risa* Pero es perfecto. Casi como perder la virginidad una segunda vez, pero sin dolor."
    mee "Me preocupaba lo que tú pudieras notar."
    mc "Lo que yo noto es a una mujer perfecta abrazando mi polla de una forma perfecta con su perfecto coño."
    mc "No tienes nada que envidiar a nadie."
    if persistent.lactation:
        scene c26s001_925-wm-pv with dissolve
        show c26s001_925wmv
    else:
        scene c26s001_925-wm-pv with dissolve
        show c26s001_925nmv
    "Para demostrárselo, empiezas a bombear con tus caderas en su estrechísimo coño."
    mee "*Gemido* ¡Ooof! *Jadeo*"
    if persistent.family:
        "No sabes si es por la sensibilidad producida por el orgasmo anterior o por la estrechez del coño de tu abuela, pero la sensación es increíble."
    else:
        "No sabes si es por la sensibilidad producida por el orgasmo anterior o por la estrechez del coño de [mee], pero la sensación es increíble."
    mee "*Jadeo* ¡Es alucinante! *Gemido* ¡Casi me vuelvo a correr! *Jadeo*"
    "Estás esperando que llegue el momento en que lo haga."
    if persistent.lactation:
        scene c26s001_935-wm-pv with dissolve
        show c26s001_935wmv
        hide c26s001_925wmv
        "Estás deseando empezar a ver surgir la leche como un géiser de unos pechos que son más que perfectos para la edad de la mujer que tienes debajo tuyo."
    else:
        scene c26s001_935-nm-pv with dissolve
        show c26s001_935nmv
        hide c26s001_925nmv
    "Todas las emociones y lo que siente [mee] con cada embestida se reflejan en su cara. Te alegras de que haya querido que vuestra primera vez sea cara a cara."
    mee "*Gemido* Estoy notando cómo me das de sí cada vez que llegas al fondo. *Jadeo*"
    "Tú también puedes notarlo. Poco a poco tu polla entra más profundamente, su coño recuperando algo de flexibilidad con el proceso."
    mee "*Jadeo* Me encanta sentirte profundamente. *Gemido*"
    "La sensación de extrañeza que habías notado al principio va desapareciendo paulatinamente, convirtiéndose en una sensación maravillosa." id c26s001_MeeSex_00fb5829
    scene c26s001_930-pv with dissolve
    show c26s001_930v
    hide c26s001_935wmv
    hide c26s001_935nmv
    "Todavía no puedes meter toda la extensión de Mjolnir, pero dudas si hubieras podido en circunstancias normales. [mee] es pequeña."
    mee "*Gemido* ¡Estoy a punto de correrme! *Jadeo* ¡Otra vez! *Gemido*"
    "A ti aún te queda un rato, con lo que es el momento de hacer disfrutar a tu nueva pareja oficial. La primera noche de muchas."
    mee "*JADEO* ¡No voy a poder aguantarlo mucho más! *GEMIDO*"
    "No hace falta que lo haga. La noche es joven todavía y no quieres que te espere."
    mc "Córrete para mí, preciosa."
    "La suerte de ser una mujer multiorgásmica es que puede tener tantos orgasmos como su resistencia le permita."
    if persistent.lactation:
        call OrgasmXS3 ("c26s001_475wm") from _call_OrgasmXS3_62
        "Tus palabras hacen que su cuerpo vuelva a explotar en un par de géiseres blancos."
    else:
        call OrgasmXS3 ("c26s001_475nm") from _call_OrgasmXS3_63
    hide c26s001_930v
    mee "*GEMIDO* ¡JODER, SÍ! *JADEO*"
    "Su cuerpo se tensa y relaja al ritmo de las oleadas que lo recorren, intentando ordeñar tu polla de un semen que todavía no ha llegado."
    "Para eso no ha perdido ni un ápice de flexibilidad. Sus paredes internas se cierran con fuerza sobre Mjolnir."
    if persistent.lactation:
        scene c26s001_940-wm-pv with dissolve
        show c26s001_940wmv
    else:
        scene c26s001_940-nm-pv with dissolve
        show c26s001_940nmv
    if persistent.family:
        "Si hasta ahora era placentero, los espasmos que recorren el coño de tu abuela hacen que alcances nuevas cotas de placer."
    else:
        "Si hasta ahora era placentero, los espasmos que recorren el coño de [mee] hacen que alcances nuevas cotas de placer."
    mee "*JADEO* ¡POR EL AMOR DE DIOS! *GEMIDO* ¡NO PUEDO PARAR DE CORRERME!"
    "Esperas que no lo haga. El abrazo de hierro y húmedo terciopelo alrededor de tu polla es maravilloso."
    mee "*GEMIDO* ¡BÉSAME! *JADEO* ¡BÉSAME MIENTRAS ME HACES EL AMOR! *GEMIDO*"
    "A menos que quieras arrancarle la pierna que tiene apoyada en tu hombro, se requiere un cambio de postura para ello."
    scene c26s001_950-pv with fade
    show c26s001_950v
    hide c26s001_940wmv
    hide c26s001_940nmv
    "Cambiáis de posición sin palabras y sin dejar que Mjolnir abandone su nueva casa, para permitir que vuestros labios se junten en un apasionado beso."
    mee "*JADEO*"
    "El continuo bombeo hace que vuestros labios pierdan contacto de vez en cuando, permitiéndoos recuperar el aliento."
    mee "*GEMIDO* ¡ASÍ! *JADEO*"
    "El corto espacio de tiempo de separación no permite dialogar más allá de alguna palabra suelta."
    scene c26s001_955-pv with fade
    show c26s001_955v
    hide c26s001_950v
    "Sigues sin poder penetrar a [mee] hasta el fondo, pero no importa. Con su coño ordeñándote la sensación es igual de increíble."
    mee "*GEMIDO*"
    "Sus clímax se suceden uno tras otro, mientras el tuyo se acerca a pasos agigantados."
    mee "*JADEO* ¡SÍ! *GEMIDO*"
    "Los jadeos y gemidos que la mujer exhala en tu boca al ritmo que marca la llegada de sus orgasmos hacen que todo sea más sensual."
    scene c26s001_945-pv with fade
    show c26s001_945v
    hide c26s001_955v
    "Una sensación conocida empieza a reptar por tus pantorrillas, anunciando tu inminente corrida."
    mc "Estoy a punto de correrme."
    "[mee] aprieta más sus piernas a tu alrededor, indicándote que no te va a dejar ir."
    mee "*GEMIDO* ¡CÓRRETE DENTRO! *JADEO*"
    "A menos que uses la violencia, no vas a poder desobedecer sus órdenes."
    call OrgasmXS3 ("c26s001_480") from _call_OrgasmXS3_64
    hide c26s001_945v
    mc "¡Mpfft!"
    "Es tu turno de explotar, descargando toda tu semilla en el interior de [mee]."
    mee "*JADEO* ¡ESTÁ SUPER CALIENTE! *GEMIDO*"
    scene c26s001_480d with dissolve
    if persistent.family:
        "Notas cómo el corto túnel de tu abuela se llena hasta rebosar, empezando a gotear parte de tu semen."
    else:
        "Notas cómo el corto túnel de [mee] se llena hasta rebosar, empezando a gotear parte de tu semen."
    "Os quedáis inmóviles unos momentos, la mujer debajo tuyo exhausta después de todas las sensaciones de la noche."
    call BlinkXPS3 ("c26s001_485" , "f") from _call_BlinkXPS3_2561
    stop music fadeout (1.5)
    "Cuando su respiración empieza a recuperar la normalidad..."
    play music ("music/Emotional-Piano-Sad.ogg")
    mee "¿Qué te ha parecido tu primera vez con una mujer... incompleta?"
    mc "¿Incompleta? No lo estás, Meemaw. Estás tan completa como cualquier otra mujer de la casa."
    mc "Y me ha parecido maravilloso."
    mc "¿Qué te ha parecido a ti?"
    call BlinkXPS3 ("c26s001_490" , "d") from _call_BlinkXPS3_2562
    mee "Tenía mucho miedo... No, no era miedo. Era ansiedad sobre si te iba a parecer extraño."
    mc "Pues puedes olvidarte de esa ansiedad. Simple y llanamente maravilloso."
    stop music fadeout (1.5)
    mc "Pero aún no me has dicho si es lo que esperabas."
    play music ("music/Fragile-Beauty.ogg")
    call BlinkXPS3 ("c26s001_495" , "d") from _call_BlinkXPS3_2563
    mee "Mucho mejor de lo que esperaba. No esperaba poder adaptarme tan bien al monstruo que tienes entre las piernas."
    mc "*Risa* Mjolnir se siente un poco ofendido ahora mismo."
    call BlinkXPS3 ("c26s001_500" , "d") from _call_BlinkXPS3_2564
    mee "*Risa* No era mi intención insultarlo. Se ha portado como un caballero. Un caballero travieso, pero un caballero al fin y al cabo."
    mee "Pero, ¿sabes lo que me apetece ahora mientras te recuperas?"
    mc "Si te pareces lo más mínimo a mí, una sesión de abrazos. Aunque puedes volver a subir a mi boca si quieres."
    call BlinkXPS3 ("c26s001_505" , "d") from _call_BlinkXPS3_2565
    mee "*Risa* Tu boca es como una droga para mí, pero no quiero morir de sobredosis o de deshidratación."
    mee "Necesito recuperarme un poco después de esto. Y no hay mejor forma que con unos abrazos."
    mc "Déjame tumbarme si no quieres que te aplaste."
    call BlinkXPS3 ("c26s001_510" , "f") from _call_BlinkXPS3_2566
    mee "Mucho mejor así. Si estás incómodo, dímelo."
    mc "Meemaw, eres ligera como una pluma. No te preocupes."
    call BlinkXPS3 ("c26s001_515" , "d") from _call_BlinkXPS3_2567
    mee "No había tenido tantos orgasmos nunca. Eres un amante increíble, y muy considerado."
    mee "Pero es agotador. Tengo que trabajar en mi resistencia."
    mc "Te puedes unir a las clases de yoga o ir a correr con [kat]."
    mc "Pero no te preocupes, no creo que tengas ningún problema de resistencia."
    call BlinkXPS3 ("c26s001_520" , "d") from _call_BlinkXPS3_2568
    mee "*Risa* Veamos cómo aguanto el segundo asalto."
    mc "Como has dicho en la cena, no hace falta que lo descubramos todo el primer día... o la primera noche."
    call BlinkXPS3 ("c26s001_525" , "d") from _call_BlinkXPS3_2569
    mee "Tienes razón, pero no quiero que pienses que soy una mujer de un solo asalto."
    mee "Cuando era joven..."
    scene c26s001_525c with dissolve
    "Silencio."
    mcp "(¿Se ha quedado dormida a media frase?)"
    "Esperas unos segundos para asegurarte de que no está recordando algo... con los ojos cerrados y respirando profundamente."
    scene c26s001_525d with dissolve
    "Cuando estás seguro de que no se va a despertar en breve, apagas la luz, intentando moverte lo menos posible para no perturbar su sueño."
    "No te sientes demasiado cansado y crees que te va a costar dormirte."
    scene c26s001_525d with fade
    stop music fadeout (1.5)
    "Parpadeas."
    scene black with dissolve
    "Cierras los ojos."
    "Duermes."
    if persistent.family:
        "Duermes como un bebé en los brazos de tu abuela, como algunas veces cuando eras pequeño."
    else:
        "Duermes como un bebé en los brazos de la mujer a la que siempre has considerado tu abuela, como algunas veces cuando eras pequeño."
    centered "{size=+20}{b}DÍA 28 – LUNES{/b}{/size}"
    call BlinkXPS3 ("c26s001_530" , "d") from _call_BlinkXPS3_2570
    play music ("music/i-feel-alive.ogg")
    "Te despiertas cuando ya es de día. Hay una hermosa mujer de pelo gris mirándote."
    mee "Buenos días, cielo."
    mc "Buenos días, Meemaw. ¿Llevas mucho rato despierta?"
    "Te das cuenta de que, en algún momento, se ha quitado la joyería."
    call BlinkXPS3 ("c26s001_535" , "d") from _call_BlinkXPS3_2571
    mee "Alrededor de 20 minutos. Estabas durmiendo tan a gusto que no he querido despertarte."
    mc "Podías hacerlo. No me hubiera importado."
    call BlinkXPS3 ("c26s001_540" , "d") from _call_BlinkXPS3_2572
    mee "*Risita* Bueno, he estado tentada cuando has tenido una erección mientras dormías."
    mc "*Risa* Me hubiera importado menos todavía si me hubiera despertado porque hubieras estado jugando con Mjolnir."
    mc "Por cierto, ¿qué le ha pasado a tu pelo? Nunca te lo había visto tan alborotado."
    call BlinkXPS3 ("c26s001_545" , "d") from _call_BlinkXPS3_2573
    mee "*Risa* Yo me he preguntado lo mismo cuando me he visto, hasta que me he acordado de que me dormí con el pelo húmedo."
    call BlinkXPS3 ("c26s001_550" , "d") from _call_BlinkXPS3_2574
    mee "Siento haberme quedado dormida y haberte dejado sin el segundo asalto."
    mc "No te preocupes por eso. *Risa* Creo que cubrimos el expediente con creces anoche."
    call BlinkXPS3 ("c26s001_555" , "d") from _call_BlinkXPS3_2575
    mee "Eso no significa que no podamos continuar por la mañana, ¿verdad?"
    mc "Alguien se ha levantado traviesa."
    mee "No, pero después de 20 minutos de mirarte, mi nivel de 'traviesismo' se ha ido incrementando tanto como mi humedad."
    call BlinkXPS3 ("c26s001_560" , "d") from _call_BlinkXPS3_2576
    mee "Y no me intentes decir que una erección mañanera no sirve para el sexo. Esas mentiras no cuelan."
    if persistent.family:
        mc "*Risa* ¿El abuelo intentó mentirte con eso?"
    else:
        mc "*Risa* ¿John intentó mentirte con eso?"
    call BlinkXPS3 ("c26s001_565" , "d") from _call_BlinkXPS3_2577
    mee "*Risita* Digamos que, cuando yo era joven, era un poco... codiciosa. O insaciable, como decía John."
    mc "*Risa* Veo que eso no ha cambiado. ¿O nos has mentido sobre tu edad?"
    call BlinkXPS3 ("c26s001_570" , "d") from _call_BlinkXPS3_2578
    mee "Al igual que tú, no miento. *Risa* Sólo oculto las verdades. Y mi edad no es una de las cosas que oculte."
    mee "Igual que Mjolnir no puede mentir. Parece que se ha levantado tan travieso como yo."
    mc "¿Te sorprende? Llevas con él en la mano un rato."
    mc "¿Quieres que volvamos a hacer el amor?"
    call BlinkXPS3 ("c26s001_575" , "d") from _call_BlinkXPS3_2579
    mee "No, lo de ayer fue increíble, pero hoy quiero que me folles."
    mee "Una vez que hemos descubierto que... todavía funciono... quiero un poco de sexo salvaje."
    mc "¿Sin besos antes? ¡Me sorprendes, Meemaw!"
    scene c26s001_575d with dissolve
    if persistent.family:
        "Tu abuela trepa hasta tus labios para darte un apasionado beso de buenos días. Su mano no abandona a Mjolnir en ningún momento."
    else:
        "[mee] trepa hasta tus labios para darte un apasionado beso de buenos días. Su mano no abandona a Mjolnir en ningún momento."
    "Por los jadeos que deja ir en tu boca descubres que no mentía en cuanto a su nivel de humedad. No hace falta que compruebes su entrepierna."
    call BlinkXPS3 ("c26s001_580" , "d") from _call_BlinkXPS3_2580
    mee "*Respiración entrecortada* ¿Contento? Ya ha habido besos."
    mc "Muy contento. Ahora..."
    call BlinkXPS3 ("c26s001_585" , "h") from _call_BlinkXPS3_2581
    "Volteas a la diminuta mujer, sujetándola contra el colchón por las muñecas."
    mee "¡[mc]! ¿Qué haces?"
    stop music fadeout (1.5)
    mc "¿No querías un poco de sexo salvaje?"
    play music ("music/SexyLoungeMusic.ogg")
    call BlinkXPS3 ("c26s001_590" , "d") from _call_BlinkXPS3_2582
    mee "¿Me vas a follar como a una guarrilla?"
    mc "No. Te voy a follar como a una de las mujeres más maravillosas del mundo."
    scene c26s001_595An with vpunch
    "La penetras con fuerza sin esperar a que diga nada. Puedes llegar mucho más profundamente que la noche anterior."
    mee "*JADEO* ¡JODER! *GEMIDO* ¡VAS A ROMPERME! *JADEO*"
    mc "Sexo salvaje es sexo salvaje, muñeca. Así aprenderás a poner límites a lo que pides."
    call BlinkXPS3 ("c26s001_605" , "d") from _call_BlinkXPS3_2583
    "Pese a tus palabras, no puedes disimular un rictus de preocupación por si has sido demasiado brusco. Tu expresión es detectada por [mee]."
    mee "*Jadeo* No me he quejado porque me rompas. *Gemido risueño* Solo te informaba. *Jadeo*"
    "Aliviado por sus palabras, reemprendes el rol en el que has pensado."
    mc "Entonces prepárate. Hay más de dónde ha salido esto."
    if persistent.lactation:
        scene c26s001_975-wm-pv with dissolve
        show c26s001_975wmv
    else:
        scene c26s001_975-nm-pv with dissolve
        show c26s001_975nmv
    "Empiezas a bombear con fuerza, rítmicamente. [mee] no puede disimular el placer que recibe."
    mee "*Gemido* ¡Oh, sí! *Jadeo* ¡Fóllame duro! *Gemido*"
    "Las palabras en labios de [mee], siempre comedida si no es para echar una bronca, parecen fuera de lugar."
    mee "*Jadeo* ¡Dame todo lo que tengas! *Gemido*"
    "Pero parecen encajar perfectamente con la nueva personalidad que estás descubriendo en la pequeña mujer."
    if persistent.lactation:
        scene c26s001_960-wm-pv with dissolve
        show c26s001_960wmv
        hide c26s001_975wmv
    else:
        scene c26s001_960-nm-pv with dissolve
        show c26s001_960nmv
        hide c26s001_975nmv
    "Tus embestidas incrementan su velocidad tal como vas rebasando nuevos límites que no incomodan a la mujer que hay debajo tuyo."
    mee "*Gemido* ¡Joder, [mc]! *Jadeo* ¡Has nacido para esto! *Gemido*"
    "Con sus piernas en alto, te da la sensación de que cada vez puedes penetrarla más profundamente."
    mee "*Gemido* ¿Te estabas reteniendo anoche? *Jadeo*"
    "No es que te retuvieras, sino que hoy la vagina de [mee] parece mucho más profunda y flexible."
    scene c26s001_965-pv with dissolve
    show c26s001_965v
    "Ahora puedes meter toda tu polla hasta el fondo y no parece incomodarle. Sigues notando el extraño fondo en cada embestida."
    mee "*JADEO* ¡SIGUE ASÍ! *GEMIDO* ¡NO PARES! *JADEO*"
    "No tienes intención de parar ni podrías hacerlo aunque quisieras. Ambos habéis entrado en un trance en el que solo existen vuestros cuerpos."
    mee "*GEMIDO* ¡FÓLLAME MÁS DURO! *JADEO* ¡ESTOY A PUNTO DE CORRERME! *GEMIDO*"
    "Bombeas más rápido, más duro. No quieres que ella pierda ese punto en el que está. Y estás deseando ser ordeñado de nuevo."
    if persistent.lactation:
        call OrgasmXS3v ("c26s001_610awm" , "c26s001_595b" , "c26s001_610bwm") from _call_OrgasmXS3v
    else:
        call OrgasmXS3v ("c26s001_610anm" , "c26s001_595b" , "c26s001_610bnm") from _call_OrgasmXS3v_1
    hide c26s001_965v
    mee "*JADEO* ¡SÍ! ¡JODER! ¡SÍ! *GEMIDO*"
    "Escuchar ese tipo de palabras en boca de [mee] empieza a perder su extrañeza inicial. Sabes que va a soltar tacos cada vez que tenga un orgasmo intenso."
    "Y este lo es. Sus muros internos se cierran con fuerza sobre Mjolnir durante unos eternos segundos."
    if persistent.lactation:
        scene c26s001_970-wm-pv with dissolve
        show c26s001_970wmv
    else:
        scene c26s001_970-nm-pv with dissolve
        show c26s001_970nmv
    "Continúas tus embestidas contra la imponente resistencia que opone el coño de [mee]. Bendita resistencia que hace que notes cada uno de sus pliegues."
    mee "*GEMIDO* ¡POR EL AMOR DE DIOS! *JADEO*"
    "Cuando su vagina parece empezar a relajar su presión, una nueva oleada la incrementa de nuevo, masajeando tu polla desde su entrada hasta el fondo."
    "Intentando ordeñar hasta la última gota del semen que está a punto de llegar."
    "Puede que no tenga útero, pero su coño sigue funcionando como ha sido diseñado por milenios de evolución."
    if persistent.walkthrough:
        $ wt1 = _("Sin consecuencias.")
        $ wt2 = _("Sin consecuencias.")
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Correrte dentro." (wt=wt1):
            if persistent.lactation:
                call OrgasmXS3v ("c26s001_595b" , "c26s001_615awm"  , "c26s001_615b") from _call_OrgasmXS3v_2
            else:
                call OrgasmXS3v ("c26s001_595b" , "c26s001_615anm"  , "c26s001_615b") from _call_OrgasmXS3v_3
            mc "¡Mpfft!"
            "Vuelves a explotar en el coño de [mee] como la noche anterior, llenándola de nuevo hasta el borde."
            mee "*GEMIDO* ¡SÍ! *JADEO* ¡DÁMELA TODA! *GEMIDO*"
            "Parte de tu semen vuelve a escaparse, recorriendo tu polla hasta su base."
            $ inside = True
        "Correrte sobre su estómago." (wt=wt1):
            if persistent.lactation:
                call OrgasmXS3 ("c26s001_620wm") from _call_OrgasmXS3_65
            else:
                call OrgasmXS3 ("c26s001_620nm") from _call_OrgasmXS3_66
            mc "¡Mpfft!"
            "Sales justo a tiempo para rociar el estómago de [mee] con tu semen."
            mee "*GEMIDO* ¡SÍ! *JADEO* ¡BÁÑAME EN TU LECHE! *GEMIDO*"
            "El cuadro que pintas sobre el hermoso lienzo podría estar en cualquier museo de arte moderno."
            "Siempre has pensado que los cuadros abstractos podrían ser pintados tirando pintura sobre el lienzo. O semen."
            $ inside = False
    $ resetWalkthrough ()
    call BlinkXPS3 ("c26s001_625" , "f") from _call_BlinkXPS3_2584
    stop music fadeout (1.5)
    "Al cabo de unos segundos, cuando vuestras respiraciones vuelven a la normalidad..."
    play music ("music/Stardust.ogg")
    mee "Eso ha sido increíble. No sabía que podías ser tan... salvaje."
    mc "Has pedido sexo salvaje. No sabía si sería suficientemente salvaje para ti."
    call BlinkXPS3 ("c26s001_630" , "d") from _call_BlinkXPS3_2585
    mee "*Risa* Más salvaje de lo que esperaba. Cuando me has inmovilizado contra el colchón... Ha sido increíble..."
    mee "Llevaba días pensando en cómo sería algo así con el siempre tierno y dulce [mc]."
    call BlinkXPS3 ("c26s001_635" , "d") from _call_BlinkXPS3_2586
    mee "¿Cuál sería la palabra contraria a decepcionada? Porque es como estoy ahora mismo."
    mc "No sé.... Ilusionada, satisfecha..."
    call BlinkXPS3 ("c26s001_640" , "d") from _call_BlinkXPS3_2587
    mee "*Risa* Creo que 'satisfecha' me sirve. En todos los sentidos."
    if persistent.family:
        mee "¿Cómo ha sido para ti la experiencia de follarte a tu abuela?"
    else:
        mee "¿Cómo ha sido para ti la experiencia de follarte a tu Meemaw?"
    if bet._var("route") or nor._var("route") or mar._var("route") or emm._var("route") or eri._var("route") or dap._var("route"):
        mc "Si hubieras sido el primer miembro de la antigua familia con quien me acuesto, posiblemente traumático. *Risa*"
    elif oma._var("route") or eil._var("route") or sai._var("route") or sca._var("route") or sam._var("route") or sim._var("route") or eva._var("route") or mad._var("route") or meg._var("route") or kia._var("route"):
        mc "Si hubieras sido el primer miembro de esta nueva familia que estamos formando con quien me acuesto, posiblemente traumático. *Risa*"
    else:
        mc "Teniendo en cuenta que eres el primer miembro de esta familia que estamos formando con quien me acuesto, posiblemente acabe traumatizado. *Risa*"
    mc "Es broma. Ha sido increíble, aunque prefiero lo de ayer."
    call BlinkXPS3 ("c26s001_645" , "d") from _call_BlinkXPS3_2588
    mee "Yo también. Aunque de vez en cuando me guste esto, no hay nada como el sexo dulce y tierno."
    stop music fadeout (1.5)
    mc "Yo pienso que..."
    scene c26s001_645d with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    play music ("music/SneakySnitch.ogg")
    nor "*A través de la puerta* Mamá, [mc], el desayuno está listo. Podéis bajar cuando hayáis acabado."
    mc "No te preocupes por mí, [nor]. Desayunaré en casa un poco más tarde, pero gracias."
    nor "*A través de la puerta* ¿Mamá? ¿Te esperamos para desayunar?"
    call BlinkXPS3 ("c26s001_650" , "d") from _call_BlinkXPS3_2589
    mee "*Susurrando* ¿Qué le digo?"
    mc "*Risa* No sé. ¿Tienes hambre? Ya sabe que estoy aquí, con lo que no tiene ningún sentido que no le contestes."
    call BlinkXPS3 ("c26s001_655" , "d") from _call_BlinkXPS3_2590
    mee "Dame unos minutos para que me duche y bajo a desayunar con vosotras, cielo."
    nor "*A través de la puerta* OK. Tómate tu tiempo. Te esperamos abajo."
    call BlinkXPS3 ("c26s001_660" , "h") from _call_BlinkXPS3_2591
    mee "*Susurrando* ¿Ha dicho 'esperamos'? ¿Quién más había detrás de esa puerta?"
    mc "*Risa* Estuviera quién estuviera, son menos personas a las que tienes que informar de que estamos juntos."
    mc "Voy a dejarte que te des esa ducha... a la que supongo que no estoy invitado."
    call BlinkXPS3 ("c26s001_665" , "d") from _call_BlinkXPS3_2592
    mee "*Susurrando* ¿Cómo vas a estar invitado? ¿No ves que ahora saben que estamos aquí?"
    mc "*Risa* Creo que lo saben desde anoche. Tía [bet] duerme en la habitación de al lado... si le hemos dejado dormir."
    mc "De todas formas, te vas a tener que acostumbrar a que sepan cuando nos acostamos juntos. *Risa* O eso o compro una mordaza."
    call BlinkXPS3 ("c26s001_670" , "d") from _call_BlinkXPS3_2593
    mee "*Risa* Si me amordazas te perderás mis fabulosas mamadas. Una vez las informe, me dará lo mismo que sepan cuando nos acostamos juntos."
    mc "¡Esa es la forma de pensar! Ahora ve a ducharte antes de que se te enfríe demasiado el desayuno."
    if persistent.lactation and inside:
        scene c26s001_670d with dissolve
    elif persistent.lactation and not inside:
        scene c26s001_670e with dissolve
    elif not persistent.lactation and inside:
        scene c26s001_670f with dissolve
    elif not persistent.lactation and not inside:
        scene c26s001_670g with dissolve
    "Besas a [mee] de una forma que sabe a despedida, a fin de una noche maravillosa, aunque ya sea por la mañana."
    "Vendrán más, muchas más, en las que ya no le importará si llaman a la puerta para informar de que el desayuno está listo."
    scene c26s001_670h with dissolve
    "Pocos segundos después, ella se va a la ducha y te quedas unos segundos mirando la vacía habitación, atesorando el recuerdo de una noche especial."
    stop music fadeout (1.5)
    "Evitas pasar por la cocina de camino a la camioneta. Informar a la familia es tarea de [mee]."
    return
label c26s002_EriDapSca:
    if _in_replay:
        call mrS3_mee_route from _call_mrS3_mee_route_6
        call mrS3_dap_route from _call_mrS3_dap_route_7
        call mrS3_sca_route from _call_mrS3_sca_route_7
        call mrS3_eri_route from _call_mrS3_eri_route_8
    if mee._var("route"):
        scene c26s002_005a with dissolve
        "Después de meter el coche en el garaje y pasar por tu habitación a cambiarte y a ducharte, vas a la cocina a desayunar algo."
    else:
        scene black with dissolve
        centered "{size=+20}{b}DÍA 28 – LUNES{/b}{/size}"
        scene c26s002_005a with dissolve
        "Cuando te levantas bajas a la cocina a desayunar algo."
    play music ("music/RhythmPlay.ogg")
    mc "Buenos días, chicas."
    if eri._var("route"):
        call KissXPS3 ("c26s002_010" , "d") from _call_KissXPS3_66
    else:
        scene c26s002_010c with dissolve
    eri "Buenos días, [mc]."
    if dap._var("route"):
        call KissXPS3 ("c26s002_020" , "d") from _call_KissXPS3_67
    else:
        scene c26s002_020c with dissolve
    dap "Buenos días, [mc]."
    if sca._var("route"):
        call KissXPS3 ("c26s002_015" , "d") from _call_KissXPS3_68
    else:
        scene c26s002_015c with dissolve
    sca "Buenos días, [mc]."
    call BlinkXPS3 ("c26s002_025" , "d") from _call_BlinkXPS3_2594
    eri "¿Has visto a Tía [mar]? No la encontramos por ningún lado. Ni a mi madre tampoco."
    mc "No tengo ni idea de dónde pueden estar. No las he visto hoy. ¿Por qué?"
    call BlinkXPS3 ("c26s002_030" , "d") from _call_BlinkXPS3_2595
    dap "[eri] y yo hemos recibido un mensaje en el móvil cuando íbamos a ducharnos y no sabemos si es real o es phishing."
    mc "¿Qué dice?"
    dap "¡Que hemos recibido una transferencia internacional de $83,000! ¡Cada una!"
    mc "¿No dice de dónde viene?"
    call BlinkXPS3 ("c26s002_035" , "d") from _call_BlinkXPS3_2596
    eri "No, sólo pone un código bancario. ¿Tú no has recibido nada?"
    mc "No he mirado el teléfono hoy..."
    call BlinkXPS3 ("c26s002_040" , "h") from _call_BlinkXPS3_2597
    emm "¡Soy rica!"
    mc "Hola, [emm]. ¿Tú también has recibido el mensaje?"
    call BlinkXPS3 ("c26s002_045" , "d") from _call_BlinkXPS3_2598
    emm "¿Vosotros también? ¿No soy la única rica de la familia?"
    mc "Al menos [dap] y [eri] lo han recibido. ¿[sca]?" id c26s002_EriDapSca_7bdb7347
    call BlinkXPS3 ("c26s002_050" , "d") from _call_BlinkXPS3_2599
    sca "No, yo no he recibido nada."
    mc "[emm], ¿tú sabes qué es?"
    call BlinkXPS3 ("c26s002_055" , "d") from _call_BlinkXPS3_2600
    emm "No tengo ni idea, pero voy a poder comprarme un montón de ropa, y un coche, y..."
    mc "No empieces a gastar el dinero antes de saber de dónde viene."
    call BlinkXPS3 ("c26s002_060" , "d") from _call_BlinkXPS3_2601
    eri "Voy a llamar a [ama]. Es posible que venga de NTR. Si lo hemos recibido [emm], [dap], y yo, pero no [sca]..."
    mc "Sí, hazlo, por favor. Yo tengo el móvil en la habitación."
    call BlinkXPS3 ("c26s002_065" , "f") from _call_BlinkXPS3_2602
    "Un minuto después..."
    eri "Sí, es de NTR. Es nuestra parte de los beneficios, por las acciones..."
    mc "Bueno, ahora somos accionistas de una empresa millonaria. Hay que enterarse bien de cómo funciona."
    eri "[ama] me ha dicho que es un pago anual."
    call BlinkXPS3 ("c26s002_070" , "d") from _call_BlinkXPS3_2603
    sca "Entonces, ya no necesitarás trabajar en el café, ¿verdad?"
    sca "¿Podrías recomendarme para coger tu puesto?"
    mc "¿Quieres trabajar en el café, [sca]?"
    call BlinkXPS3 ("c26s002_075" , "d") from _call_BlinkXPS3_2604
    sca "Quiero contribuir en algo a la familia. Estoy aquí sin hacer nada hasta que empiecen las clases..."
    mc "Pero [dap] y tú ibais a venir a Aruba conmigo, ¿no?"
    call BlinkXPS3 ("c26s002_080" , "d") from _call_BlinkXPS3_2605
    sca "Si encuentro un trabajo, no podré ir. Ya habrá más oportunidades más tarde."
    mc "No creo que sea necesario que contribuyas económicamente, [sca]."
    mc "Eres de la familia y no tienes que pagar alquiler. Si [emm] no lo paga..."
    call BlinkXPS3 ("c26s002_085" , "d") from _call_BlinkXPS3_2606
    emm "*Risa* Ahora podría pagarlo."
    call BlinkXPS3 ("c26s002_090" , "d") from _call_BlinkXPS3_2607
    emm "[lis], [deb.nick], [kat], [sai], y [kim] también son de la familia y pagan por su alojamiento." id c26s002_EriDapSca_52127a86
    emm "No sé si deberíamos hacer algo al respecto."
    mc "Creo que eso lo deberíamos comentar con Mamá y con Tía [nor]. La verdad es que es raro..."
    call BlinkXPS3 ("c26s002_095" , "d") from _call_BlinkXPS3_2608
    eri "De todas formas, [sca], no voy a dejar el trabajo en el café hasta que empiecen las clases."
    mc "¿Por qué? Ahora no necesitas el dinero..."
    call BlinkXPS3 ("c26s002_100" , "d") from _call_BlinkXPS3_2609
    eri "Creo que ya sé en qué voy a gastar ese dinero, con lo que voy a estar en la misma situación."
    mc "¿En qué?"
    eri "Lo tengo que confirmar todavía. Pero, de momento, no voy a dejar mi trabajo."
    call BlinkXPS3 ("c26s002_105" , "d") from _call_BlinkXPS3_2610
    eri "[sca], igualmente le puedo decir a mi jefe que buscas trabajo para un mes. El chico que contrató para sustituir a Jack no está funcionando bien."
    eri "Si al final lo despide, podríamos trabajar juntas [eil], tú, y yo."
    call BlinkXPS3 ("c26s002_110" , "d") from _call_BlinkXPS3_2611
    sca "¡Oh! ¡Eso sería fantástico!"
    call BlinkXPS3 ("c26s002_115" , "d") from _call_BlinkXPS3_2612
    sca "Bueno, no por el pobre chico, pero..."
    mc "*Risa* Creo que te hemos entendido."
    call BlinkXPS3 ("c26s002_120" , "d") from _call_BlinkXPS3_2613
    dap "¿Crees que podemos gastar algo de ese dinero, [mc]?"
    mc "Una vez que [ama] ha confirmado que viene de NTR, creo que sí. Pero no os lo gastéis todo."
    mc "Es un pago anual, con lo que os lo vais a tener que administrar durante un año."
    call BlinkXPS3 ("c26s002_125" , "d") from _call_BlinkXPS3_2614
    emm "¿Quieres decir que Mamá dejará de darme la paga semanal?"
    mc "No es que lo crea. Le voy a proponer que deje de hacerlo. Ahora tienes tu propio dinero y tienes que aprender a administrarlo."
    call BlinkXPS3 ("c26s002_130a" , "d") from _call_BlinkXPS3_2615
    emm "¡Pero eso es injusto! Ella seguramente también lo ha cobrado..."
    mc "Y ella se ocupa de todos los gastos de la casa. No seas egoísta, [emm]."
    call BlinkXPS3 ("c26s002_130b" , "d") from _call_BlinkXPS3_2616
    emm "Tienes razón. Le preguntaré si necesita algo..."
    emm "Voy a buscarla para darle la noticia."
    call BlinkXPS3 ("c26s002_135" , "d") from _call_BlinkXPS3_2617
    dap "[sca], vamos a nuestra habitación. Creo que tenemos que renovar tu portátil."
    mcp "(La primera compra que hace es para [sca]. [dap] es maravillosa.)"
    call BlinkXPS3 ("c26s002_140" , "d") from _call_BlinkXPS3_2618
    sca "¿Qué? ¿Por qué? El mío aún puede durar..."
    mc "[sca], tu portátil todavía tiene Doors 8. Creo que ya es hora de jubilarlo, y no digas que no a un regalo."
    mc "Creo que le va a hacer más ilusión a [dap] comprártelo que a ti recibirlo."
    call BlinkXPS3 ("c26s002_145" , "d") from _call_BlinkXPS3_2619
    eri "Yo voy a hablar con Tía [bet] sobre unas cosas..."
    scene c26s002_005b with fade
    "Todas desaparecen y te quedas solo en la cocina."
    "Solo con tu hambre. Aún no has desayunado."
    stop music fadeout (1.5)
    "Pones remedio a esa situación."
    return
label c26s003_Sai:
    if _in_replay:
        call mrS3_mee_route from _call_mrS3_mee_route_7
        call mrS3_sai_route from _call_mrS3_sai_route_7
        call mrS3_meg_route from _call_mrS3_meg_route_2
    call BlinkXPS3 ("c26s003_005" , "d") from _call_BlinkXPS3_2620
    play music ("music/These-Little-Moments.ogg")
    "Al acabar de desayunar, de camino a tu habitación."
    mc "Hola, [sai], ¿qué haces tan sola?"
    sai "Les he mandado a mis padres unas fotos de la clase de tiro de ayer y estábamos chateando."
    sai "Tenías que haber venido. Fue muy divertido."
    mc "Me tienes que enseñar esas fotos."
    call BlinkXPS3 ("c26s003_010" , "d") from _call_BlinkXPS3_2621
    sai "Siéntate conmigo un momento y te las enseño."
    mc "¿No estabas chateando con tus padres?"
    call BlinkXPS3 ("c26s003_015" , "d") from _call_BlinkXPS3_2622
    sai "Me había despedido justo antes de que llegaras."
    mc "Enséñame esas fotos, entonces."
    scene c26s003_020a with dissolve
    sai "Mira, aquí estamos disparando las del primer turno. [eva] fue super estricta con la seguridad."
    mc "Sí que lo es. Es parte de su entrenamiento. Al menos no os hizo poneros trajes raros como a mí."
    call BlinkXPS3 ("c26s003_025" , "d") from _call_BlinkXPS3_2623
    sai "¿Cómo tuviste que vestirte?"
    mc "Me llevó en la moto y me hizo ponerme un traje de skydiving. Era bastante incómodo."
    call BlinkXPS3 ("c26s003_030" , "d") from _call_BlinkXPS3_2624
    sai "*Risa* Lástima que no haya fotos de eso. Nosotras disparamos con la ropa que llevábamos."
    mc "No sé si os gustaría verme con ese traje. *Risa* A menos que fuera para reíros de mí, claro."
    mc "Vosotras estáis mucho mejor. Pero quiero ver más fotos."
    scene c26s003_020b with dissolve
    sai "Estas son las del segundo turno. Había seis puestos de tiro, y éramos diez, más [ama] y [eva], con lo que dos turnos fueron bien."
    mc "¿Competíais entre vosotras?"
    call BlinkXPS3 ("c26s003_035" , "d") from _call_BlinkXPS3_2625
    sai "Quisimos hacerlo. [ama] dijo que no estaba bien para la primera lección, que era para aprender."
    sai "[emm] y yo insistimos, que era competir solo por diversión entre la familia."
    sai "[eva] fue al último puesto de tiro, disparó siete veces, y dijo algo como '¿Estáis seguras de que queréis competir?'"
    mc "*Risa* Y se acabó la discusión."
    call BlinkXPS3 ("c26s003_040" , "d") from _call_BlinkXPS3_2626
    sai "*Risa* Seis tiros dieron en el 10 y uno en el 9. 69 puntos."
    mc "Es extraño que fallara uno."
    call BlinkXPS3 ("c26s003_045" , "d") from _call_BlinkXPS3_2627
    sai "[ama] nos dijo luego que lo había hecho a propósito. Así, si alguien quería competir, tendría una oportunidad de superarla."
    mc "*Risa* Eso suena tan a... [eva]..."
    call BlinkXPS3 ("c26s003_050" , "d") from _call_BlinkXPS3_2628
    sai "Totalmente [eva]. Dejó clara su posición, pero dejó margen por si alguien quería competir de verdad."
    sai "Las que más se aceraron a su puntuación fueron [sam] y [kat], con 51 y 54 puntos. Ya habían disparado antes. Son muy buenas."
    mc "¿Cuál fue tu puntuación?"
    call BlinkXPS3 ("c26s003_055" , "d") from _call_BlinkXPS3_2629
    sai "*Risa* Unos horribles 23 puntos con siete disparos en mi mejor ronda. Y no fui la peor, pero no te diré quién fue."
    mc "*Risa* Deberías decírmelo, para salir corriendo si alguna vez la veo con un arma."
    scene c26s003_020c with dissolve
    sai "Mira, esta es la última foto, cuando habíamos acabado."
    mc "Me extraña mucho que [eva] y [ama] os dejaran posar con las pistolas..."
    sai "[emm] y [dap] querían que nos hiciéramos una foto en plan malotas. Tu madre insistió en que [ama] y [eva] revisaran todas las armas antes de la foto."
    mc "Pero no parecéis malotas. Estáis sonriendo todas. Quizás tú eres la que pareces más seria."
    call BlinkXPS3 ("c26s003_060" , "d") from _call_BlinkXPS3_2630
    sai "*Risa* Eso es porque en la foto en plan malotas... parecíamos unas drogadictas con el mono."
    sai "Las únicas que quedaron bien fueron [kim] y [lis]. Es imposible que esas chicas queden mal en ninguna foto."
    mc "*Risa* Quiero verla."
    call BlinkXPS3 ("c26s003_065" , "d") from _call_BlinkXPS3_2631
    sai "*Risa* ¿No nos conoces aún? Esa foto fue borrada una milésima de segundo después de verla."
    sai "Somos mujeres. No vamos a conservar una foto en la que salimos mal. Ni siquiera [lis] o [kim] la quisieron conservar."
    mc "¡Qué consideradas! *Risa* Les tendré que preguntar a [ama] y a [eva] si había cámaras de seguridad."
    call BlinkXPS3 ("c26s003_070" , "d") from _call_BlinkXPS3_2632
    sai "Aunque las hubiera, no te enseñarían las grabaciones."
    mc "¿Por qué?"
    call BlinkXPS3 ("c26s003_075" , "d") from _call_BlinkXPS3_2633
    sai "Primero porque era una cosa entre chicas. Segundo porque protegernos incluye destruir cualquier prueba de la existencia de esa foto. *Risa*"
    sai "Y, por último, porque ellas también quedaron mal. Pueden dar miedo cuando se ponen serias, pero cuando {b}fingen{/b} ser malotas... Quedaron horribles."
    mc "*Risa* Lo entiendo."
    call BlinkXPS3 ("c26s003_080" , "d") from _call_BlinkXPS3_2634
    sai "Seguramente hace una semana no les hubiera importado. ¿Ahora? Se están volviendo tan femeninas como el resto."
    sai "[eva] incluso está empezando a pedir consejos de belleza, aunque no los necesite. Me encanta esa evolución."
    mc "Es cierto. Sentirse arropadas por todas vosotras está haciendo que se abran más."
    scene c26s003_080d with dissolve
    "Te diriges a la cámara que sabes que una de las dos está mirando ahora mismo."
    mc "Bien hecho, chicas. Estoy orgulloso de vosotras."
    "Te puedes imaginar que, en algún lugar de la base, suena una risita."
    call BlinkXPS3 ("c26s003_085" , "d") from _call_BlinkXPS3_2635
    sai "A veces me olvido de que ven y escuchan todo lo que hacemos fuera de las habitaciones y los baños."
    mc "Es fácil olvidarse. Pero de todas formas, no importa. Creo que, cuando nos escuchan hablar de ellas, tienen que pasar la mitad del tiempo ruborizándose."
    mc "Aún no he oído a nadie decir nada malo de ellas."
    call BlinkXPS3 ("c26s003_090" , "d") from _call_BlinkXPS3_2636
    sai "Si alguien dijera algo malo de ellas, no sobreviviría hasta que llegaran a casa para vengarse."
    sai "Destrozaríamos entre todas a quien osara decir algo de nuestras chicas."
    scene c26s003_090d with dissolve
    "Ahora es cuando [sai] se dirige a la cámara."
    sai "Y sabéis que lo digo en serio. Todas os queremos."
    "Estás seguro de que quien esté escuchando se habrá ruborizado, o quizás se le hayan saltado unas lágrimas. No están muy acostumbradas a recibir cariño."
    "Se van a acostumbrar muy rápido."
    call BlinkXPS3 ("c26s003_095" , "d") from _call_BlinkXPS3_2637
    mc "¿Vais a hacer más lecciones de tiro?"
    sai "[eri] tiene que hacer una, pero será en el bosque. Creo que [eil] también se apuntará, y alguna de las de ayer también."
    sai "Fue muy divertido, y queremos repetirlo. Además, algunas queremos aprender a disparar con otras armas."
    mc "Además es una actividad en grupo para estrechar lazos entre vosotras."
    call BlinkXPS3 ("c26s003_100a" , "d") from _call_BlinkXPS3_2638
    sai "*Risa* ¿Estrechar lazos aún más? Vamos a parecer piezas de un corsé a este paso."
    call BlinkXPS3 ("c26s003_100b" , "d") from _call_BlinkXPS3_2639
    sai "En dos semanas aquí he estrechado más lazos de lo que hice el primer año en Portland, cuando vivía en el dormitorio."
    sai "Incluso con las chicas que no viven en casa, como [sam], [meg], o [oma]."
    mc "Entonces, ¿no te arrepientes de haber venido?"
    call BlinkXPS3 ("c26s003_105" , "d") from _call_BlinkXPS3_2640
    if sai._var("route"):
        sai "No me arrepiento en absoluto. Vine por ti, pero aunque no hubiéramos vuelto a estar juntos, hubiera valido la pena por las chicas."
        sai "Aunque no hubiera salido bien lo nuestro, la convivencia con esas chicas me hubiera hecho quedarme."
    else:
        sai "No me arrepiento en absoluto. Vine por ti, pero aunque no hemos vuelto a estar juntos, vale la pena por las chicas."
        sai "Tenías razón cuando me dijiste que no centrara mi vida en ti cuando no volvimos juntos, tenía que probar la convivencia con esas chicas para entenderlo."
    mc "Me alegra mucho que seas feliz aquí."
    call BlinkXPS3 ("c26s003_110" , "d") from _call_BlinkXPS3_2641
    sai "Lo soy. Mucho. Cuando en Portland me hablabas de tu familia no me podía imaginar algo así. Creía que exagerabas y resulta que te quedabas corto."
    mc "*Risa* Yo tampoco me podía imaginar algo así. No era así cuando me marché, pero me alegra que lo sea ahora."
    mc "¿Y qué tal con [meg]? A veces me sabe mal haberte pedido que compartas tu habitación con ella."
    call BlinkXPS3 ("c26s003_115" , "d") from _call_BlinkXPS3_2642
    sai "Me lo pediste la semana pasada y no hubo ningún problema. Esta semana ya tiene el coche arreglado y quería volver a su piso después de trabajar."
    sai "No le dejé hacerlo. Para mí, es una más y no me importa compartir la habitación con ella tres días por semana."
    sai "O aunque fueran todos los días. Es un cielo y si volviera a su piso después de trabajar seguramente no vendría a las comidas. Y no hubiera conocido a Zeus."
    mc "*Risa* Te estás convirtiendo en una Marks por derecho propio."
    call BlinkXPS3 ("c26s003_120" , "d") from _call_BlinkXPS3_2643
    sai "*Risa* He sonado como [eri], ¿verdad?"
    mc "*Risa* Un poco."
    sai "Es un ejemplo que deberíamos seguir todas. Creo que es la persona menos egoísta que he conocido en mi vida."
    mc "Tienes razón. Creo que esa sería una buena definición de [eri]."
    call BlinkXPS3 ("c26s003_125" , "d") from _call_BlinkXPS3_2644
    sai "Tener a personas como ella alrededor hace que el resto queramos ser mejores personas."
    mc "Será mejor que ella no te oiga decir eso o empezará a justificarse diciendo que lo que ella hace es lo normal en una familia."
    call BlinkXPS3 ("c26s003_130" , "d") from _call_BlinkXPS3_2645
    "En ese momento sale [meg] de la habitación que comparte con [sai]."
    meg "Bueno, ya he recogido todo y he cambiado las sábanas."
    call BlinkXPS3 ("c26s003_135" , "d") from _call_BlinkXPS3_2646
    sai "No hacía falta que lo hicieras. Me podía ocupar yo de todo."
    mc "¿Ya vuelves a casa?"
    call BlinkXPS3 ("c26s003_140" , "d") from _call_BlinkXPS3_2647
    meg "Ya sabes, hoy es mi día libre y tengo que hacer la colada para que los vestidos estén listos para mañana."
    mc "Déjame llevarte la maleta hasta el coche."
    call BlinkXPS3 ("c26s003_145" , "d") from _call_BlinkXPS3_2648
    meg "No hace falta. No pesa demasiado."
    mc "Insisto. ¿Lo tienes en el garaje de [nor]?"
    meg "Sí, y gracias."
    if sai._var("route"):
        call BlinkXPS3 ("c26s003_150" , "d") from _call_BlinkXPS3_2649
        sai "Cuando dejes la maleta de [meg], ¿podrías venir a mi habitación? Necesito tu ayuda con algo."
        mc "Ningún problema. En unos minutos paso a verte."
        call BlinkXPS3 ("c26s003_155" , "d") from _call_BlinkXPS3_2650
        meg "Chicos, puedo bajar la maleta yo sola. Tú tienes que ir a clase en un par de horas y..."
        mc "[meg], no creo que a [sai] le venga de cinco minutos, ¿verdad?"
        call BlinkXPS3 ("c26s003_160" , "d") from _call_BlinkXPS3_2651
        sai "Ni de cinco ni de diez. No hay prisa."
        mc "¿Ves?"
    stop music fadeout (1.5)
    scene black with dissolve
    "Las chicas se despiden con un abrazo y acompañas a [meg] hasta el garaje de [nor]."
    "Los abrazos se repiten con cada chica que os encontráis por el camino."
    if _in_replay:
        call c26s003_Sai2 from _call_c26s003_Sai2_1
    return
label c26s003_Sai2:
    call BlinkXPS3("c26s003_165" , "f") from _call_BlinkXPS3_2652
    play music ("music/thinking-of-you.ogg")
    "Al llegar al garaje de [nor], una vez metida la maleta de [meg] en su coche."
    mc "¿Te lo has pasado bien el fin de semana?"
    meg "Ha sido fantástico. Con Zeus me reí muchísimo ayer."
    mc "*Risa* No me hables del gato destructor de camas."
    call BlinkXPS3("c26s003_170" , "d") from _call_BlinkXPS3_2653
    meg "*Risa* No le eches la culpa al pobre gato. Me han dicho que estabais ocho personas en esa cama."
    mc "Sí, pero aguantó bien y no se rompió hasta que no subió Zeus."
    if meg._var("route"):
        call KissXPS3("c26s003_175" , "d") from _call_KissXPS3_69
    else:
        scene c26s003_175c with dissolve
    meg "Bueno, me tengo que ir. Debo hacer la colada e ir al supermercado."
    mc "Creo que deberías dejar ropa aquí la próxima vez que vengas. No me refiero a los vestidos para el trabajo, pero algo de ropa casual."
    mc "Cuando vuelvas la semana siguiente, estará limpia, y así sólo necesitas ir y venir con lo que necesites para trabajar."
    call BlinkXPS3("c26s003_180" , "d") from _call_BlinkXPS3_2654
    meg "[mar] me dijo lo mismo, pero no quiero darle más trabajo del necesario."
    mc "Si ella te lo propuso, es porque no le importa. Piénsalo."
    call BlinkXPS3("c26s003_185" , "d") from _call_BlinkXPS3_2655
    if meg._var("route"):
        meg "Lo pensaré. Si decido hacerlo antes de que vengas a verme a Westport, quizá te dé un poco de ropa para que la traigas."
        meg "Así podré venir con una maleta más pequeña, solo con los vestidos. Y no tendrás que cargarla arriba y abajo."
    else:
        meg "Lo pensaré. Si decido hacerlo, podré venir con una maleta más pequeña dentro de dos semanas, solo con los vestidos."
        meg "Y no tendrás que ir arriba y abajo con ella."
    mc "Me parece una buena idea."
    call BlinkXPS3("c26s003_190" , "d") from _call_BlinkXPS3_2656
    if meg._var("route"):
        meg "Te veo el fin de semana, o cuando quieras pasar por mi apartamento."
    else:
        meg "Te veo el fin de semana que viene."
    mc "Conduce con cuidado."
    scene c26s003_175c with dissolve
    stop music fadeout (1.5)
    "Os dais un abrazo de despedida antes de que suba al coche."
    scene black with dissolve
    return
label c26s002_Solomon:
    if _in_replay:
        $ mc._var("relationships", 0, "set")
        call mrS3_kia_route from _call_mrS3_kia_route_8
        call mrS3_oma_route from _call_mrS3_oma_route_4
        call mrS3_rels from _call_mrS3_rels_15
    scene black with dissolve
    play music ("music/Throne-King.ogg")
    "Mientras [sai] te enseñaba las fotos, en la comisaría..."
    scene c26s002_200a with dissolve
    sol "Buenos días, Agente. Le traigo lo que me pidió."
    call BlinkXPS3 ("c26s002_205" , "d") from _call_BlinkXPS3_2657
    oma "Bien. Se ha tomado su tiempo. Ha tardado una semana entera."
    scene c26s002_200b with dissolve
    sol "Lo siento... No me lo han entregado hasta hoy. No he podido hacerlo antes."
    call BlinkXPS3 ("c26s002_210" , "d") from _call_BlinkXPS3_2658
    oma "Bueno, vamos a ir a entregarlo."
    scene c26s002_210d with dissolve
    oma "¡Schrute! Sustitúyeme en el mostrador. Tengo que acompañar a este señor a un sitio."
    "Schrute" "*Desde la parte de atrás* No te preocupes, ahora voy."
    scene c26s002_200c with dissolve
    sol "¿Vamos a ir ahora? ¿Tengo que ir yo también?"
    call BlinkXPS3 ("c26s002_215" , "d") from _call_BlinkXPS3_2659
    oma "Sí, tiene que venir. Aunque sea tan solo por una vez en su vida, compórtese como un hombre."
    oma "Si quiere comportarse como una damisela asustada, puedo llamar a mi hermana la rubia para que le... 'ayude'... a encontrar sus cojones."
    scene c26s002_200d with dissolve
    sol "¡Vale, vale! Vamos..."
    scene c26s002_200e with fade
    "Un par de minutos después, en la puerta de la biblioteca..."
    sol "¿Estoy bien?"
    call BlinkXPS3 ("c26s002_220" , "d") from _call_BlinkXPS3_2660
    oma "No creo que hayas estado bien en tu vida, [sol]."
    oma "Además, no te iba a servir de mucho. No va a volver contigo aunque ella quisiera."
    scene c26s002_200f with dissolve
    sol "¿Aunque ella quisiera? ¿Significa eso que hay una oportunidad?"
    call BlinkXPS3 ("c26s002_225" , "d") from _call_BlinkXPS3_2661
    oma "No. Significa que si, por alguna razón desconocida, quisiera volver contigo, haría lo posible para que la encerraran en un psiquiátrico antes de dejarle hacerlo."
    oma "Pero no te preocupes. No tienes ninguna oportunidad. Por primera vez es libre y está descubriendo lo que es vivir. Sin ti."
    scene c26s002_200g with dissolve
    sol "No he sido tan malo... Los hay peores."
    call BlinkXPS3 ("c26s002_230" , "d") from _call_BlinkXPS3_2662
    oma "Sí, los hay que asesinan a sus mujeres porque dicen que las quieren. Creo que es la única categoría peor que tú."
    oma "Además, tú eres más patético."
    oma "Vamos dentro antes de que vomite del asco que me das."
    call BlinkXPS3 ("c26s002_235" , "f") from _call_BlinkXPS3_2663
    kia "¡[sol]! ¿Qué haces aquí? ¿Y tú, [oma]?"
    call BlinkXPS3 ("c26s002_240" , "d") from _call_BlinkXPS3_2664
    oma "No te preocupes, ha sido idea mía. Y le acompaño para que no intente nada raro."
    oma "[sol], di lo que tengas que decir."
    scene c26s002_200h with dissolve
    sol "Venía a entregarte esto... pero sólo si quieres..."
    sol "Si quieres... puedes volver a casa..."
    call BlinkXPS3 ("c26s002_245" , "d") from _call_BlinkXPS3_2665
    kia "¿Qué es?"
    call BlinkXPS3 ("c26s002_250" , "d") from _call_BlinkXPS3_2666
    stop music fadeout (1.5)
    oma "Ábrelo, [kia]. Por temas legales, digamos que te lo he entregado yo."
    call BlinkXPS3 ("c26s002_255" , "h") from _call_BlinkXPS3_2667
    play music ("music/Looking-Forward.ogg")
    kia "¿El divorcio? ¿Me estás pidiendo el divorcio?"
    scene c26s002_200i with dissolve
    sol "No es que yo quiera, pero..."
    call BlinkXPS3 ("c26s002_260" , "d") from _call_BlinkXPS3_2668
    oma "[sol], ya te puedes ir. Ni siquiera deberías estar aquí para entregar los papeles."
    oma "Eso va en contra de las condiciones con las que has pedido el divorcio."
    scene c26s002_200j with dissolve
    sol "¡Pero ha sido usted quien me ha dicho que debía venir yo!"
    call BlinkXPS3 ("c26s002_265" , "d") from _call_BlinkXPS3_2669
    oma "No quería perderme ver cómo lloriqueabas hasta el último momento."
    call BlinkXPS3 ("c26s002_270" , "d") from _call_BlinkXPS3_2670
    kia "Espera un momento, [oma]."
    kia "Aquí pone que me cedes la casa... Bueno, tu mitad de la casa."
    scene c26s002_200k with dissolve
    sol "Es lo que me dijo la Agente Martinez. Además, sin trabajo no puedo pagar la hipoteca y la acabaría perdiendo."
    sol "Me iré a vivir con un amigo de mi antiguo trabajo y con su novia hasta que encuentre algo."
    call BlinkXPS3 ("c26s002_275" , "d") from _call_BlinkXPS3_2671
    kia "¿También me das los ahorros?"
    scene c26s002_200l with dissolve
    sol "La Agente Martinez..."
    call BlinkXPS3 ("c26s002_280" , "d") from _call_BlinkXPS3_2672
    kia "Los ahorros te los puedes quedar para empezar de nuevo. No hay mucho y el valor de la casa es mayor, con lo que me parece justo."
    call BlinkXPS3 ("c26s002_285" , "d") from _call_BlinkXPS3_2673
    oma "[kia], esto no lo tenéis que discutir ahora. Te hemos... te he entregado los papeles y ahora tienes 30 días para responder a la petición."
    oma "La división de bienes puede venir después, y lo ideal sería que fuera con ayuda de un abogado. Hay que hacer una Declaración de Bienes y otras cosas."
    call BlinkXPS3 ("c26s002_290" , "d") from _call_BlinkXPS3_2674
    kia "Lo entiendo... Creía que... En las películas..."
    call BlinkXPS3 ("c26s002_295a" , "d") from _call_BlinkXPS3_2675
    oma "No te preocupes, no es complicado. Te ayudaremos con lo que necesites."
    oma "Tienes que firmar el recibo como que te he entregado los papeles y dármelo. No tienes que firmar los papeles aún."
    call BlinkXPS3 ("c26s002_295b" , "d") from _call_BlinkXPS3_2676
    oma "[sol], te puedes marchar."
    scene c26s002_200m with dissolve
    sol "Aún podemos arreglarlo..."
    call BlinkXPS3 ("c26s002_295b" , "d") from _call_BlinkXPS3_2677
    oma "[sol], vete antes de que me arrepienta de haberte dado esta oportunidad."
    call BlinkXPS3 ("c26s002_300" , "f") from _call_BlinkXPS3_2678
    "[sol] se va inmediatamente."
    "[kia] firma el recibo y se lo entrega a [oma]..."
    kia "¿Le has obligado a hacer esto? ¿Cómo?"
    call BlinkXPS3 ("c26s002_305" , "d") from _call_BlinkXPS3_2679
    oma "Vino a comisaría a poner una denuncia falsa contra [mc] por lo que pasó en la fiesta de cumpleaños. Ese día estaba yo en el mostrador."
    oma "Le di a elegir entre la cárcel y pedirte el divorcio. Lloriqueó un poco con lo de ser católico antes de aceptar."
    oma "Supongo que sus convicciones religiosas no son tan fuertes como su miedo a acabar en prisión."
    oma "Por lo que pudiera ser, le he dicho que no se acercara a menos de un metro del mostrador. No me fío de él."
    call BlinkXPS3 ("c26s002_310" , "d") from _call_BlinkXPS3_2680
    kia "Siempre ha sido un cobarde y un mentiroso..."
    scene c26s002_315d with dissolve
    pause (0.9)
    scene c26s002_315e with dissolve
    pause (0.9)
    call BlinkXPS3 ("c26s002_315" , "h") from _call_BlinkXPS3_2681
    kia "Gracias, [oma]. Nunca lo habría logrado sin ti."
    oma "No tienes por qué darme las gracias. En esta familia estamos para ayudarnos entre nosotras, ¿no?"
    call BlinkXPS3 ("c26s002_320" , "d") from _call_BlinkXPS3_2682
    oma "Me sentí muy mal cuando fuimos a tu antigua casa y me tuve que ir poco antes de que [sol] llegara. Afortunadamente, [mc] estaba allí."
    oma "Esta vez, he podido ayudar sin tener que depender de que él haga algo."
    call BlinkXPS3 ("c26s002_325" , "d") from _call_BlinkXPS3_2683
    kia "No tienes que sentirte mal, [oma]. No podéis estar todo el día para protegerme de [sol]."
    call BlinkXPS3 ("c26s002_330" , "d") from _call_BlinkXPS3_2684
    oma "Parece que, con un poco de suerte, ya no será necesario."
    call BlinkXPS3 ("c26s002_335" , "d") from _call_BlinkXPS3_2685
    kia "Gracias a ti."
    if kia._var("route") and oma._var("route"):
        call BlinkXPS3 ("c26s002_340" , "d") from _call_BlinkXPS3_2686
        oma "Hablando de [mc]..."
        call BlinkXPS3 ("c26s002_345" , "d") from _call_BlinkXPS3_2687
        kia "*Risa* Me parece que nos pasamos la vida hablando de él."
        call BlinkXPS3 ("c26s002_350" , "d") from _call_BlinkXPS3_2688
        oma "*Risa* Tienes razón. Todo esto es muy nuevo..."
        call BlinkXPS3 ("c26s002_355" , "d") from _call_BlinkXPS3_2689
        if mc._var("relationships")==2:
            kia "Para ti, pero también para mí..."
        else:
            kia "Para ti, para mí, y para todas nosotras..."
        kia "Pero dime, ¿de qué querías hablar sobre él?"
        call BlinkXPS3 ("c26s002_360" , "d") from _call_BlinkXPS3_2690
        oma "Es sobre el anillo que te dio..."
        if mc._var("relationships")==2:
            oma "He pensado que..."
        elif mc._var("relationships")==3:
            oma "Lo estuvimos hablando el otro día con..."
        else:
            oma "He hablado con las chicas y..."
        scene black with dissolve
        "Las dos mujeres pasan un rato hablando y haciendo planes, hasta que cada una tiene que volver a sus obligaciones."
    else:
        "Las dos mujeres pasan un rato abrazadas hasta que cada una tiene que volver a sus obligaciones."
        scene black with dissolve
    stop music fadeout (1.5)
    return
label c26s003_SaiSex:
    if _in_replay:
        $ mc._var("relattionsips", 0, "set")
        call mrS3_deb_route from _call_mrS3_deb_route_11
        call mrS3_eil_route from _call_mrS3_eil_route_5
        menu:
            "¿Estás en una relación con [dap], [sca], [eri], [emm], [sim], o [eva]?"
            "Sí, con todas ellas.":
                $ dap._var("route" , True)
                $ sca._var("route" , True)
                $ eri._var("route" , True)
                $ emm._var("route" , True)
                $ eva._var("route" , True)
                $ sim._var("route" , True)
                $ mc._var("relattionsips", 6, "add")
            "Sí, pero no con todas ellas.":
                call mrS3_dap_route from _call_mrS3_dap_route_8
                call mrS3_sca_route from _call_mrS3_sca_route_8
                call mrS3_eri_route from _call_mrS3_eri_route_9
                call mrS3_emm_route from _call_mrS3_emm_route_14
                call mrS3_sim_route from _call_mrS3_sim_route_4
                if dap._var("route") and sca._var("route") and eri._var("route") and emm._var("route") and sim._var("route"):
                    pass
                else:
                    call mrS3_eva_route from _call_mrS3_eva_route_11
            "No, con ninguna.":
                $ dap._var("route" , False)
                $ sca._var("route" , False)
                $ eri._var("route" , False)
                $ emm._var("route" , False)
                $ eva._var("route" , False)
                $ sim._var("route" , False)
    scene c26s003_195a with fade
    "Cuando llegas a la planta de las estudiantes, [sai] ya no está en el sofá."
    scene c26s003_195b with dissolve
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "[sai], soy yo. ¿Puedo pasar?"
    sai "*A través de la puerta* Dame un minuto para que acabe con una cosa."
    "Esperas un par de minutos."
    scene c26s003_195b with fade
    sai "*A través de la puerta* Ya puedes pasar."
    "Por suerte los minutos de [sai] solo duran el doble de los de la mayoría de los hombres."
    play music ("music/RayOfHope.ogg")
    scene c26s003_200d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c26s003_200" , "d") from _call_BlinkXPS3_2691
    mc "¡Por el amor de Dios, [sai]! ¡Estás increíble!"
    call addProfileImageS3 (7, "saira_7", sai, _(": 15 - Especial"), "") from _call_addProfileImageS3_15
    sai "Gracias. Me alegra que te guste."
    mc "Antes me has dicho que necesitabas mi ayuda. ¿Necesitas ayuda para quitarte eso?"
    mc "Va a ser una lástima tener que quitártelo. ¿Te puedes dejar las medias? ¿O los zapatos? ¿O los guantes? ¿O como se llame eso del cuello?"
    call BlinkXS3 ("c26s003_205") from _call_BlinkXS3
    sai "*Risa* Parece que te has acelerado de golpe al verme. No pareces decidirte sobre qué me tengo que dejar puesto."
    sai "Pero no has dicho nada del antifaz."
    mc "Por nada del mundo me perdería los ojos más bonitos del universo."
    call BlinkXS3 ("c26s003_210") from _call_BlinkXS3_1
    sai "Me vas a hacer ruborizar..."
    mc "Te pones guapísima cuando te ruborizas." id c26s003_SaiSex_7be16e5c
    mc "Pero tú no has dicho qué te puedes dejar puesto. O qué quieres dejarte puesto..."
    scene c26s003_215d with dissolve
    pause (1.5)
    call BlinkXS3 ("c26s003_215") from _call_BlinkXS3_2
    sai "Me querría dejar puesto todo lo que has pedido, pero no puedo."
    mc "¿Por qué? ¿Es incómodo?"
    call BlinkXS3 ("c26s003_220") from _call_BlinkXS3_3
    sai "No es eso. La lencería no es mía. Al menos no todavía."
    mc "¿De quién es? ¿Ahora os prestáis lencería entre vosotras?"
    call BlinkXS3 ("c26s003_225") from _call_BlinkXS3_4
    sai "Aún no hemos llegado a eso. *Risa* La lencería es muy personal."
    sai "Esta la compró [emm] para [nor] cuando estuvisteis en Monterey, pero no calculó bien la talla de [nor] y no le queda bien."
    call BlinkXS3 ("c26s003_230") from _call_BlinkXS3_5
    sai "Me la ha prestado para que me la pruebe y, si me queda bien, me la regalará. Si no me queda bien, la cambiará por una de su talla, y de color rojo."
    sai "¿Tú qué opinas? ¿Debería quedármela?"
    mc "Creo que, si te gusta, te la puedes quedar. Te queda espectacular."
    mc "*Risa* Y una vez hemos decidido que te la vas a quedar, ¿qué partes te vas a dejar puestas?"
    call BlinkXS3 ("c26s003_235") from _call_BlinkXS3_6
    sai "No seas insistente. *Risa* No me voy a dejar nada puesto hasta que no sea oficialmente mío."
    sai "Pero viendo los ojos hambrientos con los que me miras, me parece que le diré que me la quedo."
    mc "Me parece una idea excelente. La próxima vez que tengamos un rato a solas, podemos usarla."
    call BlinkXS3 ("c26s003_240") from _call_BlinkXS3_7
    sai "Yo esperaba que la próxima vez fuera... ahora. No tengo clase hasta dentro de casi dos horas."
    mc "Esa idea me parece más excelente todavía. Supongo que no puedo colaborar en quitarte la lencería."
    scene c26s003_240d with dissolve
    sai "Me moriría de vergüenza si le tengo que decir a [nor] que me quedo su lencería porque la has roto."
    sai "Voy a quitármela al lavabo. Te conozco demasiado y sé que no podrías tener las manos quietas."
    sai "Espérame en la cama. No hace falta que te dejes nada de ropa; ya sabes que no soy fetichista con eso."
    mc "¡No es un fetiche! *Risa* Tan sólo me encanta cómo te queda esa lencería. Y me encantan los tacones."
    scene c26s003_240e with dissolve
    sai "Cielo... eso es la definición de fetiche. *Risa*"
    scene c26s003_240f with dissolve
    "Se encierra en el lavabo para desnudarse. Casi consigues desnudarte antes de que se cierre la puerta."
    call BlinkXPS3 ("c26s003_245" , "f") from _call_BlinkXPS3_2692
    "Sale al cabo de unos minutos, con la preciosa lencería con la que nació. Y, desafortunadamente, descalza."
    sai "Tienes cara de decepcionado."
    mc "¿Decepcionado? Nada más lejos de la realidad. Me encantas al natural."
    mc "Por un momento me he imaginado que traerías los zapatos. Esos son tuyos."
    call BlinkXS3 ("c26s003_250") from _call_BlinkXS3_8
    sai "¿Desnuda y con tacones? *Risa* ¿Sin las medias? ¿Por quién me has tomado? ¡Quedarían feísimos!"
    sai "Además, con esos tacones soy más alta que tú, y prefiero que sea al revés."
    call BlinkXS3 ("c26s003_255") from _call_BlinkXS3_9
    if deb._var("route"):
        sai "Y no digo que no hagas una buena pareja con [deb.nick], pero..."
    sai "Me gusta cuando tengo que mirar un poco hacia arriba para mirarte a los ojos."
    stop music fadeout (1.5)
    mc "Entonces será mejor que me ponga de pie."
    scene c26s003_260a with dissolve
    play music ("music/Rumba.ogg")
    "Te levantas y la besas dulcemente. Incluso sin tacones es casi tan alta como tú."
    "Tus manos empiezan a recorrer su cuerpo y te alegras de que la lencería no sea un estorbo."
    "Ni siquiera la seda puede mejorar el suave tacto de su piel desnuda."
    scene c26s003_260b with fade
    "La guías, rodeando la cama y sin dejar de besaros, hasta el lugar en el que has planeado tu próximo movimiento."
    "Dejarte sólo en una habitación con tu vívida imaginación da para hacer muchos planes."
    "La dulzura de los besos ha dejado paso a una pasión desenfrenada."
    scene c26s003_260c with fade
    "La tumbas en la cama suavemente, sin dejar de besarla."
    "Ahora la tienes donde quieres y es el momento de dar el siguiente paso."
    call BlinkXS3 ("c26s003_265") from _call_BlinkXS3_10
    "Interrumpes el beso y miras en los profundos pozos oscuros que son los ojos de la exótica mujer."
    sai "¿Ya se han acabado los besos?"
    mc "No, pero creo que tus labios no son lo suficientemente avariciosos como para acaparar los míos durante las dos horas de las que hablabas."
    call BlinkXS3 ("c26s003_270") from _call_BlinkXS3_11
    sai "Creo que me has entendido mal. Tengo {b}que estar en clase{/b} en menos de dos horas. Debería salir de casa en una hora y cuarto..."
    mc "Entonces, mi plan tiene que acelerarse un poco, pero los pasos son los mismos."
    scene c26s003_260c with dissolve
    "No te quedas mirando su cara de extrañeza y vuelves a besarla."
    scene c26s003_275a with dissolve
    "Tus labios emprenden el camino de los suyos hasta el lugar en que su cuello se une a su clavícula. Uno de sus múltiples puntos sensibles."
    sai "Si tu plan era ponerme la carne de gallina, lo estás consiguiendo."
    sai "Llevo esperando esto desde que te has ido con [meg]."
    scene c26s003_275b with dissolve
    "No puedes contestar con su pezón en la boca. Te educaron para que no hablaras con la boca llena."
    "De todas formas, la piel de gallina formaba parte del plan."
    sai "Puedes seguir con tu plan. *Gemido leve* Los primeros pasos me encantan."
    scene c26s003_275c with dissolve
    "El siguiente paso de tus labios es su terso estómago, con tu nariz rozando su ombligo."
    "Ella arquea la espalda para maximizar el contacto con tu boca. Adoras recorrer el perfecto cuerpo de la estudiante."
    sai "*Risita* Eso hace cosquillas. Pero cosquillas de las buenas."
    mc "Ahora es cuando vienen las cosquillas de verdad..."
    scene c26s003_275d with dissolve
    "Su muslo tiembla cuando tus labios se posan en su cara interior."
    sai "*Gemido* ¡Sabía que ibas a hacer eso! *Gemido*"
    sai "*Jadeo* Conoces cada uno de mis puntos sensibles. *Jadeo*"
    sai "*Gemido* Como se te ocurra saltar al otro muslo, cierro las piernas sobre tus orejas. *Gemido risueño*"
    "La amenaza está hecha en broma, pero conoces a [sai] lo suficiente como para saber que es capaz de llevarla a cabo."
    scene c26s003_275e with dissolve
    "Tu lengua se reencuentra con su clítoris, perfectamente duro e hinchado."
    sai "*Gemido* ¡Dioses! *Jadeo* ¡Casi no podía esperar! *Gemido*"
    "Lo sabes. Siempre ha sido impaciente cuando sabe que tu lengua se acerca a su centro de placer."
    scene c26s003_920pv with dissolve
    show c26s003_920v
    "Ella se acomoda para dejarte hacer a tu ritmo, dándote el espacio que necesitas sin tener que temer por tus orejas."
    sai "*Jadeo* ¿Por qué eres tan bueno haciendo eso? *Gemido*"
    "Otra vez no puedes contestar. Tampoco sabrías qué contestar, con lo que te centras en recorrer los lugares que sabes que la hacen gemir."
    sai "*Gemido* ¡Cómo te voy a echar de menos cuando te vayas a Aruba! *Jadeo*"
    "No es el momento, pero una fugaz imagen tuya usando el avión de la empresa los fines de semana te asalta en un flash."
    scene c26s003_925pv with dissolve
    hide c26s003_920v
    show c26s003_925v
    "Desechas la imagen y te centras en lo que realmente es importante en ese momento. Cada pliegue y cada curva del coño de [sai]."
    sai "*Jadeo* ¡Me encanta! *Gemido*"
    "El sabor característico de la chica asalta cada una de tus papilas gustativas mientras el fresco olor a recién lavada inunda tu nariz."
    "Ha aprovechado el tiempo que has estado con [meg] para prepararse para ti, no sólo poniéndose lencería."
    "Pero el nuevo olor que emana de su húmedo coño está empezando a igualar su olor a jabón."
    scene c26s003_915pv with dissolve
    hide c26s003_925v
    show c26s003_915v
    "Sigues lamiendo, notando cómo [sai] empieza a tensarse. Sus muslos endureciéndose bajo tus dedos en una conocida sensación."
    sai "*Gemido* ¡Estoy a punto de llegar! *Jadeo*"
    "No dejas que tu lengua descanse, recorriendo cada uno de los rincones que sabes que le dan placer, introduciendo la punta dentro de su agujero."
    "Presionas más fuerte cada vez que pasas por su clítoris, suavizando la fuerza que ejerce tu lengua cuando pasas por sus labios."
    "Casi acariciándolos. Cambiando la dirección. Sorprendiéndola."
    call OrgasmXS3 ("c26s003_280") from _call_OrgasmXS3_67
    sai "*GEMIDO* ¡SÍ! *JADEO* ¡OSTIA PUTA! *GEMIDO*"
    "La bella india explota en tu boca, regalándote una enorme cantidad de sus fluidos más íntimos."
    "Cada mujer tiene un sabor diferente. El de [sai] es maravilloso."
    scene c26s003_275f with fade
    "Se derrumba sobre la cama como una muñeca rota. Si no la conocieras tan bien, seguirías lamiendo para prolongar su placer."
    "Pero sabes que ella prefiere que la dejes descansar y recuperar el aliento."
    sai "*Respiración entrecortada* Ha sido increíble. *Gemido* Me encanta mirar cómo me comes. *Jadeo*"
    sai "*Respiración entrecortada* Tenía que haber empezado a hacerlo antes..."
    mc "*Risa* Te lo dije muchas veces..."
    call BlinkXS3 ("c26s003_285") from _call_BlinkXS3_12
    sai "*Gemido* ¡No te rías con tu boca en mi coño! *Jadeo* ¡Está sensible! *Gemido*"
    mc "Lo intentaré, pero tienes que dejar de decir cosas graciosas."
    sai "Túmbate un momento conmigo..."
    call BlinkXPS3 ("c26s003_290" , "f") from _call_BlinkXPS3_2693
    sai "¿Qué cosas graciosas he dicho?"
    mc "Has dicho lo de mirarme como si hubiera sido idea tuya, y me pasé más de un año diciéndote de hacerlo."
    call BlinkXS3 ("c26s003_295") from _call_BlinkXS3_13
    sai "*Risa* Sólo miro a la cara durante el sexo a mi novio, cielo. Y no lo eras."
    mc "¡Eres una capulla! *Risa* ¡No lo era porque tú no querías!"
    call BlinkXS3 ("c26s003_300") from _call_BlinkXS3_14
    sai "*Risa* ¿Vamos a discutir sobre de quién es la culpa o vamos a seguir?"
    sai "Te recuerdo que tengo que ir a clase y seguro que... mi Pequeñín está esperando para entrar en Mami."
    mc "¿Tu Pequeñín?"
    call BlinkXPS3 ("c26s003_305" , "f") from _call_BlinkXPS3_2694
    sai "*Risa* Nunca conseguirás que lo llame Mjolnir. Es y siempre será mi Pequeñín. Y yo siempre seré su Mami."
    sai "La única vez que lo llamé Mjolnir me sentía rara haciéndolo."
    mc "Puedes llamarlo como quieras, no se ofende. Pero... ¿En el borde de la cama? ¿No acabas de decir que te gusta mirarme?"
    call BlinkXS3 ("c26s003_310") from _call_BlinkXS3_15
    sai "¿Estás en baja forma? ¿Sólo vamos a hacer una postura?"
    mc "Uhh... No..."
    call BlinkXS3 ("c26s003_315a") from _call_BlinkXS3_16
    sai "Entonces empecemos así. Los clásicos nunca pasan de moda. Y aunque me encante mirarte, también me encanta así."
    mc "Como desees. Pero tienes que prometerme que en la siguiente postura podré mirar esos hermosos ojos."
    call BlinkXS3 ("c26s003_315b") from _call_BlinkXS3_17
    sai "*Risa* ¡Tú quieres reírte de las caras que pongo!"
    mc "*Risa* Te prometí no reírme y no lo voy a hacer. Aunque sean muy graciosas."
    sai "¿Ves? *Risa* ¡Dices que pongo caras raras!"
    mc "Raras no, graciosas."
    scene c26s003_320a with fade
    mc "¿Preparada?"
    sai "Sí. El Pequeñín y yo ya nos conocemos, con lo que no hace falta que te contengas."
    sai "No soy una virgen con la que tengas que ir con cuidado."
    if dap._var("route") or eri._var("route") or emm._var("route") or sca._var("route") or sim._var("route") or eva._var("route"):
        "No sabes si es un comentario casual o una referencia a alguna de las chicas vírgenes con las que has estado. [sai] incluida."
    else:
        "Lo sabes. Vivisteis juntos el momento en que dejó de serlo."
    scene c26s003_320An with dissolve
    "La penetras profundamente. La estrechez de su túnel es compensada por la lubricación provocada por su orgasmo anterior. Mjolnir se siente como en casa."
    "Nunca pensarás en él como en 'El pequeñín'."
    sai "*Gemido* ¡Sí! *Jadeo* ¡Mami había echado de menos al pequeñín! *Gemido*"
    if sim._var("route"):
        "Mjolnir parece ignorar el mote que, aparte de [sai], sólo usa [sim]."
    else:
        "Mjolnir parece ignorar el mote. Por suerte sólo [sai] lo llama así."
    scene c26s003_900pv with dissolve
    hide c26s003_915v
    show c26s003_900v
    "Le haces caso y no vas con cuidado. No es la posición más cómoda, ni para ti ni para ella, pero notar cómo su cuerpo se estremece a cada embestida la hace excelente."
    sai "*Jadeo* ¡Así! *Gemido* ¡Tierno pero con fuerza! *Jadeo*"
    "No eres capaz de imaginar de dónde ha sacado la idea de que estás haciéndolo tiernamente."
    sai "*Gemido* ¡Me encanta! *Jadeo* ¡Veo chispas de colores cada vez que llegas al fondo! *Gemido*"
    "Parece que Mjolnir no solo es afrodisiaco, sino también alucinógeno."
    if eva._var("route"):
        mcp "(¿Tiene razón [eva] en que tengo una polla mágica? *Risa mental*)"
    scene c26s003_910pv with dissolve
    hide c26s003_900v
    show c26s003_910v
    "Tu ritmo va cambiando cíclicamente, para que la preciosa mujer que aprisionas contra el colchón no sepa a qué velocidad la vas a embestir."
    sai "*GEMIDO* ¡OH, SÍ! *JADEO* ¡Esos cambios de ritmo me están matando... de placer! *GEMIDO*"
    "Sabes que vas a poder mirarla a la cara en breve, pero desearías poder hacerlo ahora que sus gemidos están aumentando de volumen."
    sai "*JADEO* ¡VOY A ORDEÑARTE HASTA LA ÚLTIMA GOTA! *GEMIDO* ¡Toda esa leche va a ser mía! *JADEO*"
    "Conoces a [sai] lo suficiente como para saber que lo va a intentar. Casi siempre ha preferido que te corras dentro."
    scene c26s003_905pv with dissolve
    hide c26s003_910v
    show c26s003_905v
    "Sus movimientos se empiezan a hacer más erráticos, pero es demasiado pronto para que se corra por segunda vez."
    sai "*GEMIDO* ¡PODRÍA HACER ESTO DURANTE HORAS! *JADEO* ¡ODIO LAS CLASES! *GEMIDO*"
    "Habías olvidado por completo que tenía que ir a la universidad y que el tiempo era limitado. Sus movimientos erráticos se deben a que ella también lo ha recordado ahora."
    "Ella siempre ha adorado ir a clase, tan solo el sexo lo hace odiar tener que ir."
    sai "*JADEO* ¡ODIO QUE SEAS TAN BUENO EN ESTO! *GEMIDO*"
    "Sabes que no es cierto. Los estremecimientos que la recorren te indican lo mucho que está disfrutando."
    call BlinkXS3 ("c26s003_325") from _call_BlinkXS3_18
    "[sai] se queda quieta por un momento."
    sai "*GEMIDO* Cambiemos de postura *JADEO*"
    mc "¿Estás a punto de correrte?"
    sai "*Jadeo* No, pero... después de haberlo probado... *Gemido* me gusta más hacerlo mirándote. *Jadeo*"
    call BlinkXS3 ("c26s003_330") from _call_BlinkXS3_19
    "Hacéis un cambio rápido de posición, en la que ella se sitúa encima. Hay cosas que no cambian. La guerra y el sexo."
    sai "*Gemido* Así mejor... *Jadeo* Y no me hagas gritar tanto... *Gemido*"
    mc "*Risa* ¿Por qué? Nunca has sido de las silenciosas."
    scene c26s003_930pv with dissolve
    hide c26s003_905v
    show c26s003_930v
    "Aprovechando su posición, empieza a moverse a un ritmo lento y maravilloso. Su pelo cae encima de tu cara, como una caricia peluda."
    "Ha elegido una posición en la que, tal como ha dicho, va a poder ordeñarte sin que puedas hacer nada por evitarlo."
    sai "*Gemido* [kat] se ha quedado estudiando en su habitación. *Jadeo* No quiero molestarla. *Gemido*"
    "La habitación de [kat] está al otro lado del descansillo, pero en esta casa se oye todo."
    sai "*Jadeo* Sé que está lejos, pero... *Gemido* Me conozco y conozco mis gemidos. *Jadeo*"
    "Con el volumen que estaban alcanzando sus gemidos, te preguntas si molestaríais a las estudiantes que hay en el campus."
    scene c26s003_935pv with dissolve
    hide c26s003_930v
    show c26s003_935v
    "El rítmico movimiento de las caderas de [sai] empiezan a acercarte a tu clímax. Aún puedes retenerlo, esperando a vuestro orgasmo compartido."
    sai "*Gemido* Esto es muchísimo mejor. *Jadeo* Cara a cara hay muchas posturas que quiero probar. *Gemido*"
    "Vais a tener tiempo de probar todas las que podáis imaginar en los siguientes años. Incluso de investigar las que no podáis imaginar."
    sai "*Jadeo* Tengo que investigar nuevas posturas. *Gemido* Pero esta me encanta. *Jadeo*"
    "Hay un dicho sobre las grandes mentes, pero no lo puedes recordar. Sufres de una falta de sangre en el cerebro."
    "Mjolnir es un acaparador de sangre."
    scene c26s003_945pv with dissolve
    hide c26s003_935v
    show c26s003_945v
    "Su pelo, cada vez más alborotado, sigue haciéndote cosquillas en la cara y en el pecho, pero no es capaz de tapar las preciosas vistas de las tetas de [sai]."
    "Al menos no en su totalidad. Entre tanto pelo, lo de mirarte a la cara mientras hacéis el amor es casi una quimera."
    sai "*GEMIDO* ¡Me estoy acercando muy rápido! *JADEO*"
    "Lo de no gemir tan alto ha quedado como un deseo inalcanzable del pasado."
    sai "*JADEO* ¡ESTOY A PUNTO DE CORRERME! *GEMIDO*"
    "Sus paredes interiores empiezan a estrujar a Mjolnir. ¿A punto de correrse? ¡Casi ha empezado!"
    mc "Hazlo. No te preocupes por mí."
    call OrgasmXS3 ("c26s003_335") from _call_OrgasmXS3_68
    sai "*GEMIDO* ¡HOLY SHIT! *JADEO* ¡TE QUIERO! *GEMIDO*"
    "Ciertamente, tan solo era un deseo inalcanzable."
    "La hermosa mujer explota alrededor de Mjolnir, mientras oleadas de presión lo recorren."
    "Todo su cuerpo se queda paralizado por un segundo antes de reanudar sus movimientos."
    scene c26s003_940pv with dissolve
    hide c26s003_945v
    show c26s003_940v
    "Esos movimientos que, unidos al masaje que su coño está haciendo sobre tu polla, te acercan a tu propio orgasmo a pasos agigantados."
    sai "*JADEO* ¡SIGUE ASÍ! *GEMIDO* ¡NO PARES! *JADEO*"
    "Casi se te escapa la risa debido a que es ella quien está haciendo todo el trabajo. Un maravilloso trabajo."
    mc "Estoy a punto de correrme, [sai]."
    sai "*GEMIDO* ¡NO ME PIENSO BAJAR DE AQUÍ! *JADEO* ¡HAZLO DENTRO! *GEMIDO*"
    "No tienes más opción que cumplir sus órdenes si no quieres quitártela de encima por la fuerza."
    if persistent.pregnancy and not sai._var("pregnant"):
        if persistent.walkthrough:
            $ wt1 = _("[sai] embarazada.")
            $ wt2 = _("Sin consecuencias.")
        else:
            $ wt1 = ""
            $ wt2 = ""
        menu:
            "Correrte dentro. Ir a por el bebé." (wt = wt1):
                $ sai._var("pregnant", True)
                $ sai._var("undiscoveredPregnancy", True)
                play sound ("music/OldMusicBox5.ogg")
            "Correrte dentro." (wt = wt2):
                pass
    $ resetWalkthrough ()
    call OrgasmXS3 ("c26s003_340") from _call_OrgasmXS3_69
    mc "¡Mpfft!"
    "Es tu turno de explotar, llenando el útero de la hermosa chica que te aprisiona contra el colchón."
    sai "*JADEO* ¡SÍ! *GEMIDO* ¡DÁMELA TODA! *JADEO*"
    "Y se la das toda. Le das tanta leche que un poco se escapa del abrazo de su coño."
    call BlinkXPS3 ("c26s003_345" , "f") from _call_BlinkXPS3_2695
    "Unos segundos después, cuando la belleza que tienes encima recupera el aliento y te descabalga..."
    sai "Ha sido increíble, como siempre, pero diferente."
    mc "Siempre es diferente, cielo. *Risa* El día que nos volvamos repetitivos deberemos empezar a preocuparnos."
    call BlinkXS3 ("c26s003_350") from _call_BlinkXS3_20
    sai "No me refiero a eso. Tan solo se siente diferente. La última vez fue la primera vez desde que llegué."
    sai "Era como volvernos a encontrar después de una pausa. Había deseo y ansiedad."
    call BlinkXS3 ("c26s003_355") from _call_BlinkXS3_21
    sai "Esta vez es como... no sé... como si fuera la primera vez del resto de nuestras vidas."
    sai "Como si haber aceptado que estoy loca por ti le hubiera dado un significado diferente."
    mc "Me gusta como suena eso, 'La primera vez del resto de nuestras vidas'."
    mc "Quizás tienes razón y hoy ha sido más natural que la última vez, después del Jazz Corner."
    mc "Como si fuera nuestra primera vez saliendo juntos, sin tener que demostrarnos nada a nosotros mismos."
    call BlinkXS3 ("c26s003_360") from _call_BlinkXS3_22
    sai "Creo que es exactamente eso. Es nuestra segunda vez como pareja 'real'. La primera fue fantástica y ésta la ha mejorado."
    sai "No mentía cuando he dicho que me podría pasar horas haciendo esto."
    stop music fadeout (1.5)
    mc "Yo también, pero tienes que ir a clase."
    call BlinkXPS3 ("c26s003_365" , "h") from _call_BlinkXPS3_2696
    play music ("music/SaveMe.ogg")
    sai "¿Qué hora es?"
    mc "No tengo ni idea. Mi móvil se ha quedado en los pantalones."
    sai "El mío en el bolso. Déjame ir a mirarlo."
    scene c26s003_370d with fade
    "[sai] se levanta y empieza a revolver en su bolso, buscando el móvil."
    call BlinkXS3 ("c26s003_370") from _call_BlinkXS3_23
    sai "Creo que voy a tener que echarte. Me quiero duchar antes de ir a clase."
    mc "*Risa* Y supongo que no puedo enjabonarte la espalda, ¿verdad?"
    call BlinkXS3 ("c26s003_375") from _call_BlinkXS3_24
    sai "*Risa* Será mejor que no lo hagas si quieres que tu novia apruebe el curso."
    mc "Entonces me tendré que vestir e irme. Pero lo hago contra mi voluntad. *Risa* Enjabonarte es una forma de ayudarte a que vayas más rápido."
    call BlinkXS3 ("c26s003_380") from _call_BlinkXS3_25
    sai "*Risa* Que vaya más rápido hacia suspender la asignatura, ¿no?"
    sai "Si entras en esa ducha, los dos sabemos cómo acabará."
    mc "*Fingiendo estar ofendido* ¡[sai]! ¿Me estás tratando como si fuera tan solo una polla con piernas? *Risa*"
    call BlinkXS3 ("c26s003_385") from _call_BlinkXS3_26
    sai "No, cielo. Por impresionante que sea El Pequeñín, lo mejor de ti está en tu cabeza."
    mc "*Risa* ¿Mi pelazo?"
    call BlinkXS3 ("c26s003_390") from _call_BlinkXS3_27
    sai "*Risa* No, idiota. Es cómo piensas, y cómo siempre tratas de pensar en todo el mundo antes que en ti mismo."
    mc "¿Tú también vas a empezar a llamarme idiota? *Risa* Voy a tener que prohibirte que pases tanto tiempo con [eil]."
    scene c26s003_390d with dissolve
    "Te da un dulce beso que sabe a despedida. Sabes que tiene que ir a ducharse o no llegará a clase."
    call BlinkXS3 ("c26s003_395") from _call_BlinkXS3_28
    sai "Atrévete a prohibirnos algo a cualquiera de las dos."
    mc "*Risa* Supongo que si lo hiciera, mi integridad física correría peligro."
    call BlinkXS3 ("c26s003_400") from _call_BlinkXS3_29
    if eil._var("route"):
        sai "*Risa* Puedes estar seguro de eso. Eres nuestro novio, no nuestro amo."
        sai "Aunque sé que lo dices en broma, prohibirnos algo así está fuera de tus atribuciones."
    else:
        sai "*Risa* Puedes estar seguro de eso. Eres mi novio, no mi amo."
        sai "Aunque sé que lo dices en broma, prohibirme algo así está fuera de tus atribuciones."
    mc "Nunca lo haría. Ver cómo os lleváis es una de las mayores sorpresas desde que he vuelto a casa."
    mc "Y he recibido un montón de sorpresas."
    scene c26s003_400d with dissolve
    sai "Y las que te quedan por recibir."
    mc "¿Cómo cuáles?"
    sai "Ten paciencia y las recibirás a su debido tiempo."
    scene c26s003_400e with dissolve
    "Y con esa enigmática frase, cierra la puerta del baño, dejándote intrigado sobre qué estará preparando."
    "¿Lo está preparando ella sola o es entre varias?"
    stop music fadeout (1.5)
    "Sabes que insistir no te va a dar ninguna de las respuestas que corren por tu cabeza ahora mismo, con lo que decides vestirte e irte."
    scene c26s003_400f with fade
    "De camino a la cocina para hidratarte un poco bebiendo mucha agua..."
    play music ("music/MeganMoan.ogg")
    kat "*Desde su habitación* ¡SÍ! *GEMIDO* ¡DÁMELA TODA A MÍ TAMBIÉN! *JADEO*"
    mcp "*Risa mental* ([sai] estaba preocupada por si molestábamos a [kat] mientras estudiaba. Parece que ya ha acabado de estudiar.)"
    stop music fadeout (1.5)
    return
label c26s003_NoSai:
    scene c26s003_1000 with fade
    play music ("music/RayOfHope.ogg")
    "Vuelves a tu habitación y juegas un rato a My Residence."
    "Tienes una tórrida escena con Aishwarya, la chica India que se aloja con la familia alien."
    "Te estás empezando a volver paranoico."
    "Después de que [deb.nick] te dijera que Vee y Mandy se parecen a [eva] y [ama], les ves parecido a las chicas del juego con las mujeres de la casa."
    "Aishwarya te recuerda a [sai], y no solo porque sean del mismo país."
    "Después de jugar su escena, bajas a beber algo a la cocina."
    stop music fadeout (1.5)
    return
label c26s004_MarEmm:
    if _in_replay:
        call mrS3_mar_route from _call_mrS3_mar_route_13
        call mrS3_emm_route from _call_mrS3_emm_route_15
    scene c26s004_005a with dissolve
    "Mientras tanto, en la cocina..."
    play music ("music/LifeOfAWanderingWizard.ogg")
    emm "Entonces, ¿qué debería hacer con el dinero?"
    mom "Creo que la idea de [mc] de que lo administres durante un año es buena."
    call BlinkXS3 ("c26s004_010") from _call_BlinkXS3_30
    mom "Las necesidades básicas las vas a tener cubiertas en casa, y es un montón de dinero para tus caprichos."
    mom "Hay muchas familias que viven con mucho menos durante un año."
    call BlinkXS3 ("c26s004_015") from _call_BlinkXS3_31
    emm "¡No son caprichos, necesito un coche!"
    call BlinkXS3 ("c26s004_020") from _call_BlinkXS3_32
    mom "¿Para qué?"
    call BlinkXS3 ("c26s004_025") from _call_BlinkXS3_33
    emm "Para ir a la universidad... No quiero coger el bus cada día."
    call BlinkXS3 ("c26s004_030") from _call_BlinkXS3_34
    mom "Son 30 minutos andando, y menos aún en bicicleta."
    mom "Además, cuando [mc] se vaya a Aruba podrás coger su camioneta si es necesario. O si no, mi coche."
    call BlinkXS3 ("c26s004_035") from _call_BlinkXS3_35
    emm "Pero así podría llevar a las chicas..."
    call BlinkXS3 ("c26s004_040") from _call_BlinkXS3_36
    mom "¿A qué chicas? [dap], [eri], [sca], y tú casi llenáis un coche. ¿A quién más vas a llevar?"
    mom "[deb.nick], [sai], [lis], [kim], [kat]... Solo puedes elegir una."
    mom "Y faltan por llegar las seis chicas que se alojarán en casa de tu tía."
    call BlinkXS3 ("c26s004_045") from _call_BlinkXS3_37
    emm "Pues casi debería comprarme un autobús. *Risa*"
    emm "Y si me dejas coger tu coche, ¿por qué las chicas van en bus?"
    call BlinkXS3 ("c26s004_050") from _call_BlinkXS3_38
    mom "Les dije que lo podían coger si lo necesitaban. Ninguna de ellas ha querido cogerlo aún."
    mom "Prefieren ir en autobús juntas si coinciden en los horarios. Sólo [kat] lo ha cogido una vez."
    mom "Con lo que, una vez descartada la necesidad del coche, sigamos con el resto de caprichos."
    call BlinkXS3 ("c26s004_055") from _call_BlinkXS3_39
    emm "¡La ropa no es un capricho! ¡No tengo nada que ponerme!"
    call BlinkXS3 ("c26s004_060") from _call_BlinkXS3_40
    mom "*Risa* No me hagas reír. Creo que esa frase la hemos dicho todas las mujeres del mundo alguna vez."
    mom "Tienes el armario lleno de ropa, y en el sótano tienes otro armario solo para tu ropa. También lleno."
    mom "¿Estás segura de que vas a necesitar más ropa? ¿Dónde la vas a meter? ¿Vas a tirar ropa?"
    call BlinkXS3 ("c26s004_065") from _call_BlinkXS3_41
    emm "No lo había pensado... Lo de tirar ropa está descartado. Me encanta mi ropa."
    emm "Supongo que podría usar el armario de [mc] cuando se vaya a Aruba..."
    call BlinkXS3 ("c26s004_070") from _call_BlinkXS3_42
    mom "¿Y qué vas a hacer cuando vuelva?"
    call BlinkXS3 ("c26s004_075") from _call_BlinkXS3_43
    emm "Tendré que comprar armarios para mi habitación. Tengo toda una pared libre."
    call BlinkXS3 ("c26s004_080") from _call_BlinkXS3_44
    mom "Me parece bien. *Risa* Al menos has dicho que te los tendrías que comprar tú en vez de decir que te los comprara yo."
    mom "Será complicado encontrar el mismo modelo y..."
    call BlinkXS3 ("c26s004_085") from _call_BlinkXS3_45
    emm "¡Entonces tendría que cambiar todos los muebles! No quiero que mi habitación parezca hecha de muebles que he recogido en la basura."
    emm "Quizás pueda pasar sin comprar demasiada ropa... Me gustan mis muebles..."
    call BlinkXS3 ("c26s004_090") from _call_BlinkXS3_46
    mom "Entonces solo queda precisamente lo que no considero un capricho."
    mom "Creo que puedes montar el estudio de fotografía en el sótano sin ningún problema. Pero tú te ocupas de todo."
    call BlinkXS3 ("c26s004_095") from _call_BlinkXS3_47
    emm "Ya lo he estado mirando por internet... lo miré incluso antes de tener el dinero para hacerlo."
    emm "Un par de fondos, iluminación, cámaras, objetivos... Es caro, pero asumible."
    call BlinkXS3 ("c26s004_100") from _call_BlinkXS3_48
    mom "Pero es una inversión en tu futuro, con lo que me parece un gasto correcto. Si quieres dedicarte a la fotografía tendrás que practicar mucho."
    mom "Y tener buen material para hacerlo es imprescindible."
    call BlinkXS3 ("c26s004_105") from _call_BlinkXS3_49
    emm "Además podré ayudar a [mad.nick] con sus diseños y a [kim] con su portfolio. Hay que aprovechar que tenemos una modelo profesional en la familia."
    emm "Incluso puedo empezar un canal de MeTube cuando tenga un poco de experiencia. Eso puede hacerme ganar dinero..."
    call BlinkXS3 ("c26s004_110") from _call_BlinkXS3_50
    mom "*Risa* ¿Necesitas más dinero? Creo que no eres consciente de cuánto puedes abarcar con $83,000..."
    mom "Si quieres hacerlo, no tengo nada en contra siempre y cuando no descuides tus estudios."
    call BlinkXS3 ("c26s004_115") from _call_BlinkXS3_51
    emm "*Risa* Tienes razón. Lo del canal de MeTube lo pensé antes de recibir el dinero. ¡Me he olvidado de que ahora soy rica!" id c26s004_MarEmm_6c7c3d3b
    emm "Pues creo que voy a pedir en Amazonian todo lo que necesito. Ya lo tengo guardado en mi lista de deseados."
    emm "Queda el tema de pintar el sótano..."
    call BlinkXS3 ("c26s004_120") from _call_BlinkXS3_52
    mom "Puedes hacerlo tú misma, con ayuda de las chicas o de [mc], igual que pintamos la habitación de [sai]."
    mom "O contratar a alguien para que lo haga. [nor] tiene los teléfonos de los proveedores si quieres llamar ya."
    mom "O puedes buscar en mis archivos..."
    call BlinkXS3 ("c26s004_125") from _call_BlinkXS3_53
    emm "*Risa* Mejor se lo pido a Tía [nor]. Estoy segura de que tú lo tienes en papel."
    call BlinkXS3 ("c26s004_130") from _call_BlinkXS3_54
    mom "¿Qué tiene de malo el papel?"
    scene c26s004_125d with dissolve
    emm "No tenía nada de malo... hasta que entramos en el Siglo XXI. *Risa*"
    emm "Te veo luego, Mamá."
    scene black with dissolve
    scene c26s004_125e with hpunch
    "Cuando estás a punto de entrar en la cocina, un bólido rosa impacta contra ti."
    mc "¡[emm]! ¿Dónde vas tan deprisa y sin mirar por dónde vas?"
    call BlinkXS3 ("c26s004_135") from _call_BlinkXS3_55
    emm "¡Tengo que ir a ver a Tía [nor]! ¡Mamá me ha dejado montar el estudio de fotografía en el sótano!"
    mc "Genial. Ahora venía a hablar con Mamá de lo de tu paga semanal."
    call BlinkXS3 ("c26s004_140") from _call_BlinkXS3_56
    emm "No hace falta. Ya se lo he dicho yo. *Risa* Como me ha mirado con cara rara, le he dicho que era idea tuya."
    emm "Después de pensarlo bien, me he dado cuenta de que tienes razón. No sería justo que me diera la paga si tengo tanto dinero."
    emm "Y ahora me tengo que ir. Quiero que el estudio esté acabado antes de que te vayas a Aruba."
    if emm._var("route"):
        call KissXS3 ("c26s004_145") from _call_KissXS3
    emm "Hasta luego, [mc]."
    stop music fadeout (1.5)
    mc "Hasta luego, [emm]."
    call BlinkXPS3 ("c26s004_150" , "f") from _call_BlinkXPS3_2697
    if persistent.family:
        $ mart = __("Mamá")
    else:
        $ mart = mar
    play music ("music/RhythmPlay.ogg")
    mc "Hola, [mart]. Parece que has hecho feliz a [emm] con lo del estudio."
    mom "Bueno, después de quitarle de la cabeza unas cuantas ideas locas, lo del estudio me ha parecido la mejor idea que ha tenido hoy."
    mc "Le servirá para practicar y además..."
    call BlinkXS3 ("c26s004_155") from _call_BlinkXS3_57
    mom "Sí, me lo ha dicho, para ayudar a [kim] y a [mad.nick]."
    mc "Exacto. [emm] cada vez más piensa en ayudar a los demás, en vez de ayudarse a si misma."
    mc "Creo que es un efecto imprevisto de la llegada de las chicas."
    call BlinkXS3 ("c26s004_160") from _call_BlinkXS3_58
    mom "No solo eso. El resto de las chicas también están siendo una buena influencia en ella."
    mom "Sabes que siempre ha sido bastante tacaña, y cuando fue a Monterey nos trajo un regalo a cada una. ¡Lencería!"
    if sai._var("route") or bet._var("route"):
        mc "Lo sé. Es sorprendente, pero es un cambio bienvenido."
    else:
        mc "Es sorprendente, pero es un cambio bienvenido."
    if mar._var("route"):
        mc "Tengo ganas de ver cómo te queda lo que te compró a ti."
        mc "Pero antes quiero mi beso de buenos días."
        call KissXS3 ("c26s004_165") from _call_KissXS3_1
        mom "Eso es muy fácil de cumplir. Buenos días, [mc]."
        mc "Buenos días, [mart]."
        call BlinkXS3 ("c26s004_170") from _call_BlinkXS3_59
        mom "La lencería que me compró es muy bonita, además acertó tanto con mi talla como con el color que me gusta."
        mom "Ella y yo usamos casi la misma talla, con lo que no era difícil acertar. Pero no me hubiera sorprendido que la hubiera comprado en rosa en vez de negro."
        mc "*Risa* Estoy seguro de que el rosa te sentaría genial."
    call BlinkXS3 ("c26s004_175") from _call_BlinkXS3_60
    mc "Volviendo al tema del dinero de NTR, ¿necesitas algo?"
    mom "No, nada. La transferencia ha sido una sorpresa. [nor] y yo la esperábamos en diciembre, como cada año."
    mc "Cuando las chicas me han hablado de la transferencia, me ha sorprendido que llegara ahora. Estaba seguro de que llegaba a final de año."
    mc "Si hubiéramos sabido esto, no hubiera sido necesario montar el dormitorio para las chicas."
    call BlinkXS3 ("c26s004_180") from _call_BlinkXS3_61
    mom "No lo sabíamos. Pero aunque lo hubiéramos sabido, lo habríamos hecho igualmente una vez tu padre se fue."
    mom "NTR... ¿o debería decir GILF?... siempre ha sido poco transparente, y tener otra fuente de ingresos da tranquilidad."
    mc "Lo entiendo. ¿Qué vamos a hacer ahora con el dormitorio?"
    call BlinkXS3 ("c26s004_185") from _call_BlinkXS3_62
    mom "¿A qué te refieres?"
    mc "Ahora NTR es nuestro. No necesitamos el dormitorio para vivir. No digo que lo cerremos, pero..."
    call BlinkXS3 ("c26s004_190") from _call_BlinkXS3_63
    mom "No tengo intención de cerrarlo. Primero, porque las chicas viven aquí. Creo que su llegada nos ha ido bien a todos."
    mom "Acabamos de hablar de lo buena influencia que son para [emm]."
    mc "Estoy de acuerdo. Pero supongo que hay un segundo punto."
    call BlinkXS3 ("c26s004_195") from _call_BlinkXS3_64
    mom "A quien mejor le ha ido es a mí. ¿Te acuerdas de cómo estaba cuando llegaste?"
    mc "Por supuesto que me acuerdo. En un proceso de depresión."
    call BlinkXS3 ("c26s004_200") from _call_BlinkXS3_65
    mom "Imagínate cómo hubiera estado si no hubiera estado ocupada con montar el dormitorio."
    mom "He descubierto que llevo demasiados años ociosa, y tener algo que hacer me ayudó mucho."
    mom "Además, me encanta cocinar para mucha gente."
    mc "Creo que en vez de montar un dormitorio deberías haber montado un restaurante."
    call BlinkXS3 ("c26s004_205") from _call_BlinkXS3_66
    mom "Lo pensé, pero hubiera sido más caro y no tendríamos a las chicas, con lo que me alegro de no haberlo hecho."
    mom "Además, no tendríamos la subvención de la Universidad, con lo que hubiera sido mucho más arriesgado."
    mom "Quizás en el futuro..."
    mc "Bueno, hasta que llegue ese futuro, tienes un montón de gente a la que alimentar en casa. *Risa*"
    call BlinkXS3 ("c26s004_210") from _call_BlinkXS3_67
    mom "*Risa* Lo estoy intentando, pero entre tú y [emm] me estáis retrasando."
    mc "Entonces voy a dejar que sigas cocinando. Estaré en mi habitación si necesitas algo."
    scene c26s004_1000 with dissolve
    "Vuelves a tu habitación y compruebas las cuentas bancarias. Tú también has recibido la transferencia."
    "Además de una segunda transferencia, bastante menor en comparación, en la que pone 'Nómina'."
    "Compruebas el correo electrónico, donde encuentras una hoja de salario. Haces unos cálculos y silbas sorprendido."
    "Tu sueldo como CEO de NTR sobrepasa el medio millón de dólares anuales antes de impuestos."
    stop music fadeout (1.5)
    scene black with dissolve
    return
label c26s004_Cafe:
    if _in_replay:
        call mrS3_eri_route from _call_mrS3_eri_route_10
        call mrS3_eil_route from _call_mrS3_eil_route_6
        call mrS3_mee_route from _call_mrS3_mee_route_8
    scene drive_day with fade
    "Después de comer, llevas a [eri] y a [eil] al café. Tienes que hacer algunas compras en el centro de la ciudad y aprovechas el viaje."
    scene c26s004_250a with fade
    play music ("music/On-The-Rise.ogg")
    eil "Gracias por el viaje, [mc]. Voy a ir a cambiarme. Aún nos quedan 15 minutos para empezar nuestro turno."
    eri "A veces te envidio por tener una taquilla propia aquí. Yo tengo que venir vestida de casa."
    mc "¿Habéis pensado en compartir taquilla? No sé el tamaño que tienen, pero..."
    scene c26s004_250An with dissolve
    eil "¡Somos idiotas!"
    eri "¿Puedes creerte que nunca se nos ha ocurrido? Y eso que guardo mis cosas de valor en su taquilla..."
    mc "A veces tenemos la solución delante de las narices y no la vemos."
    eil "¡Pero si incluso sabe la combinación y mis cosas están en su bolso!"
    eri "Y la uso cuando no estás y no se nos había ocurrido nunca. ¡Somos idiotas!"
    scene c26s004_250e with dissolve
    eil "Dame tus cosas y las meto en la taquilla. Voy a cambiarme antes de que se haga tarde. ¿Un café?"
    eri "Sí, por favor. Dile a Roger que nos lo traiga a la mesa."
    mc "Un espresso para mí, por favor."
    call BlinkXPS3 ("c26s004_255" , "f") from _call_BlinkXPS3_2698
    mc "No sé cómo no se os había ocurrido lo de la taquilla."
    eri "Supongo que, como nos dijeron que era personal, no hemos pensado más allá. Dejar el bolso y que me diera su combinación ya nos parecía que era romper las reglas."
    mc "Parece que habéis pensado tan solo dentro del marco de las reglas. Pero bueno, ya está resuelto."
    call BlinkXS3 ("c26s004_260") from _call_BlinkXS3_68
    eri "Le pediré permiso a mi jefe para hacerlo. No quiero que me despidan por algo así si me ven hurgando en la taquilla de [eil]."
    eri "Siempre que metía el bolso cuando ella no estaba, me parecía que me iban a decir que le estaba robando o algo así."
    mc "Parece una buena idea aclararlo con tu jefe antes de hacer nada."
    mc "¿El chico que nos ha traído el café es el sustituto de Jack? ¿El que no está funcionando bien?"
    call BlinkXS3 ("c26s004_265") from _call_BlinkXS3_69
    eri "Sí, es un buen chico, pero no sirve para esto. Se aturde cuando llega mucha gente de golpe y se queda paralizado."
    eri "Y no ha mejorado en... creo que lleva más de dos semanas aquí. Sólo tienes que ver que hay mesas sucias..."
    mc "Puedes aprovechar la conversación de la taquilla para hablarle a tu jefe de [sca]."
    call BlinkXS3 ("c26s004_270") from _call_BlinkXS3_70
    eri "Sí, lo haré. Me ha sorprendido que quiera trabajar aquí. Le queda un mes para empezar las clases. Pero me hará ilusión si la contratan."
    mc "Ya la has oído. Cree que tiene la obligación de colaborar económicamente en casa. Por mucho que le digamos que está equivocada, no va a cambiar de opinión."
    call BlinkXS3 ("c26s004_275") from _call_BlinkXS3_71
    eri "*Risa* Es tan cabezona como [dap]. A veces pienso que es su hermana en vez de serlo yo."
    mc "Somos una familia de cabezones cuando se trata de ayudar, ¿no?"
    call BlinkXS3 ("c26s004_280") from _call_BlinkXS3_72
    eri "Un poco. *Risa* Pero es una de las mejores cosas de esta familia."
    mc "Y supongo que lo de no dejar el trabajo y gastarte el dinero será para ayudar a alguien también, ¿verdad?"
    eri "*Risa* A veces da miedo que nos conozcamos tanto."
    call BlinkXS3 ("c26s004_285") from _call_BlinkXS3_73
    eri "¿Sabes qué planes tienen la abuela y Tía [bet] cuando venda la casa de Florida?"
    mc "Oí que quería comprar o alquilar algo aquí, en la ciudad."
    call BlinkXS3 ("c26s004_290") from _call_BlinkXS3_74
    eri "Exacto. Y pasaría como con [sim], [mad.nick], o [oma]. Vendrían a la comida del domingo y una o dos veces entre semana."
    eri "He estado hablando con Tía [bet] y le he preguntado por qué no compran el terreno enfrente de casa y mandan construir una casa allí."
    eri "No debería ser muy caro para ellas dos y alguna habitación extra. La casa de la abuela en Florida es mucho más grande."
    mc "Y le has ofrecido el dinero de NTR por si lo necesitan, ¿no?"
    call BlinkXS3 ("c26s004_295") from _call_BlinkXS3_75
    eri "Sí. Mi madre no lo va a coger y yo no lo necesito, con lo que me parecía la mejor inversión."
    mc "No tengo ni idea de cuánto se tarda en construir una casa o cuánto puede costar."
    eri "Yo tampoco. Quien más sabe de eso es la abuela, precisamente. Pero le he dicho a Tía [bet] que si necesitan el dinero pueden contar con él."
    mc "¿Por qué no se lo has dicho directamente a la abuela?"
    call BlinkXS3 ("c26s004_300") from _call_BlinkXS3_76
    eri "Porque rechazaría el dinero. Si Tía [bet] lo disfraza como parte de su indemnización tendrá que aceptarlo, porque ese era el plan inicial."
    if mee._var("route"):
        eri "*Risita* Además, no creo que después de vuestra sesión de anoche tenga el cerebro demasiado lúcido."
        mc "*Risa* Es posible, no voy a negarlo."
    mc "Pero hacer que Tía [bet] mienta sobre el origen del dinero..."
    call BlinkXS3 ("c26s004_305") from _call_BlinkXS3_77
    eri "*Risa* No va a mentir. Le va a decir 'Yo puedo aportar X para una casa nueva', y dentro de esa X está mi dinero."
    eri "Fíjate que nadie miente últimamente. Ni siquiera [emm]. Disfrazamos la verdad. Nos estamos convirtiendo en las magas de aquellos libros que leías hace años."
    mc "Sí, el Círculo del Tiempo. Espero que no os convirtáis en tan ruines como eran algunas de ellas."
    call BlinkXS3 ("c26s004_310") from _call_BlinkXS3_78
    eri "No lo vamos a hacer. No hay necesidad de mentir, pero a veces no conviene decir toda la verdad."
    eri "Y saber que alguien nos está viendo por las cámaras todo el día ayuda. Ninguna queremos que [eva] o [ama] piensen que somos unas mentirosas."
    mc "*Risa* Perder privacidad para ganar en sinceridad. No me parece un mal cambio, sobre todo con [emm]."
    mc "Aunque me sorprendería si alguna vez aprendiera a mentir. Siempre ha sido horrible en eso."
    stop music fadeout (1.5)
    call BlinkXS3 ("c26s004_315") from _call_BlinkXS3_79
    eil "[eri], tenemos que empezar el turno."
    play music ("music/SneakySnitch.ogg")
    call BlinkXS3 ("c26s004_320") from _call_BlinkXS3_80
    eil "Por cierto, [mc], ¿podrías pasar por el supermercado y comprar unas latas de atún cuando vuelvas a casa?"
    eil "[nor] dice que creía tener varias latas en la despensa, pero que debía estar equivocada."
    mc "¿Cuántas latas de atún le disteis a Zeus ayer?"
    call BlinkXS3 ("c26s004_325") from _call_BlinkXS3_81
    eil "Yo sólo le di una, después de preguntarle a [mad.nick]. Aunque sean individuales, son mucho atún para un gatito."
    call BlinkXS3 ("c26s004_330") from _call_BlinkXS3_82
    mc "¿[eri]?"
    eri "*Silba*"
    mc "¿[eri]? ¿Cuánto le diste de comer al gato?"
    call BlinkXS3 ("c26s004_335") from _call_BlinkXS3_83
    eri "*Cough* ¡Mira qué hora es! ¡Nuestro turno va a empezar!"
    mc "*Risa* Mas de una lata, ¿verdad?"
    call BlinkXS3 ("c26s004_340") from _call_BlinkXS3_84
    eri "Es que es tan mono y tan agradecido..."
    mc "*Risa* Lo vais a convertir en un cerdo si cada una de vosotras lo alimenta por separado."
    if eil._var("route"):
        call KissXS3 ("c26s004_345") from _call_KissXS3_2
    call BlinkXS3 ("c26s004_345") from _call_BlinkXS3_85
    eil "*Risa* Un poco más gordito sería aún más achuchable. Como tú antes de irte a la universidad."
    mc "*Risa* Y también rompería más camas."
    eil "*Risa* Tienes razón. Te vemos luego en casa."
    if eil._var("route"):
        call KissXS3 ("c26s004_350") from _call_KissXS3_3
    call BlinkXS3 ("c26s004_350") from _call_BlinkXS3_86
    eri "Además, [mad.nick] nos dijo que podíamos darle de comer."
    mc "¡Pero en cantidades normales para un cachorro! *Risa* No tres o cuatro latas cada una de vosotras."
    eri "Bueno, si no lo hubiéramos hecho, no podrías comprar una cama más grande. Hasta luego, [mc]. Es hora de empezar a trabajar."
    scene c26s004_250f with dissolve
    stop music fadeout (1.5)
    mc "Hasta luego, chicas."
    scene black with dissolve
    return
label c26s004_SamSim:
    if _in_replay:
        call mrS3_sam_route from _call_mrS3_sam_route_5
        call mrS3_sim_route from _call_mrS3_sim_route_5
    scene c26s004_360a with fade
    play music ("music/Separation.ogg")
    "Cuando llegas al supermercado te encuentras con una cara conocida."
    "O con una espalda conocida, en este caso."
    if sam._var("route"):
        scene c26s004_360b with dissolve
        "No puedes resistirte a darle una suave palmada en el culo."
        scene c26s004_365a with vpunch
        sam "¡Puto pervertido...!"
        call BlinkXS3 ("c26s004_370") from _call_BlinkXS3_87
        sam "¡Oh! Eres tú. Has estado a punto de que te dé un bofetón."
        mc "*Risa* Menos mal que eres de reflejos rápidos. Te cambio el bofetón por un beso."
        call KissXS3 ("c26s004_375") from _call_KissXS3_4
        sam "Eso es fácil de cumplir."
    else:
        "Buenas tardes, [sam]."
        call BlinkXS3 ("c26s004_370") from _call_BlinkXS3_88
        sam "¡Oh! No esperaba verte por aquí."
    mc "¿No trabajas hoy?"
    call BlinkXS3 ("c26s004_375") from _call_BlinkXS3_89
    sam "He salido de un turno largo hace un rato. Necesitaba llenar la nevera, y aprovecharme de la mula de carga..."
    mc "¿Mula de carga?"
    call BlinkXS3 ("c26s004_380") from _call_BlinkXS3_90
    sim "Esa soy yo. *Risa*"
    if sim._var("route"):
        call KissXS3 ("c26s004_385") from _call_KissXS3_5
    else:
        call BlinkXS3 ("c26s004_385") from _call_BlinkXS3_91
    sim "Buenos tardes, [mc]."
    mc "*Risa* Creía que la mula de carga sería Jamaal. Al menos él va con ruedas."
    call BlinkXS3 ("c26s004_390") from _call_BlinkXS3_92
    sam "No sé dónde está. Cuando he llegado a casa no estaba."
    call BlinkXS3 ("c26s004_395") from _call_BlinkXS3_93
    sim "Ha quedado con un amigo para comer. No sé quién puede aguantarlo aparte de ti."
    mc "Es lo que estaba pensando. Ya van dos veces que me decís que ha quedado con alguien."
    mc "No estará saliendo con alguien, ¿no?"
    call BlinkXS3 ("c26s004_400") from _call_BlinkXS3_94
    sim "No creo... Aunque últimamente ha estado raro... O más raro de lo normal."
    mc "*Risa* ¿Más raro? Eso es difícil para tu hermano."
    call BlinkXS3 ("c26s004_405") from _call_BlinkXS3_95
    sam "Lleva mucho sin salir con nadie. Y sale poco de casa... O salía poco de casa hasta hace un par de semanas."
    sam "Si sale con alguien, no sé dónde puede haberlo conocido."
    mc "¿Online, quizás? Se pasa la vida pegado a una pantalla, con lo que no sería descabellado."
    mc "Pero bueno, si está saliendo con alguien y nos lo quiere contar, ya lo hará cuando llegue el momento."
    call BlinkXS3 ("c26s004_410") from _call_BlinkXS3_96
    sam "No creo que esté saliendo con nadie. Te lo hubiera contado a ti por lo menos, ¿no?"
    mc "Si lo hace, seguramente seré el primero a quien se lo cuente. Cuando esté preparado."
    mc "A lo mejor solo es un amigo con el que queda para hablar de videojuegos y le estamos dando demasiada importancia a sus... rarezas."
    call BlinkXS3 ("c26s004_415") from _call_BlinkXS3_97
    sam "Tienes razón. A lo mejor sólo es Jamaal siendo Jamaal."
    sam "Y por cierto, gracias por comportarte como tú mismo."
    mc "No tengo ni idea de a lo que te estás refiriendo. ¿Qué he hecho esta vez?"
    call BlinkXS3 ("c26s004_420") from _call_BlinkXS3_98
    sam "Convencer a mi cabezota hija para que vaya a entrenar con [deb.nick] a la Universidad."
    call BlinkXPS3 ("c26s004_425" , "h") from _call_BlinkXPS3_2699
    sim "¡Mamá!"
    mc "*Risa* Un poco cabezota sí que eres. Casi tanto como tu hermano."
    call BlinkXS3 ("c26s004_430") from _call_BlinkXS3_99
    sim "¡No te pases! ¡Nadie es tan cabezota como mi hermano!"
    mc "¿Estás segura? Hace un par de días no querías entrenar con [deb.nick]..."
    call BlinkXS3 ("c26s004_435") from _call_BlinkXS3_100
    sam "Y si no fuera por lo que hicisteis tú y ella, [sim] seguiría sin querer ir."
    sam "Parece que si no puede ganar, no quiere competir. Ni siquiera entrenar."
    mc "Es lo que yo le dije. Al menos, por una vez, entró en razón y tomó una decisión correcta."
    call BlinkXS3 ("c26s004_440") from _call_BlinkXS3_101
    sim "Si no lo hubiera hecho, [deb.nick] y tú aún os estaríais riendo de mí e ignorando todo lo que dijera."
    mc "Funcionó, ¿no? Significa que lo hicimos bien."
    call BlinkXS3 ("c26s004_445") from _call_BlinkXS3_102
    sim "¿Podemos cambiar de tema? Parece que entre los dos me estéis echando la bronca."
    stop music fadeout (1.5)
    mc "Vale. *Risa* ¿Cómo es que habéis venido a este supermercado? ¿Ha cerrado el que tenéis al lado de casa?"
    call BlinkXS3 ("c26s004_450") from _call_BlinkXS3_103
    play music ("music/SadSoul.ogg")
    sam "No, pero este es algo más barato. El mes pasado me dieron pocas horas extras y... Bueno, teníamos que comprar mucho, con lo que el ahorro se nota."
    mc "[sam], si necesitáis algo no tenéis nada más que pedirlo."
    call BlinkXS3 ("c26s004_455") from _call_BlinkXS3_104
    sam "No voy a aceptar caridad, [mc]. Ya hacéis suficiente por nosotros."
    call BlinkXS3 ("c26s004_460") from _call_BlinkXS3_105
    sim "¿Quieres ofendernos, [mc]? Porque lo estás consiguiendo."
    mc "Tan sólo os digo que si necesitáis algo, estoy aquí."
    if sam._var("route") and sim._var("route"):
        mc "Salgo con las dos, ofenderos es lo último que querría."
    elif sam._var("route"):
        mc "Salgo con tu madre, ofenderla es lo último que querría."
    elif sim._var("route"):
        mc "Salgo contigo, ofenderte es lo último que querría."
    else:
        mc "Sois de la familia, ofenderos es lo último que querría."
    call BlinkXS3 ("c26s004_465") from _call_BlinkXS3_106
    sam "Sabemos que tu intención es buena, [mc], pero no te preocupes. A final de año terminaré de pagar el coche."
    sam "Después sólo quedarán otros tres préstamos por pagar y por fin podremos ir más desahogados."
    call BlinkXS3 ("c26s004_470") from _call_BlinkXS3_107
    sim "*Risa* ¡Nadaremos en billetes cuando paguemos todos los préstamos!"
    mc "¿No podéis refinanciar alguno?"
    call BlinkXS3 ("c26s004_475") from _call_BlinkXS3_108
    sam "Lo estuve mirando, pero sale muy caro. Nos subirían el interés casi al doble. Y con nuestro historial es muy difícil que nos lo aprueben."
    mc "¿Me dejarías hacer unas comprobaciones sin que os ofendáis?"
    call BlinkXS3 ("c26s004_480") from _call_BlinkXS3_109
    sam "Si no incluye darnos dinero puedes hacer todas las comprobaciones que quieras. Ya te he dicho que no vamos a aceptar caridad."
    mc "Vale. Déjame hablar con Jam y con [nor] para mirar si la idea que se me acaba de ocurrir es posible."
    mc "¿Os queda mucho que comprar?"
    call BlinkXS3 ("c26s004_485") from _call_BlinkXS3_110
    sim "No, ya lo tenemos todo."
    mc "Pero si no lleváis nada..."
    sim "Lo está embolsando Arthur en la caja."
    mc "Dejadme coger unas latas de atún y os ayudo a llevar la compra al coche. A [nor] se le acabó ayer."
    scene c26s004_490An with dissolve
    mc "*Risa* ¿Vosotras también? ¡Ese gato va a pesar 300 kilos si sigue viniendo cada domingo!"
    scene c26s004_490c with dissolve
    sim "¿Verdad que sí? Te mira con esos ojitos..." (multiple=2)
    sam "Es que es irresistible..." (multiple=2)
    sam "Te esperamos en la caja, coge mucho atún para el domingo que viene."
    stop music fadeout (1.5)
    return
label c26s004_Jamaal:
    if _in_replay:
        call mrS3_lis_route from _call_mrS3_lis_route_5
    scene c26s004_495a with fade
    "Después de dejar la compra de los Washington en su coche y despediros, mientras caminas hacia donde has aparcado la camioneta..."
    play music ("music/What-Ive-Found.ogg")
    mcp "(Jamaal y... ¿Anthony?)"
    scene c26s004_495An with dissolve
    mcp "(Sí, es Anthony. Ese coche es inconfundible.)"
    scene c26s004_495e with fade
    mc "Hey, Jam."
    scene c26s004_500 with hpunch
    jam "¡Joder, hermano! ¡Me has asustado!"
    mc "¿Por qué? *Risa* ¿Tienes algo que ocultar?"
    mc "*Risa* Y no me refiero a esa cara. Deberías ir con careta por la calle para no traumatizar a los niños."
    call BlinkXS3 ("c26s004_505") from _call_BlinkXS3_111
    jam "Te lo pensaba contar..."
    mc "¿El qué? No he visto {b}absolutamente nada{/b} que no quieras que haya visto."
    call BlinkXS3 ("c26s004_510") from _call_BlinkXS3_112
    jam "No es eso... Me has pillado fuera de juego."
    jam "He venido a este barrio para no cruzarme con [sim] ni con mi madre, y me cruzo contigo... Eso es mala suerte."
    mc "No te quejes de suerte. Acabo de dejar a tu madre y a tu hermana en el coche. Tienes suerte que hayan ido en dirección contraria, si les quieres ocultar algo."
    mc "Sea lo que sea... yo no he visto nada, pero seguramente ellas no serían ciegas selectivas como lo soy yo."
    call BlinkXS3 ("c26s004_515") from _call_BlinkXS3_113
    jam "Eres un amigo jodidamente bueno. Lo sabes, ¿verdad?"
    mc "*Risa* Lo sé. ¿Quieres tomar un café?"
    call BlinkXS3 ("c26s004_520") from _call_BlinkXS3_114
    jam "Sí, tengo algo que contarte que me convertirá en un dios capaz de curar la ceguera... *Risa* al menos la selectiva."
    mc "Vamos. ¿Conoces algún sitio por aquí cerca en el que hagan buen café?"
    jam "Sí, el bar del que acabo de salir. *Risa*"
    call BlinkXPS3 ("c26s004_525" , "f") from _call_BlinkXPS3_2700
    "Una vez sentados en el bar... Una vez {b}tú{/b} te sientas en el bar..."
    jam "Te aseguro que te lo iba a contar."
    mc "Lo sé. Precisamente he hablado de eso con tu madre y tu hermana. Lo contarías cuando estuvieras preparado."
    mc "Pero no nos debes explicaciones a nadie. Es tu vida y estaremos ahí cuando quieras, no para sacarte unas explicaciones que no quieres dar."
    call BlinkXS3 ("c26s004_530") from _call_BlinkXS3_115
    jam "Es complicado... Nos conocimos hace un par de semanas. Casi lo atropello cuando él salía de una papelería."
    jam "Fue el día que viniste a casa y mi madre me dio unas cajas de pizza para tirar... y me quedé sin pastitas."
    mc "*Risa* Lo recuerdo."
    call BlinkXS3 ("c26s004_535") from _call_BlinkXS3_116
    jam "Iba despistado hablando con su hermana por teléfono y no me vio. Se sintió fatal y empezó a pedir disculpas como un loco."
    mc "Joder, Jam, si me lo cuentas así me puedo imaginar la escena típica de película de instituto en la que el chico le tira los libros a la chica."
    call BlinkXS3 ("c26s004_540") from _call_BlinkXS3_117
    jam "*Risa* No irías muy desencaminado. Pero no le tiré los libros, ni los papeles que llevaba. No llegué a atropellarlo."
    jam "Total, que me dijo que me pagaba un café porque era culpa suya. Fuimos a aquel café al que fuimos cuando tenías que ir a comisaría."
    call BlinkXS3 ("c26s004_545") from _call_BlinkXS3_118
    jam "Empezamos a hablar y nos caímos bien..."
    mc "Y os pusisteis a follar como locos en el lavabo. *Risa*"
    call BlinkXS3 ("c26s004_550") from _call_BlinkXS3_119
    jam "No, qué va. Por eso te decía que es complicado. Él estaba intentando descubrir cómo se sentía respecto a su sexualidad. Estaba quedando con una chica y..."
    mc "Sí, lo sé. [lis]."
    call BlinkXPS3 ("c26s004_555" , "h") from _call_BlinkXPS3_2701
    jam "¿Qué? ¿[lis]? ¿{b}Nuestra{/b} [lis]?"
    mc "Sí, nuestra [lis]. Se habían conocido online mientras ella estaba en Phoenix."
    jam "¡Joder, hermano! Eso no lo sabía. Me dijo el nombre, pero no lo relacioné con nuestra [lis]."
    call BlinkXS3 ("c26s004_560") from _call_BlinkXS3_120
    if lis._var("route"):
        jam "Siempre que la he visto parecía tener ojos sólo para ti."
    else:
        jam "Si me hubieran preguntado, hubiera dicho que estaba colada por ti."
    jam "Pero bueno, a lo que iba... estaba intentando descubrir cómo se sentía, con lo que no hicimos nada. Nos intercambiamos los teléfonos, pero en plan buen rollo. Nada más."
    call BlinkXS3 ("c26s004_565") from _call_BlinkXS3_121
    jam "Me llamó al cabo de unos días para quedar a tomar otro café. Estuvimos hablando y ya había resuelto lo de la chica... lo de [lis]."
    mc "*Risa* Es divertido ver cómo conocemos la misma historia desde dos perspectivas diferentes."
    call BlinkXS3 ("c26s004_570") from _call_BlinkXS3_122
    jam "Sí que lo es. Pero bueno... Continuando mi historia..."
    jam "Quedamos un par de veces más antes de besarnos por primera vez la semana pasada."
    mc "¿El martes?"
    call BlinkXS3 ("c26s004_555") from _call_BlinkXS3_123
    jam "¿Cómo lo sabes?"
    mc "Estuve en tu casa y tu madre me dijo que habías quedado con un amigo."
    call BlinkXS3 ("c26s004_575") from _call_BlinkXS3_124
    jam "*Risa* Y como no tengo más amigos aparte de ti..."
    mc "*Risa* Exacto."
    jam "*Risa* Pero quedamos más veces esa semana, podría haber sido el jueves o el sábado."
    mc "Entonces hubieras dicho hace cuatro días o hace dos. 'La semana pasada' suena más lejano que 'dos o cuatro días'."
    call BlinkXS3 ("c26s004_580") from _call_BlinkXS3_125
    jam "¡[dap]! ¡Abandona el cuerpo de mi amigo! ¡Él no es tan listo como para deducir eso! *Risa*"
    mc "*Risa* Vivir con 15 mujeres hace que desarrolles un sexto sentido, hermano."
    mc "Pero decías que lo de Anthony es complicado. No le veo la complicación por ningún sitio. Os conocisteis, encajasteis, y estáis saliendo."
    call BlinkXS3 ("c26s004_585") from _call_BlinkXS3_126
    jam "Es más complicado que eso..."
    if lis._var("route"):
        mc "Si lo dices por [lis], no te preocupes. Se veía que era una pareja que no podía funcionar. Tú has acabado saliendo con uno y yo con la otra."
    else:
        mc "Si lo dices por [lis], no te preocupes. Se veía que era una pareja que no podía funcionar."
    call BlinkXS3 ("c26s004_590") from _call_BlinkXS3_127
    jam "No es por [lis], pero no me corresponde a mí contártelo."
    mc "¿Por qué no lo traes a casa un domingo? Cuando estéis preparados para presentárselo a la familia como tu pareja. Sin prisa y sin presión."
    mc "Muchas de las chicas ya lo conocen de la noche en el Jazz Corner, antes del cumpleaños de [emm], [eri], y [dap]."
    call BlinkXS3 ("c26s004_595") from _call_BlinkXS3_128
    jam "Sería una buena idea, pero antes quiero presentárselo a mi madre y a mi hermana."
    mc "Es lógico que lo hagas."
    jam "Dame un poco de tiempo. Anthony es tímido."
    mc "Todo el tiempo que necesites. Ya te he dicho que no hay prisa, pero esta ciudad es pequeña y es fácil que alguien os vea."
    call BlinkXS3 ("c26s004_600") from _call_BlinkXS3_129
    jam "Eres el mejor amigo que se puede tener. Bueno, lo serías si fueras gay. *Risa*"
    mc "*Risa* Entonces me estarías tirando los trastos todo el día. La excusa de que no te gustan los blancos ya no cuela."
    call BlinkXS3 ("c26s004_605") from _call_BlinkXS3_130
    jam "Eso lo decía cuando tenía un crush contigo..."
    call BlinkXPS3 ("c26s004_605" , "h") from _call_BlinkXPS3_2702
    mc "¿QUÉ? ¿Cuándo has tenido un crush conmigo?"
    call BlinkXS3 ("c26s004_610") from _call_BlinkXS3_131
    jam "En el instituto, el último año. No te preocupes, duró poco. ¿Recuerdas lo desastrosas que fueron mis relaciones aquel año?"
    mc "Claro que lo recuerdo. Ibas de un capullo al siguiente. Creo que saliste con todos los gays capullos del instituto."
    call BlinkXS3 ("c26s004_610b") from _call_BlinkXS3_132
    jam "Exacto. Y, por otro lado, tenía que veros a [eil] y a ti todos los días. Yo quería eso, pero solo conseguía capullos."
    mc "Joder, Jam. Lo siento. Nunca pensé que te pudiera afectar."
    call BlinkXS3 ("c26s004_610a") from _call_BlinkXS3_133
    jam "Ya te digo que duró poco. Obviamente era imposible, con lo que seguí encadenando capullos."
    mc "Tío, cosas como esas me las tenías que haber dicho."
    call BlinkXS3 ("c26s004_620") from _call_BlinkXS3_134
    jam "¿Y arriesgar nuestra amistad? ¡Ni de coña, hermano!"
    mc "No hubiera pasado. Nuestra amistad está por encima de esas cosas."
    jam "Hubiera sido más plausible volverme hetero y tener el crush con [eil]. *Risa* Al fin y al cabo tú eras un capullo más."
    mc "*Risa* Creo que soy tan capullo porque te acepté como mascota. *Risa* ¿Te pido un platito de Dog Chew?"
    call BlinkXS3 ("c26s004_625") from _call_BlinkXS3_135
    jam "¿Ves cómo eres un capullo? *Risa* Pero eres el mejor amigo que se puede tener."
    mc "Hablando de amigos... ¿Qué sabes de los préstamos de tu madre?"
    call BlinkXS3 ("c26s004_630") from _call_BlinkXS3_136
    jam "Que se llevan casi todo el dinero que entra en casa. Mis facturas médicas fueron muy caras y mi madre se endeudó mucho."
    mc "¿Puedes conseguir los datos de esos préstamos? Banco, importe que debe todavía..."
    call BlinkXS3 ("c26s004_635") from _call_BlinkXS3_137
    jam "No estás pensando en pagar esos préstamos, ¿verdad? Mi madre no lo va a consentir."
    mc "Lo sé, pero se me ha ocurrido una idea que tengo que consultar con [nor]."
    jam "¿Qué idea? A veces me preocupas..."
    scene c26s004_640An with dissolve
    "Le explicas tu idea a Jamaal. Le parece factible, aunque no sabe cómo se la va a tomar [sam]."
    "Te dice que buscará los datos necesarios y te los enviará por correo electrónico."
    scene drive_afternoon with fade
    "Al cabo de un rato os despedís. Se acerca la hora de la cena y vuelves a casa con las latas de atún."
    stop music fadeout (1.5)
    "Olvidas comprar lo que venías a comprar a la ciudad. Ya volverás mañana."
    return
label c26s005_EvaDap:
    if _in_replay:
        call mrS3_eva_route from _call_mrS3_eva_route_12
        call mrS3_dap_route from _call_mrS3_dap_route_9
        call mrS3_nor_route from _call_mrS3_nor_route_8
    call BlinkXPS3 ("c26s005_005" , "f") from _call_BlinkXPS3_2703
    play music ("music/RhythmPlay.ogg")
    "Al llegar a casa, pasas por la cocina de [nor] a entregar las latas de atún."
    mc "Hola, [nor]. Te traigo las latas que me ha pedido [eil] para el Monstruo del Atún."
    nor "*Risa* Me imaginé que alguna de las chicas le daría alguna lata, pero no que me dejarían sin atún."
    nor "Es difícil resistirse cuando te mira como el gato de la película del ogro y el burro."
    mc "Por cierto, me he encontrado con [sam] y [sim] en la tienda."
    call BlinkXS3 ("c26s005_010") from _call_BlinkXS3_138
    nor "Ese 'por cierto' me suena a que se te ha ocurrido alguna idea que las atañe."
    mc "Más o menos. Jamaal me tiene que enviar una información que le he pedido, pero quería consultar contigo si era plausible."
    call BlinkXS3 ("c26s005_015") from _call_BlinkXS3_139
    nor "A ver, explícame esa idea. Menos mal que tus ideas suelen funcionar mejor que las de [emm]."
    mc "Déjame tu móvil para enseñarte los cálculos que he hecho en mi cabeza."
    scene c26s005_015d with dissolve
    "Le explicas tu plan y cree que puede ser factible. Te pide que le pases la información que te mande Jamaal en cuanto la tengas."
    "Ella se apunta al plan y colaborará en llevarlo a cabo. Habrá que hacer algunas cosas que posiblemente no de tiempo de acabar antes de que te tengas que ir a Aruba."
    "Te dice que eso puede ser bueno. Conociendo a [sam] y a [sim], que haya medio continente y un mar entre vosotros cuando se enteren es idóneo para tu seguridad."
    "*Ring-Ring*"
    "Suena su teléfono."
    call BlinkXS3 ("c26s005_020") from _call_BlinkXS3_140
    nor "Hola, cielo."
    nor "Sí, está conmigo en la cocina."
    nor "Ahora se lo digo."
    call BlinkXS3 ("c26s005_025") from _call_BlinkXS3_141
    nor "Era [dap]. Está en tu habitación y quiere que vayas cuando puedas."
    mc "OK. Ahora voy. Te mando la información en cuanto Jamaal me la envíe."
    if nor._var("route"):
        call KissXS3 ("c26s005_030") from _call_KissXS3_6
    call BlinkXS3 ("c26s005_030") from _call_BlinkXS3_142
    nor "Hasta luego. La cena está en el horno y estará preparada en media hora más o menos. Cenamos aquí."
    mc "Voy a ver qué quiere [dap] y bajamos a cenar."
    nor "Mientras vas a verla, yo voy a cambiarme. Preguntále a [mar] si necesita ayuda para traer la comida cuando vengas, por favor."
    "Ya nadie le da importancia a que, de vez en cuando, vaya en ropa interior o, como en este caso, en bikini y un vestido transparente."
    call BlinkXPS3 ("c26s005_035" , "f") from _call_BlinkXPS3_2704
    stop music fadeout (1.5)
    "Al llegar a tu habitación..."
    play music ("music/MorningFunnyBeat.ogg")
    mc "Hola, [eva]. [nor] me ha dicho que [dap] me estaba buscando."
    call BlinkXPS3 ("c26s005_040" , "h") from _call_BlinkXPS3_2705
    eva "¿[eva]?"
    mc "¿Qué pasa, [eva]?"
    mc "¡Ah! Ahora lo veo. Te has peinado como [dap]."
    call BlinkXS3 ("c26s005_045") from _call_BlinkXS3_143
    eva "¿Qué ha fallado en mi disfraz? ¿Cómo lo has sabido?"
    mc "No lo sé. He entrado y sabía que eras tú."
    call BlinkXS3 ("c26s005_050") from _call_BlinkXS3_144
    eva "Pero algo me tiene que haber delatado... Somos idénticas."
    mc "Si tuviera que racionalizarlo... [dap] no tiene esos músculos. Y además, puedo verle un pie detrás del armario, aunque no me había fijado hasta ahora."
    call BlinkXS3 ("c26s005_055") from _call_BlinkXS3_145
    dap "Te dije que no funcionaría. Además, no hablas como yo."
    mc "Bueno, no le he dado tiempo a hablar."
    call BlinkXS3 ("c26s005_065") from _call_BlinkXS3_146
    dap "Creía que la ibas a detectar por la voz, pero tienes razón, no ha hablado."
    if dap._var("route") and eva._var("route"):
        mc "Pero ¿realmente pensáis que no distinguiría a una de mis chicas de la otra?"
    elif dap._var("route") or eva._var("route"):
        mc "Pero ¿realmente pensáis que no sabría con quién estoy saliendo y con quién no?"
    else:
        mc "Pero ¿realmente pensáis que no os distinguiría?"
    mc "Las dos sois únicas e inconfundibles."
    scene c26s005_060a with dissolve
    dap "A veces es monísimo..."
    eva "Dan ganas de darle un abrazo y romperle un par de huesos..."
    mc "*Risa* Acepto ese abrazo pero, si puede ser, me gustaría conservar mis huesos intactos."
    scene c26s005_060b with dissolve
    eva "¿Te acuerdas cuando no quería abrazos, [mc]?"
    mc "*Risa* Claro que me acuerdo. El disgusto por los abrazos te duró un minuto hasta que te abrazó [nor]."
    dap "*Risa* Lo hubieras pasado muy mal en esta familia si no lo hubieras superado."
    eva "Me estáis volviendo blanda. ¡Pero me encanta!"
    "Entre las muchas diferencias que puedes notar entre ambas está la diferencia de altura provocada por los zapatos de [dap]."
    "En lo único que son idénticas es en que las dos son adorables, cada una a su manera."
    "El abrazo dura varios minutos, hasta que tenéis que separaros para ir a cenar."
    scene c26s005_060c with fade
    "Nadie confunde a las chicas cuando llegáis a la cocina de [nor]. Alguna comenta el cambio de peinado de [eva]."
    stop music fadeout (1.5)
    "[eva] está exultante por sentirse única."
    return
label c26s005_LisDebKat:
    if _in_replay:
        call mrS3_deb_route from _call_mrS3_deb_route_12
        call mrS3_lis_route from _call_mrS3_lis_route_6
    call BlinkXPS3 ("c26s005_100" , "f") from _call_BlinkXPS3_2706
    play music ("music/Morning-Sun.ogg")
    "Después de cenar y ayudar a [nor] a recoger, de camino a tu habitación..."
    mc "Hola, [kat], ¿qué tal? ¿Qué haces aquí sola?"
    kat "Estaba leyendo un rato mientras [kim] se pone el pijama."
    mc "¿Sales para darle privacidad? Eso es nuevo, ¿no?"
    call BlinkXS3 ("c26s005_105") from _call_BlinkXS3_147
    kat "La tengo muy vista. *Risa* Nunca sabes cuándo te la vas a encontrar desnuda."
    kat "Esa chica se cambia de ropa más de lo normal. *Risa*"
    mc "Es uno de los inconvenientes de compartir habitación, supongo."
    mc "¿Me puedo sentar?"
    call BlinkXS3 ("c26s005_110") from _call_BlinkXS3_148
    kat "*Risa* ¿Quién ha dicho que fuera un inconveniente?"
    mc "*Risa* Tienes razón. Aunque mi segundo compañero de habitación en Portland dormía desnudo. ¡Eso era un inconveniente!"
    call BlinkXS3 ("c26s005_115") from _call_BlinkXS3_149
    kat "Había oído que tú también duermes desnudo. No sería un problema entonces..."
    mc "Siempre he dormido desnudo, pero no en el dormitorio por entonces. Me parecía una falta de respeto para mi compañero."
    mc "Cuando llegó Fabian y empezó a dormir desnudo, intenté convencerlo. Como no funcionó, yo también empecé a hacerlo."
    call BlinkXS3 ("c26s005_120") from _call_BlinkXS3_150
    kat "Y supongo que él dejó de hacerlo. *Risa*"
    mc "¿Por qué supones eso, [kat]?"
    call BlinkXS3 ("c26s005_125") from _call_BlinkXS3_151
    kat "¿Qué?... Porque... No sé... He oído que... Era solo una suposición... No sé si el chico se sentiría... acomplejado..."
    mc "*Risa* Creo que es la primera vez que te veo ruborizarte, [kat]."
    mc "Creo que es una justa venganza por lo que me hiciste con las belugas."
    call BlinkXS3 ("c26s005_130") from _call_BlinkXS3_152
    kat "*Risa* ¿Me he ruborizado? No sé por qué... Puedo hablar de pollas sin ningún problema..."
    mc "*Risa* Supongo que no es lo mismo hablar de pollas en general que de una en concreto."
    mc "Y menos aún con el propietario de la polla en cuestión."
    call BlinkXS3 ("c26s005_135") from _call_BlinkXS3_153
    kat "¿Podemos dejar de hablar de tu polla? *Risita* Al final voy a tener que comprobar si lo que se dice es cierto..."
    mc "*Risa* Cuando quieras. Lo de pillarme desnudo en la ducha fue el deporte principal en esta casa durante un tiempo."
    call BlinkXS3 ("c26s005_140") from _call_BlinkXS3_154
    kat "¡Gracias por darme la oportunidad de cambiar de tema!"
    mc "¿Cuándo lo he hecho?"
    call BlinkXS3 ("c26s005_145") from _call_BlinkXS3_155
    kat "Has hablado de deporte y tú y yo habíamos quedado para desayunar un día viendo a las chicas hacer yoga."
    mc "¡Vaya! ¿No te vas a ruborizar más, entonces?"
    call BlinkXS3 ("c26s005_150") from _call_BlinkXS3_156
    kat "*Risa* Espero que no. No me gusta que me pillen fuera de juego. Pero hablemos de ese desayuno."
    mc "Quieres decir la {b}cita{/b} para desayunar, ¿verdad?"
    call BlinkXS3 ("c26s005_155") from _call_BlinkXS3_157
    kat "¡Joder, [mc]! ¡Me has vuelto a hacer ruborizar!"
    mc "No sé por qué. *Risa* Fuiste tú la que dijo cita. Además estás monísima cuando te ruborizas."
    call BlinkXS3 ("c26s005_160") from _call_BlinkXS3_158
    kat "¿Puedes parar de una vez? ¿Está fallando el aire acondicionado? Aquí empieza a hacer demasiado calor..."
    kat "Me equivoqué. Quería decir una... reunión para desayunar..."
    mc "¿Cuál va a ser el orden del día en esa reunión?"
    call BlinkXS3 ("c26s005_165") from _call_BlinkXS3_159
    kat "*Risa* ¡Estoy pagando carísimo lo de las belugas!"
    mc "Donde las dan las toman. *Risa* ¿Entonces no es una cita?"
    call BlinkXS3 ("c26s005_170") from _call_BlinkXS3_160
    kat "¡NO! *Risa* ¡Tan solo quedamos para desayunar al lado de la piscina y comentar las vistas!"
    mc "*Risa* Me parece bien. ¿Mañana te va bien?"
    call BlinkXS3 ("c26s005_175") from _call_BlinkXS3_161
    kat "¿Mañana? ¡No he preparado nada!"
    if persistent.family:
        mc "*Risa* El café se prepara por la mañana, [kat]. Y los croissants o los bizcochos los hornea mi madre por norma."
    else:
        mc "*Risa* El café se prepara por la mañana, [kat]. Y los croissants o los bizcochos los hornea [mar] por norma."
    call BlinkXS3 ("c26s005_180") from _call_BlinkXS3_162
    kat "Lo sé... ¡No soy idiota!"
    mc "Entonces, ¿a qué te refieres con que no has preparado nada para el desayuno de mañana?"
    call BlinkXS3 ("c26s005_185") from _call_BlinkXS3_163
    lis "Hola, chicos. ¿Preparando la cita para desayunar?"
    call BlinkXS3 ("c26s005_190") from _call_BlinkXS3_164
    kat "¡No es una cita!" (multiple=2)
    mc "*Risa* No es una cita." (multiple=2)
    call BlinkXS3 ("c26s005_195") from _call_BlinkXS3_165
    kat "Me tengo que ir. Nos vemos mañana."
    mc "¿Pero al final desayunamos juntos mañana o no?"
    call BlinkXS3 ("c26s005_200") from _call_BlinkXS3_166
    kat "Sí, pero no es una cita."
    mc "OK. Quedamos mañana para desayunar en una no-cita. ¿A qué hora?"
    scene c26s005_205An with dissolve
    kat "Las chicas hacen yoga es a las 7:30. Quedamos en la piscina."
    call BlinkXS3 ("c26s005_210") from _call_BlinkXS3_167
    lis "Nunca creí que vería a [kat] nerviosa por desayunar."
    mc "Creo que la equivocación con la palabra 'cita' la ha puesto más nerviosa de lo necesario."
    stop music fadeout (1.5)
    lis "Incluso se ha olvidado el comic y los zapatos..."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    "Oyes golpes en el piso de abajo."
    kat "[mar], soy yo. ¿Estás ahí? ¿Puedo pasar? Es urgente."
    call BlinkXS3 ("c26s005_220") from _call_BlinkXS3_168
    play music ("music/PositiveWoman.ogg")
    "[lis] hace como que no ha oído lo que estás seguro de que los dos habéis oído. Supones que no quiere ahondar en el extraño comportamiento de [kat]."
    "Deja el comic en la mesa y se sienta a tu lado."
    if lis._var("route"):
        lis "Hablando de citas... ¿Te gustan las fiestas?"
        mc "Depende. ¿Qué tipo de fiestas?"
        call BlinkXS3 ("c26s005_215") from _call_BlinkXS3_169
        lis "Una amiga me invitó a una fiesta que da el jueves. No pensaba ir, pero si quieres..."
        lis "Será algo pequeño... 70 o 90 personas, en su piso."
        mc "*Risa* Tu concepto de pequeño y el mío son diferentes."
        mc "¿Y en qué tipo de piso caben 70 o 90 personas para una fiesta? Incluso esta casa parecería una lata de sardinas si no usáramos el jardín."
        call BlinkXS3 ("c26s005_225") from _call_BlinkXS3_170
        lis "Bueno, es un dúplex y en vez de jardín tiene una terraza con piscina."
        mc "No conozco ningún edificio en Newport así..."
        lis "No es en Newport. Tendríamos que ir a L.A. ¿Te apetece?"
        mc "Si a ti te apetece, me parece bien. Me gustaría conocer a tus amigos."
        mc "Pero no pensabas ir, con lo que no lo tienes que hacer por mí."
        call BlinkXS3 ("c26s005_230") from _call_BlinkXS3_171
        lis "*Risa* No lo hago sólo por ti. Quiero vacilarles de novio."
        mc "*Risa* ¿De verdad me vas a exhibir, Princesa? No sé si hay mucho de lo que vacilar."
        call BlinkXS3 ("c26s005_235") from _call_BlinkXS3_172
        lis "Es broma. Me gustaría ir, pero la invitación nos llegó en medio de la mudanza y casi la había olvidado."
        lis "Después, cuando tú y yo... nos besamos... pensé que quizás sería una buena idea. Así podemos tener una noche para nosotros solos."
        mc "Y para 70 o 90 personas. *Risa* Pero vale. Me apunto a la fiesta."
        mc "Depende de en qué parte de L.A. sea, tendremos que salir con más de cuatro horas de antelación."
        call BlinkXS3 ("c26s005_240") from _call_BlinkXS3_173
        lis "No te preocupes por eso. Contrataré un helicóptero. Es poco más de una hora de vuelo y podemos aterrizar a 20 minutos del apartamento de mi amiga."
        lis "Ella puede mandar a su chófer a recogernos."
        mc "Eso es un nivel muy diferente del que estoy acostumbrado..."
        mc "Espera. Ya has contratado el helicóptero, ¿verdad?"
        call BlinkXS3 ("c26s005_245") from _call_BlinkXS3_174
        lis "Sí, por si querías venir... ¿cómo lo has sabido?"
        mc "He vivido casi toda mi vida en Newport y no tengo ni idea de cuánto tiempo se tarda en volar a L.A."
        mc "Y tengo aún menos idea de dónde hay algún helipuerto. *Risa* Tú llevas algo más de dos semanas aquí y ya sabes cuánto se tarda o dónde se puede aterrizar."
        call BlinkXS3 ("c26s005_250") from _call_BlinkXS3_175
        lis "Quería presentarte el plan completo. Y conducir cuatro horas no me parece un buen plan."
        mc "No suele serlo, no. Y las cuatro horas para volver tampoco."
        call BlinkXS3 ("c26s005_255") from _call_BlinkXS3_176
        lis "Yo había pensado... si te apetece... en reservar una habitación de hotel y pasar la noche allí..."
        mc "Ya lo has hecho, ¿no?"
        call BlinkXS3 ("c26s005_260") from _call_BlinkXS3_177
        lis "Sí, pero puedo cancelarla si no quieres..."
        mc "Me encantaría pasar la noche contigo en esa habitación de hotel. Me encantaría pasarla aunque fuera en un iglú."
        scene c26s005_260d with dissolve
        "[lis] se acerca y te da un suave beso en los labios. Supones que la respuesta ha sido la adecuada."
        call BlinkXS3 ("c26s005_265") from _call_BlinkXS3_178
        if deb._var("route"):
            lis "Perfecto, pero dejando de lado nuestra cita..."
    if deb._var("route"):
        stop music fadeout (1.5)
        lis "¿Cuándo vas a tener la primera cita con [deb.nick]?"
        play music ("music/UnforeseenMotive.ogg")
        mc "No quiero sonar grosero, pero eso es algo entre ella y yo."
        call BlinkXS3 ("c26s005_270") from _call_BlinkXS3_179
        lis "Lo sé, lo sé. Pero creo que lo estás alargando demasiado. Hace siglos que os besasteis."
        if lis._var("route"):
            lis "Y no quiero que nuestra primera cita, en la fiesta, sea antes que la suya."
            mc "[lis], no es una competición. Da lo mismo a quién besé primero para decidir con quién debo tener una cita primero."
            call BlinkXS3 ("c26s005_275") from _call_BlinkXS3_180
            lis "A ti te da lo mismo. A mí no. [deb.nick] siempre se ha sentido que estaba por debajo de mí en muchas cosas."
            lis "Equivocadamente, pero ella se siente así."
            mc "No debería..."
            call BlinkXS3 ("c26s005_280") from _call_BlinkXS3_181
            lis "Precisamente porque no debería, no quiero que se sienta así con el hombre que compartimos."
            lis "La elegiste a ella primero, con lo que ella va a ser la primera en tener una cita contigo."
        mc "Como te he dicho, es algo entre ella y yo."
        call BlinkXS3 ("c26s005_285") from _call_BlinkXS3_182
        lis "Vale. Lo entiendo."
        lis "Por cierto, ¿tienes algún plan para comer mañana?"
        mc "No, pensaba comer en casa. ¿Por qué?"
        call BlinkXS3 ("c26s005_290") from _call_BlinkXS3_183
        lis "Han abierto un sitio nuevo que creo que te podría gustar. Es una pizzería artesanal italiana."
        lis "Por lo que he leído, la cocinera es una abuelita italiana. Italiana de verdad."
        mc "Me parece una buena idea."
        if lis._var("route"):
            mc "Pero hace un momento has dicho que no querías tener una cita conmigo antes de que [deb.nick] y yo la tuviéramos. No te entiendo."
            call BlinkXS3 ("c26s005_295") from _call_BlinkXS3_184
            lis "*Risa* Acostúmbrate a no entenderme. Yo no consideraría esa comida como que tú y yo tenemos una cita."
            lis "Sólo es una comida en un sitio que no conoces y que he descubierto."
        else:
            call BlinkXS3 ("c26s005_295") from _call_BlinkXS3_185
        lis "¿Te apetece entonces?"
        mc "Sí, claro. Nunca digo que no a una buena pizza."
        call BlinkXS3 ("c26s005_300") from _call_BlinkXS3_186
        lis "Perfecto. Voy a hacer una reserva para mañana para comer. La hago a tu nombre. Haz hueco en tu agenda."
        mc "¿Por qué a mi nombre?"
        call BlinkXS3 ("c26s005_305") from _call_BlinkXS3_187
        deb "Hola, chicos. ¿Qué hacéis aquí?"
        mc "Estábamos charlando sobre una pizzería."
        call BlinkXS3 ("c26s005_310") from _call_BlinkXS3_188
        lis "¿Te acuerdas de la pizzería de la que estuvimos hablando? [mc] tiene una reserva para comer mañana. Dos personas."
        lis "Y tú no tienes clase a la hora de comer, al revés que yo, con lo que sólo puede ser para vuestra cita."
        mc "¡[lis]!"
        call BlinkXS3 ("c26s005_315") from _call_BlinkXS3_189
        lis "¡Oh! Lo siento si he chafado la sorpresa que querías darle."
        lis "Os dejo solos para que habléis de vuestra cita."
        scene c26s005_315d with dissolve
        lis "*Susurro risueño* Acostúmbrate a las encerronas de las hermanas Selden. Te he mandado la dirección del sitio. Tienes una reserva a la 1:00 PM."
        lis "*Susurro risueño* En ningún momento he dicho que la comida fuera conmigo, por si te lo estás preguntando."
        if lis._var("route"):
            scene c26s005_315g with dissolve
            "Te da un dulce beso en el que puedes saborear su sensación de triunfo."
        scene c26s005_315e with dissolve
        lis "Buenas noches, [mc]. Te veo luego, [deb.nick]."
        deb "Hasta ahora, [lis]."
        mc "Hasta mañana, [lis]."
        call BlinkXPS3 ("c26s005_320" , "f") from _call_BlinkXPS3_2707
        deb "¿Cómo has descubierto esa pizzería? Lo abrieron la semana pasada y lo descubrimos el viernes por un cartel que había en la universidad."
        mc "¿Te acuerdas de cuando me encerraste en tu habitación con [lis]?"
        mc "Creo que esta ha sido su respuesta a aquello. Es ella quien ha hecho la reserva, haciéndome creer que iba a ir a comer con ella."
        call BlinkXS3 ("c26s005_325") from _call_BlinkXS3_190
        deb "Si no quieres que vayamos, no tenemos por qué hacerlo. Lo entendería..."
        mc "No voy a renunciar a ello porque haya sido una encerrona de tu hermana. Le tengo que dar las gracias por hacerlo."
        mc "Tengo muchas ganas de que tengamos la primera cita, [deb.nick]. Al menos la primera cita oficial."
        mc "Para mí, cuando estuvimos en el lago solos cuenta como una perfecta primera cita."
        call BlinkXS3 ("c26s005_330") from _call_BlinkXS3_191
        deb "A mí también me apetece. Y, para mí, cada momento que estamos juntos es una cita."
        deb "Nunca he entendido ese protocolo de cena, cine, y cama. Creo que se puede disfrutar de cada momento sin ponerle etiquetas."
        mc "Estoy de acuerdo. Las cosas tienen que surgir naturales."
        call BlinkXS3 ("c26s005_335") from _call_BlinkXS3_192
        deb "*Risa* Pero ahora que sé que vamos a tener una cita 'oficial' no voy a poder dejar de pensar en qué ponerme."
        mc "*Risa* No deja de asombrarme lo mucho que has cambiado desde que llegaste, cielo."
        call BlinkXS3 ("c26s005_340") from _call_BlinkXS3_193
        deb "¿A qué te refieres?"
        mc "La [deb.nick] que bajó de aquel avión se hubiera puesto unos vaqueros y una camiseta."
        call BlinkXS3 ("c26s005_345") from _call_BlinkXS3_194
        deb "*Risa* Aquella [deb.nick] no tendría una cita contigo. Pensaría que te quieres reír de ella. Pero tienes razón. La ropa no me importaba nada."
        deb "La culpa del cambio la tienes tú en gran medida. Si no me hubieras llevado a la tienda de [mad.nick]..."
        mc "*Risa* Si no te hubiera llevado a la tienda, no hubieras tenido ropa. Le hubieras tenido que coger ropa a [kim] o a [emm]."
        mc "Creo que deben ser las que tienen la talla más parecida. [eil] aún no vivía en casa."
        call BlinkXS3 ("c26s005_350") from _call_BlinkXS3_195
        deb "*Risita* Sus vaqueros no me servirían y tendría que usar sus shorts y sus tops. Con lo que el resultado sería el mismo."
        deb "Sobre todo si me hubieras mirado igual que ahora..."
        mc "¿A qué te refieres?"
        call BlinkXS3 ("c26s005_355") from _call_BlinkXS3_196
        deb "Me miras como si fuera... atractiva..."
        mc "¿Atractiva? Eso es lo que se le dice a un amigo cuando le vas a presentar a una chica que no es guapa."
        mc "Tú no eres atractiva, [deb.nick]. Tú eres guapísima."
        call BlinkXS3 ("c26s005_360") from _call_BlinkXS3_197
        deb "Gracias, [mc]... Aún me sorprende que te guste, pero es una de las cosas que no quiero que cambies."
        deb "Y creo que nunca me cansaré de oírtelo decir."
        mc "*Risa* ¿Ya estás pensando en cambiarme?"
        call BlinkXS3 ("c26s005_365") from _call_BlinkXS3_198
        deb "*Risa* ¿Tengo que contestar a esa pregunta?"
        mc "*Risa* Mejor no lo hagas."
        call BlinkXS3 ("c26s005_370") from _call_BlinkXS3_199
        deb "Debería ir a mi habitación... a elegir ropa y a pedirle consejo a [lis]. Mañana no tendré tiempo..."
        deb "¿A qué hora es la reserva?"
        mc "A la 1:00 PM."
        call BlinkXS3 ("c26s005_375") from _call_BlinkXS3_200
        deb "Perfecto. Me dará tiempo de venir a casa a cambiarme después de la última clase. ¿Me pasas a buscar por mi habitación a las 12:30?"
        mc "Sí, ningún problema. No sería una cita completa si no paso a buscar a mi chica, ¿no?"
        scene c26s005_380d with dissolve
        "Se levanta y te da un dulce beso lleno de anticipación por lo que vendrá mañana."
        call BlinkXS3 ("c26s005_380") from _call_BlinkXS3_201
        deb "Espero que las cosquillas que me recorren cada vez que dices 'mi chica' no desaparezcan nunca."
        deb "Te veo mañana, cielo."
        stop music fadeout (1.5)
        mc "Hasta mañana, preciosa."
    else:
        lis "Se me ha ocurrido una idea. A lo mejor me meto donde no me llaman, pero después de unas semanas aquí... ¿Aceptáis sugerencias sobre cómo mejorar el dormitorio?"
        if lis._var("route"):
            mc "*Risa* Eso sí que es un cambio de tema. De planificar nuestra primera cita a sugerencias sobre el dormitorio."
            call BlinkXS3 ("c26s005_295") from _call_BlinkXS3_202
            lis "*Risa* Lo sé, pero si seguimos hablando de la fiesta, me voy a pasar hasta el jueves pensando en ello."
            mc "Lo entiendo. Adelante con esas sugerencias."
        else:
            mc "Por supuesto, [lis]."
        scene c26s005_385An with dissolve
        "[lis] pasa un rato proponiendo cosas que podrían mejorar el dormitorio, especialmente de cara a cuando las chicas nuevas lleguen en poco más de un mes."
        "Tomas nota de las más interesantes para comentarlo con [mar] y [nor]."
        call BlinkXS3 ("c26s005_290") from _call_BlinkXS3_203
        lis "Y eso es todo. Creo que voy a ir a mi habitación a acabar unas cosas antes de dormir."
        mc "Perfecto. Te veo mañana."
        if lis._var("route"):
            scene c26s005_315d with dissolve
            lis "*Susurro sensual* Creo que no hablar de ello no va a evitar que piense en la fiesta. Ni en la noche de después."
            scene c26s005_315g with dissolve
            "Te da un dulce beso en el que puedes saborear su sensación de anticipación."
    scene c26s005_315f with fade
    "Te quedas solo en el sofá. Hora de ir a tu habitación a dormir."
    "Tienes una no-cita con [kat] por la mañana."
    stop music fadeout (1.5)
    "Después de hacerle pagar lo de las belugas, parece que estáis en igualdad de condiciones."
    return
label c26s006_KatBreakfast:
    if _in_replay:
        "Atención: Hay dos diálogos 'escondidos' en esta escena:"
        "Uno sucederá si has abierto todas las relaciones de la familia original menos la de [emm]."
        "El otro si has abierto la ruta con [emm] y estás en más de una relación."
        "El diálogo de [kim] también cambiará dependiendo si estás en una relación con todas las chicas, con todas las chicas que viven en casa, o con todas las estudiantes."
        $ mc._var("relationships" , 0, "set")
        menu:
            "¿Has abierto todas las relaciones posibles?"
            "Sí.":
                $ sai._var("route" , True)
                $ mar._var("route" , True)
                $ emm._var("route" , True)
                $ eri._var("route" , True)
                $ nor._var("route" , True)
                $ dap._var("route" , True)
                $ sca._var("route" , True)
                $ eil._var("route" , True)
                $ sam._var("route" , True)
                $ sim._var("route" , True)
                $ ama._var("route" , True)
                $ oma._var("route" , True)
                $ eva._var("route" , True)
                $ mad._var("route" , True)
                $ meg._var("route" , True)
                $ mee._var("route" , True)
                $ kim._var("route" , True)
                $ deb._var("route" , True)
                $ lis._var("route" , True)
                $ bet._var("route" , True)
                $ kia._var("route" , True)
                $ mc._var("relationships" , 21, "set")
            "No.":
                $ sai._var("route" , False)
                $ mar._var("route" , False)
                $ emm._var("route" , False)
                $ eri._var("route" , False)
                $ nor._var("route" , False)
                $ dap._var("route" , False)
                $ sca._var("route" , False)
                $ eil._var("route" , False)
                $ sam._var("route" , False)
                $ sim._var("route" , False)
                $ ama._var("route" , False)
                $ oma._var("route" , False)
                $ eva._var("route" , False)
                $ mad._var("route" , False)
                $ meg._var("route" , False)
                $ mee._var("route" , False)
                $ kim._var("route" , False)
                $ deb._var("route" , False)
                $ lis._var("route" , False)
                $ bet._var("route" , False)
                $ kia._var("route" , False)
                menu:
                    "¿Has abierto todas las relaciones con [sai], [mar], [emm], [eri], [nor], [dap], [sca], [eil], [mee], [kim], [deb.nick], [lis], [bet], y [kia]?"
                    "Sí.":
                        $ sai._var("route" , True)
                        $ mar._var("route" , True)
                        $ emm._var("route" , True)
                        $ eri._var("route" , True)
                        $ nor._var("route" , True)
                        $ dap._var("route" , True)
                        $ sca._var("route" , True)
                        $ eil._var("route" , True)
                        $ mee._var("route" , True)
                        $ kim._var("route" , True)
                        $ deb._var("route" , True)
                        $ lis._var("route" , True)
                        $ bet._var("route" , True)
                        $ kia._var("route" , True)
                        $ mc._var("relationships" , 14, "set")
                    "No.":
                        menu:
                            "¿Has abierto todas las relaciones con [mar], [eri], [nor], [dap], [mee], y [bet], PERO NO con [emm]?"
                            "Sí.":
                                $ mar._var("route" , True)
                                $ eri._var("route" , True)
                                $ nor._var("route" , True)
                                $ dap._var("route" , True)
                                $ mee._var("route" , True)
                                $ bet._var("route" , True)
                                $ mc._var("relationships" , 6, "add")
                            "No.":
                                pass
                        menu:
                            "¿Has abierto todas las relaciones con [sai], [kim], [deb.nick], y [lis]?"
                            "Sí.":
                                $ sai._var("route" , True)
                                $ kim._var("route" , True)
                                $ deb._var("route" , True)
                                $ lis._var("route" , True)
                                $ mc._var("relationships" , 4, "add")
                            "No.":
                                pass
        if not kim._var("route"):
            call mrS3_kim_route from _call_mrS3_kim_route_3
        if mc._var("relationships")<2:
            call mrS3_rels from _call_mrS3_rels_16
        call mrS3_kat_slim from _call_mrS3_kat_slim_1
        call mrS3_kat_rps (-10, 0, 10) from _call_mrS3_kat_rps_1
        if not persistent.lesbian:
            call mrS3_kat_lesbian from _call_mrS3_kat_lesbian_1
    scene black with dissolve
    centered "{size=+20}{b}DÍA 29 – MARTES{/b}{/size}"
    scene c26s006_005b with dissolve
    play music ("music/heavy-rain.ogg")
    "Te despierta el sonido de lluvia en el tejado un rato antes de que suene la alarma. Es una de las pocas cosas que siempre has odiado de esta habitación."
    "Supones que las chicas no harán yoga en la piscina, con lo que se suspenderá la no-cita con [kat]."
    "Para tu sorpresa, estás un poco más decepcionado por la cancelación del desayuno que por la del yoga."
    "Ahora que le devuelves los golpes a [kat], se está volviendo más divertido pasar rato con ella."
    stop music fadeout (1.5)
    "Te vistes y decides bajar a tomar un café."
    call BlinkXPS3 ("c26s006_010" , "f") from _call_BlinkXPS3_2708
    play music ("music/RhythmPlay.ogg")
    eri "Hola, [mc]."
    mc "Buenos días, [eri]."
    eri "¿Dónde vas?"
    mc "A la cocina, a tomar un café."
    call BlinkXS3 ("c26s006_015") from _call_BlinkXS3_204
    eri "Será mejor que no entres ahí. Ahora mismo es territorio prohibido para ti."
    mc "¿Por qué?"
    call BlinkXS3 ("c26s006_020") from _call_BlinkXS3_205
    eri "¿Lo has olvidado? ¡Tienes un desayuno programado con [kat]!"
    mc "No lo he olvidado, pero iba a ser un desayuno mientras comentábamos vuestras posturas de yoga."
    mc "Está lloviendo y dudo que hagáis yoga, ¿no?"
    call BlinkXS3 ("c26s006_025") from _call_BlinkXS3_206
    eri "No vamos a hacer yoga, pero tú vas a desayunar con [kat]."
    eri "Ha empezado a llover hace 10 minutos, y ella ya estaba preparando el desayuno con Tía [mar]."
    mc "Y tú estás aquí para evitar que yo entre en la cocina, ¿verdad?"
    call BlinkXS3 ("c26s006_030") from _call_BlinkXS3_207
    eri "*Risa* No, estoy aquí para mandarte de vuelta a tu habitación por si se te ocurría bajar antes de tiempo."
    mc "*Risa* Entonces me quedo sin café."
    call BlinkXS3 ("c26s006_035") from _call_BlinkXS3_208
    eri "Ahora te subimos un café a tu habitación. Y cámbiate de ropa. Esos shorts no son adecuados para una cita."
    mc "*Risa* No es una cita." (multiple=2)
    kat "*Desde la cocina* ¡Joder! ¡No es una cita!" (multiple=2)
    mc "OK. Espero ese café. ¿Pero me cambio de ropa o no?"
    call BlinkXS3 ("c26s006_040") from _call_BlinkXS3_209
    eri "Cámbiate."
    mom "*Desde la cocina* Si vas con shorts cámbiate."
    kat "*Desde la cocina* Da lo mismo cómo vaya. NO ES UNA PUTA CITA."
    mom "*Desde la cocina* Ese lenguaje, señorita. En mi cocina no se dicen tacos."
    call BlinkXPS3 ("c26s006_045" , "f") from _call_BlinkXPS3_2709
    "Al cabo de un rato, en tu habitación..."
    emm "Te traigo el café que has pedido."
    mc "Gracias, pero creía que me lo iba a traer [eri]..."
    call BlinkXS3 ("c26s006_050") from _call_BlinkXS3_210
    emm "*Risa* Ella sigue vigilando la puerta de la cocina. Por si te habías escondido en la planta de las estudiantes."
    mc "*Risa* ¿Para qué iba a hacer eso? Solo quería un café..."
    call BlinkXS3 ("c26s006_055a") from _call_BlinkXS3_211
    emm "¿No tienes curiosidad por saber qué están preparando en la cocina? Me sorprendes, [mc]."
    if kat._var("slim"):
        mc "Supongo que lo de siempre, pero [kat] está colaborando en prepararlo."
    else:
        mc "Supongo que lo de siempre, pero [kat] está colaborando en prepararlo en vez de comiendo."
    scene c26s006_055d with dissolve
    emm "No sabes nada, [mc] Marks."
    scene c26s006_005a with dissolve
    play sound ("music/Portazo.ogg")
    "*Blam*"
    emm "*A través de la puerta* Me voy a quedar aquí mirando el gimnasio. No se te ocurra salir hasta que te avisemos."
    "Parece que [kat] ha enrolado en vuestra no-cita a la mitad de la familia."
    "Te quedas solo en tu habitación con tu solitario café."
    "Ahora tienes curiosidad por saber qué están preparando para desayunar."
    if mar._var("route") and not emm._var("route") and eri._var("route") and nor._var("route") and dap._var("route") and mee._var("route") and bet._var("route"):
        call BlinkXPS3 ("c26s006_055b" , "f") from _call_BlinkXPS3_2710
        emm "Por cierto... No he tenido la oportunidad de decírtelo, pero te odio. *Risa*"
        mc "¿Qué? ¿Por qué?"
        emm "Desde ayer sales con toda la familia original menos conmigo. *Risa*"
        mc "[emm]..."
        call BlinkXS3 ("c26s006_055c") from _call_BlinkXS3_212
        emm "No te preocupes, no te lo tengo en cuenta. No hubiera funcionado nunca. *Risa*"
        emm "Tienes un gusto horrible para elegir colores. Seguro que me comprabas algún vestido negro."
    elif emm._var("route") and mc._var("relationships")>1:
        call BlinkXPS3 ("c26s006_055b" , "f") from _call_BlinkXPS3_2711
        emm "Por cierto... Es una lástima que Monterey esté tan lejos. *Risa*"
        mc "¿Por qué? ¿Quieres alquilar otra vez el coche?"
        emm "No, pero no sé si te acuerdas de Amber, la chica de la agencia de coches. Nos intercambiamos los teléfonos y hemos estado chateando."
        call BlinkXS3 ("c26s006_055c") from _call_BlinkXS3_213
        emm "Es super simpática y creo que sería un buen añadido para el harén."
        emm "Es guapísima y tiene un gusto exquisito para los colores. Nunca vienen mal otras chicas que adoren el rosa."
        mc "*Risa* ¿Estás segura de que quieres buscarme más novias? Eso significaría menos tiempo para ti..."
        emm "*Risa* Ni de coña. Cambio mi frase inicial a 'Es una suerte que Monterey esté tan lejos'."
    scene c26s006_005a with hpunch
    play sound ("music/Portazo.ogg")
    "*Blam*"
    scene c26s006_005a with fade
    "Al cabo de un rato que se hace muy largo, unos minutos antes de las 7:30..."
    kim "*A través de la puerta* Ya puedes salir. El desayuno está preparado."
    call BlinkXPS3 ("c26s006_060" , "f") from _call_BlinkXPS3_2712
    mc "¿[kim]? ¿Dónde está [emm]? Creía que ella era mi carcelera."
    kim "Ha ido a ayudar a bajar las cosas. No quieres que yo baje una bandeja por las escaleras, ¿verdad?"
    kim "*Risa* Seguramente acabaríais desayunando recogiendo la comida directamente de los escalones. Y yo acabaría con un tobillo roto."
    mc "*Risa* Entonces es mejor que actúes de Guardiana del Calabozo."
    mc "¿Dónde es el desayuno?"
    call BlinkXS3 ("c26s006_065") from _call_BlinkXS3_214
    kim "Abajo, en la piscina. En el porche."
    mc "¡Pero está lloviendo!"
    kim "Ahora sólo caen unas gotas. No os vais a mojar."
    mc "¿Cómo os ha enredado a todas en este desayuno?"
    call BlinkXS3 ("c26s006_070") from _call_BlinkXS3_215
    kim "No lo ha hecho. Nos hemos prestado voluntarias para ayudar."
    if mar._var("route") and sai._var("route") and emm._var("route") and eri._var("route") and nor._var("route") and dap._var("route") and sca._var("route") and eil._var("route") and sam._var("route") and sim._var("route") and oma._var("route") and eva._var("route") and mad._var("route") and meg._var("route") and ama._var("route") and mee._var("route") and kim._var("route") and deb._var("route") and lis._var("route") and bet._var("route") and kia._var("route"):
        kim "Después de que [mee] hiciera público que estáis juntos, [kat] es la única de las chicas de la familia que no se ha unido al harén..."
        kim "No sería un harén completo si no está ella."
    elif mar._var("route") and sai._var("route") and emm._var("route") and eri._var("route") and nor._var("route") and dap._var("route") and sca._var("route") and eil._var("route") and mee._var("route") and kim._var("route") and deb._var("route") and lis._var("route") and bet._var("route") and kia._var("route"):
        kim "Después de que [mee] hiciera público que estáis juntos, [kat] es la única de las chicas que vivimos en casa que no se ha unido al harén..."
        kim "No sería un harén casero completo si no está ella."
    elif sai._var("route") and kim._var("route") and deb._var("route") and lis._var("route"):
        kim "Después de que tú y yo... empezáramos a salir en el barco... [kat] es la única de las estudiantes que no se ha unido al harén..."
        kim "No sería un harén estudiantil completo si no está ella."
    elif mc._var("relationships")>1:
        kim "[kat] nunca ha tenido la oportunidad de unirse a tu harén..."
    else:
        kim "[kat] está muy ilusionada con este desayuno no-cita..."
    mc "*Risa* No sé si os habéis dado cuenta, pero [kat] es lesbiana..."
    call BlinkXS3 ("c26s006_075") from _call_BlinkXS3_216
    kim "Como diría [emm], no sabes nada, [mc] Marks."
    if kim._var("route"):
        if persistent.lesbian or kat._var ("lesbianContent"):
            kim "Y no sé si te has dado cuenta, pero yo la besé en la playa."
            mc "¿Crees que deberíamos hablar de eso? ¿Quieres que...?"
            kim "Quizás otro día. Ahora tienes un desayuno pendiente."
    kim "Sígueme."
    call BlinkXPS3 ("c26s006_080" , "f") from _call_BlinkXPS3_2713
    kim "Y aquí estamos. Ha dejado de llover, pero ya es tarde para empezar a hacer yoga."
    mc "¿Dónde está [kat]?"
    kim "Acabándose de cambiar. No creo que quisiera venir a la cita manchada de harina."
    call BlinkXS3 ("c26s006_085") from _call_BlinkXS3_217
    kat "¡JODER! ¡NO ES UNA PUTA CITA!"
    "Las 7:30 en punto."
    if persistent.family:
        mc "*Risa* Ese lenguaje, señorita. En la piscina de mi madre no se dicen tacos. Se pueden enseñar las tetas, pero no decir tacos."
    else:
        mc "*Risa* Ese lenguaje, señorita. En la piscina de [mar] no se dicen tacos. Se pueden enseñar las tetas, pero no decir tacos."
    call BlinkXS3 ("c26s006_090") from _call_BlinkXS3_218
    kim "Os dejo solos. Disfrutad de vuestra cit... de vuestro desayuno. *Risa*"
    kat "*Grrrr*"
    stop music fadeout (1.5)
    mc "Gracias, [kim]."
    call BlinkXS3 ("c26s006_095") from _call_BlinkXS3_219
    play music ("music/romantic-day.ogg")
    kat "¿Desayunamos antes de que se enfríe?"
    mc "Estás muy guapa, [kat]."
    call BlinkXS3 ("c26s006_100") from _call_BlinkXS3_220
    kat "¡No empieces con eso! No vas a conseguir ruborizarme."
    mc "*Risa* Pues es una lástima. Estás más guapa todavía cuando te ruborizas."
    call BlinkXPS3 ("c26s006_105" , "h") from _call_BlinkXPS3_2714
    kat "¡Ya está! ¡Ya lo has conseguido! ¿Contento?"
    mc "*Risa* Sí."
    call BlinkXS3 ("c26s006_110") from _call_BlinkXS3_221
    kat "Pero gracias..."
    call BlinkXS3 ("c26s006_115") from _call_BlinkXS3_222
    kat "Mira a ver si te gusta lo que hemos preparado para desayunar..."
    scene c26s006_115d with dissolve
    kat "Tu bandeja es la de los huevos fritos."
    mc "¡[kat]! ¡Has hecho que [mar] haga demasiada comida!"
    call BlinkXS3 ("c26s006_120") from _call_BlinkXS3_223
    kat "¿[mar]? ¡Ella ha hecho los croissants! ¡El resto lo he hecho yo!"
    kat "No quería darle más trabajo del que tiene habitualmente porque tú y yo tengamos una... {i}(¡No digas cita, no digas cita!){/i} reunión para desayunar."
    kat "{i}(¡Ufff!){/i}"
    call BlinkXS3 ("c26s006_125") from _call_BlinkXS3_224
    kat "Aunque me ha ayudado con la masa de los gofres... Y diciéndome qué te gusta desayunar."
    mc "Pues te has lucido. ¡Es un desayuno impresionante!"
    scene c26s006_125d with dissolve
    mc "¿Nos sentamos?"
    call BlinkXS3 ("c26s006_130") from _call_BlinkXS3_225
    kat "Hemos quedado en que no es una cita, [mc]. No hace falta que me apartes la silla."
    mc "Es lo menos que puedo hacer viendo el trabajo que te has tomado."
    mc "Puedes sentarte o nos podemos quedar aquí de pie. No pienso soltar la silla."
    scene c26s006_135An with dissolve
    kat "Gracias..."
    mc "Gracias a ti por este desayuno fantástico."
    mc "Aunque te tengo que informar de que no estaré aquí para Acción de Gracias. Estaré en Aruba."
    call BlinkXS3 ("c26s006_140") from _call_BlinkXS3_226
    kat "Lo sé, pero no entiendo a qué te refieres."
    mc "No hace falta que me cebes como a un pavo. *Risa*"
    call BlinkXS3 ("c26s006_145") from _call_BlinkXS3_227
    kat "*Risa* ¿He hecho demasiada comida?"
    mc "A menos que se nos vayan a unir un par de personas más, sí."
    mc "Has hecho demasiada comida para mí y veo poca para ti."
    call BlinkXS3 ("c26s006_150") from _call_BlinkXS3_228
    kat "Me he levantado sin hambre... {i}(Jodidos nervios){/i} [mar] me ha convencido de que me pusiera más comida de la que me iba a poner." id c26s006_KatBreakfast_3aeb0d7b
    if kat._var("slim"):
        kat "Además, me convencisteis para que comiera más sano. Fruta, huevo duro... Aún no me he acostumbrado del todo."
    call BlinkXS3 ("c26s006_155") from _call_BlinkXS3_229
    kat "Aunque miro a tus gofres y me dan ganas de robártelos. *Risa*"
    mc "Podemos compartirlos. Yo no me voy a acabar toda esta comida."
    kat "Mejor no. *Risa* No sé si podría parar si empiezo a robarte comida ¿Empezamos antes de que se enfríe?"
    mc "Empecemos."
    call BlinkXS3 ("c26s006_160") from _call_BlinkXS3_230
    mc "El bacon está en su punto. Felicidades."
    kat "Gracias. [mar] me ha dicho el punto en el que te gusta."
    mc "¿Te han hecho muchas bromas sobre la no-cita?"
    call BlinkXS3 ("c26s006_165") from _call_BlinkXS3_231
    kat "*Risa* Llevan dos días con las bromas. Les comenté {b}que me había equivocado de palabra{/b} delante de [meg]."
    kat "Esa chica es un hueso duro de roer y tiene una mente rápida para las bromas."
    mc "Lo sé. Creo que es la única que ha conseguido dejar callado a Jamaal."
    call BlinkXS3 ("c26s006_170") from _call_BlinkXS3_232
    kat "Jamaal también es rápido, pero [meg] lo es más."
    kat "A partir de que ella hizo la primera broma, el resto no han parado. Se han puesto un poco pesadas."
    mc "Y eso que ellas no te tenían que devolver la broma de las belugas..."
    call BlinkXS3 ("c26s006_175") from _call_BlinkXS3_233
    kat "*Risa* Bueno, creo que la mayoría de ellas tenía alguna broma guardada que devolverme..."
    kat "Pero se han aliado las 21 contra mí. *Risa* Ni siquiera yo puedo contra eso. ¡Incluso la siempre seria [ama] me hizo una broma!" id c26s006_KatBreakfast_e9c2fb56
    mc "Da gusto ver lo bien que os lleváis. Incluso con [lis]. No lo hubiera pensado el día que llegasteis."
    call BlinkXS3 ("c26s006_180") from _call_BlinkXS3_234
    kat "Las dos teníamos un concepto equivocado de la otra. Nunca nos hubiéramos hecho amigas en un dormitorio normal."
    kat "Ya sabes, la reina del gallinero y esas cosas. [lis] hubiera luchado por la posición y yo la hubiera intentado sabotear."
    kat "Aquí es diferente. Las reinas del gallinero son [mar] y [nor], con lo que [lis] y yo no tenemos conflictos."
    mc "Anoche parecíais casi amigas."
    call BlinkXS3 ("c26s006_185") from _call_BlinkXS3_235
    kat "El 'casi' es la parte importante de esa frase. Nos llevamos bien, pero no creo que ninguna elija a la otra como la madrina de sus hijos."
    mc "Ser amigas no significa ser las mejores amigas, [kat]."
    mc "Yo tenía amigos en Portland, pero el padrino de mis hijos será Jamaal. Solo puede haber un padrino, pero muchos amigos."
    call BlinkXS3 ("c26s006_190") from _call_BlinkXS3_236
    kat "Visto así... Creo que tienes razón. Posiblemente seamos amigas ahora."
    kat "Aunque en nuestras respectivas listas la otra esté en el puesto 21, si solo contamos a las chicas de la familia, claro."
    mc "Es un paso muy importante. Hace tres semanas no hubierais estado en la lista de la otra."
    call BlinkXS3 ("c26s006_195") from _call_BlinkXS3_237
    kat "Pero sólo estamos hablando de mí..."
    mc "*Risa* No estamos hablando de ti. Estás hablando de las otras chicas y cómo te llevas con ellas."
    mc "En cinco minutos has nombrado a [meg], [mar], [nor], [ama], y [lis]. Incluso a Jamaal."
    call BlinkXS3 ("c26s006_200") from _call_BlinkXS3_238
    kat "*Risa* ¡A Jamaal lo has metido tú en la conversación, no yo! Yo sólo he respondido."
    mc "*Risa* Bueno, no recuerdo exactamente cómo ha sido. Pero lo importante es que no estás hablando de ti."
    call BlinkXS3 ("c26s006_205") from _call_BlinkXS3_239
    kat "Pero habíamos quedado para desayunar y hablar de las chicas mientras hacían yoga. No para hablar de mí."
    mc "Pero cómo no hay chicas haciendo yoga, los planes pueden cambiar."
    mc "Cuéntame algo sobre ti."
    call BlinkXS3 ("c26s006_210") from _call_BlinkXS3_240
    kat "*Risa* ¿Entrevista estándar? Soy de Pittsburgh y tengo dos hermanos. Kevin es actor, o lo intenta, y vive en Los Angeles."
    kat "Randall es agente de comercio y vive en 'Burgh. Mi madre sigue viva, Randall vive con ella, pero mi padre murió en un incendio."
    mc "[kat], te cuesta hablar de ti, ¿verdad? Antes, en vez de hablar de ti hablabas de las chicas. Ahora hablas de tu familia."
    call BlinkXS3 ("c26s006_215") from _call_BlinkXS3_241
    kat "Es que no sé qué puede interesarte sobre mí. Lo más interesante que me había pasado antes de llegar aquí ya te lo conté."
    kat "Y no fue agradable. No me refiero a contártelo, sino a vivirlo. Ya sabes, el chico aquel..."
    mc "Estoy seguro de que tienes mil cosas interesantes que contar. ¿Por qué estudias Oceanografía?"
    mc "Y no me digas que es porque consideras a las ballenas y a las focas tus primas."
    call BlinkXS3 ("c26s006_220") from _call_BlinkXS3_242
    kat "*Risa* ¡Esa ha sido buena! ¡Serías buena competencia para...! Vale, no voy a nombrar a la cantante otra vez."
    if kat._var("slim"):
        kat "Pero ya he perdido ocho libras desde que empecé a comer más sano, con lo que mis primas me van a echar de la familia. *Risa*"
    call BlinkXS3 ("c26s006_190") from _call_BlinkXS3_243
    kat "Me gusta el mar. Tengo un buen recuerdo de cuando fuimos con mis padres un par de años antes de que mi padre muriera."
    kat "Como no me apetecía trabajar en una plataforma petrolífera ni ser pescadora, decidí estudiar oceanografía."
    mc "¿Ves cómo hay historias interesantes?"
    call BlinkXS3 ("c26s006_225") from _call_BlinkXS3_244
    kat "¿Y tú? ¿Por qué estudiaste Administración de Empresas?"
    mc "*Risa* Lo mío es mucho menos emotivo. Quería ganar mucho dinero y no tener un trabajo físico. Administración de Empresas cumplía los requisitos."
    call BlinkXS3 ("c26s006_230") from _call_BlinkXS3_245
    kat "Una buena razón. Y justo cuando acabas la carrera heredas una empresa millonaria y tienes más dinero del que podrás gastar en tu vida."
    mc "Pero alguien tiene que administrar esa empresa. *Risa* Al final haré lo que quería hacer, pero trabajando para mí, para la empresa familiar."
    mc "En el fondo es lo que elegí hacer cuando vine aquí. Tenía ofertas de trabajo, pero trabajar con [mar] y [nor] me apetecía más."
    mc "Podrías decir que soy un tipo familiar."
    call BlinkXS3 ("c26s006_235") from _call_BlinkXS3_246
    kat "¿No te da miedo? Yo estaría histérica. Ir a un país nuevo, a una empresa que no conozco, donde la mayoría de la gente son asesinos entrenados..."
    kat "A una empresa donde ha habido facciones literalmente matándose entre ellos. Estaría cruzando los dedos para que nadie decidiera asesinarme."
    mc "Bueno, [ama] y [eva] van a estar conmigo allí. Además, el tema de las facciones está más o menos resuelto."
    mc " Y Aaron, uno de los primeros clones, me está enviando muchísima información. No voy a ir a ciegas ni a estar en riesgo. Es un reto nuevo, pero no uno que me asuste."
    mc "*Risa* Aunque conociendo a [eva] y a [ama], seguro que me hacen hacer mucho trabajo físico."
    mc "Y otra vez has desviado la atención de ti."
    call BlinkXS3 ("c26s006_240") from _call_BlinkXS3_247
    kat "Es posible que a ti te interese que yo hable de mí, pero a mí me interesa que tú hables de ti. *Risa* Tenemos un conflicto de intereses."
    mc "Tenemos suerte de que esto no sea una primera cita. *Risa* Sería una conversación rarísima en la que ninguno querría hablar de sí mismo."
    kat "*Risa* ¡Tienes razón! Hablaríamos del menú, del camarero, del tiempo... pero no hablaríamos de nosotros."
    mc "Bueno, creo que de nosotros, sí que hablaríamos. No cada uno de sí mismo, sino de nosotros como pareja."
    call BlinkXS3 ("c26s006_245") from _call_BlinkXS3_248
    kat "No te entiendo."
    mc "Tú querrías saber si quiero tener hijos, por ejemplo. Pero querrías saberlo para saber si mi respuesta es la misma que darías tú si te lo preguntara yo."
    mc "No serían preguntas al azar, sino que serían preguntas para saber si lo nuestro puede funcionar."
    call BlinkXS3 ("c26s006_250") from _call_BlinkXS3_249
    kat "*Risa* Creo que has tenido más primeras citas que yo. No creo que haya tenido una primera cita al uso, de esas que sirven para conocerse."
    kat "Cuando tenía una cita, solía ser con chicas con las que ya había tenido algo..."
    mc "Bueno, pero estamos empatados en no-citas, ¿no? Esta es mi primera no-cita."
    kat "*Risa* ¿Vas a volver con ese tema?"
    mc "Tengo que intentar que te ruborices de nuevo. Estás monísima cuando lo haces."
    call BlinkXS3 ("c26s006_255") from _call_BlinkXS3_250
    kat "*Risita* Pues creo que lo acabas de conseguir. ¡Odio ruborizarme! ¡Parezco un personaje de anime!"
    mc "Nota mental: Decirle que está monísima la ruboriza."
    call BlinkXS3 ("c26s006_260") from _call_BlinkXS3_251
    kat "*Risa* ¡[mc]! ¡Para o tendré que robarte gofres!"
    mc "¿Qué tienen que ver los gofres en esto?"
    call BlinkXS3 ("c26s006_265") from _call_BlinkXS3_252
    kat "Cuando me pongo nerviosa, como. Cuanto más dulce mejor. O no como nada de nada." id c26s006_KatBreakfast_c03d0f62
    kat "Y algo como ruborizarme, sobre lo que no tengo ningún control, me pone nerviosa."
    mc "Vale, entonces dejaré de hacerlo. Al menos por hoy."
    call BlinkXS3 ("c26s006_270") from _call_BlinkXS3_253
    kat "Gracias. Eres todo un caballero."
    mc "Tendré que esperar a que no haya comida cerca para decirte que estás monísima. *Risa*"
    call BlinkXS3 ("c26s006_260") from _call_BlinkXS3_254
    kat "¡Eres un capullo! *Risa* ¡Retiro lo de caballero!"
    mc "Sólo bromeaba. Pese a que ahora tengo el contraataque perfecto para tus bromas, intentaré no usarlo demasiado."
    call BlinkXS3 ("c26s006_275") from _call_BlinkXS3_255
    kat "¿Por si me vuelvo inmune? ¡Visto lo visto, no creo que pase!"
    mc "No, [kat]. Porque parece incomodarte y ponerte nerviosa."
    mc "Si vamos a tener más no-citas para desayunar, no quiero que tengas miedo de sentirte incómoda."
    call BlinkXS3 ("c26s006_280") from _call_BlinkXS3_256
    kat "¡Por Dios, [mc]! ¿Puedes dejar de hacerme ruborizar de una puta vez?"
    mc "¿Qué he hecho ahora? Precisamente he dicho que no quiero que te sientas incómoda..."
    kat "¡Precisamente eso! ¿Por qué tienes que preocuparte por mí?"
    if persistent.walkthrough:
        if kat._var("slim"):
            $ wt1 = _("[gr][kat] + 15.\nNo afectará a su dieta.\nÚltima oportunidad de ganar puntos con [kat].")
        else:
            $ wt1 = _("[gr][kat] + 15.\nÚltima oportunidad de ganar puntos con [kat].")
        $ wt2 = "Sin consecuencias."
    else:
        $ wt1 = ""
        $ wt2 = ""
    menu:
        "Darle un trozo de gofre." (wt=wt1):
            $ kat.rp (30)
            $ kat._var("waffle" , True)
            scene c26s006_285An with dissolve
            mc "Toma un poco de gofre."
            scene c26s006_285d with dissolve
            kat "Mmmmm... ¡Me han quedado buenísimos!"
            mc "¿Estás mejor?"
            call BlinkXS3 ("c26s006_290") from _call_BlinkXS3_257
            kat "Sí. Perdona por lo de..."
            mc "¿Lo de... qué?"
            call BlinkXS3 ("c26s006_295") from _call_BlinkXS3_258
            mc "¿Qué pasa, [kat]?"
            call BlinkXPS3 ("c26s006_295" , "h") from _call_BlinkXPS3_2715
            kat "¿Me acabas de dar de comer en la boca?"
            stop music fadeout (1.5)
            mc "Sí... creía que necesitabas un trozo de gofre. Te estabas poniendo un poco... irracional..."
            call BlinkXS3 ("c26s006_300") from _call_BlinkXS3_259
            play music ("music/pianomatic.ogg")
            kat "¡Joder, [mc]! ¡No soy tu novia! ¡No puedes hacer esas cosas!"
            mc "Perdona... no quería que pareciera algo así..."
        "No hacerlo." (wt=wt2):
            $ kat._var("waffle" , False)
            mc "Porque me caes bien, [kat]. Y quiero que estés relajada cuando estés conmigo, no que estés nerviosa esperando cuándo voy a hacer que te ruborices."
            stop music fadeout (1.5)
            mc "Si vas a estar incómoda, pese a que no me guste, deberíamos dejar de tener estas no-citas."
            play music ("music/pianomatic.ogg")
            call BlinkXPS3 ("c26s006_295" , "h") from _call_BlinkXPS3_2716
            kat "¡Joder! ¡No sé por qué coño dije cita!"
    $ resetWalkthrough()
    scene c26s006_305An with dissolve
    kat "¡Hemos dicho que esto no era una puta cita!"
    kat "¡No tienes por qué comportarte como si fueras mi puto novio ni preocuparte por mí!"
    mc "¡[kat]!"
    "Desaparece tras la esquina."
    "Si algo te ha enseñado crecer rodeado de mujeres es que no es el momento de seguirla."
    "Cuando se le pase el disgusto que no entiendes qué has hecho para provocar, ya habrá tiempo de hablar."
    mcp "(Quizás he ido demasiado lejos con lo de ruborizarla. Soy idiota. A veces no sé cuándo parar con una broma.)"
    scene black with dissolve
    "Recoges los restos del desayuno y los subes a la cocina."
    "De alguna forma, el resto de las chicas con las que te cruzas saben que algo ha salido mal."
    "Ninguna te pregunta por la no-cita."
    "Supones que han visto a [kat] subir a su habitación con cara de pocos amigos."
    "Vas a tu habitación y pasas una par de horas leyendo unos correos de Aaron sobre la empresa."
    if kat.rps>4:
        scene c26s006_310a with fade
        "Mientras recoges el desayuno, en la cocina de [nor]..."
        scene c26s006_310An with dissolve
        nor "¿Qué pasa, [kat]?"
        nor "¿Ha ido mal la cita?"
        kat "*Sollozo* ¡No era una puta cita!"
        nor "¿Entonces dime qué te pasa? Pareces molesta. ¿Qué ha ido mal?"
        call BlinkXS3 ("c26s006_315") from _call_BlinkXS3_260
        kat "¿Por qué me tiene que tratar como si fuera una chica normal?"
        kat "Creo que me estoy enamorando..."
    stop music fadeout (1.5)
    return
label c26s007_Bet:
    if _in_replay:
        call mrS3_bet_route from _call_mrS3_bet_route_3
    scene c26s006_005a with fade
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    "Tu lectura de la documentación de NTR se ve interrumpida por unos golpes en la puerta."
    "Lo agradeces. Parece que, mires donde mires, hay un exceso de NTR en el mundo."
    play music ("music/Inspire.ogg")
    bet "*A través de la puerta* Soy yo, ¿puedo pasar?"
    mc "Adelante."
    call BlinkXPS3 ("c26s007_005" , "f") from _call_BlinkXPS3_2717
    bet "¡[mc]! ¡Ya no soy monja! ¡Oficialmente! Acabo de recibir un correo electrónico del Obispado. Y también la transferencia bancaria."
    mc "¡Eso son grandes noticias! ¡Dame un abrazo!"
    call BlinkXS3 ("c26s007_010") from _call_BlinkXS3_261
    bet "Gracias, [mc]. No lo hubiera conseguido sin ti. O al menos, no lo hubiera conseguido en estas condiciones."
    mc "La decisión fue tuya. Yo solo negocié el dinero. Y eso es mucho menos importante que sentirte libre."
    call BlinkXS3 ("c26s007_015") from _call_BlinkXS3_262
    bet "Nos va a venir muy bien. [eri] me ha hecho una propuesta..."
    mc "Lo sé, me lo ha explicado. ¿Qué le ha parecido a Meemaw?"
    call BlinkXS3 ("c26s007_020") from _call_BlinkXS3_263
    bet "Aún no se lo he dicho. Aprovecharé el viaje de mañana para comentárselo. Creo que, si es posible, le parecerá bien."
    mc "¿Viaje? ¿Mañana?"
    call BlinkXS3 ("c26s007_025") from _call_BlinkXS3_264
    bet "¿No te acuerdas? Vamos a Florida, a poner la casa en venta."
    mc "No sabía que era mañana. Creía que iba a ir Meemaw una vez yo estuviera en Aruba."
    bet "Ese era el plan inicial, pero lo hemos adelantado y yo voy a acompañarla para ayudarle a empaquetar las cosas."
    mc "¿Cuánto tiempo vais a estar allí? ¿Os veré antes de irme a Aruba?"
    call BlinkXS3 ("c26s007_030") from _call_BlinkXS3_265
    bet "No lo sabemos, pero no te preocupes, si no hemos acabado para cuando te vayas, vendremos aquí a despedirte."
    mc "Te veo ilusionada, entre lo del final de tu relación con la iglesia y lo de la casa, estás exultante."
    call BlinkXS3 ("c26s007_035") from _call_BlinkXS3_266
    bet "No es para menos. Hace menos de una semana mis opciones eran irme a Latinoamérica a un convento o meterme en un convento de clausura."
    bet "Ahora voy a vivir al lado de mi familia para siempre. Si esos terrenos están en venta y se puede construir en ellos, claro."
    mc "Creo que Meemaw es la que más sabe de eso, con lo que es la persona idónea para hacerlo."
    mc "Además, a las estudiantes de casa de [nor] les queda más de un mes para llegar."
    call BlinkXS3 ("c26s007_040") from _call_BlinkXS3_267
    bet "Sí, pero no tengo ni idea de cuánto tiempo tardarán la venta, los permisos de construcción, la construcción en sí misma..."
    bet "Es un mundo del que no sé nada, pero es imposible que todo esté listo antes de que lleguen las chicas nuevas."
    mc "Deberíais alquilar algo durante ese periodo. O usar mi habitación."
    call BlinkXS3 ("c26s007_045") from _call_BlinkXS3_268
    bet "Lo he pensado. [mee] puede dormir con [nor] y yo con [mar]. [kia] y [eil] pueden usar tu habitación mientras tú estés en Aruba..."
    mc "*Risa* Las cuatro podríais dormir en mi habitación si quisierais. Hoy llega la cama nueva. No es anti gatos, pero hay espacio para cuatro personas."
    mc "Y [eri] y [emm] aún tienen sus habitaciones para ellas solas. Si es necesario, podrían compartir una y quedaría una habitación libre."
    call BlinkXS3 ("c26s007_050") from _call_BlinkXS3_269
    bet "Hay muchas opciones, pero ninguna servirá de nada si no convenzo a [mee] o si no se puede construir en esos terrenos."
    mc "Estoy seguro de que lo descubriréis antes de que lleguen las nuevas estudiantes, no te preocupes por ello."
    mc "¿Sabes algo sobre tu recertificación?"
    call BlinkXS3 ("c26s007_055") from _call_BlinkXS3_270
    bet "Lo estuve mirando por internet. No es demasiado complicado y lo podría tener resuelto a finales de septiembre o principios de octubre como muy pronto."
    bet "Una vez recertificada, podría empezar a buscar trabajo. ¡Podría estar trabajando antes de acabar el año!"
    mc "Esa es una noticia increíble. Sé que te hace mucha ilusión volver a trabajar."
    call BlinkXS3 ("c26s007_060") from _call_BlinkXS3_271
    bet "Todo eso si es que apruebo la recertificación, claro. Pero no parece difícil."
    mc "Me alegro. Si lo hubieras visto muy difícil, había pensado en darte trabajo en NTR, si se necesitan médicos allí."
    mc "Incluso había pensado, cuando salimos de la primera reunión en Monterey, en contratarte y que NTR pagara la certificación si no nos daban lo que pedíamos."
    mc "*Risa* ¡No llevo ni un mes como CEO y ya estoy pensando en usar el nepotismo para contratar a mi tía abuela!"
    call BlinkXS3 ("c26s007_065") from _call_BlinkXS3_272
    bet "*Risa* Esa mentalidad corrupta te iría muy bien en algunos sitios en los que he trabajado."
    mc "Creo que para el negocio de NTR una mentalidad que no siga las normas al 100\% puede ser buena, pero intentaré usarla sólo cuando sea necesario." id c26s007_Bet_71756d90
    call BlinkXS3 ("c26s007_070") from _call_BlinkXS3_273
    bet "Por cierto, ¿cuándo llega tu cama? Yo he dormido muchas veces en el suelo, pero no sé si tú estás acostumbrado."
    mc "Llega en una hora o así. Me han llamado para confirmar la entrega hace un rato."
    mc "No he notado nada por dormir en el suelo. El colchón es bueno. Lo voy a echar de menos."
    call BlinkXS3 ("c26s007_075") from _call_BlinkXS3_274
    bet "¿Necesitas ayuda para retirar el colchón o algo?"
    mc "No, gracias. El colchón lo voy a dejar en el gimnasio por ahora. Y el resto se va a quedar como está."
    mc "Seguramente acabe bajándolo al sótano. A lo mejor a [emm] le va bien para el estudio de fotografía."
    mc "Quizás mueva un poco el sofá depende cómo quede la habitación con la cama montada, pero eso lo puedo hacer yo."
    call BlinkXS3 ("c26s007_080") from _call_BlinkXS3_275
    bet "Entonces te voy a dejar y voy a ir a hacer la maleta."
    mc "¿Necesitaréis que os lleve al aeropuerto mañana?"
    call BlinkXS3 ("c26s007_085") from _call_BlinkXS3_276
    bet "No hace falta. [nor] se ha ofrecido a llevarnos. Hace unos días que [mee] y ella se han vuelto casi inseparables."
    mc "Me alegra mucho que haya pasado eso. [nor] estaba muy tensa los días antes de que llegarais."
    call BlinkXS3 ("c26s007_090") from _call_BlinkXS3_277
    bet "*Risa* Yo también lo hubiera estado. [mee] puede ser un poco bruja a veces. Especialmente con [nor]."
    bet "Pero eso parece que forma parte del pasado, al menos hasta que encuentre una nueva víctima."
    if bet._var("route"):
        call KissXS3 ("c26s007_095") from _call_KissXS3_7
    call BlinkXS3 ("c26s007_095") from _call_BlinkXS3_278
    bet "Bueno, me voy ya o, si no, no voy a hacer la maleta nunca."
    stop music fadeout (1.5)
    if bet._var("route"):
        mc "Te veo luego, [bet]."
    else:
        mc "Te veo luego, Tía [bet]."
    return
label c26s007_Bed:
    if _in_replay:
        call mrS3_deb_route from _call_mrS3_deb_route_13
    scene black with dissolve
    play music ("music/SadSummer.ogg")
    if deb._var("route"):
        "El transportista de la cama llega un par de horas antes de tu cita con [deb.nick]. Te asegura que habrá acabado antes de que tengas que ir a buscarla."
    else:
        "El transportista de la cama llega un par de horas antes de la hora de comer. Te asegura que habrá acabado antes de que tengas que la comida esté preparada."
    "Eso es antes de ver las escaleras por las que tendrán que subir la cama."
    "Una vez han subido las cajas con las piezas de la cama y el colchón, empiezan a montarlo todo tras mover los muebles que les molestan."
    "Te quedas en el descansillo, por si los montadores necesitan alguna cosa. Aceptan que les subas una jarra de agua fría."
    call BlinkXS3 ("c26s007_100") from _call_BlinkXS3_279
    "Las mujeres de la casa no tardan en empezar a subir para ver el nuevo mueble."
    mom "Deberías haberla centrado con la cortina. Así queda rara."
    mc "Si la centro con la cortina, quedaría demasiado pegada al sofá y no se podría usar. Tengo que pegar el sofá al escritorio para que siga siendo útil."
    call BlinkXS3 ("c26s007_105") from _call_BlinkXS3_280
    mom "Es una buena razón, pero no me acaba de gustar. No queda simétrica dentro de la habitación."
    mc "¿Crees que importará mucho para los abrazos familiares que no esté simétrica?"
    call BlinkXS3 ("c26s007_110") from _call_BlinkXS3_281
    mom "*Risa* No, no importará. Y creo que ahí cabremos unas cuantas más."
    mc "Tengo que comprar una trampa anti gatos, para evitar que vuelva a romperse."
    call BlinkXS3 ("c26s007_115") from _call_BlinkXS3_282
    mom "Bueno, te voy a dejar con los chicos. Voy a seguir haciendo la comida."
    mc "Perfecto. Puedes pasar a verla acabada después de comer."
    scene c26s007_115d with dissolve
    mom "Lo haré, no te preocupes. Y criticaré tu elección de colores para la ropa de cama. *Risa*"
    call BlinkXPS3 ("c26s007_120" , "f") from _call_BlinkXPS3_2718
    emm "¿He oído que Mamá va a criticar tu elección de colores? ¿Has elegido algo rosa? Mamá tiene mal gusto para los colores, ya lo sabes."
    mc "No, [emm], lo siento. Nada rosa en mi habitación, excepto cuando estás tú."
    call BlinkXS3 ("c26s007_125") from _call_BlinkXS3_283
    emm "Veo que tú has heredado el mal gusto de Mamá. Déjame ver..."
    scene c26s007_125d with dissolve
    pause (1.0)
    call BlinkXS3 ("c26s007_130") from _call_BlinkXS3_284
    emm "¡Es enorme! Cuando acaben de montarla quiero ser la primera en probarla."
    mc "Creo que debería ser yo el primero en probarla, ¿no?"
    call BlinkXS3 ("c26s007_135") from _call_BlinkXS3_285
    emm "Bueno, después de ti, claro. Vamos a caber un montón de chicas ahí."
    emm "Los abrazos familiares van a ser épicos."
    mc "*Risa* Por eso la he comprado tan grande. Si lo instauramos como costumbre vamos a necesitar el espacio."
    call BlinkXS3 ("c26s007_140") from _call_BlinkXS3_286
    emm "¿Me puedo mudar aquí cuando estés en Aruba? Creo que me va a encantar esa cama."
    mc "Tus sábanas serán pequeñas con ese colchón, no tendrás nada rosa en la habitación."
    scene c26s007_140d with dissolve
    emm "Entonces no. Seguramente me levantaría deprimida todas las mañanas."
    emm "Y no solo porque te vuelvas a ir. Ya tuve que pasar por eso cuando te fuiste a Portland."
    call BlinkXPS3 ("c26s007_145" , "f") from _call_BlinkXPS3_2719
    eri "¿Ya está montada?"
    mc "Aún no. Les queda poco."
    scene c26s007_150d with dissolve
    pause (1.0)
    call BlinkXS3 ("c26s007_150") from _call_BlinkXS3_287
    eri "¡Es gigantesca! Si la última cama aguantó a ocho personas, creo que esta puede aguantar a diez o doce."
    mc "*Risa* Y a un gato."
    call BlinkXS3 ("c26s007_155") from _call_BlinkXS3_288
    eri "*Risa* No, con el gato no pudo."
    mc "*Risa* Tienes razón. Si no le hubierais dado tantas latas de atún..."
    call BlinkXS3 ("c26s007_160") from _call_BlinkXS3_289
    eri "No hubieras comprado una cama nueva enorme. Le tienes que dar gracias a Zeus y a su Secta de Alimentadoras. *Risa*"
    mc "¿Ya habéis montado una secta?"
    call BlinkXS3 ("c26s007_165") from _call_BlinkXS3_290
    eri "Es broma, pero no es mala idea. Nombraríamos a [mad.nick] Suma Sacerdotisa y así nadie le dará más comida de la debida al gatito."
    eri "Nadie quiere que coja un empacho y se ponga enfermo."
    mc "¡Estáis todas locas!"
    call BlinkXS3 ("c26s007_170") from _call_BlinkXS3_291
    eri "Por cierto, viendo esa cama, creo que el problema de espacio para la abuela, Tía [bet], [kia] y [eil] cuando lleguen las chicas nuevas podría estar resuelto."
    eri "Podrían dormir todas en tu cama. Aunque [eil] también podría dormir en la mía."
    mc "Bueno, creo que habrá tiempo de hablar de eso. He estado hablando con Tía [bet] antes y..."
    scene c26s007_175d with dissolve
    "Transportista" "Señor, ya está acabada. ¿Quiere pasar a verla y a probarla?"
    "Transportista" "También debería firmar la entrega."
    call BlinkXS3 ("c26s007_175") from _call_BlinkXS3_292
    eri "Te dejo con estos señores. Voy a ver si Tía [mar] necesita ayuda con la comida."
    scene black with dissolve
    "Pruebas la cama y todo parece estar en orden. Firmas la entrega y acompañas a los transportistas a la salida."
    "Vuelves a subir a tu habitación para poner las sábanas y el edredón."
    scene c26s007_175e with dissolve
    stop music fadeout (1.5)
    mcp "(Una cama enorme. Espero que resista unos cuantos abrazos familiares.)"
    return
label c26s008_DebTeaser:
    scene black with dissolve
    play music ("music/Wonder.ogg")
    "Cuando se acerca la hora de ir a buscar a [deb.nick] vas a darte una ducha rápida y a cambiarte."
    "Ya has tenido una no-cita con la ropa que llevas y la cita que vas a tener ahora es demasiado especial como para repetir vestuario."
    mcp "(Parezco [eil] eligiendo el vestido para nuestro baile de promoción.) *Risa mental*"
    mcp "(¿Es tan importante [deb.nick] para mí?)"
    mcp "(Creo que es una de las preguntas más tontas que me he hecho nunca. La respuesta es, obviamente, sí.)"
    scene c26s008_005a with fade
    "Bajas una planta hasta la habitación que [deb.nick] comparte con [lis] y llamas a la puerta."
    play sound ("music/knock.ogg")
    "*Knock-Knock*"
    mc "Soy yo. ¿Puedo pasar?"
    deb "*A través de la puerta* Dame dos minutos. Espérame en los sofás, por favor."
    scene c26s008_005b with fade
    "Te sientas en el sofá y esperas."
    "¿Dos minutos para estar lista? A veces desearías que la sirena no se hubiera feminizado tanto."
    "Seguramente la [deb.nick] que bajó de aquel avión habría cumplido con los dos minutos exactos."
    scene c26s008_005b with fade
    "Cuando ha pasado un minuto, para tu sorpresa, oyes cómo se abre la puerta de las hermanas Selden."
    scene c26s008_005c with dissolve
    pause (1.5)
    scene c26s008_005b with dissolve
    mcp "(¿[kim] ayudando a mi cita con algo? ¿Maquillaje quizás? No es que [deb.nick] lo necesite para estar preciosa, pero...)"
    "Ni siquiera ha mirado en tu dirección. Sigues esperando."
    scene c26s008_005b with fade
    "Cuando han pasado los dos minutos exactos, la puerta vuelve a abrirse."
    scene c26s008_010d with fade:
        yalign 1.0
        linear 5.0 yalign 0.0
    pause (5.0)
    call BlinkXPS3 ("c26s008_010" , "d") from _call_BlinkXPS3_2720
    deb "¿Nos vamos?"
    "Te quedas sin palabras por un momento. No te hubiera importado esperar dos horas en vez de dos minutos."
    call addProfileImageS3 (1, "deborah_01", deb, _(": 15 - Especial"), "") from _call_addProfileImageS3_16
    mc "Cuando quieras. Estás preciosa, [deb.nick]."
    stop music fadeout (1.5)
    return
